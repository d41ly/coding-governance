# cMendedVintage — the acceptance ledger for unit 19

**Serves:** journal DEPL-cMendedVintage-19

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every line below was taken by calling the new arm's own function
directly against a scratch fixture, once with the engine as this tree leaves it and once with the
engine as `b1621f59` had it.*

## The one thing worth reading twice

**The criterion's own Red-when was not reachable by the fixture the criterion described, and the arm
as first written stayed green over the defect it exists to close.** AC2 said the moved row "is
restored from gov's bytes over the target's own copy" when the guard is left in place. It is not: a
destination the adopter edited IN PLACE grids to `patched`, and `patched` writes nothing at BASE
either. Measured, not reasoned — the first fixture ran against the BASE engine and reported `wrote 0`
and unchanged bytes, which is the same observation the fixed engine gives. The restore needs an
ABSENT destination: a path the adopter renamed away grids to `missing`, which is a raw-write verdict,
and at BASE gov writes its own bytes back over a path the adopter deliberately emptied. The arm
carries both destinations now. Against the BASE engine it fails six arms including that one; against
this tree's engine all sixteen hold. AC2 is recorded AMENDED for that reason and the change is
logged at spec rev-2.

**The refusal floor is DECLINED, with the measurement rather than an argument.** `BRANCH_PIN` stays
at 255: read off `refusal_join.py`'s own `enumerate_branches` at both ends, 255 at base `b1621f59`
and 255 on this tree. The branch split adds a REPORT and no refusal, so the population it floors did
not move, and raising a shrink-only pin over an unmoved population asserts a relation that is false.

**Evidences:** DEPL-cMendedVintage-19

- AC1 — `govkit.py update --target` run against the aged fixture, the CONTROL row. The fixture's
  third destination is claimed by no carve-out, so its recorded role and its current resolution
  still agree; it reports `current` on this tree's engine, which is byte-for-byte what it reports
  against the BASE engine on the same fixture. Both runs were taken. The un-gated re-resolution
  therefore moves no row that did not move, which is the whole of what this criterion asks.
- AC2 — amended rev-2 — the criterion's Red-when named a restore an edited-in-place row cannot
  reach, so the fixture gained a second moved destination the adopter had RENAMED AWAY. Both are
  asserted: the edited one reports `role-moved` and its bytes are byte-identical afterwards, and the
  emptied one reports `role-moved` and is NOT put back. Against the BASE engine the second is
  restored and the arm reds. The printed row names the role the row landed under, the role the
  descriptor declares now and the path, in that order, with the path as its last field.
- AC3 — `install.json`, read before the run and after it, whose moved row still carries
  `role = "engine"` and is equal field for field to the row the install wrote. The run's own tally
  reads `wrote 0, moved 0, deleted 0`, so the row was counted as no change as well as written for
  as none.
- AC4 — `govkit.py update --target` over a second fixture identical but for a receipt aged back to
  schema 1. It still refuses, with the message ending "a role a schema-1 receipt cannot be trusted
  about", and the moved row does NOT take the reporting path. The two branches are two.

## What did not run, and why

`govkit acceptance matrix` is OWED. The arm is wired into that gate's `main`, and the four criteria
above were answered by calling the arm's function directly rather than by running the gate, which
this pass is not permitted to do. `govkit selftest`, `govkit selfcheck` and `govkit refusal join` are
owed on the same terms; the refusal-join figure above was taken by calling that module's own
enumerator, not by running its gate.

The engine change also moves a descriptor resolution onto every row of every run where it used to sit
only on a schema-1 receipt's. It is memoised per kit inside the verb, which §5's risks paragraph
named as the local answer if the reading found it costly. No timing was taken against a
ninety-row target, because no such target exists in this tree to take it against.
