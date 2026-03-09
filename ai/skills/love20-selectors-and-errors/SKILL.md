---
name: love20-selectors-and-errors
description: "Decode LOVE20 function selectors, custom error selectors, event topics, and frontend error mappings across interface, script, core, periphery, extension, and group repos. Use when asked what a 4-byte selector or topic means, which contract emitted an event, which custom error a revert corresponds to, how the frontend turns raw errors into Chinese messages, or how to trace ABI signatures back to LOVE20 code."
---

# LOVE20 Selectors and Errors

Use this skill for debugging and reverse lookup tasks around selectors, topics, and error decoding.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/decoding-workflow.md`.
2. Read `references/source-files.md` to locate the authoritative selector or error source.
3. Read only the generated reference you need:
   - `references/generated-function-selector-index.md`
   - `references/generated-error-selector-index.md`
   - `references/generated-event-topic-index.md`
4. Open the matching ABI, interface, or frontend parser file only after you know the likely contract or symbol.

## Working Rules

- Treat `interface/docs/function-selectors.json` as the generated function-selector catalog for frontend ABI modules across core, extension, extension-group, and group contracts.
- Treat `script/abi/**/*Errors.json` as the repo-neutral ABI mirror used for custom error decoding.
- Treat `script/abi/**/*Events.json` as the repo-neutral ABI mirror used for topic decoding.
- Treat `core`, `extension`, `extension-lp`, `extension-group`, and `group` as the final authority when you need to confirm where a selector, error, or event is originally declared for deployed immutable contracts.
- Treat `interface/src/errors/contractErrorParser.ts` and `unifiedErrorMap.ts` as the frontend decoding layer, not the origin of the ABI itself.
- When multiple contracts share the same selector because they share a signature, say so explicitly and list the candidate contracts.

## Guardrails

- Distinguish function selectors, custom error selectors, and event topic0 values. They are all keccak-derived but used differently.
- If a selector is missing from `function-selectors.json` for a contract that clearly exists in `interface/src/abis`, treat the generated catalog as stale and regenerate it before concluding the selector is absent.
- For errors, separate:
  - raw selector and signature
  - frontend message mapping
  - where the error is declared in LOVE20 ABI sources
- For events, call out indexed parameters because they explain which values land in topics beyond topic0.
- If a selector or topic is not in the generated references, check whether the source is an inherited ERC20/ERC721/Uniswap interface rather than a LOVE20-specific contract.

## References

- `references/decoding-workflow.md`
- `references/source-files.md`
- `references/generated-function-selector-index.md`
- `references/generated-error-selector-index.md`
- `references/generated-event-topic-index.md`
- `scripts/generate_selector_indexes.py`
