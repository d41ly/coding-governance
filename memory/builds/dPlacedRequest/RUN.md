# dPlacedRequest - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 5352805c87e4fd9d3b239a2f4aac68c77d89f73e
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dplacedrequest-f41432
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-24T22:11:20Z
pid-image: claude.exe
host: compeeto-agent
pid: 22224
session: a4a72c24-4423-4b1e-9176-5acec5cc094f
keepalive: 37ace83d
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: c63aabbb4a73d44315dd5dd1219ff1dac5055cf8
anchor-ref: refs/heads/main
base: c63aabbb4a73d44315dd5dd1219ff1dac5055cf8

## Parked

2026-10-25T00:28:06Z rescope · item add TOOL-dPlacedRequest-23 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 21 at HIGH, item H3

2026-10-25T00:28:08Z rescope · item add TOOL-dPlacedRequest-24 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 56 at HIGH, item H9

2026-10-25T00:28:09Z rescope · item add TOOL-dPlacedRequest-25 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 20 at HIGH, item H1 shared with id 1

2026-10-25T00:28:11Z rescope · item add TOOL-dPlacedRequest-26 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 1 at HIGH, item H1 shared with id 20

2026-10-25T00:28:13Z rescope · item add TOOL-dPlacedRequest-27 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 52 at HIGH, item H6

2026-10-25T00:28:14Z rescope · item add TOOL-dPlacedRequest-28 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 53 at HIGH, item H7

2026-10-25T00:28:17Z rescope · item add TOOL-dPlacedRequest-29 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 51 at HIGH, item H5

2026-10-25T00:28:19Z rescope · item add TOOL-dPlacedRequest-30 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 54 at HIGH, item H4 shared with id 22

2026-10-25T00:28:21Z rescope · item add TOOL-dPlacedRequest-31 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 22 at HIGH, item H4 shared with id 54

2026-10-25T00:28:24Z rescope · item add TOOL-dPlacedRequest-32 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 55 at HIGH, item H8

2026-10-25T00:28:27Z rescope · item add TOOL-dPlacedRequest-33 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) finding id 6 at HIGH, item H2

2026-10-25T00:28:30Z rescope · item add TOOL-dPlacedRequest-34 · reason closes spec-audit round 1 (2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) findings at MEDIUM ids 2 3 4 5 7 8 9 10 11 13 14 15 16 23 24 25 26 27 28 32 33 34 35 36 37 38 39 44 45 46 47 48 49 50 57 58 59 60 61 62 63 65 66 67 68 69 70 71 72 73 and at LOW ids 12 17 18 19 29 30 31 40 41

2026-10-25T00:57:42Z review · item dPlacedRequest-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 11 · minors 59 · disposition promote
