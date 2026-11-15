# Fix — TOOL-aTrimmedWait-10: a scoped run that skips check 12 dies on an unbound variable

**Serves:** research TOOL-aTrimmedWait-10

## The prompt

The main loop's pass-legs run over 42e99371c..8c95cdc73 reported the leg
`memory hygiene (the pass checks)` red, quoted:

> tools/memory-tree/check-memory-hygiene.sh: line 3771: c12_sel: unbound variable

The pass commit 49cdded06 hoisted the `P`-line count of the liveness line out of the
`if [ "$SCOPED" = 1 ]` branch, so every `--only` run whose selection leaves out check 12 reads
`c12_sel` before anything assigns it, and `set -u` ends the run. At base the count sat inside that
branch, so only a scoped run, which always assigns it, read it. The pass legs' own `--only` run is
the first observed case. The same run reported three record reds in the spec, which the main loop
cleared as records.

## The brief

### Goal
Restore every `--only` run's verdict and liveness line to what it was before 49cdded06, keeping the
no-fork count of S7.

### Items
1. The `P`-line count of the liveness line in `tools/memory-tree/check-memory-hygiene.sh` is computed
   only inside the scoped branch, where `c12_sel` is always assigned, so an unscoped `--only` run
   never reads it. No fork comes back, and the `var-pipe` count stays at its registry row.
2. Per [left-shift], an arm in `tools/memory-tree/check-memory-hygiene.test.sh`: an unscoped
   `--only` run of a check other than 12 exits 0, prints its `HYGIENE --only ... ran checks` line,
   and prints no `unbound variable`. It is RED at 49cdded06, which the main loop observes at the close.
3. The ledger row for AC9 records both runs: the scoped one it names and the unscoped one above.

### Acceptance
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2` exits 0 and prints no `unbound variable`.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --build aTrimmedWait` prints its liveness
  line over the build's spec count, as AC9 states.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No other line of the hygiene engine, and no change to the spec beyond its status header.

### Limitations
Copied from the build's brief: measurements on node a, one at a time.

### Reuse
The base's placement of the count, inside the scoped branch.
