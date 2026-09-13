# aBatchedArm - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: c2db2f5d2d6100af08a09da113086d114c67b603
phase: RUNNING
branch-sha: c2db2f5d2d6100af08a09da113086d114c67b603
branch-ref: refs/heads/branch/unattended-checks-performance-a37d8d
mode: prompt
anchor-kind: run-branch
keepalive: c1d67ccd
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 09a22d2bf5c3fc51bdc3ccee8c727b0793664106
anchor-ref: refs/heads/main
base: c2db2f5d2d6100af08a09da113086d114c67b603

## Parked

2026-09-13T10:09:42Z rescope · item add TOOL-aBatchedArm-4 · reason Owner ruling 2026-09-10 on the parked scope question: the route is the shared runner. tools/run-gates/run-selftests.sh gets a slash-tolerant row checker and DECLARED execution modes, so pooled is available and serial stays possible when it is deliberately declared. This is the unit that unblocks TOOL-aBatchedArm-3, whose eight shard rows cannot be declared today (the row checker reds any slash-bearing argv token) and would run serially if they could (OUTER=1 except under --sweep, which withholds cost verdicts). A change to a shared runner grading 61 suites, added by owner instruction rather than by the run's own authority.
