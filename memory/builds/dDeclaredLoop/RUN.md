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
