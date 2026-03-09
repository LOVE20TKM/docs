# Demo Response: integration-dev-extension-end-to-end

先锁定行为 owner，再往外同步 adapter。

推荐顺序：

1. 行为 owner repo
   先看具体扩展所在仓库，例如 `extension-lp/src/*` 或 `extension-group/src/*`。这里定义真实的 join、reward、verify 规则。
2. 部署与地址层
   同步对应仓库的 `script/deploy/*`，然后先确认 repo-local `*/script/network/<network>/*.params` 已写入新地址，例如 `extension-lp/script/network/<network>/address.extension.lp.params`、`extension-group/script/network/<network>/address.extension.group.params`、`periphery/script/network/<network>/address.params`；`script/script/network/<network>/*` 只在 cast 或导出链路需要时再同步 mirror。
3. script 交互层
   如果 ABI 或交互入口变化，同步 `script/abi/*` 和需要复用的 `script/script/cast/*`。
4. frontend 层
   同步 `interface/src/abis/*`、`.env*`、`interface/src/config/extensionConfig.ts`；如果这是新扩展类型，再按 `interface/docs/extension.md` 接到 deploy、public tabs、join panel、my participation 这几处共享注册面。

必须对齐的 sync points：

- behavior owner repo
- deploy script 与 repo-local network address 文件
- script ABI/cast 入口
- frontend ABI/env/extensionConfig

最小 end-to-end 验证：

1. 先完成一次 deploy 或 factory create
2. 用 query 脚本或 viewer 确认链上状态已经可读
3. 再打开对应前端页面，确认 route 能识别该 factory 或 extension，并能读到同一份状态
