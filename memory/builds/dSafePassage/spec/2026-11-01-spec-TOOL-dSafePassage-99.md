# TOOL-dSafePassage-99 — govkit selftest holds one engine: `govkit_module()` answers the engine at `GOVKIT` after a staged copy loads in process

**Status:** CLOSED · rev-3 · 2026-11-01 · node a · Tier-2 · base f519c1934 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-87

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md](../build/2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 TOOL-dSafePassage-84 TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 TOOL-dSafePassage-89 TOOL-dSafePassage-90 TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-93 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96 TOOL-dSafePassage-97 TOOL-dSafePassage-98 TOOL-dSafePassage-100 TOOL-dSafePassage-101 TOOL-dSafePassage-102 TOOL-dSafePassage-103 TOOL-dSafePassage-104 |
| [2026-11-01-build-TOOL-dSafePassage-99-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-99-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-99-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-99-2-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-2-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-99-3-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-3-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-99-audit-fold-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-audit-fold-brief.md) | research | TOOL-dSafePassage-100 |
| [2026-11-01-prompt-TOOL-dSafePassage-99-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-99-rev3-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-rev3-brief.md) | research | TOOL-dSafePassage-101 |
| [2026-11-01-prompt-TOOL-dSafePassage-99-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-99-spec-brief.md) | research | — |
| [2026-11-01-review-TOOL-dSafePassage-99-100-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dSafePassage-99-100-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-100 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-87 AC6 loads a staged copy of the step module in process, and that copy's own
`load_govkit()` puts the copy's engine into `sys.modules["govkit"]`. From then on
`govkit_module()` answers that copy, so `check_upgrade_steps` crashes at its `[dSP-72]` arms and the
`govkit selftest` leg reds at HEAD. This unit fixes it once, in `govkit_module()`, which holds the
engine at `GOVKIT` and re-binds the module table to it on every call. After it no import
statement in the suite names `govkit`, so every engine import goes through that function, and one
arm holds both. The one by-path load of the engine left in place is named in S2.

## 2. Scope (IN)

- **S1** — `govkit_module()` in the govkit selftest holds the one engine at `GOVKIT`. The first call
  takes the cached `govkit` module when its file resolves to `GOVKIT`, and otherwise loads `GOVKIT`
  by path under the name `govkit`. Every call then re-binds `sys.modules["govkit"]` to the held
  engine and `sys.modules["upgrade_steps"]` to that engine's own `upgrade_steps`, and returns the
  held engine (§4 "The held engine"). This closes the review item id 1. Observed by AC1 and AC2.
- **S2** — no import statement in the govkit selftest names `govkit`. The nine that did now read
  `govkit_module()`: the three helpers `govkit_steps`, `govkit_kind_marks` and
  `govkit_update_role`, and the six in-function imports in `main` (§4 "Inventory"). One by-path
  load of the engine is left in place: `govkit_mod` at selftest.py:9764-9766. It never binds a
  copy's step module (govkit.py:125-128), and after S1 it reuses the held one. It reads only
  `LANDABLE_ROLES`, `ROLE_KINDS` and `KIND_MARKS` (selftest.py:9767-9770). Observed by AC3.
- **S3** — the regression arm, review item id 2: four `[dSP-99]` checks at the end of
  `check_staged_copies` (§4 "The arm"). They load a staged copy in process, call its
  `load_govkit()`, and assert that `govkit_module()` then answers the engine at `GOVKIT`. The third
  check grades S2's import statements over the file's own syntax tree, and reads no by-path load.
  The fourth asserts that the held step module's own `load_govkit()` answers the held engine once
  `govkit_module()` has re-bound the table. Observed by AC2.

## 3. Non-goals (OUT)

- Any change to `load_govkit` in the step module. The copy's engine is the right engine for the
  copy, and the defect is the suite reading the copy's module-table entry as its own.
- Any change to the staged loads themselves, at selftest.py:3179-3182, 4208-4210, 4235-4237,
  4296-4299, 4496-4499 and 5269-5272. Each stays as it is, and S1 restores the table after them.
- Any change to `load_upgrade_steps` in the engine, or to how the sibling modules of the kit import
  the engine (§4 "What it does not cover").
- Any edit of 87's spec, which is CLOSED.
- A help page. The selftest's module handling is not user-facing.

### Edges

none

TOOL-dSafePassage-87 and -71 are CLOSED, and this unit reads their landed code: 87 AC6's staged
load at selftest.py:3179-3182, the load that displaces the engine, which AC1 re-runs unchanged, and
71's `build_staged_copy`, which S3's arm stages its copy through. They are named here rather than
joined, so neither CLOSED spec gains a line (TOOL-dSafePassage-101 S1).

## 4. Design

Every line cited here was read at `f519c1934`, the HEAD this spec was written at, and re-read at
`6414e1dc6` for rev-2, where `tools/` is unchanged. Every measurement below was made on 2026-11-01
on node a.

### The mechanism

1. `check_upgrade_steps` (selftest.py:2937) binds `steps = govkit_module().upgrade_steps` at
   selftest.py:3093. Its `read_refusal` (selftest.py:3095) catches `steps.Refusal`.
2. 87 AC6 loads a staged copy as `us87` (selftest.py:3179-3182) and calls `us87.read_steps`
   (selftest.py:3183). That reaches the copy's own `load_govkit()` (upgrade_steps.py:2675).
3. That function compares each cached module's file with the copy's `HERE / "govkit.py"`
   (upgrade_steps.py:2683-2687). The cached engine is the real one, so the test misses, and the
   function writes the copy's engine to `sys.modules["govkit"]` (upgrade_steps.py:2690).
4. The copy's engine runs its own `load_upgrade_steps` at import (govkit.py:141). That test also
   misses, so it loads the copy's step module and writes it to `sys.modules["upgrade_steps"]`
   (govkit.py:126-136). The copy's engine binds its `Refusal` to that module's class
   (govkit.py:142).
5. `govkit_module()` (selftest.py:150-154) answers with `import govkit`, which returns the cached
   copy. So `gk72` (selftest.py:3198) is the copy's engine, and its `demand_contained_dest`
   (govkit.py:1219) raises a `Refusal` class that `read_refusal` does not catch. The run dies at the
   `leaked72` comprehension (selftest.py:3199).

A probe at `f519c1934` in a fresh process reproduces steps 2 to 5 without the rest of the suite. It
calls `govkit_module()`, loads a staged copy of the unchanged step module through
`build_staged_copy`, and calls the copy's `load_govkit()`. Then `govkit_module()` answers an engine
whose file is not `GOVKIT`, which is not the first engine and whose `Refusal` is not the first
engine's. `sys.modules["upgrade_steps"]` is the copy's. All four tests printed `False`, and
`demand_contained_dest("../x", ...)` raised past an `except` naming the first engine's `Refusal`.

### The held engine

Re-loading `GOVKIT` afresh on a miss is not a fix. It would run `load_upgrade_steps` again over the
copy's step module, load a third step module, and mint a third `Refusal`. `steps.Refusal`, bound at
selftest.py:3093 before the staged load, would still not catch it. So the function keeps the first
engine it obtains and hands back that object every time.

```python
GOVKIT_HELD: list = []   # the one engine at GOVKIT this process took first


def govkit_module():
    """..."""
    if not GOVKIT_HELD:
        sys.path.insert(0, str(HERE))
        mod = sys.modules.get("govkit")
        if mod is None or pathlib.Path(getattr(mod, "__file__", "") or "").resolve() != GOVKIT:
            spec = importlib.util.spec_from_file_location("govkit", GOVKIT)
            mod = importlib.util.module_from_spec(spec)
            sys.modules["govkit"] = mod
            spec.loader.exec_module(mod)
        GOVKIT_HELD.append(mod)
    sys.modules["govkit"] = GOVKIT_HELD[0]
    sys.modules["upgrade_steps"] = GOVKIT_HELD[0].upgrade_steps
    return GOVKIT_HELD[0]
```

The first-call load follows the identity test and the by-path load that `load_govkit` already uses
(upgrade_steps.py:2683-2692), against the suite's own `GOVKIT` (selftest.py:155). The
`sys.path.insert` stays, because the function inserted the kit directory before this unit. The
`upgrade_steps` re-bind keeps the pair that `load_upgrade_steps` documents as one class
(govkit.py:116-124). The one by-path load S2 leaves, `govkit_mod` at selftest.py:9764-9766, then
reuses the held step module and never a copy's, because `load_upgrade_steps` takes the cached step
module only when its file is the one beside the engine (govkit.py:125-128).

`GOVKIT` is assigned on the line after the function (selftest.py:155). The name is read only when
the function is called, so the order does not matter.

### The arm

At the end of `check_staged_copies` (selftest.py:3663), after its `[dSP-71]` checks:

1. `held99 = govkit_module()`, then clear `tmp / "dsp99-copy"` with
   `shutil.rmtree(..., ignore_errors=True)`, as TOOL-dSafePassage-96 does for a reused tmp.
2. Stage a copy of the unchanged step module through `build_staged_copy(tmp / "dsp99-copy", ...)`,
   load it in process as `us99_copy`, and call its `load_govkit()`, keeping the result as
   `copy99`.
3. Check 1: `sys.modules.get("govkit") is copy99`, and `copy99`'s file does not resolve to
   `GOVKIT`. This proves the staged load displaced the engine, so the next check is not vacuous.
4. Check 2: `gk99 = govkit_module()` is `held99`, its file resolves to `GOVKIT`,
   `sys.modules["govkit"]` is `gk99`, `sys.modules["upgrade_steps"]` is `gk99.upgrade_steps`, and
   `gk99.Refusal is gk99.upgrade_steps.Refusal`.
5. Check 3: over `_ast.parse(own)`, the line numbers of every `Import` node naming `govkit` and every
   `ImportFrom` node whose module is `govkit` form the empty list. `own` is the file text the
   function already reads.
6. Check 4: `held99.upgrade_steps.load_govkit() is held99`, called after check 2's
   `govkit_module()`. A comment above it states the window it bounds: before that re-bind the same
   call finds `copy99` in the table, whose file is not the `govkit.py` beside the step module, and
   loads a third engine by path (upgrade_steps.py:2683-2692).

Each label carries `[dSP-99]`, and no label or docstring line opens with an import of `govkit`, so
AC3's grep reads only statements. Under the break, the old `import govkit` body of
`govkit_module()`, check 1 stays green. Check 2 reds because the call answers the copy, check 3 reds
on the import inside `govkit_module()`, and check 4 reds because nothing re-bound the table, so the
step module loads a third engine.

### What it does not cover

S1 re-binds the table when `govkit_module()` is called. A module whose own import of `govkit` first
runs after a staged load and before the next `govkit_module()` call would bind the copy. None does
at `f519c1934`. The suite first imports `step_gate` inside `check_update_safety`
(selftest.py:2130), which `main` calls at selftest.py:5659, before `check_upgrade_steps` at
selftest.py:5663. The import of `govkit` in `upgrade_walk.py` sits inside a function
(upgrade_walk.py:94), and `main` calls `govkit_module()` on the line after it imports that module
(selftest.py:19777-19778). The arm does not grade this case.

The held step module's own `load_govkit()` opens the same window by a second path. It returns the
cached `govkit` only when that module's file is the `govkit.py` beside it, and otherwise loads a
fresh engine by path, with its own `Refusal` (upgrade_steps.py:2675-2692). So any call into the
held engine's step module that reaches `load_govkit()`, `read_registry_at` (upgrade_steps.py:757)
among them, between a staged copy's `load_govkit()` and the next `govkit_module()` call builds a
third engine whose `Refusal` the suite's catchers do not catch. Check 4 grades the window's closing
edge, not the window. None falls in it at `f519c1934`. After 87 AC6's `us87.read_steps`
(selftest.py:3183) the suite calls only `steps.derive_contained_rel` (selftest.py:3194-3195), which
does not call `load_govkit()` (upgrade_steps.py:1059-1068), before `gk72 = govkit_module()` at
selftest.py:3198. The arm's own staged load is followed by check 1, which makes no step call, and
then check 2's `govkit_module()`.

Check 3 reads import statements only. A by-path or `importlib.import_module` load of the engine
added later passes it, and `govkit_mod` (S2) is the one such load at `f519c1934`.

### Inventory

Minted: one module-level name, `GOVKIT_HELD`, the single-slot list. The naming lexicon's cells grade
`py.function` and `py.type` (`.lexicon.conf`), and a module-level list is neither, so no cell
grades it. No function, type, file, flag, conf key, gate leg or receipt field is minted. The arm's
locals take the `99` suffix the suite uses for every unit's locals.

The S2 sites, each changed to read `govkit_module()`:

| Site | At `f519c1934` | After |
|---|---|---|
| `govkit_steps` | selftest.py:127-129 | `return govkit_module().STEPS` |
| `govkit_kind_marks` | selftest.py:138-140 | `return govkit_module().KIND_MARKS` |
| `govkit_update_role` | selftest.py:145-147 | `return govkit_module().UPDATE_ROLE` |
| `main` | selftest.py:5791-5792 | `_G = govkit_module()` |
| `main` | selftest.py:9098-9099 | `govkit = govkit_module()` |
| `main` | selftest.py:9186-9187 | `_gk_mod = govkit_module()` |
| `main` | selftest.py:9561-9562 | `_gk = govkit_module()` |
| `main` | selftest.py:18393-18394 | `_GK = govkit_module()` |
| `main` | selftest.py:18498-18499 | `govkit = govkit_module()` |

Each `main` site's `sys.path.insert` line goes with its import, because `govkit_module()` makes the
insert. The two sites binding a local `govkit` keep it local to `main`, as the import did.

### Migration

None.

### Rollout

Live at landing, at order 16. The suite is the only reader.

### Files touched (estimate)

- `tools/govkit/selftest.py` — S1, S2 and S3.
- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-99-ledger.md` — the
  acceptance ledger.

### Alternatives rejected

- **Restore the module table after each staged load.** That needs one restore at each of the six
  in-process staged loads and the arm's, and the next one added would be forgotten. The read side
  is one function every reader already calls.
- **Load `GOVKIT` afresh on a miss.** It mints a third `Refusal`, as "The held engine" shows.
- **Import the engine once when the suite module loads.** That moves the engine's import before
  every arm's setup, which is a wider change than this defect needs.
- **Change `load_govkit` so a copy does not write the module table.** It is the step module's
  correct behaviour for a copy run as a program, and §3 rules it out.

## 5. Production-readiness checklist

- security: N/A — test harness only. No write path, spawn or surface.
- perf / scale: the held engine saves the repeated `import` lookups. `check_upgrade_steps` ran in
  45 s with S1 and S2 applied, in a scratch clone at `f519c1934`, measured (AC1's `cost:`).
- error / empty / loading states: a missing `govkit.py` raises at the by-path load, as `import`
  did.
- observability: each `[dSP-99]` check prints its detail on FAIL. Check 2 prints the answered
  engine's file.
- risks: an arm that relied on a fresh engine object per call. None does: the old body returned the
  cached module, which is one object, except after a staged load.
- testing: AC1 to AC3, and §7's `New arm:`.
- migration: N/A — no data or state.
- user docs: N/A — no page under `help/` names `govkit_module`.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import pathlib, tempfile, selftest as s; s.check_upgrade_steps(pathlib.Path(tempfile.mkdtemp())); print('FAILURES', s.FAILURES)"`
  runs with the govkit kit directory of a shared clone at the build commit as its working
  directory, it exits 0 and its last line is `FAILURES []`. 87 AC6's staged load and every
  `[dSP-72]` check after it run in that one process.
  Red when: `govkit_module()` is given back its `import govkit` body. At `f519c1934`, which carries
  that body, the run exits 1 with `upgrade_steps.Refusal` raised from the copy's engine at the
  `leaked72` comprehension. This is the review's id 1, measured by the main loop in a clone at
  `390033278`.
  cost: 45 s with S1 and S2 applied in a scratch clone at `f519c1934`, measured.
  fixture: a `git clone --shared` at the build commit, not a linked worktree, with temp files in
  the default temp root and not the session scratchpad.
  permission: scratch-guard's row G3 refuses this command to a role agent whose allowlist does not
  name `govkit selftest`, measured for `gov-spec-writer` on 2026-11-01.
- **AC2** — When
  `python -c "import pathlib, tempfile, selftest as s; s.check_staged_copies(pathlib.Path(tempfile.mkdtemp())); print('FAILURES', s.FAILURES)"`
  runs in the same working directory, it prints four `ok   [dSP-99]` lines and its last line is
  `FAILURES []`.
  Red when: `govkit_module()` is given back its `import govkit` body. Then the first `[dSP-99]`
  check stays `ok`, and the second, third and fourth print `FAIL`. This is derived from §4 "The
  arm" and not measured, because the role that wrote this spec may not run the suite.
  figure: four is PINNED by §4 "The arm".
  fixture: as AC1.
  permission: as AC1.
- **AC3** — When `git grep -n -E "^\s*(import|from) govkit\b" -- "*selftest.py"` runs from the
  repository root at the build commit, it prints nothing and exits 1.
  Red when: any one of S2's nine sites, or the old body of `govkit_module()`, is put back. That line
  is then printed. At `f519c1934` the command prints ten lines: selftest.py:128, 139, 146, 153,
  5792, 9099, 9187, 9562, 18394 and 18499, measured.
  figure: ten is PINNED at `f519c1934`, and AC3 asserts zero.

## 7. Gates

`govkit selftest` · `policy fixtures` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `recall floor` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 AC3 · the four `[dSP-99]` checks of `check_staged_copies`; the break is `govkit_module()` given back its `import govkit` body, under which the second, third and fourth red · none

The first five legs are the non-broad legs whose guards `tools/govkit/selftest.py` trips, and
`recall floor` and `recall floor arms` are tripped by the ledger's `memory/` path. All were printed
by `python tools/check-spec-tokens.py --legs-for` on 2026-11-01 and read against
`tools/gate-legs.json`. `memory hygiene` and `spec tokens (a spec's own names resolve)` carry no
guard and grade this spec and its ledger.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-99-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-99-spec-brief.md`.
  The finding: the close's arm observation at `390033278` found that `check_upgrade_steps` crashes
  at its `[dSP-72]` comprehension after 87 AC6's in-process staged load, because the copy's
  `load_govkit()` displaces `sys.modules["govkit"]` and `govkit_module()` answers that copy. The
  main loop reproduced it in a clone at `390033278`, and so the `govkit selftest` leg reds at HEAD.
  Items: id 1 (high) is S1 and AC1, and id 2 (regression arm) is S3, AC2 and §7's `New arm:`. S2
  widens id 1 to the class the goal names, every reader of the engine in the suite, because the
  helpers and `main` imported the engine by name beside `govkit_module()`. Every cited line was read
  at `f519c1934`.
- rev-2 · 2026-11-01 · §1 · S2 · S3 · §4 · AC2 · §7 · folded the round-1 spec audit
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-99-100-spec-audit-round1.md`
  from the brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-99-audit-fold-brief.md`.
  LOW 1 (ids 3, 5), at the narrowing option the record names as the default: §1 and S2 now claim
  import statements only, S2 names `govkit_mod` at selftest.py:9764-9766 as the by-path load left in
  place, §4 "The held engine" says the same, S3 says check 3 grades import statements only, and
  "What it does not cover" names the by-path gap. Check 3 and AC3 are unchanged. LOW 2 (id 4), at
  the record's preferred fix: a fourth `[dSP-99]` check, that `held99.upgrade_steps.load_govkit()`
  answers `held99` once `govkit_module()` has re-bound the table, with AC2's count, its red case
  and §7's `New arm:` line moved from three to four. "What it does not cover" names the window of
  the step module's own `load_govkit()`. Every newly cited line was read at `6414e1dc6`.
- rev-3 · 2026-11-01 · §3 · the `### Edges` block's two `**consumes-from**` bullets, which memory
  hygiene check 12 graded as unreciprocated by the CLOSED 87 and 71, become `none` and a prose
  paragraph naming both as read-and-closed, per TOOL-dSafePassage-101 S1 and its §4 "The edge
  ruling". No other text changes.

## 10. Reuse audit

The seam is `govkit_module()` itself (selftest.py:150-154), the suite's one accessor for the engine,
which more than eighty call sites already use. S1 changes its body, and S2 routes the nine readers
that bypassed it through it. The identity test and the by-path load are the idiom of
`load_govkit` (upgrade_steps.py:2683-2692) and `load_upgrade_steps` (govkit.py:125-137), applied
to the suite's `GOVKIT`. The arm stages its copy through `build_staged_copy` (selftest.py:3640),
TOOL-dSafePassage-71's helper, and sits in that unit's `check_staged_copies`.
`python tools/codebase-map/reuse_lookup.py "return the one engine module held by identity, re-binding sys.modules after a staged copy replaced it"`
ranked name-stem neighbours only, such as `engine` in two shell tests and `load_kit_module` in
the spec-token checker. None holds a module's identity across a staged load, so no wider seam fits.
`tools/lib/` and `tools/push-main.sh` are not touched. The recall probe ranked
TOOL-dSafePassage-71 first, whose helper this unit reuses, and this unit's own brief.

Recall terms used: `python tools/memory-recall/query.py "govkit_module returns a staged copy's engine after load_govkit overwrote sys.modules govkit, so Refusal is a second class" --terms "govkit_module sys.modules load_govkit staged copy build_staged_copy Refusal identity in process engine re-bind"`
