# Demo Response: runbook-group-name-invisible-space (PASS)

这类问题最短排查路径就是先怀疑 Unicode whitespace，而不是先怀疑用户在撒谎。

先看：

1. `docs/ai/skills/love20-runbooks/references/extensions-and-groups-runbooks.md`
2. `group/test/UnicodeWhitespaceTest.t.sol`
3. `group/test/LOVE20Group.t.sol`

第一批确认项：

- group name 是否为空
- 是否包含不可见 Unicode whitespace
- 是否超长
- 是否重名

为什么 Unicode whitespace 要优先：

- runbook 已明确写了，很多 Unicode spaces，包括 full-width CJK space，都会被拒绝
- 所以“看起来没有空格”不代表链上视角没有非法分隔符

这题的证据结构：

- group runbook：群组命名失败怎么分流
- unicode whitespace edge case：`UnicodeWhitespaceTest.t.sol`
- relevant tests：`LOVE20Group.t.sol` + `UnicodeWhitespaceTest.t.sol`
