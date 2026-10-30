#!/usr/bin/env python3
"""Gate ambiguous role prompts before research or delivery."""
import argparse
import json
import re
import sys
from pathlib import Path

ROLES_FILE = Path(__file__).parent / "fixtures" / "fork_roles.yml"

def load_roles():
    roles = []
    for line in ROLES_FILE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-\s*(.+?)\s*$", line)
        if m:
            roles.append(m.group(1))
    return roles

def check(utterance, state, fork_label=""):
    matched = [r for r in load_roles() if r.casefold() in utterance.casefold()]
    valid = state in {"clarified", "skipped", "not_needed"}
    reasons = []
    if matched and not valid:
        reasons.append("命中高分叉角色（" + "、".join(matched) + "），须澄清、跳过或声明不需要")
    if state == "clarified" and not fork_label.strip():
        reasons.append("clarify_state=clarified 时必须提供 fork-label")
    return {"ok": not reasons, "reason": reasons, "required_questions_hint": ("请用 1–3 个选项式短问锁定角色用途、服务对象与场景" if matched else "") , "matched_roles": matched}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--user-utterance", default="")
    p.add_argument("--user-utterance-file")
    p.add_argument("--clarify-state", default="pending", choices=["pending", "clarified", "skipped", "not_needed"])
    p.add_argument("--fork-label", default="")
    a = p.parse_args()
    utterance = a.user_utterance
    if a.user_utterance_file:
        utterance = Path(a.user_utterance_file).read_text(encoding="utf-8")
    result = check(utterance, a.clarify_state, a.fork_label)
    print(json.dumps(result, ensure_ascii=False))
    if not result["ok"]:
        print("；".join(result["reason"]), file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
