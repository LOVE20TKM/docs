# Frontend Development Workflow

Make all frontend changes in `interface-test`. Do not edit `interface`; it is the released production target.

## Core route and component clusters

- Base pages:
  `interface-test/src/pages/launch`,
  `interface-test/src/pages/stake`,
  `interface-test/src/pages/submit`,
  `interface-test/src/pages/vote`,
  `interface-test/src/pages/acting`,
  `interface-test/src/pages/verify`,
  `interface-test/src/pages/my`,
  `interface-test/src/pages/dex`
- Extension and group pages:
  `interface-test/src/pages/extension/*`,
  `interface-test/src/pages/group/*`
- Shared extension UI:
  `interface-test/src/components/Extension/Base/*`
- Plugin-specific UI:
  `interface-test/src/components/Extension/Plugins/Lp/*`,
  `interface-test/src/components/Extension/Plugins/Group/*`,
  `interface-test/src/components/Extension/Plugins/GroupService/*`

## Preferred implementation order

1. Pick the closest existing route and plugin cluster.
2. Confirm which reads come from composite hooks and which writes end at contract hooks.
3. Patch the contract hook or extension hook first if the public data or write surface changes.
4. Patch the page and component layer after the hook surface is stable.
5. Update ABI and env-configured addresses when new functions or contracts are introduced.
6. Verify build output and the smallest realistic acceptance path.
7. If formal release is explicitly requested, run `yarn release:test-to-interface-main` only after the `interface-test` branch is clean and verified.

## High-value starting points

- Extension registry and tab wiring:
  `interface-test/src/config/extensionConfig.ts`
- Shared extension deploy UI:
  `interface-test/src/components/Extension/Base/Center/ExtensionDeploy.tsx`
- Shared action surfaces:
  `interface-test/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`,
  `interface-test/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`,
  `interface-test/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`
- Shared extension hooks:
  `interface-test/src/hooks/extension/base/composite/*`,
  `interface-test/src/hooks/extension/base/contracts/*`
- Transaction wrapper:
  `interface-test/src/lib/universalTransaction.ts`

## What a finished frontend change includes

- route or component entry point
- hook and ABI surface aligned
- config and env gating aligned
- user-visible loading, error, and success path still coherent
- build or acceptance verification recorded
- manual release status recorded separately from development completion
