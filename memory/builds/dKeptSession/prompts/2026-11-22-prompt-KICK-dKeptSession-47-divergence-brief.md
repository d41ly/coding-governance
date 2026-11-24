**Serves:** research KICK-dKeptSession-47

# Brief — dKeptSession: KICK-dKeptSession-47's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-47's builder (run `wf_3f88cb25-dcc`) stopped before its first edit and returned a DIVERGENCE: section 5
says the user docs are none beyond unit 30 S5's paragraph, "which names no compaction rule", but the `context` paragraph
KICK-dKeptSession-30 landed in `tools/runlog/README.md` does name it: the observation is the largest main usage sum on the
model and the largest compaction `preTokens` across the newest `CONTEXT_WINDOW_SCAN` main transcripts. That is the
unfiltered fold S1 removes, so the sentence becomes false the moment S1 lands, and the README is neither in Files touched
nor in the write set. Every other claim the builder probed held at its base (e8b22050). Revise the spec to the ruling
below.

### Items

1. F-readme: resolved by the main loop: the README's compaction clause is rewritten in this unit to count only a
   compaction whose newest earlier main usage in the same transcript is on that model. Correct section 5's user-docs
   line, add `tools/runlog/README.md` to Files touched tied to S1, and extend a criterion, or add one, that observes the
   rewritten clause and the old unfiltered wording gone.
2. Name the `tools/runlog/extract.py#derive_context_window` docstring, which also states the unfiltered rule, as
   rewritten under S1 (it is already in the write set).
3. Bump the spec to rev-6, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`,
   pin every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep
   within the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-47` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-47's. Read files; edit only the
spec, in the run worktree.
