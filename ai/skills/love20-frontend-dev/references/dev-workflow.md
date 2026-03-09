# Frontend Development Workflow

## Core route and component clusters

- Base pages:
  `interface/src/pages/launch`,
  `interface/src/pages/stake`,
  `interface/src/pages/submit`,
  `interface/src/pages/vote`,
  `interface/src/pages/acting`,
  `interface/src/pages/verify`,
  `interface/src/pages/my`,
  `interface/src/pages/dex`
- Extension and group pages:
  `interface/src/pages/extension/*`,
  `interface/src/pages/group/*`
- Shared extension UI:
  `interface/src/components/Extension/Base/*`
- Plugin-specific UI:
  `interface/src/components/Extension/Plugins/Lp/*`,
  `interface/src/components/Extension/Plugins/Group/*`,
  `interface/src/components/Extension/Plugins/GroupService/*`

## Preferred implementation order

1. Pick the closest existing route and plugin cluster.
2. Confirm which reads come from composite hooks and which writes end at contract hooks.
3. Patch the contract hook or extension hook first if the public data or write surface changes.
4. Patch the page and component layer after the hook surface is stable.
5. Update ABI and env-configured addresses when new functions or contracts are introduced.
6. Verify build output and the smallest realistic acceptance path.

## High-value starting points

- Extension registry and tab wiring:
  `interface/src/config/extensionConfig.ts`
- Shared extension deploy UI:
  `interface/src/components/Extension/Base/Center/ExtensionDeploy.tsx`
- Shared action surfaces:
  `interface/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`,
  `interface/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`,
  `interface/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`
- Shared extension hooks:
  `interface/src/hooks/extension/base/composite/*`,
  `interface/src/hooks/extension/base/contracts/*`
- Transaction wrapper:
  `interface/src/lib/universalTransaction.ts`

## What a finished frontend change includes

- route or component entry point
- hook and ABI surface aligned
- config and env gating aligned
- user-visible loading, error, and success path still coherent
- build or acceptance verification recorded
