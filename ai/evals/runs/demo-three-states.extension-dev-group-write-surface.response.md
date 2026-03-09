# Demo Response: extension-dev-group-write-surface (PASS)

不要只说“改 group-service 合约”，这类需求最少涉及 4 处，而且每处都要落到具体文件：

1. group extension 源码
   先改 `extension-group/src/ExtensionGroupService.sol` 和 `extension-group/src/interface/IGroupService.sol`。
2. tests
   先补 `extension-group/test/ExtensionGroupService.t.sol`；如果这个写入口会影响 group-service 的多步流程，再补 `extension-group/test/integration/GroupServiceFlow.t.sol`。
3. frontend handoff
   如果 dApp 要调用这个新写入口，至少同步 `interface/src/hooks/extension/plugins/group-service/contracts/useExtensionGroupService.ts`；如果还要改聚合读，再看 `interface/src/hooks/extension/plugins/group-service/composite/useExtensionParams.ts`。
4. deploy 或公开入口
   如果这个写入口依赖 factory 或部署参数暴露，再同步 `extension-group/script/deploy/06_deploy_group_service_factory.sh`。

最小 file plan：

- `extension-group/src/ExtensionGroupService.sol`
- `extension-group/src/interface/IGroupService.sol`
- `extension-group/test/ExtensionGroupService.t.sol`
- `extension-group/test/integration/GroupServiceFlow.t.sol`
- `interface/src/hooks/extension/plugins/group-service/contracts/useExtensionGroupService.ts`
- `interface/src/hooks/extension/plugins/group-service/composite/useExtensionParams.ts`
- `extension-group/script/deploy/06_deploy_group_service_factory.sh`

完成标准不是“合约改完”，而是：

1. 接口和实现一致
2. `ExtensionGroupService.t.sol` 至少覆盖这条新写入口
3. 影响多步流程时，`GroupServiceFlow.t.sol` 也能跑通
4. 前端 handoff 点已经明确命名，不留“以后再接”的黑盒
