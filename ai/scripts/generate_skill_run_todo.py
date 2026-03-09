#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a TODO checklist for incomplete or review-needed LOVE20 skill benchmark cases."
    )
    parser.add_argument("run_file", help="Path to ai/evals/runs/*.json")
    parser.add_argument(
        "--output",
        default=None,
        help="Optional output markdown path. Defaults to <run_file>.todo.md",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def display_run_file(repo_root: Path, run_file: Path) -> str:
    try:
        return f"docs/{run_file.relative_to(repo_root)}"
    except ValueError:
        return str(run_file)


def case_status(case: dict, benchmark: dict) -> tuple[str, list[str], int, int]:
    warnings: list[str] = []
    selected_skills = case.get("selected_skills", [])
    response_file = case.get("response_file", "")
    cited_files = case.get("cited_files", [])
    judgement = case.get("judgement", {})
    must_cover = judgement.get("must_cover", {})
    output_shape = judgement.get("output_shape_match")

    must_cover_total = len(benchmark.get("must_cover", []))
    must_cover_hit = sum(1 for value in must_cover.values() if value is True)
    must_cover_complete = len(must_cover) == must_cover_total and all(
        value is not None for value in must_cover.values()
    )

    primary_hit = benchmark["primary_skill"] in selected_skills
    if not primary_hit:
        warnings.append("missing primary skill routing")
    if not response_file:
        warnings.append("missing response file")
    if not cited_files:
        warnings.append("no cited files recorded")
    if not must_cover_complete:
        warnings.append("must_cover judgement incomplete")
    if output_shape is None:
        warnings.append("output_shape judgement incomplete")

    if not warnings and output_shape is True and must_cover_hit == must_cover_total:
        return "PASS", warnings, must_cover_hit, must_cover_total
    if response_file and cited_files and output_shape is True and primary_hit:
        return "REVIEW", warnings, must_cover_hit, must_cover_total
    return "INCOMPLETE", warnings, must_cover_hit, must_cover_total


def render_todo(repo_root: Path, run_file: Path, run_data: dict, benchmark_data: dict) -> str:
    benchmark_by_id = {item["id"]: item for item in benchmark_data["benchmarks"]}

    review_rows: list[dict] = []
    incomplete_rows: list[dict] = []

    for case in run_data["results"]:
        benchmark = benchmark_by_id[case["id"]]
        status, warnings, must_cover_hit, must_cover_total = case_status(case, benchmark)
        row = {
            "case": case,
            "benchmark": benchmark,
            "warnings": warnings,
            "must_cover_hit": must_cover_hit,
            "must_cover_total": must_cover_total,
        }
        if status == "REVIEW":
            review_rows.append(row)
        elif status == "INCOMPLETE":
            incomplete_rows.append(row)

    lines = [
        "# LOVE20 Skill Run TODO",
        "",
        f"- Run file: `{display_run_file(repo_root, run_file)}`",
        f"- Run name: `{run_data['run_name']}`",
        f"- Review cases: {len(review_rows)}",
        f"- Incomplete cases: {len(incomplete_rows)}",
    ]

    if not review_rows and not incomplete_rows:
        lines.extend(["", "All cases are PASS."])
        return "\n".join(lines).rstrip() + "\n"

    if review_rows:
        lines.extend(["", "## REVIEW", ""])
        for row in review_rows:
            case = row["case"]
            benchmark = row["benchmark"]
            lines.append(f"### {benchmark['title']}")
            lines.append("")
            lines.append(f"- `id`: `{case['id']}`")
            lines.append(f"- Current must-cover: {row['must_cover_hit']}/{row['must_cover_total']}")
            lines.append("- Remaining work:")
            for item in benchmark["must_cover"]:
                value = case.get("judgement", {}).get("must_cover", {}).get(item)
                if value is not True:
                    lines.append(f"  - fill or fix: `{item}`")
            lines.append("")

    if incomplete_rows:
        lines.extend(["", "## INCOMPLETE", ""])
        for row in incomplete_rows:
            case = row["case"]
            benchmark = row["benchmark"]
            lines.append(f"### {benchmark['title']}")
            lines.append("")
            lines.append(f"- `id`: `{case['id']}`")
            lines.append("- Missing or pending:")
            for warning in row["warnings"]:
                lines.append(f"  - {warning}")
            lines.append("- Expected must-cover:")
            for item in benchmark["must_cover"]:
                lines.append(f"  - `{item}`")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    run_file = Path(args.run_file).resolve()
    run_data = load_json(run_file)

    repo_root = Path(__file__).resolve().parents[2]
    benchmark_rel = run_data["benchmark_file"].replace("docs/", "", 1)
    benchmark_file = (repo_root / benchmark_rel).resolve()
    benchmark_data = load_json(benchmark_file)

    output = Path(args.output).resolve() if args.output else run_file.with_suffix(".todo.md")
    output.write_text(render_todo(repo_root, run_file, run_data, benchmark_data), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
