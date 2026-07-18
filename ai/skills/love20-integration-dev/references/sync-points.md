# Sync Points

## Address synchronization

- Core and extension deploy scripts usually write into network or params files.
- Canonical repo-local address handoff files include:
  `core/script/network/<network>/address.params`,
  `extension/script/network/<network>/address.extension.center.params`,
  `extension-lp/script/network/<network>/address.extension.lp.params`,
  `extension-group/script/network/<network>/address.extension.group.params`,
  `group/script/network/<network>/address.group.params`,
  `group/script/network/<network>/address.group.defaults.params`,
  `group-chat/script/network/<network>/address.group.chat.params`,
  `periphery/script/network/<network>/address.params`,
  `periphery/script/network/<network>/address.core.params`
- The `script` repo may mirror or consume addresses for interaction and export flows:
  `script/script/network/<network>/address.params`,
  `script/script/network/<network>/address.extension.center.params`,
  `script/script/network/<network>/address.extension.lp.params`,
  `script/script/network/<network>/address.extension.group.params`,
  `script/script/network/<network>/address.group.params`,
  `script/script/network/<network>/contracts.json`
- For group-chat, the current `script` repo handoff is the contract catalog and ABI mirror, not a separate `address.group.chat.params` file:
  `script/script/network/<network>/contracts.json`,
  `script/abi/GroupChat.sol/GroupChat.json`,
  related group-chat manager, source, admin, member, and ban-list ABI folders under `script/abi`
- During the group-chat community pilot, a replacement deployment does not preserve historical compatibility. Treat the new address and ABI set as one atomic handoff across `group-chat`, `script`, and `interface-test`.
- Frontend env targets live in:
  `interface-test/.env.development`,
  `interface-test/.env.test`,
  `interface-test/.env.public_test`,
  `interface-test/.env.production`
- Default group identity uses:
  `NEXT_PUBLIC_CONTRACT_ADDRESS_GROUP_DEFAULTS`

## ABI synchronization

- Script-side ABI consumers read from `script/abi/*`.
- Frontend ABI consumers read from `interface-test/src/abis/*`.
- If the frontend surface changed, run the required `yarn generate:abi`, `yarn generate:selectors`, or `yarn generate:errors` command in `interface-test`.

## Viewer and hook synchronization

- Periphery viewers aggregate protocol state for frontend or script consumers.
- Frontend read paths usually terminate in:
  `interface-test/src/hooks/contracts/*`,
  `interface-test/src/hooks/composite/*`,
  `interface-test/src/hooks/extension/*`
- New extension UI usually also requires:
  `interface-test/src/components/Extension/Base/Center/ExtensionDeploy.tsx`,
  `interface-test/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`,
  `interface-test/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`,
  `interface-test/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`
- Default group UI and address-transfer context use:
  `interface-test/src/hooks/extension/base/contracts/useGroupDefaults.ts`,
  `interface-test/src/components/Extension/Base/Group/MyGroups.tsx`,
  `interface-test/src/components/Extension/Base/Group/GroupTransfer.tsx`,
  `interface-test/src/components/WalletButton/index.tsx`,
  `interface-test/src/components/Token/Transfer.tsx`

## History and exported-data synchronization

- If the feature depends on indexed events or exported history, refresh the log pipeline instead of checking contract state only.
- High-value files:
  `script/script/log/one_click_process.sh`,
  `script/script/log/block_processor.py`,
  `script/script/log/event_processor.py`,
  `script/script/log/export_query.py`

## Minimum end-to-end acceptance

- Named target network.
- Named repo-local address source and env source.
- One write surface or deployment action.
- One downstream read from cast script, viewer, or hook.
- One user-visible proof:
  frontend render, exported log row, or query result.
- If release is in scope, a separately confirmed `yarn release:test-to-interface-main` step after all `interface-test` checks pass.
