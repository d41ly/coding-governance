# dUnstuckLanding - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes, 3 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 44af4ab1962bd811d880b189d97aeefc2f9fe6c2
phase: BUILDING
branch-sha: 0c16a66b53c9fd809ca198b612a23c62132edcc0
branch-ref: refs/heads/branch/unattended-build-closing-f90fd9
may: none
mode: prompt
run-branch: refs/heads/branch/unattended-build-closing-f90fd9
anchor-kind: run-branch
lease-utc: 2026-10-04T09:47:59Z
pid-image: claude.exe
host: compeeto
pid: 5164
session: 564117a5-ca8d-4f79-bbd3-b35058d54c66
keepalive: cf4f4ce8
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: a587e82dc6180a9a720560e1633995e47734803a
anchor-ref: refs/heads/main
base: 0c16a66b53c9fd809ca198b612a23c62132edcc0

## Parked

2026-10-04T08:58:35Z brief · item TOOL-dUnstuckLanding-1 · reason 35135466c91b memory/builds/dUnstuckLanding/prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-1-build-brief.md

2026-10-04T09:07:01Z brief · item TOOL-dUnstuckLanding-2 · reason d7d06997c9d4 memory/builds/dUnstuckLanding/prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-2-build-brief.md

2026-10-04T09:25:49Z review · item dUnstuckLanding · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · disposition promote

2026-10-04T09:25:55Z rescope · item add TOOL-dUnstuckLanding-12 · reason closing review round 1 CONVERGED with five HIGH items (H1-H5); the severity rule promotes them to one unit whose mechanism closes them: design rev-2 for the witness predicate, the aged-leg escalation home, the run-gates stamp predicate, the HELD-to-LANDED carriers, and ABSORB after the ask moves

2026-10-04T09:31:54Z brief · item TOOL-dUnstuckLanding-12 · reason 84306afa49d0 memory/builds/dUnstuckLanding/prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-12-build-brief.md

2026-10-04T09:37:46Z decision · item Ratify or decline the reversal in ask TOOL-dUnstuckLanding-6: kit default INHERITED_RED becomes land, and the age bound becomes an escalation instead of a stop (supersedes part of D12-i4, TOOL-dDerivedDocket-24) · reason Options: ratify it (permanent reds stop parking every later run), keep D12-i4 (the bound stays a stop), or ratify only for gov. Refused because it reverses an owner ruling and edits governance carriers (M3 veto 2); the evidence is design section 3

2026-10-04T09:37:47Z decision · item Ratify or decline the reversal in ask TOOL-dUnstuckLanding-8: build-complete meets on a carry-forward partial landing (DEFERRED units with open asks and no consumes-from edge), superseding D8 as it applies to build-complete · reason Options: ratify (cBriefedPilot-shaped builds land their closed units), keep D8 (partial builds still abort or override), or ratify only for dark-landed units. Refused because it reverses the owner's merge-only-when-fully-done rule and edits governance carriers (M3 veto 2); evidence is design section 5

2026-10-04T09:37:48Z decision · item Scaffold the implementation build(s) for asks TOOL-dUnstuckLanding-3 to -11, in the order design section Order gives (3 then 4 and 5, then 8; 6, 7 and 9 independent; 10 after 3; 11 last) · reason Options: one build carrying 3-10 and a separate deployer build for 11 (recommended, because 11 writes into foreign repos), one build per section, or a subset first (3, 4 and 5 fix the ABORTED-forever complaint alone). Refused because a run may not write the README that authorizes its own mandate (UNATTENDED-ASKS section 1); the owner lands it

2026-10-04T09:48:49Z rescope · item add TOOL-dUnstuckLanding-13 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-3

2026-10-04T09:48:50Z rescope · item add TOOL-dUnstuckLanding-14 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-4

2026-10-04T09:48:51Z rescope · item add TOOL-dUnstuckLanding-15 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-5

2026-10-04T09:48:52Z rescope · item add TOOL-dUnstuckLanding-16 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-6

2026-10-04T09:48:53Z rescope · item add TOOL-dUnstuckLanding-17 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-7

2026-10-04T09:48:55Z rescope · item add TOOL-dUnstuckLanding-18 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-8

2026-10-04T09:48:56Z rescope · item add TOOL-dUnstuckLanding-19 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-9

2026-10-04T09:48:57Z rescope · item add TOOL-dUnstuckLanding-20 · reason owner ruling TOOL-dUnstuckLanding-21: build ask TOOL-dUnstuckLanding-10

2026-10-04T10:20:23Z dispatch · item efe00377 TOOL-dUnstuckLanding-13 · reason tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.test.sh tools/unattended/check-unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-13.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-13-1-acceptance-ledger.md memory/builds/dUnstuckLanding/README.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-04T10:20:24Z brief · item TOOL-dUnstuckLanding-13 · reason cd089f69a73f memory/builds/dUnstuckLanding/prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md

2026-10-04T10:29:34Z dispatch · item efe00377 TOOL-dUnstuckLanding-13 · reason tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.test.sh tools/unattended/check-unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-13.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-13-1-acceptance-ledger.md memory/builds/dUnstuckLanding/README.md memory/LIVE.md memory/ledger/2026-10.md tools/drift-audit/drift_report.py tools/runlog/model.py tools/runlog/selftest.py

2026-10-04T10:49:19Z dispatch · item efe00377 TOOL-dUnstuckLanding-13 · reason tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.test.sh tools/unattended/check-unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-13.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-13-1-acceptance-ledger.md memory/builds/dUnstuckLanding/README.md memory/LIVE.md memory/ledger/2026-10.md tools/drift-audit/drift_report.py tools/runlog/model.py tools/runlog/selftest.py memory/backlog/TOOL.md

2026-10-04T10:52:27Z dispatch · item efe00377 TOOL-dUnstuckLanding-13 · reason tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.test.sh tools/unattended/check-unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-13.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-13-1-acceptance-ledger.md memory/builds/dUnstuckLanding/README.md memory/LIVE.md memory/ledger/2026-10.md tools/drift-audit/drift_report.py tools/runlog/model.py tools/runlog/selftest.py memory/backlog/TOOL.md memory/map/features/unattended.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/guides/SESSION-KICKOFF.md

2026-10-04T10:54:24Z dispatch · item efe00377 TOOL-dUnstuckLanding-13 · reason tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.test.sh tools/unattended/check-unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-13.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-13-1-acceptance-ledger.md memory/builds/dUnstuckLanding/README.md memory/LIVE.md memory/ledger/2026-10.md tools/drift-audit/drift_report.py tools/runlog/model.py tools/runlog/selftest.py memory/backlog/TOOL.md memory/map/features/unattended-stops.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/guides/SESSION-KICKOFF.md

2026-10-04T10:57:38Z dispatch · item 24b22949 TOOL-dUnstuckLanding-13 · reason memory/builds/dUnstuckLanding/README.md memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-13.md memory/guides/UNATTENDED-PROTOCOL.md tools/drift-audit/selftest.py tools/unattended/PROTOCOL.template.md

2026-10-04T11:00:34Z dispatch · item eb3144d5 TOOL-dUnstuckLanding-14 · reason tools/unattended/unattended.sh tools/unattended/lib-unattended.sh tools/unattended/check-unattended.sh tools/unattended/unattended.test.sh tools/unattended/check-unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-14.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-14-1-acceptance-ledger.md

2026-10-04T11:00:40Z brief · item TOOL-dUnstuckLanding-14 · reason cd089f69a73f memory/builds/dUnstuckLanding/prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md

2026-10-04T11:43:46Z dispatch · item eaf779cd TOOL-dUnstuckLanding-15 · reason tools/drift-audit/drift_report.py tools/drift-audit/selftest.py tools/drift-audit/drift_signals.py tools/drift-audit/drift_signals.template.py tools/drift-audit/README.md memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-15.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-15-1-acceptance-ledger.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/features/drift-audit.md memory/LIVE.md memory/ledger/2026-10.md

2026-10-04T11:43:47Z brief · item TOOL-dUnstuckLanding-15 · reason cd089f69a73f memory/builds/dUnstuckLanding/prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md

2026-10-04T12:01:54Z dispatch · item eaf779cd TOOL-dUnstuckLanding-15 · reason tools/drift-audit/drift_report.py tools/drift-audit/selftest.py tools/drift-audit/drift_signals.py tools/drift-audit/drift_signals.template.py tools/drift-audit/README.md memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-15.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-15-1-acceptance-ledger.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/features/drift-audit.md memory/LIVE.md memory/ledger/2026-10.md memory/backlog/TOOL.md memory/builds/dUnstuckLanding/README.md

2026-10-04T12:05:06Z brief · item TOOL-dUnstuckLanding-16 · reason cd089f69a73f memory/builds/dUnstuckLanding/prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md

2026-10-04T12:06:00Z dispatch · item d4a91213 TOOL-dUnstuckLanding-16 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md .githooks/pre-push .githooks/pre-push.test.sh .githooks/gate-env.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md tools/unattended/.unattended.conf.example memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-PROTOCOL.md .claude/skills/unattended/SKILL.md tools/memory-tree/gen_build_index.py memory/map/features/run-gates.md memory/builds/dUnstuckLanding/spec/2026-10-04-spec-TOOL-dUnstuckLanding-16.md memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-16-1-acceptance-ledger.md memory/builds/dUnstuckLanding/README.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json

2026-10-04T12:36:30Z dispatch · item d4a91213 TOOL-dUnstuckLanding-16 · reason memory/guides/SESSION-KICKOFF.md
