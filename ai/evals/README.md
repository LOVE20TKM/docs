# LOVE20 Skill Evals

这个目录放 LOVE20 skills 的 benchmark 源数据、demo run、以及 report 产物。

## 文件分层

- `love20_skill_benchmarks.json`
  benchmark source of truth
- `love20_skill_benchmarks.md`
  由脚本生成的人类可读目录
- `runs/*.json`
  单次 run 的结构化记录
- `runs/*.report.md`
  由脚本生成的 run 报告
- `runs/*.todo.md`
  由脚本生成的 run 待办清单
- `runs/*.md`
  单个 case 的示例响应文件
- `run-summary.md`
  所有 runs 的汇总面板

## 当前两种 demo baseline

- `runs/demo-walkthrough.json`
  理想答案基线
  目标是全 PASS，用来说明“标准答案应长什么样”
- `runs/demo-three-states.json`
  状态演示基线
  保留 `PASS / REVIEW / INCOMPLETE`
  用来说明 report 如何区分不同完成度

## Run JSON 最小结构

每个 run 文件都应包含：

```json
{
  "schema_version": 1,
  "run_name": "demo-name",
  "created_at": "2026-03-09T00:00:00+08:00",
  "benchmark_file": "docs/ai/evals/love20_skill_benchmarks.json",
  "results": [
    {
      "id": "navigator-fair-launch-source-of-truth",
      "selected_skills": ["love20-navigator"],
      "response_file": "docs/ai/evals/runs/example.case1.response.md",
      "cited_files": [
        "docs/whitepaper/LOVE20协议设计.md"
      ],
      "judgement": {
        "must_cover": {
          "docs vs code hierarchy": true,
          "specific repos or directories": true,
          "exact file paths or entry files": true
        },
        "output_shape_match": true,
        "notes": "short reviewer note"
      }
    }
  ]
}
```

## 字段规则

- `id`
  必须与 `love20_skill_benchmarks.json` 中的 benchmark id 对齐
- `selected_skills`
  记录实际命中的主 skill，至少应包含 benchmark 的 `primary_skill`
- `response_file`
  指向该 case 的示例回答 markdown
- `cited_files`
  记录回答中真正引用的 docs / code / tests / hooks / SQL 文件
- `judgement.must_cover`
  key 必须与 benchmark 的 `must_cover` 完全一致
- `judgement.output_shape_match`
  `true` / `false` / `null`
- `judgement.notes`
  简短人工备注

## 状态判定

`ai/scripts/generate_skill_run_report.py` 现在按下面规则出状态：

- `PASS`
  主 skill 命中，response/citations 完整，`must_cover` 全通过，`output_shape_match=true`
- `REVIEW`
  主 skill 命中，response/citations 存在，`output_shape_match=true`，但 `must_cover` 不完整或不全通过
- `INCOMPLETE`
  缺 response、缺 citations、缺主 skill、缺 judgement 之一

## 新增 run 的推荐流程

1. 最省事的方式是直接用半自动 runner：

```bash
python3 ai/scripts/run_skill_benchmarks.py <run-name>
```

它会自动：

- 生成或更新 run JSON
- 为每个 case 生成 response skeleton markdown
- 生成该 run 的 report
- 生成该 run 的 todo
- 刷新全局 run summary

2. 如果你只想要空白 run，再生成 skeleton：

```bash
python3 ai/scripts/generate_skill_run_skeleton.py <run-name>
```

3. 再填 `selected_skills`、`response_file`、`cited_files`、`judgement`
4. 为每个 case 填：
   - `selected_skills`
   - `response_file`
   - `cited_files`
   - `judgement`
5. 把 case 响应写成单独的 `runs/*.md`
6. 运行：

```bash
python3 ai/scripts/generate_skill_run_report.py ai/evals/runs/<run>.json
```

7. 如果你想先看还缺什么：

```bash
python3 ai/scripts/generate_skill_run_todo.py ai/evals/runs/<run>.json
```

8. 如果你想看所有 runs 的摘要：

```bash
python3 ai/scripts/generate_skill_run_summary.py
```

9. 或直接运行：

```bash
bash ai/scripts/refresh_love20_skills.sh
```

如果你想输出到别的路径：

```bash
python3 ai/scripts/generate_skill_run_skeleton.py <run-name> --output ai/evals/runs/<custom>.json
```

半自动 runner 的常用参数：

```bash
python3 ai/scripts/run_skill_benchmarks.py <run-name> --case <benchmark-id>
python3 ai/scripts/run_skill_benchmarks.py <run-name> --limit 3
python3 ai/scripts/run_skill_benchmarks.py <run-name> --append
python3 ai/scripts/run_skill_benchmarks.py <run-name> --overwrite-response
```

## 编写 case 响应时的约定

- 回答里要体现 source-of-truth hierarchy
- 优先引用 deployed contract repos：
  `core`、`extension`、`extension-lp`、`extension-group`、`group`
- `periphery`、`script`、`interface` 默认作为 adapter / read model / example
- 回答文件名建议体现 case 编号和状态：
  - `.pass.md`
  - `.review.md`
  - `.incomplete.md`

## 维护建议

- `demo-walkthrough` 尽量保持全 PASS
- `demo-three-states` 至少保留一个 `REVIEW` 和一个 `INCOMPLETE`
- 如果 benchmark 增加或 `must_cover` 变化，要同步修 run JSON
- 如果 run 还没收敛到全 PASS，优先先跑 todo 脚本，再补 response/judgement
- 新增 run 统一使用 skeleton 脚本生成，不再维护手工模板文件
