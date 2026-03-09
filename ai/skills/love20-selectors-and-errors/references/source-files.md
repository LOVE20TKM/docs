# Source Files

## Function selectors

- `interface/scripts/generateFunctionSelectors.ts`
  Frontend generator that computes the selector catalog from ABI TypeScript modules.
- `interface/docs/function-selectors.json`
  Generated selector output used for reverse lookup. When current, it should include the ABI modules in `interface/src/abis`, including extension and group contracts.
- `interface/src/abis`
  ABI TypeScript source modules that feed selector generation.

## Custom error decoding

- `interface/scripts/generateErrorSelectors.ts`
  Frontend generator that builds the unified selector and name maps.
- `interface/src/errors/errorMessages.ts`
  Maintained Chinese translation source.
- `interface/src/errors/unifiedErrorMap.ts`
  Generated frontend selector and name lookup table.
- `interface/src/errors/contractErrorParser.ts`
  Runtime parser that extracts selectors, names, gas errors, RPC errors, and cancellation cases.

## ABI source of truth for errors and events

- `script/abi`
  JSON ABI mirror for LOVE20, extension, group, ERC, WETH, and Uniswap interfaces.
- `*Errors.json`
  Custom error ABI subsets.
- `*Events.json`
  Event ABI subsets.

## Event topic calculation

- `script/calculate_event_topics.py`
  Manual event-topic calculation helper using keccak.

## Practical guidance

- Use the frontend-generated files when debugging what the UI is already using.
- If a selector is missing for a contract that already exists in `interface/src/abis`, refresh the frontend-generated catalog before assuming the selector is unavailable.
- Use the script ABI JSON files when you need a repo-neutral ABI mirror that spans core, extension, and group contracts.
- Use `core`, `extension`, `extension-lp`, `extension-group`, and `group` source files when you need the final declaration site for deployed immutable contracts.
- If selectors conflict across multiple contracts, use transaction calldata context, contract address, or frontend hook path to disambiguate.
