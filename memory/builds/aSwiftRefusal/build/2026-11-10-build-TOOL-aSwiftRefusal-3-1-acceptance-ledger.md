# TOOL-aSwiftRefusal-3 — acceptance ledger

**Serves:** journal TOOL-aSwiftRefusal-3

Observed at the build tip 217827de6 on node a, 2026-11-10. Unless an answer says otherwise, the instruments are the spec's own §6 commands, run verbatim from the worktree root. BEFORE is the kit at base `ae6735c1` (units 1 to 3) or at `17308b6c` (unit 4), extracted with `git archive` to a short path outside the worktree.

The fixture criteria go through the driver suite's arms. They were observed GREEN in the attributed serial self-test run at the tip, 6f7d2089d, which shares 217827de6's tools tree. Driver shards 3 and 4 ran there with `NEW 0`, so no arm of this build failed. The owner stopped that run after 14 hours, at 11 of 27 suites, with the check-unattended suite never reached. The staged-break red observations were never run, so no arm was seen red at the close.

**Evidences:** TOOL-aSwiftRefusal-3
- AC1 — `probe DEFERRED "$S/run-deferred.md"` — AFTER printed only `deadbeef TOOL-x-1 left out as deferred, so
  its declared paths reserve nothing until it is dispatched again: work/a`, the same with `current`.
  BEFORE printed the dispatch row and no deferred line.
- AC2 — `probe INPROGRESS "$S/run-deferred.md"` — the dispatch row ending `work/a`, no deferred line;
  `probe CLOSED` printed `left out as terminal (CLOSED)`, no deferred line.
- AC3 — `probe DEFERRED "$S/run-retaken.md"` — both rows, `deadbeef` work/a and `deadbee2` work/b, no
  deferred line.
- AC4 — `type read_open_passes` — 0 lines reading defer or dispatch rows, 1 call to `check_unit_deferred`.
- AC5 — `dispatched again` — the reader's header comment names the deferral (1) and the block comment
  carries `dispatched again` (1).
- AC6 — `A pass of a deferred unit, whose spec reads DEFERRED` — 1 in each copy (0 in the BEFORE template),
  and the `diff` printed nothing.
