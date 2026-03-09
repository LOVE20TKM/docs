# Demo Response: integration-dev-viewer-and-log-sync

不要只改合约字段，最少要串 4 层：

1. 行为 truth
   先确认字段来自哪个 `core` 或 `extension` 合约。
2. viewer 层
   如果前端或脚本通过聚合读，补到 `periphery/src/LOVE20RoundViewer.sol`、`LOVE20TokenViewer.sol` 或最接近的 viewer。
3. script 日志与导出层
   如果这个字段要进入历史、统计或导出结果，就要同步 `script/script/log/one_click_process.sh` 相关流程，而不是只看当前链上 state。
4. frontend 读取层
   把 viewer 变化接到 `interface/src/hooks/contracts/*Viewer.ts`，再接到 composite hook 或页面。

集成检查清单：

- viewer 已暴露该字段
- log/export 层在需要时也能产出该字段
- frontend hook 和 env/ABI 读取链路已对齐
- 页面明确区分当前状态与历史导出值

验证顺序：

1. 合约原始 read
2. viewer read
3. log export 或 export query
4. 前端最终渲染
