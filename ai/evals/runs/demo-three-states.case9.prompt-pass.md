# Demo Response: prompts-rewrite-vague-state-question (PASS)

可以改写成下面这个 prompt：

```text
Use $love20-state-and-events and $love20-frontend-bridge.

我需要追踪 LOVE20 页面上某个数字是怎么来的。

已知锚点：
- token 或 symbol: <填写>
- page / component: <填写，如果未知就写 unknown>
- actionId / round / account: <已知则写，未知可写 unknown>

请输出：
- 当前链上真值应该先看哪个 deployed contract read surface
- 对应的 viewer function 是什么
- 前端直接 hook 和 composite hook 分别是哪一个
- 页面最终是如何把 viewer 返回值拼成这个数字的
- 涉及的精确文件路径和函数名

要求：
- 对当前真值，优先 `core`、`extension`、`extension-lp`、`extension-group`、`group`
- 说明 `periphery` viewer 和 frontend hook 只是 read model / adapter
- 如果页面值依赖派生计算，明确区分 raw state 和 derived metric
```

这个改写比原问题更好，因为它补齐了：

- 任务目标
- 证据要求
- 输出格式
- source-of-truth hierarchy
- 推荐搭配 skill：`love20-state-and-events` + `love20-frontend-bridge`
