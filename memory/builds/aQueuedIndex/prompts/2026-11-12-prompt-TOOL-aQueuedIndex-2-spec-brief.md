**Serves:** research TOOL-aQueuedIndex-2

# Brief: spec TOOL-aQueuedIndex-2 — the closing review's round-1 findings on the queued-writers plant

## The prompt

> fix the tag index contention so bars don't flake

— owner, 2026-11-12. TOOL-aQueuedIndex-1 fixed the contention: five races on a fresh index all exited green on both writers,
and the new plant over BASE's index module reds on the original refusal. The closing review's round 1,
`memory/builds/aQueuedIndex/reviews/2026-11-12-review-TOOL-aQueuedIndex-1-diff-review-round1.md`, is BLOCKED on the plant's
own arms; read it whole first.

## The brief

### Goal

Write spec TOOL-aQueuedIndex-2, a micro-spec for one mechanical fix unit at order 2 that makes the plant's arms able to fail
on what they claim, per the review's three items.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/foldaq2/2026-11-12-spec-TOOL-aQueuedIndex-2.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md` for a Tier-1 micro-spec; status line `DEFERRED · rev-1 ·
   2026-11-12 · node a · Tier-1 · base <HEAD short sha> · streams tooling · order 2`. Mark any fork you resolve in its own span.
2. **B1, the blocker.** The plant grades writer two only on its parsed count, which the blob-parse cache keeps at 0 whether or
   not the waiter re-reads `tree_built` under the lock; the main loop observed the plant exit 0 with the re-read deleted. Grade
   the waiter on something a rebuild changes, as the review's fix suggests (its skipped and run counters, or an unchanged
   `tree_built` timestamp), and restate TOOL-aQueuedIndex-1's AC2 through this unit's own criterion rather than editing the
   CLOSED spec.
3. **M1.** No arm fails when the overlay or the collection write block loses its `BEGIN IMMEDIATE`. Give each a check that reds
   on the loss, or say why one plant covers both.
4. **L1.** The plant prints `both writers green` before its checks run; print it only once they pass.
5. Criteria observe each arm red on its staged break and green after, the deleted re-read among them. The spec-token check grades
   a live spec's acceptance bullets word by word: no acceptance command whose words include an untracked path, no `path#symbol`,
   no suite as the observation, each backticked span on one line, every tripped leg on the gates line. Every new fact pinned,
   every new `path:line` blob-pinned, every minted function through the lexicon's `--suggest`.

### Acceptance

- Spec TOOL-aQueuedIndex-2 builds as written over HEAD, and each of its arms has a staged break that reds it.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code. No edit outside the scratch copy. No change to the locking TOOL-aQueuedIndex-1 shipped.
