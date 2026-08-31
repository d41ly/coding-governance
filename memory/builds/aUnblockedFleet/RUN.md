# aUnblockedFleet - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 864916663d95f4a88508f42f6677cd7482cd5ef7
phase: REVIEWING
branch-sha: 117de044094bc7ac729358edfc24541ba3a1486a
branch-ref: refs/heads/branch/unattended-builds-blocking-640d0d
mode: prompt
anchor-kind: run-branch
keepalive: 6a6fb940
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 396cd9db154f1621db5cb4cde72b93470b2f690c
anchor-ref: refs/heads/main
base: 117de044094bc7ac729358edfc24541ba3a1486a

## Parked

2026-08-30T23:55:59Z review · item spec-set · reason verdict BLOCKED · blockers 3

2026-08-30T23:58:31Z rescope · item add TOOL-aUnblockedFleet-6 · reason spec audit round 1 blocker B1: the merge bar's repo-wide turnstile (run-gates.sh:415-441, GATE_TURNSTILE default 1, keyed on git-common-dir) serializes two concurrent --close bars in one clone, and the queue wait sits INSIDE the run's declared GATE_BOUND=3600 while TS_MAXWAIT derives to >=7200s. Removing the two run-state checks alone therefore moves the wedge from STARTING to CLOSING rather than removing it.
