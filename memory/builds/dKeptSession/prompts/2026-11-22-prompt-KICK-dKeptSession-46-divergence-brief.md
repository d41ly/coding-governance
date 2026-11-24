**Serves:** research KICK-dKeptSession-46

# Brief — dKeptSession: KICK-dKeptSession-46's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-46's builder (run `wf_1cb1e731-5b6`) stopped before its first edit and returned a DIVERGENCE with
three findings against the tree after KICK-dKeptSession-14, -30, -9 and -45 landed. Revise the spec to the main loop's
rulings below; each adopts the builder's proposed fix.

### Items

1. F-readme: `tools/runlog/README.md`'s context paragraph says `derive_context_fill(ev, window=None)` falls back to the
   window derived under the harness's default projects root, which S1 removes, and section 5's "no page names the
   reader's signature" misses the kit README. Ruling: the README sentence is rewritten to the new signature,
   `derive_context_fill(ev, *, window=None, root=None)`, which requires one of the two; add `tools/runlog/README.md` to
   Files touched tied to S1, correct section 5, and extend a criterion, or add one, that observes the sentence.
2. F-third-caller: section 4's "its only two callers" misses the liveness check in
   `tools/runlog/selftest.py#test_extract_context_fill`, which calls `derive_context_fill` with no window and no root
   and would raise under S1. Ruling: it is re-spelt with the case's own root (`root=projects`); that root observes at
   most 180000, which lands on the 200000 rung, so its pinned 0.95 holds. Name it in section 2 and section 4, and have
   S4 or the ledger answer unit 30 S2's default-root wording for that check.
3. F-orient-cache: S2 says `tools/runlog/extract.py#measure_orient_tree` computes each row's context as
   `derive_context_fill(ev, root=root)`, but the built code keeps one window per model per run, derived by
   `derive_context_window(model)` and passed by position. Ruling: S2 keeps the cache: its `derive_context_window` call
   takes the function's own `root`, and the fill passes that window by name as `window=`, which gives the same share
   without re-deriving per row; how often the window is derived stays section 3's non-goal for KICK-dKeptSession-56.
4. Bump the spec to rev-6, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`,
   pin every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep
   within the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-46` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-46's. Read files; edit only the
spec, in the run worktree.
