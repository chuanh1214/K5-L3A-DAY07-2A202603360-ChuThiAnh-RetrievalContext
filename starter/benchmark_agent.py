"""Chạy agent trên một split, lưu kết quả từng câu để chấm thủ công."""
import argparse
import json
import os
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv

from run_rag_agent import connect_retriever, run_agent


def write_json(path, data):
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--split", required=True, choices=["dev", "test"])
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--method", choices=["tfidf", "dense", "hybrid"], default="hybrid"
    )
    parser.add_argument("--budget", type=int, default=1600)
    parser.add_argument("--max-searches", type=int, default=4)
    args = parser.parse_args()

    if args.budget < 1 or args.max_searches < 1:
        parser.error("Budget và max-searches phải lớn hơn 0.")
    if args.output.exists():
        parser.error("Output đã tồn tại. Hãy chọn thư mục mới.")

    base = Path(__file__).resolve().parent
    load_dotenv(base / ".env")

    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    model_name = os.getenv("OPENROUTER_MODEL", "").strip()
    if not api_key or not model_name:
        raise ValueError("Thiếu cấu hình OpenRouter.")

    questions = json.loads(
        args.questions.read_text(encoding="utf-8")
    )
    selected = [q for q in questions if q.get("split") == args.split]

    if not selected:
        raise ValueError("Split không có câu hỏi.")

    ids = [q["id"] for q in selected]
    if len(ids) != len(set(ids)):
        raise ValueError("Query ID bị trùng.")

    chunks = json.loads(
        (base.parent / "data/day6_chunks.json").read_text(encoding="utf-8")
    )

    args.output.mkdir(parents=True)
    write_json(args.output / "config.json", {
        "model": model_name,
        "method": args.method,
        "split": args.split,
        "budget_chars": args.budget,
        "max_searches": args.max_searches,
        "questions_file": str(args.questions),
    })

    # Chỉ dùng các trường này cho script tổng hợp đánh giá sau này.
    cases = [
        {
            "id": q["id"],
            "split": q["split"],
            "answerable": q.get("answerable", True),
        }
        for q in selected
    ]
    write_json(args.output / "cases.json", cases)

    print("Đang chuẩn bị retriever...", flush=True)
    connection, index = connect_retriever(chunks, args.method)
    traces = []

    try:
        for number, question in enumerate(selected, start=1):
            print(
                f"[{number}/{len(selected)}] {question['id']}",
                flush=True,
            )

            # Không truyền gold, expected_answer hoặc nhãn answerable.
            trace = run_agent(
                question=question["question"],
                index=index,
                api_key=api_key,
                model_name=model_name,
                budget=args.budget,
                max_searches=args.max_searches,
            )
            trace["query_id"] = question["id"]
            trace["split"] = args.split
            trace["retrieval_method"] = args.method
            traces.append(trace)

            # Lưu sau mỗi câu để giữ kết quả nếu bị gián đoạn.
            write_json(args.output / "traces.json", traces)
            print(
                f"  status={trace['status']}, "
                f"searches={trace['search_count']}",
                flush=True,
            )
    finally:
        connection.close()

    known_costs = [
        t["reported_cost_usd"]
        for t in traces
        if t["reported_cost_usd"] is not None
    ]
    summary = {
        "split": args.split,
        "method": args.method,
        "n": len(traces),
        "statuses": dict(Counter(t["status"] for t in traces)),
        "total_searches": sum(t["search_count"] for t in traces),
        "sum_known_cost_usd": sum(known_costs),
        "queries_with_unknown_cost": len(traces) - len(known_costs),
        "note": "Chưa chấm độ đúng, citation hoặc abstention.",
    }
    write_json(args.output / "run_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()