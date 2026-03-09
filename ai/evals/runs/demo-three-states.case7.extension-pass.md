# Demo Response: extension-new-factory-integration (PASS)

如果要新增一种 LOVE20 扩展行动工厂，并接到 `ExtensionCenter`，建议按这个实现顺序看：

1. 扩展框架层
   - `extension/src/interface/IExtension.sol`
   - `extension/src/interface/IExtensionFactory.sol`
   - `extension/src/interface/IExtensionCenter.sol`
2. 中心注册层
   - `extension/src/ExtensionCenter.sol`
   - 这里重点看 action 注册、account/verification info 路由、extension 绑定关系
3. 具体实现层
   - 新的 concrete extension contract
   - 新的 factory contract
4. 初始化和动作绑定
   - `initializeIfNeeded()`
   - `ExtensionCenter.registerActionIfNeeded`

核心集成点：

- concrete extension contract + factory 都要补齐
- action whitelist target 是 extension contract address
- account add/remove 和 verification-info 更新要走 `ExtensionCenter`
- 如果是 reward-bearing flow，还要补 `IReward` 这条面

实现顺序建议：

1. 先确定 base class 选型
2. 写 concrete extension
3. 写 factory
4. 接 `ExtensionCenter`
5. 再补测试和前端 factory registry

边界上要分清：

- `extension` 负责框架和注册模式
- `extension-lp` / `extension-group` 负责具体已部署扩展行为
- 前端 wiring 不是行为真值来源
