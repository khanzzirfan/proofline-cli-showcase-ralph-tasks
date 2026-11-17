#!/usr/bin/env bash
# One-shot health check of the current research turn (used by the 5-minute watchdog).
cd "$(dirname "$0")"
date '+now %T'
tail -2 runs/queue.log
grep -q "CHAIN DONE" runs/queue.log && echo "CHAIN DONE"
pgrep -f "bun .*[r]alph-tui run" > /dev/null && echo ralph-alive || echo ralph-NOT-running
pgrep -f "[r]un-chain.sh" > /dev/null && echo chain-alive || echo chain-NOT-running
# The current turn is the most recently started one (a turn can be restarted after a fix).
D=$(grep "START turn" runs/queue.log | tail -1 | sed -E "s/.*START turn [0-9] ([^ ]+).*/runs\/\1\//")
echo "current: ${D:-none}"
[ -z "$D" ] && exit 0
grep -E "\[(progress|engine|WARN|ERROR)\]" "$D/ralph.log" | tail -4
grep -cE "\[(WARN|ERROR)\]" "$D/ralph.log" | sed 's/^/warn+error lines: /'
python3 -c "import json,sys;s=json.load(open(sys.argv[1]))['userStories'];print('passes',sum(x['passes'] for x in s),'/',len(s))" "$D/prd.json"
echo "nodes $(ls "$D/nodes" | wc -l | tr -d ' ') raw $(ls "$D/raw" | wc -l | tr -d ' ')"
find "$D" -type f -print0 | xargs -0 stat -f '%Sm %N' -t '%T' | sort | tail -1 | sed 's/^/newest file: /'
s=$(git -C ../session-recorder-chrome-extension status --short | head -3); echo "extension repo: ${s:-clean}"
