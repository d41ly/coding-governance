# dTrueNorth - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 7bf32c437315dc808fc9b210acd6bdd70f82f368
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3 PLAY-dClosedLoop-2
mode: slug
run-branch: refs/heads/branch/unattended-dtruenorth-4cb56e
anchor-kind: default-branch
cli-version: 2.1.299
lease-utc: 2026-10-21T13:19:44Z
pid-image: claude.exe
host: compeeto
pid: 55004
session: bc821d4c-b305-40e3-bf2f-7dc1519c57f1
keepalive: d191a5fc
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 271aa59defcb695133a50a49dc07650f9058a930
anchor-ref: refs/heads/main
base: 271aa59defcb695133a50a49dc07650f9058a930

## Parked

2026-10-21T14:53:28Z rescope · item add TOOL-dTrueNorth-8 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 1 HIGH, item H1: no unit owns re-rendering the as-built view once the deviation records land, and unit 6 forbids editing it; repairs TOOL-dTrueNorth-6

2026-10-21T14:53:47Z rescope · item add TOOL-dTrueNorth-9 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 11 HIGH, item H2: the _expand_ids 3-tuple strands read_idlist and backlog.read_header_verbs, its two unlisted callers; repairs TOOL-dTrueNorth-5

2026-10-21T14:53:48Z rescope · item add TOOL-dTrueNorth-10 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 12 HIGH, item H3: deviation records 2 and 3 exist nowhere and no spec writes them; repairs TOOL-dTrueNorth-4

2026-10-21T14:53:49Z rescope · item add TOOL-dTrueNorth-11 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 28 HIGH, item H4: the build-index and memory-hygiene self-test legs skip when only check-spec-tokens.py changes; repairs TOOL-dTrueNorth-3

2026-10-21T14:53:50Z rescope · item add TOOL-dTrueNorth-12 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 30 HIGH, item H5: the routed-commits selftest reads an unguarded sibling kit and gov-only design records; repairs TOOL-dTrueNorth-4

2026-10-21T14:53:51Z rescope · item add TOOL-dTrueNorth-13 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 39 HIGH, item H6: spec-audit pins cannot represent a design-document audit; repairs TOOL-dTrueNorth-5

2026-10-21T14:53:52Z rescope · item add TOOL-dTrueNorth-14 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 40 HIGH, item H7: the audit-pin cutoff refuses records written by runs already in flight; repairs TOOL-dTrueNorth-5

2026-10-21T14:53:53Z rescope · item add TOOL-dTrueNorth-15 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) id 41 HIGH, item H8: check 29 grades an empty population on the harness path and says nothing; repairs TOOL-dTrueNorth-3

2026-10-21T14:53:53Z rescope · item add TOOL-dTrueNorth-16 · reason spec-audit round 1 (reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) the 37 confirmed minors batched into one unit: 23 MEDIUM, ids 2 3 4 13 5 23 43 6 14 15 19 20 21 22 27 29 31 32 42 44 45 46 47 (items M1 to M20), and 14 LOW, ids 8 26 10 16 17 35 18 24 25 33 34 36 37 38 (items L1 to L12); one unit, not two, because both candidate halves read design_lib.py and check-spec-tokens.py as contracts

2026-10-21T15:20:40Z review · item dTrueNorth-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 8 · minors 37 · disposition promote

2026-10-21T16:09:50Z rescope · item add TOOL-dTrueNorth-17 · reason spec-audit round 2 (reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) id 1 HIGH, item H1: the order-3 transition re-renders the as-built view with no owner, so the second of units 4 and 6 to land is refused at check 9 or re-renders undeclared; repairs TOOL-dTrueNorth-8

2026-10-21T16:09:50Z rescope · item add TOOL-dTrueNorth-18 · reason spec-audit round 2 (reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) id 34 HIGH, item H2: two amends of one clause are ordered by lexical path, so the view can render the older record's text and hash; repairs TOOL-dTrueNorth-8

2026-10-21T16:09:51Z rescope · item add TOOL-dTrueNorth-19 · reason spec-audit round 2 (reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) id 38 HIGH, item H3: the audit-writer reader passes every graded record path as argv, which raises WinError 206 near 330 records, and a missing harness blob exempts its record; repairs TOOL-dTrueNorth-14

2026-10-21T16:09:52Z rescope · item add TOOL-dTrueNorth-20 · reason spec-audit round 2 (reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) the 38 confirmed minors batched into one unit: 21 MEDIUM, ids 2 4 5 11 12 13 24 25 26 27 28 29 30 33 36 37 39 40 41 42 43 (items M1 to M18), and 17 LOW, ids 3 6 7 9 10 14 15 16 18 19 20 23 31 32 35 45 46 (items L1 to L15); one unit, not two, because every candidate half writes a file the other reads as a contract

2026-10-21T16:25:50Z review · item dTrueNorth-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 3 · minors 38 · disposition promote
