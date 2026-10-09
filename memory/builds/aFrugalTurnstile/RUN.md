# aFrugalTurnstile - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 4f363647191177c6b838bd024c76e8d9dc03cf1b
phase: BUILDING
branch-sha: bef97330574caabfd43c374dbe8c39b26c560203
branch-ref: refs/heads/branch/awesome-cannon-44b2b1
may: none
mode: prompt
run-branch: refs/heads/branch/awesome-cannon-44b2b1
anchor-kind: run-branch
cli-version: 2.1.293
lease-utc: 2026-10-09T17:10:47Z
pid-image: claude.exe
host: compeeto-agent
pid: 34476
session: c43608a7-c8e7-4081-be42-83f438359a45
keepalive: 01835c71
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 5a836bf0fc940029136b4b3fd57a87f35ff40f26
anchor-ref: refs/heads/main
base: bef97330574caabfd43c374dbe8c39b26c560203

## Parked

2026-10-09T18:41:33Z brief · item TOOL-aFrugalTurnstile-1 · reason 142385d5e412 memory/builds/aFrugalTurnstile/prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md

2026-10-09T18:42:59Z brief · item TOOL-aFrugalTurnstile-10 · reason 142385d5e412 memory/builds/aFrugalTurnstile/prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md

2026-10-09T18:44:25Z brief · item PLAY-aFrugalTurnstile-1 · reason 142385d5e412 memory/builds/aFrugalTurnstile/prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md

2026-10-09T18:45:53Z brief · item DEPL-aFrugalTurnstile-1 · reason 142385d5e412 memory/builds/aFrugalTurnstile/prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md

2026-10-09T19:03:23Z dispatch · item 4f363647 TOOL-aFrugalTurnstile-1 · reason .githooks/pre-push .githooks/pre-push.test.sh tools/run-gates/run-gates.sh tools/run-gates/run-gates.evidence.test.sh tools/run-gates/README.md memory/guides/MERGE-BAR.md memory/builds/aFrugalTurnstile/spec/2026-10-09-spec-TOOL-aFrugalTurnstile-1.md memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-acceptance-ledger.md memory/builds/aFrugalTurnstile/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-09T19:48:05Z dispatch · item 4f363647 TOOL-aFrugalTurnstile-1 · reason memory/guides/SESSION-KICKOFF.md

2026-10-09T19:55:57Z dispatch · item 89c20a6a DEPL-aFrugalTurnstile-1 · reason WIRE-INTO-PROJECT.md memory/builds/aFrugalTurnstile/spec/2026-10-09-spec-DEPL-aFrugalTurnstile-1.md memory/builds/aFrugalTurnstile/build/2026-10-09-build-DEPL-aFrugalTurnstile-1-1-acceptance-ledger.md memory/builds/aFrugalTurnstile/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T20:06:32Z dispatch · item 62aab23b PLAY-aFrugalTurnstile-1 · reason coding-governance-agents.template.md AGENTS.md tools/template-size-highwater.txt memory/guides/SESSION-KICKOFF.md memory/builds/aFrugalTurnstile/spec/2026-10-09-spec-PLAY-aFrugalTurnstile-1.md memory/builds/aFrugalTurnstile/build/2026-10-09-build-PLAY-aFrugalTurnstile-1-1-acceptance-ledger.md memory/builds/aFrugalTurnstile/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T20:18:17Z dispatch · item 194ab9c8 TOOL-aFrugalTurnstile-10 · reason memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/PROTOCOL.template.md tools/template-size-limits.txt memory/guides/SESSION-KICKOFF.md memory/builds/aFrugalTurnstile/spec/2026-10-09-spec-TOOL-aFrugalTurnstile-10.md memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-10-1-acceptance-ledger.md memory/builds/aFrugalTurnstile/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T20:26:56Z dispatch · item 194ab9c8 TOOL-aFrugalTurnstile-10 · reason memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/PROTOCOL.template.md tools/template-size-limits.txt tools/template-size-highwater.txt memory/guides/SESSION-KICKOFF.md memory/builds/aFrugalTurnstile/spec/2026-10-09-spec-TOOL-aFrugalTurnstile-10.md memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-10-1-acceptance-ledger.md memory/builds/aFrugalTurnstile/README.md memory/LIVE.md memory/ledger/2026-10.md
