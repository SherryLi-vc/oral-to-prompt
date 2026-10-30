# oral-to-prompt（提示词优化）

> ## 这不是什么（请先看）
>
> - **不是** [awesome-copilot `prompt-optimizer`](https://github.com/github/awesome-copilot) 那条「把草稿收成**单条可粘贴 user prompt**」赛道。  
> - **不是** [getsentry/skills `prompt-optimizer`](https://github.com/getsentry/skills) 那条 **eval / 多候选 / 跨模型移植** 工程调优赛道。  
> - **不是** `socratic-coach`（炼用户自己的高水平问题）。  
> - **不是** `grill-me`（烤可动手方案）。  
> - **本仓库**：把口语命令改成**固定六段 system / 助手提示词**；**改写 ≠ 代做**（例如「写个爬虫抓 HN」→ 只出六段，**不交爬虫代码**）。

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
| 优化对象 | 口语命令 → **固定六段 system 提示词** | 草稿 → **单条 user prompt**（明确非 API system） | system/developer + **eval 回路** | 用户意图 → **高水平问题句** |
| 输出 | 六段标题锁死的 Markdown 代码块 | 通常一个代码块 user prompt | Target / Success Criteria / Optimized Prompt 等整包 | 【梳理】‖ 问题句 |
| 是否 eval 赛道 | **否**（不做 holdout、多候选、跨模型移植） | 否 | **是** | 否 |
| 「写个爬虫」时 | **只交六段**；本会话不实现 | 改写成更好的 prompt，不执行 | 工程向改写 | 先问清 X，不写六段 |

一句话：**苏格拉底炼「该问什么」；grill 烤「怎么做」；Copilot 类收成聊天 prompt；Sentry 类走 eval；本 skill 只产出固定六段 system 提示词，且绝不代跑任务。**

## 触发

- **自动（主路径）**：Grok Bot 靠 frontmatter `description` 与用户话匹配。用户自然提到「提示词」「系统提示词」「prompt」「优化 prompt / 优化提示词」「改写命令 / 改写口令」「把这段话写成提示词」「帮我写个 system prompt」等，即可加载本 skill，**不必先打口令**。
- **口令（备选）**：`/提示词优化`、`/改写命令`。

语言：跟随本轮输入（中→中，英→英）。

## Install

```text
workflows/
  oral-to-prompt/
    SKILL.md
```

## 六段模板（标题固定，不可增减）

```markdown
# 角色定位
# 任务背景
# 总体目标
# 具体需求
# 输出风格
# 规则限制
```

## 仓库结构

| 路径 | 说明 |
|---|---|
| [`SKILL.md`](./SKILL.md) | 可加载 skill 正文 |
| [`docs/examples/`](./docs/examples/) | 含准备门禁、缺口追问、**爬虫只出六段** |
| [`docs/uat-summary.md`](./docs/uat-summary.md) | U1–U6 与跨 bot U5 的结果、条件性 P0 判定及未验证项摘要 |
| [`CHANGELOG.md`](./CHANGELOG.md) | rename 与版本 |
| [`LICENSE`](./LICENSE) | MIT |

## License

MIT © 2026 SherryLi-vc
