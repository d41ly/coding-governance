# dDeclaredLoop - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
hold-run: 
hold-streak: 2 · at 815abf73
resume-owed: none · owner
held-at: 2026-11-13T10:37:19Z
hold-reason: the owner withdrew the ruling to re-run the spec audit before any audit started; check 118 still refuses every dispatch, and the parked decision stands
hold-until: owner
hold-code: host-owner-action
held-from: BUILDING
refreshed-at: 2ba17e9d690eb26ef8796fc0eddf190daba3b43b · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 5f0d0633dc69263e1fb4fecf82021ca62e5692f6
phase: BUILDING
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-declared-loop-d56bf0
anchor-kind: default-branch
cli-version: 2.1.321
lease-utc: 2026-11-13T10:41:50Z
pid-image: claude.exe
host: compeeto-agent
pid: 25292
session: 7c85732c-fa0c-43e9-83f2-238d293195e0
keepalive: 45e677fb
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 2ba17e9d690eb26ef8796fc0eddf190daba3b43b
anchor-ref: refs/heads/main
base: 2ba17e9d690eb26ef8796fc0eddf190daba3b43b

## Parked

2026-11-13T04:55:18Z brief · item TOOL-dDeclaredLoop-18 · reason a382adfd781a memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-18-build-brief.md

2026-11-13T06:04:47Z decision · item the dispatch gate (check 118) refuses every unit of this build run until a spec-audit chain covers all 98 live specs, and the owner ended this build's audit chain at round 12: which stands? · reason options: (a) the owner rules the audit run again, and the run re-invokes the build harness with auditIds over the 98 specs (PINNED), a chain that ran twelve rounds here without a clean round; (b) the owner sets review.spec-audit.disposal off by-nature or removes spec-audit from the README, so the gate does not read the chain for this build run; (c) the owner rules how the twelve recorded rounds enter a chain-rounds record. Refused to choose: (a) reverses the owner's 2026-10-24 stop, (b) edits an owner-landed README key or a policy value to pass a gate, (c) hand-builds an append-only record; none is delegated

2026-11-13T06:07:18Z hold · item host-owner-action · reason until owner · reaped b9b65262 · resume none(owner)

2026-11-13T10:36:20Z resume · item dDeclaredLoop · reason held · keepalive 22094182 · manual

2026-11-13T10:37:23Z hold · item host-owner-action · reason until owner · reaped 22094182 · resume none(owner)

2026-11-13T10:42:03Z resume · item dDeclaredLoop · reason held · keepalive 45e677fb · manual

2026-11-13T11:31:45Z dispatch · item 0ca2f812 TOOL-dDeclaredLoop-18 · reason tools/playbook/namespaces.toml tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/policy_value.py tools/playbook/adopt-playbook.sh tools/playbook/README.md help/tags.md memory/map/features/policy.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-18-1-acceptance-ledger.md memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-18-deviation-184.md memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md memory/builds/dDeclaredLoop/README.md memory/LIVE.md memory/ledger/2026-11.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-13T13:11:59Z dispatch · item 75a5904c TOOL-dDeclaredLoop-18 · reason tools/playbook/namespaces.toml tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/policy_value.py tools/playbook/adopt-playbook.sh tools/playbook/README.md tools/playbook/kinds.toml tools/lexicon/lexicon.py help/tags.md memory/map/features/policy.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-18-1-acceptance-ledger.md memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md memory/builds/dDeclaredLoop/README.md memory/LIVE.md memory/ledger/2026-11.md

2026-11-13T13:53:59Z brief · item TOOL-dDeclaredLoop-1 · reason 824f207bd2ef memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-1-build-brief.md

2026-11-13T15:56:10Z dispatch · item 9667ba4c TOOL-dDeclaredLoop-1 · reason tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/adopt-loop.sh tools/loop/README.md tools/roles/workflows.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/adopt-roles.sh tools/roles/adopt-roles.test.sh tools/roles/kit.toml tools/roles/SKILL.template.md tools/roles/README.md .claude/skills/build/SKILL.md tools/playbook/render_playbook.py tools/playbook/load_sets.py tools/playbook/instruction_units.py tools/playbook/core-pending.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/govkit/usage.toml tools/gate-legs.json tools/playbook-kit-waivers.txt .gitattributes memory/map/features/loop.md memory/map/features/roles.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json help/loop.md help/README.md help/roles.md memory/guides/SESSION-KICKOFF.md memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-1-1-acceptance-ledger.md memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-1-deviation-14.md memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-1.md memory/builds/dDeclaredLoop/README.md memory/LIVE.md memory/ledger/2026-11.md memory/backlog/TOOL.md

2026-11-13T16:24:14Z dispatch · item 9667ba4c TOOL-dDeclaredLoop-1 · reason tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/adopt-loop.sh tools/loop/README.md tools/roles/workflows.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/adopt-roles.sh tools/roles/adopt-roles.test.sh tools/roles/kit.toml tools/roles/SKILL.template.md tools/roles/README.md .claude/skills/build/SKILL.md tools/playbook/render_playbook.py tools/playbook/load_sets.py tools/playbook/instruction_units.py tools/playbook/core-pending.txt tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/govkit/usage.toml tools/gate-legs.json tools/playbook-kit-waivers.txt .gitattributes memory/map/features/loop.md memory/map/features/roles.md memory/map/generated/CARDS.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json help/loop.md help/README.md help/roles.md memory/guides/SESSION-KICKOFF.md memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-1-1-acceptance-ledger.md memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-1-deviation-14.md memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-1.md memory/builds/dDeclaredLoop/README.md memory/LIVE.md memory/ledger/2026-11.md memory/backlog/TOOL.md tools/playbook/README.md tools/playbook/tag_index.py tools/govkit/upgrade_steps.py

2026-11-13T17:18:53Z brief · item TOOL-dDeclaredLoop-36 · reason 8225a5799df2 memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-36-build-brief.md

2026-11-13T18:19:43Z dispatch · item 094af7f7 TOOL-dDeclaredLoop-36 · reason tools/govkit/registry.toml help/loop.md help/upgrade-steps.md tools/playbook-kit-waivers.txt memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-36-1-acceptance-ledger.md memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-36.md memory/builds/dDeclaredLoop/README.md memory/LIVE.md memory/backlog/TOOL.md

2026-11-13T18:47:44Z dispatch · item 094af7f7 TOOL-dDeclaredLoop-36 · reason memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-36-deviation-363.md

2026-11-13T19:19:00Z brief · item TOOL-dDeclaredLoop-23 · reason 387f3459bf58 memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-23-build-brief.md
