# LOVE20 Skills A/B/C Test Pack

这份清单用于比较不同 AI 模型在有无 LOVE20 skills 辅助时，是否能正确理解并使用 LOVE20 协议。

选用 6 个代表性 case，重点看：

- 是否会选对 skill
- 是否会找对证据
- 是否能区分 docs 和链上行为真值
- 是否能给出可执行答案

## 使用方法

每个 case 对同一个模型跑三次：

1. `A 组`
   只给原始问题，不给任何 skill。
2. `B 组`
   给正确的 LOVE20 skill。
3. `C 组`
   给正确的 LOVE20 skill，并强制统一输出结构。

建议每个回答单独保存，文件名可按下面格式：

- `model-name.case-id.A.md`
- `model-name.case-id.B.md`
- `model-name.case-id.C.md`

`C 组`统一输出结构：

1. `Used skills`
2. `Anchors`
3. `Evidence`
4. `Answer`
5. `Doc-code conflicts`
6. `Next checks`

## Case 1: core-governance-lifecycle-explainer

目标：
测试模型是否能通过 skill 正确理解 LOVE20 治理生命周期。

### A 组 Prompt

```text
请解释 LOVE20 的三阶段治理生命周期，从 stake、submit、vote、join、verify、mint 一直到奖励兑现。要求同时说明协议意图和合约里的真实行为。
```

### B 组 Prompt

```text
Use $love20-core-protocol and $love20-navigator.

请解释 LOVE20 的三阶段治理生命周期，从 stake、submit、vote、join、verify、mint 一直到奖励兑现。要求同时说明协议意图和合约里的真实行为。
```

### C 组 Prompt

```text
Use $love20-core-protocol and $love20-navigator.

请解释 LOVE20 的三阶段治理生命周期，从 stake、submit、vote、join、verify、mint 一直到奖励兑现。要求同时说明协议意图和合约里的真实行为。

请严格按以下结构输出：
1. Used skills
2. Anchors
3. Evidence
4. Answer
5. Doc-code conflicts
6. Next checks
```

主要观察点：

- 是否解释了 phase 和 round 逻辑
- 是否引用核心合约和函数
- 是否把 docs 和 code 分层处理

## Case 2: playbook-launch-child-token

目标：
测试模型能否输出可执行的 LOVE20 子币公平发射交互手册。

### A 组 Prompt

```text
我想让一个用户发起 LOVE20 子币公平发射。请给我精确的交互手册：需要哪些合约、函数、批准、前置条件、时间限制，以及能复用哪些 cast 脚本。
```

### B 组 Prompt

```text
Use $love20-contract-playbooks and $love20-core-protocol.

我想让一个用户发起 LOVE20 子币公平发射。请给我精确的交互手册：需要哪些合约、函数、批准、前置条件、时间限制，以及能复用哪些 cast 脚本。
```

### C 组 Prompt

```text
Use $love20-contract-playbooks and $love20-core-protocol.

我想让一个用户发起 LOVE20 子币公平发射。请给我精确的交互手册：需要哪些合约、函数、批准、前置条件、时间限制，以及能复用哪些 cast 脚本。

请严格按以下结构输出：
1. Used skills
2. Anchors
3. Evidence
4. Answer
5. Doc-code conflicts
6. Next checks
```

主要观察点：

- 是否落到具体 write surface
- 是否说明 approval、余额、等待期
- 是否先给 direct contract surface，再提 helper/script

## Case 3: frontend-trace-token-stat-card

目标：
测试模型能否从前端卡片一路追到真实读取来源。

### A 组 Prompt

```text
LOVE20 页面上某个 token 的统计卡片数据是从哪里来的？请从页面或 hook 一直追到 viewer/合约函数，并指出环境变量和 ABI 入口。
```

### B 组 Prompt

```text
Use $love20-frontend-bridge and $love20-state-and-events.

LOVE20 页面上某个 token 的统计卡片数据是从哪里来的？请从页面或 hook 一直追到 viewer/合约函数，并指出环境变量和 ABI 入口。
```

### C 组 Prompt

```text
Use $love20-frontend-bridge and $love20-state-and-events.

LOVE20 页面上某个 token 的统计卡片数据是从哪里来的？请从页面或 hook 一直追到 viewer/合约函数，并指出环境变量和 ABI 入口。

请严格按以下结构输出：
1. Used skills
2. Anchors
3. Evidence
4. Answer
5. Doc-code conflicts
6. Next checks
```

主要观察点：

- 是否能从 page 到 hook 到 viewer/contract
- 是否给出 ABI 和 env binding
- 是否把 viewer/hook 误当成链上行为真值

## Case 4: runbook-eth-contribute-invalid-recipient

目标：
测试模型是否能按最短路径排查具体失败。

### A 组 Prompt

```text
LOVE20Hub 的 contributeFirstTokenWithETH 失败了，报的是 Invalid recipient address。请给我最短的排查路径和该先看的测试/合约文件。
```

### B 组 Prompt

```text
Use $love20-runbooks and $love20-contract-playbooks.

LOVE20Hub 的 contributeFirstTokenWithETH 失败了，报的是 Invalid recipient address。请给我最短的排查路径和该先看的测试/合约文件。
```

### C 组 Prompt

```text
Use $love20-runbooks and $love20-contract-playbooks.

LOVE20Hub 的 contributeFirstTokenWithETH 失败了，报的是 Invalid recipient address。请给我最短的排查路径和该先看的测试/合约文件。

请严格按以下结构输出：
1. Used skills
2. Anchors
3. Evidence
4. Answer
5. Doc-code conflicts
6. Next checks
```

主要观察点：

- 是否先判断失败层级
- 是否给出最少但关键的检查动作
- 是否会把 wrapper 问题直接误判成 core 问题

## Case 5: selectors-decode-custom-error

目标：
测试模型是否能从 selector 反推 LOVE20 错误来源。

### A 组 Prompt

```text
我有一个 LOVE20 回滚选择器 0xa748da06。请告诉我它对应什么错误、可能来自哪些合约、前端会怎么翻译它。
```

### B 组 Prompt

```text
Use $love20-selectors-and-errors and $love20-runbooks.

我有一个 LOVE20 回滚选择器 0xa748da06。请告诉我它对应什么错误、可能来自哪些合约、前端会怎么翻译它。
```

### C 组 Prompt

```text
Use $love20-selectors-and-errors and $love20-runbooks.

我有一个 LOVE20 回滚选择器 0xa748da06。请告诉我它对应什么错误、可能来自哪些合约、前端会怎么翻译它。

请严格按以下结构输出：
1. Used skills
2. Anchors
3. Evidence
4. Answer
5. Doc-code conflicts
6. Next checks
```

主要观察点：

- 是否能识别 custom error selector
- 是否给出候选合约和声明位置
- 是否能分清前端翻译层和合约声明层

## Case 6: prompts-split-broad-request

目标：
测试模型是否真正理解 skill 的用途，而不是只会直接答题。

### A 组 Prompt

```text
把这个大需求拆成 3 个更精确的 LOVE20 prompts：帮我理解这个协议、告诉我怎么交互、顺便排查页面为什么失败。每个 prompt 都要说明适合搭配哪个 LOVE20 skill。
```

### B 组 Prompt

```text
Use $love20-prompts, $love20-core-protocol, $love20-contract-playbooks, and $love20-runbooks.

把这个大需求拆成 3 个更精确的 LOVE20 prompts：帮我理解这个协议、告诉我怎么交互、顺便排查页面为什么失败。每个 prompt 都要说明适合搭配哪个 LOVE20 skill。
```

### C 组 Prompt

```text
Use $love20-prompts, $love20-core-protocol, $love20-contract-playbooks, and $love20-runbooks.

把这个大需求拆成 3 个更精确的 LOVE20 prompts：帮我理解这个协议、告诉我怎么交互、顺便排查页面为什么失败。每个 prompt 都要说明适合搭配哪个 LOVE20 skill。

请严格按以下结构输出：
1. Used skills
2. Anchors
3. Evidence
4. Answer
5. Doc-code conflicts
6. Next checks
```

主要观察点：

- 是否会拆成 explanation / interaction / debug 三题
- 是否能给每题配对正确 skill
- 是否给出了可直接复用的 prompt

## 快速评分表

每个 case 按这五项打分，每项 `0-2` 分，总分 `10`：

1. `Skill routing`
2. `Anchors`
3. `Evidence quality`
4. `Truth hierarchy`
5. `Actionability`

建议额外记录一句结论：

- `A -> B` 是否提升
- `B -> C` 是否提升
- 这个模型最常见的错误是什么
