---
name: love20-prompts
description: "Frame LOVE20 requests into precise prompts and response contracts for protocol explanation, contract interaction, state inspection, troubleshooting, selector decoding, code review, and docs or skill updates. Use when a LOVE20 ask is underspecified, when you want a reusable prompt for another AI agent, or when a broad task should be split into smaller prompts with the right evidence requirements and companion skills."
---

# LOVE20 Prompts

Use this skill to turn a vague LOVE20 request into a prompt that is specific enough for another agent to execute correctly.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/prompt-selection.md`.
2. Choose one prompt family:
   - `references/protocol-and-architecture-prompts.md`
   - `references/interaction-state-and-debug-prompts.md`
   - `references/review-and-doc-sync-prompts.md`
3. Copy the closest template and replace placeholders such as token, round, action, account, network, file, or symptom.
4. Keep only the companion LOVE20 skills that the task actually needs.
5. If one ask mixes explanation, execution, and debugging, split it into multiple prompts.

## Working Rules

- Every prompt should specify:
  - objective
  - entity anchors such as token, action, round, account, network
  - source-of-truth requirements
  - expected output shape
  - conflict handling between docs and code
- Ask for file paths, contract names, function names, or script paths instead of generic descriptions.
- Prefer prompts that force the agent to separate:
  - protocol intent from docs
  - actual behavior from deployed contract repos (`core`, `extension`, `extension-lp`, `extension-group`, `group`)
  - convenience wrappers from core rules
  - current state from indexed history
- When the task could touch immutable on-chain behavior, require the prompt to treat `periphery`, `script`, and `interface` as adapters, examples, or read models rather than the final behavior authority.

## Guardrails

- Do not ask one prompt to both teach the protocol and produce exact write calls unless the user explicitly wants both.
- Do not request debugging help without providing the best available symptom:
  revert string, selector, topic, Chinese UI message, tx hash, or screenshot path.
- Do not request state inspection without naming at least one anchor if it is known:
  token, symbol, actionId, round, account, or network.
- For review prompts, require findings first and force the agent to cite files and lines.
- For docs or skill update prompts, require the agent to validate and mention what was regenerated.

## References

- `references/prompt-selection.md`
- `references/protocol-and-architecture-prompts.md`
- `references/interaction-state-and-debug-prompts.md`
- `references/review-and-doc-sync-prompts.md`
