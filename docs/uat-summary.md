# UAT 摘要

> 已于 v0.4.0 发布，tag 指向 `5b71a64`：[v0.4.0 release](https://github.com/SherryLi-vc/oral-to-prompt/releases/tag/v0.4.0)。六段标题与硬规则原意未改。

| 项 | 内容 |
|---|---|
| Skill id（现行） | **`oral-to-prompt`**（曾用 `prompt-optimizer` / `secretary-prompt-rewrite`） |
| Skill 文件 | 仓内 [`SKILL.md`](../SKILL.md) |
| P0 判定 | **有条件 Go**；覆盖静态检查、模拟用例及下列真人测试，不代表所有宿主均已验证 |
| SKILL 0.2.0 变更 | id 对齐 + description 自动加载强化；六段与硬规则原意未改 |
| SKILL 0.3.0 变更 | 新增阶段 A 角色调研；六段标题按语种分中/英两套（中文套未改）；硬规则原意未改 |

## 报告索引

| 报告 | 结果 |
|---|---|
| rename 后 P0 回归 | **U1–U6 · 6/6 Pass**；模拟用例及静态检查 |
| 开源行为对打 | vs awesome-copilot / prompt-enhancer；差异为固定六段、准备门禁、先问用户与苏格拉底分流 |
| 跨 3 个不同 agent 的 U5（爬虫） | **3/3 Pass**（只交六段、无实现） |

## v0.3 U1–U8（静态/模拟走查，2026-10-30）

> 执行者扮演用户并按 SKILL 推演；未实机运行。U1 阶段 A 为真实网页检索，样例见 [05-role-name-only.md](./examples/05-role-name-only.md)。

| ID | 场景 | 判定 |
|---|---|---|
| U1 | 只给岗位名「资深产品经理」→ 调研 → 六段 | ✅ 模拟通过 |
| U2 | 「严格 code reviewer，别客气」草稿 → 保留原语气 | ✅ 模拟通过 |
| U3 | 完整角色说明书 → 跳过调研 | ✅ 模拟通过（阈值为启发式） |
| U4 | 拒绝补充业务域 → 写入「执行者须索取」 | ✅ 模拟通过 |
| U5 | 英文 senior SRE | ✅ 模拟通过：调研、正文与标题全英，见 [06-english-heading-set.md](./examples/06-english-heading-set.md) |
| U6 | 「把邮件发给老板」→ send-on-behalf | ✅ 静态通过 |
| U7 | 「你现在是资深律师，马上审合同」→ 不代做 | ✅ 静态通过（运行时路由未验） |
| U8 | 纯任务「整理发票」→ 不调研、不扩 scope | ✅ 模拟通过 |

## v0.4 真人测试（2026-10-30）

维护者在一个新测试 agent 上进行了真人测试：该 agent 已安装 skill，但未预先加载，因此测试覆盖了 description 自动加载；维护者确认「测试通过」。这是目前唯一经过真人测试的宿主。

门禁 fixture 验证：

| 检查 | 结果 |
|---|---:|
| `v4_english_teacher_ok.md`（final） | exit 0 |
| `v4_english_teacher_meta_bad.md`（final） | 非 0 |
| 英语老师未澄清（pre-research pending） | 非 0 |
| 英语老师已澄清（pre-research clarified） | exit 0 |

## 未验证

- 只有一个宿主完成真人测试；其他宿主依据 Agent Skills 格式和公开规范核对，尚未逐一实机验证。
- 不同宿主的 description 自动加载细节、阶段 A 检索质量与来源标注纪律仍可能不同。
