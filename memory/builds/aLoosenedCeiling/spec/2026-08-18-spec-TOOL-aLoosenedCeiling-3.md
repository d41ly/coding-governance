# TOOL-aLoosenedCeiling-3 — this repo's read-path ceiling, re-derived at the new headroom

**Status:** OPEN · rev-2 · 2026-08-18 · node a · Tier-1 · base 6382c564 · streams tooling

## 1. Goal

Move this repo's `READ_PATH_CEILING` from 86476 to 111994 — the measured read path plus the
headroom default unit 1 establishes — and record the movement beside the number, in the register
the key's existing comment block already uses.

## 2. Scope (IN)

- **S1** — `.memory-tree.conf` declares the new ceiling.
- **S2** — the comment block above it gains the fifth movement's entry: what was measured, what the
  headroom is, why the headroom convention itself moved, and that no read-path member was trimmed
  to get here. The block is a running record and existing entries are not rewritten.
- **S3** — the conf declares `READ_PATH_HEADROOM` explicitly at the new default, so the arithmetic
  in S2 is reproducible from the file rather than from the kit's built-in. The engine that reads
  that key is unit 1, so between this unit landing and that one the declaration is INERT, and the
  comment says so in as many words. Unit 4 refuses an inert declaration in the adopter repo; the
  difference is that there the engine is seventeen releases away and here it is one unit away, and
  a window a spec names is not the same defect as a window nobody records.
- **S4** — the live carriers of the OLD ceiling move in the same commit as the conf. There is one:
  a backlog row that restates the ceiling and a read-path measurement, both stale. Dated records
  under the build folders are immutable history and stay as they are.
- **S5** — the SECOND wall this build can hit is named. `memory/backlog/TOOL.md` sits a few hundred
  bytes under check 6's row-document cap, so a backlog row minted by this build reds a different
  check than the one this unit moves. Naming the disposition is in scope; turning check 6's knob is
  not, and unit 2 declines it for the same reason.

## 3. Non-goals (OUT)

- No read-path member is trimmed, split or rotated. This is a budget movement, not a curation pass,
  and the number was derived without assuming any trim.
- No per-class cap is declared or moved. That knob is unit 2's and turning it is outside the ask.
- `READ_PATH_WAIVER` stays empty. Every member is still capped by check 6.
- No other pin in this conf moves.

## 4. Design

Measured at this unit's base: 86394 B over six members, against a ceiling of 86476. Eighty-two
bytes of headroom, which is less than one decision row. The build that contains this unit appends
rows to `memory/DECISIONS.md`, and that file is a read-path member, so the ceiling has to move
before the next FULL hygiene run after such an append. Not before the commit: the pre-commit leg
runs the staged fast path, which skips the delegation check 16 lives behind, so the deadline is
the next unstaged run and not the commit hook.

**Ordering consequence, and the reason this unit is sequenced first among the pin movements:** the
raise lands in or before the commit that first grows a read-path member. A run that appends the
decision row first and raises afterwards spends a red gate to learn something already known here.

New value: 86394 measured plus 25600 headroom is 111994. The headroom convention moved from 20480
in unit 1, and the two halves are recorded together so a later reader is not left inferring which
number changed.

**Measured at the BASE, not at the close.** This build grows the read path itself — a generated
index row for its own build folder, then its decision rows — and a ceiling sized from the closing
measurement would hand the build a budget shaped around what it had already spent. The base
measurement is the honest input, and this build's own growth spends from the headroom, which is
what headroom is for. The eighty-two bytes were in fact consumed by the generated index row before
this unit's edit landed, so the ordering claim above is an observation and not a prediction.

This repo's read path is six files, four of them guides the charter names as binding. The largest
is 25036 B. The previous headroom could not absorb one more member of that class, and this build
did not create that situation — it was created by two binding documents growing in one merge, which
the conf's own comment block already records as the third movement.

## 5. Production-readiness checklist

- risks — the honest one: a ceiling raised is a ratchet loosened, and the check only ever measures
  against what it is told. The mitigation is the one this repo already uses, which is that the
  number carries its derivation in the comment above it, so a raise that cannot state its
  measurement is visible as such in review.
- testing + left-shift gates — check 16 itself is the test; it runs on the bar.
- migration / rollback — a single declared value; rollback is restoring the previous number, which
  reds only if the corpus has since grown past it.
- everything else — N/A, this unit changes one declaration and its comment.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/corpus_ids.py --report` runs on this repo, the read-path
  total is under the declared 111994 with at least 20000 B of margin.
- **AC2** — When `.memory-tree.conf` is read, its comment block states the base measurement 86394
  and the headroom 25600, and those two sum to the declared `READ_PATH_CEILING`. This is an
  identity against the recorded base, NOT a comparison with `--measure`: that tool re-measures the
  live tree, which section 4 says will keep growing, so the two numbers agree only at the instant
  of the base measurement and the first draft of this criterion was false the day it was written.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs after this build appends its
  decision rows, check 16 is silent.
- **AC4** — When `grep -rn 86476 memory/backlog/ .memory-tree.conf` runs, no live carrier still
  states the old ceiling as current.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `python tools/memory-tree/corpus_ids.py
--report` · `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded spec-audit round 1. AC2 was the audit's first blocker: it demanded
  `--measure` print the conf's value while section 4 pins from the base and `--measure` re-measures
  live, so the criterion was false when the change was right — measured 107323 against a declared
  111994. Restated as the at-base identity. S3 gained the inert-window statement the conf now also
  carries, S4 the stale-carrier obligation unit 1's rev-2 handed here, and S5 the check-6 wall no
  spec in the set had named. AC1 states its margin as a number rather than as a judgement.

## 10. Reuse audit

Satisfied for the set by unit 1's section 10. This unit writes no code and extends no seam; it
moves one declared value in the file the set's recall probe identified as the carrier for exactly
this kind of movement.
