# dIndexedDesign - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: 57bc3b91861a061dc9f37529bfe41db756c24fcd · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: c20c29685a6f3efafb7dc0bee67eefa6fe63a564
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dindexeddesign-516d37
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-10-28T01:10:54Z
pid-image: claude.exe
host: compeeto
pid: 18144
session: 75965d52-bd39-4234-bbfb-fb440f651df7
keepalive: beefbdcd
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 57bc3b91861a061dc9f37529bfe41db756c24fcd
anchor-ref: refs/heads/main
base: 57bc3b91861a061dc9f37529bfe41db756c24fcd

## Parked

2026-10-28T02:33:04Z rescope · item add TOOL-dIndexedDesign-20 · reason TOOL-dIndexedDesign-8's writer split cl-dClosedLoop-0390 by M2's one-mechanism test: unit 8 carries part 1/2 (design.decompose, feature designs, forks); this unit carries part 2/2 (design.reentry, the additive-versus-breaking diff, design.input and the re-design inventory)

2026-10-28T03:32:32Z review · item dIndexedDesign-spec-set-r1 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 6 · minors 42 · disposition promote

2026-10-28T03:41:21Z rescope · item add TOOL-dIndexedDesign-31 · reason closes report id 37 at BLOCKER (item B1) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md: the blinded scout input as a true allow-list, repairing TOOL-dIndexedDesign-5

2026-10-28T03:41:31Z rescope · item add TOOL-dIndexedDesign-32 · reason closes report id 19 at HIGH (item H1, shared with ids 20 and 21) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md: the feature-design and fork Serves kinds bind, repairing TOOL-dIndexedDesign-8

2026-10-28T03:41:32Z rescope · item add TOOL-dIndexedDesign-33 · reason closes report id 20 at HIGH (item H1, shared with ids 19 and 21) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md: the seams Serves kind binds, repairing TOOL-dIndexedDesign-13

2026-10-28T03:41:33Z rescope · item add TOOL-dIndexedDesign-34 · reason closes report id 21 at HIGH (item H1, shared with ids 19 and 20) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md: the diff and inventory Serves kinds bind and diff has one writer, repairing TOOL-dIndexedDesign-20

2026-10-28T03:41:33Z rescope · item add TOOL-dIndexedDesign-35 · reason closes report id 28 at HIGH (item H2) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md: the coverage lens runs as its own stage inside the agent-cap lens bound, repairing TOOL-dIndexedDesign-16

2026-10-28T03:41:34Z rescope · item add TOOL-dIndexedDesign-36 · reason closes report id 33 at HIGH (item H3) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md: BUILD-METHOD M6 names the dispatch refusals the hand-off and coverage add, repairing TOOL-dIndexedDesign-1

2026-10-28T03:41:35Z rescope · item add TOOL-dIndexedDesign-37 · reason closes report id 39 at HIGH (item H4) of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md: one write-set path predicate that keeps root files, repairing TOOL-dIndexedDesign-15

2026-10-28T03:41:36Z rescope · item add TOOL-dIndexedDesign-38 · reason closes the 42 MEDIUM and LOW findings of memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md batched in one unit, report ids 1 2 3 4 6 7 8 9 10 11 12 13 14 15 16 17 18 22 23 24 25 26 27 29 30 31 32 34 35 36 38 40 41 42 43 44 45 46 47 48 50 51

2026-10-28T04:40:31Z decision · item TOOL-dIndexedDesign-38 §8 F1: how does the build run pass the window between unit 16's pass and its first coverage-lens reading, when --dispatch refuses every unit under design.coverage refuse and design.coverage.semantic every-exit and no lens reading exists until unit 35 lands? · reason options (a) the owner commits design.coverage = warn on the run branch at unit 16's pass and restores refuse once the first lens record lands; (b) a grace in check_design_exit reading an audit record with no coverage field as WARN, which relaxes the gate for every unit audited before the lens; (c) move unit 16's S8 and S9 to the last order, a re-scope of unit 16 no repair unit may make. Refused to pick: (a) is an owner turn on a guarded policy file, (b) widens what the gate admits beyond the tier priced (veto 3), (c) amends another unit's scope; M3 parks a fork whose survivors are owner turns. Surfaced at the build run's M3 sweep before its first unit
