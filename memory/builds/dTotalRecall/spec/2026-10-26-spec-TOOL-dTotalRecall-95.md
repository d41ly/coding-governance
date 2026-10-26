# TOOL-dTotalRecall-95 — a record of unit 59's absorbs departure carries one key, `pass(59)` with the string, whichever unit writes it, so every counter of it counts the same records

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 37 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, its item **H2**, alone in that item. Ids 13 and 19 (item M5,
MEDIUM) are the same defect seen from the counter's side and from the key's side; the report grades
them apart, and the batch `TOOL-dTotalRecall-100` takes them.

`TOOL-dTotalRecall-90` §4 "The deviation record" sets a record's Evidence to the labelled line, the
ledger path and the token `audit-77 id <report id> <label>`. The `s1-59` labelled line is
`s1-59 <sha> <count> <string>`, the shape `TOOL-dTotalRecall-81` §4's `read_at` prints, so it carries
the absorbs-is-absent string and never the literal `pass(59)`. Unit 90's S4 writes an owed record of
unit 59 by that recipe at order 36. `TOOL-dTotalRecall-89` (order 38) counts the departure in its S2
by `pass(59)` and the string, and its S4 writes a record wherever that count is 0. On the arm where
unit 90 wrote the record, unit 89 counts 0 and writes a second record of the same departure.
`TOOL-dTotalRecall-83` §4 "The deviation records" and `TOOL-dTotalRecall-74` §4 "The deviation
record" both put `pass(59)` and the string in its Evidence, so the key every other writer uses is
the pair.

This unit makes that pair the one key of the departure. Every live record of unit 59 that names the
string also names `pass(59)`: a record unit 90 wrote without it is re-stated once with the full key,
and two records of the departure are made one. Unit 89 counts through the key and writes by it. It
repairs `TOOL-dTotalRecall-90`, at order 37, one above that unit's 36.

## 2. Scope (IN)

- **S1** — The key. A deviation record of `TOOL-dTotalRecall-59` that names the string
  `` `absorbs` is absent `` carries `pass(59)` in its Evidence too, whichever unit writes it. §4's
  table lists, for each unit unit 90's S4 may write a record of, the tokens its owing spec names that
  the labelled line does not carry; unit 59's row is the only one with such a token. Observed by AC1.
- **S2** — The check. §4's `key59` sets the records of unit 59 that name the string beside those that
  name the string and `pass(59)`, both listed by `TOOL-dTotalRecall-93`'s `has_deviation --paths`, and
  prints `key59 missing <path>` for each record in the first list and not the second, then
  `key59 <a> <b>`. Observed by AC1 and AC2.
- **S3** — The re-statement. Each record `key59` names missing gets one re-stating record of unit 59,
  §4's, whose Evidence adds `pass(59)` and the token `audit-89 id 2 s3`. Observed by AC2.
- **S4** — One record per departure. After S3, where `has_deviation` over the build folder for unit 59
  with the string prints 2 or more, each later record is made one with the earliest by `TOOL-dTotalRecall-93` §4's
  correcting record, its Evidence carrying `audit-89 id 2 s4`. Observed by AC2.

## 3. Non-goals (OUT)

- The probe's unit key (item H1, ids 1 and 28): `TOOL-dTotalRecall-93` and `TOOL-dTotalRecall-94`.
- Unit 89's guard and the tip re-check of the key after units 89 and 92 have written (item M5, ids 13
  and 19): the batch `TOOL-dTotalRecall-100`.
- Deleting or editing a record that lacks the key. A deviation record is evidence of what a pass did,
  as spec 83 §4 "Alternatives rejected" states, so it is superseded and kept.
- Editing spec 90, frozen once its unit builds.
- The checklist entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-90` — its record recipe and the records of unit 59 its S4 wrote, which this unit checks and re-states
- **consumes-from** `TOOL-dTotalRecall-93` — `has_deviation --paths` and the correcting record, through which `key59` lists the records and S4 makes a pair one
- **consumes-from** `TOOL-dTotalRecall-83` — the Evidence its §4 puts in a record of unit 59, `pass(59)` and the string, from which the key is taken
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3's and S4's records are written through
- **hands-off** `TOOL-dTotalRecall-89` — the key, by which that unit's S2 count and S4 guard name every record of unit 59's absorbs departure, whichever unit wrote it
- **hands-off** `TOOL-dTotalRecall-100` — `key59`, which that batch runs again at the tip for ids 13 and 19

## 4. Design

### The key

| Record of | Tokens its owing spec names beyond the labelled line | Source |
|---|---|---|
| `TOOL-dTotalRecall-59` | `pass(59)` | spec 74 §4 "The deviation record", spec 83 §4 "The deviation records" |
| units 67, 70, 74, 82, 83, 84 | none: the owing paragraph names the read's string, which the labelled line carries | spec 82 §4, spec 83 §4, spec 84 §4 "The deviation records" |

A writer of a record of unit 59 by unit 90 §4's recipe adds `pass(59)` to the Evidence the recipe
names.

### The check

```bash
# run from the repository root, with TOOL-dTotalRecall-93 §4's has_deviation sourced
key59() {  # folder -> "key59 missing <path>" per record of unit 59 naming the string without pass(59), then "key59 <a> <b>"
  local s='`absorbs` is absent' a b
  a=$(has_deviation --paths "$1" 59 "$s" | sed -n 's/^rec //p' | sort)
  b=$(has_deviation --paths "$1" 59 "$s" 'pass(59)' | sed -n 's/^rec //p' | sort)
  comm -23 <(printf '%s\n' "$a" | grep .) <(printf '%s\n' "$b" | grep .) | sed 's/^/key59 missing /'
  echo "key59 $(printf '%s\n' "$a" | grep -c .) $(printf '%s\n' "$b" | grep -c .)"
}
key59 memory/builds/dTotalRecall/build
```

Both lists come from one counter, so they differ only by the token. The key holds where the last line
prints two equal numbers.

### The re-stating record

Written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-59`,
with every field of the record it re-states copied unchanged except these:

| Field | Value |
|---|---|
| Evidence | the re-stated record's Evidence, then `pass(59)` and the token `audit-89 id 2 s3` |
| Follow-through | `new unit TOOL-dTotalRecall-95` |
| Caused-by | `TOOL-dTotalRecall-95` |
| Supersedes | the re-stated record's stem |

The re-stated record leaves the live set, so the departure keeps one live record, now under the key.

### The fixture

```bash
# run from the repository root; SCRATCH is the run's scratch folder
FX="$SCRATCH/fx95"; rm -rf "$FX"; mkdir -p "$FX"
SRC=memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md
R1="$FX/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md"
sed -e 's/^\*\*Serves:\*\* deviation .*/**Serves:** deviation TOOL-dTotalRecall-59/' \
    -e 's/^- \*\*Evidence:\*\* .*/- **Evidence:** s1-59 0123abcd 0 `absorbs` is absent, audit-77 id 22 s1-59/' "$SRC" > "$R1"
key59 "$FX"
sed -e 's/^\(- \*\*Evidence:\*\* .*\)$/\1, pass(59), audit-89 id 2 s3/' \
    -e 's/^- \*\*Caused-by:\*\* .*/- **Caused-by:** TOOL-dTotalRecall-95/' "$R1" > "$FX/2026-10-26-build-TOOL-dTotalRecall-59-deviation-592.md"
printf '%s\n' '- **Supersedes:** 2026-10-26-build-TOOL-dTotalRecall-59-deviation-591' >> "$FX/2026-10-26-build-TOOL-dTotalRecall-59-deviation-592.md"
key59 "$FX"
```

The first record carries the `s1-59` line as unit 90's recipe writes it, and the second re-states it
by §4's table. PINNED, measured 2026-10-26 at `32febccb6` with these exact commands: the first `key59`
printed one `key59 missing` line naming `-59-deviation-591` and `key59 1 0`, the second printed
`key59 1 1` and nothing else, and over `memory/builds/dTotalRecall/build` it printed `key59 0 0`.

### Why order 37

Unit 90 writes at order 36 and unit 89 counts at 38. This unit consumes `TOOL-dTotalRecall-93`,
which shares order 37, and the dispatch verb holds it until that unit is CLOSED
(`tools/unattended/unattended.sh:13691-13698`).

### Inventory

Minted: the function `key59`, spec text only; re-stating records and correcting records of unit 59
only where S3 or S4 owes one. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S3 and S4)

### Alternatives rejected

- **Unit 89 counts by the union of both keys.** The report's second option. It leaves two spellings
  of one departure in the folder, so every later counter must know both; one key leaves one.
- **Count by the string alone.** With the unit fixed by `unit_of` it would count the same records
  today, and it would still leave unit 89's written key, `pass(59)` with the string, unmet by a record
  unit 90 wrote, which is the duplicate this unit removes.

## 5. Production-readiness checklist

- security — no surface. The fixture folder sits in the run's scratch.
- perf / scale — two probe calls over the build folder.
- error / empty / loading states — a folder with no record of unit 59 prints `key59 0 0`, which holds.
- observability — every missing record is named by path.
- risks — a writer after order 37 that drops `pass(59)` is caught by the batch's tip re-run of `key59`.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `key59` runs over §4's scratch fixture, it prints one `key59 missing` line and
  `key59 1 0`, and after the re-stating record is added it prints `key59 1 1` and no `missing` line.
  Red when: a record lacking `pass(59)` goes unnamed, or the re-stated record still counts.
  fixture: the folder is made in the run's scratch by the pass; the tree holds none.
  figure: the lines are PINNED in §4, measured 2026-10-26.
- **AC2** — When `key59 memory/builds/dTotalRecall/build` runs after the pass, it prints no `missing`
  line, its two numbers are equal, and `has_deviation memory/builds/dTotalRecall/build 59 'pass(59)'`
  with the string prints at most 1.
  Red when: a live record of unit 59 names the string without `pass(59)`, or two live records name the
  departure.
  figure: both numbers are DERIVED at the pass.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is `key59` over the build folder and a scratch fixture.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 2
  (HIGH, item H2), one defect with ids 13 and 19 (item M5).

## 10. Reuse audit

The seams are `TOOL-dTotalRecall-93`'s `has_deviation --paths`, whose two member lists `key59`
compares with `comm`, and the Evidence that spec 74 §4 and spec 83 §4 already name for a record of
unit 59. `python tools/codebase-map/reuse_lookup.py "assign a deviation record to its unit by its file name stem"`
ranked `read_records` (`tools/memory-tree/deviation_join.py:268`) among its SEAM candidates, and the
probe it extends is already the per-file reader. The recall query below found this audit's items H2
and M5, spec 83's and spec 74's record paragraphs, and the class `append-without-an-idempotence-key`.
No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "which tokens does every writer and counter of one deviation record use as its write-once key" --terms "deviation record unit 59 pass(59) absorbs Evidence token write-once key recipe labelled line idempotence"`
