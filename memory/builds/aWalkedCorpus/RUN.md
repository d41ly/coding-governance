# aWalkedCorpus - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 30db4329e93a58f7838061ec36c4c3d38462bf80
phase: ABORTED
keepalive: 267649f9
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 3e5c6d4373050f545eb516b6e305d352ceb10b66
anchor-ref: refs/heads/main
base: 3e5c6d4373050f545eb516b6e305d352ceb10b66
keepalive-reaped: yes
parked-surfaced: yes

## Parked

**The adopter-facing recall floor — REFUSED as scope, not resolved.** The question: should an
adopting repo receive a graded recall floor at all, or only this one? The options seen were (a)
withhold the fixture, the gate program and its arms from the kit payload, which is what this run
built, and (b) declare a third gate leg in the kit descriptor plus an adoption-time path by which an
adopter seeds their own fixture and MEASURES their own value. Option (b) was refused because it
differs from (a) in what gets BUILT — it needs a seeding mechanism, an adopter-facing measuring verb,
and an answer for a corpus too small to score — and a standing mandate delegates fork resolution,
never scope. It is marked RESOLVED for this unit only in the spec's section 8, and the parked half is
a successor's subject. The round-1 audit of the predecessor asked for this decision and never got
one, which is why it is written here rather than left implicit.

**The round-4 fixes were self-verified rather than independently re-reviewed — a judgement I took,
recorded so it can be reversed.** The closing review returned SHIP WITH FIXES with zero blockers and
eleven findings; all eleven were folded. The options were (a) a fifth adversarial round over the fix,
or (b) relying on the arms each fix added plus the full bar. I took (b), because the build method
re-reviews a FIX for blockers and there were none, and because every fix carries an arm I watched
fire — the NOT MEASURED red, the chunks-measured audit, the extract refusal at exit 2, the malformed
question refusal, and a leak delta of zero. An owner who wants (a) has lost nothing by the delay.

**What the corpus will do to this pin, stated because nobody has watched it yet.** The floor is
derived from h=10 and R=12 over a corpus that moves every commit. It has been green across this
build only. The first genuine movement — a record retired, a question that starts or stops hitting —
is the first real test of whether the one-retirement headroom is the right budget, and nothing here
has observed that yet.

2026-08-17T18:22:13Z abort · item aWalkedCorpus · reason Landing refused, not attempted: origin/main is RED on two of its own merge-bar legs at 43eb6b1, measured in a clean detached worktree carrying none of this branch's changes — lexicon naming predicates (verb offenders 450 over pin 417) and govkit selftest (the DEFAULT-selection apply arm). The unit is BUILT, reviewed across four rounds and CLOSED, and every leg this run owns is green on the reconciled tree; the pre-push hook runs the full bar and would refuse the push, and bypassing it discards the entire bar the standing mandate leans on. Raising another build's shrink-only pin or re-pinning its selftest arm is a SCOPE decision a standing mandate does not delegate, so it is parked as TOOL-aWalkedCorpus-7 rather than absorbed. The branch is complete and committed: merge and push it once main is green, or hand the two legs to their owning builds first.
