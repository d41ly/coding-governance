# aProvenReuse - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
keepalive-reaped: yes
parked-surfaced: yes, 0 surfaced
witness: 09ad99157473d69753aff2544c667768cf555792
phase: VERIFYING
branch-sha: 3bfc5e877e1c416781bffa9e5bf5e1b1b7a27036
branch-ref: refs/heads/branch/unattended-kit-gaps-a3b869
mode: prompt
anchor-kind: run-branch
keepalive: 2526ce95
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 396cd9db154f1621db5cb4cde72b93470b2f690c
anchor-ref: refs/heads/main
base: 3bfc5e877e1c416781bffa9e5bf5e1b1b7a27036

## Parked

2026-08-31T02:26:39Z review · item spec-set · reason verdict BLOCKED · blockers 4

2026-08-31T03:00:51Z review · item spec-set · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT

2026-08-31T06:01:14Z review · item aProvenReuse · reason verdict BLOCKED · blockers 2

2026-08-31T06:02:19Z rescope · item add TOOL-aProvenReuse-5 · reason Closing-review F9, adopted under protocol section 11 rather than parked: the example-conf parity arm derives its population from the engine's ${NAME:-} reads, so a BARE preset is invisible to it. Two adopter keys are already through that hole -- FORK_MARK_CUTOFF and REVIEW_VERDICT_CUTOFF are absent from the shipped example and nothing noticed -- and this build's own SPEC10_EVIDENCE_CUTOFF walked through it too. Strictly beneficial: it makes adopter-key discoverability strictly better, makes nothing worse, and trips no M3 veto. Gate the CLASS, not the instance.

2026-08-31T08:04:46Z review · item aProvenReuse · reason verdict BLOCKED · blockers 1

2026-08-31T10:09:25Z review · item aProvenReuse · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT
