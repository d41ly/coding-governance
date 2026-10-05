**Serves:** journal TOOL-aGraftedHelix-34

# Spec brief — TOOL-aGraftedHelix-34, adopted mid-run

Tier-2, streams tooling, `order 18`. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states the twelve invariants that bind it.
In your OWN return, name the spec you author in `authored` by its unit id, `TOOL-aGraftedHelix-34`,
never by its path.

## What was observed

The owed unattended suites ran ONCE, pooled, on a frozen clone at `90a6f6fae` — the tree as it
stood before the rotation, so before units 29 to 33, the check-wiring fix and the latest reconciling
merge. The sweep finished RED: 20 suites, 11 MISMATCH, 1 killed. Two kinds of row are in that count
and must not be confused.

**Count-only MISMATCHes** (rc 0, 0 FAIL, more arms executed than the calibrated baseline): adopter
e2e, gate shards 2 to 5, stall-recorder and stop-guard (both of which had a recorded 1-FAIL baseline
and now read 0). These are new arms from this build and the merges, not defects; they want a
`--calibrate`, which the close takes, not this unit.

**Real reds** — every failing arm, verbatim from the frozen clone's
`.git/gate-logs/selftests/*.out` (the sweep summary truncates to a few per suite):

- driver selftest (12): `missing: closing-review-recorded` · `S4 rule 1 does NOT fire on a copy
  with verb_close's stage removed` · `the driver has 8 phase writer(s); this arm drives 6 of them and
  the rotation arm below drives the seventh` · `missing: the project conf at the default-branch side
  of the pinned BASE could not be evaluated to the end` · `missing: specs-audited — not gradable …` ·
  `AC3 an unanswering remote exits 2: expected [2], got [0]` · `missing: the claims on the remote
  could not be read …` · `missing: a process this slug's driver started is still alive, and a hold
  now would …` · `AC6 the refused hold wrote nothing to the record` · `missing: phase HELD · code
  platform-limit` · `missing: unattended: the process ledger is KEPT …` · `AC12 --abort removed a
  ledger that still names a live process`.
- cross-component (1): `arm 3b: the leg is silent over what the driver produced`, which got a
  `check 23 fleet — 0 undeclared write(s) …` line.
- gate shard 1/8 (1): `a dispatched verb is absent from a surface an agent reads`, naming
  `--highs` and `--minors` in usage and in refusal.
- gate shard 8/8: killed at its 6260 s evidence bound after printing `fixture no-op on
  tools/unattended/unattended.sh: s|^  if \[ -f "$rel" \] \&\& is_terminal "$DP_PHASE"; then$|…`, the
  G0 fixture failure that follows from it, and three `may:`-grant arms.
- resume-tick (2): `AC4 the sleep is gone from tasklist` · `AC13 the hung launched pid is gone from
  tasklist`.

## What to decide

For EACH real red, decide one of three, and say which in §4 with the evidence:

1. **Already fixed at HEAD** — a later unit or merge moved the code; prove it with a slice of that
   arm against HEAD, green.
2. **Ours** — this build (or one of its reconciling merges) caused it: fix the product or the
   fixture, whichever the arm shows is wrong. A fixture that greps a driver line this build rewrote
   is a stale fixture, and its fix routes through the suite's mutate helper. Observe each fixed arm
   red under the break it guards, then green.
3. **Inherited** — origin/main reds the same arm on its own: prove it on a worktree at
   `origin/main` with the same slice, and record it, without fixing what is not ours.

Slice, never re-run a whole suite: prologue plus the one block, in a temp script inside the kit
dir, deleted after (the driver suite ran 17142 s pooled). The resume-tick pair touches real
processes through `tasklist`; first decide whether it is contention under an 8-wide pool, by
slicing it alone. Shard 8's timeout follows from its fixture no-op; say whether the fixed fixture
lets the shard finish inside its bound, from a slice, never from a whole-shard run.
