# Decoding Workflow

## Function selector

Use this path when you have a 4-byte selector such as `0x823ed39d`.

1. Search `generated-function-selector-index.md`.
2. Confirm the candidate contract in `interface/docs/function-selectors.json`.
3. If a known ABI family such as extension, extension-group, or group is missing from the generated catalog, regenerate `function-selectors.json` before concluding the selector is absent.
4. Open the matching ABI module in `interface/src/abis`.
5. Confirm the matching Solidity interface or implementation in `core`, `extension`, `extension-lp`, `extension-group`, or `group` when the selector belongs to a deployed immutable contract.

## Custom error selector

Use this path when you have a revert selector such as `0xa748da06` or a decoded error name.

1. Search `generated-error-selector-index.md`.
2. If you only have a frontend message, open:
   - `interface/src/errors/contractErrorParser.ts`
   - `interface/src/errors/unifiedErrorMap.ts`
3. Confirm the ABI mirror entry in `script/abi/**/*Errors.json`.
4. Open the original Solidity interface or implementation in `core`, `extension`, `extension-lp`, `extension-group`, or `group` to confirm where the error is actually declared.

## Event topic

Use this path when you have a log topic0 such as `0xddf252ad...`.

1. Search `generated-event-topic-index.md`.
2. Confirm the event ABI in `script/abi/**/*Events.json`.
3. Explain indexed vs non-indexed parameters so the log structure is clear.
4. Confirm the original event declaration in the deployed contract repo when the topic belongs to LOVE20, extension, or group contracts. If it is not LOVE20-specific, check inherited ERC20, ERC721, WETH, or Uniswap ABIs.

## Frontend error decoding

Use this path when the user asks why the UI shows a specific Chinese message.

1. Open `interface/src/errors/contractErrorParser.ts`.
2. Open `interface/src/errors/unifiedErrorMap.ts`.
3. Open `interface/src/errors/errorMessages.ts` if you need the maintained source for the Chinese translation text.
4. Mention whether the message came from:
   - custom error selector lookup
   - error name lookup
   - RPC or gas heuristic
   - user cancellation handling
