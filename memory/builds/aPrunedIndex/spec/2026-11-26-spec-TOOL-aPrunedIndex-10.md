# TOOL-aPrunedIndex-10 — the closing review's four lows: the sweep's cost stated as its ceiling, a named plant helper, and two steps whose HEAD git cannot read

**Status:** CLOSED · rev-2 · 2026-11-26 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md](../build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md) | journal | — |
| [2026-11-26-prompt-TOOL-aPrunedIndex-10-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-10-1-spec-brief.md) | research | TOOL-aPrunedIndex-4 |
| [2026-11-26-prompt-TOOL-aPrunedIndex-17-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-1-spec-brief.md) | research | TOOL-aPrunedIndex-17 |
| [2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3.md) | diff-review | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-20 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 |
| [2026-11-26-review-TOOL-aPrunedIndex-4-10-diff-review-round2.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-4-10-diff-review-round2.md) | diff-review | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 |
| [2026-11-26-review-TOOL-aPrunedIndex-4-10-spec-audit-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-4-10-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-4 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review, `2026-11-26-review-TOOL-aPrunedIndex-1-2-3-4-diff-review-round1`, confirmed four low
findings, L1 to L4, and the owner answered "Fix lows first". `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` promotes them into one unit,
and this is it. After it, the README states the release sweep's cost as the ceiling the code states. The
plant helper the naming leg could not see becomes a named `def`. Two `gc-predates` steps make each HEAD
probe's git call fail. One review class no fix here gates is filed as an ask for the owner; the other's gate
is already asked by `PLAY-dClosedLoop-21`.

## 2. Scope (IN)

- **S1** — L1. The sentence of `tools/playbook/README.md` that says a build clears released rows at "one
  seek per released pair" states the ceiling instead: up to two seeks per released pair against the trees,
  and up to two scans of `dirty_path` for each pair no tree holds. Observed by AC1.
- **S2** — L2. In the `released-rows` plant of `tools/playbook/gov_tag.py`, the lambda bound to
  `commit_texts` becomes a nested `def write_commit_texts`, and its nine call sites take that name.
  Observed by AC2 and AC3.
- **S3** — L3, step A. The `gc-predates` plant gains a step 7: an orphan worktree `wt5`, whose listed HEAD
  is the all-zero sha and whose directory holds no registry, makes the registry probe's `read_git` fail, and
  `--gc` refuses naming `wt5` with no row moved. Observed by AC4 and AC6.
- **S4** — L3, step B. The plant gains a step 8: `wt5` holds the fixture kit on disk, uncommitted, and no
  `.memory-tree.conf`, so the conf probe's `read_git` fails, and `--gc` refuses naming `wt5` with no row
  moved. Observed by AC5 and AC6.
- **S5** — One ask in `memory/builds/aPrunedIndex/BACKLOG.md`, for the review left-shift that no fix here
  gates and no open ask names: `naming-leg-grades-what-python-named`. It has a SEV row and a KEEP row
  awaiting the owner, as asks 5 to 9 do. Observed by AC7.
- **S6** — The `gc-predates` plant is timed alone before and after S3 and S4. The `tags bundle selftest`
  rows move only when the increase stands outside the plant's own run-to-run spread. Observed by AC8.

## 3. Non-goals (OUT)

- L4 makes no edit. Spec 4 is CLOSED and frozen. The spec audit this invocation runs beside this unit
  covers `TOOL-aPrunedIndex-4` at rev-4, and that audit clears the build index's
  `moved past its audited revision` line.
- The `dirty_path(blob)` index, or any other edit to `tools/playbook/tag_index.py`. Nothing in its import
  closure changes either; the brief, `2026-11-26-prompt-TOOL-aPrunedIndex-10-1-spec-brief`, lists that
  closure as printed by `import_walk.derive_module_closure`. Each edit there re-versions the `tag_index:*`
  extractors, and each node then pays a full re-parse, measured at 441 s on node a. (PINNED, 2026-11-26)
- The class-level lexicon gate, which would have `_python_defs` grade a name bound to a lambda. A probe over
  tracked Python on 2026-11-26 found 54 such names in 23 files across several kits. That gate is the first (PINNED, 2026-11-26)
  ask of S5.
- The other lambda-bound names in the same plant, `write_text` and `add`. Each already leads with a
  declared verb.
- A gate refusing CLOSED over an unaudited revision, and an ask for one. L4's class
  `closed-over-an-unaudited-spec-revision` is already asked by `PLAY-dClosedLoop-21`
  (`memory/builds/dClosedLoop/BACKLOG.md`), OPEN at LOW on 2026-11-26: the `specs-audited` term at
  `--close` reads a unit as audited only when a spec-audit record pins its current revision, waived by the
  existing `--override specs-audited`. A second ask at the build index would split one gate across two
  seams.
- L1's class `observed-by-claim-no-arm-discharges` is not asked again: a cost sentence written as a ceiling
  is its cure. L3's class `rule-stated-with-no-check-that-fails` is already ask `TOOL-aPrunedIndex-5`.
- The `gc-predates` row of `SELFTEST_ROWS` in `tools/playbook/tag_bundle.py`, and the plant's last line. Both
  keep their bytes, so spec 4's AC9 stays true. Steps 2 to 6 keep their numbers, which spec 4's
  criteria cite.
- Spec 3's section 5 sentence "a sweep costs one seek per released pair". Spec 3 is CLOSED and frozen.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py`, which other sessions are landing.
- Any `gov_tag.py` verb outside `--fixture` in a pass. Every observation of section 5 that a pass makes
  runs in a fixture's own scratch repository or reads a file. The gates of section 6 are not such
  observations: those that open the live index are owed at the close, under section 6's rider.

### Edges

- **consumes-from** `TOOL-aPrunedIndex-4` — the `gc-predates` plant with its helpers, and the two HEAD
  probes of `read_live_versions` that steps 7 and 8 make fail.
- **consumes-from** `TOOL-aPrunedIndex-3` — the `released-rows` plant, which holds the lambda S2 names.
- **hands-off** external — the spec audit of `TOOL-aPrunedIndex-4` at rev-4, which this invocation runs
  beside this unit, for L4.
- **hands-off** external — the gate S5 asks for, which awaits the owner, and `PLAY-dClosedLoop-21`'s for L4's
  class.

## 4. Design

### L1, the README sentence

`tools/playbook/README.md@72f63c58:340` reads "and nothing else holds, one seek per released pair, and an
overlay clears none". `tools/playbook/tag_index.py#remove_released_rows` filters `dirty_path` on path and
blob, and then on blob alone. `dirty_path` is keyed on worktree and path
(`tools/playbook/tag_index.py@4d1a9ef3:115`), so neither filter has an index to seek. Its own ponytail
comment, `tools/playbook/tag_index.py@4d1a9ef3:877`, states the ceiling: each EXISTS's dirty half scans
`dirty_path` once per pair no tree holds. Two DELETE statements each carry a tree half and a dirty half
(lines 879 to 884 of that blob), so a pair no tree holds pays two tree seeks and two `dirty_path` scans.
The sentence's middle clause becomes:

> up to two seeks per released pair against the trees, and up to two scans of `dirty_path` for each pair no tree holds

The rest of the sentence keeps its bytes. The help page `help/tags.md` makes no cost claim, so it is not
edited.

### L2, the lambda-bound helper

`tools/playbook/gov_tag.py@c22d4773:1365` binds `commit_texts = lambda files: write_commit(root,
derive_texts(files), "texts")`, with `# noqa: E731`. It becomes a nested `def write_commit_texts(files)`
whose body returns that call, in the same place, and the `noqa` goes. Its call sites at lines 1368, 1372,
1377, 1379, 1383, 1406, 1408, 1421 and 1503 of that blob take the new name. On 2026-11-26
`python tools/lexicon/lexicon.py --suggest write_commit_texts --as py.function` answered OK, leading with
`write`. The same probe of `commit_texts` answered that `commit` is not in the declared table.
`memory/map/generated/symbols.json` holds no nested name of this plant, so it is not regenerated.

### L3, the two steps

`tools/playbook/tag_index.py#read_live_versions` has two `read_git` calls on a worktree's listed HEAD. The
registry probe runs when no registry stands on disk. The conf probe runs when the registry reads and no
`.memory-tree.conf` file stands on disk. Each failure is a `TagError` inside the `try`, which refuses
naming the worktree. No step of `gc-predates` makes either call fail
(`tools/playbook/gov_tag.py@c22d4773:1045`, the plant at lines 1045 to 1132).

An orphan worktree supplies a HEAD git cannot read with no synthetic value. On 2026-11-26, on git 2.56.1,
`git worktree add -q --orphan -b five <path>` made a worktree whose directory held only `.git`.
`git worktree list --porcelain` listed it as `HEAD 0000000000000000000000000000000000000000`. On that sha
`git ls-tree --full-tree --name-only` exited 128 with `fatal: not a tree object`. `read_worktree_trees`
already passes over that HEAD's failed `rev-parse`, so only the two probes see it.

Steps 7 and 8 run after step 6, so the earlier steps keep their numbers. Before step 7 the plant counts the
rows of the root's live version with `measure_version(live)`, and the rows of `wt4`'s conf key from step 6
with `measure_version(key=key)`. Both counts must be above 0.

7. It adds `wt5` as an orphan worktree on branch `five`. Its directory holds no registry and no conf.
   `run_collect()` must return a refusal naming `/wt5 cannot be read` and `namespaces.toml`. Both counts
   must not move.
8. It copies the root's `FIXTURE_KIT` directory into `wt5`, uncommitted, so the registry and its modules
   read. No conf stands there. `run_collect()` must return a refusal naming `/wt5 cannot be read` and
   `.memory-tree.conf`, and both counts must not move.

Each step prints its `step <n>:` line ending `held` or `FAILED`, as steps 2 to 6 do. The last line is
printed only when steps 1 to 8 all hold, and keeps its bytes.

Each step's refusal names the probe that failed, because `read_git` quotes the failed git arguments. A swallow
around one probe therefore reds only its own step. Under a swallow around the registry probe, step 7 skips
`wt5` and exits 0, while step 8 never reaches that probe. Under a swallow around the conf probe, step 8 derives
the default key and exits 0, while step 7 refuses before it.

What the steps do not check: the counts guard against a move and discriminate nothing. `wt5` holds no row,
so a `--gc` that wrongly read it would collect nothing in this fixture. Nor does the absence of a skipped
line: `tools/playbook/gov_tag.py#run_gc` prints skipped lines only after `remove_dead_versions` returns, so
a refusal already implies none. The refusal is the discriminating assertion.

### The asks

The ask joins the `## Asks` list of `memory/builds/aPrunedIndex/BACKLOG.md` in the row shape of asks 5
to 9, and its text opens `THE CLASS naming-leg-grades-what-python-named`, as theirs open `THE CLASS`, so the
class leads the summary cell `render_summary_cell` cuts (`tools/memory-tree/backlog.py#render_summary_cell`).
Its id is the next of the build's family. The session owning the slug mints them, never a
fan-out child (`memory/HYGIENE.md`, "Ids — how a session mints them"). An ask filed on or after
`ASK_CUTOFF` owes a SEV row (`tools/memory-tree/backlog.py`, verdict 12), so it also gets a SEV row and a
KEEP row under `## Dispositions`. A new id changes the generated renders, so
`python tools/memory-tree/gen_build_index.py --write` re-renders them in the same pass.

| class | text names | accept |
|---|---|---|
| `naming-leg-grades-what-python-named` | review id 5; `_python_defs` grades only `FunctionDef` and `AsyncFunctionDef` names; 54 lambda-bound names in 23 tracked files on 2026-11-26 | `_python_defs` grades `Assign` and `AnnAssign` targets bound to a `Lambda` in the `lexicon naming predicates` leg, seen red on a planted name off the VERBS table, its offenders drained or pinned |

The SEV row grades LOW, as the review graded the finding. The KEEP row reads "awaiting the owner: a gate
for a review class this build's diff met, out of its scope".

### Timing

The budget file states that a single reading cannot tell a regressed suite from a busy box
(`tools/run-gates/selftest-budgets.txt`, its calibration paragraph). Unit 4's acceptance ledger measured
`gc-predates` at 46 s on one busy machine (its AC1 line). Spec 4 gives two prototype ranges for it, 19 to 35 s (PINNED, 2026-11-26)
in its AC1 and 17 to 35 s in its AC8, and neither is the measured figure. So the builder times (PINNED, 2026-11-25)
`python tools/playbook/gov_tag.py --fixture --plant gc-predates` three times before the edit and three times after it, back to back on one box. The steps
lengthen the plant enough to matter only when the fastest reading after exceeds the slowest reading before.
Then the main loop re-times the leg alone at the close, by unit 4's AC8 method, and rewrites the
`tags bundle selftest` budget row by hand and the evidence row by
`python tools/run-gates/derive-ceilings.py --write --observed`, as unit 4's ledger records for its AC8.
Otherwise neither row moves: both keep spec 4's reading at `d5288a92d` as the build's final figure, and
the ledger says so, recording that this replaces spec 4 AC8's "after the last unit of the build is built"
clause for unit 10.

### Migration

`tools/playbook/gov_tag.py` is in `instruction_units`' import closure, so S2 to S4 re-version the
`instruction_units:extract_unit` and `instruction_units:extract_repo` extractors, and each node re-parses
their rows at its next check. The brief accepts that cost; those extractors already re-version at every
`routed_commits.py` landing. The main loop measures the re-parse at the close on a private copy of the
node's index, by unit 1's timings method, and records it in the ledger (AC9).

### Files touched (estimate)

- `tools/playbook/README.md`, `tools/playbook/gov_tag.py`
- `memory/builds/aPrunedIndex/BACKLOG.md`
- regenerated for the new id by the generator's `--write` that The asks names:
  `memory/builds/aPrunedIndex/README.md` (its `ids:` line and generated regions), `memory/backlog/TOOL.md`
  and `memory/LIVE.md`
- the unit's acceptance ledger under `memory/builds/aPrunedIndex/build/`, one line per criterion, with the
  six readings AC8 takes and the re-parse AC9 records
- only where AC8's rule fires, by the main loop at the close: `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/ceiling-evidence.txt`

## 5. Acceptance criteria

- **AC1** — When
  `python -c "import re, sys; t = re.sub(r'\s+', ' ', open(sys.argv[1], encoding='utf-8').read()).replace(chr(96), ''); print('one seek per released pair,' in t, 'up to two scans of dirty_path for each pair no tree holds' in t)" tools/playbook/README.md`
  runs, it prints `False True`.
  Red when: the sentence still claims one seek per released pair, or names one scan where the code's two
  statements make two.
- **AC2** — When `grep -nw commit_texts tools/playbook/gov_tag.py` runs, it prints nothing. When
  `grep -cw write_commit_texts tools/playbook/gov_tag.py` runs, it prints 10, the `def` and its nine call
  sites. When `grep -c 'def write_commit_texts(' tools/playbook/gov_tag.py` runs, it prints 1. When
  `grep -cE 'commit_texts *= *lambda' tools/playbook/gov_tag.py` runs, it prints 0. When
  `python tools/lexicon/lexicon.py --suggest write_commit_texts --as py.function` runs, it answers OK.
  Red when: a lambda stays bound under either name, so the `def` grep prints 0 and the lambda grep 1, or
  one call site keeps the old name.
  figure: the nine call sites are PINNED at blob `c22d4773`, read 2026-11-26.
- **AC3** — When `python tools/playbook/gov_tag.py --fixture --plant released-rows` runs, it exits 0 and its
  last line is `only replaced edits left, and nothing lost`.
  Red when: a call site keeps the old name, so the plant stops on a `NameError`.
  cost: 49 s in unit 3's ledger. (PINNED, 2026-11-26)
- **AC4** — When `python tools/playbook/gov_tag.py --fixture --plant gc-predates` runs, its `step 7:` line
  ends `held`. That needs a refusal naming `/wt5 cannot be read` and `namespaces.toml`, and both counts
  above 0 and unmoved.
  Red when: a staged `except TagError` around the registry probe's `read_git` in `read_live_versions` reads
  the failure as an empty tree, so `wt5` is skipped and `--gc` exits 0.
- **AC5** — When the same plant runs, its `step 8:` line ends `held`. That needs a refusal naming
  `/wt5 cannot be read` and `.memory-tree.conf`, and both counts unmoved.
  Red when: a staged `except TagError` around the conf probe's `read_git` reads the failure as no conf in
  HEAD, so `wt5` derives the default key and `--gc` exits 0.
- **AC6** — When the same plant runs, it exits 0 and prints its last line ending
  `refused on wt4, wt3 read and then skipped by name, refused on none, refused on a conf`. Under either
  staged break of AC4 or AC5 it prints `FAILED` on that step and exits 1.
  Red when: the new steps' results are left out of the condition guarding the last line, so a red step 7
  or 8 still exits 0.
  cost: 46 s before this unit, in unit 4's ledger, plus the two steps. (PINNED, 2026-11-26)
- **AC7** — When `python tools/memory-tree/gen_build_index.py --asks --build aPrunedIndex --all` runs, it
  lists the new ask as OPEN with severity LOW, its summary opening
  `THE CLASS naming-leg-grades-what-python-named`. Its `build-index: backlog` line reads `0 verdict(s)`.
  When `python tools/memory-tree/gen_build_index.py --check` runs, it reports no drift.
  Red when: the ask has no SEV row, so the backlog line counts a verdict and its severity reads
  unlabelled, or the renders were not regenerated, so `--check` names a stale region.
- **AC8** — When the builder times `python tools/playbook/gov_tag.py --fixture --plant gc-predates` three
  times before the edit and three after, on one box, the ledger records the six walls and the rule's
  answer. Where the fastest after does not exceed the slowest before, at the close
  `git grep -h '^tags bundle selftest' b15bee51 -- tools/run-gates/selftest-budgets.txt` and
  `grep '^tags bundle selftest' tools/run-gates/selftest-budgets.txt` print the same line, the same two
  probes over `tools/run-gates/ceiling-evidence.txt` print the same line, and the ledger
  records that the rows keep spec 4's `d5288a92d` reading. Otherwise the main loop's re-timing of the leg is
  recorded beside both rows. Each probe reads that leg's row alone, so a merge of the default branch that
  moves other rows does not red it.
  Red when: a row moves on an increase inside the plant's own spread, or one outside it is recorded and the
  rows stay.
  cost: six plant runs, about five minutes.
  permission: a pass runs no self-test leg, so re-timing the leg is the main loop's, at the close.
  figure: the six walls are PINNED when measured, in the ledger.
- **AC9** — When the main loop, at the close, points `derive_index_path` at a private copy of the node's
  index and calls `gov_tag.main(["check"])` once at this unit's tip, by unit 1's timings method, the ledger
  records the run's wall and its summary line's `blobs parsed` and `extractor runs` counts.
  Red when: the ledger holds no such line, so the re-parse that section 4's Migration accepts stands
  unmeasured.
  permission: the call opens a private copy and never the live index, so it is the main loop's, at the close.
  figure: DERIVED at observation time.

## 6. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `instruction units selftest` · `lexicon naming predicates` · `tags bundle selftest` · `playbook render selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The line is spec 4's section 7 line carried over in full, for the files the two units share, plus
`memory hygiene` for the regenerated renders. Of it, the four legs spec 4's section 3 lists as opening the
live index, `tags (the resolver's checks)`, `instruction edits (manifest checks)`,
`edges (every declared edge parses, is registered and resolves)` and `instruction units selftest`, are
owed at the close once the owner's go holds, and by no pass before it.

New arm: tools/playbook/tag_bundle.py · covers AC4 AC6 · the `gc-predates` row's step 7; staged red by an `except TagError` reading the registry probe's failed `read_git` as empty, in the fixture only, never committed · none
New arm: tools/playbook/tag_bundle.py · covers AC5 AC6 · the `gc-predates` row's step 8; staged red by the same swallow around the conf probe's `read_git`, in the fixture only, never committed · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-26 · initial draft.
- rev-2 · 2026-11-26 · §1 §2 §3 §4 §5 §6 S1 S5 AC1 AC2 AC4 AC7 AC8 AC9 · folded
  `2026-11-26-review-TOOL-aPrunedIndex-4-10-spec-audit-round1`: finding 1 (AC2 tells a `def` from a
  lambda), 2 (the ask opens `THE CLASS`), 3 (Timing cites unit 4's measured 46 s), 4 (the rows keep spec
  4's `d5288a92d` reading, replacing its "after the last unit" clause for unit 10), 6 (section 3 narrowed
  to section 5's observations), 7 and 11 (the Migration subsection and AC9 measure the `instruction_units`
  re-parse), 8 and 15 (the cost sentence keeps the comment's "each"), 9 (L4's class is
  `PLAY-dClosedLoop-21`'s, so S5 files one ask), 10 and 13 (spec 4's leg line carried over with its
  owed-at-close rider, and `derive-ceilings.py --write --observed` named), 12 (the regenerated renders
  and `memory hygiene`), 14 (AC8 reads the leg's rows alone), 16 (no skipped line is not a check).

## 9. Reuse audit

The seams extended are the `gc-predates` plant with its own helpers `run_collect`, `check_refused` and
`measure_version`, and the fixture's `write_files` and `run_git`. The probe
`python tools/codebase-map/reuse_lookup.py "a fixture worktree whose HEAD git cannot read, so a git ls-tree probe fails"`
ranked only generic readers such as `read_git` and `run_git`, which the plant already calls. No existing
seam builds an unreadable HEAD, so the orphan worktree is git's own. The recall answered spec 4 first, then
this unit's review finding and brief, then `TOOL-dSweptBranches-7`, whose unread worktree status is a
different refusal.
Recall terms used: gc-predates plant orphan worktree unreadable HEAD ls-tree read_git TagError refuses skip registry conf
