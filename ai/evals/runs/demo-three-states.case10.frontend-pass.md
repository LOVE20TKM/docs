# Demo Response: frontend-trace-token-stat-card (PASS)

如果要追 LOVE20 页面上某个 token 统计卡片的数据来源，建议按这条链看：

1. frontend route / component
   - `interface/src/pages`
   - `interface/src/components`
2. direct contract hook
   - `interface/src/hooks/contracts/useLOVE20TokenViewer.ts`
3. viewer 合约读面
   - `periphery/src/LOVE20TokenViewer.sol`
   - 重点函数：`tokenStatistics(address tokenAddress)`、`tokenDetail(address tokenAddress)`
4. ABI 和环境绑定
   - `interface/src/abis/*.ts`
   - `.env.development*` / `.env.production` / `.env.test`

更具体地说：

- token 统计类卡片，优先怀疑 `useTokenStatistics`
- 它背后对应 `LOVE20TokenViewer.tokenStatistics`
- 如果卡片还混了 launch info，再追 `useTokenDetail` 和 `tokenDetail`

这里的层级要分清：

- viewer / contract function：
  `LOVE20TokenViewer.tokenStatistics` 是聚合读面
- frontend hook chain：
  `useLOVE20TokenViewer.ts` -> `useTokenStatistics`
- ABI / env binding：
  ABI 在 `interface/src/abis`，地址和环境切换受 `.env.*` 控制

如果继续追“这个统计数字的链上真值是什么”，再回到 `core` 合约，而不是把 frontend 聚合层当最终 authority。
