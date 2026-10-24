# TOOL-dDeclaredLoop-95 — the loop kit reads `.memory-tree.conf` through `load_tree_lib`, so 94 AC1's route probe holds on the built tree

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 49 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-95-deviation-951.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-95-deviation-951.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-96 |

<!-- /gen:spec-records -->

## 1. Goal

The round-11 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**. No other id shares that item.

`TOOL-dDeclaredLoop-94` AC1 runs a probe over `tools/loop/` that counts any
`resolve_kit_dir("memory-tree", ...)` call outside `load_tree_lib` as a hit. Units 41 (order 6), 72
(order 36) and 79 (order 40) build before 94 (order 48), and each specifies a read of `.memory-tree.conf`
through the memory-tree kit's `parse_conf`, reached by that very call. Routed through the loader instead,
`parse_conf` is a member outside the three-name `TREE_LIB_SYMBOLS`, which is also a hit. Either way AC1 is
red on a correct build of the whole set.

This unit gives the loop kit one reader of `.memory-tree.conf`, `read_tree_conf`, which reaches
`parse_conf` through `load_tree_lib(need=("parse_conf",))`, and adds `parse_conf` to `TREE_LIB_SYMBOLS`.
94's probe then holds on the built tree with no exception in it. It builds immediately after 94 and
repairs `TOOL-dDeclaredLoop-94`.

## 2. Scope (IN)

- **S1** — `TREE_LIB_SYMBOLS` in `tools/loop/loop_lib.py` holds `parse_conf` beside
  `derive_docstring_ids`, `derive_constant_charges` and `GIT_ENV_LEAKS`. It is the union every caller of
  `load_tree_lib` may read, now four names. Observed by AC1, AC2.
- **S2** — `read_tree_conf(tree)` in `tools/loop/loop_lib.py` is the loop kit's one reader of
  `.memory-tree.conf`. Where `<tree>/.memory-tree.conf` is absent it returns `{}` and never calls the
  loader. Otherwise it returns `load_tree_lib(need=("parse_conf",)).parse_conf(text, {})`, the
  signature 79 S25 fixes. Observed by AC1, AC3, AC5.
- **S3** — Every `.memory-tree.conf` read units 41 and 72 specify takes S2. These are 41's read of
  `MEMORY_ROOT` and `DESIGN_RECORD` (41 S1, S2) and the `.memory-tree.conf` branch of
  `resolve_memory_root_source` (76 S1), whose root `resolve_memory_root` (72 S1) returns. Where an earlier
  pass reached `parse_conf` through its own `resolve_kit_dir` call, this pass moves that read onto S2.
  `resolve_memory_root_source` keeps its own test of the file's existence, which 82 S15's source needs.
  Observed by AC1, AC3, AC4.
- **S4** — A tree that holds `.memory-tree.conf` while no memory-tree kit resolves gets the loader's named
  refusal: the run exits non-zero printing `govkit update --kits memory-tree`, with no `Traceback`. A tree
  with no `.memory-tree.conf` reads it as empty, so 41's rows print `foreign build` and the root falls to
  the driver's conf or `memory`. 41 S2's clause "With no memory-tree kit or no conf" reads "With no
  `.memory-tree.conf`", and names the refusal for a conf that no kit reads, in this unit's rev bump of 41.
  Observed by AC5, AC6.
- **S5** — The sibling texts that spell the tuple name `parse_conf`: 90's sketch "The tree_lib route, after
  this unit", 92 S8 and 92's sketch of the same name, and 94's sketch "The tree_lib route, after this
  unit". 94 §5 "perf / scale" reads "at most four attributes per call". 94 AC1 states that its population
  holds `parse_conf` read in `loop_lib.py`. All of these land in this unit's rev bumps of 90, 92 and 94.
  Observed by AC6.

## 3. Non-goals (OUT)

- An exception in 94's probe for a conf reader. 94 §8 F2 already refused an exemption that grows with
  each new caller, and S2 leaves no site that would need one.
- 94's other probe classes: the escape forms and the positional `need` are the round-11 ids 13 and 14,
  scope items of `TOOL-dDeclaredLoop-96`.
- The report's left-shift gate, a run of each new AST or grep probe over the tree its predecessors leave
  before a spec is promoted. It is a second mechanism in the harness (BUILD-METHOD M2). The class is
  recorded at the close, and AC1 is this instance's run.
- `read_driver_conf` and the `.unattended.conf` branch of `resolve_memory_root_source`: 70's and 72's,
  unchanged.
- What a kit that resolves but fails to import answers inside `read_tree_conf`: the loader's refusal, as
  94 S21 states it. This unit adds no case of its own.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-94` — AC1's tree_lib route probe, §4's sketch "The tree_lib route, after this unit" and §5, which S1 and S5 make hold on the built tree (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-92` — `load_tree_lib`, S8 and its sketch "The tree_lib route, after this unit", whose tuple S5 restates (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S4, AC4 and the sketch "The tree_lib route, after this unit", whose tuple S5 restates and whose attribute probe AC2 re-runs (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-79` — S25 and AC25, the `parse_conf(text, {})` signature and the absent-file rule `read_tree_conf` keeps, which AC3 re-runs (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-76` — `resolve_memory_root_source`, whose `.memory-tree.conf` read S3 moves onto `read_tree_conf` (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root` and AC3's `confs-disagree` plant, which AC4 re-runs over the moved read (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-41` — S1's and S2's `.memory-tree.conf` read and AC1's plants, which S3 moves onto `read_tree_conf` and S4 restates for a conf no kit reads (the round-11 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-96` — the four-name `TREE_LIB_SYMBOLS`, `read_tree_conf` and 94's probe as this unit leaves it, which that unit's rewrites of 90's loader block and 94's probe keep (the round-11 spec audit's ids 1, 9, 13, 14)
- **hands-off** `TOOL-dDeclaredLoop-97` — `read_tree_conf`, which that unit declares in `CONF_READERS` so the `no-own-conf-read` rule answers its calls (the round-12 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-100` — S2, S4, §4's Evidence and sketch "The conf read, after this unit", §5, §7, §10, AC4 and AC5, with `read_tree_conf`, which that unit restates and hardens (the round-12 spec audit's ids 6, 7, 8, 10, 12, 20)

## 4. Design

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 41 S1 reads `MEMORY_ROOT` from `.memory-tree.conf` through `parse_conf`, "reached by
  `resolve_kit_dir("memory-tree", "tree_lib.py", here)`", and 41 S2 reads `DESIGN_RECORD` from the same
  conf. 41's Files touched names `tools/loop/loop_lib.py`.
- 72 S1 puts `resolve_memory_root(tree)` in `tools/loop/loop_lib.py`, reading `.memory-tree.conf`'s
  `MEMORY_ROOT` through `parse_conf`. 76 S1 makes `resolve_memory_root_source` carry 72's branches, and
  `resolve_memory_root` returns its root. 82 S15 names the source per branch by which conf exists.
- 79 S25 fixes the call as `parse_conf(text, {})`, an absent file read as empty text, and 79 AC25 greps
  `parse_conf(` in `loop_lib.py`.
- 94 §4 "The tree_lib route probe" counts any `resolve_kit_dir` call whose first argument is the str
  `memory-tree` outside `loop_lib.load_tree_lib` as a hit, and requires every member to be inside its
  call's `need` and every `need` to be a subset of `TREE_LIB_SYMBOLS`.
- 90 AC4 collects every `ast.Attribute` name in `loop_lib.py` that is also a module-level `def` of
  `tools/memory-tree/tree_lib.py` and requires the set to be a subset of `TREE_LIB_SYMBOLS`.
  `parse_conf` is such a `def` (`tools/memory-tree/tree_lib.py:135`), so a `tl.parse_conf` read beside a
  three-name tuple reds 90 AC4 as well.
- 90 S4 says every route that reaches `tree_lib` takes the loader.
- Over `memory/builds/dDeclaredLoop/spec/`, `parse_conf` occurs 0 times in 90's sketch range, 92's S8 range,
  92's sketch range and 94's sketch range. 94 §5 holds `at most three` once. 41's S2 range holds
  `no memory-tree kit` once.
- `tools/loop/` is absent at base, so every function this unit touches is sibling-minted.

### The conf read, after this unit

```
TREE_LIB_SYMBOLS = ("derive_docstring_ids", "derive_constant_charges", "GIT_ENV_LEAKS", "parse_conf")

def read_tree_conf(tree):                      # the loop kit's one .memory-tree.conf reader
    path = tree / ".memory-tree.conf"
    if not path.exists(): return {}            # no conf: the loader is never called
    return load_tree_lib(need=("parse_conf",)).parse_conf(path.read_text(), {})

resolve_memory_root_source(tree):  mt = read_tree_conf(tree).get("MEMORY_ROOT")    # 72 S1, 76 S1
41's tree read:                    conf = read_tree_conf(tree)                     # MEMORY_ROOT, DESIGN_RECORD
```

A tree holding the conf with no memory-tree kit reaches the loader, whose `LookupError` branch is 88 S33's
named refusal.

### Write set

This pass writes `tools/loop/loop_lib.py` (S1 to S3). Inside this build's folder it amends the specs of
41, 90, 92 and 94 as rev bumps, one per spec, each with its §9 line. `read_tree_conf` is a public
module-level `def`, so `memory/map/generated/symbols.json` gains its row. The build README's regions are
the generator's render.

### Inventory

- `read_tree_conf` — a public function in `tools/loop/loop_lib.py`, one row in
  `memory/map/generated/symbols.json`.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `memory/map/generated/symbols.json`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One stated exception in 94's probe, inside `resolve_memory_root` (the report's first option).** 41's
  read of `DESIGN_RECORD` is a second site that `resolve_memory_root` does not answer, so the probe stays
  red on 41's read. 90 AC4 also stays red on any `tl.parse_conf` read beside a three-name tuple.
  Widening the exception to a class of conf readers keeps two routes into `tree_lib`, against 90 S4.
- **The loader route with the loader's no-kit refusal caught inside each reader (the report's
  alternative as written).** The refusal exits the run, so catching it means catching the exit. That also
  swallows a kit that lacks `parse_conf` or fails to import, reading a broken install as an adopter's
  tree.
- **A keyword such as `absent_ok` that makes the loader return `None` where no kit resolves.** It keeps
  41 S2's no-kit clause, but every reader of a loader result must then handle `None`, and 94's probe
  gains a value form to grade. S2's existence test gives the no-conf case the same answer with no new
  keyword.

## 5. Production-readiness checklist

- security — one route into `tree_lib`, symbol-checked. A conf that no kit reads is refused by name
  rather than read as an adopter's tree (deny by default).
- perf / scale — one `hasattr` more per default-`need` call. `read_tree_conf` loads the kit once per
  call, as the earlier reads did.
- error / empty / loading states — no conf reads `{}` without the loader. A conf with no kit, a kit lacking
  `parse_conf` or a kit that fails to import is the loader's named refusal, never a traceback.
- observability — the refusal names `govkit update --kits memory-tree`, as 88 S33 states.
- risks — S4 narrows 41 S2's no-kit clause to the no-conf case. 41's criteria observe neither case, and
  AC5 observes both.
- testing — AC1 to AC6 as probes over the built tree, plant re-runs, a kit-less scratch copy and greps.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none: no adopter-facing command or flag moves.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe runs 94 §4's "The tree_lib route probe" over every `*.py` under
  `tools/loop/` as built through this unit, it reports no hit. Its population holds
  `("loop_lib.py", "parse_conf")` from a call whose `need` is `("parse_conf",)`.
  Red when: a conf read reaches `tree_lib` by its own `resolve_kit_dir` call, staged in a scratch copy of
  `tools/loop/`, `tools/lib/` and `tools/memory-tree/` by giving `read_tree_conf` that call. The probe
  over the copy's `loop/` then reports a hit naming `resolve_kit_dir`.
  figure: the population is DERIVED from the files at observation time.
- **AC2** — When 90 AC4's probe runs in `tools/loop/`, the `ast.Attribute` names in `loop_lib.py` that are
  module-level `def`s of `tools/memory-tree/tree_lib.py` form a subset of `loop_lib.TREE_LIB_SYMBOLS`
  holding `parse_conf`. `python -c "import loop_lib; print(len(loop_lib.TREE_LIB_SYMBOLS), 'parse_conf' in loop_lib.TREE_LIB_SYMBOLS)"`
  prints `4 True`.
  Red when: `parse_conf` is read beside a tuple that omits it, staged in a scratch copy by dropping it from
  the tuple.
- **AC3** — When a `python -c` probe parses every `*.py` under `tools/loop/`, every `Call` whose callee is
  named `parse_conf` sits inside `read_tree_conf`. `resolve_memory_root_source` and the function holding
  41's tree read each call `read_tree_conf`. `grep -n "parse_conf(" loop_lib.py` in `tools/loop/` shows
  every call passing text and a dict, and `python budget.py --fixture --plant no-confs` answers `memory`
  with no `Traceback`, 79 AC25 re-run.
  Red when: a second conf reader keeps its own `parse_conf` call.
- **AC4** — When `python loop_lib.py --fixture --plant actor-list-foreign` runs in `tools/loop/`, it exits 0
  printing both seeded rows as `foreign build`. `--plant actor-list-no-build` exits 1 naming
  `dNoSuchBuild`, and `python budget.py --fixture --plant confs-disagree` exits non-zero printing
  `records root:` and both values. These are 41 AC1 and 72 AC3, re-run over the moved read.
  Red when: the move drops `MEMORY_ROOT` or `DESIGN_RECORD`, or picks one conf silently.
- **AC5** — When a scratch copy of `tools/loop/` and `tools/lib/` alone sits under the run's scratch
  directory, outside any repository, `python loop_lib.py --fixture --plant actor-list-foreign` in the
  copy's `loop/` exits non-zero printing `govkit update --kits memory-tree`, with no `Traceback`.
  `python budget.py --fixture --plant no-confs` there answers `memory` with no `Traceback`.
  Red when: a conf that no kit reads passes as an adopter's tree, or a tree with no conf calls the loader.
  fixture: the scratch copy is made at observation time; a copy inside the repository resolves the real
  kit through the receipt and observes nothing.
- **AC6** — When each range below is piped to its grep, it prints at least 1:
  `awk '/^### The tree_lib route/,/^### Evidence/'` over the 90 spec with `grep -c parse_conf`;
  `awk '/^- \*\*S8\*\*/,/^- \*\*S9\*\*/'` and `awk '/^### The tree_lib route/,/^### The OSError/'` over the
  92 spec, each with `grep -c parse_conf`; `awk '/^### The tree_lib route, after/,/^### The tree_lib route probe/'`
  over the 94 spec with `grep -c parse_conf`; and `awk '/^## 5/,/^## 6/'` over the 94 spec with
  `grep -c "at most four"`. Over the same 94 range `grep -c "at most three"` prints 0, and
  `awk '/^- \*\*S2\*\*/,/^- \*\*S3\*\*/'` over the 41 spec piped to `grep -c "no memory-tree kit"` prints 0.
  Red when: a sibling still spells the three-name tuple, or 41 S2 still promises a foreign-build line where
  the loader refuses.
  figure: each `parse_conf` grep prints 0, `at most three` 1 and `no memory-tree kit` 1 at HEAD, PINNED
  2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures` and `loop definition fixtures`, neither a leg at HEAD. This pass
adds and moves no arm: AC1 to AC6 are probes and re-runs of plants that 41, 72 and 79 mint.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — How does the conf read stop reddening 94 AC1 (id 1)?** (a) one stated exception in 94's probe
  for `resolve_memory_root`; (b) the loader route, with the no-kit refusal caught in each reader; (c) one
  reader, `read_tree_conf`, on the loader route, with no conf read as empty before the loader is called.
  (a) leaves 41's read and 90 AC4 red. (b) swallows every refusal along with the no-kit one. (c)
  satisfies AC1 and 90 AC4 with no exemption, holds 90 S4 as written, and changes only 41 S2's no-kit
  clause, which no criterion observes. RESOLVED (agent, 2026-10-24, delegated): (c), S2 to S4.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-11 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-97 and TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 92's `load_tree_lib` in `tools/loop/loop_lib.py`, extended by one tuple member, with the
memory-tree kit's `parse_conf` (`tools/memory-tree/tree_lib.py:135`) as the function it reaches. The two
conf reads 41 and 72 specify are the kind's second instance, so they share `read_tree_conf` rather than
each keeping a copy.
`python tools/codebase-map/reuse_lookup.py "read a kit conf file through a sibling kit loader that checks its symbols"`
ranked `read`, `read_text`, `check`, `load`, `load_conf`, `kit_rel`, `parse_conf` and `resolve_kit_dir`.
`parse_conf` and `resolve_kit_dir` are the two the loader already reaches, and none of the others loads a
sibling kit's module. The memory-recall query returned the round-11 report's H1, 90's loader sketch and
64's §10 naming 41 S1's route.

Recall terms used: load_tree_lib TREE_LIB_SYMBOLS parse_conf resolve_memory_root memory-tree conf resolve_kit_dir route probe exemption
