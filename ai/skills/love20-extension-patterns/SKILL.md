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
- Distinguish the generic extension framework repo from concrete extension repos such as LP and chain-group.
- Distinguish `extension-group` from `group`: the first defines chain-group extension behavior, the second defines the chain-group NFT protocol the extension depends on.

## References

- `references/extension-framework.md`
- `references/extension-examples.md`
