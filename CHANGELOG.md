# Changelog

## [0.2.0] — 2026-10-30

### Renamed

- Skill id：`prompt-optimizer` → **`oral-to-prompt`**（与公开仓名对齐）
- Install 路径：`workflows/prompt-optimizer/` → `workflows/oral-to-prompt/`

### Changed

- **description（自动加载）**：补充中英触发词（提示词 / 系统提示词 / prompt / 优化 prompt / 改写命令·口令 / system prompt 等）；写明 Grok Bot 路由靠 description 匹配，口令仅备选；与 `socratic-coach` / `grill-me` / `send-on-behalf` 的分流句保留。
- **SKILL.md 正文**：分流图与展示段中的旧 id 改为 `oral-to-prompt`；适用场景补自然触发例句；不适用补「要直接执行命令而非改写成提示词」分流。六段标题、硬规则原意未改。
- **README / docs**：现行 skill id、Install 路径、触发说明与仓名对齐。

### Notes

- Codex 审读（REVIEW.md，未入库）：P1 文档过期文案与内部路径已在 [PR#1](https://github.com/SherryLi-vc/oral-to-prompt/pull/1) 清完；本版落实 id 对齐与 description 自动加载强化。无口令真人路由与真人压力测试仍待验证，不标为已通过。

## [0.1.0] — 2026-10-29

### Renamed

- Skill id：`secretary-prompt-rewrite` → **`prompt-optimizer`**
- Skill 文件：仓内 [`SKILL.md`](./SKILL.md)
- 语义：通用提示词优化；「私人秘书」仅为可选情景代入

### Added

- 发布至公开仓 [SherryLi-vc/oral-to-prompt](https://github.com/SherryLi-vc/oral-to-prompt)，首发 `main` tip 为 `1031e1c`（详见 [RESULT.md](./RESULT.md)）；包含 README（vs socratic / grill / send-on-behalf）、MIT、示例、触发说明和 UAT 摘要
- 硬规则：不编造、不改原意、先确认准备、改写≠代做、禁假占位、不自动派下游

### Notes

- 内部 UAT（旧 id）：U1–U6 通过已执行的静态检查与模拟用例；P0 判定为**有条件 Go**，仅覆盖这些检查与用例。无口令 description 自动加载及真人压力测试仍未验证。完整报告为内部归档，未公开。

### Docs

- README 大字声明：非 Copilot user-prompt 赛道、非 Sentry eval 赛道、非苏格拉底
- 示例增加「爬虫只出六段」

### Naming（公开仓）

- Search 撞车：**勿**用公开仓名 `prompt-optimizer`
- **用户已定公开仓名：`oral-to-prompt`**（已发布：[SherryLi-vc/oral-to-prompt](https://github.com/SherryLi-vc/oral-to-prompt)；首发 `main` tip `1031e1c`，见 [RESULT.md](./RESULT.md)）
- 本地 skill id 在 0.1.0 仍为 `prompt-optimizer`（与仓名分离；0.2.0 起对齐为 `oral-to-prompt`）
