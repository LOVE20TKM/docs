# Contract And Test Checklist

## Contract checklist

- Base class matches the actual user flow:
  `ExtensionBaseReward`,
  `ExtensionBaseRewardJoin`,
  or `ExtensionBaseRewardTokenJoin`.
- `initializeIfNeeded()` is called before relying on action-bound state.
- `registerActionIfNeeded()` is called before maintaining action user lists.
- `ExtensionCenter` updates are present for account add, remove, and verification-info writes when required.
- Reward claim or burn logic remains explicitly tied to the underlying LOVE20 action reward.
- Token custody, approval, and exit behavior are defined if the extension holds user assets.
- Round-sensitive accounting is tested if the extension depends on block progress, verification rounds, or carry-over state.

## Minimum tests

- Happy path:
  deploy factory,
  create extension,
  initialize,
  join,
  verify or settle if applicable,
  claim or mint reward,
  exit if supported.
- Negative path:
  zero amount,
  bad phase,
  duplicate registration,
  missing permission,
  invalid token or group binding,
  premature exit or claim.
- Integration path:
  one full round or multi-round flow in the nearest integration suite.

## High-value existing tests

- General framework:
  `extension/test/ExampleTokenJoin.t.sol`,
  `extension/test/ExampleFactoryTokenJoin.t.sol`,
  `extension/test/ExtensionCenter.t.sol`,
  `extension/test/ExtensionFactoryBase.t.sol`
- LP extension:
  `extension-lp/test/ExtensionLp.t.sol`,
  `extension-lp/test/integration/Flow.t.sol`,
  `extension-lp/test/integration/RewardCalculation.t.sol`,
  `extension-lp/test/integration/EdgeCases.t.sol`
- Group extension:
  `extension-group/test/ExtensionGroupAction.t.sol`,
  `extension-group/test/ExtensionGroupService.t.sol`,
  `extension-group/test/GroupJoin.t.sol`,
  `extension-group/test/GroupVerifyBatchSubmission.t.sol`,
  `extension-group/test/integration/GroupActionFlow.t.sol`,
  `extension-group/test/integration/GroupServiceFlow.t.sol`,
  `extension-group/test/integration/GroupNegativePaths.t.sol`

## Post-change verification

- Compile and run the smallest relevant Foundry test slice first.
- Then run the nearest integration tests.
- Name the viewer or state reads that confirm the deployed change:
  factory registration,
  action binding,
  participant list,
  reward state,
  or group membership state.
