# aHalvedInstall - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gates-run: unattended-179096159559588315679-1697 8cdcc9ea
parked-surfaced: yes, 0 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: a3f46c284046d417ed21da11ce5e553a8b11b426
phase: VERIFYING
branch-sha: cd90f7fa5c8cddf152e3a2a065f5df7ad64f355b
branch-ref: refs/heads/branch/kit-bugs-keys-renderer-conflict-eddde0
may: none
mode: prompt
run-branch: refs/heads/branch/kit-bugs-keys-renderer-conflict-eddde0
anchor-kind: run-branch
lease-utc: 2026-10-02T12:51:47Z
pid-image: claude.exe
host: compeeto-agent
pid: 19276
session: 81a68c77-3260-4c90-95a0-32da7860d03f
keepalive: 9f6995e9
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: a587e82dc6180a9a720560e1633995e47734803a
anchor-ref: refs/heads/main
base: cd90f7fa5c8cddf152e3a2a065f5df7ad64f355b

## Parked

2026-10-02T13:03:32Z brief · item DEPL-aHalvedInstall-1 · reason f3210ed86429 memory/builds/aHalvedInstall/prompts/2026-10-02-prompt-DEPL-aHalvedInstall-1-2-build-brief.md

2026-10-02T13:03:35Z brief · item DEPL-aHalvedInstall-2 · reason e894c56a0276 memory/builds/aHalvedInstall/prompts/2026-10-02-prompt-DEPL-aHalvedInstall-2-2-build-brief.md

2026-10-02T13:03:40Z brief · item DEPL-aHalvedInstall-3 · reason 7c40d4482404 memory/builds/aHalvedInstall/prompts/2026-10-02-prompt-DEPL-aHalvedInstall-3-2-build-brief.md

2026-10-02T13:03:43Z brief · item DEPL-aHalvedInstall-4 · reason 36c9e6e8068e memory/builds/aHalvedInstall/prompts/2026-10-02-prompt-DEPL-aHalvedInstall-4-2-build-brief.md

2026-10-02T13:03:51Z dispatch · item e9dfe2cd DEPL-aHalvedInstall-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/unattended/kit.toml memory/builds/aHalvedInstall/spec/2026-10-02-spec-DEPL-aHalvedInstall-1.md memory/LIVE.md

2026-10-02T13:04:39Z dispatch · item d53b503a DEPL-aHalvedInstall-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/unattended/kit.toml memory/builds/aHalvedInstall/spec/2026-10-02-spec-DEPL-aHalvedInstall-1.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aHalvedInstall/README.md

2026-10-02T13:14:28Z dispatch · item c4ea9dd6 DEPL-aHalvedInstall-2 · reason tools/govkit/govkit.py tools/unattended/kit.toml tools/govkit/entries/playbook.kit.toml memory/builds/aHalvedInstall/spec/2026-10-02-spec-DEPL-aHalvedInstall-2.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aHalvedInstall/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md

2026-10-02T13:18:47Z dispatch · item 6d7dcc05 DEPL-aHalvedInstall-3 · reason tools/govkit/govkit.py tools/playbook/kit.toml tools/playbook/README.md tools/agent-instructions/kit.toml tools/codebase-map/kit.toml tools/hooks/kit.toml tools/process-monitor/kit.toml tools/run-gates/kit.toml tools/govkit/entries/settings-merge.kit.toml memory/builds/aHalvedInstall/spec/2026-10-02-spec-DEPL-aHalvedInstall-3.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aHalvedInstall/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md

2026-10-02T13:23:04Z dispatch · item 18dcb54f DEPL-aHalvedInstall-4 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/aHalvedInstall/spec/2026-10-02-spec-DEPL-aHalvedInstall-4.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aHalvedInstall/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md

2026-10-02T13:48:02Z review · item aHalvedInstall · reason verdict BLOCKED · blockers 0 · CONVERGED · disposition promote

2026-10-02T13:49:25Z rescope · item add DEPL-aHalvedInstall-5 · reason closing review round 1 H1 (ids 1, 4), promoted at CONVERGED: the held set misses the classification walk's refusals and the landing loop's, so a kit can still land half its bytes

2026-10-02T13:53:31Z dispatch · item 6dd9ceb7 DEPL-aHalvedInstall-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/drift-audit/kit.toml tools/codebase-map/kit.toml memory/builds/aHalvedInstall/spec/2026-10-02-spec-DEPL-aHalvedInstall-1.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aHalvedInstall/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md

2026-10-02T14:12:10Z dispatch · item f92c7452 DEPL-aHalvedInstall-5 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/aHalvedInstall/spec/2026-10-02-spec-DEPL-aHalvedInstall-5.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aHalvedInstall/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md
