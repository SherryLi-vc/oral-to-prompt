# UAT 摘要

> SKILL **未改**。公开仓名已定 **`oral-to-prompt`**（**勿**用撞车名 `prompt-optimizer`）。完整报告在 `/workspace/prompt-optimizer/`。

| 项 | 内容 |
|---|---|
| Skill id（现行） | `prompt-optimizer`（曾用 `secretary-prompt-rewrite`） |
| 生产路径 | `/home/box/agent-data/workflows/prompt-optimizer/SKILL.md` |
| P0 判定 | **有条件 Go**（非 Blocker） |
| SKILL 是否改动 | **否** |

## 报告索引

| 报告 | 结果 | 路径 |
|---|---|---|
| rename 后 P0 回归 | **U1–U6 · 6/6 Pass**；静态 Pass | [`uat-prompt-optimizer-post-rename.md`](/workspace/prompt-optimizer/uat-prompt-optimizer-post-rename.md) |
| 开源行为对打 | vs awesome-copilot / prompt-enhancer；壁垒=固定六段+准备门禁+先问用户+苏格拉底分流；**同名须 README 写清** | [`opensource-behavior-bench.md`](/workspace/prompt-optimizer/opensource-behavior-bench.md) |
| 跨 bot U5（爬虫） | 大总管 / Coding / Search **3/3 Pass**（只交六段、无实现） | [`uat-prompt-optimizer-agents-u5.md`](/workspace/prompt-optimizer/uat-prompt-optimizer-agents-u5.md) |

公开 README 已要求写清 vs Copilot 同名差异（六段 system ≠ 单条 chat prompt；**非** Sentry eval 赛道）。见根目录 [README.md](../README.md)。

## 条件备注（非 No-Go）

- U4：六段**标题固定中文**；英文输入 → 段内英文、标题中文（与旧 UAT 相同）。
- 口令落地：`/提示词优化`、`/改写命令`。

## 未验证

- **无口令**时 description 自动加载（路由层）
- **真人**压力测试（本轮均为角色扮演 / 指令触发）

## 待补（发布后）

- [ ] 空仓 `SherryLi-vc/oral-to-prompt` URL 到手后 push（文案已改齐）
- [ ] （可选）无口令自动加载抽测、真人短测
