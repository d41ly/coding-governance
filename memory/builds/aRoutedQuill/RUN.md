# aRoutedQuill - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: 5a836bf0fc940029136b4b3fd57a87f35ff40f26 · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: ff0b3dc327514e020eb47009de931d4dfd78c608
phase: REVIEWING
may: none
mode: slug
run-branch: refs/heads/branch/unattended-arouted-quill-71b76b
anchor-kind: default-branch
cli-version: 2.1.293
lease-utc: 2026-10-09T16:31:44Z
pid-image: claude.exe
host: compeeto-agent
pid: 7844
session: ace81ee6-6d50-4d21-9b54-3d0aa25d29c2
keepalive: f935a658
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 5a836bf0fc940029136b4b3fd57a87f35ff40f26
anchor-ref: refs/heads/main
base: 5a836bf0fc940029136b4b3fd57a87f35ff40f26

## Parked

2026-10-09T17:17:13Z decision · item The README's expected improvement 'An adopter gets the routing by installing gov, with nothing left to wire' is not implied by any spec: under TOOL-aRoutedQuill-5 F4, /session-kickoff stays a per-machine link that apply only prints, and the adopter confirms the scaffolded ROUTED_PATHS. Reword the bullet? · reason Options: reword the README bullet to name the one remaining per-machine step (the M2 cross-read's fix), or widen TOOL-aRoutedQuill-5 to install the kickoff link. Refused: the README's goal and expectations are the owner's description slot, which a run may not amend (M3), and widening unit 5 reverses the owner's F4 ruling.

2026-10-09T17:31:43Z dispatch · item 06071f44 TOOL-aRoutedQuill-1 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/.memory-tree.conf.example tools/memory-tree/gen_build_index.py memory/TEMPLATE-SPEC.md memory/HYGIENE.md .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-1.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-1-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/map/generated/symbols.json

2026-10-09T17:32:27Z brief · item TOOL-aRoutedQuill-1 · reason a956d5fc4f92 memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-build-brief.md

2026-10-09T18:26:38Z dispatch · item db0d57da KICK-aRoutedQuill-1 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md memory/map/features/session-kickoff.md memory/map/generated/symbols.json memory/builds/aRoutedQuill/spec/2026-10-09-spec-KICK-aRoutedQuill-1.md memory/builds/aRoutedQuill/build/2026-10-09-build-KICK-aRoutedQuill-1-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md

2026-10-09T18:27:10Z brief · item KICK-aRoutedQuill-1 · reason 7d083dbf1e6c memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-KICK-aRoutedQuill-1-build-brief.md

2026-10-09T19:17:37Z dispatch · item db0d57da KICK-aRoutedQuill-1 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md memory/map/features/session-kickoff.md memory/map/generated/symbols.json memory/builds/aRoutedQuill/spec/2026-10-09-spec-KICK-aRoutedQuill-1.md memory/builds/aRoutedQuill/build/2026-10-09-build-KICK-aRoutedQuill-1-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/backlog/TOOL.md

2026-10-09T19:25:16Z dispatch · item db0d57da KICK-aRoutedQuill-1 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md memory/map/features/session-kickoff.md memory/map/generated/symbols.json memory/builds/aRoutedQuill/spec/2026-10-09-spec-KICK-aRoutedQuill-1.md memory/builds/aRoutedQuill/build/2026-10-09-build-KICK-aRoutedQuill-1-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/backlog/TOOL.md memory/LIVE.md

2026-10-09T19:44:24Z dispatch · item 6b02b9d3 TOOL-aRoutedQuill-2 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/scratch-guard.fragment.json tools/hooks/agent-cap.js tools/hooks/README.md .claude/settings.json .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/features/agent-cap.md memory/map/generated/symbols.json memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-2.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-2-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T19:45:09Z brief · item TOOL-aRoutedQuill-2 · reason a82d37007455 memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-TOOL-aRoutedQuill-2-build-brief.md

2026-10-09T20:26:55Z brief · item TOOL-aRoutedQuill-3 · reason 4707aac72490 memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-TOOL-aRoutedQuill-3-build-brief.md

2026-10-09T20:51:48Z dispatch · item 82edc653 TOOL-aRoutedQuill-3 · reason tools/memory-tree/routed_commits.py tools/push-main.sh tools/push-main.test.sh memory/guides/SESSION-KICKOFF.md tools/memory-tree/tree_lib.py tools/memory-tree/transition_audit.py tools/memory-tree/kit.toml tools/memory-tree/.memory-tree.conf.example tools/memory-tree/README.md tools/gate-legs.json tools/run-gates/selftest-budgets.txt .memory-tree.conf memory/map/features/memory-tree-hygiene.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-3.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-3-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T21:16:55Z dispatch · item 82edc653 TOOL-aRoutedQuill-3 · reason tools/memory-tree/routed_commits.py tools/push-main.sh tools/push-main.test.sh memory/guides/SESSION-KICKOFF.md tools/memory-tree/tree_lib.py tools/memory-tree/transition_audit.py tools/memory-tree/kit.toml tools/memory-tree/.memory-tree.conf.example tools/memory-tree/README.md tools/gate-legs.json tools/run-gates/selftest-budgets.txt .memory-tree.conf memory/map/features/memory-tree-hygiene.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-3.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-3-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md tools/govkit/subject-pins.tsv

2026-10-09T21:28:27Z rescope · item defer TOOL-aRoutedQuill-6 · reason The trial needs four owner asks and an approved budget, and its own spec runs it only in an attended session; carried forward under UNATTENDED-STOPS.md section 15 with the ask TOOL-aRoutedQuill-8 filed in this build's BACKLOG.md.

2026-10-09T21:37:58Z brief · item TOOL-aRoutedQuill-4 · reason 67b39c2bc3af memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-TOOL-aRoutedQuill-4-build-brief.md

2026-10-09T21:53:14Z dispatch · item b6d2f89a TOOL-aRoutedQuill-4 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/scratch-guard-subagent.fragment.json tools/hooks/kit.toml tools/hooks/README.md .claude/settings.json memory/map/features/agent-cap.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-4.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-4-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T22:42:04Z dispatch · item 0585bcf8 PLAY-aRoutedQuill-1 · reason coding-governance-agents.template.md AGENTS.md tools/template-size-highwater.txt memory/guides/SESSION-KICKOFF.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-PLAY-aRoutedQuill-1.md memory/builds/aRoutedQuill/build/2026-10-09-build-PLAY-aRoutedQuill-1-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T22:42:24Z brief · item PLAY-aRoutedQuill-1 · reason 0b2e1142e8cf memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-PLAY-aRoutedQuill-1-build-brief.md

2026-10-09T23:13:32Z brief · item TOOL-aRoutedQuill-5 · reason f142d1100b0c memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-TOOL-aRoutedQuill-5-build-brief.md

2026-10-09T23:17:00Z dispatch · item fb57dce0 TOOL-aRoutedQuill-5 · reason tools/govkit/registry.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/matrix.py tools/hooks/kit.toml tools/memory-tree/kit.toml tools/memory-tree/adopt-memory-tree.sh tools/memory-tree/.memory-tree.conf.example tools/memory-tree/README.md tools/memory-tree/check-memory-hygiene.test.sh tools/check-wiring.sh tools/check-wiring.test.sh WIRE-INTO-PROJECT.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-5.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-5-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T23:35:39Z dispatch · item fb57dce0 TOOL-aRoutedQuill-5 · reason tools/govkit/registry.toml tools/govkit/entries/check-agent-cap-restatement.kit.toml tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/matrix.py tools/hooks/kit.toml tools/memory-tree/kit.toml tools/memory-tree/adopt-memory-tree.sh tools/memory-tree/.memory-tree.conf.example tools/memory-tree/README.md tools/memory-tree/check-memory-hygiene.test.sh tools/check-wiring.sh tools/check-wiring.test.sh WIRE-INTO-PROJECT.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-5.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-5-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-10T00:55:22Z dispatch · item 77d9cdf8 TOOL-aRoutedQuill-7 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/kit.toml memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md .unattended.conf memory/guides/SESSION-KICKOFF.md tools/template-size-limits.txt memory/map/features/unattended.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-7.md memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-7-1-acceptance-ledger.md memory/builds/aRoutedQuill/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-10T00:55:34Z brief · item TOOL-aRoutedQuill-7 · reason 716b55fb723a memory/builds/aRoutedQuill/prompts/2026-10-09-prompt-TOOL-aRoutedQuill-7-build-brief.md

2026-10-10T02:20:35Z review · item aRoutedQuill · reason verdict BLOCKED · blockers 1

2026-10-10T02:30:08Z review · item aRoutedQuill · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT · highs 2 · minors 24 · disposition promote

2026-10-10T02:30:21Z rescope · item add TOOL-aRoutedQuill-9 · reason closing review round 2 blocker: the routed-commits leg is red in WHOLE mode at the landing tip, because a reconcile merge brought in cutoff-day mints no waiver names

2026-10-10T02:30:25Z rescope · item add TOOL-aRoutedQuill-10 · reason closing review H1: the landing push grades the routed-commits leg in RANGE mode only, so main's CI sees a WHOLE-mode red the push never saw

2026-10-10T02:30:29Z rescope · item add TOOL-aRoutedQuill-11 · reason closing review H2: check-wiring reads MEMORY_ROOT with a default the write gate rejects, certifying an unarmed conf as armed

2026-10-10T02:30:32Z rescope · item add TOOL-aRoutedQuill-12 · reason closing review minors M1-M9 and L1-L7, batched as the severity rule requires

2026-10-10T02:57:36Z brief · item TOOL-aRoutedQuill-9 · reason 34d3dd117b22 memory/builds/aRoutedQuill/prompts/2026-10-10-prompt-TOOL-aRoutedQuill-9-build-brief.md
