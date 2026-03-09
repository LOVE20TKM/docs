# Demo Response: selectors-map-chinese-error-message (PASS)

“链上交易失败，流动性不足，请稍后重试” 这种中文提示，要倒查三层：

1. frontend parser heuristic
   - `interface/src/errors/contractErrorParser.ts`
2. unified selector / name map
   - `interface/src/errors/unifiedErrorMap.ts`
3. 中文文案来源
   - `interface/src/errors/errorMessages.ts`

回答这类问题时，不要直接说“这是哪个合约抛的”。
更准确的说法是：

- parser 先根据 selector、error name、RPC/gas 特征做归类
- unified map 再把它映射到统一错误类型
- `errorMessages.ts` 再给出中文文案

ABI / 合约范围要这样交代：

- 如果最后能解到具体 selector，就回到 `script/abi` 和对应 deployed contract repo 确认范围
- 如果只是前端 heuristic 命中的“流动性不足”类消息，那它可能对应的是一类 raw error category，不一定已经唯一定位到单个 LOVE20 合约

所以这题的重点不是只找一个合约名，而是把：

- parser 规则
- raw error category
- ABI / contract scope

这三层分开说清楚
