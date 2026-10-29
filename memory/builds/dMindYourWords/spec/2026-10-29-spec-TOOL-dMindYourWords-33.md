# TOOL-dMindYourWords-33 — "the records that commit adds" lists only added paths, renames excluded

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 8 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-34 TOOL-dMindYourWords-30 TOOL-dMindYourWords-32 TOOL-dMindYourWords-35 TOOL-dMindYourWords-31 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 12 of `reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`,
HIGH, item H2. TOOL-dMindYourWords-28 S3 spells the added-set read as `git diff-tree --root -r
--name-only --no-commit-id <commit>` and calls its output "the records that commit adds", but without a
filter it lists every path the commit touches. A suppression row committed beside an ordinary edit to an
old `unit.lexicon.suppressions` record is then admitted, the pointer-to-any-old-record bypass
TOOL-dMindYourWords-5 rejected. This unit makes the read list only the paths the commit adds, with a
renamed old record not counted as added.

## 2. Scope (IN)

- **S1** — The added filter. The `rev=<commit>` mode of `read_vocabulary_record` in
  `tools/lexicon/lexicon_conf.py` (TOOL-dMindYourWords-11 S1, spelled by TOOL-dMindYourWords-28 S3)
  passes `-M --diff-filter=A` to its `git diff-tree`, beside whatever other flags that command carries,
  so only a path the commit creates is an added record, and a path it modifies, erases or moves under
  a new name is not. Observed by AC1 and AC2.
- **S2** — The root commit unchanged. Under `--root`, every path of a root commit is an add, so unit 28
  S3's root case still reads the root's whole tree as added. Observed by AC3.
- **S3** — A new record still admits. A commit that adds a new `unit.lexicon.suppressions` record beside
  its suppression row is admitted as before. Observed by AC4.

## 3. Non-goals (OUT)

- A graft point's parents, TOOL-dMindYourWords-32 (id 23), and the provenance blame,
  TOOL-dMindYourWords-30 (id 1).
- A merge commit's added set: `diff-tree` on a merge with no parent named prints nothing, and the one
  reader that asks it of a merge, the contract-record walk, defines it in TOOL-dMindYourWords-36.
- The idiom-ban arm and checklist entry the report names as H2's left-shift gate: a gate is its own unit
  (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-28` — S3's `diff-tree` spelling of the added set for a commit; without it there is no read to filter
- **hands-off** `TOOL-dMindYourWords-43` — S1's rename rule, which that unit applies to unit 36's per-parent merge read (review id 1)
- **hands-off** `TOOL-dMindYourWords-44` — S1's filtered single-commit read, which that unit spells through one argv builder shared with the merge read (review id 16)

## 4. Design

### Evidence

- Unit 11 S1 defines `rev` a commit as "only the records that commit adds count"
  (`spec/2026-10-29-spec-TOOL-dMindYourWords-11.md` S1); unit 28 S3 spells the read without a filter.
- Measured on git 2.54.0 in a fixture under `%TEMP%`: the report reproduced that a commit only
  appending to `f.txt` printed `f.txt` under the unfiltered read and nothing under `--diff-filter=A`; a
  commit that `git mv`s `rec.md` to `rec2.md` printed `rec2.md` under `--diff-filter=A` without `-M` and
  nothing with `-M`, since `diff-tree` detects no rename by default. PINNED 2026-10-29.
- TOOL-dMindYourWords-26 S1 already reads its added set rename-aware (`-M --diff-filter=A`), and its AC3
  keeps a `git mv` of an old record from admitting (`spec/2026-10-29-spec-TOOL-dMindYourWords-26.md` S1,
  AC3); this unit gives the per-commit read the same rule.

### Inventory

Minted: none.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-28 and beside TOOL-dMindYourWords-30 and -32, each
a separate change; none consumes another.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **`--no-renames`**, the refuted finder's fix (review id 18): it turns a `git mv` of an old record into a
  delete plus an add, so the renamed old record counts as added and reopens the bypass.
- **`--diff-filter=A` without `-M`**: `diff-tree` does no rename detection by default, so a renamed old
  record still reads as an add.

## 5. Production-readiness checklist

- security — deny by default: only a record the commit itself created admits its row.
- perf / scale — rename detection on one commit's diff, bounded by that commit's size.
- error / empty / loading states — a commit adding nothing prints nothing, which reads as no record and
  reds the row, the intended verdict.
- observability — the join's `SUPPRESSION WITHOUT PROVENANCE` names the row and the commit, unchanged.
- risks — a record moved and edited in one commit past the rename threshold reads as an add; that
  admits a row only with a record whose text the commit rewrote, the case unit 11 already admits.
- testing — AC1 to AC4 and the arm of §7.
- migration — none.
- user docs — N/A — the kit README's provenance sentence (unit 28 S4) already says "adds".

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in a fixture whose second commit appends a line to a
  `unit.lexicon.suppressions` record the first commit added and writes a suppression row for a live
  offender, it exits 1 naming `SUPPRESSION WITHOUT PROVENANCE` and the second commit's sha8.
  Red when: the edited old record admits the row.
  fixture: the repository under `%TEMP%/<short>`.
- **AC2** — When the second commit instead `git mv`s the old record to a new name and writes the row, the
  run exits 1 naming the same line.
  Red when: the renamed old record reads as added.
- **AC3** — When `python <kit>/lexicon.py` runs in a fixture whose root commit adds both the record and
  the row, it exits 0 with the row judged.
  Red when: the filter empties the root commit's added set.
- **AC4** — When the second commit adds a new `unit.lexicon.suppressions` record beside the row, the run
  exits 0.
  Red when: the filter refuses a genuinely added record.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 · four fixtures, an edited old record, a renamed old record, a root commit and a new record, its failing case the `--diff-filter=A` cut out of the read, under which AC1's row is admitted · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 12 (HIGH, item H2) of the round-1 audit of
  units 22 to 29.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 30 to 37
  declare toward this unit (TOOL-dMindYourWords-43, TOOL-dMindYourWords-44); no scope, design or criterion moved.

## 10. Reuse audit

The seam is the read itself, `read_vocabulary_record`'s `rev` mode (TOOL-dMindYourWords-11 S1 in
`tools/lexicon/lexicon_conf.py`), and the rename-aware added rule TOOL-dMindYourWords-26 S1 already
states for the branch's added set. `python tools/codebase-map/reuse_lookup.py "list only the paths a
commit adds, renames excluded"` ranked name-stem helpers (`build_commit`, `build_spec_path_re`,
`attribute_paths`) and no added-set reader, and `git grep -n 'diff-filter=A' -- tools` finds the filter
spelled per caller for its own population (`tools/drift-audit/drift_report.py:838`, `:1491`), so no
existing seam fits beyond the read this unit changes.

Recall terms used: `python tools/memory-recall/query.py "how does a git history reader stay honest when replace refs graft a commit onto no parent" --terms "graft replace no-replace-objects blame porcelain root boundary provenance diff-tree added shallow history"`
