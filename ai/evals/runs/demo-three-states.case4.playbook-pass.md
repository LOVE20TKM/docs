# Demo Response: playbook-launch-child-token (PASS)

如果目标是发起 LOVE20 子币公平发射，默认优先直接走 core 合约写面，再把现成 `cast send` 脚本当模板。

建议顺序：

1. 先确认写面
   - `core/src/interfaces/ILOVE20Launch.sol`
   - 主写函数：`launchToken(symbol, parentTokenAddress)`
2. 先读前置状态
   - `remainingLaunchCount`
   - `launchInfo`
   - `tokenAddressBySymbol`
3. 再确认时序和限制
   - `docs/ai/skills/love20-contract-playbooks/references/prerequisites-and-timing.md`
   - 重点是 launch eligibility、child-launch quota、claim delay、contribute/withdraw waiting blocks
4. 执行时默认用 `cast send`
   - 不推荐先从 helper 封装开始理解

批准和前置条件：

- `launchToken` 本身先看 launch eligibility 和子币配额
- 如果后续还有公平发射申购流程，父币贡献通常需要先 `approve`
- 只有 native ETH 包装这种便利场景，才把 `periphery/src/LOVE20Hub.sol` 当辅助样例看

可复用模板：

- `script/script/cast/launch_deploy.sh`
- `script/script/cast/launch_query.sh`
- `script/script/cast/launch_stat.sh`

结论：

- 权威写面先看 `ILOVE20Launch`
- 默认表达方式是 direct `cast send`
- 脚本是模板，不是新的协议 API
