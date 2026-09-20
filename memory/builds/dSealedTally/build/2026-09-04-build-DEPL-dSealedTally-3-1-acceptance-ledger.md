# Acceptance ledger — DEPL-dSealedTally-3

**Serves:** journal DEPL-dSealedTally-3

Tier-1 · node d · 2026-09-04

## What changed, and what the scope turned out to be

`paths_never_lost(before, after, excused)` joins `count_never_falls` in `tools/govkit/govkit.py`,
and the standing assertion site in the suite now calls it.

**The scope was narrower than the spec implied.** rev-2 said "the assertion sites"; there is exactly
ONE site that grades the standing never-falls property. The other two tracked-file count assertions
test specific DIRECTIONS — a landing raising the total by one, a withdrawal lowering it — and
replacing those would have broken checks that are correct. The sites were counted rather than
assumed: `grep -nE "_files_before|_files_pre|_files_post|_files_after"` returns four assertion
lines, one standing predicate and three direction checks.

**The third argument is the whole design, and its direction is load-bearing.** `excused` holds the
paths a run legitimately removed, sourced from what the run REPORTED — its `renamed` verdict lines,
which carry the row's OLD path. Not from the difference being graded, which would make the predicate
a restatement of its own input.

The rejected alternative is recorded in the function's own docstring so it is not re-proposed:
`set(before) <= set(after)` reds on a legal rename, because a rename removes the old path and the
subset never holds for a run that moved anything.

## The criteria

**Evidences:** DEPL-dSealedTally-3

- AC1 — MET, OBSERVED — `python tools/govkit/selftest.py` asserts a delete-one-land-one pair
  returns `False` from `paths_never_lost` while `count_never_falls` returns `True` on it. The
  second half is what shows the unit has a reason to exist.
- AC2 — MET, OBSERVED — the `[-11]` rename fixture passes with its old paths excused, and a
  companion arm in `tools/govkit/selftest.py` asserts the rejected `set(before) <= set(after)` still
  reds on that same pair, so the record of why it was rejected cannot go stale silently.
- AC3 — MET, OBSERVED in `tools/govkit/selftest.py` — a withdrawn path is excused when named and
  NOT excused when the set is empty — asserted both ways, so the argument is load-bearing rather
  than decorative.
- AC4 — MET, OBSERVED BY STAGED BREAK — dropping the `excused` subtraction in
  `tools/govkit/govkit.py` reds four arms, including the REAL `[-11]` site with its nine reported
  renames. A second mutation returning `True` unconditionally reds four DIFFERENT arms. The two sets
  are complementary: one kills the should-pass arms, the other the should-fail arms, and neither
  produced any unrelated failure.
- AC5 — NOT MET AS WRITTEN — no fixture in `tools/govkit/selftest.py` performs a real
  delete-one-land-one run through the
  assertion site; the case is graded by table only. What IS observed is that the site calls the
  shipped predicate and its verdict matters, because mutation A redded that site. That is adjacent
  to AC5 rather than equal to it, and is recorded as such.
- AC6 — MET, OBSERVED — excusing the rename DESTINATION instead of its pre-rename path still
  reds, proved by an arm in `tools/govkit/selftest.py`. This is the defect rev-1 of the spec
  shipped, and it is now unfalsifiable-proof.
- AC7 — MET — `python tools/govkit/selftest.py` exits 0 at **1110 arms**, ten more than the 1100 at
  the head of `order 3`, against a spec floor of five.

## Two arms exist only to stop this becoming decorative

A LIVENESS arm asserts the `[-11]` run really reported renames; without it, an empty excused set
would make the predicate grade nothing it was written for and still pass. And an AC4 LIVENESS arm
asserts the truth table produces BOTH verdicts — it reds under both mutations, which is correct,
because a single-valued table proves nothing whichever value it holds.

That second arm is the direct descendant of `count_never_falls`'s own history: its predecessor was
"armed" by an arm that re-implemented the comparison in the test and was a tautology. A copy of a
predicate grades the copy.

## Residue

AC5's real-run fixture. Building it means a gov vintage that both withdraws a tracked source and
ships a new one in the same update, which is a fixture shape this suite does not have. The table
covers the predicate; nothing covers the site's behaviour on that specific state.
