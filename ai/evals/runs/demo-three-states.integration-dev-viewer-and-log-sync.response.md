# Demo Response: integration-dev-viewer-and-log-sync (PASS)

检查顺序不要漏层：

1. 先确认字段来自哪个 core 或 extension 合约
2. 再补 periphery viewer
3. 如果它应该出现在历史或导出里，再补 `script/script/log` 流程
4. 最后补前端 hook 和页面

最少要检查：

- viewer 是否已暴露该字段
- log/export 是否在需要时也输出该字段
- frontend hook 是否改到对应 viewer 入口
- 页面是否区分当前值和历史导出值

验证顺序：

1. 合约 read
2. viewer read
3. export 或 log query
4. 前端渲染
