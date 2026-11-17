# US-001: Search plan — pain research run `6-minimax-m3`

Agent: `minimaxai/minimax-m3`. Output dir: `<mission>/research/runs/6-minimax-m3`.
Date: 2026-11-17.

## 0. What we already know (from `00-context-notes.md`)

Five pains are already logged in section 5 of the notes. They are **hypotheses to re-test with independent evidence**, not
gifts to restate:

1. The agent cannot see the browser (console, network, DOM).
2. Copy-paste friction when handing context to an agent (logs leak secrets; pasted logs sometimes never arrive).
3. People want to hand bugs straight to an agent, often through MCP.
4. Cloud agents start from GitHub issues; users want proof that a fix works.
5. Redaction and safety (tokens, cards) is wanted but imperfect.

The notes also list the **open PRs in the extension that must not be duplicated** (#49, #48, #47, #46, #45, #44, #43, #42, #41,
#40, #39, #38, #37, #33, #32, #31, #30, #29, #25, #24, #23, #21, and #22 closed by its author).

The notes' **current leaning** is feature A ("Copy for coding agent: prompt + trimmed report on the clipboard") plus the shared
instructions block from B. A key risk is that the owner is already leaning A, so this run must look **harder** for pains A does
not solve, and must be honest about the competitive landscape.

### Facts I verified in the extension source (2026-11-17)

- The "Suggested prompt" for agents exists **only in `docs/report-format.md`**, not in code. `grep` for `prompt` in `entrypoints/`
  and `lib/` returns no agent-handoff prompt constant.
- The only clipboard write is `copyIssue()` in `entrypoints/share/useShareReport.ts:330` — it copies the **GitHub issue body
  markdown**, not `report.md` plus a prompt.
- `lib/export/trimmer.ts:519-528` keeps `video-segment` events at every verbosity level but **clears the file reference at L2+**,
  so at Compact and Minimal the agent sees the clip's time span but no video asset. `lib/export/bundle.ts:448-451` notes the
  same for L2. Video files exist at L0/L1 only (`bundle.video.test.ts`).
- Screenshots are written as `screenshots/NNN-mmss.jpg` and referenced from `report.md`; the report is prose-first and the
  screenshots are pointers, not inlined.

### Competitive landscape I found (critical for the `novelty` score)

Fetching the Chrome Web Store listing for Darnly surfaced a **"Related extensions" carousel** naming ~12 direct competitors,
several explicitly aimed at AI agents: **Handoff — Visual Feedback for AI Agents**, **Vox Issue**, **POKEIT — Visual QA
Inspector**, **Vibe Annotations**, **ElementAgent**, **Yocoolab**, **Pluck**, **Staktab**, **Contexify**, **Setu**, **AIScan**,
plus **Darnly**, **Jam**, **Marker.io**, **FlowLens**, **Faylee**. Most ship a "Copy for agent" button. So a naive
"copy the report to the clipboard" feature is **not novel** — the novelty must come from something these competitors and
the extension's open PRs do not do. I must search each competitor's reviews for the gap they leave.

One review already hints at a real gap (Alexandre Bourget, Vibe Annotations, 2026-05-14): he wants to **alter the baseline
context that is copied** — the copied block talks about Tailwind and other noise he does not want. Copy verbosity control and
copied-content control is a pain the competitors have too.

---

## 1. Source-type map and what each tool can actually do (probed, not assumed)

I probed every endpoint before writing this plan, because two of the PRD's suggested tools do not work from this machine.

| # | Source type | Tool | Status | Notes |
|---|---|---|---|---|
| S1 | GitHub issues (reactions) | `curl` → `api.github.com/search/issues?sort=reactions` | **works** | Returns `reactions.total_count`, `reactions["+1"]`, `comments`, `state`, `html_url`. 10 req/min. |
| S2 | GitHub issues (comments) | same, `sort=comments` | **works** | Sometimes surfaces different issues than `sort=reactions`; run both. |
| S3 | GitHub repo discovery | `curl` → `api.github.com/search/repositories?sort=stars` | **works** | Good for finding the newest competing tools. |
| S4 | GitHub issue body/comments | `curl` → `api.github.com/repos/{o}/{r}/issues/{n}` | **works** | Needed for verbatim quotes. |
| S5 | Cursor forum (Discourse JSON) | `curl` → `forum.cursor.com/search.json?q=…` and `forum.cursor.com/t/{id}.json` | **works, best forum tool** | Returns topic id, `posts_count`, `reply_count`, `like_count`, dates, and full post text. Far better than web fetch, which renders almost nothing. |
| S6 | Reddit (top posts) | `curl` → `reddit.com/r/<sub>/search.json?sort=top` | **BLOCKED (HTTP 403)** | Reddit's `.json` and `.rss` endpoints 403 from this host, with any UA tried; `old.reddit.com` serves an interstitial. `web_fetch` on the same URL 504s. |
| S7 | Reddit (via web search) | `web_search` with `allowed_domains:["reddit.com"]` | **works** | Use `site:reddit.com`-style queries with `allowed_domains`. Snippets give quotes; the post URL can then be opened with `web_fetch` (tested: works on normal post pages). |
| S8 | Hacker News (points) | `curl` → `hn.algolia.com/api/v1/search?tags=story` | **works** | `points` + `num_comments` present. **Caution:** `tags=comment` hits have **no** `points` field — the popularity of a comment lives on its parent story, so always run the `tags=story` query and join by `story_id`. |
| S9 | Chrome Web Store listing + reviews | `web_fetch` on the listing and on `…/reviews` | **works** | Reviews render in full, including the "Lowest to highest rating" filter. The listing's "Related extensions" carousel is a competitor index. |
| S10 | Vendor docs / changelogs | `web_fetch` | **works** | Copilot visual-input docs, chrome-devtools-mcp README, Playwright MCP, OpenHands, Devin, pr-agent. |
| S11 | G2 reviews | `web_fetch` and `curl` | **BLOCKED (403 / 504)** | Both paths fail. Substitute: Chrome Web Store reviews (S9) and Product Hunt-style launch posts. |
| S12 | Product Hunt | `web_fetch` and `curl` | **BLOCKED (403 / 504)** | Substitute: Show HN posts (S8) carry the same "launched a bug-report-for-agents tool" narrative with points. |

**Reddit and G2/Product Hunt are blocked.** Per the PRD I will note this in `run-summary.md` and use web search
(`site:reddit.com` via `allowed_domains`) as the Reddit path, and Chrome Web Store reviews plus Show HN as the G2/PH
substitute. I will **not** invent Reddit engagement numbers I cannot see.

---

## 2. Search queries (28 concrete queries across 8 source types)

All `curl` calls use `-A "pain-research/1.0"`, sleep ~2 s between calls to the same host, and save the raw JSON under `raw/`.

### A. GitHub issues — most-reacted first (S1/S2/S4)

```
A1  api.github.com/search/issues?q=repo:anthropics/claude-code+browser+console&sort=reactions&order=desc&per_page=20
A2  api.github.com/search/issues?q=repo:anthropics/claude-code+screenshot+vision&sort=reactions&order=desc&per_page=20
A3  api.github.com/search/issues?q=repo:anthropics/claude-code+copy+paste+terminal&sort=reactions&order=desc&per_page=20
A4  api.github.com/search/issues?q=repo:getcursor/cursor+browser+console+network&sort=reactions&order=desc&per_page=20
A5  api.github.com/search/issues?q=repo:openai/codex+screenshot+image+attach&sort=reactions&order=desc&per_page=20
A6  api.github.com/search/issues?q=repo:github/copilot-cli+screenshot+visual&sort=reactions&order=desc&per_page=20
A7  api.github.com/search/issues?q=repo:All-Hands-AI/OpenHands+browser+screenshot&sort=reactions&order=desc&per_page=20
A8  api.github.com/search/issues?q=repo:RooCodeInc/Roo-Code+screenshot+visual+regression&sort=reactions&order=desc&per_page=20
A9  api.github.com/search/issues?q=repo:sst/opencode+screenshot+image&sort=reactions&order=desc&per_page=20
A10 api.github.com/search/issues?q=repo:cline/cline+browser+screenshot&sort=reactions&order=desc&per_page=20
A11 api.github.com/search/issues?q=repo:ChromeDevTools/chrome-devtools-mcp+screenshot+vision&sort=reactions&order=desc&per_page=20
A12 api.github.com/search/issues?q=repo:microsoft/playwright-mcp+screenshot+video&sort=reactions&order=desc&per_page=20
A13 api.github.com/search/issues?q=org:github+discussion+coding+agent+screenshot+visual+input&sort=comments&order=desc&per_page=20
A14 api.github.com/search/issues?q=repo:anthropics/claude-code+reproduce+bug+test+flaky&sort=comments&order=desc&per_page=20
A15 api.github.com/search/issues?q=repo:anthropics/claude-code+image+token+context+window&sort=reactions&order=desc&per_page=20
```

`A15` matters for the vision hypothesis: an issue titled *"Oversized image breaks conversation permanently"* (claude-code
#13480, +1: 90, 111 comments) already surfaced in the probe, and *"Copy/paste from terminal includes unwanted indentation"*
(#18170, +1: 304, 140 comments) is direct evidence for the copy-paste hypothesis.

### B. GitHub repo discovery (S3)

```
B1  api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc&per_page=20
B2  api.github.com/search/repositories?q=visual+feedback+AI+coding+agent+chrome+extension&sort=stars&order=desc&per_page=20
B3  api.github.com/search/repositories?q=playwright+reproduction+from+video+browser&sort=stars&order=desc&per_page=20
```

`B1` already surfaced **BugTraceAI-CLI (183★)**, **vynix-mcp**, **hearback** ("Every player who reports a bug hears back.
Agent-native, human..."), **argus** ("MCP tools that help coding agents test web apps systematically").

### C. Cursor forum — Discourse JSON (S5)

```
C1  forum.cursor.com/search.json?q=browser+console+screenshot+agent
C2  forum.cursor.com/search.json?q=bug+report+evidence+coding+agent
C3  forum.cursor.com/search.json?q=copy+paste+context+agent
C4  forum.cursor.com/search.json?q=visual+regression+PR+review+screenshot
C5  forum.cursor.com/search.json?q=reproduce+bug+flaky+fix+verification
C6  forum.cursor.com/t/{id}.json   # for each promising topic id, to get full post bodies + like_count
```

`C1` already proved out: topic **152452** (the notes' browser-console pain, 4 posts, 260 views) plus fresh topics I had not
seen: **178559** ("@Web / Cursor Agent browser tool not capturing rendered DOM elements"), **145855** ("Browser screenshot tool
now missing" — the agent says *"I don't see a visual screenshot capability - I only have browser_snapshot"*), **71905**
("Claude can't view images unless manually uploaded?"), **145211** ("Misleading Confirmation of Completion" — the agent
*claims* a task is complete), **174630** (AnnotateFix founder: *"the report doesn't tell you what they clicked, what the
browser logged, or which request failed"*).

### D. Reddit — via web search, since the JSON API is blocked (S7)

```
D1  web_search "site:reddit.com Claude Code agent browser console network debug" (allowed_domains: reddit.com)
D2  web_search "site:reddit.com r/cursor agent cannot see console network tab" (allowed_domains: reddit.com)
D3  web_search "site:reddit.com r/ChatGPTCoding coding agent screenshot image not working" (allowed_domains: reddit.com)
D4  web_search "site:reddit.com r/webdev bug report AI agent handoff context" (allowed_domains: reddit.com)
D5  web_search "site:reddit.com r/QualityAssurance AI agent bug report screenshot video" (allowed_domains: reddit.com)
D6  web_search "site:reddit.com r/ExperiencedDevs AI agent broken fix verification" (allowed_domains: reddit.com)
D7  web_search "site:reddit.com r/programming paste console logs to agent token leak" (allowed_domains: reddit.com)
```

### E. Hacker News — points (S8)

```
E1  hn.algolia.com/api/v1/search?query=browser+bug+coding+agent&tags=story&hitsPerPage=25
E2  hn.algolia.com/api/v1/search?query=visual+feedback+AI+agent+extension&tags=story&hitsPerPage=25
E3  hn.algolia.com/api/v1/search?query=screenshot+regression+AI+review&tags=story&hitsPerPage=25
E4  hn.algolia.com/api/v1/search?query=video+bug+report+agent&tags=story&hitsPerPage=25
E5  hn.algolia.com/api/v1/search?query=Claude+Code+copy+paste+context&tags=story&hitsPerPage=25
```

`E1` already surfaced **Show HN: Heckle – Send a bug's full browser context to your coding agent (6 pts)**,
**Show HN: Crit – Visual QA for iOS apps and AI coding agents (5 pts)**, **Show HN: MaruCheck – Independent QA for
AI-generated code (3 pts)**, and **Launch HN: Momentic – Agents that catch bugs by using your app (168 pts, 135 comments)**.
These are launch posts for *competitors*, so they are evidence that the category is crowded and that specific design choices
are contested.

### F. Chrome Web Store reviews — low-star reviews (S9)

```
F1  web_fetch chromewebstore …/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj
F2  web_fetch …/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj/reviews
F3  web_fetch …/detail/vibe-annotations-visual-f/gkofobaeeepjopdpahbicefmljcmpeof/reviews
F4  web_fetch …/detail/handoff-—-visual-feedback/kdojobaddodgeecdboledochcdndkehf/reviews
F5  web_fetch …/detail/pokeit-—-visual-qa-inspec/dbjfemfcgaebmpnkppokcokefnihealm/reviews
F6  web_fetch …/detail/vox-issue/dcgfoocpjkneaeigobkojjbljbhbofea/reviews
F7  web_fetch …/detail/elementagent/dniglbeepgcjlhfjbhmdbjaclijjjobo/reviews
F8  web_fetch …/detail/yocoolab-visual-feedback/kidpbehkjihfegmjeneacdicganoogle/reviews
F9  web_fetch …/detail/pluck-—-copy-any-element/emnpkpfjggnlpoliadgjbpicpajngffh/reviews
F10 web_fetch chromewebstore …/detail/session-recorder/dboiheheijgmfpfhbmjggiijpgondghh/reviews
F11 web_fetch chromewebstore listing for Jam, Marker.io, FlowLens, Faylee, BetterBugs
```

### G. Vendor docs and changelogs (S10)

```
G1  web_fetch docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs
G2  web_fetch github.com/ChromeDevTools/chrome-devtools-mcp  (README, tool-reference, CHANGELOG)
G3  web_fetch github.com/microsoft/playwright-mcp (README)
G4  web_fetch docs.openhands.dev/openhands/usage/run-openhands/github-action
G5  web_fetch docs.devin.ai/work-with-devin/devin-review
G6  web_fetch docs.cline.bot / Roo Code docs / opencode.ai/docs/mcp-servers
G7  web_fetch jam.dev/docs (MCP + AI features) and marker.io/docs
G8  web_fetch docs.codium-ai/pr-agent (PR review capabilities)
```

### H. Web search — broad discovery (S7/S10), each with `allowed_domains` for one host

```
H1  web_search "coding agent cannot see browser console network reproduce bug" (allowed_domains: ["github.com"])
H2  web_search "AI coding agent bug report handoff visual evidence" (allowed_domains: ["news.ycombinator.com"])
H3  web_search "visual regression screenshot diff AI code review agent" (allowed_domains: ["github.com"])
H4  web_search "PR agent screenshot before after visual check" (allowed_domains: ["github.com"])
H5  web_search "bug report extension AI agent" (allowed_domains: ["chromewebstore.google.com"])
H6  web_search "Claude Code paste image screenshot issue" (allowed_domains: ["reddit.com"])
```

---

## 3. Hypotheses to test (9)

Each states the claim, the evidence that would confirm it, the evidence that would kill it, and where I look.

**H1 — "The agent cannot see the browser."** (notes pain 1)
*Confirm:* more than one independent source where an agent says it cannot read console/network/DOM, and users asking for capture.
*Kill:* most complaints are actually about the agent's own browser tooling being broken (a Cursor-MCP configuration problem),
not about missing evidence.
*Look:* A1, A4, C1, C2, D1, D2, G2, G3.
*Already seen:* cursor 152452, 151228, 147882, 149307; Cursor staff say the browser tab has no "run JavaScript" tool (151984).

**H2 — "Copy-paste friction, and pasted context can be lossy or leak."** (notes pain 2)
*Confirm:* users describe losing context between clipboard and agent, or pasting noisy/secret-bearing output.
*Kill:* the real complaint is only about verbosity, not about losing or leaking.
*Look:* A3, A14, A15, C3, D7, E5, F3 (Bourget's "baseline context too noisy" review).
*Already seen:* claude-code #18170 (+1: 304) "Copy/paste from terminal includes unwanted indentation and tabs".

**H3 — "Handing a bug straight to an agent (usually via MCP) is what people want."** (notes pain 3)
*Confirm:* users name a desired destination and a trigger (a slash command, a label, a comment).
*Kill:* the desire is real but the *mechanism* people want is a GitHub issue body, not an MCP server.
*Look:* B1, C2, D4, E1, G4, G5, G7, F1.
*Already seen:* Cursor topic 174630 (AnnotateFix) and 152452 users naming MCP explicitly.

**H4 — "Users want proof that a fix worked; today they don't get it."** (notes pain 4)
*Confirm:* people ask for screenshot/video evidence attached to the PR or the issue, and distrust "done" claims.
*Kill:* the ask is rare or mostly satisfied by the agent's own browser automation.
*Look:* C5, D6, E3, A14, G1, G5, H3, H4.
*Already seen:* Cursor 145211 "Misleading Confirmation of Completion"; the notes' "screenshots in the PR not reliable today".

**H5 — "Redaction and secrets are a first-class worry."** (notes pain 5)
*Confirm:* users describe pasting tokens/keys by accident, or asking for masking.
*Kill:* redaction is already solved well enough by competitors and the extension's own PRs (#31, #37, #38, #42, #44).
*Look:* D7, C3, G2, F1 (Darnly's redaction claims), plus the extension's open PR list.

**H6 — REPRODUCTION is the pain, not capture.** The extension records everything but cannot prove a *sequence* leads to a
failure, because it has no replay, no deterministic step list an agent can re-run, and no way to distinguish "the bug" from
"the noise before the bug".
*Confirm:* users say the agent needs the exact steps, or that a recording cannot be re-run.
*Kill:* agents are happy with a prose timeline; Playwright/MCP already covers re-running.
*Look:* C2, D4, E1, G3, H1.
*This is a candidate pain the notes' section 5 does not list.*

**H7 — AGENT-SIDE TRIAGE AND DUPLICATES.** Filling a GitHub issue is cheap but triage is not: the same visual bug gets filed
many times, and agents re-fix the same thing.
*Confirm:* people complain about duplicate issues, spam, or agents landing on an already-fixed bug.
*Kill:* no source mentions it.
*Look:* C5, D6, A14, G4, G5, and GitHub issue searches for `duplicate bug report agent`.
*Another candidate pain the notes' section 5 does not list.*

**H8 — VISUAL AND VIDEO EVIDENCE (required area).** Two sub-parts, and they may have different answers:
  (a) *PR review and visual checks* — AI reviewers and PR agents cannot see the UI a change produces; visual regression and
      before/after screenshot diffs are not understood by the reviewing agent.
  (b) *Agents that cannot consume images or video* — CLI agents without image paste; agents that cannot watch a screen
      recording, so a bug video must become key frames, a timeline, or text.
*Confirm for (a): an issue or discussion where a reviewer or PR agent says it cannot verify a UI change, or where
before/after screenshots in a PR are ignored or unreadable.
*Confirm for (b): an issue where an agent refuses or fails to read a screenshot or video, or a tool that exists purely to
turn video into agent-readable frames.
*Kill:* the gap is already closed by chrome-devtools-mcp's `take_screenshot` and Playwright's video, or by the extension
already recording video, screenshots and annotations.
*Look:* A2, A11, A12, A13, A15, C4, D3, D5, E2, E3, E4, G1, G2, G3, H3, H4.
*Known data points:* chrome-devtools-mcp has `take_screenshot` and a `video` command (57.7k★ repo, verified 2026-11-17);
Cursor topic 145855 reports the agent saying it has only `browser_snapshot`, no visual screenshot capability; Cursor 71905
"Claude can't view images unless manually uploaded?"; the notes' Copilot visual-input docs page.
*Sub-question I must answer:* Session Recorder already records tab video, screenshots and annotations — **what can an agent
actually consume from them today?** From the source: at L0/L1 the video files ship in the ZIP (`video/NNN-mmss.webm`), but at
L2/L3 the video file is dropped and only the time span survives; screenshots are always separate `.jpg` files that only a
file-reading agent can open. **No agent-readable text rendering of the visual/video evidence exists.** That is a candidate gap —
but I must prove agents want it, not just that we could build it.*

**H9 — Pains the notes missed entirely.** I keep the node list open and will add any pain that appears in two or more
independent sources and is not one of the five above or H6/H7. The competitor-extension review pages (F1-F11) are the most
likely place to find these, because low-star reviews name exactly what is missing from a tool that otherwise works.

---

## 4. Node targets (aim 15-20 nodes, minimum 12)

| Provisional | Pain | Primary sources | Notes-list overlap |
|---|---|---|---|
| P01 | Agent cannot see the browser (console/network/DOM) | A1, A4, C1, D1 | notes 1 |
| P02 | Copy-paste friction; pasted context noisy or lost | A3, A15, C3, D7, F3 | notes 2 |
| P03 | Want to hand a bug straight to an agent | B1, C2, D4, E1, G7 | notes 3 |
| P04 | No proof the fix worked | C5, D6, G1, G5 | notes 4 |
| P05 | Secrets and redaction worry | D7, C3, G2 | notes 5 |
| P06 | Reproduction: steps are not re-runnable | C2, D4, G3 | **new** (H6) |
| P07 | Duplicate issues / re-fixing the same bug | C5, D6, A14 | **new** (H7) |
| P08 | PR review cannot see the UI a change produces | A2, C4, E3, H3, H4 | **new** (H8a) |
| P09 | Agents cannot read images; screenshots unused | A15, D3, C1, G1 | **new** (H8b) |
| P10 | Agents cannot watch video; need frames/timeline/text | A12, E4, G2, C4 | **new** (H8b) |
| P11 | Verbosity/context budget: too much noise per bug | F3, A15, E5 | **new** |
| P12 | Login/auth/CAPTCHA walls block agent reproduction | C1, D1, G2 | possibly new |
| P13 | Environment mismatch (wrong browser/build/localhost/auth) | C1, C2, D4 | possibly new |
| P14 | Flaky fixes; the agent "fixed" a non-bug | A14, C5, D6 | possibly new |
| P15 | Cost/latency of agent runs and of evidence | A15, D6, E1 | possibly new |
| P16 | Report goes to the wrong place / triage routing | C5, G4, G5 | possibly new |
| P17 | Existing competitors already do "copy for agent" | F1-F11, B2, E2 | **new** (competitive constraint) |

**At least three nodes must not be in the notes' section 5.** P06, P07, P08/P09/P10, P11 and P17 are candidates; I will keep
whichever survive verification. If P17 turns out to be the real story (the category is saturated and the differentiator must
be something else), I will say so plainly rather than force a feature.

---

## 5. Method rules I will follow

- **Every claim cites a URL I actually opened.** Verbatim quotes only, **at most 30 words**, cut with an ellipsis if needed.
- **Popularity signal recorded per source**: `reactions["+1"]`/`total_count`/`comments` for GitHub, `score`/`num_comments`
  for Reddit (only when the page shows them), `points`/`num_comments` for HN, `like_count`/`posts_count`/`reply_count` for the
  Cursor forum, star count and rating count for Chrome Web Store.
- **No invented engagement numbers.** If a signal is not visible, I write `signal not visible`.
- **Vendor marketing is weak evidence** and will be labelled as such (Jam, Marker.io, Darnly, FlowLens, Faylee marketing).
- **Blocked sources are declared**, not silently dropped: Reddit JSON (403), G2 (403/504), Product Hunt (403/504).
- **Reddit substitute**: `web_search` with `allowed_domains: ["reddit.com"]`, then `web_fetch` the individual post URL to
  open it and confirm the text before quoting.
- **Raw JSON kept** in `raw/` (small files only) so the owner can re-check every number.
- **Node status discipline**: `verified` only if the main claim rests on a source I opened; `partly-verified` if some sources
  are blocked or thin; `unverified` only for a claim I saw only in a search snippet.
- **No duplicate of the extension's open PRs.** Every node's "Session Recorder angle" names the overlapping PR numbers
  (#49, #48, #47, #46, #45, #44, #43, #42, #41, #40, #39, #38, #37, #33, #32, #31, #30, #29, #25, #24, #23, #21, #22) or
  says "none".
- **Novelty is scored against competitors too**, not only against our own repo — several rivals already ship a copy-to-clipboard
  button.
- **Dates as `YYYY-MM-DD`.** No emails, no tokens, generic UA only, no git write commands, no sign-ins, no PRs/issues opened.

## 6. Risks in this plan

1. **Reddit is blocked.** Reddit's share of the evidence will be thin. If `web_search` snippets do not yield openable post
   pages, Reddit claims will be marked `unverified` rather than guessed.
2. **G2 and Product Hunt are blocked.** Review mining leans entirely on Chrome Web Store, which is acceptable — that is where
   the direct competitors' users actually complain.
3. **The owner may be anchored on feature A.** I will score `pick_score` honestly even if the winner is not A, and I will
   penalise any candidate that a competitor already ships.
4. **Popular GitHub issues are noisy.** `sort=reactions` in a big repo returns account-management and quota issues with
   thousands of reactions. I will filter by title keywords before writing a node, not by reaction count alone.
5. **GitHub rate limit is 10 req/min unauthenticated.** I will pace calls and cache raw responses under `raw/`.

---

## 7. Reconciliation with the final node set (added in US-003)

The table in section 4 was a *provisional* map. The IDs in `nodes/` are the final ones, and they
diverged from the plan because the evidence went where the evidence was. Final set (16 nodes,
one merged away):

| Final | Pain | Was planned as |
|---|---|---|
| P01 | Agent cannot see the browser | P01 |
| P02 | Copy-paste friction, mangled paste | P02 |
| P03 | Hand the bug straight to the agent | P03 |
| P04 | Agents cannot watch a bug video | P10 (vision/video) |
| P05 | Agents cannot consume screenshots | P09 (vision/video) |
| P06 | No proof the fix worked | P04 / P14 |
| P07 | PR review cannot see the UI | P08 (vision/video) |
| P08 | Login walls block reproduction | P12 |
| P10 | No agent trigger on the filed issue | P16 |
| P11 | Cannot reproduce | P06 |
| P12 | Secrets and privacy in recordings | P05 |
| P13 | False completion claims | P14 |
| P14 | Reporter cannot describe the bug | (new, not planned) |
| P15 | Competitors already do "copy for agent" | P17 |
| P16 | Bug reports must be auditable | (new, not planned) |
| P17 | Evidence cost and context budget | P11 + P15 (merged) |

Two planned nodes never became nodes: **P13 (environment mismatch)** and **P14 (flaky fixes)**
as separate nodes — the evidence for them turned out to be the same source as P08 and P13
respectively, so they were folded in rather than given thin files of their own. **P09 in this
plan's numbering is P05 in the final set**, and the *final* P09 was merged into P17 in US-003.

The vision/video area required by the PRD is covered by **P04** (video → frames + transcript +
timeline), **P05** (the agent cannot consume the screenshots) and **P07** (the reviewer cannot
see the UI) — three nodes, above the required two. Risk 3 in section 6 materialised: the
"obvious" features are already shipped by Clipy, ThinkRun and a dozen Chrome extensions, so
the novelty scores were cut against competitors, not only against our own repo.
