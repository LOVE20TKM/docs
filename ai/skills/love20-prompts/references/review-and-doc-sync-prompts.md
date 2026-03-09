# Review and Doc Sync Prompts

## Ask for a code or contract review

Recommended skills:

- the most relevant domain skill for the changed area
- add `$love20-runbooks` if the diff affects failure handling

Template:

```text
Use the relevant LOVE20 skill for this diff.

Review the changes related to <area>.

Requirements:
- findings first, ordered by severity
- focus on bugs, behavioral regressions, security or correctness risks, and missing tests
- cite exact files and line references
- keep summaries brief after the findings

Context:
- changed files: <paths or repo area>
- expected behavior: <what should remain true>
```

## Ask for a docs or skill update

Recommended skills:

- choose the domain skill that matches the changed area
- add `$love20-prompts` only if you want the output phrasing or prompt contract improved too

Template:

```text
Use the relevant LOVE20 skill for this area.

Update the LOVE20 docs or skills for <topic> based on the current codebase.

Requirements:
- read the current docs and the current implementation
- preserve the source-of-truth hierarchy
- make the smallest set of edits needed
- regenerate any derived references if the skill has generator scripts
- report which files changed and what was validated
- treat deployed contract repos as higher priority than wrappers, scripts, or frontend layers when updating behavior-facing docs or skills
```

## Ask for a reusable answerbook entry

Recommended skills:

- `$love20-prompts`
- plus the domain skill for the topic

Template:

```text
Use $love20-prompts and the relevant LOVE20 domain skill.

Create a reusable answer pattern for the recurring LOVE20 question:
<question pattern>

Deliver:
- a short canonical answer
- the minimum evidence sources that should always be checked
- a follow-up checklist for when the question becomes more specific
- the best companion LOVE20 skill to use for deeper investigation

Requirements:
- identify which source is design intent and which source is behavior truth
- keep adapters and frontend layers secondary unless the recurring question is explicitly about them
```
