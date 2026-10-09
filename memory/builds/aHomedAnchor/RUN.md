# aHomedAnchor - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes, 0 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 4e49aeb53a88568ff6c7989c8c38a9d4c324c80b
phase: VERIFYING
branch-sha: 11224126c2e48935ee3cc2e802bd3099c0f225fe
branch-ref: refs/heads/branch/unattended-kit-slug-mode-e3ba61
may: none
mode: prompt
run-branch: refs/heads/branch/unattended-kit-slug-mode-e3ba61
anchor-kind: run-branch
cli-version: 2.1.293
lease-utc: 2026-10-09T01:37:27Z
pid-image: claude.exe
host: compeeto-agent
pid: 27420
session: 8214b73e-f512-40f8-b204-27abe7b24f72
keepalive: 511a5962
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
