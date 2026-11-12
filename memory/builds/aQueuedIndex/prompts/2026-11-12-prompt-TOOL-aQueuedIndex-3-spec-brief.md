**Serves:** research TOOL-aQueuedIndex-3

# Brief: spec TOOL-aQueuedIndex-3 — the closing review's round-2 minor: the busy timeout is pinned

## The prompt

> fix the tag index contention so bars don't flake

— owner, 2026-11-12. The closing review's round 2,
`memory/builds/aQueuedIndex/reviews/2026-11-12-review-TOOL-aQueuedIndex-2-diff-review-round2.md`, CONVERGED clean with one LOW,
which the kit promotes to a unit: `BUSY_TIMEOUT = 600` in `tools/playbook/tag_index.py` has no check that fails if it shrinks;
read the record whole first.

## The brief

### Goal

Write spec TOOL-aQueuedIndex-3, a micro-spec for one mechanical unit at order 3 that pins the busy timeout in a check the bar runs.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/foldaq3/2026-11-12-spec-TOOL-aQueuedIndex-3.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md` for a Tier-1 micro-spec; status line `DEFERRED · rev-1 ·
   2026-11-12 · node a · Tier-1 · base <HEAD short sha> · streams tooling · order 3`. Write no open fork: take the review's
   cheapest fix, and if a choice remains, mark it resolved in its own span.
2. **The fix.** The review's own: the `queued-writers` plant prints `busy timeout <ti.BUSY_TIMEOUT> s` and its row in
   `tools/playbook/adopt-playbook.sh` requires `busy timeout 600 s`, or the plant's green verdict requires the timeout at 600 or
   more. Pick the one that reds on a scratch copy with the value set to 60, and keep the plant's last line `both writers green`.
3. Criteria observe the check red with the value at 60 and green restored. The spec-token check grades a live spec's acceptance
   bullets word by word: no acceptance command whose words include an untracked path, no `path#symbol`, no suite as the
   observation, each backticked span on one line, every tripped leg on the gates line. Every new fact pinned, every new `path:line`
   blob-pinned, every minted function through the lexicon's `--suggest`.

### Acceptance

- Spec TOOL-aQueuedIndex-3 builds as written over HEAD, and its check has a staged break that reds it.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code. No edit outside the scratch copy. No change to the timeout's value or to the locking.
