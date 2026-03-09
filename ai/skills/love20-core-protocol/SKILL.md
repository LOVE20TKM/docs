---
name: love20-core-protocol
description: "Explain LOVE20 core protocol mechanics and map them to the core contracts and whitepaper. Use when asked about fair launch, parent and child token rules, SL and ST staking, governance rounds, action submission, voting, joining, random verification, reward minting, or how LOVE20 rules are implemented on-chain."
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

## Working Rules

- Start from the whitepaper semantics in `docs/whitepaper/LOVE20协议设计.md`, then verify against `core/src/interfaces`.
- When extension-backed or chain-group-backed behavior matters, prioritize the deployed-contract repos `extension`, `extension-lp`, `extension-group`, and `group` over adapters.
- Separate launch-time behavior from governance-time behavior.
- Map every user-visible action to a contract: `Launch`, `Stake`, `Submit`, `Vote`, `Join`, `Random`, `Verify`, `Mint`, `Token`, `TokenFactory`.
- Mention contract dependencies when they matter. `Verify` depends on `Join`, `Vote`, and `Random`; `Mint` depends on `Vote`, `Verify`, and `Stake`.
- Prefer interface files for public surface area and implementation files for edge cases or state transitions.

## Guardrails

- Treat `Phase.currentRound()` as a contract-local timing primitive. Always name the contract whose round you mean.
- Treat deployment `originBlocks` offsets as part of the timing backbone. Submit and vote, join and random, and verify do not share the same origin block.
- Treat `LOVE20TokenFactory` and `LOVE20Launch` as the token tree entry point.
- Treat `LOVE20Token`, `LOVE20SLToken`, and `LOVE20STToken` as asset primitives, not governance flow contracts.
- Call out when a constant is documented in the whitepaper but not exposed by the interface you are citing.

## References

- `references/protocol-overview.md`
- `references/governance-lifecycle.md`
- `references/core-contract-map.md`
- `references/core-data-structures.md`
- `references/generated-interface-index.md`
- `scripts/generate_interface_index.py`
