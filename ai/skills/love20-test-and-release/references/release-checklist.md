# Release Checklist

## Pre-merge

- Name the changed repos and changed surfaces:
  contract, viewer, script, log, env, frontend, or extension registration.
- Run the smallest targeted tests first.
- Regenerate generated artifacts if ABI, selector, error-map, or env-binding inputs changed.
- Record exactly which checks were run and which were skipped.

## Pre-deploy

- Confirm the target network and the correct params directory.
- High-value deploy entry points:
  `core/script/deploy/*`,
  `extension/script/deploy/*`,
  `extension-lp/script/deploy/*`,
  `extension-group/script/deploy/*`,
  `group/script/deploy/*`,
  `periphery/script/deploy/*`
- Canonical repo-local network files:
  `core/script/network/<network>/address.params`,
  `extension/script/network/<network>/address.extension.center.params`,
  `extension-lp/script/network/<network>/address.extension.lp.params`,
  `extension-group/script/network/<network>/address.extension.group.params`,
  `group/script/network/<network>/address.group.params`,
  `periphery/script/network/<network>/address.params`,
  `periphery/script/network/<network>/address.core.params`
- `script` repo network files are mirrors or consumers for interaction and export flows:
  `script/script/network/<network>/*.params`,
  `script/script/network/<network>/contracts.json`

## Post-deploy

- Confirm the deployed addresses landed in the expected params or env files.
- Run at least one read from:
  `script/script/cast/*_query.sh`
  or a periphery viewer.
- If the frontend changed, verify the corresponding route or component path with the correct `.env*` file.
- If the feature depends on history or exported state, refresh:
  `script/script/log/one_click_process.sh`

## Signoff expectations

- State whether validation covered:
  local only,
  public test,
  or actual release target.
- State unresolved gaps explicitly:
  checks not run,
  deploy not performed,
  log refresh not verified,
  frontend smoke path not exercised.
