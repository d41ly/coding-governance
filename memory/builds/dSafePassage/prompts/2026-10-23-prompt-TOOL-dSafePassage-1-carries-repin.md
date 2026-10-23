**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-11 TOOL-dSafePassage-13

# Brief — dSafePassage: three Carries lines pinned to a clause hash the as-built view has moved

## The prompt

> GATE FAIL  spec tokens (a spec's own names resolve) — carries join, 3 unwaived hits:
> TOOL-dSafePassage-1 pins cl-dClosedLoop-0018@ed08a364, and the clause's text in the view hashes d4cade33;
> TOOL-dSafePassage-11 pins cl-dClosedLoop-0028@032ca791, the view hashes dae8abad;
> TOOL-dSafePassage-13 pins cl-dClosedLoop-0030@274077d4, the view hashes e7612082.

— the merge bar `unattended.sh --close dSafePassage` ran on the prepared merge, leg attributed OWN

## The brief

### Goal

Pin each of the three specs to its clause's hash in the as-built view, which this spec run's own deviation
records (11, 31, 51 and 52) moved, so the carries join of `tools/check-spec-tokens.py` reads each clause carried
whole at its current hash.

### Items

1. In `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md`, change the binding line
   `**Carries:** cl-dClosedLoop-0018@ed08a364 whole` to `**Carries:** cl-dClosedLoop-0018@d4cade33 whole`.
2. In `…-TOOL-dSafePassage-11.md`, `cl-dClosedLoop-0028@032ca791` becomes `cl-dClosedLoop-0028@dae8abad`.
3. In `…-TOOL-dSafePassage-13.md`, `cl-dClosedLoop-0030@274077d4` becomes `cl-dClosedLoop-0030@e7612082`.
4. Confirm each new hash against the view,
   `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, through the instrument's
   own reader rather than by eye. If the view disagrees with a hash above, pin the view's and say so.
5. Bump each spec's rev by one, with a §9 line naming the re-pin and the deviation record that moved the clause.
6. Every token the amended clause text carries must still appear in the spec in backticks. If the amended text
   (each record's `**After:**`) names a token the spec lacks, add it where the spec already discusses that subject.

### Acceptance

`python tools/check-spec-tokens.py` reports no `carries` hit for these three specs, and
`python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py --build dSafePassage --exit`
exits 0. Both are read-only checks of the spec tree, so you may run them.

### Gates

Only those two reads.

### Non-goals

No other change, no record edited, nothing staged or committed. The worktree's HEAD is a prepared landing merge:
do not commit, reset, merge or check out anything. Write nothing outside the three specs.

### Limitations

This is an unattended run, so nobody will answer a question.

### Reuse

The binding-line grammar in `tools/memory-tree/design_lib.py`.
