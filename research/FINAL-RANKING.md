# Final ranking: pains of people handing bugs to AI coding agents

Combined from the 7 Ralph research runs that completed on 17 Nov 2026 (8 turns, one skipped; same brief, same scoring rubric). Source counts are each run's own report of what it re-opened.
Per-run detail: `runs/<run>/ranking.md`, nodes in `runs/<run>/nodes/`. Machine comparison: `compare/comparison.md`.

## The runs

| Run | Model | Stories | Notes | Sources (verified / unverified / dropped) | Top pick |
|---|---|---|---|---|---|
| 1 | DeepSeek v4 Flash | 5/5 | 14 | 67 / 12 / 4 | Copy for coding agent |
| 2 | MiniMax m3.1 Flash | 5/5 | 14 | 60 / 0 / 1 | Copy for coding agent |
| 3 | GPT-6 Luna | 5/5 | 13 | 14 / 4 / 1 (thin) | One-click agent hand-off |
| 4 | Claude Sonnet | 5/5 | 13 | 51 / 9 / 1 | Copy for coding agent |
| 5 | DeepSeek v4 Pro | 5/5 | 15 | 25 / 0 / 3 | **Video → key frames + timeline** |
| 6 | MiniMax m3 | 5/5 | 16 | 51 / 0 / 8 | Copy for coding agent |
| 7 | GPT-6 Astra | skipped | | not in the Command Code plan | |
| 8 | Claude Opus | 5/5 | 15 | 78 / 9 / 14 (most thorough) | Copy for coding agent |

## 1. What hurts most in the world (pain ranking)

| # | Pain | Runs ranking it top 5 | Strongest evidence (checked by hand on 17 Nov) |
|---|---|---|---|
| 1 | **The agent can't see the browser**: no console, network, DOM or rendered page, so it guesses | 7 of 7 | claude-code [#57034](https://github.com/anthropics/claude-code/issues/57034) (76 reactions, open); [#75632](https://github.com/anthropics/claude-code/issues/75632); Cursor forum [152452](https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452) |
| 2 | **The agent says "fixed" without proof**, and the UI is still broken | 5 of 7 (Opus #1) | [#75632](https://github.com/anthropics/claude-code/issues/75632) ("reviewing the PR blind"); GitHub community [#169913](https://github.com/orgs/community/discussions/169913) |
| 3 | **Agents can't watch a bug video**; people cut frames by hand | 5 of 7 (DeepSeek Pro #1) | claude-code [#12676](https://github.com/anthropics/claude-code/issues/12676) (57 reactions, 21 comments, open); single-purpose tools videobug, amagi-screen, BugDump |
| 4 | **Copy-paste hand-off is slow and lossy** | 6 of 7 | Cursor forum [58803](https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803); HN "Heckle" Show HN (6 points, weak) |
| 5 | **Screenshots don't reach the agent** (CLI agents can't paste images; oversized images break chats) | 4 of 7 | Copilot docs on visual inputs; copilot-cli image paste requests |
| 6 | **Vague reports: missing steps, state, expected vs actual** → agent fixes the wrong thing | 5 of 7 | several runs, mostly forum and blog evidence |
| 7 | Fear of leaking secrets in recordings | 3 of 7 | real, but the extension already has 5 open redaction PRs (4 from applicants, 1 from the maintainer) |

## 2. Best PR for Session Recorder (pick ranking)

| # | Feature | Runs | Avg pick score /40 | Size | Overlap with open PRs |
|---|---|---|---|---|---|
| 1 | **Copy for coding agent**: one click puts a ready prompt + trimmed `report.md` on the clipboard | top pick in 5 of 7 by name, 6 counting GPT-6 Luna's "one-click agent hand-off"; top 2 in all 7 | ≈ 34 | small | none |
| 2 | **Video → key frames + timeline** in the report (frames at clicks, errors, annotations) | top 5 in 5 of 7 | ≈ 32 | medium | none |
| 3 | **Acceptance check / "how to verify the fix"** block (failing requests and errors that must disappear) | 4 of 7 | ≈ 31 | small | none |
| 4 | **Agent brief**: steps to reproduce, expected vs actual, at the top of `report.md` | 4 of 7 | ≈ 31 | small | none |
| 5 | Agent-safe screenshot export (paths, captions, size cap) | 3 of 7 | ≈ 30 | small | none |

## 3. Caveats

- **Anchoring.** Every agent read our context notes, which already named "Copy for coding agent" as the leaning. So the agreement on pick #1 is partly inherited. The pain ranking (section 1) is more independent: it comes from evidence the agents found, and pain #1 and #3 are backed by high-reaction GitHub issues I checked myself.
- **Reddit was weak** in most runs (blocked or few relevant threads). GitHub issues, the Cursor forum and HN carried most of the evidence.
- **GPT-6 Luna** cited few sources (14 verified); weight it lower. GPT-6 Astra did not run.

## 4. Recommendation

**Main PR:** "Copy for coding agent", with its payload built as an *agent brief*: repro steps, expected vs actual, the first error, and an acceptance check (what must stop happening for the fix to count). That merges picks 1, 3 and 4 into one small, coherent feature that answers pains 1, 2, 4 and 6.

**Strong alternative or second PR:** key frames + a timeline from the recorded tab video. It has the clearest unmet demand (57 reactions on claude-code #12676), it uses evidence the extension already records, and no open PR does it. It is larger and only helps when video recording is on.
