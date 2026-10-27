# dSafePassage - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
hold-run: 
hold-streak: 1 · at 96e9dd87
resume-owed: none · owner
held-at: 2026-10-26T17:36:43Z
hold-reason: TOOL-dSafePassage-11 raises the interpreter floor to Python 3.15 and node a resolves only 3.14.6; provisioning (AP-31) is the owner's. Units 8 and 12 consume 11, and --dispatch's order gate refuses every order-4+ unit while order-3 units stand, so no carried unit can build. 13 of 59 units built; 61 waits on TOOL-dGroundRules-13
hold-until: owner
hold-code: host-owner-action
held-from: BUILDING
refreshed-at: c8d46e188985ce49caad48cf874934661ad3fc7c · park · 43 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 4cbd011d59e15a76f53cbaf53b25146b658d0db8
phase: BUILDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dsafepassage-567339
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-26T18:23:28Z
pid-image: claude.exe
host: compeeto-agent
pid: 23020
session: c5f50d22-89c6-41d7-84e5-2382dcd49faa
keepalive: 94fa87dd
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 60d90cb71db51e651aa1c5efe3f6d48ba21a997d
anchor-ref: refs/heads/main
base: 60d90cb71db51e651aa1c5efe3f6d48ba21a997d

## Parked

2026-10-26T09:06:44Z rescope · item add TOOL-dSafePassage-61 · reason TOOL-dSafePassage-1's build pass diverged at §8 F8: the landed policy guard (tools/policy/guard.py, TOOL-dGroundRules-6) refuses S8's seven-key write of .governance/policy.toml ('7 keys changed; one cap raised is the one agent shape'), and TOOL-dGroundRules-13, the ask that would admit it, is OPEN; F8 says the build run stops S8 if not granted, so the gov migration of template-size-limits.txt moves to this new unit, DEFERRED until TOOL-dGroundRules-13

2026-10-26T09:58:28Z dispatch · item 2d20e0b5 TOOL-dSafePassage-1 · reason tools/govkit/upgrade_steps.py tools/govkit/steps.toml tools/govkit/steps/fanout_cap.py tools/govkit/govkit.py tools/govkit/registry.toml tools/govkit/selftest.py tools/govkit/refusal_join.py tools/govkit/subject-pins.tsv tools/govkit/matrix.py tools/check-install-prefix.test.sh tools/hooks/kit.toml tools/hooks/README.md tools/gate-legs.json help/upgrade-steps.md help/README.md memory/guides/SESSION-KICKOFF.md memory/map/features/govkit.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-1-ledger.md

2026-10-26T09:58:34Z brief · item TOOL-dSafePassage-1 · reason 4ad3dd0f8071 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-1-build-brief.md

2026-10-26T10:39:05Z dispatch · item 2d20e0b5 TOOL-dSafePassage-1 · reason tools/govkit/upgrade_steps.py tools/govkit/steps.toml tools/govkit/steps/fanout_cap.py tools/govkit/govkit.py tools/govkit/registry.toml tools/govkit/selftest.py tools/govkit/refusal_join.py tools/govkit/subject-pins.tsv tools/govkit/matrix.py tools/check-install-prefix.test.sh tools/hooks/kit.toml tools/hooks/README.md tools/gate-legs.json help/upgrade-steps.md help/README.md memory/guides/SESSION-KICKOFF.md memory/map/features/govkit.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-1-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T10:43:20Z dispatch · item 2d20e0b5 TOOL-dSafePassage-1 · reason .gitattributes

2026-10-26T10:56:17Z dispatch · item 29ccb065 TOOL-dSafePassage-1 · reason tools/govkit/selftest.py memory/map/generated/symbols.json

2026-10-26T11:29:59Z dispatch · item 14054d44 TOOL-dSafePassage-3 · reason tools/govkit/govkit.py tools/govkit/upgrade_steps.py tools/govkit/steps.toml tools/govkit/steps/receipt_schema_4.py tools/govkit/selftest.py tools/govkit/matrix.py tools/govkit/refusal_join.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-3.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-3-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/features/govkit.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T11:30:19Z brief · item TOOL-dSafePassage-3 · reason 3df06df6ea40 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-3-build-brief.md

2026-10-26T11:45:05Z dispatch · item 14054d44 TOOL-dSafePassage-3 · reason tools/govkit/govkit.py tools/govkit/upgrade_steps.py tools/govkit/steps.toml tools/govkit/steps/receipt_schema_4.py tools/govkit/selftest.py tools/govkit/matrix.py tools/govkit/refusal_join.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-3.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-3-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/features/govkit.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-3-deviation-165.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-10-26T12:06:51Z brief · item TOOL-dSafePassage-16 · reason 009ed7d60646 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-16-build-brief.md

2026-10-26T12:11:29Z dispatch · item 885d0ff9 TOOL-dSafePassage-16 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-16.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-16-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T12:24:11Z brief · item TOOL-dSafePassage-20 · reason 8afb1c293e7a memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-20-build-brief.md

2026-10-26T12:32:29Z dispatch · item c4fc7de1 TOOL-dSafePassage-20 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py tools/govkit/refusal_join.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-20.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-20-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T12:43:52Z brief · item TOOL-dSafePassage-43 · reason 567106089b61 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-43-build-brief.md

2026-10-26T12:48:03Z dispatch · item adc480e5 TOOL-dSafePassage-43 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-43.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-43-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T13:01:44Z brief · item TOOL-dSafePassage-7 · reason d427289f281b memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-7-build-brief.md

2026-10-26T13:09:45Z dispatch · item 0becfe7d TOOL-dSafePassage-7 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py tools/govkit/refusal_join.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-7.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-7-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T13:28:53Z brief · item TOOL-dSafePassage-2 · reason 26a49c296f4d memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-2-build-brief.md

2026-10-26T13:32:45Z dispatch · item 5aac6409 TOOL-dSafePassage-2 · reason tools/govkit/upgrade_steps.py tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/refusal_join.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-2.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-2-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/features/govkit.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T14:24:38Z dispatch · item f8262323 TOOL-dSafePassage-4 · reason tools/govkit/upgrade_steps.py tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/refusal_join.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-4.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-4-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/features/govkit.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T14:24:43Z brief · item TOOL-dSafePassage-4 · reason 7d3491cc41cd memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-4-build-brief.md

2026-10-26T15:25:29Z dispatch · item 16cfa267 TOOL-dSafePassage-15 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-15.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-15-ledger.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/features/govkit.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T15:25:38Z brief · item TOOL-dSafePassage-15 · reason 96f496fcf412 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-15-build-brief.md

2026-10-26T15:36:53Z decision · item TOOL-dSafePassage-11 needs Python 3.15 on the build node: provision node a (and every node) at 3.15 final, or rule how the floor lands · reason options: (a) the owner provisions 3.15 per AP-31 and the run resumes 11 and its 38 dependants; (b) the owner rules a different landing for the floor. Refused to choose: node a resolves only 3.14.6 (py -0p; uv lists 3.15.0b2 only); provisioning is a §3 non-goal and an owner act; a resolver refusing below 3.15 would refuse every later hook and the close's bar; a floor switch is the fail-open override §3 rules out. Units outside 11's consumes-from closure build meanwhile

2026-10-26T15:43:18Z dispatch · item ee025c5f TOOL-dSafePassage-18 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-18.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-18-ledger.md

2026-10-26T15:43:24Z brief · item TOOL-dSafePassage-18 · reason 8e9915b50083 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-18-build-brief.md

2026-10-26T16:38:49Z dispatch · item dfb5381c TOOL-dSafePassage-19 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-19.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-19-ledger.md memory/builds/dSafePassage/README.md memory/LIVE.md memory/backlog/TOOL.md memory/map/generated/symbols.json

2026-10-26T16:38:56Z brief · item TOOL-dSafePassage-19 · reason bd47d8ece66f memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-19-build-brief.md

2026-10-26T17:01:33Z dispatch · item a860921f TOOL-dSafePassage-22 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-22.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-22-ledger.md memory/builds/dSafePassage/README.md memory/map/generated/symbols.json

2026-10-26T17:01:41Z brief · item TOOL-dSafePassage-22 · reason f236ff62e3e6 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-22-build-brief.md

2026-10-26T17:15:51Z dispatch · item a182f2c2 TOOL-dSafePassage-24 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py tools/govkit/refusal_join.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-24.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-24-ledger.md memory/builds/dSafePassage/README.md memory/LIVE.md memory/map/generated/symbols.json

2026-10-26T17:15:57Z brief · item TOOL-dSafePassage-24 · reason 367133729cff memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-24-build-brief.md

2026-10-26T17:36:47Z hold · item host-owner-action · reason until owner · reaped 6e25bf31 · resume none(owner)

2026-10-26T18:23:36Z resume · item dSafePassage · reason held · keepalive 94fa87dd · manual

2026-10-26T18:36:24Z brief · item TOOL-dSafePassage-11 · reason 5c224e575915 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-11-build-brief.md

2026-10-26T18:41:36Z dispatch · item 2e382c09 TOOL-dSafePassage-11 · reason tools/lib/python-floor.txt tools/lib/python-floor.sh tools/lib/python_floor.py tools/lib/resolve-python.sh tools/lib/resolve-python.test.sh tools/govkit/steps.toml tools/memory-tree/merge-rows.test.sh tools/settings-merge.py tools/govkit/govkit.py tools/govkit/check_runbook_parity.py tools/codebase-map/map_lib.py tools/codebase-map/README.md README.md tools/check-line-length.sh tools/playbook/adopt-playbook.sh help/python-floor.md help/README.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-11.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-11-ledger.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json .githooks/pre-push .githooks/pre-push.runlog.test.sh .githooks/pre-push.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh tools/check-agent-cap-restatement.test.sh tools/check-hook-destinations.sh tools/check-hook-destinations.test.sh tools/check-install-prefix.sh tools/check-kit-placeholders.test.sh tools/check-kit-versions.sh tools/check-line-length.test.sh tools/check-playbook-parity.sh tools/check-playbook-parity.test.sh tools/check-spec-tokens.test.sh tools/check-template-size.sh tools/check-testsuite-counts.test.sh tools/check-wiring.sh tools/check-wiring.test.sh tools/codebase-map/adopt-codebase-map.sh tools/codebase-map/adopt-codebase-map.test.sh tools/drift-audit/adopt-drift-audit.sh tools/govkit/census.test.sh tools/hooks/agent-cap.test.sh tools/hooks/format-guard.test.sh tools/hooks/scratch-guard.test.sh tools/lexicon/adopt-lexicon.sh tools/memory-recall/adopt-memory-recall.sh tools/memory-tree/adopt-memory-tree.sh tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/check-verdict-epoch.sh tools/memory-tree/kit-dogfood-parity.test.sh tools/memory-tree/merge-rows.sh tools/memory-tree/merge-rows.test.sh tools/policy/adopt-policy.sh tools/policy/policy-shim.sh tools/process-monitor/adopt-process-monitor.sh tools/process-monitor/adopt-process-monitor.test.sh tools/push-main.sh tools/push-main.test.sh tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh tools/roles/adopt-roles.sh tools/run-gates/foreign-prefix.gov.test.sh tools/run-gates/run-gates.evidence.test.sh tools/run-gates/run-gates.gov.test.sh tools/run-gates/run-gates.runlog.test.sh tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/run-gates.turnstile.test.sh tools/run-gates/run-held-wsl.sh tools/run-gates/run-selftests.sh tools/run-gates/run-selftests.test.sh tools/runlog/adopt-runlog.sh tools/unattended/adopt-unattended.sh tools/unattended/adopt-unattended.test.sh tools/unattended/check-brief-recorded.test.sh tools/unattended/check-pass-order.test.sh tools/unattended/check-unattended.sh tools/unattended/gate-guard.test.sh tools/unattended/run-unattended-gates.sh tools/unattended/runlog-writer.test.sh tools/unattended/stall-recorder.test.sh tools/unattended/stop-guard.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/workflows/check-protocol-parity.test.sh tools/workflows/check-review-join.sh tools/workflows/check-review-join.test.sh tools/workflows/check-verifier-fanout.sh tools/workflows/check-verifier-fanout.test.sh tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh

2026-10-26T20:30:03Z brief · item TOOL-dSafePassage-8 · reason f5899d4f67c7 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-8-build-brief.md

2026-10-26T20:35:53Z dispatch · item 3f102408 TOOL-dSafePassage-8 · reason tools/govkit/govkit.py tools/govkit/upgrade_steps.py tools/govkit/selftest.py tools/govkit/refusal_join.py tools/govkit/matrix.py tools/push-main.sh tools/push-main.test.sh tools/run-gates/check-receipt.py tools/memory-tree/check-verdict-epoch.sh memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-8.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-8-ledger.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-8-deviation-166.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/features/govkit.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-26T20:43:39Z dispatch · item 3f102408 TOOL-dSafePassage-8 · reason tools/govkit/govkit.py tools/govkit/upgrade_steps.py tools/govkit/selftest.py tools/govkit/refusal_join.py tools/govkit/matrix.py tools/push-main.sh tools/push-main.test.sh tools/run-gates/check-receipt.py tools/memory-tree/check-verdict-epoch.sh memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-8.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-8-ledger.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-8-deviation-166.md memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/LIVE.md memory/map/features/govkit.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-10-26T20:55:28Z brief · item TOOL-dSafePassage-12 · reason a93eb905f05e memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-12-build-brief.md

2026-10-26T21:00:53Z dispatch · item 4987c13d TOOL-dSafePassage-12 · reason .github/workflows/remote-ci.yml memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-12.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-12-ledger.md memory/builds/dSafePassage/README.md memory/LIVE.md

2026-10-26T21:16:19Z dispatch · item 1d30fd14 TOOL-dSafePassage-10 · reason tools/govkit/step_gate.py tools/govkit/surface-classes.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md help/step-gate.md help/README.md memory/map/generated/symbols.json

2026-10-26T21:16:26Z brief · item TOOL-dSafePassage-10 · reason ff04c15588ca memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-10-build-brief.md

2026-10-26T21:41:56Z dispatch · item 1d30fd14 TOOL-dSafePassage-10 · reason tools/govkit/step_gate.py tools/govkit/surface-classes.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md help/step-gate.md help/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-10-26T21:48:32Z dispatch · item 1d30fd14 TOOL-dSafePassage-10 · reason tools/govkit/step_gate.py tools/govkit/surface-classes.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md help/step-gate.md help/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/guides/SESSION-KICKOFF.md

2026-10-26T21:55:26Z dispatch · item 1d30fd14 TOOL-dSafePassage-10 · reason tools/govkit/step_gate.py tools/govkit/surface-classes.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md help/step-gate.md help/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/guides/SESSION-KICKOFF.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-10-deviation-167.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-10-deviation-168.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-10-deviation-169.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-10-ledger.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-10.md

2026-10-26T22:15:16Z dispatch · item f7e56a96 TOOL-dSafePassage-17 · reason tools/govkit/upgrade_steps.py tools/govkit/steps.toml tools/govkit/selftest.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-17.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-17-ledger.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-10-26T22:15:22Z brief · item TOOL-dSafePassage-17 · reason 10fa24169a9e memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-17-build-brief.md

2026-10-26T22:42:19Z dispatch · item 66631b0f TOOL-dSafePassage-23 · reason .githooks/pre-push .githooks/pre-push.runlog.test.sh .githooks/pre-push.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh tools/check-agent-cap-restatement.test.sh tools/check-hook-destinations.sh tools/check-hook-destinations.test.sh tools/check-install-prefix.sh tools/check-kit-placeholders.test.sh tools/check-kit-versions.sh tools/check-line-length.sh tools/check-line-length.test.sh tools/check-playbook-parity.sh tools/check-playbook-parity.test.sh tools/check-spec-tokens.test.sh tools/check-template-size.sh tools/check-testsuite-counts.test.sh tools/check-wiring.sh tools/check-wiring.test.sh tools/codebase-map/adopt-codebase-map.sh tools/codebase-map/adopt-codebase-map.test.sh tools/drift-audit/adopt-drift-audit.sh tools/govkit/census.test.sh tools/hooks/agent-cap.test.sh tools/hooks/format-guard.test.sh tools/hooks/scratch-guard.test.sh tools/lexicon/adopt-lexicon.sh tools/lib/resolve-python.sh tools/memory-recall/adopt-memory-recall.sh tools/memory-tree/adopt-memory-tree.sh tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/check-verdict-epoch.sh tools/memory-tree/kit-dogfood-parity.test.sh tools/memory-tree/merge-rows.sh tools/memory-tree/merge-rows.test.sh tools/playbook/adopt-playbook.sh tools/policy/adopt-policy.sh tools/policy/policy-shim.sh tools/process-monitor/adopt-process-monitor.sh tools/process-monitor/adopt-process-monitor.test.sh tools/push-main.sh tools/push-main.test.sh tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh tools/roles/adopt-roles.sh tools/run-gates/foreign-prefix.gov.test.sh tools/run-gates/run-gates.evidence.test.sh tools/run-gates/run-gates.gov.test.sh tools/run-gates/run-gates.runlog.test.sh tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/run-gates.turnstile.test.sh tools/run-gates/run-held-wsl.sh tools/run-gates/run-selftests.sh tools/run-gates/run-selftests.test.sh tools/runlog/adopt-runlog.sh tools/unattended/adopt-unattended.sh tools/unattended/adopt-unattended.test.sh tools/unattended/check-brief-recorded.test.sh tools/unattended/check-pass-order.test.sh tools/unattended/check-unattended.sh tools/unattended/gate-guard.test.sh tools/unattended/run-unattended-gates.sh tools/unattended/runlog-writer.test.sh tools/unattended/stall-recorder.test.sh tools/unattended/stop-guard.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/workflows/check-protocol-parity.test.sh tools/workflows/check-review-join.sh tools/workflows/check-review-join.test.sh tools/workflows/check-verifier-fanout.sh tools/workflows/check-verifier-fanout.test.sh tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh tools/lib/resolve-python.test.sh help/python-floor.md memory/guides/SESSION-KICKOFF.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-23.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-23-ledger.md

2026-10-26T22:42:26Z brief · item TOOL-dSafePassage-23 · reason b1c90b0b5b61 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-23-build-brief.md

2026-10-26T23:00:32Z dispatch · item 8b379abf TOOL-dSafePassage-25 · reason tools/push-main.sh tools/push-main.test.sh

2026-10-26T23:00:38Z brief · item TOOL-dSafePassage-25 · reason e8c42c671280 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-25-build-brief.md

2026-10-26T23:22:43Z dispatch · item 8b379abf TOOL-dSafePassage-25 · reason tools/push-main.sh tools/push-main.test.sh memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-25-ledger.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-25-deviation-170.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-25.md

2026-10-26T23:46:15Z dispatch · item da77d7ac TOOL-dSafePassage-29 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-29.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-29-ledger.md

2026-10-26T23:46:21Z brief · item TOOL-dSafePassage-29 · reason 3003603fc35d memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-29-build-brief.md

2026-10-27T00:05:27Z dispatch · item 22be190d TOOL-dSafePassage-30 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-30.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-30-ledger.md memory/builds/dSafePassage/README.md memory/map/generated/symbols.json

2026-10-27T00:05:35Z brief · item TOOL-dSafePassage-30 · reason 76ca538419c7 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-30-build-brief.md

2026-10-27T00:15:37Z dispatch · item 22be190d TOOL-dSafePassage-30 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-30.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-30-ledger.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-30-deviation-171.md memory/builds/dSafePassage/README.md memory/map/generated/symbols.json

2026-10-27T00:24:38Z dispatch · item 22be190d TOOL-dSafePassage-30 · reason tools/govkit/upgrade_steps.py tools/govkit/selftest.py help/upgrade-steps.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-30.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-30-ledger.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-30-deviation-171.md memory/builds/dSafePassage/README.md memory/map/generated/symbols.json memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-10-27T00:41:56Z dispatch · item 602fe92c TOOL-dSafePassage-32 · reason tools/govkit/upgrade_steps.py tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-32.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-32-ledger.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-32-deviation-172.md memory/builds/dSafePassage/README.md memory/map/generated/symbols.json memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-10-27T00:42:03Z brief · item TOOL-dSafePassage-32 · reason 24fe63339426 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-32-build-brief.md

2026-10-27T01:06:14Z dispatch · item ab5614c2 TOOL-dSafePassage-6 · reason tools/govkit/shims.py tools/govkit/shims.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/gate-legs.json help/shims.md help/README.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-6.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-6-ledger.md memory/map/generated/symbols.json

2026-10-27T01:06:22Z brief · item TOOL-dSafePassage-6 · reason f0fd5b7a8f92 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-6-build-brief.md

2026-10-27T01:24:04Z dispatch · item ab5614c2 TOOL-dSafePassage-6 · reason tools/govkit/shims.py tools/govkit/shims.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/gate-legs.json help/shims.md help/README.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-6.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-6-ledger.md memory/map/generated/symbols.json memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-6-deviation-173.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-6-deviation-174.md

2026-10-27T01:34:20Z dispatch · item ab5614c2 TOOL-dSafePassage-6 · reason tools/govkit/shims.py tools/govkit/shims.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/gate-legs.json help/shims.md help/README.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-6.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-6-ledger.md memory/map/generated/symbols.json memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-6-deviation-173.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-6-deviation-174.md memory/guides/SESSION-KICKOFF.md

2026-10-27T01:53:46Z dispatch · item 57f29f7f TOOL-dSafePassage-9 · reason tools/govkit/govkit.py tools/govkit/fixtures/retired_edits.py tools/govkit/selftest.py tools/gate-legs.json help/update-edits.md help/README.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-9.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-9-ledger.md memory/map/generated/symbols.json memory/guides/SESSION-KICKOFF.md memory/builds/dSafePassage/README.md

2026-10-27T01:53:51Z brief · item TOOL-dSafePassage-9 · reason b25e49ae5cb2 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-9-build-brief.md

2026-10-27T02:13:12Z dispatch · item 57f29f7f TOOL-dSafePassage-9 · reason tools/govkit/govkit.py tools/govkit/fixtures/retired_edits.py tools/govkit/selftest.py tools/gate-legs.json help/update-edits.md help/README.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-9.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-9-ledger.md memory/map/generated/symbols.json memory/guides/SESSION-KICKOFF.md memory/builds/dSafePassage/README.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-9-deviation-175.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-10-27T02:35:32Z dispatch · item 1b64e20a TOOL-dSafePassage-13 · reason tools/govkit/docs_leg.py tools/govkit/usage.toml tools/govkit/selftest.py tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/gate-legs.json tools/run-gates/ceiling-evidence.txt tools/drift-audit/drift_signals.py memory/project/docs-undocumented.txt memory/map/features/govkit.md help/docs-leg.md help/README.md help/roles.md help/measure-legs.md help/step-gate.md help/upgrade-steps.md help/shims.md help/update-edits.md help/python-floor.md help/policy.md help/size-caps.md help/agent-limit.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-13.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-13-ledger.md memory/map/generated/symbols.json memory/builds/dSafePassage/README.md memory/guides/SESSION-KICKOFF.md

2026-10-27T02:35:39Z brief · item TOOL-dSafePassage-13 · reason d59cb53097d6 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-13-build-brief.md

2026-10-27T02:55:42Z dispatch · item 1b64e20a TOOL-dSafePassage-13 · reason tools/govkit/docs_leg.py tools/govkit/usage.toml tools/govkit/selftest.py tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/gate-legs.json tools/run-gates/ceiling-evidence.txt tools/drift-audit/drift_signals.py memory/project/docs-undocumented.txt memory/map/features/govkit.md help/docs-leg.md help/README.md help/roles.md help/measure-legs.md help/step-gate.md help/upgrade-steps.md help/shims.md help/update-edits.md help/python-floor.md help/policy.md help/size-caps.md help/agent-limit.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-13.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-13-ledger.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/backlog/TOOL.md memory/builds/dSafePassage/README.md memory/guides/SESSION-KICKOFF.md

2026-10-27T03:02:36Z dispatch · item 1b64e20a TOOL-dSafePassage-13 · reason tools/govkit/docs_leg.py tools/govkit/usage.toml tools/govkit/selftest.py tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/gate-legs.json tools/run-gates/ceiling-evidence.txt tools/drift-audit/drift_signals.py memory/project/docs-undocumented.txt memory/map/features/govkit.md help/docs-leg.md help/README.md help/roles.md help/measure-legs.md help/step-gate.md help/upgrade-steps.md help/shims.md help/update-edits.md help/python-floor.md help/policy.md help/size-caps.md help/agent-limit.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-13.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-13-ledger.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/backlog/TOOL.md memory/builds/dSafePassage/README.md memory/guides/SESSION-KICKOFF.md .memory-tree.conf

2026-10-27T03:24:18Z dispatch · item 4cabc885 TOOL-dSafePassage-21 · reason tools/govkit/govkit.py tools/govkit/step_gate.py tools/govkit/selftest.py memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-21.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-21-ledger.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-10-27T03:24:22Z brief · item TOOL-dSafePassage-21 · reason 4bc4670ec981 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-21-build-brief.md

2026-10-27T03:34:56Z dispatch · item 4cabc885 TOOL-dSafePassage-21 · reason tools/govkit/govkit.py tools/govkit/step_gate.py tools/govkit/selftest.py tools/govkit/surface-classes.toml memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-21.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-21-ledger.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-10-27T03:40:02Z dispatch · item 4cabc885 TOOL-dSafePassage-21 · reason tools/govkit/govkit.py tools/govkit/step_gate.py tools/govkit/selftest.py tools/govkit/surface-classes.toml help/step-gate.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-21.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-21-ledger.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-21-deviation-176.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-21-deviation-177.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-10-27T03:45:58Z dispatch · item 4cabc885 TOOL-dSafePassage-21 · reason tools/govkit/govkit.py tools/govkit/step_gate.py tools/govkit/selftest.py tools/govkit/surface-classes.toml help/step-gate.md memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-21.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-21-ledger.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-21-deviation-176.md memory/builds/dSafePassage/build/2026-10-27-build-TOOL-dSafePassage-21-deviation-177.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/builds/dSafePassage/README.md memory/backlog/TOOL.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-10-27T04:10:28Z dispatch · item 4749dfba TOOL-dSafePassage-27 · reason tools/push-main.sh tools/push-main.test.sh memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-27.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-27-ledger.md

2026-10-27T04:10:36Z brief · item TOOL-dSafePassage-27 · reason 6f9fc234407e memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-27-build-brief.md

2026-10-27T04:55:44Z dispatch · item f877719e TOOL-dSafePassage-28 · reason tools/push-main.test.sh memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-28.md memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-28-ledger.md memory/builds/dSafePassage/README.md

2026-10-27T04:55:50Z brief · item TOOL-dSafePassage-28 · reason fbdfd2ffab38 memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-28-build-brief.md
