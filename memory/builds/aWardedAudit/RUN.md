# aWardedAudit - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 0268517dc10872821d63459b31a921c440f55d5d
phase: BUILDING
branch-sha: 856ad8a6856225bfe0d610d9a530b8fe852192b8
branch-ref: refs/heads/branch/unattended-spec-review-owner-b471cf
may: none
mode: prompt
run-branch: refs/heads/branch/unattended-spec-review-owner-b471cf
anchor-kind: run-branch
lease-utc: 2026-10-04T22:09:39Z
pid-image: claude.exe
host: compeeto-agent
pid: 13232
session: 28de3efb-24e3-49b3-87a3-ae6629fc41d7
keepalive: 88869531
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 35438ba0a188cf38c1d73b6e1df7b3a1342a17de
anchor-ref: refs/heads/main
base: 856ad8a6856225bfe0d610d9a530b8fe852192b8

## Parked

2026-10-04T22:10:59Z brief · item TOOL-aWardedAudit-1 · reason 9c69bc9dbf8b memory/builds/aWardedAudit/prompts/2026-10-05-prompt-TOOL-aWardedAudit-1-1-build-brief.md

2026-10-04T22:11:06Z dispatch · item 030cb510 TOOL-aWardedAudit-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/aWardedAudit/spec/2026-10-05-spec-TOOL-aWardedAudit-1.md

2026-10-04T22:16:18Z brief · item TOOL-aWardedAudit-2 · reason 80afbd99671e memory/builds/aWardedAudit/prompts/2026-10-05-prompt-TOOL-aWardedAudit-2-1-build-brief.md

2026-10-04T22:16:26Z dispatch · item 1872bdfe TOOL-aWardedAudit-2 · reason tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh memory/builds/aWardedAudit/spec/2026-10-05-spec-TOOL-aWardedAudit-2.md

2026-10-04T22:19:00Z brief · item TOOL-aWardedAudit-3 · reason 656c9c2cbddd memory/builds/aWardedAudit/prompts/2026-10-05-prompt-TOOL-aWardedAudit-3-1-build-brief.md

2026-10-04T22:21:13Z dispatch · item 0268517d TOOL-aWardedAudit-2 · reason tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh memory/builds/aWardedAudit/spec/2026-10-05-spec-TOOL-aWardedAudit-2.md

2026-10-04T22:24:10Z dispatch · item f28ff537 TOOL-aWardedAudit-3 · reason tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/.unattended.conf.example .unattended.conf tools/hooks/README.md memory/builds/aWardedAudit/spec/2026-10-05-spec-TOOL-aWardedAudit-3.md

2026-10-04T22:26:30Z dispatch · item 72900b7a TOOL-aWardedAudit-3 · reason tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/.unattended.conf.example .unattended.conf tools/hooks/README.md memory/builds/aWardedAudit/spec/2026-10-05-spec-TOOL-aWardedAudit-3.md memory/guides/SESSION-KICKOFF.md
