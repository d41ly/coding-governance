# TOOL-dScopedBuild-42 — the exit arm's rerun witness counts the staged ask rows, so a duplicated row turns it red

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 19 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-43 |
| [2026-11-01-prompt-TOOL-dScopedBuild-42-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-42-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 and 41
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-40-spec-audit-round1.md`)
confirmed finding **id 14 at HIGH**, report item **H1**, which no other id shares. `TOOL-dScopedBuild-41`
S1 has unit 39 AC17's arm read the staged set by `git diff --cached --name-only`, and its AC2 says a
rerun at the same tip leaves that output unchanged. `write_ask_rows` stages the backlog on the first
run (`tools/unattended/unattended.sh:9994`), so the name list already holds `BACKLOG.md` and cannot
change on a rerun. A writer with no reuse step appends a second row under a fresh id
(`derive_ask_seq`, `:9780`), and the witness stays green. So unit 39 AC17's "a rerun at the same tip
stages none" and unit 27 AC3's "files one per run" red can no longer fail.

This unit keeps the name list for the path half and adds a count of the staged ask rows, joined one
to one to the findings. It repairs `TOOL-dScopedBuild-41` and builds one step after it (order 19).

## 2. Scope (IN)

- **S1** — The witness. In each of unit 39 S22's two trees, after the first run and again after the
  rerun at the same tip, the arm reads the staged content of the fixture build's `BACKLOG.md` by
  `git diff --cached -U0 -- <bl>`. It counts the added lines that open an ask row, matched by
  `^+- [A-Z][A-Z]*-tFix-[0-9][0-9]* · filed `. SEV and KEEP rows open `- SEV ·` and `- KEEP ·`
  (`unattended.sh:10067-10072`), so the pattern counts ask rows alone. Observed by AC1 and AC2.
- **S2** — The join. The count after the first run equals the number of `ask ·` lines that run
  printed, which is at least 1. The ask ids in the added rows are distinct, and each finding's key,
  as unit 35 S32 states it, appears in exactly one added row. The count and the id set after the rerun
  equal those after the first run. This supersedes unit 41 AC2's "a rerun at the same tip leaves that
  output unchanged" and unit 41 S1's name-list read as the rerun's witness. Unit 41 AC2's "every path
  is a `BACKLOG.md`" half stands. Observed by AC2.
- **S3** — The build. This unit's pass extends the driver-suite arm unit 39 builds for its AC17 with
  S1 and S2. It adds no filer and no fixture. Observed by AC2.

## 3. Non-goals (OUT)

- Changing `write_gate_asks` or its reuse key. Unit 14 S6 and unit 35 S32 own them; this unit only
  makes their absence visible.
- The report's left-shift entry. The class is already recorded at
  `memory/gotchas/append-without-an-idempotence-key.md`, and no clause of this build names a new one.
- Rewording units 27, 39 and 41. Each clause is superseded by name.

### Edges

- **consumes-from** `TOOL-dScopedBuild-41` — S1's cached-diff read and AC2's rerun half, which S1 and S2 supersede with a count of the staged ask rows (id 14)
- **consumes-from** `TOOL-dScopedBuild-39` — S22's two trees and AC17's driver-suite arm, which S3 extends with the count (id 14)
- **consumes-from** `TOOL-dScopedBuild-35` — S32's stable key, by which `write_gate_asks` reuses an OPEN ask, which S2's join names and whose absence stages the red (id 14)

## 4. Design

### Evidence

- `unattended.sh:9994`: `write_ask_rows` writes the rows and then runs `GIT add -- "$bl"`.
- `unattended.sh:10030-10042`: in the one built filer, the reuse loop reads back each existing ask
  for the same subject before a new id is minted. `:10058-10059` mint the id fresh through
  `derive_ask_seq`. Unit 14 S6 gives `write_gate_asks` the same reuse.
- `unattended.sh:10061-10072`: the ask row opens `- $id · filed $today ·`, the SEV row `- SEV ·` and
  the KEEP row `- KEEP ·`.
- A probe on this node on 2026-11-01 staged one ask row in a scratch tree, then a second row for
  the same finding under a fresh id. The name list printed `BACKLOG.md` both times. The added-row
  count printed 1, then 2. PINNED on 2026-11-01.

### The witness

```
run 1 over tree T   -> n = count of "ask ·" lines printed, n >= 1
added = git diff --cached -U0 -- <bl> | grep '^+- [A-Z][A-Z]*-tFix-[0-9][0-9]* · filed '
  count(added) == n ; ids(added) distinct ; each finding key in exactly one row     (S2)
run 2 over tree T   -> count and id set unchanged                                  (S2)
git diff --cached --name-only -> every path ends BACKLOG.md                        (unit 41 AC2)
```

### Inventory

Minted: nothing. The arm is unit 39's, extended in place. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 19, one step after unit 41 (order 18). Units 27, 35 and 39 build earlier, so the arm,
its trees and the reuse key exist. `TOOL-dScopedBuild-43` at order 20 also writes
`tools/unattended/unattended.test.sh`, so BUILD-METHOD M6 sequences the two.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: unit 39 AC17's arm gains the count and the join

### Alternatives rejected

- **Compare the backlog's bytes before and after the rerun.** It catches a duplicate but not a first
  run that files two rows for one finding, and it names no key.
- **Count every added row.** Each ask files three rows, so the count is three per finding and a
  SEV row written alone would pass as a third of an ask.

## 5. Production-readiness checklist

- security — N/A — a suite arm's read; no write path changes.
- perf / scale — two `git diff` reads per tree.
- error / empty / loading states — a run that prints no `ask ·` line fails S2's at-least-1 clause, so
  an empty population is never read as a pass.
- observability — the arm names the tree, the expected count and the ids it read.
- risks — the count depends on the ask row's opening; S1 cites the line that writes it.
- testing — AC1 by probe, AC2 in the driver suite at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a scratch git tree with a tracked `BACKLOG.md` has one ask row appended and staged,
  `git diff --cached -U0 -- BACKLOG.md | grep -c '^+- [A-Z][A-Z]*-tFix-[0-9][0-9]* · filed '` prints
  1. When a second row for the same finding is appended under a fresh id and staged, it prints 2,
  while `git diff --cached --name-only` prints `BACKLOG.md` both times. A SEV and a KEEP row appended
  with them change neither count.
  Red when: the count reads the name list, or counts a SEV or KEEP row.
  fixture: a scratch tree under the run's short temp root, made by `git init`.
- **AC2** — When the driver suite's unit 39 AC17 arm runs the sliced `check_build_exit` twice over
  each of its two trees under `warn-and-ask`, the count of added ask rows in `git diff --cached -U0`
  equals the run's `ask ·` line count after the first run and again after the rerun, the ids are
  distinct, and each finding's key sits in exactly one row.
  Red when: `write_gate_asks` runs with its reuse of an OPEN ask cut out, so the rerun appends a second row
  per finding while the name list stays the same.
  permission: observed at the close, after units 35 and 39 are built.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC2 · unit 39 AC17's trees read by the count of staged ask rows after each run, staged by cutting the reuse of an OPEN ask out of `write_gate_asks` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 41's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 40 and 41, id 14
  (HIGH, item H1).

## 10. Reuse audit

The seam is unit 39 AC17's driver-suite arm, over unit 39 S22's two `build_fixture` trees, extended
in place, and the ask row's own opening as `write_inherited_asks` writes it
(`tools/unattended/unattended.sh:10061`). `python tools/codebase-map/reuse_lookup.py "count the ask
rows a rerun stages so a duplicate row turns the check red"` ranked `rows`, `row`, `check`, `counts`
and `extract_row`. None counts staged ask rows, so no existing seam fits beyond the arm named.

Recall terms used: `python tools/memory-recall/query.py "how does an idempotence criterion over an append-only backlog writer read its rows" --terms "append-only idempotence key rerun ask row staged BACKLOG.md write_gate_asks reuse duplicate cached diff"`
