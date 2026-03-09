# Sync Points

## Address synchronization

- Core and extension deploy scripts usually write into network or params files.
- Canonical repo-local address handoff files include:
  `core/script/network/<network>/address.params`,
  `extension/script/network/<network>/address.extension.center.params`,
  `extension-lp/script/network/<network>/address.extension.lp.params`,
  `extension-group/script/network/<network>/address.extension.group.params`,
  `group/script/network/<network>/address.group.params`,
  `periphery/script/network/<network>/address.params`,
  `periphery/script/network/<network>/address.core.params`
- The `script` repo may mirror or consume addresses for interaction and export flows:
  `script/script/network/<network>/address.params`,
  `script/script/network/<network>/address.extension.center.params`,
  `script/script/network/<network>/address.extension.lp.params`,
  `script/script/network/<network>/address.extension.group.params`,
  `script/script/network/<network>/address.group.params`,
  `script/script/network/<network>/contracts.json`
- Frontend env targets live in:
  `interface/.env.development`,
  `interface/.env.test`,
  `interface/.env.public_test`,
  `interface/.env.production`

## ABI synchronization

- Script-side ABI consumers read from `script/abi/*`.
- Frontend ABI consumers read from `interface/src/abis/*`.
- If the frontend surface changed, check whether `yarn generate:abi`, `yarn generate:selectors`, or `yarn generate:errors` is required in `interface`.

## Viewer and hook synchronization

- Periphery viewers aggregate protocol state for frontend or script consumers.
- Frontend read paths usually terminate in:
  `interface/src/hooks/contracts/*`,
  `interface/src/hooks/composite/*`,
  `interface/src/hooks/extension/*`
- New extension UI usually also requires:
  `interface/src/components/Extension/Base/Center/ExtensionDeploy.tsx`,
  `interface/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`,
  `interface/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`,
  `interface/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`

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
