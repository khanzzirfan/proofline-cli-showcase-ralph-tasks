# Comparison of the four research runs

## Run health

| Run | Stories passed | Nodes | Verified line in sources.md | Files |
|---|---|---|---|---|
| 1-deepseek-v4-flash | 5/5 | 14 | verified: 67, unverified: 12, dropped: 4 | plan.md, ranking.json, ranking.md, recommendation.md, run-summary.md, sources.md |
| 2-minimax-m3.1-flash | 5/5 | 14 | verified: 60, unverified: 0, dropped: 1 | plan.md, ranking.json, ranking.md, recommendation.md, run-summary.md, sources.md |
| 3-gpt-6-luna | 5/5 | 13 | verified: 14, unverified: 4, dropped: 1 | plan.md, ranking.json, ranking.md, recommendation.md, run-summary.md, sources.md |
| 4-claude-sonnet | 5/5 | 13 | verified: 51, unverified: 9, dropped: 1 | plan.md, ranking.json, ranking.md, recommendation.md, run-summary.md, sources.md |
| 5-deepseek-v4-pro | 5/5 | 15 | verified: 25, unverified: 0, dropped: 3 | plan.md, ranking.json, ranking.md, recommendation.md, run-summary.md, sources.md |
| 6-minimax-m3 | 5/5 | 16 | verified: 51, unverified: 0, dropped: 8 | plan.md, ranking.json, ranking.md, recommendation.md, run-summary.md, sources.md |
| 7-gpt-6-astra | 0/5 | 0 | missing | SKIPPED.md |
| 8-claude-opus | 5/5 | 15 | verified: 78, unverified: 9, dropped: 14 | plan.md, ranking.json, ranking.md, recommendation.md, run-summary.md, sources.md |

## Top 5 by pick_score, per run

### 1-deepseek-v4-flash
Top pick: **One-click 'Copy for coding agent' (prompt + trimmed report) to the clipboard** (P02)

| Rank | Node | pick | pain | Feature idea |
|---|---|---|---|---|
| 1 | Copy-pasting logs and cURL into the agent by hand is slow, lossy and leaks tokens | 35 | 16 | One-click 'Copy for coding agent' (prompt + trimmed report) to the clipboard |
| 2 | An agent cannot watch a screen recording: users need frames and a text timeline | 33 | 16 | Extract N key frames + a timestamped timeline from the recording into report.md |
| 3 | An agent can't reproduce the bug: missing steps, state, auth and data | 31 | 16 | Emit an ordered 'repro steps + required state' block for the agent |
| 4 | Terminal agents still can't take a pasted screenshot: images in issues are unusable | 31 | 16 | Emit an image manifest (paths + captions) so text-only agents can read report screenshots |
| 5 | My agent can't see the browser: it can't read the console, network tab or live DOM | 31 | 16 | Hand the captured console + network to the agent on the clipboard or in the ZIP |

### 2-minimax-m3.1-flash
Top pick: **One click copies an agent-ready bundle (trimmed report.md plus the suggested prompt) to the clipboard, so a recorded browser bug reaches a coding agent without export, unzip and paste.** (P03)

| Rank | Node | pick | pain | Feature idea |
|---|---|---|---|---|
| 1 | People want to hand a bug straight to an agent, and this recorder has no channel to do it | 37 | 18 | One click copies an agent-ready bundle (trimmed report.md plus the suggested prompt) to the clipboard. |
| 2 | A CLI agent has no way to take a screenshot or read an image, so the bug stays a story | 34 | 18 | Write the screenshot files next to report.md with explicit paths the agent can open. |
| 3 | The agent has no console, no network panel and no DOM, so it guesses at frontend bugs | 34 | 16 | Deliver the recorded console/network/DOM evidence to the agent as one copyable bundle (the same delivery as P03). |
| 4 | Nobody can prove the fix worked - the agent asserts it is done without ever looking | 32 | 18 | Put the reporter's annotated evidence into the PR so the fix claim arrives with a picture. |
| 5 | Copy-paste is the hand-off, and the paste arrives mangled or not at all | 32 | 14 | One 'Copy for AI agent' action that puts the clean report on the clipboard instead of relying on a terminal paste. |

### 3-gpt-6-luna
Top pick: **Add a compact, one-click agent handoff that bundles the captured browser state and tells the agent how to use the evidence without claiming live browser access.** (P01)

| Rank | Node | pick | pain | Feature idea |
|---|---|---|---|---|
| 1 | “Claude can’t see the running page I need it to fix” | 34 | 16 | Add a compact, one-click agent handoff that bundles the captured browser state and tells the agent how to use the evidence without claiming live browser access. |
| 2 | “I keep copying browser errors into the agent by hand” | 33 | 14 | Provide a copy-for-agent action that puts a concise evidence summary and prompt on the clipboard alongside the existing ZIP export. |
| 3 | “A code change or passing test doesn’t show me the UI fix worked” | 32 | 16 | Add a report handoff prompt that presents the recorded failure and asks the coding agent to reproduce it and attach post-fix browser evidence. |
| 4 | “The agent invents API behavior because my browser session is elsewhere” | 31 | 14 | Make captured request and response evidence easy to locate and understand in the agent report, without adding new cURL or HAR export behavior. |
| 5 | “A browser crawler can click around but still miss the bug that matters” | 30 | 12 | Put the recorded narration, annotations and expected-versus-observed notes prominently in the agent handoff prompt. |

### 4-claude-sonnet
Top pick: **"Copy for coding agent" action: prompt plus trimmed report.md on the clipboard** (P03)

| Rank | Node | pick | pain | Feature idea |
|---|---|---|---|---|
| 1 | I found the bug, now give my agent the exact context in one step | 32 | 12 | "Copy for coding agent" action: prompt plus trimmed report.md on the clipboard |
| 2 | The agent can't reproduce my bug, so it guesses and fixes the wrong thing | 31 | 16 | Deterministic "Steps to reproduce / Expected vs actual" block at top of report.md |
| 3 | The agent can't see my browser: console, network, DOM, what is on screen | 30 | 18 | Make the recording the agent's browser: one-step hand-off of console, network, screenshots |
| 4 | One oversized or corrupt screenshot breaks the whole agent conversation | 30 | 16 | Agent-safe screenshot export: cap longest side and file size |
| 5 | The agent says it's fixed and the UI is still broken | 29 | 16 | "How to verify the fix" checklist in report.md (steps, expected result, failing request) |

### 5-deepseek-v4-pro
Top pick: **Emit keyframes, a timestamped transcript and click targets from the recorded video into the report.** (P08)

| Rank | Node | pick | pain | Feature idea |
|---|---|---|---|---|
| 1 | Agents can't watch a screen recording; they need keyframes, a timeline and a transcript | 34 | 16 | Emit keyframes, a timestamped transcript and click targets from the recorded video into the report. |
| 2 | Handing browser evidence to an agent is manual copy-paste, and pasted logs get lost | 32 | 14 | One-click 'Copy for coding agent' that puts a trimmed report.md plus the suggested prompt on the clipboard. |
| 3 | The agent can't see the browser (console, network, DOM), so it guesses at frontend bugs | 31 | 18 | Export the recorded session (console, network, clicks, DOM, screenshots) as agent-consumable context. |
| 4 | A screenshot alone is ambiguous — the agent can't tell which element or environment | 30 | 12 | Emit the annotated element's selector and text next to each screenshot in report.md. |
| 5 | Vague bug reports cause reproduction back-and-forth — missing steps and environment | 30 | 14 | Frame the recorded steps and environment as agent-ready reproduction steps in the report. |

### 6-minimax-m3
Top pick: **One 'Copy for agent' action that puts a clean prompt plus the trimmed report on the clipboard.** (P02)

| Rank | Node | pick | pain | Feature idea |
|---|---|---|---|---|
| 1 | I paste console logs into the agent by hand and the paste is mangled | 32 | 16 | One 'Copy for agent' action that puts a clean prompt plus the trimmed report on the clipboard. |
| 2 | My agent can't see the browser - no console, no network, no rendered DOM | 31 | 18 | Ship the captured console/network/DOM snapshot as a first-class agent-readable section of report.md. |
| 3 | The agent can't consume my screenshots: paste fails, images dropped/resized, oversized ones kill the session | 31 | 18 | Tell the agent which screenshot file to open, and deliver the bytes (image paste / attachment path) instead of a dead markdown link. |
| 4 | Agents can't watch a bug video - I have to turn it into frames and text myself | 31 | 16 | A local 'visual brief': narration transcript + click targets + change-detected frames, rendered to text for the agent. |
| 5 | A bug report the agent can't prove - 'I can't tell' beats a wrong yes | 31 | 14 | A deterministic three-valued verdict (pass/fail/unverified) plus a not-a-bug state, computed from the recorded evidence. |

### 7-gpt-6-astra
No usable ranking.json ([Errno 2] No such file or directory: '<mission>/research/runs/7-gpt-6-astra/ranking.json').

### 8-claude-opus
Top pick: **'Copy for coding agent' button: puts a ready prompt plus the trimmed report.md on the clipboard in one click** (P02)

| Rank | Node | pick | pain | Feature idea |
|---|---|---|---|---|
| 1 | I copy and paste console logs into the agent all day | 35 | 16 | 'Copy for coding agent' button: puts a ready prompt plus the trimmed report.md on the clipboard in one click |
| 2 | The agent says 'fixed' without checking, and the bug is still there | 34 | 18 | 'Acceptance check' section in report.md/issue: the exact errors and failing requests that must be gone after the fix |
| 3 | My agent can't watch the bug video, so I screenshot frames by hand | 32 | 14 | Extract key frames from the tab video around clicks, errors and annotations into frames/*.jpg and list them in the report timeline |
| 4 | Vague bug reports make agents ship confident fixes for the wrong problem | 31 | 16 | Fixed-shape 'Agent brief' block in report.md/issue: expected vs actual, failing request, route and click-target cues |
| 5 | My coding agent can't see the running app: no page, console or network | 30 | 18 | Position the report.md hand-off as the 'frozen browser snapshot' for agents with no live browser (docs + report header) |

## Consensus (rough keyword clusters, check by hand)

| Runs agreeing | Mean pick_score | Best rank | Example titles |
|---|---|---|---|
| 7 | 28.0 | 1 | 1: My agent can't see the browser: it can't read the console, n / 2: The agent has no console, no network panel and no DOM, so it / 2: Copy-paste is the hand-off, and the paste arrives mangled or / 2: People want to hand a bug straight to an agent, and this rec |
| 2 | 29.5 | 6 | 1: A claimed fix needs visual proof: agents open PRs from an is / 1: AI PR review has no eyes: a code diff cannot show the UI the / 2: The issue an agent starts from arrives with no visual eviden / 2: An AI reviewer or PR agent cannot see the UI the change prod |
| 2 | 27.6 | 1 | 1: Copy-pasting logs and cURL into the agent by hand is slow, l / 1: People want to hand a captured bug straight to an agent, usu / 1: Fear of leaking secrets: screenshots, network bodies, URLs a / 1: Cost and context: dumping a whole capture into the prompt is |
| 1 | 33.0 | 2 | 1: An agent cannot watch a screen recording: users need frames  |
| 1 | 31.0 | 4 | 1: Terminal agents still can't take a pasted screenshot: images |
| 1 | 31.0 | 3 | 1: An agent can't reproduce the bug: missing steps, state, auth |
| 1 | 28.0 | 9 | 1: Triage and duplicates: reports are either too thin or far to |
| 1 | 23.0 | 13 | 1: Environment and flaky bugs: the agent's environment does not |
