# TOOL-dTotalRecall-90 — units 82 to 84's S1 counts are read again with every line labelled and an unresolved pass printed red, and each decision they fed is made from its own line

**Status:** INPROGRESS · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-90-deviation-901.md](../build/2026-10-26-build-TOOL-dTotalRecall-90-deviation-901.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-90-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-90-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-90-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-90-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-90-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-90-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-91 TOOL-dTotalRecall-89 TOOL-dTotalRecall-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 77 to 88
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md`)
confirmed finding **id 22 at HIGH**, its item **H2**, alone in that item. It is one defect with id 10
(item M5, MEDIUM), graded on a narrower consequence and taken by the batch `TOOL-dTotalRecall-92`.

`TOOL-dTotalRecall-81` §4 defines `pass_of` to echo `red <n> no pass commit` on stdout and return 1. As
audited, units 82, 83 and 84 each spelled their S1 read as `P=$(pass_of N) && read_at ...` with no `||`
arm, in their §4 "The re-read". The substitution captures the red line into `P` and `&&` skips
`read_at`, so nothing prints. Unit 83's two `653bed738` liveness reads still printed, and its §4 called
the first printed line S1. Its S1 then read 0 from the liveness line over spec 59, the value that owes a
record of unit 59, so an unresolved `pass(59)` wrote the fabricated record unit 83 exists to stop.

Re-grounded at `6d0627dd6`: spec 83 rev-4 and spec 84 rev-3 read through `if ... then ... else echo`, so
an unresolved pass prints its red there, and spec 83 takes S1 by the sha it prints. Unit 82, CLOSED, ran
the `&&` form, its pass resolved and it printed its one line. No read names itself: spec 84 §4 still
takes the first line as S1, and no block is red on a missing line. Each of the three passes resolves, so
each count is settled and §4 pins it.

This unit reads the three S1 counts again through one labelled read: every line it prints starts with
the read's label, an unresolved pass is a labelled red line, and the block is red when it prints fewer
labelled lines than it has reads. It sets each labelled count beside the S1 its unit recorded, re-makes
that unit's decision from the labelled line and writes each record still owed once. It repairs
`TOOL-dTotalRecall-83`, at order 36, one above that unit's 35, which also follows unit 82 at 22 and unit
84 at 35.

## 2. Scope (IN)

- **S1** — The labelled read. §4's `s1` takes a label, a unit, a parent mark, a spec and a strings
  file. It resolves the unit's pass through `pass_of` and reads the spec there through `read_at`, both
  `TOOL-dTotalRecall-81`'s, and prefixes every line it prints with the label. Where `pass_of` fails it
  prints `<label> red <n> no pass commit`, and where `read_at` fails its red line carries the label.
  Observed by AC1.
- **S2** — The block. §4's seven reads are labelled `s1-67`, `s1-59` and `s1-46`, the three units' S1,
  and `live-59`, `live-62`, `live-46` and `live-64`, the liveness reads of units 83 and 84 at
  `653bed738`. Every label leads exactly one line. Observed by AC1.
- **S3** — The comparison. The ledger sets each `s1-*` line beside the S1 its unit's AC1 ledger line
  recorded. Where a unit recorded no S1, or a value its labelled line does not give, the unit's
  decision is made again from the labelled line by its own table: spec 82 §4 "The decision table",
  spec 83 §4 "The decision table" and spec 84 §4 "The comparison". A red `s1-*` line decides nothing,
  and the ledger names it as unresolved. §4's "What is settled" is re-observed, and nothing is written
  for a row it settles. Observed by AC2.
- **S4** — The records, once. Where the re-made decision owes a record its unit did not write, this
  pass writes it. Where its unit wrote a record the re-made decision does not owe, the ledger names
  that record by path, and a deviation record of the unit whose pass wrote it names the line it was
  decided from. Each record is written only where §4's `has_deviation` prints 0 for its row of §4's
  "The guards", by §4's recipe. At `6d0627dd6` only records of units 74, 83 and 84 can still be owed.
  The writes for units 59, 67 and 70 are cut for the reason §4's "What is settled" gives, and their
  guards are still run. Observed by AC2.
- **S5** — The write-once probe. §4's `has_deviation` counts, in a folder of the working tree, the
  records of one unit whose Evidence holds every token given and that no other record's
  `**Supersedes:**` names. It parses only `*-deviation-*.md` files, tracked or not, through
  `tools/memory-tree/deviation_join.py#read_record`. Observed by AC3.

## 3. Non-goals (OUT)

- The liveness of an unresolved pass as a `red` line, and the ledger naming the swallowed cause for
  each of units 82 to 84 (item M5, id 10): the batch `TOOL-dTotalRecall-92`, which reads through `s1`.
- `read_at` and `pass_of` themselves: `TOOL-dTotalRecall-81`.
- Unit 88's AC13 over the records of unit 59 (item H1, id 1): `TOOL-dTotalRecall-89`.
- Editing the specs of units 82, 83 or 84, each frozen once its unit builds.
- `has_deviation`'s key, the record's Departs from address, and the census over the real records:
  `TOOL-dTotalRecall-93`, which re-keys it, and `TOOL-dTotalRecall-94`, which copies it verbatim as its
  red arm.
- The probe-fence lint the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-82` — its S1 line, its AC1 record and its decision table, which this unit re-makes from a labelled line
- **consumes-from** `TOOL-dTotalRecall-83` — its S1 line, its decision table and any record of unit 59 its pass wrote, which this unit re-decides from a labelled line
- **consumes-from** `TOOL-dTotalRecall-84` — its S1 line and its comparison, which this unit re-makes from a labelled line
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, which `s1` calls; without them no revision is verified
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4's records are written through
- **hands-off** `TOOL-dTotalRecall-89` — `s1` and `has_deviation`, through which that unit re-derives unit 83's S1 and counts the records of unit 59
- **hands-off** `TOOL-dTotalRecall-91` — `has_deviation` and §4's record recipe, through which that unit writes its records once
- **hands-off** `TOOL-dTotalRecall-92` — `s1`, `has_deviation` and §4's record recipe, which that batch reads through for its items of ids 10, 12, 15, 20 and 24
- **hands-off** `TOOL-dTotalRecall-93` — `has_deviation`, its record recipe and the write-once guards its S4 ran, which that unit re-keys on the record's own unit and runs again (the round-1 audit of units 89 to 92, id 1)
- **hands-off** `TOOL-dTotalRecall-94` — its probe and its AC3 answer, which that unit's census sees red and records against the real records (the round-1 audit of units 89 to 92, id 28)
- **hands-off** `TOOL-dTotalRecall-95` — its record recipe and the records of unit 59 its S4 wrote, to which that unit adds `pass(59)` as the departure's key (the round-1 audit of units 89 to 92, id 2)
- **hands-off** `TOOL-dTotalRecall-100` — its record recipe and its cites, which that batch reads and re-points (the round-1 audit of units 89 to 92, ids 11, 19)

## 4. Design

### The labelled read

```bash
# run from the repository root, with unit 81 §4's first bash fence sourced from a file under $SCRATCH
s1() {  # label · unit · parent mark ('' or '^') · spec · strings file -> labelled lines only
  local P; P=$(pass_of "$2") || { echo "$1 $P"; return 0; }
  read_at "$P$3" "$4" "$5" | sed "s/^/$1 /"
}
```

`P` holds `pass_of`'s red line where it fails, so the label prefixes the cause. `read_at`'s own red
line passes through the same `sed`. The return status is not read: the line count is the verdict.

### The block

```bash
# the strings files are unit 82 §4's, unit 83 §4's and unit 84 §4's, each written by a quoted heredoc
s1 s1-67 67 ''  57 "$SCRATCH/s82.txt"
s1 s1-59 59 '^' 59 "$SCRATCH/s83.txt"
s1 s1-46 46 '^' 46 "$SCRATCH/s84.txt"
read_at 653bed738 59 "$SCRATCH/s83.txt" | sed 's/^/live-59 /'
read_at 653bed738 62 "$SCRATCH/s83.txt" | sed 's/^/live-62 /'
read_at 653bed738 46 "$SCRATCH/s84.txt" | sed 's/^/live-46 /'
read_at 653bed738 64 "$SCRATCH/s84.txt" | sed 's/^/live-64 /'
```

A value is taken from the line its label leads, never from a line's position.

The two red reads, which print through the same `s1` and are no part of the block's seven:

```bash
s1 s1-999 999 '' 57  "$SCRATCH/s82.txt"
s1 s1-bad 67  '' 999 "$SCRATCH/s82.txt"
```

PINNED 2026-11-24 at `6d0627dd6`, these exact reads. Each count line ends in the counted string:

| Label | Printed (PINNED 2026-11-24) |
|---|---|
| `s1-67` | `56390bab8cce52668b940893b8378621df78e4b7 1` |
| `s1-59` | `206422580b7363ab9582e37ffe7de7c25773a721 1` |
| `s1-46` | `254057fa6d5bbc19cd48329737487c88a10b0085 0` |
| `live-59`, `live-62`, `live-46`, `live-64` | `653bed738685c8d41ee71fbf740a5e3654bdd703` with 0, 1, 1 and 0 |
| `s1-999` | `red 999 no pass commit` |
| `s1-bad` | `red no blob at 56390bab8cce52668b940893b8378621df78e4b7:` and spec 999's path |

The four `live-*` counts are the ones measured 2026-10-26 at `1e255b0c6`, where the three `s1-*` lines
printed their reds because no pass had been made. `pass_of` printed `47afc89374e5` for unit 59 and
`63f283ddd383` for unit 46, abbreviated (PINNED 2026-11-24), the commits whose parents the two `^` reads
took.

### What is settled

| Line | The unit's own record | Decision |
|---|---|---|
| `s1-67` reads 1 | unit 82's AC1 ledger line: the same sha and 1 | no record of unit 67, spec 82's second row |
| `s1-59` reads 1 | spec 83 rev-4 §4 pins the same sha and 1 | no record of unit 59, spec 83's third row |
| `s1-46` reads 0 | unit 70's AC8 ledger line: 0; spec 84 rev-3 §4 pins the same sha and 0 | no record of unit 70, spec 84's second row |

Each count is a property of a blob that cannot move, and units 70 and 82 are CLOSED with the figures
shown, in `2026-11-24-build-TOOL-dTotalRecall-70-1-acceptance-ledger.md` and
`2026-11-22-build-TOOL-dTotalRecall-82-1-acceptance-ledger.md`. What stays open until units 74, 83 and 84
pass is what their ledgers record. A figure of unit 74 that differs from its labelled line owes the record
of unit 74 that specs 83 and 84 state. An S1 of unit 83 or 84 that differs from its labelled line owes a
record of that unit. Unit 74's sha is twelve digits long and is compared as a prefix. A record of unit 59
asserting the departure would be an unowed one, spec 83's fourth row.

### The write-once probe

```bash
has_deviation() {  # folder · unit number · token... -> count of live records of that unit holding every token
  python - "$@" <<'PROBE'
import glob, os, pathlib, sys
sys.path.insert(0, 'tools/memory-tree')
import deviation_join
folder, unit, tokens = sys.argv[1], 'TOOL-dTotalRecall-' + sys.argv[2], sys.argv[3:]
recs = [deviation_join.read_record(p.replace(os.sep, '/'), pathlib.Path(p).read_text(encoding='utf-8'))
        for p in sorted(glob.glob(os.path.join(folder, '*-deviation-*.md')))]
gone = {r['supersedes'] for r in recs if r['supersedes']}
print(sum(1 for r in recs if r['id'] not in gone and r['address'].startswith(unit + '@')
          and all(t in (r['evidence'] or '') for t in tokens)))
PROBE
}
```

The `@` after the unit keeps unit 5 from matching unit 59. A ledger that quotes a record's Serves
line is not a `*-deviation-*.md` file and is never counted. The glob reads the working tree, so a
record written and not yet committed is counted. No token may hold a single quote.

PINNED, measured 2026-10-26 and again 2026-11-24 at `6d0627dd6` with this probe over a scratch folder
holding one record of unit 59 and a ledger quoting its Serves line and token: for `pass(59)` with
`audit-77 id 22 s1-59` it printed 1, and 1 again after a second record superseding the first was added.
With the second record superseding none it printed 2 (PINNED 2026-11-24). It printed 0 for
`audit-77 id 1` with a trailing space and for units 590 and 5 (PINNED 2026-11-24).

The key is the record's Departs from address, so a record that departs from the build or from a clause is
never counted: 72 of the folder's 150 deviation records depart from their own unit (DERIVED 2026-11-24 at
`6d0627dd6`, by `read_record` over the glob). Every record a guard below looks for departs from its own
unit's revision, by the recipe here and by specs 83 and 84, so the key reads it. The wider key is
`TOOL-dTotalRecall-93`'s.

### The guards

```bash
B=memory/builds/dTotalRecall/build
has_deviation "$B" 67 'TOOL-dTotalRecall-56'
has_deviation "$B" 59 '`absorbs` is absent'
has_deviation "$B" 70 'SUFFIX_RE'
has_deviation "$B" 74 's1-59'
has_deviation "$B" 74 'SUFFIX_RE'
has_deviation "$B" 83 'audit-77 id 22 s1-59'
has_deviation "$B" 84 'audit-77 id 22 s1-46'
```

The tokens of the first five rows are ones specs 82, 83 and 84 §4 put in a record's Evidence, so a record
its own unit wrote is counted and is not written a second time; an `audit-77` token alone would read 0
over it. Each row printed 0 at `6d0627dd6` (PINNED 2026-11-24, these commands). With `spec changed at` for
the token, units 70 and 83 printed 1 each (PINNED 2026-11-24), so the probe is seen both ways over the
real folder. A record naming an unowed one is guarded by the unit whose pass wrote that one and the token
`audit-77 id 22 <label>`. The ledger names each guard it ran by its unit and token.

### The deviation record

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id> --title <text>`,
which refuses a missing `--title` or required field (`tools/memory-tree/build_records.py#write_new_record`),
with one `--field` per required name of the deviation entry of `tools/memory-tree/build_records.py#KINDS`:

| Field | Value |
|---|---|
| Departs from | `TOOL-dTotalRecall-<n>@rev-<N> [§6 AC1]`, the rev in that unit's status header at its pass commit |
| Hand-off | `spec-to-code` |
| Before | the value the unit recorded, on one line holding no pipe character |
| After | the value the labelled read gives, on one line holding no pipe character |
| Cause | `review finding` |
| Reason | one sentence naming the audit item |
| Evidence | the labelled line, the ledger path, the guard's token and the token `audit-77 id <report id> <label>` |
| Risk | `loosening` where the recorded figure certifies a reading the blob does not hold, as specs 83 and 84 spell it; `stricter` where the verified read turns an outcome red; `editorial` where it corrects a stated value only |
| Approver | `author`, the pass of the writing unit, under the chain's `author-recorded` value (`tools/memory-tree/deviation_join.py#HOST_APPROVAL`, `PLAY-dClosedLoop-4`) |
| Follow-through | `new unit TOOL-dTotalRecall-<writing unit>`, the grammar of `tools/memory-tree/deviation_join.py#FOLLOW` |
| Caused-by | `TOOL-dTotalRecall-<writing unit>` |

A record correcting another adds `**Supersedes:**` naming that record's stem
(`tools/memory-tree/deviation_join.py#SUPERSEDES`).

### Why order 36

Units 83 and 84 record their S1 at order 35, and unit 82, CLOSED, recorded its own at 22. The §3 edges run
those passes first: `--dispatch` refuses a unit while a unit of its build it consumes from is neither
CLOSED nor WONTDO (`tools/unattended/unattended.sh#verb_dispatch`, reading
`tools/unattended/lib-unattended.sh#read_consumes_from`). Unit 88, at order 37, rests its S19 on unit 83's
decision.

### Inventory

Minted: the probe functions `s1` and `has_deviation`, spec text only; deviation records only where a
re-made decision owes one, at most one per departure, of units 74, 83 and 84. Naming cell: none, no
product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S4)

### Alternatives rejected

- **`pass_of` writing its red line to stderr as well.** The report's alternative. It still leaves
  unit 83 taking S1 by position, so a red read beside a printed liveness line is mistaken again.
  Labels make the position irrelevant.
- **The `else echo` arm of specs 83 and 84, taken as the whole fix.** It prints the cause, and a reader
  counting by position still has to know how many lines each read printed. One label per read is the
  same fix with the count made checkable.
- **Guard each record by its `audit-77` token alone, as rev-2 did.** A record unit 83 or 84 wrote carries
  no such token, so the guard reads 0 over it and this pass writes the departure twice.
- **`git grep -l` over the build folder as the write-once guard, as units 79 to 88 wrote it at
  their audit.** It
  reads tracked files only and lists any ledger that quotes the Serves token (items M12 and M13).

## 5. Production-readiness checklist

- security — no surface. The strings files and the fixture folder sit in the run's scratch.
- perf / scale — three pass-commit walks and seven blob reads, 8 s with the red reads (PINNED 2026-11-24, node a).
- error / empty / loading states — an unresolved pass and an absent blob each print a labelled red
  line; a missing label is the block's red. Once a run-state rotation moves a unit's dispatch row out of
  `RUN.md`, `pass_of` is that red, as unit 81 §5 states.
- observability — every line names its read; the ledger sets each beside the unit's own record.
- risks — a unit whose ledger records S1 only in prose is read by eye, as that unit's own table
  states. The probe's key reads only records departing from their own unit, as §4 states.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's block runs at this pass's base, each of the seven labels `s1-67`, `s1-59`,
  `s1-46`, `live-59`, `live-62`, `live-46` and `live-64` leads exactly one line, each holding the sha and
  count §4 pins for it. The two red reads print one line each, `s1-999 red 999 no pass commit` and one
  opening `s1-bad red no blob at`.
  Red when: the block prints fewer labelled lines than its seven reads, a line carries no label, a red
  read prints nothing or a count, or a value is taken from a line by position.
  figure: the shas and counts are PINNED in §4, measured 2026-11-24; the pass's own lines are DERIVED by
  it.
- **AC2** — When `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-90" -- memory/builds/dTotalRecall/build`
  runs after the pass, the ledger it names has an AC2 line setting each `s1-*` line beside the S1 of units
  82, 83 and 84, quoted with its ledger's file name, with each decision and each guard by unit and token.
  For a guard whose record a decision owes, `has_deviation` over `memory/builds/dTotalRecall/build` prints
  1; for every other row of §4's "The guards" it prints 0, or the ledger names by path each record it
  counts as unowed.
  Red when: a decision is re-made from a red line, an owed record is absent, a record is written that no
  decision owes, or `has_deviation` prints 2 or more for one guard.
- **AC3** — When `has_deviation` runs over a scratch folder holding one record of unit 59 with the
  token `audit-77 id 22 s1-59` and a ledger quoting that record's Serves line and token, it prints 1,
  and it prints 1 again after an uncommitted second record whose `**Supersedes:**` names the first is
  added. With the `**Supersedes:**` line taken out of that second record it prints 2.
  Red when: the ledger is counted, the uncommitted record is missed, or a superseded record counts.
  figure: the three counts are PINNED in §4, measured 2026-11-24.
  fixture: the folder is made in the run's scratch by the pass; the tree holds none.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's labelled block, its two red reads and the probe's fixture folder.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 77 to 88, id 22
  (HIGH, item H2), one defect with id 10 (item M5).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-93, TOOL-dTotalRecall-94, TOOL-dTotalRecall-95, TOOL-dTotalRecall-100, each the other end of an edge a
  unit the round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.
- rev-3 · 2026-11-24 · §1 S3 S4 S5 §3 §4 §5 AC1 AC2 AC3 §7 §10 · re-grounded at HEAD `6d0627dd6` per
  `2026-11-24-prompt-TOOL-dTotalRecall-90-reground-brief`, over spec 82 rev-3, 83 rev-4 and 84 rev-3: the
  Goal's `&&` form is history in specs 83 and 84 and the pin that no unit has a pass commit is gone; all
  seven lines are pinned, the writes for units 59, 67 and 70 are settled and cut, and the two red reads
  observe what a resolved pass hides. Each guard is keyed on the Evidence its own unit writes, as an
  `audit-77` token alone reads 0 over it. The recipe names `--title` and its fields by symbol; line cites
  became symbols or sections; AC2 reads untracked files.

## 10. Reuse audit

The seams, re-read at `6d0627dd6`, are `TOOL-dTotalRecall-81` rev-4's `pass_of` and `read_at`, CLOSED, the
record door `gov_record.py new deviation` of `TOOL-dTotalRecall-2`, CLOSED, and the deviation format's own
parser `tools/memory-tree/deviation_join.py#read_record`, whose `address`, `evidence` and `supersedes` keys
the probe reads. `python tools/codebase-map/reuse_lookup.py "count deviation records of one unit by a computed key over the working tree"`
ranked `tools/memory-tree/deviation_join.py#read_records` among its SEAM candidates; it lists tracked and
staged files only, so the probe calls the per-file `read_record` over a working-tree glob instead. Re-run
2026-11-24 it ranks both again. The recall query below found this audit's items M12, M13 and L5, specs 82,
83, 85 and 86, whose `git grep -l` guards this probe replaces, and the `TOOL-dTrueNorth-18` ledger that
probed `read_record`'s `**Supersedes:**` grammar. Re-run 2026-11-24 it adds no reader of this shape. No
existing seam fits beyond them. `tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder
walks of `record_causes.py#check_cause_writers` and `record_kinds.py#check_alias_compares` are no seam
here: this unit reads no marker and no registry.

Recall terms used: `python tools/memory-recall/query.py "how does a write-once guard find a deviation record already written, including one not yet committed" --terms "deviation record written once untracked git grep Serves anchored evidence token read_record Supersedes duplicate door"`
