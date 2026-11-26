**Serves:** journal TOOL-dTotalRecall-67
**Caused-by:** TOOL-dTotalRecall-67

# Build brief — TOOL-dTotalRecall-67, a spec-check unit the main loop closes

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 67's deliverable is the probe of its §4 over the specs of units 55,
56 and 57 after unit 61's pass (`778edd3a3`), and an amendment only where the probe finds a gap.

## The brief

### Goal

Run §4's probe over each spec in its table at this pass's tip; amend a spec only where a string prints 0.

### Items

1. The probe printed 1 for each of the six strings and for `amended by TOOL-dTotalRecall-61` over each of the three
   specs at `778edd3a3`, so no spec is amended and no spec writer is spawned.
2. The main loop writes the acceptance ledger, naming the PINNED base counts of §4 and the tip counts, and flips the
   unit CLOSED in the pass commit.

### Acceptance

AC1 holds at the pass tip; AC3's ledger block names a base and a tip count for every string and §9 form.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec edit where the probe finds the text present.
