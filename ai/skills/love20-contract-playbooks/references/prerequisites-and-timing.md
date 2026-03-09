# Prerequisites and Timing

## General

- Most LOVE20 writes are phase-sensitive because core contracts inherit `IPhase`.
- The current round comes from `currentRound()` on the relevant phase-aware contract.
- `currentRound()` is contract-local. Read it from the contract you are about to call, not from a different phase contract.
- Core deployment offsets the phase contracts by one phase each:
  - submit and vote start at `T0`
  - join and random start at `T0 + phaseBlocks`
  - verify starts at `T0 + 2 * phaseBlocks`
- At the same wall-clock block, submit and vote round `r` aligns with join and random round `r - 1`, and verify round `r - 2`.
- A script or frontend flow should read eligibility before sending a write whenever the interface exposes it.

## Launch

- `launchToken` is gated by launch eligibility and child-launch quotas.
- `withdraw` during fair launch is subject to waiting blocks after contribution.
- `claim` requires launch end plus the one-block claim delay in `ILOVE20Launch`.
- Contribute flows require allowance on the parent token unless a helper like `LOVE20Hub` wraps native ETH for you.

## Stake

- `stakeLiquidity` and `stakeToken` are not valid at round zero.
- `promisedWaitingPhases` must stay within min and max bounds and cannot decrease across later stakes for the same account/token.
- `unstake` starts a delayed exit flow; `withdraw` is only valid after the waiting period is fully satisfied.
- Losing or transferring away SL or ST receipt tokens can disable governance or delay exits, because receipt balance matters to effective status.

## Submit and vote

- `canSubmit` should be checked before action creation or submission.
- Each eligible governor can submit only within the round constraints enforced by `LOVE20Submit`.
- `vote` is bounded by `maxVotesNum` and can fail if action eligibility or remaining votes are insufficient.

## Join and verification

- Joining late in the phase is blocked by `JOIN_END_PHASE_BLOCKS`.
- Base-action joining requires the action to have been voted and can also be constrained by action whitelist and minimum stake.
- Generic extension joins can call `initializeIfNeeded()` on first use. That initialization discovers the extension-backed action from the current voted action set and registers it in `ExtensionCenter`, so it can fail if the action is not yet active in the current join round.
- Group-action joins go through `GroupJoin`, not `LOVE20Join`, and add `extension` and `groupId` to the write parameters.
- Verification depends on prepared random-account sets and only makes sense for actions the verifier supported.
- Verification scores must satisfy the monotonic or bound checks enforced by `LOVE20Verify`.

## Reward minting

- Reward mints require the round to be ready and reward state to be prepared.
- Governance reward and action reward mint paths track whether a user has already minted for that round.
- Boost or action overflow can be burned instead of minted under LOVE20 reward rules.

## Practical approval checklist

- Launch contribution:
  approve parent token unless using native helper flow.
- Stake liquidity:
  approve both token and parent token, or follow the helper contract flow.
- Stake token:
  approve token.
- Join base action:
  approve action token.
- Join generic token-based extension action:
  approve the extension contract's `JOIN_TOKEN_ADDRESS`.
- LP extension join:
  approve LP token.
- Group action join:
  approve the group action's join token to `GroupJoin`.
- Group service join:
  no join-token approval by default, but the caller still needs whatever extension-specific eligibility the contract enforces, such as active groups.
- Burn for parent token:
  approve or hold enough LOVE20 token balance, then call `burnForParentToken`.
