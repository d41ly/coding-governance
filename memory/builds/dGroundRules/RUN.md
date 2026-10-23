# dGroundRules - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
asks-at-landing: TOOL-dGroundRules-12=OPEN
units-at-landing: TOOL-dGroundRules-1 TOOL-dGroundRules-11 TOOL-dGroundRules-16 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-24 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-19 TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-9 TOOL-dGroundRules-15 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-25 TOOL-dGroundRules-29 TOOL-dGroundRules-27 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52
hold-run: 
hold-streak: 1 · at d794a81b
resume-owed: none · owner
held-at: 2026-10-23T04:30:23Z
hold-reason: The spec audit's promotion chain does not shrink: six rounds promoted 9, 4, 7, 2, 9 and 9 units (51 on the roster for 11 clauses) at precision 0.85-1.00, and M4 bounds the chain only by a round below the 0.5 floor, so whether to cap it, and where, is the parked decision; units 44-52 are specced and unaudited, units 1-43 audited
hold-until: owner
hold-code: owner-decision
held-from: REVIEWING
refreshed-at: 3708a705e834709f340a2d160f9acdf9c18b699f · handoff · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: d794a81bc493f73af152ed3e0732de119cea0bb0
phase: HELD
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dgroundrules-0e6f4a
anchor-kind: default-branch
cli-version: 2.1.304
lease-utc: 2026-10-22T22:12:53Z
pid-image: claude.exe
host: compeeto-agent
pid: 13172
session: b814b019-d9ae-4d0f-83be-8b1c25fb814d
keepalive: ccc970f5
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 3708a705e834709f340a2d160f9acdf9c18b699f
anchor-ref: refs/heads/main
base: 3708a705e834709f340a2d160f9acdf9c18b699f

## Parked

2026-10-22T23:38:53Z review · item dGroundRules-spec-set-r1 · reason verdict BLOCKED · blockers 2 · BOUNDED · highs 6 · minors 41 · disposition promote

2026-10-22T23:46:14Z rescope · item add TOOL-dGroundRules-13 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 1 at BLOCKER, item B1

2026-10-22T23:46:21Z rescope · item add TOOL-dGroundRules-14 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 31 at BLOCKER, item B1

2026-10-22T23:46:22Z rescope · item add TOOL-dGroundRules-15 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 2 at HIGH, item H1

2026-10-22T23:46:24Z rescope · item add TOOL-dGroundRules-16 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 4 at HIGH, item H2

2026-10-22T23:46:25Z rescope · item add TOOL-dGroundRules-17 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 37 at HIGH, item H2

2026-10-22T23:46:26Z rescope · item add TOOL-dGroundRules-18 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 13 at HIGH, item H3

2026-10-22T23:46:28Z rescope · item add TOOL-dGroundRules-19 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 32 at HIGH, item H4

2026-10-22T23:46:29Z rescope · item add TOOL-dGroundRules-20 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 finding id 35 at HIGH, item H5

2026-10-22T23:46:30Z rescope · item add TOOL-dGroundRules-21 · reason 2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1 minors batch: MEDIUM ids 3 5 6 7 8 9 14 15 16 17 18 19 21 24 25 27 33 34 36 38 39 40 41 42 44 45 47 48 49 50 51 52 53 and LOW ids 10 11 20 26 29 43 54 56

2026-10-23T00:49:32Z rescope · item add TOOL-dGroundRules-22 · reason 2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1 finding id 10 at HIGH, item H1

2026-10-23T00:49:33Z rescope · item add TOOL-dGroundRules-23 · reason 2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1 finding id 38 at HIGH, item H1

2026-10-23T00:49:35Z rescope · item add TOOL-dGroundRules-24 · reason 2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1 finding id 17 at HIGH, item H2

2026-10-23T00:49:36Z rescope · item add TOOL-dGroundRules-25 · reason 2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1 minors batch: MEDIUM ids 1 2 3 4 5 6 7 11 12 18 20 21 23 24 25 27 28 29 30 32 36 37 39 40 41 42 43 44 and LOW ids 8 9 14 15 16 19 22 26 33 34 35

2026-10-23T01:09:09Z review · item dGroundRules-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 3 · minors 39 · disposition promote

2026-10-23T01:43:52Z rescope · item add TOOL-dGroundRules-26 · reason 2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1 finding id 1 at HIGH, item H1

2026-10-23T01:43:53Z rescope · item add TOOL-dGroundRules-27 · reason 2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1 finding id 7 at HIGH, item H1

2026-10-23T01:43:55Z rescope · item add TOOL-dGroundRules-28 · reason 2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1 finding id 23 at HIGH, item H1

2026-10-23T01:43:56Z rescope · item add TOOL-dGroundRules-29 · reason 2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1 finding id 17 at HIGH, item H2

2026-10-23T01:43:57Z rescope · item add TOOL-dGroundRules-30 · reason 2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1 finding id 18 at HIGH, item H3

2026-10-23T01:43:58Z rescope · item add TOOL-dGroundRules-31 · reason 2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1 finding id 24 at HIGH, item H4

2026-10-23T01:43:59Z rescope · item add TOOL-dGroundRules-32 · reason 2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1 minors batch: MEDIUM ids 3 4 5 8 9 10 13 14 19 21 25 27 28 and LOW ids 6 11 12 15 16 22 29

2026-10-23T02:03:16Z review · item dGroundRules-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 6 · minors 20 · disposition promote

2026-10-23T02:40:16Z rescope · item add TOOL-dGroundRules-33 · reason 2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1 finding id 26 at HIGH, item H1

2026-10-23T02:40:22Z rescope · item add TOOL-dGroundRules-34 · reason 2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1 minors batch: MEDIUM ids 1 2 3 4 5 6 10 14 15 18 19 22 23 24 25 28 29 31 32 33 34 35 37 and LOW ids 7 8 9 11 12 13 16 17 20 21 27 30 36 38

2026-10-23T02:51:16Z review · item dGroundRules-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 1 · minors 37 · disposition promote

2026-10-23T03:17:40Z rescope · item add TOOL-dGroundRules-35 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 22 at HIGH, item H1

2026-10-23T03:17:42Z rescope · item add TOOL-dGroundRules-36 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 7 at HIGH, item H1

2026-10-23T03:17:43Z rescope · item add TOOL-dGroundRules-37 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 1 at HIGH, item H1

2026-10-23T03:17:44Z rescope · item add TOOL-dGroundRules-38 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 18 at HIGH, item H2

2026-10-23T03:17:45Z rescope · item add TOOL-dGroundRules-39 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 2 at HIGH, item H3

2026-10-23T03:17:47Z rescope · item add TOOL-dGroundRules-40 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 17 at HIGH, item H3

2026-10-23T03:17:48Z rescope · item add TOOL-dGroundRules-41 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 21 at HIGH, item H3

2026-10-23T03:17:49Z rescope · item add TOOL-dGroundRules-42 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 finding id 25 at HIGH, item H3

2026-10-23T03:17:50Z rescope · item add TOOL-dGroundRules-43 · reason 2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1 minors batch: MEDIUM ids 3 4 5 6 8 9 10 11 20 26 27 and LOW ids 12 13 15 16

2026-10-23T03:36:44Z review · item dGroundRules-spec-set-r5 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 8 · minors 15 · disposition promote

2026-10-23T03:38:33Z decision · item Cap the spec-audit promotion chain? Rounds 1-5 promoted 9, 4, 7, 2 and 9 units (the roster is 42), each round's precision 0.85-1.00, so M4's only bound, a round below the 0.5 floor, has not fired and the chain shows no shrink · reason Options: let the chain run until a round promotes nothing; cap it at a round, as the owner capped dTrueNorth's audit at round 2, the later promotions closing under a recorded specs-audited override; or lower the audit's intensity for promoted repair specs. Refused because a round cap is the owner's ruling (M4 states no cap, and dTrueNorth's cap was the owner's own words) and the run keeps auditing meanwhile

2026-10-23T04:02:01Z review · item dGroundRules-spec-set-r6 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 7 · minors 25 · disposition promote

2026-10-23T04:13:55Z rescope · item add TOOL-dGroundRules-44 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 29 at BLOCKER, item B1

2026-10-23T04:13:56Z rescope · item add TOOL-dGroundRules-45 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 20 at HIGH, item H1

2026-10-23T04:13:57Z rescope · item add TOOL-dGroundRules-46 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 10 at HIGH, item H1

2026-10-23T04:13:58Z rescope · item add TOOL-dGroundRules-47 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 1 at HIGH, item H1

2026-10-23T04:14:00Z rescope · item add TOOL-dGroundRules-48 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 2 at HIGH, item H2

2026-10-23T04:14:01Z rescope · item add TOOL-dGroundRules-49 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 11 at HIGH, item H2

2026-10-23T04:14:03Z rescope · item add TOOL-dGroundRules-50 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 22 at HIGH, item H2

2026-10-23T04:14:04Z rescope · item add TOOL-dGroundRules-51 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 finding id 21 at HIGH, item H3

2026-10-23T04:14:05Z rescope · item add TOOL-dGroundRules-52 · reason 2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1 minors batch: MEDIUM ids 3 4 5 6 12 13 14 15 19 25 26 30 31 33 35 36 and LOW ids 7 8 9 16 17 18 34 37 38

2026-10-23T04:30:26Z handoff · item owner-decision · reason in the run worktree: bash tools/push-main.sh --prepare --slug dGroundRules && bash tools/push-main.sh --land --slug dGroundRules && bash tools/unattended/unattended.sh --settle dGroundRules

2026-10-23T04:30:26Z hold · item owner-decision · reason until owner · reaped ccc970f5 · resume none(owner)
