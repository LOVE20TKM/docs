# Core Contract Map

## Timing and shared state

- `core/src/Phase.sol`
  Shared round and phase timing utilities.

## Token creation and assets

- `core/src/LOVE20TokenFactory.sol`
  Creates LOVE20 tokens and wires launch, mint, and stake dependencies.
- `core/src/LOVE20Token.sol`
  Main ERC20 token with `mint`, `burn`, and `burnForParentToken`.
- `core/src/LOVE20SLToken.sol`
  LP-backed staking receipt and liquidity withdrawal accounting.
- `core/src/LOVE20STToken.sol`
  Token-only staking receipt.

## Launch and staking

- `core/src/LOVE20Launch.sol`
  Fair launch, launch eligibility, contribution, withdrawal, claim, and launch indexing.
- `core/src/LOVE20Stake.sol`
  SL and ST staking, unstake request, delayed withdrawal, governance vote tracking.

## Governance and actions

- `core/src/LOVE20Submit.sol`
  Action definitions and per-round submission records.
- `core/src/LOVE20Vote.sol`
  Vote allocation and vote indexing.
- `core/src/LOVE20Join.sol`
  Action participation, verification info, weighted account lists, and random candidate preparation.
- `core/src/LOVE20Random.sol`
  Random seed updates used during verification.
- `core/src/LOVE20Verify.sol`
  Verifier-submitted scores and verifier score accounting.
- `core/src/LOVE20Mint.sol`
  Reward reservation, governance reward minting, action reward minting, burn paths.

## Libraries and support

- `core/src/lib/FenwickTree.sol`
  Weighted index support used by action participation and random selection logic.
- `core/src/lib/ArrayUtils.sol`
  Shared array helpers.

## Recommended interface entry points

- Timing:
  `core/src/interfaces/IPhase.sol`
- Launch:
  `core/src/interfaces/ILOVE20Launch.sol`
- Stake:
  `core/src/interfaces/ILOVE20Stake.sol`
- Submit:
  `core/src/interfaces/ILOVE20Submit.sol`
- Vote:
  `core/src/interfaces/ILOVE20Vote.sol`
- Join:
  `core/src/interfaces/ILOVE20Join.sol`
- Verify:
  `core/src/interfaces/ILOVE20Verify.sol`
- Mint:
  `core/src/interfaces/ILOVE20Mint.sol`
- Token primitives:
  `core/src/interfaces/ILOVE20Token.sol`
  `core/src/interfaces/ILOVE20SLToken.sol`
  `core/src/interfaces/ILOVE20STToken.sol`
