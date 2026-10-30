# oral-to-prompt v0.4 gates

所有脚本只依赖 Python 3，无第三方包。交付前统一调用 `gate_final.py`。阶段 A 调研前使用 `--mode pre-research`；若失败，只做短问，不开搜、不出六段。终稿使用 `--mode final --draft-file ...`；门禁失败时禁止交付终稿。

```bash
python3 scripts/gate_final.py --mode pre-research --user-utterance "写一个关于英语老师的提示词" --clarify-state pending
python3 scripts/gate_final.py --mode pre-research --user-utterance "写一个关于英语老师的提示词" --clarify-state clarified --fork-label "AI英语私教"
python3 scripts/gate_final.py --mode final --draft-file draft.md --clarify-state clarified --fork-label "AI英语私教" --lang zh
python3 scripts/fork_clarify.py 英语老师
```

失败时 stderr 会列出中文原因及「门禁未过：…禁止出终稿」；修正后重跑。
