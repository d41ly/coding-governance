# aGraftedHelix - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: b3a5e2ecf798e53857c882e695883fb59ecda8d9
phase: REVIEWING
branch-sha: 5266d22eba31cdbf15425773d245cd23d7b9cdf5
branch-ref: refs/heads/branch/helixir-review-gov-adoption-ce32e1
spec-audit: 2026-10-04
may: none
mode: prompt
run-branch: refs/heads/branch/helixir-review-gov-adoption-ce32e1
anchor-kind: run-branch
lease-utc: 2026-10-04T15:42:10Z
pid-image: claude.exe
host: compeeto-agent
pid: 3932
session: 1b37a234-acee-4cd7-8267-704d25af99be
keepalive: 90b28c46
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: ac65de998f094a244540905b35d7c5f6880ab850
anchor-ref: refs/heads/main
base: 5266d22eba31cdbf15425773d245cd23d7b9cdf5

## Parked

2026-10-04T15:45:33Z rescope · item add TOOL-aGraftedHelix-9 · reason M2 decompose: unit 6 named two mechanisms, an exact content-key check (memory-tree) and a near-match relation check (recall index); one mechanism per spec splits them

2026-10-04T17:06:16Z review · item aGraftedHelix-spec-set-r1 · reason verdict BLOCKED · blockers 2 · BOUNDED · disposition promote

2026-10-04T17:15:16Z rescope · item add TOOL-aGraftedHelix-10 · reason spec-audit round 1 id 38 BLOCKER and id 31 HIGH: the claim push names a URL, and the tracked pre-push hook refuses a URL push wherever GOV_DEFAULT_BRANCH is unset; repairs TOOL-aGraftedHelix-1

2026-10-04T17:15:19Z rescope · item add TOOL-aGraftedHelix-11 · reason spec-audit round 1 id 39 BLOCKER: --beat from the OS-scheduled tick rewrites the claim's session to absent, and the holder then reads its own claim as foreign; repairs TOOL-aGraftedHelix-1

2026-10-04T17:15:23Z rescope · item add TOOL-aGraftedHelix-12 · reason spec-audit round 1 id 2 HIGH and id 3 HIGH: the refusing cells of the claim write table and the writes --beat declines have no criterion; repairs TOOL-aGraftedHelix-1

2026-10-04T17:15:26Z rescope · item add TOOL-aGraftedHelix-13 · reason spec-audit round 1 id 20 HIGH: the hygiene engine's dispatch of check 28 is observed only by a grep that a comment satisfies; repairs TOOL-aGraftedHelix-6

2026-10-04T17:15:30Z rescope · item add TOOL-aGraftedHelix-14 · reason spec-audit round 1 id 27 HIGH: the hygiene engine's dispatch of check 27 is observed only by a grep that a comment satisfies; repairs TOOL-aGraftedHelix-9

2026-10-04T17:36:04Z rescope · item add TOOL-aGraftedHelix-15 · reason discovery while driving the harness: a build whose specs the SPEC stage authors always meets the AUDIT stage's empty-subject refusal on the first call (the specs are uncommitted), and the documented re-invoke under resumeFromRunId replays the resolver's cached empty answer; observed twice on wf_7b67cf1d-995 (the second failure in 20 ms); the route completed only with caller-pinned subjects

2026-10-04T18:36:21Z rescope · item add TOOL-aGraftedHelix-16 · reason spec-audit of units 10 to 15 round 1 id 21 HIGH: the commit stage stages the authored specs before the generator rewrites them, so the commit holds pre-render blobs and the dirty-tree refusal fires on the first call; repairs TOOL-aGraftedHelix-15

2026-10-04T18:36:31Z rescope · item add TOOL-aGraftedHelix-17 · reason spec-audit of units 10 to 15 round 1 id 16 HIGH: unit 14's fixture row restates a base row, so unit 6's check 28 reds the same branch and the permanent arm cannot fail once unit 6 lands; repairs TOOL-aGraftedHelix-14

2026-10-04T18:36:34Z rescope · item add TOOL-aGraftedHelix-18 · reason spec-audit of units 10 to 15 round 1 id 22 HIGH: the holder row's write_lease moves the lease facts mid-call and unit 11 states no read-before-write order, so a holder whose session changed reads its own claim as foreign live; repairs TOOL-aGraftedHelix-11

2026-10-04T18:36:36Z rescope · item add TOOL-aGraftedHelix-19 · reason spec-audit of units 10 to 15 round 1 id 31 HIGH: unit 12's arm keeps a hand-typed copy of the claim write table, so a verdict or mode added later leaves it green while the record calls it the class gate; repairs TOOL-aGraftedHelix-12

2026-10-04T18:52:42Z review · item aGraftedHelix-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-10-04T19:26:41Z rescope · item add TOOL-aGraftedHelix-20 · reason spec-audit of units 16 to 19 round 1 id 9 HIGH: unit 18 runs write_lease before the claim CAS, so a changed-session holder call whose claim push does not complete leaves the record and the claim naming different sessions, and the next call refuses its own claim with check 90; repairs TOOL-aGraftedHelix-18

2026-10-04T19:26:51Z rescope · item add TOOL-aGraftedHelix-21 · reason spec-audit of units 16 to 19 round 1 id 22 HIGH and id 17 HIGH: the delta loop lists untracked paths in another mode than the pre-stage record holds them, so a wholly untracked foreign directory is staged whole, and it filters by a shell variable that nothing keeps across a split block, so every changed path is staged; repairs TOOL-aGraftedHelix-16

2026-10-04T19:26:54Z rescope · item add TOOL-aGraftedHelix-22 · reason spec-audit of units 16 to 19 round 1 id 6 HIGH: unit 19's read-axis refusal has no criterion, so a build that omits it passes every criterion and the derived arm stays green over an uncovered cell; repairs TOOL-aGraftedHelix-19

2026-10-04T19:44:17Z review · item aGraftedHelix-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-10-04T20:16:20Z rescope · item add TOOL-aGraftedHelix-23 · reason spec-audit of units 20 to 22 round 1 id 6 HIGH, id 12 HIGH, id 2 HIGH, id 7 HIGH and id 1 HIGH: unit 20's prior-session fact stays sticky while other writers land the claim under a new session, no criterion drives two incomplete holder calls in a row, a stored absent session reads as no fact, and the widened mine test is driven only at --resume, so a live run reads its own claim as foreign and is forced to claim-lost; repairs TOOL-aGraftedHelix-20
