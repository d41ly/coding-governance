# cMendedVintage — the acceptance ledger for unit 27

**Serves:** journal DEPL-cMendedVintage-27

*Node `c`, 2026-09-19, written by the pass that built the unit. No merge bar, no `*.test.sh` suite
and no run of the deployer's own selftest program ran in this pass — the pass's own directive holds
that over the brief, which asked for the suite. Every criterion below was answered by replaying its
own arm OUTSIDE the suite against scratch fixture targets under this run's scratchpad, in the shape
the permanent arms use; the command is stated per criterion. Every arm was run against TWO engines —
this unit's parent `eff7a08f` and the blob that shipped here — so each failing case was observed
before it was observed fixed.*

## Which of the nine `[-PV]` arms this unit makes green, stated before anything else

**All nine, and that is not the same answer as "force all nine green".** The brief warns that
forcing them re-breaks what `DEPL-cMendedVintage-19` fixed. It would, if the repair were a revert of
the un-gating — and the measurement that says this one is not is that the existing role-move arms,
the ones built for `-19`'s own transition, pass UNCHANGED under both engines. A move to
`project-owned` still stands back, still writes nothing, still re-stamps nothing, and a schema-1
receipt carrying the same disagreement still refuses. What moved is a different population: the rows
whose new role is served by the kit's own regenerate.

**The two `PRECONDITION` arms are un-flipped deliberately, and the fixture header's prediction is
not repudiated — its premise is.** That header records that the pair flips when the durable repair
lands AND the migration retires with it. Section 8's Q1 refuses the retirement in this unit, so the
runbook still ships, and a precondition asserting the state a live runbook starts from has to hold
for exactly as long as that runbook does. They flip in the unit that retires it. The direct replay of
that precondition is AC2 below: after `update` alone, the target's index holds gov's own render for
the moved row. It was RED under the parent engine and green under this one.

## The spec asked for a state the fixture makes impossible, again

rev-1's AC1 ended "and the file on disk is the target's own". Measured at both vintages: the kit's
declared regenerate runs after the row is graded and puts its own render in the WORKTREE either way,
so that clause is green before the fix and green after it — it grades nothing. What this unit
actually moves is the git directory and the run's account of itself: gov writes nothing for a
conflicted row so the index entry is untouched, and the run now refuses, names the path and the
three-way conflict, and leaves one order, where the parent engine exited 0 having said nothing at
all. rev-2 rewrites the criterion onto those three and records the worktree overwrite as the standing
ceiling the third non-goal already declines to close. The permanent arm asserts that ceiling
explicitly and labels it as one, because an arm green at both vintages certifies nothing and is worse
unlabelled.

Section 4's `touched_kits` paragraph was wrong the same way and cost a fixture. It named the
template's landing as what puts the kit in the run's touched set; it does not — the template arrives
as the `rendered` rule's own source, which is neither an acted row nor a landed one. A fixture built
on that claim ran no regenerate at all under the parent engine, so the row stood back AND nothing
overwrote it, and the byte loss the goal describes never happened. The fixture now moves a second row
of the same kit, which is the real shape of a vintage that re-roles a destination, and under the
parent engine it reproduces the loss.

## What was NOT done, and why it is not tidiness

No arm was added to the deployer's own selftest program. The brief is right that `b52b5d80` touched
that file not at all and that the suite carries nothing tagged for `-19` — but the suite was not
silent about it: nine arms went red, in the one place that drives this transition end to end. The
evidence for `-19` went into the acceptance matrix, and this unit's goes beside it, in the same
function, as the pair that function has never carried. A third copy in a third program would be a
third answer to one question.

No refusal against the regenerate, and no gate on the worktree overwrite. Both are the third
non-goal. Declining a kit's declared argv over a moved row removes the conflict path instead of
restoring it, which is the state this unit exists to leave.

**Evidences:** DEPL-cMendedVintage-27

- AC1 — `python tools/govkit/govkit.py update --target <fixture> --write` against a scratch target
  whose aged schema-3 receipt rows a destination `engine`, whose gov now serves that destination from
  a `rendered` rule with a declared regenerate, and whose own committed copy conflicts with gov's
  bytes at the new vintage. Under this engine the run exits non-zero, one line names that path and
  `diverged and the three-way conflicts`, exactly one conflict order is written for it, and the
  adopter's bytes stand byte for byte in the git directory. Under the parent engine the run exits 0,
  reports `role-moved`, writes no order and names nothing, while the regenerate overwrites the
  worktree copy — the shipped defect, reproduced before the fix existed. rev-2 records why the
  criterion could not be written as rev-1 wrote it.
- AC2 — `python tools/govkit/govkit.py update --target <fixture> --write` against the same recipe
  built with no local edit. Under this engine the row grades `stale`, takes the recorded role's raw
  write, and the target's INDEX holds gov's second-vintage bytes afterwards. Under the parent engine
  the row stands back and the index still holds the first vintage. This is the direct replay of the
  two `PRECONDITION` arms named above: it is the same assertion about the same transition, made
  outside the runbook.
- AC3 — `python tools/govkit/govkit.py update --target <fixture> --write` on the AC2 run, asserted
  over its printed lines. Exactly one line both opens with two spaces and ends with that row's path,
  and a further line — off the row channel, through `Report.note` — names the role the row landed
  under, the role gov declares now and the path. The criterion's red-when is closed by construction:
  the count is asserted as `== 1`, so a move reported as a second row line reds here rather than
  shadowing the verdict for every reader keying on the path suffix.
- AC4 — `role-moved` over the existing aged fixture whose destination moved to `project-owned`, run
  directly as the acceptance matrix's own role-move arm rather than through any suite. The moved row
  still reports that verdict, gov does not put its bytes back at the destination the adopter emptied,
  the write tally reads zero, and not one field of the receipt row is rewritten. Every one of those
  arms passes under BOTH engines, which is the measurement that separates this repair from a revert
  of `DEPL-cMendedVintage-19`.
- AC5 — `python tools/govkit/govkit.py selfcheck` over a copy of this tree with the new declared set
  staged to a value the dispatch maps no role to. The staged run exits non-zero and names that member
  on its own line; unstaging it in the same copy leaves the run one problem shorter with that line
  gone, so the copy's own unrelated problems are not what the criterion is reading. Unstaged at this
  repository's root the verb exits 0. The break is staged into the DECLARATION and not into the guard
  that reads it, so the guard is not being tested against itself.

## What is OWED

- **Every `[-PV]` arm's verdict INSIDE the suite is OWED**, all nine of them, and so is the acceptance
  matrix's own verdict on the pair added here. They were replayed OUTSIDE the suite in this pass,
  against fixtures built by the recipe the permanent arms use, and all held.
- **The full selftest program is NOT run in this pass and no red count is reported from it.** The
  pass's directive forbids running a self-test suite inside a unit and overrides the brief; the
  program also takes about 33 minutes, which is past this pass's command bound, and a run straddling
  this unit's own commit would grade two engines. It is the main loop's owed bar. The number to beat
  is the one the attribution recorded, less what `DEPL-cMendedVintage-26` returns, less these nine.
- Nothing else. No criterion here needed a gate, a merge bar or a `*.test.sh` to observe.

## What this unit did NOT fix, deliberately

A kit's declared regenerate still overwrites the worktree copy of a destination whose row this run
refused to reconcile. Gov's half now refuses, names the row and writes an order, so the operator has
both a record and their own committed bytes — but the file under their editor is the render, and
nothing puts it back. That is the same ceiling `DEPL-cMendedVintage-24` recorded one unit over for
uncommitted work at a destination gov does not track, it is the third non-goal here, and closing it
means deciding what an `update` owes a destination it declined to write. The arm states it rather
than leaving a reader to discover it.

The harness migration still ships and still has to be run by hand. Section 8's Q1 recommends against
retiring it here and the recommendation stands: those arms are the only end-to-end exercise of a
scoped `update` through a consumer's own commit hooks, and the retirement owes a replacement for that
coverage before it lands.
