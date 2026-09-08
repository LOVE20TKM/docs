# Read, Write, And Registration Notes

All paths and commands below belong to `interface-test`. `interface` is updated only through the manual release command after testing.

## Read-path rule

- Prefer composite hooks over ad hoc page state.
- Start with:
  `interface-test/src/hooks/composite/*`,
  `interface-test/src/hooks/contracts/*`,
  `interface-test/src/hooks/extension/base/composite/*`,
  `interface-test/src/hooks/extension/plugins/*/composite/*`
- If a page mixes base and extension actions, trace the action participation adapter before changing UI conditions:
  `interface-test/src/hooks/extension/base/composite/useActionParticipationAdapter.ts`

## Write-path rule

- Write flows should end in hooks using `useUniversalTransaction` from
  `interface-test/src/lib/universalTransaction.ts`.
- Common base write hooks:
  `interface-test/src/hooks/contracts/useLOVE20Launch.ts`,
  `interface-test/src/hooks/contracts/useLOVE20Join.ts`,
  `interface-test/src/hooks/contracts/useLOVE20Vote.ts`,
  `interface-test/src/hooks/contracts/useLOVE20Mint.ts`,
  `interface-test/src/hooks/contracts/useLOVE20Stake.ts`
- Common extension write hooks:
  `interface-test/src/hooks/extension/base/contracts/useExtensionCenter.ts`,
  `interface-test/src/hooks/extension/base/contracts/useIReward.ts`,
  `interface-test/src/hooks/extension/plugins/lp/contracts/useExtensionLp.ts`,
  `interface-test/src/hooks/extension/plugins/lp/contracts/useExtensionLpFactory.ts`,
  `interface-test/src/hooks/extension/plugins/group/contracts/useExtensionGroupAction.ts`,
  `interface-test/src/hooks/extension/plugins/group/contracts/useGroupJoin.ts`,
  `interface-test/src/hooks/extension/plugins/group/contracts/useGroupManager.ts`,
  `interface-test/src/hooks/extension/plugins/group/contracts/useGroupVerify.ts`,
  `interface-test/src/hooks/extension/plugins/group-service/contracts/useExtensionGroupService.ts`

## Extension registration surfaces

`interface-test/docs/extension.md` names the three shared UI registration surfaces:

- Factory deploy component:
  `interface-test/src/components/Extension/Base/Center/ExtensionDeploy.tsx`
- Action public tabs:
  `interface-test/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`
- Join panel:
  `interface-test/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`
- My participation:
  `interface-test/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`

The trusted-factory gate lives in:

- `interface-test/src/config/extensionConfig.ts`
- `.env*` entries such as `NEXT_PUBLIC_CONTRACT_ADDRESS_EXTENSION_FACTORY_*`

## ABI and build checks

- ABI sources live under `interface-test/src/abis`.
- Generation commands live in `interface-test/package.json`:
  `yarn generate:abi`,
  `yarn generate:selectors`,
  `yarn generate:errors`
- Build verification commands:
  `yarn build`
  or `yarn test` when the repo uses build-as-test.

## Acceptance checklist

- The route renders with the expected feature gate.
- Reads refetch or invalidate correctly after writes.
- Error messages still flow through the existing parser and mapping layer in `interface-test/src/errors`.
- New extension UI is impossible to reach when the trusted factory address is absent.
- `yarn test` passes before any `yarn release:test-to-interface-main` publication.
