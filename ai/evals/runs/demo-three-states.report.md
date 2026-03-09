# LOVE20 Skill Benchmark Run Report

- Run file: `docs/ai/evals/runs/demo-three-states.json`
- Run name: `demo-three-states`
- Total benchmark cases: 18
- Cases in run: 18
- Complete cases: 17
- Passed cases: 16
- Primary skill hit rate: 18/18
- Cited files complete rate: 18/18
- Average must-cover score: 91%
- Output-shape pass rate: 17/17

## Case Results

| Case | Status | Primary Skills | Response | Must Cover | Output Shape | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `navigator-fair-launch-source-of-truth` | PASS | hit | ok | 3/3 | pass | demo PASS case |
| `navigator-routing-for-extension-question` | REVIEW | hit | ok | 1/3 | pass | demo REVIEW case: routing hit, but coverage is too shallow |
| `core-governance-lifecycle-explainer` | INCOMPLETE | hit | ok | 0/3 | pending | demo INCOMPLETE case: response exists, but judgement has not been filled yet |
| `core-parent-child-token-behavior` | PASS | hit | ok | 3/3 | pass | demo PASS case for parent-child token explanation |
| `playbook-launch-child-token` | PASS | hit | ok | 3/3 | pass | demo PASS case for contract playbook |
| `playbook-mint-and-burn-rewards` | PASS | hit | ok | 3/3 | pass | demo PASS case for reward playbook |
| `extension-new-factory-integration` | PASS | hit | ok | 3/3 | pass | demo PASS case for extension integration |
| `extension-group-vs-lp-patterns` | PASS | hit | ok | 3/3 | pass | demo PASS case for extension comparison |
| `frontend-trace-token-stat-card` | PASS | hit | ok | 3/3 | pass | demo PASS case for frontend trace |
| `frontend-trace-stake-lp-flow` | PASS | hit | ok | 3/3 | pass | demo PASS case for stake LP frontend trace |
| `selectors-decode-custom-error` | PASS | hit | ok | 3/3 | pass | demo PASS case for selector decoding |
| `selectors-map-chinese-error-message` | PASS | hit | ok | 3/3 | pass | demo PASS case for Chinese error mapping |
| `runbook-eth-contribute-invalid-recipient` | PASS | hit | ok | 3/3 | pass | demo PASS case for wrapper triage |
| `runbook-group-name-invisible-space` | PASS | hit | ok | 3/3 | pass | demo PASS case for Unicode whitespace triage |
| `state-govdata-read-path` | PASS | hit | ok | 3/3 | pass | demo PASS case for state read path |
| `state-reward-and-flow-history` | PASS | hit | ok | 3/3 | pass | demo PASS case for history indexing |
| `prompts-rewrite-vague-state-question` | PASS | hit | ok | 3/3 | pass | demo PASS case for prompt rewrite |
| `prompts-split-broad-request` | PASS | hit | ok | 3/3 | pass | demo PASS case for prompt splitting |

## Details

### Locate source of truth for fair launch and claim delay

- `id`: `navigator-fair-launch-source-of-truth`
- Selected skills: `love20-navigator`
- Response file: `docs/ai/evals/runs/demo-three-states.case1.pass.md`
- Cited files:
  - ok: `docs/whitepaper/LOVE20协议设计.md`
  - ok: `docs/ai/skills/love20-navigator/references/source-of-truth.md`
  - ok: `core/src/interfaces/ILOVE20Launch.sol`
  - ok: `core/src/LOVE20Launch.sol`
- Manual notes: demo PASS case

### Route an extension-related question to the right repos

- `id`: `navigator-routing-for-extension-question`
- Selected skills: `love20-navigator`
- Response file: `docs/ai/evals/runs/demo-three-states.case2.review.md`
- Cited files:
  - ok: `docs/ai/skills/love20-navigator/references/repo-index.md`
  - ok: `extension/README.md`
  - ok: `group/README.md`
- Manual notes: demo REVIEW case: routing hit, but coverage is too shallow

### Explain the three-stage governance lifecycle

- `id`: `core-governance-lifecycle-explainer`
- Selected skills: `love20-core-protocol`
- Response file: `docs/ai/evals/runs/demo-three-states.case3.incomplete.md`
- Cited files:
  - ok: `docs/whitepaper/LOVE20协议设计.md`
  - ok: `core/src/interfaces/IPhase.sol`
- Warnings:
  - must_cover judgement incomplete
  - output_shape judgement incomplete
- Manual notes: demo INCOMPLETE case: response exists, but judgement has not been filled yet

### Explain parent-child token relationship and burn path

- `id`: `core-parent-child-token-behavior`
- Selected skills: `love20-core-protocol`
- Response file: `docs/ai/evals/runs/demo-three-states.case13.core-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-core-protocol/references/protocol-overview.md`
  - ok: `core/src/interfaces/ILOVE20Launch.sol`
  - ok: `core/src/interfaces/ILOVE20Token.sol`
  - ok: `core/src/LOVE20TokenFactory.sol`
- Manual notes: demo PASS case for parent-child token explanation

### Build a concrete launch-token write playbook

- `id`: `playbook-launch-child-token`
- Selected skills: `love20-contract-playbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case4.playbook-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-contract-playbooks/references/operation-playbooks.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/prerequisites-and-timing.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/cast-script-index.md`
  - ok: `core/src/interfaces/ILOVE20Launch.sol`
- Manual notes: demo PASS case for contract playbook

### Build a reward mint and burn playbook

- `id`: `playbook-mint-and-burn-rewards`
- Selected skills: `love20-contract-playbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case14.mint-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-contract-playbooks/references/operation-playbooks.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/cast-script-index.md`
  - ok: `core/src/interfaces/ILOVE20Mint.sol`
  - ok: `periphery/src/LOVE20MintViewer.sol`
- Manual notes: demo PASS case for reward playbook

### Plan a new extension factory integration

- `id`: `extension-new-factory-integration`
- Selected skills: `love20-extension-patterns`
- Response file: `docs/ai/evals/runs/demo-three-states.case7.extension-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-extension-patterns/references/extension-framework.md`
  - ok: `docs/ai/skills/love20-extension-patterns/references/extension-examples.md`
  - ok: `extension/src/interface/IExtensionCenter.sol`
  - ok: `extension/src/ExtensionCenter.sol`
- Manual notes: demo PASS case for extension integration

### Compare group and LP extension patterns

- `id`: `extension-group-vs-lp-patterns`
- Selected skills: `love20-extension-patterns`
- Response file: `docs/ai/evals/runs/demo-three-states.case15.extension-compare-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-extension-patterns/references/extension-examples.md`
  - ok: `extension-lp/src/ExtensionLp.sol`
  - ok: `extension-group/src/ExtensionGroupAction.sol`
  - ok: `extension-group/src/GroupJoin.sol`
- Manual notes: demo PASS case for extension comparison

### Trace a token stats UI card to its data source

- `id`: `frontend-trace-token-stat-card`
- Selected skills: `love20-frontend-bridge`
- Response file: `docs/ai/evals/runs/demo-three-states.case10.frontend-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-frontend-bridge/references/frontend-map.md`
  - ok: `docs/ai/skills/love20-frontend-bridge/references/data-loading-map.md`
  - ok: `periphery/src/LOVE20TokenViewer.sol`
  - ok: `interface/src/hooks/contracts/useLOVE20TokenViewer.ts`
- Manual notes: demo PASS case for frontend trace

### Trace the stake-LP page flow from UI to contract

- `id`: `frontend-trace-stake-lp-flow`
- Selected skills: `love20-frontend-bridge`
- Response file: `docs/ai/evals/runs/demo-three-states.case16.frontend-stake-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-frontend-bridge/references/data-loading-map.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/periphery-and-viewers.md`
  - ok: `interface/src/hooks/composite/useStakeLpPageData.ts`
  - ok: `periphery/src/LOVE20Hub.sol`
- Manual notes: demo PASS case for stake LP frontend trace

### Decode a custom error selector

- `id`: `selectors-decode-custom-error`
- Selected skills: `love20-selectors-and-errors`
- Response file: `docs/ai/evals/runs/demo-three-states.case6.selector-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-selectors-and-errors/references/generated-error-selector-index.md`
  - ok: `docs/ai/skills/love20-selectors-and-errors/references/decoding-workflow.md`
  - ok: `interface/src/errors/contractErrorParser.ts`
  - ok: `interface/src/errors/unifiedErrorMap.ts`
- Manual notes: demo PASS case for selector decoding

### Map a Chinese UI error message back to source

- `id`: `selectors-map-chinese-error-message`
- Selected skills: `love20-selectors-and-errors`
- Response file: `docs/ai/evals/runs/demo-three-states.case12.selector-ui-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-selectors-and-errors/references/source-files.md`
  - ok: `interface/src/errors/contractErrorParser.ts`
  - ok: `interface/src/errors/unifiedErrorMap.ts`
  - ok: `interface/src/errors/errorMessages.ts`
- Manual notes: demo PASS case for Chinese error mapping

### Troubleshoot contribute-with-ETH invalid recipient failure

- `id`: `runbook-eth-contribute-invalid-recipient`
- Selected skills: `love20-runbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case8.runbook-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-runbooks/references/evidence-sources.md`
  - ok: `docs/ai/skills/love20-runbooks/references/launch-and-stake-runbooks.md`
  - ok: `periphery/test/LOVE20Hub.contributeWithETH.t.sol`
  - ok: `periphery/src/LOVE20Hub.sol`
- Manual notes: demo PASS case for wrapper triage

### Troubleshoot group name invisible whitespace failure

- `id`: `runbook-group-name-invisible-space`
- Selected skills: `love20-runbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case17.runbook-group-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-runbooks/references/extensions-and-groups-runbooks.md`
  - ok: `group/test/UnicodeWhitespaceTest.t.sol`
  - ok: `group/test/LOVE20Group.t.sol`
- Manual notes: demo PASS case for Unicode whitespace triage

### Find the current govData read path

- `id`: `state-govdata-read-path`
- Selected skills: `love20-state-and-events`
- Response file: `docs/ai/evals/runs/demo-three-states.case5.state-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-state-and-events/references/entity-lookup-playbooks.md`
  - ok: `docs/ai/skills/love20-state-and-events/references/generated-state-event-index.md`
  - ok: `periphery/src/LOVE20RoundViewer.sol`
  - ok: `interface/src/hooks/composite/useMyGovData.ts`
- Manual notes: demo PASS case for state read path

### Find indexed queries for reward and flow history

- `id`: `state-reward-and-flow-history`
- Selected skills: `love20-state-and-events`
- Response file: `docs/ai/evals/runs/demo-three-states.case11.history-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-state-and-events/references/event-and-indexing.md`
  - ok: `docs/ai/skills/love20-state-and-events/references/generated-state-event-index.md`
  - ok: `script/script/log/sql/stat/flow.sql`
  - ok: `script/script/log/sql/init/02_views.sql`
- Manual notes: demo PASS case for history indexing

### Rewrite a vague state question into a precise prompt

- `id`: `prompts-rewrite-vague-state-question`
- Selected skills: `love20-prompts`
- Response file: `docs/ai/evals/runs/demo-three-states.case9.prompt-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-prompts/references/prompt-selection.md`
  - ok: `docs/ai/skills/love20-prompts/references/interaction-state-and-debug-prompts.md`
  - ok: `docs/ai/skills/love20-state-and-events/SKILL.md`
  - ok: `docs/ai/skills/love20-frontend-bridge/SKILL.md`
- Manual notes: demo PASS case for prompt rewrite

### Split a broad LOVE20 ask into smaller prompts

- `id`: `prompts-split-broad-request`
- Selected skills: `love20-prompts`
- Response file: `docs/ai/evals/runs/demo-three-states.case18.prompts-split-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-prompts/references/prompt-selection.md`
  - ok: `docs/ai/skills/love20-prompts/references/interaction-state-and-debug-prompts.md`
  - ok: `docs/ai/skills/love20-prompts/references/protocol-and-architecture-prompts.md`
- Manual notes: demo PASS case for prompt splitting
