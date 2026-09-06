# aJoinedCanon - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 3354f72ab32f464585dbe86be858b3baba161bc9
phase: BUILDING
mode: slug
anchor-kind: default-branch
keepalive: ccc33b22
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 274aa39b786c886991726896927337c0e3048e0c
anchor-ref: refs/heads/main
base: 274aa39b786c886991726896927337c0e3048e0c

## Parked

2026-09-06T12:56:23Z dispatch · item 274aa39b TOOL-aJoinedCanon-1 · reason tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh .memory-tree.conf tools/memory-tree/.memory-tree.conf.example memory/TEMPLATE-SPEC.md memory/HYGIENE.md tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md memory/guides/SESSION-KICKOFF.md

2026-09-06T13:53:57Z decision · item TOOL-aJoinedCanon-2 cannot land: its fold procedure needs 1046 bytes in memory/guides/BUILD-METHOD.md and M1's budget leaves 12. Raise the byte budget, or rule where the table goes instead? · reason Measured at build time, not estimated: BUILD-METHOD.template.md is 24564 B against M1's stated ceiling of 24 KB (24576 B), so headroom is 12 B; S1's block as §4 writes it is 1046 B, a breach of 1034. The LINE half is fine at 335 of 350, exactly as M1 predicts when it says the BYTE half binds first. Three options seen, none survivable by this run. (1) Raise the budget — M1 says the figure is a stated constraint of a document and every prior raise was an owner call, and M3 puts M1's own budget outside the mandate's delegation by name, so this is veto 2 and not mine. (2) Trim ~1034 B of BUILD-METHOD prose to fit — the only block that size which is not instructional is M1's own record of the prior owner budget calls, and deleting the record of an owner decision to make room for my own edit is not a trade this run gets to make; any other trim is unspecced surgery on a governance carrier. (3) Put the table in memory/gotchas/fold-text-is-unreviewed-surface.md, which unit 2's own §10 names as the seam it extends, and leave M4 a pointer — this is M1's own pointer design and it is what I would recommend, but it fails AC1 and AC3 as written, so veto 1 refuses it and even a two-line pointer overruns 12 B. M3's rule is park, never the least-bad option. NOTE the precedent this repeats: M1 records that the 2026-08-21 raise happened because two builds added rules concurrently, nothing was droppable, and the owner moved the constraint instead of the content. Unit 2 is the ONLY unit of this build that writes method PROSE — units 8 and 11 touch that file only through the byte-neutral version-marker re-render — so units 3 through 11 are unaffected and the run continues through them. Unit 2 stays SPECCED, which will block build-complete at close.

2026-09-06T13:55:23Z rescope · item retire TOOL-aJoinedCanon-2 · reason M1's byte budget on memory/guides/BUILD-METHOD.md leaves 12 B and S1's fold procedure needs 1046 B, measured at build time. Raising that number is an owner call M3 puts outside the mandate by name, the only trim of that size is M1's own record of the prior owner budget calls, and the pointer alternative fails AC1 and AC3. Parked in full with the measurement and the three options; the owner's ruling reopens it as a new unit.

2026-09-06T13:57:26Z dispatch · item 323703f7 TOOL-aJoinedCanon-3 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh .memory-tree.conf tools/memory-tree/.memory-tree.conf.example tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/HYGIENE.template.md memory/TEMPLATE-SPEC.md memory/HYGIENE.md memory/guides/SESSION-KICKOFF.md

2026-09-06T14:35:20Z dispatch · item d0fcadcb TOOL-aJoinedCanon-4 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh .memory-tree.conf tools/memory-tree/.memory-tree.conf.example tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/HYGIENE.template.md memory/TEMPLATE-SPEC.md memory/HYGIENE.md memory/guides/SESSION-KICKOFF.md

2026-09-06T15:08:39Z dispatch · item 0e8164a2 TOOL-aJoinedCanon-5 · reason tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md

2026-09-06T15:56:36Z dispatch · item e3d26f84 TOOL-aJoinedCanon-7 · reason tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md .memory-tree.conf memory/map/features/spec-tokens.md memory/guides/SESSION-KICKOFF.md

2026-09-06T16:05:42Z dispatch · item 1430e86a TOOL-aJoinedCanon-8 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/check-memory-hygiene.test.sh .memory-tree.conf tools/memory-tree/.memory-tree.conf.example tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/HYGIENE.template.md memory/TEMPLATE-SPEC.md memory/HYGIENE.md memory/guides/SESSION-KICKOFF.md
