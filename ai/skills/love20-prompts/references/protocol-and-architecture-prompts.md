# Protocol and Architecture Prompts

## Explain one mechanism

Recommended skills:

- `$love20-navigator`
- `$love20-core-protocol`

Template:

```text
Use $love20-navigator and $love20-core-protocol.

Please explain the LOVE20 mechanism around <topic>. Focus on:
1. the protocol intent from docs
2. the actual behavior from contracts
3. the main contracts, interfaces, and state transitions involved
4. any places where docs and code differ

Requirements:
- cite the exact doc files and code files you used
- name the core contracts and key functions
- if docs and code conflict, state the conflict explicitly and treat code as behavior truth
- when deployed immutable behavior is involved, prioritize `core`, `extension`, `extension-lp`, `extension-group`, and `group` over `periphery`, `script`, or `interface`
- keep the answer concise and structured for an engineer
```

## Compare docs to implementation

Recommended skills:

- `$love20-navigator`
- `$love20-core-protocol`

Template:

```text
Use $love20-navigator and $love20-core-protocol.

Compare the documented design and the current implementation for <topic>.

Deliver:
- a short summary of the documented intent
- a short summary of the implemented behavior
- a list of mismatches or ambiguities
- the exact files that should be treated as source of truth

Requirements:
- cite docs and code separately
- do not hide mismatches
- if implementation changed behavior, say so explicitly
- when identifying behavior truth, prioritize deployed contract repos over adapters or frontend layers
```

## Map a cross-repo architecture path

Recommended skills:

- `$love20-navigator`
- add one or more of:
  `$love20-core-protocol`
  `$love20-contract-playbooks`
  `$love20-frontend-bridge`
  `$love20-state-and-events`

Template:

```text
Use $love20-navigator and whichever LOVE20 skills are needed.

Map the end-to-end architecture for <feature or page>. I need:
- the user-facing concept
- the core contracts and interfaces
- any periphery or hub wrappers
- the frontend hooks or pages involved
- the scripts or event pipeline pieces involved, if any

Output:
- a short top-down walkthrough
- exact file paths
- the most important functions or hooks at each layer

Requirements:
- distinguish deployed contract behavior from wrappers, scripts, and frontend layers
- if multiple repos are involved, say which repo is the behavior truth at each step
```
