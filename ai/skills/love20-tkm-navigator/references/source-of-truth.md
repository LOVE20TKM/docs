# Source of Truth

## Priority order

1. Design intent and terminology:
   `docs/whitepaper/LOVE20协议设计.md`
   `docs/whitepaper/LOVE20宣言与设计原则.md`
   `docs/whitepaper/FAQ.md`
2. Contract repos and on-chain behavior for each deployed instance:
   `core/src/interfaces/*.sol`
   `core/src/*.sol`
   `extension/src/*.sol`
   `extension-lp/src/*.sol`
   `extension-group/src/*.sol`
   `group/src/interfaces/*.sol`
   `group/src/*.sol`
   `group-chat/src/interfaces/*.sol`
   `group-chat/src/interfaces/**/*.sol`
   `group-chat/src/*.sol`
   `group-chat/src/managers/*.sol`
   `group-chat/src/sources/**/*.sol`
   For timing questions, start with:
   `core/src/interfaces/IPhase.sol`
   `docs/ai/skills/love20-tkm-core-protocol/references/governance-lifecycle.md`
3. Deployed network address and parameter files:
   `group-chat/script/network/thinkium70001_public/address.group.chat.params`
   `group-chat/script/network/thinkium70001_public/group.chat.params`
4. Read and write adapters around deployed contracts:
   `periphery/src/*.sol`
5. Executable interaction examples:
   `script/script/cast/*.sh`
6. Active frontend development and public-test integration:
   `interface-test/src`
7. Released production frontend:
   `interface/src`

## Conflict handling

- Use docs for protocol intent, motivations, and formulas that explain why a rule exists.
- Use contract source as the highest-priority behavior truth for the deployed instance being inspected.
- During the group-chat community pilot, treat the current instance and constructor parameters as immutable, but allow the complete suite to be redeployed after testing without preserving historical compatibility.
- For the current group-chat deployment addresses and parameters, use `group-chat/script/network/thinkium70001_public/address.group.chat.params` and `group-chat/script/network/thinkium70001_public/group.chat.params`.
- Treat `periphery`, `script`, `interface-test`, and `interface` as adapters, helpers, or execution examples. Use `interface-test` for active work and `interface` only for released production behavior.
- For `phase` versus `round`, separate:
  - protocol timing semantics from `IPhase.sol` and lifecycle docs
  - viewer or indexed read semantics from periphery, frontend hooks, and event SQL
- Treat LOVE20 timing as a rolling pipeline across overlapping rounds, not a single round that fully finishes before the next one starts.
- If docs and code differ, report both:
  - "documented design" from the whitepaper
  - "implemented behavior" from the contract surface

## Avoid

- Avoid starting from `core/src/merged/*.sol`. Those files are flattened artifacts, not the best reading entry point.
- Avoid using frontend code as the authority for protocol rules.
- Avoid assuming extension repo behavior applies to base LOVE20 actions unless the action is explicitly extension-backed.
