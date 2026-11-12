# aNimbleMend - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: c428a23c390fbd605389e7f03f92665f0a44d5f8
phase: REVIEWING
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

2026-11-12T16:14:02Z dispatch · item 43f38988 TOOL-aNimbleMend-7 · reason tools/workflows/unattended-unit.js tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/unattended/VERBS.template.md tools/roles/SKILL.template.md memory/guides/UNATTENDED-VERBS.md .claude/skills/build/SKILL.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-7-1-acceptance-ledger.md

2026-11-12T16:14:04Z brief · item TOOL-aNimbleMend-7 · reason f3d516ac08bd memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-7-build-brief.md

2026-11-12T16:21:16Z dispatch · item 43f38988 TOOL-aNimbleMend-7 · reason tools/workflows/unattended-unit.js tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/unattended/VERBS.template.md tools/roles/SKILL.template.md memory/guides/UNATTENDED-VERBS.md .claude/skills/build/SKILL.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-7-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-7.md

2026-11-12T16:28:15Z rescope · item add TOOL-aNimbleMend-13 · reason the pass legs' first run over this build, after unit 7, redded eight legs: three false reds from legs that read the filtered leg list as their subject, a kit-subject leg the rule selects and the runner holds, a kit.toml sentence govkit selfcheck refuses, one unruled function name in pass_legs.py, and a stale docstring; each sits in a CLOSED unit

2026-11-12T16:53:41Z brief · item TOOL-aNimbleMend-13 · reason de1155b411c2 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-13-build-brief.md

2026-11-12T16:59:12Z dispatch · item b7bfe5fa TOOL-aNimbleMend-13 · reason tools/run-gates/pass-legs.sh tools/run-gates/pass_legs.py tools/gate-legs.json tools/run-gates/kit.toml tools/run-gates/derive-ceilings.py tools/run-gates/run-held-wsl.sh tools/run-gates/held_halves.py tools/run-gates/README.md tools/run-gates/run-gates.test.sh tools/run-gates/run-gates.evidence.test.sh memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-13-1-acceptance-ledger.md

2026-11-12T17:05:34Z dispatch · item b7bfe5fa TOOL-aNimbleMend-13 · reason memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/builds/aNimbleMend/README.md

2026-11-12T17:14:10Z dispatch · item cb1ee1c5 TOOL-aNimbleMend-13 · reason memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-13-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md memory/LIVE.md memory/builds/aNimbleMend/README.md

2026-11-12T17:22:55Z dispatch · item 1d010f40 TOOL-aNimbleMend-8 · reason tools/hooks/scratch-guard.js tools/hooks/agent-cap.js tools/hooks/scratch-guard.test.sh tools/hooks/README.md tools/memory-tree/routed_commits.py tools/memory-tree/tree_lib.py tools/memory-tree/build_records.py tools/memory-tree/gotchas.py memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-8.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-8-1-acceptance-ledger.md

2026-11-12T17:22:57Z brief · item TOOL-aNimbleMend-8 · reason 31459d489d13 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-8-build-brief.md

2026-11-12T17:34:14Z dispatch · item 1d010f40 TOOL-aNimbleMend-8 · reason memory/LIVE.md memory/builds/aNimbleMend/README.md memory/map/generated/symbols.json

2026-11-12T17:45:54Z dispatch · item 53c28923 TOOL-aNimbleMend-9 · reason tools/memory-tree/tree_lib.py tools/memory-tree/build_records.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-9.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-9-1-acceptance-ledger.md

2026-11-12T17:45:56Z brief · item TOOL-aNimbleMend-9 · reason c32de8f14408 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-9-build-brief.md

2026-11-12T17:58:54Z dispatch · item 53c28923 TOOL-aNimbleMend-9 · reason tools/memory-tree/tree_lib.py tools/memory-tree/build_records.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-9.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-9-1-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md

2026-11-12T18:08:29Z dispatch · item 15805b46 TOOL-aNimbleMend-9 · reason tools/memory-tree/check-memory-hygiene.test.sh memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-9.md

2026-11-12T18:19:24Z dispatch · item 17b2715d TOOL-aNimbleMend-10 · reason tools/memory-tree/routed_commits.py tools/memory-tree/README.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-10-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-10.md

2026-11-12T18:19:26Z brief · item TOOL-aNimbleMend-10 · reason 3d668574d22c memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-10-build-brief.md

2026-11-12T18:35:12Z dispatch · item cf606486 TOOL-aNimbleMend-11 · reason help/pass-legs.md help/red-fix-lane.md help/README.md help/policy.md help/charter.md help/reference/policy.md tools/govkit/usage.toml tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-11-1-acceptance-ledger.md

2026-11-12T18:35:13Z brief · item TOOL-aNimbleMend-11 · reason 046e2d56d6a4 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-11-build-brief.md

2026-11-12T18:43:01Z dispatch · item cf606486 TOOL-aNimbleMend-11 · reason help/pass-legs.md help/red-fix-lane.md help/README.md help/policy.md help/charter.md help/reference/policy.md tools/govkit/usage.toml tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-11-1-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md

2026-11-12T18:52:15Z dispatch · item b443d708 TOOL-aNimbleMend-11 · reason tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/template-size-limits.txt memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-11-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-11.md

2026-11-12T19:04:10Z dispatch · item 883e7e25 TOOL-aNimbleMend-12 · reason tools/policy/check_policy.py tools/policy/README.md tools/gate-legs.json memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-12-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-12.md

2026-11-12T19:04:12Z brief · item TOOL-aNimbleMend-12 · reason 38fe9d723c08 memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-12-build-brief.md

2026-11-12T19:22:19Z dispatch · item 883e7e25 TOOL-aNimbleMend-12 · reason tools/policy/check_policy.py tools/policy/README.md tools/gate-legs.json memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-12-1-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md

2026-11-12T19:35:04Z dispatch · item 679697d7 TOOL-aNimbleMend-12 · reason tools/policy/check_policy.py memory/builds/aNimbleMend/build/2026-11-12-build-TOOL-aNimbleMend-12-1-acceptance-ledger.md memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-12.md memory/LIVE.md memory/builds/aNimbleMend/README.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json

2026-11-12T19:50:29Z dispatch · item ee8a7d73 TOOL-aNimbleMend-12 · reason tools/policy/check_policy.py memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-12.md

2026-11-12T19:55:24Z dispatch · item ee8a7d73 TOOL-aNimbleMend-12 · reason tools/policy/check_policy.py memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-12.md memory/LIVE.md memory/builds/aNimbleMend/README.md

2026-11-12T20:20:13Z review · item aNimbleMend · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 3 · minors 20 · disposition promote

2026-11-12T20:20:16Z rescope · item add TOOL-aNimbleMend-14 · reason promoted at the closing diff review's round 1 exit (0 blockers, 3 highs, 20 minors): unit 14 the one HIGH item, unit 15 the mediums and lows batched

2026-11-12T20:20:18Z rescope · item add TOOL-aNimbleMend-15 · reason promoted at the closing diff review's round 1 exit (0 blockers, 3 highs, 20 minors): unit 14 the one HIGH item, unit 15 the mediums and lows batched
