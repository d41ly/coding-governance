# Spec brief — TOOL-aBriskPreflight-6: the pre-push straggler layer runs only over pushed branches, and sets up only when one is pushed

**Serves:** research TOOL-aBriskPreflight-6

Read first: the build README, the prompt record and the baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`, section "The pre-push hook on a
claim-shaped push").

## What the measurement shows

The unattended claim write (`write_claim` in `tools/unattended/unattended.sh`) pushes a parentless,
empty-tree commit to `refs/gov/runs/<slug>` under `REMOTE_BOUND=60`, and that push runs
`.githooks/pre-push`. Fed one such ref line, the hook took 53 s on node `a` (45 forks, 31 execs) to
reach its `skip-nondefault` exit; the peer measured 46 s; four preflights in a row were refused at
check 109 because the push was killed at 60 s. About 35 s of it is the straggler layer's setup —
sourcing `straggler-guard.sh` and `init_straggler_guard`, `resolve_python`, two `resolve_kit_dir`
python starts — spent to ask `check_has_delta`, which for a parentless empty-tree commit can only
answer no.

## The mechanism, one

The straggler layer (the block headed "the shards-to-builds STRAGGLER layer, PER PUSHED REF") states
its own population: "per pushed ref that is not the default branch and not a delete", and every
bullet under it is about a feature BRANCH that will later merge. The layer selects only pushed refs
under `refs/heads/`, and does its setup — the library source, `init_straggler_guard`, the python and
module resolution — only when at least one such ref is in the push. A push carrying no branch reaches
the existing exits with the same decision and the same run-log lines it writes today.

## Things the spec must settle, with the reason

- What a non-branch ref the layer used to audit (a tag, a note, any other namespace) loses, and
  whether that is a weakening. A tag does not merge, but `git merge <tag>` exists; the spec decides
  whether `refs/tags/` stays in the population, by M3's rule, and records the loss of anything it
  drops. The prompt's role statement binds: weaken no check.
- That the layer's announcements (the pre-flip NOTICE, the two "did NOT run" lines, DEAD PROBE,
  REFUSING) still print for a branch push exactly as today, and the `refuse-straggler` decision and
  exit 1 are unchanged.
- Whether the hook's prelude ABOVE the stdin read (the kit-root ladder, `check_reviewed_file` on
  `gate-env.sh`) can also be skipped for a branchless push. Only if it loses nothing; the run log's
  START and END lines are kept for every push.
- What a claim push costs after, measured the same way (the hook fed one claim-shaped line in a
  throwaway clone, never the shared git dir, whose push journal it would write), and whether that
  fits `REMOTE_BOUND` with margin at this host's spawn cost.

## Out of scope

- `REMOTE_BOUND`, which the prompt forbids raising.
- The default-branch gates below the exits: the merge-loss check, the bar, the doc class.
- `straggler-guard.sh`'s own predicates.

## Acceptance shape

- The claim-shaped push before and after: wall and spawn count, with host state.
- RED on a staged break, GREEN restored, through a sliced arm of `.githooks/pre-push.test.sh` (or
  the straggler arms of whichever suite owns them): a feature-branch push carrying an unaccounted
  transition merge is still REFUSED; a pre-flip branch still gets its notice.
- The run-log decision for a claim push is still `skip-nondefault`.
- Witnesses in §6 by basename.

## Conventions

- Tier-2: the push boundary.
- `.githooks/pre-push` ships through the push-main kit: its version marker moves once at the end of
  the build, in every carrier `bash tools/check-kit-versions.sh` names, and a kickoff-manifest watch
  on it owes a `last-audit` re-stamp.
- Order: 1, with units 1 and 5 (disjoint write sets).
