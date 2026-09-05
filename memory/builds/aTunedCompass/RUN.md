# aTunedCompass - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 839601f37d79d1f603d36867b04973a50ecc38b4
phase: BUILDING
mode: slug
anchor-kind: default-branch
keepalive: 6ced7a37
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 22d75b31296a3a4fe28cf53a85c51076b8e6d798
anchor-ref: refs/heads/main
base: 22d75b31296a3a4fe28cf53a85c51076b8e6d798

## Parked

2026-09-05T07:34:57Z review · item spec-set · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-05T07:35:26Z decision · item The review row at 2026-09-05T07:34:57Z, subject 'spec-set', verdict CLEAN, blockers 0, is NOT backed by a review and must not be read as one. · reason I emitted it by mistake while setting the SPECCING phase, before the M4 spec audit had been run at all. The row is history-class and append-only, so I have not edited it out; 'spec-set' is not a unit id and joins to no subject, so nothing downstream reads it as a verdict on any spec. The real audit rounds are recorded per spec id afterwards. Surfaced because a review row nobody ran is exactly the green-by-absence shape this repo gates against, and the owner is entitled to see that one exists on this record.

2026-09-05T08:04:25Z review · item TOOL-aTunedCompass-1 · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-05T08:04:27Z review · item TOOL-aTunedCompass-2 · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-05T08:04:29Z review · item TOOL-aTunedCompass-3 · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-05T08:04:30Z review · item TOOL-aTunedCompass-5 · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-05T08:04:32Z review · item TOOL-aTunedCompass-7 · reason verdict CLEAN · blockers 0 · CONVERGED

2026-09-05T08:04:33Z review · item TOOL-aTunedCompass-8 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T08:04:35Z review · item TOOL-aTunedCompass-10 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T08:04:36Z review · item TOOL-aTunedCompass-11 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T08:04:38Z review · item TOOL-aTunedCompass-4 · reason verdict BLOCKED · blockers 1

2026-09-05T08:04:39Z review · item TOOL-aTunedCompass-6 · reason verdict BLOCKED · blockers 1

2026-09-05T08:04:41Z review · item TOOL-aTunedCompass-9 · reason verdict BLOCKED · blockers 1

2026-09-05T08:50:59Z review · item TOOL-aTunedCompass-4 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-09-05T08:51:00Z review · item TOOL-aTunedCompass-6 · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT · disposition fold

2026-09-05T08:51:03Z review · item TOOL-aTunedCompass-9 · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT · disposition fold

2026-09-05T13:15:29Z decision · item Unit 11 is implemented and committed but UNVERIFIED: the unattended kit's driver suite, which carries its three new MAP_CLI arms and eight arms it re-worded, never completed. · reason Two attempts, each producing ZERO output before being killed at its bound — one at 50 minutes, one at 90. A pristine-tree baseline was equally silent for its first 100 seconds, so the silence is this suite's buffering rather than a hang this build introduced; that is why the work was committed rather than reverted. But buffering is not evidence of passing, so unit 11's spec stays SPECCED and is not closed. Every other leg over it is green: unattended kit gate (check 22 observed RED on the undocumented key first, then green with all six carriers), memory hygiene, spec tokens, dead paths, kit version markers, install prefix, lexicon and wiring. The owner's call is whether to run that suite on a quieter node and close the unit, or to treat the arms as suspect.

2026-09-05T13:15:32Z decision · item Units 2, 3 and 9 are UNBUILT and the run stopped rather than start unit 9. · reason 2 and 3 are blocked on 9, and 9 is the largest single piece in the build: a sampled, agent-judged fixture plus engine changes binding the audit's graded set to each fixture. Starting it without finishing would leave a half-authored question set that TOOL-aTunedCompass-3 is due to pin the merge bar against, which is worse than none. What the run did instead: unit 9's spec gained a MEASURED candidate pool at rev-5 — 165 of 179 distinct logged questions carry a chunk hit in an unanchored file — so the next run inherits the sampling frame rather than rediscovering it. The judgement half F1 resolved is untouched.

2026-09-05T13:45:54Z review · item aTunedCompass · reason verdict BLOCKED · blockers 2
