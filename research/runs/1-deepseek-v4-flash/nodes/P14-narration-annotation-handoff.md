---
id: P14
title: "Narration and annotation are the de-facto hand-off, but they are not machine-readable"
who: QA, product, developers
tools: [Loom, Jam, BugDump, Session Recorder]
status: partly-verified
---
## Pain
Non-technical reporters explain bugs by talking over a screen recording and drawing on a
screenshot. That is the easiest report to produce, but the value sits in voice and pixels an
agent cannot read. Tools then transcribe and OCR to recover text, and the transcript itself can
be wrong.

## Evidence
- https://news.ycombinator.com/item?id=49119880 (hn, 2026-07-31, verified): Tentomushi: "We built this side project to reduce the back-and-forth that follows vague bug reports." A commenter: "users often submit recordings without enough context. They show what happened, but not what they expected to happen."
- https://bugdump.com/blog/whisper-transcribing-narrated-bug-reports (blog, verified): Whisper transcription of narrated bug reports, and "where it goes wrong" (a silent clip came back as "you").
- https://videolens.io/screen-recording-analyzer (vendor, verified): "Turn a screen recording into an actionable report." via "Transcript + frame vision + OCR".
- https://www.reddit.com/r/webdev/comments/ymooqx/i_made_a_browser_extension_that_makes_it_easier/ (reddit, unverified): a tool to "annotate and comment on top of your UI then post the screenshot directly to a GitHub or GitLab pull/merge request".

## How users want it fixed
- Turn narration and on-screen annotation into structured text (steps + expected vs actual) the agent can use.
- Capture the reporter's expected behaviour, not just what happened.

## Workarounds people use today
- Transcribe the video by hand; retype what was drawn; OCR screenshots.

## Session Recorder angle
The extension already records narration and transcripts and supports annotations. The gap is
whether the agent-facing `report.md` turns annotations/narration into clean, ordered text next to
the event they describe. That is a plausible small feature and no open PR covers the annotation →
agent-text mapping directly. Not in section 5.

## Scores
frequency: 3  severity: 3  fit: 4  smallness: 4  novelty: 3
