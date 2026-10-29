#!/bin/bash
set -euo pipefail
cd /Users/vizhangkk/src/oral-to-prompt
exec /Users/vizhangkk/.hermes/node/bin/codex exec \
  --dangerously-bypass-approvals-and-sandbox \
  --skip-git-repo-check \
  "$(cat /Users/vizhangkk/src/oral-to-prompt/CODEX_PUBLISH.md)"
