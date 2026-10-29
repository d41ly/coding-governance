# TOOL-dMindYourWords-45 — a suppression row blamed to a merge is judged by the merge's rename-aware added set

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-45-deviation-451.md](../build/2026-10-29-build-TOOL-dMindYourWords-45-deviation-451.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 23 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dMindYourWords-43), 16 (TOOL-dMindYourWords-44) and 29
(TOOL-dMindYourWords-46). TOOL-dMindYourWords-36 S3 changes `read_vocabulary_record`'s shared `rev`
mode for every caller, and the provenance join of TOOL-dMindYourWords-30 is one: blame names the merge
for a suppression row written in a conflict resolution, and the join asks that mode which records the
merge adds. So the merge-path rename bypass reaches suppressions as well as `CONTRACTS:` rows, and unit
36's criteria exercise only the latter. This unit declares the provenance join a reader of the merge
mode and holds it, on the suppression path, to the rename rule TOOL-dMindYourWords-43 gives that mode.

## 2. Scope (IN)

- **S1** — The join's merge case. When the provenance blame of `check_suppression_provenance` names a
  commit with more than one parent, the join judges the row by `read_vocabulary_record(root,
  ("unit.lexicon.suppressions",), rev=<merge>)`, the per-parent intersection with the rename rule, and
  never by a whole-tree or first-parent read. The kit README's suppression section says a row written
  in a merge resolution needs a record that resolution adds. Observed by AC1 and AC2.
- **S2** — The rename case refused. A merge resolution that renames a `unit.lexicon.suppressions`
  record both parents hold and writes a suppression row is refused `SUPPRESSION WITHOUT PROVENANCE`
  naming the merge's sha8. Observed by AC1.

## 3. Non-goals (OUT)

- The rename rule in the merge read: TOOL-dMindYourWords-43 (id 1).
- A row in a merge resolution whose record was added on one side only, and one whose record the
  resolution adds: review id 24, the minors batch TOOL-dMindYourWords-52.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-43` — the rename-aware per-parent read; without it AC1's renamed record is admitted
- **consumes-from** `TOOL-dMindYourWords-36` — S3's merge semantics of the shared `rev` mode, which the join now asks of a merge

## 4. Design

### Evidence

- Unit 30 §4 "The join, pinned" calls `read_vocabulary_record(root, TAG, rev=commit)` for whatever
  commit blame names (`spec/2026-10-29-spec-TOOL-dMindYourWords-30.md` §4).
- Unit 36 S3: "`read_vocabulary_record`'s `rev` mode reads a merge this way", and its AC1 to AC4 name
  only `CONTRACTS:` rows (`spec/2026-10-29-spec-TOOL-dMindYourWords-36.md` S3, §6).
- Blame attributes a line introduced in a merge's conflict resolution to the merge commit, the case the
  report's ids 23 and 24 rest on.

### The join for a merge

```
commit = blame[row].commit
if commit has more than one parent:
    ok = read_vocabulary_record(root, ("unit.lexicon.suppressions",), rev=commit)  # per-parent ∩, -M
```

### Inventory

Minted: none. The join's code is unchanged where unit 30 already passes the blamed commit to the `rev`
mode; S1 is then a declared reader and the README sentence, and the arm of §7 is the artifact.

### Rollout

Live at landing, after TOOL-dMindYourWords-43 at the same order, which sorts first.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, where the join special-cases a merge today
- `tools/lexicon/README.md`: S1
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **Judging a merge-blamed row by its first parent's added set**: it reads the side the merge took, not
  the resolution, and admits a row whose record came from the other branch.
- **Refusing every row blamed to a merge**: it reds a resolution that adds its own record, the case
  unit 36 admits for `CONTRACTS:` rows.

## 5. Production-readiness checklist

- security — closes the suppression half of the merge-path bypass: no renamed old record admits a row
  a resolution wrote.
- perf / scale — one per-parent read per merge-blamed row, rare by construction.
- error / empty / loading states — a failed per-parent read raises, and the join prints `cannot judge
  provenance — <why>` (unit 28 §5).
- observability — the refusal names the merge.
- risks — none beyond unit 43's rename threshold.
- testing — AC1, AC2 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S1).

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in a fixture whose two branches each hold the same
  `unit.lexicon.suppressions` record and whose merge, in its resolution, `git mv`s that record to a new
  name and writes a suppression row for a live offender, it exits 1 naming `SUPPRESSION WITHOUT
  PROVENANCE` and the merge's sha8.
  Red when: the renamed record reads as added against both parents and the row is admitted.
  fixture: a scratch repository under `%TEMP%/<short>`, no `core.hooksPath`.
- **AC2** — When `git grep -n -i 'merge' -- tools/lexicon/README.md` runs after the pass, a line in the
  suppression section says a row written in a merge resolution needs a record that resolution adds.
  Red when: the README still reads as if provenance only ever judged ordinary commits.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 · a merge resolution renaming a both-parent suppressions record beside a new row, its failing case `-M` cut from the per-parent read, under which the row is admitted · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 23 (HIGH, item H1, shared with ids 1, 16
  and 29) of the round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is the provenance join TOOL-dMindYourWords-5 S4 adds and unit 30 pins, reading through
`read_vocabulary_record`'s `rev` mode (TOOL-dMindYourWords-11 S1) as unit 36 S3 extends it to merges.
`python tools/codebase-map/reuse_lookup.py "judge a merge commit by whether each keyed row equals one
parent's"` ranked name-stem helpers and the row-keyed merge driver `tools/memory-tree/merge-rows.py`,
which merges rows and judges none, so no existing seam fits beyond the join this unit holds.

Recall terms used: `python tools/memory-recall/query.py "how is a change made in a merge resolution held to the same record rule as an ordinary commit" --terms "evil merge resolution rename suppression provenance blame intersection parent record row"`
