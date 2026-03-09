#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a markdown summary across LOVE20 skill benchmark runs."
    )
    parser.add_argument(
        "--runs-dir",
        default=None,
        help="Optional runs directory. Defaults to ai/evals/runs",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional output markdown path. Defaults to ai/evals/run-summary.md",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def bool_count(values: list[bool | None]) -> tuple[int, int]:
    considered = [value for value in values if value is not None]
    return sum(1 for value in considered if value), len(considered)


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


def summarize_run(run_file: Path, repo_root: Path) -> dict[str, object]:
    run_data = load_json(run_file)
    benchmark_rel = run_data["benchmark_file"].replace("docs/", "", 1)
    benchmark_file = (repo_root / benchmark_rel).resolve()
    benchmark_data = load_json(benchmark_file)
    benchmark_by_id = {item["id"]: item for item in benchmark_data["benchmarks"]}

    total_must_cover_hit = 0
    total_must_cover = 0
    primary_hits = 0
    cited_complete = 0
    complete_cases = 0
    passed_cases = 0
    review_cases = 0
    incomplete_cases = 0
    output_shape_values: list[bool | None] = []

    for case in run_data["results"]:
        benchmark = benchmark_by_id[case["id"]]
        status, _, must_cover_hit, must_cover_total = case_status(case, benchmark)
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
        elif status == "REVIEW":
            review_cases += 1
        else:
            incomplete_cases += 1
        output_shape_values.append(case.get("judgement", {}).get("output_shape_match"))

    output_shape_pass, output_shape_total = bool_count(output_shape_values)
    average_must_cover = 0 if total_must_cover == 0 else round((total_must_cover_hit / total_must_cover) * 100)

    return {
        "run_name": run_data["run_name"],
        "run_file": run_file,
        "total_cases": len(run_data["results"]),
        "complete_cases": complete_cases,
        "passed_cases": passed_cases,
        "review_cases": review_cases,
        "incomplete_cases": incomplete_cases,
        "primary_hits": primary_hits,
        "cited_complete": cited_complete,
        "average_must_cover": average_must_cover,
        "output_shape_pass": output_shape_pass,
        "output_shape_total": output_shape_total,
    }


def render_summary(repo_root: Path, run_summaries: list[dict[str, object]]) -> str:
    lines = [
        "# LOVE20 Skill Run Summary",
        "",
        "| Run | Cases | Pass | Review | Incomplete | Complete | Primary Skill Hit | Cited Files | Must Cover | Output Shape |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for summary in sorted(run_summaries, key=lambda item: str(item["run_name"])):
        run_file = Path(summary["run_file"])
        report_file = run_file.with_suffix(".report.md")
        todo_file = run_file.with_suffix(".todo.md")
        run_label = f"`{summary['run_name']}`"
        run_ref = f"`docs/{run_file.relative_to(repo_root)}`"
        links = [run_ref]
        if report_file.exists():
            links.append(f"[report]({report_file.relative_to(repo_root).as_posix()})")
        if todo_file.exists():
            links.append(f"[todo]({todo_file.relative_to(repo_root).as_posix()})")
        run_text = f"{run_label}<br>{'<br>'.join(links)}"
        lines.append(
            "| "
            + " | ".join(
                [
                    run_text,
                    str(summary["total_cases"]),
                    str(summary["passed_cases"]),
                    str(summary["review_cases"]),
                    str(summary["incomplete_cases"]),
                    str(summary["complete_cases"]),
                    f"{summary['primary_hits']}/{summary['total_cases']}",
                    f"{summary['cited_complete']}/{summary['total_cases']}",
                    f"{summary['average_must_cover']}%",
                    f"{summary['output_shape_pass']}/{summary['output_shape_total']}",
                ]
            )
            + " |"
        )

    lines.extend(["", "## Notes", ""])
    lines.append("- `demo-walkthrough` should stay as the all-PASS ideal-answer baseline.")
    lines.append("- `demo-three-states` should keep at least one REVIEW and one INCOMPLETE case.")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    runs_dir = (
        Path(args.runs_dir).resolve()
        if args.runs_dir
        else (repo_root / "ai" / "evals" / "runs").resolve()
    )
    output = (
        Path(args.output).resolve()
        if args.output
        else (repo_root / "ai" / "evals" / "run-summary.md").resolve()
    )

    run_summaries = [
        summarize_run(run_file, repo_root)
        for run_file in sorted(runs_dir.glob("*.json"))
    ]
    output.write_text(render_summary(repo_root, run_summaries), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
