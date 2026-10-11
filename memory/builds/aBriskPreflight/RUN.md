# aBriskPreflight - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 78279ba2e18fed5eedc26ca72e86f1847e246923
phase: BUILDING
may: none
mode: prompt
run-branch: refs/heads/branch/sleepy-kapitsa-1f69c8
anchor-kind: local
cli-version: 2.1.293
lease-utc: 2026-10-11T01:22:33Z
pid-image: claude.exe
host: compeeto-agent
pid: 11836
session: 653ff713-97af-487f-8f4e-2f4c9c73a605
keepalive: 0fe01023
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b726385f2b5b8fd16802925c02104377253a9045
anchor-ref: refs/heads/main
base: 271a90045723817f694de4d22c56f88dbcd0063e

## Parked

2026-10-11T03:40:27Z dispatch · item a0a35056 TOOL-aBriskPreflight-1 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-spawns-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-1.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T03:41:11Z brief · item TOOL-aBriskPreflight-1 · reason 8740a5745416 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-build-brief.md

2026-10-11T05:59:29Z dispatch · item e8932e9f TOOL-aBriskPreflight-1 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-spawns-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-1.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T05:59:38Z brief · item TOOL-aBriskPreflight-1 · reason f39eea28b6eb memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-rebuild-brief.md

2026-10-11T06:39:36Z dispatch · item d6859204 TOOL-aBriskPreflight-5 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-5.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T06:39:51Z brief · item TOOL-aBriskPreflight-5 · reason 61f6904962f7 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-5-build-brief.md

2026-10-11T07:28:52Z dispatch · item 138b0c45 TOOL-aBriskPreflight-6 · reason .githooks/pre-push .githooks/straggler-guard.test.sh .githooks/pre-push.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-6-claim-push-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-6.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T07:29:00Z brief · item TOOL-aBriskPreflight-6 · reason 29e8bec69500 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-6-build-brief.md

2026-10-11T08:09:46Z dispatch · item 20a9e88e TOOL-aBriskPreflight-2 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-2-spawns-ab.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-2.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T08:09:56Z brief · item TOOL-aBriskPreflight-2 · reason 162d8aaea8b6 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-2-build-brief.md

2026-10-11T10:07:31Z dispatch · item 900d74e6 TOOL-aBriskPreflight-4 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/features/unattended-stops.md memory/map/generated/symbols.json memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.sh memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-11T10:08:05Z brief · item TOOL-aBriskPreflight-4 · reason 5651db253a5e memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-4-build-brief.md

2026-10-11T13:58:36Z dispatch · item 2a64d49b TOOL-aBriskPreflight-3 · reason memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md memory/builds/aBriskPreflight/BACKLOG.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-3.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json memory/backlog/TOOL.md

2026-10-11T14:00:18Z brief · item TOOL-aBriskPreflight-3 · reason 521337f9e3b3 memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-3-build-brief.md

2026-10-11T14:42:25Z rescope · item add TOOL-aBriskPreflight-10 · reason origin/main tracks .githooks/pre-commit 100644 since the aDistilledCharter reconcile 60bea5e80; this build met it as a check-4 refusal of its own A/B fixture after the mid-build merge. Restoring 100755 makes the wiring hooks-mode arm, an observable this repo measures, strictly better and makes nothing worse

2026-10-11T15:02:48Z brief · item TOOL-aBriskPreflight-10 · reason 60d7c4d96e4b memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-10-build-brief.md

2026-10-11T15:27:11Z dispatch · item e4fd1b83 TOOL-aBriskPreflight-10 · reason .githooks/pre-commit memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-10.md memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-10-build-brief.md memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-11T19:05:19Z dispatch · item b91d30f7 TOOL-aBriskPreflight-7 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/README.md memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log memory/builds/aBriskPreflight/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-11T19:06:10Z brief · item TOOL-aBriskPreflight-7 · reason 0455d49e591f memory/builds/aBriskPreflight/prompts/2026-10-11-prompt-TOOL-aBriskPreflight-7-build-brief.md
