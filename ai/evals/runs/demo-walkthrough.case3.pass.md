# Demo Response: core-governance-lifecycle-explainer (PASS)

LOVE20 的治理生命周期不是单轮串行，而是滚动流水线：

- round N 在 submit and vote
- round N-1 在 action
- round N-2 在 verify

关键入口：

- `docs/whitepaper/LOVE20协议设计.md`
- `docs/ai/skills/love20-core-protocol/references/governance-lifecycle.md`
- `core/src/interfaces/IPhase.sol`
- `core/src/LOVE20Submit.sol`
- `core/src/LOVE20Vote.sol`
- `core/src/LOVE20Join.sol`
- `core/src/LOVE20Verify.sol`
- `core/src/LOVE20Mint.sol`

从机制上看：

- submit and vote 决定哪些 action 进入本轮并获得治理票
- action phase 负责参与、追加 stake、更新 verification info
- verify phase 负责随机候选和验证打分
- 验证完成后，`LOVE20Mint` 才会准备并兑现治理奖励和行动奖励

文档与实现的关系：

- whitepaper 负责解释三阶段治理和 rolling pipeline 的意图
- `IPhase.sol` 和各 phase-aware core contracts 负责真实链上行为
- 如果文档与实现有差异，行为真值以 `core` 为准
