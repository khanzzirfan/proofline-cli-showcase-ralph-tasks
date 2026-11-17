#!/usr/bin/env bash
# Runs research turns strictly one after another.
# Usage: research/run-chain.sh 2 3 4 5 6 7 8
# Waits for any Ralph run already going, then for each turn: run-turn.sh rewrites the shared
# config and runs Ralph. After each turn it logs any change in the extension repo (runs must
# only read it), and it pauses the chain if the turn passed no story at all.
# Fixed after the run: the logged exit code. `$?` used to sit in the same string as `$(date)`,
# which reset it, so every "CHAIN turn N exit=" line in runs/queue.log reads 0.
set -u
cd "$(dirname "$0")"
LOG=runs/queue.log
while pgrep -f "bun .*[r]alph-tui run" > /dev/null; do sleep 20; done
for turn in "$@"; do
  ./run-turn.sh "$turn"
  code=$?
  echo "$(date '+%F %T') CHAIN turn $turn exit=$code" >> "$LOG"
  stray=$(git -C ../session-recorder-chrome-extension status --short | head -5)
  [ -n "$stray" ] && echo "$(date '+%F %T') WARNING turn $turn: extension repo changed: $stray" >> "$LOG"
  # Safety stop: a turn that passed no story at all is broken (agent setup, model access), so pause the chain.
  passed=$(python3 -c 'import json,glob,sys;f=glob.glob(f"runs/{sys.argv[1]}-*/prd.json")[0];print(sum(s["passes"] for s in json.load(open(f))["userStories"]))' "$turn")
  if [ "$passed" = "0" ]; then echo "$(date '+%F %T') CHAIN PAUSED: turn $turn passed no story; fix it, then rerun run-chain.sh from turn $turn" >> "$LOG"; exit 3; fi
done
python3 compare.py > /dev/null 2>&1
echo "$(date '+%F %T') CHAIN DONE ($*)" >> "$LOG"
