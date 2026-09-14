# aProbedUnit - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 23e302e4508e5956b38bed115ba921fdd670d041
phase: BUILDING
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
