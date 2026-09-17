# cMendedVintage — the acceptance ledger for unit 14

**Serves:** journal DEPL-cMendedVintage-14

*Node `c`, 2026-09-17, written by the pass that built the unit. Every observation below was taken
against scratch fixture targets built under this run's scratchpad, never against a real tree. No
merge bar, no `*.test.sh` and no self-test suite ran in this pass; what ran was a throwaway driver
that builds the same fixtures the committed arm builds and invokes the real engine on them.*

## The three things worth reading twice

**The collision was observed as a LOSS, not as an exit code.** The fixture drives THREE rows into a
three-way conflict —

`tools/demo/one/conf.txt`

`tools/demo/two/conf.txt`

`tools/sib/conf.txt`

— all three named `conf.txt`. Against the engine at this commit's parent the outbox afterwards held
exactly ONE file, `update-conflict-conf.txt.md`, while the run exited 1 and named all three
conflicts on stderr. Two orders were overwritten by the third and nothing reported it. At this tip
the same fixture leaves three orders, each naming its own full path in its body. The arms assert the
BODIES and not the count, because a count alone would pass over an order whose content belongs to
another row.

**Both guards were staged RED before being called guards.** Each break was applied to a COPY of the
engine inside the scratch driver, never to the worktree.

- Scope guard neutered (`if kits:` to `if False:`): the scoped run deleted
  `update-conflict-tools-sib-conf-txt-*.md`, the only record that an out-of-scope row was still
  conflicted, having never classified that kit. Two arms went red. This is S4's silent data loss,
  reproduced.
- Glob widened to `update-*.md`: the run reported
  `reap: removed 2 stale conflict order(s)` naming two WITHDRAWAL orders, and the planted
  `update-rollback-demo.md`, `update-preexisting-red-demo.md` and `update-declined-red-demo.md` went
  with them. Four arms red. This is S5's distinction, reproduced.
- The collection set emptied (both `_orders_written.add` sites removed): the run deleted all three
  conflict orders in the SAME run that wrote them, with all three conflicts live —
  `reap: removed 3 stale conflict order(s)`. That is exactly the shape a read-only run presents, and
  it is why the write-only-ness is asserted structurally rather than trusted.

**S3's scoping is CONFIRMED and not assumed.** One file of every other order family was planted in a
fixture's outbox and an unscoped write run was driven over it:

`update-rollback-demo.md`

`update-preexisting-red-demo.md`

`update-declined-red-demo.md`

`demo-tools-demo-machine.md`

`hole-demo.md`

All five survived, and the run printed `reap: removed 0 stale conflict order(s)`. The last two are
the ones recorded in a receipt's `orders` list that `check` asserts against disk; reaping one would
red a target's own install check, and the glob cannot reach them.

**Evidences:** DEPL-cMendedVintage-14

- AC1 — OBSERVED. A scratch fixture was conflicted on three rows, the orders committed, then
  `tools/demo/one/conf.txt` was resolved to gov's own blob and committed, and the run

  `python tools/govkit/govkit.py update --target <fixture> --write`

  was repeated. Its order was gone, the other two stood, and the run printed
  `govkit update — reap: removed 1 stale conflict order(s): update-conflict-tools-demo-one-conf-txt-8be1d155.md`.
  The same run re-emitted the two still-open conflicts, which is the migration in miniature. The
  RED named in the criterion was reached by the emptied-set break above, which reaps on existence
  rather than on this run's set and takes the live orders with it.
- AC2 — OBSERVED. Two receipt rows sharing the basename `conf.txt` conflicted in one

  `python tools/govkit/govkit.py update --target <fixture> --write`

  run, and the outbox held two conflict orders naming `tools/demo/one/conf.txt` and
  `tools/demo/two/conf.txt` in their bodies. The criterion's RED is the measured one: the same
  fixture against `HEAD` left one file for three live conflicts.
- AC3 — OBSERVED. Its own fixture, because a withdrawn row is gone from gov's tree and cannot also
  conflict. Two rows sharing the basename `gone.txt` were withdrawn in one

  `python tools/govkit/govkit.py update --target <fixture> --write`

  run and the outbox held two withdrawal orders, each naming its own full path. Against `HEAD` the
  same fixture left one, `update-withdrawn-gone.txt.md` — so the withdrawal writer really was the
  third call site and re-keying only the two conflict writers would have been an instance fix.
- AC4 — OBSERVED. With a sibling kit's conflict order on disk, the run

  `python tools/govkit/govkit.py update --target <fixture> --write --kits <one-kit>`

  left every order untouched and printed one line:
  `govkit update — reap: SKIPPED, this run is scoped to 1 kit(s) and an order it did not write may belong to a row it never classified`.
  The criterion's RED was staged: with the scope guard neutered the out-of-scope order was deleted.
- AC5 — OBSERVED, in two forms, because the runtime form alone is nearly vacuous. Runtime: with a
  conflict order and a withdrawal order on disk,

  `python tools/govkit/govkit.py update --target <fixture>`

  with no `--write` left both. Structural: the reap carries no `if write:` guard, because the
  read-only branch RETURNS before the outbox is bound and a condition that cannot be false is the
  shape this engine bans. The committed arm asserts that ordering on the source — the last
  `if not write:` before the outbox bind returns, and `write` is never rebound — so the arm reds if
  that return ever moves. The criterion's RED was staged directly by emptying the collection set,
  which is the state a read-only run would arrive in.

## Owed

Nothing in this unit is observable against this repository: gov does not dogfood govkit and keeps no
receipt, so every criterion above needed a fixture and none of them has a home here.

- `govkit selftest` — OWED. The `[-14R]` arm is committed and was not run in this pass; no suite
  runs here. Its matchers were grounded individually against captured output from the live engine:
  the reap line spelling, the `withdrawn          [` row count of 2, and the structural AC5
  assertion, which was evaluated standalone against the committed source and holds. Its first cut
  did NOT hold — it keyed on the first of three `if not write:` occurrences and read a branch that
  never returns — and that was found and fixed by running the predicate rather than by reading it.
- `govkit selfcheck` — OWED. Nothing in this diff touches a descriptor, a planned destination or a
  reserved prefix.
- `govkit refusal join` — OWED, and §7's conditional raise of `BRANCH_PIN` is declined with a
  reason. Q3 resolved a failed unlink to a `print`, so this commit adds no refusal branch and
  removes none; the pin is a FLOOR that reds only when the count drops below it, so neither
  direction can red from this change.
- `govkit acceptance matrix` — OWED.
- The carried-prefix ban was checked by inspection rather than by running its gate, which this pass
  may not do. No new line in `tools/govkit/govkit.py` or in `WIRE-INTO-PROJECT.md` spells a kit-
  prefixed path at all. The new lines in `tools/govkit/selftest.py` spell only `tools/demo/` and
  `tools/sib/`, which are fixture-internal layouts and not kit ids — the same class every existing
  arm in that file already carries, and that file holds no row in the ban list.
