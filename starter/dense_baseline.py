"""Benchmark dense retrieval bằng model và pgvector đã có từ Day 6."""

import argparse
import json
import os
import statistics
import time
from pathlib import Path

from baseline import TfidfIndex, evaluate, validate

DAY6 = Path(
    "D:/study/VinAI/projectAI/"
    "K5-L3A-Day06-ChuThiAnh-2A202603360-DataIngestion/starter"
)
MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
REVISION = "e8f8c211226b894fcb81acc59f3b34ba3efd5f42"
COLLECTION = "thinkpython2_e8412522c5d43b8e"
STRATEGY = "B"


class DenseIndex:
    def __init__(self, connection, model):
        self.connection = connection
        self.model = model

    def search(self, question, top_k=3):
        from pgvector import Vector

        tokens = self.model.tokenizer(
            question, truncation=False, add_special_tokens=True
        )["input_ids"]

        if len(tokens) > self.model.max_seq_length:
            raise ValueError("Câu hỏi vượt giới hạn token của model Day 6.")

        embedding = self.model.encode(
            [question],
            normalize_embeddings=True,
            show_progress_bar=False,
            convert_to_numpy=True,
        )[0]
        vector = Vector(embedding)

        rows = self.connection.execute(
            """
            SELECT chunk_id AS id, document_id AS source_id,
                   source, page, text, metadata,
                   1 - (embedding <=> %s) AS score
            FROM day6_chunks
            WHERE collection = %s AND strategy = %s
            ORDER BY embedding <=> %s, chunk_id
            LIMIT %s
            """,
            (vector, COLLECTION, STRATEGY, vector, top_k),
        ).fetchall()

        return [{**row, "strategy": "dense"} for row in rows]


class HybridIndex:
    def __init__(self, dense, lexical, candidates=10, rrf_k=60):
        self.dense = dense
        self.lexical = lexical
        self.candidates = candidates
        self.rrf_k = rrf_k

    def search(self, question, top_k=3):
        rankings = {
            "dense": self.dense.search(question, top_k=self.candidates),
            "tfidf": self.lexical.search(question, top_k=self.candidates),
        }
        merged = {}

        for method, results in rankings.items():
            for rank, chunk in enumerate(results, start=1):
                chunk_id = chunk["id"]

                if chunk_id not in merged:
                    merged[chunk_id] = {
                        **chunk,
                        "strategy": "hybrid",
                        "score": 0.0,
                        "retriever_ranks": {},
                        "retriever_scores": {},
                    }

                item = merged[chunk_id]
                item["score"] += 1.0 / (self.rrf_k + rank)
                item["retriever_ranks"][method] = rank
                item["retriever_scores"][method] = chunk["score"]

        return sorted(
            merged.values(),
            key=lambda chunk: (-chunk["score"], chunk["id"]),
        )[:top_k]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunks", required=True, type=Path)
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--split", required=True, choices=["dev", "test"])
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--method", choices=["dense", "hybrid"], default="dense")
    parser.add_argument("--budget", type=int, default=800)
    args = parser.parse_args()

    chunks = json.loads(args.chunks.read_text(encoding="utf-8"))
    questions = json.loads(args.questions.read_text(encoding="utf-8"))
    selected = [q for q in questions if q.get("split") == args.split]
    validate(chunks, selected)

    if any((args.output / name).exists() for name in ("summary.json", "traces.json")):
        raise ValueError("Output đã tồn tại. Hãy dùng thư mục kết quả mới.")

    from dotenv import dotenv_values
    import psycopg
    from psycopg.rows import dict_row
    from pgvector.psycopg import register_vector

    database_url = os.getenv("DATABASE_URL") or dotenv_values(DAY6 / ".env").get(
        "DATABASE_URL"
    )
    if not database_url:
        raise ValueError("Chưa có DATABASE_URL trong môi trường hoặc .env Day 6.")

    snapshot = (
        DAY6
        / "models"
        / ("models--" + MODEL.replace("/", "--"))
        / "snapshots"
        / REVISION
    )
    if not snapshot.is_dir():
        raise FileNotFoundError(f"Không tìm thấy model Day 6: {snapshot}")

    with psycopg.connect(
        database_url,
        autocommit=True,
        connect_timeout=10,
        row_factory=dict_row,
    ) as connection:
        connection.execute("SET default_transaction_read_only = on")
        register_vector(connection)

        stored = connection.execute(
            """
            SELECT chunk_id AS id, document_id AS source_id,
                   source, page, text, metadata,
                   vector_dims(embedding) AS dimensions
            FROM day6_chunks
            WHERE collection = %s AND strategy = %s
            ORDER BY chunk_id
            """,
            (COLLECTION, STRATEGY),
        ).fetchall()

        if not stored or any(row["dimensions"] != 384 for row in stored):
            raise ValueError("Index trống hoặc vector không có 384 chiều.")

        stored_chunks = [
            {k: v for k, v in row.items() if k != "dimensions"} for row in stored
        ]
        if stored_chunks != sorted(chunks, key=lambda c: c["id"]):
            raise ValueError("Dữ liệu database khác với file chunk đã xuất.")

        print(f"Đã kiểm tra {len(stored)} chunk. Đang nạp model...", flush=True)

        import torch
        from sentence_transformers import SentenceTransformer

        torch.manual_seed(0)
        torch.set_num_threads(4)
        started = time.perf_counter()
        model = SentenceTransformer(str(snapshot), device="cpu", local_files_only=True)
        model_load_seconds = time.perf_counter() - started

        if model.get_embedding_dimension() != 384:
            raise ValueError("Model không tương thích với vector Day 6.")

        print("Model sẵn sàng. Đang chạy benchmark...", flush=True)
        index = DenseIndex(connection, model)

        if args.method == "hybrid":
            index = HybridIndex(
                dense=index,
                lexical=TfidfIndex(chunks),
                candidates=10,
                rrf_k=60,
            )

        if args.budget < 1:
            raise ValueError("Context budget phải lớn hơn 0.")

        traces = evaluate(index, selected, budget=args.budget)

        for trace in traces:
            trace["strategy"] = args.method

    summary = {
        "strategy": args.method,
        "candidate_k": 10 if args.method == "hybrid" else 3,
        "rrf_k": 60 if args.method == "hybrid" else None,
        "split": args.split,
        "n": len(traces),
        "hit1": sum(t["hit1"] for t in traces),
        "hit3": sum(t["hit3"] for t in traces),
        "context_hit": sum(t["context_hit"] for t in traces),
        "avg_context_chars": statistics.mean(t["context_chars"] for t in traces),
        "median_ms": statistics.median(t["elapsed_ms"] for t in traces),
        "model_load_seconds": model_load_seconds,
        "model": MODEL,
        "revision": REVISION,
        "dimensions": 384,
        "collection": COLLECTION,
        "day6_strategy": STRATEGY,
        "top_k": 3,
        "budget_chars": args.budget,
        "filter_policy": "none",
        "service_cost_usd": 0,
    }

    args.output.mkdir(parents=True, exist_ok=True)
    for name, data in (
        ("summary.json", summary),
        ("traces.json", traces),
    ):
        (args.output / name).write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
