# cMendedVintage — the acceptance ledger for unit 18

**Serves:** journal DEPL-cMendedVintage-18

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real engine against
scratch fixture targets at the shell — once with the unit unlanded and once with it landed — because
this repo keeps no receipt of its own and no criterion here is observable against it.*

## The one thing worth reading twice

**The defect is live and it was reproduced; the residue is in the INDEX, not the worktree.** The
brief and rev-1 both say the file stays on disk and nothing in the receipt claims it. Measured, on
the engine with this unit unlanded: the post-run receipt carried no row for the withdrawn path, the
worktree file was ABSENT, and `git ls-files` still named it — because the rollback's `update-index`
re-staged the pre-run blob and `checkout-index` only then refused. The loss is the same shape and it
lands one layer down. That matters for exactly one thing: S4's invariant as rev-1 wrote it quantified
over the worktree alone and would have stayed green over the defect this unit closes. It reads the
index too, and that is the half doing the work.

**rev-1's fixture technique does not reach the branch.** A directory planted at the withdrawn
worktree path is dirty against the index, and the claimed-path guard refuses the run before a byte
moves. Committing the directory instead takes the blob out of the index, which sends the rollback
down its `entry is None` branch, where the unlink is skipped for a non-file and the path is reported
RESTORED. `DEPL-cMendedVintage-2`'s own block already records the same measurement for its own path,
in the header two lines above the fixture rev-1 borrowed. The working technique is that unit's other
one: a `required` smudge filter installed by the kit's own check, in the window between the write and
the rollback.

**One statement moved, and it retired a second copy of itself.** The `attributes` branch carried its
own `withdrawn_rows` un-drop, below the same gate, for the same reason. Hoisting the removal above
the gate serves both branches, so the fix is a net deletion in the engine rather than an addition.

**Evidences:** DEPL-cMendedVintage-18

*Every token below sits on its own bullet's FIRST physical line where the form is OBSERVED, because
check 23 reads form from that line alone; the AMENDED bullets deliberately carry no backtick there,
which is what makes them AMENDED rather than OBSERVED.*

- AC1 — `--write-withdrawals` — on a scratch fixture whose withdrawn path the rollback could not
  restore, the post-run receipt carries `tools/demo/gone.txt` with the unit landed and does NOT carry
  it with the unit unlanded. Same fixture, same flags, two engines. Liveness on the same run: the
  verdict table printed `withdrawn`, the run printed the `checkout-index` refusal for that path, and
  `git ls-files` named it afterwards — so the arm graded a real withdrawal whose real restore really
  failed, over bytes the target really still held.
- AC2 — amended rev-2, logged at section 9 — the criterion asked for this run's field values "and
  not the pre-run ones", and the receipt cannot carry that distinction. Measured pre-run against
  post-run on the kept row: every one of the six `ROLLBACK_FIELDS` keys is unchanged, because the
  write loop appends a withdrawn row to the delete list and writes none of them. The one key the run
  does add is `carry`, which is not in that tuple. So hoisting the revert out with the removal would
  produce a byte-identical receipt and rev-1's red-when could not fire. The amended criterion asserts
  the equality, and the arm that checks it is written against the measurement.
- AC3 — `NOT restored` — the order for that run names the path under that verb and says this run
  WITHDREW it, that the rollback could not finish putting it back, and that its receipt row was KEPT
  rather than dropped. The rewrite branch's sentence appears nowhere in the file, which is the half
  that fails if the withdrawn case falls through to it.
- AC4 — amended rev-2, logged at section 9 — widened from "present in the worktree" to present in
  the target, worktree file OR staged index entry, for the reason at the top of this record. The
  predicate that ships was run standalone over two fixture targets before being inlined: it reds on
  the one the unlanded engine produced, naming the path absent from `files[]` and still in the index,
  and it passes on the one the landed engine produced. Its population is DISCOVERED — every rollback
  order under the suite's scratch root, and the paths that order itself names — so a new rollback arm
  is graded without being added to anything. Its execution over the SUITE's own arms is OWED below.

## OWED

- **The gate-side encoding of AC1 through AC4, and the cross-arm sweep's verdict over the existing
  arms.** The arms landed in this unit's write set are `[-18]` arms and only the govkit self-test
  suite can execute them. That suite is a merge-bar leg, no gate or bar ran in this pass, and the
  cross-arm sweep is by construction a statement about arms that only exist inside it. The four
  criteria were answered here by fixture targets built with the same builders those arms use, but
  the sweep's verdict over the suite's OWN rollback orders is unobserved and is owed to the bar the
  main loop runs once every unit is terminal. If it reds an arm nobody was thinking about, that is
  this unit's finding arriving late rather than a regression: the arms it grades all predate it.
- **No other unit's owed criterion is discharged here.** This unit found none open against it.
