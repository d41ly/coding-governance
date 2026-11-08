# dOrderedCharter - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: ae6735c1f237423022016714b3da193f8ed971b7 · park · 146 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 8bf37ad532be8132b464c2253a6e7d0f352999ee
phase: BUILDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dorderedcharter-725f52
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-11-08T03:16:27Z
pid-image: claude.exe
host: compeeto-agent
pid: 20408
session: 0394fa33-012c-408f-a840-e6e4cfaac23f
keepalive: 84c0e58e
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

2026-11-03T00:33:35Z dispatch · item 93a13a05 PLAY-dOrderedCharter-17 · reason tools/playbook/layers.toml tools/playbook/README.md tools/memory-tree/kit.toml tools/memory-tree/gen_build_index.py tools/memory-tree/gotchas.py tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/README.md tools/memory-tree/.memory-tree.conf.example tools/push-main.sh tools/push-main.test.sh .githooks/pre-push .githooks/pre-push.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/kit.toml tools/check-install-prefix.sh tools/check-install-prefix.test.sh tools/run-gates/run-gates.sh tools/run-gates/kit.toml tools/govkit/entries/push-main.kit.toml tools/govkit/entries/check-install-prefix.kit.toml tools/govkit/entries/check-kit-versions.kit.toml tools/govkit/entries/check-wiring.kit.toml tools/govkit/entries/settings-merge.kit.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/policy/kit.toml tools/check-wiring.test.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-17.md memory/builds/dOrderedCharter/README.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-17-ledger.md memory/map/generated/symbols.json

2026-11-03T00:33:43Z brief · item PLAY-dOrderedCharter-17 · reason 70aafa14179d memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-17-build-brief.md

2026-11-03T03:23:23Z dispatch · item 20cb62fa PLAY-dOrderedCharter-19 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/namespaces.toml tools/playbook/aliases.toml tools/playbook/positional-refs.txt tools/playbook/policy_value.py tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/lib/coverage_join.py tools/lib/common_dir.py tools/lib/resolve-python.test.sh tools/memory-tree/coverage_join.py tools/codebase-map/map_lib.py tools/codebase-map/gen_map.py tools/codebase-map/map_diff.py tools/codebase-map/selftest.py tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py tools/memory-recall/query.py tools/gate-legs.json tools/run-gates/run-gates.test.sh tools/run-gates/ceiling-evidence.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/map/features/playbook.md memory/map/features/codebase-map.md memory/map/features/memory-tree-hygiene.md memory/map/features/memory-recall.md memory/map/baseline.toml help/tags.md help/README.md memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md memory/builds/dOrderedCharter/README.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-19-ledger.md

2026-11-03T03:23:46Z brief · item PLAY-dOrderedCharter-19 · reason 92ba52f11a9b memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-19-build-brief.md

2026-11-03T03:35:32Z dispatch · item 20cb62fa PLAY-dOrderedCharter-19 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/namespaces.toml tools/playbook/aliases.toml tools/playbook/positional-refs.txt tools/playbook/policy_value.py tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/lib/coverage_join.py tools/lib/common_dir.py tools/lib/resolve-python.test.sh tools/memory-tree/coverage_join.py tools/codebase-map/map_lib.py tools/codebase-map/gen_map.py tools/codebase-map/map_diff.py tools/codebase-map/selftest.py tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py tools/memory-recall/query.py tools/gate-legs.json tools/run-gates/run-gates.test.sh tools/run-gates/ceiling-evidence.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/govkit/usage.toml memory/project/docs-undocumented.txt tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/map/features/playbook.md memory/map/features/codebase-map.md memory/map/features/memory-tree-hygiene.md memory/map/features/memory-recall.md memory/map/baseline.toml help/tags.md help/README.md memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md memory/builds/dOrderedCharter/README.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-19-ledger.md

2026-11-03T05:14:25Z dispatch · item 793d3435 PLAY-dOrderedCharter-19 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/namespaces.toml tools/playbook/aliases.toml tools/playbook/positional-refs.txt tools/playbook/policy_value.py tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/lib/coverage_join.py tools/lib/common_dir.py tools/lib/resolve-python.test.sh tools/memory-tree/coverage_join.py tools/codebase-map/map_lib.py tools/codebase-map/gen_map.py tools/codebase-map/map_diff.py tools/codebase-map/selftest.py tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py tools/memory-recall/query.py tools/gate-legs.json tools/run-gates/run-gates.test.sh tools/run-gates/ceiling-evidence.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/govkit/usage.toml memory/project/docs-undocumented.txt tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/map/features/playbook.md memory/map/features/codebase-map.md memory/map/features/memory-tree-hygiene.md memory/map/features/memory-recall.md memory/map/baseline.toml .lexicon.conf help/tags.md help/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md memory/builds/dOrderedCharter/README.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-19-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-19-deviation-195.md

2026-11-03T05:14:35Z brief · item PLAY-dOrderedCharter-19 · reason 49c19d3abed6 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-19-build-brief.md

2026-11-03T06:53:20Z dispatch · item 5c76b68a PLAY-dOrderedCharter-10 · reason tools/playbook/namespaces.toml tools/playbook/readers.toml tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/layers.toml tools/playbook/kit.toml tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/lexicon/lexicon.py tools/lexicon/selftest.py help/tags.md tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-10-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-10-deviation-103.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-11-03T06:54:22Z brief · item PLAY-dOrderedCharter-10 · reason 3272fb25847a memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-10-build-brief.md

2026-11-03T07:27:36Z dispatch · item 5c76b68a PLAY-dOrderedCharter-10 · reason tools/playbook/namespaces.toml tools/playbook/readers.toml tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/layers.toml tools/playbook/kit.toml tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/lexicon/lexicon.py tools/lexicon/selftest.py help/tags.md tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-10-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-10-deviation-103.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-10-deviation-104.md

2026-11-03T08:03:16Z dispatch · item cf0c9457 PLAY-dOrderedCharter-44 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh tools/playbook/README.md help/tags.md memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-44.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-44-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-11-03T08:03:28Z brief · item PLAY-dOrderedCharter-44 · reason 46ebb48cc44c memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-44-build-brief.md

2026-11-03T09:52:37Z dispatch · item ee6d3cff PLAY-dOrderedCharter-22 · reason memory/project/chain.toml tools/playbook/gov_tag.py tools/playbook/tag_index.py tools/playbook/namespaces.toml .memory-tree.conf tools/playbook/adopt-playbook.sh help/tags.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-22.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-22-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-22-deviation-schema-row.md

2026-11-03T09:52:49Z brief · item PLAY-dOrderedCharter-22 · reason 7835450e3501 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-22-build-brief.md

2026-11-03T10:27:40Z dispatch · item ee6d3cff PLAY-dOrderedCharter-22 · reason memory/project/chain.toml tools/playbook/gov_tag.py tools/playbook/tag_index.py tools/playbook/namespaces.toml .memory-tree.conf tools/playbook/adopt-playbook.sh help/tags.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-22.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-22-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-22-deviation-schema-row.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-22-deviation-222.md

2026-11-03T11:17:30Z dispatch · item b770b1d5 PLAY-dOrderedCharter-51 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh tools/playbook/README.md help/tags.md tools/govkit/usage.toml tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-51.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-51-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-51-deviation-512.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-51-deviation-513.md memory/builds/dOrderedCharter/README.md memory/map/generated/symbols.json

2026-11-03T11:17:37Z brief · item PLAY-dOrderedCharter-51 · reason 7a3f27cddb67 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-51-build-brief.md

2026-11-03T12:01:39Z rescope · item add PLAY-dOrderedCharter-63 · reason unit 24's dispatch was refused (run wf_7db2dca6-39a): check-spec-tokens.py's LIVE pattern matches a fenced **Status:** OPEN example inside DEFERRED TOOL-dIndexedDesign-12, so that spec is graded live and its §7 owes the playbook render selftest leg unit 51's guard added; the checker reads a spec's status from its header line, outside fences

2026-11-03T13:12:44Z dispatch · item 6e0f4aad PLAY-dOrderedCharter-24 · reason tools/playbook/edges.toml tools/playbook/edge_grammar.py tools/memory-tree/design_lib.py tools/playbook/README.md tools/playbook/adopt-playbook.sh help/tags.md tools/govkit/usage.toml memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-24.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-24-ledger.md memory/builds/dOrderedCharter/README.md

2026-11-03T13:13:24Z brief · item PLAY-dOrderedCharter-24 · reason 4f744b3d9aa1 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-24-build-brief.md

2026-11-03T14:07:03Z dispatch · item 8f63a0e0 PLAY-dOrderedCharter-63 · reason tools/check-spec-tokens.py tools/check-spec-tokens.test.sh memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-11-03-spec-PLAY-dOrderedCharter-63.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-63-ledger.md memory/builds/dOrderedCharter/README.md

2026-11-03T14:07:21Z brief · item PLAY-dOrderedCharter-63 · reason 06aabed1ee4d memory/builds/dOrderedCharter/prompts/2026-11-03-prompt-PLAY-dOrderedCharter-63-build-brief.md

2026-11-03T14:47:58Z brief · item PLAY-dOrderedCharter-28 · reason c357d49e6d7f memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-28-build-brief.md

2026-11-03T15:08:51Z dispatch · item e05e1c08 PLAY-dOrderedCharter-28 · reason tools/playbook/edges.toml tools/playbook/edge_grammar.py tools/playbook/namespaces.toml tools/playbook/gov_tag.py tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/govkit/usage.toml tools/run-gates/ceiling-evidence.txt memory/map/features/playbook.md help/tags.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-28-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-28-deviation-283.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-03T15:55:45Z brief · item PLAY-dOrderedCharter-28 · reason bb9eaa29cecc memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-28-build-brief.md

2026-11-03T16:56:17Z dispatch · item 8aa5913b PLAY-dOrderedCharter-28 · reason tools/playbook/edges.toml tools/playbook/edge_grammar.py tools/playbook/namespaces.toml tools/playbook/gov_tag.py tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/govkit/usage.toml tools/run-gates/ceiling-evidence.txt memory/map/features/playbook.md help/tags.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-28-ledger.md memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-28-deviation-283.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-03T21:17:45Z dispatch · item 233f2411 PLAY-dOrderedCharter-26 · reason tools/playbook/positional.py tools/playbook/gov_tag.py tools/playbook/positional-refs.txt tools/gate-legs.json memory/guides/SESSION-KICKOFF.md tools/workflows/REVIEW-PROTOCOL.template.md memory/guides/REVIEW-PROTOCOL.md tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/drift-audit-code.template.js tools/workflows/drift-audit-code.js tools/workflows/drift-audit-state.template.js tools/workflows/drift-audit-state.js tools/roles/agents/gov-diff-reviewer.agent.md .claude/agents/gov-diff-reviewer.md tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/map/features/playbook.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-26-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-03T21:17:56Z brief · item PLAY-dOrderedCharter-26 · reason dfea28707eab memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-26-build-brief.md

2026-11-03T22:00:23Z dispatch · item effc343c PLAY-dOrderedCharter-47 · reason tools/playbook/positional.py tools/playbook/gov_tag.py tools/playbook/README.md memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-47-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/map/features/playbook.md

2026-11-03T22:00:30Z brief · item PLAY-dOrderedCharter-47 · reason 97c0fc633509 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-47-build-brief.md

2026-11-03T22:47:00Z dispatch · item 41bd0369 PLAY-dOrderedCharter-48 · reason tools/playbook/positional.py tools/playbook/positional-producers.txt tools/playbook/gov_tag.py tools/roles/agents/gov-spec-writer.agent.md .claude/agents/gov-spec-writer.md tools/workflows/orient-counterfactual.js tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/playbook/README.md memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-48.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-48-ledger.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/map/features/playbook.md memory/LIVE.md memory/builds/dOrderedCharter/README.md

2026-11-03T22:47:20Z brief · item PLAY-dOrderedCharter-48 · reason 88121eb8685c memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-48-build-brief.md

2026-11-03T23:35:06Z dispatch · item c7269a97 PLAY-dOrderedCharter-50 · reason tools/run-gates/owed_rows.py tools/run-gates/run-gates.test.sh tools/run-gates/kit.toml tools/govkit/subject-pins.tsv tools/playbook/kit.toml memory/map/features/run-gates.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/CARDS.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-50-ledger.md

2026-11-03T23:35:50Z brief · item PLAY-dOrderedCharter-50 · reason ed3a9839799f memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-50-build-brief.md

2026-11-04T00:09:43Z dispatch · item c7269a97 PLAY-dOrderedCharter-50 · reason tools/run-gates/owed_rows.py tools/run-gates/run-gates.test.sh tools/run-gates/kit.toml tools/govkit/subject-pins.tsv tools/govkit/selftest.py tools/playbook/kit.toml memory/map/features/run-gates.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/CARDS.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-50-ledger.md memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-50.md memory/builds/dOrderedCharter/README.md

2026-11-04T01:01:27Z rescope · item add PLAY-dOrderedCharter-64 · reason the template-conformance check's revision-scope arm accepts only the section-sign form, which unit 26's positional check grades and unit 53's per-line rule will red; one arm must accept a section named in words, a class repair before unit 53 (sweep fold 2)

2026-11-04T02:01:36Z dispatch · item c862b645 PLAY-dOrderedCharter-25 · reason tools/playbook/gov_tag.py tools/playbook/tag_bundle.py tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/map/features/playbook.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json tools/govkit/subject-pins.tsv tools/playbook/kit.toml tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-25-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-04T02:03:10Z brief · item PLAY-dOrderedCharter-25 · reason a16234889d3e memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-25-build-brief.md

2026-11-04T02:23:02Z dispatch · item c862b645 PLAY-dOrderedCharter-25 · reason tools/playbook/gov_tag.py tools/playbook/tag_bundle.py tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/map/features/playbook.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json tools/govkit/subject-pins.tsv tools/playbook/kit.toml tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-25-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/backlog/PLAY.md

2026-11-04T03:47:17Z dispatch · item 106e97a4 PLAY-dOrderedCharter-7 · reason tools/playbook/core.py tools/playbook/principles.toml tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/memory-tree/build_records.py tools/memory-tree/deviation_join.py tools/memory-tree/check-verdict-epoch.sh tools/gate-legs.json tools/playbook/edges.toml memory/map/features/playbook.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json tools/govkit/subject-pins.tsv tools/playbook/kit.toml tools/govkit/registry.toml tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/backlog/PLAY.md memory/builds/dOrderedCharter/README.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-7-ledger.md

2026-11-04T03:47:43Z brief · item PLAY-dOrderedCharter-7 · reason d022fda36642 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-7-build-brief.md

2026-11-04T04:52:03Z dispatch · item 40427f33 PLAY-dOrderedCharter-64 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/.memory-tree.conf.example .memory-tree.conf memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-4.md memory/builds/dOrderedCharter/spec/2026-11-04-spec-PLAY-dOrderedCharter-64.md memory/builds/dOrderedCharter/build/2026-11-04-build-PLAY-dOrderedCharter-64-ledger.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/backlog/PLAY.md memory/builds/dOrderedCharter/README.md

2026-11-04T04:52:15Z brief · item PLAY-dOrderedCharter-64 · reason 9d7da2401920 memory/builds/dOrderedCharter/prompts/2026-11-04-prompt-PLAY-dOrderedCharter-64-build-brief.md

2026-11-04T05:05:15Z rescope · item add PLAY-dOrderedCharter-65 · reason unit 7's kinds register mints kind.kit, kind.layer and kind.practice, whose first segment is a namespace word; the tags leg reds six times (mid-build lint after unit 7); a repair renames them before unit 53

2026-11-04T05:50:08Z dispatch · item f4acbd4a PLAY-dOrderedCharter-65 · reason tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/playbook/core.py memory/builds/dOrderedCharter/spec/2026-11-04-spec-PLAY-dOrderedCharter-65.md memory/builds/dOrderedCharter/build/2026-11-04-build-PLAY-dOrderedCharter-65-ledger.md memory/LIVE.md memory/builds/dOrderedCharter/README.md

2026-11-04T05:50:16Z brief · item PLAY-dOrderedCharter-65 · reason d0c4cbe4d526 memory/builds/dOrderedCharter/prompts/2026-11-04-prompt-PLAY-dOrderedCharter-65-build-brief.md

2026-11-04T06:35:07Z dispatch · item 0e89b19b PLAY-dOrderedCharter-53 · reason tools/playbook/positional.py tools/playbook/gov_tag.py memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-53.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-53-ledger.md memory/LIVE.md memory/builds/dOrderedCharter/README.md

2026-11-04T06:35:15Z brief · item PLAY-dOrderedCharter-53 · reason ba40d4516796 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-53-build-brief.md

2026-11-04T06:47:25Z dispatch · item 0e89b19b PLAY-dOrderedCharter-53 · reason tools/playbook/README.md memory/map/generated/symbols.json

2026-11-04T07:25:43Z dispatch · item 794c3df3 PLAY-dOrderedCharter-13 · reason tools/playbook/instruction_units.py tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/playbook.md memory/map/generated/MAP.md memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-13.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-13-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-04T07:25:53Z brief · item PLAY-dOrderedCharter-13 · reason 8bb434b1e95e memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-13-build-brief.md

2026-11-04T08:09:00Z dispatch · item 17a4ab1a PLAY-dOrderedCharter-42 · reason tools/memory-tree/tree_lib.py tools/memory-tree/build_records.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/check-memory-hygiene.test.sh memory/HYGIENE.md memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-42-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-11-04T08:09:09Z brief · item PLAY-dOrderedCharter-42 · reason 9ab0ced973a3 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-42-build-brief.md

2026-11-04T08:26:49Z dispatch · item 17a4ab1a PLAY-dOrderedCharter-42 · reason memory/backlog/PLAY.md

2026-11-04T09:18:22Z dispatch · item a294f103 PLAY-dOrderedCharter-12 · reason tools/playbook/instruction_units.py tools/playbook/render_playbook.py .governance/instructions.lock AGENTS.md skills/session-kickoff/SKILL.md WIRE-INTO-PROJECT.md tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/playbook.md memory/map/generated/MAP.md memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/map/generated/inventories.json tools/memory-tree/build_records.py memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-12-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-04T09:18:45Z brief · item PLAY-dOrderedCharter-12 · reason 86295d77fc91 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-12-build-brief.md

2026-11-04T09:43:54Z dispatch · item 9cc88e71 PLAY-dOrderedCharter-12 · reason .lexicon.conf

2026-11-04T10:49:29Z dispatch · item 4773fbef PLAY-dOrderedCharter-9 · reason tools/playbook/instruction_units.py tools/playbook/tag_index.py tools/playbook/edge_grammar.py tools/playbook/gov_tag.py tools/playbook/namespaces.toml tools/playbook/edges.toml tools/playbook/tag_bundle.py help/tags.md memory/map/features/session-kickoff.md memory/map/features/playbook.md memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-9-ledger.md memory/builds/dOrderedCharter/build/2026-11-04-build-PLAY-dOrderedCharter-9-deviation-94.md

2026-11-04T10:49:41Z brief · item PLAY-dOrderedCharter-9 · reason 192198ec568c memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-9-build-brief.md

2026-11-04T11:19:38Z dispatch · item 4773fbef PLAY-dOrderedCharter-9 · reason memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-04T12:04:50Z decision · item Should the default kit set gain playbook-render, so the roles kit can require it and its agents scope can leave render_agents.py? · reason Options: (a) widen the default set, which changes what every install lands; (e) keep the agents scope on render_agents.py, the run's interim ruling. Refused because widening the default set is the owner's.

2026-11-04T12:04:54Z decision · item May BUILD-METHOD's size cap be raised so the guide can carry its instruction envelope? · reason Spec 3's open fork. The render is 30659 of 30720 bytes and the envelope needs at least 80. The cap's own row reserves any raise to the owner, and every option that leaves the cap alone hits a veto. Unit 3 cannot register BUILD-METHOD without this.

2026-11-04T13:41:13Z dispatch · item 4128bf11 PLAY-dOrderedCharter-20 · reason tools/playbook/instruction_units.py tools/playbook/render_playbook.py tools/playbook/adopt-playbook.sh tools/playbook/core.py tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/playbook/renderers.toml tools/playbook/instructions-legacy.txt tools/playbook/README.md tools/roles/templates/work-order.template.md tools/roles/handoff.py tools/roles/README.md tools/agent-instructions/adopt-agent-instructions.sh tools/agent-instructions/kit.toml tools/agent-instructions/README.md tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/playbook.md memory/map/generated/MAP.md memory/map/generated/symbols.json tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json .governance/instructions.lock memory/project/spawn-idiom-sites.txt memory/project/unarmed-branches.txt memory/guides/SESSION-KICKOFF.md .memory-tree.conf

2026-11-04T13:41:17Z brief · item PLAY-dOrderedCharter-20 · reason 90cf3b2beda9 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-20-build-brief.md

2026-11-04T14:30:15Z brief · item PLAY-dOrderedCharter-20 · reason da3dde71e7f1 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-20-build-brief.md

2026-11-04T16:21:41Z dispatch · item 392089fc PLAY-dOrderedCharter-20 · reason tools/playbook/instruction_units.py tools/playbook/render_playbook.py tools/playbook/adopt-playbook.sh tools/playbook/core.py tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/playbook/renderers.toml tools/playbook/instructions-legacy.txt tools/playbook/README.md tools/roles/templates/work-order.template.md tools/roles/handoff.py tools/roles/README.md tools/agent-instructions/adopt-agent-instructions.sh tools/agent-instructions/kit.toml tools/agent-instructions/README.md tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/playbook.md memory/map/generated/MAP.md memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/map/generated/inventories.json tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json .governance/instructions.lock memory/project/spawn-idiom-sites.txt memory/project/unarmed-branches.txt memory/guides/SESSION-KICKOFF.md .memory-tree.conf .lexicon.conf memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-20-ledger.md memory/builds/dOrderedCharter/build/2026-11-04-build-PLAY-dOrderedCharter-20-deviation-204.md memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-20-build-brief.md

2026-11-04T16:28:27Z brief · item PLAY-dOrderedCharter-20 · reason 6dcb1926015d memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-20-build-brief.md

2026-11-04T16:31:13Z dispatch · item 392089fc PLAY-dOrderedCharter-20 · reason memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-04T18:34:08Z brief · item PLAY-dOrderedCharter-15 · reason e3e98b8a0427 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-15-build-brief.md

2026-11-04T18:47:43Z dispatch · item da0d8eae PLAY-dOrderedCharter-15 · reason tools/playbook/instructions_edit.py tools/playbook/packs.toml tools/playbook/instruction_units.py tools/playbook/render_playbook.py tools/playbook/gov_tag.py tools/playbook/README.md help/tags.md tools/playbook/edge_grammar.py tools/playbook/namespaces.toml tools/memory-tree/build_records.py tools/memory-tree/merge-rows.py .gitattributes tools/gate-legs.json memory/guides/SESSION-KICKOFF.md tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/playbook.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt .governance/policy.json memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-15-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-04T21:35:50Z dispatch · item d0c16d29 PLAY-dOrderedCharter-1 · reason tools/playbook/practices.toml tools/playbook/instruction_units.py tools/playbook/render_playbook.py tools/playbook/README.md tools/playbook/positional.py tools/playbook/core-pending.txt tools/check-playbook-parity.sh tools/check-playbook-parity.test.sh coding-governance-agents.template.md AGENTS.md .governance/instructions.lock .governance/policy.json help/charter.md help/README.md help/tags.md memory/project/docs-undocumented.txt tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt tools/memory-tree/row_grammar.py tools/memory-recall/selftest.py memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/features/playbook.md

2026-11-04T21:35:52Z brief · item PLAY-dOrderedCharter-1 · reason ac03830e252b memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-1-build-brief.md

2026-11-04T22:00:46Z dispatch · item d0c16d29 PLAY-dOrderedCharter-1 · reason tools/playbook/practices.toml tools/playbook/instruction_units.py tools/playbook/render_playbook.py tools/playbook/README.md tools/playbook/positional.py tools/playbook/core-pending.txt tools/check-playbook-parity.sh tools/check-playbook-parity.test.sh coding-governance-agents.template.md AGENTS.md .governance/instructions.lock .governance/policy.json help/charter.md help/README.md help/tags.md memory/project/docs-undocumented.txt tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt tools/memory-tree/row_grammar.py tools/memory-recall/selftest.py memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/features/playbook.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-1-ledger.md memory/builds/dOrderedCharter/build/2026-11-04-build-PLAY-dOrderedCharter-1-deviation-15.md memory/builds/dOrderedCharter/README.md memory/backlog/PLAY.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-04T22:46:33Z dispatch · item bdffc93d PLAY-dOrderedCharter-45 · reason tools/memory-tree/merge-rows.py tools/memory-tree/merge-rows.test.sh tools/playbook/instructions_edit.py tools/playbook/core.py tools/playbook/instruction_units.py tools/playbook/render_playbook.py memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-45.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-45-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md

2026-11-04T22:46:37Z brief · item PLAY-dOrderedCharter-45 · reason d978b1c5b01b memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-45-build-brief.md

2026-11-04T23:08:36Z dispatch · item bdffc93d PLAY-dOrderedCharter-45 · reason memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-04T23:25:46Z dispatch · item bdffc93d PLAY-dOrderedCharter-45 · reason memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-45-deviation-453.md

2026-11-04T23:50:45Z rescope · item defer PLAY-dOrderedCharter-11 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:47Z rescope · item defer PLAY-dOrderedCharter-14 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:48Z rescope · item defer PLAY-dOrderedCharter-2 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:50Z rescope · item defer PLAY-dOrderedCharter-21 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:52Z rescope · item defer PLAY-dOrderedCharter-23 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:54Z rescope · item defer PLAY-dOrderedCharter-27 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:56Z rescope · item defer PLAY-dOrderedCharter-29 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:58Z rescope · item defer PLAY-dOrderedCharter-3 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:50:59Z rescope · item defer PLAY-dOrderedCharter-30 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:01Z rescope · item defer PLAY-dOrderedCharter-31 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:03Z rescope · item defer PLAY-dOrderedCharter-32 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:05Z rescope · item defer PLAY-dOrderedCharter-33 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:07Z rescope · item defer PLAY-dOrderedCharter-34 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:08Z rescope · item defer PLAY-dOrderedCharter-35 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:10Z rescope · item defer PLAY-dOrderedCharter-36 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:12Z rescope · item defer PLAY-dOrderedCharter-37 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:14Z rescope · item defer PLAY-dOrderedCharter-4 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:16Z rescope · item defer PLAY-dOrderedCharter-5 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:17Z rescope · item defer PLAY-dOrderedCharter-6 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:20Z rescope · item defer PLAY-dOrderedCharter-8 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:21Z rescope · item defer PLAY-dOrderedCharter-39 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:23Z rescope · item defer PLAY-dOrderedCharter-40 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:25Z rescope · item defer PLAY-dOrderedCharter-41 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:27Z rescope · item defer PLAY-dOrderedCharter-43 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:29Z rescope · item defer PLAY-dOrderedCharter-46 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:30Z rescope · item defer PLAY-dOrderedCharter-49 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:32Z rescope · item defer PLAY-dOrderedCharter-52 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:34Z rescope · item defer PLAY-dOrderedCharter-54 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-04T23:51:36Z rescope · item defer PLAY-dOrderedCharter-55 · reason owner ordered the build paused after unit 45 and the branch landed; carried forward against ask PLAY-dOrderedCharter-38

2026-11-05T00:19:03Z review · item dOrderedCharter · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 3 · minors 20 · disposition promote

2026-11-05T00:19:05Z rescope · item add PLAY-dOrderedCharter-67 · reason promoted from the closing diff review: H1, the recall suites' guards miss the moved id grammar

2026-11-05T00:19:08Z rescope · item add PLAY-dOrderedCharter-68 · reason promoted from the closing diff review: H2, the tag scanners drop every line after an unclosed fence

2026-11-05T00:19:10Z rescope · item add PLAY-dOrderedCharter-69 · reason promoted from the closing diff review: H3, fixtures act on the real repository under an inherited GIT_DIR

2026-11-05T00:19:16Z rescope · item add PLAY-dOrderedCharter-70 · reason promoted from the closing diff review: the closing review's mediums and low, batched

2026-11-05T03:23:09Z dispatch · item 7ae097e4 PLAY-dOrderedCharter-67 · reason tools/gate-legs.json tools/run-gates/py_reads.py tools/run-gates/kit.toml tools/run-gates/run-gates.gov.test.sh tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/run-gates.md memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/gotchas/held-suite-guard-misses-a-sibling-kit.md memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-11-05-spec-PLAY-dOrderedCharter-67.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-67-ledger.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-67-deviation-671.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-05T03:23:19Z brief · item PLAY-dOrderedCharter-67 · reason 781325610c98 memory/builds/dOrderedCharter/prompts/2026-11-05-prompt-PLAY-dOrderedCharter-67-build-brief.md

2026-11-05T03:51:22Z dispatch · item 7ae097e4 PLAY-dOrderedCharter-67 · reason memory/gotchas/INDEX.md

2026-11-08T03:08:01Z brief · item PLAY-dOrderedCharter-68 · reason a0d36e5912f8 memory/builds/dOrderedCharter/prompts/2026-11-05-prompt-PLAY-dOrderedCharter-68-build-brief.md

2026-11-08T03:17:39Z dispatch · item dcfdbbe8 PLAY-dOrderedCharter-68 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh tools/playbook/README.md help/tags.md memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md tools/run-gates/py_reads.py memory/builds/dOrderedCharter/spec/2026-11-05-spec-PLAY-dOrderedCharter-68.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-68-ledger.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-68-deviation-681.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T03:55:38Z dispatch · item 7b3d7476 PLAY-dOrderedCharter-69 · reason tools/playbook/instruction_units.py tools/playbook/gov_tag.py tools/playbook/edge_grammar.py tools/playbook/adopt-playbook.sh tools/playbook/README.md memory/builds/dOrderedCharter/spec/2026-11-05-spec-PLAY-dOrderedCharter-69.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-69-ledger.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-69-deviation-691.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T03:55:58Z brief · item PLAY-dOrderedCharter-69 · reason 3b69ffb79469 memory/builds/dOrderedCharter/prompts/2026-11-05-prompt-PLAY-dOrderedCharter-69-build-brief.md

2026-11-08T04:31:53Z dispatch · item ec555288 PLAY-dOrderedCharter-70 · reason tools/playbook/instruction_units.py tools/playbook/render_playbook.py tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh tools/playbook/README.md tools/playbook/instructions_edit.py tools/playbook/kit.toml tools/playbook/check_layers.py tools/playbook/core.py tools/playbook/positional-refs.txt tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/check-unattended.test.sh tools/memory-tree/build_records.py tools/memory-tree/merge-rows.py tools/memory-tree/merge-rows.test.sh tools/memory-tree/gotchas.py tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/.memory-tree.conf.example tools/memory-tree/README.md tools/memory-tree/check-memory-hygiene.sh skills/session-kickoff/manifest-check.sh tools/check-wiring.sh tools/run-gates/owed_rows.py tools/run-gates/run-gates.test.sh tools/check-install-prefix.test.sh tools/govkit/govkit.py tools/govkit/selftest.py memory/gotchas/observed-by-claim-no-arm-discharges.md memory/gotchas/amendment-leaves-its-other-half-standing.md memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-11-05-spec-PLAY-dOrderedCharter-70.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-70-ledger.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-70-deviation-701.md memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-70-deviation-702.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T04:32:03Z brief · item PLAY-dOrderedCharter-70 · reason 681b42598d32 memory/builds/dOrderedCharter/prompts/2026-11-05-prompt-PLAY-dOrderedCharter-70-build-brief.md

2026-11-08T05:15:34Z rescope · item add PLAY-dOrderedCharter-71 · reason found at the close: govkit selfcheck's adopter-name ban scans project-owned sources, which ship no bytes, so it reds on gov's own positional list

2026-11-08T06:50:15Z dispatch · item b6a0090b PLAY-dOrderedCharter-71 · reason tools/govkit/govkit.py tools/govkit/adopters.toml tools/govkit/selftest.py tools/memory-tree/merge-rows.py tools/run-gates/owed_rows.py memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-71.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-71-ledger.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-71-deviation-711.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T06:50:23Z brief · item PLAY-dOrderedCharter-71 · reason f3518386ecde memory/builds/dOrderedCharter/prompts/2026-11-08-prompt-PLAY-dOrderedCharter-71-build-brief.md

2026-11-08T08:29:18Z rescope · item add PLAY-dOrderedCharter-72 · reason found at the close: gov's positional lists live under tools/ and red install-prefix, drift-audit, dead-path and method-carrier legs; move them under memory/project and fix the shipped-surface paths

2026-11-08T08:29:20Z rescope · item add PLAY-dOrderedCharter-73 · reason found at the close: encoding, shell-hygiene, remote-literal, acceptance-matrix and policy-census reds the build's own units left

2026-11-08T10:16:50Z dispatch · item 559237fe PLAY-dOrderedCharter-72 · reason memory/project/positional-refs.txt memory/project/positional-producers.txt tools/playbook/positional-refs.txt tools/playbook/positional-producers.txt tools/playbook/positional.py tools/playbook/gov_tag.py tools/playbook/render_playbook.py tools/govkit/selftest.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md .memory-tree.conf tools/playbook/kit.toml tools/playbook/README.md tools/playbook/aliases.toml help/tags.md tools/playbook/core.py tools/playbook/instruction_units.py tools/playbook/adopt-playbook.sh tools/playbook/namespaces.toml tools/playbook/tag_index.py tools/playbook/principles.toml tools/lexicon/lexicon.py tools/lexicon/selftest.py tools/run-gates/py_reads.py tools/memory-tree/gotchas.py memory/LIVE.md memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-72.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-72-ledger.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-72-deviation-721.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-72-deviation-722.md memory/builds/dOrderedCharter/README.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T10:16:57Z brief · item PLAY-dOrderedCharter-72 · reason 6ef87bf1f359 memory/builds/dOrderedCharter/prompts/2026-11-08-prompt-PLAY-dOrderedCharter-72-build-brief.md

2026-11-08T11:01:18Z dispatch · item be0e9945 PLAY-dOrderedCharter-73 · reason tools/lib/common_dir.py tools/memory-tree/build_records.py tools/memory-tree/id_grammar.py tools/playbook/core.py tools/playbook/positional.py tools/playbook/instruction_units.py tools/unattended/unattended.sh tools/memory-tree/merge-rows.test.sh skills/session-kickoff/manifest-check.test.sh tools/unattended/check-unattended.test.sh tools/playbook/adopt-playbook.sh tools/playbook/kit.toml tools/govkit/matrix.py tools/run-gates/owed_rows.py memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-73.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-73-ledger.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-73-deviation-731.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-73-deviation-732.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T11:06:27Z decision · item Does playbook-render require the memory-tree and policy kits, so its three plant legs and the acceptance matrix pass in a scratch install? · reason Options: (a) requires playbook, memory-tree and policy, and the matrix installs that closure, which unit 73's builder showed passes all three legs; (b) the legs resolve those kits lazily and the matrix states their failing install-day verdicts; (c) the matrix leaves the renderer's plant legs unstated. The policy kit is not in the default selection, so (a) refuses an adopter that takes the renderer without it: a new install requirement, the fork rule's second veto, the owner's. Interim: unit 73 builds without the matrix change, and the matrix leg stays red into the hand-off.

2026-11-08T11:43:50Z dispatch · item a55be3c6 PLAY-dOrderedCharter-73 · reason tools/lib/common_dir.py tools/memory-tree/build_records.py tools/memory-tree/id_grammar.py tools/playbook/core.py tools/playbook/positional.py tools/playbook/instruction_units.py tools/unattended/unattended.sh tools/memory-tree/merge-rows.test.sh skills/session-kickoff/manifest-check.test.sh tools/unattended/check-unattended.test.sh tools/playbook/adopt-playbook.sh tools/run-gates/owed_rows.py memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-73.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-73-ledger.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-73-deviation.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T11:43:58Z brief · item PLAY-dOrderedCharter-73 · reason 8ae2393b436a memory/builds/dOrderedCharter/prompts/2026-11-08-prompt-PLAY-dOrderedCharter-73-build-brief.md

2026-11-08T12:28:55Z rescope · item add PLAY-dOrderedCharter-74 · reason found by the second full bar: unit 73's DERIVED_UNIT_KEYS still trips the remote-literal ban, and the layer-dependencies leg's ceiling falls 4s short of its evidenced margin

2026-11-08T13:04:18Z dispatch · item 550ea807 PLAY-dOrderedCharter-74 · reason tools/playbook/instruction_units.py tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-74.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-74-ledger.md memory/builds/dOrderedCharter/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md memory/map/generated

2026-11-08T13:04:23Z brief · item PLAY-dOrderedCharter-74 · reason 926f565e3ae5 memory/builds/dOrderedCharter/prompts/2026-11-08-prompt-PLAY-dOrderedCharter-74-build-brief.md

2026-11-08T14:32:48Z dispatch · item eb1c90a1 PLAY-dOrderedCharter-41 · reason tools/playbook/render_playbook.py help/charter.md WIRE-INTO-PROJECT.md memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-41.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-41-ledger.md memory/map/generated/symbols.json

2026-11-08T14:32:59Z brief · item PLAY-dOrderedCharter-41 · reason f79c92e5c5bb memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-41-build-brief.md

2026-11-08T15:33:14Z dispatch · item f56f6a18 PLAY-dOrderedCharter-52 · reason tools/memory-tree/merge-rows.py tools/memory-tree/merge-rows.test.sh tools/playbook/instructions_edit.py memory/map/generated/symbols.json memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-52.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-52-ledger.md

2026-11-08T15:33:21Z brief · item PLAY-dOrderedCharter-52 · reason b962f7915252 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-52-build-brief.md

2026-11-08T16:17:16Z dispatch · item 05aeb20a PLAY-dOrderedCharter-3 · reason tools/lib/envelope.py tools/lib/resolve-python.test.sh tools/playbook/documents.toml tools/playbook/instruction_units.py tools/playbook/policy_value.py tools/playbook/tag_index.py tools/playbook/render_playbook.py tools/playbook/namespaces.toml tools/roles/roles_lib.py tools/roles/render_agents.py tools/gate-legs.json tools/template-size-limits.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/playbook.md memory/map/generated/MAP.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/CARDS.md coding-governance-agents.template.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/ANNOTATION-STYLE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/ASKS.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/SKILL.template.md tools/workflows/REVIEW-PROTOCOL.template.md tools/roles/SKILL.template.md tools/branch-reconcile/SKILL.template.md tools/drift-audit/SKILL.template.md tools/lexicon/SKILL.template.md tools/memory-recall/SKILL.template.md tools/runlog/SKILL.template.md skills/session-kickoff/SKILL.md skills/deploy-governance/SKILL.md memory/guides/MERGE-BAR.md memory/guides/SESSION-KICKOFF.md .claude/rules/product.md AGENTS.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/REVIEW-PROTOCOL.md .claude/skills/build/SKILL.md .claude/skills/cleanup/SKILL.md .claude/skills/drift-audit/SKILL.md .claude/skills/lexicon/SKILL.md .claude/skills/memory-recall/SKILL.md .claude/skills/runlog/SKILL.md .claude/skills/unattended/SKILL.md .governance/instructions.lock help/charter.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-3-ledger.md

2026-11-08T16:17:23Z brief · item PLAY-dOrderedCharter-3 · reason 5ac4af4e19e6 memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-3-build-brief.md

2026-11-08T16:43:34Z dispatch · item 69963fd9 PLAY-dOrderedCharter-3 · reason memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-3-deviation-34.md memory/LIVE.md memory/backlog/PLAY.md memory/builds/dOrderedCharter/README.md

2026-11-08T16:53:02Z dispatch · item 69963fd9 PLAY-dOrderedCharter-3 · reason tools/lib/envelope.py tools/lib/resolve-python.test.sh tools/playbook/documents.toml tools/playbook/instruction_units.py tools/playbook/policy_value.py tools/playbook/tag_index.py tools/playbook/render_playbook.py tools/playbook/namespaces.toml tools/roles/roles_lib.py tools/roles/render_agents.py tools/gate-legs.json tools/template-size-limits.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/playbook.md memory/map/generated/MAP.md memory/map/generated/symbols.json memory/map/generated/inventories.json memory/map/generated/CARDS.md coding-governance-agents.template.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/ANNOTATION-STYLE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/ASKS.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/SKILL.template.md tools/workflows/REVIEW-PROTOCOL.template.md tools/roles/SKILL.template.md tools/branch-reconcile/SKILL.template.md tools/drift-audit/SKILL.template.md tools/lexicon/SKILL.template.md tools/memory-recall/SKILL.template.md tools/runlog/SKILL.template.md skills/session-kickoff/SKILL.md skills/deploy-governance/SKILL.md memory/guides/MERGE-BAR.md memory/guides/SESSION-KICKOFF.md .claude/rules/product.md AGENTS.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-ASKS.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/REVIEW-PROTOCOL.md .claude/skills/build/SKILL.md .claude/skills/cleanup/SKILL.md .claude/skills/drift-audit/SKILL.md .claude/skills/lexicon/SKILL.md .claude/skills/memory-recall/SKILL.md .claude/skills/runlog/SKILL.md .claude/skills/unattended/SKILL.md .governance/instructions.lock help/charter.md memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-3-ledger.md memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-3-deviation-34.md memory/LIVE.md memory/backlog/PLAY.md memory/builds/dOrderedCharter/README.md

2026-11-08T17:03:40Z dispatch · item 69963fd9 PLAY-dOrderedCharter-3 · reason memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md
