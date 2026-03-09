# Test Matrix

## Core

- Repo: `core`
- Typical commands:
  `forge test --match-path 'test/unit/*'`,
  `forge test --match-path 'test/amount/*'`,
  `forge test --match-path 'test/boundary/*'`,
  `forge test --match-path 'test/integration/*'`,
  `forge test --match-path 'test/fuzz/*'`
- High-value suites:
  `core/test/unit/LOVE20Launch.t.sol`,
  `core/test/unit/LOVE20Join.t.sol`,
  `core/test/unit/LOVE20Mint.t.sol`,
  `core/test/amount/TestLaunchAmount.t.sol`,
  `core/test/amount/TestMintAmount.t.sol`,
  `core/test/integration/Flow.t.sol`,
  `core/test/integration/Revert.t.sol`,
  `core/test/boundary/TestJoinBoundary.t.sol`,
  `core/test/fuzz/TestJoinFuzz.t.sol`

## Extension framework

- Repo: `extension`
- Typical commands:
  `forge test --match-path 'test/*.t.sol'`,
  `forge test --match-path 'test/lib/*.t.sol'`
- High-value suites:
  `extension/test/ExtensionCenter.t.sol`,
  `extension/test/ExtensionFactoryBase.t.sol`,
  `extension/test/ExampleTokenJoin.t.sol`,
  `extension/test/ExampleFactoryTokenJoin.t.sol`,
  `extension/test/lib/RoundHistoryAddress.t.sol`,
  `extension/test/lib/TokenLib.t.sol`

## LP extension

- Repo: `extension-lp`
- Typical commands:
  `forge test --match-path 'test/ExtensionLp.t.sol'`,
  `forge test --match-path 'test/integration/*'`
- High-value suites:
  `extension-lp/test/ExtensionLp.t.sol`,
  `extension-lp/test/integration/Flow.t.sol`,
  `extension-lp/test/integration/RewardCalculation.t.sol`,
  `extension-lp/test/integration/Factory.t.sol`

## Group extension

- Repo: `extension-group`
- Typical commands:
  `forge test --match-path 'test/*.t.sol'`,
  `forge test --match-path 'test/integration/*'`
- High-value suites:
  `extension-group/test/GroupJoin.t.sol`,
  `extension-group/test/ExtensionGroupAction.t.sol`,
  `extension-group/test/ExtensionGroupService.t.sol`,
  `extension-group/test/integration/GroupActionFlow.t.sol`,
  `extension-group/test/integration/GroupServiceFlow.t.sol`,
  `extension-group/test/integration/GroupNegativePaths.t.sol`

## Periphery

- Repo: `periphery`
- Typical command:
  `forge test`
- High-value suites:
  `periphery/test/LOVE20RoundViewer.t.sol`,
  `periphery/test/LOVE20TokenViewer.t.sol`,
  `periphery/test/LOVE20MintViewer.t.sol`,
  `periphery/test/LOVE20Hub.contributeWithETH.t.sol`,
  `periphery/test/LOVE20Hub.stakeLiquidity.t.sol`

## Frontend

- Repo: `interface`
- High-value commands from `package.json`:
  `yarn generate:abi`,
  `yarn generate:env`,
  `yarn generate:selectors`,
  `yarn generate:errors`,
  `yarn build`,
  `yarn test`
- Use `yarn test` only with the understanding that this repo treats build as the test gate.

## Alternate frontend or env sandbox

- Repo: `interface-test`
- High-value commands:
  `yarn build`,
  `yarn dev`
- Use this repo only when the task explicitly targets it or its env templates.

## Scripts and logs

- Repo: `script`
- There is no single unit-test gate. Validate by:
  cast query scripts in `script/script/cast/*`,
  canonical repo-local network files in `*/script/network/<network>/*.params`,
  `script/script/network/*` only when validating mirror or export consumers,
  and log refresh flow in `script/script/log/one_click_process.sh`
