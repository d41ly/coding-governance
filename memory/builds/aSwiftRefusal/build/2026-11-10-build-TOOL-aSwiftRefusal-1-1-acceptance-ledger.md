# TOOL-aSwiftRefusal-1 — acceptance ledger

**Serves:** journal TOOL-aSwiftRefusal-1

Observed at the build tip 217827de6 on node a, 2026-11-10. Unless an answer says otherwise, the instruments are the spec's own §6 commands, run verbatim from the worktree root. BEFORE is the kit at base `ae6735c1` (units 1 to 3) or at `17308b6c` (unit 4), extracted with `git archive` to a short path outside the worktree.

The fixture criteria go through the driver suite's arms. They were observed GREEN in the attributed serial self-test run at the tip, 6f7d2089d, which shares 217827de6's tools tree. Driver shards 3 and 4 ran there with `NEW 0`, so no arm of this build failed. The owner stopped that run after 14 hours, at 11 of 27 suites, with the check-unattended suite never reached. The staged-break red observations were never run, so no arm was seen red at the close.

**Evidences:** TOOL-aSwiftRefusal-1
- AC1 — `grep -nF` — after: checker 14653, order gate 14378, condition 1 14627, claim read 14696; the
  checker sits between them. BEFORE: checker 14329, above the order gate at 14383, which is the red.
- AC2 — `neither terminal nor dispatched: ARCH-tRun-4` — the driver suite's region-3 arm, green at the tip
  in shard 3. No red observed at the close.
- AC3 — `two passes claiming one file are not disjoint` — the same arm group, green at the tip in shard 3.
  No red observed at the close.
- AC4 — `--dispatch refuses: the declared spec-token checker reds over the live tree` — the L1 positive
  control in region 3, green at the tip in shard 3. It asserts the refusal text only: that `RUN.md`
  gains no `dispatch` row was not observed. No red observed at the close.
- AC5 — `check-arms.py` — the probe printed check 49's branches, ordinal 18 the sibling malformed-order
  signature and 38 the resolver. `unarmed-branches.txt` holds rows at 8, 18 and 38, and none
  carries `an earlier step still holds`.
- AC6 — `Before any of that it runs the DECLARED spec-token checker` — 0 in both copies (1 in the BEFORE
  template), and the `diff` past the marker line printed nothing.
