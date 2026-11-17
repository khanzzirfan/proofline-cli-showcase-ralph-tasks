---
id: P14
title: "Devs (and agents) can't reproduce the bug QA reported"
who: QA, developers
tools: [any]
status: partly-verified
---
## Pain
"Can't reproduce" is the classic QA-dev loop and it carries over to agents: without exact steps, environment and runtime evidence, the fixer guesses. Agents also lose runtime evidence that the human produced while reproducing.
## Evidence
- https://www.reddit.com/r/QualityAssurance/comments/1nq62ti/how_do_you_deal_with_cant_reproduce_bugs_in_your/ (reddit, 2025-09-25, unverified, SerpAPI snippet): "they'd find an issue, write up a ticket, and devs would say “can't reproduce.”"
- https://www.reddit.com/r/QualityAssurance/comments/1swiriv/how_do_you_deal_with_bug_reports_that_devs_cant/ (reddit, 2026-04-26, unverified, snippet): "provide them the clean system and a video on reproducing it."
- https://www.reddit.com/r/ExperiencedDevs/comments/ointdy/why_is_it_so_hard_to_add_steps_to_reproduce_a_bug/ (reddit, 2021-07-12, unverified, snippet): "I can't fix what I can't reproduce and if I'm guessing at the root cause then I'm more likely to introduce another bug"
- https://overreacted.io/how-to-fix-any-bug/ (blog, verified): "Claude was repeatedly wrong because it didn’t have a repro"
- https://forum.cursor.com/t/debug-mode-browser-fetch-to-ingest-server-127-0-0-1-7772-never-writes-debug-sessionid-log-agent-cant-read-runtime-evidence/167378 (forum, 2026-08-04, verified): "Agent could not read runtime evidence and had to use console.debug + git instead." 94 views
## How users want it fixed
- Video plus clean environment details with each report (reddit QA, unverified).
## Workarounds people use today
- Screen recordings, bug-report tools (Jam, Session Recorder), pairing.
## Session Recorder angle
Core use case, already served (steps, env, console, network, video). Env info is #29; typed values #25. Little novel to add.
## Scores
frequency: 4  severity: 4  fit: 4  smallness: 2  novelty: 1
