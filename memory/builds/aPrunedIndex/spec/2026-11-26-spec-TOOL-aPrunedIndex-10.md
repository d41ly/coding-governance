# TOOL-aPrunedIndex-10 — the closing review's four lows: the sweep's cost stated as its ceiling, a named plant helper, and two steps whose HEAD git cannot read

**Status:** SPECCED · rev-1 · 2026-11-26 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-26-prompt-TOOL-aPrunedIndex-10-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-10-1-spec-brief.md) | research | TOOL-aPrunedIndex-4 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review, `2026-11-26-review-TOOL-aPrunedIndex-1-2-3-4-diff-review-round1`, confirmed four low
findings, L1 to L4, and the owner answered "Fix lows first". BUILD-METHOD M4 promotes them into one unit,
and this is it. After it, the README states the release sweep's cost as the ceiling the code states. The
plant helper the naming leg could not see becomes a named `def`. Two `gc-predates` steps make each HEAD
probe's git call fail. The two review classes no fix here gates are filed as asks for the owner.

## 2. Scope (IN)

- **S1** — L1. The sentence of `tools/playbook/README.md` that says a build clears released rows at "one
  seek per released pair" states the ceiling instead: one seek per released pair against the trees, plus a
  scan of `dirty_path` for each pair no tree holds. Observed by AC1.
- **S2** — L2. In the `released-rows` plant of `tools/playbook/gov_tag.py`, the lambda bound to
  `commit_texts` becomes a nested `def write_commit_texts`, and its nine call sites take that name.
  Observed by AC2 and AC3.
- **S3** — L3, step A. The `gc-predates` plant gains a step 7: an orphan worktree `wt5`, whose listed HEAD
  is the all-zero sha and whose directory holds no registry, makes the registry probe's `read_git` fail, and
  `--gc` refuses naming `wt5` with no row moved. Observed by AC4 and AC6.
- **S4** — L3, step B. The plant gains a step 8: `wt5` holds the fixture kit on disk, uncommitted, and no
  `.memory-tree.conf`, so the conf probe's `read_git` fails, and `--gc` refuses naming `wt5` with no row
  moved. Observed by AC5 and AC6.
- **S5** — Two asks in `memory/builds/aPrunedIndex/BACKLOG.md`, one per review left-shift that no fix here
  gates: `naming-leg-grades-what-python-named` and `closed-over-an-unaudited-spec-revision`. Each has a SEV
  row and a KEEP row awaiting the owner, as asks 5 to 9 do. Observed by AC7.
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
- A gate refusing CLOSED over an unaudited revision. That is the second ask of S5.
- L1's class `observed-by-claim-no-arm-discharges` is not asked again: a cost sentence written as a ceiling
  is its cure. L3's class `rule-stated-with-no-check-that-fails` is already ask `TOOL-aPrunedIndex-5`.
- The `gc-predates` row of `SELFTEST_ROWS` in `tools/playbook/tag_bundle.py`, and the plant's last line. Both
  keep their bytes, so spec 4's AC9 stays true. Steps 2 to 6 keep their numbers, which spec 4's
  criteria cite.
- Spec 3's section 5 sentence "a sweep costs one seek per released pair". Spec 3 is CLOSED and frozen.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py`, which other sessions are landing.
- Any `gov_tag.py` verb outside `--fixture` in a pass. Every observation here runs in a fixture's own
  scratch repository or reads a file.

### Edges

- **consumes-from** `TOOL-aPrunedIndex-4` — the `gc-predates` plant with its helpers, and the two HEAD
  probes of `read_live_versions` that steps 7 and 8 make fail.
- **consumes-from** `TOOL-aPrunedIndex-3` — the `released-rows` plant, which holds the lambda S2 names.
- **hands-off** external — the spec audit of `TOOL-aPrunedIndex-4` at rev-4, which this invocation runs
  beside this unit, for L4.
- **hands-off** external — the two gates S5 asks for, which await the owner.

## 4. Design

### L1, the README sentence

`tools/playbook/README.md@72f63c58:340` reads "and nothing else holds, one seek per released pair, and an
overlay clears none". `tools/playbook/tag_index.py#remove_released_rows` filters `dirty_path` on path and
blob, and then on blob alone. `dirty_path` is keyed on worktree and path
(`tools/playbook/tag_index.py@4d1a9ef3:115`), so neither filter has an index to seek. Its own ponytail
comment, `tools/playbook/tag_index.py@4d1a9ef3:877`, states the ceiling: the dirty half scans `dirty_path`
once per pair no tree holds. The sentence's middle clause becomes:

> one seek per released pair against the trees plus a scan of `dirty_path` for each pair no tree holds

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
   `run_collect()` must return a refusal naming `/wt5 cannot be read` and `namespaces.toml`, with no
   skipped line. Both counts must not move.
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
so a `--gc` that wrongly read it would collect nothing in this fixture. The refusal is the discriminating
assertion.

### The asks

The two asks join the `## Asks` list of `memory/builds/aPrunedIndex/BACKLOG.md` in the row shape of asks 5
to 9. Their ids are the next two of the build's family. The session owning the slug mints them, never a
fan-out child (`memory/HYGIENE.md`, "Ids — how a session mints them"). An ask filed on or after
`ASK_CUTOFF` owes a SEV row (`tools/memory-tree/backlog.py`, verdict 12), so each also gets a SEV row and a
KEEP row under `## Dispositions`.

| class | text names | accept |
|---|---|---|
| `naming-leg-grades-what-python-named` | review id 5; `_python_defs` grades only `FunctionDef` and `AsyncFunctionDef` names; 54 lambda-bound names in 23 tracked files on 2026-11-26 | `_python_defs` grades `Assign` and `AnnAssign` targets bound to a `Lambda` in the `lexicon naming predicates` leg, seen red on a planted name off the VERBS table, its offenders drained or pinned |
| `closed-over-an-unaudited-spec-revision` | review id 8; the build index prints `moved past its audited revision` and still renders CLOSED | the build index refuses CLOSED on an id that line lists unless a waiver is recorded, seen red on a planted CLOSED spec above its audited revision |

Each SEV row grades LOW, as the review graded the finding. Each KEEP row reads "awaiting the owner: a gate
for a review class this build's diff met, out of its scope".

### Timing

The budget file states that a single reading cannot tell a regressed suite from a busy box
(`tools/run-gates/selftest-budgets.txt`, its calibration paragraph). Spec 4 pins `gc-predates` prototypes at
17 to 35 s on one busy machine. So the builder times `python tools/playbook/gov_tag.py --fixture --plant (PINNED, 2026-11-25)
gc-predates` three times before the edit and three times after it, back to back on one box. The steps
lengthen the plant enough to matter only when the fastest reading after exceeds the slowest reading before.
Then the main loop re-times the leg alone at the close, by unit 4's AC8 method, and rewrites the
`tags bundle selftest` budget and evidence rows. Otherwise neither row moves, and the ledger says so.

### Files touched (estimate)

- `tools/playbook/README.md`, `tools/playbook/gov_tag.py`
- `memory/builds/aPrunedIndex/BACKLOG.md`
- the unit's acceptance ledger under `memory/builds/aPrunedIndex/build/`, one line per criterion, with the
  six readings AC8 takes
- only where AC8's rule fires, by the main loop at the close: `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/ceiling-evidence.txt`

## 5. Acceptance criteria

- **AC1** — When
  `python -c "import re, sys; t = re.sub(r'\s+', ' ', open(sys.argv[1], encoding='utf-8').read()).replace(chr(96), ''); print('one seek per released pair,' in t, 'a scan of dirty_path for each pair no tree holds' in t)" tools/playbook/README.md`
  runs, it prints `False True`.
  Red when: the sentence still claims one seek per released pair, with no scan named.
- **AC2** — When `grep -nw commit_texts tools/playbook/gov_tag.py` runs, it prints nothing. When
  `grep -cw write_commit_texts tools/playbook/gov_tag.py` runs, it prints 10, the `def` and its nine call
  sites. When `python tools/lexicon/lexicon.py --suggest write_commit_texts --as py.function` runs, it
  answers OK.
  Red when: the lambda stays bound, or one call site keeps the old name.
  figure: the nine call sites are PINNED at blob `c22d4773`, read 2026-11-26.
- **AC3** — When `python tools/playbook/gov_tag.py --fixture --plant released-rows` runs, it exits 0 and its
  last line is `only replaced edits left, and nothing lost`.
  Red when: a call site keeps the old name, so the plant stops on a `NameError`.
  cost: 49 s in unit 3's ledger. (PINNED, 2026-11-26)
- **AC4** — When `python tools/playbook/gov_tag.py --fixture --plant gc-predates` runs, its `step 7:` line
  ends `held`. That needs a refusal naming `/wt5 cannot be read` and `namespaces.toml`, no skipped line,
  and both counts above 0 and unmoved.
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
  lists both new asks as OPEN with severity LOW, their summaries naming `naming-leg-grades-what-python-named`
  and `closed-over-an-unaudited-spec-revision`. Its `build-index: backlog` line reads `0 verdict(s)`.
  Red when: an ask has no SEV row, so the backlog line counts a verdict and its severity reads unlabelled.
- **AC8** — When the builder times `python tools/playbook/gov_tag.py --fixture --plant gc-predates` three
  times before the edit and three after, on one box, the ledger records the six walls and the rule's
  answer. Where the fastest after does not exceed the slowest before,
  `git diff --exit-code b15bee51 -- tools/run-gates/selftest-budgets.txt tools/run-gates/ceiling-evidence.txt`
  prints nothing at the close. Otherwise the main loop's re-timing of the leg is recorded beside both rows.
  Red when: a row moves on an increase inside the plant's own spread, or one outside it is recorded and the
  rows stay.
  cost: six plant runs, about five minutes.
  permission: a pass runs no self-test leg, so re-timing the leg is the main loop's, at the close.
  figure: the six walls are PINNED when measured, in the ledger.

## 6. Gates

`tags bundle selftest` · `lexicon naming predicates` · `instruction units selftest` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/tag_bundle.py · covers AC4 AC6 · the `gc-predates` row's step 7; staged red by an `except TagError` reading the registry probe's failed `read_git` as empty, in the fixture only, never committed · none
New arm: tools/playbook/tag_bundle.py · covers AC5 AC6 · the `gc-predates` row's step 8; staged red by the same swallow around the conf probe's `read_git`, in the fixture only, never committed · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-26 · initial draft.

## 9. Reuse audit

The seams extended are the `gc-predates` plant with its own helpers `run_collect`, `check_refused` and
`measure_version`, and the fixture's `write_files` and `run_git`. The probe
`python tools/codebase-map/reuse_lookup.py "a fixture worktree whose HEAD git cannot read, so a git ls-tree probe fails"`
ranked only generic readers such as `read_git` and `run_git`, which the plant already calls. No existing
seam builds an unreadable HEAD, so the orphan worktree is git's own. The recall answered spec 4 first, then
this unit's review finding and brief, then `TOOL-dSweptBranches-7`, whose unread worktree status is a
different refusal.
Recall terms used: gc-predates plant orphan worktree unreadable HEAD ls-tree read_git TagError refuses skip registry conf
