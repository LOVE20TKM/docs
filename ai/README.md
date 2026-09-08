# LOVE20 AI

这个目录集中放 LOVE20 面向 AI Agent 的 skills、evals 和辅助脚本。

## 结构

- [skills](/ai/skills)
  LOVE20 skills 定义与 references
- [evals/README.md](/ai/evals/README.md)
  benchmark、demo run、report、todo、summary
- [scripts](/ai/scripts)
  catalog、skeleton、report、todo、summary、runner

## 真值层级

分析 LOVE20 真实链上行为时：

1. `docs/whitepaper/*`
   设计意图和术语
2. `core`、`extension`、`extension-lp`、`extension-group`、`group`、`group-chat`
   每个已部署实例的合约行为真值；group-chat 当前社区首轮测试结束后可整套重新部署，无需历史兼容
3. `periphery`、`script`、`interface-test`、`interface`
   adapter、read model、execution layer；前端开发与测试只在 `interface-test`，`interface` 是手动发布目标

## 技能范围

当前目录位于 `LOVE20TKM/docs`，这里的技能只服务 `LOVE20TKM / Thinkium`。涉及链上实现时，回答首句标明：`当前协议：LOVE20TKM / Thinkium`。

BSC 版本以后在 `LOVE20BSC` 自己的 docs/skills 中维护；不要把当前 TKM 合约、ABI、地址、脚本或前端配置当作 BSC 的实现依据。

## 入口

- [AI skills 目录](/ai/skills)
- [AI evals 说明](/ai/evals/README.md)
- [skill benchmark 目录](/ai/evals/love20_skill_benchmarks.md)
- [run summary](/ai/evals/run-summary.md)
- demo baseline：
  - [walkthrough](/ai/evals/runs/demo-walkthrough.report.md)
  - [three-states](/ai/evals/runs/demo-three-states.report.md)
  - [three-states todo](/ai/evals/runs/demo-three-states.todo.md)

## 常用命令

```bash
bash ai/scripts/refresh_love20_skills.sh
python3 ai/scripts/sync_codex_skills.py --dry-run
python3 ai/scripts/generate_skill_run_skeleton.py <run-name>
python3 ai/scripts/generate_skill_run_report.py ai/evals/runs/<run>.json
python3 ai/scripts/generate_skill_run_todo.py ai/evals/runs/<run>.json
python3 ai/scripts/generate_skill_run_summary.py
python3 ai/scripts/run_skill_benchmarks.py <run-name>
```

## 约定

- `demo-walkthrough` 保持全 PASS
- `demo-three-states` 保留至少一个 `REVIEW` 和一个 `INCOMPLETE`
