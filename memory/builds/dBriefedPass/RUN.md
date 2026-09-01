# dBriefedPass - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 1dc4f0316d41edc3cb8020d26e5ae4bc2b60bae6
phase: BUILDING
branch-sha: 269dacae79bd5001486de32b3277675a953d3483
branch-ref: refs/heads/branch/unattended-kit-workflow-40540b
mode: prompt
anchor-kind: run-branch
keepalive: 9cc0eda1
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: d65da7abb562957247720898fba1d7ef983f242a
anchor-ref: refs/heads/main
base: 269dacae79bd5001486de32b3277675a953d3483

## Parked

2026-09-01T10:24:58Z review · item dBriefedPass-spec-set · reason verdict BLOCKED · blockers 5

2026-09-01T11:03:57Z review · item dBriefedPass-spec-set · reason verdict BLOCKED · blockers 2

2026-09-01T11:42:04Z review · item dBriefedPass-spec-set · reason verdict BLOCKED · blockers 3 · NON-CONVERGENT

2026-09-01T11:42:19Z decision · item The unattended Skill instructs a run to record the NON-CONVERGENT exit disposition with --disposition fold|promote, and claims the merge bar reads that field. Neither is true: the driver refuses the flag with check 14 unknown-argument, and check-unattended.sh contains zero occurrences of disposition. Should the flag and a checker term be built? · reason MEASURED at the exit this run reached, by running the documented command: SKILL.template.md:607 and the installed render both carry the instruction; unattended.sh has one occurrence of the word, in a comment at :3758; check-unattended.sh has none; UNATTENDED-PROTOCOL.md never mentions a review disposition at all. So an agent that follows the Skill at a NON-CONVERGENT exit halts on an unknown argument, and the sentence promising the bar reads the field is false in the direction that matters. This is the same instruction-with-no-route class the protocol records about the DECISION park kind. NOT ADOPTED under protocol section 11: it needs a new public surface (a driver flag) plus edits to the Skill template and the protocol, which is M3 veto 2, and section 11 says a discovery tripping a veto is parked rather than taken. Options seen: (a) build the flag and a checker term as a unit of this build - refused, veto 2 reserves it; (b) file a backlog row - refused, section 11 routes a veto trip to a park and a backlog row would understate that the shipped instruction is currently unexecutable; (c) park it here, which is what this is. The run continues: dropping the flag records the round correctly, so this blocks nothing.

2026-09-01T11:45:06Z dispatch · item 1dc4f031 TOOL-dBriefedPass-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/guides/BUILD-METHOD.md tools/memory-tree/BUILD-METHOD.template.md

2026-09-01T11:57:29Z dispatch · item ac4875fb TOOL-dBriefedPass-2 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/PROTOCOL.template.md tools/unattended/SKILL.template.md memory/guides/UNATTENDED-PROTOCOL.md .claude/skills/unattended/SKILL.md

2026-09-01T11:59:16Z brief · item TOOL-dBriefedPass-2 · reason 27a8086b8ae6 memory/builds/dBriefedPass/prompts/2026-09-01-prompt-TOOL-dBriefedPass-2.md

2026-09-01T11:59:26Z brief · item TOOL-dBriefedPass-2 · reason b5ea709eb4a5 memory/builds/dBriefedPass/prompts/2026-09-01-prompt-TOOL-dBriefedPass-2.md

2026-09-01T12:01:12Z brief · item TOOL-dBriefedPass-2 · reason 45aa419343d4 memory/builds/dBriefedPass/prompts/2026-09-01-prompt-TOOL-dBriefedPass-2.md

2026-09-01T12:01:13Z brief · item TOOL-dBriefedPass-3 · reason 8fc37263f2ef memory/builds/dBriefedPass/prompts/2026-09-01-prompt-TOOL-dBriefedPass-3.md

2026-09-01T12:06:44Z brief · item TOOL-dBriefedPass-3 · reason 3941879a56d2 memory/builds/dBriefedPass/prompts/2026-09-01-prompt-TOOL-dBriefedPass-3.md

2026-09-01T12:11:04Z decision · item The unattended protocol render is at its declared INDEX_CAP_BYTES and cannot absorb a new verb's documentation. Should the cap move, should the protocol be split, or should section 7 stop carrying a paragraph per verb?  · reason MEASURED while landing TOOL-dBriefedPass-2's carrier row. memory/guides/UNATTENDED-PROTOCOL.md was 61353 bytes against .memory-tree.conf's INDEX_CAP_BYTES=61440, so 87 bytes of headroom for a kit whose section 7 gives every other verb a four-to-eight line paragraph. Documenting --brief at that density costs about 550 bytes. I landed it by cutting the entry to two lines and trimming four neighbouring entries in the same section by about 500 bytes total, which preserves every fact and loses prose the entries could spare - but that is a one-time move and the NEXT verb has 55 bytes to work with. Options seen: (a) raise INDEX_CAP_BYTES - refused, it is a project declaration in .memory-tree.conf and M3 veto 2 plus protocol section 11 reserve a governance-carrier declaration to the owner; (b) rotate the protocol to archive as hygiene check 6's message suggests - refused, that remedy is written for an append-only index and this is a binding contract every run reads whole; (c) split section 7 into its own carrier - a real option, and a structural change to a governance carrier, which is the same veto; (d) trim to fit and park the structural question, which is what I did. What makes this worth an owner turn rather than a backlog row is that it is not about this verb: the kit has added --propose, --attest, --rescope, --dispatch, --review and now --brief, section 7 grows once per verb, and the cap is a fixed number nobody has revisited.

2026-09-01T12:12:14Z dispatch · item b9fb4fb0 TOOL-dBriefedPass-3 · reason tools/unattended/unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-pass-order.test.sh tools/gate-legs.json .unattended.conf tools/unattended/.unattended.conf.example tools/unattended/kit.toml tools/govkit/subject-pins.tsv memory/map/features/unattended.md

2026-09-01T12:13:27Z dispatch · item b9fb4fb0 TOOL-dBriefedPass-4 · reason tools/workflows/unattended-build.js

2026-09-01T12:13:30Z dispatch · item b9fb4fb0 TOOL-dBriefedPass-5 · reason tools/z.sh

2026-09-01T12:30:11Z dispatch · item ead1b820 TOOL-dBriefedPass-4 · reason tools/workflows/unattended-build.js tools/workflows/unattended-build.test.sh tools/workflows/kit.toml tools/gate-legs.json memory/map/features/workflow-scripts.md

2026-09-01T12:33:06Z decision · item tools/hooks/agent-cap.js denies any agent() inside a loop body unconditionally, which forbids STRICTLY SEQUENTIAL per-unit dispatch — the one shape TOOL-cBriefedPilot-21's ratified 'parallelism route: none' actually permits. Should the rule distinguish a sequential await from a loop-built thunk array? · reason MEASURED by running the hook's own predicate over tools/workflows/unattended-build.js: it denied L171 and L209 with 'agent() inside a loop body - a loop-built thunk array is the evasion this rule exists for'. The two lines are 'const r = await agent(...)' directly in a for-of body, which runs ONE agent at a time and is the safest dispatch shape there is. The hook's comment at :95-112 states the whitelist is closed and names no marker for this case, so there is no author claim that admits it. THE CONFLICT IS EXACT: bounded-parallel fan-out is PERMITTED by the hook and FORBIDDEN by the ratified parallelism verdict; sequential dispatch is REQUIRED by that verdict and FORBIDDEN by the hook. A harness that iterates a build's units sits precisely in the gap. Note also that the rule's stated ceiling is the VERIFY-stage total of 5, and a build stage is not a verify stage, so the predicate is applying a verify rule to a dispatch loop. Options seen: (a) teach the hook that an awaited call in a loop body with no thunk array is sequential - refused, agent-cap.js is a governance carrier named by charter section 8 and machine-compared by check-playbook-parity.sh, which is M3 veto 2; (b) restructure the harness so the agent() call sits in a helper the loop calls - refused, that is textually indistinguishable from the evasion the rule names, and passing a checker by indirection is worse than not passing it; (c) collapse each stage to ONE agent handling all units in declared order, which is what I built: it needs no loop, keeps the STAGE order structural (which is the defect the owner actually reported), and delegates per-unit order to TOOL-dBriefedPass-3's --dispatch refusal, a machine check stronger than JS control flow. Spec 4 moved to rev-5 to record the divergence before the code changed. The run continues; this blocks nothing.
