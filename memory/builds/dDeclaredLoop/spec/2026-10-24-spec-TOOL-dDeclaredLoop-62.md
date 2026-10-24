# TOOL-dDeclaredLoop-62 — the transition-record merge driver chosen against the recorded union measurement and the row driver's own refusal

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 30 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-62-deviation-621.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-62-deviation-621.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 38 at HIGH**, its item **H4**, which it shares with id 53; id 53 is
`TOOL-dDeclaredLoop-61`. `TOOL-dDeclaredLoop-49` S3 adds `merge=union` for transition records on the
evidence that `.gitattributes` "declares no `merge=` rule today". It declares `merge=rows` and
`merge=ours` (`.gitattributes:71`, :72, :78, :84-86 and :94), and :63-65 record that union was rejected for
introducing a duplicate in 147 of 151 historical conflicts; and union takes two identical appended rows
once, so the budget under-counts. `TOOL-dDeclaredLoop-61` makes every row unique. This unit makes the
driver choice on the corrected evidence, measures both candidates against draw rows, and ships the one
that keeps every draw exactly once. It repairs `TOOL-dDeclaredLoop-49`.

## 2. Scope (IN)

- **S1** — The candidates are weighed in the tree, not assumed: the `.gitattributes` comment above the
  transition-record line names the existing `merge=rows` route and the 147-of-151 union measurement, and
  states why each does or does not fit draw rows, citing §4's two probes. Observed by AC3.
- **S2** — The driver is union over unique rows: the line stays
  `memory/builds/*/build/*-transition-*.md merge=union`, now resting on `TOOL-dDeclaredLoop-61`'s draw id
  instead of on the false evidence, per §8 F2. This supersedes `TOOL-dDeclaredLoop-49` §4's Evidence
  bullet on `.gitattributes`. Observed by AC1, AC2.
- **S3** — The duplicate half of the measurement, the half the union record was about, is observed on
  draw rows: two sides appending distinct draws merge with each row present exactly once, and a side
  that appends two rows while the other appends one yields three, none repeated. Observed by AC2.
- **S4** — Draw rows stay append-only, the property union's safety rests on: `record_draw` and
  `freeze_budget` only append to a record and never rewrite a line already in it, asserted by a plant
  that diffs the record before and after a draw. Observed by AC4.

## 3. Non-goals (OUT)

- The draw id: `TOOL-dDeclaredLoop-61`.
- The rule reaching adopters' `.gitattributes`, and the literal `memory/` in the glob: the audit's ids 62
  and 8, batched into `TOOL-dDeclaredLoop-67`.
- A checklist entry that an Evidence claim "declares no X" is backed by a recorded grep, the left-shift
  of the paired medium: the class is recorded at the close.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-49` — the `.gitattributes` line for transition records and the build-wide count it protects, whose evidence and driver this unit restates
- **consumes-from** `TOOL-dDeclaredLoop-61` — the draw id, without which union takes two identical draws once
- **hands-off** `TOOL-dDeclaredLoop-67` — the driver and its weighing, which that unit carries into the loop README and the adopter route (ids 18 and 62)

## 4. Design

### Evidence

- `grep -n merge .gitattributes` at base `ed497191`: `merge=rows` at :71, :72 and :78, `merge=ours` at
  :84-86 and :94, and the union rejection at :63-65 (147 of 151 `DECISIONS.md` conflicts).
- Probe 1, 2026-10-24, node `d`: `python tools/memory-tree/merge-rows.py O A B <transition path>` over a
  record where each side appended `- draw · fix-pass · TOOL-dX-2 · 2/10 · <distinct id>` exited 1 with
  `DuplicatedContent: ... 'TOOL-dX-2' x3 against x2`. Its id half refuses a record whose rows lead with
  one id more often than any input (`tools/memory-tree/merge-rows.py:117-118`, `row_ids` at :479), and
  a draw row names its unit, so two legitimate draws on one unit always conflict: PINNED, that date.
- Probe 2, the same date: `git merge-file --union` over bare rows kept both rows when they differed only
  in their draw id, and kept one when they were byte-identical: PINNED.

### Why union survives here

The 147-of-151 record measured files whose rows are edited in place, where union keeps both versions of
an edited line. That cause is UNVERIFIED by this unit; S4 makes it unreachable for draw rows by
asserting they are never edited, and S3 measures the duplicate direction on draw rows directly.

### Files touched (estimate)

- `.gitattributes`
- `tools/loop/budget.py`

### Alternatives rejected

- **`merge=rows`.** Probe 1: its id postcondition refuses two draws on one unit, the exact parallel case.
- **No driver.** git's text merge conflicts on every pair of appends at a record's end, which
  `TOOL-dDeclaredLoop-49` AC2 forbids.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — none.
- error / empty / loading states — a union merge never conflicts; a malformed merged row is named by
  `budget_state` as `TOOL-dDeclaredLoop-61` says.
- observability — the `.gitattributes` comment carries the weighing.
- risks — a future writer that edits a draw row in place reintroduces union's duplicate; S4's plant reds
  on it.
- testing — AC1 to AC4 as plants; the arm under §7, observed at the close.
- migration — none: the line's value is unchanged.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant parallel-append-identical-union` merges two branches
  that each drew the same cause on the same item with the same typed figure, under the tree's
  `git check-attr merge` answer for a transition record, the merge exits 0 and `budget_state` counts both.
  Red when: the attribute names `rows`, which refuses, or the rows carry no id and union keeps one.
- **AC2** — When `--plant parallel-append-distinct` merges one draw on one side and two on the other,
  the merged record holds three draw rows and no row line twice, counted by `sort | uniq -d` printing
  nothing.
  Red when: union writes a row twice.
- **AC3** — When `grep -n -B4 'transition-\*.md merge=' .gitattributes` runs, its comment lines name
  `merge=rows`, `147 of 151` and the draw id.
  Red when: the line rests on no recorded weighing, as `TOOL-dDeclaredLoop-49` §4 left it.
- **AC4** — When `--plant append-only` diffs a record before and after one draw, the diff adds lines and
  removes none.
  Red when: a draw rewrites an existing row.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/budget.py · covers AC1 AC2 AC4 · the identical, distinct and append-only plants, staged against a fixture attribute naming `rows` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which driver merges transition records?** The report's fix says to stop using union and route
  through `merge=rows` or make every row unique. Options: (a) `merge=rows`, the repository's ratified
  append-collision driver; (b) union over `TOOL-dDeclaredLoop-61`'s unique rows; (c) no driver. (a) fails
  `TOOL-dDeclaredLoop-49` AC2 by Probe 1, its id postcondition refusing two draws on one unit; (c) fails
  the same criterion by conflicting; veto 1 discards both. RESOLVED (agent, 2026-10-24, delegated): (b),
  the only survivor, with the row uniqueness that closes the collapse and S3 and S4 closing the
  duplicate direction. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 38 (HIGH, item H4, shared
  with id 53).

## 10. Reuse audit

The seams are the existing drivers git and this repository ship: `tools/memory-tree/merge-rows.py`,
measured and refused for draw rows by Probe 1, and git's union, kept. `python
tools/codebase-map/reuse_lookup.py "unique field on an appended row so a merge keeps both"` ranked
`rows`, `row`, `merge` (`tools/memory-tree/merge-rows.py`, `tools/settings-merge.py`), `field`,
`extract_row` and `id_rows`; the two `merge` functions are the row driver and the settings merger, and
the first is the candidate this unit tested and rejected.

Recall terms used: gitattributes merge union rows driver transition record draw row duplicate 147 DuplicatedContent
