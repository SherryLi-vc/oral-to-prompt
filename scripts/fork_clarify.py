#!/usr/bin/env python3
"""Print short option-style clarification suggestions for a role name."""
import sys

def main():
    role=" ".join(sys.argv[1:]).strip()
    if not role: print("用法：python3 fork_clarify.py 角色名",file=sys.stderr); return 2
    if "英语" in role or "English" in role.casefold():
        qs=["你指哪种用途：AI 英语私教、学校任课老师，还是培训机构教师？", "服务对象和目标是什么：成人/孩子，日常口语/考试/职场？", "需要纯对话，还是也安排练习和纠错？"]
    else:
        qs=[f"你指哪种用途：真人职业模拟、AI 助手人设，还是其他？（{role}）", "服务对象、产品/场合或主要目标是什么？", "有必须包含或排除的职责边界吗？"]
    for q in qs: print("- "+q)
    return 0
if __name__ == "__main__": raise SystemExit(main())
