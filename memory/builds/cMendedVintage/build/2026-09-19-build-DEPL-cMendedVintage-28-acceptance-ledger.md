# cMendedVintage — the acceptance ledger for unit 28

**Serves:** journal DEPL-cMendedVintage-28

*Node `c`, 2026-09-19, written by the pass that built the unit. No merge bar, no `*.test.sh` suite
and no run of the deployer's own selftest program ran in this pass — the pass's own directive holds
that over the brief. Every criterion below was answered by replaying its own arm OUTSIDE the suite
against scratch fixture targets under this run's scratchpad, built by the recipe the permanent arms
use. Every arm was run against TWO engines — the parent blob at `aca91cea`, exec'd in process with
its `__file__` left pointing at the real engine, and the blob that shipped here — so each failing
case was observed before it was observed fixed.*

## The collision needs a precondition the spec's table left out, and it decides which arms are red

The untracked-shadow predicate tests index membership AND presence on disk. An escaping path is in no
index by construction, but it is only PRESENT where something put bytes there. So the shipped engine
answered the CREATION fixture with the containment refusal all along — nothing exists outside that
target, which is that fixture's whole assertion — and the collision reaches the WITHDRAWAL fixture,
which writes real bytes at the escaping path to prove the splice destroys them.

Both red arms are therefore the withdrawal branch's, and the second one is the sharper find. One
asserts the refusal names containment; it got the shadow wording. The other is the liveness arm that
proves the fixture reaches the splice at all — and it could not, because staging the containment call
out left the shadow refusal answering in its place. An arm that reproduces the defect was reproducing
a different refusal. rev-2 records both.

## What the fix is, and what it deliberately is not

One call to the containment helper the engine already owns, in the preamble, over the SAME derived
row population the shadow refusal grades, placed above it. No new refusal text, no second predicate,
no narrowing of the shadow population — `DEPL-cMendedVintage-24`'s widening exists because gov was
staging an operator's uncommitted attributes file on every run and destroying it in the rollback, and
AC2 is the arm written against undoing that.

`DEPL-cMendedVintage-23` argued a receipt-wide preamble guard out, on the ground that a row whose
role is not landable may legitimately name a destination outside the target. That argument holds and
is not overturned: it does not reach this population, whose members are the rows a writing
disposition puts gov's bytes at, and one of those escaping is a defect by definition. The comment
carrying the old argument is corrected in place rather than deleted, and the pins arm's own call
stays — it is the one that survives a `--kits` narrowing of the preamble's list.

**Evidences:** DEPL-cMendedVintage-28

- AC1 — `update --write` against a scratch target whose receipt rows the attributes destination one
  level above its own root, with real bytes at that path. Under this engine the run refuses naming
  `leaves the target repository`, names the receipt row that supplied it, and those bytes are
  byte-identical afterwards. Under the parent engine the same fixture takes the untracked-shadow
  wording instead — the shipped defect, reproduced before the fix. rev-2 adds the bytes-exist
  precondition, without which the shadow predicate does not match and the criterion grades nothing.
- AC2 — `update --write` against a graded target whose `.gitattributes` was left on disk and taken
  out of the index with `git rm --cached`. The run refuses with the untracked-shadow wording naming
  that path, the containment message is absent, and the operator's bytes are untouched. Identical
  under both engines, which is the measurement that separates this reorder from a narrowing of the
  population `DEPL-cMendedVintage-24` widened. Taken a second way, because a refusal arm alone does
  not prove the ordinary path is unmoved: an ORDINARY run over a freshly applied target, once scoped
  to one kit and once unscoped, produces output that is byte-identical between the two engines with
  the target path folded out. Nothing this unit adds can refuse a row the shadow test would not have
  graded, because both read the same derivation over the same list.
- AC3 — `govkit:lf-pins` and its sentinel line, asserted byte for byte on the withdrawal fixture
  AND joined to the containment message in the same condition, so the arm can no longer be satisfied
  by a refusal that never reached the branch it grades. Measured both ways under the parent engine:
  the bytes-only form passes there, which is the skip wearing a pass; the same arm with the reach
  clause fails there and passes here.
- AC4 — `demand_contained_dest` staged out of the preamble alone, through the liveness helper's new
  staging parameter, against the same withdrawal fixture. The run is then answered by the
  untracked-shadow refusal, which the arm asserts by name, together with the impossible remedy it
  offers — confirmed against git directly, which answers that the path is outside the repository.
  Staging that call out is what makes the shipped arms above red, naming the guard that answered in
  their own detail, so the order is observed rather than asserted by the spec.

## What is OWED

- **Every one of these arms' verdicts INSIDE the deployer's own selftest program is OWED**, including
  the ordering arm added here and the two arms this unit returns to green. They were replayed outside
  the suite against fixtures built by the recipe the permanent arms use, against both engines.
- **The merge bar is OWED**, and with it the `govkit acceptance matrix` and `govkit refusal join`
  legs. Two checks the bar wraps were run DIRECTLY in this pass and both are reported above:
  `govkit selfcheck` exits 0 and its structural probe reports no ungraded root-join write on a
  receipt-supplied value. The refusal-branch floor is shrink-only and this unit adds a call rather
  than a `raise`, so no branch count moves and nothing there needed re-deriving.
- Nothing else. No criterion here needed a gate or a `*.test.sh` to observe.

## One red left standing, and it is not this unit's

`check_runbook_parity.py` exits 1 at this repository's root with eighteen problems, every one of them
a registry entry with no anchored runbook section. It reports the same anchor count against the
runbook at `aca91cea` as against the one this unit edited, so the red predates this pass and the
sentence added here neither helps nor hurts it. Named rather than fixed: closing it means writing
eighteen runbook sections, which is a build and not a line.
