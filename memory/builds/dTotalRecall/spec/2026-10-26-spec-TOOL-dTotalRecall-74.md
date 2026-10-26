# TOOL-dTotalRecall-74 — unit 70's backticked strings are re-read at step 34 by a probe no shell quotes, and the departure unit 70's S3 owed for unit 59 is written

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 34 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |
| [2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
confirmed finding **id 11 at HIGH**, its item **H3**, alone in that item.

`TOOL-dTotalRecall-70` (order 33) defines "the probe" as unit 67 §4's joined-text count, whose
template passes each string in shell double quotes. Unit 70's §4 table wants 1 for its string
over unit 59's spec at `pass(59)^`, ``` `absorbs` is absent ```. Double-quoted, bash runs
`absorbs` as a command and the probe counts ` is absent`, which prints 2 over spec 59 where the real
count is 0. The row is green before unit 62's amendment exists. Unit 70's AC1 then certifies that unit 59
built from unit 62's amended text when it did not, and the deviation record unit 70's S3 owes is
never written. Its PINNED reading of ``Minted: `SUFFIX_RE` `` over unit 46's spec has the same
hazard.

This unit re-reads those two strings at the tip by a probe whose strings never pass through the
shell, proves the probe reads a 0 and a 1, and writes the deviation record of unit 59 that unit 70's
S3 owed where the amendment was absent. It repairs `TOOL-dTotalRecall-70`, at step 34, one above
that unit's order.

## 2. Scope (IN)

- **S1** — The re-read. The probe of §4 counts ``` `absorbs` is absent ``` over unit 59's spec at
  `pass(59)^`, and ``Minted: `SUFFIX_RE` `` over unit 46's spec at `pass(46)^`. Observed by AC1.
- **S2** — The liveness. The same run counts ``` `absorbs` is absent ``` over unit 59's spec at
  `653bed738`, which must print 0, and over unit 62's spec at `653bed738`, which must print 1. It
  counts ``Minted: `SUFFIX_RE` `` over unit 46's spec at `653bed738`, which must print 1. Observed
  by AC1.
- **S3** — The departure. Where S1's first count is 0, unit 59 built from text without unit 62's
  amendment. This pass writes the deviation record of `TOOL-dTotalRecall-59` that unit 70's S3 owed,
  its approver `author-recorded`, naming `pass(59)`, the missing string and unit 62's §4. It then
  runs the criterion that amendment carried, unit 59's AC2, at the tip. Observed by AC2.
- **S4** — The record. This unit's ledger names both S1 counts beside the counts unit 70's AC1 and
  AC8 lines recorded for them. A count unit 70 recorded at 1 or more where S1 reads 0 is named as a
  false certification, on the deviation record of S3 where there is one. Observed by AC3.

## 3. Non-goals (OUT)

- Unit 70's other rows. None holds a backtick or a `$`, so the double-quoted form reads them as
  written. The bridge from `git show` to the probe that every row needs (ids 2 and 25) is the batch
  `TOOL-dTotalRecall-76`'s.
- Editing unit 70's spec, frozen once its unit builds at order 33.
- Unit 46's body, which unit 70's S16 and S17 judge by the code. ``Minted: `SUFFIX_RE` `` is a
  PINNED text reading, and S1 only corrects the record of it.
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
in it. Each revision is read by `git show` inside Python with `check=True`, so a failed read raises
and is a red, never a 0. Text is joined on whitespace, as unit 67 §4 joins it.

```bash
# run from memory/builds/dTotalRecall/spec/ ; P59 and P46 are pass(59)^ and pass(46)^
P59=<pass(59)^> P46=<pass(46)^> python - <<'PROBE'
import os, re, subprocess
ABS = '`absorbs` is absent'
MINT = 'Minted: `SUFFIX_RE`'
def count(rev, n, s):
    raw = subprocess.run(['git', 'show', rev + ':./2026-10-26-spec-TOOL-dTotalRecall-%s.md' % n],
                         capture_output=True, check=True).stdout.decode('utf-8')
    return re.sub(r'\s+', ' ', raw).count(s)
for label, rev, n, s in (('s1-59', os.environ['P59'], '59', ABS), ('s1-46', os.environ['P46'], '46', MINT),
                         ('live-59', '653bed738', '59', ABS), ('live-62', '653bed738', '62', ABS),
                         ('live-46', '653bed738', '46', MINT)):
    print(label, count(rev, n, s))
PROBE
```

"pass(N)" is the first line of
`git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-N$' 462d20f3..HEAD`, as unit 70 §2
defines it.

PINNED, measured 2026-10-26 with this probe's `count` form: ``` `absorbs` is absent ``` prints 0
over spec 59 and 1 over spec 62 at `653bed738`, and ``Minted: `SUFFIX_RE` `` prints 1 over spec 46
there. The double-quoted form printed 2 over spec 59, with `absorbs: command not found` on stderr,
as the report's re-run shows.

### The deviation record

It follows the build's existing records, for example
`memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`:
`**Serves:** deviation TOOL-dTotalRecall-59`, `Hand-off: spec-to-code` (a value of `HANDS` in
`tools/memory-tree/deviation_join.py:148`), `Cause: design defect`, and the approver line naming the
chain's `author-recorded` value (`PLAY-dClosedLoop-4`). Its Evidence names `pass(59)`, the string,
unit 62's §4 "The amendments to unit 59", unit 70's AC1 line and this unit's `s1-59` count.

### Why order 34

The strings can only be re-read once unit 70 has recorded its reading at order 33. Step 34 is the
first step after that. The batch `TOOL-dTotalRecall-76` lands at 35, above every unit.

### Inventory

Minted: nothing in code; at most one deviation record of `TOOL-dTotalRecall-59`.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's ledger line, and the deviation record where S1
  reads 0)

### Alternatives rejected

- **Re-run unit 70's whole table.** Its other rows hold no backtick, and the batch re-runs them with
  the `git show` bridge they lack (ids 2 and 25).
- **Single-quote the strings on the command line.** That breaks again on the first string holding a
  `'`. A literal in a quoted heredoc holds both.
- **Repair unit 59's code where the amendment was absent.** Unit 59's AC2 decides that. It reads
  the factory and `kit.toml` for `absorbs`, and S3 runs it rather than guessing a repair.

## 5. Production-readiness checklist

- security — no surface: reads of history and one record.
- perf / scale — five counts, each one `git show`.
- error / empty / loading states — a revision `git show` cannot read raises, a red, never a 0. A
  missing pass commit leaves `P59` or `P46` empty, which `git show` refuses.
- observability — the ledger names all five counts and unit 70's recorded ones.
- risks — unit 70's ledger names its counts in prose. S4 reads them by eye and quotes them.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the probe of §4 runs at this pass's base, it prints `live-59 0`, `live-62 1` and
  `live-46 1`, and an `s1-59` and an `s1-46` line.
  Red when: a liveness line reads otherwise, or a revision read fails.
  figure: the liveness values are PINNED in §4, measured 2026-10-26; the `s1-` counts are DERIVED by
  the probe at the pass.
- **AC2** — When `s1-59` prints 0,
  `git grep -l "deviation TOOL-dTotalRecall-59" -- memory/builds/dTotalRecall/build` prints a record
  naming `pass(59)` and ``` `absorbs` is absent ```, and `git grep -n "absorbs" -- legacy_ledger.py`
  run from `tools/lib/` at the tip prints nothing.
  Red when: unit 59 built from unamended text and no deviation record names it, or the field
  survives.
- **AC3** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-74" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC1 line names `s1-59` and `s1-46` beside the counts unit 70 recorded for
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

## 10. Reuse audit

The seam is unit 67's joined-text probe, with each string moved from a shell argument into a literal
in a quoted heredoc, and the revision read is the `subprocess.run(['git', 'show', ...], check=True)`
form unit 70 §4's body compare uses. The deviation record is the build's existing shape.
`python tools/codebase-map/reuse_lookup.py "count a phrase holding backticks in a spec file without shell quoting"`
ranked name-stem neighbours only (`counts`, `read_spec_revisions`, `parse_spec_h1`), none of which
counts a phrase in a spec body. The recall query below found the audit's own items and unit 67's
probe. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a probe pass a string holding backticks to python without the shell running it" --terms "probe backtick double-quote command-substitution argv joined-text count spec amendment liveness stdin heredoc"`
