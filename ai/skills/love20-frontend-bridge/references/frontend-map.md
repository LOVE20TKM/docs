# Frontend Map

## Trace order

1. Start from the route in `interface/src/pages`.
2. Open the page's feature component in `src/components`.
3. If the page can render extension-backed actions, open `src/hooks/extension/**/composite` and the extension base components first.
4. Open core composite hooks in `src/hooks/composite`.
5. Open direct contract hooks in `src/hooks/contracts` or `src/hooks/extension/**/contracts`.
6. Open ABI modules in `src/abis` and config in `src/config`.

## Key directories

- `src/pages`
  Route-level entry points for launch, stake, submit, vote, acting, verify, my, token, dex, extension, and group flows.
- `src/components`
  Feature UI grouped by domain such as `Launch`, `Stake`, `Vote`, `Verify`, `ActionDetail`, `Dex`, and `My`.
- `src/hooks/contracts`
  Wagmi contract wrappers such as `useLOVE20Launch`, `useLOVE20Stake`, `useLOVE20Join`, `useLOVE20Vote`, `useLOVE20RoundViewer`, and `useLOVE20TokenViewer`.
- `src/hooks/composite`
  Higher-level read models such as `useActionDetailData`, `useMyGovData`, and liquidity or reward page adapters.
- `src/hooks/extension`
  Extension detection, `ExtensionCenter` reads, extension reward hooks, and plugin-specific composite logic for LP, group action, and group service flows.
- `src/config/extensionConfig.ts`
  Trusted factory registry and extension-specific tab definitions.
- `src/errors`
  Contract-specific error maps and parsing.

## High-value route clusters

- Launch:
  `src/pages/launch/*`
- Governance and action selection:
  `src/pages/submit/*`, `src/pages/vote/*`
- Action participation:
  `src/pages/acting/*`, `src/pages/action/*`
- Extension-backed action participation:
  `src/pages/acting/join.tsx` detects extension actions through `useExtensionByActionInfoWithCache` and dispatches into `ExtensionActionJoinPanel`.
- Verification:
  `src/pages/verify/*`
- Wallet and reward dashboards:
  `src/pages/my/*`
- DEX and liquidity:
  `src/pages/dex/*`, `src/pages/stake/*`
- Extensions and groups:
  `src/pages/extension/*`, `src/pages/group/*`

## Environment-sensitive areas

- `.env.development*`, `.env.production`, `.env.test`, and `.env.public_test`
  Control contract addresses and environment-specific feature flags.
- `NEXT_PUBLIC_CONTRACT_ADDRESS_EXTENSION_*`
  The effective extension feature gates. If a factory address is absent, that extension type is not registered in `extensionConfig.ts`.
- `NEXT_PUBLIC_TOKEN_PREFIX`
  Only sets a local `isTestEnv` hint in `extensionConfig.ts`; it is not the actual gate used to decide whether extension UI is registered.
