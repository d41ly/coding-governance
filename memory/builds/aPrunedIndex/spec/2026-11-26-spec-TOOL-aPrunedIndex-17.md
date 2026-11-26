# TOOL-aPrunedIndex-17 — the five tag plants hold the git answers that cannot change while they run

**Status:** CLOSED · rev-4 · 2026-11-26 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md](../build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md) | journal | — |
| [2026-11-26-build-TOOL-aPrunedIndex-17-deviation-1.md](../build/2026-11-26-build-TOOL-aPrunedIndex-17-deviation-1.md) | deviation | — |
| [2026-11-26-prompt-TOOL-aPrunedIndex-17-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-1-spec-brief.md) | research | TOOL-aPrunedIndex-10 |
| [2026-11-26-prompt-TOOL-aPrunedIndex-17-2-revision.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-2-revision.md) | research | — |
| [2026-11-26-prompt-TOOL-aPrunedIndex-17-4-spec-writer.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-4-spec-writer.md) | journal | — |
| [2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md) | research | TOOL-aPrunedIndex-20 |
| [2026-11-26-prompt-TOOL-aPrunedIndex-20-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-20-1-spec-brief.md) | research | TOOL-aPrunedIndex-20 |
| [2026-11-26-prompt-TOOL-aPrunedIndex-24-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-24-1-spec-brief.md) | research | TOOL-aPrunedIndex-24 |
| [2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3.md) | diff-review | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-20 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 |
| [2026-11-26-review-TOOL-aPrunedIndex-17-20-spec-audit-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-17-20-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-20 |
| [2026-11-26-review-TOOL-aPrunedIndex-17-spec-audit-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-17-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The `tags bundle selftest` leg passed in 521 s at `22c3e175d`, over its 159 s budget row and its 300 s (PINNED, 2026-11-26)
ceiling, and round 2 of the closing review owns that as id 1. The owner's answer was "Make plants
cheaper". The five plants this build added spend most of their wall starting git processes, and many
of those processes ask git a question whose answer cannot change while the plant runs. After this unit
those five plants answer such a question once and reuse the answer. Every verdict they give stays
the same.

This unit delivers fewer spawns in those five plants and nothing more. It does not merge verb runs, and
it does not promise that `tags bundle selftest` fits its ceiling under load: section 4 measures it short
of that, AC8 reads the leg at the close, and the rest is `TOOL-aPrunedIndex-20`'s pool, which section
3 hands off to. The build README's row 6 is stated to match.

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
- **S5** — The builder times three interleaved A/B pairs of the five plants on the one built tree. A
  is the built code with `HELD_PLANTS` emptied and B is the code as built, and a load gauge stands
  beside each run. Observed by AC7.
- **S6** — The main loop re-times the leg at the close, on the parent of the unit's build commit and
  on the build commit itself, each in its own detached worktree. When AC8 is green it lowers that
  leg's node-a row of `tools/run-gates/ceiling-evidence.txt` to the worst reading after, through
  `--reset` with `--observed`, because the file is monotone and a plain `--observed` at or under its
  stored maximum is refused. The `--reset` takes the leg's non-ok rows out of the retained run files
  before any refusal. A retained ok reading at or above the worst reading after makes the call refuse
  with its MONOTONE line, and the evidence row then keeps its value from before the call. The
  `tags bundle selftest` row of `tools/run-gates/selftest-budgets.txt` is then derived from the
  evidence row as the call leaves it. Neither row moves up. When AC8 is red it writes neither row.
  Observed by AC8.

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
  mechanism, in another file, and it is `TOOL-aPrunedIndex-20`, handed off below.
- Moving any ceiling or budget up. The leg's 300 s `ceiling` in `tools/gate-legs.json` keeps its value.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py`, which other sessions are landing.
- Any `gov_tag.py` verb outside `--fixture` in a pass. Every pass observation runs in a fixture's own
  scratch repository or is a `python -c` probe that opens no index.

### Edges

- **consumes-from** external — the five plants and the staged breaks the build's acceptance ledgers
  record for them. Units built and closed earlier in this build wrote both. A closed spec is frozen
  and declares no edge back.
- **hands-off** `TOOL-aPrunedIndex-20` — the bounded pool over the leg's plants in
  `tools/playbook/tag_bundle.py#run_selftest`. Section 4 measures this unit alone short of the brief's
  target. AC8's readings at the close stand in this unit's ledger, and unit 20's AC5 runs after them.
  Unit 20 builds after this unit's build commit, because both write the same generated map and the
  same two run-gates rows.

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
| `rebuild`, outside the five | 32 | not held |

The five plants spawn 561 times without held answers and 361 times with them, 36 % fewer. On the same (PINNED, 2026-11-26)
box, at that time, one `git --version` spawn took 0.21 to 0.68 s, so spawns account for most of each (PINNED, 2026-11-26)
plant's wall. The two large plants carry most of the saving. The three small ones are held too, so one
rule covers the build's five. With the scratch copy in place each plant exited 0, and its printed lines
matched the run without it once AC5's normaliser replaced the scratch path.

One round of the five, each plant run without and then with the scratch copy, back to back under a
gauge of 0.21 to 0.23 s per spawn, summed 223.6 s without and 157.7 s with, a ratio of 0.71. The wall (PINNED, 2026-11-26)
is noisy: two of the small plants ran slower with the copy than without it. The spawn counts are the
stable measure.

**What this does not reach.** The brief's target is the five plants at about 40 s on a quiet node, from
about 84 s, a ratio near 0.48. This unit measures near 0.71, so on its own it leaves the five near 60 s
quiet. Under the load of the 521 s reading it would leave the leg near 400 s, still over its 300 s (PINNED, 2026-11-26)
ceiling. The remaining gap is wall time spent on reads that are not held, and only running the plants
side by side shortens that: "Alternatives rejected" below measures a pool near 0.49 on its own. That
pool is `TOOL-aPrunedIndex-20`, the hand-off of section 3, and AC8's readings stand in the ledger beside
it.

### Mechanism

1. `derive_held_key(repo, args)` returns `(str(repo), args)` in two cases, and `None` otherwise.
   - `args` is `("rev-parse", "--git-common-dir")` or `("rev-parse", "--show-toplevel")`, and a `.git`
     entry stands at `repo`. With no `.git` there, the read is not held, so a removed worktree, or a
     path below a worktree's top, still asks git.
   - `args[0]` is `rev-parse` or `ls-tree`, exactly one later element is a full 40-hex object id, alone
     or followed by `^{tree}`, and it is the only revision argument. Every other element is a flag from
     `--full-tree`, `--name-only`, `-r`, `-z` and `--`, or a path after `--`. A full id names one
     object, so the answer is fixed. A read with any other element, such as `rev-parse <id> HEAD`, is
     not held, because part of its answer moves. The rule is an allow-list of every element, and the
     reads today's callers make, in `tools/playbook/tag_index.py#read_worktree_trees` and
     `tools/playbook/tag_index.py#read_live_versions` among them, each fall inside it.
2. `read_held_git(repo, *args)` derives the key. With no key it calls the real reader. With a key it
   returns the stored answer, or calls the real reader and stores what it returns. A reader that raises
   stores nothing, so a failed read, such as the all-zero sha of `gc-predates` steps 7 and 8, asks git
   again each time.
3. `set_git_held()` is a `contextlib.contextmanager`. It binds one `read_held_git` over a dictionary the
   block owns, then enters `unittest.mock.patch.object(ti, "read_git_stdout", held)` and
   `unittest.mock.patch.object(ti, "git", held)` around its `yield`, so both readers are put back on
   every exit. That is the swap `tools/loop/guard.py@c55c8905:805` makes for a block.
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
- by the main loop at the close, on AC8's green only: `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/ceiling-evidence.txt`. On AC8's red neither file is touched.

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
  where the owner asked for cheaper plants. It is a second mechanism in another file, so it is
  `TOOL-aPrunedIndex-20`, the hand-off of section 3, not this unit's. A scratch pool of four workers
  ran the five plants without held answers in 109.3 s, the wall of `released-rows` alone. Just before it the same five had summed (PINNED, 2026-11-26)
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
  a full id or a standing worktree fixes, and AC5 compares every printed line before and after. AC8's
  `--reset` at the close deletes the leg's non-ok rows from the retained run files under
  `<git-dir>/gate-run/` before any refusal, on its MONOTONE path too.
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
  with this repository's top for each of eleven reads, it prints
  `[True, False, True, False, False, False, True, True, False, False, False]`, where `True` means a key
  came back. The reads are `rev-parse --git-common-dir`, the same read at `tools/`,
  `rev-parse --show-toplevel`, the same read at `tools/`, `rev-parse HEAD^{tree}`,
  `worktree list --porcelain`, `ls-tree --full-tree --name-only <id> -- x`, `rev-parse <id>^{tree}`,
  `diff --name-only HEAD`, `hash-object <id>` and `rev-parse <id> HEAD`. Each `<id>` is the output of
  `git rev-parse HEAD`.
  Red when: the rule holds `HEAD^{tree}` or the worktree listing, whose answers move inside a plant,
  holds `--git-common-dir` or `--show-toplevel` where no `.git` entry stands, drops either of them
  where one does, or holds `rev-parse <id> HEAD`, which mixes a full id with a moving ref.
- **AC3** — When a `python -c` probe counts `subprocess.Popen` calls inside `with gov_tag.set_git_held():`,
  `ti.read_git` of the all-zero sha followed by `^{tree}` raises `TagError` twice and spawns twice. Then
  `rev-parse <id>^{tree}` for `git rev-parse HEAD`'s id returns one answer twice and spawns once. After
  the block, `ti.read_git_stdout` and `ti.git` are the functions they were before it.
  Red when: a failure is stored, so the second failing read spawns nothing, or the readers outlive the
  block.
- **AC4** — When a `python -c` probe prints `set(gov_tag.HELD_PLANTS) == {"dead-versions",
  "named-probe", "released-rows", "released-cost", "gc-predates"}` and
  `set(gov_tag.HELD_PLANTS) <= set(gov_tag.PLANTS)`, both print `True`. When the AC3 probe's spawn
  count wraps `gov_tag.main(["--fixture", "--plant", <plant>])` for each of the five, it prints at most
  these bounds: `dead-versions` 20, from 24, `named-probe` 17, from 20, `released-cost` 31, from 34,
  `gc-predates` 90, from 152, and `released-rows` 210, from 331. The first three are section 4's 'with'
  column. The last two are deliberate slack over its 86 and 207, because the scratch copy that counted
  those is not the built code. For the `rebuild` plant,
  outside the five, it prints 32, as before the edit.
  Red when: either set probe prints `False`, any of the five plants' counts stays at its 'without'
  value because `run_fixture` skips `set_git_held()` for it, or `run_fixture` enters it for every plant,
  so `rebuild` drops below 32.
  figure: the before counts are PINNED at `f963331d`, on 2026-11-26. They are the same on each run.
- **AC5** — When the builder runs each of the five plants once before the edit and once after, and
  passes each line of each run's stdout and stderr through one normaliser,
  `re.sub(r'(?i)[a-z]:[\\/].*?[\\/]gt[a-z0-9_]+', '<SCRATCH>', line)`, `diff` of the two outputs
  prints nothing. The normaliser is needed because `run_fixture` in `tools/playbook/gov_tag.py` makes the
  scratch top with `tempfile.mkdtemp(prefix="gt")`, whose suffix is random on every run, and
  `derive_worktree_key` in `tools/playbook/tag_index.py` prints it with forward slashes and a lower-cased
  drive letter. Before the edit the builder confirms the normaliser: two pre-edit runs of `gc-predates`
  already diff empty through it.
  Red when: a held answer changes any printed count or line, so a step prints other numbers than before.
  cost: two runs of the five, about 6.5 minutes at a 0.21 s gauge, from section 4's 223.6 s and 157.7 s;
  it scales with the gauge.
- **AC6** — When the main loop, at the close, re-stages each break that a `seen-red` line of the build's
  acceptance ledgers records for the five plants, `python tools/playbook/gov_tag.py --fixture --plant <plant>`
  exits 1 under each break and 0 with it removed. The ledgers hold eight `seen-red` lines for the
  five: one each for `dead-versions`, `released-rows` and `released-cost`, two for `named-probe` and
  three for `gc-predates`, as section 7's arms state.
  Red when: the held answers mask a break, so its plant exits 0 under it.
  permission: a staged break is the main loop's to stage and record, at the close.
  fixture: the lines in the ledgers of units 1 to 4 name 26 breaks, and unit 10's two lines name 2. The (PINNED, 2026-11-26)
  brief counts 27 for the first group. The main loop re-stages what the lines name, and records the count
  it staged.
- **AC7** — When the builder times three interleaved A/B pairs of the five-plant set on the one built
  tree, the ledger records each run's wall. Each run is
  `python -c "import sys; sys.path.insert(0, 'tools/playbook'); import gov_tag; <A only: gov_tag.HELD_PLANTS = ()>; sys.exit(gov_tag.main(['--fixture', '--plant', '<plant>']))"`,
  so A is the built code with `HELD_PLANTS` emptied and B is the code as built. Inside a pair each
  plant runs its A and its B back to back, A first in pairs 1 and 3 and B first in pair 2, so a drift
  in load lands on both halves of a plant's reading. Beside each run the ledger records a load gauge:
  the mean wall of 20 `git --version` spawns, taken just before the run. It also records each pair's
  five-wall sums for A and for B, and that pair's B over A.
  Red when: a pair's B sum is not below its own A sum, or the median of the three B over A ratios is
  above 0.85. The bound sits above section 4's 0.71 round for the five and the builder's interleaved
  probe of `gc-predates` alone near 0.56, on node a on 2026-11-26, so a correct build clears it under (PINNED, 2026-11-26)
  the noise that round showed. It sits below 1.0, where a no-op build's ratio centres, and a
  no-op passes the first condition alone with probability 1/8 for three pairs.
  The wall is noisy and AC4's spawn counts remain the stable measure; AC7 only shows the saving
  reaches the wall.
  cost: three pairs of the five plants, about 19 minutes at a 0.21 s gauge, three times section 4's
  381 s round; it scales with the gauge.
  figure: the walls and gauges are PINNED when measured, in the ledger.
- **AC8** — When the main loop, at the close, times `python tools/playbook/tag_bundle.py --selftest`
  alone three times on the tree before the edit and three times on the built tree, back to back in one
  session, with the AC7 gauge beside each, the ledger records the six readings and the six gauges.
  Both trees are detached worktrees pinned by commit, each removed after. The tree before the edit is at
  the parent of the unit's build commit, under `"$TEMP/pi17-base"`. The built tree is at the unit's
  build commit itself, under `"$TEMP/pi17-after"`, so no later commit at the tip reaches either
  reading, `TOOL-aPrunedIndex-20`'s pool among them. AC8 is green when all four hold: every reading
  exits 0 and stays under the leg's 300 s `ceiling` in `tools/gate-legs.json`; the largest of the six gauges is at most
  1.5 times the smallest; the worst reading after over the worst reading before is at most 0.90; and
  the worst reading after is at most 106 s, so the budget row cannot pass the 159 it reads today. (PINNED, 2026-11-26)
  A set whose gauges fall outside that band is retaken, at most twice, and a third such set is red.
  On green, the evidence row is written by one call:
  `GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --reset 'tags bundle selftest' --observed 'tags bundle selftest=<worst after>' --how '<the three readings after and their gauges>'`.
  Before anything else, on every path, the call's `--reset` deletes this leg's non-ok rows from the
  retained run files under `<git-dir>/gate-run/`, through its `remove_reset_rows`, defined at
  `tools/run-gates/derive-ceilings.py@b8c1709f:314` and called at
  `tools/run-gates/derive-ceilings.py@b8c1709f:548`. It then re-derives the leg's row from the
  retained ok readings, whose maximum is R. Where no such reading exists, or R is below the worst after,
  the observed reading lands and the node-a row reads `<worst after>`. Like every `--write`, the call
  then also re-derives the other legs' rows, and the ledger records the file's diff. Where R is at or
  above the worst after, the call exits 1 with its MONOTONE line
  (`tools/run-gates/derive-ceilings.py@b8c1709f:601`) before it writes the evidence file. That file is
  then unchanged, and the node-a row keeps its value from before the call, 106.0 today. (PINNED, 2026-11-26)
  Next the budget value is derived as 1.5 times the node-a row as the call leaves it, floored at 60. It
  is tested against 159 first, and only then written to the budget row by hand, naming the readings
  and their gauges. A value above 159 can arise only on the MONOTONE path, where the evidence file was
  not written. It is red, and the budget row is not written either.
  On red, the main loop writes neither row and records the readings, the gauges and the failed
  condition in the ledger. `TOOL-aPrunedIndex-20` already exists, so no unit is opened: its AC5 runs
  after this criterion and reads the ledger beside its own readings.
  Red when: a reading exits non-zero or reaches the ceiling, the gauges stay out of band, the ratio
  exceeds 0.90, or the worst reading after exceeds 106 s. On green, also red when the call exits (PINNED, 2026-11-26)
  non-zero with no MONOTONE line, when the call printed no MONOTONE line and the leg's node-a row
  afterwards does not read `<worst after>`, when it printed one and `tools/run-gates/ceiling-evidence.txt`
  differs from its bytes before the call, or when the budget value exceeds 159.
  fixture: before the call, the main loop checks the MONOTONE path in a fixture repository under
  `"$TEMP/pi17-fx"` holding copies of `tools/run-gates/` and `tools/gate-legs.json`. The copy matters
  because `EVIDENCE` resolves beside the script (`tools/run-gates/derive-ceilings.py@b8c1709f:80`). Its
  retained run files hold an ok reading of this leg at or above the observed value and one non-ok row,
  and the spelled call runs on the copy. The call must exit 1, leave the copy's evidence file byte for
  byte unchanged, and leave no non-ok row of the leg in the run files.
  permission: a pass runs no self-test leg, so these readings and both writes are the main loop's, at
  the close.
  cost: six readings of the leg. At a 0.21 s gauge, section 4's sums for the five plants put them at no
  less than 3 times 223.6 s before and 3 times 157.7 s after, about 19 minutes, plus the eight `bundle-*`
  plants, which nothing here has timed. The cost scales with the gauge. At that gauge a reading after is
  at least 157.7 s, so the 106 s bound is reachable only at a gauge near or under 0.14 s, which is 0.21
  times 106 over 157.7. The 106 s row at `tools/run-gates/ceiling-evidence.txt@a8ce27b0:149` records no (PINNED, 2026-11-26)
  gauge.
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
- rev-2 · 2026-11-26 · §1 §2 §4 §6 §10 S6 AC2 AC4 AC5 AC7 AC8 · folded
  `2026-11-26-review-TOOL-aPrunedIndex-17-spec-audit-round1`: findings 1, 6, 9 and 12 (AC8's evidence
  write spelled in full as `--reset` with `--observed`, so the monotone refusal cannot fire on the green
  path, and S6 says the row is lowered; lowering is taken because it keeps S6's own promise, where
  leaving the row would narrow it), 4 and 13 (AC4 asserts `HELD_PLANTS` equals the five and sits in
  `PLANTS`, and bounds all five counts; the `rebuild` row joins section 4's table), 2 (AC7 reds when
  the spreads overlap, with a no-op's pass probability), 3 (AC8 compares before and after in one
  session, inside a gauge band, at a ratio of at most 0.90), 14 (AC8 and S6 state what is written on
  red: neither row), 5 (section 1 says what the unit delivers, and the README's row 6 is restated), 7
  (AC5 names its normaliser and proves it on two pre-edit runs), 8 (AC5's and AC7's costs from section
  4's pinned sums), 11 (section 10 cites the two prior reader swaps and the grep that found them), 15
  (the hold key is an allow-list of every element, with a ninth AC2 read).
- rev-3 · 2026-11-26 · AC7 reworded to interleaved A/B pairs on one tree, after the builder's divergence (two-block rounds red under a 0.041 to 0.324 s gauge swing)
- rev-4 · 2026-11-26 · §1 §2 §3 §4 §5 §6 §10 S5 S6 AC2 AC4 AC6 AC8 · folded
  `2026-11-26-review-TOOL-aPrunedIndex-17-20-spec-audit-round1`: findings 9 and 20 (AC8 and S6 say the
  `--reset` deletes the leg's non-ok run rows before any refusal, the refusal fires at R at or above
  the worst after, a MONOTONE refusal leaves the evidence row at its value before the call, and a
  fixture checks that path), 2 (the budget value derives from the evidence row as the call leaves it
  and is tested against 159 before it is written), 4 and 19 (the pool is `TOOL-aPrunedIndex-20` in §1,
  §3, §4 and AC8, and the hands-off edge names it), 1 (S5 asks for AC7's interleaved pairs, the half
  rev-3 left standing), 21 (AC8's built tree is pinned to the build commit in its own worktree), 10
  (the worktrees spelled `"$TEMP/..."`), 11 (AC8's cost derived from section 4's timed sums, with the
  gauge at which 106 s is reachable), 7 and 12 (AC4's 90 and 210 named as slack over 86 and 207), 6
  (AC2 probes `--show-toplevel`, eleven reads), 8 (AC6 states the eight `seen-red` lines), 16 (S2's
  swap is `patch.object`, after `tools/loop/guard.py`, and §10's grep is widened).

## 10. Reuse audit

The seam extended is `tools/playbook/gov_tag.py#run_fixture`, which already holds a process-wide value
for a plant's block through `tools/memory-tree/deviation_join.py#set_env_aside`; the held answers are a
second such block beside it. The probe
`python tools/codebase-map/reuse_lookup.py "hold a per-worktree git answer constant across a fixture plant so each index open spawns no git"`
ranked generic git readers: `git`, `run_git`, `read_git` and `read_git_output`. Each starts a process
per call and none holds an answer. A grep for assignments to a module's `git`, `read_git` or
`read_git_stdout` attribute, `git grep -nE "^\s*[A-Za-z_]+\.(git|read_git|read_git_stdout) = " -- '*.py'`,
found two prior instances of rebinding a module's git reader for a block. `tools/chain-packet.py#set_reads`
keeps a `cache = {}`, answers `show` reads from it and installs `schedule.git = read_git`; it is a
hyphenated script no module imports by name, and its cache keys one read kind. The `worktree-spelling`
step of `tools/playbook/gov_tag.py#run_plant` swaps `ti.read_git` for one call inside an inline
try/finally that stores nothing. That grep matches assignments only, so it missed the other form.
`git grep -nE "mock\.patch|patch\.object" -- 'tools/*.py'` found `tools/loop/guard.py@c55c8905:805`,
which swaps module attributes for a block with `contextlib.ExitStack` and
`unittest.mock.patch.object`, and the same shape in `tools/loop/budget.py`. S2 takes that precedent:
two `patch.object` swaps around the block, which put both readers back on every exit. The recall answered this
unit's brief first, then round 1's closing review on the five plants' serial cost, then
`PLAY-dOrderedCharter-25`, the leg's origin. The candidates tested and rejected are under section 4's
"Alternatives rejected": the memo of `derive_index_path` alone cut `gc-predates` from 152 spawns to (PINNED, 2026-11-26)
116, and S1's rule cut it to 86, so the narrower memo lost.
Recall terms used: tag plant fixture selftest ceiling spawn load_index derive_index_path budget leg concurrency
