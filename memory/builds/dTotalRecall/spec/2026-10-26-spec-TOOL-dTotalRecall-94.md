# TOOL-dTotalRecall-94 — the write-once probe is seen to count the real records: a census over every unit holding one, seen red on unit 90's probe, and a fixture of the records' own shape

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 37 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-94-deviation-941.md](../build/2026-10-26-build-TOOL-dTotalRecall-94-deviation-941.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 28 at HIGH**, its item **H1**, which it shares with id 1 (HIGH, taken by
`TOOL-dTotalRecall-93`). The report files it under the class
`staged-break-substitutes-a-synthetic-value`.

`TOOL-dTotalRecall-90` §6 AC3 grades its write-once probe over a scratch folder holding one record of
unit 59 whose Departs from names unit 59 itself. No record in the build folder has that shape:
measured 2026-10-26 at `32febccb6`, all 8 depart from a clause or a foreign spec, for example
`-2-deviation-21` from `cl-dClosedLoop-0213@09982ca6`. Unit 74 §4 tells its builder to model the
record of unit 59 on `-2-deviation-21`, and unit 83 §4 pins no Departs from. So AC3 passes while the
probe misses every real record, and no criterion of unit 90 ever runs the probe over the folder it
guards.

This unit makes the probe's verdict an observation of the real population. A census sets, for every
unit a record's file stem names, the probe's count beside the number of that unit's live record files.
It is seen red on unit 90's probe and green on `TOOL-dTotalRecall-93`'s, and a fixture built from a
real record carries the shapes the folder holds. Unit 90's AC3 answer is recorded against the census.
It repairs `TOOL-dTotalRecall-90`, at order 37, one above that unit's 36.

## 2. Scope (IN)

- **S1** — The census. §4's `census` takes a folder and a probe function and prints, for every unit a
  record's file stem names, `census <n> probe <a> files <b>`, where `a` is the probe's count with no
  token and `b` is the unit's record files less those a `**Supersedes:**` line names. Where the two
  differ it prints `red census <n>`. Observed by AC1.
- **S2** — Seen red. The same census over the same folder with unit 90 §4's probe, copied verbatim and
  renamed `has_deviation_90`, prints a `red census` line for every unit. Observed by AC2.
- **S3** — The fixture of the real shape. §4's `mk` builds records from
  `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`, changing
  only Serves, Departs from and Evidence: two records of unit 59 departing from a clause and from
  `TOOL-dTotalRecall-62@rev-2`, a record of unit 5, a record of unit 89 departing from unit 59, a
  ledger quoting the key, and a record superseding the second of unit 59. The probe's counts over it
  are §4's. Observed by AC3.
- **S4** — Unit 90's AC3, answered again. The ledger sets unit 90's AC3 answer beside the census line
  this pass prints over `memory/builds/dTotalRecall/build`. A deviation record of
  `TOOL-dTotalRecall-90` names AC3's fixture as a shape no real record has and the census as its
  observation, written once, only where `has_deviation memory/builds/dTotalRecall/build 90 'audit-89 id 28 ac3'`
  prints 0. Observed by AC4.

## 3. Non-goals (OUT)

- The key itself and the consumers' edges (item H1, id 1): `TOOL-dTotalRecall-93`.
- Running the census at the build's tip. Each later unit counts through the re-keyed probe, which is
  what this census certifies.
- Editing spec 90, frozen once its unit builds.
- The bug-class entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-93` — the re-keyed `has_deviation`, the probe the census certifies; without it the census has nothing to see green
- **consumes-from** `TOOL-dTotalRecall-90` — its probe, copied verbatim as the census's red arm, and its AC3 answer, which this unit records against the census
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4's record is written through

## 4. Design

### The census

```bash
# run from the repository root, with TOOL-dTotalRecall-93 §4's has_deviation sourced
census() {  # folder · probe function -> one census line per unit a record's file stem names, and a red where they differ
  local u a b s
  for u in $(ls "$1" | sed -n 's/^[0-9-]*-build-TOOL-dTotalRecall-\([0-9]*\)-deviation-[0-9]*\.md$/\1/p' | sort -un); do
    a=$("$2" "$1" "$u")
    b=$(ls "$1" | grep -c "^[0-9-]*-build-TOOL-dTotalRecall-$u-deviation-[0-9]*\.md$")
    s=$(cat "$1"/*-deviation-*.md | sed -n "s/^- \*\*Supersedes:\*\* \`\{0,1\}\([0-9-]*-build-TOOL-dTotalRecall-$u-deviation-[0-9]*\).*/\1/p" | sort -u | wc -l)
    echo "census $u probe $a files $((b - s))"
    [ "$a" = "$((b - s))" ] || echo "red census $u"
  done
}
census memory/builds/dTotalRecall/build has_deviation
census memory/builds/dTotalRecall/build has_deviation_90
```

The file count is an independent reader: `ls` and `sed` over names and Supersedes lines, never
`read_record`. A unit whose records are all superseded reads 0 on both sides.

PINNED, measured 2026-10-26 at `32febccb6` over the build folder: with the re-keyed probe the census
printed seven lines, `census 2 probe 1 files 1`, `census 3 probe 2 files 2`, and 1 against 1 for units
6, 8, 21, 22 and 23, and no `red` line. With `has_deviation_90` every probe value was 0 and it printed
`red census` for all seven units.

### The fixture

```bash
# run from the repository root; SCRATCH is the run's scratch folder
FX="$SCRATCH/fx94"; rm -rf "$FX"; mkdir -p "$FX"
SRC=memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md
mk() {  # unit · n · Departs from · extra line -> one record shaped as SRC, its Evidence naming the unit-59 key
  sed -e "s/^\*\*Serves:\*\* deviation .*/**Serves:** deviation TOOL-dTotalRecall-$1/" \
      -e "s/^- \*\*Departs from:\*\* .*/- **Departs from:** \`$3\`/" \
      -e "s/^- \*\*Evidence:\*\* .*/- **Evidence:** pass(59), \`absorbs\` is absent, audit-89 id 28 fx/" "$SRC" > "$FX/2026-10-26-build-TOOL-dTotalRecall-$1-deviation-$2.md"
  [ -z "$4" ] || printf '%s\n' "$4" >> "$FX/2026-10-26-build-TOOL-dTotalRecall-$1-deviation-$2.md"
}
mk 59 591 cl-dClosedLoop-0213@09982ca6
mk 59 592 TOOL-dTotalRecall-62@rev-2
mk 5 51 TOOL-dTotalRecall-5@rev-2
mk 89 891 TOOL-dTotalRecall-59@rev-2
printf '**Serves:** journal TOOL-dTotalRecall-94\n\nquotes deviation TOOL-dTotalRecall-59, pass(59) and `absorbs` is absent\n' > "$FX/2026-10-26-build-TOOL-dTotalRecall-94-ledger.md"
```

The probe then runs for units 59, 5, 89 and 590 with the tokens `pass(59)` and
`` `absorbs` is absent ``, and `mk 59 593 TOOL-dTotalRecall-62@rev-2 "- **Supersedes:** 2026-10-26-build-TOOL-dTotalRecall-59-deviation-592"`
adds the superseding record before unit 59 is counted again.

PINNED, measured 2026-10-26 at `32febccb6` with these exact commands: the re-keyed probe printed 2, 1,
1 and 0 for units 59, 5, 89 and 590, and 2 for unit 59 after the superseding record. Unit 90's probe
printed 1, 1, 0 and 0. `census "$FX" has_deviation` printed no `red` line, and
`census "$FX" has_deviation_90` printed `red census 59` and `red census 89`.

### Why order 37

Unit 90 runs at order 36. This unit consumes `TOOL-dTotalRecall-93`, which shares order 37, and the
dispatch verb holds a consumer until its producer of the same build is CLOSED or WONTDO
(`tools/unattended/unattended.sh:13691-13698`).

### Inventory

Minted: the functions `census` and `mk`, spec text only; at most one deviation record of
`TOOL-dTotalRecall-90`. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the record of S4)

### Alternatives rejected

- **Pin today's per-unit counts as the criterion.** The folder grows with every later pass, so a pinned
  count goes stale at the next record; the census derives both sides at the moment it runs.
- **Count files with the probe's own `read_record` parse.** A second reader sharing the probe's parse
  shares its blind spots, and a guard must not share state with what it guards.

## 5. Production-readiness checklist

- security — no surface. The fixture folder sits in the run's scratch.
- perf / scale — one probe call per unit holding a record, about ten today.
- error / empty / loading states — an empty folder prints no census line, which AC1 reads as red at
  this build's folder; a record whose stem the grammar refuses counts for no unit on either side.
- observability — every census line names its unit and both counts.
- risks — none beyond the probe's, which `TOOL-dTotalRecall-93` states.
- testing — AC1 to AC4 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `census memory/builds/dTotalRecall/build has_deviation` runs at this pass's base, it
  prints at least seven `census` lines and no `red census` line.
  Red when: a unit holding a record is counted short or over, or the census prints no line at all.
  figure: the seven units at `32febccb6` are PINNED in §4; at the pass both counts are DERIVED.
- **AC2** — When `census memory/builds/dTotalRecall/build has_deviation_90` runs at this pass's base, it
  prints a `red census` line for every unit a record's file stem names.
  Red when: unit 90's probe reads green over any real unit, which would mean the census cannot tell the
  two probes apart.
- **AC3** — When §4's fixture is built and `has_deviation "$FX" <n>` runs with the tokens `pass(59)`
  and `` `absorbs` is absent `` for units 59, 5, 89 and 590, it prints 2, 1, 1 and 0, and 2 for unit 59 after the superseding
  record is added.
  Red when: the unit-89 record departing from unit 59 counts for 59, a clause-departing record of 59 is
  missed, or the ledger is counted.
  fixture: the folder is made in the run's scratch by the pass; the tree holds none.
  figure: the counts are PINNED in §4, measured 2026-10-26.
- **AC4** — When `has_deviation memory/builds/dTotalRecall/build 90 'audit-89 id 28 ac3'` runs after the
  pass, it prints 1, and that record's Evidence names the census line of AC1.
  Red when: unit 90's AC3 stands as the probe's only observation with no record, or two records.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the census is a probe this spec spells, run over the build folder and a scratch fixture.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 28
  (HIGH, item H1, shared with id 1).

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-93`'s re-keyed `has_deviation`, which the census certifies, and the
build folder's own record `2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`, from which the
fixture is made so its shape is the real one. `python tools/codebase-map/reuse_lookup.py "assign a deviation record to its unit by its file name stem"`
ranked `read_records` (`tools/memory-tree/deviation_join.py:268`) among its SEAM candidates; the
census deliberately counts without it, by file name, so the guard and the guarded do not share a
parse. The recall query below found this audit's item H1, unit 90's AC3 fixture and the bug class it
names. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how is a probe's fixture shown to have the shape of the real records it guards" --terms "deviation record fixture real population census synthetic shape staged break has_deviation stem Departs from"`
