# TOOL-dSafePassage-77 — the closing review's five walk-leg minors: an order matched by its kind, an arm graded by its defect, a dirty tree refused, reds counted per unit

**Status:** DEFERRED · rev-3 · 2026-10-28 · node d · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · closes TOOL-dSafePassage-79 · ratified 2026-10-28

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-prompt-TOOL-dSafePassage-76-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-76-spec-brief.md) | research | TOOL-dSafePassage-76 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build confirmed ten mediums and five lows. This unit is the batch of
the five in the `upgrade-walk` leg (BUILD-METHOD M4): M6 (id 14), M7 (id 16), M8 (id 17), M10
(id 20) and L4 (id 18), each at the fix the review's skeptic judged sound. Today the leg can print
green for an order it never saw, an arm red for a reason unrelated to its defect, and an engine edit
it never ran, and its summary can count a negative number of passes. Its write set is the leg and
its fixtures, apart from the engine batch TOOL-dSafePassage-76; §8 F2 names the one page both touch.

## 2. Scope (IN)

- **S1** — M6, an `ordered` plant is matched by its order's kind. Each `[[plant]]` with
  `expect = "ordered"` in `tools/govkit/fixtures/release-0/plants.toml` (`:95-107`) carries `order`,
  the order kind gov writes for it, §4's table. An `ordered` row with no `order` is a `Stop` when the
  rows are read.
  `check_plant_rows` (`tools/govkit/upgrade_walk.py:473-515`) reads `ordered` where
  `<tree>/.governance/outbox/<render_row_order_key(order, path)>.md` is a file, the name gov's one
  order writer uses (`tools/govkit/govkit.py:9290-9295`), and no longer where the path appears in any
  outbox text (`:478-479`, `:483`). The file's header comment (`:8-9`) says so. Observed by AC1 and
  AC7.
- **S2** — M7, an arm is caught only by its own defect. Each `[[arm]]` row of
  `tools/govkit/fixtures/release-0/arms.toml` carries `needle`, the text its case's red must hold,
  §4's table; a row with none is a `Stop` when the rows are read. `check_arm_caught(rows, got, want,
  lines)` is true where `got == want` and every `needle` of the set's rows appears in one of
  `lines`, the case's reds or, for exit 2, the `Stop`'s message. `run_case_arms` (`:813-836`) grades
  each set by it in place of `got == want` (`:826-834`), and a set caught for another reason prints
  `arm <names> · <case> · red, but no red names <needle>` and is a red. Observed by AC2 and AC8.
- **S3** — M8, the leg refuses a tree it would not run. `check_tree_clean(gov_root, own)` returns the
  paths `git status --porcelain --untracked-files=no` lists outside `own`, the files the leg reads
  from the working tree: `tools/govkit/upgrade_walk.py`, `tools/govkit/fixture_target.py` and
  `tools/govkit/fixtures/release-0/`. `main` (`:875`), on every run but `--list`, calls it before
  `build_release_tree` (`:911`) and raises `Stop` (exit 2) with
  `the working tree differs from HEAD at <paths>, and the walk runs HEAD's committed bytes; commit
  or stash them`. Observed by AC3 and AC5.
- **S4** — M10, the summary counts units. `render_case_counts(per_case)` renders each case as
  `<case> <n - u> passed <u> red`, where `u` counts the units that redded: the row id for a per-step
  case and the plant id for `plants`, each the second ` · ` field of a red line, and the case itself
  for `up`, `down`, `reup` and `shims`. It ends with `red lines <k>`, every red line counted. `main`
  (`:937-950`) keeps each case's red lines beside `n` (`:938`) and prints the summary through it in
  place of `n - k` (`:944`). Observed by AC4.
- **S5** — M10, the hand-off's receiving row. TOOL-dSafePassage-69 §3 handed this summary's
  arithmetic off as "recommended as its own unit" with no row receiving it. The ask row
  TOOL-dSafePassage-79 in `memory/builds/dSafePassage/BACKLOG.md` receives it, carrying §4's text,
  and this unit closes it, its header carrying `closes TOOL-dSafePassage-79`; §8 F1 records who filed
  it. Observed by AC9.
- **S6** — L4, the `missing-plant` arm reaches the real admission path. An injected arm carrying
  `plant` has that plant applied through `write_plant_edits` (`:129-156`) to each case tree
  `build_case_tree` copies from release-0 (`:572-577`), then committed, as release-0's own plants are
  (`:197-198`). So `missing-plant` reaches `write_plant_edits`' own `Stop` (`:144-145`).
  `check_inject` (`:838-847`) validates `--inject` names only, and its own path test (`:844-847`) is
  the duplicate the review names, not kept. Observed by AC6.
- **S7** — The graders' arm. `check_graders()` runs on every invocation, after the arguments parse
  and before anything is measured. It feeds S1, S2, S3 and S4's functions fabricated inputs, prints
  `upgrade-walk: grader · <name> · ok`, or `· RED · <what it saw>`, for `order-kind`, `arm-needle`,
  `tree-clean` and `case-counts`, and exits 1 on any red. Observed by AC1, AC2, AC3 and AC4.
- **S8** — The page. The leg's section of `help/upgrade-steps.md` (`:371-413`) says that a plant is
  ordered when an order of its kind names it, that an arm's case must go red naming its defect, that
  each run checks its own graders first, and that a working tree differing from HEAD outside the
  leg's own files is a fifth exit-2 cause, beside the four `:409-413` lists. Observed by AC10.

## 3. Non-goals (OUT)

- The engine's nine items, M1, M3, M4, M5, M9, L1, L2, L3 and L5. They are TOOL-dSafePassage-76's.
- Snapshotting the working tree into the clone (M8's other option). A `git stash create` commit is
  unreferenced, so the clone cannot fetch it without a ref written into gov's own store.
- Refusing untracked files. A file HEAD does not hold is walked by nobody, so nothing claims it ran,
  and a step reaching one needs a tracked edit, which S3 refuses.
- The `--list` mode's dirty tree. It walks nothing, and govkit selftest runs it over the working tree
  (`tools/govkit/selftest.py:19288`).
- TOOL-dSafePassage-68's hand-off of `check_walk_exit`'s tail. The review's checklist row for unreceived
  hand-offs is not one of this brief's items.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-5's leg, its plants, arms,
cases and summary; TOOL-dSafePassage-9's order writer and `render_row_order_key`; TOOL-dSafePassage-68's
child stand-ins; and TOOL-dSafePassage-69, whose §3 hand-off S5 receives. The edge join counts CLOSED
specs, and a CLOSED spec cannot take the matching `hands-off` line.

## 4. Design

### S1: each ordered plant's kind

| Plant | Path | `order` | gov's writer |
|---|---|---|---|
| `edited-render` (`plants.toml:95-100`) | `.claude/skills/lexicon/SKILL.md` | `render-edited` | `write_row_order` for an edited render (`tools/govkit/govkit.py:10943`) |
| `edited-retired` (`plants.toml:102-107`) | `tools/hooks/README.md` | `retired-edited` | the same writer, for an edited file gov withdrew, under `install.retired-edits = order` |

### S2: each arm's needle

DERIVED from the line each red is printed by, at `83817478f`. The build confirms each against its
arm's run; a needle no run prints is an amendment to this table, with a rev.

| Arm | Case | `needle` | The red that holds it |
|---|---|---|---|
| `witness-first` | kill | `.uw-arm/1-payload` | the re-run skips by the witness the killed up wrote first, so the payload is missing: `the re-run's digest differs from up's at ...` (`:760`) |
| `not-rerunnable` | kill | `.uw-arm/0-lines` | the re-run's up appends a second line (`:760`) |
| `no-op` | skip | `not load-bearing` | `:692` |
| `lossy-down` | down | `.uw-arm/lossy` | `rollback to the pin: the digest differs at ...` (`:608`) |
| `drops-plant` | plants | `engine-edit` | `plants · engine-edit · ...` (`:512`, `:650`) |
| `held-shim`, `drops-shim` | shims | `is gone from the walked target` | `:538` |
| `breaks-isolation` | isolation | `breach` | `<id> · breach · ...` (`:664`) |
| `missing-plant` | up, exit 2 | `is absent at release-0` | `write_plant_edits`' `Stop` (`:145`), after S6 |

The case the review measured is the kill case's `first write undetermined` red (`:724-725`), which
`derive_first_write` raises on an mtime tie between `arm_step.py`'s two writes 50 ms apart
(`tools/govkit/fixtures/release-0/arms/arm_step.py:55`, `:59`). It names the step, not the payload,
so it no longer passes for the arm's defect.

### S4: the unit of each case

| Case | `n` (`:938`) | A unit |
|---|---|---|
| `skip`, `kill`, `fail`, `isolation` | the pool's rows | the row id, the second ` · ` field |
| `plants` | the plants | the plant id, the second ` · ` field |
| `up`, `down`, `reup`, `shims` | 1 | the case: any red reds it |

`up` prints one red per step row against `n = 1`, and `reup` folds `down`'s reds into its own
(`:636`), which is how `n - k` went negative. Under this table both read `0 passed 1 red`.

### S7: the graders' inputs

| Grader | Input | ok when |
|---|---|---|
| `order-kind` | a scratch `git init` tree whose outbox holds only `update-rollback-demo.md`, its text naming `.claude/skills/lexicon/SKILL.md`, and the `edited-render` row | `check_plant_rows` reds it, then reads it `ordered` once `<render_row_order_key("render-edited", path)>.md` is written |
| `arm-needle` | the `witness-first` row with its needle | `check_arm_caught` is false over a `first write undetermined` red, false at `got = 0`, and true over a red naming `.uw-arm/1-payload` |
| `tree-clean` | a scratch repository tracking `tools/govkit/steps.toml` and `tools/govkit/fixtures/release-0/plants.toml` | `check_tree_clean` returns `[]` with `plants.toml` edited or an untracked file added, and `["tools/govkit/steps.toml"]` with `steps.toml` edited |
| `case-counts` | `down` at `n = 1` with two red lines, `kill` at `n = 2` with two red lines on one row | the line holds `down 0 passed 1 red`, `kill 1 passed 1 red` and `red lines 4` |

Each is a pure call or a scratch repository, seconds in all, so it runs on every invocation, the
held leg's included. A grader sharing nothing with release-0 is what lets `--list` observe it.

### S5: the ask row's text

For the row §8 F1 files, `<id>` the id its resolver mints:

```
- <id> · filed 2026-10-28 · THE UPGRADE-WALK LEG'S SUMMARY SUBTRACTS RED LINES FROM A COUNT OF UNITS. TOOL-dSafePassage-69's measured `--case down` run printed `down -1 passed 2 red` (`tools/govkit/upgrade_walk.py:944`), handed off in its §3 as recommended as its own unit, and the closing diff review's M10 (id 20) found no row receiving it · accept the leg's summary prints passed and red per unit, seen red on a whole-tree case with two red lines
- SEV · <id> · LOW · a merge-bar leg's summary can print a negative or overstated pass count, its exit still correct
- DEFERRED · <id> · until TOOL-dSafePassage-77 · filed 2026-10-28; TOOL-dSafePassage-77 S4 builds the per-unit count
```

### Inventory

Minted, each answering OK to `python tools/lexicon/lexicon.py --suggest <name> --as py.function` on
2026-10-28: `check_arm_caught`, `check_tree_clean`, `render_case_counts` and `check_graders`, all in
`tools/govkit/upgrade_walk.py`. The fixture keys `order` on `[[plant]]` and `needle` on `[[arm]]`, the
grader names of S7, and the summary's `red lines` segment. No flag is added, so the `usage.toml`
row `script:tools/govkit/upgrade_walk.py` (`tools/govkit/usage.toml:187-190`) and the page's usage
marker do not move. No `Refusal` site is added: the leg raises its own `Stop`, which
`tools/govkit/refusal_join.py` does not count.

### Migration

None. The fixture files gain keys the leg alone reads.

### Rollout

Live at landing, at order 16. The leg's files are this unit's alone. `help/upgrade-steps.md` is also
TOOL-dSafePassage-76's, so per §8 F2's recommendation this unit builds after 76 by order of dispatch.

### Files touched (estimate)

- `tools/govkit/upgrade_walk.py`
- `tools/govkit/fixtures/release-0/arms.toml`
- `tools/govkit/fixtures/release-0/plants.toml`
- `help/upgrade-steps.md`

### Alternatives rejected

- **The graders as `tools/govkit/selftest.py` checks.** That file is TOOL-dSafePassage-76's write
  set, and a check there runs only when the govkit selftest leg does, not with the leg it grades.
- **A `--selftest` flag.** It moves the usage row and the page's marker for no reading the default
  run does not already give.
- **A per-case counter beside `add_red`.** S4 derives the unit from the red line each case already
  prints, so no second record of the same fact is kept.
- **The order matched by parsing its path line.** The file name is the one spelling gov's writer
  owns (`render_row_order_key`), so S1 asks the same function.

## 5. Production-readiness checklist

- security: no new write path. S3 runs `git status` on gov's own checkout; the graders write only
  under a scratch directory they remove.
- perf / scale: the graders add seconds to a leg that runs over an hour; S3 adds one `git status`.
- error / empty / loading states: a fixture row missing `order` or `needle` is a `Stop`, exit 2,
  naming the row; a dirty tree is a `Stop` naming its paths.
- observability: four grader lines on every run; each arm line names its needle when it misses; the
  summary adds `red lines <k>`.
- risks: S3 makes the leg exit 2 on a local run over uncommitted engine edits, where it printed
  green. That is the finding; the bar already refuses to stamp such a tree
  (`tools/run-gates/run-gates.sh:5701-5703`).
- testing: S7's graders, each staged red, and the arms of §7.
- migration: none.
- user docs: S8's four sentences.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/upgrade_walk.py --list` runs, it prints
  `upgrade-walk: grader · order-kind · ok` and exits 0.
  Red when: `check_plant_rows` still matches the path anywhere in the outbox text, so the held-back
  notice reads `ordered` and the grader prints `RED`.
  cost: the clone `--list` makes, about a minute.
- **AC2** — When the same command runs, it prints `upgrade-walk: grader · arm-needle · ok`.
  Red when: an arm is caught by `got == want` alone, so the `first write undetermined` red passes.
- **AC3** — When the same command runs, it prints `upgrade-walk: grader · tree-clean · ok`.
  Red when: `check_tree_clean` is absent or reads the leg's own fixture files as dirty.
- **AC4** — When the same command runs, it prints `upgrade-walk: grader · case-counts · ok`.
  Red when: the summary still prints `n - k`, so the `down` input reads `-1 passed 2 red`.
- **AC5** — When `python tools/govkit/upgrade_walk.py --case up` runs in a scratch
  `git worktree add` of HEAD whose tracked `tools/govkit/steps.toml` carries one appended blank
  line, it exits 2 printing `upgrade-walk: nothing measured: the working tree differs from HEAD at
  tools/govkit/steps.toml`, before any clone. With that line in
  `tools/govkit/fixtures/release-0/plants.toml` instead, it passes the check and goes on to build
  release-0; `--list` exits 0 in both.
  Red when: the leg walks HEAD's engine and prints its cases over an edit it never ran.
- **AC6** — When `python tools/govkit/upgrade_walk.py --case up --inject missing-plant` runs, it exits
  2 printing a `Stop` line that opens `plant missing-plant:`, names the arm's planted path, the
  file arms.toml declares at `:59`, and ends `is absent at release-0`, and
  `git grep -c -F "is absent at release-0" -- tools/govkit/upgrade_walk.py` prints `1`, the one
  `Stop` in `write_plant_edits`.
  Red when: the arm's plant is tested by a second existence check rather than joining
  `write_plant_edits`, so the grep counts 2.
  cost: release-0 is applied before the first case tree, several minutes.
- **AC7** — When `python tools/govkit/upgrade_walk.py --case plants` runs, it exits 0 printing
  `plants · edited-render · ordered` and `plants · edited-retired · ordered`.
  Red when: an `ordered` plant's `order` names a kind gov does not write for it, so the order file is
  absent and the plant reds.
  cost: one walk to the tip over release-0, tens of minutes.
- **AC8** — When each arm's case runs with that arm injected, as
  `python tools/govkit/upgrade_walk.py --case kill --inject witness-first` does for the first, it
  exits with the row's exit, 1 or 2, and prints a red, or for exit 2 the `Stop`, holding the row's
  `needle`, for every row of §4's needle table.
  Red when: a row's `needle` is text its case never prints, so the leg's arm pass would read that
  arm uncaught.
  cost: one case per arm over release-0, several minutes to tens of minutes each.
- **AC9** — When `git grep -n -F "THE UPGRADE-WALK LEG'S SUMMARY SUBTRACTS RED LINES FROM A COUNT OF UNITS" -- memory/builds/dSafePassage/BACKLOG.md`
  runs, it prints the ask row, and its `DEFERRED` line names `until TOOL-dSafePassage-77`.
  Red when: TOOL-dSafePassage-69's hand-off still has no receiving row.
- **AC10** — When `git grep -n -F -e "an order of its kind" -e "naming its defect" -e "checks its own graders" -e "differs from HEAD" -- help/upgrade-steps.md`
  runs, it prints one line per phrase.
  Red when: the leg's section still says a plant is ordered when any order names it, or its exit-2 list
  (`:410-412`) omits the dirty tree.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/upgrade_walk.py · covers AC1 AC2 AC3 AC4 · `check_graders`, run first on every invocation, each grader staged red by a working copy carrying today's code: the outbox substring match, `got == want` grading, no clean check, and `n - k` · none
New arm: tools/govkit/fixtures/release-0/arms.toml · covers AC6 AC8 · every `[[arm]]` row's `needle`, graded by `check_arm_caught` in the leg's arm pass, and `missing-plant` reaching `write_plant_edits`, staged red by a needle naming text its case never prints · none

AC5 and AC7 run the leg's own cases; AC9 and AC10 are greps.

## 8. Open questions

- **F1 — Who files S5's ask row, under which id, and how does this unit close it?**
  (a) The main loop mints the id when it commits this spec, files §4's three lines in
  `memory/builds/dSafePassage/BACKLOG.md`, and adds `closes <id>` to this header in a rev-2 of the
  same commit. A fan-out child never mints (`memory/HYGIENE.md`, "Ids"), so this writer could not.
  (b) The build pass files it. The builder is a dispatched child, so the id is still the main loop's
  to mint, and the hand-off stays untracked until the build.
  (c) No ask row: this spec's §9 names TOOL-dSafePassage-69's hand-off as received here. It departs
  from the brief, which names an ask row.
  Recommendation: (a). It tracks the hand-off from the commit that specs its fix, the id is minted
  by the one party allowed to, and the `closes` verb makes this unit's CLOSED flip close the ask.
  RESOLVED (agent, 2026-10-28, delegated): (a), the main loop mints the id and files the M10 ask row
  when it commits this spec; it filed TOOL-dSafePassage-79 and added `closes TOOL-dSafePassage-79`
  to this header.
- **F2 — S8's page is in TOOL-dSafePassage-76's write set. How do the two units share it?**
  (a) This unit writes the leg's section (`help/upgrade-steps.md:371-413`) and builds after 76 by
  order of dispatch, as M6 sequences two passes whose write sets intersect.
  (b) TOOL-dSafePassage-76 takes S8's four sentences into its own S9, so the leg's write set stays
  disjoint and the two build in parallel. 76 would then document a change it does not build.
  (c) No page change. The `[docs]` rule refuses it: the page would list three exit-2 causes and
  match any order, and its exit-2 list would miss the dirty tree.
  Recommendation: (a). The page sentences belong to the change they describe, and both units sit at
  order 16, so sequencing costs no reordering. The brief drew the write sets before the page was
  found to describe the leg's exits and its plant rule.
  RESOLVED (agent, 2026-10-28, delegated): (a), this unit writes the leg's help section and builds
  after TOOL-dSafePassage-76.

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft: the walk-leg batch of the closing diff review,
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`,
  items M6, M7, M8, M10 and L4 (ids 14, 16, 17, 20 and 18), by
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-76-1-spec-writer.md`.
  Lines re-read at `83817478f`: the review's `build_release_tree` at `:162-216` starts at `:159`, and
  its `write_plant_edits` at `:128-153` is `:129-156`.
- rev-2 · 2026-10-28 · §8 · F1 resolved to (a), the main loop filing the M10 ask row at commit, and
  F2 to (a), this unit writing the leg's help section after TOOL-dSafePassage-76, delegated by the
  coordinator.
- rev-3 · 2026-10-28 · S5 · AC6 · §8 · S5 and F1's resolution name the ask TOOL-dSafePassage-79 the
  main loop filed, with the header's `closes`; AC6's planted path is spelled out of backticks for the
  spec-token checker.

## 10. Reuse audit

Each item extends the leg function the review names. S1 asks `render_row_order_key`
(`tools/govkit/govkit.py:9290`), gov's one spelling of an order's name, through `load_engine`
(`tools/govkit/upgrade_walk.py:82-87`). S2 extends `run_case_arms` (`:813`) and the arm rows
`read_arm_rows` reads (`:125`). S3 reuses the leg's `run_git` (`:62`). S4 reads the red lines
`run_walk_case` (`:562`) already returns. S6 routes the arm's plant through `write_plant_edits`
(`:129`), the function release-0's plants take. `python tools/codebase-map/reuse_lookup.py "upgrade-walk leg grades an arm's red by the defect it names and counts reds per unit in its summary"`
ranked `counts`, `arm`, `legs`, `leg`, `walk` and `units`, shell-test name-token matches, then
`run_arms` (`tools/lib/lib-selftest.sh`) and `run_plant_arms` (`tools/memory-tree/deviation_join.py`),
other kits' arm runners with no needle and no per-unit count, so no existing seam fits beyond the
leg's own functions. The recall probe ranked TOOL-dSafePassage-5's spec, the review's L4 and
TOOL-dSafePassage-5's ledger, which records the whole leg as longer than a role agent's command
bound, so AC8 runs each arm's case alone.

Recall terms used: `python tools/memory-recall/query.py "how does the upgrade-walk leg grade its arms plants and summary counts" --terms "upgrade-walk leg arm needle plants ordered summary passed red dirty tree clone HEAD missing-plant"`
