# TOOL-dTotalRecall-81 — the guarded revision read: a pass commit resolved by the driver's rule, verified as a commit and read by `read_blobs_at`, refused when any step answers empty, first applied to unit 71's PASS67

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 22 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |

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
  pass commit through `pass_commit` (`tools/unattended/lib-unattended.sh:1026`), and the shell
  function `read_at`, which verifies a revision with `tree_lib.read_git_output`
  (`tools/memory-tree/tree_lib.py:278`) and reads its blob with `tree_lib.read_blobs_at`
  (`tools/memory-tree/tree_lib.py:328`). Every string it counts comes from a file written by a quoted
  heredoc, so no string is a shell argument. Observed by AC1.
- **S2** — Its liveness. At this pass's base the read prints a red line, and exits 1, for each of four
  inputs: an empty revision, a bare `^`, a revision naming no commit, and a unit with no pass commit.
  It prints the pinned counts of §4 over specs 59 and 62 at `653bed738`. Observed by AC1.
- **S3** — Unit 71's PASS67. At this pass's base `pass_of 67` resolves unit 67's pass commit, and the
  ledger prints its sha beside the line unit 71's AC3 recipe prints at the same base. Where the
  recipe prints an empty line or another sha, unit 71's `pass67` count was read at a revision that
  was not unit 67's pass, and this pass writes a deviation record of `TOOL-dTotalRecall-71` naming
  both values. Before writing, it reads whether such a record already exists. Observed by AC2.
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

## 4. Design

### The read

Run from the repository root. `pass_of` takes a unit number. `read_at` takes a revision, a spec
number and the path of a strings file, one string per line.

```bash
# run from the repository root
source tools/unattended/lib-unattended.sh
pass_of() {  # unit number -> its first pass commit's sha, or a red line and rc 1
  local s; s=$(pass_commit 462d20f3 "TOOL-dTotalRecall-$1" memory/builds/dTotalRecall/RUN.md) || s=""
  [ -n "$s" ] || { echo "red $1 no pass commit"; return 1; }
  printf '%s\n' "$s"
}
read_at() {  # revision · spec number · strings file -> "<sha> <count> <string>" per string, or a red line and rc 1
  REV=$1 SPEC=$2 python - "$3" <<'PROBE'
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

`pass_commit` is the driver's pass rule. It reads the token rule of a `Pass:` trailer, so
`Pass: A, B` names both, falls back to the subject where a commit carries no trailer, and skips a
commit that touches only the run-state file. `deviation_join.read_first_passes`
(`tools/memory-tree/deviation_join.py:325`) states the same rule in Python. Text is joined on
whitespace before counting, as unit 67 §4 joins it.

### Why each step refuses

| Input | What git does unguarded | What `read_at` prints |
|---|---|---|
| empty revision | `git show ':./<spec>'` reads the index blob, exit 0 | `red no revision before its parent mark` |
| bare `^` | `git show '^:./<spec>'` prints nothing, exit 0 | `red no revision before its parent mark` |
| a sha naming no commit | `git show` exits 128 | the `rev-parse` refusal `read_git_output` raises |
| a path the commit lacks | `git show` exits 128 | `red no blob at <sha>:<path>` |

PINNED, measured 2026-10-26 at `af814dba8` with this exact read: `` `absorbs` is absent `` prints
`653bed738685c8d41ee71fbf740a5e3654bdd703 0` over spec 59 and `... 1` over spec 62 at
`653bed738`. An empty revision, a bare `^` and `deadbeef` each print a red line and exit 1.
`pass_of 67` prints `red 67 no pass commit`, because no unit has a pass commit at that sha. The
unguarded `git show ':./<spec 59>'` printed 10962 bytes, the index blob.

### S3's comparison

```bash
P=$(pass_of 67); echo "driver $P"
echo "recipe $(git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-67$' 462d20f3..HEAD | head -1)"
```

The two lines go into the ledger. Equal values mean unit 71 read at unit 67's pass. Any other pair
means it did not, which S3 records.

### The deviation record

It is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-71`
with one `--field` per REQUIRED name of `tools/memory-tree/deviation_join.py:146`: `Departs from`
naming `TOOL-dTotalRecall-71` at its rev, `Hand-off` `spec-to-code`, `Cause` `review finding`, the
approver under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`), and `Caused-by`
`TOOL-dTotalRecall-81`. Its Evidence names item H2, both lines of S3 and this unit's ledger. The
record is written only where
`git grep -l "deviation TOOL-dTotalRecall-71" -- memory/builds/dTotalRecall/build` lists no record
whose Evidence names item H2.

### Why order 22

The read must exist before the first unit that re-reads through it, `TOOL-dTotalRecall-82` at step
22. Step 22 is the first step after unit 71's pass. The §3 edge runs this pass before unit 82's.

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

## 5. Production-readiness checklist

- security — no surface. The strings files sit in the run's scratch directory.
- perf / scale — one `pass_commit` walk per unit and one `git cat-file --batch` per read.
- error / empty / loading states — each of the four inputs of §4's table is a red line with rc 1,
  never a count. A unit with no pass commit is `red <n> no pass commit`.
- observability — every count line carries the full sha it was read at.
- risks — `pass_commit` returns the FIRST pass commit. A unit built over several passes is read at
  its first, which is the text it was built from.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `read_at` and `pass_of` of §4 run at this pass's base, `read_at 653bed738 59` and
  `read_at 653bed738 62` over the string of §4 print 0 and 1 with the sha `653bed738685`, and the
  inputs `''`, `^`, `deadbeef` and `pass_of 67` before unit 67's pass each print a line starting
  `red` and exit 1.
  Red when: any of the four inputs prints a count, or a count line carries no sha.
  figure: the counts are PINNED in §4, measured 2026-10-26.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-81" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names the `driver` and `recipe` lines of §4. Where they differ,
  `git grep -l "deviation TOOL-dTotalRecall-71" -- memory/builds/dTotalRecall/build` prints exactly
  one record whose Evidence names item H2.
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

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 37
  (HIGH, item H2, shared with id 10).

## 10. Reuse audit

The seams are the driver's pass rule `pass_commit` (`tools/unattended/lib-unattended.sh:1026`), the
kit's one revision runner `tree_lib.read_git_output` and its one blob reader `tree_lib.read_blobs_at`
(`tools/memory-tree/tree_lib.py:278` and `:328`). `python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output`, `read_blobs_at` and `build_git_env` among its SEAM candidates, and
`run_git` in `deviation_join.py`; the first two are what this read calls. The recall query below
found the audit's own fix and `memory/builds/aUnmannedHelm/reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-2.md`,
which refused an unpinned base before a `git show` by `rev-parse --verify --quiet "$base^{commit}"`,
the same guard. No new seam is minted.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe"`
