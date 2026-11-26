# TOOL-aPrunedIndex-17 — the five tag plants hold the git answers that cannot change while they run

**Status:** SPECCED · rev-1 · 2026-11-26 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-26-prompt-TOOL-aPrunedIndex-17-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-1-spec-brief.md) | research | TOOL-aPrunedIndex-10 |

<!-- /gen:spec-records -->

## 1. Goal

The `tags bundle selftest` leg passed in 521 s at `22c3e175d`, over its 159 s budget row and its 300 s (PINNED, 2026-11-26)
ceiling, and round 2 of the closing review owns that as id 1. The owner's answer was "Make plants
cheaper". The five plants this build added spend most of their wall starting git processes, and many
of those processes ask git a question whose answer cannot change while the plant runs. After this unit
those five plants answer such a question once and reuse the answer. Every verdict they give stays
the same.

## 2. Scope (IN)

- **S1** — `tools/playbook/gov_tag.py` gains `derive_held_key(repo, args)`. It returns a key only for a
  git read whose answer is fixed for the plant's life, and `None` for every other read. The rule is item
  1 of section 4's Mechanism. Observed by AC2.
- **S2** — `tools/playbook/gov_tag.py` gains a context manager, `set_git_held()`. For the length of its
  block it answers each read that has a key from a dictionary, and runs git for the first read of each
  key. It never stores a failure. On exit it puts `tag_index`'s two git readers back.
  Observed by AC3.
- **S3** — `tools/playbook/gov_tag.py#run_fixture` runs the five plants of this build inside
  `set_git_held()`, and runs every other plant as today. The five are `dead-versions`, `named-probe`,
  `released-rows`, `released-cost` and `gc-predates`, held in one tuple, `HELD_PLANTS`.
  Observed by AC4 and AC5.
- **S4** — Every verdict stays. Each of the five plants keeps its exit, its last line and each step
  line it prints today. Every staged break the build's acceptance ledgers record for them still turns
  its plant red. Observed by AC1, AC5 and AC6.
- **S5** — The builder times the five plants before and after the edit, back to back, with a load
  gauge beside each reading. Observed by AC7.
- **S6** — The main loop re-times the leg at the close. It rewrites the `tags bundle selftest` row of
  `tools/run-gates/selftest-budgets.txt` and that leg's row of `tools/run-gates/ceiling-evidence.txt`
  from the new readings, and neither row moves up. Observed by AC8.

## 3. Non-goals (OUT)

- Any edit to `tools/playbook/tag_index.py` or to a module in its import closure. The brief lists that
  closure, and on 2026-11-26 `import_walk.derive_module_closure` printed the same nine modules. An edit
  there re-versions every `tag_index:*` extractor, and each node then pays a full re-parse. So the held
  answers live in `gov_tag.py` and replace `tag_index`'s two module attributes for the plant's block
  only. The bytes of `tag_index.py` do not change.
- A held answer for any plant outside the five. The other plants run in other legs, with their own
  recorded reds, which this unit does not re-observe.
- Merging verb runs, or reusing a built fixture across steps or plants. Section 4's "Alternatives
  rejected" gives the measured reason for each.
- Running the leg's plants concurrently in `tools/playbook/tag_bundle.py#run_selftest`. It is a second
  mechanism, in another file. It is handed off below, for the case where AC8's readings miss.
- Moving any ceiling or budget up. The leg's 300 s `ceiling` in `tools/gate-legs.json` keeps its value.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py`, which other sessions are landing.
- Any `gov_tag.py` verb outside `--fixture` in a pass. Every pass observation runs in a fixture's own
  scratch repository or is a `python -c` probe that opens no index.

### Edges

- **consumes-from** external — the five plants and the staged breaks the build's acceptance ledgers
  record for them. Units built and closed earlier in this build wrote both. A closed spec is frozen
  and declares no edge back.
- **hands-off** external — a bounded pool over the leg's plants in `run_selftest`, as a unit the session
  owning this slug mints. Section 4 measures this unit alone short of the brief's target, so the pool is
  likely owed. AC8's readings at the close decide it.

## 4. Design

### Evidence

Every git command the index module runs itself goes through one of two module attributes. Its blob
reads and its `hash-object` run through memory-tree's `tree_lib` instead, and this unit holds none of
them. `tools/playbook/tag_index.py#read_git` calls `read_git_stdout` by its global name.
`tools/playbook/tag_index.py#common_git_dir` calls `git`, which `tools/playbook/tag_index.py@4d1a9ef3:597`
binds to the same function. `tools/playbook/tag_index.py#derive_index_path` calls `common_git_dir`, so
each `load_index` starts one `git rev-parse --git-common-dir`. Each `derive_context` starts one
`git rev-parse --show-toplevel`. `tools/playbook/tag_index.py#read_worktree_trees` starts one
`git rev-parse <sha>^{tree}` for each listed worktree, and `remove_dead_holders` calls it on every build
and every `--gc`. The two HEAD probes of `tools/playbook/tag_index.py#read_live_versions` each start
one `git ls-tree --full-tree --name-only <sha> -- <path>`.

A scratch probe counted each plant's process spawns by patching `subprocess.Popen` around
`gov_tag.main(["--fixture", "--plant", <plant>])`, at `f963331d`, on node a, 2026-11-26. The counts were
the same on each repeated run, so they do not depend on load. For `gc-predates` it counted 152 spawns: (PINNED, 2026-11-26)

| git read | spawns | can its answer change while the plant runs |
|---|---|---|
| `rev-parse --git-common-dir` | 40 | no, for a worktree that exists |
| `rev-parse <sha>^{tree}` | 27 | no: a sha names one object |
| `worktree list --porcelain` | 19 | yes, the plant adds and removes worktrees |
| `ls-tree --full-tree --name-only <sha> -- <path>` | 15 | no: a sha names one object |
| `rev-parse --show-toplevel` | 10 | no, for a worktree that exists |
| the rest: `HEAD^{tree}`, `diff`, `hash-object`, the fixture's own writes | 41 | yes, or not a read of `tag_index` |

The spawn counts PINNED on 2026-11-26 at `f963331d`, first without held answers and then with a scratch (PINNED, 2026-11-26)
copy of S1 and S2 patched in:

| plant | spawns without | spawns with |
|---|---|---|
| `dead-versions` | 24 | 20 |
| `named-probe` | 20 | 17 |
| `released-cost` | 34 | 31 |
| `gc-predates` | 152 | 86 |
| `released-rows` | 331 | 207 |

The five plants spawn 561 times without held answers and 361 times with them, 36 % fewer. On the same (PINNED, 2026-11-26)
box, at that time, one `git --version` spawn took 0.21 to 0.68 s, so spawns account for most of each (PINNED, 2026-11-26)
plant's wall. The two large plants carry most of the saving. The three small ones are held too, so one
rule covers the build's five. With the scratch copy in place each plant exited 0, and its printed lines
matched the run without it once the scratch path was replaced.

One round of the five, each plant run without and then with the scratch copy, back to back under a
gauge of 0.21 to 0.23 s per spawn, summed 223.6 s without and 157.7 s with, a ratio of 0.71. The wall (PINNED, 2026-11-26)
is noisy: two of the small plants ran slower with the copy than without it. The spawn counts are the
stable measure.

**What this does not reach.** The brief's target is the five plants at about 40 s on a quiet node, from
about 84 s, a ratio near 0.48. This unit measures near 0.71, so on its own it leaves the five near 60 s
quiet. Under the load of the 521 s reading it would leave the leg near 400 s, still over its 300 s (PINNED, 2026-11-26)
ceiling. The remaining gap is wall time spent on reads that are not held, and only running the plants
side by side shortens that: "Alternatives rejected" below measures a pool near 0.49 on its own. That
is the hand-off of section 3, and AC8 is the reading that shows whether it is owed.

### Mechanism

1. `derive_held_key(repo, args)` returns `(str(repo), args)` in two cases, and `None` otherwise.
   - `args` is `("rev-parse", "--git-common-dir")` or `("rev-parse", "--show-toplevel")`, and a `.git`
     entry stands at `repo`. With no `.git` there, the read is not held, so a removed worktree, or a
     path below a worktree's top, still asks git.
   - `args[0]` is `rev-parse` or `ls-tree`, and another element of `args` is a full 40-hex object id,
     alone or followed by `^{tree}`. A full id names one object, so the answer is fixed.
2. `read_held_git(repo, *args)` derives the key. With no key it calls the real reader. With a key it
   returns the stored answer, or calls the real reader and stores what it returns. A reader that raises
   stores nothing, so a failed read, such as the all-zero sha of `gc-predates` steps 7 and 8, asks git
   again each time.
3. `set_git_held()` is a `contextlib.contextmanager`. It saves `ti.read_git_stdout` and `ti.git`, sets
   both to one `read_held_git` over a dictionary the block owns, and in its `finally` sets both back.
4. `run_fixture` enters `set_git_held()` beside `set_env_aside(GIT_ENV_LEAKS)` when `plant` is in
   `HELD_PLANTS`, and enters `contextlib.nullcontext()` otherwise. The store therefore lives for one
   plant run, and its keys carry the repository path.

`tools/memory-tree/deviation_join.py#set_env_aside` is the house shape for a block that holds a
process-wide value and puts it back in its `finally`, and `run_fixture` already enters it.

### What it cannot see

- A plant that rewrites a worktree's `.git` entry in place. Its `--show-toplevel` answer would then be
  stale while the entry stands. None of the five does this.
- An object deleted from the store while the plant runs. No plant runs `git gc` or `git prune`;
  `git worktree prune` removes worktree records and no objects.
- A read that is not held. `worktree list`, `HEAD^{tree}`, `diff` and every fixture write still start a
  process each, so the plants still cost what those reads cost.

### Inventory

Two functions, `derive_held_key` and `read_held_git`, and one context manager, `set_git_held`. On
2026-11-26 `python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for each,
leading with `derive`, `read` and `set`. One constant, `HELD_PLANTS`; `py.constant` is no declared cell.

### Migration

`tools/playbook/gov_tag.py` is in the import closure of `instruction_units.py`, as printed by
`import_walk.derive_module_closure` on 2026-11-26. This edit therefore re-versions the
`instruction_units:extract_unit` and `instruction_units:extract_repo` extractors, and each node
re-parses their rows at its next check. Unit 10's edit of the same file re-versioned the same two
extractors, and its AC9 line measured that re-parse at 24 blobs. This unit pays the same re-parse once (PINNED, 2026-11-26)
more and does not measure it again. No schema, row or file name moves.

### Rollout

Live at landing. The held answers exist only inside a `--fixture` run of the five plants.

### Files touched (estimate)

- `tools/playbook/gov_tag.py`
- `memory/map/generated/symbols.json`, regenerated by the codebase-map generator's `--write` for the
  three new functions
- the unit's acceptance ledger under `memory/builds/aPrunedIndex/build/`, one line per criterion, with
  AC7's readings
- by the main loop at the close: `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/ceiling-evidence.txt`

### Alternatives rejected

- A cache inside `tag_index.py` of `derive_index_path` or `read_git`. The brief's cut-line refuses it,
  because an edit there forces a full re-parse on every node.
- One connection held across a plant's counts. The profile attributed the cost of an open to its
  `--git-common-dir` spawn, 37 s of 69 opens in `released-rows`. The held answer removes that spawn for (PINNED, 2026-11-26)
  every open, the verbs' own opens included, which a held connection does not reach.
- Fewer verb runs, by merging steps. Each `check_step` of `released-rows` rebuilds and then reads what
  the sweep would clear. That build is the act the step asserts on, so two merged steps observe one state
  where the plant observed two.
- One built fixture reused across steps or plants. The steps already share one fixture inside each
  plant. Across plants, `build_tags_fixture` costs five spawns, its `init`, `config`, `add`, `commit` and
  `rev-parse`, under 2 % of `released-rows`. A shared fixture would let one plant's rows reach another's (PINNED, 2026-11-26)
  verdict.
- A bounded pool in `run_selftest`. It shortens the leg's wall and leaves each plant's cost as it is,
  where the owner asked for cheaper plants. It is a second mechanism in another file, so it is the
  hand-off of section 3, not this unit's. A scratch pool of four workers ran the five plants without
  held answers in 109.3 s, the wall of `released-rows` alone. Just before it the same five had summed (PINNED, 2026-11-26)
  223.6 s one after another, so the pool's ratio is near 0.49. The gauge read 0.21 s before the pool and (PINNED, 2026-11-26)
  0.34 s after it. The four workers follow `tools/govkit/selftest.py@daac944b:21214`, which runs the docs
  leg's plants under `ThreadPoolExecutor(max_workers=4)` and reads them back in row order.

## 5. Production-readiness checklist

- security: no new write path, grant or input. Every held key is built from arguments the code already
  passes to git.
- perf / scale: the store holds one answer per key for one plant run. The largest is one
  `ls-tree -r` of a fixture tree.
- error / empty / loading states: a failed read is never stored, so it fails each time, as today.
- observability: no printed line changes. The spawn counts in section 4 are the observation.
- risks: a held answer that goes stale would move a step's counts. Section 4's rule holds only answers
  a full id or a standing worktree fixes, and AC5 compares every printed line before and after.
- testing: AC2 and AC3 probe the rule and the store, AC5 the plants' lines, and AC6 the recorded breaks.
- migration: the `instruction_units` re-parse of section 4, accepted.
- user docs: N/A — no verb, flag or printed line changes, and `help/tags.md` makes no cost claim.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant <plant>` runs for each of
  `dead-versions`, `named-probe`, `released-rows`, `released-cost` and `gc-predates`, each exits 0. Each
  prints the line its row of `tag_bundle.SELFTEST_ROWS` names.
  Red when: a held answer goes stale, so a step's count moves, the step prints `FAILED` and the plant
  exits 1.
- **AC2** — When a `python -c` probe imports `gov_tag` from `tools/playbook` and calls `derive_held_key`
  with this repository's top for each of eight reads, it prints
  `[True, False, False, False, True, True, False, False]`, where `True` means a key came back. The reads
  are `rev-parse --git-common-dir`, the same read at `tools/`, `rev-parse HEAD^{tree}`,
  `worktree list --porcelain`, `ls-tree --full-tree --name-only <id> -- x`, `rev-parse <id>^{tree}`,
  `diff --name-only HEAD` and `hash-object <id>`. Each `<id>` is the output of
  `git rev-parse HEAD`.
  Red when: the rule holds `HEAD^{tree}` or the worktree listing, whose answers move inside a plant, or
  holds `--git-common-dir` where no `.git` entry stands.
- **AC3** — When a `python -c` probe counts `subprocess.Popen` calls inside `with gov_tag.set_git_held():`,
  `ti.read_git` of the all-zero sha followed by `^{tree}` raises `TagError` twice and spawns twice. Then
  `rev-parse <id>^{tree}` for `git rev-parse HEAD`'s id returns one answer twice and spawns once. After
  the block, `ti.read_git_stdout` and `ti.git` are the functions they were before it.
  Red when: a failure is stored, so the second failing read spawns nothing, or the readers outlive the
  block.
- **AC4** — When the AC3 probe's spawn count wraps `gov_tag.main(["--fixture", "--plant", "gc-predates"])`,
  it prints at most 90 spawns, from 152, and for `released-rows` at most 210, from 331. For the
  `rebuild` plant, outside the five, it prints 32, as before the edit.
  Red when: `run_fixture` skips `set_git_held()` for a plant of `HELD_PLANTS`, so the count stays at
  152, or enters it for every plant, so `rebuild` drops below 32.
  figure: the before counts are PINNED at `f963331d`, on 2026-11-26. They are the same on each run.
- **AC5** — When the builder runs each of the five plants once before the edit and once after, and
  replaces each run's scratch directory path with one token, `diff` of the two outputs prints nothing.
  Red when: a held answer changes any printed count or line, so a step prints other numbers than before.
  cost: two runs of the five, about five minutes on a loaded node.
- **AC6** — When the main loop, at the close, re-stages each break that a `seen-red` line of the build's
  acceptance ledgers records for the five plants, `python tools/playbook/gov_tag.py --fixture --plant <plant>`
  exits 1 under each break and 0 with it removed. The ledger records one `seen-red` line per plant.
  Red when: the held answers mask a break, so its plant exits 0 under it.
  permission: a staged break is the main loop's to stage and record, at the close.
  fixture: the lines in the ledgers of units 1 to 4 name 26 breaks, and unit 10's two lines name 2. The (PINNED, 2026-11-26)
  brief counts 27 for the first group. The main loop re-stages what the lines name, and records the count
  it staged.
- **AC7** — When the builder times the five plants three times before the edit and three times after,
  back to back on one box, the ledger records each run's wall. Beside each it records a load gauge: the
  mean wall of 20 `git --version` spawns, taken just before the reading. The ledger also records the sum
  of the five walls per round, and that sum after over before.
  Red when: the fastest round after is not faster than the slowest round before, so the change is lost
  inside the spread.
  cost: six rounds of the five plants, ten to fifteen minutes.
  figure: the walls and gauges are PINNED when measured, in the ledger.
- **AC8** — When the main loop times `python tools/playbook/tag_bundle.py --selftest` alone three times at
  the close, with the AC7 gauge beside each, each reading exits 0 and stays under the leg's 300 s `ceiling`
  in `tools/gate-legs.json`. The budget row is rewritten by hand as 1.5 times the worst reading, floored
  at 60, naming the readings and their gauges. It must not exceed the 159 it reads today. The evidence (PINNED, 2026-11-26)
  row is written by `python tools/run-gates/derive-ceilings.py --write --observed`.
  Red when: the worst reading exceeds 106 s, so the budget row would move up, or a reading reaches the (PINNED, 2026-11-26)
  ceiling. Either red is the hand-off of section 3.
  permission: a pass runs no self-test leg, so these readings are the main loop's, at the close.
  figure: DERIVED at observation time.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `instruction units selftest` · `lexicon naming predicates` · `tags bundle selftest` · `playbook render selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The line is unit 10's section 6 line, for the same files. Of it, the four legs that open the live index,
`tags (the resolver's checks)`, `instruction edits (manifest checks)`,
`edges (every declared edge parses, is registered and resolves)` and `instruction units selftest`, are
owed at the close once the owner's go holds, and by no pass before it.

New arm: tools/playbook/tag_bundle.py · covers AC6 · the `dead-versions` row, re-observed under the held answers; staged red by each break its `seen-red` line names · none
New arm: tools/playbook/tag_bundle.py · covers AC6 · the `named-probe` row, re-observed under the held answers; staged red by each break its two `seen-red` lines name · none
New arm: tools/playbook/tag_bundle.py · covers AC6 · the `released-rows` row, re-observed under the held answers; staged red by each break its `seen-red` line names · none
New arm: tools/playbook/tag_bundle.py · covers AC6 · the `released-cost` row, re-observed under the held answers; staged red by each break its `seen-red` line names · none
New arm: tools/playbook/tag_bundle.py · covers AC6 · the `gc-predates` row, re-observed under the held answers; staged red by each break its three `seen-red` lines name · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-26 · initial draft.

## 10. Reuse audit

The seam extended is `tools/playbook/gov_tag.py#run_fixture`, which already holds a process-wide value
for a plant's block through `tools/memory-tree/deviation_join.py#set_env_aside`; the held answers are a
second such block beside it. The probe
`python tools/codebase-map/reuse_lookup.py "hold a per-worktree git answer constant across a fixture plant so each index open spawns no git"`
ranked generic git readers: `git`, `run_git`, `read_git` and `read_git_output`. Each starts a process
per call and none holds an answer, so no existing seam stores a git answer. The recall answered this
unit's brief first, then round 1's closing review on the five plants' serial cost, then
`PLAY-dOrderedCharter-25`, the leg's origin. The candidates tested and rejected are under section 4's
"Alternatives rejected": the memo of `derive_index_path` alone cut `gc-predates` from 152 spawns to (PINNED, 2026-11-26)
116, and S1's rule cut it to 86, so the narrower memo lost.
Recall terms used: tag plant fixture selftest ceiling spawn load_index derive_index_path budget leg concurrency
