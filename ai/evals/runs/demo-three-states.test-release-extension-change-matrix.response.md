# Demo Response: test-release-extension-change-matrix (PASS)

最小充分矩阵：

合并前：

- `extension-lp` 先跑 `extension-lp/test/ExtensionLp.t.sol`
- 如果奖励或轮次公式动了，再补 `extension-lp/test/integration/Flow.t.sol`
- `interface` 如果 ABI 变了先生成，再至少 `yarn build`

发布前：

- 确认目标网络和 repo-local 地址文件，例如 `extension-lp/script/network/<network>/address.extension.lp.params`
- 如果工厂地址或扩展注册有变，同步 `.env*` 和 `extensionConfig.ts`
- 明确 deploy 前要看的脚本入口和要写回的 repo-local 地址文件；只有 query/export 依赖时才补 `script/script/network/<network>/*` mirror

上线后：

- 至少一条 query 或 viewer read
- 至少一条前端 route smoke path

残余风险必须明说：

- 没有 public-test deploy
- 没有前端 smoke
- 没有日志或历史验证
