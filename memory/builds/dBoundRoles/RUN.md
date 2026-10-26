# dBoundRoles - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 4914545b1f40863a78d9c35df75e1f211da555ff
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dboundroles-a396a1
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-25T21:15:09Z
pid-image: claude.exe
host: compeeto
pid: 12100
session: e21e2f44-d94e-4d90-8c0d-fed7326fab13
keepalive: 74caefa1
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 462d20f3510072a1dddb5b948370937cfd3bbe0e
anchor-ref: refs/heads/main
base: 462d20f3510072a1dddb5b948370937cfd3bbe0e

## Parked

2026-10-25T23:33:51Z rescope · item add TOOL-dBoundRoles-37 · reason spec-audit round1 finding id 4 at HIGH, report item H5 (id 47 shares the defect at MEDIUM, item M25)

2026-10-25T23:33:51Z rescope · item add TOOL-dBoundRoles-38 · reason spec-audit round1 finding id 52 at HIGH, report item H4

2026-10-25T23:33:52Z rescope · item add TOOL-dBoundRoles-39 · reason spec-audit round1 finding id 21 at HIGH, report item H1, shared with id 56

2026-10-25T23:33:53Z rescope · item add TOOL-dBoundRoles-40 · reason spec-audit round1 finding id 56 at HIGH, report item H1, shared with id 21

2026-10-25T23:33:53Z rescope · item add TOOL-dBoundRoles-41 · reason spec-audit round1 finding id 22 at HIGH, report item H2 (id 53 shares the defect at MEDIUM, item M30)

2026-10-25T23:33:54Z rescope · item add TOOL-dBoundRoles-42 · reason spec-audit round1 finding id 42 at HIGH, report item H3 (id 3 shares the defect at MEDIUM, item M3)

2026-10-25T23:34:00Z rescope · item add TOOL-dBoundRoles-43 · reason spec-audit round1 minors batched: MEDIUM ids 1 2 3 5 6 7 8 32 9 10 11 12 13 36 24 46 25 26 27 28 31 35 37 38 63 43 44 45 47 48 49 50 51 53 54 55 57 58 59 60 61 62 64 (items M1-M39) and LOW ids 15 33 14 16 17 18 19 20 29 30 34 39 40 41 (items L1-L13)

2026-10-26T00:03:09Z review · item dBoundRoles-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 6 · minors 57 · disposition promote

2026-10-26T00:38:46Z rescope · item add TOOL-dBoundRoles-44 · reason spec-audit round1 minors batch split by write set (BUILD-METHOD M4): TOOL-dBoundRoles-43 was 60120 bytes over the 49152 spec ceiling; 44 takes MEDIUM ids 3 5 26 28 43 48 49 51 62 and LOW ids 16 17, whose Files touched share no path with 43's
