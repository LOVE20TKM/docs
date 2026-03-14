# Junior-Agent Acceptance Cases

Use these cases after updating LOVE20 skills, docs, or reusable prompts for another AI agent.

## Global Pass Rules

- Fail the answer if it talks about `round` or `phase` without clarifying business round vs contract-local `currentRound()` when timing matters.
- Fail the answer if it talks about `join`, `claim`, or `verify` without first deciding whether the surface is base LOVE20, extension, or group.
- Fail the answer if it treats `periphery`, `script`, or `interface` as immutable behavior truth when deployed contract repos are relevant.
- Prefer small targeted evals. Run only the cases that match the changed skill or prompt.

## Case A1: Round Translation

- Ask:
  `同一时刻如果 submit/vote 合约的 round 是 3，那么 join/random 和 verify 分别应该怎么理解？`
- Must include:
  - `currentRound()` is contract-local
  - `originBlocks` offsets from deployment
  - same wall-clock block maps to submit/vote `3`, join/random `2`, verify `1`
- Minimum sources:
  - `core/src/Phase.sol`
  - `core/script/DeployLOVE20.s.sol`
- Fail if:
  - it says all phase contracts share the same round number
  - it explains only the whitepaper pipeline but not the contract-local round mapping

## Case A2: Base vs Extension Join Surface

- Ask:
  `一个 action 要调用 LOVE20Join，还是扩展合约，还是 GroupJoin？`
- Must include:
  - determine the action type first from whitelist or extension detection
  - base action uses `LOVE20Join`
  - extension action may use an extension contract or `GroupJoin`
- Minimum sources:
  - `core/src/interfaces/ILOVE20Submit.sol`
  - `extension/src/ExtensionBase.sol`
  - `extension-group/src/GroupJoin.sol`
- Fail if:
  - it defaults to `LOVE20Join` without classifying the action

## Case A3: Chain-Group Join Flow

- Ask:
  `如何加入链群行动？`
- Must include:
  - `GroupJoin.join(extension, groupId, amount, verificationInfos)`
  - extension address and `groupId` are part of the user-facing write
  - join-token approval and group constraints are prerequisites
- Minimum sources:
  - `extension-group/src/GroupJoin.sol`
  - `extension-group/src/ExtensionGroupAction.sol`
- Fail if:
  - it recommends `LOVE20Join.join(...)` as the main write

## Case A4: Extension Reward Claim

- Ask:
  `LP 行动奖励怎么领？`
- Must include:
  - extension reward claims use `IReward.claimReward` or `claimRewards`
  - the write target is the extension contract, not `LOVE20Mint`
  - `burnRewardIfNeeded` can be relevant for extension reward handling
- Minimum sources:
  - `extension/src/interface/IReward.sol`
  - `extension-lp/src/ExtensionLp.sol`
- Fail if:
  - it tells the user to call `mintActionReward` on `LOVE20Mint`

## Case A5: Frontend Branching on `acting/join`

- Ask:
  `acting/join 页面怎么判断走普通行动还是扩展行动？`
- Must include:
  - route entry `interface/src/pages/acting/join.tsx`
  - `useActionInfo`
  - `useExtensionByActionInfoWithCache`
  - extension branch to `ExtensionActionJoinPanel`, base branch to normal join components
- Minimum sources:
  - `interface/src/pages/acting/join.tsx`
  - `interface/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`
- Fail if:
  - it traces only core hooks and misses the extension branch

## Case A6: Extension Participation State Source

- Ask:
  `扩展行动的参与人数和参与金额从哪里读？`
- Must include:
  - `ExtensionCenter.accountsCount` for participant count in the generic extension path
  - extension contract `joinedAmount` for extension-side total joined amount
  - group variants can additionally involve `GroupJoin`
- Minimum sources:
  - `extension/src/interface/IExtensionCenter.sol`
  - `interface/src/hooks/extension/base/composite/useExtensionParticipationData.ts`
  - `extension-group/src/GroupJoin.sol`
- Fail if:
  - it claims `LOVE20Join.amountByActionId` and `numOfAccounts` are universal for all actions

## Case A7: Selector Coverage and Stale Catalogs

- Ask:
  `为什么某个 GroupJoin 或 ExtensionCenter 的 selector 在旧索引里查不到？`
- Must include:
  - generated selector catalogs can be stale
  - `interface/docs/function-selectors.json` should include extension and group ABI modules when regenerated
  - the agent should regenerate before concluding the selector is absent
- Minimum sources:
  - `interface/scripts/generateFunctionSelectors.ts`
  - `docs/ai/skills/love20-selectors-and-errors/SKILL.md`
- Fail if:
  - it concludes "不存在这个 selector" without checking generator freshness

## Case A8: Prompt Handoff for Another Agent

- Ask:
  `帮我写一个让别的 AI 解释 LOVE20 join 流程的 prompt。`
- Must include:
  - anchors such as token, action, round, account, or page when known
  - a triage step for base vs extension and business round vs contract-local round
  - a source-of-truth rule that prioritizes deployed contract repos
  - an explicit output contract
- Minimum sources:
  - `docs/ai/skills/love20-prompts/SKILL.md`
  - one domain skill such as `love20-contract-playbooks` or `love20-core-protocol`
- Fail if:
  - the prompt is generic and does not constrain truth sources or round semantics

## Case A9: SL Unlock Period and Exit Flow

- Ask:
  `LOVE20 的流动性质押解锁期到底对应什么，申请解锁和取回资产分别是什么链上动作？`
- Must include:
  - whitepaper `解锁期` maps to `promisedWaitingPhases`
  - `unstake` is the unlock request and `withdraw` retrieves assets after the full wait
  - governance-vote or eligibility impact depends on unlock period and SL or ST receipt-token balance
- Minimum sources:
  - `docs/whitepaper/LOVE20协议设计.md`
  - `core/src/interfaces/ILOVE20Stake.sol`
- Fail if:
  - it treats `unstake` and `withdraw` as the same step
  - it ignores the receipt-token balance caveat

## Case A10: Extension Participation Negative Check

- Ask:
  `某个地址是不是参与过这个行动？我查不到 LOVE20Join 里的 amount，是不是就说明没参与？`
- Must include:
  - classify the action as base, extension, or group before concluding
  - generic extension paths use `IExtensionCenter.isAccountJoined` or extension `joinedAmountByAccount`
  - chain-group paths can use `GroupJoin.joinedAmountByAccount` or `joinInfo`
- Minimum sources:
  - `core/src/interfaces/ILOVE20Join.sol`
  - `extension/src/interface/IExtensionCenter.sol`
  - `extension-group/src/interface/IGroupJoin.sol`
- Fail if:
  - it treats missing `LOVE20Join.amountByActionIdByAccount` as universal proof of non-participation
