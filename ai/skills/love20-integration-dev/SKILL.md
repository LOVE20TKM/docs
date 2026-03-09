---
name: love20-integration-dev
description: "Wire LOVE20 changes across contract repos, periphery viewers, cast or log scripts, network address files, and frontend env or hook layers. Use when asked to carry a feature across multiple LOVE20 repos, align ABIs and addresses, integrate a new contract into viewers or scripts, reconcile end-to-end read and write paths, or make a local or public-test integration actually work."
---

# LOVE20 Integration Development

Use this skill when the task is to make multiple LOVE20 layers work together end to end, not just change one repo in isolation.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/integration-workflow.md`.
2. Read `references/sync-points.md`.
3. Identify the behavior-owning repo first:
   - `core`, `extension`, `extension-lp`, `extension-group`, or `group`
4. Map the downstream adapters that must stay in sync:
   - `periphery` viewers or hub
   - `script` ABI, cast, log, and network files
   - `interface` ABI, env, config, hooks, and pages
5. Patch the minimum set of layers needed to restore one complete read path or write path.

## Mandatory Triage

Before editing, classify the task on these axes:

1. Which repo owns the real behavior?
2. Is this a new deployment or an integration against already-deployed contracts?
3. Which sync points must align: ABI, address, viewer, cast script, log export, env, or frontend hook?
4. Does the task need read path, write path, or both?
5. Does success mean a code patch, an integration plan, or an end-to-end verification checklist?

If the change is still mostly about contract implementation, pair this skill with `love20-extension-dev` or `love20-core-protocol` first.

## Working Rules

- Start from the behavior truth, then move outward to adapters.
- Keep deployment scripts, network address files, and frontend env bindings aligned in one pass.
- If contract surface changes, update every consumer that depends on it:
  viewer, script ABI, cast usage, frontend ABI or hook, and extension registration if applicable.
- Use periphery viewers for aggregated current-state checks, not as a substitute for contract truth.
- Use `script/script/log` when the task depends on indexed history, exported events, or downstream data reconstruction.
- Treat integration as incomplete until one full path is named:
  write -> chain state -> viewer or script read -> frontend render or log export.

## Guardrails

- Do not patch only the UI when the contract surface or address registry changed underneath it.
- Do not assume ABI or address changes propagate automatically across `script` and `interface`.
- Do not mix local, public-test, and production-like env files without naming the target network explicitly.
- Do not call integration complete without at least one downstream verification step after the write surface.
- Do not let adapter behavior override deployed contract behavior when they conflict.

## Response Contract

When answering or executing, keep this shape:

1. Behavior owner and downstream layers.
2. File plan by repo.
3. ABI, address, viewer, script, and env sync points.
4. End-to-end verification path.
5. Remaining risk or follow-up gaps.

## References

- `references/integration-workflow.md`
- `references/sync-points.md`
