# Cast Script Index

These scripts are reusable templates around `cast call` and `cast send`.
Use them after you identify the target contract surface; do not treat the script name as the authoritative protocol API.

## Setup

- `000_init.sh`
  Load network-specific environment before other cast call/send scripts.
- `101_flow_all.sh`
  Run an end-to-end scripted `cast` flow.

## Launch

- `launch_deploy.sh`
  Start a launch.
- `launch_contribute.sh`
  Contribute to a launch.
- `launch_withdraw.sh`
  Withdraw pre-end launch contribution.
- `launch_claim.sh`
  Claim launch allocation and refund.
- `launch_query.sh`
  Read launch-specific state.
- `launch_stat.sh`
  Inspect launch stats.

## Stake

- `stake_liquidity.sh`
  Stake LP-backed liquidity.
- `stake_token.sh`
  Stake token-only balance.
- `stake_unstake.sh`
  Request unstake.
- `stake_withdraw.sh`
  Withdraw after waiting period.
- `stake_query.sh`
  Query stake state.

## Actions and voting

- `submit_new_action.sh`
  Create a new action and submit it.
- `submit.sh`
  Submit an existing action.
- `submit_query.sh`
  Query submit state and actions.
- `vote.sh`
  Vote on actions.
- `vote_query.sh`
  Query vote state.

## Join and verification

- `join.sh`
  Join an action or add stake.
- `join_update.sh`
  Update verification info.
- `join_withdraw.sh`
  Withdraw from an action.
- `join_query.sh`
  Query join state.
- `random.sh`
  Trigger random-account preparation or random-related operations.
- `random_query.sh`
  Query random state.
- `verify.sh`
  Submit verification scores.
- `verify_query.sh`
  Query verification state.

## Rewards and token state

- `mint_gov_reward.sh`
  Mint governance reward.
- `mint_action_reward.sh`
  Mint action reward.
- `mint_query.sh`
  Query reward state.
- `token_query.sh`
  Query token state.
- `burnForParentToken.sh`
  Redeem against the parent pool.

## WETH helpers

- `weth_deposit.sh`
- `weth_withdraw.sh`
- `weth_query.sh`
- `weth_stat.sh`
