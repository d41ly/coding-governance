# TOOL-dTotalRecall-93 — the write-once probe counts a deviation record under the unit its own file stem names, never under its Departs from address

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 37 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-93-deviation-931.md](../build/2026-10-26-build-TOOL-dTotalRecall-93-deviation-931.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-93-round9-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-93-round9-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-94 |
| [2026-10-26-prompt-TOOL-dTotalRecall-93-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-93-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-93-round9-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-93-round9-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, which it shares with id 28 (HIGH, taken by
`TOOL-dTotalRecall-94`).

`TOOL-dTotalRecall-90` §4 "The write-once probe" keeps a record where
`r['address'].startswith(unit + '@')` (the probe's `print` line). `deviation_join.read_record` fills
`address` from the record's **Departs from** field (`tools/memory-tree/deviation_join.py:259`). The
door's `--unit`, the file stem and the `**Serves:**` line all name the record's own unit instead, and
Departs from names the clause or spec the record departs from. Measured 2026-10-26 at `32febccb6`:
none of the 8 records in `memory/builds/dTotalRecall/build/` departs from its own unit, and unit 90's
probe, run verbatim, printed 0 for units 2, 3 and 6, which hold 1, 2 and 1 records. The key also
over-counts: a record of unit 89 that departs from `TOOL-dTotalRecall-59@rev-2` counts as unit 59's.
Units 89, 91 and 92 guard their writes and grade their criteria through this probe, and unit 92's tip
scan groups its `by` and `dup` lines by the same address.

This unit re-keys the probe on the unit the record's own file stem names, parsed with the deviation
grammar's id pattern, and hands that key to every reader of this round. At its pass it re-runs each
write-once guard unit 90 ran, writes any record a miscount skipped, and makes one any pair a miscount
let through. It repairs `TOOL-dTotalRecall-90`, at order 37, one above that unit's 36.

## 2. Scope (IN)

- **S1** — The probe, re-keyed. §4's `has_deviation` keeps unit 90's arguments, a folder, a unit
  number and tokens, and counts the live records whose own file stem names the unit, through
  `unit_of`. It never reads Departs from. Observed by AC1 and AC2.
- **S2** — The member list. `has_deviation --paths` prints `rec <path>` for each record it counts,
  then the count, so a check over the counted records reads the counter's own list. Observed by AC2.
- **S3** — The one key. `unit_of` is the record-to-unit key of every reader this round touches: the
  guards and criteria of units 89, 91 and 92 that call `has_deviation`, and the `by` and `dup` lines
  of unit 92's tip scan, which group by `unit_of` in place of the Departs from address. Each takes it
  through its §3 edge from this unit. Observed by AC3.
- **S4** — Unit 90's guards, re-run. For each write-once guard unit 90's S4 ran, which its ledger's
  AC2 line names by unit and token, `has_deviation` runs again under the new key. Where it prints 0
  and unit 90 skipped the write as done, this pass writes the owed record by unit 90 §4's recipe with
  the token `audit-89 id 1 s4`. Where it prints 2 or more, each later record is made one with the
  earliest by §4's correcting record. Observed by AC4.

## 3. Non-goals (OUT)

- The census over every unit holding a record, the real-shaped fixture and the probe seen red (item
  H1, id 28): `TOOL-dTotalRecall-94`.
- The Evidence tokens a record of unit 59 carries (item H2, id 2): `TOOL-dTotalRecall-95`.
- Editing spec 90, frozen once its unit builds. Specs 89, 91 and 92 take the key through their §3
  edges, and nothing in their bodies is rewritten here.
- A rule that every record departs from its own unit, the report's alternative: §4 "Alternatives
  rejected".
- The bug-class entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-90` — `has_deviation`'s arguments, its record recipe and the write-once guards its S4 ran, which this unit re-keys and runs again
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4's records are written through
- **hands-off** `TOOL-dTotalRecall-89` — the re-keyed `has_deviation`, through which that unit's S2, S4 and S5 guards and its AC2 and AC3 counts are made in place of unit 90's
- **hands-off** `TOOL-dTotalRecall-91` — the re-keyed `has_deviation`, through which that unit's S4 guards and its AC3 counts are made in place of unit 90's
- **hands-off** `TOOL-dTotalRecall-92` — the re-keyed `has_deviation` and `unit_of`, by which that batch's guards count and its tip scan groups its `by` and `dup` lines
- **hands-off** `TOOL-dTotalRecall-94` — the re-keyed `has_deviation`, which that unit's census runs over every unit holding a record
- **hands-off** `TOOL-dTotalRecall-95` — the re-keyed `has_deviation` and §4's correcting record, through which that unit counts and re-states the records of unit 59
- **hands-off** `TOOL-dTotalRecall-96` — the re-keyed `has_deviation`, through which that unit writes its records once
- **hands-off** `TOOL-dTotalRecall-99` — `unit_of`, by which that unit's witnessed scan groups its `by` and `dup` lines
- **hands-off** `TOOL-dTotalRecall-100` — `has_deviation` with its `--paths` mode and §4's correcting record, which that batch's items read and write through

## 4. Design

### The key and the probe

```bash
# run from the repository root; PY is the launcher tools/lib/resolve-python.sh resolves
has_deviation() {  # [--paths] folder · unit number · token... -> count of live records of that unit holding every token
  "$PY" - "$@" <<'PROBE'
import glob, os, pathlib, re, sys
sys.path.insert(0, 'tools/memory-tree')
import deviation_join
args = sys.argv[1:]
paths = args[0] == '--paths'
folder, unit, tokens = args[paths], 'TOOL-dTotalRecall-' + args[paths + 1], args[paths + 2:]
def unit_of(r):  # the unit the record's own file stem names, never its Departs from address
    m = re.fullmatch(r'\d{4}-\d{2}-\d{2}-build-(' + deviation_join._ID + r')-deviation-\d+', r['id'])
    return m.group(1) if m else None
recs = [deviation_join.read_record(p.replace(os.sep, '/'), pathlib.Path(p).read_text(encoding='utf-8'))
        for p in sorted(glob.glob(os.path.join(folder, '*-deviation-*.md')))]
gone = {r['supersedes'] for r in recs if r['supersedes']}
hits = [r for r in recs if r['id'] not in gone and unit_of(r) == unit
        and all(t in (r['evidence'] or '') for t in tokens)]
for r in hits if paths else ():
    print('rec', r['path'])
print(len(hits))
PROBE
}
```

`r['id']` is the record's file stem (`deviation_join.py:256`), and `_ID` is the id pattern the
grammar's own `_STEM` is built from (`:155`, `:159`). The unit is compared whole, so unit 5 never
matches unit 59 or 590. The door writes the stem and the Serves line from one `--unit`, so the stem is
the key without a second parse. A stem the grammar refuses has no unit and counts for none. Every other
property of unit 90's probe stands: the working-tree glob, the `**Supersedes:**` exclusion, the
substring test per token, and no token holding a single quote.

PINNED, measured 2026-10-26 at `32febccb6` with this probe over `memory/builds/dTotalRecall/build`
and no token: units 2, 3, 6, 8, 21, 22 and 23 printed 1, 2, 1, 1, 1, 1 and 1, and units 5 and 59
printed 0. Unit 90's probe printed 0 for every one of them. Over a scratch folder holding a record of
unit 59 departing from `cl-dClosedLoop-0213@09982ca6`, one departing from `TOOL-dTotalRecall-62@rev-2`
and a record of unit 89 departing from `TOOL-dTotalRecall-59@rev-2`, each naming `pass(59)`, this
probe printed 2 for unit 59 and 1 for unit 89, and unit 90's printed 1 and 0.

### The correcting record

Two live records of one departure are made one by a third record of the same unit, written by
`python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <that unit>`:

| Field | Value |
|---|---|
| Departs from | the later record's Departs from, unchanged |
| Hand-off | `spec-to-code` |
| Before | `the record <later stem>` |
| After | `superseded as a duplicate of <earlier stem>` |
| Cause | `review finding` |
| Reason | one sentence naming the audit item and the key both records answer to |
| Evidence | both stems and the token `audit-89 id <report id> <label>`, and never a token of the departure's own key |
| Risk | `editorial` (`RISKS`, `deviation_join.py:150`) |
| Approver | `author`, the pass of the writing unit, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`) |
| Follow-through | `new unit TOOL-dTotalRecall-<writing unit>` |
| Caused-by | `TOOL-dTotalRecall-<writing unit>` |
| Supersedes | the later record's stem |

Its Evidence holds no token of the departure, so the probe counts the earlier record alone. Its
Before and After are its own, so no live record shares its unit, Before and After, and the tip scan's
`dup` key never pairs it again.

### Unit 90's guards

The guards are read from unit 90's acceptance ledger, which names each owed record by unit and token.
Each runs again as `has_deviation memory/builds/dTotalRecall/build <unit> <token>...`, and the
ledger sets the new count beside the one unit 90 recorded.

### Why order 37

Unit 90 runs its guards at order 36. Unit 91 shares order 37 and consumes this probe: the dispatch
verb refuses a consumer while a producer of its own build is neither CLOSED nor WONTDO, units of one
order included (`tools/unattended/unattended.sh:13691-13698`), so unit 91 builds after this unit.

### Inventory

Minted: the probe `has_deviation` re-keyed, its `--paths` mode and the function `unit_of`, all spec
text only; deviation records only where a re-run guard owes one, and correcting records only where it
counts two. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S4)

### Alternatives rejected

- **Every record departs from its own unit, with a check refusing one that does not.** The report's
  alternative. Measured above, all 8 records in the folder depart from a clause or a foreign spec,
  which is what Departs from is for; the rule would make the field restate the stem.
- **Key on the `**Serves:**` line.** It names the same unit from the same `--unit`, and reading it
  means a second parse of the text `read_record` already keyed by its stem.
- **Key on Departs from or the stem, either.** A record of unit 89 departing from unit 59 would then
  count for both, the over-count measured above.

## 5. Production-readiness checklist

- security — no surface. The fixture folder sits in the run's scratch.
- perf / scale — one pass over the build folder's records per call.
- error / empty / loading states — a stem the grammar refuses counts for no unit; an empty folder
  prints 0.
- observability — `--paths` names every record counted; the ledger sets each re-count beside unit 90's.
- risks — a reader of this round that kept unit 90's probe is named by AC3.
- testing — AC1 to AC4 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `has_deviation memory/builds/dTotalRecall/build <n>` runs at this pass's base for
  each unit a record's file stem names, it prints that unit's number of live record files, and unit 5
  prints 0.
  Red when: a unit holding a record prints 0, or one unit counts another's record.
  figure: the counts at `32febccb6` are PINNED in §4; at the pass they are DERIVED by `ls` of the folder.
- **AC2** — When `has_deviation --paths` runs over §4's three-record scratch folder for unit 59 with
  the token `pass(59)`, it prints two `rec` lines, each a record of unit 59, and the count 2, and for
  unit 89 it prints 1.
  Red when: the unit-89 record departing from unit 59 counts for 59, or a unit-59 record departing from
  a clause is missed.
  fixture: the folder is made in the run's scratch by the pass; the tree holds none.
- **AC3** — When `git grep -l "consumes-from\*\* .TOOL-dTotalRecall-93." -- memory/builds/dTotalRecall/spec`
  runs, it lists the specs of units 89, 91, 92, 94, 95, 96, 99 and 100.
  Red when: a unit of this build that calls `has_deviation` or groups by unit after order 36 names no
  edge to this unit.
- **AC4** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-93" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC4 line sets each guard unit 90 ran beside its count under the new key, and
  for each owed record `has_deviation memory/builds/dTotalRecall/build <unit> <token>` prints 1.
  Red when: a guard re-counts 0 where unit 90 skipped the write, or 2 or more after the pass.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is the probe over the build folder, its scratch fixture and this pass's
re-run guards.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 1
  (HIGH, item H1, shared with id 28).

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-90`'s `has_deviation`, re-keyed, and the deviation grammar's own
record reader `deviation_join.read_record` (`tools/memory-tree/deviation_join.py:212`) with its id
pattern `_ID` (`:155`), from which the grammar builds `_STEM` and `RECORD_NAME` (`:159-160`).
`python tools/codebase-map/reuse_lookup.py "assign a deviation record to its unit by its file name stem"`
ranked `read_records` (`deviation_join.py:268`) among its SEAM candidates and no function that maps a
record to its unit; `read_records` reads tracked files only, so the probe keeps the per-file
`read_record` over a working-tree glob. The recall query below found this audit's item H1, spec 90's
probe and the `TOOL-dTrueNorth-4` record kind. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a probe key a deviation record to its own unit and see the real records" --terms "deviation record stem unit Serves Departs from address has_deviation write-once fixture real population"`
