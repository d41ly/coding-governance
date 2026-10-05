# aGraftedHelix - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 9d35d64743c2a416a918eb1b8fcf7a89f2163b23
phase: BUILDING
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

2026-10-04T20:29:43Z review · item aGraftedHelix-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-10-04T20:57:58Z rescope · item add TOOL-aGraftedHelix-24 · reason spec-audit of unit 23 round 1 id 11 HIGH, id 6 HIGH and id 1 HIGH: unit 23 adds to the prior-session set after write_lease has moved the record's session, so an interrupted call leaves the claim under a session no member names, and its restart and --hold criteria run where the same-session row answers before the widening they certify is reached; repairs TOOL-aGraftedHelix-23

2026-10-04T21:05:46Z review · item aGraftedHelix-spec-set-r5 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-10-04T21:33:35Z rescope · item add TOOL-aGraftedHelix-25 · reason spec-audit of unit 24 round 1 id 11 HIGH: unit 24 moves the prior-session add ahead of write_lease but states no rule for the add's own failure, so a build that continues into write_lease after a failed add leaves the claim under a session no member names and the next call answers check 90; repairs TOOL-aGraftedHelix-24

2026-10-04T21:39:13Z review · item aGraftedHelix-spec-set-r6 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-10-04T22:04:47Z rescope · item add TOOL-aGraftedHelix-26 · reason spec-audit of unit 25 round 1 id 5 HIGH, id 8 HIGH and id 6 HIGH: the add's return 1 never reaches the --resume exit because only fail sets status, so AC1's exit assertion reds a correct build, and AC1 drives only the CAS-incomplete one of the add's two triggers; repairs TOOL-aGraftedHelix-25

2026-10-04T22:18:59Z review · item aGraftedHelix-spec-set-r7 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · disposition promote

2026-10-04T22:19:36Z decision · item Build a check-arms.py class gate that discovers a delegated dispatch block setting status=1 with no fail call (checks 24, 27, 28 share the shape), the second discovery signature ask TOOL-aDeferredBar-8 names? · reason options: build it in this run, or keep the documented check (unit 13's presence-probe gotcha); refused: a gate is its own mechanism, the finding was MEDIUM (folded, never promoted), and it would red check 24's block, which no unit here touches; owner ruling 2026-10-05 leaves further findings to the closing review

2026-10-04T22:22:17Z dispatch · item 2de21d28 TOOL-aGraftedHelix-1 · reason tools/unattended/unattended.sh tools/unattended/resume-tick.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/SKILL.template.md tools/unattended/.unattended.conf.example tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/guides/SESSION-KICKOFF.md memory/map/features/unattended-stops.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/kit.toml memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated

2026-10-04T22:22:24Z brief · item TOOL-aGraftedHelix-1 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T00:02:57Z dispatch · item 04714367 TOOL-aGraftedHelix-1 · reason tools/unattended/unattended.sh tools/unattended/resume-tick.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/SKILL.template.md tools/unattended/.unattended.conf.example tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/guides/SESSION-KICKOFF.md memory/map/features/unattended-stops.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/kit.toml memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-1.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated memory/backlog/TOOL.md

2026-10-05T00:11:16Z dispatch · item 3ec8b807 TOOL-aGraftedHelix-10 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-10.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md memory/gotchas/INDEX.md .claude/skills/unattended/SKILL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/SKILL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/kit.toml memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated memory/guides/SESSION-KICKOFF.md

2026-10-05T00:11:25Z brief · item TOOL-aGraftedHelix-10 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T00:42:37Z dispatch · item 01282da3 TOOL-aGraftedHelix-11 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-11.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh .claude/skills/unattended/SKILL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/SKILL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/kit.toml memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated memory/guides/SESSION-KICKOFF.md

2026-10-05T00:42:47Z brief · item TOOL-aGraftedHelix-11 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T01:22:09Z dispatch · item b5d9532e TOOL-aGraftedHelix-12 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-12.md tools/unattended/unattended.test.sh .claude/skills/unattended/SKILL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/SKILL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/unattended.sh tools/unattended/kit.toml memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated memory/guides/SESSION-KICKOFF.md

2026-10-05T01:22:16Z brief · item TOOL-aGraftedHelix-12 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T01:51:01Z dispatch · item 98ce1e96 TOOL-aGraftedHelix-2 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-2.md skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/map/features/session-kickoff.md memory/map/generated memory/guides/SESSION-KICKOFF.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T01:51:04Z brief · item TOOL-aGraftedHelix-2 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T02:31:53Z dispatch · item 9747c9b8 TOOL-aGraftedHelix-18 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-18.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh .claude/skills/unattended/SKILL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/SKILL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/kit.toml memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated memory/guides/SESSION-KICKOFF.md

2026-10-05T02:32:00Z brief · item TOOL-aGraftedHelix-18 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T02:53:05Z dispatch · item c8a16598 TOOL-aGraftedHelix-19 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh .claude/skills/unattended/SKILL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/SKILL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/kit.toml memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated memory/guides/SESSION-KICKOFF.md

2026-10-05T02:53:13Z brief · item TOOL-aGraftedHelix-19 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T03:20:41Z dispatch · item e78ce89d TOOL-aGraftedHelix-3 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md tools/memory-tree/gotchas.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/HYGIENE.template.md tools/memory-tree/ANNOTATION-STYLE.template.md tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/README.md tools/memory-tree/.memory-tree.conf.example tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/README.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md memory/guides/BUILD-METHOD.md memory/guides/SESSION-KICKOFF.md memory/gotchas/canary-waits-on-a-rendezvous-not-a-clock.md memory/gotchas/sweep-issues-no-cost-verdict.md memory/gotchas/concurrent-runs-are-announced-not-refused.md memory/map/features/run-gates.md memory/map/features/unattended.md memory/map/features/review-harnesses.md memory/map/generated .memory-tree.conf memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T03:20:51Z brief · item TOOL-aGraftedHelix-3 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T03:39:37Z dispatch · item e78ce89d TOOL-aGraftedHelix-3 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-3.md tools/memory-tree/gotchas.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/HYGIENE.template.md tools/memory-tree/ANNOTATION-STYLE.template.md tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/README.md tools/memory-tree/.memory-tree.conf.example tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/README.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md memory/guides/BUILD-METHOD.md memory/guides/SESSION-KICKOFF.md memory/gotchas/canary-waits-on-a-rendezvous-not-a-clock.md memory/gotchas/sweep-issues-no-cost-verdict.md memory/gotchas/concurrent-runs-are-announced-not-refused.md memory/map/features/run-gates.md memory/map/features/unattended.md memory/map/features/unattended-mandate.md memory/map/features/review-harnesses.md memory/map/generated .memory-tree.conf memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-05T03:54:42Z rescope · item add TOOL-aGraftedHelix-27 · reason discovery in the unit-3 pass: inside the commit-msg hook GIT_DIR is set, resolve_generated_indexes finds no kit outputs, so --check-commit refuses a regenerated index that --dispatch check 49 refuses to declare beside its generator; INDEX.md landed after the build commit

2026-10-05T03:54:45Z rescope · item add TOOL-aGraftedHelix-28 · reason discovery in the unit-3 pass: the by-design block header is spelled in gotchas.py and in tier2-review.template.js with no gate holding them equal; a reworded header empties the review's by-design list silently

2026-10-05T04:26:24Z dispatch · item 72b04279 TOOL-aGraftedHelix-27 · reason memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-27.md tools/unattended/lib-unattended.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/README.md tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/SKILL.template.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-ASKS.md memory/guides/PLAYBOOK-TEMPLATE.md .claude/skills/unattended/SKILL.md memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md memory/map/features/unattended-mandate.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md

2026-10-05T04:26:30Z brief · item TOOL-aGraftedHelix-27 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T04:51:35Z dispatch · item 77cdc810 TOOL-aGraftedHelix-20 · reason memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md tools/unattended/unattended.sh tools/unattended/lib-unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md .claude/skills/unattended/SKILL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md

2026-10-05T04:51:42Z brief · item TOOL-aGraftedHelix-20 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md
