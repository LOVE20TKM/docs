# Demo Response: navigator-fair-launch-source-of-truth (PASS)

这个问题建议按下面顺序读：

1. `docs/whitepaper/LOVE20协议设计.md`
   先看公平发射和 claim delay 的设计意图。
2. `docs/ai/skills/love20-navigator/references/source-of-truth.md`
   这里明确了 docs、已部署合约仓库、adapter 层之间的优先级。
3. `core/src/interfaces/ILOVE20Launch.sol`
   先从 launch 相关接口看可读写面。
4. `core/src/LOVE20Launch.sol`
   再落到真实实现，确认 launch、contribute、withdraw、claim 的链上行为。

如果问题进一步追问 claim delay 和阶段窗口，再补看：

- `core/src/interfaces/IPhase.sol`
- `docs/ai/skills/love20-core-protocol/references/governance-lifecycle.md`

简化记法：

- 设计意图先看 `docs`
- 行为真值再看 `core`
- 不要先从 frontend、viewer、hub helper 开始
