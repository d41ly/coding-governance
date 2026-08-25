# TOOL-aBranchedMandate-12 — a blocked --close names the leg that blocked it

**Status:** CLOSED · rev-2 · 2026-08-18 · node a · Tier-1 · base 401416fa · streams tooling · ratified 2026-08-18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-18-build-TOOL-aBranchedMandate-12-measured-not-yet-rowed.md](../build/2026-08-18-build-TOOL-aBranchedMandate-12-measured-not-yet-rowed.md) | journal | TOOL-aBranchedMandate-13 |

<!-- /gen:spec-records -->

## 1. Goal

`dod_met`'s `gates-green` arm runs `$GATE_CMD >/dev/null 2>&1`, so a blocked `--close` reports THAT
the bar is red and never WHICH leg. Surface the bar's own output, the way `check_wiring` already
surfaces the declared wiring check's.

## 2. Scope (IN)

- **S1** — capture `$GATE_CMD`'s combined output and print it, indented, under the `fail 13` line
  when the item is unmet. On success nothing is printed: a green bar's output is noise.

## 3. Non-goals (OUT)

- Changing what `gates-green` DECIDES. Only what a refusal says.
- The other `dod_met` arms. `records-current` and `authorization-reachable` compute their answers
  in-process and have no discarded child output; this is the one arm that runs a project command.

## 4. Design

`TOOL-aBranchedMandate-2`'s S4 fixed exactly this shape one function away, for `WIRING_CHECK`, and
fixed only the call site its spec named. This is the sibling that grep would have found. The same
seam applies: capture into a local, emit indented, keep the refusal as the headline.

Measured cost of not having it: this build's own run paid three extra full-bar runs — 15-30 minutes
each under load — to recover a leg name the driver already had in hand.

## 5. Production-readiness checklist

- security — none. A refusal gains detail; nothing about what passes moves.
- error states — an EMPTY capture prints nothing rather than an empty indent block.
- testing — S1's arm, below. The existing check-13 arm uses `GATE_CMD="false"`, which prints
  nothing, so it passes whether the output is forwarded or discarded — the same blind spot unit 2's
  AC4 found in the wiring arm.
- rollback — revert; nothing persists.

## 6. Acceptance criteria

- **AC1** — When `--close` blocks on `gates-green` with a `GATE_CMD` whose failure carries a
  distinctive literal, that literal appears in the driver's output.
- **AC2** — When `--close` passes `gates-green`, the bar's output does NOT appear.

## 7. Gates

- `bash tools/unattended/unattended.test.sh` · `python tools/memory-tree/check-arms.py`
- `bash tools/run-gates.sh`

## 8. Open questions

none.

## 9. Revision log

- rev-2 · 2026-08-18 · BUILT and CLOSED, with one divergence from S1. S1 said print the bar's
  output; measured live, that was 95 lines under a single refusal, 68 of them `GATE ok` — burying
  the one line the unit exists to surface. The implementation FILTERS `GATE ok`/`GATE skip` and
  prints the rest, so a FAIL line, the summary and any stderr survive. AC1 observed live on this
  build's own close: `GATE FAIL  drift-audit records (exit 1)` appeared under the refusal, where
  recovering it previously cost a separate full-bar run.

- rev-1 · 2026-08-18 · from the closing review's fold record; the sibling unit 2's S4 did not grep for.

## 10. Reuse audit

The seam is `check_wiring` in the same file, which captures `$WIRING_CHECK` and emits it indented
under its own refusal. This unit is the third instance of that shape, not a new one.
