# Governance Lifecycle

## Pipeline model

- The whitepaper describes a rolling three-phase pipeline:
  - round N submit and vote
  - round N-1 action
  - round N-2 verify
- Each phase has equal length.
- LOVE20 should not be read as "finish all of round N, then start round N+1". Different rounds overlap in different phases at the same time.
- A more accurate mental model is a moving pipeline. At a given time:
  - one round is in submit and vote
  - an earlier round is in action
  - an even earlier round is in verify
- When one phase window advances, the lifecycle for the same round moves forward and a newer round also enters the pipeline.

## Contract timing model

- `Phase.currentRound()` is contract-local, not a global round counter shared by all contracts.
- `Phase.roundByBlockNumber(blockNumber)` simply divides the block offset by `phaseBlocks` for that contract's own `originBlocks`.
- Core deployment aligns contracts to the pipeline by offsetting their origins:
  - `LOVE20Stake`, `LOVE20Submit`, `LOVE20Vote`: `originBlocks = T0`
  - `LOVE20Join`, `LOVE20Random`: `originBlocks = T0 + phaseBlocks`
  - `LOVE20Verify`: `originBlocks = T0 + 2 * phaseBlocks`
- Practical translation at the same block:
  - submit and vote contract round `r`
  - join and random contract round `r - 1`
  - verify contract round `r - 2`
- When explaining LOVE20 to another agent, use "business round" for the whitepaper pipeline and "contract round on X" for exact call semantics.

## Phase 1: submit and vote

- Action authors or eligible governors create or nominate actions through `LOVE20Submit`.
- Governors allocate governance votes through `LOVE20Vote`.
- Useful reads:
  - `canSubmit`
  - `actionInfo`
  - `votesNumByActionId`
  - `maxVotesNum`

## Phase 2: action

- Participants join voted actions through `LOVE20Join.join`.
- Participants can add more stake and update verification info.
- `JOIN_END_PHASE_BLOCKS` limits late joins near phase end.
- Extension-backed actions may replace the user-facing join surface with extension contracts or `GroupJoin`, but they still depend on the same voted action existing in the current join window.
- Useful reads:
  - `amountByActionId`
  - `amountByActionIdByAccount`
  - `verificationInfo`
  - `numOfAccounts`

## Phase 3: verify

- Randomness is maintained in `LOVE20Random`.
- Random candidate lists are prepared through `LOVE20Join.prepareRandomAccountsIfNeeded`.
- Governors verify actions they supported by calling `LOVE20Verify.verify`.
- `prepareRandomAccountsIfNeeded` runs from the join contract's current round and prepares the previous join round for verification, matching the deployment offset between join and verify.
- Useful reads:
  - `randomAccounts`
  - `scoreByActionId`
  - `scoreByVerifier`

## Reward preparation and minting

- `LOVE20Mint.prepareRewardIfNeeded` reserves the round reward state.
- Governors mint governance rewards through `mintGovReward`.
- Verified action participants mint action rewards through `mintActionReward`.
- Useful reads:
  - `govRewardByAccount`
  - `actionRewardByActionIdByAccount`
  - `rewardReserved`
  - `rewardMinted`
  - `rewardBurned`

## Supporting state that appears across phases

- `LOVE20Stake.validGovVotes` gates effective governance power.
- `LOVE20Stake.accountStakeStatus` explains SL, ST, and waiting periods.
- `LOVE20Token.parentPool` and `burnForParentToken` sit outside the round pipeline but affect token economics.
