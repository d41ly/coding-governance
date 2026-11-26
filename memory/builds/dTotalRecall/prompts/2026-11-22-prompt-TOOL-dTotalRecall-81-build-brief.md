**Serves:** journal TOOL-dTotalRecall-81
**Caused-by:** TOOL-dTotalRecall-81

# Build brief — TOOL-dTotalRecall-81, a history-read unit the main loop closes

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 81's deliverable is the guarded revision read of its §4, `pass_of`
and `read_at`, seen to refuse each empty answer, and its first application to unit 71's PASS67, after unit 71's pass
(`5e004ad39`).

## The brief

### Goal

Run §4's read at this pass's base over AC1's inputs and S3's comparison, and write a deviation record of unit 71 only
where the driver's and the recipe's resolutions of unit 67's pass differ.

### Items

1. At `5e004ad39` the read printed the pinned counts over specs 59 and 62, a red line and rc 1 for each refused input,
   and `pass_of 10` resolved `d735e47b9`; S3's driver and recipe lines both named `56390bab8`, so no deviation record
   is written and no builder is spawned.
2. The main loop writes the acceptance ledger and flips the unit CLOSED in the pass commit.

### Acceptance

AC1 holds at the pass base; AC2's ledger line names the driver and recipe lines.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec edit. No deviation record where the two resolutions agree.
