# Prompt Selection

## Start with the task shape

- Protocol or mechanism explanation:
  use `$love20-navigator` and `$love20-core-protocol`.
- Extension or derivative protocol implementation:
  use `$love20-extension-dev`; add `$love20-extension-patterns` when base-class choice or reward model is still unclear.
- Cross-repo integration or end-to-end wiring:
  use `$love20-integration-dev`; add the most relevant implementation skill when the owning repo still needs code changes.
- Contract interaction or user flow:
  use `$love20-contract-playbooks`, and add `$love20-extension-patterns` if extensions are involved.
- State query, read path, viewer, hook, or event timeline:
  use `$love20-state-and-events`.
- Failure triage:
  use `$love20-runbooks`; add `$love20-selectors-and-errors` when the symptom is a selector, topic, or raw revert.
- Frontend source mapping:
  use `$love20-frontend-bridge`; add `$love20-state-and-events` if the ask includes viewers or event history.
- Frontend feature or extension UI implementation:
  use `$love20-frontend-dev`; add `$love20-frontend-bridge` when you first need to trace the nearest existing page or hook chain.
- Test, regression, or release planning:
  use `$love20-test-and-release`; add `$love20-integration-dev` when the change crosses contract, script, and frontend layers.
- Acceptance or regression checks for another agent:
  use `$love20-prompts` and `references/junior-agent-acceptance-cases.md`.
- Review, docs sync, or skill update:
  pair the task with the most relevant domain skill above.

## Minimum fields a prompt should contain

- Goal:
  what the agent must produce.
- Anchors:
  token, symbol, round, actionId, account, network, tx hash, file path, or repo.
- Evidence rules:
  docs, code, tests, scripts, hooks, SQL, or selectors.
- Output contract:
  short answer, checklist, table, playbook, findings-first review, or patch summary.
- Conflict rule:
  when docs and code disagree, state both and say which is behavior truth.
- Source-of-truth rule:
  treat `core`, `extension`, `extension-lp`, `extension-group`, and `group` as the highest-priority code sources for deployed immutable behavior; treat `periphery`, `script`, and `interface` as adapters or execution layers unless the task is explicitly about them.

## When to split one prompt into several

Split when the user is actually asking for more than one of these:

- explain the mechanism
- tell me how to interact with it
- tell me current state
- debug a failure
- review code or docs changes

A smaller prompt usually gives better evidence and less hallucinated glue logic.
