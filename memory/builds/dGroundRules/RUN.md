# dGroundRules - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: 3c2b69be4652ade1ec267f0ce0e3d99389531633 · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 28554d7ff8812d622f07314636d363e44b9881f7
phase: BUILDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dgroundrules-e47ae1
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-23T19:14:57Z
pid-image: claude.exe
host: compeeto-agent
pid: 2556
session: 7ea4ff9e-7e37-4093-bc35-c581a17fe1c6
keepalive: 6e52b18d
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 3c2b69be4652ade1ec267f0ce0e3d99389531633
anchor-ref: refs/heads/main
base: 3c2b69be4652ade1ec267f0ce0e3d99389531633

## Parked

2026-10-23T19:39:07Z dispatch · item 35c1a533 TOOL-dGroundRules-1 · reason .governance/policy.toml tools/policy/kit.toml tools/policy/README.md tools/policy/catalogue.toml tools/policy/policy.py tools/policy/check_policy.py tools/policy/adopt-policy.sh tools/policy/unsummarised-keys.txt tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt tools/playbook-kit-waivers.txt .gitattributes help/policy.md help/README.md memory/map/features/policy.md memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-1-ledger.md

2026-10-23T19:39:13Z brief · item TOOL-dGroundRules-1 · reason cdc05f8541f6 memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-build-brief.md

2026-10-23T19:59:37Z dispatch · item 35c1a533 TOOL-dGroundRules-1 · reason memory/guides/SESSION-KICKOFF.md memory/backlog/TOOL.md memory/builds/dGroundRules/README.md

2026-10-23T20:12:23Z dispatch · item 81887798 TOOL-dGroundRules-11 · reason tools/policy/catalogue.toml tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/map/features/policy.md memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-11.md memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-11-ledger.md memory/builds/dGroundRules/README.md memory/backlog/TOOL.md

2026-10-23T20:12:28Z brief · item TOOL-dGroundRules-11 · reason f7c18feb27f2 memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-11-build-brief.md

2026-10-23T20:23:29Z dispatch · item 0c430c81 TOOL-dGroundRules-16 · reason tools/policy/check_policy.py tools/policy/README.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-16.md memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-16-ledger.md memory/builds/dGroundRules/README.md memory/backlog/TOOL.md

2026-10-23T20:23:34Z brief · item TOOL-dGroundRules-16 · reason b33cb6e219e8 memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-16-build-brief.md

2026-10-23T20:44:00Z decision · item Should a near-miss key under the budgets.* wildcard row (e.g. budgets.enforse) be refused rather than resolve to budgets.* and read its default once unit 3 lands? · reason Options: (a) unit 2 AC4 probes a key no row matches and the near-miss stays fail-open under budgets.* (taken for unit 2); (b) unit 9's caps census narrows budgets.* to the cap names it lists, so a near-miss refuses. Refused to decide (b) here: it amends unit 9's audited spec beyond the divergence, and unit 2 cannot depend on a later unit (M2 ordering); owner call whether unit 9 owes it.
