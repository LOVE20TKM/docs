# LOVE20 Skills Model Comparison Benchmark

这份文档定义一套面向多模型横向比较的人工评测方法。目标不是测试模型会不会“背答案”，而是测试模型在给定 LOVE20 skills 后，是否能更可靠地：

- 选对 skill
- 找对证据
- 说清协议意图和链上真实行为的区别
- 给出可以落地的 LOVE20 操作或排查答案

这套 benchmark 适合比较高、中、低不同档位模型，尤其适合观察中低端模型在 skill 加持前后是否有明显提升。

## 1. 评测目标

重点看四件事：

1. `理解`
   是否正确理解 LOVE20 的核心机制、术语和阶段流程。
2. `导航`
   是否能找到正确的 docs、repo、合约、viewer、hook、脚本入口。
3. `执行`
   是否能把问题回答成具体的交互手册、状态读取路径或排查步骤。
4. `守边界`
   是否知道 `docs` 是设计意图，`core`、`extension`、`extension-lp`、`extension-group`、`group` 才是链上行为真值。

## 2. 实验分组

每个模型建议跑三组，观察 skill 的边际收益：

1. `A 组：No Skill`
   不提供任何 LOVE20 skill，只给原始问题。
2. `B 组：Skill Only`
   提供正确的 LOVE20 skill，但不强制输出格式。
3. `C 组：Skill + Output Contract`
   提供正确的 LOVE20 skill，并强制统一输出结构。

如果模型很弱，优先比较 `A` 和 `C`。这两组的差异通常最明显。

## 3. 统一输出结构

`C 组`统一要求模型按下面结构回答：

1. `Used skills`
2. `Anchors`
3. `Evidence`
4. `Answer`
5. `Doc-code conflicts`
6. `Next checks`

字段要求：

- `Used skills`
  明确写出用了哪些 LOVE20 skills。
- `Anchors`
  写清 token、symbol、round、actionId、account、network、page、tx hash 中已知的锚点。
- `Evidence`
  给出精确文件路径，并尽量带上合约名、函数名、hook 名称、脚本名。
- `Answer`
  直接回答问题，不要只做泛泛概述。
- `Doc-code conflicts`
  如果文档和实现不一致，必须显式写出来。
- `Next checks`
  给出最小下一步验证动作。

## 4. 题型设计

建议至少跑 8 题，覆盖解释、交互、读取、排查、拆题五类能力。

### Case 1: 协议机制解释

目标：测试模型能否通过 skill 理解 LOVE20 的核心阶段流程。

推荐 skill：

- `$love20-navigator`
- `$love20-core-protocol`

Prompt：

```text
Use $love20-navigator and $love20-core-protocol.

请解释 LOVE20 的三阶段治理生命周期，从 stake、submit、vote、join、verify、mint 到奖励兑现。

要求：
- 区分文档里的协议意图和合约里的真实行为
- 给出关键合约、接口和函数
- 如果 docs 和 code 冲突，要直接指出，并把 code 当作行为真值
```

主要看点：

- 是否正确解释阶段和轮次逻辑
- 是否给出核心合约和函数，而不是只给概念
- 是否会把 docs 和 code 混成一层

### Case 2: 文档与实现对比

目标：测试模型是否知道“先看哪层，哪层是真值”。

推荐 skill：

- `$love20-navigator`
- `$love20-core-protocol`

Prompt：

```text
Use $love20-navigator and $love20-core-protocol.

请对比 LOVE20 的公平发射和 claim delay：
- 文档怎么说
- 当前实现怎么做
- 哪些文件应该被视为 source of truth

要求：
- docs 和 code 分开引用
- 不要掩盖冲突或歧义
- 行为真值优先看 deployed contract repos
```

主要看点：

- 是否给出准确 repo 和文件路径
- 是否理解 source-of-truth hierarchy
- 是否能说出冲突而不是“自动圆回来”

### Case 3: 合约交互手册

目标：测试模型能否把协议理解转换成可执行操作。

推荐 skill：

- `$love20-contract-playbooks`

Prompt：

```text
Use $love20-contract-playbooks.

我想让一个用户发起 LOVE20 子币公平发射。请给我精确的交互手册：
- 需要调用哪些合约和函数
- 需要哪些 approval、余额、阶段限制、等待期
- 可以复用哪些 cast 脚本
- 发交易前要先读哪些状态

要求：
- 先给 direct deployed contract surface
- 脚本和 helper 只当 convenience path，不要当行为真值
```

主要看点：

- 是否能落到具体 write surface
- 是否知道先读哪些状态再发交易
- 是否能区分 core surface 和 helper wrapper

### Case 4: 读路径追踪

目标：测试模型是否能从页面一路追到 truth source。

推荐 skill：

- `$love20-state-and-events`
- `$love20-frontend-bridge`

Prompt：

```text
Use $love20-state-and-events and $love20-frontend-bridge.

请追踪 LOVE20 某个 token 统计卡片的数据来源：
- 页面或组件
- hook
- viewer 或合约函数
- 是否还用了 indexed history 或 SQL

要求：
- current truth source 和 frontend read model 要区分开
- 给出精确文件路径和函数名
```

主要看点：

- 是否能从 UI tracing 到 hook 和 viewer
- 是否把 viewer/hook 错当成行为真值
- 是否能区分 current state 和 indexed history

### Case 5: 失败排查

目标：测试模型能否借助 skill 做最短路径排查。

推荐 skill：

- `$love20-runbooks`
- `$love20-selectors-and-errors`

Prompt：

```text
Use $love20-runbooks and $love20-selectors-and-errors.

LOVE20Hub 的 contributeFirstTokenWithETH 失败了，提示 Invalid recipient address。

请给出：
- 最先检查的状态
- 最可能的失败层
- 该先看的测试、合约或前端文件
- 哪些读操作能最快确认根因
```

主要看点：

- 是否先排 wrapper layer 还是直接怪 core
- 是否能给出短链路排查，而不是大而全 checklist
- 是否能把症状和根因分层

### Case 6: Selector / Error 解码

目标：测试模型是否会从原始链上信号反推 LOVE20 源码位置。

推荐 skill：

- `$love20-selectors-and-errors`

Prompt：

```text
Use $love20-selectors-and-errors.

请解码这个 LOVE20 回滚选择器：0xa748da06

输出：
- 它是什么类型的 selector
- 对应签名
- 候选合约
- 如果前端有映射，映射链路在哪里
```

主要看点：

- 是否能区分 function selector、custom error selector、event topic
- 是否能定位 ABI 或声明位置
- 是否知道前端映射只是 UI 层，不是合约真值

### Case 7: 跨仓导航

目标：测试模型能否正确路由复杂问题。

推荐 skill：

- `$love20-navigator`
- `$love20-extension-patterns`

Prompt：

```text
Use $love20-navigator and $love20-extension-patterns.

如果我要回答“链群扩展的加入、验证、奖励分别在哪看”，请按阅读顺序给我导航：
- 先看哪些 docs
- 再看哪些 repo
- 再看哪些实现文件

要求：
- 区分设计文档和实际实现
- 给出最小阅读路径，不要泛泛列仓库
```

主要看点：

- 是否会路由到正确 repo
- 是否给出阅读顺序
- 是否能保持问题范围，不泛化成整个协议导览

### Case 8: 宽泛需求拆题

目标：测试模型是否知道复杂问题要先拆，再选 skill。

推荐 skill：

- `$love20-prompts`

Prompt：

```text
Use $love20-prompts.

把这个大需求拆成 3 个更精确的 LOVE20 prompts：
“帮我理解这个协议、告诉我怎么交互、顺便排查页面为什么失败。”

要求：
- 每个 prompt 都写清目标
- 每个 prompt 都写清 anchors
- 每个 prompt 都写清 evidence rules
- 每个 prompt 都指定最小 skill 组合
```

主要看点：

- 是否知道 explanation / interaction / debugging 应拆开
- 是否能给出可直接喂给另一个 agent 的 prompt
- 是否选对 companion skills

## 5. 评分标准

每题按五个维度打分，每个维度 `0-2` 分，总分 `10` 分：

1. `Skill routing`
   有没有选对 skill，是否有无关 skill 污染。
2. `Anchors`
   有没有把 token、round、actionId、page、account 等锚点说清楚。
3. `Evidence quality`
   是否引用了准确文件路径、函数、hook、合约、脚本。
4. `Truth hierarchy`
   是否正确区分 docs、deployed contracts、wrappers、frontend、indexing。
5. `Actionability`
   答案是否足够具体，工程师能否直接继续操作。

打分解释：

- `0`
  明显错误、缺失，或大部分是空泛话术。
- `1`
  基本方向对，但证据或操作细节不够。
- `2`
  证据清楚、边界正确、可以复核和继续执行。

建议阈值：

- `60-80`
  适合做生产辅助，人工复核成本较低。
- `45-59`
  可以做草稿生成，但不适合直接指导操作。
- `<45`
  不建议用于执行型 LOVE20 任务。

## 6. 记录模板

建议每个模型每个实验组都保留一份记录。最简单的记录模板如下：

```md
# LOVE20 Skill Benchmark Run

- Model:
- Variant: A / B / C
- Date:

## Case 1
- Score:
- Findings:

## Case 2
- Score:
- Findings:

## Case 3
- Score:
- Findings:

## Case 4
- Score:
- Findings:

## Case 5
- Score:
- Findings:

## Case 6
- Score:
- Findings:

## Case 7
- Score:
- Findings:

## Case 8
- Score:
- Findings:

## Total
- Total Score:
- Main Failure Pattern:
- Verdict:
```

`Main Failure Pattern` 建议重点记录这几类常见错误：

- 没选 skill
- 选错 truth source
- 只讲文档，不讲合约
- 只讲概念，不给文件和函数
- 会描述问题，但不会给操作路径

## 7. 如何使用现有 eval 目录

这份文档本身是人工横评协议，不会自动接入当前的 `run_skill_benchmarks.py`。

当前仓库里的现有脚本和文件：

- [love20_skill_benchmarks.json](/Users/BigPolarBear/Documents/github/LOVE20TKM/docs/ai/evals/love20_skill_benchmarks.json)
  是当前自动 runner 的 benchmark source of truth。
- [run_skill_benchmarks.py](/Users/BigPolarBear/Documents/github/LOVE20TKM/docs/ai/scripts/run_skill_benchmarks.py)
  只能生成 JSON 里已经存在的 benchmark cases。
- [ai/evals/README.md](/Users/BigPolarBear/Documents/github/LOVE20TKM/docs/ai/evals/README.md)
  说明了现有 run/report/todo/summary 的结构。

如果你只是想快速比较模型，最省事的做法是：

1. 手工按这份文档跑 `A/B/C` 三组 prompt。
2. 把每个模型的回答保存到 `ai/evals/runs/` 下。
3. 用上面的记录模板人工打分。

如果你后续想把这份 benchmark 也自动化，需要额外做两件事：

1. 把这些 case 正式写入 benchmark JSON。
2. 给 run schema 增加 `model` 和 `variant` 之类字段，让 report/summary 能按模型和 A/B/C 汇总。

## 8. 建议的对比结论

最终比较时，优先写这三类结论：

1. `skills 有没有显著提升中低端模型的证据质量`
   看它们是否开始稳定引用正确 repo、文件、函数。
2. `skills 有没有降低真值层级错误`
   看它们是否不再把 docs、frontend、SQL、viewer 当成链上行为真值。
3. `skills 有没有提升答案的可执行性`
   看它们是否从“会解释”变成“能指导交互、读取和排查”。
