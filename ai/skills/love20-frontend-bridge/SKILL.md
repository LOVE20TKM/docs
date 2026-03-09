---
name: love20-frontend-bridge
description: "Trace LOVE20 frontend behavior to pages, components, hooks, ABIs, viewer contracts, and environment configuration. Use when asked how a LOVE20 UI action works, which contract a page calls, where data is aggregated in the frontend, how extension pages are registered, or how wagmi hooks map to LOVE20 contracts."
---

# LOVE20 Frontend Bridge

Use this skill to trace a LOVE20 screen or component down to the contract and data-loading layer.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/frontend-map.md`.
2. Read `references/data-loading-map.md`.
3. Start from the page route, then descend into components, extension-aware adapters, composite hooks, contract hooks, ABI modules, and configs.
4. Open `interface/docs/extension.md` when the task involves extension UI plugins.

## Working Rules

- Trace reads through `src/hooks/extension`, `src/hooks/composite`, and `src/hooks/contracts` before reading low-level UI code.
- Trace writes through hooks that use `useUniversalTransaction`.
- Use `src/config/extensionConfig.ts` and `.env*` files to understand which extension factories are enabled.
- Treat `NEXT_PUBLIC_TOKEN_PREFIX` as a test-environment hint only. Actual extension UI availability comes from configured factory addresses in env plus `extensionConfig.ts`.
- Use ABI files in `src/abis` and the lazy loader in `src/lib/abiLoader.ts` when the question is about contract surface or bundle behavior.
- If the question becomes "what is the protocol truth" rather than "how does the UI load or send it", route to `docs/ai/skills/love20-state-and-events/SKILL.md` or `docs/ai/skills/love20-core-protocol/SKILL.md`.

## Guardrails

- Treat periphery viewer hooks as aggregated read adapters, not protocol truth.
- Treat deployed contract repos `core`, `extension`, `extension-lp`, `extension-group`, and `group` as the final authority when a frontend trace must be reconciled with real on-chain behavior.
- Distinguish page routing in `src/pages` from reusable components in `src/components`.
- Follow extension flows through the action participation adapter when an action can be either base LOVE20 or extension-backed.
- Use error maps in `src/errors` when explaining frontend failure states.

## References

- `references/frontend-map.md`
- `references/data-loading-map.md`
