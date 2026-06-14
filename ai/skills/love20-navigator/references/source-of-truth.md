# Source of Truth

## Priority order

1. Design intent and terminology:
   `docs/whitepaper/LOVE20协议设计.md`
   `docs/whitepaper/LOVE20宣言与设计原则.md`
   `docs/whitepaper/FAQ.md`
2. Immutable deployed-contract repos and on-chain behavior:
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
   `docs/ai/skills/love20-core-protocol/references/governance-lifecycle.md`
3. Deployed network address and parameter files:
   `group-chat/script/network/thinkium70001_public/address.group.chat.params`
   `group-chat/script/network/thinkium70001_public/group.chat.params`
4. Read and write adapters around deployed contracts:
   `periphery/src/*.sol`
5. Executable interaction examples:
   `script/script/cast/*.sh`
6. Frontend integration:
   `interface/src`

## Conflict handling

- Use docs for protocol intent, motivations, and formulas that explain why a rule exists.
- Use `core`, `extension`, `extension-lp`, `extension-group`, `group`, and `group-chat` as the highest-priority code repositories when the question is about immutable deployed contract behavior.
- For group-chat public deployment addresses and immutable deployment parameters, use `group-chat/script/network/thinkium70001_public/address.group.chat.params` and `group-chat/script/network/thinkium70001_public/group.chat.params`.
- Treat `periphery`, `script`, and `interface` as adapters, helpers, or execution examples around those deployed contracts.
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
