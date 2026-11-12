# aNimbleMend - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 72a9a7a8cc97f8bf46d1eabc046f84eaa5eabb7f
phase: BUILDING
may: none
mode: prompt
run-branch: refs/heads/branch/inline-bar-fixes-pass-legs-1a64f7
anchor-kind: local
cli-version: 2.1.321
lease-utc: 2026-11-12T13:21:52Z
pid-image: claude.exe
host: compeeto-agent
pid: 3468
session: 33df6610-2b81-4fa2-a831-77ce390341f0
keepalive: 3977d6b1
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 97e0841d7d0bdb38df314a1f8d01616a4d431dad
anchor-ref: refs/heads/main
base: 1265772cc365418ac6431a7f0f9e069f3bb79dc0

## Parked

2026-11-12T14:35:41Z dispatch · item 5484178a TOOL-aNimbleMend-1 · reason tools/policy/catalogue.toml tools/policy/README.md .governance/policy.json memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-1.md

2026-11-12T14:35:43Z brief · item TOOL-aNimbleMend-1 · reason 1cbf0ffc957c memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-build-brief.md

2026-11-12T14:38:27Z dispatch · item 5484178a TOOL-aNimbleMend-1 · reason tools/policy/catalogue.toml tools/policy/README.md .governance/policy.json memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-1.md

2026-11-12T14:42:23Z dispatch · item 75115e9a TOOL-aNimbleMend-1 · reason tools/policy/catalogue.toml tools/policy/README.md .governance/policy.json memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-1.md

2026-11-12T14:46:22Z dispatch · item 2121531d TOOL-aNimbleMend-1 · reason tools/policy/catalogue.toml tools/policy/README.md .governance/policy.json memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-1.md memory/LIVE.md memory/builds/aNimbleMend/README.md

2026-11-12T14:50:52Z dispatch · item a4a3b4ed TOOL-aNimbleMend-2 · reason tools/run-gates/pass_legs.py tools/run-gates/pass-leg-evidence.txt tools/gate-legs.json tools/run-gates/kit.toml tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-2.md

2026-11-12T14:50:54Z brief · item TOOL-aNimbleMend-2 · reason 3495a99c3b81 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-2-build-brief.md

2026-11-12T14:58:51Z dispatch · item a4a3b4ed TOOL-aNimbleMend-2 · reason tools/run-gates/pass_legs.py tools/run-gates/pass-leg-evidence.txt tools/gate-legs.json tools/run-gates/kit.toml tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-2.md memory/LIVE.md memory/builds/aNimbleMend/README.md memory/map/generated/symbols.json memory/guides/SESSION-KICKOFF.md

2026-11-12T15:05:16Z dispatch · item a02ce85e TOOL-aNimbleMend-4 · reason tools/gate-legs.json tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/run-gates/pass_legs.py tools/run-gates/pass-leg-evidence.txt tools/run-gates/run-gates.test.sh tools/run-gates/ceiling-evidence.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/playbook/core-pending.txt memory/map/features/memory-tree-hygiene.md memory/map/features/playbook.md memory/map/features/spec-tokens.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-4.md memory/LIVE.md memory/builds/aNimbleMend/README.md memory/guides/SESSION-KICKOFF.md

2026-11-12T15:05:18Z brief · item TOOL-aNimbleMend-4 · reason 7dd119a456c7 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-4-build-brief.md

2026-11-12T15:22:54Z dispatch · item 88efda13 TOOL-aNimbleMend-4 · reason tools/run-gates/ceiling-evidence.txt tools/run-gates/pass-leg-evidence.txt tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/builds/aNimbleMend/README.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-4.md

2026-11-12T15:38:05Z dispatch · item a49837d4 TOOL-aNimbleMend-3 · reason tools/run-gates/pass_legs.py tools/run-gates/derive-ceilings.py tools/run-gates/run-gates.evidence.test.sh tools/run-gates/README.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-3-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-3.md

2026-11-12T15:38:07Z brief · item TOOL-aNimbleMend-3 · reason ced0d1e4d184 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-3-build-brief.md

2026-11-12T15:48:32Z dispatch · item 19ed9d30 TOOL-aNimbleMend-5 · reason tools/run-gates/pass-legs.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-5-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-5.md

2026-11-12T15:48:34Z brief · item TOOL-aNimbleMend-5 · reason 6bd4fe894f72 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-5-build-brief.md

2026-11-12T16:04:55Z dispatch · item 8079fde2 TOOL-aNimbleMend-6 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/README.md tools/unattended/gate-guard.js tools/unattended/gate-guard.test.sh memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-6.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-6-1-acceptance-ledger.md

2026-11-12T16:04:57Z brief · item TOOL-aNimbleMend-6 · reason e7ee96fbeffa memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-6-build-brief.md
