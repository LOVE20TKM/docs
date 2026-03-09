# LOVE20 Skill Benchmark Run Report

- Run file: `docs/ai/evals/runs/demo-walkthrough.json`
- Run name: `demo-walkthrough`
- Total benchmark cases: 26
- Cases in run: 26
- Complete cases: 26
- Passed cases: 26
- Primary skill hit rate: 26/26
- Cited files complete rate: 26/26
- Average must-cover score: 100%
- Output-shape pass rate: 26/26

## Case Results

| Case | Status | Primary Skills | Response | Must Cover | Output Shape | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `playbook-launch-child-token` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `playbook-mint-and-burn-rewards` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `core-governance-lifecycle-explainer` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `core-parent-child-token-behavior` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `extension-new-factory-integration` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `extension-group-vs-lp-patterns` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `extension-dev-new-token-join-flow` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `extension-dev-group-write-surface` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `frontend-trace-token-stat-card` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `frontend-dev-new-extension-plugin` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `frontend-dev-new-write-page` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `integration-dev-extension-end-to-end` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `integration-dev-viewer-and-log-sync` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `frontend-trace-stake-lp-flow` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `navigator-fair-launch-source-of-truth` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `navigator-routing-for-extension-question` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `prompts-rewrite-vague-state-question` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `prompts-split-broad-request` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `test-release-extension-change-matrix` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `test-release-core-viewer-rollout` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `runbook-eth-contribute-invalid-recipient` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `runbook-group-name-invisible-space` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `selectors-decode-custom-error` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `selectors-map-chinese-error-message` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `state-govdata-read-path` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |
| `state-reward-and-flow-history` | PASS | hit | ok | 3/3 | pass | demo PASS walkthrough case |

## Details

### Build a concrete launch-token write playbook

- `id`: `playbook-launch-child-token`
- Selected skills: `love20-contract-playbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case4.playbook-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-contract-playbooks/references/operation-playbooks.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/prerequisites-and-timing.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/cast-script-index.md`
  - ok: `core/src/interfaces/ILOVE20Launch.sol`
- Manual notes: demo PASS walkthrough case

### Build a reward mint and burn playbook

- `id`: `playbook-mint-and-burn-rewards`
- Selected skills: `love20-contract-playbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case14.mint-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-contract-playbooks/references/operation-playbooks.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/cast-script-index.md`
  - ok: `core/src/interfaces/ILOVE20Mint.sol`
  - ok: `periphery/src/LOVE20MintViewer.sol`
- Manual notes: demo PASS walkthrough case

### Explain the three-stage governance lifecycle

- `id`: `core-governance-lifecycle-explainer`
- Selected skills: `love20-core-protocol`
- Response file: `docs/ai/evals/runs/demo-walkthrough.case3.pass.md`
- Cited files:
  - ok: `docs/whitepaper/LOVE20协议设计.md`
  - ok: `docs/ai/skills/love20-core-protocol/references/governance-lifecycle.md`
  - ok: `core/src/interfaces/IPhase.sol`
  - ok: `core/src/LOVE20Mint.sol`
- Manual notes: demo PASS walkthrough case

### Explain parent-child token relationship and burn path

- `id`: `core-parent-child-token-behavior`
- Selected skills: `love20-core-protocol`
- Response file: `docs/ai/evals/runs/demo-three-states.case13.core-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-core-protocol/references/protocol-overview.md`
  - ok: `core/src/interfaces/ILOVE20Launch.sol`
  - ok: `core/src/interfaces/ILOVE20Token.sol`
  - ok: `core/src/LOVE20TokenFactory.sol`
- Manual notes: demo PASS walkthrough case

### Plan a new extension factory integration

- `id`: `extension-new-factory-integration`
- Selected skills: `love20-extension-patterns`
- Response file: `docs/ai/evals/runs/demo-three-states.case7.extension-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-extension-patterns/references/extension-framework.md`
  - ok: `docs/ai/skills/love20-extension-patterns/references/extension-examples.md`
  - ok: `extension/src/interface/IExtensionCenter.sol`
  - ok: `extension/src/ExtensionCenter.sol`
- Manual notes: demo PASS walkthrough case

### Compare group and LP extension patterns

- `id`: `extension-group-vs-lp-patterns`
- Selected skills: `love20-extension-patterns`
- Response file: `docs/ai/evals/runs/demo-three-states.case15.extension-compare-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-extension-patterns/references/extension-examples.md`
  - ok: `extension-lp/src/ExtensionLp.sol`
  - ok: `extension-group/src/ExtensionGroupAction.sol`
  - ok: `extension-group/src/GroupJoin.sol`
- Manual notes: demo PASS walkthrough case

### Plan a new token-join extension implementation

- `id`: `extension-dev-new-token-join-flow`
- Selected skills: `love20-extension-dev`
- Response file: `docs/ai/evals/runs/demo-walkthrough.extension-dev-new-token-join-flow.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-extension-dev/references/dev-workflow.md`
  - ok: `docs/ai/skills/love20-extension-dev/references/contract-and-test-checklist.md`
  - ok: `extension/src/ExtensionBaseRewardTokenJoin.sol`
  - ok: `extension/src/examples/ExampleTokenJoin.sol`
  - ok: `extension-lp/src/ExtensionLp.sol`
  - ok: `extension-lp/src/ExtensionLpFactory.sol`
  - ok: `extension-lp/src/interface/ILp.sol`
  - ok: `extension-lp/src/interface/ILpFactory.sol`
  - ok: `extension-lp/script/DeployExtensionLpFactory.s.sol`
  - ok: `extension-lp/script/deploy/01_deploy_extension_lp_factory.sh`
  - ok: `extension-lp/test/ExtensionLp.t.sol`
  - ok: `extension-lp/test/integration/Factory.t.sol`
  - ok: `extension-lp/test/integration/Flow.t.sol`
  - ok: `extension-lp/script/network/thinkium70001_public/address.extension.lp.params`
- Manual notes: demo PASS walkthrough case

### Extend a group-based extension write surface

- `id`: `extension-dev-group-write-surface`
- Selected skills: `love20-extension-dev`
- Response file: `docs/ai/evals/runs/demo-walkthrough.extension-dev-group-write-surface.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-extension-dev/references/dev-workflow.md`
  - ok: `docs/ai/skills/love20-extension-dev/references/contract-and-test-checklist.md`
  - ok: `extension-group/src/ExtensionGroupService.sol`
  - ok: `extension-group/src/interface/IGroupService.sol`
  - ok: `extension-group/test/ExtensionGroupService.t.sol`
  - ok: `extension-group/test/integration/GroupServiceFlow.t.sol`
  - ok: `extension-group/script/deploy/06_deploy_group_service_factory.sh`
  - ok: `interface/src/hooks/extension/plugins/group-service/contracts/useExtensionGroupService.ts`
  - ok: `interface/src/hooks/extension/plugins/group-service/composite/useExtensionParams.ts`
- Manual notes: demo PASS walkthrough case

### Trace a token stats UI card to its data source

- `id`: `frontend-trace-token-stat-card`
- Selected skills: `love20-frontend-bridge`
- Response file: `docs/ai/evals/runs/demo-three-states.case10.frontend-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-frontend-bridge/references/frontend-map.md`
  - ok: `docs/ai/skills/love20-frontend-bridge/references/data-loading-map.md`
  - ok: `periphery/src/LOVE20TokenViewer.sol`
  - ok: `interface/src/hooks/contracts/useLOVE20TokenViewer.ts`
- Manual notes: demo PASS walkthrough case

### Implement a new extension plugin in the dApp

- `id`: `frontend-dev-new-extension-plugin`
- Selected skills: `love20-frontend-dev`
- Response file: `docs/ai/evals/runs/demo-walkthrough.frontend-dev-new-extension-plugin.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-frontend-dev/references/dev-workflow.md`
  - ok: `docs/ai/skills/love20-frontend-dev/references/read-write-and-registration.md`
  - ok: `interface/docs/extension.md`
  - ok: `interface/src/abis/ExtensionLp.ts`
  - ok: `interface/src/abis/ExtensionLpFactory.ts`
  - ok: `interface/src/hooks/extension/plugins/lp/contracts/useExtensionLp.ts`
  - ok: `interface/src/hooks/extension/plugins/lp/contracts/useExtensionLpFactory.ts`
  - ok: `interface/src/hooks/extension/plugins/lp/composite/useExtensionParams.ts`
  - ok: `interface/src/components/Extension/Plugins/Lp/LpDeploy.tsx`
  - ok: `interface/src/components/Extension/Plugins/Lp/LpJoinPanel.tsx`
  - ok: `interface/src/components/Extension/Plugins/Lp/LpMyParticipation.tsx`
  - ok: `interface/src/config/extensionConfig.ts`
  - ok: `interface/.env.development`
  - ok: `interface/src/components/Extension/Base/Center/ExtensionDeploy.tsx`
  - ok: `interface/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`
- Manual notes: demo PASS walkthrough case

### Add a new frontend write flow

- `id`: `frontend-dev-new-write-page`
- Selected skills: `love20-frontend-dev`
- Response file: `docs/ai/evals/runs/demo-walkthrough.frontend-dev-new-write-page.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-frontend-dev/references/dev-workflow.md`
  - ok: `docs/ai/skills/love20-frontend-dev/references/read-write-and-registration.md`
  - ok: `interface/src/lib/universalTransaction.ts`
  - ok: `interface/src/hooks/contracts/useLOVE20Join.ts`
  - ok: `interface/src/pages/acting/join.tsx`
  - ok: `interface/src/abis/LOVE20Join.ts`
  - ok: `interface/package.json`
- Manual notes: demo PASS walkthrough case

### Wire a new extension end to end

- `id`: `integration-dev-extension-end-to-end`
- Selected skills: `love20-integration-dev`
- Response file: `docs/ai/evals/runs/demo-walkthrough.integration-dev-extension-end-to-end.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-integration-dev/references/integration-workflow.md`
  - ok: `docs/ai/skills/love20-integration-dev/references/sync-points.md`
  - ok: `extension-lp/src/ExtensionLp.sol`
  - ok: `extension-lp/src/ExtensionLpFactory.sol`
  - ok: `extension-lp/script/network/thinkium70001_public/address.extension.lp.params`
  - ok: `script/abi/ILp.sol/ILp.json`
  - ok: `script/abi/ILpFactory.sol/ILpFactory.json`
  - ok: `script/script/cast/join_query.sh`
  - ok: `interface/docs/extension.md`
  - ok: `interface/src/config/extensionConfig.ts`
- Manual notes: demo PASS walkthrough case

### Sync a new read surface across viewers and logs

- `id`: `integration-dev-viewer-and-log-sync`
- Selected skills: `love20-integration-dev`
- Response file: `docs/ai/evals/runs/demo-walkthrough.integration-dev-viewer-and-log-sync.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-integration-dev/references/integration-workflow.md`
  - ok: `docs/ai/skills/love20-integration-dev/references/sync-points.md`
  - ok: `periphery/src/LOVE20RoundViewer.sol`
  - ok: `script/script/log/one_click_process.sh`
  - ok: `interface/src/hooks/contracts/useLOVE20RoundViewer.ts`
- Manual notes: demo PASS walkthrough case

### Trace the stake-LP page flow from UI to contract

- `id`: `frontend-trace-stake-lp-flow`
- Selected skills: `love20-frontend-bridge`
- Response file: `docs/ai/evals/runs/demo-three-states.case16.frontend-stake-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-frontend-bridge/references/data-loading-map.md`
  - ok: `docs/ai/skills/love20-contract-playbooks/references/periphery-and-viewers.md`
  - ok: `interface/src/hooks/composite/useStakeLpPageData.ts`
  - ok: `periphery/src/LOVE20Hub.sol`
- Manual notes: demo PASS walkthrough case

### Locate source of truth for fair launch and claim delay

- `id`: `navigator-fair-launch-source-of-truth`
- Selected skills: `love20-navigator`
- Response file: `docs/ai/evals/runs/demo-walkthrough.case1.response.md`
- Cited files:
  - ok: `docs/whitepaper/LOVE20协议设计.md`
  - ok: `docs/ai/skills/love20-navigator/references/source-of-truth.md`
  - ok: `core/src/interfaces/ILOVE20Launch.sol`
  - ok: `core/src/LOVE20Launch.sol`
- Manual notes: demo PASS walkthrough case

### Route an extension-related question to the right repos

- `id`: `navigator-routing-for-extension-question`
- Selected skills: `love20-navigator`
- Response file: `docs/ai/evals/runs/demo-walkthrough.case2.pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-navigator/references/repo-index.md`
  - ok: `extension/README.md`
  - ok: `extension-group/src/ExtensionGroupAction.sol`
  - ok: `group/src/LOVE20Group.sol`
- Manual notes: demo PASS walkthrough case

### Rewrite a vague state question into a precise prompt

- `id`: `prompts-rewrite-vague-state-question`
- Selected skills: `love20-prompts`
- Response file: `docs/ai/evals/runs/demo-three-states.case9.prompt-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-prompts/references/prompt-selection.md`
  - ok: `docs/ai/skills/love20-prompts/references/interaction-state-and-debug-prompts.md`
  - ok: `docs/ai/skills/love20-state-and-events/SKILL.md`
  - ok: `docs/ai/skills/love20-frontend-bridge/SKILL.md`
- Manual notes: demo PASS walkthrough case

### Split a broad LOVE20 ask into smaller prompts

- `id`: `prompts-split-broad-request`
- Selected skills: `love20-prompts`
- Response file: `docs/ai/evals/runs/demo-three-states.case18.prompts-split-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-prompts/references/prompt-selection.md`
  - ok: `docs/ai/skills/love20-prompts/references/interaction-state-and-debug-prompts.md`
  - ok: `docs/ai/skills/love20-prompts/references/protocol-and-architecture-prompts.md`
- Manual notes: demo PASS walkthrough case

### Choose the minimum checks for an extension change

- `id`: `test-release-extension-change-matrix`
- Selected skills: `love20-test-and-release`
- Response file: `docs/ai/evals/runs/demo-walkthrough.test-release-extension-change-matrix.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-test-and-release/references/test-matrix.md`
  - ok: `docs/ai/skills/love20-test-and-release/references/release-checklist.md`
  - ok: `extension-lp/test/ExtensionLp.t.sol`
  - ok: `extension-lp/test/integration/Flow.t.sol`
  - ok: `extension-lp/script/network/thinkium70001_public/address.extension.lp.params`
  - ok: `interface/src/config/extensionConfig.ts`
  - ok: `interface/package.json`
- Manual notes: demo PASS walkthrough case

### Plan release checks for a core plus viewer rollout

- `id`: `test-release-core-viewer-rollout`
- Selected skills: `love20-test-and-release`
- Response file: `docs/ai/evals/runs/demo-walkthrough.test-release-core-viewer-rollout.response.md`
- Cited files:
  - ok: `docs/ai/skills/love20-test-and-release/references/test-matrix.md`
  - ok: `docs/ai/skills/love20-test-and-release/references/release-checklist.md`
  - ok: `core/test/integration/Flow.t.sol`
  - ok: `periphery/test/LOVE20RoundViewer.t.sol`
  - ok: `core/script/network/thinkium70001_public/address.params`
  - ok: `periphery/script/network/thinkium70001_public/address.core.params`
  - ok: `script/script/log/one_click_process.sh`
- Manual notes: demo PASS walkthrough case

### Troubleshoot contribute-with-ETH invalid recipient failure

- `id`: `runbook-eth-contribute-invalid-recipient`
- Selected skills: `love20-runbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case8.runbook-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-runbooks/references/evidence-sources.md`
  - ok: `docs/ai/skills/love20-runbooks/references/launch-and-stake-runbooks.md`
  - ok: `periphery/test/LOVE20Hub.contributeWithETH.t.sol`
  - ok: `periphery/src/LOVE20Hub.sol`
- Manual notes: demo PASS walkthrough case

### Troubleshoot group name invisible whitespace failure

- `id`: `runbook-group-name-invisible-space`
- Selected skills: `love20-runbooks`
- Response file: `docs/ai/evals/runs/demo-three-states.case17.runbook-group-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-runbooks/references/extensions-and-groups-runbooks.md`
  - ok: `group/test/UnicodeWhitespaceTest.t.sol`
  - ok: `group/test/LOVE20Group.t.sol`
- Manual notes: demo PASS walkthrough case

### Decode a custom error selector

- `id`: `selectors-decode-custom-error`
- Selected skills: `love20-selectors-and-errors`
- Response file: `docs/ai/evals/runs/demo-three-states.case6.selector-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-selectors-and-errors/references/generated-error-selector-index.md`
  - ok: `docs/ai/skills/love20-selectors-and-errors/references/decoding-workflow.md`
  - ok: `interface/src/errors/contractErrorParser.ts`
  - ok: `interface/src/errors/unifiedErrorMap.ts`
- Manual notes: demo PASS walkthrough case

### Map a Chinese UI error message back to source

- `id`: `selectors-map-chinese-error-message`
- Selected skills: `love20-selectors-and-errors`
- Response file: `docs/ai/evals/runs/demo-three-states.case12.selector-ui-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-selectors-and-errors/references/source-files.md`
  - ok: `interface/src/errors/contractErrorParser.ts`
  - ok: `interface/src/errors/unifiedErrorMap.ts`
  - ok: `interface/src/errors/errorMessages.ts`
- Manual notes: demo PASS walkthrough case

### Find the current govData read path

- `id`: `state-govdata-read-path`
- Selected skills: `love20-state-and-events`
- Response file: `docs/ai/evals/runs/demo-three-states.case5.state-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-state-and-events/references/entity-lookup-playbooks.md`
  - ok: `docs/ai/skills/love20-state-and-events/references/generated-state-event-index.md`
  - ok: `periphery/src/LOVE20RoundViewer.sol`
  - ok: `interface/src/hooks/composite/useMyGovData.ts`
- Manual notes: demo PASS walkthrough case

### Find indexed queries for reward and flow history

- `id`: `state-reward-and-flow-history`
- Selected skills: `love20-state-and-events`
- Response file: `docs/ai/evals/runs/demo-three-states.case11.history-pass.md`
- Cited files:
  - ok: `docs/ai/skills/love20-state-and-events/references/event-and-indexing.md`
  - ok: `docs/ai/skills/love20-state-and-events/references/generated-state-event-index.md`
  - ok: `script/script/log/sql/stat/flow.sql`
  - ok: `script/script/log/sql/init/02_views.sql`
- Manual notes: demo PASS walkthrough case
