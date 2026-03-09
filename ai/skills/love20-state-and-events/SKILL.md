---
name: love20-state-and-events
description: "Inspect LOVE20 chain state, viewer reads, frontend query hooks, and indexed event history across core, periphery, interface, and script repos. Use when asked where a token, round, action, account, reward, or event timeline is read from, which contract or hook powers a page, how to query historical events, or why current state and indexed history disagree."
---

# LOVE20 State and Events

Use this skill for read-path discovery and state inspection, not for write-flow playbooks.

## Path Convention

- Cross-repo references use canonical GitHub repo names: `docs`, `core`, `periphery`, `script`, `interface`, `extension`, `extension-lp`, `extension-group`, `group`.
- If local checkout names differ, map local aliases to these canonical names before following any path.

## Workflow

1. Read `references/query-workflow.md` first.
2. If the question is keyed by a token, round, action, or account, read `references/entity-lookup-playbooks.md`.
3. If the question is about logs, timelines, SQL, or analytics mismatch, read `references/event-and-indexing.md`.
4. Read `references/generated-state-event-index.md` when you need a refreshed inventory of viewer functions, core and extension read hooks, composite hooks, SQL tables, SQL views, or stat queries.
5. Open the exact contract, hook, script, or SQL file only after you know which read surface should answer the question.

## Read Decision Tree

1. Decide whether the user wants current truth or historical timeline.
2. Decide whether the entity is base LOVE20 or extension or group scoped.
3. Choose the narrowest truth source:
   - direct contract state for current truth
   - viewer contracts for aggregated current reads
   - frontend hooks only when tracing UI data flow
   - SQL views and logs for history
4. If a round is mentioned, decide whether it is:
   - event payload round
   - block-derived `log_round`
   - contract-local `currentRound()`
5. For extension-backed actions, check `ExtensionCenter`, extension contracts, or `GroupJoin` before assuming `LOVE20Join` owns the state.

## Working Rules

- Treat `core`, `extension`, `extension-lp`, `extension-group`, and `group` as the highest-priority truth sources for current on-chain state.
- Prefer direct chain state for "what is true now" questions.
- Prefer indexed events and SQL views for "what happened over time" questions.
- Treat periphery viewers, frontend hooks, and SQL tables/views as read models layered on top of deployed contracts.
- Use periphery viewer contracts for aggregated protocol reads after identifying the underlying deployed-contract truth source.
- Use frontend hook files only after you identify the underlying contract surface.
- When a page or API can involve extension-backed actions, inspect `interface/src/hooks/extension/**` and `ExtensionCenter` before assuming the data comes from `LOVE20Join` or a periphery viewer.
- When the user asks "where does the page get this data", bridge all three layers:
  - contract or viewer function
  - direct hook or composite hook
  - page or component usage

## Guardrails

- Do not infer historical event order from current contract state alone.
- Do not treat viewer output, frontend hook state, or SQLite rows as higher-priority than deployed contract state for current truth questions.
- Do not explain indexed analytics without naming the SQL view, DB table, or log processor stage involved.
- Do not assume extension action participation totals are stored in `LOVE20Join.amountByActionId`; many extension-backed actions read participation from `ExtensionCenter`, extension contracts, or `GroupJoin`.
- Distinguish `log_round` from `round` in the SQLite event DB:
  - `log_round` is block-derived protocol round
  - `round` is the event payload field decoded from ABI data
- If the task depends on exact event signatures or topic decoding, switch to `love20-selectors-and-errors`.
- If the task turns into a concrete user operation or write sequence, switch to `love20-contract-playbooks`.

## Response Contract

When answering, state:

1. Primary truth source.
2. Supporting adapter layers such as viewer, hook, or SQL view.
3. Exact lookup keys: token, actionId, round, account, or block range.
4. One caveat about round semantics, extension routing, or history-vs-current differences when relevant.

## References

- `references/query-workflow.md`
- `references/entity-lookup-playbooks.md`
- `references/event-and-indexing.md`
- `references/generated-state-event-index.md`
- `scripts/generate_state_event_index.py`
