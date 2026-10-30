#!/usr/bin/env python3
"""Check machine-verifiable final delivery checklist requirements."""
import argparse,json,re,sys
from pathlib import Path
ZH_END="回答前先核对：是否覆盖具体需求且未编造。"
EN_END="Think carefully before answering: cover the specific requirements without inventing facts."
def check(text,state,lang="auto"):
    reasons=[]
    if state=="skipped":
        rules=re.search(r"^\s{0,3}#{1,6}\s+(规则限制|Constraints)\s*$",text,re.M|re.I)
        if not rules: reasons.append("未找到规则限制/Constraints 段")
        else:
            tail=text[rules.end():]
            if not re.search(r"须索取|须向用户索取|must ask|must request",tail,re.I): reasons.append("clarify_state=skipped 时规则限制须含「须索取」类要求")
    endings=([EN_END] if lang=="en" else [ZH_END] if lang=="zh" else [ZH_END,EN_END])
    if not any(x in text for x in endings): reasons.append("缺少固定收尾句")
    return {"ok":not reasons,"reason":reasons}
def main():
    p=argparse.ArgumentParser(); p.add_argument("draft_file"); p.add_argument("--clarify-state",default="not_needed"); p.add_argument("--lang",default="auto",choices=["auto","zh","en"]); a=p.parse_args()
    r=check(Path(a.draft_file).read_text(encoding="utf-8"),a.clarify_state,a.lang); print(json.dumps(r,ensure_ascii=False))
    if not r["ok"]: print("；".join(r["reason"]),file=sys.stderr); return 1
    return 0
if __name__ == "__main__": raise SystemExit(main())
