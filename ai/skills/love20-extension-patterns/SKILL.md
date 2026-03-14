---
name: love20-extension-patterns
description: "Explain and design LOVE20 extensions, extension factories, and whitelist-based reward flows. Use when asked how the extension framework works, how to build a new extension, how ExtensionCenter should be used, how LP or chain-group extensions behave, or how extension actions map back into LOVE20 rewards."
---

# LOVE20 Extension Patterns

Use this skill to understand or design LOVE20 extension contracts without losing the connection to the underlying action reward flow.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/extension-framework.md`.
2. Read `references/extension-examples.md` for LP and chain-group patterns.
3. Open the specific extension repo that matches the task.
4. Read frontend extension notes only if the task includes interface wiring.

## Extension Decision Tree

1. Decide who the base action participant is:
   - the extension contract itself in the core whitelist model
   - the end user in the extension's own join model
2. Choose the closest join base:
   - `ExtensionBaseRewardJoin` for no-amount joins
   - `ExtensionBaseRewardTokenJoin` for amount-based token joins
   - `GroupJoin` when the user-facing write includes `extension` and `groupId`
3. Decide where membership and verification info live:
   `ExtensionCenter`, the extension contract, or `GroupJoin`.
4. Trace how extension reward accounting maps back to the underlying LOVE20 action reward.

## Working Rules

- Treat `extension`, `extension-lp`, `extension-group`, and `group` as deployed-contract repos with higher priority than adapters or frontend wiring when explaining actual extension behavior.
- Treat the extension contract as the action participant when an action whitelist points to the extension address.
- Use `ExtensionCenter` as the canonical account registry and cross-extension query surface.
- Choose the highest-level base class that matches the join model before designing custom logic.
- Keep the relationship between extension reward accounting and base LOVE20 action rewards explicit.

## Guardrails

- Call `initializeIfNeeded()` before relying on action-bound state.
- Call `registerActionIfNeeded()` before maintaining extension user lists.
- Route user join, exit, and verification info changes through `ExtensionCenter` when the base classes expect it.
- Do not conflate LP extension join accounting with core SL staking or unlock-period rules. Shared LP terminology does not mean they use the same governance-stake semantics.
- Distinguish the generic extension framework repo from concrete extension repos such as LP and chain-group.
- Distinguish `extension-group` from `group`: the first defines chain-group extension behavior, the second defines the chain-group NFT protocol the extension depends on.

## Response Contract

When explaining an extension, include:

1. Participant model.
2. Extension base class or helper contract.
3. User-facing join or reward surface.
4. Registry dependencies such as `ExtensionCenter`, factory, or group manager.
5. How rewards ultimately depend on the underlying LOVE20 action.

## References

- `references/extension-framework.md`
- `references/extension-examples.md`
