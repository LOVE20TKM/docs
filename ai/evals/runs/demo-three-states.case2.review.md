# Demo Response: navigator-routing-for-extension-question (REVIEW)

回答“链群扩展的加入、验证、奖励分别在哪看”，我会先这样导航：

1. `docs/ai/skills/love20-navigator/references/repo-index.md`
   先确认 extension 相关仓库的阅读入口和分工。
2. `extension/README.md`
   先理解扩展框架和 `ExtensionCenter` 的位置。
3. `extension-group/docs/链群行动扩展协议.md`
   看链群行动扩展的设计意图。
4. `extension-group/src/GroupJoin.sol`
   看加入流程。
5. `extension-group/src/GroupVerify.sol`
   看验证流程。
6. `extension-group/src/GroupRecipients.sol`
   看奖励接收方和分配配置。
7. `group/README.md`
   如果问题继续涉及链群 NFT 本体，再补看 group repo。

这版路由已经能把人带到大方向，但还不够完整：

- 还应该补 `ExtensionGroupAction.sol` / `ExtensionGroupService.sol`
- 还应该更明确区分 `extension-group` 和 `group`

所以它适合作为 REVIEW 样例，不适合作为 PASS 样例
