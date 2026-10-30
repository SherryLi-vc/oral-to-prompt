# Changelog

## [0.4.0] — 2026-10-30

### Added

- P1：模糊角色在调研前进行 1–3 个短问澄清；拒问时记录须索取项。
- P2：任务背景限定为下游真实执行场景，禁止提示词交付过程等 meta 内容。
- Python 硬门禁：`gate_clarify.py`、`gate_six_sections.py`、`gate_background_meta.py`、`gate_checklist.py` 与总入口 `gate_final.py`；附分叉建议、fixtures 和使用说明。
- 更新 SKILL v0.4、纯正文及独立 description 文本。


## [0.3.0] — 2026-10-30

### Added

- **阶段 A · 角色/岗位调研**：用户点名角色/岗位（或草稿里角色过薄）时，先检索「资深且优秀的 xxx」的知识、能力、特质、职责边界、常见场景，再归档进六段。证据标注【来源】/【综合·多来源】/【推断】（推断建议 ≤20%）；禁止无检索捏造「资深标准」、虚构 JD 原文或证书年限。
- 跳过阶段 A 的条件：职责 + 边界自洽的角色说明书；用户说别搜；纯任务改写；只润色已有六段。
- 交付说明新增「本轮调研：开（来源类型）/ 关（原因）」，以及与原意冲突时的取舍说明。
- 示例 [`05-role-name-only.md`](./docs/examples/05-role-name-only.md)：只给岗位名的完整流程。
- 示例 [`06-english-heading-set.md`](./docs/examples/06-english-heading-set.md)：英文输入 → 英文标题套。

### Changed

- 已拍板默认：调研后**自动归档**，只有冲突或失败时才问用户；**不新增口令**；用户要求时才另附调研原文；准备门禁可与首包材料合并，少一轮。
- **六段标题按语种分两套**：中文输入用原中文套（角色定位 / 任务背景 / 总体目标 / 具体需求 / 输出风格 / 规则限制）；英文输入用固定英文套（Role / Background / Objective / Requirements / Output Style / Constraints），顺序一一对应。「标题不可改」改为「按语种选两套之一，套内不可改、不可增减、不混用」；自检清单与反例同步。取代 v0.2 的「英文输入 → 标题仍中文」。
- 硬规则 1 区分「用户事实」（仍禁止编造）与「角色共性」（须来自检索并标注）；硬规则 2/3/4/5 补充调研相关表述。**硬规则原意与中文六段标题未改。**
- description 补充「写一段 xxx 角色/岗位的提示词」「write a system prompt for a senior xxx」等触发；写明不等于「现在就扮演该角色干活」。
- 分流图新增「直接执行意图」一条；注明角色调研 ≠ 苏格拉底 ≠ grill。

### Notes

- v0.3 U1–U8 只做了静态/模拟走查（U1 阶段 A 为真实检索）；未建测试 bot、未实机运行。U5（英文输入）已按用户拍板改为英文标题套，见 [UAT 摘要](./docs/uat-summary.md)。

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
