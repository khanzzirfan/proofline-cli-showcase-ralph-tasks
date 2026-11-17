verified: 51, unverified: 0, dropped: 8

Research run `6-minimax-m3` (agent `minimaxai/minimax-m3`), 2026-11-17.
Every URL below was opened by this run with `web_fetch` or `curl` (re-checked in US-003).
Popularity signals are recorded as they were shown on the page at the time of the check.

## Verification pass (US-003, 2026-11-17)

Every one of the 51 distinct URLs cited in `nodes/` and in the earlier `sources.md` was
re-opened, and two more were added while re-opening the evidence (S50 Clipy, S51 ThinkRun).
Result: **51 verified, 0 unverified, 8 dropped** (dropped = claims removed, not URLs that
failed to load — see "Dropped claims"). Every source row in the table below is `verified`;
there are no `unverified` rows left. Two new sources were added rather than left out, because
both are competitors that change the novelty score of the features this run would otherwise
recommend.

What changed in this pass:

- **S47** (`forum.cursor.com` topic 58803) was carried over from `00-context-notes.md` and
  had not been opened. It is now **verified** via the Discourse JSON API (200, title
  "When I try to copy and paste debug terminal output, the agent can no longer see it",
  2 posts, 752 views, created 2025-03-03). The quote in P02 was a paraphrase; it is now a
  verbatim line from the topic body.
- **S48** (`github.com/orgs/community/discussions/169913`) was also carried over and
  unverified. It is now **verified** via `web_fetch` (title: "How can i ensure that issues
  that copilot is assigned to add screenshots to the PR?", 4 participants, 3 comments,
  opened 2025-08-15). It became the strongest single piece of evidence for P07.
- **Reaction counts corrected.** claude-code #12676 was recorded as 👍 57; the live page
  shows **👍 46, ❤️ 11**. Cursor forum topic 155742 was recorded as 186 views; the API
  returns **187**. HN item 50339913 was recorded as "135 comments"; Algolia returns **44
  top-level comments** (the 135 figure counted nested replies, which are not the same
  signal). vscode-pull-request-github #7770 was recorded as "closed"; it was closed as
  **completed** on 2026-04-08.
- **Dates corrected.** Cursor topic 152452 was recorded as "n/a"; it was created
  **2026-02-20**. Cursor topic 155742 was created 2026-03-24 (recorded correctly).
- **One quote replaced.** P01 quoted the *title* of Cursor topic 152452 as if it were a body
  quote. It is now quoted from the body, which is stronger: the agent's MCP tools returned
  "Unsupported content type 'metadata'".
- **Duplicate merged.** P09 (report too noisy) and P17 (evidence is expensive) shared the
  same lead evidence (#16592's "86 % of context" comment) and the same proposed feature
  (a copy-for-agent action with a user-controlled block). P09 was merged into **P17** and
  the P09 file was deleted. P17 keeps the better framing because it also covers the *money*
  half of the pain, which P09 never did.
- **One unsupported claim dropped.** P02's pain statement claimed pasted output "carries
  tokens, cookies or API keys straight into a third-party model". No source in P02 supports
  that; the secrets pain has its own node (P12) with real evidence. The claim was removed
  from P02 rather than left dangling.
- **No node was dropped.** All 16 remaining nodes keep at least two verified sources.

## Popular places covered (PRD requires >= 8)

| # | Place | How | Covered via |
|---|---|---|---|
| 1 | anthropics/claude-code (issues) | GitHub issue pages + web_fetch | S1, S2, S3, S5, S6, S7 |
| 2 | forum.cursor.com (Discourse JSON + web_fetch) | `t/{id}.json` | S4, S8, S9, S10, S11, S12, S13, S14, S15, S47 |
| 3 | github/copilot-cli (issues) | GitHub issue pages | S16, S17 |
| 4 | openai/codex (issues) | GitHub issue page | S18 |
| 5 | cline/cline (issues) | GitHub issue page | S19 |
| 6 | RooCodeInc/Roo-Code (issues + PRs) | GitHub issue/PR pages | S20, S21 |
| 7 | ChromeDevTools/chrome-devtools-mcp | repo page | S6 |
| 8 | microsoft/playwright-mcp | GitHub issue page | S22 |
| 9 | Hacker News (Algolia + web_fetch) | `hn.algolia.com/api/v1/items/{id}` | S24–S30, S41–S43 |
| 10 | Chrome Web Store (competitor listings + reviews) | curl + text extraction | S37–S40 |
| 11 | Microsoft/vscode-pull-request-github | GitHub issue page | S33 |
| 12 | GitHub community discussions + Agentic Workflows | web_fetch + curl | S35, S36, S48, S49 |
| 13 | GitHub repo discovery (competitors) | `api.github.com/search/repositories` | S44, S45 |
| 14 | GitHub Copilot docs (visual inputs) | vendor-doc | S34 |

**Not covered (declared, not silently dropped):**
- `r/ClaudeAI`, `r/cursor`, `r/ChatGPTCoding`, `r/webdev`, `r/QualityAssurance`,
  `r/ExperiencedDevs`, `r/programming` — **blocked**. Reddit's `.json` endpoints return
  **HTTP 403** from this host with every user agent tried (`pain-research/1.0`, a desktop
  Chrome UA); `old.reddit.com` returns 302 to a consent interstitial; `web_fetch` on a post
  URL returns the "Prove your humanity" bot challenge (HTTP 200 but no content).
  `web_search` with `allowed_domains:["reddit.com"]` returned only two r/webdev posts
  about Jam and Requestly, neither of which adds a new pain. **No Reddit claim in any node
  is sourced from Reddit.**
- `getcursor/cursor`, `sst/opencode`, `All-Hands-AI/OpenHands` GitHub issue searches — the
  API returned `422 Validation Failed` ("The listed users and repositories cannot be
  searched") for these repos in this environment. The Cursor forum (same company) was used
  instead for Cursor. OpenHands and opencode are therefore covered only indirectly, through
  the notes' prior research — a real gap in this run's evidence.
- G2 and Product Hunt — **blocked** (403/504 on both web_fetch and curl). Substitute:
  Chrome Web Store reviews and HN launch threads, which carry the same "launched a
  bug-report-for-agents tool" narrative with points and comment counts.
- Reddit `r/webdev` "Building a bug reporting extension to auto-capture console" — dropped;
  the fetch returned the bot challenge, so the snippet could not be confirmed.

## Source list

| ID | URL | Type | Date | Status | Popularity signal | Used by |
|---|---|---|---|---|---|---|
| S1 | https://github.com/anthropics/claude-code/issues/75632 | github-issue | 2026-07-08 | verified | 👍 8, 21 comments, closed as stale/not planned 2026-09-22 | P01, P06, P07, P10 |
| S2 | https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 | forum | 2026-02-20 | verified | 4 posts, 260 views | P01 |
| S3 | https://forum.cursor.com/t/-web-cursor-agent-browser-tool-not-capturing-rendered-dom-elements-on-my-site/178559 | forum | 2026-11-16 | verified | 2 posts, 26 views | P01 |
| S4 | https://github.com/anthropics/claude-code/issues/57034 | github-issue | 2026-05-07 | verified | 👍 55, ❤️ 21, 24 comments | P01, P06, P07 |
| S5 | https://github.com/anthropics/claude-code/issues/76809 | github-issue | 2026-07-12 | verified | 👍 21, 20 comments | P01 |
| S6 | https://github.com/ChromeDevTools/chrome-devtools-mcp | vendor-doc | n/a | verified | 57.7k stars, 4.9k forks | P01, P06, P07, P08, P12 |
| S7 | https://github.com/anthropics/claude-code/issues/12676 | github-issue | 2025-11-29 | verified | 👍 46, ❤️ 11, 21 comments | P04, P17 |
| S8 | https://forum.cursor.com/t/ctrl-v-image-paste-always-fails-on-macos-execfile-missing-encodingbuffer/176096 | forum | 2026-10-25 | verified | 7 posts, 188 views | P05 |
| S9 | https://forum.cursor.com/t/grok-bot-drops-mcp-typeimage-bytes-from-remote-tool-results-full-res-screenshots-unsavable/177756 | forum | 2026-11-08 | verified | 2 posts, 44 views | P05 |
| S10 | https://forum.cursor.com/t/cursor-does-not-have-access-to-built-in-browser-anymore/164605 | forum | 2026-07-02 | verified | 3 posts, 174 views, 4 likes | P05, P08, P13 |
| S11 | https://forum.cursor.com/t/can-not-login-to-aws-via-cursors-browser/162714 | forum | 2026-06-08 | verified | 3 posts, 106 views | P08 |
| S12 | https://forum.cursor.com/t/misleading-browser-debugging-difficulty-with-complex-backend-tasks-terminal-process-stuck-and-disrupting-previously-corrected-code/145211 | forum | 2025-12-04 | verified | 3 posts, 178 views, 2 likes | P13 |
| S13 | https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630 | forum | 2026-10-13 | verified | 1 post, 36 views | P03, P14 |
| S14 | https://forum.cursor.com/t/agent-browser-as-a-full-window-the-agent-can-still-control/177500 | forum | 2026-11-06 | verified | 2 posts, 33 views | P01 (context only) |
| S15 | https://forum.cursor.com/t/browser-mcp-not-working-browser-icon-missing-and-agent-cannot-control-the-browser/155742 | forum | 2026-03-24 | verified | 7 posts, 187 views | P01 (context only) |
| S16 | https://github.com/github/copilot-cli/issues/2675 | github-issue | 2026-04-13 | verified | 👍 7, 3 comments, open | P05 |
| S17 | https://github.com/github/copilot-cli/issues/1241 | github-issue | 2026-02-01 | verified | 👍 7, closed 2026-04-07 as fixed | P05 |
| S18 | https://github.com/openai/codex/issues/29451 | github-issue | n/a | verified | +1 89, 3 comments, closed | context only (codex image artifacts) |
| S19 | https://github.com/cline/cline/issues/9902 | github-issue | 2026-03-20 | verified | 👍 4, 5 comments, closed as not planned 2026-10-28 | P05 |
| S20 | https://github.com/RooCodeInc/Roo-Code/pull/9963 | github-pr | 2025-12-10 | verified | merged 2025-12-10 | P05 (context: agents want to save screenshots to disk) |
| S21 | https://github.com/RooCodeInc/Roo-Code/issues/2270 | github-issue | n/a | verified | +1 10, 36 comments | context only |
| S22 | https://github.com/microsoft/playwright-mcp/issues/1382 | github-issue | n/a | verified | 5 comments | context only (MCP agent observing a browser session) |
| S23 | https://github.com/anthropics/claude-code/issues/13480 | github-issue | 2025-12-09 | verified | 👍 90, 111 comments | P05 |
| S24 | https://github.com/anthropics/claude-code/issues/18170 | github-issue | 2026-01 | verified | 👍 304, 140 comments | P02 |
| S25 | https://news.ycombinator.com/item?id=48795580 | hn | n/a | verified | 6 points, 2 comments | P02, P03 |
| S26 | https://news.ycombinator.com/item?id=46047931 | hn | n/a | verified | 5 points, 1 comment | P03, P14 |
| S27 | https://news.ycombinator.com/item?id=45909113 | hn | n/a | verified | 5 points, 0 comments | P03 |
| S28 | https://news.ycombinator.com/item?id=42647248 | hn | n/a | verified | 2 points, 2 comments | P11 |
| S29 | https://news.ycombinator.com/item?id=50339913 | hn | n/a | verified | 168 points, 44 top-level comments | P11, P16, P17 |
| S30 | https://news.ycombinator.com/item?id=49466704 | hn | n/a | verified | 40 points, 11 comments | P06, P12, P13 |
| S31 | https://github.com/anthropics/claude-code/issues/16592 | github-issue | 2026-01-07 | verified | 👍 14, 8 comments | P05, P17 |
| S32 | https://github.com/anthropics/claude-code/issues/82668 | github-issue | 2026 | verified | 7 comments, closed as not planned 2026-09-07 | P08, P12 |
| S33 | https://github.com/Microsoft/vscode-pull-request-github/issues/7770 | github-issue | 2025-09-07 | verified | 👍 1, 9 comments, closed as completed 2026-04-08 | P06, P13 |
| S34 | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs | vendor-doc | n/a | verified | n/a | P07 |
| S35 | https://github.com/microsoft/hve-core/blob/main/.github/agents/issue-triage.agent.md | github-repo | n/a | verified | n/a | P10 |
| S36 | https://github.github.com/gh-aw/gallery/ai-issue-triage/ | github-repo | n/a | verified | n/a | P10 |
| S37 | https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj | listing | updated 2026-11-10 | verified | 6 users, 0 ratings; names 15 competitors | P12, P14, P15 |
| S38 | https://chromewebstore.google.com/detail/vibe-annotations-visual-f/gkofobaeeepjopdpahbicefmljcmpeof/reviews | review | 2026-05-14, 2025-08-07 | verified | 5.0 / 11 ratings, 2,000 users; 1 helpful | P17, P12, P14, P15 |
| S39 | https://chromewebstore.google.com/detail/handoff-%E2%80%94-visual-feedback/kdojobaddodgeecdboledochcdndkehf/reviews | review | 2026-08-26, 2026-09-02 | verified | 5.0 / 2 ratings, 17 users | P14, P15 |
| S40 | https://chromewebstore.google.com/detail/vox-issue/dcgfoocpjkneaeigobkojjbljbhbofea/reviews | review | n/a | verified (listing renders, **no reviews exist**) | 0 ratings, no reviews | P15 |
| S41 | https://news.ycombinator.com/item?id=49644238 | hn | n/a | verified | 3 points, 1 comment | P11 |
| S42 | https://news.ycombinator.com/item?id=47075182 | hn | n/a | verified | 5 points, 0 comments | P11 |
| S43 | https://news.ycombinator.com/item?id=45762012 | hn | n/a | verified | 116 points, 16 top-level comments | P11 (context) |
| S44 | https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc&per_page=20 | github-api | 2026-11-17 | verified | 54 results; BugTraceAI-CLI 183★, vynix-mcp 10★, hearback 9★, argus 7★, Webvizio/mcp 6★ | P03, P15 |
| S45 | https://api.github.com/search/repositories?q=visual+feedback+AI+coding+agent+chrome+extension&sort=stars | github-api | 2026-11-17 | verified | 6 results; fixative-ai 1★, almost-video-feedback 1★, Elemnt 1★, agent-inspect-extension 0★, agentation-browser-extension 0★, agenteye 0★ | P15 (context) |
| S46 | https://github.com/UseVynix/vynix-mcp | github-repo | n/a | verified | 10 stars | P03, P12 |
| S47 | https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 | forum | 2025-03-03 | **verified (was unverified)** | 2 posts, 752 views; auto-closed 2025-04-03 | P02 |
| S48 | https://github.com/orgs/community/discussions/169913 | github-discussion | 2025-08-15 | **verified (was unverified)** | 3 comments, 4 participants, unanswered | P07, P10 |
| S49 | https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows/ | github-blog | 2026-01-13 | verified | n/a | P10 |
| S50 | https://github.com/clipy-recorder/clipy-mcp | github-repo | n/a | verified | 5 stars, 2 forks; ships `get_agent_context`, `get_key_moments`, `read_context_document`, three-valued verdict glyphs | P04, P16 |
| S51 | https://chromewebstore.google.com/detail/thinkrun-screen-recorder-for/affbcanbhbnolapiokgjnkfjccdmefmd | listing | updated 2026-08-19 | verified | 23 users, 0 ratings, v0.2.12 | P04, P15 |

The Clipy repo (S50) was **added during the US-003 verification pass**. It was named inside the
claude-code #12676 thread as a workaround, and opening it directly showed that a competitor
already ships the "visual brief for the agent" shape — `get_agent_context` returns
"summary + interaction timeline + key moments + transcript + available browser diagnostics) as
markdown". That materially lowered P04's novelty score and added a concrete competing
implementation to P16's auditability section.

The ThinkRun listing (S51) was **added during the US-003 verification pass** after a web
search for "Clipy Chrome extension" surfaced it in the Chrome Web Store. Its own description
makes it the closest competitor to Session Recorder found in this run: "clicks, console logs,
network requests, and screenshots, all timestamped", "AI-ready bug reports", "LLM-ready
Markdown or JSON", and "Real browser control: let Claude Code, Cursor, or any MCP client
drive the Chrome you already use — your tabs, your cookies, your logged-in sessions". It also
claims the local-first privacy angle ("Local mode keeps page content on your machine") and
ships its own MCP server (`npx @thinkrun/mcp`). It has only 23 users and 0 ratings, so it is
not yet proven in the market, but it removes most of the novelty of the obvious features.

## Dropped claims

| Claim | Why dropped |
|---|---|
| Reddit r/webdev "Building a bug reporting extension to auto-capture console/network" (2023) | fetch returned the bot challenge; snippet could not be confirmed |
| Reddit r/ChatGPTCoding "pasting screenshots to ChatGPT for errors" | fetch returned the bot challenge; also about ChatGPT chat, not a coding agent |
| Reddit r/ChatGPT "Issue Cut and Paste into ChatGPT — pasting as image" | about ChatGPT chat UI, not a coding agent; bot challenge |
| "Claude Code #52907 console capture and DOM inspection" | not re-opened in this run and not needed; the same pain is covered by S1, S2, S4, S5 |
| Cursor topic 145855 "Browser screenshot tool now missing" (from the US-001 plan) | topic body not opened in this run; the same pain is covered by S4, S5 and S8 which were opened |
| "Claude can't view images unless manually uploaded?" (Cursor 71905, from the US-001 plan) | topic body not opened in this run; covered instead by S16, S17, S23 |
| P09 as a separate node (context noise) | **merged into P17** — same lead evidence (#16592), same proposed fix (a user-controlled copy block). P09's file was deleted; its surviving evidence is carried in P17. |
| P02's "pasted output carries tokens, cookies or API keys into a third-party model" | no source in P02 supported it. The secrets pain is covered properly by P12 (S30, S6, S32). Removed from P02's pain statement rather than left without evidence. |

## Raw JSON kept under `raw/`

`A1…A15` GitHub issue searches (claude-code, codex, copilot-cli, chrome-devtools-mcp,
playwright-mcp, opencode, Roo-Code, cline, org:github), `B1`/`B2` GitHub repo discovery,
`C1`/`C_q_*`/`C_topic_*` Cursor forum search and topic bodies, `E1`–`E6` and `HN_*` Hacker News,
`S1`–`S2`, `V1`–`V5`, `X1`–`X4`, `Y1`–`Y5` further GitHub searches, `CC_*` Claude Code issue bodies.
US-003 added the re-fetched verification payloads: `cf_*.json` (Cursor forum topic bodies),
`hn_*.json` (HN Algolia items), `v_*.json` / `v_*.html` (the two previously unverified sources
and the gh-aw pages), and `gh_cc_*.html` / `gh_*.html` (GitHub issue pages).
