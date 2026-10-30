# UAT 摘要

> 公开仓 [SherryLi-vc/oral-to-prompt](https://github.com/SherryLi-vc/oral-to-prompt) 已发布，首发 `main` tip 为 `1031e1c`（详见 [RESULT.md](../RESULT.md)）。完整报告为内部归档，未公开。0.2.0 起 skill id 与仓名对齐为 `oral-to-prompt`；六段标题与硬规则原意未改。

| 项 | 内容 |
|---|---|
| Skill id（现行） | **`oral-to-prompt`**（曾用 `prompt-optimizer` / `secretary-prompt-rewrite`） |
| Skill 文件 | 仓内 [`SKILL.md`](../SKILL.md) |
| P0 判定 | **有条件 Go**；仅覆盖静态检查与模拟用例，不代表整体生产就绪 |
| SKILL 0.2.0 变更 | id 对齐 + description 自动加载强化；六段与硬规则原意未改 |

## 报告索引

| 报告 | 结果 | 路径 |
|---|---|---|
| rename 后 P0 回归 | **U1–U6 · 6/6 Pass**；模拟用例及静态检查结果 | 内部归档，未公开 |
| 开源行为对打 | vs awesome-copilot / prompt-enhancer；壁垒=固定六段+准备门禁+先问用户+苏格拉底分流；**同名须 README 写清** | 内部归档，未公开 |
| 跨 bot U5（爬虫） | 大总管 / Coding / Search **3/3 Pass**（只交六段、无实现） | 内部归档，未公开 |

公开 README 已要求写清 vs Copilot 同名差异（六段 system ≠ 单条 chat prompt；**非** Sentry eval 赛道）。见根目录 [README.md](../README.md)。

## 条件备注（非 No-Go）

- U4：六段**标题固定中文**；英文输入 → 段内英文、标题中文（与旧 UAT 相同）。
- 口令落地：`/提示词优化`、`/改写命令`（备选；主路径为 description 自动命中）。

## 未验证

- **无口令**时 description 自动加载（路由层；0.2.0 已强化 description 触发词，仍待真人/运行时抽测）
- **真人**压力测试（本轮均为角色扮演 / 指令触发）

因此，P0 的**有条件 Go**只适用于已执行的静态检查与模拟用例；无口令自动加载和真人压力测试仍未验证，不应视为已通过。

## 待补（发布后）

- [x] 发布至 [SherryLi-vc/oral-to-prompt](https://github.com/SherryLi-vc/oral-to-prompt)；首发 `main` tip `1031e1c`（见 [RESULT.md](../RESULT.md)）
- [ ] （可选）无口令自动加载抽测、真人短测
