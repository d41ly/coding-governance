# TOOL-dTotalRecall-91 — unit 69's AC1 is answered only from a read in which C5 ran, classified by the read's exit status and the checks that failed before it

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 37 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-91-deviation-911.md](../build/2026-10-26-build-TOOL-dTotalRecall-91-deviation-911.md) | deviation | — |
| [2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-90 TOOL-dTotalRecall-89 TOOL-dTotalRecall-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 77 to 88
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md`)
confirmed finding **id 23 at HIGH**, its item **H3**, alone in that item.

`TOOL-dTotalRecall-80` (order 36) answers unit 69's AC1 from its `p69` read by one key: whether the
read printed a `MANIFEST check 5 FAILED` line (spec 80 §2 S2 and §4 "The answer"). Nothing reads the
`p69 rc=` line `TOOL-dTotalRecall-77`'s `read_checker` prints. The checker reaches C5 only on some
paths. Its environment errors print `MANIFEST env ERROR` and `exit 2` before any check
(`skills/session-kickoff/manifest-check.sh:205`, `:207`, `:337`, `:345`). C5's `fail 5` (`:1473`)
runs only under `BLOCK_OK=1` (`:1359-1392`), which every `fail 2` of the block parse clears
(`:1351-1384`), and only under `SKIP_RANGE=0` (`:1461`), which every `fail 3` sets (`:1438-1450`), as
does a shallow clone missing the stamp's sha (`:1442`). A `p69` read on any of those paths prints no
check-5 line, and unit 80 answers "green, the re-stamp cleared C5" although C5 never ran.

This unit classifies each of unit 80's two recorded reads by its status line and the checks that
failed before C5, and answers unit 69's AC1 only from a read in which C5 ran. A read in which it did
not is "unresolved: C5 not evaluated", named in the ledger and never answered green. It repairs
`TOOL-dTotalRecall-80`, at order 37, one above that unit's 36.

## 2. Scope (IN)

- **S1** — The classifier. §4's `c5_of` reads a file of labelled read lines and one label, with the
  repository's shallow state, and prints `<label> C5 passed`, `<label> C5 failed` or
  `<label> C5 not-evaluated <why>`, by §4's table. Observed by AC1.
- **S2** — Its liveness. Over §4's fixture reads it prints the eight verdicts §4 pins, among them
  `not-evaluated` for an exit status of 2, for a check-2 line, for a check-3 line and for a shallow
  repository. Observed by AC1.
- **S3** — The answer. `c5_of` runs over the `p69` and `p69^` lines unit 80's acceptance ledger
  recorded, with `git rev-parse --is-shallow-repository` read at this pass's base. Unit 69's AC1 is
  green where `p69` reads `passed`, red where it reads `failed`, and "unresolved: C5 not evaluated"
  where it reads `not-evaluated`. The `p69^` verdict is stated beside it. Observed by AC2.
- **S4** — The records, once. Where unit 80's answer differs from S3's, a deviation record of
  `TOOL-dTotalRecall-80` names its answer, the classified read and item H3. Where S3 is unresolved, a
  deviation record of `TOOL-dTotalRecall-69` names AC1 as not observed at `pass(69)`, with the read's
  status and failure lines. Each is written only where `has_deviation` prints 0 for its unit and the
  token `audit-77 id 23`, by `TOOL-dTotalRecall-90` §4's recipe. Observed by AC3.

## 3. Non-goals (OUT)

- Running the checker again. The two reads are unit 80's, recorded by the main loop, and no role
  agent may run that leg (`.claude/roles.json`).
- Answering unit 69's AC1 at any commit but `pass(69)`. A read at another commit is not unit 69's
  pass, so an unresolved answer stays unresolved.
- Remedying a red at this build's tip: `TOOL-dTotalRecall-79` owns the tip's verdict.
- Editing unit 80's or unit 69's spec, each frozen once its unit builds.
- The checklist entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-80` — its `p69` and `p69^` reads and its answer to unit 69's AC1, which this unit classifies and answers again
- **consumes-from** `TOOL-dTotalRecall-77` — `read_checker`'s line format, the `<label> rc=<n>` line and the labelled failure lines `c5_of` parses
- **consumes-from** `TOOL-dTotalRecall-90` — `has_deviation` and its record recipe, through which S4's records are written once
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4's records are written through
- **consumes-from** `TOOL-dTotalRecall-93` — the re-keyed `has_deviation`, through which this unit's S4 guards and its AC3 counts are made in place of unit 90's (the round-1 audit of units 89 to 92, id 1)
- **hands-off** `TOOL-dTotalRecall-96` — its classifier, its answer to unit 69's AC1 and its records, which that unit corrects and answers again (the round-1 audit of units 89 to 92, id 12)
- **hands-off** `TOOL-dTotalRecall-100` — its record of unit 69 and its cites, which that batch withdraws where a parse failed and re-points (the round-1 audit of units 89 to 92, ids 6, 17)

## 4. Design

### The table

| Status line | Failure lines | Shallow | Verdict |
|---|---|---|---|
| none | any | any | `not-evaluated no-status-line` |
| `rc=1` | a check-5 line | any | `failed` |
| neither `rc=0` nor `rc=1` | any | any | `not-evaluated rc=<n>` |
| `rc=0` or `rc=1` | a check-2 line, no check-5 line | any | `not-evaluated check-2` |
| `rc=0` or `rc=1` | a check-3 line, no check-5 line | any | `not-evaluated check-3` |
| `rc=0` or `rc=1` | no check-2, check-3 or check-5 line | `true` | `not-evaluated shallow` |
| `rc=0` or `rc=1` | no check-2, check-3 or check-5 line | `false` | `passed` |

A shallow repository reads `not-evaluated` even where its stamp's sha is present and C5 ran. That
errs toward unresolved and never toward green, since `read_checker` drops the `WARN` line that would
tell the two apart.

### The classifier

```bash
# run from the repository root
c5_of() {  # file of labelled read lines · label · shallow (true|false) -> one verdict line
  python - "$@" <<'PROBE'
import re, sys
path, label, shallow = sys.argv[1], sys.argv[2], sys.argv[3]
rc, checks = None, set()
for raw in open(path, encoding='utf-8'):
    line = raw.rstrip('\n')
    if not line.startswith(label + ' '):
        continue
    rest = line[len(label) + 1:]
    m = re.fullmatch(r'rc=(\d+)', rest)
    if m:
        rc = int(m.group(1)); continue
    m = re.match(r'MANIFEST check (\d+) FAILED', rest)
    if m:
        checks.add(int(m.group(1)))
if rc is None:
    print(label, 'C5 not-evaluated no-status-line'); sys.exit(0)
if 5 in checks and rc == 1:
    print(label, 'C5 failed'); sys.exit(0)
why = ('rc=%d' % rc if rc not in (0, 1) else 'check-2' if 2 in checks else 'check-3' if 3 in checks
       else 'shallow' if shallow != 'false' else '')
print(label, 'C5', 'not-evaluated ' + why if why else 'passed')
PROBE
}
```

A label matches only with its following space, so `p69` never reads a `p69^` line.

### The fixture reads

```bash
cat > "$SCRATCH/c5in.txt" <<'READS'
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
READS
```

PINNED, measured 2026-10-26 with this classifier: over this file with shallow `false`, `p69`, `p69^`,
`q`, `r`, `s` and `t` printed `passed`, `failed`, `not-evaluated rc=2`, `not-evaluated check-2`,
`passed` and `not-evaluated check-3`; label `none` printed `not-evaluated no-status-line`; and `p69`
with shallow `true` printed `not-evaluated shallow`. `git rev-parse --is-shallow-repository` printed
`false` at `1e255b0c6`.

### Why order 37

Unit 80 records its two reads and its answer at order 36. The driver runs units sharing an order in
id order (`tools/workflows/unattended-build.js:76-80`), so this unit runs after unit 88 at 37, which
reads neither unit 80's answer nor this one.

### Inventory

Minted: the probe function `c5_of`, spec text only; at most one deviation record each of
`TOOL-dTotalRecall-80` and `TOOL-dTotalRecall-69`. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S4)

### Alternatives rejected

- **Green only where `rc=0`.** A `p69` read failing check 9 alone exits 1 with C5 run and passed;
  that reading would call a cleared C5 unresolved and hide the answer unit 69's AC1 asks for.
- **Read the checker's full output for its `WARN` line.** `read_checker` keeps only failure lines,
  and re-running the checker is the main loop's. The shallow probe answers the same question from the
  repository.
- **Re-read at the tip when `p69` is unresolved.** The tip is not unit 69's pass, so its verdict
  answers a different question.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one classifier run per read, one `git rev-parse`.
- error / empty / loading states — a read with no status line, a non-0-or-1 status, a check-2 or
  check-3 line and a shallow repository each read `not-evaluated`, never `passed`.
- observability — the ledger quotes both reads beside their verdicts.
- risks — the shallow row is conservative, as §4 states.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `c5_of` runs over §4's fixture reads with shallow `false`, labels `p69`, `p69^`,
  `q`, `r`, `s` and `t` print `passed`, `failed`, `not-evaluated rc=2`, `not-evaluated check-2`,
  `passed` and `not-evaluated check-3`, label `none` prints `not-evaluated no-status-line`, and `p69`
  with shallow `true` prints `not-evaluated shallow`.
  Red when: a read with a non-0-or-1 status, a check-2 or check-3 line, or no status reads `passed`.
  figure: the verdicts are PINNED in §4, measured 2026-10-26.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-91" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line quotes unit 80's `p69` and `p69^` reads, `c5_of`'s verdict on each,
  the `git rev-parse --is-shallow-repository` value, and unit 69's AC1 answered from `p69`'s verdict.
  Red when: unit 69's AC1 is answered green from a read whose verdict is not `passed`.
- **AC3** — When `has_deviation memory/builds/dTotalRecall/build 80 'audit-77 id 23'` runs after the
  pass, it prints 1 where unit 80's answer differs from AC2's, else 0, and the same for unit 69 prints
  1 where AC2's answer is unresolved, else 0.
  Red when: an owed record is absent, or a record is written twice.

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

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 77 to 88, id 23
  (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the consumes-from edge to TOOL-dTotalRecall-93, the mirror of TOOL-dTotalRecall-96, the mirror of TOOL-dTotalRecall-100, each the other end of an edge a unit the
  round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dTotalRecall-77`'s `read_checker` line format, whose labelled lines `c5_of`
parses as `TOOL-dTotalRecall-79`'s span script parses them, and `TOOL-dTotalRecall-90`'s
`has_deviation` with its record recipe. `python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`
ranked `add_scratch_worktree` among its SEAM candidates, the checkout unit 80 already used; nothing
in the tree classifies the checker's exit status. The recall query below found this audit's item H3,
`TOOL-dTotalRecall-77` and `TOOL-dTotalRecall-80`, and no reader of `manifest-check.sh` that keys a
verdict on its status. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how is a manifest-check verdict read so an exit 2 or a skipped check is never green" --terms "manifest-check exit status env ERROR BLOCK_OK SKIP_RANGE C5 check 5 FAILED read_checker p69 not evaluated"`
