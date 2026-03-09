# Demo Response: test-release-extension-change-matrix

最小充分矩阵分三段。

合并前：

1. `extension-lp`
   先跑最靠近改动面的合约测试，例如 `ExtensionLp.t.sol`；如果奖励公式或轮次逻辑动了，再补 `test/integration/Flow.t.sol` 或 `RewardCalculation.t.sol`。
2. `interface`
   如果 ABI 变了，先跑 `yarn generate:abi`；然后至少做一次 `yarn build`，必要时补 `yarn test`。

发布前：

1. 确认目标网络和 repo-local 地址文件，例如 `extension-lp/script/network/<network>/address.extension.lp.params` 或 `extension-group/script/network/<network>/address.extension.group.params`
2. 如果工厂地址或扩展类型有变，更同步 `interface/.env*` 与 `interface/src/config/extensionConfig.ts`
3. 明确 deploy 前要看的脚本入口和要写回的 repo-local 地址文件；只有 query/export 依赖时才补 `script/script/network/<network>/*` mirror

上线后：

1. 做一次 query 或 viewer read，确认 extension 地址、factory 绑定和关键状态
2. 打开对应前端 route，确认 feature gate 和读取链路正常

残余风险要明确写出：

- 如果没有 public-test deploy，只能算 merge-ready，不能算 release-ready
- 如果没有做前端 smoke path 或日志验证，也要显式保留风险
