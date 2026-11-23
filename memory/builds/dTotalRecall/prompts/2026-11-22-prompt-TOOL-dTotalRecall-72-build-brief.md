**Serves:** journal TOOL-dTotalRecall-72
**Caused-by:** TOOL-dTotalRecall-72

# Build brief — TOOL-dTotalRecall-72, a spec-check unit the main loop closes

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 72's deliverable is the reading of unit 57's edge to unit 56 by a
probe no shell quotes, after unit 67's pass (`56390bab8`), and a write of the edge and its mirror only where it is absent.

## The brief

### Goal

Run §4's probe over specs 57 and 56 at this pass's base; write §4's edge and mirror bullets only where a count prints 0.

### Items

1. The probe printed 1 for the edge string over spec 57 and 1 for the mirror string over spec 56 at `d2f45193f`, so no
   spec is amended and no spec writer is spawned.
2. The main loop writes the acceptance ledger, naming both base counts on its AC1 line's first physical line, and flips
   the unit CLOSED in the pass commit.

### Acceptance

AC1 holds at the pass tip; AC3's ledger block names the base count of the edge string and of the mirror string.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec edit where the probe finds the edge present.
