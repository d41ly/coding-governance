# TOOL-aMendedFleet-16 — `gotchas.py --for-diff` ranks classes by anchor specificity and cuts in tiers

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-16-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-16-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The bug-class checklist prints every class whose anchor selects a changed path, in catalogue order,
each as a three-line item. A 17-file review fold, `e4abc55bf`, draws 47 of the 94 classes plus 6
universals, and a class that names the exact file changed sits beside one that merely shares a
basename with it, at the same weight. This unit orders the selected classes by HOW specifically an
anchor matched, full path before directory before basename, and prints whole tiers in full only while
they fit a budget, so the low-specificity tail costs one line per class instead of three. No class
leaves the checklist.

## 2. Scope (IN)

- **S1** — Every (anchor, changed path) pair `selectable` admits is given a TIER by
  `derive_anchor_tier`: `path` when the anchor names that file, written whole or as a trailing
  suffix of two or more segments; `directory` when the anchor is a LEADING directory of that path,
  ending at a segment boundary; `basename` for every other pair `selectable` admits, a floating
  directory segment that does not start the path included. A class's tier is the best
  tier any of its anchors reaches. Selection itself is untouched: `selectable` decides membership,
  and the tier only orders it. Observed by AC1 and AC2.
- **S2** — The selected classes print in tier order, and within a tier by the number of changed paths
  the class reaches at that tier, most first, then by name. The universal records keep their place
  ahead of them, unranked and always in full. Observed by AC1, AC3 and AC4.
- **S3** — THE TIERED CUT. A tier prints in full, the three lines it prints today, when no earlier
  tier was cut and either it is the first non-empty tier or the full items through it number at most
  `CHECKLIST_FULL_BUDGET`, 12. From the first tier that fails that test, every class prints as ONE
  line: `- [ ] <name> (<tier>) · <record path>`. A cut never splits a tier. Observed by AC1.
- **S4** — Every item's first line is `- [ ] <name> (<tag>)`, the tag one of `universal`, `path`,
  `directory` or `basename`, so the class slug stays the first token after the box. The two header
  lines keep their bytes, and a third header line gives the per-tier counts and says that a cut tier
  prints one line per class. Observed by AC2 and AC3.
- **S5** — `--for-paths` takes the same order and cut, because `cmd_for_diff` already delegates to
  `cmd_for_paths` as the one selection path. Observed by AC1.
- **S6** — The kit README's `gotchas.py` row says the checklist is ranked by anchor specificity and
  cut at a tier boundary, and names the budget. Observed by AC5.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Narrowing selection. `selectable`'s predicate, the three carried harvest defects and their arms
  stay exactly as they are; this unit orders and compacts what it selects.
- Suppressing universals for a markdown-only diff. The wave-1 verification kept them, because the
  inline-fence class applies to records.
- Ranking by a touched dossier's gotcha claims. Wave 1 proposed it, and its verification found that
  unioning claimed classes grows a list that already over-selects.
- Reporting anchors that select zero paths, which is `TOOL-aMendedFleet-23`.
- Recording which classes a review caught. That is unit 17, which reads the class slug as the first
  token after the box, the shape S4 keeps.
- A budgeted top-N that the unattended driver hands a unit for its dispatch set. The report sequences
  it after one measured build.

### Edges

- **hands-off** `TOOL-aMendedFleet-23` — the zero-select anchor report over the same catalogue.
- **hands-off** `TOOL-aMendedFleet-17` — recording which classes a review caught, which reads the
  item shape S4 keeps: the class slug as the first token after the box.
- **hands-off** external — the driver's budgeted top-N per dispatch, which the report sequences after
  one build has measured whether ranking cuts checklist-fix commits.

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04.

- `cmd_for_paths` in `tools/memory-tree/gotchas.py` appends each class whose anchors `selectable`
  admits, prints universals first and the rest in catalogue order, every item as three lines, and
  cuts nothing. The report's "hard top-12 cut" describes no code in this tree: no consumer truncates
  the output either. It names the shape the report rejected, not one that exists.
- The catalogue holds 94 classes, 6 universal, with 314 derived anchors: 234 carry a slash and no
  trailing slash, 33 end in a slash, and 47 are bare basenames. PINNED, measured 2026-10-04.
- Tier counts over real ranges, computed with S1's predicate, PINNED 2026-10-04:

| Range | Files | Selected | path | directory | basename | Full under S3 |
|---|---:|---:|---:|---:|---:|---:|
| `7af5f564~1..7af5f564` | 7 | 7 | 1 | 3 | 3 | 7 |
| `6a88fbf7b~1..6a88fbf7b` | 14 | 8 | 0 | 3 | 5 | 8 |
| `548246a84~1..548246a84` | 9 | 25 | 14 | 5 | 6 | 14 |
| `e4abc55bf~1..e4abc55bf` | 17 | 47 | 31 | 5 | 11 | 31 |
| `2cbb2f09c^1..2cbb2f09c` | 60 | 50 | 41 | 5 | 4 | 41 |

  On a small diff nothing is compacted and only the order changes. On a large one the path tier
  dominates and stays in full, because those classes name files the diff changed.
- `tools/workflows/tier2-review.js` splits the checklist into items at every line starting `- `, and
  a later line not starting `- ` continues the item above it. A one-line item is still one item, and
  the new header line sits before the first item, in the preamble.

### Output shape

```
# recurring-bug-class checklist for <label> (<n> <noun>(s))
# <k> class(es) selected by an anchor + <u> universal
# by anchor specificity: <a> path · <b> directory · <c> basename; a cut tier prints one line per class

- [ ] <name> (universal)
      <description>
      <record path>

- [ ] <name> (path)
      <description>
      <record path>

- [ ] <name> (basename) · <record path>
```

### Inventory

- `derive_anchor_tier(anchor, path)`, returning 0, 1 or 2; `TIER_NAMES`, the three tag words in tier
  order; and `CHECKLIST_FULL_BUDGET = 12`, module constants of `gotchas.py`.
- The lexicon's `--suggest` answered `derive_anchor_tier` OK for cell `py.function`. A name the
  lexicon leg refuses at build time is replaced with its `--suggest` answer and this list amended
  with a rev bump.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/README.md`
- `memory/map/generated/symbols.json`

The memory-tree kit's version bump is owed once, at this build's close, after the last move.

### Alternatives rejected

- **Compact the basename tier always.** §8 F1: it compacts a 7-class checklist that fits on a screen.
- **A hard cut at N items.** It drops classes, and a class nobody is shown is a class nobody checks.
- **Rank inside the path tier by line-level overlap with the hunk.** It needs anchors at line
  granularity, and none of the 314 carries a line number.

## 5. Production-readiness checklist

- security — N/A — read-only over tracked records and `git diff --name-only`.
- perf / scale — one more pass over the pairs `selectable` already admits; milliseconds at 94
  classes and 60 paths.
- error / empty / loading states — no changed file and no selected class print today's lines; the
  third header line prints zeros rather than disappearing.
- observability — the third header line says how many classes sit in each tier and that a cut tier
  is compacted, so a short checklist never reads as a narrow one.
- risks — a consumer keyed to the three-line item shape loses a basename-tier description. Unit 17
  reads the first line only, and the review harness splits items by their `- ` lines.
- testing — new arms in `gotchas.py --selftest`, and direct runs on pinned ranges.
- migration — N/A — no stored data.
- user docs — the kit README's `gotchas.py` row, S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --selftest` runs, an arm whose fixture holds
  one class anchored at the changed file's full path, one at its directory and one at its basename
  elsewhere prints them in that order, tagged `(path)`, `(directory)` and `(basename)`, all in full;
  a second arm whose fixture holds 2 path-tier and 11 directory-tier classes at the shipped budget
  prints the 2 in full and each of the 11 as one line; and both arms hold for `--for-paths`.
  Red when: the order is catalogue order, a tag is missing, or the cut splits a tier or compacts the
  first one.
- **AC2** — When `python tools/memory-tree/gotchas.py --for-diff <range>` runs for
  `e4abc55bf~1..e4abc55bf` and `2cbb2f09c^1..2cbb2f09c`, the set of slugs on its `- [ ] ` lines and
  its first two lines equal those the same command prints in a throwaway clone checked out at the
  pass's parent commit.
  Red when: a class the old order printed is missing, an extra one appears, or a header byte moved.
  fixture: a `git clone --local` under a short `%TEMP%` root; the tree holds none today.
- **AC3** — When `python tools/memory-tree/gotchas.py --for-diff e4abc55bf~1..e4abc55bf` runs, every
  item's first line matches `^- \[ \] [a-z0-9-]+ \((universal|path|directory|basename)\)`, the tags
  never return to an earlier tier, and the third header line's three counts sum to the second line's
  selected count.
  Red when: an item breaks the shape, the tiers interleave, or the counts disagree.
  figure: the counts DERIVED at observation time.
- **AC4** — When `python tools/memory-tree/gotchas.py --for-diff 6a88fbf7b~1..6a88fbf7b` runs over that
  records-only commit, it prints every universal record that `gotchas.py --report` counts, each in
  full.
  Red when: a universal is missing or compacted on a markdown diff.
- **AC5** — When `grep -n "specificity" tools/memory-tree/README.md` runs, it hits the `gotchas.py`
  row, which names the three tiers and the budget of 12.
  Red when: the row is unchanged.

## 7. Gates

`gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py --selftest · a three-tier fixture and a 2-plus-11 fixture at the shipped budget, against today's catalogue-order output · none

Both paths sit under `tools/memory-tree/`, a guard the checker excludes as broad; `gotchas selftest`
is the suite that exercises this file, and `memory hygiene` runs its checks 17 to 19.

## 8. Open questions

- **F1 — Where does the cut fall?**
  Options: always compact the basename tier; compact the directory and basename tiers; or print whole
  tiers in full while they fit a budget of 12, compacting from the first tier that does not. On the
  five ranges in §4 the first compacts the two small checklists that fit a screen, and the second and
  third agree on the large ones. The third is the reading of "cut in tiers rather than a hard top-12".
  RESOLVED (agent, 2026-10-04, delegated): the budgeted tier cut, S3.
- **F2 — Do universals join the ranking?**
  Options: rank them as a fourth tier after basename; keep them first and in full. The wave-1
  verification kept universals for records diffs, and moving them changes the head of every
  checklist.
  RESOLVED (agent, 2026-10-04, delegated): first and in full, outside the budget.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `cmd_for_paths`, `selectable` and the catalogue at base.
- rev-2 · 2026-10-04 · §2 S7 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
  §3 Edges also gains **hands-off** `TOOL-aMendedFleet-17`: that unit reads the item
  shape S4 keeps, and neither spec declared the edge.
- rev-3 · 2026-10-05 · §2 S1 · build pass: "names a directory on that path at a segment boundary"
  read two ways, and only the LEADING-prefix reading reproduces the §4 pinned tier table on all five
  ranges; the any-segment reading moved a floating directory segment into the directory tier and
  disagreed on four rows. S1 now says leading directory, and the table stands unchanged.

## 10. Reuse audit

The seams extended are `cmd_for_paths` and `selectable` in `tools/memory-tree/gotchas.py`;
`derive_anchor_tier` reads only pairs `selectable` already admits, so the one selection predicate
stays one. `python tools/codebase-map/reuse_lookup.py "rank bug classes selected for a diff by how
specifically the anchor matches"` returned name-stem neighbours only, among them `anchors` in
`merge-rows.py` and `rank_with` in the recall bench, none of which ranks path matches, so no existing
seam fits. Recall named `TOOL-aFoldedQuarry-6`, which made the checklist DERIVED and accepted that it
over-selects, `TOOL-aWeighedCompass-14`, a measured over-selection on a directory path, and unit 23's
spec over the same anchors. Where the report and the tree disagree: no hard top-12 cut exists in
the tree, and every selected class prints in full today.

Recall terms used: `python tools/memory-recall/query.py "how does the gotchas checklist select and
order classes for a diff" --terms "gotchas for-diff checklist anchors selectable basename harvest
defect universal budget over-selects tier rank"`
