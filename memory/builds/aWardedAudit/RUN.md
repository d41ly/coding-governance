# aWardedAudit - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
units-at-landing: TOOL-aWardedAudit-1 TOOL-aWardedAudit-2 TOOL-aWardedAudit-3 TOOL-aWardedAudit-5 TOOL-aWardedAudit-6
gates-run: unattended-17911836365807409466-1068676 b9f0cf7f
parked-surfaced: yes, 2 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 0ee7ce9d8c809c71535aae773e96a4202fe7abdb
phase: LANDING
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

2026-10-04T22:42:18Z review · item aWardedAudit · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 17 · disposition promote

2026-10-04T22:42:27Z rescope · item add TOOL-aWardedAudit-5 · reason closing review round 1 H1: a run can land a spec-audit: key or a SPEC_AUDIT_DEFAULT on main itself; no bar leg refuses the write, as check 19 does for may:

2026-10-04T22:42:30Z rescope · item add TOOL-aWardedAudit-6 · reason closing review round 1: the 4 medium and 7 low items (17 raw confirmed), batched

2026-10-04T22:45:55Z decision · item A prompt-mode run can no longer be opted into the spec audit by the owner's own prompt wording: should the owner get a per-build route for prompt runs? · reason Options seen: (a) as built, the owner opts in through SPEC_AUDIT_DEFAULT on the default branch or a slug-mode README the owner lands; (b) an invocation-line --spec-audit confirmed at the one owner turn and recorded as a surfaced row, as --waive is; (c) a UserPromptSubmit hook that records the owner's typed prompt for preflight to read. Refused: (b) is the run's own claim that the owner asked, the shape this ruling closes; (c) adds a hook and a public surface, an owner turn by veto 2.

2026-10-04T22:45:57Z decision · item aEvidencedLens (branch spec-review-improvements-f59dad, live) carries a prompt-mode spec-audit: line its owner asked for in its prompt; once it merges a default branch carrying check 89, its --close refuses at authorization-reachable, which takes no override. What should happen to it? · reason Options seen: land aEvidencedLens before this build; the owner lands its README as a slug-mode folder on the default branch; abort and re-run it after declaring SPEC_AUDIT_DEFAULT; or grandfather it by name. Refused: it is another run's build and a grandfather list written by this run is a run landing an opt-in, which unit 5 refuses.

2026-10-04T22:47:27Z brief · item TOOL-aWardedAudit-5 · reason 6adc39e09fe2 memory/builds/aWardedAudit/prompts/2026-10-05-prompt-TOOL-aWardedAudit-5-1-build-brief.md

2026-10-04T22:47:30Z brief · item TOOL-aWardedAudit-6 · reason 964068ab7fb7 memory/builds/aWardedAudit/prompts/2026-10-05-prompt-TOOL-aWardedAudit-6-1-build-brief.md

2026-10-04T22:47:42Z dispatch · item aa14e5eb TOOL-aWardedAudit-5 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aWardedAudit/spec/2026-10-05-spec-TOOL-aWardedAudit-5.md

2026-10-04T23:04:11Z dispatch · item c47342a3 TOOL-aWardedAudit-6 · reason tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh tools/hooks/README.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md memory/guides/SESSION-KICKOFF.md memory/builds/aWardedAudit/spec/2026-10-05-spec-TOOL-aWardedAudit-6.md
