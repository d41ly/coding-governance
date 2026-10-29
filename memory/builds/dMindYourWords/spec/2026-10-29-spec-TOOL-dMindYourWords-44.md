# TOOL-dMindYourWords-44 — one argv builder spells the added-set read for a commit and for a merge's parent

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 16 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dMindYourWords-43), 23 (TOOL-dMindYourWords-45) and 29
(TOOL-dMindYourWords-46). The defect exists because TOOL-dMindYourWords-36 spelled a second `diff-tree`
for the same question unit 33 had already answered, "which records does this commit add", and the
second spelling dropped the first one's rename rule and pin. Fixing the flag in place leaves two
spellings that can drift again at the next edit. This unit makes the single-commit read and the
per-parent read of a merge build their argv in one function, so the rule is stated once.

## 2. Scope (IN)

- **S1** — The builder. `build_added_set_argv(commit, parent=None)` in `tools/lexicon/lexicon_conf.py`
  returns the `diff-tree` argv of the added-set read: with no `parent`, `["diff-tree", "--root", "-r",
  "-M", "--diff-filter=A", "--name-only", "--no-commit-id", commit]` (TOOL-dMindYourWords-28 S3 with
  unit 33 S1's filter); with a `parent`, `["diff-tree", "-r", "-M", "--diff-filter=A", "--name-only",
  parent, commit]` (unit 36 S3 with TOOL-dMindYourWords-43 S1's filter). Observed by AC1.
- **S2** — The one spelling. `read_vocabulary_record`'s `rev` mode builds both reads through S1, and
  `--diff-filter=A` is spelled once in `tools/lexicon/lexicon_conf.py`, inside the builder. Observed by
  AC2 and AC3.

## 3. Non-goals (OUT)

- The `-M` on the per-parent read itself: TOOL-dMindYourWords-43 (id 1); this unit moves that read into
  the builder unchanged.
- The spawn and its pin: TOOL-dMindYourWords-47 runs the built argv through the kit's pinned runner.
- The branch's added set, `read_branch_added_paths` in `tools/lexicon/lexicon.py`
  (TOOL-dMindYourWords-26 S1): a `git log` over a range, a different command for a different
  population; TOOL-dMindYourWords-46's self-check holds its rename rule.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-43` — the rename-aware per-parent read S1 moves into the builder
- **consumes-from** `TOOL-dMindYourWords-33` — S1's single-commit filter, the first spelling S1 moves into the builder
- **hands-off** `TOOL-dMindYourWords-46` — the builder, whose argv literal that unit's self-check judges as one added-set read

## 4. Design

### Evidence

- Unit 33 S1 adds `-M --diff-filter=A` to the single-commit `diff-tree` and rejects the spelling without
  `-M` (`spec/2026-10-29-spec-TOOL-dMindYourWords-33.md` S1, §4); unit 36 S3 spells the per-parent
  read verbatim without it (`spec/2026-10-29-spec-TOOL-dMindYourWords-36.md` S3). The report's id 16
  names that second spelling as the reuse defect.
- `tools/lexicon/lexicon_conf.py` spells no `diff-tree` at base (`git grep -n 'diff-tree' --
  tools/lexicon/lexicon_conf.py` prints nothing); every spelling this unit folds is minted by units 11,
  28, 33, 36 and 43 in this build.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `build_added_set_argv` | function, `tools/lexicon/lexicon_conf.py` | `py.function`; `lexicon.py --suggest build_added_set_argv --as py.function` answered `OK` at writing |

### Rollout

Live at landing, after TOOL-dMindYourWords-43 at the same order, which sorts first.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1, S2
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **A module constant holding the shared flags**: the two reads differ in `--root`, `--no-commit-id`
  and the parent operand, so the constant would be spliced at each site, two spellings again.
- **One function that also spawns and parses**: the spawn is TOOL-dMindYourWords-47's runner, and a
  builder that only returns argv is what S2's grep and unit 46's self-check can read.

## 5. Production-readiness checklist

- security — N/A beyond units 33 and 43: the same reads, spelled once.
- perf / scale — none.
- error / empty / loading states — unchanged; the builder raises on no input it does not already take.
- observability — unchanged.
- risks — a future third added-set read must call the builder or trip S2's single spelling.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — internal.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/lexicon'); import lexicon_conf as c;
  a = c.build_added_set_argv('X'); b = c.build_added_set_argv('X', 'P'); print('-M' in a, '-M' in b,
  '--diff-filter=A' in a, '--diff-filter=A' in b, '--root' in a, b[-2:])"` runs, it prints `True True
  True True True ['P', 'X']`.
  Red when: either read lacks the rename rule, or the per-parent read loses its parent operand.
- **AC2** — When `git grep -n -F -e '--diff-filter=A' -- tools/lexicon/lexicon_conf.py` runs after the
  pass, it prints lines inside `build_added_set_argv` only, and at least one.
  Red when: a second spelling of the added-set filter survives beside the builder, or none remains.
- **AC3** — When unit 33's AC2 fixture and TOOL-dMindYourWords-43's AC1 fixture are run with `python
  <kit>/lexicon.py` after the pass, each exits 1 as it did before this unit.
  Red when: folding the reads into the builder changed either verdict.
  fixture: the two fixtures under `%TEMP%/<short>`.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 · the builder's two argv shapes, its failing case `-M` cut from the per-parent branch of the builder, under which the second `True` prints `False` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 16 (HIGH, item H1, shared with ids 1, 23
  and 29) of the round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is `read_vocabulary_record`'s `rev` mode in `tools/lexicon/lexicon_conf.py`
(TOOL-dMindYourWords-11 S1), whose two `diff-tree` spellings this unit folds into one builder.
`python tools/codebase-map/reuse_lookup.py "list only the paths a commit adds, renames excluded"`
ranked name-stem helpers (`build_commit`, `build_spec_path_re`, `attribute_paths`) and no added-set
argv builder anywhere in the tree, so no existing seam fits beyond the reader this unit changes.

Recall terms used: `python tools/memory-recall/query.py "how is a change made in a merge resolution held to the same record rule as an ordinary commit" --terms "evil merge resolution rename diff-filter added intersection parent contract record CONTRACTS row"`
