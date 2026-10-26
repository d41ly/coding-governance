# TOOL-dTotalRecall-99 — the tip scan is graded only on a full read: it exits 0, counts the records it read against the folder, and its `by` lines sum to the live records

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 40 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-100 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 29 at HIGH**, its item **H5**, alone in that item. The skeptic judged the
finder's fix unsound, and this unit follows the corrected fix the report writes.

`TOOL-dTotalRecall-92` §6 grades its tip scan in AC8, AC11, AC15, AC16, AC18 and AC22 only by the
absence of a line: no `malformed`, `untracked`, `shared-n` or `dup` line, or at most one `by` line per
unit. Nothing reads the scan's exit status or requires a line to appear. The scan is a bare
`python -` heredoc that imports `deviation_join` from `tools/memory-tree` relative to the working
directory and reads each record with `read_text(encoding='utf-8')` outside any `try`. It exits
non-zero with nothing on stdout when it runs outside the repository root, when a record is not UTF-8,
or when the bare `python` is the Microsoft Store stub, which `tools/lib/resolve-python.sh` exists to
refuse. In each case those criteria certify a folder the scan never read.

This unit makes the scan witness its own read. It prints how many records it read and how many are
live, turns any read failure into a red line and a non-zero exit, and runs through the resolved
launcher. `tip_check` passes only when the scan exits 0, its record count equals the folder's, and
its `by` lines sum to the live count. It groups `by` and `dup` by `TOOL-dTotalRecall-93`'s
`unit_of`. The break is seen red, and unit 92's tip criteria are graded again through it. It repairs
`TOOL-dTotalRecall-92`, at order 40, one above that unit's 39.

## 2. Scope (IN)

- **S1** — The scan. §4's `tip_scan` is unit 92's, with four changes: it prints `records <n>` first
  and `live <n>` after the per-record lines; a record it cannot read prints `red unreadable <path>`
  and a failed `git ls-files` prints `red ls-files <rc>`; it exits 1 on any red; and `dup` and `by`
  group by `unit_of`, spelled as `TOOL-dTotalRecall-93` §4 spells it. It runs under the launcher
  `resolve_python` prints. Observed by AC1.
- **S2** — The criterion. §4's `tip_check` prints the scan's lines, then `scan ok <records> <live>`,
  only where the scan exited 0, its `records` value equals the number of `*-deviation-*.md` files `ls`
  lists in the folder, and the counts on its `by` lines sum to its `live` value. Otherwise it prints
  `red scan <why>` and returns 1. Observed by AC1.
- **S3** — Seen red. `tip_check` run one directory above the repository root prints
  `red scan exit 1`, and over a fixture repository holding a record that is not UTF-8 it prints
  `red unreadable` and `red scan exit 1`. Observed by AC2.
- **S4** — Unit 92's tip criteria, graded again. At this pass's base `tip_check` runs over
  `memory/builds/dTotalRecall/build`, and the ledger grades unit 92's AC8, AC11's `dup` half, AC15,
  AC16, AC18 and AC22's tip half as `scan ok` together with the absence of the line each names, beside
  unit 92's own answer. Where unit 92 answered green from a scan that read red here, or recorded no
  scan line that shows a full read, a deviation record of `TOOL-dTotalRecall-92` names each criterion,
  with the token `audit-89 id 29 s4`, by `TOOL-dTotalRecall-90` §4's recipe, only where
  `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 29 s4'` prints 0. Observed by AC3.

## 3. Non-goals (OUT)

- The `malformed` arm reading superseded records, and the `shared-n` arm that re-implements the join
  (items M1 and L5, ids 3, 23 and 22): the batch `TOOL-dTotalRecall-100`. This unit keeps both arms as
  unit 92 spells them.
- The restore listing (item H4, id 15): `TOOL-dTotalRecall-98`.
- Editing spec 92, frozen once its unit builds.
- The checklist entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-92` — its tip scan and the answers its ledger gives AC8, AC11, AC15, AC16, AC18 and AC22, which this unit witnesses and grades again
- **consumes-from** `TOOL-dTotalRecall-93` — `unit_of`, by which the scan groups its `by` and `dup` lines
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4's record is written through
- **hands-off** `TOOL-dTotalRecall-100` — `tip_scan` and `tip_check`, which that batch changes for ids 3, 23 and 22 and runs at the tip

## 4. Design

### The scan and its criterion

```bash
# run from the repository root
. tools/lib/resolve-python.sh; PY=$(resolve_python) || exit 2
tip_scan() {  # folder -> records, live, malformed, shared-n, untracked, dup, by and quoted lines; exit 1 on any red
  "$PY" - "$1" <<'SCAN'
import collections, glob, os, pathlib, re, subprocess, sys
sys.path.insert(0, 'tools/memory-tree')
import deviation_join
def unit_of(r):  # TOOL-dTotalRecall-93 section 4, spelled identically
    m = re.fullmatch(r'\d{4}-\d{2}-\d{2}-build-(' + deviation_join._ID + r')-deviation-\d+', r['id'])
    return m.group(1) if m else None
folder = sys.argv[1]
paths = sorted(p.replace(os.sep, '/') for p in glob.glob(os.path.join(folder, '*-deviation-*.md')))
print('records', len(paths))
ls = subprocess.run(['git', 'ls-files', '--', folder], capture_output=True, text=True)
if ls.returncode:
    print('red ls-files', ls.returncode); sys.exit(1)
tracked, recs, red = set(ls.stdout.split()), [], 0
for p in paths:
    try:
        recs.append(deviation_join.read_record(p, pathlib.Path(p).read_text(encoding='utf-8')))
    except Exception as e:
        print('red unreadable', p, type(e).__name__); red += 1
seen = collections.Counter(r['n'] for r in recs if r['n'] is not None)
for r in recs:
    for field, why in r['malformed']:
        print('malformed', r['path'], field, why)
    if r['n'] is not None and seen[r['n']] > 1:
        print('shared-n', r['path'], r['n'])
    if r['path'] not in tracked:
        print('untracked', r['path'])
gone = {r['supersedes'] for r in recs if r['supersedes']}
live = [r for r in recs if r['id'] not in gone]
print('live', len(live))
key = collections.defaultdict(list)
for r in live:
    key[(unit_of(r), r['before'], r['after'])].append(r['path'])
for ps in key.values():
    if len(ps) > 1:
        print('dup', *ps)
by = collections.Counter((unit_of(r) or '-', (r['caused_by'] or '').strip('`') or '-') for r in live)
for (u, c), n in sorted(by.items()):
    print('by', u, c, n)
for q in subprocess.run(['git', 'grep', '-l', 'deviation TOOL-dTotalRecall-', '--', folder],
                        capture_output=True, text=True).stdout.split():
    if q not in paths:
        print('quoted', q)
sys.exit(1 if red else 0)
SCAN
}
tip_check() {  # folder -> the scan's lines, then "scan ok <records> <live>" or "red scan <why>" and rc 1
  local out rc n live sum
  out=$(tip_scan "$1"); rc=$?
  printf '%s\n' "$out"
  [ "$rc" = 0 ] || { echo "red scan exit $rc"; return 1; }
  n=$(ls "$1" | grep -c -- '-deviation-.*\.md$')
  [ "$(printf '%s\n' "$out" | sed -n 's/^records //p')" = "$n" ] || { echo "red scan records, glob $n"; return 1; }
  live=$(printf '%s\n' "$out" | sed -n 's/^live //p')
  sum=$(printf '%s\n' "$out" | awk '$1 == "by" { s += $4 } END { print s + 0 }')
  [ "$sum" = "$live" ] || { echo "red scan by-sum $sum live $live"; return 1; }
  echo "scan ok $n $live"
}
```

An empty `by` field prints `-`, so every `by` line keeps four fields and the sum reads each count. The
folder count is `ls`, a reader independent of the scan's glob and parse.

PINNED, measured 2026-10-26 at `32febccb6` over `memory/builds/dTotalRecall/build`: `tip_check`
printed `records 8`, `live 8`, seven `by` lines whose counts sum to 8, and `scan ok 8 8`, and returned
0. Run one directory above the repository root it printed `red scan exit 1` and returned 1.

### The fixture repository

A fixture repository needs a short path on Windows, so it is made under the system temp directory,
never inside the worktree and never at a drive root.

```bash
# run from the repository root, with tip_scan and tip_check defined
R="$TEMP/r99"; rm -rf "$R"; mkdir -p "$R/tools" "$R/memory/builds/dFx/build"
cp -r tools/memory-tree "$R/tools/"
cp memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md "$R/memory/builds/dFx/build/"
printf '\377\376 not utf-8\n' > "$R/memory/builds/dFx/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-22.md"
(cd "$R" && git init -q && git add -A && git -c user.email=f@x -c user.name=f commit -qm fx)
(cd "$R" && tip_check memory/builds/dFx/build)
```

PINNED, measured 2026-10-26 with these exact commands: it printed `records 2`, `red unreadable`
naming `-deviation-22` with `UnicodeDecodeError`, `live 1`, one `by` line and `red scan exit 1`, and
returned 1.

### Why order 40

Unit 92 runs its tip scan at order 39, so this unit grades the folder that unit left.

### Inventory

Minted: the functions `tip_scan` and `tip_check`, spec text only; at most one deviation record of
`TOOL-dTotalRecall-92`. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the record of S4)

### Alternatives rejected

- **Require only the exit status.** A scan that exits 0 over a glob matching nothing, given the wrong
  folder, reads the same as a clean folder; the record count against `ls` is what tells them apart,
  and the report's corrected fix asks for it.
- **Grade the `by` lines' presence alone.** A scan that dropped a record before grouping still prints
  `by` lines; the sum against `live` catches the drop.

## 5. Production-readiness checklist

- security — no surface. The fixture repository sits under the system temp directory and is removed.
- perf / scale — one pass over the folder's records, about twenty at the tip.
- error / empty / loading states — a crash, a failed `ls-files`, an unreadable record, a count short of
  the folder and a sum short of the live records each print a `red` line and return 1; an empty
  folder prints `scan ok 0 0`.
- observability — every red names its cause; the ledger quotes the full scan beside unit 92's answers.
- risks — none beyond the scan's, which `TOOL-dTotalRecall-92` states.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `tip_check memory/builds/dTotalRecall/build` runs from the repository root at this
  pass's base, it returns 0 and its last line is `scan ok <n> <live>`, with `<n>` equal to the number
  of `*-deviation-*.md` files `ls` lists there.
  Red when: the scan's record count, or the sum of its `by` lines, falls short of the folder.
  figure: 8 and 8 are PINNED in §4 at `32febccb6`; at the pass both are DERIVED.
- **AC2** — When `tip_check memory/builds/dTotalRecall/build` runs one directory above the repository
  root, and when §4's fixture repository is checked, each prints `red scan exit 1` and returns 1, the
  second after a `red unreadable` line.
  Red when: either break prints `scan ok`, or prints nothing and returns 0.
  fixture: the repository is made under the system temp directory by the pass; the tree holds none.
  figure: the lines are PINNED in §4, measured 2026-10-26.
- **AC3** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-99" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC3 line quotes `tip_check`'s output at this pass's base and grades each of
  unit 92's AC8, AC11, AC15, AC16, AC18 and AC22 from it beside unit 92's answer, and
  `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 29 s4'` prints 1 where any of them
  differs or rested on no full read, else 0.
  Red when: a criterion is graded green from a scan that did not end `scan ok`, or a differing answer
  goes unrecorded.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is `tip_check` over the build folder, over a fixture repository and from
outside the repository root.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 29
  (HIGH, item H5).

## 10. Reuse audit

The seams are `TOOL-dTotalRecall-92`'s tip scan, witnessed here; `deviation_join.read_record`
(`tools/memory-tree/deviation_join.py:212`); `TOOL-dTotalRecall-93`'s `unit_of`; and
`tools/lib/resolve-python.sh`'s `resolve_python`, the launcher that runs each candidate.
`python tools/codebase-map/reuse_lookup.py "assign a deviation record to its unit by its file name stem"`
ranked `read_records` (`deviation_join.py:268`) among its SEAM candidates; it reads tracked files
only, and the scan's `untracked` arm needs the working tree, so the scan keeps the per-file reader.
The recall query below found this audit's item H5, unit 92's tip scan and the Facts line naming the
MS-Store stub. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how is a scan graded so a crash with empty output never reads as a clean folder" --terms "tip scan exit status records count live by sum unreadable resolve_python absence of a line criterion"`
