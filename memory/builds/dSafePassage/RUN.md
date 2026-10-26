# dSafePassage - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 7f9df190edf29fffd43d3114277eeb851aedf3d0
phase: BUILDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dsafepassage-567339
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-26T08:36:02Z
pid-image: claude.exe
host: compeeto-agent
pid: 23020
session: c5f50d22-89c6-41d7-84e5-2382dcd49faa
keepalive: 6e25bf31
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 60d90cb71db51e651aa1c5efe3f6d48ba21a997d
anchor-ref: refs/heads/main
base: 60d90cb71db51e651aa1c5efe3f6d48ba21a997d

## Parked

2026-10-26T09:06:44Z rescope · item add TOOL-dSafePassage-61 · reason TOOL-dSafePassage-1's build pass diverged at §8 F8: the landed policy guard (tools/policy/guard.py, TOOL-dGroundRules-6) refuses S8's seven-key write of .governance/policy.toml ('7 keys changed; one cap raised is the one agent shape'), and TOOL-dGroundRules-13, the ask that would admit it, is OPEN; F8 says the build run stops S8 if not granted, so the gov migration of template-size-limits.txt moves to this new unit, DEFERRED until TOOL-dGroundRules-13
