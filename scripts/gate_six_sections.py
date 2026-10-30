#!/usr/bin/env python3
"""Enforce exactly one fixed six-heading set in the final draft."""
import argparse
import json
import re
import sys
from pathlib import Path

ZH = ["角色定位", "任务背景", "总体目标", "具体需求", "输出风格", "规则限制"]
EN = ["Role", "Background", "Objective", "Requirements", "Output Style", "Constraints"]
HEAD = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.M)
def check(text, lang="auto"):
    heads = [h.strip() for h in HEAD.findall(text)]
    zh_count = sum(h in ZH for h in heads)
    en_count = sum(h in EN for h in heads)
    if lang == "zh": expected = ZH
    elif lang == "en": expected = EN
    elif zh_count and not en_count: expected = ZH
    elif en_count and not zh_count: expected = EN
    else: expected = []
    matches = [i for i in range(len(heads)-5) if heads[i:i+6] == expected] if expected else []
    ok = bool(expected) and len(matches) == 1 and len(heads) == 6 and heads == expected
    why = [] if ok else ["终稿必须恰好包含一套固定六标题，顺序正确且无第七段或混用"]
    return {"ok": ok, "reason": why, "headings": heads}
def main():
    p=argparse.ArgumentParser(); p.add_argument("draft_file"); p.add_argument("--lang",default="auto",choices=["auto","zh","en"]); a=p.parse_args()
    r=check(Path(a.draft_file).read_text(encoding="utf-8"),a.lang); print(json.dumps(r,ensure_ascii=False))
    if not r["ok"]: print("；".join(r["reason"]),file=sys.stderr); return 1
    return 0
if __name__ == "__main__": raise SystemExit(main())
