# aTunedCompass - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 5d29a806d695ac9db9da819a834aff0effb75c04
phase: FOLDING
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
