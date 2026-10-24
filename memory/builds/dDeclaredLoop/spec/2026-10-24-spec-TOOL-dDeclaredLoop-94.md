# TOOL-dDeclaredLoop-94 — the round-10 spec audit's 24 minors, batched

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 48 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-94-deviation-941.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-94-deviation-941.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-93 |

<!-- /gen:spec-records -->

## 1. Goal

The round-10 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md`)
exited CONVERGED with 25 confirmed findings over units 91 and 92, the round-9 promotions. Its one high,
id 1, is unit 93. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW.
Each finding keeps its report id and its own scope item, including where the report merged ids into one
item. The minors land on 91 and 92 both, so this unit repairs neither in particular and builds after every
unit (order 48, above 93's 47).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2, 12, 15 | S1, S2, S3 |
| M2 | MEDIUM | 3, 17, 21 | S4, S5, S6 |
| M3 | MEDIUM | 22 | S7 |
| M4 | MEDIUM | 23 | S8 |
| M5 | MEDIUM | 4 | S9 |
| M6 | MEDIUM | 24 | S10 |
| M7 | MEDIUM | 27, 19 | S11, S12 |
| M8 | MEDIUM | 10 | S13 |
| M9 | MEDIUM | 11 | S14 |
| L1 | LOW | 6 | S15 |
| L2 | LOW | 7 | S16 |
| L3 | LOW | 8 | S17 |
| L4 | LOW | 9 | S18 |
| L5 | LOW | 13, 29 | S19, S20 |
| L6 | LOW | 14 | S21 |
| L7 | LOW | 16 | S22 |
| L8 | LOW | 20 | S23 |
| L9 | LOW | 25 | S24 |

That is 14 MEDIUM and 10 LOW findings by raw id. Four report items merge ids, and each is fixed once
across its scope items: M1 (S1 to S3), M2 (S4 to S6), M7 (S11 and S12) and L5 (S19 and S20). The report's
four refuted findings, ids 5, 18, 26 and 28, are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 2. 92 AC8's first probe bans the resolution FORMS of §4 "The tree_lib route probe", not the
  str constant `tree_lib.py`. A module name matches by equality and a path by its `tree_lib.py` suffix, and
  a docstring or a plain str naming the file is no hit. In this unit's rev bump of 92. Observed by AC1.
- **S2** — id 12. The version-skew row of `tools/loop/budget.py` (92 S7) finds the memory-tree kit it
  copies as the directory of `loop_lib.load_tree_lib(need=()).__file__`, and calls no `resolve_kit_dir`
  of its own. This pass writes that where 92's pass located the kit another way. Observed by AC1.
- **S3** — id 15. 92 S8 and 92's sketch "The tree_lib route, after this unit" name the skew row of
  `budget.py` as a third caller of the loader, in the rev bump of 92. Observed by AC2.
- **S4** — id 3. 92 AC8's attribute population is every non-dunder `ast.Attribute` whose value is a
  `load_tree_lib(...)` Call, or a Name bound from one in the same function or module body, and every
  `getattr` on either with a str Constant name. The criterion states that the population is non-empty
  and holds `GIT_ENV_LEAKS` read in `loop_witness.py`, in the rev bump of 92. Observed by AC1.
- **S5** — id 17. No `load_tree_lib(...)` Call, and no Name bound from one, is an argument of another
  call but `getattr` anywhere under `tools/loop/`, so a helper parameter cannot hide a read from S4's
  population. 92 AC8 states it, in the rev bump of 92. Observed by AC1, AC3.
- **S6** — id 21. 92 AC8 carries a staged break: a scratch `loop_witness.py` that reads
  `loop_lib.load_tree_lib(need=("GIT_ENV_LEAKS",)).derive_X` turns the probe red naming `derive_X`, in the
  rev bump of 92. Observed by AC3.
- **S7** — id 22. The banned forms outside `loop_lib.load_tree_lib` are an `import` or `from` of the module
  `tree_lib`; an `import_module` or `__import__` call whose first argument is the str `tree_lib`; any
  `resolve_kit_dir` call whose first argument is the str `memory-tree`; and a `spec_from_file_location` or
  `SourceFileLoader` call any of whose str arguments ends in `tree_lib.py`. 92 AC8 carries a staged
  `importlib.import_module("tree_lib")` that turns it red, in the rev bump of 92. Observed by AC1, AC3.
- **S8** — id 23. `tools/loop/loop_witness.py` calls the loader inside the function that reads
  `GIT_ENV_LEAKS`, at first use, so importing the module resolves nothing. Over a scratch copy whose
  `tree_lib.py` lacks `GIT_ENV_LEAKS`, its `--selftest` exits non-zero with the named refusal and no
  `Traceback`. 92 S8 and 92 §5 "error / empty / loading states" say both, in the rev bump of 92. This
  pass moves a module-level call where 92's pass left one. Observed by AC4.
- **S9** — id 4. 92 AC8 and AC16 gain the range greps for the rewrites 92 S8 and S17 order: 75's S35 range
  for `load_tree_lib`, 90's S4 range for `GIT_ENV_LEAKS`, and 88's S24 and 90's S21 ranges for
  `class name`. Each prints at least 1. Each figure is pinned at 0 at HEAD, in the rev bump of 92.
  Observed by AC5.
- **S10** — id 24. 90's sketch "The tree_lib route, after this unit" declares the three-name
  `TREE_LIB_SYMBOLS`, and 89's sketch "The conf-constant class, after this unit" reaches `tree_lib`
  through `load_tree_lib`. 92 S8 and S3 name both sketch lines as restatement sites, in the rev bump of
  92. This pass writes each line where 92's pass left it standing, in the rev bumps of 90 and 89. Observed
  by AC6.
- **S11** — id 27. 89's sketch "The conf-constant class, after this unit" states `derive_conf_rebinds` as
  91 S1 and S2 build it: `FunctionDef`, `AsyncFunctionDef` and `ClassDef` loaders, and the module-scope
  walk descending `_MODULE_SCOPE_PARTS`. Its line "never entering FunctionDef | AsyncFunctionDef |
  ClassDef | Lambda" is gone. In the rev bump of 89. Observed by AC7.
- **S12** — id 19. 89 §3's charging-by-scope bullet reads "a function's or a class's whole subtree".
  89 §5 risks and the 87 §5 risks line that 89 S5 writes each name "a function or a class whose subtree"
  holds a conf name. 91 S5 lists 89's sketch, 89 §3, 89 §5 and 87 §5 among its restatement sites, and 91
  AC4 gains their greps. In the rev bumps of 89, 87 and 91. Observed by AC8.
- **S13** — id 10. 91 AC3 copies `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, empties `_MODULE_SCOPE_PARTS` in the copy's `loop/loop_lib.py` and runs the plant from
  the copy's `loop/`. Its output names `DCONF` as missed and carries no `govkit update --kits memory-tree`.
  In the rev bump of 91. Observed by AC9.
- **S14** — id 11. 92 S17 says the `push-merge-tree-fatal` plant still exits 1, as 88 S18 and AC18 state,
  in the rev bump of 92. 88 AC18 keeps observing the rc-128 row alone, and the `OSError()` row stays 92
  AC16's. Observed by AC10.
- **S15** — id 6. 92 AC6's `annotation` half reads 87's first non-goal alone, the range
  `awk '/^## 3/,/^- A binding whose value/'`, and greps `whole predicate`, the token 92 S6 dictates, beside
  `annotation`. In the rev bump of 92. Observed by AC11.
- **S16** — id 7. 92 S9 and AC9 grep the sixth priced form, the `type` statement, as `type. statement`, and
  AC9's Red-when says six forms. In the rev bump of 92. Observed by AC12.
- **S17** — id 8. 92 AC9's half over 87's range is labelled a regression re-observation of 89 S5 and 91 S5,
  and its figure is pinned as the state after order 45. The half over 89's AC4 range is the one that decides
  S9. In the rev bump of 92. Observed by AC12.
- **S18** — id 9. 92 AC5's half over 90's S3 range greps `hands-off 88` and `consumes-from 87`, the words 92
  S5 dictates, in place of `Edges`. In the rev bump of 92. Observed by AC13.
- **S19** — id 13. 92 AC16 calls `build_failure_detail` on each exception with empty text and
  `(no output)`, the signature 88 S24 fixes, as 90 AC21 does. In the rev bump of 92. Observed by AC14.
- **S20** — id 29. `build_failure_detail` in `tools/loop/guard.py` takes the first non-blank line of the
  chosen `OSError` detail. The `push-merge-tree-fatal` plant gains an `OSError("a\nb")` row whose refusal
  reads `the clean re-merge failed: start failed: a`. 92 S17 and its sketch "The OSError detail, after this
  unit" say so, in the rev bump of 92. Observed by AC14, AC15.
- **S21** — id 14. `load_tree_lib` follows the idiom of `row_grammar.load_recall_kit`, carried inline because
  the loop kit is copy-installed. It sets `sys.dont_write_bytecode` before the import, catches any
  `Exception` the import raises into a refusal naming the exception class, and names every missing symbol
  in one refusal. 92's §10 names `tools/memory-tree/row_grammar.py`'s `load_recall_kit` and
  `tools/check-spec-tokens.py`'s `load_kit_module`, and 92's sketch shows the idiom, in the rev bump of 92.
  Observed by AC16.
- **S22** — id 16. `load_tree_lib` takes `need`, the names its caller reads, defaulting to
  `TREE_LIB_SYMBOLS`, the union every caller may read. A `need` is a literal tuple of str and a subset of
  that union. `loop_witness.py` passes `("GIT_ENV_LEAKS",)`, so a memory-tree kit lacking a `derive_*` name
  does not stop the criterion runner or the `loop computed witness` leg. 92 S8 and 92 §5 risks say so, in
  the rev bump of 92. Observed by AC1, AC4.
- **S23** — id 20. 85 S3, 86 S22 and 88 AC24 state an `OSError` detail as 92 S17 fixes it and point at 88
  S24's builder, in the rev bumps of 85, 86 and 88. 92 S17 names the three sites, in the rev bump of 92.
  Observed by AC17.
- **S24** — id 25. The skew row of `budget.py` copies into a fresh `tempfile.TemporaryDirectory()` outside
  the repository, one per run, cleaned up when the row ends whether it passes or fails. 92 S7 says so, 92 §5
  "perf / scale" prices a copy of about 3.3 MB per run, and 92 §5 "security" names the write surface, in
  the rev bump of 92. Observed by AC18.

## 3. Non-goals (OUT)

- The high's mechanism, 92 AC16's exit code: unit 93. S14 adds the sibling citation in 92 S17 and nothing
  in AC16's exit claim.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- Rewriting a passage a sibling unit already wrote as this unit's item states. An item whose target reads as
  stated is observed and recorded, never rewritten.
- A `tree_lib` loader in any kit but `tools/loop/`, and a change to 88 AC18's rows.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-92` — S3, S6, S7, S8, S9, S17, §4's sketches, §5, §10, AC5, AC6, AC8, AC9 and AC16, with `load_tree_lib`, `TREE_LIB_SYMBOLS`, the skew row of `budget.py`, the `loop_witness.py` route and `build_failure_detail` as that unit builds them (the round-10 spec audit's ids 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 29)
- **consumes-from** `TOOL-dDeclaredLoop-93` — 92 AC16 as that unit restates it to exit 1, and its exit-claim probe, which AC10 re-runs (the round-10 spec audit's id 11)
- **consumes-from** `TOOL-dDeclaredLoop-91` — S5, AC3 and AC4, which S12 and S13 restate (the round-10 spec audit's ids 10, 19, 27)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S4, S21 and the sketch "The tree_lib route, after this unit", whose tuple line S10 restates and whose ranges S9 greps (the round-10 spec audit's ids 4, 24)
- **consumes-from** `TOOL-dDeclaredLoop-89` — the sketch "The conf-constant class, after this unit", §3's charging-by-scope bullet and §5 risks, which S10, S11 and S12 restate (the round-10 spec audit's ids 19, 24, 27)
- **consumes-from** `TOOL-dDeclaredLoop-88` — S18, AC18, S24 and AC24, which S14 cites, S9 greps and S23 restates (the round-10 spec audit's ids 4, 11, 20)
- **consumes-from** `TOOL-dDeclaredLoop-87` — §3's first non-goal, which S15's grep reads, and the §5 risks line 89 S5 writes, which S12 restates (the round-10 spec audit's ids 6, 19)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S22's `OSError` spelling, which S23 restates (the round-10 spec audit's id 20)
- **consumes-from** `TOOL-dDeclaredLoop-85` — S3's `OSError` spelling, which S23 restates (the round-10 spec audit's id 20)
- **consumes-from** `TOOL-dDeclaredLoop-75` — S35 as 92 S8 restates it onto the loader, which S9's grep reads (the round-10 spec audit's id 4)
- **hands-off** `TOOL-dDeclaredLoop-95` — AC1's tree_lib route probe, §4's sketch "The tree_lib route, after this unit" and §5, which that unit makes hold on the built tree (the round-11 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-96` — S2, S5, S8, S10, S21, S22, S24, §3's Edges, §4's sketch and probe, §5, AC2, AC3, AC6, AC10 and AC18, with the skew row of `budget.py` and `load_tree_lib`, which that unit restates and completes (the round-11 spec audit's ids 2, 3, 4, 5, 7, 9, 10, 12, 13, 14, 15, 16, 17)

## 4. Design

### Write set

This pass writes `tools/loop/loop_lib.py` (S21, S22), `tools/loop/loop_witness.py` (S8, S22),
`tools/loop/budget.py` (S2, S24) and `tools/loop/guard.py` (S20). Inside this build's folder it amends the
specs of 85, 86, 87, 88, 89, 90, 91 and 92 as rev bumps, one per spec, each with its §9 line. The build
README's regions are the generator's render. `load_tree_lib` keeps its symbol row, because a keyword
parameter moves no `id`, `kind` or `file`, so `memory/map/generated/symbols.json` does not move.

### The tree_lib route, after this unit (S2, S8, S21, S22)

```
TREE_LIB_SYMBOLS = ("derive_docstring_ids", "derive_constant_charges", "GIT_ENV_LEAKS")   # the union

def load_tree_lib(need=TREE_LIB_SYMBOLS):          # row_grammar.load_recall_kit's idiom, inline
    kit = resolve_kit_dir("memory-tree", "tree_lib.py", here)   # LookupError -> 88 S33's refusal
    sys.dont_write_bytecode = True                              # no __pycache__ in the memory-tree kit
    tl  = load tree_lib.py from kit                             # any Exception -> refusal naming its class
    missing = [n for n in need if not hasattr(tl, n)]
    if missing: refuse once "tree_lib lacks <every missing name>: govkit update --kits memory-tree"
    return tl

derive_conf_reads(...), derive_conf_constants(...):  tl = load_tree_lib(need=<the names it reads>)
loop_witness.py, inside the function that reads it:
    leaks = loop_lib.load_tree_lib(need=("GIT_ENV_LEAKS",)).GIT_ENV_LEAKS
budget.py, the skew row:
    with tempfile.TemporaryDirectory() as scratch:                           # S24
        copy dirname(loop_lib.load_tree_lib(need=()).__file__) and its siblings into scratch
```

### The tree_lib route probe, after this unit (92 AC8's first probe, S1, S4, S5, S7)

```
for every *.py under tools/loop/, parsed:
    outside loop_lib.load_tree_lib, a HIT is:
        Import | ImportFrom of the module "tree_lib"
        Call to import_module | __import__ whose first argument is the str "tree_lib"
        Call to resolve_kit_dir whose first argument is the str "memory-tree"
        Call to spec_from_file_location | SourceFileLoader with a str argument ending in "tree_lib.py"
    a LOADER RESULT is a load_tree_lib(...) Call, or a Name bound from one in the same body
    a HIT too: a loader result as an argument of any call but getattr
    need(call) = its literal `need` tuple of str, else TREE_LIB_SYMBOLS; a non-literal need is a HIT
    population = every non-dunder Attribute on a loader result, and every getattr(result, "<str>")
    each member's name must be in need(its call), and every need must be a subset of TREE_LIB_SYMBOLS
assert no HIT, and population non-empty, holding ("loop_witness.py", "GIT_ENV_LEAKS")
```

A str naming `tree_lib.py` outside those calls is no hit, so the skew row of `budget.py` passes.

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- `tools/memory-tree/row_grammar.py:1010-1039` `load_recall_kit` resolves the kit, sets
  `sys.dont_write_bytecode = True`, imports under `except Exception`, and raises one refusal naming every
  missing name. `tools/memory-tree/corpus_ids.py:256` `_check_grammar_installed` is a narrower instance, and
  `tools/check-spec-tokens.py:851` `load_kit_module` loads a kit module by path with no bytecode written.
- `tools/lib/resolve_kit_dir.py:15-50` takes `(home, anchor, here)`: a receipt under the first `.git`
  ancestor, then `here/<home>` and `here/../<home>`, then `LookupError`. A scratch copy of `tools/loop/`
  alone, outside the repository, resolves no memory-tree kit; a copy of `loop/`, `lib/` and `memory-tree/`
  as siblings resolves through `here/../memory-tree`.
- `du -sk` printed 3104 for `tools/memory-tree` and 160 for `tools/lib`.
- 75 S35 routes `loop_witness.py` to `GIT_ENV_LEAKS` through `resolve_kit_dir`. 17 S8 runs
  `loop_witness.py --selftest` as the leg `loop computed witness`.
- 88 S18 and AC18 state the `push-merge-tree-fatal` plant exits 1 printing `the clean re-merge failed: 128`.
  88 S24 fixes `build_failure_detail(outcome, text, empty_label)`, and 90 AC21 calls it with empty text and
  `(no output)`.
- `tools/loop/` is absent at base, so every module this unit writes is sibling-minted.
- Baselines over `memory/builds/dDeclaredLoop/spec/`, each grep as its criterion states, at HEAD:
  - 75's S35 range `load_tree_lib`, 90's S4 range `GIT_ENV_LEAKS`, and 88's S24 and 90's S21 ranges
    `class name`: 0 each;
  - 90's sketch `GIT_ENV_LEAKS` 0; 89's sketch `load_tree_lib` 0, `_MODULE_SCOPE_PARTS` 0, and the
    never-entering line 1;
  - `a class's whole subtree` over 89 §3, and `or a class whose subtree` over 89 §5 and 87 §5: 0 each;
  - `start failed: <strerror>` 1 each over 85, 86, 88 and 90, and `and the strerror` 1 over 88's AC24 range;
  - over 92: S8's range `budget.py` 0, AC8's range `spec_from_file_location` 0, AC9's range
    `type. statement` 0, AC5's range `hands-off 88` 0, AC16's range `(no output)` 0, §10
    `load_recall_kit` 0, S7's range `TemporaryDirectory` 0, S17's range `88 S18` 0, and S6's range
    `whole predicate` 1;
  - over 91's AC3 range, `tools/memory-tree/` 0 and `govkit update` 0.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/loop_witness.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the 91 minors and the 92 minors.** The halves are not disjoint by M6. Both write the 89
  spec, S10 its route line and S11 and S12 its walk lines, which is clause 1. Each half re-renders the build
  README's units region, a generated index written with its generator, which is clause 3.
- **Exempting the skew row by name in AC8 (M1's other option).** An exemption list grows with every plant,
  and the banned forms are the class the criterion guards.
- **Pricing the all-symbols refusal in §5 (M4's and L7's other option).** It leaves the criterion runner and
  the `loop computed witness` leg refusing on a kit that holds every name `loop_witness.py` reads.

## 5. Production-readiness checklist

- security — S7 closes the routes by which a loop module reaches `tree_lib` around the symbol check. S24
  bounds the skew row's writes to a per-run temporary directory outside the repository, removed on exit.
- perf / scale — the skew row copies about 3.3 MB once per plant run; the loader checks at most three
  attributes per call.
- error / empty / loading states — S8 and S22 keep a kit lacking a name its caller reads on the named
  refusal, and S21 turns any import failure into one; S20 keeps the `OSError` detail on one line.
- observability — one refusal names every missing symbol; the plant's rows name their detail.
- risks — the amendments land on specs whose units build before this one, each a rev bump with its §9
  line. A `need` that omits a name its caller reads is a hit of AC1's probe, never a silent pass.
- testing — AC1 to AC18 as probes, staged breaks, plant runs and greps; the arm under §7, observed at the
  close.
- migration — none: every reader is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe runs §4's "The tree_lib route probe" over every `*.py` under
  `tools/loop/`, it reports no hit, a population of at least three members holding `GIT_ENV_LEAKS` from
  `loop_witness.py`, and every member inside its call's `need`. The tree holds 92 S7's skew row.
  `awk '/^- \*\*AC8\*\*/,/^- \*\*AC9\*\*/'` over the 92 spec piped to `grep -c "spec_from_file_location"`
  prints at least 1.
  Red when: the probe passes `loop_witness.py` by finding nothing, or reds a correct skew row.
  figure: the population is DERIVED from the files at observation time; the grep prints 0 at HEAD, PINNED
  2026-10-24.
- **AC2** — When `awk '/^- \*\*S8\*\*/,/^- \*\*S9\*\*/'` over the 92 spec is piped to `grep -c "budget.py"`, it
  prints at least 1, and `awk '/^### The tree_lib route/,/^### The OSError/'` over it piped to the same grep
  prints at least 1.
  Red when: the skew row reads the loader and 92 never lists it as a caller.
  figure: the first grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC3** — When a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory gains, in the copy's `loop_witness.py`, a read of
  `loop_lib.load_tree_lib(need=("GIT_ENV_LEAKS",)).derive_X`, AC1's probe over the copy's `loop/` reports a
  hit naming `derive_X`. With that read replaced by `importlib.import_module("tree_lib")`, it reports a hit
  naming `import_module`, and with a loader result passed to a helper, a hit naming the call.
  Red when: a chained read, a helper parameter or an `importlib` route passes the probe.
- **AC4** — When a scratch copy as in AC3 has the module-level `GIT_ENV_LEAKS` of its `tree_lib.py`
  renamed, `python loop_witness.py --selftest` in its `loop/` exits non-zero printing `GIT_ENV_LEAKS` and
  `govkit update --kits memory-tree` with no `Traceback`, and `python -c "import loop_witness"` there exits
  0. With `derive_constant_charges` renamed instead, `python loop_witness.py --selftest` prints no
  `derive_constant_charges` and no `Traceback`.
  Red when: `loop_witness.py` ends the skew path in a traceback, resolves at import, or refuses over a name
  it never reads.
- **AC5** — When each range below is piped to its grep, each prints at least 1:
  `awk '/^- \*\*S35\*\*/,/^- \*\*S36\*\*/'` over the 75 spec with `grep -c load_tree_lib`;
  `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'` over the 90 spec with `grep -c GIT_ENV_LEAKS`; and
  `awk '/^- \*\*S24\*\*/,/^- \*\*S25\*\*/'` over the 88 spec and `awk '/^- \*\*S21\*\*/,/^- \*\*S22\*\*/'`
  over the 90 spec, each with `grep -c "class name"`. `awk '/^- \*\*AC8\*\*/,/^- \*\*AC9\*\*/'` over the 92
  spec piped to `grep -c "S35"` prints at least 1.
  Red when: 92's pass skips a sibling rewrite and every criterion stays green.
  figure: each sibling grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC6** — When `awk '/^### The tree_lib route/,/^### Evidence/'` over the 90 spec is piped to
  `grep -c GIT_ENV_LEAKS`, and `awk '/^### The conf-constant class/,/^### Inventory/'` over the 89 spec is
  piped to `grep -c load_tree_lib`, each prints at least 1.
  Red when: 90's sketch keeps the two-name tuple or 89's keeps the inline route.
  figure: each prints 0 at HEAD, PINNED 2026-10-24.
- **AC7** — When `awk '/^### The conf-constant class/,/^### Inventory/'` over the 89 spec is piped to
  `grep -c "_MODULE_SCOPE_PARTS"`, it prints at least 1, and piped to
  `grep -cF "never entering FunctionDef | AsyncFunctionDef | ClassDef | Lambda"`, it prints 0.
  Red when: 89's sketch still skips a definition whole beside a scope item that descends it.
  figure: the greps print 0 and 1 at HEAD, PINNED 2026-10-24.
- **AC8** — When `awk '/^## 3/,/^### Edges/'` over the 89 spec is piped to `grep -c "a class's whole subtree"`,
  and `awk '/^## 5/,/^## 6/'` over the 89 spec and over the 87 spec are each piped to
  `grep -c "or a class whose subtree"`, each prints at least 1. `awk '/^- \*\*AC4\*\*/,/^## 7/'` over the 91
  spec piped to `grep -c "or a class whose subtree"` prints at least 1.
  Red when: 89's non-goal and risks speak of a function alone beside a class-body loader.
  figure: each sibling grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC9** — When 91 AC3 runs as restated, `python budget.py --fixture --plant conf-read-forms` in the copy's
  `loop/` exits non-zero, prints a parity failure naming `DCONF` as missed, and prints no
  `govkit update --kits memory-tree`. `awk '/^- \*\*AC3\*\*/,/^- \*\*AC4\*\*/'` over the 91 spec piped to
  `grep -c "tools/memory-tree/"` prints at least 1.
  Red when: the copy cannot resolve `tree_lib` and the bare non-zero exit passes for a parity failure.
  figure: the grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC10** — When `awk '/^- \*\*S17\*\*/,/^## 3/'` over the 92 spec is piped to `grep -c "88 S18"`, it prints
  at least 1, and 93 AC3's exit-claim probe over `memory/builds/dDeclaredLoop/spec/` prints the set `{1}`.
  Red when: 92 S17 leaves 88's exit statement unnamed and a later rewrite of AC16 drifts from it.
  figure: the grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC11** — When `awk '/^- \*\*AC6\*\*/,/^- \*\*AC7\*\*/'` over the 92 spec is piped to
  `grep -c "A binding whose value"` and to `grep -c "whole predicate"`, each prints at least 1. Over 87,
  `awk '/^## 3/,/^- A binding whose value/'` piped to `grep -c "whole predicate"` and to
  `grep -c annotation` each prints at least 1.
  Red when: AC6's annotation half is satisfied by another bullet of 87 §3.
- **AC12** — When `awk '/^- \*\*AC9\*\*/,/^- \*\*AC10\*\*/'` over the 92 spec is piped to
  `grep -c "type. statement"`, to `grep -c "six"` and to `grep -c "regression"`, each prints at least 1, and
  piped to `grep -c "five"`, it prints 0. `awk '/^- \*\*S9\*\*/,/^- \*\*S10\*\*/'` over it piped to
  `grep -c "type. statement"` prints at least 1.
  Red when: 92 prices five forms beside 91's six, or its 87-range half reads as S9's coverage.
  figure: the `five` grep prints 1 and the `type. statement` grep 0 at HEAD, PINNED 2026-10-24.
- **AC13** — When `awk '/^- \*\*AC5\*\*/,/^- \*\*AC6\*\*/'` over the 92 spec is piped to
  `grep -c "hands-off 88"`, it prints at least 1, and piped to `grep -c '"Edges"'`, it prints 0.
  Red when: a pointer written in S5's own words fails AC5.
- **AC14** — When a `python -c` probe imports `guard` from `tools/loop/` and calls `build_failure_detail` with
  empty text and `(no output)` on `OSError()`, `OSError(5, '')`, `OSError("boom")`,
  `FileNotFoundError(2, "No such file")` and `OSError("a\nb")`, it answers `start failed: OSError`,
  `start failed: [Errno 5]`, `start failed: boom`, `start failed: No such file` and `start failed: a`.
  `awk '/^- \*\*AC16\*\*/,/^## 7/'` over the 92 spec piped to `grep -c "(no output)"` prints at least 1.
  Red when: an interior newline splits the one-line refusal, or the probe omits a required argument.
- **AC15** — When `python guard.py --fixture --plant push-merge-tree-fatal` runs in `tools/loop/`, its
  `OSError("a\nb")` row prints `the clean re-merge failed: start failed: a`, and no output line is `b`.
  Red when: the OSError branch takes the detail whole, staged by restoring that spelling.
- **AC16** — When a scratch copy as in AC3 has `derive_docstring_ids` and `derive_constant_charges` renamed in
  its `tree_lib.py`, a `python -c` call of `loop_lib.load_tree_lib()` in its `loop/` exits non-zero with one
  refusal line naming both. With `raise RuntimeError("x")` as the first line of that `tree_lib.py` instead,
  it exits non-zero printing `RuntimeError` and `govkit update --kits memory-tree` with no `Traceback`.
  After either run, the copy's `memory-tree/` holds no `__pycache__`. The copy is made without
  `__pycache__`. `awk '/^## 10/,0'` over the 92 spec piped to `grep -c load_recall_kit` prints at least 1.
  Red when: the loader stops at the first missing name, lets a non-import error through, or writes bytecode
  into the memory-tree kit.
- **AC17** — When `grep -cF 'start failed: <strerror>'` runs over the 85, 86, 88 and 90 specs, each prints 0,
  and `awk '/^- \*\*AC24\*\*/,/^- \*\*AC25\*\*/'` over the 88 spec piped to `grep -c "and the strerror"`
  prints 0.
  Red when: a sibling spec still gives a spelling `guard.py` no longer produces.
  figure: 1 each at HEAD, PINNED 2026-10-24.
- **AC18** — When `python budget.py --fixture --plant no-own-conf-read` runs twice concurrently in
  `tools/loop/`, both exit 0 printing `tree_lib lacking derive_constant_charges`, and `git status --porcelain`
  prints the same before and after. A `python -c` probe parsing `budget.py` finds a
  `tempfile.TemporaryDirectory()` call as a `with` item. `awk '/^## 5/,/^## 6/'` over the 92 spec piped to
  `grep -c "3.3 MB"` prints at least 1.
  Red when: the skew row copies to a fixed path, inside the tree, or leaves its copy behind.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop guard fixtures` and `loop computed witness`, none a leg at
HEAD.

New arm: tools/loop/guard.py · covers AC15 · the OSError("a\nb") row of push-merge-tree-fatal, staged with the whole-detail spelling · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Narrow AC8's ban to resolution forms, or exempt the skew row by name (ids 2, 12, 15)?** (a) the
  forms of S1 and S7; (b) an exemption naming the plant rows. The report judged both sound. (b) leaves the
  ban a spelling test that the next plant trips. (a) satisfies every criterion (b) would and is the class.
  RESOLVED (agent, 2026-10-24, delegated): (a), S1, S2, S7.
  widens: none · relaxes: none
- **F3 — One all-symbols refusal for every caller, priced, or a per-caller `need` (ids 16, 23)?** (a) price
  it in 92 §5; (b) `load_tree_lib(need=...)` with the union as default. (a) leaves `loop_witness.py`
  refusing on a kit that holds the one name it reads. (b) satisfies every criterion (a) would and adds
  AC4's discriminating half. RESOLVED (agent, 2026-10-24, delegated): (b), S22.
  widens: none · relaxes: none
- **F4 — Does `loop_witness.py` load at import or at first use (id 23)?** (a) import; (b) first use, inside
  the reading function. (a) makes every import of the module resolve the kit and refuse. RESOLVED (agent,
  2026-10-24, delegated): (b), S8.
  widens: none · relaxes: none
- **F5 — Drop 92 AC9's 87-range half, or label it (id 8)?** (a) drop; (b) label it a regression
  re-observation with a re-pinned figure. (b) keeps an observation (a) discards. RESOLVED (agent,
  2026-10-24, delegated): (b), S17.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-10 spec audit's 24 minors batched (14 MEDIUM, 10 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-95 and TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy. These are 92's `tree_lib` loader and
its AC8 probe (S1 to S8, S21, S22), the `no-own-conf-read` skew row of `budget.py` (S2, S24), 88 S24's
`build_failure_detail` and 81's `push-merge-tree-fatal` plant (S19, S20), and the sibling specs' own
sentences (S9 to S18, S23). The loader follows `tools/memory-tree/row_grammar.py`'s `load_recall_kit`,
carried inline because `tools/loop/` is a copy-installed kit that cannot import a memory-tree module to
load a memory-tree module.
`python tools/codebase-map/reuse_lookup.py "import a sibling kit module late and refuse naming every missing attribute"`
ranked `kit_rel`, `resolve_kit_dir`, `kit_dir`, `CensusRefused` and `ScopeRefused`. `resolve_kit_dir` is the
locator the loader already calls, and none of the others loads a module. The ranked list missed
`load_recall_kit`, which the round-10 report's L6 named and §4 Evidence verifies. The memory-recall query
returned `TOOL-aEvidencedLens-20`, an earlier minors batch, the round-10 report's M4 and 92's §10.

Recall terms used: load_tree_lib TREE_LIB_SYMBOLS loop_witness GIT_ENV_LEAKS skew refusal scratch copy load_recall_kit dont_write_bytecode minors batch
