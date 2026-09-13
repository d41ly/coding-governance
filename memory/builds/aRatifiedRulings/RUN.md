# aRatifiedRulings - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: fc6ee211db75bf2efd76b8a6ce952286afc196f7
phase: REVIEWING
branch-sha: 16da4c6abdb5d74ad80891f51f254cd5205d0b17
branch-ref: refs/heads/branch/aRatifiedRulings
mode: prompt
anchor-kind: run-branch
keepalive: 9de7b72e
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 9fac2b53b625032b93be6a09c0bf99f912ae35dd
anchor-ref: refs/heads/main
base: 16da4c6abdb5d74ad80891f51f254cd5205d0b17

## Parked

2026-09-13T11:59:35Z review · item TOOL-aRatifiedRulings-1 · reason verdict BLOCKED · blockers 1

2026-09-13T11:59:36Z review · item TOOL-aRatifiedRulings-2 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-13T11:59:37Z review · item TOOL-aRatifiedRulings-3 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-13T11:59:38Z review · item TOOL-aRatifiedRulings-4 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-13T12:46:36Z review · item TOOL-aRatifiedRulings-1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-13T13:13:28Z dispatch · item da9b9a33 TOOL-aRatifiedRulings-1 · reason tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/guides/SESSION-KICKOFF.md memory/builds/aRatifiedRulings/build memory/builds/aRatifiedRulings/spec memory/builds/aRatifiedRulings/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T13:13:54Z brief · item TOOL-aRatifiedRulings-1 · reason 20e640d1ce04 memory/builds/aRatifiedRulings/prompts/2026-09-13-prompt-TOOL-aRatifiedRulings-1-1-build-brief.md

2026-09-13T13:19:59Z dispatch · item da9b9a33 TOOL-aRatifiedRulings-1 · reason tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/HYGIENE.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/ANNOTATION-STYLE.template.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md memory/builds/aRatifiedRulings/prompts

2026-09-13T14:06:54Z dispatch · item dba6053a TOOL-aRatifiedRulings-2 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aRatifiedRulings/build memory/builds/aRatifiedRulings/spec memory/builds/aRatifiedRulings/prompts memory/builds/aRatifiedRulings/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T14:07:13Z brief · item TOOL-aRatifiedRulings-2 · reason 679ae7ed8bc8 memory/builds/aRatifiedRulings/prompts/2026-09-13-prompt-TOOL-aRatifiedRulings-2-1-build-brief.md

2026-09-13T14:12:59Z dispatch · item dba6053a TOOL-aRatifiedRulings-2 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aRatifiedRulings/build memory/builds/aRatifiedRulings/spec memory/builds/aRatifiedRulings/prompts memory/builds/aRatifiedRulings/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T19:36:18Z dispatch · item 90348fde TOOL-aRatifiedRulings-3 · reason tools/memory-tree/check-memory-hygiene.test.sh memory/builds/aRatifiedRulings/build memory/builds/aRatifiedRulings/spec memory/builds/aRatifiedRulings/prompts memory/builds/aRatifiedRulings/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T19:36:48Z brief · item TOOL-aRatifiedRulings-3 · reason 4fd7eaf7f15e memory/builds/aRatifiedRulings/prompts/2026-09-13-prompt-TOOL-aRatifiedRulings-3-1-build-brief.md

2026-09-13T19:43:25Z dispatch · item 90348fde TOOL-aRatifiedRulings-3 · reason tools/memory-tree/check-memory-hygiene.test.sh .lexicon.conf tools/install-prefix-carried.txt memory/map/features/memory-tree-hygiene.md memory/builds/aRatifiedRulings/build memory/builds/aRatifiedRulings/spec memory/builds/aRatifiedRulings/prompts memory/builds/aRatifiedRulings/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T20:14:12Z decision · item TOOL-aRatifiedRulings-3 AC2 ratio and AC3 full-bar row: re-measure or accept the count · reason unit 3's one after run read 775.7 s against the §4 quiet 598.7 s, ratio 1.296 over the 0.8 bound, on a box carrying thirteen sibling run-gates.sh bars; trace attribution puts the changed region at 0.59 of its §4 seconds and every untouched region at 1.3-9.2x, and the count fell 20 to 13 with zero git archive. Options: the paired quiet re-measure AC2 spells, the GATE_FULL=1 GATE_SELFTESTS=1 bar AC3 spells, or accept the count as the claim. Refused here because the owner's per-pass rule allows a pass one run of the suite and no bar

2026-09-13T20:24:30Z dispatch · item e96cf2f4 TOOL-aRatifiedRulings-4 · reason tools/run-gates/run-gates.sh tools/run-gates/run-gates.test.sh tools/run-gates/README.md memory/guides/SESSION-KICKOFF.md memory/builds/aRatifiedRulings/build memory/builds/aRatifiedRulings/spec memory/builds/aRatifiedRulings/prompts memory/builds/aRatifiedRulings/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-13T20:24:54Z brief · item TOOL-aRatifiedRulings-4 · reason 87d51c529a50 memory/builds/aRatifiedRulings/prompts/2026-09-13-prompt-TOOL-aRatifiedRulings-4-1-build-brief.md

2026-09-13T21:36:35Z review · item aRatifiedRulings · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED
