# Proofline mission: research notes so far (17 Nov 2026)

Everything we learned before the multi-agent research run. Read this first.

## 1. The mission

- Role: Founding Staff / Principal Engineer at Proofline (proofline.sh). Founder: Mohsen Azimi (GitHub `mohsen1`).
- Application = a meaningful **feature** pull request (not docs-only) to one of Proofline's open source repos:
  CLI (Rust), Python SDK, TypeScript SDK, or the Chrome extension. Then email careers@proofline.sh with the PR link,
  the role and a short intro. The PR does not need to be merged.
- The PR body must say who the feature helps, the decisions made, and how it was verified.
- Every repo's `AGENTS.md` asks external contributors to put all session prompts in a hidden HTML comment in the
  PR body. Undecided: whether we include them (the owner decides).

## 2. Proofline's open source repos (github.com/prooflinedev)

| Repo | Language | Notes |
|---|---|---|
| `cli` | Rust | review, hooks (pre-commit, pre-push), SARIF, fix list/verify, ask/wiki/plan, coverage upload, export, `agent install` (claude-code, cursor, codex, gemini, kiro) |
| `sdk-python` | Python | sync + async clients, `iter_reviews`, `export_reviews` (one page) |
| `sdk-typescript` | TS | `iterReviews`, `exportReviews` (one page) |
| `session-recorder-chrome-extension` | TS, React, WXT | **chosen target**. 18 stars. AGPL-3.0. Local clone: `proofline-mission/session-recorder-chrome-extension` |
| `mcp`, `skills` | JS / config | MCP bridge (`npx @proofline/mcp`), agent skills |
| `yek` | Rust | 2.4k stars, repo serializer for LLMs (not an eligible target) |
| `ai-review-benchmarks` | Python | a Proofline engineering challenge |

## 3. What the GitHub issue and PR history shows (checked 17 Nov 2026)

- Almost no real user issues. Nearly every open item is an applicant PR. No discussions are enabled anywhere.
- **No external PR has ever been merged** in cli, sdk-python, sdk-typescript, the extension or mcp. Standing out matters more than merging.
- Crowded topics (avoid): export paging (7 PRs: TS #29 #42, Py #27 #31 #35 #52, CLI #42), GitHub job summary
  (CLI #53 #66, Py #41), SARIF, wait-for-review variants, fail-on gates, new `agent install` editors (Windsurf #56,
  Antigravity #54, Zed #60), case-insensitive Content-Type (3 PRs), redaction in the extension (5 PRs).
- Our finished TS SDK PR (`iterExportReviews`, worktree `sdk-typescript-iter-export`) duplicates 7 others, so we keep it only as a possible second PR.
- Founder's only open request in the extension: issue #28, fix three failing Playwright tests (a fix, not a feature).
- One applicant (sdk-python #48) installed Proofline on their own fork and posted the review result in the PR. That is a good way to stand out, since the maintainers' Proofline check says "author has no Proofline seat".

### Open PRs in session-recorder-chrome-extension (do not duplicate)

#49 group recordings of the same error and add to existing issues · #48 labels and assignees when filing ·
#47 per-repo transcription vocabulary · #46 Deepgram language detection · #45 shadow DOM clicks and typing ·
#44 WebSocket frame redaction · #43 Copy as cURL · #42 secret protection across evidence · #41 storage snapshot ·
#40 redirect hops as requests · #39 request and trace IDs of failed requests · #38 redact card, IBAN, tax IDs ·
#37 redact tokens in URLs · #33 E2E navigation race fix · #32 HAR export · #31 redact URL params (founder) ·
#30 isolate test tabs · #29 browser, OS, viewport in report · #25 typed value before submit · #24 Linear issues ·
#23 UJG docs bundle · #21 screenshot and pause keyboard shortcuts. Closed by its author: #22 Playwright repro test in ZIP.

### What the extension already does

Record → annotate → file a GitHub issue. Captures clicks, inputs, navigation, tabs, console, exceptions, network,
screenshots, annotations, narration and transcripts, video, files, an inferred OpenAPI description. ZIP export with
`report.md` at Full, Standard, Compact or Minimal trim levels (deterministic trimming, no LLM). AI summary,
publishing (Cloudflare Pages or Proofline hosting), GitHub issue filing. Product docs: `PRODUCT.md`, `DESIGN.md`,
`docs/report-format.md` (contains a "Suggested prompt" for coding agents), `docs/PLAN.md` (out of scope for v1:
live streaming to an agent, rrweb DOM replay, Firefox and Safari).

Gap we found: handing a report to a coding agent is manual (export ZIP, unzip, paste `report.md`, copy the prompt
from the docs). The code only copies the issue Markdown (`copyIssue` in `entrypoints/share/useShareReport.ts`).

## 4. Research on other tools (round 1: Qodo/pr-agent, opencode, Roo Code, Devin, OpenHands)

- pr-agent: /describe, /review, /improve, /ask, changelog. Good idea: readable review reports in CI.
- opencode: terminal agent, MCP under an `mcp` object with `type: "local"` and a command array; plugins; LSP; session sharing.
- Roo Code: checkpoints, custom modes, orchestrator, codebase indexing, MCP in `.roo/mcp.json` (`mcpServers`).
- Devin Review: groups big diffs, tracks bugs, auto-fix pushes to the branch, `npx devin-review <PR>`.
- OpenHands resolver: `fix-me` label or `@openhands` comment → agent opens a draft PR and comments results.

## 5. Research round 2: what users ask of cloud coding agents (thin on Reddit, stronger elsewhere)

1. **"My agent can't see the browser."** Claude Code requests: browser view in cloud sessions
   (anthropics/claude-code#75632), console capture and DOM inspection (#52907). Cursor forum: agent cannot read the
   built-in browser's console or network tab. Blogs: agents guess at frontend bugs.
2. **Copy-paste friction.** Users paste console logs, cURL or HAR by hand; tokens leak; pasted logs sometimes do not reach the agent (Cursor forum).
3. **Hand bugs straight to an agent, often through MCP.** Jam MCP (mcp.jam.dev), Darnly, FlowLens (open source), Faylee (one link over MCP for Claude Code, Codex, Cursor, opencode).
4. **Cloud agents start from GitHub issues.** Copilot (assign the issue; reads screenshots in the issue), Jules (`jules` label), Codex (`@codex`), OpenHands (`fix-me`, `@openhands`). Users want proof that a fix works (screenshots in the PR), which is not reliable today.
5. **Redaction and safety.** Faylee masks tokens and cards; a local MCP server was found open to any local process.

### Candidate features for the extension (before this research run)

| Option | Need | Size | Overlap |
|---|---|---|---|
| A. Copy for coding agent: prompt + trimmed report on the clipboard | 1, 2 | small | none |
| B. Agent-ready GitHub issue: optional agent trigger and an agent instructions block | 4 | medium | partly #48 |
| C. Local MCP server for recordings | 3 | too big; security risk | none |
| D. Playwright repro test | proof of fix | large | #22 (closed by author) |

Current leaning: A plus the shared instructions block from B.

## 6. Sources

- https://github.com/anthropics/claude-code/issues/75632
- https://github.com/anthropics/claude-code/issues/52907
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803
- https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs
- https://github.com/orgs/community/discussions/169913
- https://www.sinatra.dev/blog/copilot-coding-agent-vs-jules-vs-codex
- https://jam.dev/ · https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj
- https://www.producthunt.com/products/flowlens-ai-native-bug-reports
- https://vibehacker.com/news/faylee-turns-a-bug-report-into-one-link-your-coding-agent-can-open-over-mcp-and-
- https://www.infosecurity-magazine.com/news/chrome-extension-ai-engine-act-mcp/
- https://docs.devin.ai/work-with-devin/devin-review · https://docs.openhands.dev/openhands/usage/run-openhands/github-action
- https://github.com/Codium-ai/pr-agent · https://opencode.ai/docs/mcp-servers · https://docs.roocode.com/features
