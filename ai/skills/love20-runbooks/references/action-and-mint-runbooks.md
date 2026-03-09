# Action and Mint Runbooks

## Submit fails

Check these first:

- Confirm `canSubmit` on the relevant submit surface before attempting creation.
- Confirm the governor still has submission eligibility in the current round.
- Confirm the action parameters are internally coherent:
  - minimum stake
  - whitelist address
  - verification keys and guides
  - max random accounts

Evidence:

- Open `core/src/interfaces/ILOVE20Submit.sol`.
- Use `core/test/TestFlowHelper.sol` for the expected default field set and lifecycle ordering.

## Vote fails

Check these first:

- Confirm the action belongs to the expected round.
- Confirm the caller still has votes remaining.
- Confirm the action is actually eligible for voting in the current round.

Evidence:

- Open `core/src/interfaces/ILOVE20Vote.sol`.
- If the failure only appears through a wrapper or aggregated page, verify the action state through the round viewer before blaming voting logic.

## Join fails

Check these first:

- The action must already be voted.
- Joining late in the phase is blocked by the join-end cutoff.
- Action whitelist and minimum stake checks may reject the caller.
- Confirm token approvals for the join asset.

Evidence:

- Open `core/src/interfaces/ILOVE20Join.sol`.
- Read `docs/ai/skills/love20-contract-playbooks/references/prerequisites-and-timing.md` for join timing constraints.

## Verify fails

Check these first:

- Confirm the verifier actually supported that action.
- Confirm the random-account set has been prepared for the action and round.
- Confirm submitted scores satisfy the rule bounds expected by verification logic.

Evidence:

- Open `core/src/interfaces/ILOVE20Verify.sol`.
- If the revert is about data shape rather than score logic, inspect extension-center validation too.

## Reward mint fails

Check these first:

- Confirm the round is ready for mint.
- Confirm the user has not already minted the same reward path.
- Distinguish governance reward from action reward.
- Confirm whether the user should mint or burn overflow for parent token instead.

Evidence:

- Open `core/src/interfaces/ILOVE20Mint.sol`.
- Use `periphery/src/LOVE20MintViewer.sol` for aggregated reward-read paths.

Interpretation:

- "Already minted" style failures usually mean reward state exists and was consumed, not that round computation failed.
- If the UI reward number looks wrong, verify viewer output first, then inspect frontend hook code.
