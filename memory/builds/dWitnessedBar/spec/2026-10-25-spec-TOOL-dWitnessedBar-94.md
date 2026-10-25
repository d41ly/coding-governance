# TOOL-dWitnessedBar-94 — unit 92's note check matches a label only where it opens a continuation line, so another note's prose cannot stand in for a missing note

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 49 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-94-deviation-941.md](../build/2026-10-25-build-TOOL-dWitnessedBar-94-deviation-941.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 91 and 92
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-91-spec-audit-round1.md`)
confirmed finding **id 5 at HIGH**, report item **H2**. Id 16 is the same unanchored-label defect,
found by the failure-envelope lens at MEDIUM, item M7. The two items share one fix. This unit makes
that fix, and `TOOL-dWitnessedBar-97` takes id 16 and adds the staged arms only its fix names.

`TOOL-dWitnessedBar-92` §4 "The note check" selects a note with
`awk -v k="TOOL-dWitnessedBar-$u $s([^0-9]|\$)"` and `$0 ~ k` (spec-92 line 281), which matches the
label anywhere on a line. 92 S3 and `TOOL-dWitnessedBar-91` S2 both say a note opens with its label,
and 92 S3 claims that no item's clause can pass on another item's line. A note whose prose cites
another item's label passes that item's row with that item's note absent.

This unit anchors the label at the start of a continuation line, two or more spaces in, as 92 S6
spells a note. It repairs `TOOL-dWitnessedBar-92` and builds one step after it (order 49).

## 2. Scope (IN)

- **S1** — id 5. The label anchored. In 92 §4's note check, the one fragment `k="TOOL-dWitnessedBar-`
  on spec-92 line 281 becomes `k="^  +TOOL-dWitnessedBar-`. The selector's pattern becomes
  `^  +TOOL-dWitnessedBar-$u $s([^0-9]|\$)`: two or more spaces, then the label, then a character
  that is not a digit, or the end of the line. A line opening `- ` never matches, so a label inside an
  answer line, or a note spelled as its own `- AC<n>` line, reads as no note. Nothing else in the
  script moves. `TOOL-dWitnessedBar-93`, `TOOL-dWitnessedBar-96` and `TOOL-dWitnessedBar-97` each
  rewrite other fragments of the same script, and none of them touches this one. Observed by AC1 and
  AC2.
- **S2** — id 5. 92 §4's limit superseded. Spec-92 lines 290-291 say a note spelled as its own
  `- AC<n>` line passes the placement test. Under S1 such a line prints `NO NOTE`, so 92 S6's exact
  answer count is no longer the only refusal of it. Observed by AC3.
- **S3** — Unit 92 answered. Unit 92's acceptance ledger records AC1's and AC2's outputs as a note
  under its `- AC3` answer. The note is a continuation line, two spaces in, opening with the label
  `TOOL-dWitnessedBar-94 S3` and carrying the backticked `NO NOTE 90 S1` on that one physical line.
  Observed by AC4.

## 3. Non-goals (OUT)

- Rewording the spec text of unit 92. Its §4 line 281 fragment and lines 290-291 are superseded by
  name here and answered in its ledger, as `TOOL-dWitnessedBar-92` §3 does for unit 90.
- The arms only id 16's fix names: a label inside an answer line, and a prose mention under a second
  answer beside a correct note. `TOOL-dWitnessedBar-97` takes them, and its replacement of 91 AC2's
  selector carries this anchor.
- The placement test (`TOOL-dWitnessedBar-93`), the token's value (`TOOL-dWitnessedBar-96`) and the
  ledgers the check reads (`TOOL-dWitnessedBar-97`).
- The report's left-shift text, a spec-lint rule that a ledger selector anchors its label. No clause
  of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-92` — §4's note check, whose selector pattern on line 281 S1 anchors, and §4's own-line limit on lines 290-291, which S2 supersedes (id 5)
- **hands-off** `TOOL-dWitnessedBar-97` — the arms only id 16's fix names, the label inside an answer line and a prose mention under a second answer, each graded through the anchored selector, and the composition of S1's pattern into the note check every close-time run uses (id 16, the medium-graded half of the shared fix)

## 4. Design

### Evidence

- Spec-92 line 281 builds the selector as `awk -v k="TOOL-dWitnessedBar-$u $s([^0-9]|\$)"` and tests
  `$0 ~ k`, with no anchor. `/^- /{o=$0}` sets the opener on each answer line. 92 S3 (line 68) and
  spec-91 S2 (line 51) say a note opens with its label, and 92 S6 (lines 93-95) says a note is a
  continuation line two spaces in.
- Probed on 2026-10-25 against a scratch 89 ledger whose only note under `- AC4` reads
  `  TOOL-dWitnessedBar-90 S9` then the backticked `for unread` and prose citing
  `TOOL-dWitnessedBar-90 S1`. Rows `90|S1|89|AC4|` and `90|S9|89|AC4|for unread` printed
  `NOTES OK 2`, exit 0, through spec-92's script. With S1's pattern they printed `NO NOTE 90 S1`,
  exit 1. They printed the same with the replacements of units 93, 96 and 97 applied beside S1's.
  With a continuation note `  TOOL-dWitnessedBar-90 S1` added under `- AC4`, both scripts printed
  `NOTES OK 2`.
- In awk, `-v` processes escape sequences in its value, and bash turns `\$` inside double quotes into
  `$`, so awk receives `([^0-9]|$)`. S1 adds no backslash.

### Inventory

Minted: the ledger note labelled `TOOL-dWitnessedBar-94 S3`. No function, constant, plant, flag or
file in the product. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

At the close, after every unit is terminal. The unit takes order 49, one above unit 92's 48, beside
units 93, 95 and 96. `TOOL-dWitnessedBar-97` S8 composes S1's pattern with the other fragments for
every note-check run at the close, and the note is written then.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **`^[[:space:]]+`, the report's spelling for id 5.** It admits one space or a tab, so 92 S6's "two
  spaces in" stays ungraded. `^  +` grades it and refuses nothing a correct build writes.
- **Strip prose after the label before matching.** A note's prose has no delimiter the check can
  trust, and the anchor already confines the label to the line's start.

## 5. Production-readiness checklist

- security — no new write path. The fixture ledgers sit under the run's scratch directory.
- perf / scale — the same awk pass per row.
- error / empty / loading states — a label that no continuation line opens with prints `NO NOTE`, as a
  missing note does.
- observability — a note is found only where its writer's label opens it, so a ledger line traces to
  one item.
- risks — a note written one space in, or with a tab, reads as no note; 92 S6 spells two spaces, and
  `memory/HYGIENE.md` "Acceptance ledger" joins any indented line to the answer above.
- testing — AC1 to AC3 by fixture at the close; AC4 by ledger.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch root holding one
  `memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89-*acceptance-ledger*` file whose only note
  under `- AC4` is a continuation line opening `TOOL-dWitnessedBar-90 S9`, holding the backticked
  `for unread` and prose citing `TOOL-dWitnessedBar-90 S1`, 92 §4's note check with S1's pattern, run
  from that root and fed `90|S1|89|AC4|` and `90|S9|89|AC4|for unread`, prints `NO NOTE 90 S1` and
  exits 1. Spec-92's unreplaced script prints `NOTES OK 2` and exits 0 on the same input.
  Red when: another note's prose citing an item's label stands in for that item's missing note.
  fixture: a scratch root under the run's scratch directory.
- **AC2** — In the same scratch root with a continuation line `  TOOL-dWitnessedBar-90 S1` added
  under `- AC4`, the check with S1's pattern prints `NOTES OK 2` and exits 0.
  Red when: the anchor refuses a note spelled two spaces in with its label first.
  fixture: a scratch root under the run's scratch directory.
- **AC3** — In a scratch root whose 89 ledger holds `- AC4 — TOOL-dWitnessedBar-90 S1` as its own
  answer line and no continuation note, the check with S1's pattern, fed `90|S1|89|AC4|`, prints
  `NO NOTE 90 S1` and exits 1.
  Red when: a note spelled as its own `- AC<n>` line passes the note check.
  fixture: a scratch root under the run's scratch directory.
- **AC4** — When 92 §4's note check with S1's pattern is fed `94|S3|92|AC3|NO NOTE 90 S1`, it prints
  `NOTES OK 1`.
  Red when: unit 92 AC3 is recorded against the unanchored selector.
  permission: the ledger is written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. AC1 to AC3 run by
fixture at the close. This unit adds no arm and moves none, so it declares no `New arm:` line, and
`TOOL-dWitnessedBar-88` S6's derivation still names unit 90 the floor's owner.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 92 is itself
  derived and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-90` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which unit takes id 16, the medium-graded item of the same defect?** Options: (a) this unit,
  so the shared fix and its arms land once; (b) the minors batch, as M4 places every MEDIUM. The
  task's disposal rule puts every MEDIUM in the batch, so (a) fails it; veto 1 discards it. Under (b)
  this unit makes the anchor and the batch adds id 16's arms, so nothing is fixed twice. RESOLVED
  (agent, 2026-10-25, delegated): (b), rung 3, the one survivor, the precedent
  `TOOL-dWitnessedBar-91` §8 F2 set.
  widens: none · relaxes: none
- **F3 — Which anchor?** Options: (a) `^[[:space:]]+`, the report's spelling for id 5; (b) `^  +`, the
  spelling for id 16. Both refuse the defect. (b) also grades 92 S6's "two spaces in". RESOLVED
  (agent, 2026-10-25, delegated): (b), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 91 and 92, id 5
  (HIGH, item H2; id 16 is its medium-graded item M7, batched into TOOL-dWitnessedBar-97).

## 10. Reuse audit

The seam is 92 §4's note check itself; S1 replaces one fragment of its selector and adds no reader.
`python tools/codebase-map/reuse_lookup.py "anchor a ledger label at the start of an indented continuation line"`
ranked `anchors`, `anchor_at`, `check_line` and `render_line`, none a reader of ledger continuation
lines, so no existing seam fits beyond 92's script and the acceptance ledger of `memory/HYGIENE.md`.

Recall terms used: `python tools/memory-recall/query.py "how is a ledger label matched only where a note opens a continuation line" --terms "ledger label anchored continuation line two spaces note prose mention answer line selector awk"`
