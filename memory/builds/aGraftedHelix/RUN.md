# aGraftedHelix - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: 290d0d2d5ae893a2d723a2247ad788035d3bffdf · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 071c32bce76b2a3fe2d384504739235e574b0dd1
phase: VERIFYING
branch-sha: 018b5675727d4c3f316e5b6c53b11c688f03a472
branch-ref: refs/heads/branch/helixir-review-gov-adoption-ce32e1
may: none
mode: prompt
run-branch: refs/heads/branch/helixir-review-gov-adoption-ce32e1
anchor-kind: run-branch
lease-utc: 2026-10-05T17:04:11Z
pid-image: claude.exe
host: compeeto-agent
pid: 3932
session: 1b37a234-acee-4cd7-8267-704d25af99be
keepalive: 199408b7
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 290d0d2d5ae893a2d723a2247ad788035d3bffdf
anchor-ref: refs/heads/main
base: 018b5675727d4c3f316e5b6c53b11c688f03a472

## Parked

2026-10-05T17:41:17Z rescope · item add TOOL-aGraftedHelix-33 · reason discovery on the spec-commit stage's first live use (wf_dff1cb65-954): writers reported authored specs as ids (unit 29) and as paths (30-32); the commit stage matched ids alone, committed one of four specs, and handed out a roster with three MISSING units and no refusal

2026-10-05T17:43:49Z brief · item TOOL-aGraftedHelix-29 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T17:49:32Z dispatch · item 489f1ec7 TOOL-aGraftedHelix-29 · reason tools/memory-tree/gotchas.py tools/memory-tree/README.md tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/ANNOTATION-STYLE.template.md memory/guides/BUILD-METHOD.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md memory/gotchas/inputs-inside-the-subjects-reach.md tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/tier2-review.test.sh tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/README.md memory/map/features/memory-tree-hygiene.md memory/map/generated memory/guides/SESSION-KICKOFF.md memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-29.md memory/builds/aGraftedHelix/build/2026-10-04-build-TOOL-aGraftedHelix-29-1-acceptance-ledger.md memory/builds/aGraftedHelix/README.md

2026-10-05T18:18:18Z brief · item TOOL-aGraftedHelix-30 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T18:19:16Z dispatch · item 65b45487 TOOL-aGraftedHelix-30 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/README.md tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-ASKS.md memory/guides/PLAYBOOK-TEMPLATE.md .claude/skills/unattended/SKILL.md memory/gotchas/a-merged-in-check-can-refuse-a-pinned-record.md memory/gotchas/INDEX.md memory/map/features/unattended-mandate.md memory/map/generated memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-30.md memory/builds/aGraftedHelix/build/2026-10-04-build-TOOL-aGraftedHelix-30-1-acceptance-ledger.md memory/builds/aGraftedHelix/README.md

2026-10-05T18:41:49Z brief · item TOOL-aGraftedHelix-31 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T18:43:22Z dispatch · item c54278c1 TOOL-aGraftedHelix-31 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/README.md tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-ASKS.md memory/guides/PLAYBOOK-TEMPLATE.md .claude/skills/unattended/SKILL.md memory/map/features/unattended-mandate.md memory/map/generated memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-31.md memory/builds/aGraftedHelix/build/2026-10-04-build-TOOL-aGraftedHelix-31-1-acceptance-ledger.md memory/builds/aGraftedHelix/README.md

2026-10-05T19:36:06Z rescope · item add TOOL-aGraftedHelix-29 · reason re-recorded after the rotation: promoted by closing review round 1 and added under the previous record, now RUN.ABORTED.6410435d.md, whose rescope row this repeats so the live record carries it

2026-10-05T19:36:20Z rescope · item add TOOL-aGraftedHelix-30 · reason re-recorded after the rotation: promoted by closing review round 1 and added under the previous record, now RUN.ABORTED.6410435d.md, whose rescope row this repeats so the live record carries it

2026-10-05T19:36:38Z rescope · item add TOOL-aGraftedHelix-31 · reason re-recorded after the rotation: promoted by closing review round 1 and added under the previous record, now RUN.ABORTED.6410435d.md, whose rescope row this repeats so the live record carries it

2026-10-05T19:36:52Z rescope · item add TOOL-aGraftedHelix-32 · reason re-recorded after the rotation: promoted by closing review round 1 and added under the previous record, now RUN.ABORTED.6410435d.md, whose rescope row this repeats so the live record carries it

2026-10-05T19:38:59Z brief · item TOOL-aGraftedHelix-32 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T19:40:52Z dispatch · item e79a2072 TOOL-aGraftedHelix-32 · reason tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/check-workflow-syntax.js tools/workflows/check_by_design_parity.py tools/workflows/check-protocol-parity.test.sh tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/tier2-review.test.sh tools/workflows/README.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/unarmed-branches.txt tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/README.md tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-ASKS.md memory/guides/PLAYBOOK-TEMPLATE.md .claude/skills/unattended/SKILL.md skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md tools/memory-recall/selftest.py tools/memory-recall/README.md tools/memory-recall/recall_conf.py tools/memory-tree/row_grammar.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/ANNOTATION-STYLE.template.md tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/SPEC-TEMPLATE.template.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md memory/guides/BUILD-METHOD.md memory/map/features/unattended-stops.md memory/map/features/review-harnesses.md memory/map/features/session-kickoff.md memory/map/generated memory/gotchas/decision-re-derived-by-a-second-process.md memory/gotchas/destructive-step-before-its-precondition.md memory/gotchas/a-spelling-change-strands-its-readers.md memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md memory/gotchas/orchestrator-hand-off-owed-a-disposition.md memory/gotchas/INDEX.md memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-32.md memory/builds/aGraftedHelix/build/2026-10-04-build-TOOL-aGraftedHelix-32-1-acceptance-ledger.md memory/builds/aGraftedHelix/README.md

2026-10-05T20:21:42Z decision · item location-probe-class-gate · reason question: adopt the location-probe class gate unit 27 handed to this run's orchestrator, or park it; options: build it inside unit 32, adopt it as a new unit, park it; reason: inside unit 32 it is a second mechanism with its own population and home, which M2 makes a unit of its own, a new unit id is the orchestrator's to mint and that unit's writer may not, and no line predicate discriminates the class, since 26 probes measured at f0971667 differ only in whether a hook can reach them, a question about callers, so M12 rejects a test that cannot change the pick; the orchestrator or the owner may still adopt it

2026-10-05T21:09:13Z brief · item TOOL-aGraftedHelix-33 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T21:09:48Z dispatch · item 0bc5f0f8 TOOL-aGraftedHelix-33 · reason tools/workflows memory/map/generated memory/map/features/review-harnesses.md memory/guides/SESSION-KICKOFF.md memory/builds/aGraftedHelix/spec/2026-10-06-spec-TOOL-aGraftedHelix-33.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md

2026-10-05T21:40:52Z rescope · item add TOOL-aGraftedHelix-34 · reason discovery at VERIFYING: the owed unattended suites ran pooled on a frozen clone at 90a6f6fae and came back red (driver 12 arms, cross-component 1, gate shard 1 one, shard 8 killed after a fixture no-op, resume-tick 2); the Definition of Done cannot be met with them red, so the fixes join the build

2026-10-05T23:14:44Z brief · item TOOL-aGraftedHelix-34 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-05T23:15:20Z dispatch · item bd1f7d6b TOOL-aGraftedHelix-34 · reason tools/unattended tools/gate-legs.json memory/guides .claude/skills/unattended/SKILL.md memory/map memory/gotchas memory/builds/aGraftedHelix/spec/2026-10-06-spec-TOOL-aGraftedHelix-34.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md

2026-10-05T23:44:10Z dispatch · item bd1f7d6b TOOL-aGraftedHelix-34 · reason tools/unattended tools/gate-legs.json memory/guides .claude/skills/unattended/SKILL.md memory/map memory/gotchas memory/builds/aGraftedHelix/spec/2026-10-06-spec-TOOL-aGraftedHelix-34.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md tools/run-gates/selftest-budgets.txt memory/LIVE.md memory/ledger/2026-10.md

2026-10-06T01:52:42Z review · item aGraftedHelix · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 14 · disposition promote

2026-10-06T01:52:45Z rescope · item add TOOL-aGraftedHelix-35 · reason H1 (rotated run's closing review round 1, ids 1 and 18): the spec-audit route still merges a by-design block read at the spec commit's parent, inside the build, so a build-added invariant can exempt the specs it audits

2026-10-06T01:52:47Z rescope · item add TOOL-aGraftedHelix-36 · reason the rotated run's closing review round 1's MEDIUM and LOW findings M2-M7 and L1-L3, batched into one unit by the owner's promote-every-finding ruling; M1 is the HIGH's own defect and closes with it

2026-10-06T02:23:22Z brief · item TOOL-aGraftedHelix-35 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-06T02:24:29Z dispatch · item 7a8b2173 TOOL-aGraftedHelix-35 · reason tools/workflows tools/memory-tree memory/guides memory/map memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/builds/aGraftedHelix/spec/2026-10-06-spec-TOOL-aGraftedHelix-35.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md

2026-10-06T02:41:25Z brief · item TOOL-aGraftedHelix-36 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-06T02:42:03Z dispatch · item b56ec1fd TOOL-aGraftedHelix-36 · reason tools/unattended tools/workflows tools/memory-tree tools/push-main.sh tools/push-main.test.sh tools/check-wiring.sh tools/check-wiring.test.sh tools/check-wiring.fragment.json tools/govkit/entries memory/gotchas/decision-re-derived-by-a-second-process.md memory/gotchas/orchestrator-hand-off-owed-a-disposition.md memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md memory/guides .claude/skills/unattended/SKILL.md memory/map memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/builds/aGraftedHelix/spec/2026-10-06-spec-TOOL-aGraftedHelix-36.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md

2026-10-06T03:34:28Z decision · item unit-34-close-handoff · reason question: who runs unit 34's hand-off to the close, the pooled calibration of the five receiving shards and the eight-shard identity; options: a unit of this build, or the main loop at VERIFYING; reason: both are suite runs, which no pass may perform, and the unattended kit's README already makes the pooled suites the DoD for work touching the kit, so the close owns them

2026-10-06T04:01:34Z rescope · item add TOOL-aGraftedHelix-37 · reason discovery by unit 36's builder, left unfixed: two writers finding one stale claim-push.lock at the same moment can both break and take it, because the break is rm -rf then mkdir with no re-check; the mandate brings it into the build

2026-10-06T04:34:33Z brief · item TOOL-aGraftedHelix-37 · reason a2e60ebbeb07 memory/builds/aGraftedHelix/prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md

2026-10-06T04:35:10Z dispatch · item 83afdc95 TOOL-aGraftedHelix-37 · reason tools/unattended tools/push-main.sh tools/push-main.test.sh memory/gotchas/decision-re-derived-by-a-second-process.md memory/guides .claude/skills/unattended/SKILL.md memory/map memory/builds/aGraftedHelix/spec/2026-10-06-spec-TOOL-aGraftedHelix-37.md memory/builds/aGraftedHelix/build memory/builds/aGraftedHelix/README.md
