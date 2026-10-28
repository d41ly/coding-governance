# TOOL-dRankedPlan-43 — a disposition record's first appearance follows renames and never copies

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 6 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-43-deviation-431.md](../build/2026-10-27-build-TOOL-dRankedPlan-43-deviation-431.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) | spec-audit | TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-44 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 30 to 37
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`) confirmed
**finding 19 at HIGH**, item **H5**. `TOOL-dRankedPlan-34` S1 dates a disposition record by the oldest
add along `git log --follow --diff-filter=A`, and leaves out the caveat its own seam documents:
"`--follow` ALSO FOLLOWS COPIES" (`tools/unattended/lib-unattended.sh:1725-1727`). Disposition records
share one fields form, so a second record written after the newest transition is a near-copy of the
first, and `--follow` dates it to the first record's add, before the transition. The owner's fresh
`terminal` record is then not kept, unit 34 AC3's release never comes, and every disposition reader
built on units 24, 25 and 26 holds falsely. This unit walks renames only: one path-limited log of the
build's `build/` folder with rename detection and no copy detection, followed back from the record's
path to its oldest add. It repairs `TOOL-dRankedPlan-34`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The walk. `read_first_appearance(repo, path)` in `tools/loop/ratify.py`
  (`TOOL-dRankedPlan-34` S1) reads `git log -M --name-status --format=%H -- <folder>/`, where
  `<folder>` is the record's own directory, once per call. It walks the commits from newest to oldest
  with a current name, starting at `path`. An `R<score>` line whose new name is the current name moves
  the current name to the old one. An `A` line naming the current name is an add, and the walk keeps
  the oldest such commit. It returns that commit, or `None` when the log names no add of any of the
  record's names. Without `-C` git reports a copy as a plain `A`, so a near-copy is dated by its own
  add. This supersedes unit 34 S1's `git log --follow --diff-filter=A --format=%H -- <path>`. Unit 34's
  keeping rule and every caller stand. Observed by AC1, AC2 and AC3.
- **S2** — The plants. `reader-bound` (`TOOL-dRankedPlan-24` S3, extended by `TOOL-dRankedPlan-34` S2)
  gains `copied-fresh`: a record committed before the newest transition, then a near-copy of it with
  two lines changed committed after the transition under a new name. The near-copy is kept and the
  first record is not. A new plant, `terminal-reentry-copied`, runs `terminal-reentry` with its second
  `terminal` record written as a near-copy of the first. Observed by AC1 and AC2.
- **S3** — The caveat carried. Unit 34 §4's table gains the rows of this unit's §4 "The date after this
  unit", and its §4 cites `tools/unattended/lib-unattended.sh:1725` for the copy caveat. NOT OBSERVED
  by a criterion: it is a record correction, which S2's plants observe in behaviour.

## 3. Non-goals (OUT)

- A fresh record added in the same commit that deletes a similar stale one, which git reports as a
  rename (finding 36): `TOOL-dRankedPlan-45`'s item, over S1's walk.
- Which of several kept records governs: `TOOL-dRankedPlan-35`.
- A record renamed into the folder from outside it. The path-limited log reports it as an add in the
  folder, so it is dated by its arrival there. Disposition records are born in their build's `build/`
  folder (TOOL-dDeclaredLoop-16 §4), so the case has no writer.

### Edges

- **consumes-from** `TOOL-dRankedPlan-34` — `read_first_appearance` and the `reader-bound` and `terminal-reentry` plants, whose `--follow` read S1 rewrites; without them there is no date to correct
- **hands-off** `TOOL-dRankedPlan-45` — S1's rename walk, over which that unit's item for finding 36 states and plants the replace-in-one-commit case
- **hands-off** `TOOL-dRankedPlan-52` — S3's edit to unit 34, which that unit's item for finding 28 withdraws; carry S24 into this unit's pass (spec audit of units 38 to 45, id 28)

## 4. Design

### Evidence

- `tools/unattended/lib-unattended.sh:1725-1727`: "`--follow` ALSO FOLLOWS COPIES: at a record's first
  commit it may continue into another file that shares more than half its lines, and date by that
  one's add."
- A scratch repository under `%TEMP%`, run 2026-10-27 with git 2.54.0.windows.1, committed `d1` (a
  seven-line record), an empty transition commit `T`, `d2` (a near-copy of `d1` with two lines
  changed), and then a `git mv` of `d1`. `git log --follow --diff-filter=A --format=%s -- b/d2.md`
  printed `d1`. `git log -M --name-status -- b/` printed `A b/d2.md` at `d2` and `R100 b/d1.md
  b/d1r.md` at the rename. Both readings are PINNED.
- The same repository then removed `b/d1r.md` and added a similar `b/d3.md` in one commit, and the
  `-M` log printed `R077 b/d1r.md b/d3.md`, the case §3 hands off.

### The date after this unit

| The record's history | Unit 34 S1's date | S1's date | Kept after a transition T |
|---|---|---|---|
| added after T | the add | the add | yes |
| added before T, `git mv`'d after T | the add before T | the add before T | no |
| added after T, `git mv`'d later | the add after T | the add after T | yes |
| a near-copy of a pre-T record, added after T | the older record's add | its own add | yes |
| added before T, deleted, added again after T | the first add | the first add | no |
| never committed | none | none | no |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `copied-fresh` | `reader-bound` case | none |
| `terminal-reentry-copied` | `ratify.py` fixture plant | none |

### Rollout

Live at landing, at order 6, before any reader built on unit 24 reads a second record.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Keep `--follow` and test whether the add it finds is a copy.** It needs a second log per record to
  tell a copy from a rename, and the walk answers both from one log of the folder.
- **`tree_lib.read_adding_commits`.** It reads with `--no-renames`, so a rename is an add, which is
  finding 26's defect (`TOOL-dRankedPlan-34` §3).

## 5. Production-readiness checklist

- security — narrows: a fresh owner act is no longer held as stale because its template matches an
  older one.
- perf / scale — one `git log` of the build's `build/` folder per record, the folder's own history.
- error / empty / loading states — a path the log never adds returns `None`, which unit 34 reads as not
  kept.
- observability — the plants print which record was kept.
- risks — a fresh record added in the commit that deletes a similar stale one reads as a rename; §3
  hands that case to its own item.
- testing — `copied-fresh` and `terminal-reentry-copied`, red and green, beside unit 34's rename cases.
- migration — none.
- user docs — N/A — no surface changes.

## 6. Acceptance criteria

- **AC1** — When the plant `reader-bound` runs its `copied-fresh` case, `read_item_disposition` returns
  the near-copy, and the first record is not kept.
  Red when: a near-copy written after the transition is dated before it.
- **AC2** — When `python ratify.py --fixture --plant terminal-reentry-copied` runs, `ratify.py tFix`
  under `terminal-command` exits 1 after the B6 move, and exits 0 printing `ratified —
  terminal-command` once the near-copy `terminal` record is committed.
  Red when: the owner's second record is held as stale.
- **AC3** — When the `renamed-stale` and `renamed-fresh` cases of `TOOL-dRankedPlan-34` S2 run at this
  unit's tip, they answer as unit 34 AC1 and AC2 state.
  Red when: the walk loses a rename.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · `copied-fresh`, `terminal-reentry-copied` and unit 34's rename cases, staged by a date read with `git log --follow --diff-filter=A` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 30 to 37, finding 19 (HIGH,
  item H5), repairing `TOOL-dRankedPlan-34`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-52`, each the reciprocal of that promoted unit's own edge (spec audit of units 38 to 45, `reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-34`'s `read_first_appearance`, whose body changes and whose
callers do not. The rule it keeps from `read_first_commit_date` (`tools/unattended/lib-unattended.sh:1731`)
is the oldest add along a record's names, and the caveat at :1725 is why it no longer uses `--follow`.
`python tools/codebase-map/reuse_lookup.py "date a file by its oldest add following renames but not
copies"` printed no candidate, so no seam fits beyond unit 34's reader. The recall query returned unit 34
itself and this audit's H5 item, and they agree with the probe.

Recall terms used: `python tools/memory-recall/query.py "how is a renamed record dated without following copies" --terms "rename copy follow diff-filter name-status first appearance disposition record freshness adding commit"`
