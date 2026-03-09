#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a blank LOVE20 skill benchmark run skeleton from the benchmark catalog."
    )
    parser.add_argument("run_name", help="Run name, for example: demo-new-run")
    parser.add_argument(
        "--benchmark-file",
        default="docs/ai/evals/love20_skill_benchmarks.json",
        help="Benchmark JSON path recorded into the run file.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional output path. Defaults to ai/evals/runs/<run_name>.json",
    )
    return parser.parse_args()


def build_case(benchmark: dict[str, object]) -> dict[str, object]:
    must_cover = {
        item: None for item in benchmark["must_cover"]  # type: ignore[index]
    }
    return {
        "id": benchmark["id"],
        "selected_skills": [],
        "response_file": "",
        "cited_files": [],
        "judgement": {
            "must_cover": must_cover,
            "output_shape_match": None,
            "notes": "",
        },
    }


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]

    benchmark_rel = args.benchmark_file.replace("docs/", "", 1)
    benchmark_path = (repo_root / benchmark_rel).resolve()
    benchmark_data = json.loads(benchmark_path.read_text(encoding="utf-8"))

    run_data = {
        "schema_version": 1,
        "run_name": args.run_name,
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "benchmark_file": args.benchmark_file,
        "results": [build_case(benchmark) for benchmark in benchmark_data["benchmarks"]],
    }

    output = (
        Path(args.output).resolve()
        if args.output
        else (repo_root / "ai" / "evals" / "runs" / f"{args.run_name}.json").resolve()
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(run_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
