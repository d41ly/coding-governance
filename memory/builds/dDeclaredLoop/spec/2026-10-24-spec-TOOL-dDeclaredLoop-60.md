# TOOL-dDeclaredLoop-60 — the budget reader counts draws in every run record, rotated archives included, under `MEMORY_ROOT`

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 30 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-60-deviation-601.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-60-deviation-601.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 19 at HIGH**, its item **H3**, alone in that item. `TOOL-dDeclaredLoop-48` S3 and
S4 store a driver verb's draws in the run-state file and read them back only from the live record, a
literal `memory/builds/*/RUN.md`. `--preflight` rotates a finished record to an archive named by
`archive_name_of` (`tools/unattended/unattended.sh:4373`, the rename at :7676), and such archives are
tracked, `memory/builds/aBatchedArm/RUN.ABORTED.7742ee67.md` among nine. Once a build starts its next
run its prior draws, the `budget <origin>` rows included, leave `budget_state`'s population, so `spent`
falls and the route-back budget refills; and in a tree whose `MEMORY_ROOT` is not `memory` no patch
draw is ever counted. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-48`.

## 2. Scope (IN)

- **S1** — The run-state population `budget_state` reads is both globs the driver's own concurrency
  check reads, `<MEMORY_ROOT>/builds/*/RUN.md` and `<MEMORY_ROOT>/builds/*/RUN.*.md`
  (`tools/unattended/unattended.sh:3313`), listed through `git ls-files` so an untracked scratch copy is
  never counted. This supersedes the glob of `TOOL-dDeclaredLoop-48` S4. Observed by AC1, AC2.
- **S2** — `MEMORY_ROOT` is read once, from the tree root's `.memory-tree.conf` through the memory-tree
  kit's `parse_conf`, reached by `resolve_kit_dir("memory-tree", "tree_lib.py", here)`, the route
  `TOOL-dDeclaredLoop-41` S1 specifies; an absent conf or key reads `memory`, the driver's own default
  (`tools/unattended/unattended.sh:560`). Observed by AC2.
- **S3** — A row read from a build's own archive counts for that build, and a row carrying
  ` · budget <slug>` counts for the named build whichever record holds it; the slug is matched as a
  whole token, so `budget dX` never counts for `dXPatch`. Observed by AC1, AC3.
- **S4** — A draw row is counted once however many records hold it: the archive and the live record of
  one run never both carry a row, because rotation moves the file, and a row copied into a log record
  by `TOOL-dDeclaredLoop-30` S9 is read from the log record alone, its run-state twin skipped by its
  timestamp. Observed by AC1.

## 3. Non-goals (OUT)

- Draws of two concurrent patch runs that cannot see each other's records: the audit's id 63, batched
  into `TOOL-dDeclaredLoop-67`.
- Where a draw is written: `TOOL-dDeclaredLoop-48` S1 to S3, unchanged.
- A spec lint over literal `memory/builds/` paths, the finding's left-shift: the class is recorded at
  the close; AC2 is this reader's non-default-root fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-48` — `budget_state`'s run-state home and the ` · budget <slug>` row, whose population this unit widens to rotated archives under the resolved root
- **hands-off** `TOOL-dDeclaredLoop-67` — the resolved run-state population, which that unit's concurrent patch refusal and literal-root observation read (ids 8 and 63)

## 4. Design

### Evidence

- `check_single_live` globs `":(glob)$M/builds/*/RUN.md" ":(glob)$M/builds/*/RUN.*.md"` through
  `git ls-files` (`tools/unattended/unattended.sh:3313`), `M` being `MEMORY_ROOT` (:739).
- `git ls-files 'memory/builds/*/RUN.*.md'` lists nine archives at base `ed497191`: PINNED, read
  2026-10-24.
- `TOOL-dDeclaredLoop-30` S9 copies a pre-log draw into the first log record, which is why S4 names the
  twin.

### The read

```
root  = parse_conf(<tree>/.memory-tree.conf).get("MEMORY_ROOT") or "memory"
files = git ls-files ":(glob)<root>/builds/*/RUN.md" ":(glob)<root>/builds/*/RUN.*.md"
rows  = draw rows of <slug>'s own files  +  rows of any file whose " · budget <slug>" token matches
```

### Files touched (estimate)

- `tools/loop/budget.py`

### Alternatives rejected

- **Copying a run's draws into the next run's record at preflight.** It writes a second home for one row,
  and the driver's rotation would need to know the budget's grammar.
- **Reading the working tree with a filesystem glob.** An untracked scratch record would count; the
  driver reads tracked files for the same reason.

## 5. Production-readiness checklist

- security — no new surface; a read.
- perf / scale — one `git ls-files` and the archive files, tens per tree.
- error / empty / loading states — an archive that does not parse is named and skipped, never a silent
  zero; an empty population reads the base budget.
- observability — `budget_state --explain` prints each file it read rows from.
- risks — a hand-edited archive changes `spent`; archives are immutable by the driver's naming.
- testing — AC1 to AC3 as fixture plants; the arm under §7, observed at the close.
- migration — none: archives already on disk are read from this unit on.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant draws-survive-rotation` draws twice in a run, renames
  that run's record to `RUN.ABORTED.<hex>.md` as `--preflight` does, starts a new record and draws once
  more, `budget_state` answers `open 3/<total>`.
  Red when: the archive is outside the population and the answer reads `1/<total>`.
- **AC2** — When the same plant runs with `MEMORY_ROOT=records` in the fixture's `.memory-tree.conf`, the
  answer is the same.
  Red when: the reader globs a literal `memory/` and counts nothing.
- **AC3** — When `--plant patch-archived` archives a patch run whose rows carry ` · budget dX` and a
  second build `dXPatch` reads its own budget, `dX`'s `budget_state` counts the rows and `dXPatch`'s does
  not.
  Red when: the slug matches as a substring.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/budget.py · covers AC1 AC2 AC3 · the rotation, non-default-root and archived-patch plants, staged against the live-record glob `TOOL-dDeclaredLoop-48` S4 specified · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 19 (HIGH, item H3).

## 10. Reuse audit

The seams are the driver's own two-glob population (`tools/unattended/unattended.sh:3313`) and the
memory-tree kit's `parse_conf` reached by `resolve_kit_dir`, the root route `TOOL-dDeclaredLoop-41` S1
names. `python tools/codebase-map/reuse_lookup.py "read every run-state record including rotated
archives"` ranked generic `read`, `read_text`, `run`, `records` and `read_conf`; none lists run records
with their archives, so the population is spelled as the driver spells it, and `python
tools/codebase-map/reuse_lookup.py "resolve the memory root from the memory-tree conf"` ranked
`parse_conf` (`tools/memory-tree/tree_lib.py`) and `resolve_kit_dir`, the two this unit calls.

Recall terms used: budget_state draw run-state RUN.md rotated archive preflight archive_name_of MEMORY_ROOT patch budget slug
