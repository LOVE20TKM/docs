# Demo Response: prompts-split-broad-request (PASS)

可以拆成 3 个更精确的 prompts：

```text
Use $love20-navigator and $love20-core-protocol.

请解释 LOVE20 的协议机制，重点说明 phase、round、submit、vote、join、verify、mint 的关系。

要求：
- 先讲文档里的设计意图
- 再讲 core 合约里的真实行为
- 给出精确文件路径
```

```text
Use $love20-contract-playbooks.

请把 LOVE20 的具体交互流程拆成可执行手册，说明要调用哪些合约和函数、先读哪些状态、需要哪些 approvals 和 waiting rules。

要求：
- direct contract surface first
- cast scripts 只作为模板
```

```text
Use $love20-runbooks.

请按最短路径排查 LOVE20 页面或交易失败问题，先判断失败层级，再给出需要看的 tests、contracts、wrappers 或 parser 文件。

要求：
- findings/checklist 形式输出
- 区分 wrapper 症状和 deployed contract 根因
```

这样拆分的理由：

- 第 1 个 prompt 负责 mechanism explanation
- 第 2 个 prompt 负责 interaction playbook
- 第 3 个 prompt 负责 failure triage

也就是把一个大需求拆成三类稳定任务，并明确各自适合的 LOVE20 skill。
