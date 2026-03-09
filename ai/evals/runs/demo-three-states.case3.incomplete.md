# Demo Response: core-governance-lifecycle-explainer (INCOMPLETE)

LOVE20 不是“一个 round 做完再开始下一个 round”，而是滚动流水线：

- round N 在 submit and vote
- round N-1 在 action
- round N-2 在 verify

主要合约入口：

- `core/src/interfaces/IPhase.sol`
- `core/src/LOVE20Submit.sol`
- `core/src/LOVE20Vote.sol`
- `core/src/LOVE20Join.sol`
- `core/src/LOVE20Verify.sol`
- `core/src/LOVE20Mint.sol`

如果先看文档，再看实现：

1. `docs/whitepaper/LOVE20协议设计.md`
2. `docs/ai/skills/love20-core-protocol/references/governance-lifecycle.md`
3. `core/src/interfaces/IPhase.sol`
4. `core/src/*.sol`

这份回答已经命中主 skill，也有真实文件入口，但还没把 must-cover judgement 填完，所以保留成 INCOMPLETE 样例。
