# Evidence Sources

## Triage order

1. Get the user-visible symptom in the most concrete form available:
   - revert string
   - custom error selector
   - frontend Chinese message
   - missing event or stale page state
2. Confirm which layer failed:
   - deployed contract repo (`core`, `extension`, `extension-lp`, `extension-group`, `group`, `group-chat`)
   - hub or periphery wrapper
   - frontend parser or RPC
   - log indexing pipeline
3. Read the smallest source that can prove or disprove the suspected cause.

## Fastest evidence by symptom

### Raw revert or custom error

- Identify whether the symptom came from `interface-test` or the released `interface` build. The paths below default to active development in `interface-test`.
- Check `interface-test/src/errors/contractErrorParser.ts` for frontend heuristics and selector extraction.
- Check `interface-test/src/errors/unifiedErrorMap.ts` and `errorMessages.ts` for the final UI mapping.
- If the input is only a selector or topic, switch to `love20-selectors-and-errors`.

### Wrong phase, wrong round, or action/state mismatch

- Read the relevant deployed-contract interface or implementation first.
- Read the corresponding viewer contract in `periphery/src` when bulk state matters:
  - `LOVE20RoundViewer.sol`
  - `LOVE20TokenViewer.sol`
  - `LOVE20MintViewer.sol`
- Use `core/test/TestFlowHelper.sol` to understand the expected lifecycle order.

### Wrapper flow failed but the protocol rule is unclear

- Check `periphery/src/LOVE20Hub.sol`.
- Check the matching hub tests in `periphery/test`, especially `LOVE20Hub.contributeWithETH.t.sol`.

### Extension or group-specific failure

Split the failure first:

- Extension framework failure (`extension`)
  Check `extension/test/ExtensionCenter.t.sol` for registration, binding, and action-routing issues.
  Check `extension/test/ExtensionBaseTokenJoin.t.sol`, `ExtensionBaseJoin.t.sol`, and `ExampleTokenJoin.t.sol` for join, exit, and waiting-period logic.
- Concrete chain-group extension failure (`extension-group`)
  Check `extension-group/test/ExtensionGroupAction*.t.sol` for chain-group action extension and factory issues.
  Check `extension-group/test/ExtensionGroupService*.t.sol` for service extension and reward-routing issues.
  Check `extension-group/test/GroupJoin*.t.sol`, `GroupManager.t.sol`, `GroupRecipients.t.sol`, and `GroupVerify*.t.sol` for chain-group participation, management, recipients, and verify flows.
- Group NFT failure (`group`)
  Check `group/test/LOVE20Group.t.sol` and `UnicodeWhitespaceTest.t.sol` for naming, uniqueness, holder-index, and Unicode whitespace failures.
- Group-chat failure (`group-chat`)
  Check `group-chat/test/GroupChatLifecycle.t.sol`, `GroupChatMessages.t.sol`, `GroupChatDefaultSender.t.sol`, and `GroupChatPlugins.t.sol` for activation, posting, default sender, mention, quote, source, ban, and plugin failures.
  Check `group-chat/test/Manager.t.sol` and `TypedManagers.t.sol` when a typed decentralized chat manager owns the chat.
  During the community pilot, confirm that `script` and `interface-test` use the latest deployment addresses before diagnosing contract logic.

### Missing history, unexpected event timeline, or stale analytics

- Check `script/script/log/000_init.sh` for required network variables, derived addresses, and Python dependency checks.
- Check `script/script/log/one_click_process.sh` for the batch event sync path.
- SQLite output lives at `script/script/log/db/<network>/events.db`.

## Evidence hierarchy

- Source of truth for base LOVE20 rules: `core`
- Source of truth for extension framework rules: `extension`
- Source of truth for LP extension behavior: `extension-lp`
- Source of truth for chain-group extension behavior: `extension-group`
- Source of truth for chain-group NFT behavior: `group`
- Source of truth for public on-chain group chat behavior: `group-chat`
- Source of truth for wrapper behavior: `periphery`
- Source of truth for active-test frontend translation: `interface-test/src/errors`; use `interface/src/errors` for the released production build
- Source of truth for replayable log history: `script/script/log`
- Best behavioral witnesses for extension, group, and group-chat edge cases: `extension/test`, `extension-group/test`, `group/test`, `group-chat/test`
