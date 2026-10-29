# TOOL-dMindYourWords-36 — the contract-record walk examines merges, so a `CONTRACTS:` row made in a merge's resolution needs its record

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 20 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-34 TOOL-dMindYourWords-30 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-35 TOOL-dMindYourWords-31 TOOL-dMindYourWords-37 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 35 of `reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`,
HIGH, item H5. TOOL-dMindYourWords-29 S31 has `check_contract_record` walk `git log --full-history
--no-merges` over the commits touching `.lexicon.conf`, and states a rule for merges that `--no-merges`
never lets it apply. A `CONTRACTS:` row added or changed in a merge's conflict resolution, committed
with the hook bypassed, passes the bar with no `unit.lexicon.contracts` record. This unit walks the
merges too and judges each by a rule that admits a merge composing its parents' rows and refuses one
that writes a row none of them held.

## 2. Scope (IN)

- **S1** — Merges walked. `check_contract_record` lists the commits touching `.lexicon.conf` with `git
  log --full-history --format='%H %P' -- .lexicon.conf`, merges included, and reads each commit's
  `CONTRACTS:` rows and each parent's with the conf's own parser (TOOL-dMindYourWords-3 S1). A
  non-merge commit keeps S31's rule: rows that differ from its parent's need a record the commit adds.
  Observed by AC1 and AC4.
- **S2** — The merge rule. `check_merge_rows(merge_rows, parent_rows)` returns the tags, the rows' key
  (TOOL-dMindYourWords-3 §4 "Data model"), whose state in the merge equals its state in no parent, a
  tag's state being its row or its absence. A merge returning none composed its parents' rows, a side
  taken per tag, and needs no record; a merge returning any needs a `unit.lexicon.contracts` record it
  adds, else the run reds `CONTRACTS changed with no change record` naming the merge's sha8 and each
  tag. Observed by AC1, AC2 and AC3.
- **S3** — What a merge adds. For a commit with more than one parent, the records it adds are the paths
  `git diff-tree -r --name-only --diff-filter=A <parent> <merge>` lists for every parent, the
  intersection, since `diff-tree` on a merge with no parent named prints nothing and a path added on
  one side only is that side's, not the resolution's. `read_vocabulary_record`'s `rev` mode reads a
  merge this way. Observed by AC3.

## 3. Non-goals (OUT)

- The walk in a shallow history and at a parentless commit: review id 36, the minors batch
  TOOL-dMindYourWords-37.
- The history pin on the walk's reads: TOOL-dMindYourWords-31.
- The checklist entry the report names as H5's left-shift gate: a gate is its own unit (BUILD-METHOD
  M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-29` — S31's per-commit contract walk, which this unit widens to merges; without it there is no walk to widen
- **hands-off** `TOOL-dMindYourWords-37` — the merge-visiting walk, to which the batch adds the shallow and parentless-commit behaviour (id 36)
- **hands-off** `TOOL-dMindYourWords-43` — S3's per-parent read, to which that unit applies unit 33's rename rule (review id 1)
- **hands-off** `TOOL-dMindYourWords-45` — S3's merge semantics of the shared `rev` mode, which that unit holds on the provenance join (review id 23)
- **hands-off** `TOOL-dMindYourWords-49` — S1's merge-visiting walk and its parent reads, which that unit moves onto the pinned runner (review id 22)
- **hands-off** `TOOL-dMindYourWords-52` — S3's merge semantics, which the minors batch observes on the provenance join and applies to the branch walk (review ids 24, 37)

## 4. Design

### Evidence

- Unit 29 S31: "`check_contract_record` walks the non-merge commits touching `.lexicon.conf` (`git log
  --full-history --no-merges`) ... a merge whose rows equal its parents' combined rows needs none", and
  AC31 covers only a clean merge and a later non-merge deletion
  (`spec/2026-10-29-spec-TOOL-dMindYourWords-29.md` S31, AC31).
- A `CONTRACTS:` row is `<tag> <name> <defined> <reader> <match>`, the tag its key, which the parser
  refuses to repeat (`spec/2026-10-29-spec-TOOL-dMindYourWords-3.md` S1, §4 "Data model").
- Measured on git 2.54.0 in a fixture under `%TEMP%`: a merge whose resolution added a line to the conf
  was listed by `git log --full-history --format='%h %p %s' -- c.conf` and not by the same with
  `--no-merges`; `git diff-tree -r --name-only --no-commit-id --diff-filter=A <merge>` printed nothing,
  while `git diff-tree -r --name-only --diff-filter=A <parent> <merge>` named a record the resolution
  added for each parent, and a path from one side only for that side's other parent. PINNED 2026-10-29.

### The rule

| Tag state across the merge | Verdict |
|---|---|
| equals one parent's row, or absent where one parent lacks it | composed, no record owed |
| a row no parent holds, a new tag or a third value | resolution-made, record owed |
| absent where every parent holds it | resolution-made, record owed |

A conflicting edit resolved by taking one side's row is composed. A merge that drops a row only one
side added takes the other side's state for that tag and is composed too, as `git merge -s ours`
composes a side.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_merge_rows` | function, `tools/lexicon/lexicon.py` | `py.function`; `lexicon.py --suggest check_merge_rows --as py.function` answered `OK` at writing |

### Rollout

Live at landing, one order after TOOL-dMindYourWords-29, which mints the per-commit walk.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2
- `tools/lexicon/lexicon_conf.py`: S3
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **A merge differing from the union of its parents' rows needs a record**, the report's first wording:
  it reds a resolution that takes one side of a conflicting row edit, since the union holds both sides.
- **A three-way rule over the merge base**: it reds the same one-sided resolution, which leaves the other
  side's change unapplied.
- **A second pass over every merge in history**: it reads merges that never touched the conf;
  `--full-history` without `--no-merges` already lists every merge whose conf differs from all parents.

## 5. Production-readiness checklist

- security — closes a write-path bypass: no `CONTRACTS:` row reaches the tree through a merge without a
  record, hook or no hook.
- perf / scale — one more parse per merge parent, over the merges touching one file.
- error / empty / loading states — a merge with no conf at a parent reads that parent's rows as empty;
  an unparseable conf at any commit reds as unit 3's parser does, never a pass.
- observability — the red names the merge and every tag its resolution made.
- risks — a merge taking one side's state per tag is admitted without a record; each side's own commits
  already owed theirs under S1.
- testing — AC1 to AC4 and the arm of §7.
- migration — none.
- user docs — N/A — unit 3's README line on contract records already says each change carries one.

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in a fixture whose merge of two branches adds, in its
  resolution, a `CONTRACTS:` row neither parent holds, with no record and no `core.hooksPath`, it exits 1
  naming `CONTRACTS changed with no change record`, the merge's sha8 and the tag.
  Red when: the merge is never examined and the run exits 0, the wrong green the finding names.
  fixture: a scratch repository under `%TEMP%/<short>`.
- **AC2** — When both branches edit one row's `match` differently and the merge takes one side's row,
  the run exits 0; when the merge writes a third `match`, it exits 1 naming that tag.
  Red when: a one-sided resolution reds, or an invented row passes.
- **AC3** — When AC1's merge also adds a `unit.lexicon.contracts` record in its own resolution, the run
  exits 0; when the record was added on one branch only, it exits 1.
  Red when: a record the merge did not add admits its resolution.
- **AC4** — When the fixture merges two branches that each add a `CONTRACTS:` row and its record, the run
  exits 0, and a later commit deleting a row with no record exits 1 naming it.
  Red when: the clean merge reds, or the non-merge rule was lost.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 · an evil merge, a one-sided and a three-sided conflict resolution and a merge-added record, its failing case `--no-merges` restored to the walk, under which AC1 exits 0 · none

## 8. Open questions

- **F1 — When does a merge owe a contract record?** Options: (a) when any tag's state in the merge
  equals its state in no parent; (b) when its rows differ from the union of its parents' rows; (c) when
  they differ from a three-way merge over the base. (b) and (c) red a resolution taking one side of a
  conflicting edit, a change nobody made in the merge. RESOLVED (agent, 2026-10-29, delegated): (a),
  rung 3, the skeptic's refinement of the union test the report asked the builder for. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 35 (HIGH, item H5) of the round-1 audit of
  units 22 to 29, with the merge visibility and a merge's added set measured.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 30 to 37
  declare toward this unit (TOOL-dMindYourWords-43, TOOL-dMindYourWords-45, TOOL-dMindYourWords-49, TOOL-dMindYourWords-52); no scope, design or criterion moved.

## 10. Reuse audit

The seam is TOOL-dMindYourWords-29 S31's `check_contract_record` walk and unit 3's `CONTRACTS:` parser,
and the record read is `read_vocabulary_record`'s `rev` mode (TOOL-dMindYourWords-11 S1), extended to a
merge. `python tools/codebase-map/reuse_lookup.py "judge a merge commit by whether each keyed row equals
one parent's"` ranked name-stem helpers (`rows`, `key`, and `merge` in the row-keyed merge driver
`tools/memory-tree/merge-rows.py`); that driver merges rows and judges none, so no existing seam fits
the verdict.

Recall terms used: `python tools/memory-recall/query.py "how is a change made in a merge resolution held to the same record rule as an ordinary commit" --terms "evil merge resolution no-merges full-history parents contract record CONTRACTS row tag walk"`
