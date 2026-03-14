---
name: love20-core-protocol
description: "Explain LOVE20 core protocol mechanics and map them to the core contracts and whitepaper. Use when asked about fair launch, parent and child token rules, SL and ST staking, SL 解锁期 or unlock period, 申请解锁, 取回质押资产, governance rounds, action submission, voting, joining, random verification, reward minting, or how LOVE20 rules are implemented on-chain."
---

# LOVE20 Core Protocol

Use this skill to explain LOVE20 as a state machine backed by focused core contracts.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/protocol-overview.md`.
2. Read `references/governance-lifecycle.md` when the question spans multiple phases or rounds.
3. Read `references/core-contract-map.md` to map concepts to files and interfaces.
4. Read `references/core-data-structures.md` when structs, return shapes, or storage-facing payloads matter.
5. Read `references/generated-interface-index.md` when you need a refreshed function inventory.
6. Open only the interfaces and implementations needed for the answer.

## Mandatory Triage

Before explaining a mechanism, answer these questions explicitly in your head:

1. Is this base LOVE20 behavior, or does extension or group logic change it?
2. Does "round" mean the whitepaper business round, or `currentRound()` on a specific contract?
3. Is the user asking for design intent, implemented behavior, or both?
4. Which contract actually owns the rule being described?
5. Does the answer need current-state eligibility, or only abstract mechanics?
6. Is the user using whitepaper terms such as `解锁期`, `申请解锁`, or `取回质押资产` that must be translated into `LOVE20Stake` parameters or exit steps?

If the topic is concrete interaction rather than mechanism, switch to `love20-contract-playbooks`.

## Working Rules

- Start from the whitepaper semantics in `docs/whitepaper/LOVE20协议设计.md`, then verify against `core/src/interfaces`.
- Translate whitepaper staking terms into on-chain stake vocabulary when relevant:
  - `解锁期` -> `promisedWaitingPhases`
  - `申请解锁` -> `unstake`
  - `取回质押资产` -> `withdraw`
- When extension-backed or chain-group-backed behavior matters, prioritize the deployed-contract repos `extension`, `extension-lp`, `extension-group`, and `group` over adapters.
- Separate launch-time behavior from governance-time behavior.
- Map every user-visible action to a contract: `Launch`, `Stake`, `Submit`, `Vote`, `Join`, `Random`, `Verify`, `Mint`, `Token`, `TokenFactory`.
- Mention contract dependencies when they matter. `Verify` depends on `Join`, `Vote`, and `Random`; `Mint` depends on `Vote`, `Verify`, and `Stake`.
- Prefer interface files for public surface area and implementation files for edge cases or state transitions.

## Guardrails

- Treat `Phase.currentRound()` as a contract-local timing primitive. Always name the contract whose round you mean.
- Treat deployment `originBlocks` offsets as part of the timing backbone. Submit and vote, join and random, and verify do not share the same origin block.
- Do not explain SL staking or unlock eligibility with whitepaper language alone. Name the on-chain waiting-period parameter, the delayed exit stages, and the receipt-token balance caveat when they matter.
- Treat `LOVE20TokenFactory` and `LOVE20Launch` as the token tree entry point.
- Treat `LOVE20Token`, `LOVE20SLToken`, and `LOVE20STToken` as asset primitives, not governance flow contracts.
- Call out when a constant is documented in the whitepaper but not exposed by the interface you are citing.

## Response Contract

When answering, prefer this order:

1. Scope sentence: base-only or extension-aware.
2. Round sentence: business round or contract-local round on which contract.
3. Rule owner: name the contract or interface that enforces the behavior.
4. Dependency sentence: note any dependent contracts such as `Vote`, `Join`, `Random`, `Verify`, or `Mint`.
5. Exception sentence: mention extension or group exceptions when they materially change the base rule.

## References

- `references/protocol-overview.md`
- `references/governance-lifecycle.md`
- `references/core-contract-map.md`
- `references/core-data-structures.md`
- `references/generated-interface-index.md`
- `scripts/generate_interface_index.py`
