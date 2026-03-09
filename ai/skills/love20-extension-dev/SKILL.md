---
name: love20-extension-dev
description: "Implement LOVE20 extension or derivative protocol contracts, factories, tests, and integration wiring. Use when asked to build a new extension, scaffold a derivative protocol, add or modify a factory, write extension tests, wire ExtensionCenter registration, or carry an extension change through contract, script, and frontend handoff."
---

# LOVE20 Extension Development

Use this skill when the task is to ship an extension or derivative protocol change, not just explain how the extension framework works.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/dev-workflow.md`.
2. Read `references/contract-and-test-checklist.md`.
3. Pick the closest existing implementation before changing code:
   - `extension` for base classes, shared registry, and minimal examples
   - `extension-lp` for token-amount joins and LP reward accounting
   - `extension-group` for chain-group-backed join, verify, and factory flows
4. Open the concrete contract, factory, deploy script, and tests that most closely match the requested change.
5. Open frontend extension notes only if the task includes dApp wiring.

## Mandatory Triage

Before editing, classify the task on these axes:

1. Is this a new extension type, or a modification of LP/group/general extension behavior?
2. Is the action participant the extension contract itself, or the end user through group/helper flows?
3. Which base class is closest: `ExtensionBaseReward`, `ExtensionBaseRewardJoin`, or `ExtensionBaseRewardTokenJoin`?
4. Does the public surface change require updates to factory, interface, deploy script, tests, or frontend plugin wiring?
5. Is the request asking for generic design guidance, or for concrete code changes that must compile and test?

If base-class choice is still unclear, pair this skill with `love20-extension-patterns` first.

## Working Rules

- Start from the closest deployed example instead of inventing a new abstraction tree.
- Settle the participant model and join model before writing code.
- Keep `initializeIfNeeded()` and `registerActionIfNeeded()` explicit whenever action-bound state or membership tracking is involved.
- Route account add, remove, and verification-info writes through `ExtensionCenter` when the chosen base pattern expects it.
- When a public surface changes, update contract, factory, script, test, and frontend handoff points in the same pass.
- Use tests as the release gate. A design that is not backed by happy-path and negative-path tests is not finished.
- Treat `extension`, `extension-lp`, `extension-group`, and `group` as behavior truth. Treat frontend files as adapters around that truth.

## Guardrails

- Do not explain an implementation task at architecture level only. Name the exact file clusters to edit.
- Do not choose a low-level base class if a higher-level join base already matches the user flow.
- Do not forget the extension self-join initialization requirement when the extension contract is the whitelist participant.
- Do not add a new write surface without also naming the tests and post-deploy state reads that prove it works.
- Do not move to frontend wiring before the contract interface and factory surface are settled.

## Response Contract

When answering or executing, keep this shape:

1. Scope and closest existing implementation.
2. File plan by repo.
3. Contract and factory changes.
4. Test plan and acceptance checks.
5. Deploy, frontend handoff, or integration notes if needed.

## References

- `references/dev-workflow.md`
- `references/contract-and-test-checklist.md`
