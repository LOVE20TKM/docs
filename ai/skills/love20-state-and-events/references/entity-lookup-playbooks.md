# Entity Lookup Playbooks

## Token

Use these surfaces first:

- `core/src/interfaces/ILOVE20Launch.sol` and `core/src/interfaces/ILOVE20Token.sol` for direct launch and token truth.
- `LOVE20TokenViewer.tokenDetail` for token metadata plus launch info.
- `LOVE20TokenViewer.tokenStatistics` for supply, reserve, staking, join, and child-token counters.
- `LOVE20TokenViewer.tokenPairInfoWithAccount` for pair balances and account LP context.
- `LOVE20MintViewer.estimatedActionRewardOfCurrentRound` and `estimatedGovRewardOfCurrentRound` for current-round reward estimation.

Frontend bridges:

- `useTokenDetail`
- `useTokenStatistics`
- `useTokenPairInfoWithAccount`
- `useStakeLpPageData` when the UI also needs allowances for the hub flow

Use token history when:

- you need launch events, claim/contribute timeline, transfer flow, or reward mint history
- then switch to the event DB views in `event-and-indexing.md`

## Round

Use these surfaces first:

- `core/src/interfaces/IPhase.sol` plus the phase-aware core contracts for direct round truth.
- `LOVE20RoundViewer.actionSubmits`
- `LOVE20RoundViewer.votingActions`
- `LOVE20RoundViewer.joinableActions`
- `LOVE20RoundViewer.joinedActions`
- `LOVE20RoundViewer.verifyingActions`
- `LOVE20RoundViewer.govData`
- `LOVE20MintViewer.govRewardsByAccountByRounds`

Frontend bridges:

- `useActionSubmits`
- `useVotingActions`
- `useJoinableActions`
- `useJoinedActions`
- `useVerifyingActions`
- `useMyGovData`
- `useCanSubmit`

Use historical indexing when:

- you need per-round mint address counts, TUSDT flow, swap activity, or reward distribution history

## Action

Use these surfaces first:

- `LOVE20Submit.actionInfo` for the base action record.
- `core/src/interfaces/ILOVE20Join.sol` and `core/src/interfaces/ILOVE20Verify.sol` for direct participation and verification truth.
- `LOVE20RoundViewer.actionInfosByIds` or `actionInfosByPage` for batch lookup.
- `LOVE20RoundViewer.actionVoters`, `verificationInfos`, `verifiedAddresses`, or related verification reads when the question is about voters and verification participants.
- `LOVE20MintViewer.actionRewardsByAccountByActionIdByRounds` for reward history per action.

Frontend bridges:

- `useActionInfosByIds`
- `useActionInfosByPage`
- `useActionDetailData` for page-level aggregation of action info, participant counts, totals, current round, and extension participation data

Use historical indexing when:

- you need a timeline of votes, joins, verify events, reward claims, or cross-round action activity

## Account

Use these surfaces first:

- `core/src/interfaces/ILOVE20Stake.sol` and `core/src/interfaces/ILOVE20Mint.sol` for direct governance and reward truth.
- `LOVE20TokenViewer.participatedTokensByPage`
- `LOVE20RoundViewer.joinedActions`
- `LOVE20Stake.validGovVotes`
- `LOVE20MintViewer.govRewardsByAccountByRounds`
- `LOVE20MintViewer.actionRewardsByAccountOfLastRounds`

Frontend bridges:

- `useParticipatedTokensByPage`
- `useJoinedActions`
- `useMyGovData`
- `useActionRewardsByAccountOfLastRounds`

Use historical indexing when:

- you need account transfer flow, mint history, reward claim history, or liquidity/swap timeline
