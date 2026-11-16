# Promotion — aPiecewiseGrade: the closing review's item 1, as TOOL-aPiecewiseGrade-6

**Serves:** research TOOL-aPiecewiseGrade-6

## The prompt

> Promote, build now (Recommended)

The owner's answer, 2026-11-16, to "Build them now or file them?", put through the session's question tool after the closing review `2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1` returned CLEAN WITH FIXES with two medium items.

## The brief

### Goal
The closing review's item 1 (id 1, medium): `init_spec_token_check` in `tools/unattended/unattended.sh` sweeps every generation of the slug but the one `spec-tokens.<slug>.live` names, so it can delete another in-flight same-slug `--dispatch`'s `SPEC_TOKENS_CACHE_NEXT`, and it runs before the claim check; no lock serialises two same-slug `--dispatch` calls in one worktree. Findings stay correct, but a caller with no claim deletes state another run depends on. TOOL-aPiecewiseGrade-6 puts every piece of per-slug spec-token state under one per-slug lock.

### Items
1. Write `memory/builds/aPiecewiseGrade/spec/2026-11-16-spec-TOOL-aPiecewiseGrade-6.md`, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, order 5, Tier-2, in the shape `memory/TEMPLATE-SPEC.md` states. Read item 1 of `memory/builds/aPiecewiseGrade/reviews/2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1.md` whole; its Fix paragraph is the design to verify against HEAD, not to copy.
2. One per-slug lock in the sidecar, held from the start half to the end of the read half, covering the `.inputs` removal, the key write, the `.live` write, the sweep and the old generation's removal. A run that cannot take it runs with the cache off and records nothing. A killed run's lock is breakable, and the spec states how its staleness is judged. Reuse an existing lock primitive of the unattended kit if one fits, and say which; `claim-push.lock` is the one the review found.
3. Every refusal, note and skip line of `--dispatch` keeps its bytes; the lock-not-taken branch's announcement, if any, is new text the spec states.
4. Arms: two same-slug start halves in parallel, the first run's next generation and `.inputs` surviving the second; the lock-not-taken branch running with the cache off; a stale lock broken. Each seen red on a staged break. Shell hygiene and the harness-arms leg admit every new site.
5. Name every new function and file through `python tools/lexicon/lexicon.py --suggest`. State what the change owes: the codebase map, the symbols index, the verbs guide in both copies, mindful that `memory/guides/UNATTENDED-VERBS.md` already exceeds its byte budget in warn mode.
6. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit. Return its path and status line, each criterion's id with one line, any fork with its recommendation, and the checker's final line.

### Acceptance
- Two same-slug dispatches in one worktree never remove each other's next generation or input record.
- A run that cannot take the lock grades correctly with the cache off.
- Every existing `--dispatch` line keeps its bytes.

### Gates
`check-spec-tokens.py --spec` over the spec.

### Non-goals
- Any edit to a CLOSED spec of this build: a correction to a closed unit is this new unit's.
- Any change to a verdict, a refusal line, the summary line or an exit status of the checker or of `--dispatch`.
- A row raised in any shrink-only registry.
- `tools/check-spec-tokens.py`, which TOOL-aPiecewiseGrade-5 writes concurrently.
- Building anything: the builder follows once the spec is committed.
