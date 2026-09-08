---
name: love20-tkm-test-and-release
description: "Plan and run the minimum LOVE20 test, regression, deployment, and release matrix. Use to validate contract, extension, viewer, script, or interface-test changes before merge, public test, manual frontend release, or post-deploy signoff."
---

# LOVE20 Test And Release

Use this skill when the task is to decide, run, or report the checks needed before merge or deployment.

## Workflow

1. Read `references/test-matrix.md`.
2. Read `references/release-checklist.md`.
3. Classify the changed repos and risk surface.
4. Choose the smallest targeted checks first, then the nearest integration or build checks.
5. Add deploy and post-release verification only if the task crosses into real network rollout or env binding.

## Mandatory Triage

Before proposing or running checks, classify the task on these axes:

1. Which repos changed?
2. Is the risk in immutable on-chain behavior, adapter behavior, or frontend-only behavior?
3. Is there a new write surface, a new read surface, or both?
4. Is the target local development, public test, or real release?
5. Does the user want a validation plan, executed checks, or release signoff?

If the work spans several repos, pair this skill with `love20-tkm-integration-dev`.

## Working Rules

- Prefer the minimum sufficient matrix, not a generic "run everything".
- Contract changes should usually include:
  targeted unit or boundary tests,
  nearest integration tests,
  and deploy or address sanity if rollout is in scope.
- Periphery changes should include the affected viewer or hub tests.
- Frontend changes should include ABI or env regeneration when needed, plus a build-level check.
- Extension changes should include factory or registration tests and the nearest end-to-end flow.
- If user-visible history changes, include the log export or indexing refresh path.
- If you did not run a check, say so explicitly.

## Guardrails

- Do not say "release-ready" without naming concrete commands or file-based checks.
- Do not stop at `forge build` or `yarn build` when the task changed write behavior.
- Do not ignore env, address, or ABI synchronization in release guidance.
- Develop and validate frontend changes in `interface-test`; do not edit `interface` directly.
- Publish only after `interface-test` passes, using `yarn release:test-to-interface-main` when the user explicitly requests release.
- Do not hide residual risk when a full deploy or public-test verification was not performed.

## Response Contract

When answering or executing, keep this shape:

1. Risk surface and changed repos.
2. Commands or checks by repo.
3. Pre-deploy requirements.
4. Post-deploy verification.
5. Residual risks or skipped checks.
