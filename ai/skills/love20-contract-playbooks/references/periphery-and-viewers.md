# Periphery and Viewers

## LOVE20Hub

- File:
  `periphery/src/LOVE20Hub.sol`
- Purpose:
  Wrap common multi-step writes into simpler entry points.
- Positioning:
  Treat hub functions as convenience examples, not as the primary write surface.
- Current high-value flows:
  - `contributeFirstTokenWithETH`
  - `stakeLiquidity`

## LOVE20TokenViewer

- File:
  `periphery/src/LOVE20TokenViewer.sol`
- Purpose:
  Aggregate token catalog, parent-child token lists, launch detail, and pair detail reads.
- Frontend hook example:
  `interface/src/hooks/contracts/useLOVE20TokenViewer.ts`

## LOVE20RoundViewer

- File:
  `periphery/src/LOVE20RoundViewer.sol`
- Purpose:
  Aggregate per-round action, vote, join, verify, and account-state reads.
- Frontend hook example:
  `interface/src/hooks/contracts/useLOVE20RoundViewer.ts`

## LOVE20MintViewer

- File:
  `periphery/src/LOVE20MintViewer.sol`
- Purpose:
  Aggregate reward-focused reads for dashboards and reward pages.

## Usage guidance

- Treat deployed contract repos (`core`, `extension`, `extension-lp`, `extension-group`, `group`) as the primary behavior source.
- Use core interfaces when you need the canonical write surface or exact protocol state variables.
- Default to direct `cast call` / `cast send` against the canonical interface.
- Introduce hub functions only after showing the direct target contract path, and only when the helper materially simplifies the user flow.
- Use viewer contracts when you need paginated, aggregated, or page-level data that would otherwise require many calls.
- Check periphery tests in `periphery/test` when you need example usage patterns.
