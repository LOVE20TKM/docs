# Protocol Overview

## System outline

- LOVE20 starts from a root token and expands into a parent-child token tree.
- Each token has a maximum supply of 10 billion.
- The first 10 percent is minted through fair launch.
- The remaining 90 percent is minted through recurring governance rewards and action rewards.

## Fair launch

- The main design source is `docs/whitepaper/LOVE20协议设计.md`.
- On-chain entry points live in `core/src/interfaces/ILOVE20Launch.sol`.
- Child token creation goes through `launchToken(symbol, parentTokenAddress)`.
- Contributions go through `contribute(tokenAddress, parentTokenAmount, to)`.
- Users can `withdraw(tokenAddress)` before launch end, subject to waiting rules.
- Users can `claim(tokenAddress)` after launch end and the one-block claim delay.
- The token tree is created by `core/src/LOVE20TokenFactory.sol`.

## Governance cycle

- Timing backbone:
  `core/src/interfaces/IPhase.sol`
- The whitepaper describes three equal phases per business round:
  - submit and vote
  - action
  - verify
- The docs state one phase is 30126 blocks and rounds overlap like a pipeline.
- On-chain, each phase-aware contract exposes its own `currentRound()`. That value is contract-local and advances every `phaseBlocks` from that contract's `originBlocks`.
- Deployment aligns the rolling pipeline by offsetting `originBlocks`:
  - `LOVE20Stake`, `LOVE20Submit`, `LOVE20Vote` start at deployment block
  - `LOVE20Join`, `LOVE20Random` start one phase later
  - `LOVE20Verify` starts two phases later
- At the same wall-clock block, submit and vote may be on round `r`, join and random on round `r - 1`, and verify on round `r - 2`. Do not assume the same numeric round across contracts without translating the phase offset.
- Submit and vote decide which actions enter the round and how governance weight is allocated.
- Action phase lets participants stake into voted actions.
- Verify phase lets governors score randomly selected participants.
- Reward minting happens after verification is ready.

## Roles and stake primitives

- Governors obtain governance power through SL staking in `LOVE20Stake`.
- Governance vote count comes from LP-backed stake and promised waiting phases.
- Governors can add ST stake for boost rewards, but ST does not create governance eligibility on its own.
- For base LOVE20 actions, participants hold the action token and join through `LOVE20Join`.
- Extension-backed actions can replace that rule with extension-specific entry conditions such as a separate join token, LP position requirements, or active chain-group membership.

## Action lifecycle

- `LOVE20Submit`: create new action definitions or nominate existing actions.
- `LOVE20Vote`: allocate governance votes across nominated actions.
- `LOVE20Join`: join a base action, add more stake, update verification info, withdraw from the action.
- `LOVE20Random`: maintain randomness inputs and support verifier-side candidate selection during the verify stage.
- `LOVE20Verify`: submit verification scores.
- `LOVE20Mint`: prepare round reward state, reserve reward accounting, and let users mint governance or action rewards.
- Extension and chain-group contracts can replace the user-facing join, exit, reward-claim, or group-verification surface while still relying on the same base submit and vote pipeline.

## Asset primitives

- `LOVE20Token`: ERC20 token plus floor-pool redemption through `burnForParentToken`.
- `LOVE20SLToken`: LP-backed staking receipt.
- `LOVE20STToken`: token-only staking receipt.

## Use next

- Read `core-contract-map.md` for file-level mapping.
- Read `governance-lifecycle.md` when the question is about transitions across phases or rounds.
