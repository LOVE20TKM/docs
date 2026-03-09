# Interaction, State, and Debug Prompts

## Ask for a write-flow playbook

Recommended skills:

- `$love20-contract-playbooks`
- add `$love20-extension-patterns` if the action uses extensions

Template:

```text
Use $love20-contract-playbooks <and $love20-extension-patterns if needed>.

I need the exact LOVE20 interaction path for <operation>.

Known anchors:
- token: <token or symbol>
- actionId: <actionId or unknown>
- round: <round or unknown>
- account role: <governor / participant / verifier / user>
- network: <network or unknown>

Deliver:
- the exact contracts and functions involved
- prerequisites such as approvals, balances, phase limits, and waiting periods
- any existing cast scripts or helper contracts that should be reused
- the fastest reads to confirm the operation is currently allowed

Requirements:
- present the direct deployed contract surface first
- treat cast scripts and helper wrappers as examples or convenience paths, not the default authority
```

## Ask for a read-path or state query

Recommended skills:

- `$love20-state-and-events`
- add `$love20-frontend-bridge` if the question is page-specific

Template:

```text
Use $love20-state-and-events <and $love20-frontend-bridge if needed>.

I need to find where LOVE20 reads <state or metric> for:
- token: <token or symbol>
- actionId: <actionId or unknown>
- round: <round or unknown>
- account: <account or unknown>
- page or component: <page if relevant>

Deliver:
- which contract or viewer function is the truth source
- which frontend hook or composite hook reads it
- whether indexed event history or SQL is also involved
- the exact file paths and function names

Requirements:
- for current truth, prioritize deployed contract repos before viewers, hooks, or SQL
- if a viewer or hook is used, state that it is a read model or frontend adapter
```

## Ask for failure triage

Recommended skills:

- `$love20-runbooks`
- add `$love20-selectors-and-errors` if there is a selector, topic, or raw revert

Template:

```text
Use $love20-runbooks <and $love20-selectors-and-errors if needed>.

Help me troubleshoot this LOVE20 failure:
- operation: <operation>
- token / action / round / account: <known anchors>
- symptom: <revert string / selector / topic / Chinese UI message / tx hash>
- wrapper or page involved: <hub / page / hook / unknown>

Deliver:
- the fastest checks to run first
- the most likely failure layer
- the exact contracts, tests, scripts, or frontend files to inspect
- the concrete state reads that would confirm or falsify each likely cause

Requirements:
- trace the final root cause back to the deployed contract repo when the failure concerns immutable on-chain behavior
- separate wrapper, parser, or indexing symptoms from contract-level causes
```

## Ask for selector or event decoding

Recommended skills:

- `$love20-selectors-and-errors`

Template:

```text
Use $love20-selectors-and-errors.

Decode this LOVE20 artifact:
- selector or topic: <hex value>
- optional context: <contract / tx hash / page / error message>

Deliver:
- whether it is a function selector, custom error selector, or event topic
- the matching signatures and candidate contracts
- where the frontend maps it, if a UI message is involved
- exact file paths for the ABI or parser source

Requirements:
- use frontend parser files only for UI mapping
- confirm the final declaration site in `core`, `extension`, `extension-lp`, `extension-group`, or `group` when the artifact belongs to deployed LOVE20 contracts
```
