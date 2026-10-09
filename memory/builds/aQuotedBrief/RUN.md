# aQuotedBrief - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: b4dcc83c1363456da2c738a7b94506d398845682
phase: BUILDING
may: none
mode: slug
run-branch: refs/heads/branch/unattended-build-template-5f7d7d
anchor-kind: default-branch
cli-version: 2.1.293
lease-utc: 2026-10-09T01:05:07Z
pid-image: claude.exe
host: compeeto-agent
pid: 13112
session: 980e4a60-dcd8-4eb9-85ca-c22d52fa116a
keepalive: c660de97
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 6473ae38a517a3559f2b7daed67a9820c505bd4d
anchor-ref: refs/heads/main
base: 6473ae38a517a3559f2b7daed67a9820c505bd4d

## Parked

2026-10-09T01:25:26Z dispatch · item 759e04fd TOOL-aQuotedBrief-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md tools/unattended/.unattended.conf.example memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md .claude/skills/unattended/SKILL.md .unattended.conf memory/map/generated/symbols.json

2026-10-09T01:26:10Z brief · item TOOL-aQuotedBrief-1 · reason 69417c45acd3 memory/builds/aQuotedBrief/prompts/2026-10-09-prompt-TOOL-aQuotedBrief-1-1-build-brief.md

2026-10-09T02:18:55Z dispatch · item 759e04fd TOOL-aQuotedBrief-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md tools/unattended/.unattended.conf.example memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md .claude/skills/unattended/SKILL.md .unattended.conf memory/map/generated/symbols.json memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-1-2-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md

2026-10-09T02:49:46Z dispatch · item 759e04fd TOOL-aQuotedBrief-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md tools/unattended/.unattended.conf.example memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md .claude/skills/unattended/SKILL.md .unattended.conf memory/map/generated/symbols.json memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-1-2-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md memory/builds/aQuotedBrief/spec/2026-10-09-spec-TOOL-aQuotedBrief-1.md memory/builds/aQuotedBrief/README.md

2026-10-09T03:03:36Z dispatch · item 985e8b18 TOOL-aQuotedBrief-2 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md memory/map/generated/symbols.json memory/builds/aQuotedBrief/spec/2026-10-09-spec-TOOL-aQuotedBrief-2.md memory/builds/aQuotedBrief/README.md memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-2-4-acceptance-ledger.md

2026-10-09T03:04:22Z brief · item TOOL-aQuotedBrief-2 · reason dbd5f0cc3586 memory/builds/aQuotedBrief/prompts/2026-10-09-prompt-TOOL-aQuotedBrief-2-3-build-brief.md

2026-10-09T04:32:52Z dispatch · item 98d212d7 TOOL-aQuotedBrief-3 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-PROTOCOL.md memory/map/generated/symbols.json memory/builds/aQuotedBrief/spec/2026-10-09-spec-TOOL-aQuotedBrief-3.md memory/builds/aQuotedBrief/README.md memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-3-6-acceptance-ledger.md

2026-10-09T04:33:10Z brief · item TOOL-aQuotedBrief-3 · reason aa96088eb99a memory/builds/aQuotedBrief/prompts/2026-10-09-prompt-TOOL-aQuotedBrief-3-5-build-brief.md

2026-10-09T05:44:21Z dispatch · item 98d212d7 TOOL-aQuotedBrief-3 · reason memory/LIVE.md

2026-10-09T06:19:05Z review · item aQuotedBrief · reason verdict BLOCKED · blockers 1

2026-10-09T06:34:56Z dispatch · item cc627830 TOOL-aQuotedBrief-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/aQuotedBrief/reviews/2026-10-09-review-TOOL-aQuotedBrief-3-closing-diff-round1.md

2026-10-09T06:42:18Z review · item aQuotedBrief · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 2 · minors 11 · disposition promote

2026-10-09T06:42:34Z rescope · item add TOOL-aQuotedBrief-4 · reason Closing review round 1 H1 (with M1, ids 2 11 18): term 7 reads PROMPT_BRIEF_CUTOFF from the working copy at close and is silent when it is off; promoted at the CONVERGED exit

2026-10-09T06:42:40Z rescope · item add TOOL-aQuotedBrief-5 · reason Closing review round 1 H2 (id 7): preflight and term 7 test the prompt heading differently, so term 7 can certify a record it did not grade; promoted at the CONVERGED exit

2026-10-09T06:42:47Z rescope · item add TOOL-aQuotedBrief-6 · reason Closing review minors batched: round 1 M2 to M6 and L1 to L4, round 2 low 1; one unit, since every fix writes unattended.sh and its suite

2026-10-09T07:04:23Z dispatch · item a21c87fc TOOL-aQuotedBrief-4 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated/symbols.json memory/builds/aQuotedBrief/spec/2026-10-09-spec-TOOL-aQuotedBrief-4.md memory/builds/aQuotedBrief/README.md memory/LIVE.md memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-4-8-acceptance-ledger.md

2026-10-09T07:04:40Z brief · item TOOL-aQuotedBrief-4 · reason ecccd34476f8 memory/builds/aQuotedBrief/prompts/2026-10-09-prompt-TOOL-aQuotedBrief-4-7-build-brief.md

2026-10-09T08:23:17Z dispatch · item b74cf6c9 TOOL-aQuotedBrief-5 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated/symbols.json memory/builds/aQuotedBrief/spec/2026-10-09-spec-TOOL-aQuotedBrief-5.md memory/builds/aQuotedBrief/README.md memory/LIVE.md memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-5-10-acceptance-ledger.md

2026-10-09T08:23:40Z brief · item TOOL-aQuotedBrief-5 · reason 0af79b95d0fa memory/builds/aQuotedBrief/prompts/2026-10-09-prompt-TOOL-aQuotedBrief-5-9-build-brief.md

2026-10-09T09:05:30Z dispatch · item 99b20c20 TOOL-aQuotedBrief-6 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md .unattended.conf memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/aQuotedBrief/spec/2026-10-09-spec-TOOL-aQuotedBrief-6.md memory/builds/aQuotedBrief/README.md memory/LIVE.md memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-6-12-acceptance-ledger.md

2026-10-09T09:05:58Z brief · item TOOL-aQuotedBrief-6 · reason 3b92fbb49e73 memory/builds/aQuotedBrief/prompts/2026-10-09-prompt-TOOL-aQuotedBrief-6-11-build-brief.md

2026-10-09T10:52:38Z dispatch · item 26dc599c TOOL-aQuotedBrief-6 · reason tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md
