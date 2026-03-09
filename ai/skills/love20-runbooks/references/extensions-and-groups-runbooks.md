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
