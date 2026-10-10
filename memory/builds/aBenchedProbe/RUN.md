# aBenchedProbe - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 76ee1a1c257d0ac52fa0e2088acc9e963dc322c8
phase: BUILDING
branch-sha: 2b26f187f03cc991edbf40b25550e6590e97d26e
branch-ref: refs/heads/branch/keen-chaplygin-6b0703
may: none
mode: prompt
run-branch: refs/heads/branch/keen-chaplygin-6b0703
anchor-kind: run-branch
cli-version: 2.1.293
lease-utc: 2026-10-10T05:57:06Z
pid-image: claude.exe
host: compeeto-agent
pid: 24144
session: 485cb99b-00b3-459e-ba5c-b84631a3e411
keepalive: 7b8cb16c
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 5a836bf0fc940029136b4b3fd57a87f35ff40f26
anchor-ref: refs/heads/main
base: 2b26f187f03cc991edbf40b25550e6590e97d26e

## Parked

2026-10-09T18:06:41Z dispatch · item de219c58 TOOL-aBenchedProbe-1 · reason tools/govkit/entries/push-main.kit.toml tools/gate-legs.json tools/govkit/subject-pins.tsv memory/builds/aBenchedProbe/spec/2026-10-09-spec-TOOL-aBenchedProbe-1.md memory/builds/aBenchedProbe/build/2026-10-09-build-TOOL-aBenchedProbe-1-1-acceptance-ledger.md

2026-10-09T18:07:43Z brief · item TOOL-aBenchedProbe-1 · reason 646acc691479 memory/builds/aBenchedProbe/prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md

2026-10-09T18:17:22Z dispatch · item de219c58 TOOL-aBenchedProbe-1 · reason tools/govkit/entries/push-main.kit.toml tools/gate-legs.json tools/govkit/subject-pins.tsv memory/builds/aBenchedProbe/spec/2026-10-09-spec-TOOL-aBenchedProbe-1.md memory/builds/aBenchedProbe/build/2026-10-09-build-TOOL-aBenchedProbe-1-1-acceptance-ledger.md memory/builds/aBenchedProbe/README.md

2026-10-09T18:21:35Z dispatch · item de219c58 TOOL-aBenchedProbe-1 · reason tools/govkit/entries/push-main.kit.toml tools/gate-legs.json tools/govkit/subject-pins.tsv memory/builds/aBenchedProbe/spec/2026-10-09-spec-TOOL-aBenchedProbe-1.md memory/builds/aBenchedProbe/build/2026-10-09-build-TOOL-aBenchedProbe-1-1-acceptance-ledger.md memory/builds/aBenchedProbe/README.md memory/guides/SESSION-KICKOFF.md

2026-10-09T18:35:28Z dispatch · item 894952cb TOOL-aBenchedProbe-2 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh memory/builds/aBenchedProbe/spec/2026-10-09-spec-TOOL-aBenchedProbe-2.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aBenchedProbe/README.md

2026-10-09T18:37:10Z brief · item TOOL-aBenchedProbe-2 · reason 646acc691479 memory/builds/aBenchedProbe/prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md

2026-10-09T19:13:56Z dispatch · item 894952cb TOOL-aBenchedProbe-2 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh memory/builds/aBenchedProbe/spec/2026-10-09-spec-TOOL-aBenchedProbe-2.md memory/LIVE.md memory/ledger/2026-10.md memory/builds/aBenchedProbe/README.md memory/guides/SESSION-KICKOFF.md

2026-10-09T19:23:07Z dispatch · item e0448998 DEPL-aBenchedProbe-1 · reason tools/govkit/govkit.py memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-1.md memory/builds/aBenchedProbe/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-09T19:23:41Z brief · item DEPL-aBenchedProbe-1 · reason 646acc691479 memory/builds/aBenchedProbe/prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md

2026-10-09T19:47:46Z dispatch · item 1696d09d DEPL-aBenchedProbe-2 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/entries/push-main.kit.toml tools/run-gates/README.md memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-2.md memory/builds/aBenchedProbe/build/2026-10-09-build-DEPL-aBenchedProbe-2-1-acceptance-ledger.md memory/builds/aBenchedProbe/README.md memory/LIVE.md memory/ledger/2026-10.md memory/guides/SESSION-KICKOFF.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-09T19:48:14Z brief · item DEPL-aBenchedProbe-2 · reason 646acc691479 memory/builds/aBenchedProbe/prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md

2026-10-09T20:18:02Z review · item aBenchedProbe · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 7 · disposition promote

2026-10-09T20:18:43Z rescope · item add DEPL-aBenchedProbe-3 · reason closing review round 1 HIGH H1: govkit selfcheck 7j4's liveness reds fire on govkit selftest.py's minimal scratch-gov fixtures and its AC5 fixture, so the govkit selftest suite reds

2026-10-09T20:19:21Z rescope · item add DEPL-aBenchedProbe-4 · reason closing review round 1 minors batched: H-M1 the receipt-after-keep and second-apply arm, H-M2 persistent staged-break arms for 7j4 and the 7h ceiling clause, H-L1 the dead manifest_chunk pre-init, H-L2 CE4's leg check tied to the keep line

2026-10-09T23:35:59Z resume · item aBenchedProbe · reason working · keepalive e76c0db2 · manual

2026-10-09T23:46:05Z brief · item DEPL-aBenchedProbe-3 · reason 646acc691479 memory/builds/aBenchedProbe/prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md

2026-10-09T23:47:33Z dispatch · item 76ee1a1c DEPL-aBenchedProbe-3 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md memory/builds/aBenchedProbe/build/2026-10-09-build-DEPL-aBenchedProbe-3-1-acceptance-ledger.md memory/builds/aBenchedProbe/README.md memory/LIVE.md memory/ledger/2026-10.md memory/guides/SESSION-KICKOFF.md

2026-10-10T01:47:19Z resume · item aBenchedProbe · reason working · keepalive c936c9dd · manual

2026-10-10T01:55:17Z dispatch · item 230af495 DEPL-aBenchedProbe-3 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md memory/builds/aBenchedProbe/build/2026-10-09-build-DEPL-aBenchedProbe-3-1-acceptance-ledger.md

2026-10-10T03:52:34Z resume · item aBenchedProbe · reason working · keepalive 22925fb2 · manual

2026-10-10T04:04:38Z dispatch · item 230af495 DEPL-aBenchedProbe-3 · reason memory/builds/aBenchedProbe/README.md memory/LIVE.md

2026-10-10T05:57:17Z resume · item aBenchedProbe · reason working · keepalive 7b8cb16c · manual

2026-10-10T05:57:51Z brief · item DEPL-aBenchedProbe-4 · reason 646acc691479 memory/builds/aBenchedProbe/prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md

2026-10-10T05:58:30Z dispatch · item bc5e5cf2 DEPL-aBenchedProbe-4 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-4.md memory/builds/aBenchedProbe/build/2026-10-10-build-DEPL-aBenchedProbe-4-1-acceptance-ledger.md memory/gotchas/line-claim-matched-over-the-whole-output.md memory/gotchas/INDEX.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/aBenchedProbe/README.md memory/LIVE.md

2026-10-10T06:00:51Z dispatch · item bc5e5cf2 DEPL-aBenchedProbe-4 · reason memory/map/features/memory-tree-hygiene.md

2026-10-10T06:01:37Z dispatch · item bc5e5cf2 DEPL-aBenchedProbe-4 · reason memory/map/generated/CARDS.md
