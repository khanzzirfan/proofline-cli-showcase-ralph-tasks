#!/usr/bin/env bash
# Runs ONE research turn. It first rewrites the shared Ralph config (research/.ralph-tui/config.toml)
# for that turn's agent and model, then runs Ralph in the turn's own folder. Each run folder's
# .ralph-tui/config.toml is a symlink to the shared config, while progress.md stays per run.
# Usage: research/run-turn.sh <1-8>
#   1 = Command Code + deepseek/deepseek-v4-flash
#   2 = Command Code + minimax/minimax-m3.1-flash
#   3 = Command Code + gpt-6-luna
#   4 = Claude Code + sonnet
#   Round 2, top-tier models, same task:
#   5 = Command Code + deepseek/deepseek-v4-pro
#   6 = Command Code + minimaxai/minimax-m3
#   7 = Command Code + gpt-6-astra
#   8 = Claude Code + opus
set -u
cd "$(dirname "$0")"
R=$(pwd)
case "${1:-}" in
  1) name=1-deepseek-v4-flash;  agent=command-code-research; model=deepseek/deepseek-v4-flash ;;
  2) name=2-minimax-m3.1-flash; agent=command-code-research; model=minimax/minimax-m3.1-flash ;;
  3) name=3-gpt-6-luna;         agent=command-code-research-std; model=gpt-6-luna ;;
  4) name=4-claude-sonnet;      agent=claude;                model=sonnet ;;
  5) name=5-deepseek-v4-pro;    agent=command-code-research; model=deepseek/deepseek-v4-pro ;;
  6) name=6-minimax-m3;         agent=command-code-research; model=minimaxai/minimax-m3 ;;
  7) name=7-gpt-6-astra;        agent=command-code-research-std; model=gpt-6-astra ;;
  8) name=8-claude-opus;        agent=claude;                model=opus ;;
  *) echo "usage: $0 <1-8>" >&2; exit 64 ;;
esac
# "[r]alph" matches a running Ralph but not a shell whose command line merely contains this pattern.
if pgrep -f "bun .*[r]alph-tui run" > /dev/null; then echo "another Ralph run is still going; wait for it" >&2; exit 75; fi

cat > "$R/.ralph-tui/config.toml" <<EOF
# Shared Ralph config for the pain research. Rewritten by run-turn.sh at the start of each turn.
# Current turn: $1 ($name), started $(date '+%F %T')
configVersion = "2.1"
tracker = "json"
agent = "$agent"
maxIterations = 15
autoCommit = false
envPassthrough = ["CMDC_KEY"]

[trackerOptions]
[agentOptions]
model = "$model"
EOF

dir="$R/runs/$name"
passes() { python3 -c 'import json,sys;s=json.load(open(sys.argv[1]))["userStories"];print(f"{sum(x["passes"] for x in s)}/{len(s)}")' "$dir/prd.json"; }
LOG="$R/runs/queue.log"
echo "$(date '+%F %T') START turn $1 $name agent=$agent model=$model ($(passes))" >> "$LOG"
start=$(date +%s)
(cd "$dir" && ralph-tui run --prd ./prd.json --iterations 15 --headless --verify >> "$dir/ralph.log" 2>&1)
code=$?
echo "$(date '+%F %T') END turn $1 $name exit=$code passes=$(passes) minutes=$(( ($(date +%s) - start) / 60 ))" >> "$LOG"
python3 "$R/compare.py" > /dev/null 2>&1 || true
exit $code
