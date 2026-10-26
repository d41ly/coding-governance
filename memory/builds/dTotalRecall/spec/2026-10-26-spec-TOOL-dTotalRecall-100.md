# TOOL-dTotalRecall-100 — the round-9 minors: each reading of units 89 to 92 that a dropped line, a stale cite or a loose key could mislead is made once at the tip, and each record it decides is written once

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 41 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
exited CONVERGED with 27 confirmed findings. Its seven high ids are units 93 to 99: ids 1 and 28 are
`TOOL-dTotalRecall-93` and `TOOL-dTotalRecall-94`, id 2 is `TOOL-dTotalRecall-95`, ids 12 and 30 are
`TOOL-dTotalRecall-96` and `TOOL-dTotalRecall-97`, id 15 is `TOOL-dTotalRecall-98` and id 29 is
`TOOL-dTotalRecall-99`. This unit is the batch BUILD-METHOD M4 makes of the rest:

- the 14 MEDIUM findings, ids 3, 4, 6, 7, 13, 14, 19, 21, 23, 24, 25, 26, 31 and 32 (items M1 to M9);
- the 6 LOW findings, ids 9, 10, 11, 16, 17 and 22 (items L1 to L5).

Each id keeps its own scope item. Ids 3 and 23 share item M1, ids 13 and 19 item M5, ids 14, 26 and 31
item M6, ids 25 and 32 item M9 and ids 11 and 17 item L3; each takes its own facet of its item. Ids 13
and 19 are one defect with id 2 (H2), graded apart. The minors land on units 89 to 92, so this unit
repairs none in particular and builds after every unit: order 41, above the 40 units 98 and 99 hold.
The review record holds each item's text.

## 2. Scope (IN)

Every item states its change to the unit it lands on, as that unit was built. A spec is frozen once
its unit builds; a reading made wrongly is made again here, and a departure is a deviation record.
Every revision read goes through `TOOL-dTotalRecall-81`'s `pass_of`. Every record is written by
`TOOL-dTotalRecall-90` §4's recipe, its Evidence carrying the token `audit-89 id <report id> s<item>`,
only where `TOOL-dTotalRecall-93`'s `has_deviation` prints 0 for its unit and that token. Two records
of one departure are made one by `TOOL-dTotalRecall-93` §4's correcting record. "The scan" is §4's
amended `tip_scan`, and `tip_check` is `TOOL-dTotalRecall-99`'s over it.

- **S1** — id 3 (M1). The scan prints `malformed` only for a live record, and
  `malformed-superseded` for a record another supersedes, so the remedy unit 92's S8 prescribes, a
  correcting record, clears its AC8. Observed by AC1.
- **S2** — id 23 (M1). No pass cleared unit 92's AC8 by editing a record by hand: §4's `edited`
  listing names every record a commit of this build modified, each beside its commit's subject. A
  modification by a commit that is not one of the restores of unit 92's S11, unit 98's S3 or S12 below
  gets a deviation record of the unit whose pass made it. Observed by AC2.
- **S3** — id 4 (M2). A duplicate pair unit 92's S11 or S22 made one is made one by a record whose
  fields are `TOOL-dTotalRecall-93` §4's, so the correcting record shares no `dup` key. Where the scan
  at this pass's base prints a `dup` line naming a correcting record of unit 92, that pair is made one
  again by §4 of unit 93. Observed by AC3.
- **S4** — id 6 (M3). A record of `TOOL-dTotalRecall-69` that unit 91 wrote from a
  `no-status-line` verdict, where `TOOL-dTotalRecall-97`'s `c5_input` places a status line for `p69`
  in unit 80's ledger, is withdrawn by §4's withdrawing record: the read was sound and only unit 91's
  parse failed. Observed by AC4.
- **S5** — id 7 (M4). The manifest unit 69's checker read carried its marker:
  `git show "$(pass_of 69):memory/guides/SESSION-KICKOFF.md" | grep -c 'kickoff-manifest:'` prints
  at least 1, the first of the checker's `MANIFEST_LOCATIONS`
  (`skills/session-kickoff/manifest-check.sh:64`). Where it prints 0 and `.claude/SESSION-KICKOFF.md`
  carries no marker at that commit either, the checker skipped every check and exited 0 (`:1242`), so
  `TOOL-dTotalRecall-96`'s answer to unit 69's AC1 is restated as unresolved and a record of unit 69
  names it. Observed by AC5.
- **S6** — id 13 (M5). One live record names unit 59's absorbs departure at the tip, whichever key
  counts it: `has_deviation` for unit 59 with the string `` `absorbs` is absent `` prints at most 1
  after units 89 and 92 have written. Observed by AC6.
- **S7** — id 19 (M5). The key `TOOL-dTotalRecall-95` set still holds at the tip: its `key59` prints
  no `missing` line and two equal numbers over the build folder, after unit 89's S4 and unit 92's
  records. A record written after order 37 without `pass(59)` gets unit 95's re-stating record.
  Observed by AC7.
- **S8** — id 14 (M6). Unit 89's ancestry check, made again with three outcomes: §4's `ancestry`
  prints `before-p83` on exit status 1, `at-or-after-p83` on 0 and `red ancestry rc=<n>` on anything
  else, for each record of unit 59 that unit 89 counts. Observed by AC8.
- **S9** — id 26 (M6). A record with no adding commit reads `at-or-after-p83 untracked`, as written at
  the pass. Observed by AC9.
- **S10** — id 31 (M6). Where `pass_of 83` prints a red line, the walk prints
  `rec <path> ungraded p83 red` and unit 89's AC13 answer on the S1-at-least-1 arm reads unresolved.
  Where unit 89 answered that arm green with a red `p83` line, or without a `before-p83` line for every
  counted record, a deviation record of `TOOL-dTotalRecall-89` names it. Observed by AC10.
- **S11** — id 21 (M7). The walk of S8 to S10 runs over the records `has_deviation --paths` counts for
  unit 59 with `pass(59)` and the string, and over no second selection. Observed by AC11.
- **S12** — id 24 (M8). A restore whose path is taken, or whose `<n>` a live record already carries,
  puts the record back with its bytes unchanged under the next free `<n>` of the folder, the door's
  rule (spec 2 §4 "Minting"), by `git show "$C^:$P" > <new path>`. It never overwrites. Each restore
  `TOOL-dTotalRecall-98` refused, and each restore unit 92 made over a path that existed, is made so.
  Observed by AC12.
- **S13** — id 25 (M9). Unit 92's sweep is complete: every population unit leads a
  `<n> <sha> rc=<n>` line in unit 78's block or in a sweep file, and a unit led only by a `red` line
  is swept again by §4's corrected loop, which keeps a unit's file only once it holds a verdict line.
  Observed by AC13.
  permission: the checker is the `kickoff-manifest ratchet` leg's argv, which no role agent may run
  (`.claude/roles.json`); the main loop runs the loop and records its files under a `Pass: none` commit.
- **S14** — id 32 (M9). No scratch worktree of the sweep outlives it: the corrected loop stops when
  `add_scratch_worktree` fails and removes its worktree on exit or signal, and at the tip no worktree
  path and no common-directory entry is `gate-mc92` or `gate-mc100`. Observed by AC14.
  **Readers:** by name: no name retires, the item removing only the scratch worktrees the sweeps
  added, whose paths are spelled by `add_scratch_worktree` and `remove_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`, `:63`) and their callers `tools/run-gates/post-merge.sh`
  and `tools/run-gates/run-gates.sh` · by value: `check_pockets`, minted by `TOOL-dTotalRecall-18`,
  which reds a common-directory entry no witness row names.
- **S15** — id 9 (L1). The needle scan of unit 92 reads every needle a `read_at` call of this build
  consumes: the `<<'STRINGS'` blocks, the String column of spec 86 §4's table, and the edge strings of
  units 71 and 72 §4 that spec 88's AC1 and AC20 count. A planted block with a double space prints a
  `run` line. Observed by AC15.
- **S16** — id 10 (L2). Unit 88's AC19 predicate runs over every spec in the build folder, not units
  77 to 88: it prints 0 for every spec of units 77 to 100 but spec 92, whose one mid-line triple
  backtick, in its §4 span script, the ledger names. This spec spells that sequence as `chr(96) * 3`
  where it needs it. Observed by AC16.
- **S17** — id 11 (L3). The ledger re-points spec 90's cites: each of its cites into specs 82, 83 and
  84 and into `tools/workflows/unattended-build.js` is set beside the line `grep -n` finds its quoted
  token on at this pass's base. The sort by order and id is the comparator, not the comment at
  `:76-80`. Observed by AC17.
- **S18** — id 17 (L3). The ledger re-points the cites of specs 89 and 91 the same way: spec 88's S19
  and AC13 lines, and the driver's comparator. Observed by AC18.
- **S19** — id 16 (L4). A token is delimited: unit 89's guard and AC3 over unit 88's records are read
  again at the tip with `audit-77 id 1 ` and its trailing space, which no `audit-77 id 1<digit>` token
  matches. Every token units 93 to 100 write ends in a label after a space. Observed by AC19.
- **S20** — id 22 (L5). Two records sharing an `<n>` are found by the join that already finds them:
  `deviation_join.read_records` marks both (`tools/memory-tree/deviation_join.py:284-291`), and
  `python tools/memory-tree/deviation_join.py` prints each as `malformed:` with `shares deviation-`.
  The scan's own `shared-n` arm is not carried. Observed by AC20.

## 3. Non-goals (OUT)

- The high ids: units 93 to 99.
- Editing any spec of units 89 to 99, frozen once each builds, as §2's opening states.
- The spec lints and checklist entries the report suggests as left-shift gates: the close's left-shift
  step (BUILD-METHOD M8).
- Deleting a record. A deviation record is evidence of what a pass did; one that is wrong is
  superseded or withdrawn and kept.

### Edges

- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door every record of this unit is written through (ids 3, 4, 6, 7, 13, 19, 23, 24, 31)
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, which resolves the passes of units 69 and 83 (ids 7, 14, 26, 31)
- **consumes-from** `TOOL-dTotalRecall-88` — its AC19 predicate and the cites into its S19 and AC13 (ids 10, 17)
- **consumes-from** `TOOL-dTotalRecall-89` — its guards, its AC3 and AC13 answers and its ancestry walk (ids 13, 14, 16, 21, 26, 31)
- **consumes-from** `TOOL-dTotalRecall-90` — its record recipe and its cites (ids 11, 19)
- **consumes-from** `TOOL-dTotalRecall-91` — its record of unit 69 and its cites (ids 6, 17)
- **consumes-from** `TOOL-dTotalRecall-92` — its S8, S11 and S22 records, its sweep, its needle scan and its span script (ids 3, 4, 9, 10, 23, 24, 25, 32)
- **consumes-from** `TOOL-dTotalRecall-93` — `has_deviation`, its `--paths` mode and the correcting record (ids 3, 4, 13, 14, 21, 24)
- **consumes-from** `TOOL-dTotalRecall-95` — `key59` and the re-stating record (ids 13, 19)
- **consumes-from** `TOOL-dTotalRecall-96` — `c5_of` and its answer to unit 69's AC1 (ids 6, 7)
- **consumes-from** `TOOL-dTotalRecall-97` — `c5_input` and its extraction of unit 80's ledger (id 6)
- **consumes-from** `TOOL-dTotalRecall-98` — `deleted_records` and the restores it refused (id 24)
- **consumes-from** `TOOL-dTotalRecall-99` — `tip_scan` and `tip_check`, which this unit amends (ids 3, 4, 22, 23)

## 4. Design

### How the batch builds

One pass, after every other unit is terminal, in this order:

1. The main loop's recording of S13's sweep, under a `Pass: none` commit, before the pass starts.
2. The read-only items: S5, S8 to S11, S15 to S19, and the scan and the join at this pass's base.
3. The tree items: S12's restores.
4. The records: S2, S3, S4, S5, S6, S7, S10 and S12, each through the door.
5. The scan, `key59` and the join again over the pass's own records, last.

### The scan, amended

`TOOL-dTotalRecall-99` §4's `tip_scan`, with its block from the `seen = collections.Counter` line
through the `print('live', len(live))` line replaced by:

```python
gone = {r['supersedes'] for r in recs if r['supersedes']}
live = [r for r in recs if r['id'] not in gone]
for r in recs:
    for field, why in r['malformed']:
        print('malformed' if r['id'] not in gone else 'malformed-superseded', r['path'], field, why)
    if r['path'] not in tracked:
        print('untracked', r['path'])
print('live', len(live))
```

`tip_check` is unchanged. PINNED, measured 2026-10-26 at `32febccb6` in a fixture repository made as
unit 99 §4 makes one, holding a record with its Risk line removed and a complete record superseding
it: `tip_check` printed `malformed-superseded` naming the first, no `malformed` line, and
`scan ok 2 1`. Over `memory/builds/dTotalRecall/build` it printed `scan ok 8 8`.

### The pair fixture

```bash
# run from the repository root, with the amended tip_scan and tip_check defined
R="$TEMP/r100"; rm -rf "$R"; mkdir -p "$R/tools" "$R/memory/builds/dFx/build"; cp -r tools/memory-tree "$R/tools/"
B="$R/memory/builds/dFx/build"; SRC=memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md
D=2026-10-26-build-TOOL-dTotalRecall-59-deviation
sed 's/^\*\*Serves:\*\* deviation .*/**Serves:** deviation TOOL-dTotalRecall-59/' "$SRC" > "$B/$D-591.md"
sed 's/^- \*\*Evidence:\*\* .*/&, one more byte/' "$B/$D-591.md" > "$B/$D-592.md"
(cd "$R" && git init -q && git add -A && git -c user.email=f@x -c user.name=f commit -qm pair && tip_check memory/builds/dFx/build)
sed -e "s/^- \*\*Before:\*\* .*/- **Before:** the record $D-592/" \
    -e "s/^- \*\*After:\*\* .*/- **After:** superseded as a duplicate of $D-591/" \
    -e "s/^- \*\*Evidence:\*\* .*/- **Evidence:** $D-591, $D-592, audit-89 id 4 s3/" "$B/$D-591.md" > "$B/$D-593.md"
echo "- **Supersedes:** $D-592" >> "$B/$D-593.md"
(cd "$R" && git add -A && git -c user.email=f@x -c user.name=f commit -qm fix && tip_check memory/builds/dFx/build)
```

The repository sits under the system temp directory because a fixture repository needs a short path
on Windows. PINNED, measured 2026-10-26 with these exact commands: the first `tip_check` printed one
`dup` line naming `-591` and `-592` and `scan ok 2 2`; the second printed no `dup` line and
`scan ok 3 2`.

### The edit listing

```bash
# run from the repository root
edited() {  # -> "<commit> <subject>" then each deviation record that commit modified, rename detection off
  git log --no-renames --diff-filter=M --format='%H %s' --name-only 462d20f3..HEAD -- 'memory/builds/dTotalRecall/build/*-deviation-*.md'
}
```

### The withdrawing record

Written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-69`,
with the fields of `TOOL-dTotalRecall-93` §4's correcting record except these:

| Field | Value |
|---|---|
| Before | `the record <withdrawn stem>` |
| After | `withdrawn: unit 91 read no status line where TOOL-dTotalRecall-97 places one` |
| Evidence | the withdrawn stem, `c5_input`'s `p69` output and the token `audit-89 id 6 s4` |
| Supersedes | the withdrawn record's stem |

### The ancestry walk

```bash
# run from the repository root, with TOOL-dTotalRecall-81 §4's pass_of and TOOL-dTotalRecall-93 §4's has_deviation sourced
ancestry() {  # record path · P83, a sha or pass_of's red line -> one verdict line
  case "$2" in red*) echo "rec $1 ungraded p83 red"; return 0 ;; esac
  local A rc; A=$(git log --diff-filter=A --format=%H -1 -- "$1")
  [ -n "$A" ] || { echo "rec $1 at-or-after-p83 untracked"; return 0; }
  git merge-base --is-ancestor "$2" "$A" 2>/dev/null; rc=$?
  case $rc in 0) echo "rec $1 at-or-after-p83" ;; 1) echo "rec $1 before-p83" ;; *) echo "rec $1 red ancestry rc=$rc" ;; esac
}
P83=$(pass_of 83)
has_deviation --paths memory/builds/dTotalRecall/build 59 'pass(59)' '`absorbs` is absent' |
  sed -n 's/^rec //p' | while read -r f; do ancestry "$f" "$P83"; done
```

`P83` keeps `pass_of`'s red line where it fails, and the `case` reads it before any git call.
PINNED, measured 2026-10-26 at `32febccb6` over
`memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`: with `HEAD`
as P83 it printed `before-p83`, with `462d20f3` `at-or-after-p83`, with a sha naming no object
`red ancestry rc=128`, and with `red 83 no pass commit` `ungraded p83 red`; over a path no commit
added, `at-or-after-p83 untracked`.

### The sweep, corrected

```bash
# run by the main loop from the repository root, with lib-attribute.sh, pass_of and read_checker sourced
W="$(git rev-parse --git-common-dir)/gate-mc100"
add_scratch_worktree "$W" HEAD || { echo "gate-mc100 red worktree-add-failed"; exit 1; }
trap 'remove_scratch_worktree "$W"' EXIT INT TERM
for N in $UNRESOLVED; do
  grep -qE "^$N [0-9a-f]{40} rc=[0-9]+$" "$SCRATCH/sweep100-$N.txt" 2>/dev/null && continue
  { P=$(pass_of "$N") || { echo "$N $P"; continue; }
    git -C "$W" checkout --quiet --detach "$P" || { echo "$N red checkout-failed $P"; continue; }
    read_checker "$W" "$N $P"; } > "$SCRATCH/sweep100-$N.tmp"
  grep -qE "^$N [0-9a-f]{40} rc=[0-9]+$" "$SCRATCH/sweep100-$N.tmp" && mv "$SCRATCH/sweep100-$N.tmp" "$SCRATCH/sweep100-$N.txt"
done
```

`$UNRESOLVED` is the population units that lead no `rc=` verdict line in unit 78's block or unit 92's
sweep files. A unit's file is kept only once it holds its verdict, so a red or a killed read is read
again on resume. `gate-mc100` sits under the `gate-ledger` pocket row of `TOOL-dTotalRecall-18`
(`<git-common-dir>/gate-*`), as unit 92's `gate-mc92` does.

### The needle scan, widened

Unit 92 §4's needle scan, run over the same specs, with two more populations read into its `run`
test: each backticked cell of the String column of spec 86 §4's table, and the edge strings units 71
and 72 §4 spell. It prints `blocks <n> cells <m>`. A scratch spec holding a `STRINGS` block whose
needle carries a double space is added to its arguments once, and the scan prints a `run` line for it.

### The predicate

Unit 88's AC19 command, `python -c "import sys; [print(p, sum(1 for l in open(p, encoding='utf-8') if chr(96)*3 in l.lstrip()[1:])) for p in sys.argv[1:]]"`,
run over `memory/builds/dTotalRecall/spec/*.md`. PINNED, measured 2026-10-26 at `32febccb6` over
specs 89 to 92: 0, 0, 0 and 1.

### Why order 41

Units 98 and 99 hold 40, after unit 92 at 39. Every item reads a landed unit or its records, so this
unit builds last.

### Inventory

Minted: the functions `edited` and `ancestry`, the amended scan and the corrected sweep, spec text
only; deviation, correcting, withdrawing and re-stating records where §2's reads are red; restored
records under a free `<n>` where S12 owes one. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (the records, the restored records and this unit's ledger)

### Alternatives rejected

- **Two batches.** Every item but S8, S9, S11 and S15 to S19 writes or restores deviation records,
  whose `<n>` the door mints from one folder; two concurrent writers are the collision `<n>` sharing
  names, so BUILD-METHOD M6's clause 1 keeps them one unit.
- **Restore a taken path by overwriting it (id 24).** The newer record would be lost from the working
  tree; a free `<n>` keeps both.
- **Edit the specs of units 89 to 92 by rev bump.** Each is frozen once its unit builds, and each builds
  before order 41.

## 5. Production-readiness checklist

- security — no new write surface; S12 restores files the door wrote, from git's own objects.
- perf / scale — the scan, the join, `key59` and the ancestry walk each read the build folder once; S13
  adds one checker run per unresolved unit.
- error / empty / loading states — an unresolved pass is a red line; an ancestry error prints its
  status; a taken path is restored under a free `<n>`, never overwritten.
- observability — every red names its read; the ledger sets each value beside the landed unit's own.
- risks — S12 changes a restored record's stem, so the ledger names the old and new path together.
- testing — AC1 to AC20 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the amended scan runs through `tip_check` over the fixture repository of a record
  missing its Risk line and a complete record superseding it, it prints `malformed-superseded`, no
  `malformed` line and `scan ok 2 1`, and at the pass tip over the build folder it prints no
  `malformed` line and ends `scan ok`.
  Red when: a superseded record keeps AC8 red, or a live malformed record is reported as superseded.
  fixture: the repository is made under the system temp directory by the pass; the tree holds none.
- **AC2** — When `edited` runs after the pass, every record it lists is named in the ledger's AC2 line
  with its commit, and `has_deviation memory/builds/dTotalRecall/build <unit> 'audit-89 id 23 s2'`
  prints 1 for each unit whose pass modified a record outside a restore, else 0.
  Red when: a record edited by hand goes unnamed.
- **AC3** — When §4's pair fixture runs, the first `tip_check` prints one `dup` line and the second
  prints none and ends `scan ok 3 2`, and at the pass tip the scan prints no `dup` line.
  Red when: a correcting record re-creates the pair's key.
  fixture: the repository is made under the system temp directory by the pass; the tree holds none.
  figure: the lines are PINNED in §4, measured 2026-10-26.
- **AC4** — When `has_deviation --paths memory/builds/dTotalRecall/build 69` runs after the pass, no
  record it lists was written by unit 91 from a `no-status-line` verdict while
  `TOOL-dTotalRecall-97`'s ledger shows a placed `p69` status line, and each one withdrawn is named
  with its withdrawing record.
  Red when: a record of unit 69 states a parse failure as an unobserved criterion.
- **AC5** — When `memory/guides/SESSION-KICKOFF.md` at the commit `pass_of 69` prints is read with
  `git show` and counted with `grep -c 'kickoff-manifest:'`, the ledger's AC5 line quotes its count,
  and where it is 0 with no marker at `.claude/SESSION-KICKOFF.md` either, `has_deviation memory/builds/dTotalRecall/build 69 'audit-89 id 7 s5'`
  prints 1.
  Red when: unit 69's AC1 stands green on a read in which the checker skipped every check.
- **AC6** — When `has_deviation memory/builds/dTotalRecall/build 59` runs at the pass tip with the
  string `` `absorbs` is absent ``, it prints at most 1.
  Red when: two live records of unit 59 name the departure.
- **AC7** — When `key59 memory/builds/dTotalRecall/build` runs at the pass tip, it prints no `missing`
  line and its two numbers are equal.
  Red when: a record of unit 59 written after order 37 names the string without `pass(59)`.
- **AC8** — When §4's ancestry walk runs at this pass's base, each path `has_deviation --paths` prints
  for unit 59 leads exactly one `rec` line, whose verdict is one of the walk's four.
  Red when: a counted record prints no verdict, or a git error reads as `before-p83`.
  figure: the verdicts over `-2-deviation-21` are PINNED in §4, measured 2026-10-26.
- **AC9** — When `ancestry` runs with `HEAD` over a record path no commit added, a none-deviation-0.md
  in the build folder, it prints `at-or-after-p83 untracked`.
  Red when: a record with no adding commit reads as before `pass(83)`.
- **AC10** — When `ancestry <path> "red 83 no pass commit"` runs, it prints `ungraded p83 red`, and
  `has_deviation memory/builds/dTotalRecall/build 89 'audit-89 id 31 s10'` prints 1 where unit 89
  answered its S1-at-least-1 arm green with a red `p83` line or without a `before-p83` line per
  counted record, else 0.
  Red when: an unresolved `pass(83)` leaves AC13 green.
- **AC11** — When the ledger's AC8 line is read, its `rec` paths are exactly the paths
  `has_deviation --paths memory/builds/dTotalRecall/build 59` prints with `pass(59)` and the string.
  Red when: the walk reads a record the count does not hold, or misses one it does.
- **AC12** — When `deleted_records 462d20f3..HEAD` runs after the pass, every path it prints exists in
  the tree or names a record the ledger's AC12 line restored under a free `<n>`, every restored path was
  absent before its restore, and `python tools/memory-tree/deviation_join.py` prints no `shares deviation-`
  line naming one.
  Red when: a restore overwrote a record or left two files at one `<n>`.
- **AC13** — When the ledger's AC13 line is read, every population unit of unit 78 leads a
  `<n> <sha> rc=<n>` line in unit 78's block, unit 92's sweep files or this unit's, quoted there.
  Red when: a population unit is led only by a `red` line.
  cost: one checker run per unresolved unit.
  permission: as S13's.
- **AC14** — When `git worktree list --porcelain` and `ls "$(git rev-parse --git-common-dir)"` run at the
  pass tip, no worktree path ends `/gate-mc92` or `/gate-mc100` and no entry is named either.
  Red when: a sweep's worktree outlives it.
- **AC15** — When §4's widened needle scan runs over the build's specs, it prints its `blocks` and
  `cells` line and no `run` or `empty` line, and with the planted scratch spec added it prints one
  `run` line.
  Red when: a needle the build's reads consume is never scanned, or the planted run goes unseen.
  fixture: the planted spec is made in the run's scratch by the pass.
- **AC16** — When §4's predicate runs over `memory/builds/dTotalRecall/spec/*.md`, it prints 0 for
  every spec of units 77 to 100 but spec 92, which prints 1, and the ledger names that line.
  Red when: a spec of this round carries a mid-line triple backtick.
  figure: the counts over specs 89 to 92 are PINNED in §4; the rest are DERIVED.
- **AC17** — When `grep -n` runs for each token spec 90 cites at this pass's base, each prints one
  line, and the ledger's AC17 line sets that line beside spec 90's cite, the comparator
  `units.slice().sort` among them.
  Red when: a re-pointed cite names a line that does not hold its token.
- **AC18** — When `grep -n` runs for each token specs 89 and 91 cite, each prints one line, and the
  ledger's AC18 line sets each beside its cite.
  Red when: a re-pointed cite names a line that does not hold its token.
- **AC19** — When `has_deviation memory/builds/dTotalRecall/build 88 'audit-77 id 1 '` runs at the pass
  tip, it prints the count unit 89's AC3 recorded, and over a scratch folder holding one record of unit
  88 whose Evidence holds `audit-77 id 12 s8`, it prints 0 where `audit-77 id 1` prints 1.
  Red when: a token of another id matches the delimited token.
  fixture: the folder is made in the run's scratch by the pass, its record built from
  `2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md` with only Serves and Evidence changed.
  figure: 0 and 1 over that folder are PINNED, measured 2026-10-26 at `32febccb6`; the tip count is DERIVED.
- **AC20** — When `python tools/memory-tree/deviation_join.py` runs from the repository root at the pass
  tip, it prints no `malformed:` line naming a record under `memory/builds/dTotalRecall/build/` with
  `shares deviation-`, and the amended scan prints no `shared-n` line.
  Red when: two records of this build share an `<n>`.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: each observation is a probe this spec spells, a fixture, or a read of a landed unit's
output.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, its 20
  confirmed minors: 14 MEDIUM, ids 3 4 6 7 13 14 19 21 23 24 25 26 31 32 (items M1 to M9), and 6 LOW,
  ids 9 10 11 16 17 22 (items L1 to L5).

## 10. Reuse audit

The seams are those the minors name: `TOOL-dTotalRecall-93`'s `has_deviation` and correcting record;
`TOOL-dTotalRecall-95`'s `key59`; `TOOL-dTotalRecall-97`'s `c5_input`; `TOOL-dTotalRecall-99`'s scan,
amended; `TOOL-dTotalRecall-98`'s listings; the join `python tools/memory-tree/deviation_join.py`,
whose `read_records` already marks a shared `<n>` (`tools/memory-tree/deviation_join.py:284-291`);
and the scratch-worktree pair of `tools/run-gates/lib-attribute.sh:59` and `:63`.
`python tools/codebase-map/reuse_lookup.py "assign a deviation record to its unit by its file name stem"`
ranked `read_records` among its SEAM candidates, which S20 now grades through instead of a second
grouping. The recall query below found this audit's items M1 to M9 and L1 to L5 and the units 89 to
92 they name. No mechanism is minted beyond the amended scan, two listings, the ancestry walk and the
corrected sweep.

Recall terms used: `python tools/memory-recall/query.py "how is each minor finding over a deviation-record reading made once at the tip and recorded" --terms "deviation record tip scan malformed superseded dup ancestry pass(83) restore free n sweep resume needle scan"`
