# TOOL-dMindYourWords-30 — the provenance blame reads the real commit graph, so a graft cannot make an old row look like a root's

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 8

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-34 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-35 TOOL-dMindYourWords-31 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 11 (TOOL-dMindYourWords-31) and 23 (TOOL-dMindYourWords-32).
TOOL-dMindYourWords-28 S2 runs the provenance blame with `--root` and reads a porcelain `boundary` mark
as the sign of a grafted history, but `--root` is exactly what stops git printing that mark, so the
graft arm never fires. Under a `git replace --graft` or an `info/grafts` entry, blame attributes every
older suppression row to the graft point, and the row is judged against a commit that never wrote it.
This unit makes the blame read the real commit graph, so each row is judged against the commit that
truly wrote it, and deletes the boundary arm that can never fire.

## 2. Scope (IN)

- **S1** — The pin on the provenance blame. The one blame per registry in
  `check_suppression_provenance` (TOOL-dMindYourWords-5 S4, bounded by TOOL-dMindYourWords-28 S2) runs
  as `git --no-replace-objects blame --porcelain --root -- <registry>` with `GIT_GRAFT_FILE=/dev/null`
  in its environment, the repository's pin policy for a history read
  (`tools/memory-tree/tree_lib.py:232-243`). A replace ref or a graft file then moves no row onto the
  graft point, and each row's commit is the one that wrote it. Observed by AC1 and AC2.
- **S2** — The dead boundary arm deleted. TOOL-dMindYourWords-28 S2's branch that reds a row carrying a
  porcelain `boundary` mark, `cannot judge provenance — history boundary at <sha8>`, is removed with its
  problem line, since under `--root`, a pinned graph and S1 of unit 28 (which refuses a shallow
  history first) no row of a full blame of `HEAD` carries the mark. Observed by AC3.
  **Readers:** by name: READER NOT IN TREE — the line `history boundary` is minted by
  TOOL-dMindYourWords-28 at order 7 and no tracked file spells it at base ccd1292e; that spec's AC3 and
  §4 pseudocode quote it as records · by value: NO VALUE READERS — the problem line is printed and
  counted in the run's exit status only, and no reader parses its text.
- **S3** — The docs. The suppression section of `tools/lexicon/README.md` states that provenance reads
  the real commit graph, ignoring replace refs and graft files, and that a shallow history is refused
  (unit 28 S4). NOT OBSERVED as behaviour: prose has no grader beyond the carriers' own legs.

## 3. Non-goals (OUT)

- The added-set reader `read_vocabulary_record(rev=<commit>)`: a graft point's added set is
  TOOL-dMindYourWords-32 (id 23), and the `--diff-filter=A` added set is TOOL-dMindYourWords-33 (id 12).
- The drift blame and the shared porcelain reader of TOOL-dMindYourWords-29 S42: TOOL-dMindYourWords-31
  (id 11), which carries this pin into that reader and spells it once for the kit.
- The left-shift gate the report names under H1, a selftest arm requiring every root-trusting history
  reader to red on a graft, and its checklist entry: a gate is its own unit (BUILD-METHOD M2).
- Kit version constants: versions are minted at landing (`tools/push-main.sh:26-31`), so this unit moves
  none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-28` — the provenance blame with `--root` and the boundary arm S2 deletes; without it there is no blame to pin
- **hands-off** `TOOL-dMindYourWords-31` — the pinned provenance blame, which that unit folds into the shared `read_blame_lines` with the kit's one pin
- **hands-off** `TOOL-dMindYourWords-40` — the provenance graft arm, whose graft-file failing case that unit makes reachable by clearing the ambient pin (review id 6)
- **hands-off** `TOOL-dMindYourWords-41` — the provenance graft arms, which stage their graft through `build_graft_fixture` and its control (review id 15)
- **hands-off** `TOOL-dMindYourWords-42` — the pinned provenance blame, to whose argv that unit adds `--ignore-revs-file=` (review id 30)

## 4. Design

### Evidence

- Unit 28 S2: "blame with `--root` ... a porcelain `boundary` mark on any row that is still printed then
  means a grafted or truncated history", and its §4 pseudocode reds on `blame[row].boundary`
  (`spec/2026-10-29-spec-TOOL-dMindYourWords-28.md` S2, §4 "The join, bounded").
- Measured on git 2.54.0 in a three-commit fixture under `%TEMP%`: after `git replace --graft <c2>`,
  `git blame --porcelain --root` attributed the first commit's line to `c2` and printed no `boundary`
  line; `GIT_NO_REPLACE_OBJECTS=1` blame attributed it to `c1`. With a `.git/info/grafts` entry instead,
  `--no-replace-objects` alone still attributed it to `c2`, and `GIT_GRAFT_FILE=/dev/null` restored the
  real graph, from Python's `subprocess` as well as from bash. PINNED 2026-10-29.
- The repository already pins its history readers this way: `build_git_env` sets
  `GIT_GRAFT_FILE=/dev/null` and its callers add `--no-replace-objects`
  (`tools/memory-tree/tree_lib.py:232-243`), and the unattended kit's history leg exports the same
  variable (`tools/unattended/check-pass-order.sh:43-46`). The lexicon kit imports no sibling
  (`check_self_containment`, `tools/lexicon/lexicon.py:2359`), so the two-line pin is carried at the
  call.

### The join, pinned

```
if shallow: refuse (unit 28 S1)
for registry with rows:
    blame = git --no-replace-objects blame --porcelain --root -- <registry>   # env GIT_GRAFT_FILE=/dev/null
    for row:
        commit = blame[row].commit
        ok = read_vocabulary_record(root, TAG, rev="index" if commit is zero else commit)
        if not ok: problem("SUPPRESSION WITHOUT PROVENANCE", registry, row, commit)
```

### Inventory

Minted: none. S2 retires one problem line.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-28. Unit 28's AC3, which expects `history
boundary` on a graft, cannot pass on a correct build of unit 28 as written; its builder meets it through
M2's AMEND route at that pass, and this unit's AC1 and AC2 are the observation that replaces it.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2
- `tools/lexicon/selftest.py`: the arm of §7
- `tools/lexicon/README.md`: S3

### Alternatives rejected

- **Drop `--root` and trust a boundary mark only at a true root**, the report's second route: it keeps a
  per-row predicate (`rev-list --max-parents=0` under no replace) beside the blame, and a graft file
  still moves rows onto the graft point before any mark is read.
- **Refuse whenever a replace ref or graft file exists**: it reds every adopter who uses `git replace`
  for an unrelated object, where the pin reads their real history and judges it.

## 5. Production-readiness checklist

- security — deny by default holds: each row is judged against the commit that wrote it, and no graft
  can substitute a commit that adds a record the row's own change never carried.
- perf / scale — unchanged: one blame per registry; the pin is an argv flag and one variable.
- error / empty / loading states — a pinned blame that fails because a real parent object is missing
  reds `cannot judge provenance — <why>` (unit 28 §5), never a pass.
- observability — each refused row names its real commit, the one the adopter can inspect.
- risks — a history whose replaced objects hide a commit the object store lacks reds instead of judging;
  that is a refusal the adopter can read, not a wrong green.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in a fixture whose first commit writes a suppression row
  with no `unit.lexicon.suppressions` record, whose second commit adds such a record, and whose second
  commit is grafted onto no parent with `git replace --graft <c2>`, it exits 1 naming `SUPPRESSION
  WITHOUT PROVENANCE` and the first commit's sha8.
  Red when: the row is blamed to the graft point, whose record admits it, and the run exits 0.
  fixture: the repository under `%TEMP%/<short>`, since a repository under the scratch path fails on
  Windows with `Filename too long`.
- **AC2** — When the same fixture carries the graft as a `.git/info/grafts` line naming the second
  commit instead of a replace ref, the run exits 1 naming the same row and the first commit's sha8.
  Red when: `--no-replace-objects` alone was added and the graft file still moves the row.
- **AC3** — When `git grep -n 'history boundary' -- tools/lexicon/lexicon.py` runs after the pass, it
  prints nothing.
  Red when: the dead arm and its problem line survive beside a blame that can never feed them.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 · the replace-ref and graft-file fixtures, its failing case the pin cut out of the provenance blame, under which AC1's row is blamed to the graft point and greens · none

## 8. Open questions

- **F1 — How does the provenance blame stay honest under a graft?** Options: (a) pin the blame to the
  real graph with `--no-replace-objects` and `GIT_GRAFT_FILE=/dev/null`; (b) drop `--root` and accept a
  boundary only at a true root; (c) refuse whenever a replace ref or graft file exists. (b) still reads
  graft-file rows at the graft point, and (c) reds adopters using `git replace` for unrelated objects.
  RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the repository's own pin policy at
  `tools/memory-tree/tree_lib.py:232` and the most capable survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 1 (HIGH, item H1, shared with ids 11 and
  23) of the round-1 audit of units 22 to 29, with the fix measured against a replace ref and a graft
  file.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 30 to 37
  declare toward this unit (TOOL-dMindYourWords-40, TOOL-dMindYourWords-41, TOOL-dMindYourWords-42); no scope, design or criterion moved.

## 10. Reuse audit

The seam is the repository's history pin, `build_git_env` (`tools/memory-tree/tree_lib.py:232-243`,
`GIT_GRAFT_FILE=/dev/null` with `--no-replace-objects` at the call), which
`tools/unattended/check-pass-order.sh:43-46` also spells; it is carried here at the call because the
lexicon kit imports no sibling. `python tools/codebase-map/reuse_lookup.py "ignore git replace objects
and grafts before trusting a history read"` ranked generic readers (`read`, `git`, `run_git`) and
`build_git_env` among them, which is the seam named; no lexicon-side helper exists to extend. The recall
probe surfaced TOOL-aMooredAnchor-1, which refused a replace ref or graft by presence in the unattended
kit, and its review record measuring `GIT_NO_REPLACE_OBJECTS`, which agree with this reading.

Recall terms used: `python tools/memory-recall/query.py "how does a git history reader stay honest when replace refs graft a commit onto no parent" --terms "graft replace no-replace-objects blame porcelain root boundary provenance diff-tree added shallow history"`
