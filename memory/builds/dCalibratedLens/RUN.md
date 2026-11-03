# dCalibratedLens - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: ccf601242d2fe6cfdbfef6a2f3551bd9554e3c2c
phase: VERIFYING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dcalibratedlens-9622f6
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-11-02T15:35:25Z
pid-image: claude.exe
host: compeeto-agent
pid: 20616
session: 8628a15b-1e85-404c-a4a6-275883b9a078
keepalive: fa87da63
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 8bec4cefd957d194660a8d7c2916f420b7299074
anchor-ref: refs/heads/main
base: 8bec4cefd957d194660a8d7c2916f420b7299074

## Parked

2026-11-02T19:49:56Z rescope · item add TOOL-dCalibratedLens-19 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 1 HIGH, item H1: the value-ledger, loop-review and keep rows share one home, so each record falls under three rows' fields; repairs TOOL-dCalibratedLens-3

2026-11-02T19:49:59Z rescope · item add TOOL-dCalibratedLens-20 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 36 HIGH, item H2: no Loop Review record carries a Serves line, so the record-kinds field check grades none of them; repairs TOOL-dCalibratedLens-3

2026-11-02T19:50:01Z rescope · item add TOOL-dCalibratedLens-21 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 2 HIGH, item H3 (shares its fix with id 45, M25): units 4, 6 and 16 add multi-line record fields the shared writer refuses; repairs TOOL-dCalibratedLens-4

2026-11-02T19:50:03Z rescope · item add TOOL-dCalibratedLens-22 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 3 HIGH, item H4: gather-time proposals have no route to file and no accept text; repairs TOOL-dCalibratedLens-3

2026-11-02T19:50:06Z rescope · item add TOOL-dCalibratedLens-23 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 4 HIGH, item H5: the instruction-eval seed may land owed, which reds the unattended close bar; repairs TOOL-dCalibratedLens-10

2026-11-02T19:50:10Z rescope · item add TOOL-dCalibratedLens-24 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 16 HIGH, item H6: unit 1 AC3 feeds the agent-cap hook no payload, so it passes before the unit is built; repairs TOOL-dCalibratedLens-1

2026-11-02T19:50:22Z rescope · item add TOOL-dCalibratedLens-25 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 35 HIGH, item H7: unit 5's trailing units field breaks the format guard's agent-id test and its self-test fixtures; repairs TOOL-dCalibratedLens-5

2026-11-02T19:50:25Z rescope · item add TOOL-dCalibratedLens-26 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 48 HIGH, item H8: an empty catch source reads every leg as catches 0 and unit 5 then proposes retiring all of them; repairs TOOL-dCalibratedLens-2

2026-11-02T19:50:27Z rescope · item add TOOL-dCalibratedLens-27 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 49 HIGH, item H9: a deterministic item failure re-runs the period forever and re-files every proposal on each wake; repairs TOOL-dCalibratedLens-3

2026-11-02T19:50:29Z rescope · item add TOOL-dCalibratedLens-28 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 50 HIGH, item H10: units 9, 16 and 6 read populations through gov_record.py find and ignore its 40-row cap; repairs TOOL-dCalibratedLens-9

2026-11-02T19:50:32Z rescope · item add TOOL-dCalibratedLens-29 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) id 52 HIGH, item H11: unit 6 passes every work-order path as argv, past the Windows command-line limit; repairs TOOL-dCalibratedLens-6

2026-11-02T19:50:34Z rescope · item add TOOL-dCalibratedLens-30 · reason spec-audit round 1 (reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) minors batched into one unit, 30 MEDIUM and 11 LOW by raw id: 5 32 6 7 8 9 10 46 17 18 25 26 27 28 29 30 31 33 37 38 39 40 41 42 43 44 45 51 53 54 11 12 13 14 20 21 22 23 24 34 47; repairs no unit in particular

2026-11-02T20:23:30Z review · item dCalibratedLens-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 11 · minors 41 · disposition promote

2026-11-02T21:40:07Z review · item dCalibratedLens-spec-set-r2 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 9 · minors 28 · disposition promote

2026-11-02T21:50:27Z rescope · item add TOOL-dCalibratedLens-31 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 30 BLOCKER, item B1: the shipped renderer prints the returned line's optional units group with literal brackets; repairs TOOL-dCalibratedLens-25

2026-11-02T21:50:29Z rescope · item add TOOL-dCalibratedLens-32 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 26 HIGH, item H1 (shared with ids 2 and 11): unit 19's staged overlap break cannot go red under TOOL-dTotalRecall-42 S5; repairs TOOL-dCalibratedLens-19

2026-11-02T21:50:32Z rescope · item add TOOL-dCalibratedLens-33 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 2 HIGH, item H1 (shared with ids 11 and 26): the arm reads as coverage for disjoint homes it never tests; repairs TOOL-dCalibratedLens-19

2026-11-02T21:50:35Z rescope · item add TOOL-dCalibratedLens-34 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 11 HIGH, item H1 (shared with ids 2 and 26): unit 19 rests on the ancestor clause TOOL-dTotalRecall-42 S5 replaced; repairs TOOL-dCalibratedLens-19

2026-11-02T21:50:39Z rescope · item add TOOL-dCalibratedLens-35 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 1 HIGH, item H2: unit 19's keep is graded by no row at its build order; repairs TOOL-dCalibratedLens-19

2026-11-02T21:50:56Z rescope · item add TOOL-dCalibratedLens-36 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 6 HIGH, item H3: the seed's held verdict at unit 23 ignores guard-path edits by units 5 and 25; repairs TOOL-dCalibratedLens-23

2026-11-02T21:50:58Z rescope · item add TOOL-dCalibratedLens-37 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 24 HIGH, item H4: unit 25 adds a guard pathspec govkit selfcheck classes into no class; repairs TOOL-dCalibratedLens-25

2026-11-02T21:51:00Z rescope · item add TOOL-dCalibratedLens-38 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 19 HIGH, item H5: unit 29 writes a second adding-commit reader beside tree_lib.read_adding_commits; repairs TOOL-dCalibratedLens-29

2026-11-02T21:51:02Z rescope · item add TOOL-dCalibratedLens-39 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 27 HIGH, item H6: unit 21 makes repeated Metrics names normal but never constrains read_metrics_lines' return shape; repairs TOOL-dCalibratedLens-21

2026-11-02T21:51:04Z rescope · item add TOOL-dCalibratedLens-40 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) id 31 HIGH, item H7: an unsanitised why in an unread line blocks every period's record; repairs TOOL-dCalibratedLens-27

2026-11-02T21:51:06Z rescope · item add TOOL-dCalibratedLens-41 · reason spec-audit round 2 (reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) minors batched into one unit, 22 MEDIUM and 6 LOW by raw id: 3 4 5 16 23 39 7 33 10 20 38 12 13 15 17 21 22 32 34 35 36 40 8 9 18 29 28 41; repairs no unit in particular

2026-11-03T00:04:26Z rescope · item add TOOL-dCalibratedLens-42 · reason spec-audit round 3 (reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) id 1 HIGH, item H1: unit 35 calls derive_record_kind with the signature TOOL-dTotalRecall-53 S21 replaced; repairs TOOL-dCalibratedLens-35

2026-11-03T00:04:28Z rescope · item add TOOL-dCalibratedLens-43 · reason spec-audit round 3 (reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) id 11 HIGH, item H2: read_loop_records lists with a glob that git ls-tree never matches; repairs TOOL-dCalibratedLens-3

2026-11-03T00:04:30Z rescope · item add TOOL-dCalibratedLens-44 · reason spec-audit round 3 (reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) id 12 HIGH, item H3 (shared with id 27): unit 31's guard admits a SPEC line that still carries its literal brackets; repairs TOOL-dCalibratedLens-31

2026-11-03T00:04:32Z rescope · item add TOOL-dCalibratedLens-45 · reason spec-audit round 3 (reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) id 27 HIGH, item H3 (shared with id 12): unit 31's staged break cannot go red on SPEC and leaves a render error unspecified; repairs TOOL-dCalibratedLens-31

2026-11-03T00:04:34Z rescope · item add TOOL-dCalibratedLens-46 · reason spec-audit round 3 (reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) id 22 HIGH, item H4: unit 41 widens three guards by hand-editing a rendered manifest; repairs TOOL-dCalibratedLens-41

2026-11-03T00:04:36Z rescope · item add TOOL-dCalibratedLens-47 · reason spec-audit round 3 (reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) id 23 HIGH, item H5: unit 37 adds AGENTS.md to a guard by hand-editing the rendered manifest; repairs TOOL-dCalibratedLens-37

2026-11-03T00:04:39Z rescope · item add TOOL-dCalibratedLens-48 · reason spec-audit round 3 (reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) minors batched into one unit, 16 MEDIUM and 9 LOW by raw id: 2 3 4 29 5 6 8 13 14 19 15 20 24 28 31 32 7 16 26 9 10 17 18 21 33; repairs no unit in particular

2026-11-03T00:46:27Z review · item dCalibratedLens-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 6 · minors 25 · disposition promote

2026-11-03T01:32:02Z rescope · item defer TOOL-dCalibratedLens-1 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:05Z rescope · item defer TOOL-dCalibratedLens-2 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:08Z rescope · item defer TOOL-dCalibratedLens-3 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:10Z rescope · item defer TOOL-dCalibratedLens-4 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:13Z rescope · item defer TOOL-dCalibratedLens-5 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:16Z rescope · item defer TOOL-dCalibratedLens-6 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:18Z rescope · item defer TOOL-dCalibratedLens-7 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:20Z rescope · item defer TOOL-dCalibratedLens-8 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:22Z rescope · item defer TOOL-dCalibratedLens-9 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:24Z rescope · item defer TOOL-dCalibratedLens-10 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:27Z rescope · item defer TOOL-dCalibratedLens-11 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:30Z rescope · item defer TOOL-dCalibratedLens-12 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:32Z rescope · item defer TOOL-dCalibratedLens-13 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:34Z rescope · item defer TOOL-dCalibratedLens-14 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:36Z rescope · item defer TOOL-dCalibratedLens-15 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:38Z rescope · item defer TOOL-dCalibratedLens-16 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:41Z rescope · item defer TOOL-dCalibratedLens-17 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:43Z rescope · item defer TOOL-dCalibratedLens-19 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:45Z rescope · item defer TOOL-dCalibratedLens-20 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:47Z rescope · item defer TOOL-dCalibratedLens-21 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:49Z rescope · item defer TOOL-dCalibratedLens-22 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:51Z rescope · item defer TOOL-dCalibratedLens-23 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:53Z rescope · item defer TOOL-dCalibratedLens-24 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:56Z rescope · item defer TOOL-dCalibratedLens-25 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:32:58Z rescope · item defer TOOL-dCalibratedLens-26 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:01Z rescope · item defer TOOL-dCalibratedLens-27 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:04Z rescope · item defer TOOL-dCalibratedLens-28 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:07Z rescope · item defer TOOL-dCalibratedLens-29 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:09Z rescope · item defer TOOL-dCalibratedLens-30 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:12Z rescope · item defer TOOL-dCalibratedLens-31 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:14Z rescope · item defer TOOL-dCalibratedLens-32 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:16Z rescope · item defer TOOL-dCalibratedLens-33 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:19Z rescope · item defer TOOL-dCalibratedLens-34 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:21Z rescope · item defer TOOL-dCalibratedLens-35 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:23Z rescope · item defer TOOL-dCalibratedLens-36 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:26Z rescope · item defer TOOL-dCalibratedLens-37 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:28Z rescope · item defer TOOL-dCalibratedLens-38 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:30Z rescope · item defer TOOL-dCalibratedLens-39 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:32Z rescope · item defer TOOL-dCalibratedLens-40 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:35Z rescope · item defer TOOL-dCalibratedLens-41 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:37Z rescope · item defer TOOL-dCalibratedLens-42 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:39Z rescope · item defer TOOL-dCalibratedLens-43 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:42Z rescope · item defer TOOL-dCalibratedLens-44 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:44Z rescope · item defer TOOL-dCalibratedLens-45 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:46Z rescope · item defer TOOL-dCalibratedLens-46 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:48Z rescope · item defer TOOL-dCalibratedLens-47 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18

2026-11-03T01:33:51Z rescope · item defer TOOL-dCalibratedLens-48 · reason spec run (README rule 1): specced and audited here; the build run after this one builds it, advancing TOOL-dCalibratedLens-18
