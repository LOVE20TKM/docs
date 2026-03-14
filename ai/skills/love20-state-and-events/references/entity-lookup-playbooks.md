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

Default scope:

- If the user says only `action` or `行动`, assume the question may refer to a base action, generic extension action, LP extension action, or chain-group action until the action type is resolved.

Use these surfaces first:

- `LOVE20Submit.actionInfo` for the base action record.
- `core/src/interfaces/ILOVE20Join.sol` and `core/src/interfaces/ILOVE20Verify.sol` for direct participation and verification truth.
- `extension/src/interface/IExtensionCenter.sol` plus `extension/src/interface/IExtension.sol` when the action may be extension-backed.
- `extension-group/src/interface/IGroupJoin.sol` when the action may be chain-group-backed.
- `LOVE20RoundViewer.actionInfosByIds` or `actionInfosByPage` for batch lookup.
- `LOVE20RoundViewer.actionVoters`, `verificationInfos`, `verifiedAddresses`, or related verification reads when the question is about voters and verification participants.
- `LOVE20MintViewer.actionRewardsByAccountByActionIdByRounds` for reward history per action.

Frontend bridges:

- `useActionInfosByIds`
- `useActionInfosByPage`
- `useActionDetailData` for page-level aggregation of action info, participant counts, totals, current round, and extension participation data
- `useExtensionsByActionInfosWithCache` when the UI may branch into an extension-backed action
- `useExtensionParticipationData` for extension participant count, joined amount, and account-joined status

Use historical indexing when:

- you need a timeline of votes, joins, verify events, reward claims, or cross-round action activity

If the question is "did account X participate in action Y?", use this order:

1. Resolve the action type first from `actionInfo` plus extension detection or registration.
2. For base actions, use `ILOVE20Join.amountByActionIdByAccount` or the matching base viewer and hook surfaces.
3. For generic or LP-style extension actions, use `IExtensionCenter.isAccountJoined` plus extension `joinedAmountByAccount`; use `accountsCount` and `joinedAmount` for totals.
4. For chain-group actions, use `GroupJoin.joinedAmountByAccount` or `joinInfo`, and treat the extension contract plus `GroupJoin` as the participation owner.
5. Only conclude "not participated" after checking the surface that owns the action type.

## Extension-Backed Participation

Use this playbook whenever the question is about whether an account joined, exited, or currently counts toward an action that may be extension-backed.

- Start from the action record, then determine whether the action is base, extension, or chain-group scoped before reading account totals.
- Generic extension truths often come from `ExtensionCenter` membership reads together with the extension contract's `joinedAmount` and `joinedAmountByAccount`.
- Chain-group truths often come from `GroupJoin.joinInfo`, `joinedAmount`, and `joinedAmountByAccount`, even when the action itself is represented by an extension contract.
- Frontend traces should usually cross `useExtensionsByActionInfosWithCache`, `useExtensionParticipationData`, or group plugin hooks before any conclusion about missing participation.

## Account

Use these surfaces first:

- `core/src/interfaces/ILOVE20Stake.sol` and `core/src/interfaces/ILOVE20Mint.sol` for direct governance and reward truth.
- `extension/src/interface/IExtensionCenter.sol` and extension `joinedAmountByAccount` reads when the account question is scoped to a known extension-backed action.
- `extension-group/src/interface/IGroupJoin.sol` for group-scoped joined amounts or join metadata by account.
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
- `useMyJoinedExtensionActions` when extension-backed joined actions may be excluded from the base joined-action list

Use historical indexing when:

- you need account transfer flow, mint history, reward claim history, or liquidity/swap timeline
