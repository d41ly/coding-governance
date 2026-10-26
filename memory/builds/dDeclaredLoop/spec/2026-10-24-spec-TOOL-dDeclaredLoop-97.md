# TOOL-dDeclaredLoop-97 — the no-own-conf-read rule reads its reader calls from one declared tuple, `CONF_READERS`, which holds `read_tree_conf`

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-97-deviation-971.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-97-deviation-971.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
confirmed finding **id 1 at HIGH**, in its item **H1**. Ids 11 and 19 share that item, and each is its
own unit: `TOOL-dDeclaredLoop-98` (id 11) and `TOOL-dDeclaredLoop-99` (id 19).

`TOOL-dDeclaredLoop-95` S2 makes `read_tree_conf(tree)` the loop kit's one reader of
`.memory-tree.conf`. The `no-own-conf-read` rule, `derive_conf_reads`, counts a call as a conf read
only where its callee resolves to `parse_conf` or `read_driver_conf` (76 S2, 82 S10). After 95,
`ll.read_tree_conf(tree)` in `budget.py` or `breakpoints.py` reads the conf around
`resolve_memory_root` and its `confs-disagree` refusal (72 AC3), and the plant (76 S3) stays green.

This unit names the loop kit's conf readers once, in the tuple `CONF_READERS` in
`tools/loop/loop_lib.py`, and makes the rule's `reader call` kind read that tuple. The rule then sees a
call of `read_tree_conf` and of every reader added to the tuple later. It builds immediately after 95
and repairs `TOOL-dDeclaredLoop-95`.

## 2. Scope (IN)

- **S1** — `CONF_READERS = ("read_driver_conf", "read_tree_conf")` is a module-level tuple in
  `tools/loop/loop_lib.py`. It lists the loop kit's own functions that open a conf and return its
  values, and each member is a module-level `def` of that file. Observed by AC1.
- **S2** — `derive_conf_reads` answers `(line, "reader call")` for a call whose callee, resolved through
  `derive_import_aliases` (82 S10), is `parse_conf` or a member of its own module's `CONF_READERS`. The
  rule holds no second literal list of reader names. A Name and an Attribute callee both count, as 76 S2
  states. Observed by AC2, AC3.
- **S3** — 76 S2 and its §4 sketch "The rule", and 82 S10 and its §4 sketch "The conf-read rule, after
  this unit", read "`parse_conf` or a member of `CONF_READERS`" in place of "`parse_conf` or
  `read_driver_conf`". These land in this unit's rev bumps of 76 and 82, each with its §9 line.
  Observed by AC4.

## 3. Non-goals (OUT)

- The plant row that observes the rule answering each member of the tuple on every run: id 11's
  mechanism, `TOOL-dDeclaredLoop-98`.
- The check that keeps the tuple complete as `loop_lib.py` grows: id 19's mechanism,
  `TOOL-dDeclaredLoop-99`.
- `read_tree_conf`'s body, its decode and its unreadable-conf refusal: 95 S2, and the round-12 minors
  batch `TOOL-dDeclaredLoop-100`.
- `resolve_memory_root` and `resolve_memory_root_source`. They return a resolved root, not a conf's
  values, so they are the sanctioned route and stay out of the tuple.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-95` — `read_tree_conf` in `tools/loop/loop_lib.py`, which S1 declares as a conf reader (the round-12 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-76` — S2's `derive_conf_reads` and its §4 sketch "The rule", whose reader-call callee set S2 reads from `CONF_READERS` and S3 restates (the round-12 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-82` — S10's alias resolution and its §4 sketch "The conf-read rule, after this unit", which S2 keeps and S3 restates (the round-12 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-98` — `CONF_READERS` and the `reader call` kind read from it, which that unit's plant row observes for every member (the round-12 spec audit's ids 1, 11)
- **hands-off** `TOOL-dDeclaredLoop-99` — `CONF_READERS`, which that unit's check compares both ways with the functions of `loop_lib.py` that open a conf (the round-12 spec audit's ids 1, 19)

## 4. Design

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 76 S2 (line 41) and its sketch (line 95) match a `reader call` only where the callee is named
  `parse_conf` or `read_driver_conf`. 82 S10 (line 102) and its sketch (line 200) resolve aliases into
  the same two names.
- 95 S2 (line 37) mints `read_tree_conf` as the kit's one `.memory-tree.conf` reader. Its sketch builds
  the path inline (line 119), so 82's `conf constant` kind, which reads module-level bindings, does not
  see it. The call carries no conf-name string, so the `conf name` kind does not see it either.
- 87 §3 (line 70) and 89 S5 (line 80) send a function-returned conf read to 82's `reader call` kind.
- `read_driver_conf` is 70 S1's reader of `.unattended.conf` (`TOOL-dDeclaredLoop-70` line 34).
- `CONF_READERS` occurs in no spec of this build. Over 76's S2 range and its "The rule" range, and
  over 82's S10 range and its "The conf-read rule, after" range, `grep -c CONF_READERS` prints 0.
- `tools/loop/` is absent at base, so every function this unit touches is sibling-minted.

### The rule, after this unit

```
CONF_READERS = ("read_driver_conf", "read_tree_conf")     # the loop kit's own conf readers

derive_conf_reads(path):
    ... 82 S10's walk, 86's and 87's kinds, 80 S1's boundary, unchanged
    Call whose callee, resolved by derive_import_aliases, is "parse_conf" or in CONF_READERS
                                                                    -> (line, "reader call")
```

`TREE_LIB_SYMBOLS` (92 S8, 95 S1) is the precedent: one tuple that the loader and its probe both read.

### Write set

This pass writes `tools/loop/loop_lib.py` (S1, S2). Inside this build's folder it amends the specs of
76 and 82 as rev bumps, one per spec, each with its §9 line (S3). `CONF_READERS` is a module-level
tuple, not a `def` or a class, and no spec of this build gives `loop_lib.py` an `__all__`, so
`memory/map/generated/symbols.json` does not move. The build README's regions are the generator's
render.

### Inventory

- `CONF_READERS` — a module-level tuple in `tools/loop/loop_lib.py`. It is not a symbol row:
  `tools/codebase-map/map_lib.py:313` declares the kinds a row may carry, and a Python constant is a
  row only as an `__all__` export (`map_lib.py:327`).

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **Add `read_tree_conf` to the rule's literal pair (the report's first fix).** It closes this
  instance and leaves the next reader out the same way. The report itself prefers the class, one tuple
  that the rule and the readers share.
- **Count any call of a `loop_lib` function whose body names a conf.** `resolve_memory_root_source`
  names both confs for its existence tests (82 S15), so the readers' sanctioned route would be a hit.
- **Read the tuple by parsing the sibling `loop_lib.py`, as 86 S13 reads the conf constants.** The rule
  runs inside `loop_lib.py`, so its own module global is that tuple. In a scratch copy, the copy's
  `loop_lib.py` is the module that runs.

## 5. Production-readiness checklist

- security — the readers' no-own-conf-read rule sees every declared reader, so `confs-disagree` (72
  AC3) cannot be bypassed through `read_tree_conf`.
- perf / scale — one tuple membership test per call node, no new parse.
- error / empty / loading states — unchanged: 86 S13's and 88 S33's refusals stand.
- observability — a hit names `<file>:<line> reader call`, as 76 S3 prints it.
- risks — a reader missing from the tuple is invisible to the rule. `TOOL-dDeclaredLoop-99` checks the
  tuple against the file both ways.
- testing — AC1 to AC4 as probes, a staged break in a scratch copy and greps.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none: no adopter-facing command or flag moves.

## 6. Acceptance criteria

- **AC1** — When `python -c "import inspect, loop_lib as ll; print(ll.CONF_READERS, all(inspect.isfunction(getattr(ll, n, None)) for n in ll.CONF_READERS))"`
  runs in `tools/loop/`, it prints `('read_driver_conf', 'read_tree_conf') True`.
  Red when: the tuple omits `read_tree_conf`, or names a function `loop_lib.py` does not define.
- **AC2** — A `python -c` probe in `tools/loop/` calls `derive_conf_reads` on a scratch module that sits
  beside a copy of `loop_lib.py` in one scratch directory, the layout 86 S15 places. The module holds
  `loop_lib.read_tree_conf(tree)` after `import loop_lib`, `ll.read_tree_conf(tree)` after
  `import loop_lib as ll`, `rtc(tree)` after `from loop_lib import read_tree_conf as rtc`, and
  `read_driver_conf(tree, ["MEMORY_ROOT"])` after `from loop_lib import read_driver_conf`. The probe
  answers four hits, each `reader call`. On a scratch module holding only
  `loop_lib.resolve_memory_root(tree)`, it answers no hit.
  Red when: the callee set is the literal pair `parse_conf` and `read_driver_conf`, staged in a scratch
  copy, which answers one hit for the first module.
- **AC3** — Take a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, and give its `budget.py` the module-level
  `def _root_probe(tree): return loop_lib.read_tree_conf(tree)`. Then
  `python budget.py --fixture --plant no-own-conf-read` in the copy's `loop/` exits non-zero printing
  `budget.py:<line> reader call`. The same edit to the copy's `breakpoints.py` makes
  `python breakpoints.py --fixture --plant no-own-conf-read` exit non-zero printing
  `breakpoints.py:<line> reader call`. Over the unmodified `tools/loop/`, both plants exit 0.
  Red when: a reader calling `read_tree_conf` passes the plant, the report's consequence for id 1.
  fixture: the copy is made at observation time; the name `_root_probe` holds neither `fixture` nor
  `plant`, so 80 S1's boundary does not pass over it.
- **AC4** — When `awk '/^- \*\*S2\*\*/,/^- \*\*S3\*\*/'` and `awk '/^### The rule/,/^### Files touched/'`
  over the 76 spec, and `awk '/^- \*\*S10\*\*/,/^- \*\*S11\*\*/'` and
  `awk '/^### The conf-read rule, after/,/^### Evidence/'` over the 82 spec, are each piped to
  `grep -c CONF_READERS`, each prints at least 1.
  Red when: the rule's text still names the two-name callee set while the code reads the tuple.
  figure: each prints 0 at HEAD, PINNED 2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop breakpoints fixtures` and `loop definition fixtures`, none
a leg at HEAD. This pass adds and moves no arm: AC1 to AC4 are probes, a staged break and greps. The
lasting arm over this rule is `TOOL-dDeclaredLoop-98`'s.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Add one name to the rule's pair, or read the pair from a declared tuple (id 1)?** (a) the pair
  gains `read_tree_conf`; (b) the rule reads `CONF_READERS`, one tuple the readers' module declares.
  The report judged (a) sound and named (b) the better form. (b) satisfies every criterion (a) would and
  also covers the next reader, which (a) leaves to the next audit. RESOLVED (agent, 2026-10-24,
  delegated): (b), S1 and S2.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-12 spec audit's id 1 (HIGH, item H1, shared
  with ids 11 and 19).

## 10. Reuse audit

The seam is 76's `derive_conf_reads` in `tools/loop/loop_lib.py`, as 82 S10 extends it: its
`reader call` kind is extended in place to read a declared tuple. The tuple follows
`TREE_LIB_SYMBOLS` (92 S8), the kit's existing pattern of one tuple that a loader and its probe share.
`python tools/codebase-map/reuse_lookup.py "declare the set of functions that read a config file so a rule and its readers share one tuple"`
ranked `read`, `read_text`, `read_conf`, `read_conf_key`, `declares` (`tools/memory-tree/gotchas.py`)
and `read_design_conf`. None of these declares a set of reader functions for a rule to read, so no
existing seam fits the tuple itself, and it sits beside the rule it serves. The memory-recall query
returned the round-12 report's H1, 76's spec and S2, 80's fixture boundary and 82's sketch.

Recall terms used: derive_conf_reads reader call read_driver_conf read_tree_conf parse_conf no-own-conf-read plant callee set conf readers tuple
