# aLevelledCopy - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gates-run: unattended-179152700700248614898-2261765 2503eec7
parked-surfaced: yes, 0 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 79126924852f9ae7f9f1ad9dd5a28940402fa506
phase: VERIFYING
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

2026-10-09T03:40:59Z review · item aLevelledCopy · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 14 · disposition promote

2026-10-09T03:42:48Z rescope · item add TOOL-aLevelledCopy-7 · reason closing review round 1 HIGH H1 (id 3) with M1 (id 9), one root cause: the ssh arm overrides an operator's GIT_SSH or ssh.variant

2026-10-09T03:43:55Z rescope · item add TOOL-aLevelledCopy-8 · reason closing review round 1 minors on the check-wiring write set: M3 M4 M5 M7 L1 L2 (ids 16 6 7 13 5 10 14)

2026-10-09T03:44:57Z rescope · item add TOOL-aLevelledCopy-9 · reason closing review round 1 minors on the receipt, govkit and record write set: M2 M6 L3 L4 L5 (ids 4 12 8 15 18 19)

2026-10-09T04:26:05Z dispatch · item 176005b6 TOOL-aLevelledCopy-7 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-7.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-7-1-acceptance-ledger.md memory/builds/aLevelledCopy/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-09T04:26:34Z brief · item TOOL-aLevelledCopy-7 · reason 88b9006aa11f memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md

2026-10-09T04:47:58Z brief · item TOOL-aLevelledCopy-9 · reason 88b9006aa11f memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md

2026-10-09T04:52:36Z dispatch · item dae09ec1 TOOL-aLevelledCopy-9 · reason tools/run-gates/check-receipt.py tools/govkit/govkit.py tools/govkit/selftest.py memory/gotchas/two-answers-to-one-question.md memory/gotchas/INDEX.md memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-9.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-9-1-acceptance-ledger.md memory/builds/aLevelledCopy/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-09T05:09:54Z dispatch · item 0a09d7a0 TOOL-aLevelledCopy-8 · reason tools/check-wiring.sh tools/check-wiring.test.sh tools/govkit/entries/check-wiring.kit.toml memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-8.md memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-8-1-acceptance-ledger.md memory/builds/aLevelledCopy/README.md memory/LIVE.md memory/ledger/2026-10.md memory/map/generated/symbols.json

2026-10-09T05:10:13Z brief · item TOOL-aLevelledCopy-8 · reason 88b9006aa11f memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md
