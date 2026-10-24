# TOOL-dDeclaredLoop-100 — the round-12 spec audit's 21 minors, batched

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 51 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-100-deviation-1001.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-100-deviation-1001.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
exited CONVERGED with 24 confirmed findings over units 95 and 96, the round-11 promotions. Its three
highs, ids 1, 11 and 19, share item H1 and are units 97, 98 and 99. This unit is the batch
BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW. Each finding keeps its report id and its
own scope item, including where the report merged ids into one item. The minors land on 95 and 96 both,
so this unit repairs neither in particular and builds after every unit (order 51, above the order 50
that 96, 97, 98 and 99 share).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2 | S1 |
| M2 | MEDIUM | 14 | S2 |
| M3 | MEDIUM | 3 | S3 |
| M4 | MEDIUM | 4 | S4 |
| M5 | MEDIUM | 8 | S5 |
| M6 | MEDIUM | 10 | S6 |
| M7 | MEDIUM | 20 | S7 |
| M8 | MEDIUM | 15, 21 | S8, S9 |
| M9 | MEDIUM | 22 | S10 |
| M10 | MEDIUM | 23 | S11 |
| L1 | LOW | 5 | S12 |
| L2 | LOW | 6, 12 | S13, S14 |
| L3 | LOW | 13 | S15 |
| L4 | LOW | 7 | S16 |
| L5 | LOW | 16 | S17 |
| L6 | LOW | 18 | S18 |
| L7 | LOW | 24 | S19 |
| L8 | LOW | 17, 25 | S20, S21 |

That is 11 MEDIUM and 10 LOW findings by raw id. Three report items merge ids, and each is fixed once
across its scope items: M8 (S8 and S9), L2 (S13 and S14) and L8 (S20 and S21). Id 25 overlaps id 3 on
90 S4, so S3's rewrite of that sentence discharges S21's half there. The report's one refuted finding,
id 9, duplicated id 6 and is not in the disposal population.

## 2. Scope (IN)

- **S1** — id 2. 41 §5 "error / empty / loading states" states the rule 95 S4 gives 41 S2: a tree with
  no `.memory-tree.conf` prints every row `foreign build`, and a conf that no memory-tree kit reads is
  the loader's named refusal, `govkit update --kits memory-tree`. The phrase "no conf or no kit" leaves
  it. In this unit's rev bump of 41. Observed by AC1.
- **S2** — id 14. 41 S1 reads `MEMORY_ROOT` from `.memory-tree.conf` through `read_tree_conf` (95 S2), in
  place of "reached by `resolve_kit_dir("memory-tree", "tree_lib.py", here)`". 60 S2 and 64 S1, which
  cite "the route `TOOL-dDeclaredLoop-41` S1 specifies", read "reached through `read_tree_conf` (95 S2)"
  in place of the same call. These land in this unit's rev bumps of 41, 60 and 64. Observed by AC2.
- **S3** — id 3. 90 S4's sentence on the tuple names its four members, `parse_conf` included. 94 S10
  says 90's sketch declares `TREE_LIB_SYMBOLS` with the members 95 S1 gives it, and the word
  `three-name` leaves it. 94 AC1 states that its population holds `parse_conf` read in `loop_lib.py`,
  the sentence 95 S5 orders. These land in this unit's rev bumps of 90 and 94; where 95's pass already
  wrote one, this pass observes it. Observed by AC3.
- **S4** — id 4. 94 AC18's grep of 92 §5 reads `du -sk` in place of `3.3 MB`, as 96 S12 orders. The
  figure `3.3 MB` leaves 92 §5 and 94 §5, whose price is the `du -sk` figure 96 S12 measures. In this
  unit's rev bumps of 92 and 94. Observed by AC4.
- **S5** — id 8. 95 §4 Evidence's bullet on 90 AC4 says that 90 AC4 matches attribute names regardless
  of their receiver, and that `tools/memory-tree/tree_lib.py` defines `read_text`, `kit_rel` and
  `unfenced` among others. 95's sketch "The conf read, after this unit" holds no `.read_text` attribute
  read, and neither does `tools/loop/loop_lib.py`. In this unit's rev bump of 95. Observed by AC5.
- **S6** — id 10. `read_tree_conf` reads the conf as `design_lib.read_design_conf`
  (`tools/memory-tree/design_lib.py:479`, `TOOL-dTrueNorth-16`) does:
  `path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")`, then `parse_conf(text, {})`
  through the loader. Its `path.exists()` test before any loader call and the four-name tuple stay. 95
  S2, §4 Evidence and §10 name `read_design_conf` as the seam whose read rule it mirrors, in this unit's
  rev bump of 95. Observed by AC6.
- **S7** — id 20. An existing `.memory-tree.conf` that cannot be read, such as a directory of that name
  or a permission denial, is a named refusal. `read_tree_conf` turns an `OSError` from the read into a
  non-zero exit printing `memory-tree conf unreadable: <path> — <the error's class name>`, never a
  traceback. S6's decode cannot raise `UnicodeDecodeError`. 95 §5 "error / empty / loading states" says
  so, in the rev bump of 95. Observed by AC7.
- **S8** — id 15. In the skew row of `tools/loop/budget.py`, a failed `git rev-parse --show-toplevel`
  means that no repository encloses the run. That is a non-zero exit, or a `FileNotFoundError` where
  git is absent. The row then prints `scratch root check: no repository` and goes on, with no refusal and
  no traceback. 96 S13 and its sketch "The skew row, after this unit" say so, in this unit's rev bump of
  96. Observed by AC8.
- **S9** — id 21. "Under" in the skew row's scratch-root check is `_is_under(path, top)` in
  `tools/loop/budget.py`. Both paths pass through `os.path.realpath` and `os.path.normcase`. The answer
  is true only on the same drive by `os.path.splitdrive`, where `os.path.commonpath([path, top]) == top`.
  A `ValueError` from `commonpath` reads as not under. 96 S13 and its sketch say so, in the rev bump of
  96. Observed by AC9.
- **S10** — id 22. The skew row passes only where its child exits non-zero, its output holds
  `derive_constant_charges` and `govkit update --kits memory-tree`, and its output holds no
  `Traceback`. Otherwise it fails and prints no label. 96 S9 and the pass line of 96's sketch say so, in
  the rev bump of 96. Observed by AC10.
- **S11** — id 23. 94's tree_lib route probe treats a `Name` bound from a loader result as one in every
  nested scope that reads it: a closure, a `global` or `nonlocal` name, and a module-level binding read
  inside a function. Such a binding is a HIT unless every read of it is graded. The probe is an
  allowlist: a loader result anywhere but its three admitted positions is a HIT, whatever form holds
  it. 94 S5 and §4 "The tree_lib route probe", and 96 S6 and §4 "The tree_lib route probe, after this
  unit", say so, in the rev bumps of 94 and 96. Observed by AC11.
- **S12** — id 5. 96 S4 spells the grep 94 AC6 gains, `grep -cF "ImportError | SyntaxError"` over 90's
  sketch range printing 0, which holds the token 96 AC4 reads. 94 S10 names the three sites, `90 S4`,
  `86 S21` and `88 S33`. These land in the rev bumps of 96 and 94. Observed by AC12.
- **S13** — id 6. 95 AC4 also runs `python breakpoints.py --fixture --plant confs-disagree`, which exits
  non-zero printing `records root:` and both values, so it re-runs the whole of 72 AC3. In the rev bump
  of 95. This pass runs both halves over S6's and S7's read. Observed by AC13.
- **S14** — id 12. 95 §7 names `loop breakpoints fixtures` among the sibling-minted legs it keeps green,
  in the rev bump of 95, and this unit's §7 names it. Observed by AC14.
- **S15** — id 13. 96 §7 names `loop breakpoints fixtures` and `loop definition fixtures` among the
  sibling-minted legs it keeps green, in the rev bump of 96. Observed by AC15.
- **S16** — id 7. 95 AC5's fixture note reads: a copy inside a repository whose receipt names the
  memory-tree kit resolves that kit, so the copy goes outside any repository. In the rev bump of 95.
  Observed by AC16.
- **S17** — id 16. 94 S24's cleanup sentence, 94 AC18's `Red when` and its `TemporaryDirectory` probe,
  and the skew-row line of 94's sketch "The tree_lib route, after this unit" state 96 S13's form:
  `tempfile.TemporaryDirectory(ignore_cleanup_errors=True)`, with `scratch copy left at <path>`
  printed where the directory survives. In the rev bump of 94. Observed by AC17.
- **S18** — id 18. The `def` line of 92's sketch "The tree_lib route, after this unit" reads
  `def load_tree_lib(*, need=TREE_LIB_SYMBOLS)`, in the rev bump of 92. Observed by AC18.
- **S19** — id 24. The skew row takes `loop/` as the directory of `loop_lib.__file__`, and `memory-tree/`
  as the directory of the loaded `tree_lib`. It copies `lib/` only where a `lib/` directory sits beside
  that `loop/`. 96 S12 and the copy line of 96's sketch say so, in the rev bump of 96. Observed by
  AC19.
- **S20** — id 17. 92 §5 "perf / scale" reads "at most four attributes per call", in place of "three
  attributes once per run", in the rev bump of 92. Observed by AC20.
- **S21** — id 25. 90 AC4's sentence on the tuple names `parse_conf` beside the other members, in the
  rev bump of 90. 90 S4's sentence is S3's. Observed by AC21.

## 3. Non-goals (OUT)

- The high's mechanisms: `CONF_READERS` and the rule reading it (97), the `declared readers seen` row
  (98) and the `conf-readers-declared` plant (99). S6 and S7 keep `read_tree_conf` a function that
  builds and opens its conf path, so 99's plant still derives it.
- The report's left-shift gates and checklist entries. Each class is recorded at the close, and each
  item above carries the observation that discharges its own defect.
- Rewriting a passage a sibling unit already wrote as an item here states. An item whose target reads
  as stated is observed and recorded, never rewritten.
- 95's own pass. It builds at order 49, before this unit, and may meet 90 AC4's red on its sketch's
  `read_text`. Its builder diverges by BUILD-METHOD M2, spec first, and S5 and S6 are the read it
  converges on.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-95` — S2, S4, §4's Evidence and sketch "The conf read, after this unit", §5, §7, §10, AC4 and AC5, with `read_tree_conf` as that unit builds it, which S5, S6, S7, S13, S14 and S16 restate and harden (the round-12 spec audit's ids 6, 7, 8, 10, 12, 20)
- **consumes-from** `TOOL-dDeclaredLoop-96` — S4, S6, S9, S12, S13, §4's route-probe and skew-row sketches and §7, with the skew row of `budget.py` as that unit builds it, which S8 to S12, S15 and S19 restate and complete (the round-12 spec audit's ids 5, 13, 15, 21, 22, 23, 24)
- **consumes-from** `TOOL-dDeclaredLoop-94` — S5, S10, S24, §4's sketch and probe, §5, AC1, AC6 and AC18, which S3, S4, S11, S12 and S17 restate (the round-12 spec audit's ids 3, 4, 5, 16, 23)
- **consumes-from** `TOOL-dDeclaredLoop-92` — §5 and the sketch "The tree_lib route, after this unit", which S4, S18 and S20 restate (the round-12 spec audit's ids 4, 17, 18)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S4, AC4 and AC5, which S3 and S21 restate and S8 re-runs out of any repository (the round-12 spec audit's ids 3, 15, 25)
- **consumes-from** `TOOL-dDeclaredLoop-72` — AC3's `confs-disagree` plant in `breakpoints.py`, which S13 re-runs over the read S6 and S7 change (the round-12 spec audit's id 6)
- **consumes-from** `TOOL-dDeclaredLoop-64` — S1's route clause, which S2 restates onto `read_tree_conf` (the round-12 spec audit's id 14)
- **consumes-from** `TOOL-dDeclaredLoop-60` — S2's route clause, which S2 restates onto `read_tree_conf` (the round-12 spec audit's id 14)
- **consumes-from** `TOOL-dDeclaredLoop-41` — S1 and §5, which S1 and S2 restate to the rule 95 S4 gives S2 (the round-12 spec audit's ids 2, 14)
- **consumes-from** `TOOL-dDeclaredLoop-99` — the `conf-readers-declared` plant, which AC6 re-runs over the read S6 and S7 rewrite (the round-12 spec audit's ids 10, 19, 20)

## 4. Design

### Write set

This pass writes `tools/loop/loop_lib.py` (S5 to S7) and `tools/loop/budget.py` (S8 to S10, S19).
Inside this build's folder it amends the specs of 41, 60, 64, 90, 92, 94, 95 and 96 as rev bumps, one
per spec, each with its §9 line. `_is_under` is a private module-level `def`, and the symbol extractor
records public ones only (`tools/codebase-map/map_lib.py:325-327`), so
`memory/map/generated/symbols.json` does not move. The build README's regions are the generator's
render.

### The conf read, after this unit (S5 to S7)

```
def read_tree_conf(tree):
    path = tree / ".memory-tree.conf"
    if not path.exists(): return {}                                   # no conf: the loader is never called
    try:
        data = path.read_bytes()
    except OSError as exc:
        refuse "memory-tree conf unreadable: <path> — <type(exc).__name__>"   # non-zero exit, no traceback
    text = data.decode("utf-8", "replace").replace("\r\n", "\n")        # design_lib.read_design_conf's rule
    return load_tree_lib(need=("parse_conf",)).parse_conf(text, {})
```

### The skew row, after this unit (S8 to S10, S19)

```
loop_dir = dirname(loop_lib.__file__)
real     = dirname(loop_lib.load_tree_lib(need=()).__file__)                 # memory-tree
lib_dir  = join(dirname(loop_dir), "lib") where that directory exists, else none
top      = git rev-parse --show-toplevel ; non-zero or FileNotFoundError -> print
           "scratch root check: no repository", top = none
if top and _is_under(tempfile.gettempdir(), top): refuse "scratch root <path> is inside the repository"
with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as scratch:
    copy loop_dir, real and lib_dir where it exists, as siblings named loop, memory-tree, lib
    ... 96 S9's child run, unchanged ...
    pass only where rc != 0 and "derive_constant_charges" in out
              and "govkit update --kits memory-tree" in out and "Traceback" not in out

_is_under(path, top):
    p, t = normcase(realpath(path)), normcase(realpath(top))
    splitdrive(p)[0] != splitdrive(t)[0] -> False
    try: return commonpath([p, t]) == t
    except ValueError: return False
```

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- `tools/memory-tree/design_lib.py:479-490` `read_design_conf(root)` reads the conf as bytes, decodes
  utf-8 with replace, folds CRLF and calls `parse_conf`. Its module header (line 33) calls it the ONE
  read of the conf. It is called at `tools/check-spec-tokens.py:1086` and
  `tools/memory-tree/asbuilt_view.py:833`. Imported from `tools/memory-tree/`, it read this repository's
  conf as 67 keys with `MEMORY_ROOT` `memory`.
- This repository's `.memory-tree.conf` holds 135 lines carrying a byte at or above 0x80.
- `tools/memory-tree/tree_lib.py` defines `parse_conf` (line 135), `read_text` (line 383), `kit_rel`
  (line 48) and `unfenced` (line 390) at module level.
- `.governance/` holds `deploy.toml` alone, with no `install.json`, and `tools/lib/resolve_kit_dir.py:30-34`
  reads `install.json` and falls back to no rows.
- No file under `tools/` calls `os.path.commonpath`, so no containment helper exists to reuse.
- `tools/loop/` is absent at base, so every module this unit writes is sibling-minted.
- Baselines over `memory/builds/dDeclaredLoop/spec/`, each grep as its criterion states, at HEAD:
  - over 41: §5 `no kit` 1 and `govkit update` 0; S1's range `resolve_kit_dir` 1 and `read_tree_conf` 0;
  - over 60's S2 range and 64's S1 range: `resolve_kit_dir` 1 and `read_tree_conf` 0 each;
  - over 90: S4's range `parse_conf` 0; AC4's range `parse_conf` 0;
  - over 92: §5 `3.3 MB` 0 and `three attributes` 1; the sketch `def load_tree_lib():` 1 and
    `load_tree_lib(*, need` 0;
  - over 94: S10's range `three-name` 1, `86 S21` 0 and `88 S33` 0; AC1's range `parse_conf` 0; AC18's
    range `du -sk` 0, `3.3 MB` 1, `leaves its copy behind` 1 and `ignore_cleanup_errors` 0; §5 `3.3 MB` 1;
    S24's range `whether it passes or fails` 1 and `ignore_cleanup_errors` 0; the sketch
    `TemporaryDirectory() as scratch` 1; S5's range and the probe `nested scope` 0 each;
  - over 95: the sketch `read_text` 1; Evidence `regardless of receiver` 0; the file `read_design_conf`
    0; §5 `unreadable` 0; AC4's range `breakpoints.py` 0; §7 `loop breakpoints fixtures` 0; AC5's range
    `through the receipt` 1 and `whose receipt names` 0;
  - over 96: S4's range `grep -cF` 0; S6's range and the probe `nested scope` 0 each; S9's range and the
    skew-row sketch `Traceback` 0 each; S13's range and the sketch `commonpath` 0 each; S12's range and
    the sketch `loop_lib.__file__` 0 each; §7 `loop breakpoints fixtures` 0 and
    `loop definition fixtures` 0.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the 95 minors and the 96 minors.** The halves are not disjoint by M6. S3 and S12
  both write 94 S10, and S4 and S20 both write 92 §5, which is clause 1. Each half re-renders the build
  README's units region, a generated index written with its generator, which is clause 3.
- **Leave 60 S2 and 64 S1 as they stand, their cite resolving to the amended 41 S1 (M2's other fix).**
  Both spell the `resolve_kit_dir("memory-tree", ...)` call themselves, so the forbidden route would
  stay prescribed in two specs.
- **Narrow 90 AC4's population to attributes read on a loader result (M5's other fix).** It changes a
  criterion three units already observe. S6's read leaves no `.read_text` attribute in `loop_lib.py`, so
  90 AC4 holds as written.
- **`read_text(encoding="utf-8")` for the read (M7's corrected fix as written).** The report's synthesis
  note reconciles it with M5 and M6: it adds a `.read_text` attribute read and can raise on bad bytes.
  S6's bytes read with replace, wrapped in S7's refusal, is that reconciled form.

## 5. Production-readiness checklist

- security — S7 names an unreadable conf instead of a traceback. S9 refuses a temp root inside the
  repository by path components, never by a string prefix. S11 closes the nested-scope escape from the
  route probe's symbol check.
- perf / scale — unchanged: one read of the conf, and one `git rev-parse` per plant run.
- error / empty / loading states — S7 names an unreadable conf, S8 names the no-repository case, and
  S10 refuses a skew row whose child crashed instead of refusing.
- observability — S7's and S8's lines name the path and the case.
- risks — the amendments land on specs whose units build before this one, each a rev bump with its §9
  line. The code items change functions that 95 and 96 build, at a pass that comes after both.
- testing — AC1 to AC21 as greps, probes, staged breaks and plant runs.
- migration — none: every reader is unbuilt at base.
- user docs — none: no adopter-facing command or flag moves.

## 6. Acceptance criteria

- **AC1** — When `awk '/^## 5/,/^## 6/'` over the 41 spec is piped to `grep -c "no kit"`, it prints 0, and
  piped to `grep -c "govkit update"`, it prints at least 1.
  Red when: 41 §5 still promises foreign rows where the loader refuses.
  figure: 1 and 0 at HEAD, PINNED 2026-10-24.
- **AC2** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over the 41 spec and over the 64 spec, and
  `awk '/^- \*\*S2\*\*/,/^- \*\*S3\*\*/'` over the 60 spec, are each piped to `grep -c resolve_kit_dir`,
  each prints 0, and piped to `grep -c read_tree_conf`, each prints at least 1.
  Red when: a spec outside the loader's units still prescribes the retired route.
  figure: 1 and 0 for each at HEAD, PINNED 2026-10-24.
- **AC3** — When `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'` over the 90 spec is piped to `grep -c parse_conf`,
  it prints at least 1. `awk '/^- \*\*S10\*\*/,/^- \*\*S11\*\*/'` over the 94 spec piped to
  `grep -c three-name` prints 0. `awk '/^- \*\*AC1\*\*/,/^- \*\*AC2\*\*/'` over the 94 spec piped to
  `grep -c parse_conf` prints at least 1.
  Red when: a sibling still spells the three-name tuple, or the 94 AC1 sentence 95 S5 orders is absent.
  figure: 0, 1 and 0 at HEAD, PINNED 2026-10-24.
- **AC4** — When `awk '/^- \*\*AC18\*\*/,/^## 7/'` over the 94 spec is piped to `grep -c "du -sk"`, it
  prints at least 1, and piped to `grep -c "3.3 MB"`, it prints 0. `awk '/^## 5/,/^## 6/'` over the 92
  spec and over the 94 spec, each piped to `grep -c "3.3 MB"`, print 0.
  Red when: 94 AC18 still demands the old figure, or §5 states two prices for one copy.
  figure: 0, 1, 0 and 1 at HEAD, PINNED 2026-10-24.
- **AC5** — When a `python -c` probe in `tools/loop/` runs 90 AC4's collection, the set of `ast.Attribute`
  names in `loop_lib.py` that are module-level `def`s of `tools/memory-tree/tree_lib.py` is a subset of
  `loop_lib.TREE_LIB_SYMBOLS` and does not hold `read_text`. In a scratch copy whose `loop_lib.py` gains
  `path.read_text()` beside the tuple, the probe names `read_text`.
  `awk '/^### The conf read, after/,/^### Write set/'` over the 95 spec piped to `grep -c read_text`
  prints 0, and `awk '/^### Evidence/,/^### The conf read/'` over it piped to
  `grep -c "regardless of"` prints at least 1.
  Red when: a build that follows 95's sketch reds 90 AC4.
  figure: the sketch grep prints 1 and the Evidence grep 0 at HEAD, PINNED 2026-10-24.
- **AC6** — A `python -c` probe in `tools/loop/` writes a scratch tree whose `.memory-tree.conf` holds
  `DESIGN_RECORD=dé` and `MEMORY_ROOT=records` with CRLF line endings. With `tools/memory-tree/` on
  `sys.path`, `loop_lib.read_tree_conf(tree) == design_lib.read_design_conf(tree)` prints `True`, with
  `PYTHONUTF8=0` in the probe's environment so the locale encoding would answer a locale read. `python loop_lib.py --fixture --plant conf-readers-declared` still exits 0
  naming `read_tree_conf`, and `grep -c read_design_conf` over the 95 spec prints at least 1.
  Red when: the read decodes in the locale encoding, or the two readers of one conf answer differently.
  figure: the 95 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC7** — When a `python -c` call of `loop_lib.read_tree_conf` runs in `tools/loop/` on a scratch tree
  whose `.memory-tree.conf` is a directory, it exits non-zero printing that path and
  `memory-tree conf unreadable`, and no `Traceback`. `awk '/^## 5/,/^## 6/'` over the 95 spec piped to
  `grep -c unreadable` prints at least 1.
  Red when: an unreadable conf ends in `IsADirectoryError` or `PermissionError` as a traceback.
  figure: the 95 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC8** — When 90 AC5's scratch copy, made under the run's scratch directory outside any repository,
  has `derive_constant_charges` removed from its `tree_lib.py`, `python budget.py --fixture --plant no-own-conf-read`
  in its `loop/` exits non-zero printing `derive_constant_charges` and `govkit update --kits memory-tree`,
  and no `Traceback`. A `python -c` probe parsing `budget.py` finds a `FileNotFoundError` handler around
  the row's `git rev-parse` call.
  Red when: the row raises `CalledProcessError`, or grades an empty top against the working directory.
  fixture: the copy is made at observation time, where `git rev-parse` exits 128.
- **AC9** — When `python -c "import budget as b; print(b._is_under('C:/projects/coding-governance-tmp', 'C:/projects/coding-governance'), b._is_under('C:/projects/coding-governance/x', 'C:/projects/coding-governance'), b._is_under('D:/x', 'C:/projects'))"`
  runs in `tools/loop/`, it prints `False True False`. `awk '/^- \*\*S13\*\*/,/^## 3/'` over the 96 spec
  piped to `grep -c commonpath` prints at least 1.
  Red when: a string-prefix test refuses a sibling directory that shares the repository's name as a
  prefix.
  fixture: the drive-letter paths need a Windows host, which node `d` is; the 96 grep prints 0 at HEAD,
  PINNED 2026-10-24.
- **AC10** — Take a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, whose `load_tree_lib` replaces its per-name check with a bare `getattr(tl, n)` for
  each name. Then `python budget.py --fixture --plant no-own-conf-read` in the copy's `loop/` exits
  non-zero, and its output does not hold `tree_lib lacking derive_constant_charges`. Over the unmodified
  `tools/loop/`, the label prints. `awk '/^### The skew row, after/,/^### Evidence/'` over the 96 spec
  piped to `grep -c Traceback` prints at least 1.
  Red when: the row certifies a named refusal while the child crashed with an `AttributeError`.
  figure: the 96 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC11** — A scratch copy as in AC10, unmodified but for one staged read per form in its
  `loop_witness.py`, holds four forms. They are a module-level `TL = ll.load_tree_lib(need=("GIT_ENV_LEAKS",))`
  read as `TL.derive_docstring_ids` inside a function, `lambda: ll.load_tree_lib(need=())`,
  `(tl := ll.load_tree_lib(need=()))` used inside a call, and `(ll.load_tree_lib(need=()) or x).derive_X`.
  The probe of 94 §4 "The tree_lib route probe" over the copy's `loop/` reports a hit for each. Over the
  unmodified `tools/loop/` it reports no hit. `awk '/^- \*\*S5\*\*/,/^- \*\*S6\*\*/'` over the 94 spec and
  `awk '/^- \*\*S6\*\*/,/^- \*\*S7\*\*/'` over the 96 spec, each piped to `grep -c "nested scope"`, print
  at least 1.
  Red when: a denylist probe passes a form no rule names.
  figure: both greps print 0 at HEAD, PINNED 2026-10-24.
- **AC12** — When `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'` over the 96 spec is piped to `grep -c "grep -cF"`,
  it prints at least 1. `awk '/^- \*\*S10\*\*/,/^- \*\*S11\*\*/'` over the 94 spec piped to
  `grep -c "86 S21"` and to `grep -c "88 S33"` each print at least 1.
  Red when: 96 AC4 reads a token 96 S4 never orders, or 94 S10 names no site.
  figure: each prints 0 at HEAD, PINNED 2026-10-24.
- **AC13** — When `python budget.py --fixture --plant confs-disagree` and
  `python breakpoints.py --fixture --plant confs-disagree` run in `tools/loop/`, each exits non-zero
  printing `records root:` and both values. `awk '/^- \*\*AC4\*\*/,/^- \*\*AC5\*\*/'` over the 95 spec piped
  to `grep -c breakpoints.py` prints at least 1.
  Red when: a root-resolution slip in `breakpoints.py` passes outside every criterion.
  figure: the 95 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC14** — When `awk '/^## 7/,/^## 8/'` over the 95 spec is piped to `grep -c "loop breakpoints fixtures"`,
  it prints at least 1.
  Red when: 95 still declares fewer legs than the files it edits trip.
  figure: 0 at HEAD, PINNED 2026-10-24.
- **AC15** — When `awk '/^## 7/,/^## 8/'` over the 96 spec is piped to `grep -c "loop breakpoints fixtures"`
  and to `grep -c "loop definition fixtures"`, each prints at least 1.
  Red when: 96 still omits the legs that run the `loop_lib.py` it edits.
  figure: each prints 0 at HEAD, PINNED 2026-10-24.
- **AC16** — When `awk '/^- \*\*AC5\*\*/,/^- \*\*AC6\*\*/'` over the 95 spec is piped to
  `grep -c "through the receipt"`, it prints 0, and piped to `grep -c "whose receipt names"`, it prints at
  least 1.
  Red when: the note still says this repository resolves the kit through a receipt it does not hold.
  figure: 1 and 0 at HEAD, PINNED 2026-10-24.
- **AC17** — When `awk '/^- \*\*S24\*\*/,/^## 3/'` over the 94 spec is piped to
  `grep -c "whether it passes or fails"`, it prints 0, and piped to `grep -c ignore_cleanup_errors`, at
  least 1. `awk '/^- \*\*AC18\*\*/,/^## 7/'` over it piped to `grep -c "leaves its copy behind"` prints 0
  and to `grep -c ignore_cleanup_errors` at least 1. `awk '/^### The tree_lib route, after/,/^### The tree_lib route probe/'`
  over it piped to `grep -cF "TemporaryDirectory() as scratch"` prints 0.
  Red when: 94 still forbids the surviving copy that 96 S13 accepts.
  figure: 1, 0, 1, 0 and 1 at HEAD, PINNED 2026-10-24.
- **AC18** — When `awk '/^### The tree_lib route/,/^### The OSError/'` over the 92 spec is piped to
  `grep -cF "load_tree_lib(*, need"`, it prints at least 1, and piped to `grep -cF "def load_tree_lib():"`,
  it prints 0.
  Red when: 92's sketch shows callers passing `need=` to a loader that takes none.
  figure: 0 and 1 at HEAD, PINNED 2026-10-24.
- **AC19** — When a scratch copy holding only `loop/` and `memory-tree/`, made under the run's scratch
  directory outside any repository, runs `python budget.py --fixture --plant no-own-conf-read` in its
  `loop/`, the output holds `tree_lib lacking derive_constant_charges` and no `Traceback`.
  `awk '/^- \*\*S12\*\*/,/^- \*\*S13\*\*/'` over the 96 spec piped to `grep -cF "loop_lib.__file__"` prints at
  least 1.
  Red when: the row assumes a sibling `tools/lib/` and ends in `FileNotFoundError`.
  figure: the 96 grep prints 0 at HEAD, PINNED 2026-10-24.
- **AC20** — When `awk '/^## 5/,/^## 6/'` over the 92 spec is piped to `grep -c "three attributes"`, it
  prints 0.
  Red when: 92 §5 prices three attributes against 94 §5's four.
  figure: 1 at HEAD, PINNED 2026-10-24.
- **AC21** — When `awk '/^- \*\*AC4\*\*/,/^- \*\*AC5\*\*/'` over the 90 spec is piped to `grep -c parse_conf`,
  it prints at least 1.
  Red when: 90 AC4 names two of the tuple's four members as if they were all of them.
  figure: 0 at HEAD, PINNED 2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop breakpoints fixtures` and `loop definition fixtures`, none
a leg at HEAD.

New arm: tools/loop/budget.py · covers AC10 · the skew row's pass predicate, staged with the loader's per-name check replaced by a bare attribute read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Rewrite 60 S2 and 64 S1, or let their cite resolve to the amended 41 S1 (id 14)?** (a) rev
  bumps of 60 and 64; (b) record that the cite resolves. The report judged both sound. 60 S2 and 64 S1
  spell the `resolve_kit_dir("memory-tree", ...)` call themselves, so (b) leaves the retired route
  prescribed in two specs. (a) satisfies every criterion (b) would and leaves none. RESOLVED (agent,
  2026-10-24, delegated): (a), S2.
  widens: none · relaxes: none
- **F3 — Fix 90 AC4 against `read_text` by changing the read or by narrowing the probe (id 8)?** (a)
  `loop_lib.py` makes no `.read_text` attribute read; (b) 90 AC4's population narrows to attributes on a
  loader result. (b) changes a criterion three units observe. (a) also serves ids 10 and 20 through S6's
  read. RESOLVED (agent, 2026-10-24, delegated): (a), S5 and S6.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-12 spec audit's 21 minors batched (11 MEDIUM, 10 LOW).

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy. These are 95's `read_tree_conf`,
whose read now mirrors `design_lib.read_design_conf` (`tools/memory-tree/design_lib.py:479`, S6), 96's
skew row of `budget.py` (S8 to S10, S19), 94's tree_lib route probe (S11), and the sibling specs' own
sentences (the rest). The containment test is the standard library's `os.path.commonpath`.
`python tools/codebase-map/reuse_lookup.py "read a conf file as utf-8 with replacement and normalised line endings"`
ranked `read`, `read_text`, `load_conf`, `parse_conf`, `read_conf` and `read_conf_key`. The memory-tree
tools' `load_conf` reads this same file through `tree_lib.read_text`
(`tools/memory-tree/gen_build_index.py:310-315`), which decodes strict utf-8
(`tools/memory-tree/tree_lib.py:383-387`). Reached from `loop_lib.py`, that is a `.read_text` attribute
read, which S5 keeps out, and a decode that can raise. `git grep` on the conf's name found
`read_design_conf`, the declared one read of this file with the replace decode, and S6 mirrors it.
`python tools/codebase-map/reuse_lookup.py "test whether a path sits inside another directory after realpath"`
ranked `build_spec_path_re`, `resolve_charter_path` and `buildComparablePath`
(`tools/hooks/scratch-guard.js`). None is a Python containment test callable from the copy-installed
loop kit, so no existing seam fits S9 and it stays the row's own helper. The memory-recall query
returned 95's spec, the round-12 report's M8, 96's §10 and the round-11 report's skew-row findings.

Recall terms used: read_tree_conf read_design_conf utf-8 replace skew row show-toplevel commonpath route probe nested scope minors batch
