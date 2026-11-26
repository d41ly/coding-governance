# TOOL-dTotalRecall-81 — the guarded revision read: a pass commit resolved by the driver's rule, verified as a commit and read by `read_blobs_at`, refused when any step answers empty, first applied to unit 71's PASS67

**Status:** CLOSED · rev-4 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 22 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-81-deviation-811.md](../build/2026-10-26-build-TOOL-dTotalRecall-81-deviation-811.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-81-deviation-812.md](../build/2026-10-26-build-TOOL-dTotalRecall-81-deviation-812.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-81-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dTotalRecall-81-1-acceptance-ledger.md) | log | — |
| [2026-11-22-build-TOOL-dTotalRecall-81-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-81-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-11-22-prompt-TOOL-dTotalRecall-81-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-81-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-81-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-81-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-81-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-81-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |
| [2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md) | diff-review | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 TOOL-dTotalRecall-114 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 37 at HIGH**. It shares item **H2** with id 10, which is
`TOOL-dTotalRecall-82`.

`TOOL-dTotalRecall-71` (order 21) reads unit 57's spec at unit 67's pass commit as
`os.environ['PASS67'] + ':./' + SPEC` and never checks that PASS67 resolves. Its AC3 recipe, the first
line of a `git log --grep` pipe, prints an empty line where no commit carries the trailer. An empty
PASS67 makes the read `git show ':./<spec>'`, which reads the INDEX blob and exits 0, and a bare
`^` makes it `git show '^:./<spec>'`, which exits 0 with no output. Unit 71's §5 lists only "a
revision git show cannot read raises", so the unresolved pass is not a red. It is a read of the
wrong text.

This unit is the read every repair of this audit's H1, H2 and H3 items makes, spelled once. A pass
commit is resolved by the unattended driver's own pass rule. The revision is verified as a commit
before any read. The blob is read at that full sha, never at the index or the working tree. Each of
the three steps turns an empty answer into a printed red line, and every count it prints carries
the sha it was read at. At step 22 it is applied first to unit 71's PASS67. It repairs
`TOOL-dTotalRecall-71`, at step 22, one above that unit's order.

## 2. Scope (IN)

- **S1** — The read. §4 spells it once: the shell function `pass_of`, which resolves a unit's first
  pass commit as the driver does, `pass_commit` (`tools/unattended/lib-unattended.sh#pass_commit`)
  anchored at the unit's first dispatch row as `read_pass_declarations` prints it, with
  `tools/lib/resolve-python.sh` sourced so the trailer reader has a launcher; and the shell
  function `read_at`, which verifies a revision with `tree_lib.read_git_output`
  (`tools/memory-tree/tree_lib.py#read_git_output`) and reads its blob with `tree_lib.read_blobs_at`
  (`tools/memory-tree/tree_lib.py#read_blobs_at`). Every string it counts comes from a file written by
  a quoted heredoc, so no string is a shell argument. Observed by AC1.
- **S2** — Its liveness. At this pass's base the read prints a red line, and exits 1, for each of five
  inputs: an empty revision, a bare `^`, a revision naming no commit, a unit off the roster
  (`pass_of 999`), and a pass rule with no launcher to answer. It prints the pinned counts of §4 over
  specs 59 and 62 at `653bed738`. Observed by AC1.
- **S3** — Unit 71's PASS67. At this pass's base `pass_of 67` resolves unit 67's pass commit, and the
  ledger prints its sha beside the line unit 71's AC3 recipe prints at the same base. Where the
  recipe prints an empty line or another sha, unit 71's `pass67` count was read at a revision that
  was not unit 67's pass, and this pass writes a deviation record of `TOOL-dTotalRecall-71` naming
  both values, through `gov_record.py new deviation`, the door `TOOL-dTotalRecall-2` landed (CLOSED,
  its hands-off to this unit standing). Before writing, it reads whether such a record already
  exists. Observed by AC2.
- **S4** — The order. This pass precedes every unit that reads through S1: units 78, 80, 82, 83, 84,
  85, 86 and 88. Observed by AC3.

## 3. Non-goals (OUT)

- The re-read of unit 71's `pass67` count and the deviation record of unit 67 it decides:
  `TOOL-dTotalRecall-82`, which shares item H2 and reads through S1.
- Editing unit 71's spec, frozen once its unit builds at order 21.
- Any product code. The read is a probe of history, run by the passes that need it.
- The bug-class entry and spec lint the report suggests as the left-shift gate: the close's
  left-shift step (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-71` — its pass at step 21, its `pass67` count and its AC3 recipe, whose resolution of unit 67's pass this unit sets beside the driver's
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door the deviation record of S3 is written through
- **hands-off** `TOOL-dTotalRecall-82` — `pass_of` and `read_at`, through which that unit re-reads unit 71's `pass67` count
- **hands-off** `TOOL-dTotalRecall-83` — `pass_of` and `read_at`, through which that unit re-reads unit 74's `s1-59` count
- **hands-off** `TOOL-dTotalRecall-84` — `pass_of` and `read_at`, through which that unit re-reads unit 74's `s1-46` count
- **hands-off** `TOOL-dTotalRecall-85` — `pass_of` and `read_at`, through which that unit re-makes unit 76's S1 to S4 reads
- **hands-off** `TOOL-dTotalRecall-86` — `pass_of` and `read_at`, through which that unit re-makes unit 76's S5 and S6 reads
- **hands-off** `TOOL-dTotalRecall-78` — `pass_of`, which resolves each pass commit that unit's sweep visits
- **hands-off** `TOOL-dTotalRecall-80` — `pass_of`, which resolves unit 69's pass commit for that unit's two checker runs
- **hands-off** `TOOL-dTotalRecall-88` — `pass_of` and `read_at`, through which that batch makes its history reads
- **hands-off** `TOOL-dTotalRecall-89` — `pass_of`, which resolves unit 83's pass for that unit's ancestry check (the round-1 audit of units 77 to 88, id 1)
- **hands-off** `TOOL-dTotalRecall-90` — `pass_of` and `read_at`, which that unit's labelled read `s1` calls (the round-1 audit of units 77 to 88, id 22)
- **hands-off** `TOOL-dTotalRecall-92` — `pass_of`, `read_at`, its AC1 fourth input, its S3 case and its pin, which that batch observes, re-pins and corrects (the round-1 audit of units 77 to 88, ids 2, 11, 25, 28)
- **hands-off** `TOOL-dTotalRecall-100` — `pass_of`, which resolves the passes of units 69 and 83 for that batch's reads (the round-1 audit of units 89 to 92, ids 7, 14, 26, 31)

## 4. Design

### The read

Run from the repository root. `pass_of` takes a unit number. `read_at` takes a revision, a spec
number and the path of a strings file, one string per line.

```bash
# run from the repository root
. tools/lib/resolve-python.sh
. tools/unattended/lib-unattended.sh
pass_of() {  # unit number -> its first pass commit's sha, or a red line and rc 1
  local u="TOOL-dTotalRecall-$1" a s r R=memory/builds/dTotalRecall/RUN.md
  a=$(read_pass_declarations "$R" | awk -v u="$u" '$6 == u { print $5; exit }')
  [ -n "$a" ] || { echo "red $1 no pass commit"; return 1; }
  s=$(pass_commit "$a" "$u" "$R"); r=$?
  [ "$r" -le 1 ] || { echo "red $1 the pass rule could not answer, rc $r"; return 1; }
  [ -n "$s" ] || { echo "red $1 no pass commit"; return 1; }
  printf '%s\n' "$s"
}
read_at() {  # revision · spec number · strings file -> "<sha> <count> <string>" per string, or a red line and rc 1
  local py; py=$(resolve_python 2>/dev/null) || { echo "red no python launcher"; return 1; }
  REV=$1 SPEC=$2 "$py" - "$3" <<'PROBE'
import os, re, sys
sys.path.insert(0, 'tools/memory-tree')
import tree_lib
rev = os.environ['REV']
path = 'memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-%s.md' % os.environ['SPEC']
try:
    if not rev.split('^')[0]:
        raise OSError('no revision before its parent mark: %r' % rev)
    sha = tree_lib.read_git_output('.', ('rev-parse', '--verify', '--quiet', rev + '^{commit}')).decode().strip()
    body = tree_lib.read_blobs_at('.', [(sha, path)])[(sha, path)]
    if not body:
        raise OSError('no blob at %s:%s' % (sha, path))
except OSError as e:
    print('red', e)
    sys.exit(1)
t = re.sub(r'\s+', ' ', body)
for s in (l.strip() for l in open(sys.argv[1], encoding='utf-8')):
    if s:
        print(sha, t.count(s), s)
PROBE
}
```

A strings file is written by a heredoc whose delimiter is quoted, so bash expands nothing in it,
into the run's scratch directory:

```bash
cat > "$SCRATCH/s81.txt" <<'STRINGS'
`absorbs` is absent
STRINGS
```

`pass_commit` is the driver's pass rule, and the anchor is the driver's too: `check_pass_open`
(`tools/unattended/unattended.sh#check_pass_open`) asks it from each key `read_pass_declarations`
prints, `<utc> dispatch · item <anchor> <unit>`, and `pass_of` takes the unit's first key. It
reads the one trailer reader's tokens (`lib-unattended.sh#read_attribution_tokens`), so
`Pass: A, B` names both and `Pass: none` names nothing, falls back to the subject where a commit
carries no trailer, and skips a commit whose touch set, less the run-state file and the paths its
brief rows name, is empty. That reader needs `resolve_python`, which the library does not define
and its callers source; with none it returns 2, which `pass_of` names rather than reading as "no
pass commit". The spec-run base `462d20f3` is not an anchor: that window holds the spec run's
subject-named commits, and from it `pass_commit` answers a 2026-11-02 spec commit for unit 2.
`deviation_join.py#read_first_passes` reads the same tokens by committer date over routed paths,
a different rule, so this read takes the driver's. Text is joined on whitespace before counting,
as unit 67 §4 joins it.

### Why each step refuses

| Input | What git does unguarded | What `read_at` prints |
|---|---|---|
| empty revision | `git show ':./<spec>'` reads the index blob, exit 0 | `red no revision before its parent mark` |
| bare `^` | `git show '^:./<spec>'` prints nothing, exit 0 | `red no revision before its parent mark` |
| a sha naming no commit | `git show` exits 128 | the `rev-parse` refusal `read_git_output` raises |
| a path the commit lacks | `git show` exits 128 | `red no blob at <sha>:<path>` |

`pass_of` prints `red <n> no pass commit` for a unit with no dispatch row or no pass commit after
it, and `red <n> the pass rule could not answer, rc 2` where `pass_commit` had no launcher.

PINNED, measured 2026-10-26 at `af814dba8` and re-measured 2026-11-23 at `942294abe` with this
exact read: `` `absorbs` is absent `` prints `653bed738685c8d41ee71fbf740a5e3654bdd703 0` over spec
59 and `... 1` over spec 62 at `653bed738`. An empty revision, a bare `^`, `deadbeef` and spec 999
each print a red line and exit 1. At `942294abe`: `pass_of 10` prints `d735e47b9...`, the commit
unit 10 closed at, and `pass_of 2` prints `d91388c2f...`, unit 2's `Pass:` build commit; `pass_of
67` and `pass_of 999` print their no-pass red; with `resolve_python` unset `pass_of 10` prints the
rc-2 red. Rev-3's `pass_of`, the library alone sourced and anchored at `462d20f3`, printed `red 10
no pass commit` and, with a launcher, `66f7b8d32...` for unit 2. The unguarded
`git show ':./<spec 59>'` printed 12639 bytes, the index blob (PINNED 2026-11-23, 10962 at `af814dba8`),
and `git show '^:./<spec 59>'` 0 bytes, both exit 0 (PINNED 2026-11-23).

### S3's comparison

```bash
P=$(pass_of 67); echo "driver $P"
echo "recipe $(git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-67$' 462d20f3..HEAD | head -1)"
```

The two lines go into the ledger. Equal values mean unit 71 read at unit 67's pass. Any other pair
means it did not, which S3 records.

### The deviation record

`python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-71 --title <text>`
renders `**Serves:** deviation TOOL-dTotalRecall-71`
(`tools/memory-tree/build_records.py#write_new_record`, which refuses a missing `--title` and, by its
check of the rendered text before any write, a missing required field). It takes one `--field` per required name of the deviation entry of
`tools/memory-tree/build_records.py#KINDS`, each value inside that entry's closed sets, spelled as
unit 71 §4 and unit 82 §4 spell their records:

- `Departs from` `TOOL-dTotalRecall-71@rev-<n> [§6 AC3]`, the rev unit 71's header holds at its pass.
- `Hand-off` `spec-to-code`; `Cause` `review finding`; `Risk` `loosening`, as the `pass67` count was
  read at a revision that was not unit 67's pass.
- `Before` the recipe line of S3; `After` the driver line of S3; `Reason` the recipe's empty or
  wrong first line, which `git show` reads as the index or as nothing.
- `Approver` opening with the role `author`, under the chain's `author-recorded` value
  (`tools/memory-tree/deviation_join.py#HOST_APPROVAL`, `PLAY-dClosedLoop-4`);
  `deviation_join.py#check_approver` refuses an approver naming no role.
- `Follow-through` `ask TOOL-dTotalRecall-27`; `Caused-by` `TOOL-dTotalRecall-81`.
- `Evidence` item H2 of the round-7 audit (`2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1`),
  both lines of S3 and this unit's ledger.

It is written only where
`git grep -l --all-match -e 'Serves:\*\* deviation TOOL-dTotalRecall-71$' -e 'Caused-by:\*\* TOOL-dTotalRecall-81$' -- memory/builds/dTotalRecall/build`
lists nothing. At `942294abe` it lists nothing and exits 1, and with `PLAY-dClosedLoop-2` for the
cause it lists `2026-10-26-build-TOOL-dTotalRecall-71-deviation-711`, the roster promotion
(DERIVED 2026-11-23), so the predicate is seen both ways and that record never counts.

### Why order 22

The read must exist before the first unit that re-reads through it, `TOOL-dTotalRecall-82` at step
22. Step 22 is the first step after unit 71's pass. The §3 edge runs this pass before unit 82's:
`--dispatch` refuses a unit while a unit of its build it consumes from is neither CLOSED nor WONTDO
(`tools/unattended/unattended.sh#verb_dispatch`, reading
`tools/unattended/lib-unattended.sh#read_consumes_from`), and unit 82 consumes from this one.

### Inventory

Minted: the probe functions `pass_of` and `read_at`, spec text only; at most one deviation record
of `TOOL-dTotalRecall-71`. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger, and the deviation record S3
  writes where the resolutions differ)

### Alternatives rejected

- **`git show <rev>:<path>` with `check=True`, as units 71, 74 and 76 wrote it.** An empty and a
  bare-`^` revision both exit 0, so `check=True` refuses neither. That is the defect.
- **The `git log --grep` first line as the pass rule.** It misses a joint `Pass: A, B` trailer and
  the subject fallback, and it prints an empty line where nothing matches (item M7, id 19).
- **A new product helper in `tree_lib.py`.** The read serves this build's history checks only. The
  two library functions it calls are the kit's one revision verifier and its one blob reader, so a
  third function would add a name with one caller.
- **Single-quoted strings as shell arguments.** A string holding a `'` breaks it again. A quoted
  heredoc into a file holds both.
- **`pass_commit` from the spec-run base `462d20f3`, as rev-3 wrote it.** That window holds the spec
  run's commits, and one whose subject names a unit with no trailer reads as its pass: unit 2's
  answer there is a 2026-11-02 spec commit. The driver anchors at the dispatch row.

## 5. Production-readiness checklist

- security — no surface. The strings files sit in the run's scratch directory.
- perf / scale — one `pass_commit` walk per unit and one `git cat-file --batch` per read.
- error / empty / loading states — each of the four inputs of §4's table is a red line with rc 1,
  never a count. A unit with no dispatch row or no pass commit is `red <n> no pass commit`; a pass
  rule with no launcher is `red <n> the pass rule could not answer, rc 2`, never that.
- observability — every count line carries the full sha it was read at.
- risks — `pass_commit` returns the FIRST pass commit after the unit's first dispatch row. A unit
  built over several passes is read at its first, which is the text it was built from. The rows are
  read from `RUN.md`; once a run-state rotation moves them to an archive, `pass_of` prints the
  no-pass red, never a wrong sha.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `read_at` and `pass_of` of §4 run at this pass's base, `read_at 653bed738 59` and
  `read_at 653bed738 62` over the string of §4 print 0 and 1 with the sha `653bed738685`; the
  inputs `''`, `^` and `deadbeef` to `read_at`, `pass_of 999`, and `pass_of 10` in a subshell with
  `resolve_python` unset each print a line starting `red` and exit 1; and `pass_of 10` prints
  `d735e47b9...`.
  Red when: any of the five inputs prints a count or a sha, the rc-2 input prints `no pass commit`,
  or a count line carries no sha.
  figure: the counts and shas are PINNED in §4, re-measured 2026-11-23.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-81" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names the `driver` and `recipe` lines of §4. Where they differ,
  `git grep -l --all-match -e 'Serves:\*\* deviation TOOL-dTotalRecall-71$' -e 'Caused-by:\*\* TOOL-dTotalRecall-81$' -- memory/builds/dTotalRecall/build`
  prints exactly one record, whose Evidence names item H2.
  Red when: the two resolutions differ and no record names it, or two records name it.
- **AC3** — When `pass_of 82` resolves unit 82's pass commit,
  `git merge-base --is-ancestor <pass_of 81> <pass_of 82>` exits 0.
  Red when: unit 82 re-reads before the read it rests on is committed.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the read is a probe whose liveness AC1 observes on four refused inputs and two pinned
counts.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which input stands for AC1's fourth, "`pass_of 67` before unit 67's pass"?** This pass runs
  at order 22, after unit 67's pass at order 20, so that input cannot be produced at its base, as
  `TOOL-dTotalRecall-92` S2 found. Options: (a) keep it and leave its departure to unit 92's record
  at order 39; (b) `pass_of 999`, an id off the roster, the replacement unit 92 S2 names,
  plus the rc-2 input the re-ground's launcher finding adds. (a) fails AC1 as written; veto 1
  discards it. RESOLVED (agent, 2026-11-23, delegated): (b), the one survivor, per
  `2026-11-22-prompt-TOOL-dTotalRecall-81-reground-brief`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 37
  (HIGH, item H2, shared with id 10).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-89, TOOL-dTotalRecall-90, TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-100, each the other end of an edge a
  unit the round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.
- rev-4 · 2026-11-23 · §2 · §4 · §5 · §6 · §8 · §10 · per `2026-11-22-prompt-TOOL-dTotalRecall-81-reground-brief`,
  re-grounded at `942294abe`: `pass_of` sources the launcher resolver and names `pass_commit`'s rc 2,
  and anchors at the unit's first dispatch row, not the spec-run base; `read_at` runs the resolved
  launcher; line citations re-pointed to symbols; the deviation record spells every field of
  `build_records.py#KINDS` and its existence grep is sharpened; AC1's fourth input settled by F2;
  counts re-pinned. Names, signatures and output shape of `pass_of` and `read_at` unchanged.

## 10. Reuse audit

The seams are the driver's pass rule `pass_commit` with its dispatch keys `read_pass_declarations`
(`tools/unattended/lib-unattended.sh#pass_commit`, `#read_pass_declarations`), the one launcher
resolver `tools/lib/resolve-python.sh`, the kit's one revision runner `tree_lib.read_git_output` and
its one blob reader `tree_lib.read_blobs_at` (`tools/memory-tree/tree_lib.py#read_git_output`,
`#read_blobs_at`). `python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output`, `read_blobs_at` and `build_git_env` among its SEAM candidates, and
`run_git` in `deviation_join.py`; re-run 2026-11-23 it ranks `read_blobs_at`, `run_git` and
`read_git` among them; the first two named are what this read calls. The recall query below
found the audit's own fix and `memory/builds/aUnmannedHelm/reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-2.md`,
which refused an unpinned base before a `git show` by `rev-parse --verify --quiet "$base^{commit}"`,
the same guard; re-run 2026-11-23 it also ranks `TOOL-dWitnessedBar-88` S5, one pass-commit lookup
through `build_commit`, which asks which commit built a unit over its build folder, not the pass
rule a dispatch row closes. No new seam is minted.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe resolve_python launcher"`
