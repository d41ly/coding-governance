# TOOL-cBriefedPilot-22 — check 16's join, extended to the protocol's own two tables

**Status:** CLOSED · rev-2 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

Join the protocol's §3 phase list and §4 Definition-of-Done table to `PHASES_CORE` and `DOD_CORE`,
which no leg reads today. The gap is pre-existing; this build is what makes it worse, by adding two
rows to the second of those tables. The owner resolved P5 to fix it here.

## 2. Scope (IN)

- **S1** — check 16 gains arm D: every `PHASES_CORE` member appears in the protocol's §3 run-order
  list, and every member of that list is in `PHASES_CORE`. Both directions.
- **S2** — arm E: the same join between `DOD_CORE`'s item NAMES and the first cell of every §4 table
  row.
- **S3** — one side is read, the SHIPPED `tools/unattended/PROTOCOL.template.md`. Check 10 already
  asserts the installed copy equals it after prefix substitution, so reading both would be a second
  answer to a question that leg owns.
- **S4** — each locator's EMPTY result is a NAMED refusal, exactly as arm A's is, because a prose
  anchor that gets reworded otherwise empties the comparison silently.
- **S5** — arms in `tools/unattended/check-unattended.test.sh` for both directions of both arms plus
  both empty-extraction refusals; `ARMS_FLOORS` raised in the same commit.

## 3. Non-goals (OUT)

- **A new check number.** These are arms of check 16, whose join shape they are. The leg's check
  count does not move, so the charter's gate-suite bullet gains a clause and not a number.
- **A marker pair in the protocol.** The kit's own precedent prefers a marker over a structural
  locator, because a renamed heading silently empties a comparison. S4 buys that property for zero
  edits to a document unit 18 is already rewriting, and buys it in the form this leg already uses
  three times.
- **Joining the CHECKER column of §4.** Measured against source and refused in §4 below.
- **§7's verb list and §8's conf-key table.** Both are joinable and neither is what this build
  moves. A backlog row, not scope creep into the unit the owner asked for.
- **Rewriting the tables.** Unit 18 writes the two new DoD rows and the sentence counting them; this
  unit only refuses when they disagree with the driver.

## 4. Design

### The locators, measured in this worktree

The §3 list is the paragraph after the line ending `in run order:`, and it wraps across two lines.
Collecting the backticked all-caps tokens from that paragraph yields exactly the ten core phases, in
order. A whole-file scan does NOT work and the measurement says why: the same pattern over the entire
document also returns `LANDER`, which is a conf key, so the paragraph scope is load-bearing rather
than tidy.

The §4 rows are the lines matching a leading pipe, a backticked lowercase-hyphen token, and a closing
pipe. That selects exactly the DoD rows and nothing else: §8's key table uses uppercase-with-underscore
names and §7's verbs are list items, not table rows. The count is six as the tree stands today and
EIGHT once unit 18 lands, which this unit follows — a builder validating the selector against a fixed
number would read the growth as a broken locator.

### Why item names only, and not the checker column

`DOD_CORE` carries `<item>:<checker>` with `machine` and `agent`. The protocol's checker cells read
`machine`, `machine, PRE-LANDING` and `agent-attested` — measured today, three cells do not equal the
token the constant holds, one `machine, PRE-LANDING` and two `agent-attested`, and those spellings
exist to say something true that the constant has no room for. Joining the column would need a normalisation table, which is a third spelling of a two-value
fact. The item NAME is the thing that must not drift, and it is the thing joined.

### Ordering

This unit lands after unit 18 and not before. Unit 18 writes `build-complete` and
`closing-review-recorded` into the §4 table; unit 12 has already put them in `DOD_CORE` by way of
units 7 and 8, so arm E landing first would red on two rows the protocol does not yet carry, on a
leg that has no `guard` in `tools/gate-legs.json` and therefore runs on every commit's diff-scoped
bar.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` (arms D and E inside check 16) ·
`tools/unattended/check-unattended.test.sh` · `.memory-tree.conf` (`ARMS_FLOORS`) · `AGENTS.md` (one
clause in the gate-suite bullet).

## 5. Production-readiness checklist

- security · a11y · i18n — N/A.
- perf / scale — two awk passes over one file already opened by check 10.
- error / empty / loading states — the two empty-extraction refusals; the protocol pair's own absence
  is check 10's branch and is not re-asked here.
- observability — each direction prints the tokens that failed to match.
- risks — the locators depend on prose anchors. S4 turns a reworded anchor into a refusal rather than
  a silent pass, which is the only mitigation that does not require a marker.
- testing + left-shift gates — arms for both directions of both joins, each observed RED before its
  branch is written.
- migration / rollback — the arms are green against the tree as it stands today, measured, and stay
  green through unit 18 because that unit writes both rows.
- user docs — N/A, a gate.

## 6. Acceptance criteria

- **AC1** — When a phase is added to `PHASES_CORE` and §3's list is not touched, the leg reds naming
  the missing token; and the reverse.
- **AC2** — When a DoD item is added to `DOD_CORE` and §4's table is not touched, the leg reds naming
  the missing item; and the reverse.
- **AC3** — When §3's `in run order:` anchor is reworded so the list cannot be located, the leg reds
  with the empty-extraction refusal rather than passing.
- **AC4** — Against the tree as unit 18 leaves it, both arms are silent and the fixture's green
  control still exits 0 and prints nothing.

## 7. Gates

`unattended gate selftest` · `unattended kit gate` · `harness arms` · the full bar.

**No leg and no check is added** — these are arms of check 16. `tools/gate-legs.json`, the dossier's
`gate-legs` claim, the codebase-map re-render and the leg's own check count are all untouched; the
charter's gate-suite bullet gains a clause naming what the join now covers.

## 8. Open questions

none — P5 was resolved by the owner on 2026-08-14 to fix this in the build, and the two design
choices this unit had to make (one side of the pair, item names only) are settled in §4 against
measured source.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft. Not in the design pass's twenty-unit decomposition: this unit
  exists because the owner resolved P5 into scope on 2026-08-14, and it follows unit 18 because it
  joins against the two rows that unit writes.
- rev-2 · 2026-08-14 · §4's two locator figures qualified by WHEN they were measured. Both were taken
  against today's tree — six DoD rows, three off-token checker cells — but this unit lands after unit
  18 adds two rows, so a builder checking the selector against the printed six would read a correct
  eight as a broken locator. The row count is now stated for both trees and the checker figure names
  the three cells instead of a fraction that moves.

## 10. Reuse audit

- **Check 16 arm A, unit 12** — the seam, and the whole point of the unit. The join shape, the
  both-directions rule and the empty-extraction refusal are arm A's; arms D and E point them at two
  more tables rather than building a second comparator.
- **`core_of()`** — already reads `PHASES_CORE` and `DOD_CORE` out of the driver for checks 2 and 3.
  Both values are in hand before check 16 runs, so neither arm re-reads the driver.
- **Check 10's `SHIP`/`LIVEDOC` pair** — the reason one side suffices. It already normalises the
  install prefix and byte-compares, and it reds when either half is missing.

Recall terms used: unattended protocol phase vocabulary definition of done core set join both
directions leg check driver constant table row locator empty population refusal shrink-only floor.
