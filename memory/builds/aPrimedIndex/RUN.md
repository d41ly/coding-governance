# aPrimedIndex - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 4827b20739c2b892b406cb262d99bb797f46c7ef
phase: VERIFYING
may: none
mode: prompt
run-branch: refs/heads/branch/enforce-index-regen-before-bars-acdde6
anchor-kind: local
cli-version: 2.1.293
lease-utc: 2026-10-11T01:23:28Z
pid-image: claude.exe
host: compeeto-agent
pid: 31536
session: 86a064cd-3532-4202-93cd-dd26651975d3
keepalive: 5d684520
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b726385f2b5b8fd16802925c02104377253a9045
anchor-ref: refs/heads/main
base: 15bbfa4f867262f3c862e2473688fc69d0566b7d

## Parked

2026-10-11T01:55:22Z brief · item TOOL-aPrimedIndex-1 · reason 193a86e7bf62 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md

2026-10-11T01:55:58Z brief · item TOOL-aPrimedIndex-2 · reason 193a86e7bf62 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md

2026-10-11T01:56:38Z brief · item TOOL-aPrimedIndex-3 · reason 193a86e7bf62 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md

2026-10-11T01:57:26Z brief · item TOOL-aPrimedIndex-4 · reason 193a86e7bf62 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md

2026-10-11T02:01:46Z dispatch · item beabe0bc TOOL-aPrimedIndex-1 · reason tools/memory-tree/kit.toml tools/codebase-map/kit.toml tools/workflows/kit.toml tools/unattended/kit.toml tools/lexicon/kit.toml tools/memory-recall/kit.toml tools/drift-audit/kit.toml tools/runlog/kit.toml tools/playbook/kit.toml tools/run-gates/README.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-1-1-acceptance-ledger.md memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md

2026-10-11T02:09:44Z dispatch · item beabe0bc TOOL-aPrimedIndex-1 · reason memory/builds/aPrimedIndex/README.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-1.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-2.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-3.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-4.md

2026-10-11T02:22:11Z dispatch · item d6214c0c TOOL-aPrimedIndex-2 · reason tools/run-gates/regen.py tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-2.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-2-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/features/run-gates.md

2026-10-11T03:04:50Z dispatch · item d6214c0c TOOL-aPrimedIndex-2 · reason memory/guides/SESSION-KICKOFF.md

2026-10-11T03:21:39Z dispatch · item 3a20991f TOOL-aPrimedIndex-3 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/guides/MERGE-BAR.md memory/guides/SESSION-KICKOFF.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-3.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-3-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md memory/map/generated/symbols.json

2026-10-11T03:53:36Z dispatch · item 77c7a903 TOOL-aPrimedIndex-4 · reason tools/push-main.sh tools/push-main.test.sh tools/run-gates/README.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-4.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-4-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md memory/map/generated/symbols.json

2026-10-11T05:56:53Z dispatch · item 77c7a903 TOOL-aPrimedIndex-4 · reason tools/push-main.sh tools/push-main.test.sh tools/run-gates/README.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-4.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-4-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md memory/map/generated/symbols.json

2026-10-11T06:11:05Z dispatch · item 77c7a903 TOOL-aPrimedIndex-4 · reason memory/builds/aPrimedIndex/BACKLOG.md memory/backlog/TOOL.md

2026-10-11T06:46:51Z review · item aPrimedIndex · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 2 · minors 18 · disposition promote

2026-10-11T06:47:12Z rescope · item add DEPL-aPrimedIndex-1 · reason closing review r1 H1 (id 7): govkit apply's verdict reader gets empty maps from the new preflight's early exit and can certify an install it never compared

2026-10-11T06:47:22Z rescope · item add TOOL-aPrimedIndex-6 · reason closing review r1 H2 (id 12): GATE_REGEN_CHECK is in no pre-push knob class, so the H49 arm reds and a caller can skip the preflight at the push boundary

2026-10-11T06:47:34Z rescope · item add TOOL-aPrimedIndex-7 · reason closing review r1 minors batch, regen verb and runner: M1 M2 M4 M5 M6 M7 M10 L1 L3 L4 and the README halves of H1 and L2

2026-10-11T06:47:49Z rescope · item add TOOL-aPrimedIndex-8 · reason closing review r1 minors batch, lander: M3 M8 M9 and the arms of L2; disjoint from TOOL-aPrimedIndex-7's write set

2026-10-11T06:59:54Z brief · item DEPL-aPrimedIndex-1 · reason cf9c7df95cf8 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md

2026-10-11T07:00:03Z brief · item TOOL-aPrimedIndex-6 · reason cf9c7df95cf8 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md

2026-10-11T07:00:12Z brief · item TOOL-aPrimedIndex-7 · reason cf9c7df95cf8 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md

2026-10-11T07:00:23Z brief · item TOOL-aPrimedIndex-8 · reason cf9c7df95cf8 memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md

2026-10-11T07:02:22Z dispatch · item 6e515ad1 DEPL-aPrimedIndex-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/aPrimedIndex/spec/2026-10-11-spec-DEPL-aPrimedIndex-1.md memory/builds/aPrimedIndex/build/2026-10-11-build-DEPL-aPrimedIndex-1-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md memory/builds/aPrimedIndex/prompts/2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md memory/map/generated/symbols.json

2026-10-11T07:09:04Z dispatch · item 837ae9ee TOOL-aPrimedIndex-6 · reason .githooks/pre-push memory/gotchas/a-runner-knob-owes-a-push-class.md memory/gotchas/INDEX.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-6.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-6-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md

2026-10-11T08:24:39Z dispatch · item 837ae9ee TOOL-aPrimedIndex-6 · reason memory/map/features/run-gates.md memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/symbols.json

2026-10-11T08:37:14Z dispatch · item 32ec9117 TOOL-aPrimedIndex-7 · reason tools/run-gates/regen.py tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md tools/memory-tree/kit.toml tools/unattended/README.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-7.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-7-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md memory/map/generated/symbols.json

2026-10-11T09:12:47Z dispatch · item 32ec9117 TOOL-aPrimedIndex-7 · reason memory/guides/SESSION-KICKOFF.md

2026-10-11T09:28:11Z dispatch · item 0ab48d83 TOOL-aPrimedIndex-8 · reason tools/push-main.sh tools/push-main.test.sh memory/project/unarmed-branches.txt memory/builds/aPrimedIndex/BACKLOG.md memory/backlog/TOOL.md memory/builds/aPrimedIndex/spec/2026-10-11-spec-TOOL-aPrimedIndex-8.md memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-8-1-acceptance-ledger.md memory/builds/aPrimedIndex/README.md memory/map/generated/symbols.json
