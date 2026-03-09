# Demo Response: state-reward-and-flow-history (PASS)

如果你要看最近 30 轮的奖励地址数和 TUSDT 流入流出走势，应该优先走 event DB 和 stat SQL，而不是直接问当前链上状态。

推荐入口：

1. SQLite views
   - `v_mint_gov_reward`
   - `v_mint_action_reward`
   - `v_claim_reward`
2. stat SQL
   - `script/script/log/sql/stat/flow.sql`
   - `script/script/log/sql/stat/liquidity.sql`
   - `script/script/log/sql/stat/swap.sql`

需要知道的 caveat：

- `log_round` 是按区块和 phase 配置推导出来的 round
- `round` 是事件 payload 里解出来的字段
- 两者不一致时，不代表解码错了，而是代表它们在表达不同的 round 语义

所以如果页面和链上当前状态对不上，应这样解释：

- 当前真值先看 deployed contracts
- 历史图表和走势看 event DB / SQL
- viewer、页面、SQL 都属于 read model 或 analytics layer，不应高于当前链上状态

如果 DB 为空或明显过期，再检查：

- `script/script/log/000_init.sh`
- `script/script/log/one_click_process.sh`
- `script/script/log/db/<network>/events.db`
