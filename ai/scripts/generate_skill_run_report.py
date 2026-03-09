#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a markdown report for a LOVE20 skill benchmark run."
    )
    parser.add_argument("run_file", help="Path to ai/evals/runs/*.json")
    parser.add_argument(
        "--output",
        default=None,
        help="Optional output markdown path. Defaults to <run_file>.report.md",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def bool_count(values: list[bool | None]) -> tuple[int, int]:
    considered = [value for value in values if value is not None]
    return sum(1 for value in considered if value), len(considered)


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


def render_report(repo_root: Path, run_file: Path, run_data: dict, benchmark_data: dict) -> str:
    benchmark_by_id = {item["id"]: item for item in benchmark_data["benchmarks"]}
    results = run_data["results"]

    rows: list[dict] = []
    total_must_cover_hit = 0
    total_must_cover = 0
    primary_hits = 0
    cited_complete = 0
    complete_cases = 0
    passed_cases = 0
    output_shape_values: list[bool | None] = []

    for case in results:
        benchmark = benchmark_by_id[case["id"]]
        status, warnings, must_cover_hit, must_cover_total = case_status(case, benchmark)
        total_must_cover_hit += must_cover_hit
        total_must_cover += must_cover_total
        if benchmark["primary_skill"] in case.get("selected_skills", []):
            primary_hits += 1
        if case.get("cited_files"):
            cited_complete += 1
        if status != "INCOMPLETE":
            complete_cases += 1
        if status == "PASS":
            passed_cases += 1
        output_shape_values.append(case.get("judgement", {}).get("output_shape_match"))
        rows.append(
            {
                "case": case,
                "benchmark": benchmark,
                "status": status,
                "warnings": warnings,
                "must_cover_hit": must_cover_hit,
                "must_cover_total": must_cover_total,
            }
        )

    output_shape_pass, output_shape_total = bool_count(output_shape_values)
    average_must_cover = 0 if total_must_cover == 0 else round((total_must_cover_hit / total_must_cover) * 100)

    lines = [
        "# LOVE20 Skill Benchmark Run Report",
        "",
        f"- Run file: `{display_run_file(repo_root, run_file)}`",
        f"- Run name: `{run_data['run_name']}`",
        f"- Total benchmark cases: {len(benchmark_data['benchmarks'])}",
        f"- Cases in run: {len(results)}",
        f"- Complete cases: {complete_cases}",
        f"- Passed cases: {passed_cases}",
        f"- Primary skill hit rate: {primary_hits}/{len(results)}",
        f"- Cited files complete rate: {cited_complete}/{len(results)}",
        f"- Average must-cover score: {average_must_cover}%",
        f"- Output-shape pass rate: {output_shape_pass}/{output_shape_total}",
        "",
        "## Case Results",
        "",
        "| Case | Status | Primary Skills | Response | Must Cover | Output Shape | Notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    for row in rows:
        case = row["case"]
        benchmark = row["benchmark"]
        primary_status = "hit" if benchmark["primary_skill"] in case.get("selected_skills", []) else "miss"
        response_status = "ok" if case.get("response_file") else "missing"
        output_shape = case.get("judgement", {}).get("output_shape_match")
        output_shape_text = "pass" if output_shape is True else "fail" if output_shape is False else "pending"
        notes = case.get("judgement", {}).get("notes") or "; ".join(row["warnings"]) or "-"
        lines.append(
            f"| `{case['id']}` | {row['status']} | {primary_status} | {response_status} | {row['must_cover_hit']}/{row['must_cover_total']} | {output_shape_text} | {notes} |"
        )

    lines.extend(["", "## Details", ""])

    for row in rows:
        case = row["case"]
        benchmark = row["benchmark"]
        judgement = case.get("judgement", {})
        lines.append(f"### {benchmark['title']}")
        lines.append("")
        lines.append(f"- `id`: `{case['id']}`")
        selected = case.get("selected_skills", [])
        lines.append(
            "- Selected skills: " + (", ".join(f"`{skill}`" for skill in selected) if selected else "_none_")
        )
        response_file = case.get("response_file", "")
        lines.append(f"- Response file: `{response_file}`" if response_file else "- Response file: _missing_")
        cited_files = case.get("cited_files", [])
        if cited_files:
            lines.append("- Cited files:")
            for path in cited_files:
                lines.append(f"  - ok: `{path}`")
        else:
            lines.append("- Cited files: _none_")
        if row["warnings"]:
            lines.append("- Warnings:")
            for warning in row["warnings"]:
                lines.append(f"  - {warning}")
        notes = judgement.get("notes")
        if notes:
            lines.append(f"- Manual notes: {notes}")
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

    output = Path(args.output).resolve() if args.output else run_file.with_suffix(".report.md")
    output.write_text(
        render_report(repo_root, run_file, run_data, benchmark_data),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
