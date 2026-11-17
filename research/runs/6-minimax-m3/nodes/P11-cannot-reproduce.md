---
id: P11
title: "If I can't reproduce it, it doesn't get fixed — and a recording is not a reproduction"
who: developers, QA, support
tools: [jam, playwright, playwright-mcp, momentic, opslane, marucheck]
status: verified
---
## Pain
Support and QA teams lose most reported bugs at the reproduction step: nobody can get the
same failure twice, so the ticket bounces between support and engineering. A screen recording
proves the bug happened but does not prove it will happen again, and an agent cannot re-run
a video. The tools that exist for this are large, paid, or both.

## Evidence
- https://news.ycombinator.com/item?id=42647248 (hn, verified): "unable to repro bugs is one of the biggest reasons that bugs don't get fixed. This leads to communication overhead as engineers and support teams go back and forth in a game of ping pong to try to determine who owns a bug." (signal: 2 points, 2 comments)
- https://news.ycombinator.com/item?id=46047931 (hn, verified): "hoping it can reproduce the behavior" — named as the gap in the agent-led flow (signal: 5 points, 1 comment)
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "Testing was always a pain in the ass (esp Playwright and Selenium), so we built agents to do it for us. Modern day software has a ton of bugs and the change failure rate is only growing faster as coding agent adoption scales." (signal: 168 points, 44 top-level comments; Momentic launch)
- https://news.ycombinator.com/item?id=49644238 (hn, verified): "Show HN: MaruCheck – Independent QA for AI-generated code" (signal: 3 points, 1 comment)
- https://news.ycombinator.com/item?id=47075182 (hn, verified): "Show HN: Crit – Visual QA for iOS apps and AI coding agents" (signal: 5 points, 0 comments)

## How users want it fixed
- Turn a report into a re-runnable script: "AI Agent that turns Jam bug reports into Playwright Tests" (https://news.ycombinator.com/item?id=42647248)
- Have an agent drive the app to find the bug itself: Momentic's "agents that autonomously plan, explore, and bug-bash controls and user flows in your web, iOS, Android, and (soon) desktop apps" (https://news.ycombinator.com/item?id=50339913)
- Open PRs that match real usage: PR #22 in the extension was "Playwright repro test in ZIP", closed by its author (notes, section 3).

## Workarounds people use today
- Playwright MCP / chrome-devtools-mcp drive the app live (57.7k stars; https://github.com/ChromeDevTools/chrome-devtools-mcp)
- Paid QA agents: Momentic, Propolis (116 points, 16 top-level comments; https://news.ycombinator.com/item?id=45762012)
- Manual: a human reproduces it and writes the steps (the status quo)

## Session Recorder angle
This is the pain the notes' option D (Playwright repro test) targeted, and the open PR #22
already tried it and was closed by its author — so a full repro generator is **not** the
clean-PR opportunity. The narrower, cheaper version that fits one PR: the extension already
records clicks, inputs, navigation and network with timestamps, so it can emit a
**deterministic step list** — "clicked X at 0:14, typed 'foo' into Y at 0:16, request Z
returned 500 at 0:18" — that a human or an agent can replay by hand or convert to Playwright
later. That is a text artifact, not a new test runner. Overlapping open PRs: #22 (Playwright
repro test, closed by author) — must not duplicate; #25 (typed value before submit) and
#40 (redirect hops as requests) change what the step list contains.

## Scores
frequency: 4  severity: 5  fit: 3  smallness: 2  novelty: 2
pain_score: 18  pick_score: 28
