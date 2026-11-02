# dOrderedCharter - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 02b35d060204f7a706ac76bb38ecbd60ebaa409c
phase: BUILDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dorderedcharter-725f52
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-11-02T15:36:10Z
pid-image: claude.exe
host: compeeto-agent
pid: 5584
session: 0394fa33-012c-408f-a840-e6e4cfaac23f
keepalive: a1fc4c14
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 8bec4cefd957d194660a8d7c2916f420b7299074
anchor-ref: refs/heads/main
base: 8bec4cefd957d194660a8d7c2916f420b7299074

## Parked

2026-11-02T18:02:17Z dispatch · item 98995aa2 PLAY-dOrderedCharter-18 · reason tools/memory-tree/id_grammar.py tools/memory-recall/extract.py tools/memory-recall/recall_conf.py tools/memory-recall/bench.py tools/memory-recall/verbatim.json tools/memory-recall/selftest.py tools/memory-recall/README.md tools/memory-tree/backlog.py tools/memory-tree/corpus_ids.py tools/memory-tree/merge-rows.py tools/memory-tree/transition_audit.py tools/memory-tree/gen_build_index.py tools/memory-tree/row_grammar.py tools/memory-tree/gotchas.py tools/memory-tree/migrate_backlog.py tools/memory-tree/check-verdict-epoch.sh tools/memory-tree/check-verdict-epoch.test.sh tools/memory-tree/kit.toml tools/memory-tree/merge-rows.test.sh tools/memory-tree/transition-audit.test.sh tools/memory-tree/check-memory-hygiene.test.sh tools/drift-audit/drift_report.py tools/drift-audit/selftest.py tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh skills/session-kickoff/manifest-check.test.sh .githooks/straggler-guard.test.sh tools/check-wiring.test.sh memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-18.md memory/builds/dOrderedCharter/README.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-18-ledger.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-18-deviation-184.md memory/map/generated/symbols.json

2026-11-02T18:02:26Z brief · item PLAY-dOrderedCharter-18 · reason c2157c65924c memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-18-build-brief.md

2026-11-02T19:38:24Z dispatch · item 64454cba PLAY-dOrderedCharter-16 · reason tools/playbook/layers.toml tools/playbook/check_layers.py tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/memory-tree/import_walk.py tools/memory-tree/check-verdict-epoch.sh tools/memory-tree/check-verdict-epoch.test.sh tools/agent-instructions/kit.toml tools/branch-reconcile/kit.toml tools/codebase-map/kit.toml tools/drift-audit/kit.toml tools/gate-lint/kit.toml tools/govkit/entries/check-agent-cap-restatement.kit.toml tools/govkit/entries/check-install-prefix.kit.toml tools/govkit/entries/check-kit-versions.kit.toml tools/govkit/entries/check-line-length.kit.toml tools/govkit/entries/check-microformats.kit.toml tools/govkit/entries/check-placeholders.kit.toml tools/govkit/entries/check-testsuite-counts.kit.toml tools/govkit/entries/check-wiring.kit.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/entries/playbook.kit.toml tools/govkit/entries/push-main.kit.toml tools/govkit/entries/settings-merge.kit.toml tools/hooks/kit.toml tools/lexicon/kit.toml tools/memory-recall/kit.toml tools/memory-tree/kit.toml tools/playbook/kit.toml tools/policy/kit.toml tools/process-monitor/kit.toml tools/pytest-parallel-guardrails/kit.toml tools/roles/kit.toml tools/run-gates/kit.toml tools/runlog/kit.toml tools/unattended/kit.toml tools/workflows/kit.toml tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/playbook.md memory/map/generated/symbols.json memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md memory/builds/dOrderedCharter/README.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-16-ledger.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-16-deviation-163.md

2026-11-02T19:38:43Z brief · item PLAY-dOrderedCharter-16 · reason f9e8e0dc0a19 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-16-build-brief.md

2026-11-02T20:06:35Z rescope · item add PLAY-dOrderedCharter-61 · reason repairs PLAY-dOrderedCharter-16's CLOSED check_layers.py, which unit 17's builder found over-reporting (run wf_dce016de-13e): message text, .git/ journal paths, id strings and fixture pins read as edges, the check's own read of govkit/entries reads as one, and core test suites building fixtures from optional kits have no disposition; also lands unit 16's owed playbook render selftest guard

2026-11-02T21:40:43Z dispatch · item ebb0ebfe PLAY-dOrderedCharter-61 · reason tools/playbook/check_layers.py tools/playbook/adopt-playbook.sh tools/playbook/README.md tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-11-02-spec-PLAY-dOrderedCharter-61.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-61-ledger.md

2026-11-02T21:40:53Z brief · item PLAY-dOrderedCharter-61 · reason ed7e877c03ed memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-61-build-brief.md

2026-11-02T22:03:42Z brief · item PLAY-dOrderedCharter-17 · reason f70b313113de memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-17-build-brief.md

2026-11-02T22:20:45Z rescope · item add PLAY-dOrderedCharter-62 · reason unit 17's builder found (run wf_2c160031-b97) that check_layers.py matches a flat govkit entry's optional part only as a full tools/<file> path, which the install-prefix ban refuses, and never resolves {prefix}/; the check is CLOSED units 16 and 61's, so its correction is a new unit before 17

2026-11-02T23:22:11Z dispatch · item ab1edfb5 PLAY-dOrderedCharter-62 · reason tools/playbook/check_layers.py tools/playbook/adopt-playbook.sh tools/playbook/README.md memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-11-03-spec-PLAY-dOrderedCharter-62.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-62-ledger.md

2026-11-02T23:22:22Z brief · item PLAY-dOrderedCharter-62 · reason ce2111399082 memory/builds/dOrderedCharter/prompts/2026-11-03-prompt-PLAY-dOrderedCharter-62-build-brief.md
