# Demo Response: frontend-dev-new-extension-plugin

如果这是新的 join/reward 型扩展，最接近的模板是 LP 插件；实际开发顺序不要先写页面，而是先把 ABI、hook、shared registration 和 plugin 组件一起补齐。

建议顺序：

1. ABI 与 contract hook
   先补或仿照 `interface/src/abis/ExtensionLp.ts`、`interface/src/abis/ExtensionLpFactory.ts`，然后同步 `interface/src/hooks/extension/plugins/lp/contracts/useExtensionLp.ts`、`interface/src/hooks/extension/plugins/lp/contracts/useExtensionLpFactory.ts`。
2. 插件组件
   从 `interface/src/components/Extension/Plugins/Lp/LpDeploy.tsx`、`LpActionPublicTabs.tsx`、`LpJoinPanel.tsx`、`LpMyParticipation.tsx`、`LpBasicInfo.tsx`、`LpActionRewardsList.tsx` 起步。
3. 共享注册面
   按 `interface/docs/extension.md` 接到 `interface/src/components/Extension/Base/Center/ExtensionDeploy.tsx`、`interface/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`、`interface/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`、`interface/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`。
4. 配置与环境变量
   更新 `interface/src/config/extensionConfig.ts`，并同步 `interface/.env.development`、`interface/.env.test`、`interface/.env.public_test`、`interface/.env.production` 中的 factory 地址。

文件级改动地图至少包括：

- `interface/src/abis/ExtensionLp.ts`
- `interface/src/abis/ExtensionLpFactory.ts`
- `interface/src/hooks/extension/plugins/lp/contracts/useExtensionLp.ts`
- `interface/src/hooks/extension/plugins/lp/contracts/useExtensionLpFactory.ts`
- `interface/src/hooks/extension/plugins/lp/composite/useExtensionParams.ts`
- `interface/src/hooks/extension/plugins/lp/composite/useMyLpActionData.ts`
- `interface/src/components/Extension/Plugins/Lp/LpDeploy.tsx`
- `interface/src/components/Extension/Plugins/Lp/LpActionPublicTabs.tsx`
- `interface/src/components/Extension/Plugins/Lp/LpJoinPanel.tsx`
- `interface/src/components/Extension/Plugins/Lp/LpMyParticipation.tsx`
- `interface/src/components/Extension/Plugins/Lp/LpBasicInfo.tsx`
- `interface/src/components/Extension/Plugins/Lp/LpActionRewardsList.tsx`
- `interface/src/components/Extension/Base/Center/ExtensionDeploy.tsx`
- `interface/src/components/Extension/Base/Action/ExtensionPublicTabs.tsx`
- `interface/src/components/Extension/Base/Action/ExtensionActionJoinPanel.tsx`
- `interface/src/components/Extension/Base/Action/ExtensionMyParticipation.tsx`
- `interface/src/config/extensionConfig.ts`
- `interface/.env.development`
- `interface/.env.test`
- `interface/.env.public_test`
- `interface/.env.production`

最低验收：

1. trusted factory gate 能在 `extensionConfig.ts` 和 `.env*` 上对齐
2. route 打开后能看到 deploy、public tabs、join panel、my participation 这 4 个共享接入面
3. 写操作最终走 extension hook，并复用 `useUniversalTransaction`
4. 至少执行一次 `yarn generate:abi` 和 `yarn build`
