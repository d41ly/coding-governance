# TOOL-aSwiftRefusal-2 — acceptance ledger

**Serves:** journal TOOL-aSwiftRefusal-2

Observed at the build tip 217827de6 on node a, 2026-11-10. Unless an answer says otherwise, the instruments are the spec's own §6 commands, run verbatim from the worktree root. BEFORE is the kit at base `ae6735c1` (units 1 to 3) or at `17308b6c` (unit 4), extracted with `git archive` to a short path outside the worktree.

The fixture criteria go through the driver suite's arms. They were observed GREEN in the attributed serial self-test run at the tip, 6f7d2089d, which shares 217827de6's tools tree. Driver shards 3 and 4 ran there with `NEW 0`, so no arm of this build failed. The owner stopped that run after 14 hours, at 11 of 27 suites, with the check-unattended suite never reached. The staged-break red observations were never run, so no arm was seen red at the close.

**Evidences:** TOOL-aSwiftRefusal-2
- AC1 — `check_unit_deferred` — run from `lib-unattended.sh`, where unit 4 moved it, over scratch files: 0 0 0
  for defer-only, dispatch-then-defer and defer then `ARCH-tRun-5`'s look-alike row; 1 1 1 1 for
  INPROGRESS, defer-then-dispatch, no row and `ARCH-tRun-44`'s row; 2 for a missing file. BEFORE: 127,
  the predicate absent.
- AC2 — `--dispatch tRun --pass ARCH-tRun-5` — the region-3 admission arm, green at the tip in shard 3.
  No red observed at the close.
- AC3 — `ARCH-tRun-4 (order 1, INPROGRESS)` — the region-3 blocker arm, green at the tip in shard 3.
- AC4 — `ARCH-tRun-4` — the DEFERRED-without-row blocker arm, `neither terminal nor dispatched`,, green at the tip in shard 3.
- AC5 — `consumes-from` — the edge-refusal arm, green at the tip in shard 3.
- AC6 — `grep -nE` — three `hit` assertions in `unattended.test.sh`: the admission line and both blockers.
- AC7 — `git show --format= <pass-sha>` — over 3e8557dc6, no removed line of `unattended.sh` carries `fail`.
