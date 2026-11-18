# TOOL-dDeclaredLoop-97 — the no-own-conf-read rule reads its reader calls from one declared tuple, `CONF_READERS`, which holds the three callee names it answers

**Status:** CLOSED · rev-2 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-97-deviation-971.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-97-deviation-971.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-97-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-97-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-97-2-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-97-2-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-97-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-97-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-97-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-97-reground-brief.md) | research | — |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
confirmed finding **id 1 at HIGH**, in its item **H1**. Ids 11 and 19 share that item, and each is its
own unit: `TOOL-dDeclaredLoop-98` (id 11) and `TOOL-dDeclaredLoop-99` (id 19).

When rev-1 was written, `TOOL-dDeclaredLoop-95` S2 minted `read_tree_conf(tree)` as the loop kit's
reader of `.memory-tree.conf`, and the `no-own-conf-read` rule, `derive_conf_reads`, named its reader
callees by hand. A call of the new reader in `budget.py` or `breakpoints.py` would then have passed the
plant (76 S3) around `resolve_memory_root` and its `confs-disagree` refusal (72 AC3).

At rev-2 that instance has no trigger. 95 rev-3 builds no `read_tree_conf`: every loop read of the conf
takes the memory-tree kit's `read_design_conf`, which the rule already answers (§4 Evidence). The class
stays. `derive_conf_reads` holds its three callee names as a literal inside its body, and the plant row
of `TOOL-dDeclaredLoop-98` and the completeness check of `TOOL-dDeclaredLoop-99`, both at order 50,
read the same names. This unit names them once, in the tuple `CONF_READERS` in
`tools/loop/loop_lib.py`, and makes the rule read that tuple. The rule, the row and the check then read
one source, and a reader added later is one entry. It builds at order 50, before 98 and 99.

## 2. Scope (IN)

- **S1** — `CONF_READERS = ("read_design_conf", "read_driver_conf", "parse_conf")` is a module-level
  tuple in `tools/loop/loop_lib.py`, set directly above `derive_conf_reads` under a `#` comment that
  names it the callees the rule answers as a `reader call`. Each member is a function: `read_driver_conf`
  of `loop_lib.py`, `read_design_conf` of `tools/memory-tree/design_lib.py` and `parse_conf` of
  `tools/memory-tree/tree_lib.py`. The tuple keeps the order the rule's literal holds at HEAD.
  Observed by AC1.
- **S2** — `derive_conf_reads` answers `(line, "reader call")` for a call whose callee name is a member
  of its own module's `CONF_READERS`, looked up when the call runs. The callee name is an attribute's
  name, or the last segment of what `derive_import_aliases` binds a name to, as built. The function body
  holds no literal list of reader names. Its docstring and its row in the table of `loop_lib.py`
  functions in `tools/loop/README.md` name the tuple where each now lists the three names. Every other
  kind, the alias resolution and the fixture boundary stay as built. Observed by AC2, AC3, AC4, AC5.
  **Readers:**
  by name: `tools/loop/README.md`, its table row for the rule, which spells the three callee names
  by value: `tools/loop/budget.py` and `tools/loop/breakpoints.py`, whose `no-own-conf-read` plants and `conf-read-forms` rows compare the rule's hits with the hits they owe

## 3. Non-goals (OUT)

- **Rev-1 items settled at HEAD.** Each was read on the branch tip §4 Evidence names. Rev-1's AC4 leaves
  the scope with S3; AC5 is a new label, so a sibling's citation of AC4 lands on this table.

| Item | Rev-1 ordered | Settled because |
|---|---|---|
| S1's member `read_tree_conf` | the tuple holds `read_driver_conf` and `read_tree_conf`, each a `def` of `loop_lib.py` | no `read_tree_conf` exists at HEAD and 95 rev-3 builds none; the loop kit's `.memory-tree.conf` reads take `read_design_conf`, so S1 holds the three names the built rule answers |
| S2's literal pair | the rule's set grows from `parse_conf` and `read_driver_conf` to the tuple | the built rule already answers `read_design_conf` beside those two, since 76's build (§4 Evidence); S2 moves that set into the tuple and adds no member |
| S3 and AC4 | rev bumps of 76 S2 and its sketch, and of 82 S10 and its sketch, reading "a member of `CONF_READERS`" | 76 and 82 are CLOSED and frozen; their hands-off bullets to this unit stand as record, and the code's docstring and README row carry the restatement (S2) |

- The plant row that observes the rule answering each member of the tuple on every run: id 11's
  mechanism, `TOOL-dDeclaredLoop-98`.
- The check that keeps the tuple complete as `loop_lib.py` grows: id 19's mechanism,
  `TOOL-dDeclaredLoop-99`. Two members are defined outside `loop_lib.py`, which that unit's
  re-ground reads (§5).
- `read_tree_conf`, a loop-kit wrapper of `read_design_conf`: 95 rev-3 §8 F3 refuses it as a layer no
  caller needs.
- `resolve_memory_root` and `resolve_memory_root_source`. They return a resolved root, not a conf's
  values, so they are the sanctioned route and stay out of the tuple.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-95` — rev-3's settled state, no `read_tree_conf` and every `.memory-tree.conf` read on `read_design_conf`, which S1 declares beside `read_driver_conf` and `parse_conf` (the round-12 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-76` — S2's `derive_conf_reads` and its built callee set, which S2 moves into `CONF_READERS`; its frozen sketch "The rule" keeps its text (the round-12 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-82` — S10's alias resolution, which S2 keeps; its frozen sketch "The conf-read rule, after this unit" keeps its text (the round-12 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-98` — `CONF_READERS` and the `reader call` kind read from it, which that unit's plant row observes for every member (the round-12 spec audit's ids 1, 11)
- **hands-off** `TOOL-dDeclaredLoop-99` — `CONF_READERS`, two of whose members are defined outside `loop_lib.py`, which that unit's check compares with the functions of `loop_lib.py` that open a conf (the round-12 spec audit's ids 1, 19)

## 4. Design

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every read is of
`branch/unattended-declared-loop-d56bf0` at `c35e8d15d`, its `tools/` and `memory/` written by
`git archive` into the run's scratch directory, since this worktree is cut from main, which lacks the
loop kit. 95 rev-3 was read from the dispatcher's pending copy, not yet on the branch. Each staged break
and the prototype of S1 and S2 ran in a scratch copy of `tools/loop/`, `tools/lib/` and
`tools/memory-tree/`.

- `tools/loop/loop_lib.py#derive_conf_reads` answers `reader call` where the callee name is in the
  literal `("read_design_conf", "read_driver_conf", "parse_conf")` inside its body, and its docstring
  names the same three. `git log -S` over `loop_lib.py` finds that literal first in `199b4aa16`, 76's
  build. `grep -c '"read_design_conf", "read_driver_conf", "parse_conf"' tools/loop/loop_lib.py`
  prints 1.
- `grep -rn read_tree_conf tools/` prints nothing, and an import of `loop_lib` has no `CONF_READERS`.
- Seven `read_design_conf` calls sit in `tools/loop/` PINNED: two in `loop_lib.py`, in `read_builds_dir`
  and `resolve_memory_root_source`, and one each in `adapt.py`, `loop_parents.py`,
  `loop_transition.py`, `position.py` and `upstream.py`, as 95 rev-3 §4 counts them.
- `tools/memory-tree/design_lib.py#read_design_conf` and `tools/memory-tree/tree_lib.py#parse_conf`
  are module-level functions, and `tools/loop/loop_lib.py#read_driver_conf` is one of `loop_lib.py`.
- The callers of `derive_conf_reads` are `budget.py` and `breakpoints.py` alone. DERIVED by
  `grep -rn "derive_conf_reads(" tools/ --include=*.py`, which prints eight call sites in `budget.py`
  and one in `breakpoints.py` beside the `def`.
- `tools/loop/README.md`, the `derive_conf_reads` row of its function table, spells
  "one `reader call` per call of `read_design_conf`, `read_driver_conf` or `parse_conf`".
  `grep -c CONF_READERS tools/loop/README.md` prints 0.
- At the tip, `def _root_probe(tree): return loop_lib.read_design_conf(tree)` appended to a scratch
  copy's `budget.py` made `budget.py --fixture --plant no-own-conf-read` exit 1, printing
  a `reader call` hit on the staged line of `budget.py` and `MISSED 1 conf read(s) in budget.py`. The same
  line in its `breakpoints.py` printed a `reader call` hit on the staged line of `breakpoints.py` and exited 1. Unmodified, each plant exits 0
  printing `held`. Id 1's consequence has no instance at HEAD.
- The prototype, the tuple set beside `TREE_LIB_SYMBOLS` and the body's literal swapped for the
  tuple: both `no-own-conf-read` plants and the `conf-read-forms` plant exited 0, the last in
  0.8 s PINNED wall time. AC1's probe printed the tuple and `[]`. AC2's probe answered nine
  `reader call` hits, then ten once the module's tuple gained a name. With the literal kept beside the
  tuple, it answered nine and nine. With `CONF_READERS = ()`, the `aliased-reader` row printed `no hit`
  and the plant exited 1.
- The specs of units 76 and 82 are CLOSED at the tip, so frozen. 98 rev-1 S1 to S3 read
  `loop_lib.CONF_READERS` and stage a call of each member. 99 rev-1 S2 compares the tuple both ways with
  the openers its S1 derives from `loop_lib.py`.
- `loop_lib.py` holds no `__all__`, and `tools/codebase-map/map_lib.py#python_symbols` makes a module
  constant a symbol row only as a static `__all__` member. `memory/map/generated/symbols.json` holds no
  `TREE_LIB_SYMBOLS` row.

### The rule, after this unit

```
# Every callee derive_conf_reads answers as a reader call (TOOL-dDeclaredLoop-97 S1).
CONF_READERS = ("read_design_conf", "read_driver_conf", "parse_conf")

derive_conf_reads(path):
    ... 82 S10's walk, 86's and 87's kinds, 80 S1's boundary, unchanged
    Call whose callee name, resolved by derive_import_aliases, is in CONF_READERS
                                                                    -> (line, "reader call")
```

`TREE_LIB_SYMBOLS`, read by `load_tree_lib`, is the precedent: one module tuple that the code and its
plant rows read.

### Write set

This pass writes `tools/loop/loop_lib.py` (S1, S2) and the `derive_conf_reads` row of
`tools/loop/README.md` (S2). It writes no sibling spec. `CONF_READERS` is a module-level tuple, not a
`def` or a class, and `loop_lib.py` gains no `__all__`, so `memory/map/generated/symbols.json` does not
move. The build README's regions are the generator's render.

### Inventory

- `CONF_READERS` — a module-level tuple in `tools/loop/loop_lib.py`. It is not a symbol row
  (`tools/codebase-map/map_lib.py#python_symbols`).

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/README.md`

### Alternatives rejected

- **Settle id 1 in §3 and build nothing (F2 option c).** The literal set then has no name, and 98's row
  and 99's check, at order 50, would each hold a copy of the three names beside the rule's.
- **A tuple of the loop kit's own readers alone, `("read_driver_conf",)`, with the memory-tree kit's
  two names kept literal in the rule (F3 option b).** The rule would read two sources, and 98's row,
  which stages each member, would never stage `read_design_conf`, the reader every loop module takes.
- **Read the tuple by parsing the sibling `loop_lib.py`, as 86 S13 reads the conf constants.** The rule
  runs inside `loop_lib.py`, so its own module global is that tuple. In a scratch copy, the copy's
  `loop_lib.py` is the module that runs.

## 5. Production-readiness checklist

- security — the `no-own-conf-read` rule answers every name the tuple declares, so `confs-disagree`
  (72 AC3) is not bypassed through a declared reader; the set it answers is the one at HEAD.
- perf / scale — one tuple membership test per call node, as the literal was, and no new parse.
- error / empty / loading states — unchanged: 86 S13's and 88 S33's refusals stand. An empty tuple
  answers no `reader call`, which 82 AC10's `aliased-reader` row reds (AC4).
- observability — a hit names `<file>:<line> reader call`, as 76 S3 prints it.
- risks — a reader missing from the tuple is invisible to the rule. `TOOL-dDeclaredLoop-99` checks the
  tuple against `loop_lib.py`, and its re-ground reads the two members defined outside it.
- testing — AC1 to AC5 as probes, staged breaks in scratch copies and greps.
- migration — none: no stored data, and the rule answers the set it answers at HEAD.
- user docs — `tools/loop/README.md`'s `derive_conf_reads` row (S2). `help/loop.md` names a "conf
  reader call" and no reader name, and no verb, flag or usage row is added.

### The sweep

Each count is DERIVED by the command beside it, run on the branch tip.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| `derive_conf_reads`' callee set, now the tuple | the `no-own-conf-read` plants of `budget.py` and `breakpoints.py` and the `conf-read-forms` plant, `grep -rn "derive_conf_reads(" tools/ --include=*.py` | the tuple holds the literal's three names in its order, so every hit is the one at HEAD; the prototype ran all three plants to exit 0 |
| the `loop budget fixtures` and `loop breakpoint fixtures` legs | `tools/gate-legs.json`, whose argv runs each module's `--selftest`, these plants among them | the plants' owed hits do not move, and no row, plant or budget is added |
| the `loop definition fixtures` leg | `loop_lib.py --selftest` | it calls no `derive_conf_reads`; the tuple is a constant beside the rule |
| the `derive_conf_reads` README row | `tools/loop/README.md`, `grep -n "derive_conf_reads(path)" tools/loop/README.md`; 94 S21 rewrites the `load_tree_lib` row above it at order 48 | S2 edits the row's reader-call clause alone and leaves the rest as 94 leaves it |
| the rule's docstring | `tools/memory-tree/tree_lib.py#derive_docstring_ids` excludes it from the `conf name` kind | the docstring names no conf file, so no grade moves |
| a public module constant | `.lexicon.conf` CELLS, `grep -nE "^[ \t]+py\.constant[ \t]+[A-Za-z]" .lexicon.conf` printing nothing | no `py.constant` cell is declared, so no armed constant figure moves |
| the lexicon offender pin | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at the tip | no function is minted, so no `--suggest` run is owed |
| the conf-constant kind | `tools/loop/loop_lib.py#derive_conf_constants` over `loop_lib.py` | the tuple holds no conf name; the prototype's call answered `[]` |
| the symbol tier | `memory/map/generated/symbols.json`, `grep -c CONF_READERS memory/map/generated/symbols.json` printing 0 | no `def`, class or `__all__` is added |
| this spec's item and criterion ids | 98 cites S1, S2 and AC3, 99 cites S2, `grep -no "97 [SA]C\?[0-9]*" memory/builds/dDeclaredLoop/spec/*.md` | S1, S2 and AC3 keep their meaning; rev-1's S3 and AC4 land on §3's table |
| the edges naming this unit | five bullets, three hands-off from 76, 82 and 95 and two consumes-from from 98 and 99, `grep -n "^- \*\*[a-z-]*\*\* .TOOL-dDeclaredLoop-97. " memory/builds/dDeclaredLoop/spec/*.md` | rev-2 keeps its five mirrored bullets, verbs and targets unchanged |
| the H1 title | the units row of `memory/builds/dDeclaredLoop/README.md`, a generated region; the `After:` line of `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-97-deviation-971.md` | the dispatcher's index regeneration renders rev-2; the deviation record is history and keeps rev-1's title |
| this spec's positional rows | `memory/project/positional-refs.txt`, two rows naming this spec, `grep -c "dDeclaredLoop-97.md" memory/project/positional-refs.txt` | rev-2 cites code by symbol only, so both rows, each a line of `tools/codebase-map/map_lib.py`, go stale; the commit landing rev-2 runs `python tools/playbook/positional.py shrink` |
| the siblings at order 50 | 98 rev-1 and 99 rev-1, DEFERRED | each is re-grounded before its builder against this rev; 99's second case reads the members `loop_lib.py` defines |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` reads tracked `*.sh` files | the pass writes no shell script; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts and `tools/loop/` holds no `.families.txt` |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md` | `grep "^watch:" memory/guides/SESSION-KICKOFF.md \| grep -c "tools/loop"` prints 0 |
| the install-prefix ban, the verdict-epoch delegates, subject pins, upgrade steps, help anchors and usage rows | `tools/check-install-prefix.sh`, `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py`, `help/` | the pass writes no shipped install line, leg, step, verb or flag |

Order: this unit reads the code units 76, 82, 86, 87 and 88 built, each CLOSED at the tip, and
`load_tree_lib` as 94 S21 leaves it at order 48. 95 rev-3, at order 49, writes no file. 96 builds
beside it at order 50 and writes no line it writes; 98 and 99 build after it at order 50, and 100 at
order 51.

## 6. Acceptance criteria

- **AC1** — When
  `python -I -c "import sys, inspect; sys.path.insert(0, '.'); import loop_lib as ll; ll.read_memory_tree('design_lib.py'); import design_lib, tree_lib; print(ll.CONF_READERS, [n for n in ll.CONF_READERS if not any(inspect.isfunction(getattr(m, n, None)) for m in (ll, design_lib, tree_lib))])"`
  runs in `tools/loop/`, it prints `('read_design_conf', 'read_driver_conf', 'parse_conf') []`.
  Red when: the tuple names a function none of the three modules defines, staged in a scratch copy by
  appending `"read_tree_conf"` to it, where the list prints `['read_tree_conf']`. At the tip the probe
  ends in an `AttributeError` naming `CONF_READERS`.
- **AC2** — A `python -I` probe in `tools/loop/` copies `loop_lib.py` into a fresh scratch directory,
  the layout 86 S15 places, and writes beside it a module holding, for each member `m` of
  `loop_lib.CONF_READERS`, a call `loop_lib.m(t)` after `import loop_lib`, `ll.m(t)` after
  `import loop_lib as ll` and `r<i>(t)` after `from loop_lib import m as r<i>`, each in its own
  function, then `ll.read_kit_conf(t)`. `derive_conf_reads` on that module answers nine hits, each
  `reader call`. With the probe's imported `loop_lib.CONF_READERS` extended by `"read_kit_conf"`, it
  answers ten.
  Red when: the rule keeps its literal beside the tuple, staged in a scratch copy, where the probe
  answers nine and nine.
  figure: nine and ten DERIVED, three members times three spellings, plus the one extra name.
- **AC3** — Take a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, and give its `budget.py` the module-level
  `def _root_probe(tree): return loop_lib.read_design_conf(tree)`. Then
  `python budget.py --fixture --plant no-own-conf-read` in the copy's `loop/` exits 1 printing
  `budget.py:<line> reader call`. The same edit to the copy's `breakpoints.py` makes
  `python breakpoints.py --fixture --plant no-own-conf-read` exit 1 printing
  `breakpoints.py:<line> reader call`. Over the unmodified `tools/loop/`, both plants exit 0 printing
  `held`.
  Red when: a reader calling a declared reader passes the plant, the report's consequence for id 1,
  staged by `CONF_READERS = ()` in the copy's `loop_lib.py`, where both plants exit 0.
  fixture: the copy is made at observation time; the name `_root_probe` holds neither `fixture` nor
  `plant`, so 80 S1's boundary does not pass over it.
- **AC4** — `python budget.py --fixture --plant conf-read-forms` in `tools/loop/` exits 0 and prints
  `conf-read-forms · aliased-reader · line 2 reader call`, 82 AC10's row over the tuple.
  Red when: the tuple is empty, staged by `CONF_READERS = ()` in a scratch copy, where the row prints
  `no hit` and the plant exits 1.
- **AC5** — In `tools/loop/`, `grep -c '"read_design_conf", "read_driver_conf", "parse_conf"' loop_lib.py`
  prints 1, the tuple's line, and `grep -c CONF_READERS README.md` prints at least 1.
  Red when: the body keeps its literal, which prints 2, or the README row still lists the three names
  with no tuple, which prints 0.
  figure: 1 and 0 at the tip, PINNED 2026-11-17.

## 7. Gates

`recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's legs this pass keeps green, each a leg in `tools/gate-legs.json` on the branch and absent
from main's: `loop budget fixtures` and `loop breakpoint fixtures`, whose `--selftest` runs the
`no-own-conf-read` and `conf-read-forms` plants, and `loop definition fixtures`. This pass adds and
moves no arm: AC1 to AC5 are probes, staged breaks and greps. The lasting arm over this rule is
`TOOL-dDeclaredLoop-98`'s.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — With no `read_tree_conf` at HEAD, does the rule still read a declared tuple (id 1)?** (a) the
  rule's literal gains one name, rev-1's first option, which has no name left to add; (b) the rule reads
  `CONF_READERS`, one tuple in `loop_lib.py`; (c) settle id 1 in §3 and build nothing, since the rule
  already answers `read_design_conf`. (c) leaves the set unnamed while 98 and 99 at order 50 each read
  it, so each would hold a copy. Recommendation: (b), S1 and S2.
  RESOLVED (agent, 2026-11-17, delegated): (b). widens: none · relaxes: none
- **F3 — Which names does the tuple hold?** (a) the three callee names the built rule answers,
  `read_design_conf`, `read_driver_conf` and `parse_conf`; (b) the loop kit's own reader,
  `read_driver_conf`, alone, the memory-tree kit's two kept literal in the rule; (c) rev-1's
  `read_driver_conf` and `read_tree_conf`. (c) names a function that does not exist, and (b) gives the
  rule two sources and 98's row no `read_design_conf` call. Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-12 spec audit's id 1 (HIGH, item H1, shared
  with ids 11 and 19).
- rev-2 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 S2 S3 AC1 AC2 AC3 AC4 AC5 · re-grounded on the
  code at `branch/unattended-declared-loop-d56bf0` by 2026-11-17-prompt-TOOL-dDeclaredLoop-97-2-spec-writer:
  no `read_tree_conf` at HEAD under 95 rev-3, so S1's tuple holds the three names the built rule
  answers; S2 moves the rule's literal into it and names it in the docstring and README row; S3 and AC4
  settled in §3, 76 and 82 being CLOSED; AC1 to AC3 re-probed on the tip, AC4 and AC5 new; the H1
  states the tuple's members; the five Edges bullets kept with their payloads re-worded; §5's sweep
  added; F1 and F2 re-marked and F3 added.

## 10. Reuse audit

The seam is 76's `derive_conf_reads` in `tools/loop/loop_lib.py`, as 82 S10 extends it: its
`reader call` kind is extended in place to read a declared tuple. The tuple follows
`TREE_LIB_SYMBOLS`, the kit's existing module tuple that `load_tree_lib` and its plant rows read.
`python tools/codebase-map/reuse_lookup.py "declare once the callee names a rule grades as a conf read, so the rule and its plant rows read one tuple"`,
run on the branch tip 2026-11-17, ranked `rows`, `row`, `read_text`, `read`, `load_conf`,
`read_memory_tree`, `parse_conf` and `read_design_conf` among its seams. Each reads or parses a file;
none declares a set of callee names for a rule to read, so no existing seam fits the tuple itself, and it
sits beside the rule it serves. The memory-recall query at rev-1 returned the round-12 report's H1, 76's
spec and S2, 80's fixture boundary and 82's sketch.

Recall terms used: derive_conf_reads reader call read_driver_conf read_design_conf parse_conf no-own-conf-read plant callee set conf readers tuple TREE_LIB_SYMBOLS
