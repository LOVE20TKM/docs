---
name: love20-tkm-selectors-and-errors
description: "Decode LOVE20 function selectors, custom errors, event topics, and frontend error mappings. Use to identify a 4-byte value or topic, candidate contracts, declaration files, ABI signatures, or the Chinese message produced by the frontend parser."
---

# LOVE20 Selectors and Errors

Use this skill for debugging and reverse lookup tasks around selectors, topics, and error decoding.

## Workflow

1. Read `references/decoding-workflow.md`.
2. Read `references/source-files.md` to locate the authoritative selector or error source.
3. Read only the generated reference you need:
   - `references/generated-function-selector-index.md`
   - `references/generated-error-selector-index.md`
   - `references/generated-event-topic-index.md`
4. Open the matching ABI, interface, or frontend parser file only after you know the likely contract or symbol.
5. Regenerate the indexes with `python3 ai/skills/love20-tkm-selectors-and-errors/scripts/generate_selector_indexes.py` after frontend selector, error-map, or script ABI sources change.

## Decode Decision Tree

1. Classify the symbol first:
   function selector, custom error selector, event topic0, or frontend error message.
2. Check whether the generated catalog is current before trusting a "not found" result.
3. If multiple contracts share the same signature, use calldata context, contract address, repo, or hook path to narrow candidates.
4. Separate three layers:
   - ABI declaration
   - deployed contract declaration site
   - frontend translation layer

## Working Rules

- Treat `interface-test/docs/function-selectors.json` as the active frontend selector catalog across core, extension, group, and group-chat ABI modules.
- Treat `script/abi/**/*Errors.json` as the repo-neutral ABI mirror used for custom error decoding.
- Treat `script/abi/**/*Events.json` as the repo-neutral ABI mirror used for topic decoding.
- Treat contract source as the final declaration authority for the deployed instance. For group-chat, confirm that the address belongs to the latest pilot deployment before decoding against its ABI.
- Treat `interface-test/src/errors/contractErrorParser.ts` and `unifiedErrorMap.ts` as the active frontend decoding layer, not the origin of the ABI itself.
- When multiple contracts share the same selector because they share a signature, say so explicitly and list the candidate contracts.

## Guardrails

- Distinguish function selectors, custom error selectors, and event topic0 values. They are all keccak-derived but used differently.
- If a selector is missing for a contract that exists in `interface-test/src/abis`, regenerate the catalog before concluding the selector is absent.
- If a group-chat selector or topic is missing from frontend or script-generated catalogs, check `group-chat/src/interfaces/IGroupChat.sol` before concluding it is absent.
- For errors, separate:
  - raw selector and signature
  - frontend message mapping
  - where the error is declared in LOVE20 ABI sources
- For events, call out indexed parameters because they explain which values land in topics beyond topic0.
- If a selector or topic is not in the generated references, check whether the source is an inherited ERC20/ERC721/Uniswap interface rather than a LOVE20-specific contract.

## Response Contract

When answering, list:

1. Raw selector or topic.
2. Decoded signature.
3. Candidate contracts.
4. Final declaration file or ABI source.
5. Frontend message mapping only if the question is UI-facing.
