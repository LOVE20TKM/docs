# Core Data Structures

## LaunchInfo

- Source:
  `core/src/interfaces/ILOVE20Launch.sol`
- Fields:
  - `parentTokenAddress`
  - `parentTokenFundraisingGoal`
  - `secondHalfMinBlocks`
  - `launchAmount`
  - `startBlock`
  - `secondHalfStartBlock`
  - `endBlock`
  - `hasEnded`
  - `participantCount`
  - `totalContributed`
  - `totalExtraRefunded`

## AccountStakeStatus

- Source:
  `core/src/interfaces/ILOVE20Stake.sol`
- Fields:
  - `slAmount`
  - `stAmount`
  - `promisedWaitingPhases`
  - `requestedUnstakeRound`
  - `govVotes`

## ActionHead

- Source:
  `core/src/interfaces/ILOVE20Submit.sol`
- Fields:
  - `id`
  - `author`
  - `createAtBlock`

## ActionBody

- Source:
  `core/src/interfaces/ILOVE20Submit.sol`
- Fields:
  - `minStake`
  - `maxRandomAccounts`
  - `whiteListAddress`
  - `title`
  - `verificationRule`
  - `verificationKeys`
  - `verificationInfoGuides`

## ActionInfo

- Source:
  `core/src/interfaces/ILOVE20Submit.sol`
- Shape:
  - `head: ActionHead`
  - `body: ActionBody`

## ActionSubmitInfo

- Source:
  `core/src/interfaces/ILOVE20Submit.sol`
- Fields:
  - `submitter`
  - `actionId`

## Practical guidance

- Use `ActionBody` when explaining new action creation requirements.
- Use `ActionInfo` when mapping frontend action detail screens to the submit contract.
- Use `AccountStakeStatus` when explaining governance eligibility, unstake timing, and missing receipt-token edge cases.
- Use `LaunchInfo` for launch dashboards and child-token discovery logic.
