# TOOL-aPiecewiseGrade-3 — the spec-token checker resolves the memory-tree kit's `design_lib` once per process, so no caller pays the kit resolution per call

**Status:** SPECCED · rev-1 · 2026-11-15 · node a · Tier-1 · base aebbb4a72 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-3-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-3-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md) | research | TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 |

<!-- /gen:spec-records -->

## 1. Goal

`load_design_lib` in `tools/check-spec-tokens.py` keeps the first module it loads and returns that
module on every later call. The guards join and every other caller then stop resolving the kit on
each call. That is about 98 s of a 150 s whole-tree run on node `a` (DERIVED from TOOL-aPiecewiseGrade-1's table, PINNED d9f84ee14),
and no printed byte or exit status moves.

## 2. Scope (IN)

- **S1** — `load_design_lib` carries `@functools.lru_cache(maxsize=None)`, and `import functools`
  joins the checker's import block. Its docstring gains one sentence: the first load that returns is
  kept for the process, and a load that raises is not kept. Observed by AC2 and AC4.
- **S2** — With the kit resolved, the checker's stdout and exit status equal the base's over the
  real tree, over a guards fixture and under `--legs-for`. Observed by AC1.
- **S3** — With the kit unresolved, the plain run prints today's REFUSING line and returns 1, and
  `--legs-for` raises today's `ImportError` with today's message. Observed by AC3.

## 3. Non-goals (OUT)

- No change to `load_kit_module`, `KIT_LOADS` or `resolve_kit_dir`, and no memo for the kit's other
  modules. `tree_lib`, `gen_build_index` and `routed_commits` are each loaded a handful of times per
  run.
- No edit to any call site of `load_design_lib`. Every caller keeps calling the function.
- No change to any verdict, refusal line, report line, summary line or exit status.
- No per-spec cache. That is TOOL-aPiecewiseGrade-1's.
- No work on the carries join's history read, the cost left after this unit. It is filed as an ask
  at the build's wrap-up.
- No kit version bump by hand. The lander's mint moves `KIT_SPEC_TOKENS_VERSION`.

### Edges

- **hands-off** `TOOL-aPiecewiseGrade-1` — the per-spec cache over the loop this unit makes cheap. This unit builds first, at order 1. TOOL-aPiecewiseGrade-1 follows at order 2, and TOOL-aPiecewiseGrade-2 at order 3.

## 4. Design

### What the code does today

Read at `d9f84ee14`, aLightenedLoop's head, and at `aebbb4a72`, this build's base. The checker's blob
is `6763260c` at the first and `f1d1d958` at the second. `load_kit_module` and `load_design_lib`
are byte-identical across the two, so this design holds for the tree after aLightenedLoop
reconciles onto main.

- `load_design_lib` (`tools/check-spec-tokens.py@f1d1d958:1057`, `tools/check-spec-tokens.py@6763260c:1116`)
  returns `load_kit_module("design_lib")` and keeps nothing.
- `load_kit_module` (`tools/check-spec-tokens.py@f1d1d958:1020`) raises `ImportError` naming
  `KIT_MISS` when `KIT_DIR` is None. Otherwise it reuses `sys.modules["design_lib"]` when that
  module's file resolves to the kit's, comparing two `Path.resolve` answers
  (`tools/check-spec-tokens.py@f1d1d958:1038`). Next it tries `KIT_LOADS` under a third resolve
  (`tools/check-spec-tokens.py@f1d1d958:1040`). Only then does it load the file. So every call
  returns the same object, and every call pays the resolves. That costs about 1.4 ms per call on Windows (PINNED d9f84ee14).
- `KIT_DIR` is resolved once, at module level, by `resolve_kit_dir`
  (`tools/check-spec-tokens.py@f1d1d958:616`). `DESIGN_LIB` is None when it does not resolve.
  The module-level bindings `SPEC_DATE` and `NOT_A_TOKEN` call `load_design_lib` only when
  `DESIGN_LIB` is set (`tools/check-spec-tokens.py@f1d1d958:1065`,
  `tools/check-spec-tokens.py@f1d1d958:1069`). So with the kit resolved, the first load happens at
  import.
- The callers, by enclosing function, are the same set at both shas. At `aebbb4a72` they are
  `extract_files_touched`, `derive_tripped_legs`, `scan_handoffs`, `read_carries_specs`,
  `scan_carries` and `derive_carries_coverage`. `main` calls it four times in the guards join
  (`tools/check-spec-tokens.py@f1d1d958:1967-1990`) and once for the `DesignRefusal` catch
  (`tools/check-spec-tokens.py@f1d1d958:2082`). At `d9f84ee14` `read_carries_texts` also calls it.
  The guards join calls it once per guard per declared path inside generator expressions, which is
  where the call count comes from.
- Measured by TOOL-aPiecewiseGrade-1's probe over a frozen clone: `main` made 70 726 `load_kit_module`
  calls costing 97 865 ms of 166 731 ms (PINNED d9f84ee14). At the base it made 73 134 calls costing 100 619 ms (PINNED aebbb4a72).
- With the kit unresolved, `main` prints `spec-tokens: REFUSING — the memory-tree kit's
  design_lib.py does not resolve (...)` and returns 1 before any join
  (`tools/check-spec-tokens.py@f1d1d958:1762`). `--legs-for` branches before that refusal, and its
  `derive_tripped_legs` reaches `load_design_lib`, which raises the `ImportError` uncaught.

### The change

```python
@functools.lru_cache(maxsize=None)
def load_design_lib():
```

`lru_cache` keeps a returned value and never an exception. With the kit resolved, the import-time
call for `SPEC_DATE` fills the cache, and every later call returns that module without entering
`load_kit_module`. With the kit unresolved, nothing is ever kept. Each call still enters
`load_kit_module` and raises the same `ImportError` with the same message. The wrapper is the C
implementation, so a traceback gains no frame. Its line numbers move with the two added lines, and
the uncaught case prints that traceback on stderr, which this unit does not hold equal.

The module returned is the one `load_kit_module` returns today on every call. That is one object
per process, the contract TOOL-dTrueNorth-31 S11 set. So `DesignRefusal` stays one class. The
suite's namesake arm at `tools/check-spec-tokens.test.sh@dd5bb34d:1987` imports the kit's
`design_lib` before it loads the checker, then swaps a namesake into the slot and calls
`load_design_lib` twice. It still reads one load, the kit's file, a caught refusal and the namesake
kept. `gen_build_index`'s carries read loads the checker fresh per call and catches
`mod.load_design_lib().DesignRefusal`, which is the same object its `derive_carries_coverage` used.

### What the design does not check

- **A slot replaced by a second load of the kit's own file after the checker's import.** Today
  `load_design_lib` would return the replacement. After this unit it returns the first load. No
  caller in the tree does this at `aebbb4a72`. Both `sys.modules["design_lib"]` writes put a
  namesake from another file there, and today's loader does not return a namesake either.
- **The other kit modules** still resolve per call through `load_kit_module`. No join calls them in a
  loop at `aebbb4a72`.
- **The traceback's line numbers** on the unresolved `--legs-for` path move, as they do for any edit
  above them.

### The pass probe, `$SCRATCH/pg3.sh`

The two checkers must sit at one path, `tools/check-spec-tokens.py` in the graded tree. `HERE`
derives the leg manifest, the policy kit and the packet door from that path. A copied checker would
read other files, and swapping the file in place would move the cite join's line count for any spec
citing it. So `$SCRATCH/pg3.py` compiles a checker's source under a path it is given, in a fresh
module that it registers as `cst` in `sys.modules`. It then wraps `load_kit_module` with a per-name
counter and calls `main(argv)` with stdout captured:

```python
mod = types.ModuleType("cst"); mod.__file__ = as_path; sys.modules["cst"] = mod
exec(compile(pathlib.Path(source).read_text(encoding="utf-8"), as_path, "exec"), mod.__dict__)
```

It writes the captured stdout to a file, or `raised <class>: <message>` when `main` raises. It prints
`rc <rc|raised> loads <calls of load_kit_module("design_lib") during main> wall <ms>`.

`$SCRATCH/pg3.sh` takes the pass's starting commit, the reconciled base before this unit. It writes
that commit's checker to `$TEMP/pg3/base.py`. Every run unsets `SPEC_TOKENS_INPUTS`. Each step runs
the base source and then the built `tools/check-spec-tokens.py` under the same path and argv. It
prints `<step> rc <base>/<built> same <0|1> loads <base>/<built> wall <base>/<built>`, where `same`
is 1 when `cmp` finds the two captured outputs equal.

| step | cwd | as-path | argv |
|---|---|---|---|
| `real` | the pass's worktree, unchanged between the two runs | its `tools/check-spec-tokens.py` | none |
| `fixture` | `$TEMP/pg3f` | the worktree's checker path | none |
| `legs` | `$TEMP/pg3f` | the worktree's checker path | `--legs-for <prefix>x/thing.sh` |
| `nokit` | `$TEMP/pg3f` | `$TEMP/pg3k/tools/check-spec-tokens.py` | none |
| `nokitlegs` | `$TEMP/pg3f` | `$TEMP/pg3k/tools/check-spec-tokens.py` | `--legs-for <prefix>x/thing.sh` |

`$TEMP/pg3f` follows the suite's guards recipe: `scratch`, the `GUARD_LEGS` manifest,
`write_files_touched` naming `<prefix>x/thing.sh`, and `SPEC_GUARD_LEGS_CUTOFF="2026-09-01"`
(`tools/check-spec-tokens.test.sh@dd5bb34d:366`, `tools/check-spec-tokens.test.sh@dd5bb34d:805`).
It also commits a tracked `<prefix>x/thing.sh`, as the suite's `--legs-for` arms do
(`tools/check-spec-tokens.test.sh@dd5bb34d:1641`), so `--legs-for` reaches `derive_tripped_legs`.
Its plain run prints a `[guards]` hit and exits 1. `$TEMP/pg3k/tools` exists, holds no kit and has
no `.git` above it, so `resolve_kit_dir` refuses. After `nokit` the probe also prints
`refused <0|1>`, 1 when the built run's captured output opens with
`spec-tokens: REFUSING — the memory-tree kit's design_lib.py does not resolve`.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **A module-level binding of the loaded module, used at every call site.** It edits fifteen
  sites at `aebbb4a72` and sixteen at `d9f84ee14`, and with the kit unresolved the `--legs-for` path would fail on `None` rather than raise
  today's `ImportError`.
- **A memo inside `load_kit_module`, per name.** It reaches modules no loop calls and changes the
  namesake contract's reading for `tree_lib` for no measured gain.
- **Caching the resolved paths inside `load_kit_module`.** Each call would still do the
  `sys.modules` lookup and the comparisons, and the contract's code would change for the same gain.
- **A hand-written global and a None test.** `functools.lru_cache(maxsize=None)` is the stdlib form
  and the kit's own precedent, `read_gen_strip` in `tools/memory-tree/deviation_join.py@c793df78:373`.

## 5. Production-readiness checklist

- security — N/A — no input, write path or process is added.
- perf / scale — the whole-tree run on node `a` drops from about 150 s to about 69 s (DERIVED from TOOL-aPiecewiseGrade-1's table, PINNED d9f84ee14). `--spec`, `--pass-spec` and `--dispatch`
  drop by their share of the same calls. AC2 records the real figures.
- error / empty / loading states — an unresolved kit refuses as today, per S3.
- observability — N/A — nothing is printed.
- risks — a process that swaps a second load of the kit's own file into the slot keeps the first,
  as §4 states. None does.
- testing — the pass probe, and the suite's new arm observed RED then GREEN at the close.
- migration — none.
- user docs — the docstring of `load_design_lib`. No `help/` page states the checker's speed or its
  kit loading, grepped at `aebbb4a72`.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg3.sh" <starting commit>`, described in §4,
removed after the pass.

- **AC1** — When `bash "$SCRATCH/pg3.sh"` runs, its `real`, `fixture` and `legs` lines each read
  `same 1` with matching statuses: `real` 1/1 or 0/0 as the tree stands, `fixture rc 1/1`
  and `legs rc 0/0`.
  Red when: the memo returns a module other than today's, so a join's answer, a line or the exit
  status of the whole-tree run, the guards fixture or `--legs-for` moves.
  cost: two in-process whole-tree runs, about 150 s for the base and about 69 s for the built. <!-- DERIVED from TOOL-aPiecewiseGrade-1's table, PINNED d9f84ee14 -->
  permission: the probe runs no leg's argv. It calls each checker's `main` in its own process, as a probe of this unit's code.
- **AC2** — When `bash "$SCRATCH/pg3.sh"` runs, its `real`, `fixture` and `legs` lines each read
  `loads <n>/0` with `n` above 0, and the `real` line's built wall is below its base wall.
  Red when: `load_design_lib` still enters `load_kit_module` on a call after the first, or the
  cache is dropped.
  figure: `n` and both walls are DERIVED at observation and recorded in the unit's acceptance ledger.
- **AC3** — When `bash "$SCRATCH/pg3.sh"` runs, it prints `nokit rc 1/1 same 1`, `refused 1` and
  `nokitlegs rc raised/raised same 1`.
  Red when: an unresolved kit is cached as `None`, or a call stops raising today's `ImportError`
  with its message.
- **AC4** — When `grep -c "@functools.lru_cache(maxsize=None)" tools/check-spec-tokens.py` runs it prints 1, and the line after it is
  `def load_design_lib():`.
  Red when: the memo sits on another function, or on none.

## 7. Gates

`spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `spec tokens (the pass's own spec)` · `harness arms (fail branches armed or pinned)` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC2 · beside the guards arms: the checker loaded in process over the guards fixture, `load_kit_module` wrapped with a counter, asserting the run printed its `[guards]` hit and made no `design_lib` call; staged RED by removing the decorator · `FLOOR_ASSERTIONS`, raised by one, which the close confirms

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
the spec-token checker's `--spec` over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft from brief `2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief`,
  item 1, on the owner's (c) to TOOL-aPiecewiseGrade-1's F1. Grounded at `aebbb4a72` and at
  aLightenedLoop's head `d9f84ee14`.

## 10. Reuse audit

The seam this unit extends is `load_design_lib` itself (`tools/check-spec-tokens.py@f1d1d958:1057`),
the one function every caller already routes through, memoized with the stdlib form the memory-tree
kit already uses for `read_gen_strip` (`tools/memory-tree/deviation_join.py@c793df78:373`).
`tools/codebase-map/reuse_lookup.py` for "load a kit module once per process and reuse the loaded
module on every later call" ranked `resolve_kit_dir` first, which this unit leaves alone because it
already runs once per process, then generic `load` stems, so no memo seam fits beyond these. Recall's
top hits were TOOL-dTrueNorth-31, whose S11 set the one-load contract this unit keeps, and the
TOOL-dFurnishedOrders-59 audit that pins `load_design_lib().check_guard_trips` as the guards join's
one call form. `gotchas.py --for-paths tools/check-spec-tokens.py` selected
`fixture-passes-by-finding-nothing`, which the fixture's `[guards]` hit and the arm's hit assertion
answer.

Recall terms used: `python tools/memory-recall/query.py "how does the spec-token checker load the memory-tree kit's design_lib, and why is each load reused" --terms "load_kit_module load_design_lib KIT_LOADS namesake design_lib DesignRefusal one load sys.modules spec-token checker kit resolve"`
