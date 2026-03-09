# Demo Response: core-parent-child-token-behavior (PASS)

LOVE20 是父子币树模型，不是单一 token 反复扩容。

核心关系：

- root token 会继续派生 child token
- child token creation 走 `launchToken(symbol, parentTokenAddress)`
- token tree 由 `core/src/LOVE20TokenFactory.sol` 建立

这条路径里最重要的合约面：

- `core/src/interfaces/ILOVE20Launch.sol`
- `core/src/interfaces/ILOVE20Token.sol`
- `core/src/LOVE20TokenFactory.sol`
- `core/src/LOVE20Token.sol`

容易被误读的点：

- 文档会先讲公平发射和 token tree 的设计意图
- 真实行为还是要回到 `ILOVE20Launch`、`LOVE20TokenFactory`、`LOVE20Token`
- `burnForParentToken(amount)` 不属于治理奖励 mint 路径，它是 `LOVE20Token` 上的 parent-pool redemption

所以这题要分清：

- parent / child token model：
  token tree + child launch
- burn path semantics：
  `burnForParentToken` 是资产经济学路径，不是 reward mint
- source of truth：
  docs 讲设计，core 合约讲真实行为
