# dLinkedLibrary - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 5a91830114df92e6f0655a423cd5cfe9d05bd0d4
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dlinkedlibrary-4f9fd9
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-26T18:15:59Z
pid-image: claude.exe
host: compeeto
pid: 36324
session: 656f8198-ecf1-4716-a7c6-3c9ec44fadde
keepalive: 54d55780
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 5fede642ad2ff1418f12b5d7117129edc8287d7e
anchor-ref: refs/heads/main
base: 5fede642ad2ff1418f12b5d7117129edc8287d7e

## Parked

2026-10-26T21:16:53Z review · item dLinkedLibrary-spec-set-r1 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 14 · minors 64 · disposition promote

2026-10-26T21:32:57Z rescope · item add TOOL-dLinkedLibrary-37 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 58 at BLOCKER, report item R1; repairs TOOL-dLinkedLibrary-9

2026-10-26T21:33:05Z rescope · item add TOOL-dLinkedLibrary-38 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 1 at HIGH, report item R2; repairs TOOL-dLinkedLibrary-19

2026-10-26T21:33:06Z rescope · item add TOOL-dLinkedLibrary-39 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 2 at HIGH, report item R3; repairs TOOL-dLinkedLibrary-4

2026-10-26T21:33:07Z rescope · item add TOOL-dLinkedLibrary-40 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 3 at HIGH, report item R4 (id 35 shares the defect at MEDIUM, item R34); repairs TOOL-dLinkedLibrary-23

2026-10-26T21:33:08Z rescope · item add TOOL-dLinkedLibrary-41 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 4 at HIGH, report item R5; repairs TOOL-dLinkedLibrary-17

2026-10-26T21:33:10Z rescope · item add TOOL-dLinkedLibrary-42 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 8 at HIGH, report item R6; repairs TOOL-dLinkedLibrary-3

2026-10-26T21:33:11Z rescope · item add TOOL-dLinkedLibrary-43 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 20 at HIGH, report item R7; repairs TOOL-dLinkedLibrary-18

2026-10-26T21:33:12Z rescope · item add TOOL-dLinkedLibrary-44 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 22 at HIGH, report item R8; repairs TOOL-dLinkedLibrary-4

2026-10-26T21:33:12Z rescope · item add TOOL-dLinkedLibrary-45 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 30 at HIGH, report item R9; repairs TOOL-dLinkedLibrary-18

2026-10-26T21:33:14Z rescope · item add TOOL-dLinkedLibrary-46 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 49 at HIGH, report item R10, the arm lines of units 14, 15 and 21; repairs TOOL-dLinkedLibrary-15, the last of the three in order

2026-10-26T21:33:15Z rescope · item add TOOL-dLinkedLibrary-47 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 50 at HIGH, report item R11; repairs TOOL-dLinkedLibrary-8

2026-10-26T21:33:16Z rescope · item add TOOL-dLinkedLibrary-48 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 59 at HIGH, report item R12; repairs TOOL-dLinkedLibrary-12

2026-10-26T21:33:17Z rescope · item add TOOL-dLinkedLibrary-49 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 64 at HIGH, report item R13; repairs TOOL-dLinkedLibrary-24

2026-10-26T21:33:18Z rescope · item add TOOL-dLinkedLibrary-50 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 65 at HIGH, report item R14; repairs TOOL-dLinkedLibrary-19

2026-10-26T21:33:18Z rescope · item add TOOL-dLinkedLibrary-51 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 67 at HIGH, report item R15; repairs TOOL-dLinkedLibrary-8

2026-10-26T21:34:38Z rescope · item add TOOL-dLinkedLibrary-52 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) minors batched, code half split by write set (BUILD-METHOD M4, M6): MEDIUM ids 5 24 6 7 9 40 63 11 14 15 21 60 23 25 28 31 32 33 34 37 39 44 74 45 46 47 48 52 53 55 62 61 68 69 70 71 72 73 75 78 79 80 (items R16-R20, R23, R24, R26-R33, R35, R36, R38-R45, R47-R55, R57-R59) and LOW ids 17 18 19 29 41 36 38 42 54 66 81 (items R61-R68, R70, R71)

2026-10-26T21:34:39Z rescope · item add TOOL-dLinkedLibrary-53 · reason spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) minors batched, records-and-observations half split by write set (BUILD-METHOD M4, M6), its Files touched sharing no path with TOOL-dLinkedLibrary-52's: MEDIUM ids 12 26 13 16 35 43 56 76 (items R21, R22, R25, R34, R37, R46, R56) and LOW ids 10 27 57 (items R60, R69)
