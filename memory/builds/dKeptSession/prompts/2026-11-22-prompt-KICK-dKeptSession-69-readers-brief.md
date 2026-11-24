**Serves:** research KICK-dKeptSession-69

# Brief — dKeptSession: KICK-dKeptSession-69's S5 Readers clause, answered over the built tree

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-69 is built and fully staged in the run worktree's in-progress merge. Both pre-commit hooks pass, except for
hygiene check 25 on the spec itself. S5's `**Readers:**` clause lists `write_shrink_list` and `UNNAMED_HEADER` as spelled in
`check_policy.py#run_reader_join`, but S6 removes exactly those spellings, so on the built tree no reader spells either.

### Items

1. Revise S5's Readers clause so it holds over the built tree. Either mark that half `READER NOT IN TREE`, with the
   reason that S6 removes the spellings, in the form check 25 accepts, or drop the two backticked names from it. Read
   check 25 in `tools/memory-tree/check-memory-hygiene.sh` for the accepted shapes.
2. Bump the spec to rev-3, with one revision-log line naming this brief by its file stem.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 25 --spec <path>` and `--only 12 --spec <path>` exit 0 over the
staged tree.

### Gates

The memory hygiene gate (`--only 12,25 --spec`); no other.

### Non-goals

No product code, no commit, no index render, no spec other than KICK-dKeptSession-69's, and no change to the staged merge
except the spec file, which you `git add` once you have edited it.
