# Integration Workflow

## Start from behavior truth

- Base protocol behavior:
  `core/src/*`
- Generic extension framework:
  `extension/src/*`
- LP extension behavior:
  `extension-lp/src/*`
- Group extension behavior:
  `extension-group/src/*`
- Group NFT or helper behavior:
  `group/*` when the issue depends on group ownership or holder semantics

## Downstream layers that usually need to stay in sync

- Periphery viewers and hub:
  `periphery/src/LOVE20RoundViewer.sol`,
  `periphery/src/LOVE20TokenViewer.sol`,
  `periphery/src/LOVE20MintViewer.sol`,
  `periphery/src/LOVE20Hub.sol`
- Deployment scripts:
  `core/script/deploy/*`,
  `extension/script/deploy/*`,
  `extension-lp/script/deploy/*`,
  `extension-group/script/deploy/*`,
  `group/script/deploy/*`,
  `periphery/script/deploy/*`
- Network and interaction scripts:
  `core/script/network/*`,
  `extension/script/network/*`,
  `extension-lp/script/network/*`,
  `extension-group/script/network/*`,
  `group/script/network/*`,
  `periphery/script/network/*`,
  `script/script/network/*`,
  `script/script/cast/*`,
  `script/abi/*`
- Log export pipeline:
  `script/script/log/one_click_process.sh`,
  `script/script/log/export.sh`,
  `script/script/log/export_query.py`
- Frontend ABI and env surfaces:
  `interface/scripts/generateAbiTs.ts`,
  `interface/scripts/generate-env.js`,
  `interface/src/abis/*`,
  `interface/.env.*`
- Frontend hook and registration surfaces:
  `interface/src/hooks/contracts/*`,
  `interface/src/hooks/extension/*`,
  `interface/src/config/extensionConfig.ts`,
  `interface/docs/extension.md`

## Preferred order

1. Confirm the contract or viewer source that owns the behavior.
2. Update deployment or address-binding files if the integration target changed.
3. Update script or ABI consumers.
4. Update frontend hooks, env, and registration surfaces.
5. Verify with one write path and one downstream read path.

## High-value verification combinations

- Contract write -> `script/script/cast/*_query.sh`
- Contract write -> periphery viewer read
- Deploy script -> repo-local `*/script/network/<network>/*.params`
- Extension factory registration -> `interface/src/config/extensionConfig.ts` plus `.env*`
- Event-emitting write -> `script/script/log/one_click_process.sh` export output
