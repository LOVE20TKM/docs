# Operation Playbooks

## Launch a token

- Core contract:
  `core/src/interfaces/ILOVE20Launch.sol`
- Main write:
  `launchToken(symbol, parentTokenAddress)`
- Default execution form:
  direct `cast send`
- Main reads:
  `remainingLaunchCount`, `launchInfo`, `tokenAddressBySymbol`
- Existing `cast` templates:
  `launch_deploy.sh`, `launch_query.sh`, `launch_stat.sh`

## Contribute to fair launch and claim

- Core writes:
  `contribute`, `withdraw`, `claim`
- Default execution form:
  direct `cast send` to `ILOVE20Launch`
- Helper write for the first token with native ETH:
  `periphery/src/LOVE20Hub.sol`
  `contributeFirstTokenWithETH`
  Use as a convenience example when native ETH wrapping is part of the flow, not as the default surface.
- Existing `cast` templates:
  `launch_contribute.sh`, `launch_withdraw.sh`, `launch_claim.sh`

## Stake for governance

- Core contract:
  `core/src/interfaces/ILOVE20Stake.sol`
- Main writes:
  `stakeLiquidity`, `stakeToken`, `unstake`, `withdraw`
- Default execution form:
  direct `cast send`
- Helper write:
  `LOVE20Hub.stakeLiquidity`
  Use only when the helper materially simplifies liquidity assembly.
- Existing `cast` templates:
  `stake_liquidity.sh`, `stake_token.sh`, `stake_unstake.sh`, `stake_withdraw.sh`, `stake_query.sh`

## Create or nominate actions

- Core contract:
  `core/src/interfaces/ILOVE20Submit.sol`
- Main writes:
  `submitNewAction`, `submit`
- Default execution form:
  direct `cast send`
- Main reads:
  `actionInfo`, `actionSubmitsCount`, `submitInfo`
- Existing `cast` templates:
  `submit_new_action.sh`, `submit.sh`, `submit_query.sh`

## Vote on actions

- Core contract:
  `core/src/interfaces/ILOVE20Vote.sol`
- Main write:
  `vote(actionIds, votes)`
- Default execution form:
  direct `cast send`
- Main reads:
  `maxVotesNum`, `votesNumsByAccount`, `votesNumByActionId`
- Existing `cast` templates:
  `vote.sh`, `vote_query.sh`

## Join base LOVE20 actions and manage verification info

- Core contract:
  `core/src/interfaces/ILOVE20Join.sol`
- Main writes:
  `join`, `updateVerificationInfo`, `withdraw`
- Default execution form:
  direct `cast send`
- Random preparation:
  `prepareRandomAccountsIfNeeded`
- Main reads:
  `amountByActionId`, `actionIdsByAccount`, `verificationInfo`
- Existing `cast` templates:
  `join.sh`, `join_update.sh`, `join_withdraw.sh`, `join_query.sh`, `random.sh`, `random_query.sh`

## Join generic extension actions

- Extension surfaces:
  `extension/src/interface/IJoin.sol`, `extension/src/interface/ITokenJoin.sol`
- Common implementation base classes:
  `extension/src/ExtensionBaseRewardJoin.sol`, `extension/src/ExtensionBaseRewardTokenJoin.sol`
- Main writes:
  `join(...)`, `exit()`
- Default execution form:
  direct `cast send` to the extension contract
- Main reads:
  `joinInfo`, `joinedAmount`, `joinedAmountByAccount`, `joinedAmountTokenAddress`
- Critical prerequisite:
  the first join can trigger `initializeIfNeeded()` and `ExtensionCenter.registerActionIfNeeded()`, so the extension-backed action must already be discoverable from the current voted-action set for that token.

## Join LP extension actions

- Extension contract:
  `extension-lp/src/ExtensionLp.sol`
- Main writes:
  `join(amount, verificationInfos)`, `exit()`
- Default execution form:
  direct `cast send` to the extension contract
- Main reads:
  `JOIN_TOKEN_ADDRESS`, `WAITING_BLOCKS`, `rewardByAccount`, `govRatio`, `MIN_GOV_RATIO`
- Critical prerequisites:
  approve the LP token to the extension contract and satisfy the minimum governance-ratio check on first join.

## Join group-action and group-service flows

- Group join helper:
  `extension-group/src/GroupJoin.sol`
- Common reward contracts:
  `extension-group/src/ExtensionGroupAction.sol`, `extension-group/src/ExtensionGroupService.sol`
- Main writes:
  `join(extension, groupId, amount, verificationInfos)`, `trialJoin(extension, groupId, provider, verificationInfos)`, `exit(extension)`
- Default execution form:
  direct `cast send` to `GroupJoin`
- Main reads:
  `joinInfo`, `joinedAmount`, `groupIdByAccount`, `totalJoinedAmountByGroupId`
- Critical prerequisites:
  approve the extension join token to `GroupJoin`, use a valid registered extension address, and satisfy the group-manager constraints for the target `groupId`.

## Verify actions

- Core contract:
  `core/src/interfaces/ILOVE20Verify.sol`
- Main write:
  `verify`
- Default execution form:
  direct `cast send`
- Main reads:
  `scoreByActionId`, `scoreByVerifier`, `stakedAmountOfVerifiers`
- Existing `cast` templates:
  `verify.sh`, `verify_query.sh`

## Group verification and delegate management

- Group verification contract:
  `extension-group/src/interface/IGroupVerify.sol`
- Main writes:
  `submitOriginScores`, `setGroupDelegate`, `distrustVote`
- Default execution form:
  direct `cast send` to `GroupVerify`
- Main reads:
  `canVerify`, `groupIdsByVerifier`, `originScoreByAccount`, `accountScore`, `groupScore`, `totalGroupScore`

## Mint rewards

- Core contract:
  `core/src/interfaces/ILOVE20Mint.sol`
- Main writes:
  `prepareRewardIfNeeded`, `mintGovReward`, `mintActionReward`
- Default execution form:
  direct `cast send`
- Main reads:
  `govRewardByAccount`, `actionRewardByActionIdByAccount`, `rewardAvailable`
- Existing `cast` templates:
  `mint_gov_reward.sh`, `mint_action_reward.sh`, `mint_query.sh`

## Claim or burn extension rewards

- Extension reward surface:
  `extension/src/interface/IReward.sol`
- Common implementations:
  `extension-lp/src/ExtensionLp.sol`, `extension-group/src/ExtensionGroupAction.sol`, `extension-group/src/ExtensionGroupService.sol`
- Main writes:
  `claimReward`, `claimRewards`, `burnRewardIfNeeded`
- Default execution form:
  direct `cast send` to the extension contract
- Main reads:
  `reward`, `rewardByAccount`, `burnInfo`

## Redeem against the parent pool

- Core contract:
  `core/src/interfaces/ILOVE20Token.sol`
- Main write:
  `burnForParentToken(amount)`
- Default execution form:
  direct `cast send`
- Existing `cast` template:
  `burnForParentToken.sh`

## Read token and liquidity state

- Main reads:
  `LOVE20TokenViewer`, `LOVE20RoundViewer`, `LOVE20MintViewer`
- Default execution form:
  direct `cast call`
- Existing `cast` templates:
  `token_query.sh`, `weth_query.sh`, `weth_stat.sh`
