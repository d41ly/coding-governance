# TOOL-dTotalRecall-100 — the round-9 minors: each reading of units 89 to 92 that a dropped line, a stale cite or a loose key could mislead is made once at the tip, and each record it decides is written once

**Status:** CLOSED · rev-2 · 2026-11-25 · node d · Tier-2 · base 462d20f3 · streams tooling · order 41 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 |
| [2026-10-26-build-TOOL-dTotalRecall-100-deviation-1001.md](../build/2026-10-26-build-TOOL-dTotalRecall-100-deviation-1001.md) | deviation | — |
| [2026-11-25-build-TOOL-dTotalRecall-100-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dTotalRecall-100-1-acceptance-ledger.md) | log | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-100-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-100-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-100-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-100-reground-spec-writer.md) | log | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-100-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-100-build-brief.md) | journal | — |

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
repairs none in particular and builds after every unit of a lower step: order 41, above the 40 units 98
and 99 hold. The review record holds each item's text.

Re-grounded at `39ffc882e`, over units 74, 76, 81, 82, 83 and 87 as built and units 77 to 80, 84 to 86 and
88 to 99 as their specs stand. Their re-grounds took most of the report's fixes before any code. So S7's
re-statement, S5's record and S17's and S18's re-pointed cites are cut, S8 to S11 observe unit 89's own
walk, and S13 runs unit 78's loop where one is owed. The other items are reads, each record owed only on
a red. Nothing is built in code.

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
- **S2** — id 23 (M1). No pass cleared unit 92's AC8 by editing a record by hand: §4's `scan_edits`
  names every record a commit of this build modified, each beside its commit's `Pass:` trailer and
  subject. A modification by a commit whose trailer names a unit, and which is not one of the restores of
  unit 92's S11, unit 98's S3 or S12 below, gets a deviation record of that unit. One by a
  `Pass: none` commit is no pass's, and the ledger names it. Observed by AC2.
- **S3** — id 4 (M2). A duplicate pair unit 92's S11 or S22 made one is made one by a record whose
  fields are `TOOL-dTotalRecall-93` §4's, as unit 92 rev-3 spells it, so the correcting record shares no
  `dup` key. Where the scan at this pass's base prints a `dup` line naming a correcting record of unit
  92, that pair is made one again by §4 of unit 93. Observed by AC3.
- **S4** — id 6 (M3). A record of `TOOL-dTotalRecall-69` that unit 91 wrote from a
  `no-status-line` verdict, where `TOOL-dTotalRecall-97`'s `c5_input` places a status line for `p69`
  in unit 80's ledger, is withdrawn by §4's withdrawing record: the read was sound and only unit 91's
  parse failed. Observed by AC4.
- **S5** — id 7 (M4). The manifest unit 69's checker read carried its marker:
  `git show "$(pass_of 69):memory/guides/SESSION-KICKOFF.md" | grep -c 'kickoff-manifest:'` prints
  at least 1, the first path of the checker's `MANIFEST_LOCATIONS`
  (`skills/session-kickoff/manifest-check.sh@f7011dd6f:73`), so the read is not the unmanaged exit 0
  (`skills/session-kickoff/manifest-check.sh@f7011dd6f:2359`). It prints 1 at `f7011dd6f`, unit 69's
  pass (PINNED 2026-11-24), a commit that cannot move, so the record this item owed on a 0 is cut. Where
  `TOOL-dTotalRecall-96` answered AC1 of unit 69, that answer stands. Observed by AC5.
- **S6** — id 13 (M5). At most one live record names unit 59's absorbs departure at the tip, whichever
  key counts it: `has_deviation` for unit 59 with the string `` `absorbs` is absent `` prints at most 1
  after units 89 and 92 have written. None is owed (`TOOL-dTotalRecall-89` rev-3 S4), and it prints 0 at
  `39ffc882e` (PINNED 2026-11-24). Observed by AC6.
- **S7** — id 19 (M5). The key `TOOL-dTotalRecall-95` set still holds at the tip: its `key59` prints
  no `missing` line and two equal numbers over the build folder, after unit 89's S3 and unit 92's
  records. Unit 95's re-stating record is written only where the departure is owed, and `s1-59` reads 1
  over a blob that cannot move (spec 90 rev-3 §4), so the re-statement is cut; the ledger names any
  record `key59` finds missing by path as unowed. Observed by AC7.
- **S8** — id 14 (M6). Unit 89's ancestry check has three outcomes: its rev-3 `check_ancestry` prints
  `before-p83` on exit status 1, `at-or-after-p83` on 0 and `red ancestry rc=<n>` on anything else.
  Unit 89's own walk is run again at this pass's base. Observed by AC8.
- **S9** — id 26 (M6). A record with no adding commit reads `at-or-after-p83 untracked`, as written at
  the pass. Unit 89 rev-3 spells it so. Observed by AC9.
- **S10** — id 31 (M6). Where `pass_of 83` prints a red line, the walk prints `ungraded p83` with it,
  and unit 89's AC13 answer on the S1-at-least-1 arm reads unresolved. Unit 89 rev-3's table has that
  row, and `pass_of 83` prints a sha since `39ffc882e`. Where unit 89 answered that arm green over a red
  or ungraded line, or without a `before-p83` line for every counted record, a deviation record of
  `TOOL-dTotalRecall-89` names it. Observed by AC10.
- **S11** — id 21 (M7). The walk runs over the counter's own list and over no second selection: unit 89
  rev-3 pipes `has_deviation --paths` for unit 59 into it, carriage returns stripped, so every record
  either of its counts holds leads a walk line. Observed by AC11.
- **S12** — id 24 (M8). A restore whose path is taken, or whose `<n>` a record of the folder already
  carries, puts the record back with its bytes unchanged under the next free `<n>`, the door's own rule
  (`tools/memory-tree/build_records.py#write_record`), by §4's `write_free_restore`. It never overwrites,
  and bytes the folder already holds are not put back twice. Each restore `TOOL-dTotalRecall-98` refused
  as held is made so, through §4's `write_free_restores`; and where unit 92's pass modified a path
  `deleted_records` prints, the bytes that path held before that pass are put back so. A modified record
  unit 98 refused as moved-since is S2's. Observed by AC12.
- **S13** — id 25 (M9). Unit 78's population is read whole: §4's `check_swept` prints no `unswept` line
  over unit 78's block and, where unit 92's S9 ran a second sweep, that block too. A unit led only by a
  `red` line, or by `rc=1` with no failure line beneath it, is unswept where its pass resolves. A unit
  with no pass commit, held unbuilt, prints `none` and is named. Where a line is `unswept`, unit 78 §4's
  loop runs again as §4 states before this pass. Observed by AC13.
  permission: the checker is the `kickoff-manifest ratchet` leg's argv, which no role agent may run
  (`.claude/roles.json`); the main loop runs the loop and hands its output in the build brief.
- **S14** — id 32 (M9). No scratch worktree of the sweep outlives it: §4's re-run carries an exit trap
  that removes its worktree and a signal trap that exits, and at the tip no worktree path and no
  common-directory entry is `gate-mc92` or `gate-mc100`. One found is removed by
  `remove_scratch_worktree` and named. Observed by AC14.
  **Readers:** by name: no name retires, the item removing only the scratch worktrees the sweeps
  added, whose paths are spelled by `add_scratch_worktree` and `remove_scratch_worktree`
  in `tools/run-gates/lib-attribute.sh` and their callers `tools/run-gates/post-merge.sh`,
  `tools/run-gates/run-gates.sh` and `tools/run-gates/run-selftests.sh`
  · by value: `tools/memory-tree/record_kinds.py#check_pockets`, which reds a common-directory entry no
  witness row names; the `gate-ledger` row's `gate-*` home covers both names while they stand.
- **S15** — id 9 (L1). The needle scan reads every needle a `read_at` call of this build
  consumes: the `<<'STRINGS'` blocks by unit 92 §4's scan, and the String column of spec 86 §4's table
  and the edge strings of units 71 and 72 §4 that spec 88's AC1 and AC20 count by §4's `scan_cells`. A
  planted needle with a double space prints a `run` line in each. Observed by AC15.
- **S16** — id 10 (L2). Unit 88's AC19 predicate runs over every spec in the build folder, not units
  77 to 88: it prints 0 for every spec of units 77 to 100, spec 92's one span having been re-spelled with
  `chr(96) * 3` at its rev-3 and spec 86's two with two backticks. The specs it prints otherwise are
  frozen, and the ledger names them. Observed by AC16.
- **S17** — id 11 (L3). Spec 90 rev-3 cites code by symbol and no spec by line, so no cite is left to
  re-point: §4's cite scan prints nothing for it. The sort by order and id is the comparator, the line
  `grep -n "units.slice().sort"` prints in `tools/workflows/unattended-build.js`, not the comment above
  it. Observed by AC17.
- **S18** — id 17 (L3). Specs 89 and 91 are read the same way: the cite scan prints nothing for spec 89,
  and for spec 91 only lines pinned at `f7011dd6f`, each holding what it cites. Observed by AC18.
- **S19** — id 16 (L4). A token is delimited: the guard over unit 88's records is read
  at the tip with `audit-77 id 1 ` and its trailing space, which no `audit-77 id 1<digit>` token
  matches; unit 89 rev-3's `audit-77 id 1 s5` and every token units 93 to 100 write end in a label after
  a space, and no record of the folder holds a bare one. Observed by AC19.
- **S20** — id 22 (L5). Two records sharing an `<n>` are found by the join that already finds them:
  `tools/memory-tree/deviation_join.py#read_records` marks both, through
  `tools/memory-tree/build_records.py#read_records`, with a reason opening `shares deviation-`, and §4's
  `read_shared` prints each. The scan's own `shared-n` arm is not carried. Observed by AC20.

## 3. Non-goals (OUT)

- The high ids: units 93 to 99.
- Editing any spec of units 89 to 99, frozen once each builds, as §2's opening states.
- The spec lints and checklist entries the report suggests as left-shift gates: the close's left-shift
  step (BUILD-METHOD M8).
- Deleting a record. A deviation record is evidence of what a pass did; one that is wrong is
  superseded or withdrawn and kept.
- Unit 78's sweep and loop, reached through unit 92, which consumes it.

### Edges

- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door every record of this unit is written through (ids 3, 4, 6, 7, 13, 19, 23, 24, 31)
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, which resolves the passes of units 69, 83 and 92 (ids 7, 14, 24, 26, 31)
- **consumes-from** `TOOL-dTotalRecall-88` — its AC19 predicate and the edge strings its AC1 and AC20 count (ids 9, 10, 17)
- **consumes-from** `TOOL-dTotalRecall-89` — its guards, its AC3 and AC13 answers and its ancestry walk (ids 13, 14, 16, 21, 26, 31)
- **consumes-from** `TOOL-dTotalRecall-90` — its record recipe and its cites (ids 11, 19)
- **consumes-from** `TOOL-dTotalRecall-91` — its record of unit 69 and its cites (ids 6, 17)
- **consumes-from** `TOOL-dTotalRecall-92` — its S8, S11 and S22 records, its sweep, its needle scan and its span script (ids 3, 4, 9, 10, 23, 24, 25, 32)
- **consumes-from** `TOOL-dTotalRecall-93` — `has_deviation`, its `--paths` mode and the correcting record (ids 3, 4, 13, 14, 21, 24)
- **consumes-from** `TOOL-dTotalRecall-95` — `key59` and the re-stating record (ids 13, 19)
- **consumes-from** `TOOL-dTotalRecall-96` — `c5_of` and its answer to unit 69's AC1 (ids 6, 7)
- **consumes-from** `TOOL-dTotalRecall-97` — `c5_input` and its extraction of unit 80's ledger (id 6)
- **consumes-from** `TOOL-dTotalRecall-98` — `deleted_records`, `write_restores` and the restores it refused (id 24)
- **consumes-from** `TOOL-dTotalRecall-99` — `tip_scan` and `tip_check`, which this unit amends (ids 3, 4, 22, 23)

## 4. Design

### How the batch builds

One pass, after every unit of a lower step is terminal, the held units DEFERRED to an owner ask aside, in
this order:

1. The main loop runs `check_swept`, and the sweep again only where it prints an `unswept` line, before
   this pass is dispatched. Their output is in the build brief.
2. The read-only items: S5 to S11, S15 to S20, and the scan at this pass's base.
3. The tree items: S12's restores and S14's removal.
4. The records: S2, S3, S4, S10, each only where its read is red, through the door.
5. The scan, `key59` and `read_shared` again over the pass's own records, last.

Each fence below is written to a file under `$SCRATCH`, an absolute path, and run as `bash <file>`: an
isolated worktree session refuses an inline command that embeds git. `scan100.sh` is
`TOOL-dTotalRecall-99` §4's `scan99.sh` amended as below, `listings98.sh` is `TOOL-dTotalRecall-98` §4's
first fence, and `reads100.sh` holds `scan_edits`, the two restores and `read_shared`. `PY` is the launcher
`scan100.sh` resolves.

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

`tip_check` is unchanged. PINNED, measured 2026-11-24 at `594b406d3` over
`memory/builds/dTotalRecall/build`: no line but `records`, `live`, `by` and three `quoted` lines, and
`scan ok 150 147`, in 3 s on node a (PINNED 2026-11-24).

### The edit listing, the restores and the join

```bash
# $SCRATCH/reads100.sh, sourced from the repository root after scan100.sh and listings98.sh
scan_edits() {  # -> "<commit> <Pass trailer> <subject>", then each deviation record that commit modified, rename detection off
  git log --no-renames --diff-filter=M --format='%H %(trailers:key=Pass,valueonly,separator=%x2C) %s' --name-only 462d20f3..HEAD -- 'memory/builds/dTotalRecall/build/*-deviation-*.md'
}
write_free_restore() {  # record path · commit that took it out or overwrote it -> one verdict line
  local b d n new
  b=$(git rev-parse -q --verify "$2^:$1") || { echo "red $1 $2 no-blob"; return 1; }
  d=${1%/*}
  git hash-object "$d"/*-deviation-*.md | grep -qx "$b" && { echo "held $1 $2 bytes-present"; return 0; }
  n=$(ls "$d" | sed -n 's/.*-deviation-\([0-9]*\)\.md$/\1/p' | sort -n | tail -1)
  new="${1%-deviation-*}-deviation-$((n + 1)).md"
  git show "$b" > "$new" || { rm -f "$new"; echo "red $1 $2 show-failed"; return 1; }
  echo "restored $1 $2 as $new"
}
write_free_restores() {  # range -> write_restores' lines, each refused as held put back under a free n
  write_restores "$1" | while read -r verb p c how rest; do
    if [ "$verb $how" = "refused held" ]; then write_free_restore "$p" "$c"; else echo "$verb $p $c $how $rest"; fi
  done
}
read_shared() {  # repository root · folder under it -> the count of records read there, then the join's shares lines
  "$PY" - "$1" "$2" <<'PROBE'
import pathlib, sys
root = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / 'tools/memory-tree'))
import deviation_join as d
rs = [r for r in d.read_records(root, {}) if r['path'].startswith(sys.argv[2] + '/')]
print('read', len(rs))
for r in rs:
    for _field, why in r['malformed']:
        if why.startswith('shares deviation-'):
            print('malformed:', r['path'], why)
PROBE
}
```

The door's next `<n>` is one above the highest in the folder, so a restored record never meets another.
A restored record keeps its heading's old `<n>`, which no check reads, and the ledger names its old and
new path together. What `scan_edits` does not read is a merge commit's own edit; with `-m` it printed the
same three commits at `39ffc882e` (PINNED 2026-11-24).

PINNED, measured 2026-11-24 at `39ffc882e` over the build: `read_shared . memory/builds/dTotalRecall/build`
printed `read 150` alone, in 3 s (PINNED 2026-11-24); `write_free_restores 462d20f3..HEAD` nothing; and `scan_edits` three
commits, `9773de4ad`, `1c944a4ac` and `f070230a5`, each with the trailer `none`, over five records, the
deviations 83, 15, 21, 231 and 81 (PINNED 2026-11-24). Each is a main-loop spec commit, so S2 owes no
record at that commit.

### The fixture

```bash
# $SCRATCH/fx100.sh, run as bash <file> from the repository root
. "$SCRATCH/scan100.sh"; . "$SCRATCH/listings98.sh"; . "$SCRATCH/reads100.sh"
SRC="$PWD/memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md"
R="${SCRATCH:?}/r100"; rm -rf "$R"; mkdir -p "$R/tools"; cp -r tools/memory-tree "$R/tools/"; cd "$R" || exit 2
X=memory/builds/dFx/build; Y=memory/builds/dFy/build; Z=memory/builds/dTotalRecall/build; mkdir -p $X $Y $Z; git init -q
write_commit() { git add -A && git -c user.email=f@x -c user.name=f commit -qm "$1"; }
D=2026-10-26-build-TOOL-dTotalRecall-59-deviation
sed 's/^\*\*Serves:\*\* deviation .*/**Serves:** deviation TOOL-dTotalRecall-59/' "$SRC" > $X/$D-591.md
sed 's/^- \*\*Evidence:\*\* .*/&, one more byte/' $X/$D-591.md > $X/$D-592.md
sed '/^- \*\*Risk:\*\*/d' $X/$D-591.md > $Y/$D-591.md
cp $X/$D-591.md $Z/$D-1.md; cp $X/$D-592.md $Z/$D-2.md; write_commit one
echo "== pair"; tip_check $X
echo "== malformed"; tip_check $Y
sed -e "s/^- \*\*Before:\*\* .*/- **Before:** the record $D-592/" \
    -e "s/^- \*\*After:\*\* .*/- **After:** superseded as a duplicate of $D-591/" \
    -e "s/^- \*\*Evidence:\*\* .*/- **Evidence:** $D-591, $D-592, audit-89 id 4 s3/" $X/$D-591.md > $X/$D-593.md
echo "- **Supersedes:** $D-592" >> $X/$D-593.md
{ cat $X/$D-591.md; echo "- **Supersedes:** $D-591"; } > $Y/$D-592.md
rm $Z/$D-2.md; cp $X/$D-593.md $Z/2026-10-27-build-TOOL-dTotalRecall-60-deviation-2.md; write_commit two
echo "== corrected"; tip_check $X
echo "== superseded"; tip_check $Y
echo "== free"; write_free_restores HEAD~1..HEAD; git rev-parse "HEAD~1:$Z/$D-2.md"; git hash-object $Z/$D-3.md
echo "== again"; write_free_restores HEAD~1..HEAD
echo "== join"; git add -A; read_shared . $Z
echo "== shared"; cp $Z/$D-3.md $Z/2026-10-28-build-TOOL-dTotalRecall-59-deviation-1.md; git add -A; read_shared . $Z
```

The repository sits directly under the pass's scratch folder because a fixture repository needs a short
path on Windows. PINNED, measured 2026-11-24 on node a with these exact commands:

| Block | Printed (PINNED 2026-11-24) |
|---|---|
| `pair` | one `dup` line naming `-591` and `-592`, and `scan ok 2 2` |
| `malformed` | one `malformed` line ending `Risk is missing`, and `scan ok 1 1` |
| `corrected` | no `dup` line, and `scan ok 3 2` |
| `superseded` | `malformed-superseded` naming `-591`, no `malformed` line, and `scan ok 2 1` |
| `free` | `restored` naming `-deviation-2` and, as its new path, `-deviation-3`, then one blob id twice |
| `again` | `held`, ending `bytes-present` |
| `join` | `read 3` alone |
| `shared` | `read 4` and two `malformed:` lines, each `shares deviation-1 with` the other |

### The withdrawing record

Written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-69 --title <text>`,
with the fields of `TOOL-dTotalRecall-93` §4's correcting record except these. Its Departs from is the
withdrawn record's, unchanged:

| Field | Value |
|---|---|
| Before | `the record <withdrawn stem>` |
| After | `withdrawn: unit 91 read no status line where TOOL-dTotalRecall-97 places one` |
| Evidence | the withdrawn stem, `c5_input`'s `p69` output and the token `audit-89 id 6 s4`, and never the withdrawn record's own token |
| Supersedes | the withdrawn record's stem |

### The ancestry walk

Unit 89 rev-3 §4's two fences, unchanged, run from a file with the fences it names sourced: unit 81's
`pass_of` and `read_at`, unit 90's `s1` and unit 93's `has_deviation`. PINNED, measured 2026-11-24 at
`39ffc882e`, unit 83 CLOSED there: `p83` printed `39ffc882ed18d2f5234fe4b86739ca4175a1d656`, both counts
printed 0, and the walk one line, unit 59's roster record `before-p83` with its adding commit
`9443f6b3d152`. The red reads printed `before-p83` at `HEAD`, `at-or-after-p83` at `462d20f3`,
`red ancestry rc=128` at `deadbeef`, `ungraded p83 red 83 no pass commit` for the red line, and
`at-or-after-p83 untracked` for the path no commit added (PINNED 2026-11-24).

### The sweep, read whole

```bash
# run from the repository root, with unit 81 §4's pass_of sourced; $SWEEP is a file of the lines inside the
# fenced block of unit 78's AC1 answer, then those of the second block unit 92's AC9 answer holds, if any
check_swept() {  # file of swept lines -> one line per population unit with no verdict at its pass, then the counts
  local n p u s=0 t=0
  u=$(awk -F'|' '/\/gen:build-order/{f=0;next} /gen:build-order/{f=1;next} f && $2+0>=1 && $2+0<36 {print $3}' memory/builds/dTotalRecall/README.md |
      grep -oE 'TOOL-dTotalRecall-[0-9]+' | sed 's/.*-//')
  for n in $u; do
    t=$((t + 1))
    p=$(pass_of "$n") || { echo "none $n ${p#red "$n" }"; continue; }
    if grep -qx "$n $p rc=1" "$1" && ! grep -q "^$n $p MANIFEST check " "$1"; then echo "unswept $n $p"
    elif grep -qE "^$n $p rc=[0-9]+$" "$1"; then s=$((s + 1))
    else echo "unswept $n $p"; fi
  done
  echo "population $t swept $s"
}
check_swept "$SWEEP"
```

The population is unit 78 §4's own `awk`. A status that names another commit than the pass is no verdict
for it. PINNED, measured 2026-11-24 at `39ffc882e` over the
block of unit 76's ledger, which unit 78 takes over: `none` for units 8, 37, 14, 15, 26 and 84, `unswept`
for units 76 and 83, whose passes follow that sweep, and `population 72 swept 64`,
in 74 s on node a (PINNED 2026-11-24). Unit 78's own sweep reads both, and no line is expected at this pass's base.

Where it prints an `unswept` line, the main loop runs unit 78 §4's sweep again as that spec spells it, in
the background, with three changes. `HAVE` is `$SWEEP` without the lines each unswept unit leads, then
the two `live` lines unit 77's AC1 answer quotes, which that loop's own guard reads. `W` ends
`gate-mc100`. After the `W=` line it carries these two lines, so a killed run leaves no worktree:

```bash
trap 'remove_scratch_worktree "$W"' EXIT
trap 'exit 130' INT TERM
```

A signal trap that only removes the worktree would let the loop go on with none. Run in a scratch
repository, the pair left one worktree and no `gate-mc100` entry after a `TERM`, after a normal removal
and after an exit without one (PINNED 2026-11-24, node a). A failed add prints a red per unit and reads
nothing, unit 78's own rule, so this unit stops no loop on it. `HAVE` is made by:

```bash
check_swept "$SWEEP" | sed -n 's/^unswept \([0-9]*\) .*/\1/p' > "$SCRATCH/unswept100.txt"
awk 'FILENAME == ARGV[1] {bad[$1]; next} !($1 in bad)' "$SCRATCH/unswept100.txt" "$SWEEP" > "$SCRATCH/have100.txt"
```

### The needle scan, widened

```bash
# run from the repository root, with PY set
scan_cells() {  # spec 86 · specs 71 and 72, or copies -> a run line per needle holding a whitespace run, then the counts
  "$PY" - "$@" <<'CELLS'
import re, sys
rows = re.findall(r'^\| \d+ \| \d+ \| (`+) ?(.+?) ?\1 \|', open(sys.argv[1], encoding='utf-8').read(), re.M)
edges = [m for p in sys.argv[2:] for m in re.findall(r"^(?:EDGE|MIRROR) = '(.+)'$", open(p, encoding='utf-8').read(), re.M)]
cells = [c for _, c in rows]
for s in cells + edges:
    if re.search(r'\S\s{2,}\S|\t', s):
        print('run', repr(s))
print('cells', len(cells), 'edges', len(edges))
CELLS
}
P=memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall
scan_cells $P-86.md $P-71.md $P-72.md
sed 's/no base re-key is built/no base  re-key is built/' $P-86.md > "$SCRATCH/s86p.md"
sed "s/^MIRROR = .*/MIRROR = 'a  b'/" $P-72.md > "$SCRATCH/s72p.md"
scan_cells "$SCRATCH/s86p.md" $P-71.md "$SCRATCH/s72p.md"
```

Unit 92 §4's needle scan runs beside it over the same folder, then again with a scratch spec added whose
one `STRINGS` block holds `one  two`. PINNED, measured 2026-11-24 at `594b406d3`: the first `scan_cells`
printed `cells 10 edges 3`, the second a `run` line for each planted needle and the same counts; unit
92's scan printed `blocks 14`, and with the scratch spec a `run` line and `blocks 15` (PINNED 2026-11-24).

### The predicate and the cites

Unit 88's AC19 predicate as the report names it,
`python -c "import sys; [print(p, sum(1 for l in open(p, encoding='utf-8') if chr(96)*3 in l.lstrip()[1:])) for p in sys.argv[1:]]"`,
runs over `memory/builds/dTotalRecall/spec/*.md`. PINNED, measured 2026-11-24 at `594b406d3`: 0 for every
spec but two CLOSED ones, unit 70's at 3 and unit 76's at 1 (PINNED 2026-11-24).

The cite scan, from the spec folder, over specs 90, 89 and 91:

```bash
grep -nE '(spec [0-9]+|\.(js|sh|py|md)(@[0-9a-f]{7,40})?):[0-9]+' 2026-10-26-spec-TOOL-dTotalRecall-{90,89,91}.md
```

At `594b406d3` it printed five lines, all of spec 91 and all pinned at `f7011dd6f`, and over the scratch
file `printf 'spec 88%s
x.js%s
' :115 :76-80` writes it printed both (PINNED 2026-11-24).

### Why order 41

Units 98 and 99 hold 40, after unit 92 at 39. Every item reads a landed unit or its records, so this
unit builds last. The §3 edges hold the order: `--dispatch` refuses a unit while a unit of its build it
consumes from is neither CLOSED nor WONTDO (`tools/unattended/unattended.sh#verb_dispatch`, reading
`tools/unattended/lib-unattended.sh#read_consumes_from`).

### Inventory

Minted: the functions `scan_edits`, `write_free_restore`, `write_free_restores`, `read_shared`,
`check_swept` and `scan_cells` and the amended scan, spec text only; deviation, correcting and
withdrawing records where §2's reads are red; restored records under a free `<n>` where S12 owes one.
Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (the records, the restored records and this unit's ledger)

### Alternatives rejected

- **Two batches.** S2, S3, S4, S10 and S12 write or restore deviation records, whose `<n>` the door mints
  from one folder; two concurrent writers are the collision `<n>` sharing names, so BUILD-METHOD M6's
  clause 1 keeps them one unit.
- **Restore a taken path by overwriting it (id 24).** The newer record would be lost from the working
  tree; a free `<n>` keeps both.
- **Edit the specs of units 89 to 92 by rev bump.** Each is frozen once its unit builds, and each builds
  before order 41.
- **A second ancestry walk and a second sweep loop, as rev-1 spelled them.** Unit 89 rev-3's walk and unit
  78's loop already give each outcome, so a copy would be a second spelling of each.

## 5. Production-readiness checklist

- security — no new write surface; S12 restores files the door wrote, from git's own objects.
- perf / scale — the scan, the join, `key59` and the ancestry walk each read the build folder once; S13
  adds one checker run per unswept unit, off the pass.
- error / empty / loading states — an unresolved pass is a red line; an ancestry error prints its
  status; a taken path is restored under a free `<n>`, never overwritten; a blob that cannot be read
  leaves no file behind; a listing from the wrong directory prints nothing, which `read_shared`'s
  positive count and unit 98's liveness line rule out.
- observability — every red names its read; the ledger sets each value beside the landed unit's own.
- risks — S12 changes a restored record's stem, so the ledger names the old and new path together, and a
  record superseding the old stem is named beside it.
- testing — AC1 to AC20 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

"As at HEAD" marks a reading the pass observes and builds nothing for.

- **AC1** — When §4's fixture runs, its `malformed` block prints one `malformed` line and its `superseded`
  block prints `malformed-superseded`, no `malformed` line and `scan ok 2 1`, and at the pass tip
  `tip_check` over the build folder prints no `malformed` line and ends `scan ok`.
  Red when: a superseded record keeps AC8 red, or a live malformed record is reported as superseded.
  fixture: the repository is made under the pass's scratch folder; the tree holds none.
  figure: the lines are PINNED in §4, measured 2026-11-24.
- **AC2** — When `scan_edits` runs after the pass, every record it lists is named in the ledger's AC2 line
  with its commit and `Pass:` trailer, and `has_deviation memory/builds/dTotalRecall/build <unit> 'audit-89 id 23 s2'`
  prints 1 for each unit whose pass modified a record outside a restore, else 0. The listing holds at
  least the three commits §4 pins.
  Red when: a record edited by hand goes unnamed, or the listing is read empty from another directory.
- **AC3** — When §4's fixture runs, its `pair` block prints one `dup` line and its `corrected` block
  prints none and ends `scan ok 3 2`, and at the pass tip the scan prints no `dup` line, as at HEAD.
  Red when: a correcting record re-creates the pair's key.
  fixture: as AC1's.
  figure: the lines are PINNED in §4, measured 2026-11-24.
- **AC4** — When `has_deviation --paths memory/builds/dTotalRecall/build 69 'audit-77 id 23 s4'` runs after
  the pass, no record it lists was written from a `no-status-line` verdict while
  `TOOL-dTotalRecall-97`'s ledger shows a placed `p69` status line, and each one withdrawn is named
  with its withdrawing record.
  Red when: a record of unit 69 states a parse failure as an unobserved criterion.
- **AC5** — When `memory/guides/SESSION-KICKOFF.md` at the commit `pass_of 69` prints is read with
  `git show` and counted with `grep -c 'kickoff-manifest:'`, it prints 1, as at HEAD, the ledger's AC5
  line quotes it, and `has_deviation memory/builds/dTotalRecall/build 69 'audit-89 id 7 s5'` prints 0.
  Red when: unit 69's AC1 stands green on a read in which the checker skipped every check.
- **AC6** — When `has_deviation memory/builds/dTotalRecall/build 59` runs at the pass tip with the
  string `` `absorbs` is absent ``, it prints at most 1, as at HEAD.
  Red when: two live records of unit 59 name the departure.
- **AC7** — When `key59 memory/builds/dTotalRecall/build` runs at the pass tip, it prints no `missing`
  line and its two numbers are equal, as at HEAD, or the ledger names each missing record by path as
  unowed. `grep -l 'Caused-by:.. TOOL-dTotalRecall-100'` over the folder's
  `*-build-TOOL-dTotalRecall-59-deviation-*.md` files lists nothing, or only a correcting record of S3.
  Red when: a record of unit 59 written after order 37 names the string without `pass(59)` unnamed, or
  an unowed departure is re-stated.
- **AC8** — When unit 89 §4's two fences run at this pass's base, the walk prints one line for each path
  `has_deviation --paths` prints for unit 59, each verdict one of the four, and the red reads print what
  §4 pins for them.
  Red when: a counted record prints no verdict, or a git error reads as `before-p83`.
  figure: the lines are PINNED in §4, measured 2026-11-24.
- **AC9** — When `check_ancestry` runs with `HEAD` over a record path no commit added, a none-deviation-0.md
  in the build folder, it prints `at-or-after-p83 untracked`, as at HEAD.
  Red when: a record with no adding commit reads as before `pass(83)`.
- **AC10** — When `check_ancestry <path> "red 83 no pass commit"` runs, it prints
  `ungraded p83 red 83 no pass commit`, and
  `has_deviation memory/builds/dTotalRecall/build 89 'audit-89 id 31 s10'` prints 1 where unit 89
  answered its S1-at-least-1 arm green with a red or ungraded line or without a `before-p83` line per
  counted record, else 0.
  Red when: an unresolved `pass(83)` leaves AC13 green.
- **AC11** — When the ledger's AC8 line is read, its walk paths are exactly the paths
  `has_deviation --paths memory/builds/dTotalRecall/build 59` prints, and include every path it prints with
  the string, and with `pass(59)` and the string.
  Red when: the walk reads a record the counter's list does not hold, or misses one it does.
- **AC12** — When §4's fixture runs, its `free` and `again` blocks print what §4 pins; and when
  `write_free_restores 462d20f3..HEAD` runs after the pass, it prints no `restored`, `red` or `refused`
  line save a `moved-since` one, every path `deleted_records` prints exists in the tree or names a record
  the ledger's AC12 line restored under a free `<n>`, and AC20's read prints no `malformed:` line naming one.
  Red when: a restore overwrote a record, put one back twice or left two files at one `<n>`.
  fixture: as AC1's.
- **AC13** — When `check_swept "$SWEEP"` runs at this pass's base, with the brief's lines of a re-run
  added where one was owed, it prints no `unswept` line, its `none` lines name exactly the units of the
  population whose spec is not CLOSED, and its `population` line counts the rest as swept; the ledger
  quotes it.
  Red when: a population unit with a pass is led by no verdict at it.
  cost: one checker run per unswept unit.
  permission: as S13's.
- **AC14** — When `git worktree list --porcelain` and `ls "$(git rev-parse --git-common-dir)"` run at the
  pass tip, no worktree path ends `/gate-mc92` or `/gate-mc100` and no entry is named either, as at HEAD,
  and the first prints at least one `worktree` line.
  Red when: a sweep's worktree outlives it.
- **AC15** — When `scan_cells` and unit 92's needle scan run over the build's specs, they print
  `cells 10 edges 3` and the `blocks` line and no `run` or `empty` line, as at HEAD, and over the planted
  copies and the planted scratch spec each prints its `run` lines as §4 pins.
  Red when: a needle the build's reads consume is never scanned, or a planted run goes unseen.
  fixture: the planted copies are made in the run's scratch by the pass.
  figure: the counts are PINNED in §4, measured 2026-11-24; `blocks` is DERIVED at the pass.
- **AC16** — When §4's predicate runs over `memory/builds/dTotalRecall/spec/*.md`, it prints 0 for
  every spec of units 77 to 100, as at HEAD, and above 0 for at least one other, its liveness, which the
  ledger names.
  Red when: a spec of this round carries a mid-line triple backtick.
  figure: the counts of §4 are PINNED, measured 2026-11-24; the rest are DERIVED.
- **AC17** — When §4's cite scan runs, it prints no line of spec 90, as at HEAD, and
  `grep -n "units.slice().sort" tools/workflows/unattended-build.js` prints one line, which the ledger quotes.
  Red when: a line cite of spec 90 stands unread, or the comparator is cited by a comment's line.
- **AC18** — When §4's cite scan runs, it prints no line of spec 89, and each line of spec 91 it prints is
  pinned at `f7011dd6f`; the ledger's AC18 line sets the text `git show` gives at each first-cited line
  beside its cite, and over the scratch file of two bare cites the scan prints both.
  Red when: a cite names a line that does not hold its token, or the scan sees no bare cite.
- **AC19** — When `has_deviation memory/builds/dTotalRecall/build 88 'audit-77 id 1 '` runs at the pass
  tip, it prints the count unit 89's AC3 recorded, and over a scratch folder holding one record of unit
  88 whose Evidence holds `audit-77 id 12 s8`, it prints 0 where `audit-77 id 1` prints 1.
  `grep -lE 'audit-(77|89) id [0-9]+([^0-9 ]|$)'` over the folder's `*-deviation-*.md` files lists nothing,
  and over a scratch file holding `audit-89 id 1` at a line's end it lists it.
  Red when: a token of another id matches the delimited token, or a record carries a bare one.
  fixture: the folder and file are made in the run's scratch by the pass, the record built from
  `2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md` with only Serves and Evidence changed.
  figure: 0 and 1 over that folder are PINNED, measured 2026-11-24 at `39ffc882e`; the tip count is DERIVED.
- **AC20** — When `read_shared . memory/builds/dTotalRecall/build` runs from the repository root at the pass
  tip, it prints a `read` count equal to the number of `*-deviation-*.md` files `git ls-files` lists there
  and no `malformed:` line, as at HEAD, the scan prints no `untracked` line, and the fixture's `shared`
  block prints two `malformed:` lines.
  Red when: two records of this build share an `<n>`, or a collision goes unmarked.

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
- **F2 — Must each population unit lead an `rc=` line, as rev-1 wrote S13?** Options: (a) yes, every one;
  (b) each whose pass resolves, the held units named with their `red no pass commit` cause. The units
  deferred to owner asks have no pass, so (a) reds on a correct tree; veto 1 discards it.
  RESOLVED (agent, 2026-11-24, delegated): (b), the one survivor, the rule unit 78's AC1 states, per
  `2026-11-24-prompt-TOOL-dTotalRecall-100-reground-brief`. widens: none · relaxes: none
- **F3 — Which unit's record does S2 write for an edit a `Pass: none` commit made?** Options: (a) one of
  the unit whose record was edited; (b) none, the ledger naming the commit. S2's record is "of the unit
  whose pass made it", and no pass made such an edit, so under (a) a unit answers for the main loop's
  commit; the goal is that no pass cleared a criterion by hand. RESOLVED (agent, 2026-11-24, delegated): (b),
  the reading of S2's own words, per `2026-11-24-prompt-TOOL-dTotalRecall-100-reground-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, its 20
  confirmed minors: 14 MEDIUM, ids 3 4 6 7 13 14 19 21 23 24 25 26 31 32 (items M1 to M9), and 6 LOW,
  ids 9 10 11 16 17 22 (items L1 to L5).
- rev-2 · 2026-11-24 · §1 · S2 to S20 · §3 · §4 · §5 · AC1 to AC20 · §8 F2 F3 · §10 · re-grounded at `39ffc882e`
  per `2026-11-24-prompt-TOOL-dTotalRecall-100-reground-brief`, over units 76 and 83 as built and the
  re-grounded specs 78 and 84 to 99: the record of S5, the re-statement of S7 and the re-pointed cites of
  S17 and S18 are cut, their causes gone before any code; S8 to S11 observe unit 89's walk; S13 runs unit
  78's loop with two traps, only where `check_swept` names a unit (F2); S2 reads the `Pass:` trailer (F3);
  S12's free restore is spelled and seen over the fixture; S20 reads the join by a probe; every probe was
  run and re-pinned; citations name symbols or are pinned. No scope item or criterion is dropped.

## 10. Reuse audit

The seams, re-read at `39ffc882e`, are those the minors name: `TOOL-dTotalRecall-93`'s `has_deviation` and
correcting record; `TOOL-dTotalRecall-95`'s `key59`; `TOOL-dTotalRecall-97`'s `c5_input`;
`TOOL-dTotalRecall-99`'s scan, amended; `TOOL-dTotalRecall-98`'s `write_restores`, whose refusals
`write_free_restores` reads; unit 89 rev-3's `check_ancestry`; unit 78's sweep loop and unit 92's needle scan;
the join `tools/memory-tree/deviation_join.py#read_records`, which already marks a shared `<n>`; the
door's `<n>` rule, `tools/memory-tree/build_records.py#write_record`; and the scratch-worktree
pair of `tools/run-gates/lib-attribute.sh#add_scratch_worktree`.
`python tools/codebase-map/reuse_lookup.py "put a deleted record file back under a free number"`, run
2026-11-24, ranked `read_records` and `write_record` among its SEAM candidates, the two S20 and S12 read,
and no restore under a new number. The recall query below, re-run 2026-11-24, found this audit's record,
specs 92 and 99 and this spec, and no other reader of these minors.
`tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder walks of
`tools/memory-tree/record_causes.py#check_cause_writers` and
`tools/memory-tree/record_kinds.py#check_alias_compares` are no seam here: this unit reads no marker and
no registry. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how is each minor finding over a deviation-record reading made once at the tip and recorded" --terms "deviation record tip scan malformed superseded dup ancestry pass(83) restore free n sweep resume needle scan"`
