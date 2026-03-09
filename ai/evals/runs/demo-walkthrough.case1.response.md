# Demo Response: navigator-fair-launch-source-of-truth

先看设计意图，再看已部署不可篡改合约实现。

建议顺序：

1. `docs/whitepaper/LOVE20协议设计.md`
   先确认公平发射、claim delay、round/phase 这些概念的协议意图。
2. `docs/ai/skills/love20-navigator/references/source-of-truth.md`
   这里已经把 LOVE20 的 source-of-truth hierarchy 讲清楚了。
3. `core/src/interfaces/ILOVE20Launch.sol`
   这是公平发射和 claim 相关的首选接口入口。
4. `core/src/LOVE20Launch.sol`
   这里看真实链上实现，而不是只看 frontend 或 helper。

如果问题继续涉及时间窗口或 claim 所属阶段，再补看：

- `core/src/interfaces/IPhase.sol`
- `docs/ai/skills/love20-core-protocol/references/governance-lifecycle.md`

判断原则：

- `docs` 负责解释设计意图。
- `core` 负责解释真实链上行为。
- `periphery`、`script`、`interface` 只作为 adapter、样例或前端集成层，不应先于 `core`。
