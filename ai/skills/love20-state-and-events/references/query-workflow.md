# Query Workflow

## Decide which truth source you need

Use this split before opening files:

- Current protocol truth:
  read deployed contract repos first: `core`, `extension`, `extension-lp`, `extension-group`, `group`.
- Frontend data source:
  read the direct wagmi hook or composite hook after you know the contract surface.
- Historical timeline or analytics:
  read the event pipeline and SQLite views.

## Choose the lookup key

Most LOVE20 read questions reduce to one of these anchors:

- token
- round
- action
- account
- tx hash or event timeline

Read `entity-lookup-playbooks.md` for the first four.
Read `event-and-indexing.md` for the last one.

## Query order

1. Identify the entity key.
2. Decide whether the question is about current state or history.
3. Start with the smallest useful surface:
   - deployed contract interface or implementation for minimal truth
   - viewer contract for aggregated read model
   - hook file for frontend source mapping
   - SQLite views for historical grouping
4. Only after that, open pages or UI components.

## Common decision rules

- "What is this token's current launch or governance status":
  prefer the relevant deployed contract read first; use `LOVE20TokenViewer` or `LOVE20RoundViewer` as aggregated read models.
- "Why does the page show this number":
  find the hook first, then the underlying contract read.
- "What happened across rounds" or "show me a timeline":
  prefer the event DB and SQL views.
- "State and history disagree":
  direct chain state wins for the current moment; the index may be stale.
