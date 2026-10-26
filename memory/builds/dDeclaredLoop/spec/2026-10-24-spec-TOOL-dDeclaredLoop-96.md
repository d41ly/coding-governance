# TOOL-dDeclaredLoop-96 — the round-11 spec audit's 13 minors, batched

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-96-deviation-961.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-96-deviation-961.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-95 |

<!-- /gen:spec-records -->

## 1. Goal

The round-11 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md`)
exited CONVERGED with 14 confirmed findings over units 93 and 94, the round-10 promotions. Its one high,
id 1, is unit 95. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW.
Each finding keeps its report id and its own scope item, including where the report merged ids into one
item. The minors land on 93 and 94 both, so this unit repairs neither in particular and builds after every
unit (order 50, above 95's 49).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2 | S1 |
| M2 | MEDIUM | 4, 12 | S2, S3 |
| M3 | MEDIUM | 9 | S4 |
| M4 | MEDIUM | 10 | S5 |
| M5 | MEDIUM | 13 | S6 |
| M6 | MEDIUM | 14 | S7 |
| L1 | LOW | 3 | S8 |
| L2 | LOW | 5, 15 | S9, S10 |
| L3 | LOW | 7 | S11 |
| L4 | LOW | 16 | S12 |
| L5 | LOW | 17 | S13 |

That is 7 MEDIUM and 6 LOW findings by raw id. Two report items merge ids, and each is fixed once across
its scope items: M2 (S2 and S3) and L2 (S9 and S10). Id 7 overlaps id 9, and S4's rewrite discharges S11.
The report's three refuted findings, ids 6, 8 and 11, are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 2. 94 §6 gains AC19, one range grep over the 92 spec per sentence 94 orders there, each
  printing at least 1 and each pinned at 0 at HEAD. Over 92's AC8 range the tokens are `derive_X`,
  `import_module`, `getattr` and `non-empty`. Over its AC16 range they are `S24` and `S21`. Over its S8
  range they are `need` and `first use`. Over its S3 and S8 ranges the token is `conf-constant class`. Over
  its S17 range they are `first non-blank` and `85 S3`. AC19 lands in this unit's rev bump of 94. Where
  94's pass left one of those 92 sentences without its token, this pass writes it, in the rev bump of 92.
  Observed by AC1.
- **S2** — id 4. 93 §4's exit-claim probe reads every `*.md` under `memory/builds/dDeclaredLoop/spec/` but
  the 93 and 96 specs, the two that state the probe. 93 AC3 requires at least one claim from each of the
  81, 83, 88 and 92 specs in place of its floor of five, and pins no count per file, because 94 S14
  rewrites 92 S17. In this unit's rev bump of 93. Observed by AC2.
- **S3** — id 12. 93 §4's matcher accepts `exits`, `exit` and `exit code`, each optionally followed by `of`
  or `with`, before a number, and accepts `non-zero`. 93 AC3 passes on a set that holds 1 and no member but
  1 and `non-zero`. Its staged break rewords 92 AC16 to `exit code of 0` in a scratch copy and observes the
  probe red. 94 AC10 also re-runs 93 AC1's grep over 92's AC16 range. In this unit's rev bumps of 93 and
  94. Observed by AC2, AC3.
- **S4** — id 9. 90's sketch "The tree_lib route, after this unit" carries 94's loader whole: the
  keyword-only `need`, one refusal naming every missing name, and any `Exception` the import raises
  refused by its class name. The comment "every tree_lib name loop_lib calls" leaves it, and the
  four-name tuple 95 S1 writes stays. 90 S4, 86 S21 and 88 S33 state the refusal over the caller's
  `need`, and 88 S33 names any exception the import raises in place of `ImportError` or `SyntaxError`.
  These land in this unit's rev bumps of 90, 86 and 88. 94 S10 names the three sites and 94 AC6 gains
  their greps, in the rev bump of 94. Observed by AC4.
- **S5** — id 10. 92's sketch "The tree_lib route, after this unit" shows `derive_conf_reads` and
  `derive_conf_constants` calling `load_tree_lib(need=<the names it reads>)`, and `loop_witness.py`
  reading `GIT_ENV_LEAKS` inside its reading function with `need=("GIT_ENV_LEAKS",)`. The module-level
  `GIT_ENV_LEAKS = loop_lib.load_tree_lib().GIT_ENV_LEAKS` line leaves it. That lands in the rev bump of
  92. 94 S8 and S22 name 92's sketch as a restatement site, and 94 AC2 gains its grep, in the rev bump of
  94. Observed by AC5.
- **S6** — id 13. 94 S5 and §4 "The tree_lib route probe" state the value-flow class. A loader result may
  only be the direct value of an `Attribute`, the first argument of `getattr`, or a plain `Name` bound once
  in the same body. A loader result that is returned, yielded, assigned to an attribute, a subscript or a
  second `Name`, placed in a list, tuple, set or dict display, or passed to any call but `getattr` is a
  HIT. 94 AC3 gains a staged helper that returns `loop_lib.load_tree_lib(need=())` and is read through
  `.derive_X`. In this unit's rev bump of 94. Observed by AC6.
- **S7** — id 14. `load_tree_lib` in `tools/loop/loop_lib.py` takes `need` as a keyword-only parameter,
  `def load_tree_lib(*, need=TREE_LIB_SYMBOLS)`. 94's probe counts any positional argument of a
  `load_tree_lib` call as a HIT, and a `need` that is not a tuple display of str constants as a HIT, a list
  display included. 94 S22, its sketch and its probe say so, and 94 AC3 gains a staged positional read of
  an unchecked name, in the rev bump of 94. Observed by AC7.
- **S8** — id 3. 94's **consumes-from** `TOOL-dDeclaredLoop-93` bullet cites the round-10 spec audit's
  ids 4, 11, 13, 20 and 29, the set 93's mirroring bullet cites, in the rev bump of 94. Observed by AC8.
- **S9** — id 5. The version-skew row of `tools/loop/budget.py` checks its scratch copy in a fresh child
  `python` process, run as `sys.executable` with its working directory at the copy's `loop/`. The parent's
  `sys.modules` and `sys.path` therefore never answer for the copy. 94 S2, S21 and S24 and 94's sketch say
  so, and 92 S7 says so, in the rev bumps of 94 and 92. Where 94's pass checked the copy in-process, this
  pass moves the check into the child. Observed by AC9.
- **S10** — id 15. 94 AC18 gains a half: after an in-process `load_tree_lib()` of the real kit, the row
  still prints `tree_lib lacking derive_constant_charges`. In the rev bump of 94. Observed by AC10.
- **S11** — id 7. 90's sketch catch line and per-name loop read as 94 S21's idiom, and 88 S33 names any
  exception the import raises. S4's rewrite is what writes both. Observed by AC4.
- **S12** — id 16. 94 S24 and 94's sketch name the copied set as 90 S5 does: `tools/loop/`, `tools/lib/`
  and `tools/memory-tree/` as siblings, with `__pycache__` excluded. 94 §5 and 92 §5 price the copy from
  `du -sk` of those three directories, with the command and the list written beside the figure, measured
  at this pass. 94 AC18's grep of 92 §5 reads `du -sk` in place of `3.3 MB`. These land in the rev bumps
  of 94 and 92. Where 94's pass copied another set, this pass copies that one. Observed by AC11.
- **S13** — id 17. Before it creates its scratch directory, the skew row resolves `tempfile.gettempdir()`
  and the repository root from `git rev-parse --show-toplevel`, compared after `os.path.realpath` and
  `os.path.normcase`. Where the temp root sits under the repository, the row refuses by name, printing
  `scratch root <path> is inside the repository`, and creates nothing. It opens
  `tempfile.TemporaryDirectory(ignore_cleanup_errors=True)`, and prints `scratch copy left at <path>` where
  the directory survives the `with` block. 94 §5 "security" and 92 §5 "security" read "cleaned up on normal
  exit and on an exception". 94 AC18 asserts the created path is outside the repository root. These land
  in the rev bumps of 94 and 92. Observed by AC12, AC13.

## 3. Non-goals (OUT)

- The high's mechanism, `read_tree_conf` and the four-name tuple: unit 95. S4 keeps the tuple 95 writes.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- Rewriting a passage a sibling unit already wrote as this unit's item states. An item whose target reads as
  stated is observed and recorded, never rewritten.
- A by-path module load keyed on the resolved directory, the report's other fix for ids 5 and 15. S9's
  child process isolates the copy without changing how `load_tree_lib` imports for every caller.
- Cleanup after `SIGKILL`. No `with` block runs then, and §5 claims only normal exit and an exception.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-95` — the four-name `TREE_LIB_SYMBOLS`, `read_tree_conf` and 94's probe as that unit leaves it, which S4's rewrite of 90's loader block keeps and S6 and S7 widen (the round-11 spec audit's ids 1, 9, 13, 14)
- **consumes-from** `TOOL-dDeclaredLoop-94` — S2, S5, S8, S10, S21, S22, S24, §3's Edges, §4's sketch and probe, §5, AC2, AC3, AC6, AC10 and AC18, with the skew row of `budget.py` and `load_tree_lib` as that unit builds them (the round-11 spec audit's ids 2, 3, 4, 5, 7, 9, 10, 12, 13, 14, 15, 16, 17)
- **consumes-from** `TOOL-dDeclaredLoop-93` — §4's exit-claim probe, AC1 and AC3, which S2 and S3 restate (the round-11 spec audit's ids 3, 4, 12)
- **consumes-from** `TOOL-dDeclaredLoop-92` — S3, S7, S8, S17, AC8, AC16, §5 and the sketch "The tree_lib route, after this unit", which S1, S5, S9, S12 and S13 restate (the round-11 spec audit's ids 2, 5, 10, 16, 17)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S4 and the sketch "The tree_lib route, after this unit", which S4 and S11 restate (the round-11 spec audit's ids 7, 9)
- **consumes-from** `TOOL-dDeclaredLoop-88` — S33, which S4 and S11 restate (the round-11 spec audit's ids 7, 9)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S21, which S4 restates (the round-11 spec audit's id 9)
- **hands-off** `TOOL-dDeclaredLoop-100` — S4, S6, S9, S12, S13, §4's route-probe and skew-row sketches and §7, with the skew row of `budget.py`, which that unit restates and completes (the round-12 spec audit's ids 5, 13, 15, 21, 22, 23, 24)

## 4. Design

### Write set

This pass writes `tools/loop/loop_lib.py` (S7) and `tools/loop/budget.py` (S9, S12, S13). Inside this
build's folder it amends the specs of 86, 88, 90, 92, 93 and 94 as rev bumps, one per spec, each with its
§9 line. The build README's regions are the generator's render. A keyword-only parameter moves no `id`,
`kind` or `file` of `load_tree_lib`'s symbol row, and the pass mints no public module-level `def`, so
`memory/map/generated/symbols.json` does not move.

### The exit-claim probe, after this unit (S2, S3)

```
claim = re.compile(r"--plant push-merge-tree-fatal`((?:(?!--plant|\. |; ).){0,60}?)"
                   r"\b(?:exit(?:s| code)?(?: of| with)? (\d+)|(non-zero))")
for each *.md under memory/builds/dDeclaredLoop/spec/ but the 93 and 96 specs:
    text = the file with every whitespace run squeezed to one space
    collect (file, m.group(2) or m.group(3)) for every claim.finditer(text)
assert each of the 81, 83, 88 and 92 specs holds at least one claim
print the claims per file and the set of codes
```

### The tree_lib route probe, after this unit (S6, S7)

```
for every *.py under tools/loop/, parsed:
    outside loop_lib.load_tree_lib, the HITs of 94 §4 stand, and these join them:
        a load_tree_lib(...) Call with any positional argument
        a need that is not a tuple display of str constants
        a LOADER RESULT returned, yielded, assigned to an Attribute, a Subscript or a second Name,
          placed in a List, Tuple, Set or Dict display, or an argument of any call but getattr
    a LOADER RESULT is a load_tree_lib(...) Call, or a Name bound once from one in the same body
    a LOADER RESULT may only be the value of an Attribute, getattr's first argument, or that Name
```

### The skew row, after this unit (S9, S12, S13)

```
real   = dirname(loop_lib.load_tree_lib(need=()).__file__)          # tools/memory-tree, loaded in-process
top    = git rev-parse --show-toplevel
if under(realpath(tempfile.gettempdir()), realpath(top)): refuse "scratch root <path> is inside the repository"
with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as scratch:
    copy tools/loop/, tools/lib/ and tools/memory-tree/ as siblings into scratch, no __pycache__
    rename derive_constant_charges in scratch/memory-tree/tree_lib.py
    run [sys.executable, "-c", <call loop_lib.load_tree_lib()>] with cwd scratch/loop   # a fresh child
    pass where the child exits non-zero naming derive_constant_charges
if exists(scratch): print "scratch copy left at <path>"
```

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 93 §4's matcher, run over the spec folder, found one claim each in 81, 83 and 92, two in 88 and four in
  93, and the widened matcher above found the same nine. No spec phrases a claim as `exit code`,
  `exit with` or `non-zero` today.
- `tools/memory-tree/row_grammar.py:1010-1039` `load_recall_kit` does `sys.path.insert(0, kit)` and a plain
  `import`, so a module it loads stays cached in `sys.modules`. `tools/check-spec-tokens.py:851`
  `load_kit_module` keys its cache on the resolved path.
- `tempfile.TemporaryDirectory` honours `TMPDIR`, `TEMP` and `TMP`. Its `ignore_cleanup_errors` keyword
  exists from Python 3.10, and `python --version` printed 3.14.5.
- `tools/loop/` is absent at base, so every module this unit writes is sibling-minted.
- Baselines over `memory/builds/dDeclaredLoop/spec/`, each grep as its criterion states, at HEAD:
  - over 92: AC8's range `derive_X`, `import_module`, `getattr` and `non-empty`, AC16's range `S24` and
    `S21`, S8's range `need`, `first use` and `conf-constant class`, S3's range `conf-constant class`,
    S17's range `first non-blank` and `85 S3`, the sketch range `need=`, S7's range `child`, and §5's
    `du -sk` and `normal exit`: 0 each; the sketch range `GIT_ENV_LEAKS = loop_lib.load_tree_lib()`: 1;
  - over 90: the sketch range `need` 0, `for name in TREE_LIB_SYMBOLS` 1, `ImportError | SyntaxError` 1
    and `every tree_lib name loop_lib calls` 1; S4's range `need` 0;
  - over 86's S21 range `need` 0; over 88's S33 range `need` 0, `any exception` 0 and `SyntaxError` 1;
  - over 93: §4's probe `non-zero` 0, AC3's range `exit code of 0` 0;
  - over 94: AC10's range `93 AC1` 0, S5's range `returned` 0, the probe `positional` 0, S22's range
    `keyword-only` 0, AC3's range `positional` 0, S24's range `child`, `tools/lib/` and `__pycache__` 0
    each, the sketch `and its siblings` 1, AC18's range `show-toplevel` and `du -sk` 0 each, §5
    `normal exit` 0, and the consumes-from 93 bullet citing `ids 4, 11, 13, 20, 29` 0.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the 93 minors and the 94 minors.** The halves are not disjoint by M6. S3 writes 94
  AC10 as well as 93's probe, which is clause 1. Each half re-renders the build README's units region, a
  generated index written with its generator, which is clause 3.
- **A by-path load keyed on the resolved directory (L2's other fix).** It changes how `load_tree_lib`
  imports for every caller in order to serve one fixture row.
- **A `dir=` under a fixed path outside the repository (L5's other fix).** It picks an install location
  for every adopter. The refusal keeps the platform's temp root and names the case where it is unsafe.

## 5. Production-readiness checklist

- security — S13 refuses a scratch root inside the repository before anything is written, and S9 keeps the
  copy's module state out of the checking process. S6 and S7 close the routes by which a loader result
  escapes its symbol check.
- perf / scale — one child `python` process per plant run, beside the copy S12 prices from `du -sk`.
- error / empty / loading states — S13 names a scratch root inside the tree and a copy left behind. A
  positional `need` raises `TypeError` at the call, and the probe names it first.
- observability — S13's two lines name the path; the probe names each escaping form.
- risks — the amendments land on specs whose units build before this one, each a rev bump with its §9
  line. S12's figure is measured at this pass, because `tools/loop/` is unbuilt at HEAD.
- testing — AC1 to AC13 as greps, probes, staged breaks and plant runs.
- migration — none: every reader is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When each range of the 92 spec below is piped to its grep, each prints at least 1:
  `awk '/^- \*\*AC8\*\*/,/^- \*\*AC9\*\*/'` with `grep -c derive_X`, `grep -c import_module`,
  `grep -c getattr` and `grep -c non-empty`; `awk '/^- \*\*AC16\*\*/,/^## 7/'` with `grep -c S24` and
  `grep -c S21`; `awk '/^- \*\*S8\*\*/,/^- \*\*S9\*\*/'` with `grep -c need`, `grep -c "first use"` and
  `grep -c "conf-constant class"`; `awk '/^- \*\*S3\*\*/,/^- \*\*S4\*\*/'` with
  `grep -c "conf-constant class"`; and `awk '/^- \*\*S17\*\*/,/^## 3/'` with `grep -c "first non-blank"`
  and `grep -c "85 S3"`. `awk '/^- \*\*AC19\*\*/,/^## 7/'` over the 94 spec piped to
  `grep -c "first non-blank"` prints at least 1.
  Red when: a pass writes only the code halves of 94's items and every criterion stays green.
  figure: each 92 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC2** — When a `python -c` probe runs §4 "The exit-claim probe, after this unit" over
  `memory/builds/dDeclaredLoop/spec/`, it prints at least one claim from each of the 81, 83, 88 and 92
  specs, none from the 93 or 96 specs, and a set holding 1 and nothing but 1 and `non-zero`.
  `awk '/^### The exit-claim probe/,/^### Write set/'` over the 93 spec piped to `grep -c non-zero`, and
  `awk '/^- \*\*AC3\*\*/,/^## 7/'` over it piped to `grep -c "exit code of 0"`, each print at least 1.
  Red when: the floor is met by 93's own sentences, staged by rewording 81's claim out of the matcher in a
  scratch copy of the folder, which must turn the probe red naming the 81 spec.
  figure: both 93 greps print 0 at HEAD, PINNED 2026-10-24; the claims are DERIVED from the folder.
- **AC3** — When the probe of AC2 runs over a scratch copy of the spec folder whose 92 AC16 reads
  `exit code of 0` in place of exit 1, it prints a set holding 0 and fails; with `exits with 0` it fails
  the same way. `awk '/^- \*\*AC10\*\*/,/^- \*\*AC11\*\*/'` over the 94 spec piped to `grep -c "93 AC1"`
  prints at least 1.
  Red when: a reworded relapse of 92 AC16 leaves the probe printing `{1}`.
  figure: the 94 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC4** — When `awk '/^### The tree_lib route/,/^### Evidence/'` over the 90 spec is piped to
  `grep -c need` and to `grep -c parse_conf`, each prints at least 1, and piped to
  `grep -cF "for name in TREE_LIB_SYMBOLS"`, `grep -cF "ImportError | SyntaxError"` and
  `grep -c "every tree_lib name loop_lib calls"`, each prints 0. Each of `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'`
  over the 90 spec, `awk '/^- \*\*S21\*\*/,/^- \*\*S22\*\*/'` over the 86 spec and
  `awk '/^- \*\*S33\*\*/,/^- \*\*S34\*\*/'` over the 88 spec, piped to `grep -c need`, prints at least 1.
  The 88 range piped to `grep -c "any exception"` prints at least 1, and piped to `grep -c SyntaxError`
  prints 0. `awk '/^- \*\*AC6\*\*/,/^- \*\*AC7\*\*/'` over the 94 spec piped to `grep -c ImportError`
  prints at least 1.
  Red when: a sibling still says `need=("GIT_ENV_LEAKS",)` refuses over a missing derive name.
  figure: the `need` greps print 0 and the three negative greps 1 each at HEAD, PINNED 2026-10-24.
- **AC5** — When `awk '/^### The tree_lib route/,/^### The OSError/'` over the 92 spec is piped to
  `grep -c "need="`, it prints at least 1, and piped to `grep -cF "GIT_ENV_LEAKS = loop_lib.load_tree_lib()"`,
  it prints 0. `awk '/^- \*\*AC2\*\*/,/^- \*\*AC3\*\*/'` over the 94 spec piped to `grep -c "need="` prints
  at least 1.
  Red when: 92's sketch keeps the import-time route that 94 S8 removes.
  figure: the 92 greps print 0 and 1 at HEAD, PINNED 2026-10-24.
- **AC6** — When a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory gains, in its `loop_witness.py`, one staged read per form, the probe of §4 "The
  tree_lib route probe, after this unit" over the copy's `loop/` reports a hit for each. The forms are a
  helper returning `loop_lib.load_tree_lib(need=())` read through `.derive_X`, a generator yielding one, a
  `self.tl` store, a `CACHE["tl"]` store, a `t2 = tl` alias, a `[tl]` display and a helper argument. Over
  the unmodified `tools/loop/` it reports no hit. `awk '/^- \*\*S5\*\*/,/^- \*\*S6\*\*/'` over the 94 spec
  piped to `grep -c returned` prints at least 1.
  Red when: a returned, stored or aliased loader result passes the probe.
  figure: the 94 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC7** — When `python -c "import inspect, loop_lib; print(inspect.signature(loop_lib.load_tree_lib).parameters['need'].kind.name)"`
  runs in `tools/loop/`, it prints `KEYWORD_ONLY`. A scratch copy as in AC6 whose `loop_witness.py` reads
  `loop_lib.load_tree_lib(("GIT_ENV_LEAKS",)).derive_docstring_ids` makes the probe report a hit naming the
  positional argument, and one passing `need=["GIT_ENV_LEAKS"]` makes it report a hit naming the list.
  `awk '/^- \*\*S22\*\*/,/^- \*\*S23\*\*/'` over the 94 spec piped to `grep -c keyword-only` prints at
  least 1.
  Red when: a positional or list `need` passes the probe while the loader checks fewer names than are read.
  figure: the 94 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC8** — When `grep -c 'consumes-from\*\* .TOOL-dDeclaredLoop-93.*ids 4, 11, 13, 20, 29'` runs over the 94
  spec, it prints 1.
  Red when: the two sides of the 93 and 94 edge cite different id sets.
  figure: 0 at HEAD, PINNED 2026-10-24.
- **AC9** — When a `python -c` probe parses `budget.py` in `tools/loop/`, the function holding the skew row calls
  `subprocess.run` with `sys.executable` first in its argument list and a `cwd` under its scratch
  directory, and imports nothing from the copy in-process. `awk '/^- \*\*S7\*\*/,/^- \*\*S8\*\*/'` over the
  92 spec and `awk '/^- \*\*S24\*\*/,/^## 3/'` over the 94 spec, piped to `grep -c child`, each print at
  least 1.
  Red when: the row checks the copy in the process that already holds the real `tree_lib`.
  figure: both greps print 0 at HEAD, PINNED 2026-10-24.
- **AC10** — When a `python -c` call in `tools/loop/` first runs `loop_lib.load_tree_lib()`, then sets
  `sys.argv` to `budget.py --fixture --plant no-own-conf-read` and runs `budget.py` through
  `runpy.run_path` as `__main__`, its output holds `tree_lib lacking derive_constant_charges`.
  `awk '/^- \*\*AC18\*\*/,/^## 7/'` over the 94 spec piped to `grep -c "in-process"` prints at least 1.
  Red when: the row is staged to check the copy in-process, which then reuses the cached module and
  prints no label.
- **AC11** — When `awk '/^- \*\*S24\*\*/,/^## 3/'` over the 94 spec is piped to `grep -c "tools/lib/"` and to
  `grep -c __pycache__`, and `awk '/^## 5/,/^## 6/'` over the 92 spec and over the 94 spec are each piped
  to `grep -c "du -sk"`, each prints at least 1. The 94 sketch range
  `awk '/^### The tree_lib route, after/,/^### The tree_lib route probe/'` piped to
  `grep -c "and its siblings"` prints 0. A `python -c` probe parsing the loop kit's `budget.py` finds the str
  constants `loop`, `lib`, `memory-tree` and `__pycache__` in the function holding the skew row.
  Red when: the sketch still reads as a copy of all of `tools/`, or the price omits `loop/`.
  figure: the `and its siblings` grep prints 1 and the rest 0 at HEAD, PINNED 2026-10-24.
- **AC12** — When `python budget.py --fixture --plant no-own-conf-read` runs in `tools/loop/` with `TMPDIR`,
  `TEMP` and `TMP` all set to a directory inside the repository, it exits non-zero printing
  `scratch root` and `inside the repository`, and `git status --porcelain` prints the same before and
  after.
  Red when: the row copies into a temp root inside the tree, staged by removing the check.
  fixture: the directory is an existing tracked one. With the check removed the row exits 0 and prints no
  `scratch root` line, which is the red; its own cleanup leaves `git status` unchanged either way.
- **AC13** — When `python budget.py --fixture --plant no-own-conf-read` runs in `tools/loop/` with the
  default temp root, a `python -c` probe parsing `budget.py` finds `ignore_cleanup_errors=True` on the
  `tempfile.TemporaryDirectory` call, and the run prints no `scratch copy left at`. `awk '/^## 5/,/^## 6/'`
  over the 92 spec and over the 94 spec, piped to `grep -c "normal exit"`, each print at least 1.
  `awk '/^- \*\*AC18\*\*/,/^## 7/'` over the 94 spec piped to `grep -c show-toplevel` prints at least 1.
  Red when: §5 still promises removal on every exit, or a cleanup error on Windows ends the row in a
  traceback.
  figure: each grep prints 0 at HEAD, PINNED 2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures` and `loop computed witness`, neither a leg at HEAD.

New arm: tools/loop/budget.py · covers AC12 · the no-own-conf-read skew row with its temp root inside the repository, staged with the root check removed · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Isolate the skew row's copy by a child process or by a path-keyed load (ids 5, 15)?** (a) a
  fresh child `python` with its working directory at the copy's `loop/`; (b) `load_tree_lib` loading by
  path under a key naming the resolved directory. The report judged both sound. (b) changes the import of
  every caller to serve one row, and the row would then observe something the real readers do not.
  (a) satisfies every criterion (b) would. RESOLVED (agent, 2026-10-24, delegated): (a), S9.
  widens: none · relaxes: none
- **F3 — Keep the scratch copy out of the tree by a `dir=` or by a refusal (id 17)?** (a) a `dir=` under a
  chosen path outside the repository; (b) refuse by name where the temp root sits under the repository.
  (a) picks a location for every adopter, which veto 2 reserves to the owner. RESOLVED (agent,
  2026-10-24, delegated): (b), S13.
  widens: none · relaxes: none
- **F4 — Make `need` keyword-only, or read a positional argument as `need` (id 14)?** (a) keyword-only;
  (b) the probe reads the first positional argument as `need`. (a) fails at the call as well as in the
  probe, and leaves one spelling to grade. RESOLVED (agent, 2026-10-24, delegated): (a), S7.
  widens: none · relaxes: none
- **F5 — Which side of the 93 and 94 edge moves (id 3)?** (a) 94's bullet cites ids 4, 11, 13, 20 and 29;
  (b) 93's bullet cites id 11 alone. The report found ids 13 and 29 cross the edge, so (b) under-cites it.
  RESOLVED (agent, 2026-10-24, delegated): (a), S8.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-11 spec audit's 13 minors batched (7 MEDIUM, 6 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy. These are 93's exit-claim probe (S2,
S3), 94's tree_lib route probe and `load_tree_lib` (S6, S7), the `no-own-conf-read` skew row of
`budget.py` (S9, S10, S12, S13), and the sibling specs' own sentences (S1, S4, S5, S8, S11). The temp
root and the child process are the standard library's `tempfile` and `subprocess`.
`python tools/codebase-map/reuse_lookup.py "check a scratch copy of a kit in a fresh process outside the repository"`
ranked `check`, `scratch`, `kit_rel`, `resolve_kit_dir`, `kit_dir` and `add_scratch_worktree`
(`tools/run-gates/lib-attribute.sh`). `scratch` is a helper of three bash test suites and
`add_scratch_worktree` a bash worktree helper, neither callable from the copy-installed loop kit, and
`resolve_kit_dir` is the locator the loader already calls. So no existing seam fits the row's isolation,
and it stays the row's own lines. The memory-recall query returned the round-11 report's L2, 94's §4
sketch and the scratch-guard specs `TOOL-aProbedUnit-5` and `TOOL-aTetheredScratch-1`, which guard an
agent's writes rather than a fixture's temp root.

Recall terms used: exit-claim probe floor matcher load_tree_lib need keyword-only escape skew row child process scratch root minors batch
