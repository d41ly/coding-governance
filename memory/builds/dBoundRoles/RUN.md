# dBoundRoles - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
asks-at-landing: TOOL-dBoundRoles-27=DEFERRED TOOL-dBoundRoles-28=OPEN TOOL-dBoundRoles-29=DEFERRED TOOL-dBoundRoles-30=OPEN TOOL-dBoundRoles-31=OPEN TOOL-dBoundRoles-32=OPEN TOOL-dBoundRoles-33=DEFERRED TOOL-dBoundRoles-34=OPEN TOOL-dBoundRoles-35=OPEN TOOL-dBoundRoles-36=OPEN TOOL-dBoundRoles-70=OPEN TOOL-dBoundRoles-71=OPEN TOOL-dBoundRoles-72=OPEN TOOL-dBoundRoles-73=OPEN TOOL-dBoundRoles-74=OPEN TOOL-dBoundRoles-75=OPEN TOOL-dBoundRoles-76=OPEN TOOL-dBoundRoles-77=OPEN TOOL-dBoundRoles-78=OPEN TOOL-dBoundRoles-79=OPEN TOOL-dBoundRoles-80=OPEN
units-at-landing: TOOL-dBoundRoles-14 TOOL-dBoundRoles-2 TOOL-dBoundRoles-1 TOOL-dBoundRoles-21 TOOL-dBoundRoles-37 TOOL-dBoundRoles-22 TOOL-dBoundRoles-49 TOOL-dBoundRoles-16 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-6 TOOL-dBoundRoles-13 TOOL-dBoundRoles-3 TOOL-dBoundRoles-38 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-7 TOOL-dBoundRoles-5 TOOL-dBoundRoles-10 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-4 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-12 TOOL-dBoundRoles-41 TOOL-dBoundRoles-11 TOOL-dBoundRoles-47 TOOL-dBoundRoles-26 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-20 TOOL-dBoundRoles-59 TOOL-dBoundRoles-19 TOOL-dBoundRoles-61 TOOL-dBoundRoles-18 TOOL-dBoundRoles-25 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69
hold-run: 
hold-streak: 1 · at 5f1fd8b4
resume-owed: none · owner
held-at: 2026-11-23T09:32:15Z
hold-reason: 38 of 59 units are built and CLOSED; 21 are deferred because units 19 and 20 wait on five asks (TOOL-dBoundRoles-77 to -80, TOOL-dDeclaredLoop-120) for row-grammar gaps in the playbook and loop kits, and the rest consume from them; units 42 and up were added by the landed spec run, so carry-forward cannot carry them. The closing diff review and the merge bar have not run over this branch.
hold-until: owner
hold-code: owner-decision
held-from: RUNNING
parked-surfaced: yes
keepalive-reaped: yes
refreshed-at: 4b5054df2ea652d443ff5eda27ec2b0590b870d7 · handoff · 22 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 318e20c9165fdceb2afe66b47d42c5f884d559c1
phase: RUNNING
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dboundroles-62c3df
anchor-kind: default-branch
cli-version: 2.1.326
lease-utc: 2026-11-23T09:35:54Z
pid-image: claude.exe
host: compeeto
pid: 17632
session: b48c5b81-0c25-4457-90e8-da811a25e0e9
keepalive: 675b83bc
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
2026-11-22T10:53:41Z draw · re-dispatch · TOOL-dBoundRoles-21 · 21/122 · 20261122T105341Z-6a8112

2026-11-22T10:53:41Z dispatch · item 7a0e819c TOOL-dBoundRoles-21 · reason help/roles.md tools/hooks/README.md memory/map/generated/symbols.json memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-deviation-213.md
2026-11-22T10:57:39Z draw · re-dispatch · TOOL-dBoundRoles-21 · 22/122 · 20261122T105739Z-53591d

2026-11-22T10:57:39Z dispatch · item 7a0e819c TOOL-dBoundRoles-21 · reason tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/house/policy.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/loop/factories.py tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt help/reference/policy.md .governance/policy.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-1-acceptance-ledger.md help/roles.md tools/hooks/README.md memory/map/generated/symbols.json memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-deviation-213.md

2026-11-22T11:11:38Z brief · item TOOL-dBoundRoles-22 · reason 58d0b924451c memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-22-build-brief.md

2026-11-22T11:11:39Z brief · item TOOL-dBoundRoles-49 · reason 4389e4daa322 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-49-build-brief.md

2026-11-22T11:15:12Z dispatch · item 79dc80ed TOOL-dBoundRoles-22 · reason tools/roles/workflows.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/README.md tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-22-1-acceptance-ledger.md

2026-11-22T11:17:58Z dispatch · item 79dc80ed TOOL-dBoundRoles-49 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-49-1-acceptance-ledger.md
2026-11-22T11:21:04Z draw · re-dispatch · TOOL-dBoundRoles-22 · 23/122 · 20261122T112104Z-4082c5

2026-11-22T11:21:04Z dispatch · item 79dc80ed TOOL-dBoundRoles-22 · reason tools/roles/workflows.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/README.md tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-22-1-acceptance-ledger.md memory/map/generated/symbols.json
2026-11-22T11:23:41Z draw · re-dispatch · TOOL-dBoundRoles-49 · 24/122 · 20261122T112341Z-566977

2026-11-22T11:23:41Z dispatch · item 79dc80ed TOOL-dBoundRoles-49 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-49-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T11:55:55Z brief · item TOOL-dBoundRoles-16 · reason 411a1f3fc145 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-16-build-brief.md

2026-11-22T11:58:50Z dispatch · item df41811d TOOL-dBoundRoles-54 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-54-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T11:58:52Z brief · item TOOL-dBoundRoles-54 · reason 9ae349c5e53d memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-54-build-brief.md

2026-11-22T12:03:42Z dispatch · item df41811d TOOL-dBoundRoles-16 · reason tools/roles/workflows.toml tools/roles/instructions.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/README.md tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-1-acceptance-ledger.md memory/map/generated/symbols.json
2026-11-22T12:14:29Z draw · re-dispatch · TOOL-dBoundRoles-16 · 25/122 · 20261122T121429Z-d18673

2026-11-22T12:14:30Z dispatch · item 0fdc5070 TOOL-dBoundRoles-16 · reason tools/roles/workflows.toml tools/roles/instructions.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/README.md tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-1.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-2.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-3.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-4.md

2026-11-22T12:14:31Z brief · item TOOL-dBoundRoles-16 · reason b161b66195b0 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-16-build-brief.md
2026-11-22T12:24:38Z draw · re-dispatch · TOOL-dBoundRoles-16 · 26/122 · 20261122T122438Z-21a983

2026-11-22T12:24:38Z dispatch · item 6f93ab7f TOOL-dBoundRoles-16 · reason tools/roles/workflows.toml tools/roles/instructions.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/README.md tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-1.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-2.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-3.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-4.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-deviation-163.md

2026-11-22T12:24:39Z brief · item TOOL-dBoundRoles-16 · reason 1abfa7fe8415 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-16-build-brief.md
2026-11-22T12:27:59Z draw · re-dispatch · TOOL-dBoundRoles-54 · 27/122 · 20261122T122759Z-f11954

2026-11-22T12:27:59Z dispatch · item 6f93ab7f TOOL-dBoundRoles-54 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-54-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-54-deviation-543.md

2026-11-22T12:28:00Z brief · item TOOL-dBoundRoles-54 · reason 87b6311eac90 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-54-build-brief.md
2026-11-22T12:53:14Z draw · re-dispatch · TOOL-dBoundRoles-16 · 28/122 · 20261122T125314Z-9772be

2026-11-22T12:53:14Z dispatch · item 1a50cffc TOOL-dBoundRoles-16 · reason tools/roles/workflows.toml tools/roles/instructions.toml tools/roles/roles_lib.py tools/roles/check_roles.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/role-schema.toml tools/roles/agents tools/roles/README.md tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-1.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-2.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-3.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-change-4.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-deviation-163.md tools/loop/factories.py

2026-11-22T12:53:15Z brief · item TOOL-dBoundRoles-16 · reason b2437e4e8e1f memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-16-build-brief.md
2026-11-22T12:55:55Z draw · re-dispatch · TOOL-dBoundRoles-54 · 29/122 · 20261122T125555Z-2e58f7

2026-11-22T12:55:55Z dispatch · item 1a50cffc TOOL-dBoundRoles-54 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-54-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-54-deviation-543.md

2026-11-22T12:55:56Z brief · item TOOL-dBoundRoles-54 · reason b7e3e02fc778 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-54-build-brief.md

2026-11-22T13:13:50Z brief · item TOOL-dBoundRoles-55 · reason 2d321742d234 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-55-build-brief.md

2026-11-22T13:19:24Z dispatch · item 487680c3 TOOL-dBoundRoles-55 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-55-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T13:43:47Z brief · item TOOL-dBoundRoles-15 · reason b2cd3bae82cc memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-15-build-brief.md

2026-11-22T13:48:54Z dispatch · item 4b461640 TOOL-dBoundRoles-15 · reason tools/roles/roles_lib.py tools/roles/render_agents.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/role-schema.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/policy/caps.toml tools/playbook/load_sets.py tools/loop/factories.py tools/loop/README.md help/loop.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-15-1-acceptance-ledger.md memory/map/generated/symbols.json
2026-11-22T13:54:41Z draw · re-dispatch · TOOL-dBoundRoles-15 · 30/122 · 20261122T135441Z-c2807d

2026-11-22T13:54:41Z dispatch · item ae743baa TOOL-dBoundRoles-15 · reason tools/roles/roles_lib.py tools/roles/render_agents.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/role-schema.toml tools/roles/README.md tools/roles/adopt-roles.test.sh tools/policy/caps.toml tools/playbook/load_sets.py tools/loop/factories.py tools/loop/README.md help/loop.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-15-1-acceptance-ledger.md memory/map/generated/symbols.json tools/roles/agents

2026-11-22T14:26:46Z dispatch · item 01d1f325 TOOL-dBoundRoles-17 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.sh tools/roles/adopt-roles.test.sh tools/roles/README.md tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/playbook/edge_grammar.py memory/project/work-order-legacy.txt memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T14:26:47Z brief · item TOOL-dBoundRoles-17 · reason 65284362913d memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-17-build-brief.md
2026-11-22T14:41:23Z draw · re-dispatch · TOOL-dBoundRoles-17 · 31/122 · 20261122T144123Z-8ce011

2026-11-22T14:41:23Z dispatch · item 4f256807 TOOL-dBoundRoles-17 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.sh tools/roles/adopt-roles.test.sh tools/roles/README.md tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/playbook/edge_grammar.py memory/project/work-order-legacy.txt memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-1-acceptance-ledger.md memory/map/generated/symbols.json tools/roles/render_agents.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md

2026-11-22T14:41:32Z brief · item TOOL-dBoundRoles-17 · reason 436dc14d0ad2 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-17-build-brief.md
2026-11-22T15:09:17Z draw · re-dispatch · TOOL-dBoundRoles-17 · 32/122 · 20261122T150917Z-9e282a

2026-11-22T15:09:17Z dispatch · item 2675b020 TOOL-dBoundRoles-17 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.sh tools/roles/adopt-roles.test.sh tools/roles/README.md tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/playbook/edge_grammar.py memory/project/work-order-legacy.txt memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-1-acceptance-ledger.md memory/map/generated/symbols.json tools/roles/render_agents.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md help/roles.md tools/govkit/usage.toml memory/guides/SESSION-KICKOFF.md

2026-11-22T15:09:42Z brief · item TOOL-dBoundRoles-17 · reason 04334413dbe0 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-17-build-brief.md
2026-11-22T15:32:59Z draw · re-dispatch · TOOL-dBoundRoles-17 · 33/122 · 20261122T153259Z-b2b760

2026-11-22T15:32:59Z dispatch · item 50a73223 TOOL-dBoundRoles-17 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.sh tools/roles/adopt-roles.test.sh tools/roles/README.md tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/playbook/edge_grammar.py memory/project/work-order-legacy.txt memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-1-acceptance-ledger.md memory/map/generated/symbols.json tools/roles/render_agents.py tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md help/roles.md tools/govkit/usage.toml memory/guides/SESSION-KICKOFF.md tools/playbook/instruction_units.py

2026-11-22T15:33:00Z brief · item TOOL-dBoundRoles-17 · reason 8a7e17c16161 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-17-build-brief.md

2026-11-22T15:58:32Z dispatch · item fae72daf TOOL-dBoundRoles-6 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/README.md tools/policy/guarded-paths.txt tools/policy/guard.py tools/policy/check_policy.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T15:58:33Z brief · item TOOL-dBoundRoles-6 · reason 69adb8d1d1b4 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-6-build-brief.md
2026-11-22T16:10:54Z draw · re-dispatch · TOOL-dBoundRoles-6 · 34/122 · 20261122T161054Z-d17cd2

2026-11-22T16:10:54Z dispatch · item 626015e6 TOOL-dBoundRoles-6 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/README.md tools/policy/guarded-paths.txt tools/policy/guard.py tools/policy/check_policy.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-change-1.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-deviation-61.md help/policy.md help/roles.md help/red-fix-lane.md tools/policy/README.md

2026-11-22T16:10:55Z brief · item TOOL-dBoundRoles-6 · reason 46c050e6753a memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-6-build-brief.md
2026-11-22T16:40:50Z draw · re-dispatch · TOOL-dBoundRoles-6 · 35/122 · 20261122T164050Z-992556

2026-11-22T16:40:50Z dispatch · item 60047186 TOOL-dBoundRoles-6 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/render_agents.py tools/roles/README.md tools/policy/guarded-paths.txt tools/policy/guard.py tools/policy/check_policy.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-1-acceptance-ledger.md memory/map/generated/symbols.json memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-change-5.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-deviation-64.md help/policy.md help/roles.md help/red-fix-lane.md tools/policy/README.md

2026-11-22T16:40:51Z brief · item TOOL-dBoundRoles-6 · reason 8e22ba4b4d69 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-6-build-brief.md

2026-11-22T17:00:30Z dispatch · item f2320b2f TOOL-dBoundRoles-13 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/README.md tools/roles/SKILL.template.md tools/roles/adopt-roles.test.sh tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/workflows/unattended-unit.js tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/README.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/template-size-limits.txt help/roles.md help/agent-limit.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-13-deviation-132.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-13-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T17:00:31Z brief · item TOOL-dBoundRoles-13 · reason dc14589c1b2f memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-13-build-brief.md
2026-11-22T17:10:56Z draw · re-dispatch · TOOL-dBoundRoles-13 · 36/122 · 20261122T171056Z-6f14d2

2026-11-22T17:10:56Z dispatch · item c5f15de0 TOOL-dBoundRoles-13 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/README.md tools/roles/SKILL.template.md tools/roles/adopt-roles.test.sh tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/workflows/unattended-unit.js tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/README.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/template-size-limits.txt help/roles.md help/agent-limit.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-13-deviation-132.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-13-1-acceptance-ledger.md memory/map/generated/symbols.json tools/playbook/instruction_units.py

2026-11-22T17:10:57Z brief · item TOOL-dBoundRoles-13 · reason 9df8cedc1287 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-13-build-brief.md
2026-11-22T17:24:12Z draw · re-dispatch · TOOL-dBoundRoles-13 · 37/122 · 20261122T172412Z-fb52cd

2026-11-22T17:24:12Z dispatch · item 35b19ccc TOOL-dBoundRoles-13 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/README.md tools/roles/SKILL.template.md tools/roles/adopt-roles.test.sh tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/workflows/unattended-unit.js tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/README.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/template-size-limits.txt help/roles.md help/agent-limit.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-13-deviation-132.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-13-1-acceptance-ledger.md memory/map/generated/symbols.json tools/playbook/instruction_units.py memory/guides/UNATTENDED-VERBS.md

2026-11-22T17:24:13Z brief · item TOOL-dBoundRoles-13 · reason f574580414c4 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-13-build-brief.md

2026-11-22T17:59:02Z dispatch · item 50ed4bcd TOOL-dBoundRoles-3 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/README.md tools/roles/adopt-roles.test.sh tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/loop/loop_lib.py tools/loop/README.md help/loop.md help/roles.md tools/playbook/instruction_units.py tools/govkit/usage.toml memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-3-deviation-34.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-3-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T17:59:04Z brief · item TOOL-dBoundRoles-3 · reason ef3f811b05e9 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-3-build-brief.md

2026-11-22T18:39:52Z dispatch · item 47caad9c TOOL-dBoundRoles-38 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/adopt-roles.test.sh tools/roles/README.md tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/scratch-guard.js tools/hooks/README.md tools/playbook/edge_grammar.py help/roles.md tools/playbook/instruction_units.py tools/govkit/usage.toml memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-38-deviation-383.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-38-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T18:39:54Z brief · item TOOL-dBoundRoles-38 · reason 5ef15015921a memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-38-build-brief.md

2026-11-22T19:11:02Z dispatch · item 691d34c1 TOOL-dBoundRoles-45 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/adopt-roles.test.sh tools/roles/README.md help/roles.md tools/playbook/instruction_units.py tools/govkit/usage.toml memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-45-deviation-453.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-45-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T19:11:03Z brief · item TOOL-dBoundRoles-45 · reason 585765fddbda memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-45-build-brief.md

2026-11-22T19:13:41Z dispatch · item 691d34c1 TOOL-dBoundRoles-46 · reason tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md help/agent-limit.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-46-deviation-463.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-46-1-acceptance-ledger.md

2026-11-22T19:13:42Z brief · item TOOL-dBoundRoles-46 · reason b32c865d2f01 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-46-build-brief.md

2026-11-22T19:41:09Z dispatch · item 473b4d1f TOOL-dBoundRoles-8 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/agent-cap.js tools/hooks/README.md help/roles.md help/red-fix-lane.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-8-deviation-81.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-8-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T19:41:10Z brief · item TOOL-dBoundRoles-8 · reason c832d790d873 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-8-build-brief.md

2026-11-22T20:12:18Z dispatch · item 10151b2e TOOL-dBoundRoles-48 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/adopt-roles.test.sh tools/roles/README.md tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md help/roles.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-48-deviation-482.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-48-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T20:12:29Z brief · item TOOL-dBoundRoles-48 · reason c3e2de7e6c19 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-48-build-brief.md

2026-11-22T20:52:41Z dispatch · item cae79967 TOOL-dBoundRoles-9 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/README.md help/roles.md tools/roles/check_roles.py tools/roles/render_agents.py memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-9-deviation-92.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-9-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T20:52:42Z brief · item TOOL-dBoundRoles-9 · reason b77621eca3b5 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-9-build-brief.md

2026-11-22T21:26:38Z dispatch · item 1403e58f TOOL-dBoundRoles-7 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/README.md help/roles.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-7-deviation-73.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-7-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T21:26:39Z brief · item TOOL-dBoundRoles-7 · reason b86b8e3463ef memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-7-build-brief.md

2026-11-22T21:28:27Z brief · item TOOL-dBoundRoles-7 · reason cd3bece63516 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-7-build-brief.md

2026-11-22T22:02:54Z dispatch · item 490630dc TOOL-dBoundRoles-5 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/return-check.sh tools/roles/return-check.fragment.json tools/roles/README.md help/roles.md tools/roles/SKILL.template.md tools/check-wiring.sh .claude/settings.json tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/unattended-unit.js tools/workflows/README.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-5-deviation-53.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-5-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T22:03:15Z brief · item TOOL-dBoundRoles-5 · reason 54641fa742b7 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-build-brief.md
2026-11-22T22:38:54Z draw · re-dispatch · TOOL-dBoundRoles-5 · 38/122 · 20261122T223854Z-b38c35

2026-11-22T22:38:54Z dispatch · item 51870e68 TOOL-dBoundRoles-5 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/return-check.sh tools/roles/return-check.fragment.json tools/roles/README.md help/roles.md tools/roles/SKILL.template.md tools/check-wiring.sh .claude/settings.json tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js tools/workflows/unattended-unit.js tools/workflows/README.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/map/features/roles.md tools/roles/render_agents.py tools/workflows/unattended-build.test.sh tools/workflows/tier2-review.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-5-deviation-53.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-5-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T22:38:55Z brief · item TOOL-dBoundRoles-5 · reason ef0ca7176d49 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-5-build-brief.md

2026-11-22T23:28:01Z dispatch · item 02efd60d TOOL-dBoundRoles-10 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/scratch-guard.fragment.json tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/roles/handoff.py tools/roles/README.md help/roles.md .claude/settings.json memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-10-deviation-104.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-10-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-22T23:28:03Z brief · item TOOL-dBoundRoles-10 · reason 9a76f441bc5f memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-10-build-brief.md
2026-11-22T23:33:38Z draw · re-dispatch · TOOL-dBoundRoles-10 · 39/122 · 20261122T233338Z-6350c7

2026-11-22T23:33:38Z dispatch · item 989719be TOOL-dBoundRoles-10 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/hooks/scratch-guard.fragment.json tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/roles/handoff.py tools/roles/README.md help/roles.md .claude/settings.json memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-10-deviation-104.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-10-1-acceptance-ledger.md memory/map/generated/symbols.json tools/roles/render_agents.py

2026-11-23T00:14:25Z dispatch · item 5c65171e TOOL-dBoundRoles-39 · reason tools/roles/handoff.py tools/roles/render_agents.py tools/roles/README.md help/roles.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-39-deviation-392.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-39-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T00:14:26Z brief · item TOOL-dBoundRoles-39 · reason ef0acba4ff52 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-39-build-brief.md

2026-11-23T00:44:08Z dispatch · item bdce1d73 TOOL-dBoundRoles-40 · reason tools/govkit/selftest.py memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-40-deviation-402.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-40-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T00:44:09Z brief · item TOOL-dBoundRoles-40 · reason 4a61f58a29af memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-40-build-brief.md

2026-11-23T01:07:12Z dispatch · item 03f2eb69 TOOL-dBoundRoles-4 · reason tools/roles/handoff.py tools/roles/roles_lib.py tools/roles/agents/gov-prompt-writer.agent.md tools/roles/README.md tools/roles/SKILL.template.md tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh help/roles.md tools/roles/render_agents.py memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-4-deviation-43.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-4-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T01:07:12Z brief · item TOOL-dBoundRoles-4 · reason 0334d1b37a55 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-4-build-brief.md

2026-11-23T01:55:05Z dispatch · item f389b55d TOOL-dBoundRoles-23 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/render_agents.py tools/roles/adopt-roles.test.sh tools/roles/README.md help/roles.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-23-deviation-234.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-23-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T01:55:06Z brief · item TOOL-dBoundRoles-23 · reason 027794368dee memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-23-build-brief.md

2026-11-23T02:05:12Z brief · item TOOL-dBoundRoles-23 · reason 8c465b1ee679 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-23-build-brief.md

2026-11-23T02:46:04Z dispatch · item f30d8556 TOOL-dBoundRoles-24 · reason tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/adopt-roles.test.sh tools/roles/README.md help/roles.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-24-deviation-243.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-24-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T02:46:05Z brief · item TOOL-dBoundRoles-24 · reason 7d877e124e81 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-24-build-brief.md

2026-11-23T03:13:20Z dispatch · item b46e0131 TOOL-dBoundRoles-41 · reason tools/roles/handoff.py tools/roles/adopt-roles.test.sh tools/roles/README.md tools/roles/roles_lib.py help/roles.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-41-deviation-413.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-41-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T03:13:21Z brief · item TOOL-dBoundRoles-41 · reason 8ff5455c84fe memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-41-build-brief.md

2026-11-23T03:41:28Z dispatch · item 6b28ea17 TOOL-dBoundRoles-12 · reason tools/loop/placement.py tools/roles/handoff.py tools/roles/SKILL.template.md help/roles.md tools/roles/README.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-12-deviation-123.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-12-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T03:41:29Z brief · item TOOL-dBoundRoles-12 · reason 2e54e75630dd memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-12-build-brief.md

2026-11-23T04:12:28Z dispatch · item c34080d0 TOOL-dBoundRoles-11 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh tools/memory-tree/marker-contract.test.sh tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/.memory-tree.conf.example .memory-tree.conf tools/unattended/unattended.sh tools/unattended/lib-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/unattended.test.sh tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/adopt-roles.test.sh tools/roles/agents/gov-spec-writer.agent.md tools/roles/agents/gov-builder.agent.md help/roles.md memory/guides/SESSION-KICKOFF.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-11-deviation-113.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-11-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T04:12:30Z brief · item TOOL-dBoundRoles-11 · reason 64782219c8cd memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-11-build-brief.md

2026-11-23T04:30:48Z brief · item TOOL-dBoundRoles-11 · reason 548d6021cff4 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-11-build-brief.md

2026-11-23T05:25:29Z dispatch · item 1d6abb15 TOOL-dBoundRoles-47 · reason tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-47-deviation-472.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-47-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T05:25:30Z brief · item TOOL-dBoundRoles-47 · reason bd7e823ec7fa memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-47-build-brief.md

2026-11-23T05:48:27Z dispatch · item e0abe395 TOOL-dBoundRoles-26 · reason tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/loop/position.py help/roles.md help/unattended.md .memory-tree.conf memory/project/positional-refs.txt memory/project/docs-undocumented.txt memory/guides/SESSION-KICKOFF.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-26-deviation-262.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-26-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T05:48:28Z brief · item TOOL-dBoundRoles-26 · reason d9103861f99c memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-26-build-brief.md
2026-11-23T05:52:11Z draw · re-dispatch · TOOL-dBoundRoles-26 · 40/122 · 20261123T055211Z-de4a8c

2026-11-23T05:52:11Z dispatch · item e0abe395 TOOL-dBoundRoles-26 · reason tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/loop/position.py help/roles.md help/loop.md .memory-tree.conf memory/project/positional-refs.txt memory/project/docs-undocumented.txt memory/guides/SESSION-KICKOFF.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-26-deviation-262.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-26-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T05:52:20Z brief · item TOOL-dBoundRoles-26 · reason e29c7d679609 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-26-build-brief.md
2026-11-23T06:09:29Z draw · re-dispatch · TOOL-dBoundRoles-26 · 41/122 · 20261123T060929Z-e527fb

2026-11-23T06:09:29Z dispatch · item 4fb8c240 TOOL-dBoundRoles-26 · reason tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/loop/position.py help/roles.md help/loop.md .memory-tree.conf memory/project/positional-refs.txt memory/project/docs-undocumented.txt memory/guides/SESSION-KICKOFF.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-26-deviation-262.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-26-1-acceptance-ledger.md memory/map/generated/symbols.json tools/roles/agents/gov-prompt-writer.agent.md tools/roles/render_agents.py

2026-11-23T06:09:38Z brief · item TOOL-dBoundRoles-26 · reason fb36abb00f0a memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-26-build-brief.md
2026-11-23T06:35:29Z draw · re-dispatch · TOOL-dBoundRoles-26 · 42/122 · 20261123T063529Z-1f13e6

2026-11-23T06:35:29Z dispatch · item 4a7ae9c6 TOOL-dBoundRoles-26 · reason tools/roles/role-schema.toml tools/roles/roles_lib.py tools/roles/handoff.py tools/roles/check_roles.py tools/roles/adopt-roles.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/loop/position.py help/roles.md help/loop.md .memory-tree.conf memory/project/positional-refs.txt memory/project/docs-undocumented.txt memory/guides/SESSION-KICKOFF.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-26-deviation-262.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-26-1-acceptance-ledger.md memory/map/generated/symbols.json tools/roles/agents/gov-prompt-writer.agent.md tools/roles/render_agents.py tools/roles/README.md

2026-11-23T06:35:32Z brief · item TOOL-dBoundRoles-26 · reason 7193c63fe00b memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-26-build-brief.md

2026-11-23T06:59:55Z brief · item TOOL-dBoundRoles-26 · reason fa51a1fd1218 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-26-build-brief.md

2026-11-23T07:05:44Z dispatch · item 4aa3b203 TOOL-dBoundRoles-52 · reason tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-47.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-52-deviation-522.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-52-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T07:05:45Z brief · item TOOL-dBoundRoles-52 · reason 1d253038a504 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-52-build-brief.md

2026-11-23T07:22:11Z dispatch · item ca40c3f3 TOOL-dBoundRoles-53 · reason tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-53-deviation-533.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-53-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T07:22:11Z brief · item TOOL-dBoundRoles-53 · reason 814c897f9d18 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-53-build-brief.md

2026-11-23T07:42:42Z dispatch · item e00bf176 TOOL-dBoundRoles-59 · reason tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-53-1-acceptance-ledger.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-59-deviation-593.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-59-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T07:42:43Z brief · item TOOL-dBoundRoles-59 · reason 4d9d417b0aa8 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-59-build-brief.md

2026-11-23T08:04:03Z decision · item TOOL-dBoundRoles-20, -25 and -43 wait on asks TOOL-dBoundRoles-77 to -79 and TOOL-dDeclaredLoop-120 · reason options: build the four row-mechanism gaps in the playbook and loop kits here, or land them in their own builds first; unit 20 section 8 F8 picked the asks, and the build-level rules refuse a deferral

2026-11-23T08:10:21Z brief · item TOOL-dBoundRoles-61 · reason 8050751d70c7 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-61-build-brief.md

2026-11-23T08:11:30Z rescope · item defer TOOL-dBoundRoles-20 · reason its section 8 F8 waits on the four row-mechanism asks TOOL-dBoundRoles-77 to -79 and TOOL-dDeclaredLoop-120, each gap still open at HEAD

2026-11-23T08:11:31Z rescope · item defer TOOL-dBoundRoles-25 · reason its spec consumes from TOOL-dBoundRoles-20, which waits on asks TOOL-dBoundRoles-77 to -79 and TOOL-dDeclaredLoop-120

2026-11-23T08:11:32Z rescope · item defer TOOL-dBoundRoles-43 · reason its spec consumes from TOOL-dBoundRoles-20, which waits on asks TOOL-dBoundRoles-77 to -79 and TOOL-dDeclaredLoop-120

2026-11-23T08:14:43Z dispatch · item c918856c TOOL-dBoundRoles-61 · reason tools/roles/adopt-roles.test.sh memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-59-1-acceptance-ledger.md memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-61-deviation-613.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-61-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T08:33:33Z rescope · item defer TOOL-dBoundRoles-19 · reason its section 8 F4 waits on ask TOOL-dBoundRoles-80, the level-5 adopter-rule unit the grammar refuses at HEAD

2026-11-23T08:33:35Z rescope · item defer TOOL-dBoundRoles-42 · reason its spec consumes from TOOL-dBoundRoles-25, deferred behind TOOL-dBoundRoles-20's asks

2026-11-23T08:33:35Z rescope · item defer TOOL-dBoundRoles-44 · reason its spec consumes from TOOL-dBoundRoles-25 and -42, each deferred behind TOOL-dBoundRoles-20's asks

2026-11-23T08:33:37Z rescope · item defer TOOL-dBoundRoles-50 · reason its spec consumes from TOOL-dBoundRoles-25, -42 and -43, each deferred behind TOOL-dBoundRoles-20's asks

2026-11-23T08:33:38Z rescope · item defer TOOL-dBoundRoles-51 · reason its spec consumes from TOOL-dBoundRoles-42 and -44, each deferred behind TOOL-dBoundRoles-20's asks

2026-11-23T08:33:39Z rescope · item defer TOOL-dBoundRoles-56 · reason its spec consumes from TOOL-dBoundRoles-50, deferred behind TOOL-dBoundRoles-20's asks

2026-11-23T08:33:39Z rescope · item defer TOOL-dBoundRoles-57 · reason its spec consumes from TOOL-dBoundRoles-51, deferred behind TOOL-dBoundRoles-20's asks

2026-11-23T08:33:41Z rescope · item defer TOOL-dBoundRoles-58 · reason its spec consumes from TOOL-dBoundRoles-25, -43 and their deferred consumers, behind TOOL-dBoundRoles-20's asks

2026-11-23T08:33:42Z rescope · item defer TOOL-dBoundRoles-60 · reason its spec consumes from TOOL-dBoundRoles-19, deferred on ask TOOL-dBoundRoles-80, and from -56 to -58

2026-11-23T08:33:42Z rescope · item defer TOOL-dBoundRoles-62 · reason its spec consumes from TOOL-dBoundRoles-60, deferred behind TOOL-dBoundRoles-19's ask

2026-11-23T08:33:43Z rescope · item defer TOOL-dBoundRoles-63 · reason its spec consumes from TOOL-dBoundRoles-60 and -62, each deferred behind TOOL-dBoundRoles-19's ask

2026-11-23T08:33:44Z rescope · item defer TOOL-dBoundRoles-64 · reason its spec consumes from TOOL-dBoundRoles-19 and -43, deferred on asks TOOL-dBoundRoles-77 to -80

2026-11-23T08:33:45Z rescope · item defer TOOL-dBoundRoles-65 · reason its spec consumes from TOOL-dBoundRoles-63 and -64, each deferred behind the filed asks

2026-11-23T08:33:46Z rescope · item defer TOOL-dBoundRoles-66 · reason its spec consumes from TOOL-dBoundRoles-50, -60 and -62 to -64, each deferred behind the filed asks

2026-11-23T08:33:47Z rescope · item defer TOOL-dBoundRoles-67 · reason its spec consumes from TOOL-dBoundRoles-63 and -65, each deferred behind the filed asks

2026-11-23T08:33:48Z rescope · item defer TOOL-dBoundRoles-68 · reason its spec consumes from TOOL-dBoundRoles-63 and -65, each deferred behind the filed asks

2026-11-23T08:33:49Z rescope · item defer TOOL-dBoundRoles-69 · reason its spec consumes from TOOL-dBoundRoles-60 and -63 to -67, each deferred behind the filed asks

2026-11-23T08:38:33Z dispatch · item d329db71 TOOL-dBoundRoles-18 · reason tools/govkit/steps/reviewer_merge.py tools/govkit/upgrade_steps.py tools/govkit/selftest.py tools/roles/kit.toml help/roles.md memory/project/docs-undocumented.txt memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-18-deviation-183.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-18-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T08:38:35Z brief · item TOOL-dBoundRoles-18 · reason 09d70f672cba memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-18-build-brief.md

2026-11-23T09:27:50Z brief · item TOOL-dBoundRoles-18 · reason f9ad26d7d183 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-18-build-brief.md

2026-11-23T09:30:23Z decision · item TOOL-dBoundRoles-19 waits on ask TOOL-dBoundRoles-80, and units 42, 44, 50, 51, 56 to 58, 60 and 62 to 69 consume from the deferred units · reason options: land the five asks in the playbook and loop kits and resume this build run, or rule F4 and F8 to build those gaps here; units 37 and up were added by the landed spec run, so carry-forward cannot carry them and the close hands the build to the owner

2026-11-23T09:32:18Z handoff · item owner-decision · reason in the run worktree: bash tools/push-main.sh --prepare --slug dBoundRoles && bash tools/push-main.sh --land --slug dBoundRoles && bash tools/unattended/unattended.sh --settle dBoundRoles

2026-11-23T09:32:18Z hold · item owner-decision · reason until owner · reaped beb107e9 · resume none(owner)

2026-11-23T09:35:59Z resume · item dBoundRoles · reason held · keepalive 675b83bc · manual

2026-11-23T09:38:21Z rescope · item add TOOL-dBoundRoles-81 · reason the owner's ruling of 2026-11-23, Build gaps here: the gap its ask names is built in this run

2026-11-23T09:38:22Z rescope · item add TOOL-dBoundRoles-82 · reason the owner's ruling of 2026-11-23, Build gaps here: the gap its ask names is built in this run

2026-11-23T09:38:23Z rescope · item add TOOL-dBoundRoles-83 · reason the owner's ruling of 2026-11-23, Build gaps here: the gap its ask names is built in this run

2026-11-23T09:38:24Z rescope · item add TOOL-dBoundRoles-84 · reason the owner's ruling of 2026-11-23, Build gaps here: the gap its ask names is built in this run

2026-11-23T09:38:24Z rescope · item add TOOL-dBoundRoles-85 · reason the owner's ruling of 2026-11-23, Build gaps here: the gap its ask names is built in this run

2026-11-23T10:17:34Z dispatch · item eb955137 TOOL-dBoundRoles-82 · reason tools/playbook/overlay_rows.py tools/playbook/row_checks.py tools/playbook/fixtures/row_kind.py tools/playbook/render_playbook.py help/overlay-rows.md memory/project/docs-undocumented.txt memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-82-deviation-821.md memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-82-1-acceptance-ledger.md memory/map/generated/symbols.json

2026-11-23T10:17:40Z brief · item TOOL-dBoundRoles-82 · reason 53c7e0af68f3 memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-82-build-brief.md
