# TOOL-dDeclaredLoop-90 — the round-8 spec audit's 22 minors, batched

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 45 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-90-deviation-901.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-90-deviation-901.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-8 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-87-spec-audit.md`)
exited CONVERGED with 23 confirmed findings over units 87 and 88, the round-7 promotions. Its one high,
id 19, is unit 89. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW.
Each finding keeps its report id and its own scope item, including where the report merged ids into one
item. The minors land on 87 and 88 both, so this unit repairs neither in particular and builds after every
unit (order 45, above 88's and 89's 44).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1, 9, 21 | S1, S2, S3 |
| M2 | MEDIUM | 3, 16, 22 | S4, S5, S6 |
| M3 | MEDIUM | 10, 18, 20 | S7, S8, S9 |
| M4 | MEDIUM | 2 | S10 |
| M5 | MEDIUM | 5 | S11 |
| M6 | MEDIUM | 15 | S12 |
| M7 | MEDIUM | 17 | S13 |
| L1 | LOW | 4 | S14 |
| L2 | LOW | 6 | S15 |
| L3 | LOW | 7 | S16 |
| L4 | LOW | 8 | S17 |
| L5 | LOW | 11 | S18 |
| L6 | LOW | 13 | S19 |
| L7 | LOW | 24 | S20 |
| L8 | LOW | 25 | S21 |
| L9 | LOW | 26 | S22 |

That is 13 MEDIUM and 9 LOW findings by raw id. Two defects span two grades, and each is fixed once across
its items: M3 with L1 (S7 to S9 and S14), and M4 with L6 (S10 and S19). The report's three refuted
findings, ids 12, 14 and 23, are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 1. 87 S1, 87 §3's first non-goal and 87 §4's sketch state charge rule 2's whole predicate,
  in this unit's rev bump of 87. A name is in the binding set when a str constant containing a conf name
  sits anywhere under a module-level `Assign`, `AnnAssign` or `AugAssign`: in a target, in an annotation or
  in the value. An `AnnAssign` with no value is included, and every `Name` in the targets is answered. Every
  module-level compound statement is descended, `For` and `While` bodies included. 89's sentence naming
  `derive_conf_rebinds` stays. Observed by AC1.
- **S2** — id 9. The `conf-read-forms` plant of `tools/loop/budget.py` gains three rows, each over a
  sibling scratch `loop_lib.py` as 86 S15 places it. `ANNO: Literal[".unattended.conf"]`, read as
  `ll.ANNO`, answers one `conf constant` hit. `D[".memory-tree.conf"] = 1`, read as `ll.D`, answers one.
  `for _i in range(1): FOR_BODY = ROOT / ".unattended.conf"`, read as `ll.FOR_BODY`, answers one.
  Observed by AC2.
- **S3** — id 21. 88 S13's sentence that the slice leaves 87's answer unchanged, and 88 AC13's re-run of
  87 AC2, give way to the re-run of this unit's AC2. Every shape on which the two predicates could differ
  is then planted, in this unit's rev bump of 88. Observed by AC3.
- **S4** — id 3. `tools/loop/loop_lib.py` reaches `tools/memory-tree/tree_lib.py` through one in-function
  loader. That loader is 86 S21's route, extended in place. It refuses where any name in the module-level
  tuple `TREE_LIB_SYMBOLS` is absent from the loaded module. The tuple now holds `derive_docstring_ids` and
  `derive_constant_charges`. The refusal exits non-zero printing the missing name and
  `govkit update --kits memory-tree`, never a traceback. Every route that reaches `tree_lib` takes the
  loader, `derive_conf_constants`' own call included. Observed by AC4.
- **S5** — id 16. The `no-own-conf-read` plant of `tools/loop/budget.py` gains a row over a scratch copy
  of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` whose `tree_lib.py` keeps `derive_docstring_ids`
  and lacks `derive_constant_charges`. That is the version skew of a memory-tree kit older than 88, which
  govkit cannot floor. Observed by AC5.
- **S6** — id 22. 86 S21 and 88 S33 state S4's refusal as a class over `TREE_LIB_SYMBOLS`, each naming
  `derive_constant_charges`, in this unit's rev bumps of 86 and 88. Observed by AC6.
- **S7** — id 10. 86 S13 and 86's `### The conf-constant kind` sketch hold no spelling of the old shape
  list: neither `BinOp` followed by "of str", nor "of strings", nor `PurePath`. Any spelling found is
  restated in this unit's rev bump of 86. Observed by AC7.
- **S8** — id 18. 87 AC3's negative half is restated, in this unit's rev bump of 87. It runs the
  spelling-proof pattern of S7 over 86's S13 range and its conf-constant sketch range, each printing 0. It
  keeps the whole-file `BinOp of str` grep at 0, and it gains L1's half over 86 AC13 (S14). Observed by
  AC8.
- **S9** — id 20. The pattern S7 and S8 use is shown to fire on the text it retires and to spare the class
  that replaced it. Over the 86 blob at commit `7391b88e6`, the rev-2 text the round-8 audit read as sibling
  context, it prints at least 1, and over 87 S1 it prints 0. Observed by AC9.
- **S10** — id 2. 86 S13 and the `derive_conf_constants` block of 86's conf-constant sketch say the
  binding set is the rule-2, module-qualified owners of `tree_lib.derive_constant_charges` for the two
  conf-name needles. 89's union with `derive_conf_rebinds` is kept, in this unit's rev bump of 86.
  Observed by AC10.
- **S11** — id 5. The sibling passages that five scope items of 88 order rewritten carry their rewrites,
  each written by this unit where absent and observed by AC11:
  - 83 S1 names the policy path (88 S1);
  - 85 S3 says the memo answers only while `run_merge_tree_usage` is the same object it called (88 S6);
  - 82 §10 names `read_profile_legs` (88 S12);
  - 86 §10 names `derive_constant_charges` (88 S13);
  - 85 S1 and 86 S2 name `LC_ALL=C` (88 S16).
  88 AC1, AC6, AC12, AC13 and AC16 each gain the matching range grep, in this unit's rev bump of 88.
- **S12** — id 15. `scan_glob_readers` in `tools/memory-tree/gen_build_index.py` keeps its composed
  needle, `magic = ":(" + "glob)"`, and passes `lambda s: magic in s` to the lifted walk. It never spells
  the needle as a literal. 88 S13 and 88's sketch "The lifted charge walk (S13)" say so, and they name
  TOOL-dTrueNorth-23's AC5 arm (`_scan_table23`, `gen_build_index.py:6464-6471`) as a consumer the lift
  keeps green, in this unit's rev bump of 88. Observed by AC12.
- **S13** — id 17. 82's sketch "The conf-read rule, after this unit" no longer defines the kind as
  "module-level str bindings". It reads the names `derive_conf_constants` answers (87 S1), in this unit's
  rev bump of 82. 87 S4 lists that sketch line among the passages it restates, in the rev bump of 87.
  Observed by AC13.
- **S14** — id 4. 86 AC13 plants 87 S3's rows: its range names `os.path.join` and the aliased `as C` row,
  written in this unit's rev bump of 86 where absent. Observed by AC14.
- **S15** — id 6. 80 S4 names `TOOL-dDeclaredLoop-87`'s `conf-read-forms` rows among the plants inside
  the boundary, written in this unit's rev bump of 80 where absent. 88 AC9 gains the
  `TOOL-dDeclaredLoop-87` grep, in the rev bump of 88. Observed by AC15.
- **S16** — id 7. 88 AC22's half over 81 S3 keeps only its `conflicted` grep, the token the amendment
  writes. The `failed` grep is dropped, because it prints 2 before the amendment. The edit is in this
  unit's rev bump of 88. Observed by AC16.
- **S17** — id 8. 87 AC2's bindings carry distinct names, `CONF_JOIN = ROOT / ".unattended.conf"`,
  `CONF_OSJ = os.path.join(ROOT, ".memory-tree.conf")` and `CONF_PATH = Path(ROOT, "cfg", ".unattended.conf")`.
  Each is in the expected set, and the aliased import stays an S3 plant row, not a binding. The edit is in
  this unit's rev bump of 87. Observed by AC17.
- **S18** — id 11. 88 §4 Evidence cites 75 by anchor, 75 §6 AC27 and 75 §7's
  `New arm: tools/loop/guard.py` line, never by line number, in this unit's rev bump of 88. Observed by
  AC18.
- **S19** — id 13. 87 S1, 87's sketch "The conf-constant kind, after this unit" and 87 §10 say the binding
  set is the rule-2, module-qualified slice of `tree_lib.derive_constant_charges`, in the rev bump of 87.
  88's §4 Write set names 87 among the specs it amends, in the rev bump of 88. Observed by AC19.
- **S20** — id 24. 87 §5 risks gains the NOT SEEN side, in the rev bump of 87: a conf name composed at run
  time from pieces, such as `".unattended" + ".conf"`, holds no single constant naming a conf and is
  outside the class, as `scan_glob_readers`' docstring records for its needle. Observed by AC20.
- **S21** — id 25. `build_failure_detail` in `tools/loop/guard.py` spells an `OSError` as
  `start failed: <strerror>`, falling back to `str(exc)` where `strerror` is None. The OSError row of the
  `push-merge-tree-fatal` plant raises the one-argument `OSError("boom")`. 88 S24 says so, in the rev bump
  of 88. Observed by AC21.
- **S22** — id 26. Every statement of C's state count names five states: 78's H1, its S1 and its hands-off
  edge; 75's, 81's and 84's edges; and 83 §3's first non-goal. Each edit is in this unit's rev bump of its
  spec. 88 S2 and AC2 are widened to that set, in the rev bump of 88. The build README's units region
  renders 78's H1, so it follows. Observed by AC22.

## 3. Non-goals (OUT)

- The high's mechanism, the global-loader and module-level target pass: unit 89.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- Rewriting a passage a sibling unit already wrote as this unit's item states. An item whose target reads
  as stated is observed and recorded, never rewritten.
- Clearing the credential-store entries the round-6 skeptic's probe left on node `d`, as 86 §3 and 88 §3
  record.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-75` — the edge to 78 that counts C's states, which S22 restates (id 26)
- **consumes-from** `TOOL-dDeclaredLoop-78` — the H1, S1 and hands-off edge that count C's states, which S22 restates to five (id 26)
- **consumes-from** `TOOL-dDeclaredLoop-80` — S4's plant population, which S15 widens to 87's rows (id 6)
- **consumes-from** `TOOL-dDeclaredLoop-81` — the edge to 78 that counts C's states, which S22 restates, and S3, whose `conflicted` token S16's criterion reads (ids 7, 26)
- **consumes-from** `TOOL-dDeclaredLoop-82` — S1's conf-constant kind, the conf-read sketch S13 restates and §10, which S11 completes (ids 5, 17)
- **consumes-from** `TOOL-dDeclaredLoop-83` — S1, which S11 reads for the policy path, and §3's state count, which S22 restates (ids 5, 26)
- **consumes-from** `TOOL-dDeclaredLoop-84` — the edge to 78 that counts C's states, which S22 restates (id 26)
- **consumes-from** `TOOL-dDeclaredLoop-85` — S1 and S3, which S11 completes with the locale and the probe-keyed memo (id 5)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S2, S13, S21, §10, AC13 and the conf-constant sketch, which S6, S7, S10, S11 and S14 restate and observe (ids 2, 4, 5, 10, 18, 20, 22)
- **consumes-from** `TOOL-dDeclaredLoop-87` — S1, S4, §3, §5, §10, AC2, AC3 and the conf-constant sketch, which S1, S8, S13, S17, S19 and S20 restate (ids 1, 4, 8, 13, 17, 18, 24)
- **consumes-from** `TOOL-dDeclaredLoop-88` — S2, S13, S24, S33, the lifted-walk sketch, §4 Evidence and Write set, and AC1, AC2, AC6, AC9, AC12, AC13, AC16 and AC22, with `derive_constant_charges`, `build_failure_detail` and the `tree_lib` route they mint (ids 2, 3, 5, 6, 7, 11, 13, 15, 16, 21, 22, 25, 26)
- **consumes-from** `TOOL-dDeclaredLoop-89` — `derive_conf_rebinds`' sentences in 87 S1 and 86 S13, which S1 and S10 keep, and its `tree_lib` call, which S4's refusal class covers

## 4. Design

### Write set

This pass writes `tools/loop/loop_lib.py` (S4), `tools/loop/budget.py` (S2, S5), `tools/loop/guard.py`
(S21) and `tools/memory-tree/gen_build_index.py` (S12, only where the lifted walk's caller spells the
needle as a literal). Inside this build's folder it amends the specs of 75, 78, 80, 81, 82, 83, 84, 85,
86, 87 and 88 as rev bumps, one per spec, each with its §9 line. The build README's regions are the
generator's render. The pass mints no public module-level `def`, so
`memory/map/generated/symbols.json` does not move. S9 also observes and records.

### The tree_lib route, after this unit (S4)

```
TREE_LIB_SYMBOLS = ("derive_docstring_ids", "derive_constant_charges")   # every tree_lib name loop_lib calls

load_tree_lib():                                   # 86 S21's in-function route, the only one
    kit = resolve_kit_dir("memory-tree", "tree_lib.py", here)   # LookupError -> 88 S33's refusal
    tl  = load tree_lib.py from kit                             # ImportError | SyntaxError -> 88 S33's refusal
    for name in TREE_LIB_SYMBOLS:
        if not hasattr(tl, name): refuse "tree_lib lacks <name>: govkit update --kits memory-tree"
    return tl
```

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- Charge rule 2 in `scan_scope` recurses into every child of a module-level `Assign`, `AnnAssign` or
  `AugAssign`, so a constant in a target or an annotation is charged, and every other statement falls to
  the descending arm (`tools/memory-tree/gen_build_index.py:5167-5186`).
- `scan_glob_readers` composes its needle as `magic = ":(" + "glob)"` so its own walk never finds it
  (`gen_build_index.py:5163`, docstring 5159-5161). `_scan_table23` compares the walk's answer over the
  kit with `probes23` both ways (`gen_build_index.py:6464-6471`, `probes23` from 6372).
- `tools/memory-tree/tree_lib.py` defines no `derive_constant_charges` at base.
- `python -c "print(repr(OSError('boom').strerror))"` prints `None`.
- Baselines over `memory/builds/dDeclaredLoop/spec/`, each greps as its criterion states:
  - `BinOp. of str\|of strings\|PurePath` over 86's S13 range prints 1, and so does `BinOp of str` over
    the whole 86 file;
  - `str bindings` over 82's conf-read sketch prints 1;
  - `failed` over 81's S3 range prints 2, and `conflicted` prints 0;
  - `TOOL-dDeclaredLoop-87` over 80's S4 range prints 0;
  - `NOT SEEN` over 87 §5 prints 0;
  - 88's Evidence cites 75 at "line 390" and "431", where 75's AC27 and guard arm sit at 391 and 432;
  - `three states` prints at 75:211, 78:1, 78:35, 78:64, 81:72, 83:49 and 84:66;
  - each of AC11's six range greps prints 0.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `tools/memory-tree/gen_build_index.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the code items and the spec-text items.** The halves are not disjoint by M6. Every
  code item (S2, S4, S5, S12, S21) also restates the 86, 87 or 88 spec, and so does every text item, which
  is clause 1. Each half re-renders the build README's units region, a generated index written with its
  generator, which is clause 3.
- **A `hasattr` check at each call site (S4).** A second symbol would need a second check written by
  whoever adds the call, which is the omission id 3 measured. One tuple read by one loader is a class, and
  AC4 derives the calls from the code.
- **Narrowing 88's slice to constants under the value (M1's other option).** That keeps two walks with
  different predicates under one question, the defect 88 §8 F4 removes. The wider set is the rule's
  fail-closed side.

## 5. Production-readiness checklist

- security — S1 and S2 keep the binding set equal to the walk that computes it, the wider and fail-closed
  set. S4 and S5 turn a version skew into the named refusal rather than a traceback.
- perf / scale — none: no walk is added, and the loader checks two attributes once per run.
- error / empty / loading states — S4 names a `tree_lib` missing any symbol the kit calls; S21 names a
  one-argument `OSError`.
- observability — each refusal names the missing symbol or the failure, and keeps its kind.
- risks — the amendments land on specs whose units are built, as 88 amends its siblings; each is a rev
  bump with its §9 line. S1 widens the binding set to annotation and target constants, which reports more
  and never less.
- testing — AC1 to AC22 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: every reader is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-87.md` is piped to
  `grep -c "annotation"`, it prints at least 1, and `grep -c 'AnnAssign. with a value\|AnnAssign-with-value\|ast.walk(binding.value)'`
  over the same file prints 0.
  Red when: 87 still states a value-only predicate beside a slice that charges targets and annotations.
  figure: the second grep prints 2 at HEAD, PINNED 2026-10-24.
- **AC2** — When `python budget.py --fixture --plant conf-read-forms` runs in `tools/loop/`, its `ANNO`,
  `D` and `FOR_BODY` rows each answer one `conf constant` hit. A `python -c` probe calling
  `derive_conf_constants` on a scratch `loop_lib.py` holding those three bindings and
  `while False: WHILE_BODY = ".memory-tree.conf"` answers each of `ANNO`, `D`, `FOR_BODY` and `WHILE_BODY`.
  Red when: the binding set reads only the value, so an annotation, a subscript target or a loop-body
  binding drops out.
  figure: the scratch file is written by the probe, so each expected name is DERIVED from its bytes.
- **AC3** — When `awk '/^- \*\*AC13\*\*/,/^- \*\*AC14\*\*/'` over the 88 spec is piped to
  `grep -c "87 AC2's probe"`, it prints 0, and piped to `grep -c "TOOL-dDeclaredLoop-90"`, it prints at
  least 1.
  Red when: 88 AC13 still re-runs a probe that plants no shape on which the predicates differ.
  figure: the first grep prints 1 at HEAD, PINNED 2026-10-24.
- **AC4** — When a `python -c` probe in `tools/loop/` collects every `ast.Attribute` name in
  `loop_lib.py` that is also a module-level `def` of `tools/memory-tree/tree_lib.py`, the set is a subset
  of `loop_lib.TREE_LIB_SYMBOLS`, and the tuple holds `derive_docstring_ids` and `derive_constant_charges`.
  Red when: the loop kit calls a `tree_lib` symbol its loader never checks.
  figure: the set is DERIVED from both files at observation time.
- **AC5** — When a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/`, made under the
  run's scratch directory, has `derive_constant_charges` removed from its `tree_lib.py`, then
  `python budget.py --fixture --plant no-own-conf-read` in its `loop/` exits non-zero. It prints
  `derive_constant_charges` and `govkit update --kits memory-tree`, and no `Traceback`.
  Red when: a memory-tree kit older than 88 ends the rule in an `AttributeError` traceback.
- **AC6** — When `awk '/^- \*\*S21\*\*/,/^- \*\*S22\*\*/'` over the 86 spec and
  `awk '/^- \*\*S33\*\*/,/^- \*\*S34\*\*/'` over the 88 spec are each piped to
  `grep -c "derive_constant_charges"`, each prints at least 1.
  Red when: the refusal is still stated for one symbol while the kit calls two.
- **AC7** — When `awk '/^- \*\*S13\*\*/,/^- \*\*S14\*\*/'` and `awk '/^### The conf-constant kind/,/^### Evidence/'`
  over the 86 spec are each piped to `grep -c 'BinOp. of str\|of strings\|PurePath'`, each prints 0, and
  `grep -c "BinOp of str"` over the whole 86 file prints 0.
  Red when: 86 S13 keeps its backticked shape list while the sketch is fixed.
- **AC8** — When `awk '/^- \*\*AC3\*\*/,/^## 7/'` over the 87 spec is piped to `grep -c "PurePath"`, it
  prints at least 1, and piped to `grep -c "AC13"`, it prints at least 1.
  Red when: 87 AC3 still greps one spelling and never reads 86 AC13.
  figure: the first grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC9** — When `git show` prints spec 86 as committed at `7391b88e6` (its spec file under this build's
  `spec/` folder) and that text is piped
  to `awk '/^- \*\*S13\*\*/,/^- \*\*S14\*\*/'` and then to `grep -c 'BinOp. of str\|of strings\|PurePath'`,
  it prints at least 1. The same pattern over 87's S1 range prints 0.
  Red when: the retirement pattern cannot see the text it retires, or flags the class that replaced it.
  figure: 7391b88e6 is the commit that added 87 and 88, and its 86 blob is PINNED there.
- **AC10** — When `awk '/^### The conf-constant kind/,/^### Evidence/'` over the 86 spec is piped to
  `grep -c "derive_constant_charges"`, it prints at least 1, and piped to `grep -c "ast.walk(binding.value)"`,
  it prints 0. The S13 range piped to `grep -c "derive_constant_charges"` prints at least 1.
  Red when: 86 still describes a standalone walk the lift removed.
- **AC11** — When each range below is piped to its grep, each prints at least 1:
  - `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over 83, `grep -c "policy path"`;
  - `awk '/^- \*\*S3\*\*/,/^- \*\*S4\*\*/'` over 85, `grep -c "same object"`;
  - `awk '/^## 10/,0'` over 82, `grep -c read_profile_legs`;
  - `awk '/^## 10/,0'` over 86, `grep -c derive_constant_charges`;
  - `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over 85 and `awk '/^- \*\*S2\*\*/,/^- \*\*S3\*\*/'` over 86,
    `grep -c "LC_ALL=C"`.
  Each range is over the named spec under `memory/builds/dDeclaredLoop/spec/`. The AC1, AC6, AC12, AC13
  and AC16 ranges of the 88 spec each name their sibling's spec text.
  Red when: a rev bump 88 orders is skipped with every criterion of 88 green.
  figure: each grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC12** — When `grep -c 'lambda s: ":(glob)"'` runs over `tools/memory-tree/gen_build_index.py` and
  over the 88 spec, each prints 0. `grep -c 'magic = ":(" + "glob)"'` over `gen_build_index.py` prints 1.
  A `python -c` probe importing `gen_build_index` from `tools/memory-tree/` finds
  `gen_build_index.scan_glob_readers` absent from `scan_glob_readers` over that directory.
  Red when: the walker spells its needle as a literal and charges itself, so the AC5 arm reads
  `unlisted=['gen_build_index.scan_glob_readers']`.
- **AC13** — When `awk '/^### The conf-read rule, after this unit/,/^### Evidence/'` over the 82 spec is
  piped to `grep -c "str bindings"`, it prints 0, and piped to `grep -c "derive_conf_constants"`, it prints
  at least 1.
  Red when: 82 holds two definitions of the kind, S1's and its sketch's.
- **AC14** — When `awk '/^- \*\*AC13\*\*/,/^- \*\*AC14\*\*/'` over the 86 spec is piped to
  `grep -c "os.path.join"` and to `grep -c "as C"`, each prints at least 1.
  Red when: 86 AC13 still plants only its original three shapes.
- **AC15** — When `awk '/^- \*\*S4\*\*/,/^## 3/'` over the 80 spec is piped to
  `grep -c "TOOL-dDeclaredLoop-87"`, it prints at least 1, and `awk '/^- \*\*AC9\*\*/,/^- \*\*AC10\*\*/'`
  over the 88 spec piped to `grep -c "TOOL-dDeclaredLoop-87"` prints at least 1.
  Red when: 80 S4 omits 87's rows and 88 AC9 cannot see it.
- **AC16** — When `awk '/^- \*\*AC22\*\*/,/^- \*\*AC23\*\*/'` over the 88 spec is piped to
  `grep -c 'grep -c "failed"'`, it prints 0, and piped to `grep -c 'grep -c "conflicted"'`, it prints at
  least 1.
  Red when: 88 AC22 keeps a half that is green before the amendment.
- **AC17** — When `awk '/^- \*\*AC2\*\*/,/^- \*\*AC3\*\*/'` over the 87 spec is piped to
  `grep -c "CONF_JOIN"`, it prints at least 1, and piped to `grep -c "four bindings"`, it prints 0. A
  `python -c` probe calling `derive_conf_constants` on a scratch `loop_lib.py` holding S17's three bindings
  answers each of `CONF_JOIN`, `CONF_OSJ` and `CONF_PATH`.
  Red when: one shape registering satisfies the probe for all three.
- **AC18** — When `awk '/^### Evidence/,/^### Files touched/'` over the 88 spec is piped to
  `grep -c "line 390\|sits at 431"`, it prints 0, and piped to `grep -c "75 §6 AC27"`, it prints at least 1.
  Red when: 88's Evidence lands a reader one line off 75's criterion and arm.
- **AC19** — When `awk '/^### The conf-constant kind, after this unit/,/^### Files touched/'` and
  `awk '/^## 10/,0'` over the 87 spec are each piped to `grep -c "derive_constant_charges"`, each prints at
  least 1. `awk '/^### Write set/,/^### The probe memo/'` over the 88 spec piped to `grep -c "87"` prints at
  least 1.
  Red when: 87's sketch still shows the walk 88 removed.
- **AC20** — When `awk '/^## 5/,/^## 6/'` over the 87 spec is piped to `grep -c "NOT SEEN"` and to
  `grep -c "composed"`, each prints at least 1.
  Red when: 87's risks name only the over-match side.
- **AC21** — When a `python -c` probe imports `guard` from `tools/loop/` and calls `build_failure_detail`
  on `OSError("boom")` with empty text and `(no output)`, it answers `start failed: boom`. On
  `FileNotFoundError(2, "No such file")` it answers `start failed: No such file`.
  `python guard.py --fixture --plant push-merge-tree-fatal` prints, on its OSError row,
  `the clean re-merge failed: start failed: boom`. `awk '/^- \*\*S24\*\*/,/^- \*\*S25\*\*/'` over the 88
  spec piped to `grep -c "str(exc)"` prints at least 1.
  Red when: a one-argument `OSError` prints `start failed: None` and every row still passes.
- **AC22** — When `grep -c "three states"` runs over each of the 75, 78, 81, 83 and 84 specs, each prints 0.
  `awk '/^- \*\*AC2\*\*/,/^- \*\*AC3\*\*/'` over the 88 spec piped to `grep -c 'grep -c "three states"'`
  prints at least 1.
  Red when: 78's title and the sibling edges still count three states beside an S1 that counts five.
  figure: the seven occurrences at HEAD are PINNED, 2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `tier2-review self-test` · `build-index selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures` and the leg `loop guard fixtures`, neither a leg at HEAD.

New arm: tools/loop/budget.py · covers AC2 AC5 · the annotation-only, subscript-target and loop-body rows of conf-read-forms and the tree_lib lacking derive_constant_charges, staged with the slice reading only the value and the loader checking one symbol · none
New arm: tools/loop/guard.py · covers AC21 · the one-argument OSError row of push-merge-tree-fatal, staged with the strerror-only spelling · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which binding predicate ships (ids 1, 9, 21)?** (a) 87 S1 adopts rule 2 whole: targets,
  annotations, a value-less `AnnAssign` and every compound statement; (b) 88's slice keeps only constants
  under `binding.value`. The report judged both sound. (b) puts a second predicate inside the lifted walk
  or beside it, the two-walks defect 88 §8 F4 removes. (a) reports more names, the fail-closed side, and
  needs no change to the lifted walk. RESOLVED (agent, 2026-10-24, delegated): (a), S1 to S3.
  widens: none · relaxes: none
- **F3 — Key 88 AC22's `failed` half to a new token, or drop it (id 7)?** (a) key it to a token only the
  amendment writes; (b) drop it and keep the `conflicted` half. 86 S6's amendment writes no token for
  `failed` that 81 S3 lacks today, so (a) would ask the amendment for wording it does not need. (b) leaves
  the discriminating half. RESOLVED (agent, 2026-10-24, delegated): (b), S16. widens: none · relaxes: none
- **F4 — Cite 75 by anchor, or correct the line numbers (id 11)?** (a) anchor; (b) 391 and 432, PINNED.
  (b) goes stale at 75's next one-line move, which is how the finding arose. RESOLVED (agent, 2026-10-24,
  delegated): (a), S18. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-8 spec audit's 22 minors batched (13 MEDIUM, 9 LOW).

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy. These are 88's lifted charge walk
(S1 to S3, S10, S12, S19), 86 S21's in-function `tree_lib` route (S4 to S6), 88 S24's
`build_failure_detail` (S21), and the `conf-read-forms` and `no-own-conf-read` plants of `budget.py` (S2,
S5).
`python tools/codebase-map/reuse_lookup.py "refuse when an imported kit module lacks a function the caller needs"`
ranked `need`, `kit_rel` and `resolve_kit_dir` first. `need` (`tools/check-kit-versions.sh:138`) is a
merge-bar grep for a kit's version constant, not a runtime check of a loaded module. `resolve_kit_dir` is
the locator 86 S21's loader already calls. So no existing seam fits the symbol check, and S4 extends that
loader rather than minting a second one. The memory-recall query returned the round-8 report's M2 and
88's lifted-walk sketch.

Recall terms used: spec-audit minors batch derive_constant_charges tree_lib version skew refusal retirement grep three states build_failure_detail
