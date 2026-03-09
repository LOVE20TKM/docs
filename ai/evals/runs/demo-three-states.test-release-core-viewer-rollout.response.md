# Demo Response: test-release-core-viewer-rollout (PASS)

发布前：

1. 跑 core 最近的 unit 或 integration
2. 跑对应 periphery viewer 测试
3. 确认 deploy 入口，以及 `core/script/network/<network>/address.params`、`periphery/script/network/<network>/address.params`、`periphery/script/network/<network>/address.core.params`

发布后：

1. 先看 repo-local 地址文件是否已落地
2. 再做一次 cast query 或 viewer read
3. 如果影响历史或导出，再补 `one_click_process.sh`

最低要求不是只看 build 或 deploy 成功，而是：

- core 覆盖
- viewer 覆盖
- address 文件确认
- 一次 post-release read 或 log 验证
