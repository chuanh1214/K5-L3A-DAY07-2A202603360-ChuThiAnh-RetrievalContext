import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv


BASE_URL = "https://openrouter.ai/api/v1"


def request_json(path, payload=None, api_key=None):
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    request = Request(
        BASE_URL + path,
        headers=headers,
        data=(
            json.dumps(payload).encode("utf-8")
            if payload is not None else None
        ),
    )
    with urlopen(request, timeout=60) as response:
        return json.load(response)


def main():
    load_dotenv(Path(__file__).resolve().parent / ".env")

    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    model = os.getenv("OPENROUTER_MODEL", "").strip()

    if not api_key or not model:
        raise ValueError(
            "Thiếu OPENROUTER_API_KEY hoặc OPENROUTER_MODEL."
        )

    print("Đang kiểm tra model ID...", flush=True)
    models = request_json("/models")["data"]
    matched = next((m for m in models if m["id"] == model), None)

    if matched is None:
        print(f"Không tìm thấy model ID chính xác: {model}")
        print("Một số model DeepSeek trong danh mục:")
        for item in models:
            if "deepseek" in item["id"].lower():
                print(" -", item["id"])
        print("Sửa OPENROUTER_MODEL bằng ID chính xác rồi chạy lại.")
        return 1

    print("Model ID hợp lệ:", model)
    print("Đang thử một yêu cầu gọi tool...", flush=True)

    result = request_json(
        "/chat/completions",
        api_key=api_key,
        payload={
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Use search to find evidence in Think Python "
                        "about list.pop() with no index. "
                        "Generate a search query; do not answer."
                    ),
                }
            ],
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "search",
                        "description": "Search the local document corpus.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "query": {"type": "string"}
                            },
                            "required": ["query"],
                            "additionalProperties": False,
                        },
                    },
                }
            ],
            "tool_choice": {
                "type": "function",
                "function": {"name": "search"},
            },
            "max_tokens": 1024,
        },
    )

    if "error" in result:
        raise RuntimeError(json.dumps(result["error"], ensure_ascii=False))

    message = result["choices"][0]["message"]
    calls = message.get("tool_calls") or []
    if not calls:
        raise RuntimeError(
            "API trả về nhưng không có tool_calls. "
            "Chưa xác nhận model gọi tool được."
        )

    for call in calls:
        function = call["function"]
        arguments = json.loads(function["arguments"])
        query = arguments.get("query")

        if (
            function["name"] != "search"
            or not isinstance(query, str)
            or not query.strip()
        ):
            raise ValueError("Model trả về tool hoặc query không hợp lệ.")

        print("Tool:", function["name"])
        print("Query:", query)

    print("Usage:", json.dumps(result.get("usage"), ensure_ascii=False))
    print("LLM tool-calling check OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except HTTPError as error:
        print("HTTP error:", error.code)
        print(error.read().decode("utf-8", errors="replace"))
        raise SystemExit(1)
    except (URLError, TimeoutError) as error:
        print("Lỗi kết nối hoặc timeout:", error)
        raise SystemExit(1)
    except Exception as error:
        print(type(error).__name__ + ":", error)
        raise SystemExit(1)