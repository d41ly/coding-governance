# dScopedBuild - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 807775940
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dscoped-build-bb2a9b
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-11-01T07:31:40Z
pid-image: claude.exe
host: compeeto-agent
pid: 5908
session: 837796a8-5865-4267-b799-0e5da2f1c61e
keepalive: 96b8777c
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: f4597719e4b1ff0f0f779998bd7b8c2ce5213088
anchor-ref: refs/heads/main
base: f4597719e4b1ff0f0f779998bd7b8c2ce5213088

## Parked

2026-11-01T11:10:07Z rescope · item add TOOL-dScopedBuild-25 · reason spec-audit round1 of units 1-15 finding id 1 at HIGH, report item H1

2026-11-01T11:10:18Z rescope · item add TOOL-dScopedBuild-26 · reason spec-audit round1 of units 1-15 finding id 2 at HIGH, report item H2

2026-11-01T11:10:20Z rescope · item add TOOL-dScopedBuild-27 · reason spec-audit round1 of units 1-15 finding id 3 at HIGH, report item H3

2026-11-01T11:10:21Z rescope · item add TOOL-dScopedBuild-28 · reason spec-audit round1 of units 1-15 finding id 14 at HIGH, report item H4

2026-11-01T11:10:23Z rescope · item add TOOL-dScopedBuild-29 · reason spec-audit round1 of units 1-15 finding id 17 at HIGH, report item H5

2026-11-01T11:10:24Z rescope · item add TOOL-dScopedBuild-30 · reason spec-audit round1 of units 1-15 finding id 19 at HIGH, report item H6

2026-11-01T11:10:26Z rescope · item add TOOL-dScopedBuild-31 · reason spec-audit round1 of units 1-15 finding id 20 at HIGH, report item H7

2026-11-01T11:10:27Z rescope · item add TOOL-dScopedBuild-32 · reason spec-audit round1 of units 1-15 finding id 22 at HIGH, report item H8

2026-11-01T11:10:29Z rescope · item add TOOL-dScopedBuild-33 · reason spec-audit round1 of units 1-15 finding id 30 at HIGH, report item H9

2026-11-01T11:10:30Z rescope · item add TOOL-dScopedBuild-34 · reason spec-audit round1 of units 1-15 finding id 36 at HIGH, report item H10

2026-11-01T11:10:31Z rescope · item add TOOL-dScopedBuild-35 · reason spec-audit round1 of units 1-15 minors batch, MEDIUM ids 4 5 6 12 13 15 16 18 21 25 26 27 28 29 31 32 33 34 37 38 39 40 41 42 43 44 45 46 47 48 49 50 and LOW ids 7 8 9 10 11 35

2026-11-01T11:39:09Z review · item dScopedBuild-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 10 · minors 38 · disposition promote

2026-11-01T12:58:41Z rescope · item add TOOL-dScopedBuild-36 · reason spec-audit round1 of units 25-35 finding id 11 at HIGH, report item H1

2026-11-01T12:58:42Z rescope · item add TOOL-dScopedBuild-37 · reason spec-audit round1 of units 25-35 finding id 22 at HIGH, report item H2

2026-11-01T12:58:43Z rescope · item add TOOL-dScopedBuild-38 · reason spec-audit round1 of units 25-35 finding id 26 at HIGH, report item H3

2026-11-01T12:58:45Z rescope · item add TOOL-dScopedBuild-39 · reason spec-audit round1 of units 25-35 minors batch, MEDIUM ids 1 2 3 4 5 6 7 12 13 14 15 23 27 28 30 31 and LOW ids 8 9 10 16 17 18 19 20 21 24 25 29 32

2026-11-01T13:20:37Z review · item dScopedBuild-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 3 · minors 29 · disposition promote

2026-11-01T14:41:51Z rescope · item add TOOL-dScopedBuild-40 · reason spec-audit round1 of units 36-39 finding id 24 at HIGH, report item H1

2026-11-01T14:41:53Z rescope · item add TOOL-dScopedBuild-41 · reason spec-audit round1 of units 36-39 minors batch, MEDIUM ids 1 2 3 10 17 18 19 21 25 26 and LOW ids 4 5 6 7 8 9 11 13 14 15 22 23

2026-11-01T15:04:10Z review · item dScopedBuild-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 1 · minors 22 · disposition promote

2026-11-01T16:28:26Z rescope · item add TOOL-dScopedBuild-42 · reason spec-audit round1 of units 40-41 finding id 14 at HIGH, report item H1

2026-11-01T16:28:28Z rescope · item add TOOL-dScopedBuild-43 · reason spec-audit round1 of units 40-41 minors batch, MEDIUM ids 1 3 7 8 10 11 15 and LOW ids 4 5 9 13

2026-11-01T16:47:16Z review · item dScopedBuild-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 1 · minors 11 · disposition promote
