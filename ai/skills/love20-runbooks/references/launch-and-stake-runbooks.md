# Launch and Stake Runbooks

## Launch contribution fails

Check these first:

- If the call goes through `LOVE20Hub`, open `periphery/test/LOVE20Hub.contributeWithETH.t.sol`.
- Confirm the obvious wrapper preconditions first:
  - ETH helper path must send non-zero value
  - token address cannot be zero
  - recipient address cannot be zero
- Then confirm protocol-side conditions:
  - launch is still active
  - caller has enough parent token or native token
  - allowance exists when not using the ETH helper

Likely evidence:

- `"Must send ETH"` usually means the hub wrapper path received `value == 0`.
- `"Invalid token address"` or `"Invalid recipient address"` means the failure happened before core launch logic.
- If the wrapper succeeds but launch still reverts, inspect `core/src/interfaces/ILOVE20Launch.sol`.

## Claim fails or user says "I already contributed"

Check these first:

- Confirm launch has ended.
- Confirm the one-block claim delay has passed.
- Confirm the account actually contributed to the launch token.

Evidence:

- `core/test/TestFlowHelper.sol` shows the expected sequence:
  - contribute in the first half
  - advance into the second half minimum
  - finish launch
  - skip claim delay
  - claim

Interpretation:

- If a user contributed but cannot claim immediately after launch end, the delay is probably timing-related rather than balance-related.
- If a frontend page says claim is unavailable, verify the launch round and end block from the contract before blaming UI state.

## Withdraw or fair-launch exit fails

Check these first:

- Confirm the account actually contributed.
- Confirm the required waiting blocks since contribution or unstake request have elapsed.
- Confirm the correct token address and round were used.

Evidence:

- Timing constraints are summarized in `docs/ai/skills/love20-contract-playbooks/references/prerequisites-and-timing.md`.
- If the revert is selector-only, decode it before concluding.

## Stake fails

Check these first:

- Round cannot be zero for `stakeLiquidity` or `stakeToken`.
- `promisedWaitingPhases` must stay within protocol bounds.
- Later stakes cannot reduce the waiting commitment for the same account and token.
- Confirm receipt-token implications:
  - `SL` balance matters for LP staking and governance status
  - `ST` balance matters for token staking and delayed exits

Evidence:

- Open `core/src/interfaces/ILOVE20Stake.sol`.
- If the user is staking via helper routes, also open `periphery/src/LOVE20Hub.sol`.

## Stake withdrawal fails

Check these first:

- Was `unstake` called already.
- Has the promised waiting period finished.
- Does the account still hold the expected receipt tokens.

Interpretation:

- A user can make the exit flow impossible or misleading by transferring away receipt tokens after staking.
- If a frontend only shows "cannot withdraw", verify the unstake timestamp or round from chain state before assuming the UI is wrong.
