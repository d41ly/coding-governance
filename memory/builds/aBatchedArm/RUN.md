# aBatchedArm - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 46fd95b022bff351ff6b823c3278112234b020c2
phase: REVIEWING
branch-sha: e9ed269bc7ae7a7a5453156eff5431abf7280bcc
branch-ref: refs/heads/branch/unattended-checks-performance-a37d8d
mode: prompt
anchor-kind: run-branch
keepalive: c2b564d8
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: fdd754bf62d1833361350ab7cb0b0f393027d99a
anchor-ref: refs/heads/main
base: e9ed269bc7ae7a7a5453156eff5431abf7280bcc

## Parked

2026-09-10T10:55:53Z review · item TOOL-aBatchedArm-1 · reason verdict BLOCKED · blockers 3

2026-09-10T10:58:32Z rescope · item add TOOL-aBatchedArm-2 · reason spec-audit round 1 named one structural group linter as the left-shift for five of its six findings. It grades the LINKAGE between a group's emitted set and its miss/same arms, which TOOL-aBatchedArm-1 states as a rule and cannot enforce per group. A separate mechanism under M2, so a unit rather than a scope item.

2026-09-10T11:30:16Z review · item TOOL-aBatchedArm-1 · reason verdict BLOCKED · blockers 13 · NON-CONVERGENT · disposition fold

2026-09-10T11:31:16Z rescope · item add TOOL-aBatchedArm-3 · reason Round 2 killed the admissibility rule: only 6 of 29 check numbers carry a single branch (16 carries 34, 28 carries 31), so a fired check number witnesses one of up to 34 branches and cannot witness the one a miss control is about. Excluding miss and same arms as TOOL-dScriptedRepeat-15 S3 requires leaves 95 blocks carrying 136 solo invocations, which is 36 minutes before any batch runs. MEASURED: batching alone reaches 40 to 44 minutes unsharded and misses the 20-minute goal at every group size. Raising SHARD_ARITY from 2 to 8 reaches about 10 minutes with no new mechanism and no unsound oracle, is already owner-ruled 2026-08-29 under TOOL-aGradedDoorway-7 S2, and carries assertion-count identity as its control. Adopted under protocol section 11 rather than parked: it makes the measured observable strictly better, makes nothing worse, and trips no M3 veto.
