# aGraftedHelix - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 7dca26485330e71ec546c9c2d5625f32ba038c15
phase: BUILDING
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
