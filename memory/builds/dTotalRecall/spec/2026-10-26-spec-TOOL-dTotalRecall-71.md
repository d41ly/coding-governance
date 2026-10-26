# TOOL-dTotalRecall-71 — unit 57's edge to unit 56 is certified at step 21 by a probe proven live on a copy without it, and unit 67's false reading is recorded

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 21 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |
| [2026-10-26-build-TOOL-dTotalRecall-71-round6-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-71-round6-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-71-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-71-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-71-round6-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-71-round6-fix-brief.md) | research | — |
| [2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-74 TOOL-dTotalRecall-76 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
confirmed finding **id 23 at BLOCKER**, its item **B1**. Item **H2** (id 10,
`TOOL-dTotalRecall-72`) is the same defect at its own grade.

`TOOL-dTotalRecall-67` (order 20) composes its probe as `<spec> "<string>"`. The edge string
``**consumes-from** `TOOL-dTotalRecall-56` `` holds backticks, so bash substitutes the command
`TOOL-dTotalRecall-56` and the probe counts `**consumes-from** `, which matches all four of spec
57's other consumes-from edges. AC1's edge row is therefore green whether or not the edge exists.
The check certifies what it does not check, and unit 57 can build without the sequencing edge to
unit 56 that unit 67 exists to guarantee.

This unit makes the check unit 67's AC1 meant for that row. At step 21, after
`TOOL-dTotalRecall-72` has read and written the edge, it counts the edge over unit 57's spec by a
probe whose string never passes through the shell. The same run counts it over a scratch copy with
the edge removed and over a scratch file holding only the edge, so the probe is seen to read both a
0 and a 1. It records what unit 67's AC1 line certified for that row beside what the row really
read at unit 67's tip, and a false certification becomes a recorded departure of unit 67. It
repairs `TOOL-dTotalRecall-67`, at step 21, one above that unit's order.

## 2. Scope (IN)

- **S1** — The certification. At this pass's base, the probe of §4 counts the edge string over unit
  57's spec. Observed by AC1.
- **S2** — The liveness. The same probe counts it over two scratch files under the run's scratch
  directory: unit 57's spec with every line holding the edge string deleted, and a file holding only
  §4's edge line from that spec. A probe that cannot read both a 0 and a 1 certifies nothing.
  Observed by AC1.
- **S3** — The record of unit 67's reading. The probe counts the edge string over unit 57's spec at
  unit 67's pass commit. This unit's ledger line names that count beside the count unit 67's AC1
  line recorded for the edge row. Where unit 67 recorded at least 1 and the probe reads 0, this pass
  writes a deviation record of `TOOL-dTotalRecall-67`, its approver `author-recorded`, naming the
  row, both counts and `TOOL-dTotalRecall-72` as the pass that wrote the edge. Observed by AC2.
- **S4** — The order. This pass precedes unit 57's pass. Observed by AC3.

## 3. Non-goals (OUT)

- Writing the edge or its mirror: `TOOL-dTotalRecall-72` does that at this step, before this pass.
- Editing unit 67's spec, frozen once its unit builds at order 20.
- Unit 67's other five strings and three §9 forms. None holds a backtick or a `$`, so the
  double-quoted form reads them as written.
- The bug-class entry or spec lint the report suggests as the left-shift gate: the close's
  left-shift step (BUILD-METHOD M8).
- Any code. This unit reads spec text and writes a ledger line and at most one deviation record.

### Edges

- **consumes-from** `TOOL-dTotalRecall-67` — its pass at step 20 and its AC1 ledger line, whose edge-row count this unit sets beside the probe's
- **consumes-from** `TOOL-dTotalRecall-72` — unit 57's spec as that pass leaves it; without it this check reads the gap unit 67 left and reds
- **hands-off** `TOOL-dTotalRecall-81` — its pass, its `pass67` count and its AC3 recipe, whose resolution of unit 67's pass that unit sets beside the driver's pass rule (the round-1 audit of units 71 to 76, id 37)
- **hands-off** `TOOL-dTotalRecall-82` — its `pass67` line and its S3 decision, which that unit re-makes at unit 67's verified pass commit (the round-1 audit of units 71 to 76, id 10)
- **hands-off** `TOOL-dTotalRecall-88` — its liveness lines, its S3 and AC2 answer and its AC3 ancestry, which that batch re-reads (the round-1 audit of units 71 to 76, ids 2, 19, 41)

## 4. Design

### The probe

The string is a Python literal inside a heredoc whose delimiter is quoted, so bash expands nothing
in it. A revision is read by `git show` inside Python with `check=True`, so a failed read raises and
is a red, never a 0. Text is joined on whitespace before counting, as in unit 67 §4.

```bash
# run from memory/builds/dTotalRecall/spec/ ; SCRATCH is the run's scratch directory, spelled absolute
SCRATCH=<the run's scratch directory> PASS67=<unit 67's pass commit> python - <<'PROBE'
import os, re, subprocess
EDGE = '**consumes-from** `TOOL-dTotalRecall-56`'
SPEC = '2026-10-26-spec-TOOL-dTotalRecall-57.md'
def text(raw): return re.sub(r'\s+', ' ', raw)
tip = open(SPEC, encoding='utf-8').read()
without = ''.join(l for l in tip.splitlines(True) if EDGE not in l)
only = ''.join(l for l in tip.splitlines(True) if EDGE in l)
for name, body in (('without-edge.md', without), ('edge-only.md', only)):
    open(os.path.join(os.environ['SCRATCH'], name), 'w', encoding='utf-8').write(body)
at67 = subprocess.run(['git', 'show', os.environ['PASS67'] + ':./' + SPEC], capture_output=True, check=True).stdout.decode('utf-8')
for label, body in (('tip', tip), ('without', open(os.path.join(os.environ['SCRATCH'], 'without-edge.md'), encoding='utf-8').read()),
                    ('only', open(os.path.join(os.environ['SCRATCH'], 'edge-only.md'), encoding='utf-8').read()), ('pass67', at67)):
    print(label, text(body).count(EDGE))
PROBE
```

It prints `tip 1`, `without 0` and `only 1` on a correct step 21. The `pass67` line is S3's count.
Environment variables carry the two paths into Python, so neither is a quoted shell string either.

PINNED, measured 2026-10-26 at `addc4073e` with the same `text(...)` form: the edge string prints 0
over spec 57, over spec 61 and over spec 57 at `653bed738`. Unit 67 §4's double-quoted form printed
4 over spec 57 there, with `TOOL-dTotalRecall-56: command not found` on stderr, and the
single-quoted form printed 0.

### The deviation record

It follows the build's existing records, for example
`memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`:
`**Serves:** deviation TOOL-dTotalRecall-67`, `Hand-off: spec-to-code` (a value of `HANDS` in
`tools/memory-tree/deviation_join.py:148`), `Cause: design defect`, and the approver line naming the
chain's `author-recorded` value (`PLAY-dClosedLoop-4`). Its Evidence names the review record's item
B1, unit 67's AC1 ledger line and this unit's `pass67` count.

### Why order 21

Unit 57 builds at order 30, and the certification must stand before it. It can only be made after
unit 67's pass at order 20 and `TOOL-dTotalRecall-72`'s write. Both repair units take step 21, one
above unit 67. The §3 edge to unit 72 runs that pass first under BUILD-METHOD M6, as unit 68's edge
to unit 66 orders step 32.

### Inventory

Minted: nothing in code; at most one deviation record of `TOOL-dTotalRecall-67`; two scratch files
outside the repository.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance-ledger line, and the deviation record
  where S3 finds a false certification)

### Alternatives rejected

- **Trust unit 72's own AC1.** It reads the same probe at the same step and proves no 0. A check that
  has never been seen to read a 0 is the defect this item names.
- **A liveness copy with the edge string blanked to spaces.** Joined text would still differ only in
  that token, which proves the same thing at more cost than deleting the line.
- **Re-run unit 67's AC1 whole.** Its other rows hold no backtick, and re-running them adds counts
  that cannot differ.

## 5. Production-readiness checklist

- security — no surface. The scratch files sit in the run's scratch directory, outside the
  repository.
- perf / scale — four counts and one `git show`.
- error / empty / loading states — a revision `git show` cannot read raises, a red. An `only` file
  with no line is `only 0`, a red, since then the tip carries no edge.
- observability — the ledger line names all four counts and unit 67's recorded count.
- risks — unit 67's ledger line names the edge row's count in prose. The record reads it by eye and
  quotes it.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the probe of §4 runs at this pass's base, it prints `tip 1`, `without 0` and
  `only 1`.
  Red when: unit 57's spec carries no edge to unit 56, or the probe cannot read a 0 where the edge is
  removed.
  figure: the counts are DERIVED by the probe at the pass; the base values it replaces are PINNED in
  §4, measured 2026-10-26.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-71" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names the probe's `pass67` count and unit 67's recorded count.
  Where those differ, `git grep -l "deviation TOOL-dTotalRecall-67" -- memory/builds/dTotalRecall/build`
  prints a record whose Evidence names both.
  Red when: unit 67 certified the edge present at its tip, the probe read 0 there, and no deviation
  record names it.
- **AC3** — When unit 57's pass commit is reached,
  `git merge-base --is-ancestor <this unit's pass commit> <unit 57's pass commit>` exits 0, the pass
  commit of a unit being `git log --reverse --format=%H --grep='^Pass: <unit id>$' 462d20f3..HEAD`'s
  first line.
  Red when: unit 57 builds before this certification.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's probe and its two liveness copies, and the edge it
certifies is graded by hygiene check 12's mirror rule.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 67 to 70, id 23
  (BLOCKER, item B1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-81, TOOL-dTotalRecall-82, TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is unit 67's own probe, the joined-text count of its §4, with the string moved from a shell
argument into a literal in a quoted heredoc. The revision read is the
`subprocess.run(['git', 'show', ...], check=True)` form unit 70 §4's body compare already uses, and
the deviation record is the build's existing shape. `python tools/codebase-map/reuse_lookup.py "count a phrase holding backticks in a spec file without shell quoting"`
ranked name-stem neighbours only (`counts`, `read_spec_revisions`, `parse_spec_h1`), and none counts
a phrase in a spec body. The recall query below found the audit's own items and unit 67's probe,
and `TOOL-aLexedStripper-1` §4, which records that a shell backtick opens command substitution. No
existing seam fits beyond unit 67's probe.

Recall terms used: `python tools/memory-recall/query.py "how does a probe pass a string holding backticks to python without the shell running it" --terms "probe backtick double-quote command-substitution argv joined-text count spec amendment liveness stdin heredoc"`
