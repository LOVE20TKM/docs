#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "$0")/../.." && pwd)"

python3 "$repo_root/ai/skills/love20-tkm-core-protocol/scripts/generate_interface_index.py"
python3 "$repo_root/ai/skills/love20-tkm-contract-playbooks/scripts/generate_playbook_index.py"
python3 "$repo_root/ai/skills/love20-tkm-selectors-and-errors/scripts/generate_selector_indexes.py"
python3 "$repo_root/ai/skills/love20-tkm-state-and-events/scripts/generate_state_event_index.py"
python3 "$repo_root/ai/scripts/generate_skill_benchmark_catalog.py"
python3 "$repo_root/ai/scripts/generate_skill_run_report.py" "$repo_root/ai/evals/runs/demo-walkthrough.json"
python3 "$repo_root/ai/scripts/generate_skill_run_todo.py" "$repo_root/ai/evals/runs/demo-walkthrough.json"
python3 "$repo_root/ai/scripts/generate_skill_run_report.py" "$repo_root/ai/evals/runs/demo-three-states.json"
python3 "$repo_root/ai/scripts/generate_skill_run_todo.py" "$repo_root/ai/evals/runs/demo-three-states.json"
python3 "$repo_root/ai/scripts/generate_skill_run_summary.py"
python3 "$repo_root/ai/scripts/validate_love20_skills.py"

printf 'LOVE20 skills refreshed and validated.\n'
