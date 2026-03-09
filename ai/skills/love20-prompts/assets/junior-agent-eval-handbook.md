# LOVE20 Junior-Agent Eval Handbook

Use this handbook to test another model against the current LOVE20 skills and source-of-truth rules.

## Goal

Measure whether a model can avoid the most common LOVE20 mistakes:

- confusing business round with contract-local `currentRound()`
- defaulting every join or claim flow to core contracts
- missing extension and group routing
- treating frontend, scripts, or periphery as immutable behavior truth

## Recommended Test Modes

Run the same case set in one or more modes:

1. `bare`
   Ask only the question.
   Purpose: measure the model's raw LOVE20 understanding.
2. `skills`
   Give the model the relevant `SKILL.md` files and acceptance-case question.
   Purpose: measure whether the skills are sufficient to guide the model.
3. `skills+code`
   Give the model the relevant skills plus the minimum code and reference files.
   Purpose: measure whether the model can land on the actual source of truth.

For comparison, keep the case wording identical across modes.

## Case Set

Use the acceptance cases in:

- `docs/ai/skills/love20-prompts/references/junior-agent-acceptance-cases.md`

Recommended case order:

1. `A1` round translation
2. `A2` base vs extension join surface
3. `A3` chain-group join flow
4. `A4` extension reward claim
5. `A5` frontend branching on `acting/join`
6. `A6` extension participation state source
7. `A7` selector coverage and stale catalogs
8. `A8` prompt handoff for another agent

## Stable Test Procedure

For each model:

1. Start a fresh chat for each case.
2. Keep temperature and reasoning settings fixed if the platform exposes them.
3. Use the same case wording for every model.
4. Give only the materials required for the chosen mode.
5. Score immediately after each answer with the CSV sheet.

## Minimal Context Per Mode

### `bare`

Provide:

- only the case question

### `skills`

Provide:

- the case question
- the relevant LOVE20 `SKILL.md` files
- if the case is prompt-focused, also provide `love20-prompts/SKILL.md`

### `skills+code`

Provide:

- the case question
- the relevant `SKILL.md` files
- the specific minimum sources named in `junior-agent-acceptance-cases.md`

Do not dump the entire repo unless you want to test long-context retrieval rather than reasoning quality.

## Default Evaluator Prompt

Use this wrapper when sending a case to another model:

```text
Please answer the following LOVE20 question.

Requirements:
- first decide whether this is a base LOVE20, extension, or group scenario if that distinction matters
- if round or phase is relevant, distinguish business round from contract-local currentRound()
- if docs and code conflict, treat deployed contract repos as behavior truth
- cite the file paths you relied on when sources are provided
- keep the answer concise but explicit

Question:
<paste case question>
```

## Pass-Fail Rules

Apply the case-specific rules from `junior-agent-acceptance-cases.md`.

Also mark the answer `fail` if any of these happen:

- it answers a timing question without naming the round model
- it answers a join or reward question without classifying base vs extension vs group
- it uses `periphery`, `script`, or `interface` as behavior truth for immutable contract behavior
- it confidently says a selector does not exist without considering stale generated catalogs

## Suggested Score Scale

- `2`: fully correct and grounded
- `1`: directionally correct but missing one important constraint
- `0`: materially wrong or based on the wrong source-of-truth layer

## Common Failure Tags

Use one or more of these in the CSV:

- `round-model`
- `surface-routing`
- `extension-missed`
- `group-missed`
- `wrong-truth-layer`
- `frontend-only`
- `selector-stale`
- `prompt-too-generic`

## Result Summary Template

After testing one model, summarize like this:

```text
Model: <name>
Mode: <bare / skills / skills+code>
Passes: <n>/8
Main failure tags:
- <tag>
- <tag>

Most useful note:
- <one-sentence conclusion about whether the model can safely use the LOVE20 skills>
```

## Recommended First Comparison

If you want the fastest useful benchmark:

1. run `A1`, `A2`, `A4`, `A5`, and `A7`
2. test each model in `bare` and `skills`
3. only run `skills+code` for models that are close to passing in `skills`
