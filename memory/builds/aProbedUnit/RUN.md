# aProbedUnit - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 15697d570746e47629013a10f11548fab0c5262b
phase: REVIEWING
branch-sha: 1b000d1a83998506bd2199cc815e34a9b82cdbf0
branch-ref: refs/heads/branch/unattended-build-stalls-6d0f2b
mode: prompt
anchor-kind: run-branch
keepalive: 0f1dca63
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 6074d521d6ae3fa8274a493f3b7a9be6b1274109
anchor-ref: refs/heads/main
base: 1b000d1a83998506bd2199cc815e34a9b82cdbf0

## Parked

2026-09-14T11:15:30Z review · item aProbedUnit-spec-set · reason verdict BLOCKED · blockers 3

2026-09-14T12:22:33Z review · item aProbedUnit-spec-set · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-14T12:40:59Z dispatch · item 23e302e4 TOOL-aProbedUnit-1 · reason tools/workflows/unattended-unit.js tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/workflows/unattended-build.test.sh memory/guides/SESSION-KICKOFF.md memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-1.md memory/builds/aProbedUnit/README.md memory/LIVE.md memory/ledger/2026-09.md memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-1-1-acceptance-ledger.md

2026-09-14T12:41:06Z brief · item TOOL-aProbedUnit-1 · reason 21e8b7ee8d3b memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-2-build-brief.md

2026-09-14T12:48:04Z dispatch · item a69c95b4 TOOL-aProbedUnit-2 · reason tools/workflows/unattended-unit.js tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/workflows/unattended-build.test.sh memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-2.md memory/builds/aProbedUnit/README.md memory/LIVE.md memory/ledger/2026-09.md memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-2-1-acceptance-ledger.md

2026-09-14T12:48:08Z brief · item TOOL-aProbedUnit-2 · reason 7b6a6f80583a memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-2-1-build-brief.md

2026-09-14T12:54:38Z dispatch · item 0f129179 TOOL-aProbedUnit-3 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/unattended/PROTOCOL.template.md tools/unattended/kit.toml tools/unattended/.unattended.conf.example .claude/skills/unattended/SKILL.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md .unattended.conf memory/guides/SESSION-KICKOFF.md memory/map/features/unattended.md memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-3.md memory/builds/aProbedUnit/README.md memory/LIVE.md memory/ledger/2026-09.md memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-3-1-acceptance-ledger.md

2026-09-14T12:54:44Z brief · item TOOL-aProbedUnit-3 · reason 2eca58a01da8 memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-3-1-build-brief.md

2026-09-14T13:34:02Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason tools/workflows/unattended-build.template.js

2026-09-14T13:34:09Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason tools/workflows/unattended-build.js

2026-09-14T13:34:16Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason tools/workflows/unattended-unit.js

2026-09-14T13:34:23Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason tools/workflows/unattended-build.test.sh

2026-09-14T13:34:30Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason tools/unattended/SKILL.template.md

2026-09-14T13:34:38Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason .claude/skills/unattended/SKILL.md

2026-09-14T13:34:45Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason memory/map/features/review-harnesses.md

2026-09-14T13:34:54Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-4.md

2026-09-14T13:35:03Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-4-1-acceptance-ledger.md

2026-09-14T13:35:12Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason memory/builds/aProbedUnit/README.md

2026-09-14T13:35:22Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason memory/LIVE.md

2026-09-14T13:35:33Z dispatch · item b7250a7f TOOL-aProbedUnit-4 · reason memory/ledger/2026-09.md

2026-09-14T13:35:38Z brief · item TOOL-aProbedUnit-4 · reason 7a71fffc7608 memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-4-1-build-brief.md

2026-09-14T13:55:23Z dispatch · item 5049e2ab TOOL-aProbedUnit-5 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/README.md memory/map/generated/symbols.json memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-5.md memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-5-1-acceptance-ledger.md memory/builds/aProbedUnit/README.md

2026-09-14T13:55:33Z brief · item TOOL-aProbedUnit-5 · reason 2b8b1dac6546 memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-5-1-build-brief.md

2026-09-14T14:12:52Z dispatch · item 947d54fe TOOL-aProbedUnit-6 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md .claude/skills/unattended/SKILL.md tools/unattended/kit.toml tools/unattended/.unattended.conf.example .unattended.conf tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md memory/guides/SESSION-KICKOFF.md memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-6.md memory/builds/aProbedUnit/README.md memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-6-1-acceptance-ledger.md

2026-09-14T14:13:00Z brief · item TOOL-aProbedUnit-6 · reason 146308d2fdc7 memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-6-1-build-brief.md

2026-09-14T14:34:52Z dispatch · item 47b29bb9 TOOL-aProbedUnit-7 · reason tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md .claude/skills/unattended/SKILL.md memory/guides/UNATTENDED-VERBS.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/guides/SESSION-KICKOFF.md memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-7.md memory/builds/aProbedUnit/README.md memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-7-1-acceptance-ledger.md

2026-09-14T14:34:59Z brief · item TOOL-aProbedUnit-7 · reason 1c346e045751 memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-7-1-build-brief.md

2026-09-14T15:35:15Z review · item aProbedUnit · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED
