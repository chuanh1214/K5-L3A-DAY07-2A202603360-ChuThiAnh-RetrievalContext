"""Compare fixed TF-IDF/hybrid retrieval on answerable test questions only.

Uses the existing Day 6 snapshot and never calls an answer-generating LLM.
"""
import argparse
import json
from pathlib import Path
import statistics
import time

from baseline import evaluate, validate
from run_rag_agent import connect_retriever


def write_json(path, value):
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--questions', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    chunks = json.loads((root / 'data/day6_chunks.json').read_text(encoding='utf-8'))
    questions = [q for q in json.loads(args.questions.read_text(encoding='utf-8'))
                 if q.get('split') == 'test']
    if any(not q.get('answerable', True) for q in questions):
        raise ValueError('Use the answerable-only test file; abstention is evaluated separately.')
    validate(chunks, questions)
    if args.output.exists():
        raise ValueError('Output exists; do not overwrite a test evaluation.')
    args.output.mkdir(parents=True)

    summaries = []
    for method in ('tfidf', 'hybrid'):
        print(f'Preparing {method} retrieval...', flush=True)
        started = time.perf_counter()
        connection, index = connect_retriever(chunks, method)
        setup_seconds = time.perf_counter() - started
        try:
            traces = evaluate(index, questions, budget=1600)
        finally:
            connection.close()

        for trace in traces:
            trace['strategy'] = method
        summary = {
            'strategy': method,
            'split': 'test',
            'n': len(traces),
            'hit1': sum(t['hit1'] for t in traces),
            'hit3': sum(t['hit3'] for t in traces),
            'context_hit': sum(t['context_hit'] for t in traces),
            'avg_context_chars': statistics.mean(t['context_chars'] for t in traces),
            'median_ms': statistics.median(t['elapsed_ms'] for t in traces),
            'retriever_setup_seconds': setup_seconds,
            'top_k': 3,
            'budget_chars': 1600,
            'candidate_k': 10 if method == 'hybrid' else 3,
            'rrf_k': 60 if method == 'hybrid' else None,
            'filter_policy': 'none',
            'service_cost_usd': 0,
            'note': 'One original query per question; not a multi-turn agent evaluation.',
        }
        destination = args.output / method
        destination.mkdir()
        write_json(destination / 'traces.json', traces)
        write_json(destination / 'summary.json', summary)
        summaries.append(summary)

    write_json(args.output / 'comparison.json', summaries)
    print(json.dumps(summaries, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
