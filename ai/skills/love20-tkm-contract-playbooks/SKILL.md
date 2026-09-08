---
name: love20-tkm-contract-playbooks
description: "Map concrete LOVE20 operations to contracts, functions, viewers, prerequisites, and cast templates. Use for launch, contribute, claim, stake, unlock, submit, vote, join, verify, mint, burn to parent, default group identity, group-chat activation or posting, viewer reads, and reusable interaction scripts."
---

# LOVE20 Contract Playbooks

Use this skill to turn a LOVE20 user flow into concrete contracts, functions, viewer reads, and reusable `cast call` / `cast send` templates.

## Workflow

1. Read `references/operation-playbooks.md`.
2. Read `references/periphery-and-viewers.md` when convenience contracts or aggregated reads are involved.
3. Read `references/cast-script-index.md` when the task should reuse existing `cast call` / `cast send` shell templates from `script`.
4. Read `references/prerequisites-and-timing.md` when the task depends on phase restrictions, waiting periods, or approvals.
5. Read `references/generated-playbook-index.md` when you need a refreshed contract or script inventory. Regenerate it with `python3 ai/skills/love20-tkm-contract-playbooks/scripts/generate_playbook_index.py` after its sources change.
6. Open the relevant interface or script file before giving exact call guidance.

## Operation Decision Tree

1. If the user wants reads only, prefer `call` guidance and consider switching to `love20-tkm-state-and-events`.
2. Treat unqualified `action` or `行动` as potentially base, extension-backed, or group-backed before naming any function.
3. Determine the write surface before naming any function:
   - launch or claim: `LOVE20Launch` or `LOVE20Hub`
   - stake: `LOVE20Stake` or `LOVE20Hub`
   - base submit, vote, join, verify, mint: core contracts
   - extension join, exit, reward claim: extension contracts
   - group join or trial join: `GroupJoin`
   - group verification or distrust flow: `GroupVerify`
   - default group identity: `GroupDefaults`
   - group chat activation, rule slots, posting, and message reads: `GroupChat`
4. Determine whether the action is base or extension-backed before using any join or reward function.
5. Read timing from the target contract you will call. Do not borrow `currentRound()` from a different phase contract.
6. Collect prerequisites before suggesting the write:
   allowance, voted action status, whitelist or extension registration, group membership, `promisedWaitingPhases`, receipt-token balance or unstake status for stake exits, waiting blocks, and verification data shape.

## Working Rules

- Treat contract source as the highest-priority behavior source for the deployed instance. During the group-chat pilot, use the latest deployment addresses; the instance is immutable but the suite may be replaced without historical compatibility after testing.
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
