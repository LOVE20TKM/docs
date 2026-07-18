---
name: love20-runbooks
description: "Troubleshoot LOVE20 launch, contribute, claim, stake, submit, vote, join, verify, mint, extension registration, group mint, default group identity, group-chat activation or posting, frontend transaction, event-sync, and indexed-history failures."
---

# LOVE20 Runbooks

Use this skill when the user already has a symptom and needs the shortest path to root cause.

## Workflow

1. Read `references/evidence-sources.md` first and classify the symptom:
   - contract revert or raw selector
   - phase or state mismatch
   - extension or group-specific failure
   - group-chat activation, posting, source, ban, or plugin failure
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
- Treat contract source as the highest-priority rule source for the deployed instance. During the group-chat pilot, also check whether the frontend and scripts point to the latest redeployment.
- Use tests as behavioral witnesses when docs are ambiguous. The test repos already encode many expected revert paths and timing constraints.
- Distinguish protocol truth from convenience layers:
  - core contracts define state and rules
  - periphery and hub contracts wrap user flows
  - `interface-test` translates active-test failures into UX text; `interface` reflects the released production parser
  - script/log tooling reconstructs historical events
- Call out whether the failure is caused by:
  - bad input
  - wrong phase or waiting period
  - missing approval or insufficient balance
  - stale frontend state or RPC failure
  - extension/group registration mismatch
  - group-chat owner, sender identity, source, ban, plugin, or round mismatch
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
