# TOOL-dDeclaredLoop-49 — the budget's `spent` counts every draw of the build, across every record, in commit order

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 29 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-49-deviation-491.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-49-deviation-491.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 52 at HIGH**, its item **H18**, alone in that item. `TOOL-dDeclaredLoop-30` §4
"Data model" says "`spent` is the draw's ordinal among the record's draw rows", one record, while S3 reads
the rows "over every transition record of the build". Each draw appends to the newest record and every
route-back writes a new one, so a builder following §4 resets `spent` at each transition, and the
route-back cascade this budget exists to bound never exhausts it. No criterion draws across two records.
This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-30`.

## 2. Scope (IN)

- **S1** — `spent` is the count of draw rows over every home `budget_state` reads for the build, its
  `transition` log records and its run-state rows included, ordered by the commit that wrote each row and,
  within one commit, by position; `total` is the figure of the build's one freeze row, or the base before
  it. This supersedes `TOOL-dDeclaredLoop-30` §4's "ordinal among the record's draw rows".
  Observed by AC1.
- **S2** — The typed `<spent>/<total>` on a row is what the writer derived when it wrote it. A reader
  re-derives both, and a typed figure that disagrees prints `budget: <row> typed <a>, derived <b>` and is
  not a refusal, because two worktrees appending in parallel each type the figure their own history saw.
  This supersedes `TOOL-dDeclaredLoop-30` §4's refusal of a disagreeing typed figure. Observed by AC2.
- **S3** — Two worktrees appending to one record merge by union: `.gitattributes` gains
  `memory/builds/*/build/*-transition-*.md merge=union`, so both rows survive a merge and S1 counts both.
  Observed by AC2.

## 3. Non-goals (OUT)

- Where a draw is written under a channel set without `log`: id 7, unit `TOOL-dDeclaredLoop-48`, whose
  homes S1 counts over.
- A spec lint over quantities defined twice with different scopes, the finding's left-shift: AC1 is the
  cross-record criterion every budget reader now carries.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-30` — `budget_state` and `record_draw` in `tools/loop/budget.py`, whose count this unit defines over the whole build
- **hands-off** `TOOL-dDeclaredLoop-61` — the draw rows, which that unit makes unique by a draw id (the round-2 spec audit's id 53)
- **hands-off** `TOOL-dDeclaredLoop-62` — the transition-record merge driver and its evidence, which that unit restates against the recorded measurement (the round-2 spec audit's id 38)
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 8, 18, 44 and 62: this pass keeps the loop budget fixtures leg green; the adopter route and the README weighing are scope items of that unit

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-30` S3 appends each draw to the newest `transition` record and reads the rows back
  over every `transition` record of the build; `TOOL-dDeclaredLoop-10` writes a new record per backward
  transition, so the newest record changes at every route-back.
- `.gitattributes` declares no `merge=` rule today (read 2026-10-24); git's built-in `union` driver keeps
  both sides' lines of a conflicting hunk.

### The count

```
rows = every draw row of the build, from each home budget_state reads
order rows by (commit order of the writing commit, position in that commit)
spent(row k) = k ; spent = len(rows) ; total = freeze row's figure, else the base
exhausted when spent == total
```

### Files touched (estimate)

- `tools/loop/budget.py`
- `.gitattributes`

### Alternatives rejected

- **Keeping the typed-figure refusal.** Two parallel worktrees both type `3/10`; after a union merge the
  second row disagrees with its derived `4/10`, and the refusal would wedge every later draw.
- **One budget record per build.** It changes where the rows live, which is the clause's "in its
  transition record" and `TOOL-dDeclaredLoop-48`'s concern, not the count's.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — the reader already walks every record; ordering adds one `git log` over them.
- error / empty / loading states — a build with no draw reads `0/<total>`; a disagreeing typed figure
  prints, never refuses.
- observability — the disagreement line names the row and both figures.
- risks — `merge=union` on a record whose rows are not append-only could interleave lines; transition log
  records only ever gain rows, which is why the rule names that one glob.
- testing — AC1 and AC2 as fixture plants; the arm under §7, observed at the close.
- migration — none: no budget row exists yet.
- user docs — the budget section of `help/loop.md` says the count is the build's, across records.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant draws-across-records` draws three times,
  records a route-back, then draws twice more, the fifth draw's row reads `5/<total>` and `budget_state`
  answers `open 5/<total>`.
  Red when: `spent` restarts on the route-back's new record and reads `2/<total>`.
- **AC2** — When `--plant parallel-append` commits one draw on each of two branches off one record and
  merges them, the merge has no conflict, `budget_state` counts both, and one row prints the
  `typed 1, derived 2` line.
  Red when: the merge conflicts on the record, or the disagreeing typed figure refuses the read.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/budget.py · covers AC1 AC2 · the `draws-across-records` and `parallel-append` plants, staged against the per-record ordinal · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — What happens to the typed figure's refusal?** Options: (a) keep it and forbid parallel appends;
  (b) make the typed figure advisory, the derived count deciding. (a) wedges the budget the first time two
  worktrees draw. RESOLVED (agent, 2026-10-24, delegated): (b), rung 3: the typed figure is a copy of a
  derived fact, which the charter's `[derive]` rule says never decides. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 52 (HIGH, item H18).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-61 and TOOL-dDeclaredLoop-62 and TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dDeclaredLoop-30`'s own reader, `budget_state`, and git's built-in `union` merge driver;
no new reader. `python tools/codebase-map/reuse_lookup.py "count rows across every record of a build in
commit order"` ranked generic `rows`, `row`, `counts` and `records`, none of which orders a build's rows
by commit, and the budget module is minted in this build.

Recall terms used: rework budget spent total draw rows transition records route-back union merge typed figure
