# TOOL-aRepatriatedFork-56 — brief-recorded does not grade a repair of a unit built before its run

**Status:** SPECCED · rev-1 · 2026-10-02 · node a · Tier-1 · base 65bb64c2 · streams tooling · order 27

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-prompt-TOOL-aRepatriatedFork-56-build-brief.md](../prompts/2026-10-02-prompt-TOOL-aRepatriatedFork-56-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`check-brief-recorded.sh` grades every CLOSED unit at its build commit, which the kit library's
`build_commit` picks as the EARLIEST commit in the run's range, `<base>..HEAD`, that names the unit
and touches a path outside the record surface. A unit built in an EARLIER run has its real build
commit behind the base. A VERIFYING gate repair that names that unit as the owner of a fix is then
the earliest in-range match, and the leg reds the unit for a missing brief row the run never owed it.
This run's final bar redded `TOOL-aRepatriatedFork-2` exactly so, at R2's repair commit `c22ac2b8`.
This unit makes the leg recognise a unit built before its run and announce it rather than grade it.

## 2. Scope (IN)

- **S1** — Before the leg records a missing-brief violation, it asks `build_commit` for a commit
  naming the unit at or behind the run's base, newest first and bounded by the cap pass-order's
  pre-anchor probe already uses. When one exists, the unit is NOT GRADED: one line names it, its
  in-range commit and the earlier one, and the summary counts it. Observed by AC1 and AC2.
- **S2** — A probe that reaches its cap answers nothing, and the unit is graded as at base, which
  fails closed. Observed by AC3.
- **S3** — The header states what the skip does not see. Observed by AC4.

## 3. Non-goals (OUT)

- `TOOL-aRepatriatedFork-46`'s waiver row. That unit was built in this run, and its misread is a
  records commit touching `.memory-tree.conf`, a different shape.
- `build_commit` itself, and `check-pass-order.sh`, which keeps its own pick.
- Whether brief-recorded keeps a waiver registry at all, which is parked for the owner.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-55` — the other gate this run's final bar redded; it writes
  disjoint files.

## 4. Design

### Evidence

- The final bar at `01c22e15`, `GATE_FULL=1`, 2026-10-01: `brief-recorded` red on
  `TOOL-aRepatriatedFork-2 — BUILT at c22ac2b8 with NO brief row`. `c22ac2b8` is
  `TOOL-aRepatriatedFork-2: gate repair, hook destinations at a root install`, a commit of the
  VERIFYING repair R2.
- `check-pass-order.sh` already probes behind a base with
  `build_commit "$base" … "$PREANCHOR_CAP" ""`, newest first and bounded, and treats `TRUNCATED` as
  no answer.

### Files touched (estimate)

- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/check-brief-recorded.test.sh`
- the unattended kit's version carriers

### Alternatives rejected

- A waiver row for `TOOL-aRepatriatedFork-2`. The owner chose the checker fix (2026-10-02), and every
  later repair of an earlier run's unit would need another row.
- Skipping any commit whose subject reads `gate repair`. The subject is authored, so a real build
  could buy its way out with a word.

## 5. Production-readiness checklist

- security — none; a read-only gate over tracked history.
- perf / scale — one bounded probe, and only for a unit about to be recorded as a violation.
- error / empty / loading states — a truncated probe grades the unit (S2).
- observability — every skip prints its own line and the summary counts them.
- risks — a unit with an earlier commit naming it and a real build inside this run would go
  ungraded; S3 states it, and its line names both commits.
- testing — AC1 to AC3.
- migration — none.
- user docs — none; a gov-internal leg.

## 6. Acceptance criteria

- **AC1** — When a fixture unit is built before the run's base and a later in-range commit names it
  with no brief row, the leg exits 0 and prints the unit with `built before its run`, naming both commits.
  Red when: the base checker is staged into the arm and reds the unit, which is the red-first control.
- **AC2** — When a fixture unit has no commit naming it behind the base and its in-range build
  commit has no brief row, the leg still reds it with `NO brief row`.
  Red when: the skip reaches a unit built inside the run.
- **AC3** — When the probe's cap is set below the distance to the earlier commit, the unit is graded
  and reds with `NO brief row`.
  Red when: a truncated probe buys the skip.
- **AC4** — When the leg's header is read, it states that a unit with an earlier commit naming it is
  not graded even if `its real build is in the run`.
  Red when: it does not.
- **AC5** — When `bash tools/unattended/check-brief-recorded.sh` runs on this tree, it exits 0 and
  names `TOOL-aRepatriatedFork-2` as built before its run.
  Red when: it reds that unit, or another unit moves to NOT GRADED.

## 7. Gates

`brief-recorded` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates`

New arm: `tools/unattended/check-brief-recorded.test.sh` · a unit built before the base and repaired in range, a unit built in range, and a truncated probe · the suite's floor rises by the new arms

## 8. Open questions

- **F1 — how does the leg know a unit was built before its run?** Option (a): a commit naming it
  behind the base, through the pre-anchor probe pass-order already runs. Option (b): a subject
  grammar for repair commits. Recommendation: (a), because history is not authored by the commit
  being graded.
  RESOLVED (owner, 2026-10-02): fix the checker's pick; (a) is that fix.

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft from the owner's 2026-10-02 ruling on the final bar's
  brief-recorded red.

## 10. Reuse audit

The seam is `build_commit` in `tools/unattended/lib-unattended.sh`, called exactly as
`check-pass-order.sh`'s pre-anchor probe calls it, with that leg's `PREANCHOR_CAP` default. No new
library function and no new conf key.

Recall terms used: `brief-recorded build commit pick pre-anchor base repair unit built before run`.
