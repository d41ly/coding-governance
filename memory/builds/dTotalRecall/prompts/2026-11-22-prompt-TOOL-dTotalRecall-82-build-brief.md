**Serves:** journal TOOL-dTotalRecall-82
**Caused-by:** TOOL-dTotalRecall-82

# Build brief — TOOL-dTotalRecall-82, a history-read unit the main loop closes

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 82's deliverable is the re-read of unit 71's `pass67` count at unit
67's pass commit through unit 81's guarded read (`7e151e666`), and the deviation record of unit 67 its decision table
owes, written once.

## The brief

### Goal

Run §4's re-read at this pass's base and apply §4's decision table to it.

### Items

1. At `7e151e666` `pass_of 67` resolved `56390bab8` and `read_at` printed that sha with count 1 for the edge string
   over spec 57; unit 67's AC1 ledger line recorded 1 for the edge row, so the table owes no record and no builder is
   spawned.
2. The main loop writes the acceptance ledger and flips the unit CLOSED in the pass commit.

### Acceptance

AC1 holds at the pass base; AC2's ledger line names S1's count, unit 71's `pass67` and unit 67's recorded figure.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec edit. No deviation record where the table owes none.
