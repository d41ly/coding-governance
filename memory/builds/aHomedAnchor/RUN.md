# aHomedAnchor - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
landed-by: attended
landed-derived: 97b32e950340a7fc8792e0ea23fa2ba7513f4a2f 17e8ccb7e478c99116eed0801989141baa3e3e95
asks-at-landing: TOOL-aHomedAnchor-8=OPEN TOOL-aHomedAnchor-9=OPEN TOOL-aHomedAnchor-10=OPEN TOOL-aHomedAnchor-11=OPEN TOOL-aHomedAnchor-12=OPEN TOOL-aHomedAnchor-13=OPEN TOOL-aHomedAnchor-14=OPEN TOOL-aHomedAnchor-15=OPEN TOOL-aHomedAnchor-16=OPEN TOOL-aHomedAnchor-17=OPEN TOOL-aHomedAnchor-18=OPEN TOOL-aHomedAnchor-19=OPEN TOOL-aHomedAnchor-20=OPEN TOOL-aHomedAnchor-21=OPEN
units-at-landing: TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7
refreshed-at: 5a836bf0fc940029136b4b3fd57a87f35ff40f26 · handoff · 0 touching
hold-run: 
hold-streak: 1 · at 12930f49
resume-owed: none · owner
held-at: 2026-10-09T17:01:07Z
hold-reason: owner instruction 2026-10-09: skip the bar and land this; the owner lands it by hand
hold-until: owner
hold-code: owner-decision
held-from: VERIFYING
gates-run: unattended-179153003762917425227-2416772 75ee33ec
parked-surfaced: yes, 0 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 97b32e950340a7fc8792e0ea23fa2ba7513f4a2f
phase: LANDED
branch-sha: 11224126c2e48935ee3cc2e802bd3099c0f225fe
branch-ref: refs/heads/branch/unattended-kit-slug-mode-e3ba61
may: none
mode: prompt
run-branch: refs/heads/branch/unattended-kit-slug-mode-e3ba61
anchor-kind: run-branch
cli-version: 2.1.293
lease-utc: 2026-10-09T16:50:12Z
pid-image: claude.exe
host: compeeto-agent
pid: 27420
session: 8214b73e-f512-40f8-b204-27abe7b24f72
keepalive: 04e9f438
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 6473ae38a517a3559f2b7daed67a9820c505bd4d
anchor-ref: refs/heads/main
base: 11224126c2e48935ee3cc2e802bd3099c0f225fe

## Parked

2026-10-09T02:07:46Z dispatch · item dc8591f4 TOOL-aHomedAnchor-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/adopt-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/STOPS.template.md tools/unattended/README.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-1.md

2026-10-09T02:32:05Z dispatch · item dc8591f4 TOOL-aHomedAnchor-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/adopt-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md tools/unattended/STOPS.template.md tools/unattended/README.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md .claude/skills/unattended/SKILL.md .unattended.conf memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-1.md memory/guides/SESSION-KICKOFF.md

2026-10-09T02:53:06Z dispatch · item 337b5b64 TOOL-aHomedAnchor-1 · reason tools/unattended/unattended.test.sh

2026-10-09T02:58:36Z dispatch · item 026f5eec TOOL-aHomedAnchor-2 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-2.md

2026-10-09T03:31:05Z dispatch · item 026f5eec TOOL-aHomedAnchor-2 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-2.md memory/map/generated/symbols.json

2026-10-09T03:39:12Z dispatch · item 026f5eec TOOL-aHomedAnchor-2 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-2.md memory/map/generated/symbols.json memory/builds/aHomedAnchor/README.md memory/LIVE.md

2026-10-09T04:12:49Z review · item aHomedAnchor · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 3 · minors 27 · disposition promote

2026-10-09T04:14:42Z rescope · item add TOOL-aHomedAnchor-3 · reason closing review round 1 HIGH id 7: re-render the Skill, which still names published (memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md)

2026-10-09T04:15:03Z rescope · item add TOOL-aHomedAnchor-4 · reason closing review round 1 HIGH id 17: H1's left-shift, the adopter --check at commit time when the conf or a template is staged (memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md)

2026-10-09T04:15:27Z rescope · item add TOOL-aHomedAnchor-5 · reason closing review round 1 HIGH id 28: an adopter arm proving the render of local, with M9 (memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md)

2026-10-09T04:15:46Z rescope · item add TOOL-aHomedAnchor-6 · reason closing review round 1 minors batch, driver and docs write set: M1 M3 M4 M5 M6 M7 M8 M9 L1 L2 L5 L6 L7 L8 (memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md)

2026-10-09T04:16:09Z rescope · item add TOOL-aHomedAnchor-7 · reason closing review round 1 minors batch, leg write set: M2 M10 L3 L4 (memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md)

2026-10-09T04:28:05Z dispatch · item 71a299b2 TOOL-aHomedAnchor-3 · reason .claude/skills/unattended/SKILL.md memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-3.md memory/builds/aHomedAnchor/README.md memory/LIVE.md

2026-10-09T04:32:43Z dispatch · item 4c80fedd TOOL-aHomedAnchor-5 · reason tools/unattended/adopt-unattended.test.sh memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-5.md memory/builds/aHomedAnchor/README.md memory/LIVE.md

2026-10-09T04:35:22Z dispatch · item 87f19159 TOOL-aHomedAnchor-4 · reason .githooks/pre-commit .githooks/pre-commit.test.sh memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-4.md memory/builds/aHomedAnchor/README.md memory/LIVE.md

2026-10-09T04:39:08Z dispatch · item d3b545f6 TOOL-aHomedAnchor-6 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-6.md memory/builds/aHomedAnchor/README.md memory/LIVE.md

2026-10-09T04:45:27Z dispatch · item d3b545f6 TOOL-aHomedAnchor-6 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-6.md memory/builds/aHomedAnchor/README.md memory/LIVE.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md

2026-10-09T04:48:05Z dispatch · item 2d5f232c TOOL-aHomedAnchor-7 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-7.md memory/builds/aHomedAnchor/README.md memory/LIVE.md

2026-10-09T05:32:15Z dispatch · item d31d7bc9 TOOL-aHomedAnchor-7 · reason tools/unattended/check-unattended.test.sh

2026-10-09T09:08:43Z hold · item host-degraded · reason until probe host · reaped 511a5962 · resume unattended-resume-ahomedanchor

2026-10-09T16:36:57Z decision · item land without a bar on the reconciled HEAD? · reason options: run the bar first, or land over the close's 62/63-green bar whose one red leg was HOST-attributed; the owner chose to skip the bar and land (2026-10-09)

2026-10-09T16:52:10Z resume · item aHomedAnchor · reason held · keepalive 04e9f438 · manual

2026-10-09T17:01:52Z handoff · item owner-decision · reason in the run worktree: bash tools/push-main.sh --prepare --slug aHomedAnchor && bash tools/push-main.sh --land --slug aHomedAnchor && bash tools/unattended/unattended.sh --settle aHomedAnchor

2026-10-09T17:01:56Z hold · item owner-decision · reason until owner · reaped 04e9f438 · resume none(owner)
