# TOOL-dSafePassage-30 — the step contract's config check reads every repository git can enter from the target, its submodules included

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-30-deviation-76.md](../build/2026-10-23-build-TOOL-dSafePassage-30-deviation-76.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 38** at HIGH, its item **D-3**. TOOL-dSafePassage-24 S1 reads only the target's
own `local` and `worktree` config. A populated submodule's config, at `.git/modules/<name>/config`,
can declare the same executors, and git run in the superproject runs them, because `git status`
recurses into the submodule. The report's skeptic reproduced it with the system and global scopes
off: the superproject's `git config --list --show-scope --includes` printed no `filter` key, and a
plain `git -C sup status --porcelain` ran a submodule's `filter.canary.clean`. A target with such a
submodule passes `check_target_local_config`, and a step that runs `git status` or `git diff` runs
adopter code while the contract reads isolated. This unit is id 38's promotion, the report's first
fix: the check enumerates every repository git can enter from the target and refuses on the same
key table in each.

## 2. Scope (IN)

- **S1** — The population. `read_target_repositories(target)` in `tools/govkit/upgrade_steps.py`
  returns the git directory of every repository a git command run in the target can enter:
  - the target's own, `git -C <target> rev-parse --absolute-git-dir`;
  - every directory under `<common dir>/modules/` that holds a `config` file, at any depth, the
    absorbed submodules and their nested ones, whether checked out or not;
  - every gitlink of the target's index, `git ls-files -s -z` rows of mode `160000`, whose working
    directory holds a `.git` entry, resolved by `git -C <path> rev-parse --absolute-git-dir`, and the
    same walk run over that repository's own index.
  Each directory is listed once, by its resolved path, with the submodule path that reaches it.
  Every git call runs under `build_step_env`'s environment. Observed by AC1, AC2 and AC3.
- **S2** — The read. TOOL-dSafePassage-24's `read_target_local_config` runs its
  `config --list --show-scope --show-origin --includes -z` read as `git --git-dir=<dir>` over each
  directory S1 returns, keeping the `local` and `worktree` rows of each, as it keeps the target's.
  Observed by AC1 and AC3.
- **S3** — The refusal. `check_target_local_config` matches each kept row against the one refused-key
  table, and its refusal names the step id, each key, the file that declares it, and the submodule
  path for a row outside the target's own repository. Observed by AC1 and AC2.
- **S4** — The plants. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `submodule-filter`, an absorbed submodule whose own config sets `filter.canary.clean` and whose
  `.gitattributes` reads `*.txt filter=canary`; `submodule-nested`, the same key one submodule deeper;
  and `submodule-unpopulated`, the key in `.git/modules/<name>/config` of a submodule not checked
  out. Each has a `-stub` that skips the refusal inside the fixture process only.
  Observed by AC1, AC2 and AC3.
- **S5** — The docs. The "What a step can reach" section of `help/upgrade-steps.md` says the check
  reads the config of every repository git can enter from the target, each submodule's included.
  Observed by AC4.

## 3. Non-goals (OUT)

- The key table itself: id 12, `TOOL-dSafePassage-29`, and TOOL-dSafePassage-24's §4.
- Stopping git's recursion with a command-scope `diff.ignoreSubmodules` or `status.submoduleSummary`.
  A step that runs `git -C <submodule>` or `submodule update` enters the repository anyway, so the
  refusal covers what the recursion switch would not.
- Linked worktrees other than the target's own. Git run in the target reads its own `worktree` scope,
  which TOOL-dSafePassage-24 S1 already keeps, and never another worktree's.

### Edges

- **consumes-from** `TOOL-dSafePassage-24` — `read_target_local_config`, `check_target_local_config` and the isolation plants; without them there is no read to widen

## 4. Design

### Data model

The population row, one per git directory:

```
{"git_dir": "<absolute path>", "reached_by": "" | "<submodule path, / separated, nested joined by />"}
```

The target's own row carries `reached_by` empty. A refusal line for a submodule row reads
`<key> in <file> (submodule <reached_by>)`.

### Why both halves of the population

The `modules/` walk finds every absorbed submodule, populated or not, and a `submodule update` would
populate the second kind and enter it. The gitlink walk finds a submodule cloned before git absorbed
its directory, whose `.git` is a directory inside the working tree and not under `modules/`.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: `read_target_repositories` (cell `py.function`, verb
`read`, OK by `python tools/lexicon/lexicon.py --suggest read_target_repositories --as py.function`
on 2026-10-23); the population row's keys `git_dir` and `reached_by`; the plants `submodule-filter`,
`submodule-nested`, `submodule-unpopulated` and their three `-stub` twins. No conf key, gate leg or
policy key. The refusal is TOOL-dSafePassage-24's one `raise Refusal` site, so
`tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 4, after TOOL-dSafePassage-24 (order 3). It shares
`tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with `TOOL-dSafePassage-29` at the same
order, so the build run sequences the two passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **`git submodule foreach --recursive`.** It runs a command inside each submodule, and only in the
  populated ones, so it reaches fewer repositories by a spawning route.
- **The recursion switches alone** (§3).

## 5. Production-readiness checklist

- security: the repository scope is closed over every repository git can enter from the target,
  deny by default on the one table.
- perf / scale: one `ls-files` and one `config` read per repository found; a target with no
  submodule pays one `rev-parse` and an empty directory listing.
- error / empty / loading states: a `git` call of S1 that fails is a refusal naming it, never an empty
  population; the target's own repository is always the first row, so the population is never empty.
- observability: the refusal names the submodule path beside the key and its file.
- risks: an adopter whose submodule declares an LFS filter has every step refused until an operator
  runs it attended; the refusal names the submodule, and the help page says so.
- testing: the three plants and their stubs, through §7.
- migration: none.
- user docs: the "What a step can reach" section of `help/upgrade-steps.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-filter`
  runs, the step whose up runs `git status --porcelain` in the superproject is refused before any
  spawn, naming `filter.canary.clean`, the submodule's config file and its path, the canary is absent,
  and the run exits 1; `--plant submodule-filter-stub` lets the step spawn and exits 1 naming the
  canary.
  Red when: the check reads the superproject alone and the submodule's filter runs.
  fixture: a scratch superproject and submodule under `%TEMP%`, with `GIT_CONFIG_NOSYSTEM=1` and
  `GIT_CONFIG_GLOBAL` the null device, as the report's reproduction ran.
- **AC2** — When the same family runs with `--plant submodule-nested`, the step is refused naming the
  nested path joined by `/`; `submodule-nested-stub` exits 1 naming its canary.
  Red when: the walk stops one level down.
- **AC3** — When the same family runs with `--plant submodule-unpopulated`, the step is refused naming
  the key in `.git/modules/<name>/config`.
  Red when: a submodule that is not checked out is skipped.
- **AC4** — When `git grep -n -i "submodule" -- help/upgrade-steps.md` runs, the "What a step can
  reach" section says the check reads each submodule's config.
  Red when: the page says the check reads the target's repository alone.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the self-test calls `upgrade_steps.py fixture isolation` with the three submodule plants, each failing case staged by its `-stub` twin · none

What the check does not cover: a repository the step itself creates or clones after it spawns, which
no read before the spawn can see.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 38 (HIGH, item D-3).

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-24's `read_target_local_config`, specced and unbuilt at the
base, whose read this unit runs once per repository. `python tools/codebase-map/reuse_lookup.py
"enumerate submodule git directories of a repository"` ranked `git`, `run_git`, `read_git_output` and
`build_git_env`, generic git spawners, and none enumerates submodules, so no existing seam fits beyond
that unit's spec.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
