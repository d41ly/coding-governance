# aBatchedArm - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 8d2c065e0341e35a4d082c23a1f63faa35536cd6
phase: BUILDING
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

2026-09-13T10:50:23Z review · item TOOL-aBatchedArm-4 · reason verdict BLOCKED · blockers 8

2026-09-13T10:53:13Z rescope · item add TOOL-aBatchedArm-5 · reason Spec-audit round 1 of TOOL-aBatchedArm-4 B5: its S5 pooled hang bound was a scalar factor over the serial reading, the shape TOOL-dRetiredFork-40, TOOL-aPooledSweep-2 section 3 and the full-sweep record all rejected, and derive-ceilings.py already owns the evidence shape - a per-row observed reading under the declared condition, monotone, with ceiling-margin.txt's max(120s, 1.0 x max) headroom. That bound is the mechanism that killed 14 of 58 suites once, so it is its own unit under M2 rather than a paragraph in the mode unit. Consumes the rows from unit 3 and the modes from unit 4.

2026-09-13T11:20:53Z review · item TOOL-aBatchedArm-4 · reason verdict BLOCKED · blockers 3

2026-09-13T11:53:08Z review · item TOOL-aBatchedArm-4 · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT · disposition fold

2026-09-13T11:59:15Z brief · item TOOL-aBatchedArm-4 · reason b56f676efee7 memory/builds/aBatchedArm/prompts/2026-09-13-prompt-TOOL-aBatchedArm-4-build-brief.md

2026-09-13T12:06:10Z dispatch · item 1ed8bf22 TOOL-aBatchedArm-4 · reason tools/run-gates/run-selftests.sh tools/run-gates/run-selftests.test.sh tools/unattended/run-unattended-gates.sh tools/unattended/README.md tools/unattended/kit.toml .githooks/gate-env.sh AGENTS.md memory/guides/SESSION-KICKOFF.md memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md memory/builds/aBatchedArm/build/2026-09-13-build-TOOL-aBatchedArm-4-1-acceptance-ledger.md memory/builds/aBatchedArm/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T13:40:07Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 9

2026-09-13T14:14:49Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 8

2026-09-13T15:22:35Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 4

2026-09-13T15:51:57Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 12 · NON-CONVERGENT · disposition fold
