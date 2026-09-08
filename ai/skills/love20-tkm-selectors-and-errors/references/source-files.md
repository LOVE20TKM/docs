# Source Files

## Function selectors

- `interface-test/scripts/generateFunctionSelectors.ts`
  Frontend generator that computes the selector catalog from ABI TypeScript modules.
- `interface-test/docs/function-selectors.json`
  Generated selector output used for reverse lookup. When current, it should include the ABI modules in `interface-test/src/abis`, including extension, group, and group-chat contracts that have been mirrored into the frontend.
- `interface-test/src/abis`
  ABI TypeScript source modules that feed selector generation.

## Custom error decoding

- `interface-test/scripts/generateErrorSelectors.ts`
  Frontend generator that builds the unified selector and name maps.
- `interface-test/src/errors/errorMessages.ts`
  Maintained Chinese translation source.
- `interface-test/src/errors/unifiedErrorMap.ts`
  Generated frontend selector and name lookup table.
- `interface-test/src/errors/contractErrorParser.ts`
  Runtime parser that extracts selectors, names, gas errors, RPC errors, and cancellation cases.

## ABI source of truth for errors and events

- `script/abi`
  JSON ABI mirror for LOVE20, extension, group, ERC, WETH, and Uniswap interfaces.
- `*Errors.json`
  Custom error ABI subsets.
- `*Events.json`
  Event ABI subsets.
- `group-chat/src/interfaces/IGroupChat.sol`
  Primary ABI, event, and error source for GroupChat when generated mirrors do not yet include group-chat.

## Event topic calculation

- `script/calculate_event_topics.py`
  Manual event-topic calculation helper using keccak.

## Practical guidance

- Use `interface-test` generated files for active development and public-test debugging. Use the equivalent `interface` files only for the released production dApp.
- If a selector is missing for a contract that already exists in `interface-test/src/abis`, refresh the frontend-generated catalog before assuming the selector is unavailable.
- Use the script ABI JSON files when you need a repo-neutral ABI mirror that spans core, extension, and group contracts.
- Use `group-chat/src/interfaces/*.sol` directly when decoding group-chat selectors, errors, or events that have not yet been mirrored into frontend or script ABI catalogs.
- Use contract source for the final declaration site of the deployed instance. For group-chat, match the address to the latest pilot deployment before choosing the ABI.
- If selectors conflict across multiple contracts, use transaction calldata context, contract address, or frontend hook path to disambiguate.
