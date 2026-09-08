---
name: love20-tkm-prompts
description: "Turn underspecified LOVE20 requests into precise prompts and response contracts. Use to frame protocol, interaction, state, debugging, review, or docs tasks, or to split a broad request for another agent with the right evidence and companion skills."
---

# LOVE20 Prompts

Use this skill to turn a vague LOVE20 request into a prompt that is specific enough for another agent to execute correctly.

## Workflow

1. Read `references/prompt-selection.md`.
2. Choose one prompt family:
   - `references/protocol-and-architecture-prompts.md`
   - `references/interaction-state-and-debug-prompts.md`
   - `references/review-and-doc-sync-prompts.md`
3. Read `references/junior-agent-acceptance-cases.md` when you need reusable eval or smoke-test questions for another agent.
4. Use `assets/junior-agent-eval-handbook.md` and `assets/junior-agent-scorecard.csv` when you want a ready-to-run manual evaluation pack for other models.
5. Copy the closest template and replace placeholders such as token, round, action, account, network, file, or symptom.
6. Keep only the companion LOVE20 skills that the task actually needs.
7. If one ask mixes explanation, execution, and debugging, split it into multiple prompts.

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
  - actual behavior from deployed contract repos (`core`, `extension`, `extension-lp`, `extension-group`, `group`, `group-chat`)
  - convenience wrappers from core rules
  - current state from indexed history
- For prompts aimed at junior or generic agents, force a triage step that classifies:
  - base vs extension or group
  - business round vs contract-local round
  - current state vs history
  - protocol truth vs adapter behavior
- If the prompt uses unqualified `action` or `行动`, explicitly say that the term includes extension-backed and group-backed actions unless the task is intentionally scoped to base/core only.
- When validating another agent after a LOVE20 docs or skill update, reuse the acceptance cases in `references/junior-agent-acceptance-cases.md` instead of inventing new eval questions every time.
- When the task touches on-chain behavior, require contract source as authority and treat `periphery`, `script`, `interface-test`, and `interface` as adapters or read models.

## Guardrails

- Do not ask one prompt to both teach the protocol and produce exact write calls unless the user explicitly wants both.
- Do not request debugging help without providing the best available symptom:
  revert string, selector, topic, Chinese UI message, tx hash, or screenshot path.
- Do not request state inspection without naming at least one anchor if it is known:
  token, symbol, actionId, round, account, or network.
- For review prompts, require findings first and force the agent to cite files and lines.
- For docs or skill update prompts, require the agent to validate and mention what was regenerated.
