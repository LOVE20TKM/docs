# Demo Response: frontend-trace-stake-lp-flow (PASS)

`stake LP` 页面链路建议按这条顺序追：

1. route / page / component
   - `interface/src/pages/stake/*`
   - 对应 stake 组件
2. composite read hook
   - `interface/src/hooks/composite/useStakeLpPageData.ts`
3. direct contract hooks
   - `interface/src/hooks/contracts/useLOVE20TokenViewer.ts`
   - 以及 stake / hub 相关 write hooks
4. write target contracts
   - helper path：`periphery/src/LOVE20Hub.sol` -> `stakeLiquidity`
   - protocol truth：`core/src/interfaces/ILOVE20Stake.sol`

页面先读什么：

- `tokenPairInfoWithAccount`
- allowance 相关读面

allowance checks：

- 页面会先看 token / pair allowance 是否满足
- 只有满足后才走 helper 或 direct write 路径

最后打到哪：

- UI 常会通过 `LOVE20Hub.stakeLiquidity` 简化多步流程
- 但真实协议写面仍然要回到 `ILOVE20Stake`

所以这题要明确：

- page-level data flow：`useStakeLpPageData`
- allowance checks：先于 write
- write target contracts：helper 可用，但 core 才是行为真值
