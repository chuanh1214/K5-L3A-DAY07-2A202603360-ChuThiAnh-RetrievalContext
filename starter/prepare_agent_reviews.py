"""Tạo phiếu chấm thủ công; không tự chấm nội dung hoặc gọi model."""
import argparse
import json
from pathlib import Path


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--traces", required=True, type=Path)
    parser.add_argument("--split", required=True, choices=["dev", "test"])
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    questions = [
        q for q in load(args.questions)
        if q["split"] == args.split
    ]
    traces = [
        t for t in load(args.traces)
        if t["split"] == args.split
    ]

    question_map = {q["id"]: q for q in questions}
    trace_map = {t["query_id"]: t for t in traces}

    if len(question_map) != len(questions):
        raise ValueError("Question ID bị trùng.")
    if len(trace_map) != len(traces):
        raise ValueError("Trace ID bị trùng.")
    if set(question_map) != set(trace_map):
        raise ValueError("Danh sách câu hỏi và trace không khớp.")
    if args.output.exists():
        raise ValueError("Output đã tồn tại; không ghi đè phiếu đã chấm.")

    reviews = []
    packet = [
        "# Phiếu đối chiếu câu trả lời",
        "",
        "Đọc context cuối, không chỉ kiểm tra ID citation.",
        "Gold là nhãn tham chiếu, không thay thế việc đọc evidence.",
        "",
    ]

    for question in questions:
        qid = question["id"]
        trace = trace_map[qid]
        answerable = question.get("answerable", True)
        citations = trace.get("citations", [])

        packet.extend([
            f"## {qid}",
            "",
            f"**Câu hỏi:** {question['question']}",
            "",
            f"**Có đáp án:** {answerable}",
            f"**Trạng thái:** {trace['status']}",
            "",
            "**Câu trả lời:**",
            trace.get("answer") or "(Không có)",
            "",
            "**Đáp án tham chiếu:**",
            question.get("expected_answer", "(Yêu cầu từ chối)"),
            "",
            "**Gold / lý do thiếu bằng chứng:**",
            json.dumps(
                question.get("gold", question.get("absence_reason")),
                ensure_ascii=False,
                indent=2,
            ),
            "",
            "**Citations theo thứ tự cần chấm:**",
            json.dumps(citations, ensure_ascii=False),
            "",
            "**Context cuối thực sự gửi cho model:**",
            trace.get("context") or "(Rỗng)",
            "",
            "**Các query đã tìm:**",
            json.dumps(
                [
                    event["query"]
                    for event in trace.get("events", [])
                    if event.get("event") == "search"
                ],
                ensure_ascii=False,
                indent=2,
            ),
            "",
        ])

        if trace["status"] == "error":
            packet.extend([
                "**Lỗi — báo riêng, không tạo nhãn chất lượng:**",
                json.dumps(trace.get("error"), ensure_ascii=False),
                "",
            ])
            continue

        review = {
            "query_id": qid,
            "citation_support": [None for _ in citations],
            "reason": "",
        }
        if answerable:
            review["answer_grade"] = None
            review["context_grade"] = None
        else:
            review["abstention_correct"] = None

        reviews.append(review)

    args.output.mkdir(parents=True)
    (args.output / "review_packet.md").write_text(
        "\n".join(packet), encoding="utf-8"
    )
    (args.output / "reviews.json").write_text(
        json.dumps(reviews, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("Đã tạo phiếu:", args.output / "review_packet.md")
    print("Điền nhãn tại:", args.output / "reviews.json")
    print("Số kết quả cần chấm:", len(reviews))
    print("Các giá trị null chưa phải nhãn hoàn chỉnh.")


if __name__ == "__main__":
    main()