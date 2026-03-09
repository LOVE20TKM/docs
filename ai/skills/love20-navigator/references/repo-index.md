# Repository Index

## Core docs repo

- `docs/README.md`
  Entry point for the ecosystem and repo list.
- `docs/whitepaper/LOVE20协议设计.md`
  Main protocol design.
- `docs/whitepaper/FAQ.md`
  Rationale and edge-case explanations.
- `docs/dev/合约编程风格指南.md`
  Naming and ordering conventions for contract work.

## Core protocol repo

- `core/src/LOVE20Launch.sol`
  Fair launch and child-token creation.
- `core/src/interfaces/IPhase.sol`
  Timing backbone for phases, rounds, and phase-window calculations.
- `core/src/LOVE20Stake.sol`
  SL and ST staking, unstake, withdraw.
- `core/src/LOVE20Submit.sol`
  Action creation and submission.
- `core/src/LOVE20Vote.sol`
  Governance voting.
- `core/src/LOVE20Join.sol`
  Action participation, verification info, random candidate preparation.
- `core/src/LOVE20Random.sol`
  Random seed lifecycle and verification-stage randomness support.
- `core/src/LOVE20Verify.sol`
  Verification scoring.
- `core/src/LOVE20Mint.sol`
  Governance and action reward preparation, reservation, burn, and minting.
- `core/src/LOVE20TokenFactory.sol`
  Token tree creation.
- `core/src/LOVE20Token.sol`
  ERC20 asset plus parent-pool floor burn.

## Periphery repo

- `periphery/src/LOVE20Hub.sol`
  Convenience write wrapper.
- `periphery/src/LOVE20TokenViewer.sol`
  Token catalog and launch/pair aggregations.
- `periphery/src/LOVE20RoundViewer.sol`
  Round and action aggregation.
- `periphery/src/LOVE20MintViewer.sol`
  Reward-oriented aggregation.

## Script repo

- `script/script/cast`
  Ready-made interaction scripts grouped by launch, stake, submit, vote, join, verify, mint, token, and WETH tasks.
- `script/abi`
  ABI JSONs mirrored across the ecosystem.
- `script/script/log`
  Event export and processing scripts.

## Extension framework repo

- `extension/README.md`
  High-level extension model.
- `extension/src/ExtensionBase.sol`
  Base extension identity and initialization.
- `extension/src/ExtensionBaseReward.sol`
  Reward accounting base.
- `extension/src/ExtensionBaseRewardJoin.sol`
  No-token join base.
- `extension/src/ExtensionBaseRewardTokenJoin.sol`
  Token-join base.
- `extension/src/ExtensionCenter.sol`
  Shared account registry.

## Concrete extension repos

### LP extension

- `extension-lp/README.md`
  LP extension overview and deployment context.
- `extension-lp/src/ExtensionLp.sol`
  LP-based action participation extension implementation.
- `extension-lp/src/ExtensionLpFactory.sol`
  LP extension factory and registration entry.
- `extension-lp/src/interface/ILp.sol`
  LP extension read and write surface.
- `extension-lp/src/interface/ILpFactory.sol`
  LP extension factory interface.

### Chain-group design docs

- `extension-group/docs/链群行动扩展协议.md`
  Chain-group action extension design and flow notes.
- `extension-group/docs/链群服务扩展协议.md`
  Chain-group service extension design and reward notes.
- `extension-group/docs/链群公告协议.md`
  Chain-group notice and announcement flow notes.

### Chain-group action line

- `extension-group/src/ExtensionGroupAction.sol`
  Chain-group action extension implementation.
- `extension-group/src/ExtensionGroupActionFactory.sol`
  Chain-group action factory and registration entry.
- `extension-group/src/interface/IGroupAction.sol`
  Chain-group action extension interface.

### Chain-group service line

- `extension-group/src/ExtensionGroupService.sol`
  Chain-group service extension implementation.
- `extension-group/src/ExtensionGroupServiceFactory.sol`
  Chain-group service factory and registration entry.
- `extension-group/src/GroupRecipients.sol`
  Service-recipient split and payout-recipient configuration.
- `extension-group/src/interface/IGroupService.sol`
  Chain-group service extension interface.

### Chain-group shared group ops

- `extension-group/src/GroupManager.sol`
  Group activation, ownership-linked control, and group-level administration.
- `extension-group/src/GroupJoin.sol`
  Chain-group join state and participation flow.
- `extension-group/src/GroupVerify.sol`
  Chain-group verification flow and verifier-side logic.
- `extension-group/src/GroupNotice.sol`
  Group notice and announcement surface.
- `extension-group/src/interface/IGroupJoin.sol`
  Chain-group join interface.
- `extension-group/src/interface/IGroupVerify.sol`
  Chain-group verify interface.
- `extension-group/src/interface/IGroupManager.sol`
  Chain-group manager interface.
- `extension-group/src/interface/IGroupNotice.sol`
  Chain-group notice interface.
- `extension-group/src/interface/IGroupRecipients.sol`
  Chain-group recipients interface.

## Chain-group NFT repo

- `group/README.md`
  Group NFT design and mint cost rules.
- `group/src/LOVE20Group.sol`
  ERC721 implementation.

## Frontend repo

- `interface/src/pages`
  Route-level screens.
- `interface/src/components`
  Reusable UI and feature components.
- `interface/src/hooks/contracts`
  Direct wagmi contract hooks.
- `interface/src/hooks/composite`
  Aggregated frontend data logic.
- `interface/src/hooks/extension`
  Extension-aware contract hooks and composite adapters for LP, group action, and group service flows.
- `interface/src/config/extensionConfig.ts`
  Extension factory registry for UI.
