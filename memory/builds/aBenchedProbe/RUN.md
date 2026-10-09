# aBenchedProbe - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: de219c587207cbd2234e40d87abfe8f001f029ee
phase: BUILDING
branch-sha: 2b26f187f03cc991edbf40b25550e6590e97d26e
branch-ref: refs/heads/branch/keen-chaplygin-6b0703
may: none
mode: prompt
run-branch: refs/heads/branch/keen-chaplygin-6b0703
anchor-kind: run-branch
cli-version: 2.1.293
lease-utc: 2026-10-09T17:01:10Z
pid-image: claude.exe
host: compeeto-agent
pid: 20984
session: 485cb99b-00b3-459e-ba5c-b84631a3e411
keepalive: 22a01d12
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
