**Serves:** diff-review TOOL-dQuietDisk-36

# dQuietDisk — Tier-2 CLOSING DIFF review, round 2

*Node `d`, 2026-11-22. This round reads the fold of round 1's two HIGHs, TOOL-dQuietDisk-36, with H1 and H2 handed in
as prior findings.*

**Range reviewed: `879413160dd03c1f0bd28c001007bd08b44e3a1d...4840e65ede83`** (round 1's recorded tip to the fold's
commit; the records-only commits between them change no product file).

**Round: 2.** Harness run `wf_45a65b34-7bf`, key `diff-review-r2-879413160dd0-4840e65ede83-fdd6eb0a`.

## Verdict: CLEAN

`review-shape kind=diff-review round=2 intensity=full at=verify raw=1 confirmed=0 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=0 low=0 agents=6 out-tokens=47003 trigger=owed`

Five lenses ran and returned; one skeptic batch adjudicated the one raw finding. The harness wrote no report because
nothing was confirmed, so the main loop wrote this record from its return. The loop is CONVERGED: blockers 0 and
highs 0 at round 2, with 9 MEDIUM and LOW findings of round 1 standing, promoted to one batched unit.

## The refuted finding

1. (seams, raised HIGH, skeptic MEDIUM, refuted) The `GIT_ENV_LEAKS` scrub covers the shared-template branch of
   `build_fixture` only: its no-`--template` and `per-case` paths, and the per-case branches of `mk_repo` in
   `tools/run-gates/run-gates.turnstile.test.sh` and `build_pushed_fixture` in `.githooks/pre-push.test.sh`, still run
   the builder under the caller's environment. Refuted for this fold: the same unscrubbed builder call stands at round
   1's tip and the fold neither adds nor reaches it; H1 was scoped to the template cache's verbs. It is a real
   pre-existing bypass of the same class, so the run filed it as ask TOOL-dQuietDisk-38.
