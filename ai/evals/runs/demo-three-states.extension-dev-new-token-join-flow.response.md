# Demo Response: extension-dev-new-token-join-flow (PASS)

最接近的起点是 `ExtensionBaseRewardTokenJoin`，落地时直接对照 `extension-lp`，因为它已经把“按 ERC20/LP 数量参与并按权重分配奖励”做成了完整实现。

建议开发顺序：

1. 在 `extension` 框架层确认基类和 join/reward 模型
   先读 `extension/src/ExtensionBaseRewardTokenJoin.sol`、`extension/src/examples/ExampleTokenJoin.sol`、`extension/src/examples/ExampleFactoryTokenJoin.sol`。
2. 写具体 extension contract 与 factory
   最近的文件对是 `extension-lp/src/ExtensionLp.sol`、`extension-lp/src/ExtensionLpFactory.sol`；如果公开接口变了，再同步 `extension-lp/src/interface/ILp.sol` 和 `extension-lp/src/interface/ILpFactory.sol`。
3. 补 deploy 与 network 地址落点
   同步 `extension-lp/script/DeployExtensionLpFactory.s.sol`、`extension-lp/script/deploy/01_deploy_extension_lp_factory.sh`、`extension-lp/script/deploy/99_check.sh`，并确认地址写回 `extension-lp/script/network/<network>/address.extension.lp.params` 和 `extension-lp/script/network/<network>/address.extension.center.params`。
4. 补 focused unit test
   先补 `extension-lp/test/ExtensionLp.t.sol`，覆盖 initialize、join、reward accounting 和 revert path。
5. 补最近的 integration test
   至少同步 `extension-lp/test/integration/Factory.t.sol`、`extension-lp/test/integration/Flow.t.sol`、`extension-lp/test/integration/RewardCalculation.t.sol`。

最少要改的文件簇：

- `extension/src/ExtensionBaseRewardTokenJoin.sol`
- `extension/src/examples/ExampleTokenJoin.sol`
- `extension/src/examples/ExampleFactoryTokenJoin.sol`
- `extension-lp/src/ExtensionLp.sol`
- `extension-lp/src/ExtensionLpFactory.sol`
- `extension-lp/src/interface/ILp.sol`
- `extension-lp/src/interface/ILpFactory.sol`
- `extension-lp/script/DeployExtensionLpFactory.s.sol`
- `extension-lp/script/deploy/01_deploy_extension_lp_factory.sh`
- `extension-lp/test/ExtensionLp.t.sol`
- `extension-lp/test/integration/Factory.t.sol`
- `extension-lp/test/integration/Flow.t.sol`
- `extension-lp/test/integration/RewardCalculation.t.sol`

验收最低线：

1. factory create 成功
2. extension initialize 与 join 正常
3. `ExtensionLp.t.sol`、`Factory.t.sol`、`Flow.t.sol`、`RewardCalculation.t.sol` 通过
4. deploy 后能从 `extension-lp/script/network/<network>/address.extension.lp.params` 找到新地址，并能做一次 registration 或 reward read 验证
