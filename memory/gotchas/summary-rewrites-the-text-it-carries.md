---
name: summary-rewrites-the-text-it-carries
description: a compaction summary that reproduces a block as verbatim quietly rewrites the lines that look wrong in it, so the defects the block carried read as fixed and the copy passes for the original
kind: class
universal: false
---

# A summary rewrites the text it carries

## Symptom

A session is compacted. Its summary reproduces a generated block the session must keep exact, and calls
it verbatim. Most lines are. The lines that looked wrong, such as a fragment or a non-sentence, come back
as plausible text, and nothing marks the change. A reader of the summary sees a clean block, and the
defect the block carried is gone from view.

## Where it bit

dClosedLoop's project map, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`,
`[reload-summary]`).

The summary carried the level-0 map's 355 lines and called them verbatim. Three differed from the file
read before the compaction. They were the three kits whose derived purposes were sentence fragments, and
each came back as a tidy purpose, such as "drift-audit kit". The session then told the owner that the
map had come through verbatim.

## The fix

- Never take a summary's copy for the original. After a compaction, regenerate what must stay exact, or
  re-read it from disk.
- Diff the summary's copy against the file before saying that it came through.
- Keep a block that must survive a compaction in a file the next context re-reads, not in the summary.

It has no machine gate. The standing ask to regenerate the map after every compaction is the procedure
that catches it.
