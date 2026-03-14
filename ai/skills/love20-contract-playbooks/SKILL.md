---
name: love20-contract-playbooks
description: "Find the LOVE20 contracts, functions, viewers, and cast call/send templates needed for a concrete operation. Use when asked how to launch a token, contribute, claim, stake, request unlock, withdraw staked assets, submit actions, vote, join, verify, mint rewards, burn for parent token, inspect state with viewer contracts, or reuse the existing LOVE20 cast scripts."
---

# LOVE20 Contract Playbooks

Use this skill to turn a LOVE20 user flow into concrete contracts, functions, viewer reads, and reusable `cast call` / `cast send` templates.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/operation-playbooks.md`.
2. Read `references/periphery-and-viewers.md` when convenience contracts or aggregated reads are involved.
3. Read `references/cast-script-index.md` when the task should reuse existing `cast call` / `cast send` shell templates from `script`.
4. Read `references/prerequisites-and-timing.md` when the task depends on phase restrictions, waiting periods, or approvals.
5. Read `references/generated-playbook-index.md` when you need a refreshed contract or script inventory.
6. Open the relevant interface or script file before giving exact call guidance.

## Operation Decision Tree

1. If the user wants reads only, prefer `call` guidance and consider switching to `love20-state-and-events`.
2. Treat unqualified `action` or `行动` as potentially base, extension-backed, or group-backed before naming any function.
3. Determine the write surface before naming any function:
   - launch or claim: `LOVE20Launch` or `LOVE20Hub`
   - stake: `LOVE20Stake` or `LOVE20Hub`
   - base submit, vote, join, verify, mint: core contracts
   - extension join, exit, reward claim: extension contracts
   - group join or trial join: `GroupJoin`
   - group verification or distrust flow: `GroupVerify`
4. Determine whether the action is base or extension-backed before using any join or reward function.
5. Read timing from the target contract you will call. Do not borrow `currentRound()` from a different phase contract.
6. Collect prerequisites before suggesting the write:
   allowance, voted action status, whitelist or extension registration, group membership, `promisedWaitingPhases`, receipt-token balance or unstake status for stake exits, waiting blocks, and verification data shape.

## Working Rules

- Treat `core`, `extension`, `extension-lp`, `extension-group`, and `group` as the highest-priority contract-code sources when the requested operation targets deployed immutable contracts.
- Distinguish core contracts from periphery helpers. Core contracts define the protocol; periphery contracts reduce call friction.
- Prefer direct `cast call` / `cast send` guidance against the target interface or contract.
- Prefer existing scripts in `script/script/cast` over inventing new command sequences, but treat them as executable examples of `cast call` / `cast send`, not as the primary protocol surface.
- Treat helper or wrapped write functions as call examples or convenience fallbacks, not the default recommendation.
- Mention the exact contract surface and whether the step is a read (`call`) or write (`send`) before mentioning frontend hooks or scripts.
- Use viewer contracts for bulk reads and dashboards.
- Use core contracts for base LOVE20 writes and extension or group contracts for extension-backed writes.

## Guardrails

- Do not recommend wrapped helper writes before showing the direct contract surface they ultimately call.
- Use `periphery/src/LOVE20Hub.sol` only when the helper meaningfully reduces multi-step friction such as native-asset wrapping or liquidity assembly.
- Use `periphery/src/LOVE20TokenViewer.sol`, `LOVE20RoundViewer.sol`, and `LOVE20MintViewer.sol` for aggregated reads.
- Keep direct call guidance aligned with `core/src/interfaces/*.sol`.
- If an extension-backed or chain-group-backed action is involved, prefer the corresponding deployed contract repo over helper layers or frontend wiring.
- Do not silently narrow `action` to a base-core action. State when you are classifying it as base, generic extension, LP extension, or chain-group action.
- Translate user phrases such as `解锁期`, `申请解锁`, and `取回质押资产` into the exact stake write or read surfaces before suggesting calls.
- If a user asks for a transaction sequence, state prerequisites such as approvals, phase timing, and waiting blocks.

## Response Contract

For each suggested operation, always include:

1. Target contract and function.
2. Whether it is a read or write.
3. Required parameters and what each parameter represents.
4. Required approvals or assets.
5. Timing or eligibility preconditions.
6. One confirmation read the agent should check after the write.

## References

- `references/operation-playbooks.md`
- `references/periphery-and-viewers.md`
- `references/cast-script-index.md`
- `references/prerequisites-and-timing.md`
- `references/generated-playbook-index.md`
- `scripts/generate_playbook_index.py`
