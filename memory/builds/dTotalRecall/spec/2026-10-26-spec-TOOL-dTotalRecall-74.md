# TOOL-dTotalRecall-74 — unit 70's backticked strings are re-read at step 34 by a probe no shell quotes, and unit 70's S3 departure for unit 59 is decided from the count

**Status:** CLOSED · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 34 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-74-deviation-741.md](../build/2026-10-26-build-TOOL-dTotalRecall-74-deviation-741.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-74-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-74-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-74-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-74-1-builder-return.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-74-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-74-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-74-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-74-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-74-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-74-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md) | diff-review | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 TOOL-dTotalRecall-114 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
confirmed finding **id 11 at HIGH**, its item **H3**, alone in that item.

`TOOL-dTotalRecall-70` (order 33), as audited, defined "the probe" as unit 67 §4's joined-text count, whose
template passes each string in shell double quotes. Its §4 table wants 1 for its string over unit 59's spec at
`pass(59)^`, `` `absorbs` is absent ``. Double-quoted, bash runs `absorbs` as a command and the probe counts
` is absent`, which printed 2 over spec 59 where the count was 0 (PINNED 2026-10-26, that audit's id 11). The row was
green before unit 62's amendment existed, so unit 70's AC1 could certify that unit 59 built from unit 62's amended
text when it had not, and the deviation record unit 70's S3 would owe would never be written. Its reading of
`` Minted: `SUFFIX_RE` `` over unit 46's spec had the same hazard.

Re-grounded at `db95ebf86`: `TOOL-dTotalRecall-70` rev-4 already reads through a quoted heredoc, so the hazard is gone
from the text its pass builds from. Units 46, 59 and 62 have passed. At `pass(59)^` the first string reads 1, so unit 59
built from unit 62's amended text and no departure is owed. What stands is the independent check the finding asks for:
this unit re-reads the two strings at verified revisions by a probe whose strings never pass through the shell, proves
the probe reads a 0 and a 1, decides unit 70's S3 departure from the count, and sets both counts beside the ones unit
70's ledger records. It repairs `TOOL-dTotalRecall-70`, at step 34, one above that unit's order.

## 2. Scope (IN)

- **S1** — The re-read. The probe of §4 counts `` `absorbs` is absent `` over unit 59's spec at
  `pass(59)^`, and `` Minted: `SUFFIX_RE` `` over unit 46's spec at `pass(46)^`, each line naming the sha it read.
  Observed by AC1.
- **S2** — The liveness. The same run counts `` `absorbs` is absent `` over unit 59's spec at
  `653bed738`, which must print 0, and over unit 62's spec at `653bed738`, which must print 1. It
  counts `` Minted: `SUFFIX_RE` `` over unit 46's spec at `653bed738`, which must print 1. An empty revision and a bare
  `^` must each be refused. Observed by AC1.
- **S3** — The departure, decided. S1's first count is 1, a property of a blob that cannot move, so unit 59 built from
  unit 62's amended text and no deviation record of `TOOL-dTotalRecall-59` is owed. The write is cut with that reason.
  Unit 70's S3 decides the same, and this pass reads that no record of unit 59 names `pass(59)` or its sha. It runs the
  criterion unit 62's amendment carried, both greps of unit 59's AC2, at the tip. Observed by AC2.
- **S4** — The record. This unit's ledger names both S1 counts beside the counts unit 70's AC1 and
  AC8 lines recorded for them. A count unit 70 recorded at 1 or more where S1 reads 0 is named there as a
  false certification, and so is an AC1 count of 0 for the first string. At `pass(46)^` the second string reads 0, which
  unit 70 rev-4 §4 pins. Observed by AC3.

## 3. Non-goals (OUT)

- Unit 70's other rows. Two of them hold backticks, and rev-4's blob probe reads every row through a quoted heredoc. The
  second reading of those rows (ids 2 and 25) is the batch `TOOL-dTotalRecall-76`'s.
- Editing unit 70's spec, frozen once its unit builds at order 33.
- Unit 46's body, which unit 70's S16 and S17 judge by the code. `` Minted: `SUFFIX_RE` `` is a
  text reading, and S1 only corrects the record of it.
- The read through `TOOL-dTotalRecall-81`'s `pass_of` and `read_at`: units 83 and 84 make it one step later.
- The three copies of the factory and the count of unit 59's records: `TOOL-dTotalRecall-88` (its ids 44 and 45).
- The bug-class entry or spec lint the report suggests as the left-shift gate: the close's
  left-shift step (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-70` — its pass at step 33 and its AC1 and AC8 ledger lines, whose counts for the two backticked strings this unit re-reads and corrects
- **hands-off** `TOOL-dTotalRecall-83` — its `s1-59` line and its S3 record, which that unit re-decides at the verified parent of unit 59's pass (the round-1 audit of units 71 to 76, id 9)
- **hands-off** `TOOL-dTotalRecall-84` — its `s1-46` line and its S4 comparison, which that unit re-makes at the verified parent of unit 46's pass (the round-1 audit of units 71 to 76, id 36)
- **hands-off** `TOOL-dTotalRecall-88` — its AC2 answer and the deviation records of unit 59, which that batch completes and makes one (the round-1 audit of units 71 to 76, ids 4, 14, 44, 45)

## 4. Design

### The probe

Each string is a Python literal inside a heredoc whose delimiter is quoted, so bash expands nothing
in it. The revisions are literals too, so no unset variable reaches `git`. `git show` of an empty revision reads the
index blob and of a bare `^` reads nothing, both at exit 0, so each revision is first resolved to a commit by
`git rev-parse --verify`, and `check=True` makes a failed resolve or read raise, a red, never a 0. Text is joined on
whitespace, as unit 67 §4 joins it.

```bash
# run from memory/builds/dTotalRecall/spec/
python - <<'PROBE'
import re, subprocess
ABS = '`absorbs` is absent'
MINT = 'Minted: `SUFFIX_RE`'
def read(*argv):
    return subprocess.run(['git', *argv], capture_output=True, check=True).stdout.decode('utf-8')
def count(rev, n, s):
    sha = read('rev-parse', '--verify', '--quiet', rev + '^{commit}').strip()
    raw = read('show', sha + ':./2026-10-26-spec-TOOL-dTotalRecall-%s.md' % n)
    return sha[:12], re.sub(r'\s+', ' ', raw).count(s)
for label, rev, n, s in (('s1-59', '47afc8937^', '59', ABS), ('s1-46', '63f283ddd^', '46', MINT),
                         ('live-59', '653bed738', '59', ABS), ('live-62', '653bed738', '62', ABS),
                         ('live-46', '653bed738', '46', MINT)):
    print(label, *count(rev, n, s))
for rev in ('', '^'):
    try:
        print('unrefused', repr(rev), *count(rev, '59', ABS))
    except subprocess.CalledProcessError:
        print('refused', repr(rev))
PROBE
```

"pass(N)" is the first line of
`git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-N$' 462d20f3..HEAD`, as unit 70 §2
defines it. It prints pass(46) `63f283ddd`, whose parent is `254057fa6`, and pass(59) `47afc8937`, whose parent is
`206422580`. Unit 81 §4's `pass_of` prints the same two commits (DERIVED 2026-11-24, both commands).

PINNED 2026-11-24 at `db95ebf86`, this probe: `s1-59 206422580b73 1`, `s1-46 254057fa6d5b 0`, `live-59 653bed738685 0`,
`live-62 653bed738685 1`, `live-46 653bed738685 1`, then one `refused` line for each of the two revisions. The
double-quoted form printed 2 over spec 59 (PINNED 2026-10-26), with `absorbs: command not found` on stderr, as the
report's re-run shows.

### The deviation record

None is owed (S3). The key units 83 and 95 read stays this one: a record of unit 59 for this departure would be
written through `python tools/memory-tree/gov_record.py new deviation`, `Hand-off: spec-to-code` (a value
`tools/memory-tree/build_records.py#KINDS` closes), and its Evidence would name `pass(59)`, the string, unit 62's §4 "The
amendments to unit 59", unit 70's AC1 line and this unit's `s1-59` count. The build's one record of unit 59 at
`db95ebf86`, `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md`, is its roster
record and names none of them.

### Why order 34

The comparison can only be made once unit 70 has recorded its reading at order 33. Step 34 is the
first step after that. `TOOL-dTotalRecall-87` shares the step and reads nothing this unit writes.

### Inventory

Minted: nothing in code, and no deviation record.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's ledger lines)

### Alternatives rejected

- **Re-run unit 70's whole table.** Rev-4 reads its rows by a blob probe, and the batch re-reads them (ids 2 and 25).
- **Single-quote the strings on the command line.** That breaks again on the first string holding a
  `'`. A literal in a quoted heredoc holds both.
- **Pass the revisions through the environment**, as rev-2 did. An unset variable leaves an empty revision, which
  `git show` answers from the index.
- **Repair unit 59's code where the amendment was absent.** It was present, and unit 59's AC2 decides the code. S3 runs
  it rather than guessing a repair.

## 5. Production-readiness checklist

- security — no surface: reads of history.
- perf / scale — five counts, each one `git rev-parse` and one `git show`.
- error / empty / loading states — a revision that names no commit, an empty one and a bare `^` among them, raises at the
  resolve, and an unreadable path raises at the read. Each is a red, never a 0.
- observability — the ledger names all five counts with their shas, and unit 70's recorded ones.
- risks — unit 70's ledger names its counts in prose. S4 reads them by eye and quotes them.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the probe of §4 runs at this pass's base, it prints the seven lines §4 pins, and §4's `git log` command
  prints `63f283ddd` first for unit 46 and `47afc8937` first for unit 59, each abbreviated.
  Red when: a line reads otherwise, a revision read fails, an `unrefused` line prints, or a pass is another commit.
  figure: the values are PINNED in §4, measured 2026-11-24; the pass's own lines are DERIVED by it.
- **AC2** — When `grep -lE 'pass\(59\)|47afc8937'` runs from `memory/builds/dTotalRecall/build/` over
  `*-build-TOOL-dTotalRecall-59-deviation-*.md` at the tip, it prints nothing, as at HEAD, and the same grep for
  `TOOL-dTotalRecall-59` prints the roster record's name. `git grep -n "absorbs" -- legacy_ledger.py` run from
  `tools/lib/` and `git grep -n "absorbs" -- tools/govkit/registry.toml` run from the root each print nothing, as at HEAD.
  Red when: a record of unit 59 asserts a departure S1 refutes, or the field survives.
- **AC3** — When `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-74" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC1 line names `s1-59` and `s1-46` with their shas beside the counts unit 70 recorded for
  the same strings.
  Red when: the line names only this unit's counts, so a false certification by unit 70 is
  invisible.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's probe and its liveness reads.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 67 to 70, id 11
  (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-83, TOOL-dTotalRecall-84, TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.
- rev-3 · 2026-11-24 · title §1 S1 to S4 §3 §4 §5 AC1 to AC3 §10 · re-grounded at HEAD `db95ebf86` per
  `2026-11-24-prompt-TOOL-dTotalRecall-74-reground-brief`, over unit 70 rev-4, whose own probe is a quoted heredoc: the
  pass commits of units 46 and 59 are read and named, each revision a literal resolved before it is read; the
  string reads 1 at `pass(59)^`, so S3's record is not owed and its write is cut; AC2 runs both greps of unit 59's AC2;
  §5's claim that `git show` refuses an empty revision is false and gone; the inline spans take two backticks.

## 10. Reuse audit

The seam, re-read at `db95ebf86`, is unit 67's joined-text probe with each string moved from a shell argument into a
literal in a quoted heredoc, the form unit 70 rev-4 §4's blob probe takes. The resolve before the read is
`TOOL-dTotalRecall-81` §4's rule, `rev-parse --verify` ahead of the blob. No deviation record is written.
`python tools/codebase-map/reuse_lookup.py "count a phrase holding backticks in a spec file without shell quoting"`
ranked name-stem neighbours only (`compare_counts`, `parse_spec_h1`, `read_spec_revisions`; run 2026-11-24), none of
which counts a phrase in a spec body. The recall query below found the audit's own items and the probes of units 71, 72,
76 and 94. No existing seam fits beyond them. The marker reader `tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder
walks of the two censuses are no seam here: this unit reads no marker and no registry.

Recall terms used: `python tools/memory-recall/query.py "how does a probe pass a string holding backticks to python without the shell running it" --terms "probe backtick double-quote command-substitution argv joined-text count spec amendment liveness stdin heredoc"`
