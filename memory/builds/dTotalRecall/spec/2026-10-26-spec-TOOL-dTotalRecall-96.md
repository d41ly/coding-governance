# TOOL-dTotalRecall-96 — unit 69's AC1 is answered again by a C5 classifier whose exit status must agree with the read's failure lines, so a read in which the checker never ran is never passed

**Status:** CLOSED · rev-2 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 38 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-96-deviation-961.md](../build/2026-10-26-build-TOOL-dTotalRecall-96-deviation-961.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-96-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-96-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-96-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-96-1-builder-return.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-96-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-96-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-96-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-96-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-96-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-96-reground-spec-writer.md) | log | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 12 at HIGH**, its item **H3**, which it shares with id 30 (HIGH, taken by
`TOOL-dTotalRecall-97`).

`TOOL-dTotalRecall-91` rev-3 §4 "The classifier" prints `passed` for a read whose status is `rc=1`,
which carries no check-2, check-3 or check-5 line, in a repository that is not shallow, and its table's
last row says so. Its §3 leaves that row to this unit. On a default run of
`skills/session-kickoff/manifest-check.sh`, `fail()` is the only code that sets status 1
(`skills/session-kickoff/manifest-check.sh@f7011dd6f:2396`), it always prints `MANIFEST check <n> FAILED`,
and the script's last line exits with that status (`skills/session-kickoff/manifest-check.sh@f7011dd6f:2815`).
Every literal `exit 1` sits in a card function, and a card run ends before the checks
(`skills/session-kickoff/manifest-check.sh@f7011dd6f:2344`). The checker is one blob at `f7011dd6f`, at
`ff3c1b93a` and at `b59778f81` (DERIVED 2026-11-24, `git rev-parse <rev>:<path>`). So `rc=1` with no
failure line is a run that finished no check. Two paths give it. `TOOL-dTotalRecall-77` rev-4's
`read_checker` prints it for a missing or an empty worktree, which its AC1 pins as `absent rc=1` and
`empty rc=1`. The checker, which runs under `set -u`, also gives it when it dies before any failure.
The report ran unit 91's classifier verbatim: `x rc=1` alone printed `x C5 passed`, and `z rc=0` beside
`z MANIFEST check 5 FAILED` printed `z C5 passed` too. Unit 69's AC1 is then answered green from a read
in which C5 never ran or failed, the false green unit 91 exists to stop.

This unit corrects the classifier so a status must agree with the failure lines before any verdict:
`rc=1` with no failure line, `rc=0` with one, and two status lines under one label are each
not-evaluated. It answers unit 69's AC1 again from unit 80's reads, extracted by
`TOOL-dTotalRecall-97`, and writes each record that answer owes once. Unit 69 is CLOSED and its
pass(69) is `f7011dd6f`. The `p69` read is unit 76's sweep line for that commit, lifted by unit 80 rev-4.
That sweep has run and printed `rc=0` there with no failure line (DERIVED 2026-11-24, the sweep block of
`2026-11-24-prompt-TOOL-dTotalRecall-76-build-brief.md`). The `p69^` read is not made yet. This unit
repairs `TOOL-dTotalRecall-91`, at order 38, one above that unit's 37.

## 2. Scope (IN)

- **S1** — The classifier. §4's `c5_of` reads a file of labelled lines, a label and the repository's
  shallow state, and prints one verdict by §4's table, whose agreement rows come before any other: no
  status line, two status lines, a status other than 0 or 1, `rc=0` with a failure line, and `rc=1`
  with none each read `not-evaluated`. A `<label> unplaced <n>` line with `n` above 0, or any labelled
  line it cannot place, reads `not-evaluated unplaced <n>`. Observed by AC1.
- **S2** — The answer. For `p69` and `p69^`, `c5_of` runs over the output `TOOL-dTotalRecall-97`'s
  `c5_input` gives for unit 80's acceptance ledger, by §4 "The answer", with
  `git rev-parse --is-shallow-repository` read at this pass's base. Unit 69's AC1 is green where `p69`
  reads `passed`, red where it reads `failed`, and "unresolved: C5 not evaluated" where it reads
  `not-evaluated` for any reason but `unplaced` or `no-status-line`. Those two leave AC1 unanswered and
  are named as a parse failure of unit 80's ledger. An `extraction-failed` line is neither: the call
  read no whole ledger, and the pass mends the call before it answers. The `p69^` verdict is stated
  beside it, and the ledger sets the answer beside unit 91's. Observed by AC2.
- **S3** — The records, once. Where unit 91's answer differs from S2's, an unanswered AC1 included, a
  deviation record of `TOOL-dTotalRecall-91` names both answers and the classified read. Where S2 is
  "unresolved: C5 not evaluated" and `has_deviation` prints 0 for unit 69 and unit 91's token
  `audit-77 id 23 s4`, a record of `TOOL-dTotalRecall-69` names AC1 as not observed. Where S2 names a
  parse failure, a record of `TOOL-dTotalRecall-80` names its ledger's read lines as unplaceable, and no
  record of unit 69 is written. Each carries the token `audit-89 id 12 s3`, by `TOOL-dTotalRecall-90`
  §4's recipe with §4's values, and is written only where `TOOL-dTotalRecall-93`'s `has_deviation`
  prints 0 for its unit and that token. Observed by AC3.

## 3. Non-goals (OUT)

- The extraction of the reads from unit 80's ledger and the count of unplaced lines (item H3, id 30):
  `TOOL-dTotalRecall-97`.
- A manifest carrying no marker, on which the checker exits 0 before any check (item M4, id 7), and a
  record of unit 69 that unit 91 wrote from a parse failure (item M3, id 6): the batch
  `TOOL-dTotalRecall-100`.
- A checker that dies between another check's failure and C5: it exits 1 as a finished run does, and
  the recorded lines cannot tell them apart, the risk unit 91 rev-3 §5 states.
- Running the checker again. The reads are unit 80's, recorded by the main loop, and no role agent may
  run that leg (`.claude/roles.json`).
- Editing spec 91's, spec 80's or spec 69's text, each frozen once its unit builds. Unit 90's recipe is
  read as it stands: units 91 and 93, consumed below, consume it, so no edge of this unit's own orders it.
- The checklist entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-91` — its classifier, its answer to unit 69's AC1 and the records of units 80 and 69 it wrote, which this unit corrects and answers again
- **consumes-from** `TOOL-dTotalRecall-80` — its `p69` and `p69^` reads and its acceptance ledger, the reads this unit classifies
- **consumes-from** `TOOL-dTotalRecall-97` — `c5_input`, the extraction whose output is this classifier's only input
- **consumes-from** `TOOL-dTotalRecall-93` — the re-keyed `has_deviation`, through which S3's records are written once
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3's records are written through
- **hands-off** `TOOL-dTotalRecall-100` — `c5_of`, which that batch runs again for ids 6 and 7

## 4. Design

### The table

First matching row wins.

| Status lines | Failure lines | Other | Verdict |
|---|---|---|---|
| any | any | an `unplaced` count above 0, or a labelled line not placed | `not-evaluated unplaced <n>` |
| none | any | any | `not-evaluated no-status-line` |
| two or more | any | any | `not-evaluated contradictory` |
| `rc=<n>`, n not 0 or 1 | any | any | `not-evaluated rc=<n>` |
| `rc=0` | one or more | any | `not-evaluated contradictory` |
| `rc=1` | none | any | `not-evaluated rc1-no-failure-line` |
| `rc=1` | a check-5 line | any | `failed` |
| `rc=1` | a check-2 line, no check-5 line | any | `not-evaluated check-2` |
| `rc=1` | a check-3 line, no check-5 line | any | `not-evaluated check-3` |
| `rc=0` or `rc=1` | no check-2, check-3 or check-5 line | shallow `true` | `not-evaluated shallow` |
| `rc=0` or `rc=1` | no check-2, check-3 or check-5 line | shallow `false` | `passed` |

`rc=1` with only a check-9 line still reads `passed`: the checker ran C5, and C5 printed nothing.
Unit 91 §4 states why its check-2, check-3 and shallow rows read not-evaluated, and they stand. A read
of placed lines whose one status agrees with its failure lines answers as unit 91 answers it.

### The classifier

```bash
# run from the repository root; PY, where set, is the launcher tools/lib/resolve-python.sh resolves
c5_of() {  # file of labelled read lines · label · shallow (true|false) -> one verdict line
  "${PY:-python}" - "$@" <<'PROBE'
import re, sys
path, label, shallow = sys.argv[1], sys.argv[2], sys.argv[3]
rcs, checks, unplaced = [], set(), 0
for raw in open(path, encoding='utf-8', errors='replace'):
    line = raw.rstrip('\n')
    if not line.startswith(label + ' '):
        continue
    rest = line[len(label) + 1:]
    m = re.fullmatch(r'rc=(\d+)|MANIFEST check (\d+) FAILED.*|unplaced (\d+)', rest)
    if not m:
        unplaced += 1
    elif m.group(1):
        rcs.append(int(m.group(1)))
    elif m.group(2):
        checks.add(int(m.group(2)))
    else:
        unplaced += int(m.group(3))
rc = rcs[0] if len(rcs) == 1 else None
why = ('unplaced %d' % unplaced if unplaced else 'no-status-line' if not rcs
       else 'contradictory' if len(rcs) > 1 else 'rc=%d' % rc if rc not in (0, 1)
       else 'contradictory' if rc == 0 and checks else 'rc1-no-failure-line' if rc == 1 and not checks
       else 'failed' if 5 in checks else 'check-2' if 2 in checks else 'check-3' if 3 in checks
       else 'shallow' if shallow != 'false' else '')
print(label, 'C5', why if why == 'failed' else 'not-evaluated ' + why if why else 'passed')
PROBE
}
```

Only the ASCII head of a line is parsed, so a failure message in any encoding is read. A Python that
writes its output in the locale's code page gives the failure line's dash as a byte that is no UTF-8,
and rev-1's strict read then raised and printed no verdict (DERIVED 2026-11-24, `c5_input` under
`PYTHONUTF8=0` on node a).

### The fixture reads

```bash
cat > "$SCRATCH/c5in96.txt" <<'READS'
p69 rc=0
p69^ rc=1
p69^ MANIFEST check 5 FAILED — watched files changed since last-audit
q rc=2
r rc=1
r MANIFEST check 2 FAILED — manifest-audit block lacks a last-audit value
s rc=1
s MANIFEST check 9 FAILED — stall
t rc=1
t MANIFEST check 3 FAILED — last-audit sha is not an ancestor of HEAD
x rc=1
z rc=0
z MANIFEST check 5 FAILED — watched files changed since last-audit
w rc=1
w rc=0
v rc=0
v unplaced 1
READS
```

PINNED, measured 2026-10-26 at `32febccb6` and again 2026-11-24 at `b59778f81` with this classifier
over this file and shallow `false`: `p69`, `p69^`, `q`, `r`, `s` and `t` printed `passed`, `failed`,
`not-evaluated rc=2`, `not-evaluated check-2`, `passed` and `not-evaluated check-3`, as unit 91's pin;
`x` printed `not-evaluated rc1-no-failure-line`, `z` and `w` `not-evaluated contradictory`, `v`
`not-evaluated unplaced 1`, and the label `none` `not-evaluated no-status-line`. `p69` with shallow
`true` printed `not-evaluated shallow`. `git rev-parse --is-shallow-repository` printed `false` at
`b59778f81` on node a (DERIVED 2026-11-24, that command).

### The answer

```bash
# run from the repository root, with c5_of and TOOL-dTotalRecall-97 §4's c5_input sourced from a file
LEDGER80=$(git grep -l "Evidences:\*\* TOOL-dTotalRecall-80" -- memory/builds/dTotalRecall/build)
SH=$(git rev-parse --is-shallow-repository)
for L in p69 'p69^'; do
  c5_input "$LEDGER80" "$L" > "$SCRATCH/c5-$L.txt" || { echo "$L C5 red extraction-failed"; continue; }
  c5_of "$SCRATCH/c5-$L.txt" "$L" "$SH"
done
```

The extraction's status is read because a partial file can end before a check-5 line and read `passed`.
The grep lists one file for unit 69's ledger today (DERIVED 2026-11-24, the same command with that id).
DERIVED 2026-11-24, this loop over scratch ledgers on node a with unit 97 rev-2's `c5_input`: a ledger
of unit 80 rev-4's shape, its fence holding `p69 rc=1` with a check-9 line, a `parent` line and
`p69^ rc=1` with a check-5 line, printed `p69 C5 passed` and `p69^ C5 failed`. With the `p69` status
moved into a bullet's sentence it printed `p69 C5 not-evaluated unplaced 1`. With no ledger, two paths
or an empty path it printed the `extraction-failed` red for both labels.

### The records

`TOOL-dTotalRecall-90` §4 "The deviation record" gives each field. These are the values this unit sets:

| Field | Of `TOOL-dTotalRecall-91` | Of `TOOL-dTotalRecall-69` | Of `TOOL-dTotalRecall-80` |
|---|---|---|---|
| Departs from | `TOOL-dTotalRecall-91@rev-<N> [§6 AC2]` | `TOOL-dTotalRecall-69@rev-<N> [§6 AC1]` | `TOOL-dTotalRecall-80@rev-<N> [§6 AC2]` |
| Before | the answer its ledger states | AC1 as its ledger records it, from the copied pair | the read lines as its ledger holds them |
| After | S2's answer and the classified read | AC1 not observed at pass(69), the read's status and failure lines | the lines unplaceable, `c5_input`'s output |
| Risk | `loosening` where it answered green, else `editorial` | `loosening` | `editorial` |

With the token `audit-89 id 12 s3`, `has_deviation` printed 0 for each of the three units at `b59778f81`,
and with `spec changed at` it printed 1 for unit 70 (PINNED 2026-11-24, these calls), so the probe reads
both ways over the real folder.

### Why order 38

Unit 91 answers at order 37. This unit consumes `TOOL-dTotalRecall-97`, which shares order 38, and
`--dispatch` refuses a unit while a unit of its build it consumes from is neither CLOSED nor WONTDO,
units of one order included (`tools/unattended/unattended.sh#verb_dispatch`, reading
`tools/unattended/lib-unattended.sh#read_consumes_from`). No edge joins this unit to unit 89.

### Inventory

Minted: the corrected `c5_of`, spec text only; at most one deviation record each of
`TOOL-dTotalRecall-91`, `TOOL-dTotalRecall-69` and `TOOL-dTotalRecall-80`. Naming cell: none, no
product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S3)

### Alternatives rejected

- **Green only where `rc=0`.** Unit 91 §4 rejected it: a read failing check 9 alone exits 1 with C5 run
  and passed, and that reading hides the answer unit 69's AC1 asks for.
- **Re-run the checker where a read disagrees.** The reads are unit 80's and the checker is a leg no
  role agent runs, so a disagreeing read stays unresolved.
- **Treat a parse failure as "unresolved" and record unit 69.** The read may have been sound and only
  its recording unplaceable, so a record of unit 69 would state what nobody observed; the record names
  unit 80's ledger instead.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — two extractions and two classifier runs, one `git rev-parse`.
- error / empty / loading states — every disagreement between status and failure lines, a missing
  status and an unplaced line read `not-evaluated`, never `passed`. A failed extraction prints a red.
- observability — the ledger quotes the extracted reads beside their verdicts and unit 91's answer.
- risks — the shallow row stays conservative, as unit 91 §4 states. The reads are recorded text: a line
  mis-copied into unit 80's ledger is classified as copied.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `c5_of "$SCRATCH/c5in96.txt" <label> false` runs for each label of §4's fixture, it
  prints the verdicts §4 pins, among them `x C5 not-evaluated rc1-no-failure-line` and
  `z C5 not-evaluated contradictory`.
  Red when: a read with `rc=1` and no failure line, `rc=0` with a failure line, two status lines or an
  unplaced line reads `passed`.
  fixture: the file is made in the run's scratch by the pass; the tree holds none.
  figure: the verdicts are PINNED in §4, measured 2026-10-26 and 2026-11-24.
- **AC2** — When `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-96" -- memory/builds/dTotalRecall/build`
  runs after the pass, the ledger it names has an AC2 line quoting the path §4's `LEDGER80` held, the
  `c5_input` output for `p69` and `p69^`, `c5_of`'s verdict on each, the shallow value, unit 69's AC1
  answered from `p69`'s verdict, and unit 91's answer beside it.
  Red when: unit 69's AC1 is answered green from a verdict that is not `passed`, or answered at all
  from `unplaced`, `no-status-line` or an `extraction-failed` line.
- **AC3** — When `has_deviation memory/builds/dTotalRecall/build 91 'audit-89 id 12 s3'` runs after the
  pass, it prints 1 where unit 91's answer differs from AC2's, else 0; the same for unit 69 prints 1
  where AC2 is "unresolved: C5 not evaluated" and
  `has_deviation memory/builds/dTotalRecall/build 69 'audit-77 id 23 s4'` prints 0, else 0; and for
  unit 80 it prints 1 where AC2 names a parse failure, else 0. Run before any write, all three print 0.
  Red when: an owed record is absent, a record no answer owes is written, a record is written twice, or
  a parse failure writes a record of unit 69.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the classifier's liveness is its fixture, and the reads it classifies are unit 80's.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 12
  (HIGH, item H3, shared with id 30).
- rev-2 · 2026-11-24 · §1 · S2 · S3 · §3 · §4 · §5 · AC1 · AC2 · AC3 · §10 · re-grounded at `b59778f81` per
  `2026-11-24-prompt-TOOL-dTotalRecall-96-reground-brief`, over unit 91 rev-3, unit 80 rev-4, unit 97 rev-2 and unit 93
  rev-2: the checker's citations are pinned at pass(69); the classifier takes a default launcher and any
  encoding; the answer's commands read the extraction's status; the records' values and the guard over
  unit 91's record are spelled; the fixture is re-measured; the order rests on the dispatch edge check.
  No scope item or criterion is cut.

## 10. Reuse audit

The seams, re-read at `b59778f81`, are `TOOL-dTotalRecall-91` rev-3's classifier, corrected here row by
row; `TOOL-dTotalRecall-97` rev-2's `c5_input`, its only input; `TOOL-dTotalRecall-93` rev-2's
`has_deviation`; and `TOOL-dTotalRecall-90` rev-3's record recipe.
`python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`,
re-run 2026-11-24, ranks `add_scratch_worktree` among its SEAM candidates, the checkout unit 80's parent
read already uses; asked to classify a recorded exit status against its failure lines, it ranks name-stem
neighbours of `record` and `line` and nothing that reads a checker's status. The recall query below
found this audit's item H3, spec 91's table and spec 77's `read_checker`, and found them again on its
re-run of 2026-11-24. No existing seam fits beyond them. `tools/memory-tree/id_grammar.py#read_kept_reason`
and the build-folder walks of `tools/memory-tree/record_causes.py#check_cause_writers` and
`tools/memory-tree/record_kinds.py#check_alias_compares` are no seam here: this unit reads no marker and no
registry.

Recall terms used: `python tools/memory-recall/query.py "how is a manifest-check read classified so a status that disagrees with its failure lines is never green" --terms "manifest-check exit status fail rc=1 no failure line contradictory read_checker c5_of p69 not evaluated"`
