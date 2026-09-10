# aBatchedArm - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 5632f34a830e149fccc702740a32b75c5e4fa36c
phase: SPECCING
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
