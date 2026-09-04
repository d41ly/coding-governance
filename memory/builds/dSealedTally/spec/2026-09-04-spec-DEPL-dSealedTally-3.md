# DEPL-dSealedTally-3 — the tracked-path check grades paths, excusing renames and withdrawals

**Status:** SPECCED · rev-1 · 2026-09-04 · node d · Tier-1 · base 0f19429a · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

`count_never_falls(before, after)` grades a TOTAL, so since `DEPL-dRatifiedSeam-1` relaxed it from
*unchanged* to *never falls*, deleting one tracked file and landing another satisfies it. Grade the
path SET instead, while still passing the two operations that legitimately remove a path: a rename
and a withdrawal.

## 2. Scope (IN)

- **S1** A predicate over path sets replaces the count comparison at its assertion sites in
  `tools/govkit/selftest.py`, taking the before set, the after set, and the paths this run
  legitimately removed.
- **S2** The legitimate-removal set is supplied by the fixture from what the run REPORTED it did —
  the rename destinations and the withdrawn rows in the receipt — never inferred from the
  difference it is grading.
- **S3** A staged-RED arm: a fixture that deletes one tracked file and lands another passes the old
  predicate and fails the new one.
- **S4** A mutation control that actually discriminates, checked against the two that did not in
  `dRatifiedSeam`: the control must make a legal rename look illegal, or an illegal swap look legal.

## 3. Non-goals (OUT)

- Not asserting `set(before) <= set(after)`. Measured on `tools/demo/content.txt`: it reds on a
  legal rename, and an assertion that fires on correct work teaches everyone to ignore the arm.
- Not changing `govkit.py`. This unit lives entirely in the self-test's predicate.
- Not removing `count_never_falls`. It stays as the standing count predicate where a count is what
  is meant; this unit adds the path-level one where a path is what is meant.

## 4. Design

### Data model

`paths_never_lost(before, after, excused)` returns `True` when `set(before) - set(after) <=
set(excused)`. Three arguments, and the third is the whole design: without it the predicate is the
rejected one, and with it inferred from the diff it is the vacuous one.

`excused` is assembled by the caller from two sources that both exist independently of the
comparison: the rename destinations the run reported, and the paths of the receipt rows the run
withdrew. Both are things the run SAID it did, which is what makes the predicate a check rather
than a restatement.

### Files touched (estimate)

`tools/govkit/selftest.py` (~60 lines: the predicate, its truth table, the staged-RED arm, and the
mutation control).

### Alternatives rejected

`set(before) <= set(after)`, proposed and measured during `dRatifiedSeam`'s closing review. It reds
on a legal rename because a rename removes the old path, and the `[-11]` fixture renames. Filed as
`DEPL-dRatifiedSeam-4` rather than built, and this unit is that filing being answered.

## 5. Production-readiness checklist

- security — N/A — a test predicate; it grades, it does not write.
- perf / scale — set operations over a fixture's file list; negligible.
- a11y — N/A — no rendered surface.
- i18n — N/A.
- error / empty / loading states — an empty `excused` reduces to the subset assertion, which is the
  strictest form and is correct when a run reports no removals.
- observability — a failure names the paths that vanished and were not excused, so the arm says
  WHICH file went missing rather than that a number moved.
- risks — the predicate's own failure mode is over-excusing. That is why `excused` comes from the
  run's report and never from the difference being graded.
- testing + left-shift gates — a truth table over the predicate plus S4's mutation control.
- migration / rollback — reverting the commit is the rollback.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When a fixture deletes one tracked file and lands another, `paths_never_lost` in
  `tools/govkit/selftest.py` returns `False` while `count_never_falls` returns `True`, so the two
  predicates are shown to differ on the case that motivated this unit.
- **AC2** — When the `[-11]` rename fixture runs, `paths_never_lost` returns `True`, proved by an
  arm in `tools/govkit/selftest.py` — the rejected `set(before) <= set(after)` returns `False` here.
- **AC3** — When a withdrawal removes a receipt row's path, `paths_never_lost` returns `True` with
  that path in `excused` and `False` with `excused` empty, so the argument is load-bearing.
- **AC4** — When the mutation control runs, removing the `excused` subtraction makes the AC2 arm
  FAIL, recorded as an observed break in `tools/govkit/selftest.py` rather than asserted.
- **AC5** — When `python tools/govkit/selftest.py` runs, it exits 0 with an arm count strictly
  greater than the 1074 it reports at base `0f19429a`.

## 7. Gates

`govkit selftest` · `memory-hygiene` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft; the rejected alternative is carried from `dRatifiedSeam`'s
  closing diff review, which measured it on `tools/demo/content.txt`.

## 10. Reuse audit

The seam is `count_never_falls` in `tools/govkit/selftest.py`, extracted by `DEPL-dRatifiedSeam-1`
precisely so a truth table could grade it, and this unit adds a sibling beside it rather than
rewriting it — the two answer different questions and both are wanted. No `reuse_lookup.py`
candidate ranked closer; its hits for the deploy-verification phrase were all in `govkit.py`, not
in the self-test's predicate layer.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
