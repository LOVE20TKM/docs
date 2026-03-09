---
name: love20-runbooks
description: "Troubleshoot LOVE20 protocol, contract, extension, group, and frontend failures by mapping a symptom to the fastest evidence sources and next checks. Use when a LOVE20 launch, contribute, claim, stake, submit, vote, join, verify, mint, extension registration, group mint, event sync, or frontend transaction flow does not behave as expected."
---

# LOVE20 Runbooks

Use this skill when the user already has a symptom and needs the shortest path to root cause.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/evidence-sources.md` first and classify the symptom:
   - contract revert or raw selector
   - phase or state mismatch
   - extension or group-specific failure
   - frontend message, timeout, or RPC failure
   - missing logs or inconsistent historical state
2. Read exactly one runbook first:
   - `references/launch-and-stake-runbooks.md`
   - `references/action-and-mint-runbooks.md`
   - `references/extensions-and-groups-runbooks.md`
   - `references/frontend-and-network-runbooks.md`
3. Open the concrete contract, test, script, or frontend file named in that runbook.
4. If the symptom is only a raw selector or topic, switch to `love20-selectors-and-errors` before concluding.
5. If the symptom is only a page-data mismatch, switch to `love20-frontend-bridge` after you identify the failing read path.

## Working Rules

- Prefer evidence over intuition. Start from the user-visible symptom, then verify phase, balances, allowances, and round/action state.
- Treat `core`, `extension`, `extension-lp`, `extension-group`, and `group` as the highest-priority rule sources when the failure could come from deployed immutable contracts.
- Use tests as behavioral witnesses when docs are ambiguous. The test repos already encode many expected revert paths and timing constraints.
- Distinguish protocol truth from convenience layers:
  - core contracts define state and rules
  - periphery and hub contracts wrap user flows
  - interface code translates raw failures into UX text
  - script/log tooling reconstructs historical events
- Call out whether the failure is caused by:
  - bad input
  - wrong phase or waiting period
  - missing approval or insufficient balance
  - stale frontend state or RPC failure
  - extension/group registration mismatch
  - log indexing not being refreshed

## Guardrails

- Do not answer a failure report with only a guess like "maybe allowance is missing". Name the exact contract surface and state read that would confirm it.
- If the user reports a Chinese frontend error, separate:
  - original chain or RPC failure
  - frontend parser heuristic
  - final displayed message
- If logs appear missing, verify whether `script/script/log/one_click_process.sh` has been run recently before assuming the contract failed to emit.
- When a failure may come from hub/periphery wrappers, still confirm the underlying core contract and phase rule.
- For group or extension issues, check token/action/address binding mismatches before checking UI code.
- Do not stop at wrapper, parser, or script symptoms when the failure can be confirmed against a deployed contract repo.

## References

- `references/evidence-sources.md`
- `references/launch-and-stake-runbooks.md`
- `references/action-and-mint-runbooks.md`
- `references/extensions-and-groups-runbooks.md`
- `references/frontend-and-network-runbooks.md`
