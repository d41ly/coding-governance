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

2026-10-26T01:43:27Z rescope · item add TOOL-dBoundRoles-45 · reason spec-audit round1 of units 37-44 finding id 17 at HIGH, report item H1, shared with ids 1 and 9

2026-10-26T01:43:28Z rescope · item add TOOL-dBoundRoles-46 · reason spec-audit round1 of units 37-44 finding id 1 at HIGH, report item H1, shared with ids 9 and 17

2026-10-26T01:43:29Z rescope · item add TOOL-dBoundRoles-47 · reason spec-audit round1 of units 37-44 finding id 9 at HIGH, report item H1, shared with ids 1 and 17

2026-10-26T01:43:29Z rescope · item add TOOL-dBoundRoles-48 · reason spec-audit round1 of units 37-44 finding id 34 at HIGH, report item H3

2026-10-26T01:43:30Z rescope · item add TOOL-dBoundRoles-49 · reason spec-audit round1 of units 37-44 finding id 23 at HIGH, report item H2

2026-10-26T01:43:38Z rescope · item add TOOL-dBoundRoles-50 · reason spec-audit round1 of units 37-44 minors batched, roles-code half split by write set (BUILD-METHOD M4, M6): MEDIUM ids 4 5 10 11 18 19 25 26 27 28 29 30 33 35 36 37 38 (items M3 M4 M5 M6 M8 M9 M10 M11 M12 M13 M15 M16 M17 M18) and LOW ids 6 12 15 21 22 39 40 (items L1 L4 L6 L7 L8 L9 L10)

2026-10-26T01:43:38Z rescope · item add TOOL-dBoundRoles-51 · reason spec-audit round1 of units 37-44 minors batched, records-and-Skills half split by write set (BUILD-METHOD M4, M6): MEDIUM ids 2 3 13 31 (items M1 M2 M7 M14) and LOW ids 7 8 14 20 (items L2 L3 L5)

2026-10-26T02:09:24Z review · item dBoundRoles-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 5 · minors 32 · disposition promote

2026-10-26T03:13:29Z rescope · item add TOOL-dBoundRoles-52 · reason spec-audit round1 of units 45-51 finding id 13 at HIGH, report item H1, shared with id 30 (ids 2 and 39 share the defect at MEDIUM, item M1)

2026-10-26T03:13:38Z rescope · item add TOOL-dBoundRoles-53 · reason spec-audit round1 of units 45-51 finding id 30 at HIGH, report item H1, shared with id 13 (ids 2 and 39 share the defect at MEDIUM, item M1)

2026-10-26T03:13:38Z rescope · item add TOOL-dBoundRoles-54 · reason spec-audit round1 of units 45-51 finding id 14 at HIGH, report item H2, shared with id 40

2026-10-26T03:13:39Z rescope · item add TOOL-dBoundRoles-55 · reason spec-audit round1 of units 45-51 finding id 40 at HIGH, report item H2, shared with id 14

2026-10-26T03:13:40Z rescope · item add TOOL-dBoundRoles-56 · reason spec-audit round1 of units 45-51 finding id 20 at HIGH, report item H3 (id 34 shares the defect at MEDIUM, item M9)

2026-10-26T03:13:41Z rescope · item add TOOL-dBoundRoles-57 · reason spec-audit round1 of units 45-51 finding id 29 at HIGH, report item H4

2026-10-26T03:13:42Z rescope · item add TOOL-dBoundRoles-58 · reason spec-audit round1 of units 45-51 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 2 39 3 4 37 46 5 8 15 32 21 33 11 17 34 22 23 24 25 31 42 45 47 48 (items M1-M18) and LOW ids 9 10 12 38 19 26 27 28 35 49 50 (items L1-L10)

2026-10-26T03:33:27Z review · item dBoundRoles-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 6 · minors 35 · disposition promote

2026-10-26T04:16:46Z rescope · item add TOOL-dBoundRoles-59 · reason spec-audit round1 of units 52-58 finding id 21 at HIGH, report item H1

2026-10-26T04:16:46Z rescope · item add TOOL-dBoundRoles-60 · reason spec-audit round1 of units 52-58 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 1 12 24 2 16 3 4 14 27 5 13 7 36 9 29 15 22 25 28 30 33 34 35 37 (items M1-M16) and LOW ids 6 19 8 11 17 31 18 20 23 26 32 38 39 (items L1-L11)

2026-10-26T04:34:11Z review · item dBoundRoles-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 1 · minors 37 · disposition promote

2026-10-26T05:15:42Z rescope · item add TOOL-dBoundRoles-61 · reason spec-audit round1 of units 59 and 60 finding id 19 at HIGH, report item H1 (id 9 shares the defect at MEDIUM, item M2)

2026-10-26T05:15:48Z rescope · item add TOOL-dBoundRoles-62 · reason spec-audit round1 of units 59 and 60 finding id 21 at HIGH, report item H2 (ids 2 and 10 raise the same missing floor at MEDIUM, item M1)

2026-10-26T05:15:49Z rescope · item add TOOL-dBoundRoles-63 · reason spec-audit round1 of units 59 and 60 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 2 10 15 22 9 3 4 5 13 16 17 20 (items M1-M9) and LOW ids 6 7 8 11 12 14 18 (items L1-L7)

2026-10-26T05:27:25Z review · item dBoundRoles-spec-set-r5 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 2 · minors 19 · disposition promote

2026-10-26T06:04:01Z rescope · item add TOOL-dBoundRoles-64 · reason spec-audit round1 of units 61 62 and 63 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 1 19 2 9 25 3 10 4 22 30 11 31 12 16 32 20 24 33 (items M1-M10) and LOW ids 13 5 14 6 7 21 8 23 15 29 17 26 27 28 (items L1-L10)

2026-10-26T06:21:06Z review · item dBoundRoles-spec-set-r6 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 32 · disposition promote
