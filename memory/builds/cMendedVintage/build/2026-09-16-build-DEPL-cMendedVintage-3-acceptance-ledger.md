# cMendedVintage — the acceptance ledger for unit 3

**Serves:** journal DEPL-cMendedVintage-3

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commits, `e1918d83` and `30352c6a`, both 2026-09-16.
Two kinds of line follow and they are not the same evidence. Where a criterion is answered by a
command or by a file, that command was replayed at the shell against this worktree and its result
is given, or the file was read at this tip. Where it is answered by what the building pass
measured, the commit that recorded it is cited AS the record and named as such. No merge bar, no
`*.test.sh` and no self-test runner ran in this pass: `tools/govkit/selftest.py` was READ, never
executed.*

## The one thing worth reading twice

**Two of this unit's five criteria are answered by a fixture arm that no record in this tree says
was ever run green.** The build commit records the RED half in detail — it names the fixture it
added, the refusal it staged and the three things it measured at BASE — and it records no green run
of the suite afterwards. The arms are committed and their assertions are quoted below, but an arm
sitting in a file is a claim about the future, not an observation, so those two lines say what the
commit actually recorded and stop there rather than borrowing the arm's confidence.

**The other three did not need the suite at all**, and that is a property of the criteria rather
than a convenience: AC3 is a grep over the engine, AC4 says in its own text that no arm observes it,
and AC5 is a claim about what the unit's diff changed. Each was taken directly here.

**Evidences:** DEPL-cMendedVintage-3

- AC1 — `.gitignore` in the `-ST2` mvkit fixture — the build commit `e1918d83` records the RED,
  taken against the real engine on the fixture that commit adds: the staging refusal fired by its
  own text, the destination was still an open gap, and its GAP line carried no reason while the
  reason printed three lines below. That is this criterion observed FALSE at BASE, which is what
  makes it falsifiable. The positive half is the committed arm `[-MV3] AC1` in
  `tools/govkit/selftest.py`, asserting `refused: git refused to stage it` on that same row — and
  no record in this tree says that suite was run after the fix. This pass did not run it either, so
  the green is unobserved and is owed at the run's close.
- AC2 — `_refused_new` — the residue branch and its exact wording were read at this tip in
  `tools/govkit/govkit.py`: a gap whose `dest` is absent from that list prints "no refusal reason
  was recorded for this destination in this run" and points at
  `govkit plan --coverage --emit-declines`, and it makes no claim about resolution in either
  direction. That is the source half, and it is the half the criterion's Red-when is about. The
  behavioural half — that `tools/mvkit/moved2.txt` really takes that branch on the `-ST2` fixture,
  being the one destination the rename machinery decided about without refusing — is the committed
  arm `[-MV3] AC2`, which nothing in this tree records running. Owed with AC1 and by the same
  unrun suite.
- AC3 — `grep -n 'does not exist yet' tools/govkit/govkit.py` — replayed at this tip from the repo
  root. No output, exit 1. Both carriers went in one commit, which is what this criterion asks: the
  clause left the `coverage:` tally's closing sentence, and the "IT REPORTS, IT DOES NOT LAND"
  paragraph that said the same thing left the comment ninety lines above it. The committed arm
  `[-MV3] AC3` reads the FILE rather than the printed output for exactly that reason, and an arm
  reading only output would have left the comment — the copy a reader reaches first — standing.
- AC4 — `except Exception as _ge` — graded STRUCTURALLY by reading `tools/govkit/govkit.py` at this
  tip, which is what the criterion itself says it gets and why: no fixture in the suite forces
  `coverage_rows` to raise, and the spec's rev-2 withdrew rev-1's claim that the `-11` escape
  fixture already forces this path. `_refused = dict(_refused_new)`, the annotated GAP loop and the
  `coverage:` tally all sit between the `try:` that opens the coverage block and the
  `except Exception as _ge` that prints the UNAVAILABLE line. Nothing this unit added sits outside
  that `try`, so a join that raises still degrades to UNAVAILABLE rather than failing the verb
  after bytes have landed.
- AC5 — `unclaimed sources:` — read off the diff of `e1918d83`, which is the whole of what this
  criterion asks, because it is a claim about what the unit CHANGED rather than about a run. In
  that diff the `coverage:` print's two count expressions are context and unchanged; only its
  trailing clause moves. The line computing the open-gap list is context too, so the join annotates
  the existing loop and filters nothing. The `unclaimed sources:` tally does not appear in the diff
  at all. The committed arm `[-MV3] AC5` asserts both counts behaviourally on the fixture; it was
  not run here and is not what answers this line.

## What this ledger does NOT claim

That the merge bar is green, or that any leg of it ran. None did, in the building pass or in this
one. `govkit selftest` is the leg that owns the four `[-MV3]` arms this unit added, and it is
unobserved for this unit end to end.

That the fixture's green was ever seen. It is stated twice above because it is the substantive gap
here: the building pass recorded its RED with unusual care and recorded nothing after it. A later
pass that runs `govkit selftest` clean over this tree discharges AC1 and AC2 and should say so
here rather than in a commit message.

That `30352c6a` is graded by any criterion. It deletes a count from a comment this unit had just
written, after `gotchas.py --for-diff` named the class on the diff. No criterion covers it, it
changes no behaviour, and it is named here so the unit's second commit is not silently absent from
its own record.
