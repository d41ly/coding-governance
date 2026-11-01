# TOOL-dScopedBuild-3 — scope at the push: each commit's routed paths inside its unit's write set, graded by `build.scope`

**Status:** DEFERRED · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 4 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0401@e53987d9 whole
**Carries:** node:item.build.scope
**Carries:** node:record-kind.scope
**Carries:** node:policy-key.build.scope
**Carries:** node:item.build.revert-pass
**Carries:** node:item.build.resolve

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-3-deviation-31.md](../build/2026-11-01-build-TOOL-dScopedBuild-3-deviation-31.md) | deviation | — |
| [2026-11-01-build-TOOL-dScopedBuild-3-deviation-32.md](../build/2026-11-01-build-TOOL-dScopedBuild-3-deviation-32.md) | deviation | — |
| [2026-11-01-build-TOOL-dScopedBuild-3-reuse-scout-b.md](../build/2026-11-01-build-TOOL-dScopedBuild-3-reuse-scout-b.md) | research | TOOL-dScopedBuild-5 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-3-1-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-3-1-reuse-scout.md) | journal | — |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

gap-build-01 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:362`):
scope is not bound to the unit. 120 of 584 unit-attributed product commits touched files outside
their unit's Files touched, and 42 of 582 at kit-directory granularity (PINNED, measured since
2026-10-01, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-build.md:96`).
The push-time leg passes any named id: "whether that unit's scope covers the change is not read"
(`tools/memory-tree/routed_commits.py:32`, its F1). Only an unattended dispatched pass is graded for
scope, at the commit (`check_commit_message`, `tools/unattended/unattended.sh:13510`) and by check 23
(`tools/unattended/check-unattended.sh:4115`); attended work has nothing, and the write gate admits
any `ROUTED_PATHS` write once any routed unit is buildable (`tools/hooks/scratch-guard.js:1191`).

This unit adds the scope arm to the push-time host the owner merged into `build.scope` (NP-22,
`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:687`): every
pushed commit's routed paths must sit inside its named unit's write set at kit-directory grain, for
attended and unattended work alike, graded by `build.scope` (`refuse`, `warn-and-ask`, `report`;
default `warn-and-ask`, `tools/policy/catalogue.toml:980-983`), with the refused stray's route
(`build.revert-pass`), the resolution pass's allowance (`build.resolve`) and the scope report
(`record-kind.scope`) the Build item table states
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:292-293`, :300).

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: `read_first_passes` and
`read_build_base(repo, slug)` in `tools/memory-tree/routed_commits.py` (I1), and the one exit contract
`check_build_exit` in `tools/unattended/unattended.sh` with its attended verb `--build-exit <slug>`
(I2), all TOOL-dScopedBuild-1's (S1, S2, S4, S5); the Python read `read_gate_value(key, repo)` of
`policy.py get` (I4) and the renderer `render_gate_outcome(key, value, findings)` (I5), both in
`routed_commits.py`, the filer `write_gate_asks` in `unattended.sh` (I5), and the Build-exit mode
`routed_commits.py --build <slug>`, all TOOL-dScopedBuild-14's (S1, S2, S5, S6). Shared file the build run sequences: `routed_commits.py`, which units 1, 14,
9 and 8 also write, each at its own order.

- **S1** — The kit-directory reduction, `derive_kit_dir(path)` in `tools/memory-tree/design_lib.py`
  beside `check_guard_trips` (`:589`): a path under `tools/<kit>/` reduces to `tools/<kit>/`, one under
  `skills/<skill>/` to `skills/<skill>/`, any other path holding a `/` to its first segment with a
  trailing `/`, and a root file to itself. It is the rule TOOL-dPlacedRequest-1 S9 states for
  `kit-dirs` (`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md:260-261`),
  written once in Python; the CLI `python design_lib.py --kit-dir <path>...` prints one reduction per
  line so a shell caller reads the same rule. Observed by AC1.
- **S2** — The unit's write set (I7), `read_unit_writes(unit, spec_text, run_rows, tracked)` in
  `routed_commits.py`. Dispatched: the union of the paths on every line `read_pass_declarations`
  (`tools/unattended/lib-unattended.sh:1116`) prints for the unit in its default mode, every key of the
  unit with every row under each, over its build's `RUN.md` and each rotated `RUN.*.md` at HEAD;
  `run_rows` are those lines. The one reader is called and never copied: S8's one `bash` spawn
  sources the library, found by `backlog.resolve_kit_dir("unattended", "lib-unattended.sh", KIT)`,
  and runs it over each run-state blob; where the kit does not resolve, no dispatch row is read. Its
  `current` mode is not read (§8 F8). Attended,
  where no row names it: the words `design_lib.read_spec_writes` returns from its spec, kept when the
  word has two or more real segments or names a tracked file at HEAD. Each kept path is reduced by S1.
  A unit with neither is `undeclared`. Matching is `design_lib.check_guard_trips` alone. Observed by
  AC2 and AC3.
- **S3** — The scope arm, `check_build_scope(repo, conf, read, id_map, value)` in `routed_commits.py`,
  called by `check_routed_commits` after `check_deviation_join` (`:331`). Its population is the RANGE
  half's graded commits: non-merge, on or after `ROUTED_COMMIT_CUTOFF`, touching `ROUTED_PATHS`, and
  naming at least one unit a spec defines, by the union rule of `extract_unit_ids` (`:119`, I8). Each
  routed path such a commit touches is in scope when `check_guard_trips` holds against some reduced
  write-set entry of some unit it names, and a `stray` otherwise. Its lines are prefixed
  `routed-commits: scope`, in §4 "The report". Observed by AC2, AC4 and AC5.
- **S4** — The value. `build.scope` is read once per run as `read_gate_value("build.scope", repo)`,
  the key a string literal at the call, from the landed revision (no `--rev`), so a pushed branch
  cannot loosen its own grading; a `get` refusal is the leg's exit 2, as I4 states. The strays go to
  `render_gate_outcome("build.scope", value, findings)`, one `(subject, accept)` pair per stray unit,
  the subject naming the unit and its stray paths: `refuse` lists each under the FAILED line and its
  rc 1 sets the leg's exit to 1; `warn-and-ask` lists each as an `ask ·` line, which `write_gate_asks`
  files, one ask per pair, at the Build exit (TOOL-dScopedBuild-14 S6, its §8 F2); `report` lists each. Where `backlog.resolve_kit_dir("policy", "policy.py", KIT)` finds no
  policy kit beside this kit, the arm prints one `scope off` line naming that, calls nothing, and
  grades nothing. Observed by AC2 and AC7.
- **S5** — `build.revert-pass`. A refused stray's FAILED line names its remedy: a revert pass on the
  unit, one commit naming the unit that restores each stray path to its content at the stray commit's
  first parent. A stray the unit's own later commits restore passes: a unit's stray path whose blob
  after the unit's newest commit touching it equals its blob at the first parent of the unit's
  oldest commit touching it is listed `reverted`, never `stray`. Observed by AC4.
- **S6** — `build.resolve`. A resolution pass is a commit naming the units it resolves, so its
  allowance is the union of their write sets, by the union rule of S3 with no rule of its own. A merge
  commit's own content stays ungraded, as the leg's docstring states. Observed by AC4.
- **S7** — The Build exit and the scope report. The scope arm joins TOOL-dScopedBuild-14 S5's mode
  `python routed_commits.py --build <slug>`, the one Build-exit mode, and mints none: under it the arm
  grades every unit of the build over its own commits in `<base>..HEAD`, `<base>` the parent of the
  build's oldest first pass, `read_build_base` (I1), by S2 to S6, and the mode exits 1 when the arm
  refuses a stray under `refuse`, as when the deviation half refuses, and 2 on a refusal. A `--write`
  flag on that mode also writes the scope report as a record (§4 "The record"), of the kind `scope`,
  which `RECORD_KIND_TOKENS` (`tools/memory-tree/tree_lib.py:406`) gains. The one call
  `check_build_exit` makes to the mode, inside the function and never in a verb body, gains `--write`,
  so `--build-exit` and `--close` both grade the arm. Observed by AC6 and AC9.
- **S8** — The spawn count. The write sets come from the spec texts the id map's batch already reads
  (`load_spec_paths`, `:189`), the run-state blobs from one `git cat-file --batch` and their dispatch
  lines from one `bash` running `read_pass_declarations` over them, and the revert test
  from one `git cat-file --batch-check`, each spawned only when its query is non-empty. Observed by AC8.
- **S9** — The catalogue row. `build.scope`'s row gains its `summary` and `usage`, and
  `python tools/policy/policy.py lists --write` re-renders `tools/policy/unsummarised-keys.txt` without
  it. Observed by AC7.
- **S10** — The docs: a new page `help/build-scope.md` (what the scope arm grades, its three values,
  the revert pass, `--build <slug>`), its line in `help/README.md`, `build.scope` among the keys with a
  consumer in `help/policy.md`, the `routed_commits.py` row of `tools/memory-tree/README.md`, and the
  docstring's F1 sentence (`routed_commits.py:32`) re-written to say what the scope arm now reads.
  Observed by AC10.
- **S11** — The ask, filed by the main loop: §8 F5's, in dPlacedRequest's `BACKLOG.md`. NOT OBSERVED by
  a criterion: the main loop files it after the writers return, and this unit's build observes its
  row, not its disposition.

## 3. Non-goals (OUT)

- The touch join, `build.scope`'s one check over the unit's hunks: TOOL-dScopedBuild-9. The drain and
  the claim it grades: TOOL-dScopedBuild-8. This unit hands each the per-unit population and write set.
- The write gate, and Bash or PowerShell writes before the commit: TOOL-dScopedBuild-5. This arm is
  the push-time backstop that unit's Non-goals rely on for the main loop's shell writes.
- The deviation gate at the commit and the exit: TOOL-dScopedBuild-14.
- Grading the WHOLE history for scope. The arm grades the pushed range and the Build exit (§8 F2);
  remote CI, which grades WHOLE, reads one `scope` line saying so.
- File granularity (§8 F1), and the unattended kit's `--check-commit` and check 23, which keep grading
  dispatched passes at the commit and the bar as they do.
- The per-pass `build.scope` the executor runs after `build.acceptance`: the executor is
  dWellOiledMachine's; `--build <slug>` is the call it makes.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — `read_first_passes` and `read_build_base`, which give `--build <slug>` its base, and `check_build_exit` behind `--build-exit`, the exit S7 joins; without them the scope arm has no range and no exit host
- **consumes-from** `TOOL-dScopedBuild-14` — `policy.py get`, read through `read_gate_value`, with `render_gate_outcome` and `write_gate_asks`, the one renderer and filer each stray goes to, and `--build`, the one Build-exit mode S7's arm and `--write` join; without them the arm has no value, no outcome and no exit mode
- **hands-off** `TOOL-dScopedBuild-9` — `read_spec_writes`, through `read_unit_writes`, the unit's reduced write set, and the per-unit population of graded commits the touch join runs over
- **hands-off** `TOOL-dScopedBuild-5` — `read_spec_writes`, through `read_unit_writes`, the write set the derived write gate also reads, and the push-time scope arm that backstops the main loop's shell writes
- **hands-off** `TOOL-dScopedBuild-27` — AC2's `warn-and-ask` clause, which that unit's S1 restates as the push writing no `BACKLOG.md` and its S2 as the exit filing the ask (id 3)
- **consumes-from** `TOOL-dScopedBuild-30` — S4's `build.scope` read, spelled `check_gate_value("build.scope", read_policy_value("build.scope", root), <the three values>)`, through the reader that unit makes the kit's one in place of `read_gate_value`; without it the arm reads through a second reader (id 19)
- **consumes-from** `TOOL-dScopedBuild-33` — the precondition `read_first_passes`, which stays in `deviation_join.py`; the scope arm reads its base through `read_build_base`, without which `--build <slug>` has no base (id 30)
- **hands-off** `TOOL-dScopedBuild-34` — S1's `derive_kit_dir` fall-through, which that unit narrows so a file directly under `tools/` or `skills/` reduces to itself, and AC2's fixture, which it extends (id 36)
- **hands-off** `TOOL-dScopedBuild-35` — S2's bash spawn, S26; S3's `at_exit` argument, S37; S4's scope subject as a dedupe key, S32; and S7's `scope` kind and its grammar line, S7 and S18 (ids 44, 11, 50, 21, 34)
- **hands-off** `TOOL-dScopedBuild-38` — S1's `derive_kit_dir` and S2's `read_unit_writes`, whose signatures that unit widens by `entries`, and AC2's fixture, which its S4 case follows (id 26)

## 4. Design

### Evidence

- The host already reads both populations once (`check_routed_commits`, `routed_commits.py:242`), the
  RANGE from `$GATE_PUSH_BASE..HEAD` (`derive_commit_range`, `:213`), and hosts the deviation join
  after its own verdict (`:331`, `check_deviation_join` `:334`).
- The leg attributes by the union of subject and `Pass:` trailer (`:21-25`, `extract_unit_ids` `:119`).
- `read_spec_writes` returns every backticked word under `### Files touched` with no shape filter
  (`design_lib.py:528-540`); `check_dir_shaped` (`:579`) is true only for a `/`-terminated token of two
  or more segments, so filtering by it alone, as I7 words it, keeps no file path. S2 keeps the words
  of two or more segments, the filter `derive_parallel_step` applies (`gen_build_index.py:1732-1734`),
  plus a word naming a tracked root file.
- A dispatch row is `<utc> dispatch · item <anchor> <unit> · reason <paths>`
  (`lib-unattended.sh:1116-1124`, e.g. `memory/builds/aBatchedArm/RUN.md:59`); no Python reader of it
  exists in the memory-tree kit, and the library's comment names `read_pass_declarations` the one
  reader every caller asks (`:1105-1112`). Its default mode unions every row under a key and prints
  every key; `current` keeps each unit's last key, the window a commit made now is graded in, which
  `--check-commit` reads (`unattended.sh:13546`), while check 23 grades history in the default mode
  (`check-unattended.sh:4113`).
- `policy.py get` reads the landed revision unless given `--rev` (`tools/policy/policy.py:1332`,
  `read_revision` `:724`), and in a clone with no remote, the local default branch (`:470-502`).

### The report

```
routed-commits: scope · RANGE 1a2b3c4d..5e6f7a8b · graded 3 unit(s), 7 commit(s) · 1 stray · 1 reverted · 0 undeclared · build.scope refuse
routed-commits: scope · TOOL-tFix-1 · 9c8b7a6d · tools/beta/b · stray
routed-commits: scope · TOOL-tFix-1 · 0d1e2f3a · tools/gamma/g · reverted
routed-commits: scope · TOOL-tFix-3 · undeclared — its spec carries no ### Files touched and no dispatch row names it
routed-commits: scope FAILED — a commit wrote outside its unit's write set; restore each stray path in a revert pass on the unit:
  9c8b7a6d TOOL-tFix-1 tools/beta/b — git show 9c8b7a6d^:tools/beta/b, committed as `TOOL-tFix-1: revert pass` with `Pass: TOOL-tFix-1`
```

The FAILED line and its remedy rows print under `refuse` only; the other two values print the summary
and the `stray` rows and hand the strays to I5. The WHOLE population prints one line,
`routed-commits: scope · WHOLE not graded — the scope arm grades the pushed range and --build <slug>`.
A RANGE grading no commit prints `graded 0` with the range's commit count, never a clean line.

### The write set, reduced

The reduction coarsens a write set to the kit directories it names, so a unit declaring
`tools/memory-tree/routed_commits.py` may write anywhere under `tools/memory-tree/`. That is the grain
the research measured at 7.2% red, against 20.5% at file grain
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-build.md:123-125`). A
commit naming two units, a resolution pass among them, is allowed the union of both reduced sets.

### The revert test

For each unit with a stray path, one `--batch-check` query asks `<oldest>^:<path>` and
`<newest>:<path>`, `<oldest>` and `<newest>` the unit's oldest and newest commits touching that path
among its own commits in the WHOLE log already read. Equal object ids, or both missing, read
`reverted`. Its ceiling: another unit's edit of the same path between the two commits makes the
blobs differ, so the stray stays listed, and the revert pass's remedy row names the content to
restore.

### The exit form and the record

Under `--build <slug>` the arm reads `<base>` through `read_build_base`, logs `<base>..HEAD` with
`read_routed_commits`, and grades the commits naming a unit whose spec sits under
`memory/builds/<slug>/spec/`. Where `read_build_base` finds no first pass it prints `graded 0 — <slug>
has no first pass` and exits 0. `--write` writes `memory/builds/<slug>/build/<date>-build-<lowest graded unit id>-scope.md`:

```markdown
**Serves:** scope TOOL-tFix-1 TOOL-tFix-2

# Scope report — tFix at 5e6f7a8b, base 1a2b3c4d, build.scope refuse

- routed-commits: scope · TOOL-tFix-1 · 9c8b7a6d · tools/beta/b · stray
```

One record per exit, rewritten in place by a re-run the same day; its lines are the report's lines.
Its kind joins `RECORD_KIND_TOKENS`, so `read_bindings` reads it as a typed record, not as research.

### What it does not check

Whether a declared write set is right for its spec; a path the unit should have written and did not;
a merge commit's own content; any commit outside the pushed range, at the push; a shell write before
its commit, which only the commit reaches; and file-grain strays inside a declared kit directory.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_kit_dir` | function in `design_lib.py` | `py.function`, OK at `--suggest` |
| `read_unit_writes`, `check_build_scope` | functions in `routed_commits.py` | `py.function`, OK at `--suggest` |
| `--kit-dir` | verb of `design_lib.py` | none |
| `--write` | flag of TOOL-dScopedBuild-14's `--build <slug>` mode of `routed_commits.py` | none |
| `scope` | record kind in `RECORD_KIND_TOKENS` | none |
| `stray`, `reverted`, `undeclared` | report verdicts | none |

### Migration

None. History before the push is not graded, and the catalogue row exists.

### Rollout

Live at landing at the catalogue default, `warn-and-ask`: a stray warns and files an ask, and the
push goes on. gov's `.governance/policy.toml` declares no `build.scope`.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`: S2 to S8, its self-test arms
- `tools/memory-tree/design_lib.py`: S1
- `tools/memory-tree/tree_lib.py`: S7, `RECORD_KIND_TOKENS`
- `tools/unattended/unattended.sh`: S7, the `check_build_exit` term
- `tools/policy/catalogue.toml`, render `tools/policy/unsummarised-keys.txt`: S9
- `help/build-scope.md` (new), `help/README.md`, `help/policy.md`, `tools/memory-tree/README.md`: S10

### Alternatives rejected

- **File granularity** — lost to the research's losing test: 20.5% of real commits red, noise a gate
  whose steady state is red gets bypassed for · `research-build.md:123-124`
- **A lease checked at the write (candidate B)** — lost to the `[class]` rule, the guard reading what
  the agent typed; scope at the write is TOOL-dScopedBuild-5's, from derived state · `research-build.md:128-137`
- **Extending `--check-commit` and check 23 to attended work** — lost to the population: an attended
  unit has no dispatch row, so its only write set is the spec's · scout B disagreement 7
- **A WHOLE half beside the RANGE half** — lost to the clause, "scope at the push", and to the 7.2%
  of landed history it would red on every run (§8 F2)

## 5. Production-readiness checklist

- security — reads tracked text and runs `git cat-file` with argv lists; a dispatch row's paths are
  data matched as strings, never run; the value is read at the landed revision, so a branch cannot
  set its own grade.
- perf / scale — two batched git calls at most beyond the leg's, and one `policy.py get`.
- error / empty / loading states — `graded 0` with its count; `undeclared` per unit; `scope off` with
  no policy kit; `--build` exit 2 naming an unreadable base.
- observability — one line per stray, naming unit, commit, path and remedy.
- risks — 7.2% of commits strayed at kit grain in the measured month: at the default each files an
  ask, which the owner reads; under `refuse` a stray blocks the push until its revert pass.
- testing — each value on a planted stray, its in-scope twin, the revert, the dispatch row, the
  resolution commit, the spawn count.
- migration — none.
- user docs — `help/build-scope.md`, new (S10).

## 6. Acceptance criteria

- **AC1** — When `python design_lib.py --kit-dir` runs over `tools/memory-tree/routed_commits.py`,
  `skills/session-kickoff/SKILL.md`, `.githooks/pre-push` and `WIRE-INTO-PROJECT.md`, it prints
  `tools/memory-tree/`, `skills/session-kickoff/`, `.githooks/` and `WIRE-INTO-PROJECT.md`, one per
  line, as `design_lib.derive_kit_dir` returns them.
  Red when: a path under `tools/` reduces to itself or to `tools/`.
- **AC2** — When `python -c` builds a scratch repository with `routed_commits.build_fixture`, `ROUTED_PATHS`
  `tools/`, a spec for `TOOL-tFix-1` whose Files touched names `tools/alpha/a`, a commit naming the
  unit that writes `tools/alpha/c` and one that writes `tools/beta/b`, and a committed
  `.governance/policy.toml` setting `[build] scope`, then calls `check_routed_commits` with
  `GATE_PUSH_BASE` at the spec commit: under `refuse` the exit is 1 and `routed-commits: scope FAILED`
  names `tools/beta/b`; under `warn-and-ask` the exit is 0, the `stray` line names it,
  `render_gate_outcome` prints one `ask · build.scope · TOOL-tFix-1` line and `write_gate_asks` adds one
  ask row naming it to the fixture build's `BACKLOG.md`; under `report` the exit is 0 with the `stray`
  line and no ask; and `tools/alpha/c` is never listed.
  Red when: a value's outcome differs, or the in-scope path is listed.
  fixture: the policy kit resolves beside the memory-tree kit, and the policy file sits on the
  fixture's `main`, its landed revision with no remote.
- **AC3** — When the AC2 fixture's build `RUN.md` carries a dispatch row naming `TOOL-tFix-1` with
  reason `tools/beta/`, the same `check_routed_commits` call lists no `stray`; with the row moved to a
  rotated `RUN.LANDED.0a1b2c3d.md`, still none.
  Red when: a dispatch row is not read, or a rotated one is missed.
- **AC4** — When the AC2 fixture under `refuse` gains a later commit naming `TOOL-tFix-1` that restores
  `tools/beta/b` to its first-parent content, `check_routed_commits` exits 0 and lists it
  `reverted`; and a commit whose subject names `TOOL-tFix-1` and `TOOL-tFix-2`, the second declaring
  `tools/beta/`, writing `tools/beta/d` lists no `stray`.
  Red when: a reverted stray reds, or a two-unit commit is held to one unit's set.
- **AC5** — When `check_routed_commits` runs on the AC2 fixture with no `GATE_PUSH_BASE`, it prints the
  `scope · WHOLE not graded` line and exits as the leg does without the arm; and a unit whose spec
  carries no Files touched sub-head prints `undeclared` and no `stray`.
  Red when: WHOLE is graded, or an undeclared unit reds.
- **AC6** — When `python routed_commits.py --build tFix --write` runs in the AC2 fixture under `refuse`,
  it exits 1 and writes one `-scope.md` record whose `**Serves:**` line reads `scope TOOL-tFix-1`, and
  `python -c` calling `tree_lib.read_bindings` over it reads kind `scope`; after the revert pass of
  AC4 it exits 0.
  Red when: the record is not written, is read as research, or `--build` passes a stray under `refuse`.
- **AC7** — When `python -c` runs `check_policy.scan_reader_keys(".")` in this tree, the set holds
  `build.scope`; `catalogue.toml`'s `build.scope` row carries `summary` and `usage`; and `grep -x
  build.scope unsummarised-keys.txt` finds nothing.
  Red when: the arm's read is no literal call, or the row is still unsummarised.
- **AC8** — When `routed_commits.GIT_SPAWNS` is read after `check_routed_commits` over two fixture
  histories of three and thirty commits, each with one stray and one dispatch row, the two counts are
  equal; and over a history declaring no write set the count equals the leg's count without the arm.
  Red when: the arm spawns per commit, per path or per unit.
- **AC9** — When `grep -n "routed_commits.py --build " unattended.sh` runs, its one hit is in the body
  of `check_build_exit`, calling the mode with `--write` and returning 1 on its exit 1, and no verb
  body calls the mode; and a sliced
  `check_build_exit` over the AC2 fixture under `refuse` prints the scope lines and returns 1.
  Red when: the exit does not run the scope arm, or passes a refused stray.
- **AC10** — When `grep -n "build.scope" build-scope.md policy.md` runs, the new page names the three
  values and `--build`, and the policy page lists `build.scope` among the keys a gate reads; `grep -n
  "build-scope.md" README.md` in `help/` finds its index line.
  Red when: a page is silent or the index omits it.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `policy fixtures` · `check-wiring self-test` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/routed_commits.py · covers AC2 AC3 AC4 AC5 AC6 AC8 · a scratch history with a planted stray under each `build.scope` value, its in-scope twin, a dispatch row, a revert and a two-unit commit, staged by deleting the stray's revert · the spawn-count arm's armed count, two
New arm: tools/policy/check_policy.py · covers AC7 · reader coverage over `build.scope` once dScopedBuild lands, staged by renaming the arm's literal · none

## 8. Open questions

- **F1 — At what grain is a path in scope?** Options: (a) kit directories, the write set reduced by
  S1; (b) files, the write set as written; (c) builds, any path any unit of the build declares. (b)
  reds 20.5% of measured commits and (c) leaves gap-build-01 open within a build. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 1, the owner's walk B1 asked of "declared kit directories" and
  answered warn-and-ask, its row v2:1297, and the research's kit-grain survivor (`research-build.md:123-125`). widens: none · relaxes: none
- **F2 — Which population does the arm grade at the push?** Options: (a) the RANGE half only, the
  WHOLE half printing one line; (b) RANGE and WHOLE, as the leg grades attribution. (b) grades landed
  history the clause does not name and reds 42 of 582 landed commits on every run. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 1, the clause's "scope at the push" names the pushed range, and the Build exit is graded by `--build <slug>`. widens: none · relaxes: none
- **F3 — Which write set grades a dispatched unit?** Options: (a) its dispatch rows when any names it,
  else its spec's Files touched; (b) the union of both; (c) the spec's alone. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 1, `flow-steps.md:292` grades "as the driver's `--check-commit` and check 23 already grade a pass", which read the dispatch rows. widens: none · relaxes: none
- **F4 — What is the scope report on disk?** Options: (a) one `scope` record per Build exit, written
  by `--build <slug> --write`; (b) one record per unit; (c) no record, the printed lines only. (c)
  leaves `record-kind.scope` naming nothing a later item can join; (b) writes fifteen files for one
  exit's facts. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich survivor
  with the fewer files, tie-broken by reuse of `RECORD_KIND_TOKENS` as `deviation` joined it. grants: PLAY-dClosedLoop-3 the record kind `scope` and the `--write` flag of `--build`. widens: none · relaxes: none
- **F5 — Where does the kit-directory rule live, given TOOL-dPlacedRequest-1 S9 states it for its
  shell probe and is not this build's parent?** Options: (a) `design_lib.derive_kit_dir` with a
  `--kit-dir` CLI, and an ask that dPlacedRequest's reduction reads it; (b) wait for dPlacedRequest;
  (c) a Python copy with no ask, a second answer to one question. (b) assumes a non-parent lands
  first, which the brief forbids. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3. Ask for the
  main loop to file, target build dPlacedRequest: "TOOL-dPlacedRequest-1 S9's `kit-dirs` reduction
  would be a second implementation of the rule TOOL-dScopedBuild-3 lands as `design_lib.derive_kit_dir`"
  · accept TOOL-dPlacedRequest-1 S9 reduces each path through `design_lib.py --kit-dir` before its join, seen on a planted overlap of two files of one kit. widens: none · relaxes: none
- **F6 — At which revision is `build.scope` read at the push?** Options: (a) the landed revision, the
  reader's default; (b) the pushed tip, `--rev HEAD`. (b) lets a branch loosen its own push grade.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 1, the reader's contract, "it never reads your working tree" and reads the landed revision (`help/policy.md`, `policy.py:24-26`). widens: none · relaxes: none
- **F7 — TOOL-dScopedBuild-1 S4 has `check_build_exit` write no run-state file and `--build-exit` write
  none; where does `--build <slug> --write` run?** Options: (a) as the one mode call inside
  `check_build_exit`, its writes confined to the scope record under `memory/builds/<slug>/build/` and,
  through TOOL-dScopedBuild-9, the map's grace file, both committed with the exit's records; (b)
  `check_build_exit` runs `--build <slug>` read-only and a separate write step follows a passing exit,
  a step TOOL-dScopedBuild-1 does not spec; (c) no record at the exit. (b) leaves the write with no
  caller in either mode; (c) fails F4. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich survivor; TOOL-dScopedBuild-1 S4 names these two records and the asks `write_gate_asks` stages as the exit's only writes, its arms', none of them run state. widens: none · relaxes: none

- **F8 — Which dispatch declarations make a dispatched unit's write set?** Options: (a) the union of
  every key `read_pass_declarations` prints for the unit in its default mode, the reader called by
  subprocess; (b) its `current` mode, the unit's last key alone; (c) a Python reader of the rows beside
  it. (b) answers which window a commit made now is graded in, and the scope arm grades every commit
  of the unit's life at the push and the Build exit, so a re-dispatched unit's earlier pass would read
  its own declared paths as strays; (c) is a second reader of one row, the defect the library's
  comment (`lib-unattended.sh:1105-1112`) records it removed. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the one survivor; the shell reader owes nothing, since it stays the one reader and its default mode is the answer, and the per-key grain stays check 23's. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 3, gap-build-01, the Build item table's
  `build.scope`, `build.revert-pass` and `build.resolve` rows, walk B1, the research's candidate A,
  scout B's row for this unit and its disagreements 6 and 7, and shared interfaces I1, I4 to I8.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-27, TOOL-dScopedBuild-30, TOOL-dScopedBuild-33, TOOL-dScopedBuild-34, TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-38,
  the promotions of the round-1 spec audit of units 25 to 35 (id 26).

## 10. Reuse audit

The seam extended is `check_routed_commits` (`tools/memory-tree/routed_commits.py:242`), the push-time
host NP-22 merged into `build.scope`, with the arm after `check_deviation_join` (`:334`), the union
attribution `extract_unit_ids` (`:119`), the one write-set reader `design_lib.read_spec_writes`
(`:528`) and the one matcher `check_guard_trips` (`:589`); every line verified at `5f0b11f12`. Scout B's
row holds there, with two corrections: I7's `check_dir_shaped` filter keeps no file path (§4
Evidence), and the scout's `check_deviation_join` call site is `:331`, the definition `:334`.
`python tools/codebase-map/reuse_lookup.py "check each pushed commit's paths fall inside its unit's
declared write set"` ranked name stems (`check`, `write`, `units`, `build_commit`, `attribute_paths`)
and no scope matcher; `attribute_paths` maps paths to dossiers, not to a unit's write set, so no
existing seam fits the arm beyond the host and the two design_lib readers it extends. The kit-grain
rule has no Python implementation: TOOL-dPlacedRequest-1 S9 specs it for a shell probe not yet built.

Recall terms used: `python tools/memory-recall/query.py "how does the push-time leg check a commit stays inside its unit's write set" --terms "routed commits scope write set files touched kit directory stray push dispatch writes build.scope"`.
The query's first two runs refused at `ensure_cache` with `PermissionError` (WinError 32) on the
shared recall cache sibling writers held open; the third returned 40 hits, its top ten this build's
scout B row, brief and specs, and `research-build.md`, none naming a scope seam beyond the host.
