# dTracedLattice - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
landed-anchor: remote
units-at-landing: TOOL-dTracedLattice-6 TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-7
unpushed-at-landing: 0
parked-surfaced: yes, 1 surfaced
keepalive-reaped: yes
witness: 4042505ac937813876aa313037acc4836c746e15
phase: LANDED
mode: slug
anchor-kind: default-branch
keepalive: 9cdff79b
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 6ec402bd3eb7f9cb5ce6257b0f60348ae3e593fc
anchor-ref: refs/heads/main
base: 6ec402bd3eb7f9cb5ce6257b0f60348ae3e593fc

## Parked

2026-09-05T22:53:10Z review · item TOOL-dTracedLattice-1 · reason verdict BLOCKED · blockers 3

2026-09-05T22:53:16Z review · item TOOL-dTracedLattice-1 · reason verdict BLOCKED · blockers 2

2026-09-05T22:53:36Z review · item TOOL-dTracedLattice-1 · reason verdict BLOCKED · blockers 3 · NON-CONVERGENT · disposition fold

2026-09-06T04:45:43Z review · item dTracedLattice · reason verdict BLOCKED · blockers 1

2026-09-06T05:33:30Z review · item dTracedLattice · reason verdict BLOCKED · blockers 1 · NON-CONVERGENT · disposition fold

2026-09-06T07:41:58Z decision · item Land this build over a merge-bar red that predates it, or hold it until another node clears main? · reason MEASURED, not suspected: `python tools/drift-audit/drift_report.py --check` exits 1 on origin/main ITSELF (tested in a detached worktree at ede5af2c), on the pinned BASE 6ec402bd, and on this branch — same two findings each time. (1) RATCHET WEAKENED: .lexicon.conf's LANGS says 'sh::dark' and has since b0626152 on 2026-08-16, with no justification comment above the line; the check wants one naming 'sh: parser -> dark'. I will not author it, because I do not know why shell is dark and a justification I invented would be worse than the red it clears. (2) closed_specs_with_no_product_commit = 2 against a pin of 1: TOOL-aMooredAnchor-1 (closed 2026-08-11) and a stale trace-waiver row for TOOL-aSurfacedLexicon-1. Both belong to other builds. THE OPTIONS I SAW. Fix it: needs another node's reasoning for the LANGS line and another build's spec drained, neither of which I can do truthfully. Abort: throws away seven closed, reviewed units over a red no push of mine can clear. Override gates-green and let the lander decide: what I took, because the override surfaces here and the lander still applies its own bar. NOTE the second red, 'pass-order history', is a TIMEOUT at 2400s under contention and not a leg failure — it exits 0 standalone, and two other unattended runs were BUILDING on this machine throughout. Everything this build's diff touches is green: codebase-map selftest 60/60, coverage+freshness, gate coverage, lexicon naming predicates, install-prefix, govkit selfcheck, spec tokens, memory-recall selftest 44/44 and recall floor arms 21/21.

2026-09-06T07:43:05Z override · item gates-green · reason the merge bar is RED on origin/main itself, not on this build. drift-audit records exits 1 at ede5af2c, at the pinned BASE 6ec402bd and here, with the same two findings — an unjustified .lexicon.conf LANGS ratchet dating from 2026-08-16 and closed_specs_with_no_product_commit at 2 against a pin of 1, both entries belonging to other builds. pass-order history TIMED OUT at 2400s under contention rather than failing; it exits 0 standalone. Every leg this build's diff touches is green. The decision this override represents is parked above with the options and why I refused to decide it, and the lander applies its own bar regardless of what is recorded here.
