# TOOL-dLinkedLibrary-59 — the decision log's diff against base read relative to unit 1's rotation, so a correct build reads additive

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 28 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-59-deviation-591.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-59-deviation-591.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 1 at HIGH**, report item **H3**. No other id shares the item.

`TOOL-dLinkedLibrary-52` AC4 requires every changed line of `git diff 5fede642 -- memory/DECISIONS.md` to
be an added line, and its S7 restores the rows unit 25 moved to "their bytes and positions at base".
`TOOL-dLinkedLibrary-1` S8, at order 8, rotates every settled non-major row out of the log, byte-identical,
into `memory/archive/DECISIONS.<date>.md`, and rewrites the rotation note at the log's head
(`memory/DECISIONS.md:3`). Unit 52 runs at order 27. On a correct build the diff shows unit 1's removed
rows and its replaced note, so AC4 is red, and a builder chasing it would restore the rotated rows and
undo unit 1's "the log keeps major decisions only".

This unit builds the reading AC4 needs: a verb that classifies every removed line of the log since a
base as a rotated row, the replaced note, or a departure, and checks the rows that remain keep their
base order. It repairs `TOOL-dLinkedLibrary-52` and builds one step after it (order 28).

## 2. Scope (IN)

- **S1** — The classification. `derive_log_departures(base, routing, root)` in
  `tools/memory-tree/decision_rubric.py` reads each line `git diff <base> -- memory/DECISIONS.md` marks as
  present at base and absent now, and classes each: `rotated`, when the line is a row whose id the
  routing record names as moved (`TOOL-dLinkedLibrary-1` S8's table) and the same bytes occur as a line
  of a rotated archive `memory/archive/DECISIONS.<date>.md`; `note`, when the line is the log's rotation
  note, opening `> **Rotated `; `departure`, any other line of that set. Observed by AC1 and AC2.
- **S2** — The order. Every row present at `<base>` and present now sits in the same relative order now
  as at base, and under the family heading its id's family names. A row out of either is a `departure`
  naming the row. Observed by AC2.
- **S3** — The verb. `python decision_rubric.py log-diff <base> --routing <record>` prints
  `log-diff — <r> rotated · <n> note · <d> departure(s)` and one line per departure, exits 1 when `<d>` is
  not 0, and exits 2 naming the argument when `<base>` does not resolve or the record does not parse.
  Observed by AC1 and AC2.
- **S4** — The repaired criterion. `TOOL-dLinkedLibrary-52`'s acceptance ledger answers its AC4 AMENDED,
  naming this unit and the `log-diff` line this pass prints over the tree. Observed by AC3.

## 3. Non-goals (OUT)

- The rotation itself and its routing record: `TOOL-dLinkedLibrary-1` S8's, unchanged.
- The restoration of the rows unit 25 moved: `TOOL-dLinkedLibrary-52` S7's; this unit measures it.
- `ROW_DUPLICATE_PIN` and check 27's lines: the rest of 52's AC4, unchanged.
- Check 10's grading of the rotation note: unchanged; S1 reads the note's opening only.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-1` — S8's routing record and `memory/archive/DECISIONS.<date>.md`, which S1 reads as the rotated population, and `decision_rubric.py`, which S3 extends (id 1)
- **consumes-from** `TOOL-dLinkedLibrary-52` — S7's restoration and AC4, which S2 measures and S4 answers (id 1)
- **hands-off** `TOOL-dLinkedLibrary-68` — S1's `derive_log_departures`, the §4 table and AC2's `log-diff` plant, which unit 68 re-points onto the row grammar (id 18 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-74` — S2's order check and the module docstring, which unit 74 completes (ids 4, 38 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `memory/DECISIONS.md:3` opens `> **Rotated 2026-08-10** —` at base; check 10 of
  `tools/memory-tree/check-memory-hygiene.sh` (:1628) reads it.
- `TOOL-dLinkedLibrary-1` S8: each settled row of a class other than `major` "leaves the log by the
  existing rotation, byte-identical, into `memory/archive/DECISIONS.<date>.md`, with the rotation note at
  the log's head that check 10 reads".
- `TOOL-dLinkedLibrary-1` S12 gives `decision_rubric.py` a `--fixture [--plant <case>]` harness; S3's
  plant joins it.

### The classification

| Removed line | Condition | Class |
|---|---|---|
| a row `<id> · …` | the routing record names `<id>` moved, and an archive holds the same bytes | `rotated` |
| a line opening `> **Rotated ` | at the log's head | `note` |
| anything else | | `departure` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_log_departures` | function, `decision_rubric.py` | `py.function`, asked at the pass |
| `log-diff` | verb of `decision_rubric.py` | none |
| `log-diff` | plant of `decision_rubric.py --fixture` | none |

### Files touched (estimate)

- `tools/memory-tree/decision_rubric.py`: S1 to S3 and the `log-diff` plant

### Alternatives rejected

- **AC4 compared against unit 1's tip instead of base.** It hides a departure unit 1's own pass made, and
  unit 1 rotates by rule, so its removals are the population to class, not to skip.
- **Rotated rows restored to the log.** It undoes `TOOL-dLinkedLibrary-1`'s goal.

## 5. Production-readiness checklist

- security — read-only: one `git diff`, the routing record and the archives.
- perf / scale — one diff and one read per archive; the log holds hundreds of rows.
- error / empty / loading states — a base that does not resolve, or a record that does not parse, exits 2
  naming it; an empty diff prints `0 rotated · 0 note · 0 departure(s)`.
- observability — each departure names its line and the rule it broke.
- risks — a row rotated by hand with no routing entry reads `departure`, the safe side.
- testing — the `log-diff` plant, AC2.
- migration — none.
- user docs — none under `help/`: the module's docstring states the classes.

## 6. Acceptance criteria

- **AC1** — When `python decision_rubric.py log-diff 5fede642 --routing <unit 1's routing record>` runs
  at this pass's tip, it prints `0 departure(s)` and exits 0.
  Red when: a rotated row or the replaced note reads as a departure.
  figure: DERIVED at the pass from the diff and the record.
  fixture: the routing record `TOOL-dLinkedLibrary-1`'s pass writes under `memory/builds/dLinkedLibrary/build/`.
- **AC2** — When `python decision_rubric.py --fixture --plant log-diff` runs, a scratch log
  whose tip rotates one row to an archive and replaces the note reads `0 departure(s)`; a tip that edits a
  row in place, one that removes a row no archive holds, and one that swaps two rows each read one
  departure naming the row, exit 1.
  Red when: an in-place edit, an unarchived removal or a reorder passes.
- **AC3** — When `grep -n "AC4" <unit 52's acceptance ledger>` runs, the answer reads AMENDED and names
  `TOOL-dLinkedLibrary-59`.
  Red when: unit 52's ledger certifies AC4 on a diff a correct build cannot produce.
  fixture: unit 52's acceptance ledger under `memory/builds/dLinkedLibrary/build/`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/decision_rubric.py · covers AC2 · the `log-diff` plant's four tips, the failing case staged by classing every removed line `departure` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 1 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 1 (HIGH, item
  H3).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-68, TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-1`'s `decision_rubric.py`, its routing record and its
`--fixture` harness, and the log's existing rotation, whose archives and note check 10 already grades.
`python tools/codebase-map/reuse_lookup.py "classify removed lines of the decision log diff against rotated
archives"` ranked `check_line`, `classify` (`tools/govkit/census.py`, a file census) and
`check_lease_only_diff` (`tools/unattended/lib-unattended.sh`, a run-state diff), none a reader of the
log's rotation, so no existing seam fits beyond the rubric module being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
