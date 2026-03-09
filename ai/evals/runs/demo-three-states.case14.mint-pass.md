# Demo Response: playbook-mint-and-burn-rewards (PASS)

LOVE20 奖励相关交互，先分成 4 条路径，不要混在一起：

1. governance reward
   - `core/src/interfaces/ILOVE20Mint.sol`
   - `mintGovReward`
2. action reward
   - `core/src/interfaces/ILOVE20Mint.sol`
   - `mintActionReward`
3. reward claim / read prerequisites
   - 先读 `LOVE20MintViewer`
   - 重点读：`govRewardByAccount`、`actionRewardByActionIdByAccount`、`rewardAvailable`
4. burn overflow
   - 仍然在 `LOVE20Mint` 奖励规则里处理 overflow burn

发交易前先读的状态：

- `rewardAvailable`
- `govRewardByAccount`
- `actionRewardByActionIdByAccount`
- 必要时先 `prepareRewardIfNeeded`

推荐顺序：

1. 先看 `core/src/interfaces/ILOVE20Mint.sol`
2. 再看 `periphery/src/LOVE20MintViewer.sol`
3. 再复用 `script/script/cast/mint_gov_reward.sh`
4. 再复用 `script/script/cast/mint_action_reward.sh`
5. 查询用 `script/script/cast/mint_query.sh`

关键是要把 reward paths 分开：

- gov reward 不等于 action reward
- viewer prerequisites 不等于实际 mint write
- overflow burn 也不等于 `LOVE20Token.burnForParentToken`
