# TOOL-dWitnessedBar-93 — unit 92's note check places a row when one selected note sits under its answer, so one label and token answering two criteria passes

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 49 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-93-deviation-931.md](../build/2026-10-25-build-TOOL-dWitnessedBar-93-deviation-931.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 91 and 92
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-91-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. No other id shares the item.

`TOOL-dWitnessedBar-92` §4 "The note check" prints `MISPLACED` when any note it selects for a row
sits under another answer (spec-92 line 283, `grep -qvE ... && {`). Four of its note-table rows share
one label and one token across two answers of one ledger: `92|S4|88|AC6` with `92|S4|88|AC18`, and
`92|S4|89|AC9` with `92|S4|89|AC12` (spec-92 lines 256-259). A correct build writes a note under each
answer, so the check selects both openers and prints `MISPLACED` for both rows. 92 AC4's `NOTES OK 5`
and AC12's `NOTES OK 29` cannot print on a correct build.

This unit replaces the placement test so a row passes when at least one note it selects sits under
the row's answer, and reds only when none does. It repairs `TOOL-dWitnessedBar-92` and builds one
step after it (order 49).

## 2. Scope (IN)

- **S1** — id 1. The placement test, inverted. In 92 §4's note check, the one fragment
  `grep -qvE "^- (\*\*)?$a[^0-9]" && {` on spec-92 line 283 becomes
  `grep -qE "^- (\*\*)?$a[^0-9]" || {`. The line then reads:

  ```bash
  printf '%s\n' "$o" | grep -qE "^- (\*\*)?$a[^0-9]" || { echo "MISPLACED $u $s ${t:-}"; bad=1; continue; }
  ```

  A row prints `MISPLACED` only when no opener the selector printed is the row's `- <answer>` line.
  Nothing else in the script moves. `TOOL-dWitnessedBar-94`, `TOOL-dWitnessedBar-96` and
  `TOOL-dWitnessedBar-97` each rewrite other fragments of the same script, and none of them touches
  this line. Observed by AC1 and AC2.
- **S2** — id 1. 92 §5's risk line corrected. Spec-92 lines 383-385 claim that "a row whose token two
  notes carry passes on either". Under S1 that claim holds, so this unit's §5 restates it as the risk
  that stands: a stray copy of a correctly placed note under a second answer is not refused by the
  note check. Observed by AC1.
- **S3** — Unit 92 answered. Unit 92's acceptance ledger records AC1's and AC2's outputs as a note
  under its `- AC4` answer. The note is a continuation line, two spaces in, opening with the label
  `TOOL-dWitnessedBar-93 S3` and carrying the backticked `NOTES OK 2` on that one physical line.
  Observed by AC3.

## 3. Non-goals (OUT)

- Rewording the spec text of unit 92. Its §4 line 283 and its §5 risk line are superseded by name
  here and answered in its ledger, as `TOOL-dWitnessedBar-92` §3 does for unit 90.
- A token unique to each answer, the report's second way. §4 "Alternatives rejected" says why.
- The selector's label anchor (`TOOL-dWitnessedBar-94`), the token's value (`TOOL-dWitnessedBar-96`)
  and the ledgers the check reads (`TOOL-dWitnessedBar-97`).
- The report's left-shift text, a spec-lint rule running every note-check row over a fixture ledger
  holding all of the table's notes. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-92` — §4's note check, whose placement test on line 283 S1 inverts, its note table's four shared-label `92|S4` rows, and §5's risk line, which S2 restates (id 1)
- **hands-off** `TOOL-dWitnessedBar-97` — S1's placement line, one of the fragments the batch composes into the note check every close-time run uses, which its S8 states once

## 4. Design

### Evidence

- Spec-92 lines 274-288 hold the note check. Line 281's awk prints the opener `o` of every line that
  carries the row's label and token, so a label and token written under two answers print two
  openers. Line 283 prints `MISPLACED` when any printed opener fails `^- (\*\*)?$a[^0-9]`.
- Probed on 2026-10-25 against a scratch 88 ledger holding `- AC6` and `- AC18`, each followed by the
  continuation note `TOOL-dWitnessedBar-92 S4` with the backticked `resolve_python: python3 exit 0`. Rows
  `92|S4|88|AC6|resolve_python:` and `92|S4|88|AC18|resolve_python:` printed
  `MISPLACED 92 S4 resolve_python:` twice, exit 1, through spec-92's script. With S1's line it
  printed `NOTES OK 2`, exit 0. It printed the same with the replacements of units 94, 96 and 97
  applied beside S1's. With the note under `- AC18` removed, both scripts printed
  `MISPLACED 92 S4 resolve_python:` once for the AC18 row, so the placement test still reds.
- `memory/HYGIENE.md` "Acceptance ledger" (`:686`) gives one answer line per criterion inside an
  `**Evidences:**` block, so an opener the selector prints is one answer line.

### Inventory

Minted: the ledger note labelled `TOOL-dWitnessedBar-93 S3`. No function, constant, plant, flag or
file in the product. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

At the close, after every unit is terminal. The unit takes order 49, one above unit 92's 48, beside
units 94, 95 and 96. `TOOL-dWitnessedBar-97` S8 composes S1's line with the other fragments for
every note-check run at the close, and the note is written then.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **A token unique to each answer, such as `resolve_python: (88 AC6)`.** Each pair of rows is made
  unique by a spelling chosen one at a time, so the next item that writes one note under two answers
  reopens the defect. S1 states what a row asks, that its note sits under its answer, for every row
  at once. This is the reason 92 §8 F2 gave for a label over a per-item token.
- **Keep the strict test and drop one note of each pair.** That undoes 92 S4's record of each
  derivation run under the criterion that ran it.

## 5. Production-readiness checklist

- security — no new write path. The fixture ledgers sit under the run's scratch directory.
- perf / scale — one `grep -q` per row, as before.
- error / empty / loading states — an empty selection still prints `NO NOTE`, from spec-92 line 282,
  which S1 leaves in place.
- observability — `MISPLACED` now means that no selected note sits under the row's answer.
- risks — a stray copy of a correctly placed note under a second answer passes the note check. 92
  S6's exact count of each answer refuses a stray copy spelled as its own `- AC<n>` line.
- testing — AC1 and AC2 by fixture at the close; AC3 by ledger.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch root holding one
  `memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88-*acceptance-ledger*` file, where `- AC6`
  and `- AC18` are each followed by a continuation line, two spaces in, opening with the label
  `TOOL-dWitnessedBar-92 S4` and holding the backticked `resolve_python: python3 exit 0`,
  92 §4's note check with S1's line, run from that root and fed `92|S4|88|AC6|resolve_python:` and
  `92|S4|88|AC18|resolve_python:`, prints `NOTES OK 2` and exits 0. Spec-92's unreplaced script prints
  `MISPLACED 92 S4 resolve_python:` twice and exits 1 on the same input.
  Red when: a correct note under each of two answers sharing a label and token prints `MISPLACED`.
  fixture: a scratch root under the run's scratch directory.
- **AC2** — In the same scratch root with the note under `- AC18` removed, the check with S1's line
  prints `MISPLACED 92 S4 resolve_python:` once and exits 1.
  Red when: the inverted test passes a row whose answer carries no note of its label and token.
  fixture: a scratch root under the run's scratch directory.
- **AC3** — When 92 §4's note check with S1's line is fed `93|S3|92|AC4|NOTES OK 2`, it prints
  `NOTES OK 1`.
  Red when: unit 92 AC4 is recorded against the strict placement test.
  permission: the ledger is written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. AC1 and AC2 run by
fixture at the close. This unit adds no arm and moves none, so it declares no `New arm:` line, and
`TOOL-dWitnessedBar-88` S6's derivation still names unit 90 the floor's owner.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 92 is itself
  derived and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-90` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which of the report's two sound fixes closes id 1?** Options: (a) a row passes when at least
  one selected note sits under its answer; (b) a token unique to each answer. Both survive the
  vetoes. (a) holds for every row by construction, and (b) holds only while each writer picks a
  unique spelling. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich
  survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 91 and 92, id 1
  (HIGH, item H1).

## 10. Reuse audit

The seam is 92 §4's note check itself; S1 replaces one fragment of it and adds no reader.
`python tools/codebase-map/reuse_lookup.py "pass a note check when one of several selected notes sits under the answer"`
ranked `check`, `note`, `checks` and `check_line`, none a reader that places a ledger line under an
answer, so no existing seam fits beyond 92's script and the acceptance ledger of `memory/HYGIENE.md`.

Recall terms used: `python tools/memory-recall/query.py "how does a ledger note check place a note under its acceptance answer when one label answers two criteria" --terms "acceptance ledger note check placement opener label token continuation line answer misplaced selector anchored"`
