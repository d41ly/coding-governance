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
