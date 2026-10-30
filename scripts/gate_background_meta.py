#!/usr/bin/env python3
"""Reject meta-process language in Task Background / Background."""
import argparse, json, re, sys
from pathlib import Path
SECTION = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$", re.M)
def check(text, patterns_file=None):
    heads=list(SECTION.finditer(text)); body=None
    for i,m in enumerate(heads):
        if m.group(1).strip().casefold() in {"任务背景","background"}:
            end=heads[i+1].start() if i+1<len(heads) else len(text)
            body=text[m.end():end]; break
    reasons=[]
    if body is None: reasons.append("未找到任务背景/Background 段")
    else:
        pf=Path(patterns_file) if patterns_file else Path(__file__).parent/"fixtures/meta_banned_patterns.txt"
        for line in pf.read_text(encoding="utf-8").splitlines():
            pat=line.strip()
            if not pat or pat.startswith("#"): continue
            if re.search(pat,body,re.I): reasons.append("任务背景命中禁用 meta 模式："+pat)
    return {"ok":not reasons,"reason":reasons}
def main():
    p=argparse.ArgumentParser(); p.add_argument("draft_file"); p.add_argument("--patterns-file"); a=p.parse_args()
    r=check(Path(a.draft_file).read_text(encoding="utf-8"),a.patterns_file); print(json.dumps(r,ensure_ascii=False))
    if not r["ok"]: print("；".join(r["reason"]),file=sys.stderr); return 1
    return 0
if __name__ == "__main__": raise SystemExit(main())
