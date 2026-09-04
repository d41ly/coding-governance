# DEPL-dSealedTally-3 — the tracked-path check grades paths, excusing renames and withdrawals

**Status:** CLOSED · rev-2 · 2026-09-04 · node d · Tier-1 · base 0f19429a · streams deployer · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-DEPL-dSealedTally-3-1-acceptance-ledger.md](../build/2026-09-04-build-DEPL-dSealedTally-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round1.md) | diff-review | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md) | spec-audit | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

`count_never_falls(before, after)` grades a TOTAL, so since `DEPL-dRatifiedSeam-1` relaxed it from
*unchanged* to *never falls*, deleting one tracked file and landing another satisfies it. Grade the
path SET instead, while still passing the two operations that legitimately remove a path: a rename
and a withdrawal.

## 2. Scope (IN)

- **S1** A predicate over path sets replaces the count comparison at the assertion sites in
  `tools/govkit/selftest.py` that grade a tracked-file population after an `update --write`,
  taking the before set, the after set, and the paths this run legitimately removed. The sites
  are enumerated in the pass's own commit message; every OTHER caller of `count_never_falls`
  keeps it, which is what §3's third non-goal means.
- **S2** The legitimate-removal set holds PRE-RENAME paths: each renamed receipt row's path as it
  stood BEFORE the run, plus the withdrawn rows' paths. A rename removes the OLD path, so the
  destination — which is what rev-1 said — excuses nothing. Both are read from the receipt taken
  BEFORE the run, or from the run's own rename verdict lines, never from the difference being
  graded: the post-run receipt carries only destinations and has withdrawn rows stripped out.
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

`excused` holds PRE-RENAME paths and withdrawn paths. That direction is load-bearing and rev-1
had it backwards: the set is subtracted from `before - after`, and what leaves `before` on a
rename is the OLD path. Excusing the destination excuses a path that was never lost, so the
predicate would still red on the `[-11]` fixture — the exact failure that made
`set(before) <= set(after)` unusable.

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
- **AC5** — When the delete-one-land-one fixture is driven through one of S1's named assertion
  sites, that site REDS where at base `0f19429a` it passes, proved in `tools/govkit/selftest.py`
  — without this, the predicate could be correct and reach no caller.
- **AC6** — When `paths_never_lost` is given a rename's DESTINATION as `excused` instead of its
  pre-rename path, the `[-11]` fixture REDS, proving the direction in S2 is the load-bearing one.
- **AC7** — When `python tools/govkit/selftest.py` runs, it exits 0 and its arm count is at
  least 5 greater than the count observed at the head of `order 3`, captured in §9 when this
  unit's pass opens.

## 7. Gates

`govkit selftest` · `memory-hygiene` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft; the rejected alternative is carried from `dRatifiedSeam`'s
  closing diff review, which measured it on `tools/demo/content.txt`.
- rev-2 · 2026-09-04 · folded the spec audit's H2, H9, H5 and M1. H9 is the one that mattered:
  rev-1 put the rename's DESTINATION in `excused`, and the set is subtracted from
  `before - after`, so it excused a path that was never lost and the predicate would still have
  redded on the `[-11]` rename — the exact defect that disqualified the rejected alternative. S2,
  the Data model and AC6 now carry the pre-rename direction. H2 added AC5, since rev-1 could have
  shipped a correct predicate that no assertion site called. H5 replaced the shared arm-count
  constant with a delta. M1 moved the order from 2 to 4 so this unit no longer shares a parallel
  step with `DEPL-dSealedTally-1` over `tools/govkit/selftest.py`.

## 10. Reuse audit

The seam is `count_never_falls` in `tools/govkit/selftest.py`, extracted by `DEPL-dRatifiedSeam-1`
precisely so a truth table could grade it, and this unit adds a sibling beside it rather than
rewriting it — the two answer different questions and both are wanted. No `reuse_lookup.py`
candidate ranked closer; its hits for the deploy-verification phrase were all in `govkit.py`, not
in the self-test's predicate layer.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
