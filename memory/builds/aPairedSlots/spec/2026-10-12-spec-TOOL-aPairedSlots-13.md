# TOOL-aPairedSlots-13 — the two-bar check reads the verdict by key and grades its rows at their declared width

**Status:** INPROGRESS · rev-1 · 2026-10-12 · node a · Tier-1 · base d3354597 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-14 TOOL-aPairedSlots-15 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's H3 (id 13): the two-bar check stores the first line of a run record's `verdict`
file, `ended<TAB><time>`, as the record's verdict, so each `check.tsv` row carries eleven fields under
a ten-field header. Its row predicate then compares the end time with a leg count as strings and
never reads the ledger-rows column, so at gov's leg count every row reds as lost or torn. This check
is the build's VERIFYING evidence that two concurrent bars of one repository lose nothing, and one
run of it is already under way on the old copy.

## 2. Scope (IN)

- **S1 — the verdict is read by key.** `measure_bar` takes the `verdict` key's value, and counts a
  bar's ledger rows by its run id, the ledger's sixth field, rather than by a time window. Observed by
  AC1.
- **S2 — grading is its own verb.** `grade <root>` computes the verdict from what a run left: the leg
  verdicts, the `check.tsv` rows and the run records. `run` ends by calling it. A row of any width but
  ten is refused by name, except the eleven-field row the earlier copy wrote with `ended` in its
  verdict column, which is read with that column joined. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The overlap guard (TOOL-aPairedSlots-14).
- Re-running the check: `grade` re-reads the run already under way.

## 4. Design

The ledger keeps one row per leg and is rewritten by every run, so a serial run's rows are gone once
the concurrent run of that worktree ends. They can be counted only right after the bar, which is
where `measure_bar` already runs; `grade` reads that count from the row. Everything else it
re-derives from records that survive the run.

### Files touched (estimate)

- `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh`

## 5. Acceptance criteria

- **AC1** — When `grade` runs over a fixture root holding the eleven-field rows the earlier copy
  writes, every row with one run-log line, a verdict and ledger rows at least its leg count passes,
  and a row whose ledger count is below its leg count is named.
  Red when: a passing row is named lost or torn, or the short row passes.
- **AC2** — When `grade` meets a row of nine fields, it names the row as malformed and the check fails.
  Red when: the short row is graded as if its columns were in place.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-12 · initial draft, promoted from the closing review's round 1.
