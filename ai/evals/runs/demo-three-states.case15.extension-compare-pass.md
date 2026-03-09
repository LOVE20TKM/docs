# Demo Response: extension-group-vs-lp-patterns (PASS)

链群扩展和 LP 扩展都属于 LOVE20 extension，但 join token、验证方式、奖励路径、注册方式都不一样。

LP extension：

- repo：`extension-lp`
- 主文件：
  - `extension-lp/src/ExtensionLp.sol`
  - `extension-lp/src/ExtensionLpFactory.sol`
- join model：
  LP token holder join
- reward model：
  reward split + governance-ratio limits

链群扩展：

- repo：`extension-group`
- 主文件：
  - `ExtensionGroupAction.sol`
  - `ExtensionGroupActionFactory.sol`
  - `GroupJoin.sol`
  - `GroupVerify.sol`
  - `GroupRecipients.sol`
- join model：
  通过 chain group 参与 action，不是简单 LP token join
- verify model：
  有 group-level verification 和 distrust / service-provider 机制
- reward model：
  action/service reward routing 更复杂，可能还涉及 overflow burn

注册方式上：

- 两者都要经过 extension framework / factory / center
- 但 LP 行为真值优先看 `extension-lp`
- 链群行为真值优先看 `extension-group`
- 如果问题涉及 NFT ownership / group identity，再切到 `group/src/LOVE20Group.sol`
