# Extension Framework

## Mental model

- A LOVE20 extension becomes the participant of a whitelist-restricted action.
- The action reward is minted to the extension flow first.
- The extension then redistributes or burns that reward according to its own rules.

## Core files

- `extension/README.md`
  High-level framework notes.
- `extension/src/interface/IExtension.sol`
  Minimal extension identity and initialization surface.
- `extension/src/interface/IReward.sol`
  Reward claim and burn surface.
- `extension/src/interface/IJoin.sol`
  No-token join surface.
- `extension/src/interface/ITokenJoin.sol`
  Token-backed join surface.
- `extension/src/interface/IExtensionCenter.sol`
  Shared account and verification-info registry.
- `extension/src/interface/IExtensionFactory.sol`
  Factory registry surface.

## Source-of-truth position

- Use `extension` to understand the reusable framework contracts and base classes.
- Use `extension-lp` and `extension-group` to understand concrete deployed extension behavior.
- Use `group` when the question depends on chain-group NFT ownership, naming, transfer, or holder semantics.
- Do not treat frontend extension wiring or helper scripts as a higher-priority source than these deployed contract repos.

## Base class selection

- `ExtensionBase`
  Use for low-level extension identity and initialization only.
- `ExtensionBaseReward`
  Use when reward logic is needed but join and exit are fully custom.
- `ExtensionBaseRewardJoin`
  Use for extensions that only track membership, not token amounts.
- `ExtensionBaseRewardTokenJoin`
  Use for extensions that track a join token amount per account.

## Mandatory flow

1. Create the concrete extension contract and factory.
2. Register the action through `ExtensionCenter.registerActionIfNeeded`.
3. Route account add, remove, and verification-info updates through `ExtensionCenter`.
4. Call `initializeIfNeeded()` before depending on action-bound state.
5. Claim or burn extension rewards through the `IReward` surface.

## Integration notes

- Frontends should trust known factory addresses, not arbitrary extension addresses.
- The extension contract address is the action whitelist target.
- The framework README notes that a concrete extension may need one token transferred in for `initializeIfNeeded` to join the action on behalf of the extension.
