#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate or update a semi-automatic LOVE20 skill benchmark run."
    )
    parser.add_argument("run_name", help="Run name, for example: demo-auto-run")
    parser.add_argument(
        "--benchmark-file",
        default="docs/ai/evals/love20_skill_benchmarks.json",
        help="Benchmark JSON path recorded into the run file.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional run JSON output path. Defaults to ai/evals/runs/<run_name>.json",
    )
    parser.add_argument(
        "--case",
        action="append",
        dest="case_ids",
        default=[],
        help="Only materialize the given benchmark case id. Repeatable.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only materialize the first N benchmark cases after filtering.",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append missing cases into an existing run file instead of rebuilding from scratch.",
    )
    parser.add_argument(
        "--overwrite-response",
        action="store_true",
        help="Overwrite existing response skeleton markdown files.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_case(benchmark: dict[str, object], run_name: str) -> dict[str, object]:
    must_cover = {item: None for item in benchmark["must_cover"]}  # type: ignore[index]
    case_id = benchmark["id"]
    return {
        "id": case_id,
        "selected_skills": [benchmark["primary_skill"]],
        "response_file": f"docs/ai/evals/runs/{run_name}.{case_id}.response.md",
        "cited_files": [],
        "judgement": {
            "must_cover": must_cover,
            "output_shape_match": None,
            "notes": "skeleton generated; fill response, citations, and judgement",
        },
    }


def render_response_skeleton(
    benchmark: dict[str, object],
    response_file: str,
) -> str:
    secondary = benchmark["secondary_skills"]
    secondary_text = ", ".join(f"`{skill}`" for skill in secondary) if secondary else "_none_"
    lines = [
        f"# Demo Response: {benchmark['id']}",
        "",
        "## Prompt",
        "",
        benchmark["prompt"],
        "",
        "## Expected Output",
        "",
        f"- `{benchmark['expected_output']}`",
        "",
        "## Skill Routing",
        "",
        f"- Primary: `{benchmark['primary_skill']}`",
        f"- Secondary: {secondary_text}",
        "",
        "## Must Cover",
        "",
    ]
    lines.extend(f"- {item}" for item in benchmark["must_cover"])
    lines.extend(
        [
            "",
            "## Draft Answer",
            "",
            "_Fill this response._",
            "",
            "## Candidate Citations",
            "",
            "_List exact docs/code/tests/hooks/SQL files used in the answer._",
            "",
            "## Notes",
            "",
            f"- Intended response file: `{response_file}`",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def materialize_response_file(
    repo_root: Path,
    benchmark: dict[str, object],
    case: dict[str, object],
    overwrite: bool,
) -> None:
    response_rel = case["response_file"].replace("docs/", "", 1)
    response_path = (repo_root / response_rel).resolve()
    response_path.parent.mkdir(parents=True, exist_ok=True)
    if response_path.exists() and not overwrite:
        return
    response_path.write_text(
        render_response_skeleton(benchmark, case["response_file"]),
        encoding="utf-8",
    )


def run_helper(script_path: Path, *args: str) -> None:
    subprocess.run(
        [sys.executable, str(script_path), *args],
        check=True,
    )


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    benchmark_rel = args.benchmark_file.replace("docs/", "", 1)
    benchmark_path = (repo_root / benchmark_rel).resolve()
    benchmark_data = load_json(benchmark_path)
    benchmarks = benchmark_data["benchmarks"]

    selected_benchmarks = benchmarks
    if args.case_ids:
        wanted = set(args.case_ids)
        selected_benchmarks = [item for item in selected_benchmarks if item["id"] in wanted]
    if args.limit is not None:
        selected_benchmarks = selected_benchmarks[: args.limit]

    output = (
        Path(args.output).resolve()
        if args.output
        else (repo_root / "ai" / "evals" / "runs" / f"{args.run_name}.json").resolve()
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    if args.append and output.exists():
        run_data = load_json(output)
        existing_by_id = {item["id"]: item for item in run_data["results"]}
    else:
        run_data = {
            "schema_version": 1,
            "run_name": args.run_name,
            "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "benchmark_file": args.benchmark_file,
            "results": [],
        }
        existing_by_id = {}

    benchmark_by_id = {item["id"]: item for item in benchmarks}
    all_ids_in_order = [item["id"] for item in benchmarks]

    for benchmark in selected_benchmarks:
        case_id = benchmark["id"]
        if case_id not in existing_by_id:
            existing_by_id[case_id] = build_case(benchmark, args.run_name)
        else:
            case = existing_by_id[case_id]
            if not case.get("selected_skills"):
                case["selected_skills"] = [benchmark["primary_skill"]]
            if not case.get("response_file"):
                case["response_file"] = f"docs/ai/evals/runs/{args.run_name}.{case_id}.response.md"
            if not case.get("judgement", {}).get("must_cover"):
                case["judgement"]["must_cover"] = {
                    item: None for item in benchmark["must_cover"]
                }
        materialize_response_file(
            repo_root,
            benchmark,
            existing_by_id[case_id],
            args.overwrite_response,
        )

    run_data["results"] = [
        existing_by_id[case_id]
        for case_id in all_ids_in_order
        if case_id in existing_by_id
    ]
    output.write_text(json.dumps(run_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    run_helper(repo_root / "ai" / "scripts" / "generate_skill_run_report.py", str(output))
    run_helper(repo_root / "ai" / "scripts" / "generate_skill_run_todo.py", str(output))
    run_helper(repo_root / "ai" / "scripts" / "generate_skill_run_summary.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
