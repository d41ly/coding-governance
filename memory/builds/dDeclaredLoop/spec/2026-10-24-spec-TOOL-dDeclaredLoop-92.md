# TOOL-dDeclaredLoop-92 — the round-9 spec audit's 17 minors, batched

**Status:** DEFERRED · rev-4 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 46 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-92-deviation-921.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-92-deviation-921.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-92-deviation-922.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-92-deviation-922.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-91 |

<!-- /gen:spec-records -->

## 1. Goal

The round-9 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-89-spec-audit.md`)
exited CONVERGED with 18 confirmed findings over units 89 and 90, the round-8 promotions. Its one high,
id 20, is unit 91. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW.
Each finding keeps its report id and its own scope item, including where the report merged ids into one
item. The minors land on 89 and 90 both, so this unit repairs neither in particular and builds after every
unit (order 46, above 90's and 91's 45).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 4, 9, 15, 17 | S1, S2, S3, S4 |
| M2 | MEDIUM | 1 | S5 |
| M3 | MEDIUM | 2 | S6 |
| M4 | MEDIUM | 3 | S7 |
| M5 | MEDIUM | 14 | S8 |
| M6 | MEDIUM | 21 | S9 |
| L1 | LOW | 7, 12 | S10, S11 |
| L2 | LOW | 5 | S12 |
| L3 | LOW | 6 | S13 |
| L4 | LOW | 8 | S14 |
| L5 | LOW | 11 | S15 |
| L6 | LOW | 16 | S16 |
| L7 | LOW | 22 | S17 |

That is 9 MEDIUM and 8 LOW findings by raw id. Two report items merge ids, and each is fixed once across
its scope items: M1 (S1 to S4) and L1 (S10 and S11). The report's four refuted findings, ids 10, 13, 18 and
19, are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 4. 90's §4 states the shared `tree_lib` loader as a public def this pass mints:
  `load_tree_lib()` in `tools/loop/loop_lib.py`. 90's Write set and Files touched name
  `memory/map/generated/symbols.json`, its §4 gains an `### Inventory` sub-head ahead of Files touched
  naming the symbol row, and its
  sentence that the pass mints no public module-level def is corrected, in this unit's rev bump of 90.
  Observed by AC1.
- **S2** — id 9. 90 S4 says S4 mints `load_tree_lib`, which no code holds at base, in the rev bump of 90.
  `tools/loop/loop_lib.py` defines `load_tree_lib` at module level, written by this unit where absent.
  Observed by AC2.
- **S3** — id 15. `load_tree_lib` is the one place in `tools/loop/loop_lib.py` that resolves `tree_lib`.
  `derive_conf_reads` and `derive_conf_constants` each call it and resolve nothing inline. 90 S4 and 90 §10
  say the loader is extracted from 86 S21's inline route at its second caller, in place of "86 S21's
  route, extended in place", in the rev bump of 90. Observed by AC3.
- **S4** — id 17. 90 §7's leg line names `codebase-map coverage + freshness`, in the rev bump of 90. This
  pass regenerates `memory/map/generated/symbols.json` once, so it holds the `load_tree_lib` row.
  Observed by AC4.
- **S5** — id 1. 90 S3 points at the two sentences that hold the claim: 88 §3's consumes-from 87 bullet
  and 87 §3's hands-off 88 bullet, in the rev bump of 90. Neither bullet carries the phrase
  "answer unchanged" any longer: each says the slice answers 87 S1's whole rule-2 predicate, written by
  this unit in its rev bumps of 87 and 88. 90 AC3 gains the matching greps. Observed by AC5.
- **S6** — id 2. 87 §3's first non-goal no longer says the lift "moves no answer AC2 reads". It says S1's
  class is charge rule 2's whole predicate, annotations and targets included, written by this unit where
  90 S1 left it standing, in the rev bump of 87. 90 AC1 gains the range check over 87 §3. Observed by AC6.
- **S7** — id 3. The `no-own-conf-read` plant of `tools/loop/budget.py` runs 90 S5's version-skew row on
  its own run and prints its label, `tree_lib lacking derive_constant_charges`. The row passes when its
  scratch copy refuses by name, so the unmodified plant exits 0 with the label in its output. 90 AC5 and
  its §7 arm are restated to observe the row, with the hand-made scratch copy kept as a second half
  observing 90 S4, in the rev bump of 90. Observed by AC7.
- **S8** — id 14. `tools/loop/loop_witness.py` takes `GIT_ENV_LEAKS` from the module that
  `loop_lib.load_tree_lib()` answers, imported as a sibling from its own directory, and resolves
  `tree_lib` no other way. `TREE_LIB_SYMBOLS` holds `derive_docstring_ids`, `derive_constant_charges` and
  `GIT_ENV_LEAKS`. 90 S4 and AC4 say so, and 75 S35 names the loader as its route, in the rev bumps of 90
  and 75. Observed by AC8.
- **S9** — id 21. 89 AC4 runs one grep per priced form over 87's `awk '/^## 3/,/^### Edges/'` range, each
  printing at least 1: `except`, `capture`, `globals()`, `setattr`, `import` and the backticked `def`. Its
  single alternation grep is gone, in this unit's rev bump of 89. Observed by AC9.
- **S10** — id 7. 90 AC1's figure says the second grep prints 3 at HEAD, in the rev bump of 90. Observed
  by AC10.
- **S11** — id 12. The same figure names the three lines it counts: 87 S1, the sketch's walk header and
  the sketch's value walk, in the rev bump of 90. Observed by AC10.
- **S12** — id 5. 88 S13 and 88's sketch "The lifted charge walk (S13)" name TOOL-dTrueNorth-23's AC5 arm,
  `_scan_table23`, as a consumer the lift keeps green, written by this unit where absent, in the rev bump
  of 88. 90 AC12 gains the two positive greps. Observed by AC11.
- **S13** — id 6. 90 AC11's half over 88's criteria is a command per criterion rather than a sentence, in
  the rev bump of 90. 88 AC1, AC6, AC12, AC13 and AC16 each carry the range grep 90 S11 orders, written by
  this unit where absent, in the rev bump of 88. Observed by AC12.
- **S14** — id 8. 89 S3's `with`-held loader row is shown as a multi-line block, as
  `tools/memory-tree/merge-rows.py:302-323` writes the idiom, in the rev bump of 89. The plant row in
  `tools/loop/budget.py` is written across lines. Observed by AC13.
- **S15** — id 11. 90 §4 Evidence and 90 §8 F4 cite 75 by anchor, 75 §6 AC27 and 75 §7's
  `New arm: tools/loop/guard.py` line, and carry no line number for either, in the rev bump of 90.
  Observed by AC14.
- **S16** — id 16. 89 S4's list of restatement sites names 87 §10 and 86 §10, and 89 AC3 gains their range
  greps, in the rev bump of 89. 87 §10 and 86 §10 each name `derive_conf_rebinds`, written by this unit
  where absent, in its rev bumps of 87 and 86. Observed by AC15.
- **S17** — id 22. `build_failure_detail` in `tools/loop/guard.py` spells an `OSError` as
  `start failed: <detail>`, the detail being the first non-empty of the stripped `strerror`, the stripped
  `str(exc)` and the exception's class name. The `push-merge-tree-fatal` plant gains an `OSError()` row
  and an `OSError(5, '')` row. 90 S21 and AC21 and 88 S24 say so, in the rev bumps of 90 and 88.
  Observed by AC16.

## 3. Non-goals (OUT)

- The high's mechanism, the module-scope positions of `derive_conf_rebinds`: unit 91.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- Rewriting a passage a sibling unit already wrote as this unit's item states. An item whose target reads
  as stated is observed and recorded, never rewritten.
- A `tree_lib` symbol check in any kit but `tools/loop/`. S8 covers the loop kit's two routes, and the
  loader is that kit's.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-89` — S3's `with`-held row, S4's restatement sites and AC3 and AC4, which S9, S14 and S16 restate (ids 8, 16, 21)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S3, S4, S5, S11, S12, S21, §4's Write set, sketch, Evidence and Files touched, §7, §8 F4, §10, AC1, AC3, AC4, AC5, AC11, AC12 and AC21, with `load_tree_lib`, `TREE_LIB_SYMBOLS` and `build_failure_detail` as that unit builds them (ids 1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 14, 15, 17, 22)
- **consumes-from** `TOOL-dDeclaredLoop-91` — 87 §3's binding-form bullet as that unit restates it, whose per-form tokens S9's criterion reads
- **consumes-from** `TOOL-dDeclaredLoop-87` — §3's first non-goal, §3's hands-off 88 bullet and §10, which S5, S6 and S16 restate (ids 1, 2, 16)
- **consumes-from** `TOOL-dDeclaredLoop-88` — §3's consumes-from 87 bullet, S13, S24, the lifted-walk sketch and AC1, AC6, AC12, AC13 and AC16, which S5, S12, S13 and S17 restate (ids 1, 5, 6, 22)
- **consumes-from** `TOOL-dDeclaredLoop-86` — §10, which S16 completes with `derive_conf_rebinds` (id 16)
- **consumes-from** `TOOL-dDeclaredLoop-75` — S35's `GIT_ENV_LEAKS` route in `tools/loop/loop_witness.py`, which S8 moves onto the loader (id 14)
- **hands-off** `TOOL-dDeclaredLoop-93` — AC16, whose exit code for the `push-merge-tree-fatal` plant that unit restates to 1, as 81 AC3 states (the round-10 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-94` — S3, S6, S7, S8, S9, S17, §4's sketches, §5, §10, AC5, AC6, AC8, AC9 and AC16, with `load_tree_lib`, `TREE_LIB_SYMBOLS` and `build_failure_detail`, which that unit restates and completes (the round-10 spec audit's ids 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 29)
- **hands-off** `TOOL-dDeclaredLoop-95` — `load_tree_lib`, S8 and its sketch "The tree_lib route, after this unit", whose tuple that unit restates with `parse_conf` (the round-11 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-96` — S3, S7, S8, S17, AC8, AC16, §5 and the sketch "The tree_lib route, after this unit", which that unit restates (the round-11 spec audit's ids 2, 5, 10, 16, 17)
- **hands-off** `TOOL-dDeclaredLoop-100` — §5 and the sketch "The tree_lib route, after this unit", which that unit restates (the round-12 spec audit's ids 4, 17, 18)

## 4. Design

### Write set

This pass writes `tools/loop/loop_lib.py` (S2, S3, S8), `tools/loop/loop_witness.py` (S8),
`tools/loop/budget.py` (S7, S14), `tools/loop/guard.py` (S17) and `memory/map/generated/symbols.json`
(S4). Inside this build's folder it amends the specs of 75, 86, 87, 88, 89 and 90 as rev bumps, one per
spec, each with its §9 line. The build README's regions are the generator's render. S5, S6, S12, S13 and
S16 also observe and record where the sibling text already reads as stated.

### The tree_lib route, after this unit (S1 to S4, S8)

```
TREE_LIB_SYMBOLS = ("derive_docstring_ids", "derive_constant_charges", "GIT_ENV_LEAKS")

def load_tree_lib():                       # public: loop_witness.py calls it too, so symbols.json gains a row
    kit = resolve_kit_dir("memory-tree", "tree_lib.py", here)   # LookupError -> 88 S33's refusal
    tl  = load tree_lib.py from kit                             # ImportError | SyntaxError -> 88 S33's refusal
    for name in TREE_LIB_SYMBOLS:
        if not hasattr(tl, name): refuse "tree_lib lacks <name>: govkit update --kits memory-tree"
    return tl

derive_conf_reads(...):     tl = load_tree_lib()     # 86 S21's inline resolve, extracted
derive_conf_constants(...): tl = load_tree_lib()
loop_witness.py:            GIT_ENV_LEAKS = loop_lib.load_tree_lib().GIT_ENV_LEAKS   # 75 S35's route
```

### The OSError detail, after this unit (S17)

```
detail = first non-empty of (strip(exc.strerror or ""), strip(str(exc)), type(exc).__name__)
OSError("boom")                 -> start failed: boom
FileNotFoundError(2, "No such file") -> start failed: No such file
OSError(5, "")                  -> start failed: [Errno 5]
OSError()                       -> start failed: OSError
```

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- The codebase-map symbol tier records every module-level `FunctionDef` whose name does not start with an
  underscore (`tools/codebase-map/map_lib.py:350-353`). `memory/map/generated/symbols.json` keys each row
  by `id`, `kind` and the repo-relative `file`, as its `read_kit_conf` row shows
  (`tools/memory-tree/merge-rows.py`).
- `GIT_ENV_LEAKS` is a module-level tuple of `tools/memory-tree/tree_lib.py:262`. 75 S35 routes
  `loop_witness.py` to it through `resolve_kit_dir`, outside 90's loader.
- `python -I` printed `''` for `str(OSError())`, `None` for its `strerror`, `'[Errno 5] '` for
  `str(OSError(5, ''))` and `''` for its `strerror`.
- `merge-rows.py`'s `read_kit_conf` spans lines 302-323, its `global _KIT_CONF` at 311.
- Baselines over `memory/builds/dDeclaredLoop/spec/`, each grep as its criterion states:
  - `answer unchanged` prints 1 over 87 (line 79) and 1 over 88 (line 221);
  - over 87's `awk '/^## 3/,/^### Edges/'` range, `moves no answer` prints 1 and `annotation` prints 0, and
    each of S9's six tokens prints 0;
  - over 90, `391 and 432` prints 2, `mints no public` prints 1 in the Write set, and Files touched holds
    no `symbols.json`;
  - over 90's AC1 range `prints 2 at HEAD` prints 1, and over 89's AC4 range the alternation prints 1;
  - over 87 §10 and 86 §10 `derive_conf_rebinds` prints 0, and over 88's S13 range and lifted-walk sketch
    `_scan_table23` prints 0;
  - over 88's AC1, AC6, AC12, AC13 and AC16 ranges, each of AC12's tokens prints 0.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/loop_witness.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `memory/map/generated/symbols.json`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the 89 minors and the 90 minors.** The halves are not disjoint by M6. Both write
  `tools/loop/budget.py` (S7 and S14) and the 87 spec (S5, S6 and S16), which is clause 1. Each half
  re-renders the build README's units region, a generated index written with its generator, which is
  clause 3.
- **A private `_load_tree_lib` (M1's option a).** S8 puts a second module on the loader, and a private
  name read from a sibling module is a public interface without the symbol row that would show it.
- **Pricing 75 S35's route as a non-goal (M5's alternative).** It leaves `loop_witness.py` ending in an
  `ImportError` traceback against a memory-tree kit older than 2026-10-22, the skew 90 S5 targets.

## 5. Production-readiness checklist

- security — S8 turns a version skew in a second module into the named refusal. S17 keeps a refusal's
  reason non-empty.
- perf / scale — none: the loader checks three attributes once per run.
- error / empty / loading states — S7 and S8 name a `tree_lib` lacking any symbol the kit reads; S17
  names an `OSError` with no message.
- observability — each refusal names the missing symbol or the failure, and the skew row names itself.
- risks — the amendments land on specs whose units build before this one, as 90 amends its siblings;
  each is a rev bump with its §9 line. A public `load_tree_lib` is one more symbol row to keep fresh, and
  §7 names the leg that holds it.
- testing — AC1 to AC16 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: every reader is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `awk '/^### Write set/,/^### Evidence/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md` is piped to
  `grep -c "mints no public"`, it prints 0. `awk '/^### Files touched/,/^### Alternatives/'` and
  `awk '/^### Inventory/,/^### Files touched/'` over the same file, each piped to `grep -c "symbols.json"`, each print
  at least 1.
  Red when: 90 still says no public def is minted beside a sketch that mints one.
  figure: the first grep prints 1 at HEAD and the second 0, PINNED 2026-10-24.
- **AC2** — When `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'` over the 90 spec is piped to `grep -c "mints"`, it
  prints at least 1. A `python -c` probe in `tools/loop/` that imports `loop_lib` finds
  `loop_lib.load_tree_lib` a function defined in `loop_lib.py` at module level.
  Red when: the builder takes the loader for existing code and no module-level def is written.
- **AC3** — When `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'` over the 90 spec is piped to
  `grep -c "extended in place"`, it prints 0, and `awk '/^## 10/,0'` over it piped to
  `grep -c "load_tree_lib"` prints at least 1. A `python -c` probe parsing `loop_lib.py` in `tools/loop/` finds
  the str constant `tree_lib.py` inside `load_tree_lib` alone, and a call to `load_tree_lib` inside each of
  `derive_conf_reads` and `derive_conf_constants`.
  Red when: a second inline resolve of `tree_lib` survives beside the loader.
- **AC4** — When `awk '/^## 7/,/^## 8/'` over the 90 spec is piped to
  `grep -c "codebase-map coverage + freshness"`, it prints at least 1. A `python -c` probe loading
  `memory/map/generated/symbols.json` finds a row whose `id` is `load_tree_lib` and whose `file` is
  the loop kit's `loop_lib.py`.
  Red when: the public loader is minted and the symbol tier goes stale outside the unit's write set.
- **AC5** — When `grep -c "answer unchanged"` runs over the 87 spec and over the 88 spec, each prints 0.
  `awk '/^- \*\*S3\*\*/,/^- \*\*S4\*\*/'` over the 90 spec piped to `grep -c "Edges"` prints at least 1.
  Red when: both edge bullets still claim the answer is unchanged beside a slice that answers more names.
  figure: each of the first two greps prints 1 at HEAD, PINNED 2026-10-24.
- **AC6** — When `awk '/^## 3/,/^### Edges/'` over the 87 spec is piped to `grep -c "moves no answer"`, it
  prints 0, and piped to `grep -c "annotation"`, it prints at least 1.
  `awk '/^- \*\*AC1\*\*/,/^- \*\*AC2\*\*/'` over the 90 spec piped to `grep -c "moves no answer"` prints at
  least 1.
  Red when: 87 §3 keeps the false equality with every criterion of 89 and 90 green.
  figure: over 87 the two greps print 1 and 0 at HEAD, PINNED 2026-10-24.
- **AC7** — When `python budget.py --fixture --plant no-own-conf-read` runs in `tools/loop/`, it exits 0 and
  prints `tree_lib lacking derive_constant_charges`.
  Red when: the skew row is absent, so a build that ships the loader without the row still passes.
- **AC8** — When a `python -c` probe parses every `*.py` under `tools/loop/`, no file but `loop_lib.py`
  holds an `import tree_lib`, a `from tree_lib` or the str constant `tree_lib.py`, and every attribute read
  off a name that a `load_tree_lib()` call binds is in `loop_lib.TREE_LIB_SYMBOLS`. A second probe, over a
  scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's scratch directory
  whose `tree_lib.py` lacks `GIT_ENV_LEAKS`, calls `loop_lib.load_tree_lib()` and exits non-zero printing
  `GIT_ENV_LEAKS` and `govkit update --kits memory-tree`, with no `Traceback`.
  Red when: `loop_witness.py` reaches `tree_lib` outside the loader, or the tuple omits a name it reads.
  figure: the attribute set is DERIVED from the files at observation time.
- **AC9** — When `awk '/^- \*\*AC4\*\*/,/^## 7/'` over the 89 spec is piped to `grep -cF 'except\|capture'`,
  it prints 0, and piped to `grep -c "setattr"`, it prints at least 1. Each of `except`, `capture`,
  `globals()`, `setattr`, `import` and the backticked `def`, grepped with `grep -cF` over 87's
  `awk '/^## 3/,/^### Edges/'` range, prints at least 1.
  Red when: one priced form satisfies the criterion for five.
  figure: the alternation prints 1 over 89 and each token 0 over 87 at HEAD, PINNED 2026-10-24.
- **AC10** — When `awk '/^- \*\*AC1\*\*/,/^- \*\*AC2\*\*/'` over the 90 spec is piped to
  `grep -c "prints 2 at HEAD"`, it prints 0, and piped to `grep -c "prints 3 at HEAD"` and to
  `grep -c "value walk"`, each prints at least 1.
  Red when: the pinned figure disagrees with the grep it pins.
- **AC11** — When `awk '/^### The lifted charge walk/,/^### Evidence/'` and
  `awk '/^- \*\*S13\*\*/,/^- \*\*S14\*\*/'` over the 88 spec are each piped to `grep -c "_scan_table23"`,
  each prints at least 1, and `awk '/^- \*\*AC12\*\*/,/^- \*\*AC13\*\*/'` over the 90 spec piped to the same
  grep prints at least 1.
  Red when: 88 stays silent about the selftest arm that scans the walker.
- **AC12** — When each 88 range below is piped to its `grep -cF`, each prints at least 1:
  `awk '/^- \*\*AC1\*\*/,/^- \*\*AC2\*\*/'` with `S1\*\*/`; `awk '/^- \*\*AC6\*\*/,/^- \*\*AC7\*\*/'` with
  `same object`; `awk '/^- \*\*AC12\*\*/,/^- \*\*AC13\*\*/'` with `## 10`;
  `awk '/^- \*\*AC13\*\*/,/^- \*\*AC14\*\*/'` with `## 10`; and `awk '/^- \*\*AC16\*\*/,/^- \*\*AC17\*\*/'`
  with `S2\*\*/`. `awk '/^- \*\*AC11\*\*/,/^- \*\*AC12\*\*/'` over the 90 spec piped to
  `grep -c "each name their sibling"` prints 0.
  Red when: 88's criteria never gain the greps and no criterion fails.
  figure: each 88 grep prints 0 at HEAD and the 90 grep 1, PINNED 2026-10-24.
- **AC13** — When `awk '/^- \*\*S3\*\*/,/^- \*\*S4\*\*/'` over the 89 spec is piped to
  `grep -cF 'global KIT_CONF; with'`, it prints 0. `python budget.py --fixture --plant conf-read-forms` in
  `tools/loop/` exits 0 with its `KIT_CONF` row answering one `conf constant` hit.
  Red when: the row is pasted as written and the plant answers the unparseable-`loop_lib` refusal.
- **AC14** — When `grep -c "391 and 432"` runs over the 90 spec, it prints 0, and
  `awk '/^### Evidence/,/^### Files touched/'` over it piped to `grep -c "75 §6 AC27"` prints at least 1.
  Red when: a reader checking 90's citation lands one line off 75's criterion and arm.
  figure: the first grep prints 2 at HEAD, PINNED 2026-10-24.
- **AC15** — When `awk '/^## 10/,0'` over the 87 spec and over the 86 spec is each piped to
  `grep -c "derive_conf_rebinds"`, each prints at least 1, and `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'` over the
  89 spec piped to `grep -c "§10"` prints at least 1.
  Red when: 87 §10 and 86 §10 describe the binding set without the rebinding pass.
- **AC16** — When a `python -c` probe imports `guard` from `tools/loop/` and calls `build_failure_detail` on
  `OSError()`, `OSError(5, '')`, `OSError("boom")` and `FileNotFoundError(2, "No such file")`, it answers
  `start failed: OSError`, `start failed: [Errno 5]`, `start failed: boom` and
  `start failed: No such file`. `python guard.py --fixture --plant push-merge-tree-fatal` exits 0 with its
  `OSError()` row printing `the clean re-merge failed: start failed: OSError`.
  Red when: a bare `OSError` renders `start failed: ` with nothing after it.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop guard fixtures` and `loop computed witness`, none a leg at
HEAD.

New arm: tools/loop/budget.py · covers AC7 · the no-own-conf-read version-skew row named in the plant's output, staged with the row absent from the plant · none
New arm: tools/loop/guard.py · covers AC16 · the OSError() and OSError(5, '') rows of push-merge-tree-fatal, staged with the strerror-then-str spelling · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — A private or a public loader (ids 4, 9, 15, 17)?** (a) `_load_tree_lib`, keeping
  `symbols.json` unmoved; (b) the public `load_tree_lib`, with its symbol row, the freshness leg and the
  corrected Write set. The report judged both sound. S8 puts `loop_witness.py` on the loader, so under (a)
  a sibling module reads a private name across modules, an interface the symbol tier cannot see. (b)
  satisfies every criterion (a) would and states that interface. RESOLVED (agent, 2026-10-24, delegated):
  (b), S1 to S4. widens: none · relaxes: none
- **F3 — Move `loop_witness.py` onto the loader, or price its route (id 14)?** (a) move it and add
  `GIT_ENV_LEAKS` to the tuple; (b) name 75 S35's route as a priced non-goal. (b) leaves an
  `ImportError` traceback on the skew path. RESOLVED (agent, 2026-10-24, delegated): (a), S8.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-9 spec audit's 17 minors batched (9 MEDIUM, 8 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-93 and TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-95 and TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy. These are 90's `tree_lib` loader,
extracted from 86 S21's inline route at its second caller (S1 to S4, S8), the `no-own-conf-read` and
`conf-read-forms` plants of `budget.py` (S7, S14), and 88 S24's `build_failure_detail` (S17).
`python tools/codebase-map/reuse_lookup.py "load a sibling kit module and refuse when it lacks a needed name"`
ranked `load`, `load_conf`, `need`, `kit_rel` and `resolve_kit_dir`. `resolve_kit_dir` is the locator the
loader already calls, `need` is a merge-bar grep for a version constant, and none checks a loaded
module's names, so no existing seam fits the symbol check beyond the loader itself. The memory-recall
query returned the round-9 report's M5 and `TOOL-aEvidencedLens-20`, an earlier minors batch.

Recall terms used: load_tree_lib TREE_LIB_SYMBOLS symbols.json codebase-map freshness loop_witness GIT_ENV_LEAKS build_failure_detail strerror minors batch
