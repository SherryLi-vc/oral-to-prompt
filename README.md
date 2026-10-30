# oral-to-prompt（提示词优化）

> ## 这不是什么（请先看）
>
> - **不是** [awesome-copilot `prompt-optimizer`](https://github.com/github/awesome-copilot) 那条「把草稿收成**单条可粘贴 user prompt**」赛道。  
> - **不是** [getsentry/skills `prompt-optimizer`](https://github.com/getsentry/skills) 那条 **eval / 多候选 / 跨模型移植** 工程调优赛道。  
> - **不是** `socratic-coach`（炼用户自己的高水平问题）。  
> - **不是** `grill-me`（烤可动手方案）。  
> - **本仓库**：把口语命令、草稿或**角色/岗位名**改成**固定六段 system / 助手提示词**；点名角色时先做**角色调研**（检索「资深且优秀的 xxx」，标【来源】/【推断】）；**改写 ≠ 代做**（例如「写个爬虫抓 HN」→ 只出六段，**不交爬虫代码**）。

Grok Bot / Cursor skill。

| 项 | 现行 |
|---|---|
| **公开 GitHub 仓名** | **`oral-to-prompt`**（用户已定；**勿用**撞车名 `prompt-optimizer` 作仓名） |
| 本地 skill id | **`oral-to-prompt`**（与仓名对齐；曾用 `prompt-optimizer` / `secretary-prompt-rewrite`） |
| 已发布仓库 | [SherryLi-vc/oral-to-prompt](https://github.com/SherryLi-vc/oral-to-prompt)（公开；首发 tip：`1031e1c`，详见 [RESULT.md](./RESULT.md)；现行 `main` 随版本更新） |

「私人秘书」仅为可选情景代入。见 [CHANGELOG](./CHANGELOG.md)。

## 与 Copilot / Sentry / 苏格拉底 的差异

| | **本 skill** | **Copilot prompt-optimizer** | **Sentry prompt-optimizer** | **socratic-coach** |
|---|---|---|---|---|
| 优化对象 | 口语命令 / 角色名 →（角色调研）→ **固定六段 system 提示词** | 草稿 → **单条 user prompt**（明确非 API system） | system/developer + **eval 回路** | 用户意图 → **高水平问题句** |
| 输出 | 六段标题锁死的 Markdown 代码块 | 通常一个代码块 user prompt | Target / Success Criteria / Optimized Prompt 等整包 | 【梳理】‖ 问题句 |
| 是否 eval 赛道 | **否**（不做 holdout、多候选、跨模型移植） | 否 | **是** | 否 |
| 「写个爬虫」时 | **只交六段**；本会话不实现 | 改写成更好的 prompt，不执行 | 工程向改写 | 先问清 X，不写六段 |

一句话：**苏格拉底炼「该问什么」；grill 烤「怎么做」；Copilot 类收成聊天 prompt；Sentry 类走 eval；本 skill 只产出固定六段 system 提示词，且绝不代跑任务。**

## 两阶段流程（v0.3）

1. **阶段 A · 角色调研**（用户点名角色/岗位，且没给自洽的角色说明书时）：检索「资深且优秀的 xxx」的知识、能力、特质、职责边界、常见场景；每条标【来源】/【综合·多来源】/【推断】；**禁止无搜捏造**。默认自动归档，只有冲突或检索失败时才问用户。
2. **阶段 B · 六段改写**（v0.2 原流程）：用户原意 + 调研 + 追问补齐 → 固定六段。用户原意优先于调研。

跳过阶段 A：用户贴了职责 + 边界自洽的角色说明书；用户说「别搜」；纯任务改写、未点名角色；只润色已有六段。

## 触发

- **自动（主路径）**：Grok Bot 靠 frontmatter `description` 与用户话匹配。用户自然提到「提示词」「系统提示词」「prompt」「优化 prompt / 优化提示词」「改写命令 / 改写口令」「把这段话写成提示词」「帮我写个 system prompt」，或「写一段关于 xxx（角色/岗位）的提示词」「write a system prompt for a senior xxx」等，即可加载本 skill，**不必先打口令**。
- **口令（备选）**：`/提示词优化`、`/改写命令`。

语言：跟随本轮输入（中→中，英→英）。

## Install

```text
workflows/
  oral-to-prompt/
    SKILL.md
```

## 六段模板（按语种选两套之一；套内标题固定，不可增减、不混用）

中文输入用中文套，英文输入用英文套，顺序一一对应：

| # | 中文套 | 英文套 |
|---|---|---|
| 1 | `# 角色定位` | `# Role` |
| 2 | `# 任务背景` | `# Background` |
| 3 | `# 总体目标` | `# Objective` |
| 4 | `# 具体需求` | `# Requirements` |
| 5 | `# 输出风格` | `# Output Style` |
| 6 | `# 规则限制` | `# Constraints` |

## 仓库结构

| 路径 | 说明 |
|---|---|
| [`SKILL.md`](./SKILL.md) | 可加载 skill 正文 |
| [`docs/examples/`](./docs/examples/) | 含准备门禁、缺口追问、**爬虫只出六段**、**只给岗位名（角色调研）**、**英文标题套** |
| [`docs/uat-summary.md`](./docs/uat-summary.md) | v0.2 U1–U6、v0.3 U1–U8 模拟走查、条件性判定及未验证项 |
| [`CHANGELOG.md`](./CHANGELOG.md) | rename 与版本 |
| [`LICENSE`](./LICENSE) | MIT |

## License

MIT © 2026 SherryLi-vc
