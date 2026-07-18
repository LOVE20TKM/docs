# Demo Response: frontend-dev-new-write-page

起步不要从空白页开始，直接拿现有 join 页面当模板。

推荐顺序：

1. route/page 入口
   先从 `interface-test/src/pages/acting/join.tsx` 起步，复用它的 route 和页面组织方式。
2. contract hook
   把真正的链上写操作封装到 `interface-test/src/hooks/contracts/useLOVE20Join.ts` 这种 contract hook 里，不要把交易逻辑直接写进页面。
3. transaction wrapper
   hook 内继续走 `interface-test/src/lib/universalTransaction.ts`，保持 loading、error、success 的统一处理。
4. ABI 与地址
   ABI 接 `interface-test/src/abis/LOVE20Join.ts`，地址从 `.env*` 或 config 来，不要在页面硬编码。
5. build 验证
   在 `interface-test` 至少做一次 `yarn test`；不直接改 `interface`，正式发布另行运行 `yarn release:test-to-interface-main`。

要覆盖的重点：

- `interface-test/src/pages/acting/join.tsx` -> 页面组件 -> `interface-test/src/hooks/contracts/useLOVE20Join.ts`
- `interface-test/src/hooks/contracts/useLOVE20Join.ts` -> `interface-test/src/lib/universalTransaction.ts`
- `interface-test/src/abis/LOVE20Join.ts` 与地址来源对齐
- build 或 acceptance 验证已经命名
- development 与 manual release 边界已经命名
