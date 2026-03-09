#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "$0")/../.." && pwd)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
validator="$codex_home/skills/.system/skill-creator/scripts/quick_validate.py"

python3 "$repo_root/ai/skills/love20-core-protocol/scripts/generate_interface_index.py"
python3 "$repo_root/ai/skills/love20-contract-playbooks/scripts/generate_playbook_index.py"
python3 "$repo_root/ai/skills/love20-selectors-and-errors/scripts/generate_selector_indexes.py"
python3 "$repo_root/ai/skills/love20-state-and-events/scripts/generate_state_event_index.py"
python3 "$repo_root/ai/scripts/generate_skill_benchmark_catalog.py"
python3 "$repo_root/ai/scripts/generate_skill_run_report.py" "$repo_root/ai/evals/runs/demo-walkthrough.json"
python3 "$repo_root/ai/scripts/generate_skill_run_report.py" "$repo_root/ai/evals/runs/demo-three-states.json"
python3 "$repo_root/ai/scripts/generate_skill_run_todo.py" "$repo_root/ai/evals/runs/demo-three-states.json"
python3 "$repo_root/ai/scripts/generate_skill_run_summary.py"

python3 "$validator" "$repo_root/ai/skills/love20-navigator"
python3 "$validator" "$repo_root/ai/skills/love20-core-protocol"
python3 "$validator" "$repo_root/ai/skills/love20-contract-playbooks"
python3 "$validator" "$repo_root/ai/skills/love20-extension-patterns"
python3 "$validator" "$repo_root/ai/skills/love20-frontend-bridge"
python3 "$validator" "$repo_root/ai/skills/love20-selectors-and-errors"
python3 "$validator" "$repo_root/ai/skills/love20-runbooks"
python3 "$validator" "$repo_root/ai/skills/love20-state-and-events"
python3 "$validator" "$repo_root/ai/skills/love20-prompts"

printf 'LOVE20 skills refreshed and validated.\n'
