# dRemeasuredRender - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gates-run: unattended-179171228056387817732-1509 81b937f4
parked-surfaced: yes, 0 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: b41d79bc66e7bd725c0980d46a5669fe2a889364
phase: VERIFYING
may: none
mode: prompt
run-branch: refs/heads/branch/practical-borg-90829d
anchor-kind: local
cli-version: 2.1.293
lease-utc: 2026-10-11T09:11:15Z
pid-image: claude.exe
host: compeeto
pid: 27176
session: 72a45fd5-0f33-45d8-8195-7c980ea738b9
keepalive: 583359a6
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 9a8777b8b502bce48249884e21e5830abadf3e26
anchor-ref: refs/heads/main
base: 17472e212ffd0d5e3be825502c6169bbeb2e952f

## Parked

2026-10-11T09:12:43Z brief · item TOOL-dRemeasuredRender-1 · reason a3e462920f97 memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-TOOL-dRemeasuredRender-1-1-build-brief.md

2026-10-11T09:14:52Z dispatch · item c922c7e2 TOOL-dRemeasuredRender-1 · reason .githooks/straggler-guard.test.sh memory/builds/dRemeasuredRender/BACKLOG.md memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-TOOL-dRemeasuredRender-1-1-build-brief.md skills/session-kickoff/manifest-check.test.sh tools/check-hook-destinations.test.sh tools/check-line-length.test.sh tools/check-spec-tokens.test.sh tools/check-wiring.test.sh tools/gate-legs.json tools/gate-lint/kit.toml tools/hooks/agent-cap.test.sh tools/hooks/scratch-guard.test.sh tools/lib/extract-arms.test.sh tools/lib/lib-selftest.test.sh tools/lib/resolve-python.test.sh tools/memory-tree/check-verdict-epoch.test.sh tools/memory-tree/marker-contract.test.sh tools/memory-tree/merge-rows.test.sh tools/memory-tree/transition-audit.test.sh tools/process-monitor/adopt-process-monitor.test.sh tools/push-main.test.sh tools/run-gates/foreign-prefix.gov.test.sh tools/run-gates/run-gates.runlog.test.sh tools/run-gates/run-gates.test.sh tools/run-gates/run-gates.turnstile.test.sh tools/run-gates/run-selftests.test.sh tools/unattended/adopt-unattended.test.sh tools/unattended/check-unattended.test.sh tools/unattended/cross-component.test.sh tools/unattended/resume-tick.test.sh tools/unattended/runlog-writer.test.sh tools/unattended/unattended.test.sh tools/workflows/check-verifier-fanout.test.sh tools/workflows/unattended-build.test.sh

2026-10-11T09:16:46Z dispatch · item c922c7e2 TOOL-dRemeasuredRender-1 · reason memory/builds/dRemeasuredRender/spec/2026-10-11-spec-TOOL-dRemeasuredRender-1.md memory/builds/dRemeasuredRender/build/2026-10-11-build-TOOL-dRemeasuredRender-1-1-acceptance-ledger.md

2026-10-11T09:17:41Z dispatch · item c922c7e2 TOOL-dRemeasuredRender-1 · reason memory/guides/SESSION-KICKOFF.md

2026-10-11T09:18:01Z dispatch · item c922c7e2 TOOL-dRemeasuredRender-1 · reason memory/builds/dRemeasuredRender/README.md

2026-10-11T09:20:23Z brief · item DEPL-dRemeasuredRender-1 · reason b8a7ad422b24 memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-1-1-build-brief.md

2026-10-11T09:23:56Z dispatch · item 7a474bab DEPL-dRemeasuredRender-1 · reason WIRE-INTO-PROJECT.md memory/builds/dRemeasuredRender/README.md memory/builds/dRemeasuredRender/build/2026-10-11-build-DEPL-dRemeasuredRender-1-1-acceptance-ledger.md memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-1-1-build-brief.md memory/builds/dRemeasuredRender/spec/2026-10-11-spec-DEPL-dRemeasuredRender-1.md memory/map/generated/symbols.json tools/govkit/govkit.py tools/govkit/selftest.py

2026-10-11T09:24:46Z brief · item DEPL-dRemeasuredRender-2 · reason 0e71236573f1 memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-2-1-build-brief.md

2026-10-11T09:26:57Z dispatch · item 473d2bbc DEPL-dRemeasuredRender-2 · reason WIRE-INTO-PROJECT.md memory/builds/dRemeasuredRender/build/2026-10-11-build-DEPL-dRemeasuredRender-2-1-acceptance-ledger.md memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-2-1-build-brief.md memory/builds/dRemeasuredRender/spec/2026-10-11-spec-DEPL-dRemeasuredRender-2.md tools/govkit/govkit.py tools/govkit/selftest.py

2026-10-11T09:38:45Z review · item dRemeasuredRender · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 10 · disposition promote

2026-10-11T09:39:59Z rescope · item add DEPL-dRemeasuredRender-3 · reason promoted from the closing diff review round 1, which converged with 1 HIGH and 10 minors

2026-10-11T09:40:00Z rescope · item add DEPL-dRemeasuredRender-4 · reason promoted from the closing diff review round 1, which converged with 1 HIGH and 10 minors

2026-10-11T09:41:01Z brief · item DEPL-dRemeasuredRender-3 · reason bb0f1a7a486a memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-3-1-build-brief.md

2026-10-11T09:41:01Z brief · item DEPL-dRemeasuredRender-4 · reason 303ca8242572 memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-4-1-build-brief.md

2026-10-11T09:42:12Z dispatch · item 0fa8463e DEPL-dRemeasuredRender-3 · reason WIRE-INTO-PROJECT.md memory/builds/dRemeasuredRender/build/2026-10-11-build-DEPL-dRemeasuredRender-3-1-acceptance-ledger.md memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-3-1-build-brief.md memory/builds/dRemeasuredRender/prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-4-1-build-brief.md memory/builds/dRemeasuredRender/spec/2026-10-11-spec-DEPL-dRemeasuredRender-3.md tools/govkit/govkit.py tools/govkit/selftest.py

2026-10-11T09:47:02Z dispatch · item 57a98c4f DEPL-dRemeasuredRender-4 · reason memory/builds/dRemeasuredRender/build/2026-10-11-build-DEPL-dRemeasuredRender-4-1-acceptance-ledger.md memory/builds/dRemeasuredRender/spec/2026-10-11-spec-DEPL-dRemeasuredRender-4.md memory/gotchas/INDEX.md memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json tools/govkit/govkit.py tools/govkit/selftest.py

2026-10-11T09:47:49Z dispatch · item 57a98c4f DEPL-dRemeasuredRender-4 · reason memory/map/features/govkit.md
