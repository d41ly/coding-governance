# TOOL-dTotalRecall-90 — units 82 to 84's S1 counts are read again with every line labelled and an unresolved pass printed red, and each decision they fed is made from its own line

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-91 TOOL-dTotalRecall-89 TOOL-dTotalRecall-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 77 to 88
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md`)
confirmed finding **id 22 at HIGH**, its item **H2**, alone in that item. It is one defect with id 10
(item M5, MEDIUM), graded on a narrower consequence and taken by the batch `TOOL-dTotalRecall-92`.

`TOOL-dTotalRecall-81` §4 defines `pass_of` to echo `red <n> no pass commit` on stdout and return 1.
Units 82, 83 and 84 each spell their S1 read as `P=$(pass_of N) && read_at ...` with no `||` arm
(spec 82 line 71, spec 83 line 76, spec 84 line 70). The substitution captures the red line into `P`
and `&&` skips `read_at`, so nothing prints. Re-probed at `1e255b0c6`, where no unit has a pass
commit: the form printed nothing, exited 1, and left `P` holding `red 59 no pass commit`. Unit 83's
two `653bed738` liveness reads still print, and spec 83 line 80 calls the first printed line S1. Its
S1 then reads 0 from the liveness line over spec 59, the value that owes a record of unit 59, so an
unresolved `pass(59)` writes the fabricated record unit 83 exists to stop. Unit 82 prints nothing.

This unit reads the three S1 counts again through one labelled read: every line it prints starts
with the read's label, an unresolved pass is a labelled red line, and the block is red when it
prints fewer labelled lines than it has reads. It sets each labelled count beside the S1 its unit
recorded and re-makes that unit's decision from the labelled line, writing each owed record once.
It repairs `TOOL-dTotalRecall-83`, at order 36, one above that unit's 35, which also follows unit 82
at 22 and unit 84 at 35.

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
  and the ledger names it as unresolved. Observed by AC2.
- **S4** — The records, once. Where the re-made decision owes a record its unit did not write, this
  pass writes it. Where its unit wrote a record the re-made decision does not owe, the ledger names
  that record by path, and a deviation record of the unit whose pass wrote it names the line it was
  decided from. Each record is written only where §4's `has_deviation` prints 0 for its unit and
  token, by §4's recipe. Observed by AC2.
- **S5** — The write-once probe. §4's `has_deviation` counts, in a folder of the working tree, the
  records of one unit whose Evidence holds every token given and that no other record's
  `**Supersedes:**` names. It parses only `*-deviation-*.md` files, tracked or not, through
  `deviation_join.read_record` (`tools/memory-tree/deviation_join.py:212`). Observed by AC3.

## 3. Non-goals (OUT)

- The liveness of an unresolved pass as a `red` line, and the ledger naming the swallowed cause for
  each of units 82 to 84 (item M5, id 10): the batch `TOOL-dTotalRecall-92`, which reads through `s1`.
- `read_at` and `pass_of` themselves: `TOOL-dTotalRecall-81`.
- Unit 88's AC13 over the records of unit 59 (item H1, id 1): `TOOL-dTotalRecall-89`.
- Editing the specs of units 82, 83 or 84, each frozen once its unit builds.
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
# run from the repository root, with unit 81 §4's pass_of and read_at sourced
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

PINNED, measured 2026-10-26 at `1e255b0c6` with these exact reads, before any pass commit: the three
`s1-*` lines printed `s1-67 red 67 no pass commit`, `s1-59 red 59 no pass commit` and
`s1-46 red 46 no pass commit`. The four `live-*` lines printed 0, 1, 1 and 0 with the sha
`653bed738685c8d41ee71fbf740a5e3654bdd703`. Spec 83's unguarded line printed nothing and exited 1.

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

PINNED, measured 2026-10-26 with this probe over a scratch folder holding one record of unit 59 and a
ledger quoting its Serves line and token: it printed 1 for `pass(59)` with `audit-77 id 22 s1-59`, 0
for `audit-77 id 1`, 1 again after a second record superseding the first was added, and 0 for unit
590.

### The deviation record

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id>`
with one `--field` for each of the eleven REQUIRED names of `tools/memory-tree/deviation_join.py:146`:

| Field | Value |
|---|---|
| Departs from | `TOOL-dTotalRecall-<n>@rev-<N>`, the rev in that unit's status header at its pass commit |
| Hand-off | `spec-to-code` |
| Before | the value the unit recorded, on one line holding no pipe character |
| After | the value the labelled read gives, on one line holding no pipe character |
| Cause | `review finding` |
| Reason | one sentence naming the audit item |
| Evidence | the labelled line, the ledger path, and the token `audit-77 id <report id> <label>` |
| Risk | `stricter` where the verified read turns an outcome red, `editorial` where it corrects a stated value only (`RISKS`, `:150`) |
| Approver | `author`, the pass of the writing unit, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`) |
| Follow-through | `new unit TOOL-dTotalRecall-<writing unit>`, the `FOLLOW` grammar of `:157` |
| Caused-by | `TOOL-dTotalRecall-<writing unit>` |

A record correcting another adds `**Supersedes:**` naming that record's stem (`:161`).

### Why order 36

Units 83 and 84 record their S1 at order 35 and unit 82 at 22. The driver dispatches strictly in
sequence inside one order value, sorted by id (`tools/workflows/unattended-build.js:76-80`), so this
unit runs after units 77 to 86 at 36 and before unit 88 at 37, whose S19 rests on unit 83's decision.

### Inventory

Minted: the probe functions `s1` and `has_deviation`, spec text only; deviation records only where a
re-made decision owes one, at most one per departure, of units 59, 67, 70, 74, 82, 83 and 84. Naming
cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S4)

### Alternatives rejected

- **`pass_of` writing its red line to stderr as well.** The report's alternative. It still leaves
  unit 83 taking S1 by position, so a red read beside a printed liveness line is mistaken again.
  Labels make the position irrelevant.
- **Append `|| echo` to each unit's line, as spec 85 does.** It prints the cause, and a reader
  counting by position still has to know how many lines each read printed. One label per read is the
  same fix with the count made checkable.
- **`git grep -l` over the build folder as the write-once guard, as units 79 to 88 wrote it.** It
  reads tracked files only and lists any ledger that quotes the Serves token (items M12 and M13).

## 5. Production-readiness checklist

- security — no surface. The strings files and the fixture folder sit in the run's scratch.
- perf / scale — three pass-commit walks and seven blob reads.
- error / empty / loading states — an unresolved pass and an absent blob each print a labelled red
  line; a missing label is the block's red.
- observability — every line names its read; the ledger sets each beside the unit's own record.
- risks — a unit whose ledger records S1 only in prose is read by eye, as that unit's own table
  states.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's block runs at this pass's base, each of the seven labels `s1-67`, `s1-59`,
  `s1-46`, `live-59`, `live-62`, `live-46` and `live-64` leads exactly one line, and the four `live-*`
  lines print 0, 1, 1 and 0 with the sha `653bed738685`.
  Red when: the block prints fewer labelled lines than its seven reads, or a value is taken from a
  line by position.
  figure: the liveness counts are PINNED in §4, measured 2026-10-26; the `s1-*` counts are DERIVED.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-90" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line sets each `s1-*` line beside the S1 of units 82, 83 and 84 and
  names each re-made decision. For every record that decision owes, `has_deviation` over
  `memory/builds/dTotalRecall/build` prints 1 for its unit and token.
  Red when: a decision is re-made from a red line, an owed record is absent, or `has_deviation`
  prints 2 or more.
- **AC3** — When `has_deviation` runs over a scratch folder holding one record of unit 59 with the
  token `audit-77 id 22 s1-59` and a ledger quoting that record's Serves line and token, it prints 1,
  and it prints 1 again after an uncommitted second record whose `**Supersedes:**` names the first is
  added.
  Red when: the ledger is counted, the uncommitted record is missed, or a superseded record counts.
  fixture: the folder is made in the run's scratch by the pass; the tree holds none.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's labelled block and the probe's fixture folder.

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

## 10. Reuse audit

The seams are `TOOL-dTotalRecall-81`'s `pass_of` and `read_at`, and the deviation format's own
parser `deviation_join.read_record` (`tools/memory-tree/deviation_join.py:212`), whose `address`,
`evidence` and `supersedes` keys the probe reads. `python tools/codebase-map/reuse_lookup.py "count deviation records of one unit by a computed key over the working tree"`
ranked `read_records` (`deviation_join.py:268`) among its SEAM candidates; it lists tracked and
staged files only (`:268-283`), so the probe calls the per-file `read_record` over a working-tree glob
instead. The recall query below found this audit's items M12, M13 and L5, specs 82, 83, 85 and 86,
whose `git grep -l` guards this probe replaces, and the `TOOL-dTrueNorth-18` ledger that probed
`read_record`'s `**Supersedes:**` grammar. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a write-once guard find a deviation record already written, including one not yet committed" --terms "deviation record written once untracked git grep Serves anchored evidence token read_record Supersedes duplicate door"`
