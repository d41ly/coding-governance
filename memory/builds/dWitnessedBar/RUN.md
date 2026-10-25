# dWitnessedBar - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: ad002a0247a5a129bb9982e6dd9308eadbf3734a
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dwitnessedbar-d0e46e
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-24T21:56:55Z
pid-image: claude.exe
host: compeeto
pid: 27568
session: 871858cc-6dd1-48fc-bfcd-88d1d87e87dc
keepalive: 5f3fe5e8
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: c63aabbb4a73d44315dd5dd1219ff1dac5055cf8
anchor-ref: refs/heads/main
base: cdfbd1cf9c5e31cc8620af362be33a66db61a076

## Parked

2026-10-25T00:28:42Z rescope · item add TOOL-dWitnessedBar-40 · reason spec-audit round1 finding id 18 at HIGH, report item H1

2026-10-25T00:28:43Z rescope · item add TOOL-dWitnessedBar-41 · reason spec-audit round1 finding id 59 at HIGH, report item H2

2026-10-25T00:28:44Z rescope · item add TOOL-dWitnessedBar-42 · reason spec-audit round1 finding id 60 at HIGH, report item H3

2026-10-25T00:28:44Z rescope · item add TOOL-dWitnessedBar-43 · reason spec-audit round1 finding id 63 at HIGH, report item H4

2026-10-25T00:28:45Z rescope · item add TOOL-dWitnessedBar-44 · reason spec-audit round1 finding id 62 at HIGH, report item H5

2026-10-25T00:28:46Z rescope · item add TOOL-dWitnessedBar-45 · reason spec-audit round1 finding id 33 at HIGH, report item H6

2026-10-25T00:28:47Z rescope · item add TOOL-dWitnessedBar-46 · reason spec-audit round1 finding id 34 at HIGH, report item H7

2026-10-25T00:28:47Z rescope · item add TOOL-dWitnessedBar-47 · reason spec-audit round1 finding id 35 at HIGH, report item H8

2026-10-25T00:28:48Z rescope · item add TOOL-dWitnessedBar-48 · reason spec-audit round1 finding id 27 at HIGH, report item H9

2026-10-25T00:28:49Z rescope · item add TOOL-dWitnessedBar-49 · reason spec-audit round1 finding id 49 at HIGH, report item H10

2026-10-25T00:28:49Z rescope · item add TOOL-dWitnessedBar-50 · reason spec-audit round1 finding id 50 at HIGH, report item H11

2026-10-25T00:28:59Z rescope · item add TOOL-dWitnessedBar-51 · reason spec-audit round1 minors batch, MEDIUM ids 1 2 3 4 5 6 7 8 9 10 11 19 20 21 22 23 28 29 31 36 37 38 39 40 42 46 47 48 51 52 54 55 58 61 64 65 69 and LOW ids 12 13 14 15 16 17 24 25 30 32 41 43 56

2026-10-25T01:00:03Z review · item dWitnessedBar-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 11 · minors 50 · disposition promote

2026-10-25T02:13:34Z rescope · item add TOOL-dWitnessedBar-52 · reason spec-audit round1 of units 40-51 finding id 1 at HIGH, report item H1 shared with id 13

2026-10-25T02:13:35Z rescope · item add TOOL-dWitnessedBar-53 · reason spec-audit round1 of units 40-51 finding id 13 at HIGH, report item H1 shared with id 1

2026-10-25T02:13:36Z rescope · item add TOOL-dWitnessedBar-54 · reason spec-audit round1 of units 40-51 finding id 42 at HIGH, report item H2

2026-10-25T02:13:36Z rescope · item add TOOL-dWitnessedBar-55 · reason spec-audit round1 of units 40-51 finding id 43 at HIGH, report item H3

2026-10-25T02:13:44Z rescope · item add TOOL-dWitnessedBar-56 · reason spec-audit round1 of units 40-51 minors batch A, MEDIUM ids 2 3 4 14 15 16 32 33 35 37 47 48 50 and LOW ids 11 20 23 27 41 49 52

2026-10-25T02:13:44Z rescope · item add TOOL-dWitnessedBar-57 · reason spec-audit round1 of units 40-51 minors batch B, MEDIUM ids 5 17 18 26 30 31 34 36 39 44 45 46 and LOW ids 6 7 9 10 12 19 21 22 25 29 38 51

2026-10-25T02:29:17Z review · item dWitnessedBar-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 4 · minors 44 · disposition promote

2026-10-25T03:28:11Z rescope · item add TOOL-dWitnessedBar-58 · reason spec-audit round1 of units 52-57 finding id 12 at HIGH, report item H1

2026-10-25T03:28:20Z rescope · item add TOOL-dWitnessedBar-59 · reason spec-audit round1 of units 52-57 finding id 13 at HIGH, report item H2

2026-10-25T03:28:21Z rescope · item add TOOL-dWitnessedBar-60 · reason spec-audit round1 of units 52-57 finding id 28 at HIGH, report item H3

2026-10-25T03:28:21Z rescope · item add TOOL-dWitnessedBar-61 · reason spec-audit round1 of units 52-57 finding id 35 at HIGH, report item H4

2026-10-25T03:28:22Z rescope · item add TOOL-dWitnessedBar-62 · reason spec-audit round1 of units 52-57 minors batch, MEDIUM ids 1 2 3 4 5 6 14 15 16 17 18 23 24 29 30 31 33 36 37 38 39 40 42 43 44 and LOW ids 7 9 10 11 19 20 21 22 25 26 32 34 41 45

2026-10-25T03:46:29Z review · item dWitnessedBar-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 4 · minors 39 · disposition promote
