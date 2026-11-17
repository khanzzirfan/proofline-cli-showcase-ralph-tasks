# Architecture drafts: the top two Session Recorder features

Drafts for the two features ranked highest by the multi-agent research (`research/FINAL-RANKING.md`).
Both target [`prooflinedev/session-recorder-chrome-extension`](https://github.com/prooflinedev/session-recorder-chrome-extension). Written before I switched to the CLI; neither was built.

| # | Feature | Doc | Pains it answers | Size |
|---|---|---|---|---|
| 1 | Copy for coding agent, with an agent brief | [01-copy-for-coding-agent.md](01-copy-for-coding-agent.md) | agent can't see the browser; copy-paste hand-off; vague reports; "fixed" without proof | small |
| 2 | Video key frames and timeline | [02-video-keyframes.md](02-video-keyframes.md) | agents can't watch a bug video; screenshots don't reach the agent | medium |

## How a recording becomes a report today (existing code)

```
 CAPTURE (while recording)                         STORAGE                     EXPORT (after stop)
 ─────────────────────────                         ───────                     ───────────────────
 content scripts                                                               lib/export/bundle.ts
  interactions / annotations / file-capture ─┐                                  buildBundle({session, events,
 background.ts + lib/capture/*               │    lib/storage (IndexedDB        assets, level})
  console, network (debugger), screenshots ──┼──▶ "session-recorder")  ───────▶   │
 offscreen/video.ts                          │     sessions                      ├─ lib/export/trimmer.ts
  MediaRecorder → one webm per record-span ──┤     events  (SessionEvent[])      │    applyLevel(events, L0..L3)
  (video-segment event + 'video' asset)      │     assets  (Blob: screenshot,    ├─ lib/export/markdown.ts
 offscreen audio + lib/transcription ────────┘              audio, video, …)     │    renderReport() → report.md
                                                                                 │    renderManifest() → MANIFEST.md
                                                                                 ├─ lib/export/openapi.ts
                                                                                 └─ ExportFile[] ─┬─▶ lib/export/zip.ts → .zip download
                                                                                                  ├─▶ lib/sharing/report.ts → publish
                                                                                                  └─▶ lib/sharing/summary.ts → issue text
 Callers of buildBundle: sidepanel/components/ExportPanel.tsx, report/main.ts (Download), lib/sharing/report.ts
```

Two facts drive both designs:

1. **One pipeline.** Every output goes through `buildBundle` + `applyLevel`, so redaction and trimming are already
   applied. New features should consume `ExportFile[]` (or the trimmed events) rather than re-read raw storage.
2. **Levels drop heavy bytes.** L2+ keeps events but clears file references (`thinVideo`, `thinScreenshots`,
   body clearing). That is exactly the gap feature 2 fills: compact levels lose the video entirely today.

## Shared decisions

- Deterministic, no LLM. Both features are pure transforms of recorded evidence, like the trimmer.
- No new dependency, no new permission. Clipboard writes happen in extension pages on a user click.
- Same privacy story: they reuse redacted, trimmed bundle output; nothing new leaves the browser unless the user exports, copies or publishes.
- Out of scope: live agent streaming and a local MCP server (`docs/PLAN.md` puts live streaming out of scope for v1).
