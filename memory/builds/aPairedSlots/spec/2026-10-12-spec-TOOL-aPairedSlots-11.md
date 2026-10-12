# TOOL-aPairedSlots-11 — the drift history is created with its header already in it

**Status:** INPROGRESS · rev-1 · 2026-10-12 · node a · Tier-2 · base d3354597 · streams tooling · order 8

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing review's H1 (id 7, with M6, ids 15 and 32): TOOL-aPairedSlots-7 made the drift history's
first writer create the file empty with an exclusive open and append its header with a second open.
A second writer that appends between the two lands its rows above the header, and the history's one
reader, which takes line 0 as the header, then refuses the file for good: every later `--delta`
prints `skipped` and dead-probe streaks stop. The split also leaves an empty file no later writer
heads. The unit's arm passed on that layout, because it counted header lines and never read the file
back.

## 2. Scope (IN)

- **S1 — the file appears with its header.** A writer that finds no history writes the header to a
  temporary file of its own and publishes it at the history's path with a hard link, which fails when
  the path exists. Whichever writer's link lands, the file has a header on line 0 before any row
  reaches it. A writer whose link finds the path taken writes no header. Observed by AC1.
- **S2 — every writer appends its rows in one write, and an empty file is headed.** The rows follow in
  one binary append, and a writer that finds the file empty, from a truncation or a writer killed
  before the link, writes the header first, as the writer before TOOL-aPairedSlots-7 did. Observed by
  AC2.
- **S3 — a file system with no hard links still gets a history.** A link that fails for any reason
  but an existing path falls back to the S2 append, which heads an empty or absent file. Observed by
  AC2.
- **S4 — the arm reads the file back through its reader.** The two-writers arm runs the second writer
  inside the first one's window, now the moment before its link, writes full rows, and asserts what
  `read_history_groups` returns. Observed by AC1.

## 3. Non-goals (OUT)

- A reader that accepts a header below line 0. The only files that hold one are written by the code
  this unit replaces, on a node where two bars were both first writers; none is known.
- The health log's trim (TOOL-aPairedSlots-10).

### Edges

none

## 4. Design

### The race, and why a link closes it

Two writers both find no history. Under TOOL-aPairedSlots-7 the first to create it owned the header,
but wrote it in a second step. With a link, the step that makes the path exist is the same step that
puts the header in it: the temporary file already holds the header when it is linked, so no writer
can open the path and see it headless. The loser's link raises `FileExistsError`, and it appends. A
temporary file per process, named by pid, keeps two creators from writing one temporary. It is
removed in a `finally`, whichever way the link went.

### Inventory

No function is minted. `write_drift_history` changes; `read_history_groups` does not.

### Messages

Unchanged: one stdout line on success, one stderr line on failure.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`

### Alternatives rejected

- **A reader that tolerates the header anywhere.** It repairs files the old writer could produce, and
  the new writer cannot produce them.
- **A lock file.** The link is already atomic on every file system that supports it, and the fallback
  covers the rest.

## 5. Production-readiness checklist

- security — N/A — a node-local history file under the git common dir.
- perf / scale — one extra write and link on the first write of a clone, nothing after.
- error / empty / loading states — S2 heads an empty file, S3 covers a refused link.
- observability — the existing success and failure lines.
- risks — a file system without hard links takes the fallback, which is the writer before
  TOOL-aPairedSlots-7, duplicate header race included.
- testing — the two-writers arm, staged red on the writer this replaces.
- migration — none.
- user docs — none: the history's format does not change.

## 6. Acceptance criteria

- **AC1** — When the drift self-test's two-writers arm runs a second writer just before the first
  writer's link, `read_history_groups` returns two groups and no skip reason, and line 0 is the header.
  Red when: the arm's interleaving never ran, or the reader refuses the file, or a row precedes the
  header.
- **AC2** — When `write_drift_history` writes to an existing empty history, the file's line 0 is the
  header and its rows follow.
  Red when: the rows land without a header.

## 7. Gates

`drift-audit selftest` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, promoted from the closing review's round 1.

## 10. Reuse audit

The seam is `write_drift_history` itself and its one reader beside it. `reuse_lookup.py "publish a
file atomically with its header"` ranked name-stem neighbours only, none of which publishes a file,
so no existing seam fits; `os.link` is the standard library's atomic publish. Recall named TOOL-aMendedFleet-48,
which introduced the history; TOOL-aPairedSlots-7 is the unit this one corrects.

Recall terms used: `python tools/memory-recall/query.py "how does the drift history file get its header written" --terms "drift history header writer reader append exclusive create first writer race tsv"`
