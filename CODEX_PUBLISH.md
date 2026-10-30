你是发布助手。在本机（已 gh 登录 SherryLi-vc）完成公开仓首发。工作目录应为 `/Users/vizhangkk/src/oral-to-prompt`（本目录已有骨架文件：README/SKILL/LICENSE/CHANGELOG/docs…）。

## 必须完成
1. 若 `SherryLi-vc/oral-to-prompt` 尚不存在，执行：
   `gh repo create SherryLi-vc/oral-to-prompt --public --license mit --description "Oral command/draft → fixed six-section system prompt (Grok Bot skill). Not chat rewriter / not eval optimizer."`
   若 `--license` 失败：改为无 license 建空仓（本目录已有 MIT LICENSE 文件）。
2. 若仓已存在且为空/仅有初始文件：继续推送；若已有冲突内容，写入 RESULT.md 说明并停止，勿 force-push。
3. 在本目录：`git init`（若尚无）、`git checkout -B main`、add 全部骨架（勿提交 CODEX_PUBLISH.md / RESULT.md 若你想排除；RESULT.md 可留本地不 push）、commit、`git remote add origin`（或 set-url）、`git push -u origin main`。
4. 验证：`gh repo view SherryLi-vc/oral-to-prompt --json url,isPrivate,defaultBranchRef` 确认 public；记录首个/当前 main tip commit SHA。
5. 写本目录 `RESULT.md`，必须含：
   - URL
   - commit SHA
   - push 是否成功
   - 私有/公开
   - 若有错误原文

禁止：force-push、催用户、删远程历史。（历史备注：首发时曾要求保持 name=`prompt-optimizer`；0.2.0 起已对齐为 `oral-to-prompt`，本文件仅作发布审计，勿再当现行约束。）
完成后退出。
