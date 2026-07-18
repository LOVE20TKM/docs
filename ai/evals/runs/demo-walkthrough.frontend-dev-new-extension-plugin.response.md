# Demo Response: frontend-dev-new-extension-plugin

如果这是新的 join/reward 型扩展，最接近的模板是 LP 插件；实际开发顺序不要先写页面，而是先把 ABI、hook、shared registration 和 plugin 组件一起补齐。

建议顺序：

1. ABI 与 contract hook
   先补或仿照 `interface-test/src/abis/ExtensionLp.ts`、`interface-test/src/abis/ExtensionLpFactory.ts`，然后同步 `interface-test/src/hooks/extension/plugins/lp/contracts/useExtensionLp.ts`、`interface-test/src/hooks/extension/plugins/lp/contracts/useExtensionLpFactory.ts`。
2. 插件组件
   从 `interface-test/src/components/Extension/Plugins/Lp/LpDeploy.tsx`、`LpActionPublicTabs.tsx`、`LpJoinPanel.tsx`、`LpMyParticipation.tsx`、`LpBasicInfo.tsx`、`LpActionRewardsList.tsx` 起步。
3. 共享注册面
   按 `interface-test/docs/extension.md` 接到 `interface-test/src/components/Extension/Base/Center/ExtensionDeploy.tsx`、`interface-test/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`、`interface-test/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`、`interface-test/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`。
4. 配置与环境变量
   更新 `interface-test/src/config/extensionConfig.ts`，并同步 `interface-test/.env.development`、`interface-test/.env.test`、`interface-test/.env.public_test`、`interface-test/.env.production` 中的 factory 地址。

文件级改动地图至少包括：

- `interface-test/src/abis/ExtensionLp.ts`
- `interface-test/src/abis/ExtensionLpFactory.ts`
- `interface-test/src/hooks/extension/plugins/lp/contracts/useExtensionLp.ts`
- `interface-test/src/hooks/extension/plugins/lp/contracts/useExtensionLpFactory.ts`
- `interface-test/src/hooks/extension/plugins/lp/composite/useExtensionParams.ts`
- `interface-test/src/hooks/extension/plugins/lp/composite/useMyLpActionData.ts`
- `interface-test/src/components/Extension/Plugins/Lp/LpDeploy.tsx`
- `interface-test/src/components/Extension/Plugins/Lp/LpActionPublicTabs.tsx`
- `interface-test/src/components/Extension/Plugins/Lp/LpJoinPanel.tsx`
- `interface-test/src/components/Extension/Plugins/Lp/LpMyParticipation.tsx`
- `interface-test/src/components/Extension/Plugins/Lp/LpBasicInfo.tsx`
- `interface-test/src/components/Extension/Plugins/Lp/LpActionRewardsList.tsx`
- `interface-test/src/components/Extension/Base/Center/ExtensionDeploy.tsx`
- `interface-test/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`
- `interface-test/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`
- `interface-test/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`
- `interface-test/src/config/extensionConfig.ts`
- `interface-test/.env.development`
- `interface-test/.env.test`
- `interface-test/.env.public_test`
- `interface-test/.env.production`

最低验收：

1. trusted factory gate 能在 `extensionConfig.ts` 和 `.env*` 上对齐
2. route 打开后能看到 deploy、public tabs、join panel、my participation 这 4 个共享接入面
3. 写操作最终走 extension hook，并复用 `useUniversalTransaction`
4. 在 `interface-test` 至少执行一次 `yarn generate:abi` 和 `yarn test`
5. 不直接改 `interface`；正式发布另行确认后运行 `yarn release:test-to-interface-main`
