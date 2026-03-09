# Extension Development Workflow

## Start from the closest repo

- `extension`
  Use for shared framework behavior and minimal examples:
  `src/ExtensionBase.sol`,
  `src/ExtensionBaseReward.sol`,
  `src/ExtensionBaseRewardJoin.sol`,
  `src/ExtensionBaseRewardTokenJoin.sol`,
  `src/ExtensionCenter.sol`,
  `src/ExtensionFactoryBase.sol`,
  `src/examples/ExampleTokenJoin.sol`,
  `src/examples/ExampleFactoryTokenJoin.sol`.
- `extension-lp`
  Use when the new feature looks like amount-based joins and weighted reward accounting:
  `src/ExtensionLp.sol`,
  `src/ExtensionLpFactory.sol`,
  `test/ExtensionLp.t.sol`,
  `test/integration/Flow.t.sol`,
  `test/integration/RewardCalculation.t.sol`.
- `extension-group`
  Use when the feature depends on group membership, verification, manager permissions, or service-provider flows:
  `src/ExtensionGroupAction.sol`,
  `src/ExtensionGroupActionFactory.sol`,
  `src/ExtensionGroupService.sol`,
  `src/ExtensionGroupServiceFactory.sol`,
  `src/GroupJoin.sol`,
  `src/GroupVerify.sol`,
  `test/ExtensionGroupAction.t.sol`,
  `test/ExtensionGroupService.t.sol`,
  `test/integration/GroupActionFlow.t.sol`,
  `test/integration/GroupServiceFlow.t.sol`.

## Preferred implementation order

1. Lock the user-facing join and reward model.
2. Choose the highest-level base class that matches that model.
3. Implement or modify the concrete extension contract.
4. Implement or modify the factory contract and constructor or init parameters.
5. Update deployment scripts:
   `extension/script/DeployExtensionCenter.s.sol`,
   `extension-lp/script/DeployExtensionLpFactory.s.sol`,
   `extension-group/script/DeployGroupActionFactory.s.sol`,
   `extension-group/script/DeployGroupServiceFactory.s.sol`,
   or the nearest existing script.
6. Add or update focused unit and integration tests.
7. If the change must be usable in the dApp, hand off to `interface/docs/extension.md` and the extension plugin files in `interface/src/components/Extension` and `interface/src/hooks/extension`.

## File clusters to keep in sync

- Framework or interfaces:
  `extension/src/interface/*`,
  `extension/src/*.sol`
- Concrete extension implementation:
  `extension-lp/src/*`,
  `extension-group/src/*`
- Foundry tests:
  `extension/test/*`,
  `extension-lp/test/*`,
  `extension-group/test/*`
- Deploy scripts and network config:
  `extension/script/*`,
  `extension-lp/script/*`,
  `extension-group/script/*`

## Final delivery bar

An extension change is only complete when these are all true:

- the participant model is explicit
- the factory or deployment entry point is updated
- the tests prove the join, reward, and failure paths
- the dApp handoff points are named when UI work is in scope
