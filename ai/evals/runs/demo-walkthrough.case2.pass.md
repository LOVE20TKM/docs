# Demo Response: navigator-routing-for-extension-question (PASS)

如果要回答“链群扩展的加入、验证、奖励分别在哪看”，建议按这个顺序导航：

1. `docs/ai/skills/love20-navigator/references/repo-index.md`
   先确认 docs、extension framework、extension-group、group 的分层入口。
2. `extension/README.md`
   先理解扩展框架、factory、`ExtensionCenter` 的位置。
3. `extension-group/docs/链群行动扩展协议.md`
   先看链群行动扩展设计。
4. `extension-group/docs/链群服务扩展协议.md`
   再看链群服务扩展和 reward routing 设计。
5. `extension-group/src/ExtensionGroupAction.sol`
   行动扩展主体。
6. `extension-group/src/GroupJoin.sol`
   参与和加入流程。
7. `extension-group/src/GroupVerify.sol`
   验证流程。
8. `extension-group/src/ExtensionGroupService.sol`
   服务扩展行为。
9. `extension-group/src/GroupRecipients.sol`
   奖励接收方和分配配置。
10. `group/src/LOVE20Group.sol`
   如果问题涉及 NFT ownership、group identity、名称或持有者规则，再切到 `group`。

阅读原则：

- docs 先解释设计意图
- `extension-group` 是链群扩展行为真值
- `group` 只负责 chain-group NFT 协议本体，不等于扩展实现
