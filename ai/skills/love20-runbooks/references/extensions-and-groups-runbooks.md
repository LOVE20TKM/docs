# Extensions and Groups Runbooks

## Extension registration or routing fails

Check these first:

- Confirm the extension address is non-zero and points to the expected contract.
- Confirm the extension token address matches the target LOVE20 token.
- Confirm the extension action id matches the action being registered.
- Confirm the action has not already been registered elsewhere.

Evidence:

- `extension/test/ExtensionCenter.t.sol` covers:
  - `InvalidExtensionAddress`
  - `ExtensionTokenAddressMismatch`
  - `ExtensionActionIdMismatch`
  - `ActionAlreadyRegisteredToOtherAction`
  - `ActionNotVotedInCurrentRound`

## Extension join or exit fails

Check these first:

- Confirm the join token address is correct.
- Confirm join amount is non-zero.
- Confirm the account joined before trying to exit or update.
- Confirm the waiting period has elapsed for exit-like operations.

Evidence:

- `extension/test/ExtensionBaseTokenJoin.t.sol` covers:
  - `InvalidJoinTokenAddress`
  - `JoinAmountZero`
  - `NotJoined`
  - `NotEnoughWaitingBlocks`
- `extension/test/ExampleTokenJoin.t.sol` also covers waiting-period failures.

## Extension verification or delegate flow fails

Check these first:

- Confirm the caller is the account, extension, or approved delegate expected by the route.
- Confirm the verification info array lengths match what the extension expects.
- Confirm the requested round does not exceed the join round or allowed historical window.

Evidence:

- `extension/test/ExtensionCenter.t.sol` covers:
  - `OnlyExtensionOrDelegate`
  - `OnlyAccountOrExtensionOrDelegate`
  - `VerificationInfoLengthMismatch`
  - `RoundExceedsJoinRound`
  - `AccountAlreadyJoined`
  - `InvalidAccountAddress`

## Group mint or rename fails

Check these first:

- Group name cannot be empty.
- Group name cannot contain disallowed whitespace or control-like separators.
- Group name length must stay within the configured limit.
- Group name must be unique.

Evidence:

- `group/test/LOVE20Group.t.sol` covers:
  - `GroupNameEmpty`
  - `GroupNameInvalidCharacters`
  - `GroupNameTooLong`
  - `GroupNameAlreadyExists`
  - `HolderIndexOutOfBounds`
- `group/test/UnicodeWhitespaceTest.t.sol` proves that many Unicode spaces, including full-width CJK space, are rejected.

Interpretation:

- If a user says "the visible name has no space", still check Unicode whitespace. Frontend text fields can carry non-ASCII separators that look invisible.

## Default group identity fails

Check these first:

- Confirm `GroupDefaults.GROUP_ADDRESS()` matches the deployed `LOVE20Group`.
- Confirm the caller currently owns the target `groupId` NFT before `setDefaultGroupId`.
- Confirm `NEXT_PUBLIC_CONTRACT_ADDRESS_GROUP_DEFAULTS` is set when the frontend hides or disables default group UI.
- If `defaultGroupIdOf(account)` returns `0`, check whether the NFT was transferred after the default was stored.

Evidence:

- `group/test/GroupDefaults.t.sol` covers:
  - `GroupNotExist`
  - `SenderNotGroupOwner`
  - `DefaultGroupIdAlreadySet`
  - `DefaultGroupIdNotSet`

## Group chat activation or posting fails

Check these first:

- Confirm the public-network `GroupChat` address from `group-chat/script/network/thinkium70001_public/address.group.chat.params`.
- Confirm `groupId` exists in the Group NFT contract and the caller is the current owner for `activateChat`.
- Confirm `chatInfo(groupId).activated == true` and `postingAllowed == true` before posting.
- Confirm `senderId` exists and `msg.sender` currently owns that sender NFT.
- If using `postAsDefaultSender`, confirm `GroupDefaults.defaultGroupIdOf(account)` returns a valid sender NFT owned by the account.
- For non-owner/non-delegate posters, confirm `scopeSource.canPost` and `banSource.isBanned` outcomes separately.
- If `mentionAll == true`, confirm the sender is chat owner, valid delegate, or admin.
- If quoting, confirm `quotedMessageId` is in `1..messagesCount(groupId)`.
- If the failure appears only after message write, inspect `afterPostPlugin`; after-post failures should emit `FailAfterPostPlugin` rather than rollback the message.

Evidence:

- `group-chat/test/GroupChatLifecycle.t.sol` covers activation, owner/delegate management, and posting switches.
- `group-chat/test/GroupChatMessages.t.sol` covers content length, mentions, quote validation, message ids, and paging behavior.
- `group-chat/test/GroupChatDefaultSender.t.sol` covers default sender posting.
- `group-chat/test/GroupChatPlugins.t.sol` covers source, ban, before-post, and after-post behavior.
- `group-chat/test/GroupMemberScope.t.sol`, `GroupJoinScopeSource.t.sol`, `AdminBanSource.t.sol`, and `GovVotedBanSource.t.sol` cover common source and ban modules.
