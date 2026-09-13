---
slug: cGradedDebt
node: c
opened: 2026-09-12
streams: tooling
roster: TOOL
ids: TOOL-cGradedDebt-1 TOOL-cGradedDebt-2 TOOL-cGradedDebt-3 TOOL-cGradedDebt-4 TOOL-cGradedDebt-5
authorized-by: prompt
---

# cGradedDebt — a curation-debt row that hides nothing still reds nothing

## The problem this build exists to solve

`memory/project/curation-debt.txt` drops each listed file from hygiene checks 6, 7 and 8 outright.
Its four sibling registries in `memory/project/` all carry a stale-entry guard, a shrink-only pin, or
both; this one carries only a tracked-path assertion, so a row that has stopped hiding anything
stays green forever. Measured at `09a22d2b`: the `memory/backlog/TOOL.md` row was listed for a byte
cap the same day that cap was raised past the file, and the row outlived the fault by three weeks.
While listed it also silences check 8 across 438 of the corpus's 499 backlog rows, which hides six
real status-token faults, and check 8's own population guard counts shard FILES rather than graded
ROWS, so it reports a green verdict over an 88% waived population and prints no count at all.

## Expected improvements

- A listed file that would pass unwaived is named as a stale row rather than sitting green.
- Each listed row's report names which of checks 6, 7 and 8 it actually earns, so an over-wide
  waiver is visible without redding the row.
- Check 8 announces the number of rows it graded, so a waiver covering most of them cannot read
  as coverage.
- The six real faults `TOOL.md` carries are fixed rather than waived.

## Detriments if this is not built

- The one registry in `memory/project/` with no ratchet keeps growing on rows nobody re-measures.
- Check 8 keeps a green verdict that proves nothing about 88% of its population.
- The next raised cap silently retires another row, the same way the last one did, and the next
  audit re-derives the same finding from scratch.

## Build-level rules

- **`TOOL-aWeighedCompass-3` is not pre-empted, and no exception grammar is added for it.** That
  row carries the owner's open call on splitting or shortening the `TOOL` shard. `TOOL.md` is over
  `INDEX_CAP_BYTES` by 5.8x today, so the stale guard measures it as earning its listing and leaves
  it alone. A guard needing a named exception on the day it lands would be a guard aimed at the
  wrong thing.
- **No conf pin for this registry.** `tools/drift-audit/drift_signals.py` already declares it under
  `SHRINK_ONLY` against a git-history seed. A second shrink-only assertion in `.memory-tree.conf`
  would be two answers to one question, and the one that reds first would win by accident.
- **The guard is whole-file, and per-check width is REPORTED rather than failed.** Redding a row for
  an idle check-7 waiver would red `TOOL.md` today, which is the owner call above.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-cGradedDebt-1` | 2 | a curation-debt row earns its listing, and check 8 counts what it graded |
| 2 | `TOOL-cGradedDebt-2` | 1 | the six status-token faults the `TOOL.md` row was hiding |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node c · opened 2026-09-12 · streams tooling
ids TOOL-cGradedDebt-1 TOOL-cGradedDebt-2 TOOL-cGradedDebt-3 TOOL-cGradedDebt-4 TOOL-cGradedDebt-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cGradedDebt-1 — a curation-debt row earns its listing, and check 8 counts what it graded](spec/2026-09-12-spec-TOOL-cGradedDebt-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cGradedDebt-2 — the six status-token faults the TOOL.md row was hiding](spec/2026-09-12-spec-TOOL-cGradedDebt-2.md) | 2 | 1 | CLOSED | rev-3 | 2026-09-13 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-cGradedDebt-1 TOOL-cGradedDebt-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-cGradedDebt-1` | no |
| 2 | `TOOL-cGradedDebt-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
