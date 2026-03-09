# LOVE20 One-File Test Pack

把本文件的 `给模型的完整提示词` 整段复制给你要测试的模型。

模型回答完后，把它的完整回复原样发回给我。我会按同一份题目和隐含评分标准帮你评估：

- 每题 `pass / fail`
- 每题 `0 / 1 / 2` 分
- 总分
- 主要错误类型

## 给模型的完整提示词

```text
你现在要回答一组关于 LOVE20 协议的测试题。

请严格遵守以下要求：

1. 如果题目涉及 join、claim、verify，先判断这是 base LOVE20、extension，还是 group 场景。
2. 如果题目涉及 round 或 phase，先区分：
   - business round（白皮书/业务语义）
   - contract-local currentRound()（具体合约自己的 round）
3. 如果 docs、frontend、script、periphery 和 deployed contract code 的说法冲突，以 deployed contract repo 的行为为准。
4. 每题都单独作答，不要把多题混在一起。
5. 每题都用下面固定格式输出：

### A?
- Answer:
- Why:
- Files:

其中：
- `Answer` 用简洁结论回答
- `Why` 说明关键判断依据
- `Files` 列出你依赖的文件路径；如果你没有文件依据，就明确写 `none`

6. 不要省略题号，不要跳题。
7. 不要写泛泛而谈的 LOVE20 总介绍，只回答题目本身。

测试题如下：

### A1
同一时刻如果 submit/vote 合约的 round 是 3，那么 join/random 和 verify 分别应该怎么理解？

### A2
一个 action 要调用 LOVE20Join，还是扩展合约，还是 GroupJoin？

### A3
如何加入链群行动？

### A4
LP 行动奖励怎么领？

### A5
acting/join 页面怎么判断走普通行动还是扩展行动？

### A6
扩展行动的参与人数和参与金额从哪里读？

### A7
为什么某个 GroupJoin 或 ExtensionCenter 的 selector 在旧索引里查不到？

### A8
帮我写一个让别的 AI 解释 LOVE20 join 流程的 prompt。
要求这个 prompt 里必须约束：
- base vs extension vs group 的分类
- business round vs contract-local round 的分类
- source of truth 的优先级
- 输出格式
```

## 你发回给我的内容

只需要把目标模型的完整回复原样贴回来。

我会直接返回：

1. 每题得分
2. 总分
3. 哪几题 `pass / fail`
4. 错误假设是什么
5. 如果要修 skills，应该修哪里
