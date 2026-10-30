#!/usr/bin/env python3
"""Single entry point for oral-to-prompt hard gates."""
import argparse,json,sys
from pathlib import Path
from gate_clarify import check as clarify_check
from gate_six_sections import check as sections_check
from gate_background_meta import check as meta_check
from gate_checklist import check as checklist_check

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mode",required=True,choices=["pre-research","final"])
    p.add_argument("--draft-file")
    p.add_argument("--user-utterance",default="")
    p.add_argument("--user-utterance-file")
    p.add_argument("--clarify-state",default="pending",choices=["pending","clarified","skipped","not_needed"])
    p.add_argument("--fork-label",default="")
    p.add_argument("--lang",default="auto",choices=["auto","zh","en"])
    p.add_argument("--meta-file")
    a=p.parse_args()
    utterance=a.user_utterance
    try:
        if a.user_utterance_file: utterance=Path(a.user_utterance_file).read_text(encoding="utf-8")
        if a.meta_file:
            meta=json.loads(Path(a.meta_file).read_text(encoding="utf-8"))
            a.clarify_state=meta.get("clarify_state",a.clarify_state); a.fork_label=meta.get("fork_label",a.fork_label)
        results={}
        if a.mode=="pre-research":
            results["clarify"]=clarify_check(utterance,a.clarify_state,a.fork_label)
        else:
            if not a.draft_file: print("--mode final 必须提供 --draft-file",file=sys.stderr); return 2
            draft=Path(a.draft_file).read_text(encoding="utf-8")
            results["six_sections"]=sections_check(draft,a.lang)
            results["background_meta"]=meta_check(draft)
            results["checklist"]=checklist_check(draft,a.clarify_state,a.lang)
            results["clarify"]=clarify_check(utterance,a.clarify_state,a.fork_label)
    except (OSError,ValueError,json.JSONDecodeError) as e:
        print(f"文件/元数据错误：{e}",file=sys.stderr); return 2
    reasons=[f"{name}: {reason}" for name,result in results.items() for reason in result["reason"]]
    output={"ok":not reasons,"mode":a.mode,"results":results,"reasons":reasons}
    print(json.dumps(output,ensure_ascii=False))
    if reasons:
        print("门禁未过："+"；".join(reasons)+"；禁止出终稿",file=sys.stderr); return 1
    return 0
if __name__ == "__main__": raise SystemExit(main())
