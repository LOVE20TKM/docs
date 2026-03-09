# Demo Response: integration-dev-extension-end-to-end (PASS)

先从扩展合约所在 repo 往外串，不要反过来先改前端。

顺序建议：

1. 行为 owner
   先确认 `extension-lp` 或 `extension-group` 里的具体合约和 factory。
2. deploy/address
   同步对应 repo 的 deploy 脚本，先确认 repo-local `*/script/network/<network>/*.params` 已落地，例如 `extension-lp/script/network/<network>/address.extension.lp.params` 或 `extension-group/script/network/<network>/address.extension.group.params`；`script/script/network/<network>/*` 只在 cast/export 要消费这些地址时再同步。
3. script/ABI
   同步 `script/abi/*` 和需要的 `script/script/cast/*` 入口。
4. frontend
   同步 `interface/src/abis/*`、`.env*`、`interface/src/config/extensionConfig.ts`，如果是新扩展类型，再按 `interface/docs/extension.md` 挂到共享扩展 UI。

最小验证链路：

1. deploy 或 create 一次
2. 用 query 脚本或 viewer 读一次
3. 打开对应前端页面确认 factory 或 extension 已被识别
