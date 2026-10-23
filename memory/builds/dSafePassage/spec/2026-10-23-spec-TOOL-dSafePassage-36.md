# TOOL-dSafePassage-36 — the config check walks the target worktree's own git directory for submodules, so a linked worktree's submodules are graded

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-36-deviation-129.md](../build/2026-10-23-build-TOOL-dSafePassage-36-deviation-129.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-36-deviation-82.md](../build/2026-10-23-build-TOOL-dSafePassage-36-deviation-82.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-37 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-38 TOOL-dSafePassage-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 27 to 35
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`)
confirmed finding **id 8** at HIGH, its item **D-1**. TOOL-dSafePassage-30 S1 walks
`<common dir>/modules/` for absorbed submodules. A linked worktree keeps its submodules' git
directories under its own `$GIT_DIR/modules/`, not under the common directory. This unit's probe on
node d, git 2.54.0.windows.1, 2026-10-23, in a scratch superproject under `%TEMP%` with the system and
global scopes off, read `s/.git` in the linked worktree `wt1` as
`gitdir: ../../sup/.git/worktrees/wt1/modules/s`. `rev-parse --absolute-git-dir` printed
`.../sup/.git/worktrees/wt1` and `--git-common-dir` printed `.../sup/.git`. After
`git submodule deinit -f s` in `wt1`, the submodule's directory held no `.git` entry and
`.../sup/.git/worktrees/wt1/modules/s/config` remained. So a linked-worktree target's unpopulated
submodule is missed by both halves of the population, and a step that runs `submodule update`
enters it and runs its config. Gov's own trees under `.claude/worktrees/` are linked worktrees. This
unit is id 8's promotion: the walk's root is the target's own git directory.

## 2. Scope (IN)

- **S1** — The root. `read_target_repositories` (TOOL-dSafePassage-30 S1) walks
  `<git dir>/modules/`, the directory `git -C <target> rev-parse --absolute-git-dir` prints, at any
  depth, and never `<common dir>/modules/`. In a main worktree the two are one directory, so the
  population there is unchanged; in a linked worktree the walk reads that worktree's own submodules
  and none of the main worktree's. The gitlink half is unchanged, and a submodule both halves reach
  is listed once by its resolved path, as TOOL-dSafePassage-30 S1 says. Observed by AC1 and AC2.
- **S2** — The reason, corrected. TOOL-dSafePassage-30 §4 "Why both halves of the population" is read
  as: the modules walk finds every absorbed submodule of the target's own worktree, populated or not,
  under that worktree's git directory, and a `submodule update` run in the target would populate the
  second kind and enter it. TOOL-dSafePassage-30's built text is not rewritten; its §3 hands-off bullet
  to this unit names the reading. NOT OBSERVED: a reading of another spec's rationale, which no code
  carries.
- **S3** — The plants. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `submodule-unpopulated-worktree`: a linked-worktree target whose own
  `$GIT_DIR/modules/<name>/config` sets `filter.canary.clean`, with the submodule de-initialised in
  that worktree, and a `-stub` twin that skips the refusal inside the fixture process only. It also
  gains `submodule-main-only`: the main worktree's `modules/<name>/config` sets the key, and the
  linked-worktree target's own submodule config does not. Observed by AC1 and AC2.
- **S4** — The docs. The "What a step can reach" section of `help/upgrade-steps.md` says the check
  reads the submodules of the target's own worktree, under its own git directory. Observed by AC3.

## 3. Non-goals (OUT)

- The order in which the population walk runs git commands and grades configs, and the fsmonitor an
  index read can run: finding 27, carried by the minors batch `TOOL-dSafePassage-42`.
- How `reached_by` is spelled for a `modules/` row whose name differs from its path: finding 6, the
  same batch.
- Linked worktrees other than the target, which TOOL-dSafePassage-30 §3 already leaves out; this unit
  makes the walk agree with that non-goal.

### Edges

- **consumes-from** `TOOL-dSafePassage-30` — `read_target_repositories`, its `modules/` walk and the submodule isolation plants; without them there is no walk whose root to correct
- **hands-off** `TOOL-dSafePassage-45` — the `modules/` walk listing a directory as a repository by `git --git-dir=<d> rev-parse --git-dir`, never by a `config` file, and refusing a failed read by name, finding 18 of the spec audit of units 36 to 42
- **hands-off** `TOOL-dSafePassage-47` — the `modules/` walk listing a candidate by git's own directory shape rather than by `rev-parse --git-dir`, and refusing one whose config read fails, finding 9 of the spec audit of units 43 to 46

## 4. Design

### The walk root

```
git_dir = git -C <target> rev-parse --absolute-git-dir      # .../.git, or .../.git/worktrees/<wt>
walk    = every directory under <git_dir>/modules/ holding a `config` file, at any depth
```

Nested submodules of a linked worktree sit under `<git_dir>/modules/<name>/modules/<nested>/`, so the
same walk reaches them. The common directory is not read by this half of the population.

### Inventory

Minted: the plants `submodule-unpopulated-worktree`, its `-stub` twin, and `submodule-main-only`. No
function, conf key, gate leg or policy key. The refusal is TOOL-dSafePassage-24's one `raise Refusal`
site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 5, after TOOL-dSafePassage-30 (order 4), whose walk it corrects.
It shares `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with `TOOL-dSafePassage-37`
and other units at order 5, so the build run sequences those passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Walk both `<git dir>/modules/` and `<common dir>/modules/`.** In a linked worktree the second is
  the main worktree's, which this target never enters, so the check would refuse on keys no step can
  reach.
- **Enumerate submodules with `git submodule status --recursive`.** It reads `.gitmodules` and the
  index, and an index read runs the repository's fsmonitor before any config is graded.

## 5. Production-readiness checklist

- security: closes the linked-worktree half of the repository scope TOOL-dSafePassage-30 claims.
- perf / scale: unchanged; one directory walk, now of the right directory.
- error / empty / loading states: a target with no `modules/` directory under its git directory
  yields only the gitlink half, as today.
- observability: the refusal names the per-worktree config file it read.
- risks: none beyond TOOL-dSafePassage-30's.
- testing: the two plants and the stub, through §7.
- migration: none.
- user docs: the "What a step can reach" section of `help/upgrade-steps.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-unpopulated-worktree`
  runs, the step is refused before any spawn, naming `filter.canary.clean` and the config file under
  `.git/worktrees/<wt>/modules/<name>/`, the canary is absent, and the run exits 1;
  `--plant submodule-unpopulated-worktree-stub` lets the step spawn, its `submodule update` and
  `git status --porcelain` run the filter, and the run exits 1 naming the canary.
  Red when: the walk reads `<common dir>/modules/` and the target's own submodule config is never
  graded.
  fixture: a scratch superproject, its submodule and a linked worktree under a short `%TEMP%` path,
  with `GIT_CONFIG_NOSYSTEM=1` and `GIT_CONFIG_GLOBAL` the null device, as this unit's probe ran.
- **AC2** — When the same family runs with `--plant submodule-main-only`, the linked-worktree target
  is not refused for the main worktree's submodule key, its step spawns and the run exits 0.
  Red when: the walk refuses on a config the target never enters.
- **AC3** — When `git grep -n -i -e "worktree" -e "submodule" -- help/upgrade-steps.md` runs, the
  "What a step can reach" section says the check reads the submodules of the target's own worktree.
  Red when: the page says the check reads the repository's shared modules directory.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the self-test calls `upgrade_steps.py fixture isolation` with the two linked-worktree plants, its failing case staged by the `-stub` twin and by a walk copy rooted at the common directory · none

What the check does not cover: a linked worktree's submodule the step itself initialises from a URL
after it spawns, which no read before the spawn can see.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 27 to 35's id 8
  (HIGH, item D-1).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 36 to 42, written by the disposal stage: `TOOL-dSafePassage-45`; no other section moved.
- rev-3 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 43 to 46, written by the disposal stage: `TOOL-dSafePassage-47`; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-30's `read_target_repositories`, specced and unbuilt at the
base, whose walk root this unit corrects. `python tools/codebase-map/reuse_lookup.py "walk the git
directory of a linked worktree for submodule configs"` ranked `git`, `walk`, `run_git` and `GIT`,
generic spawners and a corpus walker, none of which reads git's per-worktree layout, so no existing
seam fits beyond that unit's spec. Git's layout was read from the probe of §1, not from a record.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's promoted repairs are placed and sequenced after the unit they repair" --terms "spec audit promoted repair unit order edges hands-off consumes-from minors batch disposal rescope"`
