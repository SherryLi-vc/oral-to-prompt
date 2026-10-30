# oral-to-prompt（提示词优化）

[![License: MIT](https://img.shields.io/github/license/SherryLi-vc/oral-to-prompt)](./LICENSE) [![Release](https://img.shields.io/github/v/release/SherryLi-vc/oral-to-prompt)](https://github.com/SherryLi-vc/oral-to-prompt/releases/latest)

[English](./README.md) · **简体中文**

> 把口语命令、草稿或一个角色名，改写成固定六段式系统提示词：只改写，不代做。

oral-to-prompt 是一个遵循 Agent Skills 格式（`SKILL.md` 文件夹）的通用 skill，适用于支持该格式的 agent。它把你的原话结构化为固定六段（角色定位、任务背景、总体目标、具体需求、输出风格、规则限制），可直接交给任意助手作为 system 提示词。点名角色或岗位时，先检索「资深且优秀的 xxx」应具备的知识与能力，并为每条标注证据类型。它不是单条聊天 prompt 改写器，也不是 eval 赛道的提示词调优工具。

- **固定六段**：根据输入语言选择中文或英文标题套；不增删、改名或混用标题。
- **角色调研**：点名角色时，检索资深从业者的知识、能力、特质与职责边界，逐条标注【来源】/【综合·多来源】/【推断】；不捏造「资深标准」。
- **先澄清模糊角色**：明显存在分叉的岗位（如「英语老师」）会在调研前先问 1–3 个简短问题。
- **只改写，不代做**：「写个爬虫抓 HN」会得到六段提示词，不会得到爬虫代码。
- **Python 硬门禁**：`scripts/gate_final.py` 在交付前检查调研前澄清、六段结构、无 meta 的任务背景和自检清单；仅使用 Python 3 标准库。
- **自动触发**：frontmatter 描述匹配时加载；可选触发词 `/提示词优化` 和 `/改写命令`。

## 快速开始 / 安装

仓库根目录就是 skill 文件夹。将其克隆或复制到 skills 目录，并确保文件夹名与 skill 的 `name` 一致；`scripts/` 须与 `SKILL.md` 放在一起（克隆本仓库即可满足）。运行门禁需要 Python 3。

Codex、Cursor、Gemini CLI 和 OpenCode 读取的共享用户级目录：

```bash
git clone https://github.com/SherryLi-vc/oral-to-prompt.git ~/.agents/skills/oral-to-prompt
```

Claude Code（Cursor 和 OpenCode 也读取此目录）：

```bash
git clone https://github.com/SherryLi-vc/oral-to-prompt.git ~/.claude/skills/oral-to-prompt
```

Gemini CLI 也可运行：`gemini skills install https://github.com/SherryLi-vc/oral-to-prompt.git`。

项目级安装：将文件夹放入项目中的 `.agents/skills/oral-to-prompt/`（或 `.claude/skills/oral-to-prompt/`）。其他能加载 `SKILL.md` 文件夹的宿主可复制整个文件夹，并保留同级文件。

### 如何调用

| 宿主 | 调用方式 |
|---|---|
| 所有兼容宿主 | frontmatter 描述匹配时自动加载 |
| Claude Code | `/oral-to-prompt` |
| Codex | `$oral-to-prompt` |
| Cursor | `/` 菜单 |
| Gemini CLI | 通过 `activate_skill` 流程加载 |

`/提示词优化` 等中文口令是由 description 匹配的触发词，并非每个宿主都将其注册为斜杠命令。

**兼容性：**[Agent Skills 规范](https://agentskills.io/specification)；[Claude Code](https://code.claude.com/docs/en/skills)；[OpenAI Codex](https://developers.openai.com/codex/skills)；[Cursor](https://cursor.com/docs/context/skills)；[Gemini CLI](https://geminicli.com/docs/cli/skills/)；[OpenCode](https://opencode.ai/docs/skills/)。

### 运行门禁

在 skill 文件夹内运行：

```bash
python3 scripts/gate_final.py --mode pre-research --user-utterance "写一个关于英语老师的提示词" --clarify-state clarified --fork-label "AI英语私教"
python3 scripts/gate_final.py --mode final --draft-file scripts/fixtures/testdata/v4_english_teacher_ok.md --clarify-state clarified --fork-label "AI英语私教" --lang zh
```

## 本 skill 不是什么

- 不是 [awesome-copilot prompt-optimizer](https://github.com/github/awesome-copilot)：该项目把草稿改成一条可粘贴的 user prompt。
- 不是 [getsentry/skills prompt-optimizer](https://github.com/getsentry/skills)：该项目侧重 eval、多候选和跨模型迁移。
- 不是 `socratic-coach`（打磨用户的问题）或 `grill-me`（挑战方案）。
- 本 skill 把口语命令、草稿或角色名改写成固定六段式 system 提示词。点名角色时会先调研；改写不等于执行任务。

## 工作流程

1. **澄清**：角色存在明显分叉时，在调研前先问 1–3 个简短问题。
2. **阶段 A · 角色调研（可选）**：用户点名岗位且未提供完整角色说明时，调研优秀资深从业者的知识、能力、特质、边界与常见场景。标注证据，不捏造标准。
3. **阶段 B · 六段改写**：结合用户原意、调研结果和澄清信息，按固定模板整理；用户原意优先。
4. **门禁**：交付前运行配套检查，核对澄清、六段结构、任务背景 meta 内容和自检清单。

以下情况跳过阶段 A：用户提供了职责与边界完整的角色说明、明确要求不调研、只要求改写普通任务而未点名专业角色，或只要求润色已有六段提示词。

## 六段标题

| # | 中文 | 英文 |
|---|---|---|
| 1 | 角色定位 | Role |
| 2 | 任务背景 | Background |
| 3 | 总体目标 | Objective |
| 4 | 具体需求 | Requirements |
| 5 | 输出风格 | Output Style |
| 6 | 规则限制 | Constraints |

## 仓库结构

| 路径 | 用途 |
|---|---|
| [`SKILL.md`](./SKILL.md) | Skill 正文 |
| [`scripts/`](./scripts/) | 门禁脚本、fixtures 与使用说明 |
| [`docs/examples/`](./docs/examples/) | 完整示例 |
| [`docs/uat-summary.md`](./docs/uat-summary.md) | 用户验收测试摘要 |
| [`CHANGELOG.md`](./CHANGELOG.md) | 版本记录 |
| [`LICENSE`](./LICENSE) | MIT 许可 |

## 许可

MIT © 2026 SherryLi-vc
