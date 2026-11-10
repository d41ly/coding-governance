# PLAY-dOrderedCharter-69 — a playbook fixture sets the caller's git variables aside before its first git call

**Status:** CLOSED · rev-1 · 2026-11-08 · node d · Tier-2 · base de8d2d3a1 · streams playbook · order 17 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 |
| [2026-11-05-build-PLAY-dOrderedCharter-69-ledger.md](../build/2026-11-05-build-PLAY-dOrderedCharter-69-ledger.md) | journal | — |
| [2026-11-08-build-PLAY-dOrderedCharter-69-1-builder-return.md](../build/2026-11-08-build-PLAY-dOrderedCharter-69-1-builder-return.md) | journal | — |
| [2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief.md](../prompts/2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief.md) | research | PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-70 |
| [2026-11-05-prompt-PLAY-dOrderedCharter-69-build-brief.md](../prompts/2026-11-05-prompt-PLAY-dOrderedCharter-69-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes H3 and M17 of the closing diff review, one class with one fix shape. Under an inherited `GIT_DIR`,
`tools/playbook/instruction_units.py#run_fixture` re-initialises the real repository and flips `core.bare` in the
config every worktree shares, and the `--fixture` path of `tools/playbook/gov_tag.py` unlinks and rewrites the real
`index.db`. Each now sets `GIT_ENV_LEAKS` aside, as `tools/playbook/instructions_edit.py#run_fixture` already does,
and an arm run in a disposable repository proves it. The third fixture of the shape, in
`tools/playbook/edge_grammar.py`, takes the same fix.

## 2. Scope (IN)

Every line below was read at `62c5f0c5c`, whose `tools/` and `skills/` equal base `de8d2d3a1`.

- **S1** — H3. The body of `tools/playbook/instruction_units.py#run_fixture` runs inside
  `set_env_aside(GIT_ENV_LEAKS)`. It calls `load_memory_tree_path` before importing `deviation_join` and `tree_lib`,
  the skeptic's corrected fix. `run_git` stays as it is. Observed by AC1 and AC2.
- **S2** — M17. The whole of the `--fixture` path, `tools/playbook/gov_tag.py#run_fixture`, runs inside the same block,
  after `ti.load_memory_tree`, so every in-process `tools/playbook/tag_index.py` git call resolves the scratch
  repository. Observed by AC3.
- **S3** — The same block around `tools/playbook/edge_grammar.py#run_fixture`. The report does not name it. Its
  resolve plants reach `ti.load_index` through `read_tag_rows`, so an inherited `GIT_DIR` writes the outer `index.db`
  the way M17 does. Observed by AC4.
- **S4** — The H3 arm: a plant `git-env` in `tools/playbook/instruction_units.py#PLANTS`. Observed by AC1 and AC2.
- **S5** — The M17 arm: a plant `git-env` in `tools/playbook/gov_tag.py#PLANTS`, with one row in the tag plant table
  of `tools/playbook/adopt-playbook.sh`. It spawns the S3 fixture too. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- **`run_git`-only scrubbing.** The report's skeptic ruled it unsound: `tools/playbook/instruction_units.py#load_resolver`
  reaches `tag_index` git calls that `run_git` never sees.
- **A scrub inside `tools/playbook/tag_index.py#read_git_stdout`.** It is on the live path, and the class record warns
  against unsetting these names for a reader that may read them on purpose. The report fixes the fixtures.
- **`tools/playbook/core.py#run_fixture`.** `run_fixture_git` already drops every `GIT_*` name, and no fixture arm there
  opens the tag index.
- **The live `index.db` the review's probe replaced.** See the Edges below.

### Edges

- **hands-off** external — the main loop runs `python tools/playbook/gov_tag.py --rebuild`, the action the report owes
  outside the fixes, because the file its probe replaced is a shared derived cache and a role agent runs no check

## 4. Design

### The block

Each fixture takes the shape `tools/playbook/instructions_edit.py#run_fixture` already holds:

```python
def run_fixture(plant=None) -> tuple[list, int]:
    load_memory_tree_path()
    from deviation_join import set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    out, failed = [], 0
    for name in [plant] if plant else list(PLANTS):
        top = pathlib.Path(tempfile.mkdtemp(prefix="ladder-fx-"))
        try:
            with set_env_aside(GIT_ENV_LEAKS):
                run_git(top, "init", "-q")
                ...
```

`tools/playbook/gov_tag.py#run_fixture` wraps its `build_tags_fixture` and `run_plant` calls, inside the plant-name
check, and `tools/playbook/edge_grammar.py#run_fixture` wraps its plant branch. `set_env_aside` restores what it
held in its `finally`, so a caller of either function is left as it was.

### The arms

Each plant builds its disposable repository under the fixture's own temp directory, so the outer repository the leak
would reach is itself scratch. Nothing here names this repository, and no probe here exports a path into it.

`instruction_units.py fixture --plant git-env`, in `arm_git_env(c)`:

1. Commit one file in `c.top`, and `git worktree add` a linked worktree beside it.
2. Write sentinel bytes to `<c.top>/.git/gov/index.db`.
3. Spawn `[sys.executable, __file__, "fixture", "--plant", "statements"]` with `cwd` the linked worktree and `GIT_DIR`
   its absolute git dir, read by `rev-parse --absolute-git-dir`. `statements` is the plant that opens the tag index,
   through `load_resolver`. Once the block holds, that read is this repository's derived index, as the plant's
   every run is, and the child writes no config.
4. Check three things: the child exits 0, `git -C <c.top> config core.bare` prints `false`, and the sentinel bytes are
   unchanged.

`gov_tag.py --fixture --plant git-env`, in a `run_plant` branch of its own, does the same over the plant's `root`,
with two children under the one exported `GIT_DIR`: `gov_tag.py --fixture --plant two-versions`, the review's own
probe, and `edge_grammar.py --fixture --plant resolve-tag`. It prints
`tags: plant git-env · both children green, core.bare false, the outer index unchanged`, and returns 1 otherwise.

Before S1, the first child flips `core.bare` in the disposable repository and exits 1 with
`fatal: this operation must be run in a work tree`. Before S2, the second exits 2 and replaces the sentinel. That is
each arm's failing case, and it never leaves the temp directory.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `arm_git_env` | Python function | `py.function`, a fixture arm of `instruction_units.py` |
| `git-env` | a plant name in two tables | none |

### Migration

None. Fixture code only.

### Rollout

Live at landing.

### Files touched (estimate)

- `tools/playbook/instruction_units.py`: S1, S4. Unit 70 touches it too, for M1 and M5.
- `tools/playbook/gov_tag.py`: S2, S5. Units 68 and 70 touch it too.
- `tools/playbook/edge_grammar.py`: S3
- `tools/playbook/adopt-playbook.sh`: S5. Units 68 and 70 add rows to it too.

The overlap is the findings' own, and each edit lands at a different symbol. The passes run one after another.

### Alternatives rejected

- **Exporting `GIT_DIR` from a suite against a clone of this repository.** The plant's scratch repository is smaller,
  needs no clone, and cannot reach this one by a typo in a path.
- **A leg that bans an unwrapped fixture.** The class needs a reader of what a fixture calls, and the report's gate is
  the arm.

## 5. Production-readiness checklist

- security: the fix narrows a write surface: a fixture can no longer write `.git/config` or `index.db` outside its
  temp directory. No new input.
- perf / scale: each plant adds one or two child fixtures, seconds each. `statements` reads the warm index.
- error / empty / loading states: a child's exit and its output print in the plant's failure line.
- observability: each plant names the three facts it checked.
- risks: a plant that relied on an inherited `GIT_*` name now sees none. None reads one: `tools/playbook/instruction_units.py`
  and `tools/playbook/gov_tag.py` spell no `os.environ["GIT_` read, by `grep` at `62c5f0c5c`.
- testing: S4 and S5, and AC1 to AC4 by a pass. The main loop observes each arm red in a scratch copy with the block
  reverted, and green.
- migration: none (Migration, above).
- user docs: N/A. Fixture internals; no page under `help/` covers them.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/instruction_units.py fixture --plant git-env` runs, it exits 0 and prints
  `fixture · green`, with no `git-env` expectation failed.
  Red when: `run_fixture` reaches `run_git(top, "init", "-q")` with `GIT_DIR` still in the environment. The plant then
  reads `core.bare` as `true` in its disposable repository.
- **AC2** — When `grep -n "set_env_aside(GIT_ENV_LEAKS)" tools/playbook/instruction_units.py` runs, one line prints,
  inside `run_fixture`.
  Red when: the scrub landed in `run_git` alone, the option the report refuses.
- **AC3** — When `python tools/playbook/gov_tag.py --fixture --plant git-env` runs, it exits 0 and prints
  `tags: plant git-env · both children green, core.bare false, the outer index unchanged`.
  Red when: the child's `tag_index` git calls resolve the outer repository, so `remove_index` unlinks the sentinel, or
  the child exits 2 as it did under the review's probe.
- **AC4** — When `grep -n "set_env_aside(GIT_ENV_LEAKS)" tools/playbook/edge_grammar.py tools/playbook/gov_tag.py` runs,
  it prints one line per file, and AC3's plant ran `resolve-tag` as a child.
  Red when: the third fixture still opens the outer index under an inherited `GIT_DIR`, so AC3's sentinel changes.

## 7. Gates

`instruction units selftest` · `tags (the resolver's checks)` · `edges (every declared edge parses, is registered and resolves)` · `playbook render selftest` · `govkit acceptance matrix`

The last two are what the guards join owes `tools/playbook/`, derived by this writer from each leg's `guard` under
`BROAD_LEG_FLOOR` 5. The first three carry no guard, and they are named because they run the code S1 to S3 move.

New arm: tools/playbook/instruction_units.py · covers AC1 · the plant exports `GIT_DIR` at a child fixture over a disposable main-plus-linked-worktree repository · none
New arm: tools/playbook/adopt-playbook.sh · covers AC3 AC4 · one plant row runs `gov_tag.py --fixture --plant git-env`, whose children inherit `GIT_DIR` over a disposable repository · the suite's arm count, if a floor reads it

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-05 · initial draft, by `2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief`, H3 with the skeptic's
  corrected fix and M17, plus the third fixture of the shape, each line read at `62c5f0c5c`.

## 10. Reuse audit

The seam extended is `tools/memory-tree/deviation_join.py#set_env_aside` with `tree_lib.GIT_ENV_LEAKS`, taken as
`tools/playbook/instructions_edit.py#run_fixture` and `tools/memory-tree/build_records.py#run_fixture` already take it.
The class record is `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`. The probe
`python tools/codebase-map/reuse_lookup.py "hold a fixture's git variables aside"` ranked generic `run_git` and
`build_fixture` symbols, and `git grep set_env_aside` found the seam the report names. The recall query returned TOOL-aSealedCaravan-5 and this review. Where
the report and the source disagree: the report names two fixtures and the source holds a third, S3's.

Recall terms used: `python tools/memory-recall/query.py "an inherited GIT_DIR reaches a fixture and acts on the real repository" --terms "GIT_ENV_LEAKS set_env_aside fixture core.bare index.db inherited GIT_DIR linked worktree run_git common_git_dir"`
