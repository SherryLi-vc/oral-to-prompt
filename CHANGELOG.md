# Changelog

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
- 本地 skill id 仍为 `prompt-optimizer`（与仓名分离）
