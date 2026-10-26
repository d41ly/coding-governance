# dSafePassage - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 7f9df190edf29fffd43d3114277eeb851aedf3d0
phase: BUILDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dsafepassage-567339
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-26T08:36:02Z
pid-image: claude.exe
host: compeeto-agent
pid: 23020
session: c5f50d22-89c6-41d7-84e5-2382dcd49faa
keepalive: 6e25bf31
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
