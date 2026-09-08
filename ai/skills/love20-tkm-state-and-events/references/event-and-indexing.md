# Event and Indexing

## When to use the log pipeline

Use the event pipeline when the user asks:

- what happened over time
- which event emitted first
- how many times something happened
- how analytics, charts, or exports are derived
- why the page history is stale or missing

Do not use it as the primary source for current balances or current eligibility when a direct contract read can answer the question.
Treat it as a historical or analytical read model, not as the final authority for current on-chain truth.

## Source files

- Init and environment wiring:
  `script/script/log/000_init.sh`
- Batch event sync:
  `script/script/log/one_click_process.sh`
- Event decoding and DB write:
  `script/script/log/event_processor.py`
- Block metadata supplement:
  `script/script/log/block_processor.py`
- SQL export entry:
  `script/script/log/export.sh`

## SQLite model

Main DB path:

- `script/script/log/db/<network>/events.db`

Core tables:

- `events`
- `blocks`
- `transactions`
- `sync_status`
- `transaction_sync`

Important round distinction:

- `log_round` is computed from block number and protocol phase settings.
- `round` is decoded from the event payload itself.

If these differ, explain that they represent different notions of round rather than assuming the decoder is wrong.

## Built-in SQL surfaces

Views from `sql/init/02_views.sql` already normalize common queries such as:

- transfers
- launch contributions
- pair creation
- LOVE20/TKM20 swap flow
- LOVE20/TUSDT swap flow
- LOVE20/TUSDT liquidity flow
- governance reward mint history
- action reward mint history
- reward claims

Stat queries under `sql/stat/*.sql` are the next stop when the user wants export-ready grouped results rather than raw event rows.

## Operational checks

- If the DB is empty or stale, confirm network params and RPC URL from `000_init.sh`.
- If event rows exist but block metadata is missing, the block processor stage likely failed after event sync.
- If the user wants CSV/XLSX output, route through `export.sh` with the chosen SQL file.
