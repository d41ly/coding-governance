# TOOL-aSwiftRefusal-4 — acceptance ledger

**Serves:** journal TOOL-aSwiftRefusal-4

Observed at the build tip 217827de6 on node a, 2026-11-10. Unless an answer says otherwise, the instruments are the spec's own §6 commands, run verbatim from the worktree root. BEFORE is the kit at base `ae6735c1` (units 1 to 3) or at `17308b6c` (unit 4), extracted with `git archive` to a short path outside the worktree.

The fixture criteria go through the driver suite's arms. They were observed GREEN in the attributed serial self-test run at the tip, 6f7d2089d, which shares 217827de6's tools tree. Driver shards 3 and 4 ran there with `NEW 0`, so no arm of this build failed. The owner stopped that run after 14 hours, at 11 of 27 suites, with the check-unattended suite never reached. The staged-break red observations were never run, so no arm was seen red at the close.

**Evidences:** TOOL-aSwiftRefusal-4
- AC1 — `rescope` — AFTER after `seed`: `amendment recorded — defer ARCH-x-1`, count 2; a second call
  `amendment already recorded, unchanged`, count 2. BEFORE: `amendment already recorded, unchanged` on the
  first call, count 1, which is the red.
- AC2 — `check_unit_deferred` — defined once in the library and 0 times in the driver; `lib DEFERRED` rc=1
  after `seed`, rc=0 after the appended defer row, `lib INPROGRESS` rc=1; BEFORE rc=127; the driver's
  `type check_unit_deferred` exits 0.
- AC3 — `check 23 released ` — 1 and 1 at the tip, 0 and 0 in BEFORE. The end-to-end M4 block in the
  check-unattended suite was NOT observed, green or red: the stopped run never reached that suite.
- AC4 — `FLOOR_ASSERTIONS=3287` — the floors read 3287, 416, 403, 1152 and 227; the RAISED counts 3 and 1;
  region 3's group 11 assertions; M1, M3 and M4 5, 5 and 10.
- AC5 — `check_commit_message` — its comment block names `deferred` (2; 0 in BEFORE), and its body calls
  `check_unit_deferred` 0 times.
- AC6 — `whose spec is neither terminal nor deferred` — 1 in each copy (0 in the BEFORE template), and the
  `diff` printed nothing.
