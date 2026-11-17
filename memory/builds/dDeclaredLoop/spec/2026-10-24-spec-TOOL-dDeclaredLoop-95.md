# TOOL-dDeclaredLoop-95 — the loop kit reads `.memory-tree.conf` through the memory-tree kit's `read_design_conf` alone, and `load_tree_lib`'s tuple holds every name read on its result

**Status:** CLOSED · rev-3 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 49 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-95-deviation-951.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-95-deviation-951.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-95-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-95-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-95-deviation-952.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-95-deviation-952.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-95-red-fix-62.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-95-red-fix-62.md) | red-fix | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-95-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-95-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-95-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-95-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-95-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-95-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-96 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-11 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**. No other id shares that item.

When this spec's rev-2 was written, `TOOL-dDeclaredLoop-94` AC1 ran a probe over `tools/loop/` that counted any
`resolve_kit_dir("memory-tree", ...)` call outside `load_tree_lib` as a hit, and every `.memory-tree.conf`
read that units 41, 72 and 79 specified reached `parse_conf` by that call. No correct build of the set
held AC1. Rev-2 of this unit answered with `read_tree_conf` on the loader route and a four-name
`TREE_LIB_SYMBOLS`.

At rev-3 the defect has no trigger left. 94's rev-4 re-ground holds no route probe, no `need` argument and
no route sketch. Every loop conf read takes the memory-tree kit's `read_design_conf`, and no loop module
calls `parse_conf` (§4 Evidence). S1 to S5 are settled (§3). What this unit still owes is the observation
that the state holds once 94 S21 has rewritten `load_tree_lib` at order 48: no loop module calls
`parse_conf` and the absent-conf read answers `memory` (S6), and the tuple keeps the two names the loader
results are read for (S7). The pass writes no file of the tree. It builds at order 49 and closes on AC7 to
AC9.

## 2. Scope (IN)

- **S6** — Every `.memory-tree.conf` read of the loop kit takes `read_design_conf` of
  `tools/memory-tree/design_lib.py`, and no module under `tools/loop/` calls `parse_conf`. At this
  unit's pass, after 94 is built, the probe of AC7 finds no such call and the `no-confs` plant of
  `tools/loop/budget.py`, 79 AC25's, still answers `memory`. No code moves in this pass.
  Observed by AC7, AC9.
- **S7** — `TREE_LIB_SYMBOLS` in `tools/loop/loop_lib.py` holds `derive_docstring_ids` and
  `derive_constant_charges` after 94 S21 rewrites `load_tree_lib`, and every attribute `loop_lib.py`
  reads on a loader result is one of the two, so no conf read reaches `tree_lib` past the loader's test.
  Observed by AC8.

## 3. Non-goals (OUT)

- **S1 to S5, settled at HEAD.** Each was read on the branch tip §4 Evidence names. Their criteria, AC1
  to AC6, leave the scope with them; AC7 to AC9 are new labels, so a sibling's citation of an old one
  lands on this table.

| Item | Rev-2 ordered | Settled because |
|---|---|---|
| S1 | `parse_conf` as a third `TREE_LIB_SYMBOLS` member | no loop module reads `parse_conf` on a loader result (AC8), and 94 rev-4 §3 under 92 §8 F3 (c) keeps the two members with no `need` argument; a third member would refuse an older kit for a name nothing reads |
| S2 | `read_tree_conf(tree)`, the loop kit's one conf reader | `read_design_conf` of `tools/memory-tree/design_lib.py` is that reader: `{}` where the conf is absent, else `parse_conf` of its text with `{}`, the read rev-2 sketched and 79 S25's absent-file rule; a loop-kit wrapper of it is a layer no caller needs (F3) |
| S3 | the reads of 41, 72 and 76 moved onto S2 | 41 rev-5 S1 states `read_builds_dir` on `read_design_conf`, and `read_builds_dir` and `resolve_memory_root_source` call it at HEAD; `resolve_memory_root_source` keeps its own existence test for 82 S15's source |
| S4 | the loader's named refusal for a conf no kit reads, and 41 S2's no-kit clause narrowed | `tools/loop/kit.toml` declares `requires = ["memory-tree", "run-gates"]`, so an install holding the loop kit holds the memory-tree kit; `read_builds_dir` answers a kit that does not resolve with `(None, why)`, 41 rev-5 S1's `why`, which S2 prints as the foreign verdict; 41 is CLOSED and frozen |
| S5 | `parse_conf` in the tuples of 90's, 92's and 94's sketches, and 94 §5's "at most four" | 90 and 92 are CLOSED and frozen, and their two-name tuple is the built one; 94 rev-4 holds no route sketch, no route probe and no "at most" line to amend |

- A route probe over `tools/loop/`. 94 rev-4 holds none, and its §3 sets a ban on every `tree_lib` route
  out of scope, since `tools/loop/loop_transition.py` and `tools/loop/upstream.py` import `tree_lib` by
  name under 92 §8 F5 and 90 §8 F7.
- The report's left-shift gate, a run of each new AST or grep probe over the tree its predecessors leave
  before a spec is promoted. It is a second mechanism in the harness (BUILD-METHOD M2). The class is
  recorded at the close.
- `read_driver_conf` and the `.unattended.conf` branch of `resolve_memory_root_source`: 70's and 72's,
  unchanged.
- `load_tree_lib`'s catches and its every-name refusal: 94 S21, at order 48.
- `read_tree_conf`, `CONF_READERS` and the round-12 items that units 96 to 100 carry on them. Each of
  those units is re-grounded before its builder, against this rev.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-94` — rev-4's §3, which holds no route probe, no route sketch and no `need` argument, and S21's `load_tree_lib`, whose tuple S7 observes after order 48 (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-92` — `load_tree_lib` and §8 F3 (c), under which the tuple keeps its two members, settling S1 and S5 (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-90` — S4's tuple and AC4's loader-result collection, which AC8 re-runs, settling S5 (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-79` — S25 and AC25, the `no-confs` plant and its absent-file rule, which AC9 re-runs over `read_design_conf` (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-76` — `resolve_memory_root_source`, whose `.memory-tree.conf` read takes `read_design_conf`, settling S3 (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root`, whose root `resolve_memory_root_source` answers, settling S3 (the round-11 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-41` — rev-5 S1's `read_builds_dir` on `read_design_conf` and its foreign verdict, settling S3 and S4 (the round-11 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-96` — the two-name `TREE_LIB_SYMBOLS` and no `read_tree_conf`, the state this unit observes, which that unit's re-ground reads (the round-11 spec audit's ids 1, 9, 13, 14)
- **hands-off** `TOOL-dDeclaredLoop-97` — no `read_tree_conf` at HEAD for `CONF_READERS` to declare; `read_design_conf`, `read_driver_conf` and `parse_conf` are the reader calls `derive_conf_reads` grades, which that unit's re-ground reads (the round-12 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-100` — S2 and S4 settled on `read_design_conf` and the kit edge, and §4 Evidence, which that unit's re-ground reads in place of the `read_tree_conf` it restated (the round-12 spec audit's ids 6, 7, 8, 10, 12, 20)

## 4. Design

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every read is of
`branch/unattended-declared-loop-d56bf0` at `44be2307e`, its tree written by `git archive` into the run's
scratch directory, since this worktree is cut from main, which lacks the loop kit. The tip moved to
`77a7e1a26` while this rev was written; that commit writes unit 93's records and no file under `tools/`.
The plants ran in the extracted tree after a scratch `git init` and one commit. Each staged break ran in
a scratch copy of its `tools/loop/`, `tools/lib/` and `tools/memory-tree/`.

- `tools/loop/loop_lib.py#TREE_LIB_SYMBOLS` holds `derive_docstring_ids` and `derive_constant_charges`.
  `tools/loop/loop_lib.py#load_tree_lib` takes no argument and tests each name in tuple order. A
  `python -I` import printed the two-name tuple, the signature `()` and no `read_tree_conf` attribute.
- An `ast` probe over every `tools/loop/*.py` found no call whose callee is named `parse_conf`. It found
  seven `read_design_conf` calls PINNED: in `read_builds_dir` and `resolve_memory_root_source` of
  `loop_lib.py`, and in one function each of `adapt.py`, `loop_parents.py`, `loop_transition.py`,
  `position.py` and `upstream.py`.
- `tools/memory-tree/design_lib.py#read_design_conf` answers `{}` where `<root>/.memory-tree.conf` is not
  a file. Otherwise it answers `parse_conf` of the file's bytes decoded as UTF-8 with `replace` and CRLF
  folded, with `{}`. Its docstring calls it the one read of the conf.
- `tools/loop/loop_lib.py#resolve_memory_root_source` puts the kit on `sys.path` through
  `read_memory_tree("design_lib.py")` and reads `MEMORY_ROOT` through `read_design_conf(tree)`. It keeps
  its own `is_file` test of `.memory-tree.conf` for the source 82 S15 names.
- `tools/loop/loop_lib.py#read_builds_dir` finds the kit with
  `resolve_kit_dir("memory-tree", "design_lib.py", kit_dir)` and answers its `LookupError` with
  `(None, why)`. 41 rev-5 S1 states that read and that `why`.
- 90 AC4's collection of the attributes read on a loader result, run over `loop_lib.py`, gave
  `derive_constant_charges` and `derive_docstring_ids`, a subset of the tuple.
- 94 rev-4 holds no `### The tree_lib route` heading, and its one `parse_conf` match is
  `parse_conf_line` in its §10. Its §3 sets the `need` argument and `GIT_ENV_LEAKS` out under 92 §8 F3
  (c). Its hands-off bullet to this unit says rev-4 holds no route probe and no route sketch.
- The specs of units 41, 72, 76, 79, 90 and 92 are CLOSED at the tip, so frozen.
- `tools/loop/kit.toml` declares `requires = ["memory-tree", "run-gates"]`. In a scratch copy of
  `tools/loop/` and `tools/lib/` alone, `python budget.py --fixture --plant no-confs` ended in a
  `Traceback` from `remove_tree` in `tools/loop/loop_witness.py`, whose own
  `read_memory_tree("deviation_join.py")` reaches the kit outside any conf read. Rev-2's AC5 held on no
  reader design.
- `python budget.py --fixture --plant no-confs` in `tools/loop/` exited 0 printing `root memory` and
  `held`, in 1.4 s PINNED wall time.
- Staged breaks: `def fx_conf(t): return load_tree_lib().parse_conf(t, {})` appended to a scratch
  `loop_lib.py` made AC7's probe print 1 and AC8's collection hold `parse_conf`. With the absent branch
  of a scratch `read_design_conf` raising `FileNotFoundError`, the `no-confs` plant exited 1 printing
  `MISSED`.
- `memory/map/generated/symbols.json` holds no `read_tree_conf` row and one `read_design_conf` row.

### Write set

None under `tools/` and no sibling spec. The pass runs AC7 to AC9. The close's records and the build
README's regions are the main loop's and the generator's. The pass mints no public module-level `def`,
so `memory/map/generated/symbols.json` does not move.

### Files touched (estimate)

None under `tools/`.

### Alternatives rejected

- **Build `read_tree_conf` as rev-2 specified (F3 option b).** It wraps `read_design_conf` in a second
  function that adds nothing, and the route probe it answered is absent from 94 rev-4. Units 97 to 100
  would keep a subject, but each of them hardens a function with no caller.
- **Keep rev-2's four-name tuple.** The loader would refuse a memory-tree kit lacking `parse_conf` on
  every call, for a name no loop module reads on its result.
- **Settle S6 and S7 with S1 to S5 and close the unit unbuilt (F3 option c).** 94 S21 rewrites
  `load_tree_lib` at order 48, and the run keeps this unit's order and status, so the tuple is observed
  after that rewrite.

## 5. Production-readiness checklist

- security — one route into `tree_lib` per loader result, tested on the two names the kit reads; the
  conf reads take the memory-tree kit's own reader.
- perf / scale — one `ast` probe of one folder and one plant run, about 1.4 s PINNED 2026-11-17.
- error / empty / loading states — an absent conf reads `{}` through `read_design_conf`, which AC9
  observes; a kit that does not resolve is outside a valid install, since the loop kit requires it.
- observability — the plant's `root memory` and `held` lines are 79's; this pass reads them.
- risks — units 96 to 100 cite rev-2's `read_tree_conf` and four-name tuple; the sweep below names each,
  and each is re-grounded before its builder.
- testing — AC7 to AC9 as a probe, an import and a plant run.
- migration — none: no stored data.
- user docs — none: `grep -rln "read_tree_conf\|parse_conf\|TREE_LIB_SYMBOLS" help/` prints nothing at
  the tip, and no verb, flag or usage row is added.

### The sweep

The pass writes no file, so no function, constant or fixture moves. The readers below read this spec's
text, which the re-ground commit lands. Each count is DERIVED by the command beside it, run on the
branch tip.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| this spec's item and criterion ids | 96, 97, 99 and 100, DEFERRED, and the CLOSED 41 and 90, `grep -c "95 [SA][C0-9]" memory/builds/dDeclaredLoop/spec/*.md` less this spec | S1 to S5 and AC1 to AC6 keep their labels on §3's table, so each citation lands; the four unbuilt specs are re-grounded before their builders, and 41's and 90's text is frozen record |
| the edges naming this unit | ten bullets, seven hands-off from 41, 72, 76, 79, 90, 92 and 94 and three consumes-from from 96, 97 and 100, `grep -n "^- \*\*[a-z-]*\*\* .TOOL-dDeclaredLoop-95. " memory/builds/dDeclaredLoop/spec/*.md` | rev-3 keeps the ten mirrored bullets, verbs and targets unchanged |
| the H1 title | the units row of `memory/builds/dDeclaredLoop/README.md`, a generated region; the `After:` line of `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-95-deviation-951.md` | the dispatcher's index regeneration renders rev-3; the deviation record is history and keeps rev-1's title |
| this spec's positional rows | `memory/project/positional-refs.txt`, two rows naming this spec, `grep -c "dDeclaredLoop-95.md" memory/project/positional-refs.txt` | rev-3 keeps the `BUILD-METHOD M2` row in §3 and cites code by symbol only, so its row citing a line of `tools/memory-tree/tree_lib.py` goes stale; the commit landing rev-3 runs `python tools/playbook/positional.py shrink` |
| the symbol tier | `memory/map/generated/symbols.json`, `grep -c read_tree_conf memory/map/generated/symbols.json` printing 0 | no def is minted, so no row moves |
| the `loop budget fixtures` leg | `tools/gate-legs.json`, whose argv runs `budget.py --selftest`, every plant, `no-confs` among them | the pass adds and moves no plant row and no budget |
| the lexicon offender pin | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at the tip | no new function or constant name, so no `--suggest` run is owed |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` reads tracked `*.sh` files | the pass writes no shell script; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts and `tools/loop/` holds no `.families.txt` |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md`, eleven paths PINNED at the tip | it names no path under `memory/builds/` or `tools/loop/` |
| the install-prefix ban, the verdict-epoch delegates, subject pins, upgrade steps, help anchors and usage rows | `tools/check-install-prefix.sh`, `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py`, `help/` | the pass writes no shipped file, leg, step, verb or flag |

Order: this unit reads the code units 41, 72, 76, 79 and 90 built, each CLOSED at the tip, and 94 S21's
`load_tree_lib`, which lands at order 48 as 94 rev-4 states it. Unit 93, at order 47, writes no file.
Units 96 to 99 at order 50 and 100 at order 51 read this rev.

## 6. Acceptance criteria

- **AC7** — When a `python -I -c` probe in `tools/loop/` parses every `*.py` there with `ast` and counts
  each `Call` whose callee, a name or an attribute, is `parse_conf`, it prints 0.
  `grep -c "read_design_conf(" loop_lib.py` in the same folder prints at least 2.
  Red when: a loop module calls `parse_conf` itself, staged in a scratch copy by appending
  `def fx_conf(t): return load_tree_lib().parse_conf(t, {})` to its `loop_lib.py`, where the probe prints 1.
  figure: 0 and 2 at the tip, PINNED 2026-11-17.
- **AC8** — When `python -I -c "import sys; sys.path.insert(0, '.'); import loop_lib; print(loop_lib.TREE_LIB_SYMBOLS)"`
  runs in `tools/loop/`, it prints `('derive_docstring_ids', 'derive_constant_charges')`. 90 AC4's
  collection over `loop_lib.py`, every attribute read on a `load_tree_lib()` call or a name bound from
  one in the same function body, is a subset of that tuple.
  Red when: a loader result is read for a name outside the tuple, staged by the same appended
  `fx_conf`, where the collection holds `parse_conf`.
- **AC9** — When `python budget.py --fixture --plant no-confs` runs in `tools/loop/`, it exits 0 and prints
  `root memory` and `held`, with no `Traceback`. This is 79 AC25 re-run over `read_design_conf`.
  Red when: an absent conf reads as an error, staged in a scratch copy by making the absent branch of
  `read_design_conf` in its `design_lib.py` raise `FileNotFoundError`, where the plant exits 1 printing
  `MISSED`.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's leg this pass keeps green, a leg in `tools/gate-legs.json` on the branch and absent from
main's: `loop budget fixtures`, which runs `budget.py --selftest`, the `no-confs` plant among its plants.
This pass adds and moves no arm: the `no-confs` plant is 79's arm, and AC7 and AC8 are probes.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — How does the conf read stop reddening 94 AC1 (id 1)?** (a) one stated exception in 94's probe
  for `resolve_memory_root`; (b) the loader route, with the no-kit refusal caught in each reader; (c) one
  reader, `read_tree_conf`, on the loader route, with no conf read as empty before the loader is called;
  (d) none, settled in §3. Rev-2 chose (c). 94 rev-4 holds no route probe, so no conf read reddens it,
  and `read_design_conf` is already the one reader. Recommendation: (d).
  RESOLVED (agent, 2026-11-17, delegated): (d). widens: none · relaxes: none
- **F3 — With S1 to S5 settled at HEAD, does the unit still build?** (a) yes, as an observation pass at
  order 49 that writes no file and closes on AC7 to AC9; (b) build `read_tree_conf` as a loop-kit
  wrapper of `read_design_conf`, so units 97 to 100 keep the function they cite; (c) settle S6 and S7
  too and close the unit unbuilt. (b) mints a layer no caller needs, against [yagni]. The tuple S7
  observes is rewritten by 94 S21 at order 48, and the run keeps this unit's order and status.
  Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-11 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-97 and TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 S2 S3 S4 S5 S6 S7 AC7 AC8 AC9 · re-grounded on the
  code at `branch/unattended-declared-loop-d56bf0` by 2026-11-17-prompt-TOOL-dDeclaredLoop-95-1-spec-writer:
  S1 to S5 settled in §3, 94 rev-4 holding no route probe and every loop conf read taking
  `read_design_conf`; S6 and S7 observations with no code write; AC1 to AC6 leave with their items and
  AC7 to AC9 observe the settled state; the H1 states the observed state; the ten Edges bullets kept
  with their payloads re-worded; §5's sweep added; F2 re-marked (d) and F3 added.

## 10. Reuse audit

The seam is `read_design_conf` of `tools/memory-tree/design_lib.py`, the memory-tree kit's one reader of
the conf, which every loop conf read already calls, observed in place. No reader and no checker is
minted.
`python tools/codebase-map/reuse_lookup.py "read the memory tree conf file into a dict, empty where the file is absent"`,
run on the branch tip 2026-11-17, ranked `read_text`, `read`, `load_conf`, `parse_conf`,
`read_memory_tree` and `read_design_conf` among its seams. `read_design_conf` is the one that reads this
conf with the absent-file rule, and `parse_conf` and `read_memory_tree` are the two it and its callers
already reach. The memory-recall query at rev-1 returned the round-11 report's H1, 90's loader sketch and
64's §10 naming 41 S1's route.

Recall terms used: read_design_conf load_tree_lib TREE_LIB_SYMBOLS parse_conf resolve_memory_root_source read_builds_dir memory-tree conf route probe observation pass
