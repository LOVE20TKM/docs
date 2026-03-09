# Demo Response: runbook-eth-contribute-invalid-recipient (PASS)

最短排查路径：

1. 先判断失败层级
   - 这是 `LOVE20Hub.contributeFirstTokenWithETH` 路径
   - `"Invalid recipient address"` 属于 wrapper precondition failure，不是先看 core launch 规则
2. 先看最快证据
   - `docs/ai/skills/love20-runbooks/references/launch-and-stake-runbooks.md`
   - `periphery/test/LOVE20Hub.contributeWithETH.t.sol`
3. 第一批确认项
   - recipient address 是否是 zero address
   - token address 是否有效
   - ETH helper path 是否真的带了 `value`

为什么先这样看：

- runbook 已明确写了：
  `"Invalid recipient address"` 说明失败发生在 wrapper 进入 core launch logic 之前
- 所以不该一开始就把锅甩给 `ILOVE20Launch`

如果 wrapper 前置项都通过，再继续：

- 打开 `periphery/src/LOVE20Hub.sol`
- 然后才看 `core/src/interfaces/ILOVE20Launch.sol`

结论：

- 失败分类：wrapper-layer failure
- 最相关测试：`periphery/test/LOVE20Hub.contributeWithETH.t.sol`
- 最先确认的原因：recipient 为零地址或 helper 前置参数错误
