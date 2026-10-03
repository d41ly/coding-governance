# aWindowedPass - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 886b089dfd9c4bf98dc2024e21d7d9607f9b5cc0
phase: BUILDING
branch-sha: 886b089dfd9c4bf98dc2024e21d7d9607f9b5cc0
branch-ref: refs/heads/branch/undeclared-write-windowed-pass
may: none
mode: prompt
run-branch: refs/heads/branch/undeclared-write-windowed-pass
anchor-kind: run-branch
lease-utc: 2026-10-03T21:19:31Z
pid-image: claude.exe
host: compeeto-agent
pid: 19276
session: 81a68c77-3260-4c90-95a0-32da7860d03f
keepalive: f0205861
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: a587e82dc6180a9a720560e1633995e47734803a
anchor-ref: refs/heads/main
base: 886b089dfd9c4bf98dc2024e21d7d9607f9b5cc0

## Parked

2026-10-03T21:29:03Z brief · item TOOL-aWindowedPass-1 · reason 0c50a7ac8dcd memory/builds/aWindowedPass/prompts/2026-10-04-prompt-TOOL-aWindowedPass-1-2-build-brief.md

2026-10-03T21:29:07Z brief · item TOOL-aWindowedPass-2 · reason 83a93b978927 memory/builds/aWindowedPass/prompts/2026-10-04-prompt-TOOL-aWindowedPass-2-2-build-brief.md

2026-10-03T21:29:11Z brief · item TOOL-aWindowedPass-3 · reason 7f0dd8d46f9a memory/builds/aWindowedPass/prompts/2026-10-04-prompt-TOOL-aWindowedPass-3-2-build-brief.md

2026-10-03T21:29:15Z brief · item TOOL-aWindowedPass-4 · reason 5fa84d02b7ec memory/builds/aWindowedPass/prompts/2026-10-04-prompt-TOOL-aWindowedPass-4-2-build-brief.md

2026-10-03T21:29:19Z brief · item TOOL-aWindowedPass-5 · reason 36fa8d9cd2c1 memory/builds/aWindowedPass/prompts/2026-10-04-prompt-TOOL-aWindowedPass-5-2-build-brief.md

2026-10-03T21:45:29Z dispatch · item b22c4ad7 TOOL-aWindowedPass-4 · reason tools/unattended/lib-unattended.sh tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/memory-tree/kit.toml tools/codebase-map/kit.toml tools/govkit/govkit.py tools/govkit/selftest.py .unattended.conf memory/builds/aWindowedPass/spec/2026-10-04-spec-TOOL-aWindowedPass-4.md memory/builds/aWindowedPass/README.md memory/guides/SESSION-KICKOFF.md

2026-10-03T21:59:08Z dispatch · item 75cd13f7 TOOL-aWindowedPass-2 · reason tools/unattended/lib-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/check-unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/workflows/unattended-unit.js memory/builds/aWindowedPass/spec/2026-10-04-spec-TOOL-aWindowedPass-2.md memory/builds/aWindowedPass/README.md

2026-10-03T22:44:19Z dispatch · item 55213dd2 TOOL-aWindowedPass-1 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aWindowedPass/spec/2026-10-04-spec-TOOL-aWindowedPass-1.md memory/builds/aWindowedPass/README.md

2026-10-03T23:07:02Z dispatch · item c5582706 TOOL-aWindowedPass-5 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh tools/unattended/cross-component.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/README.md .unattended.conf memory/guides/SESSION-KICKOFF.md memory/builds/aWindowedPass/spec/2026-10-04-spec-TOOL-aWindowedPass-5.md memory/builds/aWindowedPass/README.md
