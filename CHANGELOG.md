# Changelog

## [0.1.0] — 2026-10-29

### Renamed

- Skill id：`secretary-prompt-rewrite` → **`prompt-optimizer`**
- 生产路径：`/home/box/agent-data/workflows/prompt-optimizer/SKILL.md`
- 语义：通用提示词优化；「私人秘书」仅为可选情景代入

### Added

- 公开仓最小骨架：README（vs socratic / grill / send-on-behalf）、MIT、示例、触发说明、UAT 摘要占位
- 硬规则：不编造、不改原意、先确认准备、改写≠代做、禁假占位、不自动派下游

### Notes

- 内部 UAT（旧 id）：U1–U6 Go。完整报告归档 `/workspace/prompt-optimizer/`（见 `INDEX.md`）。

### Docs

- README 大字声明：非 Copilot user-prompt 赛道、非 Sentry eval 赛道、非苏格拉底
- 示例增加「爬虫只出六段」

### Naming（公开仓）

- Search 撞车：**勿**用公开仓名 `prompt-optimizer`
- **用户已定公开仓名：`oral-to-prompt`**（拟 `SherryLi-vc/oral-to-prompt`）
- 本地 skill id 仍为 `prompt-optimizer`（与仓名分离）
- 等空仓 URL 后 push
