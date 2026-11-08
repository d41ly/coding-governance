# TOOL-dCalibratedLens-38 — the work orders' adding commits read through `tree_lib.read_adding_commits` and their policy text through `read_blobs_at`, proved on a re-added and a renamed work order

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 10 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-38-deviation-381.md](../build/2026-11-02-build-TOOL-dCalibratedLens-38-deviation-381.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 19, HIGH, item H5 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). Unit 29 S1 spells its own
`git log --diff-filter=A --name-only --format=%H` over the work orders and its own `cat-file` map,
and its §10 says no seam batches per-path history. `tree_lib.read_adding_commits`
(`tools/memory-tree/tree_lib.py:302-325`) is "THE one adding-commit reader" (TOOL-dTrueNorth-20
S32): one `git log --no-renames --diff-filter=A --reverse` over one glob, keeping the oldest add.
With rename detection on, a renamed work order shows as `R` and gets no add, so a private pass drops
it from the p90 population, and two adding-commit readers can disagree on a work order deleted and
re-added, the class S32 merged. Which add governs a re-added work order follows from what unit 6
measures: its bytes at `HEAD`, which the re-add wrote, so the policy that governs them is the one in
force at the newest add (round-3 id 15). This unit puts the step on the two shared readers, gives the
one adding-commit reader that choice and the bound unit 29's step needs, and proves both on the
histories that expose them. It repairs `TOOL-dCalibratedLens-29`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text. Unit 29 S1
  (rev-2, id 19) and unit 6's id-52 amendment (rev-3, r2 id 19): `derive_role_item_budgets` in
  `tools/loop/measure.py` takes each work order's adding commit from
  `tree_lib.read_adding_commits(root, "memory/builds/*/prompts/*.md", wanted, newest=True)`, `wanted`
  the sliced paths, and each adding commit's `.governance/policy.toml` text from ONE
  `tree_lib.read_blobs_at(root, [(sha, ".governance/policy.toml"), …])` call, grouping the commits
  by that text so `policy.py get memory.item-budget --rev <one commit of the group> --json` runs once
  per distinct text. `tree_lib` is reached through `resolve_kit_dir("memory-tree", "tree_lib.py", …)`,
  as `load_tree_lib` in `tools/policy/check_policy.py:882-886` reaches it. Unit 29 §10 names both
  seams. Observed by AC1.
- **S3** — The shared readers, in `tools/memory-tree/tree_lib.py`. `read_adding_commits(root,
  pathspec, wanted, newest=False, timeout=None)`: with `newest=True` it keeps the last add its
  `--reverse` log shows for each path, the add that wrote the bytes at `HEAD`, and with the default it
  keeps the first, so its callers at base, `tools/memory-tree/deviation_join.py:588-589` and
  `tools/memory-tree/gen_build_index.py:680`, read what they read today (round-3 id 15). `read_git_output(root, argv, stdin=None,
  timeout=None)` passes `timeout` to `subprocess.run` and turns its expiry into `OSError` naming the
  command and the bound; `read_adding_commits` and `read_blobs_at` take the same keyword and pass it
  through. Unit 29's step passes 120, so its `item-budgets: unread · timed out` line comes from the
  shared readers and no private subprocess is written (round-3 id 20). Observed by AC3 and AC4.
- **S2** — The proof, a `--fixture` plant `item-budget-history` in `tools/loop/measure.py`. In a
  scratch repository it commits three sliced work orders of one role: `a.md` added once; `b.md`
  added, taken out by `git rm` and added again under a later policy text; `c.md` added and then
  renamed by `git mv` to `d.md`. It runs the step's mapping and prints one `<path> · <sha8>` line per mapped
  work order. It holds when `b.md` maps to its second add, the re-add whose bytes are at `HEAD`,
  `d.md` to the commit that added it under its new name, and `c.md` is absent as an untracked path; it
  prints `item-budget-history — ok`, and otherwise one FAIL line per wrong or missing path. A second
  case, `item-budget-history-bound`, runs the step with its bound set to 0.001 s and holds when the
  reading is `item-budgets: unread · timed out` (round-3 id 20). Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- A gate that reds `--diff-filter=A` spelled outside `tree_lib`, the finding's left-shift line.
  `git grep` finds 49 such lines in ten files under `tools/` at base (2026-11-02, PINNED), most in
  suites that plant histories; a ban needs its own census and exemptions, which is not this build's.
- Paths with no adding commit at all, and adding commits with no policy file: ids 34 and 35, both
  `TOOL-dCalibratedLens-41`, which state the unmapped-path line and the absent group on the same step.
- The stdin form of `handoff.py reads`: unit 29 S1, unchanged.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-6` — `derive_role_item_budgets` in `tools/loop/measure.py`, whose history read S1 puts on the shared readers, newest add first (round-3 id 15); without it there is no mapping to hold
- **consumes-from** `TOOL-dCalibratedLens-29` — the one-pass step of `derive_role_item_budgets` and the `measure.py --fixture` frame its `item-budget-tree` plant joins; without them there is no step whose mapping the plant reads

## 4. Design

### Evidence

- `tools/memory-tree/tree_lib.py:302-325` at base: `read_adding_commits(root, pathspec, wanted)`,
  `log --no-renames --diff-filter=A --reverse --format=%x00%H --name-only -- <pathspec>`, keeping the
  first add seen through `added.setdefault`; a path with no add under the pathspec is absent from the
  answer.
- `tools/memory-tree/tree_lib.py:278-299` at base: `read_git_output(root, argv, stdin=None)` calls
  `subprocess.run` with no timeout, and neither reader takes one (round-3 id 20).
- Unit 6 S2 measures each tracked work order's bytes at `HEAD` and counts it only when
  `memory.item-budget` read `measured` at its adding commit; before its round-2 amendment it spelled
  `git log --diff-filter=A -1`, the newest add (round-3 id 15).
- `tools/memory-tree/tree_lib.py:328-340`: `read_blobs_at(root, requests)`, one `git cat-file
  --batch`, `None` for a `missing` object.
- `tools/policy/check_policy.py:879-886`: `resolve_kit_dir` and `load_tree_lib(kit)`, the cross-kit
  route a kit outside memory-tree already takes.
- The review's probe over this repository: 27 of 2,172 tracked work orders get no adding commit from
  a pass with rename detection on, and 2 with `--no-renames` (PINNED, 2026-11-02).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `item-budget-history` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/loop/measure.py` — S2, the plant
- `tools/memory-tree/tree_lib.py` — S3, the two keywords

### Alternatives rejected

- **Add `--reverse --no-renames` to unit 29's own pass.** The flags would agree today and drift the
  next time either reader changes; S32 merged the readers for that reason.
- **Map each work order to its oldest add, the rev-1 design.** It pairs a re-add's bytes with the
  policy of an add whose bytes no longer exist (round-3 id 15).
- **A private subprocess with its own timeout in the step.** It recreates the second reader this unit
  exists to remove (round-3 id 20).
- **A `--batch-check` sibling in `tree_lib` keyed by blob id.** The step needs one policy read per
  distinct policy, and grouping by text gives that from the reader that already exists.

## 5. Production-readiness checklist

- security — no new surface; the shared readers run fixed argv, never the paths themselves.
- perf / scale — one `git log` and one `git cat-file --batch` for the population, as unit 29 states.
- error / empty / loading states — a failed or timed-out git call is `OSError` from the reader; the
  step passes its 120 s bound to the reader and turns the error into its `unread` line, as unit 29
  states.
- observability — the plant prints each mapping.
- risks — `tree_lib` absent where the loop kit is installed alone: `resolve_kit_dir` raises, and the
  step's reading is `unread`, as any absent kit is (unit 3's id-11 amendment).
- testing — AC1 to AC4 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python measure.py --fixture --plant item-budget-history` runs from the loop kit
  directory, it prints `item-budget-history — ok`: `b.md` mapped to its second add and `d.md` to its
  rename commit.
  Red when: a re-added work order takes its first add, or a renamed one is dropped.
- **AC2** — When the plant runs with the step's mapping staged as a private pass that keeps the first
  add and runs without `--no-renames`, it prints FAIL lines naming `b.md` and `d.md`.
  Red when: the plant passes a reader that disagrees with `read_adding_commits`.
- **AC3** — When `python measure.py --fixture --plant item-budget-history` runs, its
  `item-budget-history-bound` case prints `ok`, the step's reading being
  `item-budgets: unread · timed out`.
  Red when: a bound the readers ignore lets the step block, or a timeout raises out of the walk.
- **AC4** — When a `python -c` probe from the memory-tree kit directory calls
  `tree_lib.read_adding_commits` over a scratch history adding one path twice, the default answer is
  the first add and `newest=True` answers the second.
  Red when: the default moves, so the deviation join and the index generator read a different commit.

## 7. Gates

`policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop measure fixtures` (TOOL-dCalibratedLens-4 S9) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/measure.py · covers AC1 AC2 AC3 · the `item-budget-history` plant and its bound case, staged red by a private adding-commit pass that keeps the first add without `--no-renames`, and by a bound the readers ignore · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 19 (HIGH, item H5) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; units 29 and 6 amended at the disposal
  (their rev-2 and rev-3).
- rev-2 · 2026-11-03 · §1 §3 §4 §5 §7 S1 S2 S3 AC1 AC2 AC3 AC4 · amended at the disposal of the round-3
  spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, from `TOOL-dCalibratedLens-48`:
  a re-added work order maps to its newest add, argued from what unit 6 measures, through a
  `newest` keyword on the shared reader (id 15); the readers carry unit 29's 120 s bound through a
  `timeout` keyword, with a bound case in the plant (id 20); S3, AC3 and AC4 are new; §3's
  consumes-from of unit 6 names the newest add.

## 10. Reuse audit

The seams extended are `tree_lib.read_adding_commits` and `tree_lib.read_blobs_at`
(`tools/memory-tree/tree_lib.py:302-340`), reached cross-kit the way `tools/policy/check_policy.py`
reaches them. `python tools/codebase-map/reuse_lookup.py "the commit that added each path of a glob
in one git log pass"` ranked `read_git_output` in `tools/memory-tree/tree_lib.py` among name-stem
matches (`git`, `run_git`), the module whose next function is `read_adding_commits`; its docstring
calls it "THE one adding-commit reader", and reading the module found `read_blobs_at` beside it. Unit
29 §10 at rev-1 said no seam fits; the map's hit and that claim disagree, and the source decides.
The recall probe returned TOOL-cMendedVintage-19, the placement ruling this unit's order
follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
