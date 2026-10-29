# TOOL-dMindYourWords-43 — a merge's per-parent added set follows the rename rule, so a renamed old record is not a resolution's record

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 16 (TOOL-dMindYourWords-44), 23 (TOOL-dMindYourWords-45) and 29
(TOOL-dMindYourWords-46). TOOL-dMindYourWords-36 S3 reads what a merge adds as the intersection of
`git diff-tree -r --name-only --diff-filter=A <parent> <merge>` over every parent, with no `-M`.
TOOL-dMindYourWords-33 S1 requires `-M` on the single-commit read and rejects the spelling without it,
because `diff-tree` detects no rename by default and a `git mv` of an old record reads as an add. A
merge resolution that renames a record both parents hold therefore reads as adding it against every
parent, lands in the intersection, and admits a `CONTRACTS:` row the resolution wrote, reopening on the
merge path the bypass unit 33 closed. This unit applies unit 33's rename rule to the per-parent read.

## 2. Scope (IN)

- **S1** — The rename rule on the merge read. The per-parent read of `read_vocabulary_record`'s `rev`
  mode for a commit with more than one parent (TOOL-dMindYourWords-36 S3, in
  `tools/lexicon/lexicon_conf.py`) passes `-M --diff-filter=A`, so a path a parent held under another
  name is a rename against that parent and not an add, and the intersection excludes it. The rule is
  unit 33 S1's, stated once for both reads. Observed by AC1 and AC2.
- **S2** — A genuinely new record still admits. A record the resolution creates, under a name no parent
  held, is still an add against every parent, so unit 36 AC3's admission holds. Observed by AC2.

## 3. Non-goals (OUT)

- One spelling of the added-set argv for the single-commit and the per-parent read:
  TOOL-dMindYourWords-44 (id 16), which builds on this read.
- The provenance join's merge case: TOOL-dMindYourWords-45 (id 23).
- The kit self-check that refuses a `--diff-filter=A` argv without `-M`: TOOL-dMindYourWords-46 (id 29).
- The history pin on the per-parent read: TOOL-dMindYourWords-47 routes every spawn of
  `read_vocabulary_record` through the kit's pinned runner.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-36` — S3's per-parent intersection for a merge, the read S1 changes
- **consumes-from** `TOOL-dMindYourWords-33` — S1's rename rule, `-M --diff-filter=A`, which S1 applies to the merge read
- **hands-off** `TOOL-dMindYourWords-44` — the rename-aware per-parent read, which that unit spells through one argv builder shared with the single-commit read
- **hands-off** `TOOL-dMindYourWords-45` — the rename-aware merge read, through which the provenance join judges a row blamed to a merge

## 4. Design

### Evidence

- Unit 36 S3 spells `git diff-tree -r --name-only --diff-filter=A <parent> <merge>`
  (`spec/2026-10-29-spec-TOOL-dMindYourWords-36.md` S3) and unit 33 S1 requires `-M --diff-filter=A`,
  rejecting `--diff-filter=A` without `-M` in its §4 (`spec/2026-10-29-spec-TOOL-dMindYourWords-33.md`).
- The report's reproduction on git 2.54.0: after `git mv rec.md rec3.md`, `diff-tree` without `-M`
  printed `rec3.md` and with `-M` printed nothing (review ids 1 and 29).

### The read

```
for each parent p of merge m:
    added[p] = git diff-tree -r -M --diff-filter=A --name-only <p> <m>
records the merge adds = intersection of added[p] over every parent
```

### Inventory

Minted: none.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-36, first of the order-21 repairs to unit 36.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1, S2
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **`--no-renames`**: unit 33 §4 rejects it, since a rename then reads as a delete plus an add.
- **Excluding any path one parent held under a similar name by a second similarity pass**: that is
  what `-M` already computes.

## 5. Production-readiness checklist

- security — closes the merge-path bypass: a resolution cannot launder an old record into a new one by
  renaming it.
- perf / scale — rename detection on each parent's diff of one merge, bounded by that diff.
- error / empty / loading states — a merge adding nothing prints nothing against some parent, so the
  intersection is empty and the row needs a record, the intended verdict.
- observability — the existing `CONTRACTS changed with no change record` line names the merge.
- risks — a record moved and rewritten past the rename threshold in a resolution reads as an add;
  unit 33 §5 accepts the same case for a single commit.
- testing — AC1, AC2 and the arm of §7.
- migration — none.
- user docs — N/A — unit 3's README line on contract records already says each change carries one.

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in unit 36 AC1's fixture whose merge, in its resolution,
  `git mv`s a `unit.lexicon.contracts` record both parents hold to a new name and writes a `CONTRACTS:`
  row neither parent holds, it exits 1 naming `CONTRACTS changed with no change record` and the merge's
  sha8.
  Red when: the renamed old record reads as added against every parent and the run exits 0.
  fixture: a scratch repository under `%TEMP%/<short>`, no `core.hooksPath`.
- **AC2** — When the resolution instead writes a new `unit.lexicon.contracts` record under a name no
  parent held, beside the same row, the run exits 0.
  Red when: the rename rule refuses a record the resolution genuinely created.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 · a merge resolution that renames a both-parent record and one that adds a new record, its failing case `-M` cut from the per-parent read, under which AC1 exits 0 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 1 (HIGH, item H1, shared with ids 16, 23
  and 29) of the round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is `read_vocabulary_record`'s `rev` mode (TOOL-dMindYourWords-11 S1) with unit 33 S1's rename
rule, applied to the per-parent read unit 36 S3 adds. `python tools/codebase-map/reuse_lookup.py "list
only the paths a commit adds, renames excluded"` ranked name-stem helpers and no added-set reader to
import, and `git grep -n 'diff-filter=A' -- tools` finds the filter spelled per caller for its own
population (`tools/drift-audit/drift_report.py:838`, `:1491`), so no existing seam fits beyond the read
this unit changes.

Recall terms used: `python tools/memory-recall/query.py "how is a change made in a merge resolution held to the same record rule as an ordinary commit" --terms "evil merge resolution rename diff-filter added intersection parent contract record CONTRACTS row"`
