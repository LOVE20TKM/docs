---
name: love20-navigator
description: "Navigate LOVE20 documentation and related repositories across docs, core, periphery, script, extension, extension-lp, extension-group, group, and interface. Use when asked what a LOVE20 concept means, how phase and round concepts should be interpreted, which repo or file is authoritative, how protocol terms map to code, where to start reading, or how to find the correct LOVE20 source quickly."
---

# LOVE20 Navigator

Use this skill to choose the right LOVE20 source before answering in detail.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/source-of-truth.md`.
2. Read `references/repo-index.md`.
3. Read `references/glossary.md` only when the question depends on LOVE20-specific terms.
4. Open only the repo or document that the reference files point to. Do not bulk-read every LOVE20 repo.

## Mandatory Triage

Before routing, classify the request on these axes:

1. Intent: explain, operate, inspect state, decode, debug, develop, integrate, validate, release, or update docs.
2. Surface: base LOVE20, extension, extension-lp, extension-group, group, or frontend adapter.
3. Timing: business round in the whitepaper, or contract-local `currentRound()` on a named contract.
4. Authority: design intent, deployed contract behavior, adapter behavior, or indexed history.
5. Horizon: current truth now, or historical timeline over logs and SQL.

If any axis is ambiguous, say which assumption you are making before routing deeper.

## Routing

- Continue with `docs/ai/skills/love20-core-protocol/SKILL.md` for protocol mechanics, round flow, staking, submit-and-vote flow, verification, or minting questions.
- Continue with `docs/ai/skills/love20-contract-playbooks/SKILL.md` for concrete calls, scripts, viewer contracts, or step-by-step interaction tasks.
- Continue with `docs/ai/skills/love20-extension-patterns/SKILL.md` for extension, LP extension, or chain-group extension design and behavior questions.
- Continue with `docs/ai/skills/love20-extension-dev/SKILL.md` for implementing or modifying extension, LP extension, chain-group extension, or derivative protocol contracts, factories, tests, or integration wiring.
- Continue with `docs/ai/skills/love20-frontend-bridge/SKILL.md` for UI, wagmi hooks, ABI loading, or frontend tracing.
- Continue with `docs/ai/skills/love20-frontend-dev/SKILL.md` for building or modifying LOVE20 pages, components, hooks, extension registration, or transaction flows.
- Continue with `docs/ai/skills/love20-integration-dev/SKILL.md` for cross-repo wiring across contracts, viewers, scripts, env files, and frontend hooks.
- Continue with `docs/ai/skills/love20-state-and-events/SKILL.md` for viewer reads, hook-to-contract tracing, SQL views, event indexing, or state lookup tasks.
- Continue with `docs/ai/skills/love20-selectors-and-errors/SKILL.md` for selector decoding, event topic lookup, custom error mapping, or frontend error translation questions.
- Continue with `docs/ai/skills/love20-runbooks/SKILL.md` for troubleshooting, failure classification, shortest debug path, or "what should I check first" requests.
- Continue with `docs/ai/skills/love20-test-and-release/SKILL.md` for test planning, regression scope, deployment checks, release signoff, or post-release verification.
- Continue with `docs/ai/skills/love20-prompts/SKILL.md` when the user wants to rewrite, split, or tighten a LOVE20 prompt for another AI agent.
- For "what phase is this" or "how is round computed" questions, start with `docs/ai/skills/love20-core-protocol/SKILL.md`, then use `docs/ai/skills/love20-state-and-events/SKILL.md` if the issue is about viewer data or indexed history.

## Guardrails

- Treat `docs/whitepaper/*.md` as design intent and terminology.
- Treat `core`, `extension`, `extension-lp`, `extension-group`, and `group` source files as the highest-priority on-chain behavior sources because they correspond to deployed immutable contracts.
- Treat periphery, scripts, and frontend code as adapters around the core protocol, not the primary behavioral source.
- Prefer normal source files over `core/src/merged/*.sol`.
- If a question says only "round" or "phase", force the distinction between business round and contract-local round before continuing.
- If a question says only "join" or "claim", determine whether the write surface is base LOVE20, extension, or group helper before routing to an interaction skill.
- When docs and code diverge, state the divergence explicitly and separate documented design from implemented behavior.

## References

- `references/source-of-truth.md`
- `references/repo-index.md`
- `references/glossary.md`
