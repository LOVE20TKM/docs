# Data Loading Map

## Aggregated read path

- `useLOVE20RoundViewer.ts`
  Aggregate round-level action, vote, join, and verify reads.
- `useLOVE20TokenViewer.ts`
  Aggregate token list, token detail, and pair info reads.
- `useLOVE20MintViewer.ts`
  Aggregate reward-oriented reads.

## Direct write path

- Hooks in `src/hooks/contracts` wrap contract writes with `useUniversalTransaction`.
- Extension writes also live under `src/hooks/extension/**/contracts` and plugin components that call those hooks.
- Helper wrapper example:
  - `useLOVE20Hub.ts` for `contributeFirstTokenWithETH` and `stakeLiquidity`
- Direct write hook examples:
  - `useLOVE20Stake.ts`
  - `useLOVE20Join.ts`
  - `useLOVE20Vote.ts`
  - `useLOVE20Verify.ts`
  - `useLOVE20Mint.ts`

## Composite read models

- `interface/src/hooks/composite/useActionDetailData.ts`
  Starts from submit and join base data, then switches to `useActionParticipationAdapter` when the action may be extension-backed.
- `interface/src/hooks/extension/base/composite/useActionParticipationAdapter.ts`
  Detects whether an action is extension-backed through `useExtensionByActionInfoWithCache` and switches to extension-specific read paths.
- `interface/src/hooks/extension/base/composite/useExtensionParticipationData.ts`
  Reads `ExtensionCenter.accountsCount`, `ExtensionCenter.isAccountJoined`, and the extension contract's `joinedAmount`.
- `interface/src/hooks/extension/plugins/group/composite/useGetInfoForJoin.ts`
  Group-action join adapter that combines base join round, vote status, balances, allowance, and extension verification info for the group join flow.
- `interface/src/hooks/extension/base/contracts/useIReward.ts`
  Generic extension reward reads and reward-claim writes for contracts implementing `IReward`.
- Other composite hooks build page-specific state on top of viewer contracts and direct hooks.

## ABI and selector layer

- `src/abis/*.ts`
  Typed ABI modules consumed by hooks, including core, extension, extension-group, group, and viewer contracts.
- `src/lib/abiLoader.ts`
  Lazy-load helper for ABI bundles.
- `docs/function-selectors.json`
  Generated selector mapping for the frontend toolchain. When regenerated, it covers extension and group ABI modules too.
- `scripts/generateAbiTs.ts`, `generateFunctionSelectors.ts`, `generateErrorSelectors.ts`
  Frontend ABI and selector generation scripts.

## Extension UI bridge

- `interface/docs/extension.md`
  Notes on factory deploy screens, common action UI, and extension plugin components.
- `src/config/extensionConfig.ts`
  Maps factory addresses to extension type, display name, and action-detail tabs.
- `src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`
  Dispatches extension-backed join flows to LP, group action, or group service plugin panels.

## Error handling

- `src/errors/contractErrorParser.ts`
  Central contract error parsing.
- `src/errors/*ErrorsMap.ts`
  Contract-specific error message maps.
