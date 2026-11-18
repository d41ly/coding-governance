# TOOL-dDeclaredLoop-116 — the five loop readers left on the memory tree's conf take the records root from `resolve_memory_root`

**Status:** CLOSED · rev-1 · 2026-11-17 · node a · Tier-2 · base 017b0299 · streams tooling · order 53

**Derived:** TOOL-dDeclaredLoop-72

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-117 |
| [2026-11-17-build-TOOL-dDeclaredLoop-1-deviation-1173.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-1-deviation-1173.md) | deviation | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-117 |
| [2026-11-17-build-TOOL-dDeclaredLoop-116-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-116-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-116-deviation-1161.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-116-deviation-1161.md) | deviation | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-116-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-116-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-116-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-116-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-116-spec-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-116-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dDeclaredLoop-72 made `resolve_memory_root` the loop kit's one reader of a build's records root
and left four readers on `.memory-tree.conf` alone, writing that the class is recorded at the close
(its §3 Non-goals, its F4). The closing diff review's round-1 item 2 (HIGH, findings 3 and 4) is that
class, five sites wide: in a tree whose driver conf names `MEMORY_ROOT=records` and whose memory tree's
conf names none, the owner's disposition reads `unrecorded`, the position engine and the parent route
refuse, the upstream record is refused and the actor list grades the wrong folder. This unit routes
every one of the five through `resolve_memory_root` and adds one plant that stages that tree and shows
each reader follow it.

## 2. Scope (IN)

- **S1** — `tools/loop/adapt.py#read_disposition_release` passes `read_records` the conf
  `{"MEMORY_ROOT": resolve_memory_root(root)}` in place of `read_design_conf(root)`, and drops its
  `design_lib` import. `read_records` reads no other key of its conf
  (`tools/memory-tree/build_records.py#read_records`). Observed by AC1, AC6.
  **Readers:** by name: `read_design_conf` stays defined and spelled by `read_builds_dir` in `tools/loop/loop_lib.py` (S5); only this function's import is dropped. by value: `tools/memory-tree/build_records.py#read_records` reads only `MEMORY_ROOT` from the conf it is passed.
- **S2** — `tools/loop/position.py#derive_position_into` takes `root = resolve_memory_root(repo)`
  once, builds `builds` as `repo / root / "builds"`, and passes `read_records` the conf
  `{"MEMORY_ROOT": root}` for the acceptance read, so the README, the run-state file and the
  acceptance records are read under one root. The `read_design_conf` import and the `conf` local are
  dropped, and `resolve_memory_root` joins the module's `loop_lib` import. Observed by AC2, AC6.
  **Readers:** by name: the dropped `conf` local and import have no reader outside `derive_position_into` in `tools/loop/position.py`. by value: `tools/memory-tree/build_records.py#read_records` reads only `MEMORY_ROOT` from the conf it is passed.
- **S3** — `tools/loop/loop_parents.py#read_withdrawn_parents` sets `memory_root` from
  `resolve_memory_root(root)`, so the parents' folders, their `RUN.md` and the remote path
  `refs/remotes/<remote>/<branch>:<root>/builds/<slug>/RUN.md` all follow it. Its `read_design_conf`
  import is dropped, `resolve_memory_root` joins the module's `loop_lib` import, and the module
  docstring's sentence naming `read_design_conf` as the builds folder's source names
  `resolve_memory_root`. Observed by AC3, AC6, AC7.
  **Readers:** by name: the module docstring and the `tools/loop/README.md` paragraph S7 rewrites are the only places that name the old source. by value: `memory_root` is read only inside `tools/loop/loop_parents.py#read_withdrawn_parents`.
- **S4** — `tools/loop/upstream.py#write_upstream_record` sets `memory_root` from
  `resolve_memory_root(root)`, its `read_design_conf` import dropped and `resolve_memory_root` joining
  the module's `loop_lib` import. Observed by AC4, AC6.
  **Readers:** by name: the dropped import has no reader outside `write_upstream_record` in `tools/loop/upstream.py`. by value: `memory_root` is read only inside that function.
- **S5** — `tools/loop/loop_lib.py#read_builds_dir` keeps its `read_design_conf` read for
  `DESIGN_RECORD` and its test first, then takes the root from `resolve_memory_root(root)`; a
  `LookupError` or `ValueError` it raises is answered `(None, str(e))`, so a tree whose two confs name
  two roots prints its `records root:` reason on the `--check` builds line and grades no row (§8 F2).
  Its docstring says so. Observed by AC5, AC6.
- **S6** — The plant `driver-root-readers` joins `PLANTS` in `tools/loop/budget.py`, beside the root
  plants `unattended-root`, `root-source` and `unset-driver-root`, as §4 "The plant" stages it. Its
  description: "the build moved under records, the driver's conf naming MEMORY_ROOT=records and the
  memory tree's conf no root, then each reader of a build's folder: the ending's disposition, the
  position engine's README and acceptance reads, a withdrawn parent, an upstream record and the actor
  list's builds folder, then that folder again with the memory tree's conf naming memory". It runs
  under `--selftest` through `PLANTS`. Observed by AC1, AC2, AC3, AC4, AC5.
- **S7** — The carriers. In `help/loop.md`, the actor-list paragraph of the definition section gains
  one sentence: a tree whose two confs name two records roots prints each row `foreign build, not
  graded` too, its builds line carrying the `records root:` reason; and the "Who owns it" sentence
  saying `--check` reads `DESIGN_RECORD` and `MEMORY_ROOT` through the memory-tree kit's conf reader
  says it reads `DESIGN_RECORD` there and finds the builds folder under the records root the section
  above it states. In `tools/loop/README.md`, the `read_withdrawn_parents` paragraph names
  `resolve_memory_root` as the builds folder's source, and the `read_builds_dir` table row adds a
  records root that does not resolve to its `(None, why)` causes. Observed by AC7.

## 3. Non-goals (OUT)

- No edit to `resolve_memory_root` or `resolve_memory_root_source`: the rule, its `records root:`
  refusal and its driver-conf cache stand as TOOL-dDeclaredLoop-72, 75, 76 and 82 landed them.
- No population-wide rule refusing a builds root read outside `resolve_memory_root` over every
  `tools/loop/*.py` module, round-1 item 2's left-shift gate (§8 F3).
- `tools/loop/loop_transition.py#read_build_headers` keeps its `read_design_conf` call: it reads
  `FAMILIES` there and already takes the root from `resolve_memory_root`.
- No edit to the memory-tree kit. Its record writers, `tools/memory-tree/build_records.py#write_record`
  among them, keep reading `.memory-tree.conf` alone and refuse a build folder they do not find.
- No edit to `derive_conf_openers`, `CONF_ROUTES`, the `conf-readers-declared` plant or `PLANT_OWED`
  in `tools/loop/loop_lib.py`: round-1 items 3 and 4, a later unit's scope.
- No CLOSED spec is edited, TOOL-dDeclaredLoop-72's among them.
- No change to `tools/run-gates/selftest-budgets.txt`, `tools/gate-legs.json` or any registry row
  (§5 "registry, budgets, ceilings and maps").

### Edges

- **consumes-from** external — `resolve_memory_root` and `resolve_memory_root_source` in `tools/loop/loop_lib.py`, landed on the build branch by TOOL-dDeclaredLoop-72, 75, 76 and 82; without them there is no single root to route the five readers through
- **hands-off** external — the population-wide rule of round-1 item 2's left-shift gate, a key-aware predicate over every loop module (§8 F3); an ask the dispatcher files
- **hands-off** external — the memory-tree kit's record writers, which write under `.memory-tree.conf`'s root alone and refuse loudly in a tree only the driver's conf roots; an ask the dispatcher files if the owner wants them on the driver's root

## 4. Design

Every code claim below was read at the build branch's tip, 017b0299f on
`branch/unattended-declared-loop-d56bf0`, through `git show` and `git archive`; this worktree is cut
from `main`, which holds no loop kit.

### The sites

| Site | Today | After |
|---|---|---|
| `tools/loop/adapt.py#read_disposition_release` | `read_records(root, read_design_conf(root), "disposition", ...)` | `read_records(root, {"MEMORY_ROOT": resolve_memory_root(root)}, "disposition", ...)` |
| `tools/loop/position.py#derive_position_into` | `conf = read_design_conf(repo)`; `builds` from `conf.get("MEMORY_ROOT")`; `read_records(repo, conf, "acceptance", ...)` | `root = resolve_memory_root(repo)`; `builds = repo / root / "builds"`; `read_records(repo, {"MEMORY_ROOT": root}, "acceptance", ...)` |
| `tools/loop/loop_parents.py#read_withdrawn_parents` | `memory_root` from `read_design_conf(root).get("MEMORY_ROOT")` | `memory_root = resolve_memory_root(root)` |
| `tools/loop/upstream.py#write_upstream_record` | `memory_root` from `read_design_conf(root).get("MEMORY_ROOT")` | `memory_root = resolve_memory_root(root)` |
| `tools/loop/loop_lib.py#read_builds_dir` | `DESIGN_RECORD` and the root from one `read_design_conf(root)` | `DESIGN_RECORD` from it, then the root from `resolve_memory_root(root)`, its raise answered `(None, why)` |

`adapt.py` already imports `resolve_memory_root` and calls it in `read_run_file` and
`read_fenced_row`; `read_disposition_release` is the one read in that module that did not. The other
three modules import from `loop_lib` at module level, so the name joins that import line.

### Exceptions each caller already handles

`resolve_memory_root` raises `ValueError` opening `records root:` where both confs name a root and the
two differ, a `LoopError` (a `ValueError`) where the driver conf does not source, and `LookupError`
where the memory-tree kit does not resolve (`tools/loop/loop_lib.py#resolve_memory_root_source`).

| Reader | Its caller's handling | What a disagreeing tree prints |
|---|---|---|
| `read_disposition_release` | `tools/loop/budget.py#read_ending` and `tools/loop/breakpoints.py#read_breakpoints` already call `resolve_memory_root` earlier on the same path | the refusal those modules print today, before this read is reached |
| `derive_position_into` | `tools/loop/position.py#derive_position` catches `ValueError` and `LookupError` into `invalid-input` | `invalid-input`, the reason the `records root:` text |
| `read_withdrawn_parents` | `tools/loop/loop_parents.py#main` prints `loop: unanswered · <why>` or `loop: unarmed · <why>`, exit 2 | `loop: unanswered · records root: ...`, exit 2 |
| `write_upstream_record` | `tools/loop/upstream.py#main` catches `ValueError` and `OSError` as `upstream · refused · <why>`, exit 2 | `upstream · refused · records root: ...`, exit 2 |
| `read_builds_dir` | answers `(None, why)` itself (S5) | `loop: actor-list builds · foreign · records root: ...` |

A `LookupError` from `write_upstream_record` is no new path: its first line, `read_memory_tree`,
raises it today for the same missing kit.

### The plant

`driver-root-readers` is one case of `tools/loop/budget.py#run_budget_plant`, over the scratch
`write_budget_plant` builds for it (build `tFix`, unit `TOOL-tFix-1`, the memory tree's conf naming
`memory`). The case:

1. Writes under `memory/builds/`: a `tFix` README whose front matter names `parents: tPar`, in the
   shape `tools/loop/loop_parents.py#write_parent_plant` writes; a `tPar` README; a `tPar` run-state
   file whose run facts read `phase: ABORTED`. Commits one pass for `TOOL-tFix-1`, then writes its
   acceptance record through `write_acceptance(top, FX_BUILD, FX_UNIT, <pass sha>, "stand-in",
   [("true", 0, "0" * 12)], today="2026-01-01")` and the owner's disposition through
   `write_disposition(top, FX_BUILD, FX_UNIT, EXHAUSTED_ITEM, "continue", "terminal")`, as the
   `ending` plant does, and commits. Both writers write under the memory tree's root, which is
   `memory` at this step.
2. Moves the tree as `unattended-root` does: `git mv memory records`, the memory tree's conf rewritten
   to `FAMILIES="tool:TOOL"` alone, the driver's conf `MEMORY_ROOT=records`, `PLANT_RUN` at the build's
   run-state file under `records/`, one commit.
3. Prints one line per reader, `loop: fixture · driver-root-readers · <reader> · <answer>`, and owes
   each answer below. A reader's `ValueError` is printed as its answer, so a miss names the refusal.

| Reader line | Call | Owed | Today's answer, the RED |
|---|---|---|---|
| `ending` | `run_verb(["ending", "--build", FX_BUILD])` | exit 0, the line ending `disposed continue` | `disposed unrecorded` |
| `position` | `derive_position(top, FX_BUILD)` with `GOV_POSITION_STATES` set to `render_handover([(FX_UNIT, "READY")])` for the call | an entry of its `read` opening `records/builds/tFix/README.md@`, and one opening `records/builds/tFix/build/` and naming `-acceptance-` | reason `the slug tFix names no build README under <top>/memory/builds` |
| `parents` | `read_withdrawn_parents(FX_BUILD, top)` | the keys `["tPar"]`, its text holding `phase: ABORTED` | `the build tFix's README does not read: ...` |
| `upstream` | `write_upstream_record(top, FX_BUILD, FX_UNIT, "item.design.unit-spec", ["a line"], today="2026-01-01")` | `records/builds/tFix/build/2026-01-01-build-TOOL-tFix-1-upstream-1.md` | `memory/builds/tFix/ is no build folder of this tree` |
| `builds-dir` | the memory tree's conf gains `DESIGN_RECORD="x"`, then `read_builds_dir(KIT, top)` | `(top / "records" / "builds", "")` | `(top / "memory" / "builds", "")` |
| `builds-dir disagree` | the memory tree's conf gains `MEMORY_ROOT=memory`, then `read_builds_dir(KIT, top)` | `None`, its why opening `records root:` | `(top / "memory" / "builds", "")` |

The `ending` line reads the disposition through its production caller, `read_ending`, which is where
finding 3 printed its wrong verdict. The `position` line owes the acceptance entry as well as the
README entry, so a pass that reroutes the builds path and leaves the `read_records` conf on the memory
tree's root stays red. `GOV_POSITION_STATES` is restored after the call, as the position plants restore
it. The two `builds-dir` steps rewrite the working file without a commit, since both readers read it
from the working tree, and `DESIGN_RECORD` is written only for them, so no other reader sees a
half-set design key.

The imports are local to the case, as the plant code of this module already imports inside its
branches: `read_builds_dir` from `loop_lib`, `read_withdrawn_parents` from `loop_parents`,
`derive_position`, `render_handover` and `HANDOVER` from `position`, `write_upstream_record` from
`upstream`, and `write_acceptance` and `write_disposition` from `build_records` after
`read_memory_tree("build_records.py")`. No import cycle forms: `budget.py` already loads `adapt`,
`loop_parents` and `loop_transition` at module level, the one module importing `budget` at module
level is `termination.py`, which neither `position` nor `upstream` imports, and `loop_transition`
reaches `budget` and `termination` only inside functions.

### Inventory

| Identifier | Kind | Where | Naming |
|---|---|---|---|
| `driver-root-readers` | plant id, a `PLANTS` key | `tools/loop/budget.py` | none |

No function, constant, flag or verb is minted. The conf dict of S1 and S2 is an argument expression,
not a name.

### Files touched (estimate)

- `tools/loop/adapt.py`: `read_disposition_release`
- `tools/loop/position.py`: `derive_position_into` and the `loop_lib` import line
- `tools/loop/loop_parents.py`: `read_withdrawn_parents`, the `loop_lib` import line and the module docstring
- `tools/loop/upstream.py`: `write_upstream_record` and the `loop_lib` import line
- `tools/loop/loop_lib.py`: `read_builds_dir` and its docstring
- `tools/loop/budget.py`: `PLANTS` and `run_budget_plant`
- `tools/loop/README.md`: the `read_withdrawn_parents` paragraph and the `read_builds_dir` table row
- `help/loop.md`: the actor-list paragraph and the "Who owns it" sentence

### Alternatives rejected

- **One plant per owning module (§8 F1 (b)).** Five plants in five `PLANTS` tables, each with its own
  scratch quirks and its own `help/loop.md` plant list, for the same five observations.
- **A probe in the acceptance criteria and no standing arm (§8 F1 (c)).** The defect reached the
  close because no arm staged this tree; a probe run once leaves the next reader of a builds folder
  ungraded again.
- **`read_records` grows a root argument.** It edits the memory-tree kit, another kit with its own
  version, for a value its existing conf argument already carries.
- **A minted helper answering `{"MEMORY_ROOT": resolve_memory_root(tree)}`.** Two call sites of one
  expression with no logic to share; the root reader already is the shared core.
- **`--check` refuses a disagreeing tree (§8 F2 (b)).** A new refusal path and its own arm in
  `tools/loop/loop_lib.py#main`, the function the next unit edits.

## 5. Production-readiness checklist

- security — read-only but for `write_upstream_record`, whose write boundary (slug, unit id, a build
  folder that exists, an exclusive create) is unchanged; only the folder it resolves moves to the
  driver's root, the root the driver itself writes under. No new input, path, command or remote.
- perf / scale — `resolve_memory_root` sources the driver's conf in one bash per process per conf
  content and holds the answer (`tools/loop/loop_lib.py#resolve_memory_root_source`); the position
  engine already pays it through `read_transitions`, and the route and the upstream writer pay it once
  per run. No loop grows.
- error / empty / loading states — a tree with no driver conf answers the memory tree's root or
  `memory`, as before; a tree with both confs agreeing answers the same root as before; a tree whose
  confs disagree refuses in each reader as §4 "Exceptions" tabulates; a tree whose driver conf sets
  no root beside a memory tree naming `records` now refuses in these readers too, as the budget plant
  `unset-driver-root` already owes of the budget's draw.
- observability — none added; the `--check` builds line already prints `foreign` and why.
- risks — the configuration change in the row above is the one behaviour a working tree could see:
  before, these five readers read `records` there while the driver wrote under `memory`; after, they
  refuse naming both confs, as every other loop reader does. Gov's own two confs both name `memory`
  (PINNED at 017b0299), so every answer in this tree keeps its bytes.
- dependency — order 53, after TOOL-dDeclaredLoop-115 (order 52, `tools/loop/guard.py`, round-1
  item 1) and before TOOL-dDeclaredLoop-117 (order 54). That unit edits `tools/loop/loop_lib.py` for
  round-1 items 3 and 4, at `derive_conf_openers` and the plant branch of `main`; this unit edits only
  `read_builds_dir` there, so 117 starts from this unit's landed bytes with no overlapping hunk.
- the sweep — every function the body changes, its callers, fixtures and arms at the tip, and what
  keeps each green:
  - `read_disposition_release`: callers `tools/loop/adapt.py#write_flow_states`,
    `tools/loop/budget.py#read_ending` and `tools/loop/breakpoints.py#read_breakpoints`. Arms: the
    adapt plants `owner-approves` and `loosening` and the budget plant `ending`, each over a scratch
    whose memory tree's conf names `memory` and no driver conf, so the root is unchanged; the
    breakpoints plant `unattended-root` writes no disposition record, so its released lines do not
    move.
  - `derive_position_into`: caller `tools/loop/position.py#derive_position`, called by
    `tools/loop/adapt.py#write_path_orders`, the adapt plant `mid-step` in
    `tools/loop/adapt.py#run_adapt_plant`, `tools/loop/composition.py#run_composition_plant` and the
    position CLI. Arms: every position plant; its
    scratch names `memory` in the memory tree's conf, and the driver plants copy gov's two confs,
    which agree; `steps` still owes its acceptance read under `memory`.
  - `read_withdrawn_parents`: caller `tools/loop/loop_parents.py#derive_parent_route`. Arms: the
    `loop parent routes` plants; `parent-in-extra-phase` writes a driver conf setting only
    `PHASES_EXTRA`, whose unset root reads `memory` beside the memory tree's `memory`, so they agree.
  - `write_upstream_record`: callers `tools/loop/upstream.py#main` and its `record-written` plant,
    whose scratch carries only the memory tree's conf naming `memory`.
  - `read_builds_dir`: caller `tools/loop/loop_lib.py#main` for `--check` and every
    `loop definition fixtures` plant; gov's tree answers `memory/builds` as before, and
    `actor-list-foreign` overrides the answer as before. It builds a conf path in its refusal text and
    opens nothing, so `derive_conf_openers` does not answer it and the `conf-readers-declared` plant's
    pass line keeps its count.
  - the `no-own-conf-read` plants of `budget.py` and `breakpoints.py`: the new case sits inside
    `run_budget_plant`, a definition `derive_fixture_boundary` answers, and calls no `CONF_READERS`
    member, so `derive_conf_reads` over `budget.py` still answers nothing.
  - `PLANTS` in `budget.py`: 33 plants, PINNED at 017b0299, become 34; `run_selftest` derives its
    cases from the dict, so the self-test owes the new plant `held` with no list to edit.
- registry, budgets, ceilings and maps, each the change could newly red and what keeps it green:
  - `.lexicon.conf` `VERB_OFFENDER_PIN`, 1215 at the tip (PINNED 017b0299): no function name is
    minted, so no suggest call is owed and the offender count does not move.
  - `.unattended.conf` `SHARED_RECORDS`: no pass of this unit writes `memory/DECISIONS.md` or
    `memory/project/readme-contract.txt`.
  - `.memory-tree.conf` `REFUSAL_CEILINGS` and `tools/unattended/unattended.families.txt`: they price
    `tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh` alone, neither touched;
    `ARMS_FLOORS` names no `tools/loop` file, so the `harness arms` census reads nothing here.
  - `tools/govkit/usage.toml` and the help anchors: the rows for `budget.py`, `position.py`,
    `loop_parents.py` and `upstream.py` declare flags, and no flag or verb changes; a plant id is not a
    flag, so no usage pin and no help anchor moves.
  - `tools/run-gates/selftest-budgets.txt`, row `loop budget fixtures`: not edited; it grades an
    overrun of its value, 498 (PINNED 017b0299), and the close's reading of the leg decides whether it
    moves.
  - `memory/map/generated/symbols.json`: no symbol added or renamed, and its rows carry no line, so it
    does not move.
  - `memory/guides/SESSION-KICKOFF.md`: its `watch:` line names none of the touched paths, so no
    `last-audit` re-stamp is owed.
  - the kit version marker: `tools/loop/README.md`'s first line is not edited; kit versions are minted
    at landing, as the history's `mint: kit versions` commits show.
  - the commands that re-derive these counts at the close:

    ```
    python tools/lexicon/lexicon.py --offenders
    python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import budget; print(len(budget.PLANTS))"
    git grep -n 'get("MEMORY_ROOT")' -- 'tools/loop/*.py'
    git grep -n "read_disposition_release\|derive_position_into\|read_withdrawn_parents\|write_upstream_record\|read_builds_dir" -- tools help
    ```
- testing — AC1 to AC7; the plant's RED is observed by the main loop before S1 to S5 land (§7).
- migration — none; no record, row or conf shape changes.
- user docs — `help/loop.md`, S7; the loop page's records-root paragraph already states the rule
  these readers now follow, and only the actor-list and "Who owns it" sentences change.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/budget.py --fixture --plant driver-root-readers` runs, its
  `ending` line ends `disposed continue` and the plant closes with its `held` line, exit 0.
  Red when: `read_disposition_release` passes `read_records` the memory tree's conf, and the line
  ends `disposed unrecorded`.
- **AC2** — When the same `--plant driver-root-readers` runs, its `position` line names the read
  entry of the scratch build's README under the `records` root and an entry under that build's
  `build` folder there that names `-acceptance-`.
  Red when: `derive_position_into` builds its builds path from the memory tree's conf, the reason
  naming no build README under `memory/builds`; or passes `read_records` that conf, and no acceptance
  entry is read.
  fixture: the engine's reads before the acceptance read are those its `steps` plant makes over a
  scratch with no policy file and no move; that the budget scratch reaches the acceptance read is
  UNVERIFIED until the plant's first run.
- **AC3** — When the same `--plant driver-root-readers` runs, its `parents` line names `tPar` and the
  read text holds `phase: ABORTED`.
  Red when: `read_withdrawn_parents` reads the memory tree's conf root and refuses, the build's
  README not read.
- **AC4** — When the same `--plant driver-root-readers` runs, its `upstream` line names the record
  §4's table owes, under the `records` root, and that file exists in the scratch.
  Red when: `write_upstream_record` reads the memory tree's conf root and refuses, finding no build
  folder under `memory`.
- **AC5** — When the same `--plant driver-root-readers` runs, its `builds-dir` line names
  `records/builds`, and its `builds-dir disagree` line answers `none` with a why opening
  `records root:`.
  Red when: `read_builds_dir` answers `memory/builds` in either step, or raises out of the plant.
- **AC6** — When `derive_conf_reads` runs over `tools/loop/adapt.py`, `tools/loop/position.py`,
  `tools/loop/loop_parents.py` and `tools/loop/upstream.py`, by the first command below, no module
  answers a `reader call` row; and the second command prints only lines inside
  `resolve_memory_root_source`.
  Red when: any of the four modules still calls `read_design_conf`, or a `MEMORY_ROOT` read outside
  the resolver survives, `read_builds_dir`'s included.
  figure: the tip answers a `reader call` in each of the four modules and six `get("MEMORY_ROOT")`
  lines, PINNED at 017b0299; the close's answer is DERIVED by the two commands.
  ```
  python -I -c "import sys; sys.path.insert(0, 'tools/loop'); from loop_lib import derive_conf_reads; [print(m, derive_conf_reads('tools/loop/' + m)) for m in ('adapt.py', 'position.py', 'loop_parents.py', 'upstream.py')]"
  git grep -n 'get("MEMORY_ROOT")' -- 'tools/loop/*.py'
  ```

- **AC7** — When `git grep -n "resolve_memory_root" -- tools/loop/loop_parents.py tools/loop/README.md`
  runs, the module docstring and the `read_withdrawn_parents` paragraph each name it as the builds
  folder's source, and `git grep -n "records root:" -- help/loop.md` prints the actor-list sentence
  S7 adds.
  Red when: a carrier still says the builds folder comes from `read_design_conf`, or the help page
  says nothing of a disagreeing tree's builds line.

## 7. Gates

`loop budget fixtures` · `loop position fixtures` · `loop parent routes` · `loop upstream fixtures` · `loop adapt fixtures` · `loop breakpoint fixtures` · `loop composition fixtures` · `loop definition` · `loop definition fixtures` · `loop termination` · `loop transition record` · `lexicon naming predicates` · `docs` · `help page commands` · `kit version markers` · `codebase-map coverage + freshness`

New arm: tools/loop/budget.py · covers AC1 AC2 AC3 AC4 AC5 · the plant driver-root-readers run after S6 lands and before S1 to S5, MISSED with one clause per reader · none

What the plant does not check, stated so a green is not read as more. It stages one configuration,
the driver's conf naming `records` beside a memory tree's conf naming none, plus one disagreement for
`read_builds_dir`; the other disagreements and the unset-driver case are graded for the budget's own
reads by the plants beside it, and here only by §4's reasoning. It grades the five readers it names
and no sixth: a loop function written later that builds a builds path from `.memory-tree.conf` is not
seen, which is the population-wide rule §8 F3 hands off. It reads the position engine's `read` entries
and reason, never its answer. It runs each reader in process, so the CLIs' exit codes on a refusal
are §4's table, not an observation.

## 8. Open questions

- **F1 — Where does the standing arm live?** (a) One plant, `driver-root-readers`, in `budget.py`'s
  root family beside `unattended-root`, `root-source` and `unset-driver-root`, calling the five
  readers in process over one scratch; (b) one plant in each owning module's `PLANTS`, five plants,
  each with its own `help/loop.md` plant list; (c) a probe in the acceptance criteria and no standing
  arm. (a) and (b) meet the same criteria; (a) reuses the root family TOOL-dDeclaredLoop-72 seated in
  `budget.py` and touches one table. (c) leaves the next reader ungraded, the way this one reached the
  close. Recommendation (a).
  Rung 3: (a) and (b) satisfy every criterion and the tie breaks on the seam M5 found.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-17, delegated): (a)
- **F2 — What does `read_builds_dir` answer when the two confs disagree?** (a) `(None, why)`, the
  `records root:` text, so `--check` prints `foreign` with that reason and grades no actor row, the
  contract its docstring already gives a missing kit; (b) `--check` refuses and exits non-zero, a new
  refusal path in `tools/loop/loop_lib.py#main` with its own arm. Every reader of a build's records
  refuses in that tree, so a run cannot proceed past it either way; (b) reds the definition leg for a
  fault the definition does not own and edits the function unit 117 edits. Recommendation (a), with
  §7's statement of what it leaves unseen.
  Rung 3: (a) satisfies every criterion with no new refusal arm and no hunk shared with unit 117.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-17, delegated): (a)
- **F3 — Does this unit carry the population-wide rule of round-1 item 2's left-shift gate?** (a) No:
  it is handed off as an ask, a separate mechanism under M2; (b) yes, `derive_conf_reads` run over
  every `tools/loop/*.py` module. The candidate predicate run over the tip still answers in seven
  modules after this unit's reroutes, among them the `read_design_conf` reads of `FAMILIES` in
  `tools/loop/loop_transition.py#read_build_headers` and of `DESIGN_RECORD` in `read_builds_dir`, and
  the driver-conf reads of `tools/loop/loop_table.py`, none of them a root; the rule as written would
  red on each, so (b) needs a key-aware predicate, a new mechanism. Recommendation (a).
  Rung 3: (b) fails the one-mechanism bound; (a) leaves the rule a named follow-up.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-17, delegated): (a)

## 9. Revision log

- rev-1 · 2026-11-17 · initial draft, from the writer's handoff
  2026-11-17-prompt-TOOL-dDeclaredLoop-116-1-spec-writer and the closing diff review's round-1 item 2,
  record 2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.

## 10. Reuse audit

The seam is TOOL-dDeclaredLoop-72's: `tools/loop/loop_lib.py#resolve_memory_root`, the loop kit's one
root reader, which this unit extends to the five readers that unit's §3 left on the memory tree's
conf; and the root plant family it seated in `tools/loop/budget.py#run_budget_plant`, which the new
plant joins. The map probe,
`python tools/codebase-map/reuse_lookup.py "read a build's records root from the driver conf before the memory tree conf in every loop reader"`,
run in this worktree on `main`'s map, which holds no loop kit, ranked name-stem neighbours
(`read_design_conf`, `parse_conf`, `load_conf`) and no loop symbol; the recall probe found
TOOL-dDeclaredLoop-72, which names the resolver and the plants, and TOOL-dDeclaredLoop-76, which names
the `no-own-conf-read` rule F3 weighs.

Recall terms used: `resolve_memory_root resolve_memory_root_source MEMORY_ROOT unattended.conf records-root unattended-root confs-disagree read_design_conf no-own-conf-read loop kit`, against the question "which loop modules read a build's records root and how is the driver conf root resolved".
