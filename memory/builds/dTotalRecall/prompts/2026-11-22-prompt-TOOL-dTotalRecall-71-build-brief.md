**Serves:** journal TOOL-dTotalRecall-71
**Caused-by:** TOOL-dTotalRecall-71

# Build brief — TOOL-dTotalRecall-71, a spec-check unit the main loop closes

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 71's deliverable is the certification of unit 57's edge to unit 56
by a probe no shell quotes, seen to read both a 0 and a 1, after unit 72's pass (`35e956dc6`), and a deviation record
of unit 67 only where its AC1 certified an edge its tip did not hold.

## The brief

### Goal

Run §4's probe at this pass's base and record its four counts beside unit 67's recorded edge-row count.

### Items

1. The probe printed `tip 1`, `without 0`, `only 1` and `pass67 1` at `35e956dc6`, unit 67's pass being `56390bab8`;
   unit 67's AC1 ledger line recorded 1 for the edge row, so the counts agree, no deviation record is written and no
   builder is spawned.
2. The main loop writes the acceptance ledger and flips the unit CLOSED in the pass commit.

### Acceptance

AC1 holds at the pass base; AC2's ledger line names the `pass67` count and unit 67's recorded count.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec edit. No deviation record where the two counts agree.
