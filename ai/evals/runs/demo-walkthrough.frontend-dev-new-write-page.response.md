# Demo Response: frontend-dev-new-write-page

起步不要从空白页开始，直接拿现有 join 页面当模板。

推荐顺序：

1. route/page 入口
   先从 `interface/src/pages/acting/join.tsx` 起步，复用它的 route 和页面组织方式。
2. contract hook
   把真正的链上写操作封装到 `interface/src/hooks/contracts/useLOVE20Join.ts` 这种 contract hook 里，不要把交易逻辑直接写进页面。
3. transaction wrapper
   hook 内继续走 `interface/src/lib/universalTransaction.ts`，保持 loading、error、success 的统一处理。
4. ABI 与地址
   ABI 接 `interface/src/abis/LOVE20Join.ts`，地址从 `.env*` 或 config 来，不要在页面硬编码。
5. build 验证
   至少做一次 `yarn build`；如果这个页面改动了共享状态或错误映射，再补对应测试。

要覆盖的重点：

- `interface/src/pages/acting/join.tsx` -> 页面组件 -> `interface/src/hooks/contracts/useLOVE20Join.ts`
- `interface/src/hooks/contracts/useLOVE20Join.ts` -> `interface/src/lib/universalTransaction.ts`
- `interface/src/abis/LOVE20Join.ts` 与地址来源对齐
- build 或 acceptance 验证已经命名
