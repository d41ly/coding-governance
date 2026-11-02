# Brief — dEasedEffort: the closing review's two lows, batched

**Serves:** research TOOL-dEasedEffort-2

## The brief

### Goal
The AC1 and AC3 lines of `TOOL-dEasedEffort-1`'s acceptance ledger each record an observation of the form their criterion names, and the class those two defects belong to says so. The review record is `memory/builds/dEasedEffort/reviews/2026-11-02-review-TOOL-dEasedEffort-1-closing-diff-review-round1.md`, items L1 and L2.

### Items
1. L1: the ledger's AC3 line stops claiming a command printed on a commit it could not have run at, and records the HEAD form observed at a named commit.
2. L2: the ledger's AC1 line records the spec's HEAD form observed at a named commit, and keeps the reason the staged form was used first.
3. `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` gains the form L1 found, a criterion graded on `HEAD` whose ledger line lands in the commit it observes, in its Symptom list, and L1 and L2 in its Where-it-bit section.

### Acceptance
1. Run from the worktree root, `git diff --name-only 2a6f3975 e74ef35e8 -- .claude` prints exactly the four agent-type paths, and the ledger's AC3 line names that commit and that output.
2. `git diff --numstat 2a6f3975 e74ef35e8 -- tools/roles/house/policy.toml` prints 4 added and 4 deleted, and the ledger's AC1 line names that commit and that output.
3. `grep -c` over the gotcha finds the new Symptom bullet and a `TOOL-dEasedEffort-1` line in Where it bit.
4. Every AC line of the ledger still opens with its backticked token before its first wrap, so hygiene check 23 still joins it.

### Gates
memory hygiene · spec tokens; then the full bar at the close.

### Non-goals
Any code, kit file or effort level. A re-review: the closing review's subject is terminal. `TOOL-dEasedEffort-1`'s spec, which is CLOSED and stays as written. The gotcha's count words beyond what the new bullet moves. A new gotcha class, or a machine gate: the class records that none fits.

### Limitations
Records only. No gate, suite or bar runs in the pass. Observations name fixed commits, not `HEAD`, so a later commit cannot move them.

### Reuse
The class `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` is the seam, and its Fix section already states the rule that a criterion found wrong at build time is amended where its spec allows. `TOOL-dWitnessedBar-88`'s fix brief is the record's shape.
