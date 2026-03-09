# Read, Write, And Registration Notes

## Read-path rule

- Prefer composite hooks over ad hoc page state.
- Start with:
  `interface/src/hooks/composite/*`,
  `interface/src/hooks/contracts/*`,
  `interface/src/hooks/extension/base/composite/*`,
  `interface/src/hooks/extension/plugins/*/composite/*`
- If a page mixes base and extension actions, trace the action participation adapter before changing UI conditions:
  `interface/src/hooks/extension/base/composite/useActionParticipationAdapter.ts`

## Write-path rule

- Write flows should end in hooks using `useUniversalTransaction` from
  `interface/src/lib/universalTransaction.ts`.
- Common base write hooks:
  `interface/src/hooks/contracts/useLOVE20Launch.ts`,
  `interface/src/hooks/contracts/useLOVE20Join.ts`,
  `interface/src/hooks/contracts/useLOVE20Vote.ts`,
  `interface/src/hooks/contracts/useLOVE20Mint.ts`,
  `interface/src/hooks/contracts/useLOVE20Stake.ts`
- Common extension write hooks:
  `interface/src/hooks/extension/base/contracts/useExtensionCenter.ts`,
  `interface/src/hooks/extension/base/contracts/useIReward.ts`,
  `interface/src/hooks/extension/plugins/lp/contracts/useExtensionLp.ts`,
  `interface/src/hooks/extension/plugins/lp/contracts/useExtensionLpFactory.ts`,
  `interface/src/hooks/extension/plugins/group/contracts/useExtensionGroupAction.ts`,
  `interface/src/hooks/extension/plugins/group/contracts/useGroupJoin.ts`,
  `interface/src/hooks/extension/plugins/group/contracts/useGroupManager.ts`,
  `interface/src/hooks/extension/plugins/group/contracts/useGroupVerify.ts`,
  `interface/src/hooks/extension/plugins/group-service/contracts/useExtensionGroupService.ts`

## Extension registration surfaces

`interface/docs/extension.md` names the three shared UI registration surfaces:

- Factory deploy component:
  `interface/src/components/Extension/Base/Center/ExtensionDeploy.tsx`
- Action public tabs:
  `interface/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`
- Join panel:
  `interface/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`
- My participation:
  `interface/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`

The trusted-factory gate lives in:

- `interface/src/config/extensionConfig.ts`
- `.env*` entries such as `NEXT_PUBLIC_CONTRACT_ADDRESS_EXTENSION_FACTORY_*`

## ABI and build checks

- ABI sources live under `interface/src/abis`.
- Generation commands live in `interface/package.json`:
  `yarn generate:abi`,
  `yarn generate:selectors`,
  `yarn generate:errors`
- Build verification commands:
  `yarn build`
  or `yarn test` when the repo uses build-as-test.

## Acceptance checklist

- The route renders with the expected feature gate.
- Reads refetch or invalidate correctly after writes.
- Error messages still flow through the existing parser and mapping layer in `interface/src/errors`.
- New extension UI is impossible to reach when the trusted factory address is absent.
