# Brief — aShelvedLeg: the closing review's round-1 blocker

**Serves:** research TOOL-aShelvedLeg-1

## The brief

### Goal
The closing review of b904a0f9..3203e2ac4 confirmed one BLOCKER, finding 3 in `memory/builds/aShelvedLeg/reviews/2026-11-10-review-TOOL-aShelvedLeg-1-closing-diff-round1.md`. The new `unattended kit gate` row in `tools/run-gates/selftest-budgets.txt` resolves to `bash tools/unattended/check-unattended.sh`, which lies under the evidence header's `# pooled-kit: {prefix}/unattended`. That script prints no line matching `SWEEP_TRAILER_RX`, and the row is not declared `# no-trailer:`. So the trailer arm of `run-selftests.sh --check` reds on it, and with it the bar leg `every held leg is budgeted, every budget row resolves`.

### Items
1. `tools/run-gates/selftest-pooled-evidence.txt` gains `# no-trailer: unattended kit gate` beside the two existing `no-trailer:` declarations. The prose above them grows by one clause, naming `check-unattended.sh` as a checker that exits on its status with no `PASS (` line. Nothing else in the file moves, and no reading row is written.

### Acceptance
`grep -c '^# no-trailer: unattended kit gate$' tools/run-gates/selftest-pooled-evidence.txt` prints 1. The main loop re-observes the leg `every held leg is budgeted, every budget row resolves` at the close.

### Gates
every held leg is budgeted, every budget row resolves · memory hygiene · routed commits name a specced unit.

### Non-goals
The five LOW findings of the same round, which the exit promotes into one unit. A pooled reading row for the leg, which only `--pooled --calibrate` writes. Any other file.

### Limitations
A role agent runs no runner. The `--check` observation is the main loop's.

### Reuse
The `no-trailer:` declarations for `unattended brief-recorded selftest` and `unattended pass-order selftest` are the shape.
