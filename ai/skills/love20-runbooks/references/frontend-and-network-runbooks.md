# Frontend and Network Runbooks

## Frontend shows a Chinese error message

Check these first:

- Open `interface/src/errors/contractErrorParser.ts`.
- Determine whether the message came from:
  - gas heuristic
  - timeout heuristic
  - RPC heuristic
  - user-cancel detection
  - selector or name lookup
- Then open `interface/src/errors/unifiedErrorMap.ts` or `errorMessages.ts` only if the parser points there.

Common buckets already encoded in the parser:

- `Gas费不足`
- `网络超时`
- `链上交易失败`
- user cancellation paths such as MetaMask or TrustWallet rejection

## RPC or quoting path fails

Check these first:

- Look for liquidity-related patterns such as insufficient reserves or zero liquidity.
- Look for array-position or out-of-bounds patterns that indicate chain state changed between read and write.
- Confirm whether the failure is from an off-chain quote/read path or an actual on-chain revert.

Interpretation:

- Liquidity-style RPC failures usually mean a route or pair state problem, not a LOVE20 governance rule failure.
- Position out-of-bounds style failures often indicate stale frontend data or a race with another user transaction.

## Transaction times out or page state looks stale

Check these first:

- Distinguish wallet submission failure from post-submission indexing failure.
- Re-read the relevant viewer contract directly before blaming the page.
- If the page depends on recent events, refresh the local event index.

Evidence:

- `script/script/log/000_init.sh` validates network params, derived addresses, Python deps, and DB output location.
- `script/script/log/one_click_process.sh` is the batch rebuild path for event history.
- The SQLite DB path is `script/script/log/db/<network>/events.db`.

## Missing events or analytics mismatch

Check these first:

- Confirm the contract address set for the network is current.
- Confirm `originBlocks`, `to_block`, and RPC URL are correct.
- Confirm the log processor dependencies are installed.
- Confirm the batch processor finished and block metadata supplement ran.

Interpretation:

- If chain state is correct but analytics is stale, the protocol likely worked and the indexing pipeline did not catch up.
- If the event DB is missing rows across many contracts, start with network config and RPC limits before debugging contract logic.
