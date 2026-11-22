# dKeptSession - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: c2a407b0390f3d57a118b58e376c326aeb207c13 · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: a4dd146d6773f436a4527d2a9740a7beec69e405
phase: BUILDING
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dkeptsession-a0567a
anchor-kind: default-branch
cli-version: 2.1.326
lease-utc: 2026-11-21T12:17:07Z
pid-image: claude.exe
host: compeeto
pid: 29104
session: d5b6d4ab-72df-4e61-9a7c-05dde93b7f5b
keepalive: f586eb4e
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: c2a407b0390f3d57a118b58e376c326aeb207c13
anchor-ref: refs/heads/main
base: c2a407b0390f3d57a118b58e376c326aeb207c13

## Parked

2026-11-21T13:26:22Z brief · item KICK-dKeptSession-1 · reason b9a738e8e603 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md

2026-11-21T13:27:22Z dispatch · item a4dd146d KICK-dKeptSession-1 · reason tools/policy/presets.toml tools/policy/presets.py tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md tools/loop/guard.py tools/loop/loop.toml tools/loop/factories.py tools/loop/README.md tools/playbook/kinds.toml tools/playbook/core-pending.txt help/reference/kinds.md help/policy.md
2026-11-21T14:01:58Z budget · frozen · 64 unit(s) · 132
2026-11-21T14:01:58Z draw · re-dispatch · KICK-dKeptSession-1 · 1/132 · 20261121T140158Z-b911aa

2026-11-21T14:01:58Z dispatch · item a186ba16 KICK-dKeptSession-1 · reason tools/policy/presets.toml tools/policy/presets.py tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md tools/loop/guard.py tools/loop/loop.toml tools/loop/factories.py tools/loop/README.md tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/gate-legs.json help/reference/kinds.md help/policy.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-1-1-acceptance-ledger.md
2026-11-21T14:43:57Z draw · re-dispatch · KICK-dKeptSession-1 · 2/132 · 20261121T144357Z-a0ccc9

2026-11-21T14:43:57Z dispatch · item 516f40f9 KICK-dKeptSession-1 · reason tools/policy/presets.toml tools/policy/presets.py tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md tools/loop/guard.py tools/loop/loop.toml tools/loop/factories.py tools/loop/README.md tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/gate-legs.json help/reference/kinds.md help/policy.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-1-1-acceptance-ledger.md
2026-11-21T14:46:05Z draw · re-dispatch · KICK-dKeptSession-1 · 3/132 · 20261121T144605Z-f38af8

2026-11-21T14:46:05Z dispatch · item 1de08794 KICK-dKeptSession-1 · reason tools/policy/presets.toml tools/policy/presets.py tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md tools/loop/guard.py tools/loop/loop.toml tools/loop/factories.py tools/loop/README.md tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/gate-legs.json help/reference/kinds.md help/policy.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-1-1-acceptance-ledger.md tools/check-line-length.test.sh tools/hooks/agent-cap.test.sh tools/unattended/check-unattended.test.sh tools/unattended/unattended.test.sh

2026-11-21T15:34:23Z brief · item KICK-dKeptSession-1 · reason 0b2fea5d1b46 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-rebuild-brief.md
2026-11-21T15:35:49Z draw · re-dispatch · KICK-dKeptSession-1 · 4/132 · 20261121T153549Z-69cdb6

2026-11-21T15:35:49Z dispatch · item 897f5ab9 KICK-dKeptSession-1 · reason help/policy.md help/reference/kinds.md tools/gate-legs.json tools/govkit/usage.toml tools/loop/README.md tools/loop/factories.py tools/loop/guard.py tools/loop/loop.toml tools/playbook/core-pending.txt tools/playbook/kinds.toml tools/policy/README.md tools/policy/check_policy.py tools/policy/policy.py tools/policy/presets.py tools/policy/presets.toml memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-1-1-acceptance-ledger.md
2026-11-21T15:51:37Z draw · re-dispatch · KICK-dKeptSession-1 · 5/132 · 20261121T155137Z-3f9b70

2026-11-21T15:51:38Z dispatch · item d717c27d KICK-dKeptSession-1 · reason help/policy.md help/reference/kinds.md tools/gate-legs.json tools/govkit/usage.toml tools/loop/README.md tools/loop/factories.py tools/loop/guard.py tools/loop/loop.toml tools/playbook/core-pending.txt tools/playbook/kinds.toml tools/policy/README.md tools/policy/check_policy.py tools/policy/policy.py tools/policy/presets.py tools/policy/presets.toml memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-1-1-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json help/loop.md memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md

2026-11-21T15:53:13Z brief · item KICK-dKeptSession-1 · reason 23a780f91fa3 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-commit-brief.md

2026-11-21T16:11:15Z brief · item KICK-dKeptSession-19 · reason b9a738e8e603 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md

2026-11-21T16:12:42Z dispatch · item 4dbd3e52 KICK-dKeptSession-19 · reason tools/policy/policy.py tools/policy/unnamed-keys.txt tools/policy/check_policy.py tools/policy/kit.toml tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-19-1-acceptance-ledger.md
2026-11-21T16:31:27Z draw · re-dispatch · KICK-dKeptSession-19 · 6/132 · 20261121T163127Z-18e19c

2026-11-21T16:31:27Z dispatch · item af83c474 KICK-dKeptSession-19 · reason tools/policy/policy.py tools/policy/unnamed-keys.txt tools/policy/check_policy.py tools/policy/kit.toml tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-19-1-acceptance-ledger.md

2026-11-21T17:01:57Z brief · item KICK-dKeptSession-33 · reason b9a738e8e603 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md

2026-11-21T17:03:21Z dispatch · item db7f0041 KICK-dKeptSession-33 · reason tools/policy/presets.toml tools/policy/presets.py tools/policy/check_policy.py tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-33-1-acceptance-ledger.md

2026-11-21T17:17:17Z brief · item KICK-dKeptSession-2 · reason 7f0285b83e86 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-2-build-brief.md

2026-11-21T17:18:39Z dispatch · item bd980b21 KICK-dKeptSession-2 · reason tools/policy/policy.py tools/policy/presets.py tools/policy/check_policy.py tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-2-1-acceptance-ledger.md

2026-11-21T17:44:26Z brief · item KICK-dKeptSession-3 · reason 9cfd9ae78e94 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-3-build-brief.md

2026-11-21T17:45:50Z dispatch · item c1aa24bf KICK-dKeptSession-3 · reason tools/policy/policy.py tools/policy/check_policy.py tools/playbook/policy_value.py tools/playbook/render_playbook.py tools/playbook/instruction_units.py tools/govkit/entries/playbook.kit.toml tools/govkit/usage.toml .governance/instructions.lock memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json help/policy.md help/charter.md memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-3-1-acceptance-ledger.md
2026-11-21T17:51:12Z draw · re-dispatch · KICK-dKeptSession-3 · 7/132 · 20261121T175112Z-819c73

2026-11-21T17:51:12Z dispatch · item e793d2fb KICK-dKeptSession-3 · reason tools/policy/policy.py tools/policy/check_policy.py tools/playbook/policy_value.py tools/playbook/render_playbook.py tools/playbook/instruction_units.py tools/govkit/entries/playbook.kit.toml tools/govkit/usage.toml coding-governance-agents.template.md AGENTS.md .governance/instructions.lock memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json help/policy.md help/charter.md memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-3-1-acceptance-ledger.md

2026-11-21T18:13:13Z brief · item KICK-dKeptSession-34 · reason 3022f2c40e91 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-34-build-brief.md

2026-11-21T18:14:39Z dispatch · item 7b25e1b9 KICK-dKeptSession-34 · reason tools/policy/check_policy.py memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-34-1-acceptance-ledger.md

2026-11-21T18:27:05Z brief · item KICK-dKeptSession-40 · reason d67bf8d161c1 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-40-build-brief.md

2026-11-21T18:30:03Z dispatch · item ec95533c KICK-dKeptSession-40 · reason tools/policy/policy.py tools/policy/check_policy.py tools/policy/presets.py tools/policy/presets.toml tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-40-1-acceptance-ledger.md

2026-11-21T18:44:16Z brief · item KICK-dKeptSession-4 · reason aab981689f69 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-4-build-brief.md

2026-11-21T18:45:45Z dispatch · item eabd0d44 KICK-dKeptSession-4 · reason tools/policy/kit.toml tools/policy/adopt-policy.sh tools/policy/adopt-policy.test.sh tools/policy/policy.py tools/policy/check_policy.py memory/map/generated/symbols.json tools/policy/README.md tools/govkit/selftest.py tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/matrix.py tools/govkit/usage.toml help/policy.md help/tutorial/adopt-gov.md help/tasks/change-a-gov-rule.md memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-4-1-acceptance-ledger.md

2026-11-21T19:12:36Z brief · item KICK-dKeptSession-49 · reason 1dcea1645043 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-49-build-brief.md

2026-11-21T19:14:38Z dispatch · item cd808f85 KICK-dKeptSession-49 · reason tools/policy/policy-mirror.js tools/policy/check_policy.py memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-49-1-acceptance-ledger.md
2026-11-21T19:35:00Z draw · re-dispatch · KICK-dKeptSession-49 · 8/132 · 20261121T193500Z-91a52c

2026-11-21T19:35:00Z dispatch · item b34582fb KICK-dKeptSession-49 · reason tools/policy/policy-mirror.js tools/policy/check_policy.py tools/policy/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-49-1-acceptance-ledger.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md

2026-11-21T19:45:19Z brief · item KICK-dKeptSession-50 · reason 949a38b4aadf memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-50-build-brief.md

2026-11-21T19:46:41Z dispatch · item a21b9965 KICK-dKeptSession-50 · reason tools/policy/check_policy.py tools/policy/README.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-50-1-acceptance-ledger.md

2026-11-21T19:54:14Z brief · item KICK-dKeptSession-54 · reason ce8c622ea915 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-54-build-brief.md
2026-11-21T20:05:09Z draw · re-dispatch · KICK-dKeptSession-50 · 9/132 · 20261121T200509Z-25ac70

2026-11-21T20:05:09Z dispatch · item 1c090563 KICK-dKeptSession-50 · reason tools/policy/check_policy.py tools/policy/README.md memory/map/generated/symbols.json memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-50-1-acceptance-ledger.md memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md

2026-11-21T20:42:19Z dispatch · item 055582fb KICK-dKeptSession-54 · reason memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-54-1-acceptance-ledger.md

2026-11-21T21:09:55Z brief · item KICK-dKeptSession-20 · reason 1de718b05c8b memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-20-build-brief.md

2026-11-21T21:11:20Z dispatch · item 04abaa3a KICK-dKeptSession-20 · reason tools/loop/scenario-schema.toml tools/loop/scenario.py tools/loop/README.md tools/policy/presets.py tools/policy/policy.py tools/policy/README.md tools/govkit/usage.toml help/policy.md help/loop.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-20-1-acceptance-ledger.md

2026-11-21T21:54:44Z brief · item KICK-dKeptSession-32 · reason ff45f44eaa2d memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-32-build-brief.md

2026-11-21T21:56:09Z dispatch · item 38533a59 KICK-dKeptSession-32 · reason tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md memory/map/generated/symbols.json memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-32-1-acceptance-ledger.md memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md

2026-11-21T22:21:09Z decision · item loop transition record's 120 s ceiling (PINNED, tools/gate-legs.json): raise it, or split the leg, before order step 25 · reason By the plant estimates in specs 7, 35, 11, 52, 53 and 61, the leg reaches its 120 s ceiling at order step 25 (units 35 and 42) and about 219 s by unit 61 (PINNED estimate, KICK-dKeptSession-61). Options: (a) the owner raises the ceiling, (b) the leg is split into two legs. A declared ceiling is the owner's to move (BUILD-METHOD) and gate-legs.json names no row a run may raise, so the run cannot do either. Each of those specs now stops its unit before landing if the measured time reaches the ceiling, and never edits gate-legs.json.

2026-11-21T22:26:45Z brief · item KICK-dKeptSession-58 · reason a01f1514197c memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-58-build-brief.md

2026-11-21T22:28:10Z dispatch · item c34de6d4 KICK-dKeptSession-58 · reason memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-58-1-acceptance-ledger.md

2026-11-21T22:38:16Z brief · item KICK-dKeptSession-59 · reason d107e4d1d87a memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-59-build-brief.md

2026-11-21T22:39:37Z dispatch · item ca226f9f KICK-dKeptSession-59 · reason tools/policy/check_policy.py memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-59-1-acceptance-ledger.md

2026-11-21T22:51:01Z brief · item KICK-dKeptSession-60 · reason 1095181b0d72 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-60-build-brief.md

2026-11-21T22:52:26Z dispatch · item 5198e204 KICK-dKeptSession-60 · reason tools/policy/README.md tools/policy/policy.py memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-60-1-acceptance-ledger.md

2026-11-21T23:07:19Z brief · item KICK-dKeptSession-16 · reason 0243d2e02294 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-16-build-brief.md

2026-11-21T23:08:49Z dispatch · item ca43769b KICK-dKeptSession-16 · reason tools/policy/catalogue.toml tools/policy/policy.py tools/policy/check_policy.py tools/policy/unpurposed-namespaces.txt tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-16-1-acceptance-ledger.md

2026-11-21T23:51:02Z rescope · item add KICK-dKeptSession-67 · reason pass-tree.sh's regen runs mirror --write over the uncommitted merge, and cmd_mirror refuses while a mirror input differs from HEAD, so no pass changing tools/policy/catalogue.toml or presets.toml can merge: KICK-dKeptSession-16's green pass is refused, and 14 open specs touch those inputs. A blocker between the run and its landing is a discovery (protocol section 11), adopted as this unit.

2026-11-21T23:51:02Z rescope · item defer KICK-dKeptSession-16 · reason its green pass (8426252e0 plus its mirror commit 4ee5af863) cannot merge until KICK-dKeptSession-67 lets pass-tree.sh merge a pass that changes a mirror input; re-dispatched after 67 lands

2026-11-22T00:20:03Z brief · item KICK-dKeptSession-67 · reason 1f477ee42e08 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-67-build-brief.md

2026-11-22T00:25:45Z dispatch · item 7d4c4653 KICK-dKeptSession-67 · reason tools/unattended/pass-tree.sh tools/unattended/pass-tree.test.sh tools/unattended/README.md memory/builds/dKeptSession/README.md memory/LIVE.md memory/backlog/KICK.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-67-1-acceptance-ledger.md
2026-11-22T00:41:20Z draw · re-dispatch · KICK-dKeptSession-16 · 10/132 · 20261122T004120Z-2e40a1

2026-11-22T00:41:20Z dispatch · item 53d80cea KICK-dKeptSession-16 · reason tools/policy/catalogue.toml tools/policy/policy.py tools/policy/check_policy.py tools/policy/unpurposed-namespaces.txt tools/policy/README.md help/policy.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-16-1-acceptance-ledger.md

2026-11-22T00:50:17Z brief · item KICK-dKeptSession-12 · reason 3353573b62e4 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-12-build-brief.md

2026-11-22T00:51:48Z dispatch · item 0c57f16e KICK-dKeptSession-12 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md help/orientation-card.md memory/map/generated/symbols.json memory/LIVE.md memory/backlog/KICK.md memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-12-1-acceptance-ledger.md

2026-11-22T01:19:10Z brief · item KICK-dKeptSession-13 · reason 051873635d64 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-13-build-brief.md

2026-11-22T01:23:36Z dispatch · item 5caf0cd7 KICK-dKeptSession-13 · reason tools/loop/position.py tools/run-gates/selftest-budgets.txt skills/session-kickoff/manifest-check.sh memory/guides/SESSION-KICKOFF.md skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh tools/memory-tree/gen_build_index.py tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/policy/catalogue.toml tools/policy/unsummarised-keys.txt help/reference/policy.md memory/project/docs-undocumented.txt help/orientation-card.md memory/map/generated/symbols.json memory/builds/dKeptSession/README.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-13-1-acceptance-ledger.md
