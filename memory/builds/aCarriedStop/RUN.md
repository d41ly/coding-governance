# aCarriedStop - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
hold-run: 
hold-streak: 1 · at 4bf57cb7
resume-owed: unattended-resume-acarriedstop · fire 2026-11-13T19:08:25Z
held-at: 2026-11-13T18:38:25Z
hold-reason: the close's bar is 94/95 green and its one red, routed commits name a specced unit, timed out CONTENDED at 760 s twice; alone at this tip it exits 0 in 957 s
hold-until: probe gate
hold-code: host-degraded
held-from: VERIFYING
gates-run: unattended-179464206554192622328-1124200 01787a62
parked-surfaced: yes
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 3d8689eaa
phase: VERIFYING
may: none
mode: prompt
run-branch: refs/heads/branch/sad-allen-74f7bd
anchor-kind: local
cli-version: 2.1.321
lease-utc: 2026-11-14T01:01:55Z
pid-image: claude.exe
host: compeeto-agent
pid: 29592
session: 729cb159-5621-445f-9b95-f98824ace689
keepalive: 1af57cf5
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 8db6f4bef58d5d88898d35ecf67e2297f6160cfa
anchor-ref: refs/heads/main
base: d646814e4a6a6747d3cdb471128be57a0e24e094

## Parked

2026-11-13T11:45:32Z brief · item TOOL-aCarriedStop-1 · reason 8cf3c8a5e30d memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-build-brief.md

2026-11-13T11:46:03Z brief · item TOOL-aCarriedStop-1 · reason b1335796cfc0 memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-build-brief.md

2026-11-13T11:47:24Z dispatch · item 0dd44963 TOOL-aCarriedStop-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-VERBS.md .claude/skills/unattended/SKILL.md help/spec-audit.md tools/template-size-limits.txt memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md memory/builds/aCarriedStop/build/2026-11-13-build-TOOL-aCarriedStop-1-1-acceptance-ledger.md memory/builds/aCarriedStop/README.md memory/LIVE.md memory/guides/SESSION-KICKOFF.md

2026-11-13T12:34:52Z review · item aCarriedStop · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 10 · disposition promote

2026-11-13T12:35:00Z rescope · item add TOOL-aCarriedStop-2 · reason promoted from the closing review's HIGH: the owner-stop path is held to one rule by the writer and the reader

2026-11-13T12:35:05Z rescope · item add TOOL-aCarriedStop-3 · reason promoted from the closing review: its six mediums and four lows, batched

2026-11-13T13:04:06Z brief · item TOOL-aCarriedStop-2 · reason d5d557e5e0f9 memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-2-build-brief.md

2026-11-13T13:05:21Z dispatch · item a484dc6c TOOL-aCarriedStop-2 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/spec-audit.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md memory/builds/aCarriedStop/build/2026-11-13-build-TOOL-aCarriedStop-2-1-acceptance-ledger.md memory/builds/aCarriedStop/README.md memory/LIVE.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json

2026-11-13T13:13:34Z dispatch · item a484dc6c TOOL-aCarriedStop-2 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/spec-audit.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md memory/builds/aCarriedStop/build/2026-11-13-build-TOOL-aCarriedStop-2-1-acceptance-ledger.md memory/builds/aCarriedStop/README.md memory/LIVE.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-2-1-builder.md memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-3-build-brief.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md

2026-11-13T13:17:27Z brief · item TOOL-aCarriedStop-3 · reason 6157aebb1bcc memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-3-build-brief.md

2026-11-13T13:18:41Z dispatch · item 8a248e2b TOOL-aCarriedStop-3 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md memory/builds/aCarriedStop/build/2026-11-13-build-TOOL-aCarriedStop-3-1-acceptance-ledger.md memory/builds/aCarriedStop/README.md memory/LIVE.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-3-1-builder.md

2026-11-13T18:38:32Z hold · item host-degraded · reason until probe gate · reaped 86f6a40a · resume unattended-resume-acarriedstop

2026-11-14T01:02:27Z resume · item aCarriedStop · reason held · keepalive 1af57cf5 · manual

2026-11-14T01:06:12Z rescope · item add TOOL-aCarriedStop-9 · reason owner ordered 2026-11-14: raise the routed-commits leg's ceiling and land; the close's bar timed it out at 760 s twice while it reads 957 s alone

2026-11-14T02:02:40Z brief · item TOOL-aCarriedStop-9 · reason 319fad7ee0b8 memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-9-build-brief.md

2026-11-14T02:04:10Z dispatch · item 4cb4b39f TOOL-aCarriedStop-9 · reason tools/run-gates/ceiling-evidence.txt tools/gate-legs.json memory/guides/SESSION-KICKOFF.md memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-9.md memory/builds/aCarriedStop/build/2026-11-14-build-TOOL-aCarriedStop-9-1-acceptance-ledger.md memory/builds/aCarriedStop/README.md memory/LIVE.md memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-9-2-builder.md memory/builds/aCarriedStop/build/2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md

2026-11-14T05:04:34Z rescope · item add TOOL-aCarriedStop-10 · reason adopted under M10 at the third close: install-prefix reads OWN on the inherited kit-path spellings in tools/chain-packet.py, and the push bar would refuse the same, so the owner's order to land needs them routed through resolve_kit_dir

2026-11-14T05:06:32Z brief · item TOOL-aCarriedStop-9 · reason d24e2a2dd8c9 memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-9-build-brief.md

2026-11-14T05:33:36Z brief · item TOOL-aCarriedStop-10 · reason d9234bdc2404 memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-build-brief.md

2026-11-14T05:34:54Z dispatch · item 97dbeb86 TOOL-aCarriedStop-10 · reason tools/chain-packet.py tools/chain-packet.test.sh memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-10.md memory/builds/aCarriedStop/build/2026-11-14-build-TOOL-aCarriedStop-10-1-acceptance-ledger.md memory/builds/aCarriedStop/README.md memory/LIVE.md memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-2-builder.md memory/builds/aCarriedStop/build/2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-9.md memory/guides/SESSION-KICKOFF.md memory/map/generated/symbols.json
