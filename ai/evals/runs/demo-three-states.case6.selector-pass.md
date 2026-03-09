# Demo Response: selectors-decode-custom-error (PASS)

`0xa748da06` 对应的是：

- Error: `StakeAmountMustBeSet`
- Signature: `StakeAmountMustBeSet()`

候选合约范围：

- `ILOVE20Stake`
- 最终应回到 stake 相关 deployed contract repo 去确认原始声明位置

推荐解码路径：

1. 先查 `docs/ai/skills/love20-selectors-and-errors/references/generated-error-selector-index.md`
2. 再看 frontend 解码层：
   - `interface/src/errors/contractErrorParser.ts`
   - `interface/src/errors/unifiedErrorMap.ts`
3. 再回到 ABI mirror 和 Solidity 原始声明

前端中文翻译层面，这个错误目前对应的是：

- `质押数量必须大于0`

所以这类问题要分三层说：

- selector 到 error 名称：`0xa748da06 -> StakeAmountMustBeSet`
- error 所属范围：stake 相关合约面
- frontend 最终展示：由 parser / unified map 翻译成中文消息，而不是它们定义了这个 ABI 本身
