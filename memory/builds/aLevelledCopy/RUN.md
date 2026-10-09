# aLevelledCopy - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: bb6178eab4ef9bfc9b603398e1258119873b47b5
phase: REVIEWING
branch-sha: ce9192c0ba180a67b49b2ea3fc8edf2fb8afc0cb
branch-ref: refs/heads/branch/friendly-napier-49e2c6
may: none
mode: prompt
run-branch: refs/heads/branch/friendly-napier-49e2c6
anchor-kind: run-branch
cli-version: 2.1.293
lease-utc: 2026-10-08T22:37:33Z
pid-image: claude.exe
host: compeeto-agent
pid: 12132
session: 7bb9a7dc-5af0-43b9-b4cd-40d8e56c1c70
keepalive: d8603c01
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 40a8b8c32ad1e7f30f36c7be6e71d9a0a67d142a
anchor-ref: refs/heads/main
base: ce9192c0ba180a67b49b2ea3fc8edf2fb8afc0cb

## Parked

2026-10-08T23:41:01Z dispatch · item f8de6707 DEPL-aLevelledCopy-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/aLevelledCopy/spec/2026-10-09-spec-DEPL-aLevelledCopy-1.md memory/builds/aLevelledCopy/build/2026-10-09-build-DEPL-aLevelledCopy-1-1-acceptance-ledger.md memory/builds/aLevelledCopy/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-08T23:42:10Z brief · item DEPL-aLevelledCopy-1 · reason a693eb5525d2 memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md

2026-10-09T00:17:36Z dispatch · item f8de6707 DEPL-aLevelledCopy-1 · reason memory/map/generated/symbols.json

2026-10-09T00:33:36Z brief · item TOOL-aLevelledCopy-1 · reason 88b9006aa11f memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md

2026-10-09T00:40:31Z dispatch · item 53a8cc08 TOOL-aLevelledCopy-1 · reason tools/run-gates/check-receipt.py tools/run-gates/README.md memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-1.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-1-1-acceptance-ledger.md memory/builds/aLevelledCopy/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-09T01:17:17Z dispatch · item ff49508f TOOL-aLevelledCopy-2 · reason tools/push-main.sh tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-2.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-2-1-acceptance-ledger.md

2026-10-09T01:18:12Z brief · item TOOL-aLevelledCopy-2 · reason 88b9006aa11f memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md

2026-10-09T01:57:51Z dispatch · item ff49508f TOOL-aLevelledCopy-2 · reason tools/push-main.sh tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-2.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-2-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/aLevelledCopy/README.md

2026-10-09T02:11:59Z brief · item TOOL-aLevelledCopy-3 · reason 88b9006aa11f memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md

2026-10-09T02:14:43Z dispatch · item 33a15c87 TOOL-aLevelledCopy-3 · reason .githooks/commit-msg .githooks/pre-commit .githooks/pre-push .githooks/pre-rebase tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-3-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/aLevelledCopy/README.md

2026-10-09T02:48:35Z dispatch · item 33a15c87 TOOL-aLevelledCopy-3 · reason .githooks/commit-msg .githooks/pre-commit .githooks/pre-push .githooks/pre-rebase tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-3-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/aLevelledCopy/README.md memory/LIVE.md

2026-10-09T02:55:52Z dispatch · item 33a15c87 TOOL-aLevelledCopy-3 · reason memory/builds/aLevelledCopy/BACKLOG.md

2026-10-09T03:01:25Z dispatch · item 33a15c87 TOOL-aLevelledCopy-3 · reason memory/backlog/DEPL.md memory/backlog/TOOL.md
