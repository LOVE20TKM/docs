# Demo Response: test-release-core-viewer-rollout

准备上 public test 时，按这个顺序看：

1. core 覆盖
   先跑最接近改动面的 unit 或 boundary，再补最近的 integration，例如 `core/test/integration/Flow.t.sol`。
2. periphery 覆盖
   viewer 改了就跑对应 viewer 测试，而不是只看 core。
3. network/address 文件
   deploy 前确认目标网络目录、deploy 脚本入口，以及 `core/script/network/<network>/address.params`、`periphery/script/network/<network>/address.params`、`periphery/script/network/<network>/address.core.params`；`script/script/network/<network>/*` 只作为后续 cast/export 消费层。

上 public test 之后：

1. 先确认 repo-local 地址文件已经写到预期位置
2. 再用 cast query 或 viewer read 验证新地址下的真实读数
3. 如果改动影响历史或导出，补跑 `script/script/log/one_click_process.sh`

建议命令和检查应该至少覆盖：

- core 的最近测试
- periphery 的最近 viewer 测试
- 一次 deploy 后的 address 文件确认
- 一次 post-release read 或 log 验证

如果这些只做了本地验证，没有 public-test 实跑，就不能写成已完成 release signoff。
