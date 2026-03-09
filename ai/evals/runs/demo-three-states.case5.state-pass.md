# Demo Response: state-govdata-read-path (PASS)

如果你问的是“当前 govData 这个值从哪里读”，应先分清链上真值、viewer 聚合读模型、frontend hook 三层。

建议路径：

1. 真值和语义先看
   - `core/src/interfaces/IPhase.sol`
   - `core/src/interfaces/ILOVE20Stake.sol`
2. 聚合读模型再看
   - `periphery/src/LOVE20RoundViewer.sol`
   - 关键函数：`govData(address tokenAddress)`
3. 页面 hook 再往上追
   - `interface/src/hooks/contracts/useLOVE20RoundViewer.ts`
   - `interface/src/hooks/composite/useMyGovData.ts`

这里要特别区分：

- direct contract truth：
  `IPhase.sol` 和 phase-aware core contracts 决定当前 round / phase 语义
- viewer read model：
  `LOVE20RoundViewer.govData` 把治理相关读面聚合出来
- frontend bridge：
  `useMyGovData` 会把 `validGovVotes` 和 `govData` 组合成页面所需结构

如果问题是“页面上的这个数为什么这样显示”，继续往 hook 看。
如果问题是“当前链上真实治理状态是什么”，应回到 core 合约和 phase 语义，不要只停在 viewer。
