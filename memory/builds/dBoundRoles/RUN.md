# dBoundRoles - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: 8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e
phase: RUNNING
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dboundroles-62c3df
anchor-kind: default-branch
cli-version: 2.1.326
lease-utc: 2026-11-22T02:22:54Z
pid-image: claude.exe
host: compeeto
pid: 17632
session: b48c5b81-0c25-4457-90e8-da811a25e0e9
keepalive: beb107e9
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e
anchor-ref: refs/heads/main
base: 8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e

## Parked

2026-11-22T02:48:51Z dispatch · item 7e9a8e15 TOOL-dBoundRoles-14 · reason tools/playbook/namespaces.toml tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/README.md tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/agents tools/roles/README.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-14-1-acceptance-ledger.md

2026-11-22T02:49:13Z brief · item TOOL-dBoundRoles-14 · reason 2b353b27a191 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-build-brief.md

2026-11-22T03:08:52Z brief · item TOOL-dBoundRoles-14 · reason 485b8dc1ee96 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-build-brief.md
2026-11-22T03:11:52Z budget · frozen · 59 unit(s) · 122
2026-11-22T03:11:52Z draw · re-dispatch · TOOL-dBoundRoles-14 · 1/122 · 20261122T031152Z-fdc23c

2026-11-22T03:11:52Z dispatch · item 760bfa18 TOOL-dBoundRoles-14 · reason tools/playbook/adopt-playbook.sh tools/roles/adopt-roles.test.sh help/tags.md
2026-11-22T03:15:02Z draw · re-dispatch · TOOL-dBoundRoles-14 · 2/122 · 20261122T031502Z-cfb5e1

2026-11-22T03:15:02Z dispatch · item 760bfa18 TOOL-dBoundRoles-14 · reason tools/playbook/namespaces.toml tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh tools/playbook/README.md tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/adopt-roles.test.sh tools/roles/agents tools/roles/README.md help/tags.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-14-1-acceptance-ledger.md

2026-11-22T03:27:07Z brief · item TOOL-dBoundRoles-14 · reason c710a5e929a3 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-build-brief.md
2026-11-22T03:43:25Z draw · re-dispatch · TOOL-dBoundRoles-14 · 3/122 · 20261122T034325Z-6295d1

2026-11-22T03:43:25Z dispatch · item 1d58e026 TOOL-dBoundRoles-14 · reason memory/map/generated/symbols.json
2026-11-22T03:47:17Z draw · re-dispatch · TOOL-dBoundRoles-14 · 4/122 · 20261122T034717Z-3add06

2026-11-22T03:47:17Z dispatch · item 1d58e026 TOOL-dBoundRoles-14 · reason memory/LIVE.md memory/backlog/TOOL.md memory/builds/dBoundRoles/README.md
2026-11-22T03:52:07Z draw · re-dispatch · TOOL-dBoundRoles-14 · 5/122 · 20261122T035207Z-c831c7

2026-11-22T03:52:07Z dispatch · item 1d58e026 TOOL-dBoundRoles-14 · reason memory/map/generated/symbols.json memory/LIVE.md memory/backlog/TOOL.md memory/builds/dBoundRoles/README.md help/tags.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-14-1-acceptance-ledger.md memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md tools/playbook/README.md tools/playbook/adopt-playbook.sh tools/playbook/gov_tag.py tools/playbook/namespaces.toml tools/playbook/tag_index.py tools/roles/README.md tools/roles/adopt-roles.test.sh tools/roles/agents/gov-builder.agent.md tools/roles/agents/gov-diff-reviewer.agent.md tools/roles/agents/gov-orienter.agent.md tools/roles/agents/gov-researcher.agent.md tools/roles/agents/gov-reuse-scout.agent.md tools/roles/agents/gov-session.agent.md tools/roles/agents/gov-skeptic.agent.md tools/roles/agents/gov-spec-reviewer.agent.md tools/roles/agents/gov-spec-writer.agent.md tools/roles/agents/gov-synthesizer.agent.md tools/roles/agents/gov-tester.agent.md tools/roles/check_roles.py tools/roles/handoff.py tools/roles/roles_lib.py

2026-11-22T04:28:23Z brief · item TOOL-dBoundRoles-2 · reason 67e356b9dc5d memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-2-build-brief.md

2026-11-22T04:32:23Z dispatch · item eb1647ea TOOL-dBoundRoles-2 · reason tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/handoff.py tools/roles/agents tools/roles/README.md tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-2-1-acceptance-ledger.md

2026-11-22T05:01:10Z brief · item TOOL-dBoundRoles-2 · reason 04b0a96c99e4 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-2-build-brief.md
2026-11-22T05:04:04Z draw · re-dispatch · TOOL-dBoundRoles-2 · 6/122 · 20261122T050404Z-70358f

2026-11-22T05:04:04Z dispatch · item a01362eb TOOL-dBoundRoles-2 · reason tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/handoff.py tools/roles/agents tools/roles/README.md tools/roles/adopt-roles.test.sh tools/loop/factories.py tools/loop/loop_lib.py tools/loop/README.md tools/playbook/kinds.toml tools/govkit/usage.toml help/loop.md help/reference/kinds.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-2-1-acceptance-ledger.md
2026-11-22T05:44:39Z draw · re-dispatch · TOOL-dBoundRoles-2 · 7/122 · 20261122T054439Z-60c335

2026-11-22T05:44:39Z dispatch · item 85a3f6e4 TOOL-dBoundRoles-2 · reason .claude/agents memory/map/generated/symbols.json memory/LIVE.md memory/backlog/TOOL.md memory/builds/dBoundRoles/README.md memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md
2026-11-22T05:48:47Z draw · re-dispatch · TOOL-dBoundRoles-2 · 8/122 · 20261122T054847Z-9c42ce

2026-11-22T05:48:48Z dispatch · item 85a3f6e4 TOOL-dBoundRoles-2 · reason tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/handoff.py tools/roles/agents tools/roles/README.md tools/roles/adopt-roles.test.sh tools/loop/factories.py tools/loop/loop_lib.py tools/loop/README.md tools/playbook/kinds.toml tools/govkit/usage.toml help/loop.md help/reference/kinds.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-2-1-acceptance-ledger.md
2026-11-22T05:52:45Z draw · re-dispatch · TOOL-dBoundRoles-2 · 9/122 · 20261122T055245Z-08bab4

2026-11-22T05:52:45Z dispatch · item 85a3f6e4 TOOL-dBoundRoles-2 · reason help/roles.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-2-deviation-23.md
2026-11-22T05:56:45Z draw · re-dispatch · TOOL-dBoundRoles-2 · 10/122 · 20261122T055645Z-2d4969

2026-11-22T05:56:45Z dispatch · item 85a3f6e4 TOOL-dBoundRoles-2 · reason memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-22T06:14:47Z brief · item TOOL-dBoundRoles-1 · reason 2cf4ade16200 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-1-build-brief.md

2026-11-22T06:19:06Z dispatch · item 064bd108 TOOL-dBoundRoles-1 · reason tools/roles/agents tools/roles/house tools/roles/kit.toml tools/roles/role-schema.toml tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/workflows.toml tools/roles/README.md tools/playbook/layers.toml tools/playbook/check_layers.py tools/playbook/adopt-playbook.sh tools/playbook/kinds.toml tools/loop/loop_items.py tools/loop/loop.toml tools/loop/factories.py tools/workflows/kit.toml help/loop.md help/reference/drive.md AGENTS.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-1-acceptance-ledger.md

2026-11-22T06:59:46Z brief · item TOOL-dBoundRoles-1 · reason 8f1ec07ceac8 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-1-build-brief.md
2026-11-22T07:02:18Z draw · re-dispatch · TOOL-dBoundRoles-1 · 11/122 · 20261122T070218Z-92ebad

2026-11-22T07:02:18Z dispatch · item c3122581 TOOL-dBoundRoles-1 · reason tools/roles/agents tools/roles/house tools/roles/kit.toml tools/roles/role-schema.toml tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/workflows.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/playbook/layers.toml tools/playbook/check_layers.py tools/playbook/adopt-playbook.sh tools/playbook/kinds.toml tools/loop/loop_items.py tools/loop/loop.toml tools/loop/factories.py tools/workflows/kit.toml help/loop.md help/reference/drive.md AGENTS.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-1-acceptance-ledger.md

2026-11-22T07:41:17Z brief · item TOOL-dBoundRoles-1 · reason 966cd75406f6 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-1-build-brief.md
2026-11-22T07:43:58Z draw · re-dispatch · TOOL-dBoundRoles-1 · 12/122 · 20261122T074358Z-ebf411

2026-11-22T07:43:58Z dispatch · item b1323a67 TOOL-dBoundRoles-1 · reason tools/roles/agents tools/roles/house tools/roles/kit.toml tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/workflows.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/playbook/layers.toml tools/playbook/check_layers.py tools/playbook/adopt-playbook.sh tools/playbook/kinds.toml tools/loop/loop_items.py tools/loop/loop.toml tools/loop/factories.py tools/workflows/kit.toml help/loop.md help/reference/drive.md AGENTS.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-1-acceptance-ledger.md
2026-11-22T08:05:48Z draw · re-dispatch · TOOL-dBoundRoles-1 · 13/122 · 20261122T080548Z-87416d

2026-11-22T08:05:48Z dispatch · item 85a3e2b4 TOOL-dBoundRoles-1 · reason tools/roles/agents tools/roles/house tools/roles/kit.toml tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/workflows.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/playbook/layers.toml tools/playbook/check_layers.py tools/playbook/adopt-playbook.sh tools/playbook/kinds.toml tools/loop/loop_items.py tools/loop/loop.toml tools/loop/factories.py tools/workflows/kit.toml help/loop.md help/reference/drive.md AGENTS.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-1-acceptance-ledger.md help/reference/kinds.md .governance/instructions.lock tools/govkit/usage.toml memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-deviation-13.md
2026-11-22T08:14:19Z draw · re-dispatch · TOOL-dBoundRoles-1 · 14/122 · 20261122T081419Z-0a050f

2026-11-22T08:14:19Z dispatch · item 85a3e2b4 TOOL-dBoundRoles-1 · reason tools/roles/agents tools/roles/house tools/roles/kit.toml tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/workflows.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/playbook/layers.toml tools/playbook/check_layers.py tools/playbook/adopt-playbook.sh tools/playbook/kinds.toml tools/loop/loop_items.py tools/loop/loop.toml tools/loop/factories.py tools/workflows/kit.toml help/loop.md help/reference/drive.md AGENTS.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-1-acceptance-ledger.md help/reference/kinds.md .governance/instructions.lock tools/govkit/usage.toml memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-deviation-13.md memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md

2026-11-22T08:48:53Z decision · item TOOL-dBoundRoles-23 F6: should tools/policy/guard.py stop admitting a live run's own change to the policy file under policy-file.guard = owner-only, so a run's write can never pass as the owner's? · reason options: (a) read a run's change under owner-only as the owner's by the committed mandate - refused, it widens a security surface past the unit's tier (M3 veto 3); (c) a second guard in unit 23 - breaks its AC6; (d) change the guard inside unit 23 - against its section 3 non-goal; (e) keep F3's floor and state the gap as what the floor does not check, a hands-off edge leaving the guard change outside this build - taken, so the gap stays open until the owner rules whether the guard closes it

2026-11-22T09:06:52Z brief · item TOOL-dBoundRoles-21 · reason 0a7f0f3d393e memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-21-build-brief.md

2026-11-22T09:08:34Z brief · item TOOL-dBoundRoles-37 · reason 35518283e681 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-37-build-brief.md

2026-11-22T09:12:49Z dispatch · item 918c5bcf TOOL-dBoundRoles-21 · reason tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/house/policy.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt help/reference/policy.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-1-acceptance-ledger.md

2026-11-22T09:15:22Z dispatch · item 918c5bcf TOOL-dBoundRoles-37 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-37-1-acceptance-ledger.md
2026-11-22T09:27:30Z draw · re-dispatch · TOOL-dBoundRoles-37 · 15/122 · 20261122T092730Z-e5619d

2026-11-22T09:27:30Z dispatch · item 612d66b9 TOOL-dBoundRoles-37 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-37-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T09:27:47Z brief · item TOOL-dBoundRoles-37 · reason c24a3c30b562 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-37-build-brief.md
2026-11-22T09:34:09Z draw · re-dispatch · TOOL-dBoundRoles-37 · 16/122 · 20261122T093409Z-584954

2026-11-22T09:34:09Z dispatch · item b9ee28cf TOOL-dBoundRoles-37 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-37-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-37.md

2026-11-22T09:54:54Z brief · item TOOL-dBoundRoles-21 · reason db98f54cf574 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-21-build-brief.md
2026-11-22T09:58:24Z draw · re-dispatch · TOOL-dBoundRoles-21 · 17/122 · 20261122T095824Z-1f68a3

2026-11-22T09:58:24Z dispatch · item 8e0ea5e6 TOOL-dBoundRoles-21 · reason tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/house/policy.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt help/reference/policy.md .governance/policy.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-1-acceptance-ledger.md
2026-11-22T10:09:55Z draw · re-dispatch · TOOL-dBoundRoles-21 · 18/122 · 20261122T100955Z-9946d2

2026-11-22T10:09:55Z dispatch · item 07f2d4b1 TOOL-dBoundRoles-21 · reason memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-deviation-213.md memory/builds/dBoundRoles/README.md
2026-11-22T10:13:16Z draw · re-dispatch · TOOL-dBoundRoles-21 · 19/122 · 20261122T101316Z-a518bd

2026-11-22T10:13:16Z dispatch · item 07f2d4b1 TOOL-dBoundRoles-21 · reason tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/house/policy.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt help/reference/policy.md .governance/policy.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-1-acceptance-ledger.md

2026-11-22T10:28:35Z brief · item TOOL-dBoundRoles-21 · reason ef406c1d7674 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-21-build-brief.md
2026-11-22T10:32:09Z draw · re-dispatch · TOOL-dBoundRoles-21 · 20/122 · 20261122T103209Z-e00c62

2026-11-22T10:32:09Z dispatch · item f5673cdc TOOL-dBoundRoles-21 · reason tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/house/policy.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/loop/factories.py tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt help/reference/policy.md .governance/policy.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-1-acceptance-ledger.md
