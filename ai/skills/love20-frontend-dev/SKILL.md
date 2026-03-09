---
name: love20-frontend-dev
description: "Implement or modify LOVE20 frontend pages, components, hooks, ABIs, extension registration, and transaction flows. Use when asked to build a new LOVE20 UI feature, wire a new extension or derivative protocol into the dApp, add routes or hooks, update env-configured addresses, or carry a frontend change through read and write verification."
---

# LOVE20 Frontend Development

Use this skill when the task is to build or modify LOVE20 frontend behavior, not just trace an existing page.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/dev-workflow.md`.
2. Read `references/read-write-and-registration.md`.
3. Start from the route, page cluster, or extension plugin that is closest to the requested feature.
4. Split the work into read path, write path, and config gating before editing.
5. Open the deployed contract repo only when frontend behavior depends on contract truth or a new ABI surface.

## Mandatory Triage

Before editing, classify the task on these axes:

1. Is this base LOVE20 UI, or an extension or group plugin flow?
2. Is the change read-only, write-only, or both?
3. Is it a new route, a new extension plugin, or a modification of an existing component and hook chain?
4. Do ABI, address, env, or factory-registration changes need to ship with it?
5. Does the task end at build verification, or must it include a concrete transaction or page-state acceptance path?

If the first step is understanding an existing flow, pair this skill with `love20-frontend-bridge`.

## Working Rules

- Start from an existing page, hook, and plugin pattern instead of inventing a new frontend structure.
- Trace reads through `src/hooks/composite`, `src/hooks/contracts`, and `src/hooks/extension` before patching UI state directly.
- Route writes through hooks that use `useUniversalTransaction`.
- Keep extension registration in sync across env, `src/config/extensionConfig.ts`, deploy UI, public tabs, join panel, and my-participation surfaces.
- Keep ABI source, contract hook, and configured address changes aligned in one pass.
- Treat `interface` as the adapter layer. When frontend expectations and contract behavior disagree, reconcile against the deployed contract repo.

## Guardrails

- Do not hardcode addresses in components when env or config already owns that decision.
- Do not add extension UI without trusted factory gating.
- Do not add UI-only validation that contradicts contract behavior.
- Do not stop at a component rename when the hook, ABI, and invalidation path also need changes.
- Do not call a frontend task complete without naming the build command or acceptance path used to verify it.

## Response Contract

When answering or executing, keep this shape:

1. Route or feature entry point.
2. File plan by page, component, hook, and config.
3. Read path and write path changes.
4. ABI, address, and extension-registration updates.
5. Build and acceptance checks.

## References

- `references/dev-workflow.md`
- `references/read-write-and-registration.md`
