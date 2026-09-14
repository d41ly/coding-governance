---
name: waiver-row-that-hides-nothing-reds
description: a curation-debt row whose file would pass unwaived is itself a failure, and check 8's population is the backlog shards alone — so a row listed for a fault it does not earn reds instead of protecting
kind: class
---

# A waiver row that hides nothing reds, and check 8 grades only the backlog shards

## Symptom

A file is added to `memory/project/curation-debt.txt` "to be safe", or a row survives after the
fault it covered was fixed or its cap was raised past it. The hygiene leg reds on the ROW: the file
passes checks 6, 7 and 8 unwaived, so the registry has stopped shrinking and the row hides nothing.
The remedy is to delete the row, not to re-justify it.

The second half is a population fact that misleads the same reader: check 8 grades the backlog
shards under `memory/backlog/` ALONE, and PRINTS its graded-row count on every run. A build README
is structurally outside check 8's population and a run-state file outside check 7's, so a row listed
against "6, 7 and 8" for a file only one of them can see is over-wide by construction.

## Where it bit

`TOOL-cGradedDebt-1`. The tooling shard's own row outlived its fault by three weeks after the cap
was raised past it, and nothing said so until the stale-entry guard landed. The per-row report was
added in the same unit because the registry's hand-written blast-radius paragraphs disagreed with
what the checks actually earned; where the two disagree, the run is right.

## The fix

List only a MEASURED fault. Run `bash tools/memory-tree/check-memory-hygiene.sh` and read what the
per-row report names for each row — the denominator is derived per file, never the literal three —
and delete any row it names as earning nothing. Never add a row to a registry that can only shrink
on the expectation that it will be needed.

Gated by check 6's stale-entry guard in `tools/memory-tree/check-memory-hygiene.sh`, which reds the
row; and by the report line, which is not a second verdict but is the evidence a row's width is
written against.
