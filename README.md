# oral-to-prompt

[![License: MIT](https://img.shields.io/github/license/SherryLi-vc/oral-to-prompt)](./LICENSE) [![Release](https://img.shields.io/github/v/release/SherryLi-vc/oral-to-prompt)](https://github.com/SherryLi-vc/oral-to-prompt/releases/latest)

**English** · [简体中文](./README.zh-CN.md)

> Give it a simple prompt or just a role name: it researches what a senior, excellent practitioner in that role knows and does, then writes a complete six-section system prompt — rewritten, never executed.

oral-to-prompt is an Agent Skills skill (a `SKILL.md` folder) for any agent that supports the format. You give it a simple prompt, a rough draft, or just a role name. When a role is named, it first researches the knowledge, skills, traits, and boundaries of a senior, excellent practitioner in that role and tags every point by evidence type; then it writes six fixed sections (Role, Background, Objective, Requirements, Output Style, Constraints) that any assistant can take as its system prompt. Facts about your own task are never invented: missing ones are asked for. It is not a single chat-prompt rewriter and not an eval-driven prompt optimizer.

- **Fixed six sections**: Two locked heading sets, Chinese or English, chosen by the input language; no sections added, removed, renamed, or mixed.
- **Role research**: Naming a role triggers a search for the knowledge, skills, traits, and boundaries of a senior practitioner, each tagged 【来源】/【综合·多来源】/【推断】 (source / multi-source / inferred); no invented "senior standards".
- **Clarify ambiguous roles first**: Roles with obvious forks (e.g. "English teacher") get 1–3 short questions before any research.
- **Rewrite, never execute**: "Write a crawler for HN" yields a six-section prompt, not crawler code.
- **Python hard gates**: `scripts/gate_final.py` checks clarification before research, and six-section structure, meta-free Background, and the checklist before delivery; Python 3 standard library only.
- **Auto-trigger**: Loads when the frontmatter description matches; optional trigger phrases `/提示词优化` and `/改写命令`.

## Quick start / Install

The repository root is the skill folder. Clone or copy it into a skills directory and keep the folder name equal to the skill `name`; keep `scripts/` next to `SKILL.md` (cloning this repository does this). Python 3 is needed to run the gates.

Shared user-level path read by Codex, Cursor, Gemini CLI and OpenCode:

```bash
git clone https://github.com/SherryLi-vc/oral-to-prompt.git ~/.agents/skills/oral-to-prompt
```

Claude Code (also read by Cursor and OpenCode):

```bash
git clone https://github.com/SherryLi-vc/oral-to-prompt.git ~/.claude/skills/oral-to-prompt
```

Gemini CLI alternative: `gemini skills install https://github.com/SherryLi-vc/oral-to-prompt.git`.

Project-level: put the folder under `.agents/skills/oral-to-prompt/` (or `.claude/skills/oral-to-prompt/`) in your repository. Other hosts that load `SKILL.md` folders can use a copy of the whole folder, including sibling files.

### How to invoke

| Host | Invocation |
|---|---|
| All compatible hosts | Auto-load when the description matches |
| Claude Code | `/oral-to-prompt` |
| Codex | `$oral-to-prompt` |
| Cursor | `/` menu |
| Gemini CLI | Loads via its `activate_skill` flow |

Chinese trigger phrases such as `/提示词优化` are phrases matched by the description; every host may not register them as slash commands.

**Compatibility:** [Agent Skills specification](https://agentskills.io/specification); [Claude Code](https://code.claude.com/docs/en/skills); [OpenAI Codex](https://developers.openai.com/codex/skills); [Cursor](https://cursor.com/docs/context/skills); [Gemini CLI](https://geminicli.com/docs/cli/skills/); [OpenCode](https://opencode.ai/docs/skills/).

### Run the gates

From the skill folder:

```bash
python3 scripts/gate_final.py --mode pre-research --user-utterance "写一个关于英语老师的提示词" --clarify-state clarified --fork-label "AI英语私教"
python3 scripts/gate_final.py --mode final --draft-file scripts/fixtures/testdata/v4_english_teacher_ok.md --clarify-state clarified --fork-label "AI英语私教" --lang zh
```

## What this is not

- Not [awesome-copilot prompt-optimizer](https://github.com/github/awesome-copilot): that project turns a draft into a single pasteable user prompt.
- Not [getsentry/skills prompt-optimizer](https://github.com/getsentry/skills): that project focuses on evals, multiple candidates, and cross-model prompt porting.
- Not `socratic-coach` (developing the user's question) or `grill-me` (challenging a plan).
- **What it is**: you give a simple prompt or just a role name; when a role is named, it first researches what a senior, excellent practitioner in that role knows and does (each point tagged 【来源】/【综合·多来源】/【推断】), then writes a complete fixed six-section system prompt. It only writes the prompt; it never does the task itself.

## Workflow

1. **Clarify** ambiguous roles with 1–3 short questions before research.
2. **Phase A · Role research (optional):** for a named role without a self-contained role description, research the knowledge, skills, traits, boundaries, and common situations of an excellent senior practitioner. Tag evidence and do not invent standards.
3. **Phase B · Six-section rewrite:** combine the user's intent, research, and any clarified details into the fixed template. The user's intent takes priority.
4. **Gates:** run the bundled checks for clarification, six-section structure, Background meta content, and the final checklist before delivery.

Skip Phase A when the user provides a self-contained role description, asks not to research, requests a plain task rewrite without naming a professional role, or only wants an existing six-section prompt polished.

## Six-section headings

| # | Chinese | English |
|---|---|---|
| 1 | 角色定位 | Role |
| 2 | 任务背景 | Background |
| 3 | 总体目标 | Objective |
| 4 | 具体需求 | Requirements |
| 5 | 输出风格 | Output Style |
| 6 | 规则限制 | Constraints |

## Repository structure

| Path | Purpose |
|---|---|
| [`SKILL.md`](./SKILL.md) | Skill instructions |
| [`scripts/`](./scripts/) | Gate scripts, fixtures, and usage notes |
| [`docs/examples/`](./docs/examples/) | Worked examples |
| [`docs/uat-summary.md`](./docs/uat-summary.md) | User acceptance test summary |
| [`CHANGELOG.md`](./CHANGELOG.md) | Version history |
| [`LICENSE`](./LICENSE) | MIT license |

## License

MIT © 2026 SherryLi-vc
