# Ranking — run `6-minimax-m3` (agent `minimaxai/minimax-m3`), 2026-11-17

Scored with the PRD rubric, applied to the 16 nodes in `nodes/`.

- `pain_score` = 2*frequency + 2*severity (max 20) — how much the world hurts.
- `pick_score` = 2*frequency + 2*severity + 2*fit + smallness + novelty (max 40) — how good it is as
  our one clean PR.
- `frequency` 0-5: 0 = one weak mention, 3 = several independent sources, 5 = many sources with high engagement.
- `severity` 0-5: how much time, money or trust the pain costs.
- `fit` 0-5: how directly Session Recorder (a browser bug recorder that writes reports for agents) can address it.
- `smallness` 0-5: 5 = one clean PR of a few hundred lines with tests; 0 = a new product.
- `novelty` 0-5: 5 = nothing in the extension or its open PRs covers it; 0 = already done or an open PR does it.

Both tables and `ranking.json` are now **generated from one script** (`raw/regen_ranking.py`) so the
markdown and the JSON cannot drift.

## Correction made in US-005 — the US-004 `top_pick` was wrong

US-004 recorded P05 as `top_pick` (pick 33) on the claim that "no 2000 px dimension check exists
anywhere" in the extension. **That claim was wrong, and US-005 found it by grepping for the constant
rather than the literal number.**

`lib/capture/screenshots.ts:38` reads:

```ts
const MAX_SHOT_DIM = 1400;
```

and `ScreenshotScheduler.capture()` (lines 160–190) downscales any screenshot whose longest side
exceeds 1400 px through `OffscreenCanvas`, re-encoding it as JPEG
(`canvas.convertToBlob({ type: 'image/jpeg' })`). The debugger capture is `image/jpeg` to begin with,
so the stored asset is always JPEG and always ≤ 1400 px — well under the 2000 px limit that poisons a
Claude Code session ([claude-code #13480](https://github.com/anthropics/claude-code/issues/13480)).

So "make the screenshots safe for agents" is **already shipped**. P05 was re-scored: smallness 4 → 3,
novelty 3 → 2, pick_score 33 → 29. The **open** remainder of P05 is delivery, not sizing: the report
renders a screenshot as `![ctx](screenshots/001-0012.jpg)`
(`lib/export/markdown.ts:368–376`), which is a dead reference once the report is pasted as text into a
chat, and the extension has no path at all for getting image *bytes* to an agent.

The same grep discipline re-confirmed the other US-004 score moves:

- **P17** smallness 3, novelty 1 — `lib/export/tokens.ts` exports `estimateTokens()` and
  `lib/export/bundle.ts:497` already computes `tokens: estimateTokens(report)`.
- **P16** novelty 4 — `grep` finds no `verdict`, `confidence` or not-a-bug concept anywhere in
  `lib/` or `entrypoints/`.
- **P12** novelty 1 — five open PRs already cover redaction (#42, #44, #38, #37, #31).

P15 is a **constraint node**, not a user pain. It is scored for completeness but is deliberately not a
candidate for the final pick; it exists to cap the novelty of P02, P03 and P05.

---

## Table 1 — Ranked by `pain_score` (how much the world hurts)

| Rank | ID | Node title | f | s | fit | sm | nov | **pain_score** | **pick_score** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P01 | My agent can't see the browser — no console, no network, no rendered DOM | 5 | 4 | 4 | 3 | 2 | **18** | 31 |
| 2 | P05 | The agent can't consume my screenshots: paste fails, images dropped/resized, oversized ones kill the session | 5 | 4 | 4 | 3 | 2 | **18** | 31 |
| 3 | P12 | Recording the browser means recording my passwords, tokens and customer data | 4 | 5 | 3 | 4 | 1 | **18** | 29 |
| 4 | P11 | If I can't reproduce it, it doesn't get fixed — and a recording is not a reproduction | 4 | 5 | 3 | 2 | 2 | **18** | 28 |
| 5 | P02 | I paste console logs into the agent by hand and the paste is mangled | 5 | 3 | 5 | 5 | 1 | **16** | 32 |
| 6 | P04 | Agents can't watch a bug video — I have to turn it into frames and text myself | 4 | 4 | 5 | 3 | 2 | **16** | 31 |
| 7 | P03 | I want to hand the bug straight to the agent instead of retyping it | 4 | 4 | 4 | 4 | 2 | **16** | 30 |
| 8 | P17 | Evidence is expensive: screenshots eat the window and each agent run costs money | 4 | 4 | 5 | 3 | 1 | **16** | 30 |
| 9 | P14 | The person reporting the bug doesn't know how to describe it to an agent | 4 | 4 | 4 | 3 | 2 | **16** | 29 |
| 10 | P06 | Nobody can prove the fix worked — agents fabricate screenshots and reviewers accept them | 3 | 5 | 3 | 2 | 3 | **16** | 27 |
| 11 | P16 | A bug report the agent can't prove — "I can't tell" beats a wrong yes | 3 | 4 | 5 | 3 | 4 | **14** | 31 |
| 12 | P08 | The agent can't log in, so it can't reproduce the bug behind the login | 3 | 4 | 4 | 3 | 3 | **14** | 28 |
| 13 | P13 | The agent says the task is done but nothing changed — false completion | 3 | 4 | 3 | 3 | 3 | **14** | 26 |
| 14 | P07 | The PR reviewer cannot see the UI the change produces | 3 | 4 | 3 | 2 | 3 | **14** | 25 |
| 15 | P15 | Copying the report to the agent is already a feature — the category is crowded *(constraint node)* | 5 | 2 | 2 | 1 | 0 | **14** | 19 |
| 16 | P10 | The report is filed but the agent never picks it up — the trigger is missing | 3 | 3 | 4 | 5 | 2 | **12** | 27 |

Ties are broken by `pick_score` (desc), then by node id (asc). The machine-readable order is in
`ranking.json` → `pain_rank` and `pick_rank`.

---

## Table 2 — Ranked by `pick_score` (how good it is as our one clean PR)

| Rank | ID | Node title | f | s | fit | sm | nov | **pick_score** | **pain_score** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P02 | I paste console logs into the agent by hand and the paste is mangled | 5 | 3 | 5 | 5 | 1 | **32** | 16 |
| 2 | P01 | My agent can't see the browser — no console, no network, no rendered DOM | 5 | 4 | 4 | 3 | 2 | **31** | 18 |
| 3 | P05 | The agent can't consume my screenshots: paste fails, images dropped/resized, oversized ones kill the session | 5 | 4 | 4 | 3 | 2 | **31** | 18 |
| 4 | P04 | Agents can't watch a bug video — I have to turn it into frames and text myself | 4 | 4 | 5 | 3 | 2 | **31** | 16 |
| 5 | P16 | A bug report the agent can't prove — "I can't tell" beats a wrong yes | 3 | 4 | 5 | 3 | 4 | **31** | 14 |
| 6 | P03 | I want to hand the bug straight to the agent instead of retyping it | 4 | 4 | 4 | 4 | 2 | **30** | 16 |
| 7 | P17 | Evidence is expensive: screenshots eat the window and each agent run costs money | 4 | 4 | 5 | 3 | 1 | **30** | 16 |
| 8 | P12 | Recording the browser means recording my passwords, tokens and customer data | 4 | 5 | 3 | 4 | 1 | **29** | 18 |
| 9 | P14 | The person reporting the bug doesn't know how to describe it to an agent | 4 | 4 | 4 | 3 | 2 | **29** | 16 |
| 10 | P11 | If I can't reproduce it, it doesn't get fixed — and a recording is not a reproduction | 4 | 5 | 3 | 2 | 2 | **28** | 18 |
| 11 | P08 | The agent can't log in, so it can't reproduce the bug behind the login | 3 | 4 | 4 | 3 | 3 | **28** | 14 |
| 12 | P06 | Nobody can prove the fix worked — agents fabricate screenshots and reviewers accept them | 3 | 5 | 3 | 2 | 3 | **27** | 16 |
| 13 | P10 | The report is filed but the agent never picks it up — the trigger is missing | 3 | 3 | 4 | 5 | 2 | **27** | 12 |
| 14 | P13 | The agent says the task is done but nothing changed — false completion | 3 | 4 | 3 | 3 | 3 | **26** | 14 |
| 15 | P07 | The PR reviewer cannot see the UI the change produces | 3 | 4 | 3 | 2 | 3 | **25** | 14 |
| 16 | P15 | Copying the report to the agent is already a feature — the category is crowded *(constraint node)* | 5 | 2 | 2 | 1 | 0 | **19** | 14 |

### Why the top five are ordered this way

**1. P02 (pick 32) — "copy for agent".** The highest fit and the highest smallness in the set, and the
pain is independently visible in a 304-reaction thread, a Cursor forum topic and two HN threads. The
extension already has every input this needs: `report.md` is rendered by `lib/export/markdown.ts`, the
trimmer already chooses a verbosity level, and `copyIssue()` in
`entrypoints/share/useShareReport.ts:330` already writes to the clipboard. The work is one button plus
a prompt template. It takes first place by score, but its **novelty is only 1** — P15 proved a dozen
competitors already ship "copy for agent" — so it is the right *mechanism* and the wrong
*differentiator*. US-005 builds it as the delivery vehicle for P05 and P16, not as the pitch.

**2. P01 (pick 31) — "the agent cannot see the browser".** The largest pain by raw evidence volume
(claude-code #57034 at 👍 55, #76809 at 👍 21, three Cursor forum topics, and 57.7k stars on
chrome-devtools-mcp as proof of market demand). It ties P05, P04 and P16 on 31 and is placed second
because the *gap* is large: Session Recorder can ship a captured snapshot of the real session, but it
cannot give the agent a live browser — that is chrome-devtools-mcp's job, and re-implementing it would
be a new product, not a PR (hence smallness 3).

**3. P05 (pick 31) — "the agent cannot consume my screenshots".** Frequency 5 (seven independent
sources including a 90-reaction Claude Code thread, a Copilot CLI issue, a Cline issue and two Cursor
forum topics) and severity 4 (an oversized image can poison an entire conversation with no way out but
hand-editing `~/.claude/projects/<cwd>/<sessionId>.jsonl`). It **fell from first place to third** once
US-005 found `MAX_SHOT_DIM = 1400`: the sizing and format half is already shipped, so novelty dropped
to 2. The unclaimed remainder is delivery — the report names the image file but does not hand the
agent a way to open or receive it.

**4. P04 (pick 31) — "the visual brief".** Fit 5 (the extension already records tab video, screenshots
and a narration transcript on one clock — the three exact inputs the users ask for) and it is the
strongest *new* pain found by this run. It ties on 31 but is placed fourth because novelty is only 2:
Clipy's `get_agent_context` and ThinkRun's listing already market a summary + timeline + key-moments +
transcript package, found during the US-003 verification pass, which cut this node's novelty from 4 to
2. The unclaimed remainder — offline, no MCP server, change-detection frame selection — is real but
smaller than the claimed version of the feature.

**5. P16 (pick 31) — "the audit layer: a bug report the agent can't prove".** Ties the three above on
score but is placed fifth on judgment, and it is the highest-*novelty* pain in the whole set
(novelty 4): no open PR adds a verdict, a confidence value or a not-a-bug state, and the closest shipped
precedent — Clipy's three-valued verdict glyphs — is a 5-star project in a different product. Frequency is
only 3 and it rests largely on one high-engagement HN thread, which is why it is not higher. It is the
best *idea* in this ranking and the third best *pick*, and US-005 treats it as the highest-upside option.

**Ties and near-misses.** P12 (severity 5, the highest in the set) lands eighth because **five open PRs
already attack redaction** (#42 secret protection, #44 WebSocket frames, #38 card/IBAN/tax IDs, #37 URL
tokens, #31 URL params), so novelty is 1 and the notes already flag the topic as crowded; only the
credential-*type* sub-idea — the extension knows a password was typed at 0:11 without recording its
value — is unclaimed, and that is a thin slice. P17 lands seventh because `estimateTokens` already
exists. P03's novelty is capped by P15 the same way P02's is, and the MCP-style push that users
actually ask for (S25, S26, S13) is a new product for the extension, not a PR.

---

## Notes and caveats

- **No Reddit evidence.** Reddit's JSON and page endpoints return the bot challenge from this host.
  Reddit was searched via `web_search` with `allowed_domains: ["reddit.com"]` only; no Reddit page could
  be opened, so no Reddit URL is cited as verified anywhere in this run. The PRD's list of subreddits is
  therefore only partly covered — a real limitation of the frequency scores, which are drawn from GitHub,
  Cursor forum, HN, Chrome Web Store reviews and vendor docs.
- **P15 is not a pain.** It is included in both tables because the rubric says score every node, but it
  should not be read as a candidate. Its function is to cap novelty at P02, P03 and P05.
- **Frequency is a proxy.** P05, P01 and P02 are all scored 5 on GitHub reaction counts and comment
  counts. A high-reaction GitHub issue is a proxy for how many developers have felt the pain, not for how
  many have reported it.
- **The vision/video required area was searched** (P04, P05, P06, P07). P04 carries the video-input
  evidence and P07 the visual-regression-in-PR evidence; P05 carries the "agent cannot consume
  screenshots" half. The honest finding is that the *video* gap is real for CLI agents (no mainstream CLI
  agent accepts a video file) but the *brief* that closes it is already shipped by two competitors.
- **Scores are not a forecast.** They rank *this run's* 16 pain nodes for *this extension* under the PRD's
  rubric; a different research run with different sources would score them differently, and the owner should
  compare the four rankings rather than treat any single one as ground truth.
