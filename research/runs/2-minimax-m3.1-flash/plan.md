# US-001: Search plan — Pain research run `2-minimax-m3.1-flash`

Agent/model: `command-code-research` / `minimax/minimax-m3.1-flash`
Output dir: `<mission>/research/runs/2-minimax-m3.1-flash`
Date: 2026-11-17

## 0. Goal and constraints (restated from the PRD)

Find, from public evidence, the pains developers / QA / product people hit when they report, reproduce and fix browser
bugs with AI coding agents, rank them, and turn the best into one clean PR for **Session Recorder by Proofline**.

Hard rules I will follow for the rest of the run:

- Write only inside this output dir (`plan.md`, `sources.md`, `ranking.md`, `ranking.json`, `recommendation.md`,
  `run-summary.md`, `nodes/*.md`, `raw/*.json`).
- Never open, list or read another folder under `research/runs/`. Never edit the extension repo, the PRD or the notes.
- No git commands that mutate anything, no PRs/issues/comments, no sign-ins.
- Every claim gets a real URL I actually opened. Quotes verbatim, ≤30 words. Unopenable pages are `unverified`.
  Vendor marketing is weak evidence and must be labelled as such.
- No personal data. Usernames only when they are part of a public URL. No emails.
- `curl` always with `-A "pain-research/1.0"`, ~2 s between calls to the same host, raw JSON kept under `raw/`.

## 1. What the extension already does (so I do not propose what exists)

Read on 2026-11-17: `README.md`, `PRODUCT.md`, `docs/report-format.md`, `docs/PLAN.md`, plus the `lib/` and
`entrypoints/` tree.

Already covered, therefore **novelty = 0** for anything that only repeats these:

| Capability | Where it lives today |
| --- | --- |
| Clicks, inputs, navigation, tabs | `entrypoints/interactions.content.ts`, `lib/capture/` |
| Console, exceptions, network, WebSocket frames | `lib/capture/console.ts`, `lib/capture/network.ts` |
| Screenshots, live annotations, screenshot markup | `lib/capture/screenshots.ts`, `lib/annotations/`, `entrypoints/point-annotations.content.ts` |
| Microphone narration + transcript | `lib/transcription/`, `lib/annotations/dictation.ts` |
| Tab video with sound | `lib/export/bundle.video.test.ts`, `docs/report-format.md` (video/ at L0-L1) |
| Files/attachments | `entrypoints/file-capture.content.ts` |
| Inferred OpenAPI description | `lib/export/openapi.ts` |
| ZIP export with `report.md` + 4 trim levels (Full/Standard/Compact/Minimal), deterministic, no LLM | `lib/export/trimmer.ts`, `lib/export/markdown.ts`, `lib/export/bundle.ts` |
| AI summary + GitHub issue filing + hosted report | `lib/sharing/summary.ts`, `lib/sharing/github.ts`, `lib/sharing/cloudflare.ts` |
| Copy issue Markdown to clipboard | `entrypoints/share/useShareReport.ts` → `copyIssue()` (line 330) |
| "Suggested prompt" for agents | `docs/report-format.md` (docs only, not in the product) |

**Known gap (from the notes):** handing a report to an agent is manual — export ZIP, unzip, paste `report.md`, copy the
prompt out of the docs. `copyIssue()` copies the *issue* Markdown, not an agent-ready bundle.

**Open PRs I must not duplicate** (from `00-context-notes.md` §3, extension repo):
`#49` group recordings of the same error · `#48` labels and assignees when filing · `#47` per-repo transcription
vocabulary · `#46` Deepgram language detection · `#45` shadow DOM clicks and typing · `#44` WebSocket frame redaction ·
`#43` Copy as cURL · `#42` secret protection across evidence · `#41` storage snapshot · `#40` redirect hops as requests ·
`#39` request and trace IDs of failed requests · `#38` redact card/IBAN/tax IDs · `#37` redact tokens in URLs ·
`#33` E2E navigation race fix · `#32` HAR export · `#31` redact URL params · `#30` isolate test tabs ·
`#29` browser, OS, viewport in report · `#25` typed value before submit · `#24` Linear issues · `#23` UJG docs bundle ·
`#21` screenshot and pause keyboard shortcuts · `#22` Playwright repro test in ZIP (closed by its author).

## 2. Tool status measured today (not assumed)

I probed every channel before planning so the plan only contains routes that actually work.

| ID | Source type | Endpoint | Status on 2026-11-17 | Evidence |
| --- | --- | --- | --- | --- |
| ST1 | GitHub issues, sort=reactions | `api.github.com/search/issues?...&sort=reactions` | **works**, 200. 852 hits for `repo:anthropics/claude-code+browser+console` | `raw/probe_github_reactions.json` |
| ST2 | GitHub issues, sort=comments | same, `&sort=comments` | **works**. `repo:anthropics/claude-code+browser` = 7200 hits | probe above |
| ST3 | GitHub repo discovery, sort=stars | `api.github.com/search/repositories?q=...&sort=stars` | **works**, 54 hits for `bug report mcp agent` | `raw/probe_github_repos.json` |
| ST4 | Reddit JSON, sort=top | `www.reddit.com/r/<sub>/search.json?...&sort=top` | **BLOCKED 403** (HTML shell, ~190 KB) with both a generic and a browser UA. `old.reddit.com/.../search.json` → 404. `top.json` → 403 | probe discarded |
| ST5 | Hacker News, points | `hn.algolia.com/api/v1/search?query=...&tags=story&numericFilters=points>5` | **works**. 43 hits for "coding agent browser bug" | `raw/probe_hn_algolia.json` |
| ST6 | HN comments | `hn.algolia.com/api/v1/search?...&tags=comment` | **works** (18 hits for "coding agent screenshot bug") | probe above |
| ST7 | Cursor forum (Discourse) | `forum.cursor.com/search.json?q=...` and `forum.cursor.com/t/<slug>/<id>.json` | **works**. Full thread text, usernames, dates, read counts | `raw/probe_cursor_forum_search.json`, `raw/probe_cursor_forum_thread.json` |
| ST8 | Web fetch of GitHub pages | `github.com/<org>/<repo>/issues/<n>`, `github.com/orgs/community/discussions/<n>` | **works**, returns the full issue/discussion body plus reaction counts | verified today on issue 75632 and discussion 169913 |
| ST9 | Web fetch of review sites | `chromewebstore.google.com/detail/...` | **blocked in practice**: HTTP 200 but only the JS shell, no review text | probe today |
| ST10 | Web search tool | built-in `web_search` | **works** but ranking is weak for review/long-tail pages; good for discovering URLs | verified today |

Constraints to design around:

- **GitHub API**: unauthenticated core quota is 60/hour and is now exhausted (`rate_limit` → `core.remaining 0`).
  The **search** bucket is separate (10/min) and still has quota. → Use `api.github.com/search/*` for discovery; do not
  depend on `api.github.com/repos/...` core calls. Pace search calls at **≥8 s** apart.
- **Repos with issues disabled** return `422 Validation Failed` on `repo:` searches and therefore cannot be searched
  this way: `getcursor/cursor`, `All-Hands-AI/OpenHands`, `sst/opencode`. Their pain evidence must come from
  forum.cursor.com (ST7), GitHub Discussions HTML (ST8), Reddit (ST4 fallback) and HN (ST5/ST6).
- **Searchable and worth mining**: `anthropics/claude-code` (852+ on browser+console), `openai/codex` (41 053 issues),
  `github/copilot-cli` (4 887), `cline/cline` (5 058), `RooCodeInc/Roo-Code` (3 559), `microsoft/playwright-mcp` (947),
  `ChromeDevTools/chrome-devtools-mcp` (245).
- **Reddit fallback**: when ST4 is blocked, use `web_search` with `site:reddit.com` and say so in `run-summary.md`;
  try `web_fetch` on `old.reddit.com/r/<sub>/search?q=...&sort=top` as a second fallback. Reddit evidence found this way
  must be marked `unverified` unless the page text is actually readable.
- **Chrome Web Store / Product Hunt / G2**: treat as *secondary*. ST9 returns the JS shell. Use `web_search` snippets
  and fetch the product's own site/blog, then mark CWS review text `unverified` unless readable.

## 3. Search queries

30+ concrete queries over 10 source types. Every row is a literal string/URL I will run.

### 3.1 GitHub issue search — ST1 (sort=reactions) and ST2 (sort=comments)

Base: `https://api.github.com/search/issues?q=<Q>&sort=<reactions|comments>&order=desc&per_page=20`

| # | Q | Sort | Tests |
| --- | --- | --- | --- |
| Q01 | `repo:anthropics/claude-code+browser+console` | reactions | H1 — agent cannot see console/network |
| Q02 | `repo:anthropics/claude-code+browser+console` | comments | H1, deeper discussion |
| Q03 | `repo:anthropics/claude-code+screenshot+image` | reactions | H6 — vision evidence for agents |
| Q04 | `repo:anthropics/claude-code+video+recording` | reactions | H6 — video an agent cannot watch |
| Q05 | `repo:anthropics/claude-code+visual+regression` | reactions | H6/H7 — visual diffs |
| Q06 | `repo:anthropics/claude-code+playwright+browser+verify` | comments | H7 — proof the fix works |
| Q07 | `repo:anthropics/claude-code+issue+template+reproduce+steps` | reactions | H4 — issue quality |
| Q08 | `repo:openai/codex+screenshot+image+attach` | reactions | H6 — CLI agents cannot take images |
| Q09 | `repo:openai/codex+video` | reactions | H6 |
| Q10 | `repo:openai/codex+bug+report+issue` | comments | H4 |
| Q11 | `repo:github/copilot-cli+screenshot+image` | reactions | H6 |
| Q12 | `repo:github/copilot-cli+attach+image+issue` | comments | H6/H4 |
| Q13 | `repo:cline/cline+browser+screenshot` | reactions | H1 |
| Q14 | `repo:cline/cline+image+attach+issue` | comments | H6 |
| Q15 | `repo:RooCodeInc/Roo-Code+browser+console+network` | reactions | H1 |
| Q16 | `repo:RooCodeInc/Roo-Code+screenshot+visual+diff` | reactions | H6/H7 |
| Q17 | `repo:microsoft/playwright-mcp+video+record` | reactions | H6 — MCP video |
| Q18 | `repo:microsoft/playwright-mcp+screenshot+diff` | reactions | H7 |
| Q19 | `repo:ChromeDevTools/chrome-devtools-mcp+screenshot` | reactions | H6 |
| Q20 | `repo:ChromeDevTools/chrome-devtools-mcp+video+trace` | reactions | H6 |
| Q21 | `browser+recording+report+coding+agent+in:title` | reactions | H3 — the whole category, repo-agnostic |
| Q22 | `bug+report+mcp+server+agent+in:title` | reactions | H3 |
| Q23 | `screenshot+visual+regression+pull+request+ai+review+in:title` | reactions | H6/H7 |
| Q24 | `issue+duplicate+triage+ai+bot+in:title` | reactions | H9 |
| Q25 | `token+cost+context+window+report+agent+in:title` | reactions | H10 |
| Q26 | `local+storage+cookie+state+reproduce+agent+in:title` | reactions | H8 |

### 3.2 GitHub repo discovery — ST3 (sort=stars)

Base: `https://api.github.com/search/repositories?q=<Q>&sort=stars&order=desc&per_page=20`

| # | Q | Tests |
| --- | --- | --- |
| Q27 | `bug report mcp agent` | the competitive set of hand-off tools (H3) |
| Q28 | `browser session recording agent bug report` | who already ships "record → agent" (H3) |
| Q29 | `visual regression ai agent screenshot` | who already solves the vision gap (H6) |
| Q30 | `bug report video keyframes agent` | video-to-agent tooling (H6) |

### 3.3 Hacker News — ST5 (points) and ST6 (comments)

| # | URL | Tests |
| --- | --- | --- |
| Q31 | `hn.algolia.com/api/v1/search?query=coding agent browser bug&tags=story&numericFilters=points>5` | H1, H3 — already 43 hits, incl. "Heckle – Send a bug's full browser context to your coding agent" |
| Q32 | `hn.algolia.com/api/v1/search?query=bug report screenshot agent&tags=story&numericFilters=points>10` | H3, H6 |
| Q33 | `hn.algolia.com/api/v1/search?query=visual regression ai review&tags=story&numericFilters=points>5` | H6, H7 |
| Q34 | `hn.algolia.com/api/v1/search?query=video recording bug agent&tags=story` | H6 (video) |
| Q35 | `hn.algolia.com/api/v1/search?query=coding agent screenshot bug&tags=comment&hitsPerPage=50` | H6 — comment text from "Wax" already surfaced: *"my coding agent claiming a page was pixel-perfect when it"* |
| Q36 | `hn.algolia.com/api/v1/search?query=browser context handoff agent&tags=comment` | H3 |
| Q37 | `hn.algolia.com/api/v1/search?query=prove fix works agent screenshot&tags=comment` | H7 |

### 3.4 Cursor forum (Discourse) — ST7

| # | URL | Tests |
| --- | --- | --- |
| Q38 | `forum.cursor.com/search.json?q=browser console agent` | H1 — already returns "Web / Cursor Agent browser tool not capturing rendered DOM elements" |
| Q39 | `forum.cursor.com/search.json?q=attach screenshot issue` | H4, H6 |
| Q40 | `forum.cursor.com/search.json?q=MCP bug report` | H3 |
| Q41 | `forum.cursor.com/search.json?q=video recording` | H6 |
| Q42 | `forum.cursor.com/search.json?q=visual regression screenshot` | H6, H7 |
| Q43 | `forum.cursor.com/t/<slug>/152452.json` (known thread) | H1 — verbatim: agent cannot read console/network of the built-in browser |

### 3.5 Reddit — ST4 blocked, planned fallbacks (recorded as a limitation)

| # | Query | Fallback |
| --- | --- | --- |
| Q44 | `r/ClaudeAI` top: `browser console` / `screenshot` / `debug` | `web_search "site:reddit.com/r/ClaudeAI ..."` |
| Q45 | `r/cursor` top: `browser console network` | `web_search "site:reddit.com/r/cursor ..."` |
| Q46 | `r/ChatGPTCoding` top: `bug report agent evidence` | `web_search "site:reddit.com/r/ChatGPTCoding ..."` |
| Q47 | `r/webdev` top: `before after screenshot PR AI review` | `web_search "site:reddit.com/r/webdev ..."` |
| Q48 | `r/QualityAssurance` top: `bug report AI agent` | `web_search "site:reddit.com/r/QualityAssurance ..."` |
| Q49 | `r/ExperiencedDevs` top: `AI agent context bug report` | `web_search "site:reddit.com/r/ExperiencedDevs ..."` |

### 3.6 Web fetch of known pages — ST8

| # | URL | Tests |
| --- | --- | --- |
| Q50 | `github.com/anthropics/claude-code/issues/75632` | H1, H7 — read today: "Claude can't visually verify frontend work" |
| Q51 | `github.com/anthropics/claude-code/issues/52907` | H1 — console capture + DOM inspection |
| Q52 | `github.com/orgs/community/discussions/169913` | H6, H7 — read today: "there’s no guaranteed way to make Copilot always add screenshots to a PR" |
| Q53 | `forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console.../152452` | H1 |
| Q54 | `docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs` | H6 — vendor doc (weak) |
| Q55 | `github.com/anthropics/claude-code/issues?q=is%3Aissue+label%3Aarea%3Atools+browser` | H1 label-scoped sweep |

### 3.7 Web search — ST9/ST10 (discovery + secondary review evidence)

| # | Query | Tests |
| --- | --- | --- |
| Q56 | `chrome web store Jam bug report extension review missing console network` | H2, H10 (CWS text may be unreachable → mark unverified) |
| Q57 | `"Marker.io" OR "BetterBugs" OR "Darnly" OR "FlowLens" review "AI agent" bug report missing` | H2, H3 |
| Q58 | `Product Hunt "Jam" reviews AI bug report developers want screenshot to agent` | H3 |
| Q59 | `G2 bug report extension reviews AI agent handoff` | H3 |
| Q60 | `bug report video AI agent key frames Loom analysis` | H6 (video) |
| Q61 | `"visual regression" AI code review screenshots pull request 2026` | H6, H7 |
| Q62 | `agent generated issue spam duplicate PR triage GitHub repo 2026` | H9 |
| Q63 | `coding agent token cost long report context window trimming` | H10 |

## 4. Hypotheses to test

Ten hypotheses: the five pains already in `00-context-notes.md` §5 (H1-H5), one on vision and video (H6, required),
and four on pains the notes do not list (H7-H10).

**H1 — "The agent cannot see the browser, so it guesses."**
Notes §5.1. The agent has no console, no network panel, no rendered DOM, no URL state.
Falsifier: evidence shows agents *do* get browser state by default and users are happy.
Tests: Q01, Q02, Q13, Q15, Q38, Q43, Q50, Q51, Q53, Q55.
Node: P01. Expected fit high (the extension already captures console/network/screenshots) — the missing part is the
*hand-off*, not the capture.

**H2 — "Copy-paste is the hand-off, and it leaks."**
Notes §5.2. Users paste console logs, cURL, HAR; secrets leak; pasted context sometimes never reaches the agent.
Falsifier: users report a smooth one-click channel already works for them.
Tests: Q56, Q57, Q58, Q59, Q44-Q49, Q32.
Node: P02.

**H3 — "People want to hand a bug straight to an agent."**
Notes §5.3. MCP servers, one-link handoffs, agent-installed reporters (Jam MCP, Darnly, FlowLens, Faylee).
Falsifier: the market has already converged and users are satisfied with the existing tools.
Tests: Q21, Q22, Q27, Q28, Q31, Q32, Q36, Q40, Q57, Q58.
Node: P03 (and P04 for the "no channel exists inside the tool" variant).

**H4 — "Cloud agents start from a GitHub issue, so issue quality is the bottleneck."**
Notes §5.4. Copilot reads the issue, Jules the `jules` label, Codex `@codex`, OpenHands `fix-me`.
Falsifier: agents mostly start from a branch or a prompt, not from issues.
Tests: Q07, Q10, Q12, Q39, Q44-Q49.
Node: P05.

**H5 — "Evidence carries secrets and personal data; people need masking before sharing."**
Notes §5.5. Header/URL redaction exists; screenshots, audio, free text and video are not covered.
Falsifier: users report the current redaction as sufficient and do not ask for more.
Tests: Q37 (redact), Q42 (redact card/IBAN), Q46, Q48, Q57.
Node: P06 (note the PR overlap: #31, #37, #38, #42, #44 all touch redaction — novelty for a new redaction feature is low).

**H6 — VISION AND VIDEO (required): "Neither PR reviewers nor agents can see what a change looks like."**
Two sub-pains, searched separately:
- (a) *Visual checks in PR review*: AI reviewers and PR agents cannot see the UI a change produces; visual regression
  and before/after screenshots in PRs are flaky or missing; Copilot's screenshot attach is not guaranteed (Q52).
- (b) *Agents cannot consume images*: CLI agents without an image-paste path (Codex, Copilot CLI, Cline, opencode) only
  get text; a bug video is unusable, so it must be reduced to key frames, a timeline, or a written transcript.
Falsifier: agent + PR review pipelines today reliably carry screenshots/video, so there is no gap.
Tests: Q03, Q04, Q05, Q08, Q09, Q11, Q12, Q14, Q16, Q17, Q19, Q20, Q23, Q29, Q30, Q31, Q33, Q34, Q35, Q41, Q42, Q52,
Q54, Q60, Q61, Q47, Q57.
Nodes: P07 (PR/AI review cannot see the UI), P08 (agents cannot take or read images; no image path in CLI agents),
P09 (bug video → key frames / timeline / text for an agent).
Must check what an agent can use **today** from what the extension already records: `video/` is only in the zip at
Full/Standard, `report.md` references screenshots as image links, L3 keeps screenshots as a filename manifest only, and
`docs/report-format.md` says "include the extracted folder when the agent can read screenshots". So the gap is real for
agents that only read text.
Only propose a vision/video feature if the evidence shows a real gap; otherwise say so plainly.

**H7 — "Nobody can prove the fix worked."**
Users want proof a fix works (before/after, screenshot in the PR, a regression check). Agents assert "pixel-perfect"
without looking; Copilot screenshots 404 or go missing; CI screenshot checks are flaky.
Note: the notes mention "users want proof that a fix works" only as a sub-point of §5.4, so treat H7 as its own node.
Falsifier: pipelines reliably attach before/after evidence and agents verify visually.
Tests: Q05, Q06, Q16, Q18, Q23, Q33, Q42, Q52, Q61, Q37.
Node: P10. Overlap: extension PR `#22` (Playwright repro test in ZIP, closed by its author) and `#29` (browser/OS/viewport
in report).

**H8 — "The bug only exists in *my* environment, and the agent cannot recreate it."**
Auth state, local storage, cookies, viewport, feature flags, the exact commit/build that is deployed.
Falsifier: reports already carry enough environment context and users do not ask for more.
Tests: Q26, Q07, Q39, Q48, Q50, Q51.
Node: P11. Overlap: extension PR `#41` (storage snapshot) — so a storage-snapshot feature scores novelty 0; a *report-level
environment block* that states auth/viewport/build/deployed URL may still be novel.

**H9 — "The issue queue is full of AI noise."**
Agents and AI reporters flood repos with issues and PRs; humans must dedupe, triage and decide what is real. Users want
grouping, dedupe and priority.
Falsifier: triage noise is not a top complaint.
Tests: Q24, Q39, Q46, Q62.
Node: P12. Overlap: extension PR `#49` (group recordings of the same error) — so "group duplicate recordings" is not
novel; "an agent-ready triage view" might be.

**H10 — "The evidence is too big and the cost is unknown."**
Users do not know which verbosity level to give an agent; big reports burn context and tokens; agents ask for
re-exports at the wrong level.
Falsifier: users are happy with the current 4 levels and the token estimate.
Tests: Q56, Q63, Q25, Q32, Q07.
Node: P13. The extension already has 4 levels + a token estimate, so novelty is limited to *what* is dropped for an agent
(e.g. an agent-calibrated default) — this hypothesis may score low on novelty, and that is a legitimate finding.

### Extra pains I will opportunistically capture if the evidence surfaces them (not pre-committed)

- Users reporting bugs **to a non-browser surface** (mobile, backend, mobile-web) that a browser recorder cannot cover.
- Capture **silent gaps** (DevTools open → debugger cannot attach; the report must admit what it missed).
- Reporters who **cannot sign in** to the app under test (test accounts, seeded state) — a real blocker for agents.
- Non-English reporters and the **"low-quality issue"** complaint (wrong severity, wrong area, missing repro).

## 5. Places to cover (PRD "popular places" list) and my route to each

| Place | Route | Plan |
| --- | --- | --- |
| anthropics/claude-code | ST1/ST2 | Q01-Q07, Q50, Q51, Q55 |
| getcursor/cursor + forum.cursor.com | ST7 (issues disabled) | Q38-Q43, Q53 |
| openai/codex | ST1/ST2 | Q08-Q10 |
| github/copilot-cli + github community discussions | ST1/ST8 | Q11, Q12, Q52 |
| All-Hands-AI/OpenHands | issues disabled → discussions/web | web_search `site:github.com/All-Hands-AI/OpenHands discussions screenshot browser` + Q31-Q37 |
| RooCodeInc/Roo-Code | ST1 | Q15, Q16 |
| sst/opencode | issues disabled → web/HN/Reddit | web_search `site:github.com/sst/opencode discussions screenshot` |
| cline/cline | ST1 | Q13, Q14 |
| ChromeDevTools/chrome-devtools-mcp | ST1 | Q19, Q20 |
| microsoft/playwright-mcp | ST1 | Q17, Q18 |
| BrowserMCP / browser-use | ST3 | Q27, Q28 |
| r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev, r/QualityAssurance, r/ExperiencedDevs | ST4 blocked → ST9 `site:` queries | Q44-Q49 |
| Hacker News | ST5/ST6 | Q31-Q37 |
| Chrome Web Store reviews | ST9 partially blocked | Q56, Q57 (secondary) |

## 6. Planned node list (target 16-20, ≥3 outside the notes)

| Node | Slug | Hypothesis | Likely source types | Notes overlap? |
| --- | --- | --- | --- | --- |
| P01 | agent-cannot-see-browser | H1 | ST1, ST7, ST8 | – |
| P02 | copy-paste-leaks-and-loses-context | H2 | ST7, ST9 | – |
| P03 | hand-bug-straight-to-agent-mcp | H3 | ST1, ST3, ST5 | – |
| P04 | no-agent-channel-inside-the-tool | H3 | ST7, ST8 | extension PR #48 partly |
| P05 | issue-is-the-bottleneck | H4 | ST1, ST8 | extension PR #48 partly |
| P06 | secrets-and-pii-in-evidence | H5 | ST1, ST7 | PRs #31 #37 #38 #42 #44 |
| P07 | ai-pr-reviewer-cannot-see-the-ui | H6a | ST1, ST8, ST5 | – |
| P08 | cli-agents-cannot-read-images | H6b | ST1, ST5, ST8 | – |
| P09 | bug-video-unusable-by-agents | H6c | ST1, ST5, ST7 | extension records video already |
| P10 | nobody-can-prove-the-fix | H7 | ST1, ST8, ST5 | PR #22 closed, #29 |
| P11 | environment-state-context-missing | H8 | ST1, ST7 | PR #41 |
| P12 | issue-queue-ai-noise | H9 | ST1, ST9 | PR #49 |
| P13 | context-cost-and-trim-guessing | H10 | ST9, ST1 | – |
| P14 | capture-gaps-silent-failure | extra | ST8, ST1 | – |
| P15 | repro-steps-lose-structure | H4/H8 | ST1, ST7 | – |
| P16 | agent-fixes-break-other-things | H7 | ST1, ST5 | – |
| P17 | repro-env-missing-auth-seed | H8 | ST7, ST9 | – |
| P18 | issue-quality-triage-noise-low-signal | H9 | ST1, ST9 | PR #49, #48 |

P07-P18 include at least 3 pains that are **not** in notes §5 (P07, P08, P09, P10, P11, P12, P13 all qualify).

## 7. Scoring plan for US-004 (recap of the rubric)

- `pain_score = 2*frequency + 2*severity` (max 20)
- `pick_score = 2*frequency + 2*severity + 2*fit + smallness + novelty` (max 40)
- frequency from **independent sources with engagement** (reactions/comments/score/points), not from one loud thread.
- fit from what the extension already captures and where a few-hundred-line PR can land.
- novelty = 0 if an open extension PR already does it (#21-#49 list in §1).
- smallness = 5 only for one PR of a few hundred lines with tests (e.g. clipboard handoff, report-section addition).

## 8. Risks and known gaps in this plan

1. **Reddit is blocked.** Reddit evidence will be thin and partly `unverified`. Mitigation: HN comments, GitHub issues and
   the Cursor forum carry the same population; state the limitation in `run-summary.md`.
2. **Chrome Web Store / Product Hunt / G2 review text is not machine-readable** through my tools. Those will be
   `unverified` or dropped unless a readable mirror appears.
3. **Agent repos with issues disabled** (Cursor, OpenHands, opencode) will be under-sampled; I compensate with the forum
   and Discussions.
4. **Vendor material will dominate search results** for "bug report AI"; I will treat it as weak evidence and label it.
5. **Popularity ≠ pain.** A high-reaction feature request in claude-code may be a support request rather than a pain.
   I will only keep a node when the text shows an actual frustration.
6. **Rate limits**: GitHub search is 10/min; I will pace at 8 s and log what failed.
7. **Freshness**: sources run to 2026; I will record dates and prefer the most recent strong signal, but will also use
   older high-signal threads (e.g. the 2025 Copilot discussion) when they describe the same pain.

## 9. Output files this plan produces downstream

- `nodes/P01-*.md` … `nodes/P18-*.md` — one file per pain, node format from the PRD.
- `sources.md` — every URL, with `verified | unverified | dropped`, header line `verified: N, unverified: N, dropped: N`,
  and the popular-places coverage list.
- `ranking.md` + `ranking.json` — the two tables and the machine-readable ranking.
- `recommendation.md` — top 3 features by `pick_score`, each with real file paths in the extension, a test plan, risks
  and the open PRs it must not duplicate.
- `run-summary.md` — method, counts, which tools worked, and the weaknesses above.
