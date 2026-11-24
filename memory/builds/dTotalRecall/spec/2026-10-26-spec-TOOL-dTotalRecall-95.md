# TOOL-dTotalRecall-95 — a record of unit 59's absorbs departure carries one key, `pass(59)` with the string, whichever unit writes it, so every counter of it counts the same records

**Status:** DEFERRED · rev-2 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 37 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-95-deviation-951.md](../build/2026-10-26-build-TOOL-dTotalRecall-95-deviation-951.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-95-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-95-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-95-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-95-reground-spec-writer.md) | log | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, its item **H2**, alone in that item. Ids 13 and 19 (item M5,
MEDIUM) are the same defect seen from the counter's side and from the key's side; the report grades
them apart, and the batch `TOOL-dTotalRecall-100` takes them.

As audited, `TOOL-dTotalRecall-90` §4 "The deviation record" set a record's Evidence to the labelled line,
the ledger path and the token `audit-77 id <report id> <label>`. The `s1-59` labelled line is
`s1-59 <sha> <count> <string>`, the shape `TOOL-dTotalRecall-81` §4's `read_at` prints, so it carries
the absorbs-is-absent string and never the literal `pass(59)`. `TOOL-dTotalRecall-89` (order 38) counts
the departure in its S2 by `pass(59)` and the string, and its S4 writes a record wherever that count is
0, so a record unit 90 wrote at order 36 would be counted as none and written a second time.
`TOOL-dTotalRecall-83` §4 "The deviation records" and `TOOL-dTotalRecall-74` §4 "The deviation
record" both put `pass(59)` and the string in its Evidence, so the key every other writer uses is
the pair.

Re-grounded at `02e6a8172`, the departure is not owed. Spec 74, CLOSED, spec 83 rev-4 and spec 90 rev-3
each pin `s1-59` at 1 over a blob that cannot move and cut the write, and the build folder holds no
record of unit 59 that names the string. Spec 90 rev-3 adds the guard's token to Evidence, which for
unit 59 is the string, so its recipe still names no `pass(59)`.

This unit makes that pair the one key of the departure and observes it over the folder. A record of
unit 59 that names the string without `pass(59)` is named by path. Unit 89 counts through the key and
writes by it. It repairs `TOOL-dTotalRecall-90`, at order 37, one above that unit's 36.

## 2. Scope (IN)

- **S1** — The key. A deviation record of `TOOL-dTotalRecall-59` that names the string
  `` `absorbs` is absent `` carries `pass(59)` in its Evidence too, whichever unit writes it. §4's
  table lists, for each unit spec 90 §4 "The guards" may owe a record of, the key token its owing spec
  names that the recipe does not carry; unit 59's row is the only one with such a token. Observed by AC1.
- **S2** — The check. §4's `key59` sets the records of unit 59 that name the string beside those that
  name the string and `pass(59)`, both listed by `TOOL-dTotalRecall-93`'s `has_deviation --paths`, and
  prints `key59 missing <path>` for each record in the first list and not the second, then
  `key59 <a> <b>`. Where either call of the probe fails it prints `key59 red the probe failed` and no
  numbers. Observed by AC1 and AC2.
- **S3** — The re-statement. §4's re-stating record, whose Evidence adds `pass(59)` and the token
  `audit-89 id 2 s3`, is shaped and seen over the fixture. Its write in this pass is cut: at `s1-59` 1
  no record of unit 59 is owed (spec 83 §4 "The decision table", third row), and re-stating an unowed
  one would write the false departure a second time. The ledger names each record `key59` names missing
  by path as unowed. Observed by AC1 and AC2.
- **S4** — One record per departure. `has_deviation` over the build folder for unit 59 with the string
  is read after S3. Its correcting record is cut for S3's reason: where it prints 2 or more, each record
  is an unowed one, which the ledger names by path. Observed by AC2.

## 3. Non-goals (OUT)

- The probe's unit key (item H1, ids 1 and 28): `TOOL-dTotalRecall-93` and `TOOL-dTotalRecall-94`.
- Unit 89's guard and the tip re-check of the key after units 89 and 92 have written (item M5, ids 13
  and 19): the batch `TOOL-dTotalRecall-100`.
- Deleting or editing a record that lacks the key. A deviation record is evidence of what a pass did,
  as spec 83 §4 "Alternatives rejected" states.
- Taking an unowed record of unit 59 out of the live set: unit 89's table grades it, and
  `TOOL-dTotalRecall-92`'s S11 makes a duplicate pair one.
- Editing spec 90, frozen once its unit builds.
- The checklist entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-90` — its record recipe, its guards and its reading that no record of unit 59 is owed, which this unit checks over the folder
- **consumes-from** `TOOL-dTotalRecall-93` — `has_deviation --paths`, through which `key59` lists the records and S4 counts them
- **consumes-from** `TOOL-dTotalRecall-83` — the Evidence its §4 puts in a record of unit 59, `pass(59)` and the string, from which the key is taken
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door §4's re-stating record is shaped for
- **hands-off** `TOOL-dTotalRecall-89` — the key, by which that unit's S2 count and S4 guard name every record of unit 59's absorbs departure, whichever unit wrote it, and the paths of any record the ledger names as lacking it
- **hands-off** `TOOL-dTotalRecall-100` — `key59` and the re-stating record, which that batch runs again at the tip for ids 13 and 19

## 4. Design

### The key

| Record of | Key token beyond the labelled line and unit 90's recipe | Source |
|---|---|---|
| `TOOL-dTotalRecall-59` | `pass(59)` | spec 74 §4 "The deviation record", spec 83 §4 "The deviation records" |
| units 67, 70 and 74 | none: each guard's token is part of the string or label its labelled line carries | spec 90 rev-3 §4 "The guards" |
| units 83 and 84 | none: each guard's token is the recipe's own `audit-77 id 22 <label>` | spec 90 rev-3 §4 "The guards" |

A writer of a record of unit 59 by unit 90 §4's recipe adds `pass(59)` to the Evidence the recipe
names.

### The check

```bash
# run from the repository root, with TOOL-dTotalRecall-93 §4's has_deviation sourced
key59() {  # folder -> "key59 missing <path>" per record of unit 59 naming the string without pass(59), then "key59 <a> <b>"
  local s='`absorbs` is absent' a b
  a=$(has_deviation --paths "$1" 59 "$s") && b=$(has_deviation --paths "$1" 59 "$s" 'pass(59)') ||
    { echo "key59 red the probe failed"; return 1; }
  a=$(printf '%s\n' "$a" | tr -d '\r' | sed -n 's/^rec //p' | sort)
  b=$(printf '%s\n' "$b" | tr -d '\r' | sed -n 's/^rec //p' | sort)
  comm -23 <(printf '%s\n' "$a" | grep .) <(printf '%s\n' "$b" | grep .) | sed 's/^/key59 missing /'
  echo "key59 $(printf '%s\n' "$a" | grep -c .) $(printf '%s\n' "$b" | grep -c .)"
}
key59 memory/builds/dTotalRecall/build
has_deviation --paths memory/builds/dTotalRecall/build 59
```

Both lists come from one counter, so they differ only by the token. The key holds where the last line
prints two equal numbers. rev-1's `key59` took its lists through a pipe, which hides the probe's exit:
over a probe that raised on every record it printed `key59 0 0`, the green answer (DERIVED 2026-11-24,
spec 93 rev-1's fence at `02e6a8172`, whose `_ID` is now a `SlugPattern`). The last command is the
liveness: with no token the probe lists unit 59's roster record. `tr` drops the carriage return Python
prints into a pipe on Windows, so a path is usable as printed.

### The re-stating record

No record is written by this pass (S3); `TOOL-dTotalRecall-100` reads this shape at the tip. It is written by
`python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-59 --title <text>`,
which refuses a missing `--title` or required field (`tools/memory-tree/build_records.py#write_new_record`), only where
the departure it re-states is owed, with every field of the record it re-states copied unchanged except these:

| Field | Value |
|---|---|
| Evidence | the re-stated record's Evidence, then `pass(59)` and the token `audit-89 id 2 s3` |
| Follow-through | `new unit TOOL-dTotalRecall-<writing unit>` |
| Caused-by | `TOOL-dTotalRecall-<writing unit>` |
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
key59 "$FX"
printf '%s\n' '- **Supersedes:** 2026-10-26-build-TOOL-dTotalRecall-59-deviation-591' >> "$FX/2026-10-26-build-TOOL-dTotalRecall-59-deviation-592.md"
key59 "$FX"
( has_deviation() { return 1; }; key59 "$FX" )
```

The first record carries the `s1-59` line as unit 90's recipe writes it, and the second re-states it
by §4's table. The second `key59` runs before the second record names the first, and the last over a
probe that fails.

PINNED, measured 2026-11-24 at `02e6a8172` with these exact commands and spec 93 rev-2 §4's
probe:

| Run | Printed (PINNED 2026-11-24) |
|---|---|
| first `key59` | one `key59 missing` line naming `-59-deviation-591`, then `key59 1 0` |
| second | the same `missing` line, then `key59 2 1` |
| third | `key59 1 1` alone |
| fourth | `key59 red the probe failed` alone |
| `key59 memory/builds/dTotalRecall/build` | `key59 0 0` alone |
| `has_deviation --paths` there, no token | one `rec` line naming `-59-deviation-591`, then 1 |

The first, third and fifth are the ones measured 2026-10-26 at `32febccb6`. The fixture's 591 is a scratch
file; the folder's own is the roster record
`memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md`, which names
neither token.

### Why order 37

Unit 90 writes at order 36 and unit 89 counts at 38. This unit consumes `TOOL-dTotalRecall-93`,
which shares order 37, and `--dispatch` refuses it until that unit is CLOSED or WONTDO
(`tools/unattended/unattended.sh#verb_dispatch`, reading
`tools/unattended/lib-unattended.sh#read_consumes_from`).

### Inventory

Minted: the function `key59`, spec text only, and no deviation record. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger)

### Alternatives rejected

- **Unit 89 counts by the union of both keys.** The report's second option. It leaves two spellings
  of one departure in the folder, so every later counter must know both; one key leaves one.
- **Count by the string alone.** With the unit fixed by `unit_of` it would count the same records
  today, and it would still leave unit 89's written key, `pass(59)` with the string, unmet by a record
  another unit wrote.
- **Re-state a keyless record whatever S1 reads, as rev-1 did.** At `s1-59` 1 the record is unowed, and a
  re-statement is a live record written after `pass(83)`, which spec 89 §4's table grades red.

## 5. Production-readiness checklist

- security — no surface. The fixture folder sits in the run's scratch.
- perf / scale — three probe calls over the build folder, the liveness included.
- error / empty / loading states — a folder with no record of unit 59 prints `key59 0 0`, which holds; a probe that
  fails prints the red line and never a count.
- observability — every missing record is named by path.
- risks — a writer after order 37 that drops `pass(59)` is caught by the batch's tip re-run of `key59`.
  `key59` reads Evidence alone, so a record naming the departure in another field is not seen.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's fixture runs, its four `key59` calls print what §4's table pins for them: one
  `key59 missing` line with `key59 1 0`, the same line with `key59 2 1`, `key59 1 1` with no `missing`
  line, and `key59 red the probe failed` with no numbers.
  Red when: a record lacking `pass(59)` goes unnamed, the re-stated record still counts, or a failed
  probe prints a count.
  fixture: the folder is made in the run's scratch by the pass; the tree holds none.
  figure: the lines are PINNED in §4, measured 2026-11-24.
- **AC2** — When `key59 memory/builds/dTotalRecall/build` runs after the pass, it prints no `missing`
  line and two equal numbers, and `has_deviation memory/builds/dTotalRecall/build 59` with the string
  prints at most 1, or the ledger names by path each record of unit 59 they count as unowed. With no
  token `has_deviation --paths` there lists the roster record, and `grep -l 'Caused-by:.. TOOL-dTotalRecall-95'` over
  the folder's `*-build-TOOL-dTotalRecall-59-deviation-*.md` files lists nothing.
  Red when: a live record of unit 59 names the string without `pass(59)`, or two name the departure, and
  the ledger names none of them; the liveness lists nothing; or this pass wrote a record of unit 59.
  figure: every number is DERIVED at the pass.

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
- rev-2 · 2026-11-24 · §1 §2 §3 §4 §5 AC1 AC2 §10 · re-grounded at HEAD `02e6a8172` per
  `2026-11-24-prompt-TOOL-dTotalRecall-95-reground-brief`, over spec 74 rev-3, CLOSED, 83 rev-4 and 90
  rev-3: `s1-59` reads 1, so no record of unit 59 is owed and the writes of S3 and S4 are cut, the re-stating
  record kept as the shape the batch reads; `key59` prints red where its probe fails, as rev-1's printed
  `0 0` over one that raised, and drops the carriage return; the fixture gains the un-superseded and the
  failed-probe arms, AC2 its liveness; line cites became symbols.

## 10. Reuse audit

The seams are `TOOL-dTotalRecall-93`'s `has_deviation --paths`, whose two member lists `key59`
compares with `comm`, and the Evidence that spec 74 §4 and spec 83 §4 already name for a record of
unit 59. `python tools/codebase-map/reuse_lookup.py "assign a deviation record to its unit by its file name stem"`
ranked `tools/memory-tree/deviation_join.py#read_records` and `#read_record` among its SEAM candidates (re-run
2026-11-24), and the probe it extends is already the per-file reader. The recall query below found this audit's items H2
and M5, spec 83's and spec 74's record paragraphs, and the class `append-without-an-idempotence-key`;
re-run 2026-11-24 it adds no reader of this shape.
No existing seam fits beyond them. `tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder
walks of `tools/memory-tree/record_causes.py#check_cause_writers` and `tools/memory-tree/record_kinds.py#check_alias_compares` are no seam
here: this unit reads no marker and no registry.

Recall terms used: `python tools/memory-recall/query.py "which tokens does every writer and counter of one deviation record use as its write-once key" --terms "deviation record unit 59 pass(59) absorbs Evidence token write-once key recipe labelled line idempotence"`
