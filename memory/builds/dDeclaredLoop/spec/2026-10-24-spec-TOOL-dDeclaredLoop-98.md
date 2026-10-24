# TOOL-dDeclaredLoop-98 — the `conf-read-forms` plant proves on every run that the rule answers a call of each declared conf reader

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-98-deviation-981.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-98-deviation-981.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
confirmed finding **id 11 at HIGH**, in its item **H1**. Ids 1 and 19 share that item, and each is its
own unit: `TOOL-dDeclaredLoop-97` (id 1) and `TOOL-dDeclaredLoop-99` (id 19).

Id 11 is the blast radius of H1. 95's write set never extends `derive_conf_reads`, so a
`loop_lib.read_tree_conf(tree)` call in `budget.py` or `breakpoints.py` passes the `no-own-conf-read`
plant (76 S3). The plant then certifies "no own conf read" (72 S3) over a file that reads one. The rule's
form fixture, the `conf-read-forms` plant of `tools/loop/budget.py`, stages one reader call: an aliased
`read_driver_conf` (82 AC10). No row stages a call of any other reader, so a reader the rule misses
leaves every row green.

This unit gives `conf-read-forms` a lasting row. On every run, the row stages one call of each member of
`CONF_READERS` (97 S1) in three spellings, and fails unless the rule answers every one as a
`reader call`. A rule that misses a declared reader then reds the plant before any reader can use the
gap. It builds immediately after 95, beside 97, and repairs `TOOL-dDeclaredLoop-95`.

## 2. Scope (IN)

- **S1** — The `conf-read-forms` plant of `tools/loop/budget.py` gains the row `declared readers seen`.
  It writes one scratch module beside the plant's scratch `loop_lib.py`, in one scratch directory, the
  layout 86 S15 places. For each member `m` of `loop_lib.CONF_READERS`, the module holds three calls,
  each in its own module-level function whose name holds neither `fixture` nor `plant`:
  `loop_lib.m(tree)` after `import loop_lib`, `ll.m(tree)` after `import loop_lib as ll`, and
  `r<i>(tree)` after `from loop_lib import m as r<i>`. Observed by AC1, AC3.
- **S2** — The row runs `derive_conf_reads` on that module in-process and passes only where the hits are
  exactly the call lines it wrote, each `reader call`. On a pass it prints
  `declared readers seen: <n> calls — <the members>`. Observed by AC1.
- **S3** — The row fails, and the plant exits non-zero, where a call line answers no `reader call`,
  printing `declared reader not answered: <member> as <spelling>`. It also fails where `CONF_READERS`
  is empty, printing `CONF_READERS is empty`, so an empty tuple cannot pass as a clean rule. The row
  reads the tuple and holds no reader name of its own. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- The tuple and the rule reading it: id 1's mechanism, `TOOL-dDeclaredLoop-97`.
- Whether the tuple lists every function of `loop_lib.py` that opens a conf: id 19's mechanism,
  `TOOL-dDeclaredLoop-99`. This row proves the rule sees what the tuple names, never that the tuple is
  complete.
- A row in `breakpoints.py`. Both modules' `no-own-conf-read` plants run the same `derive_conf_reads`
  from the same `loop_lib.py`, so one row observes the rule they share. 97 AC3 stages the call in each
  module.
- 82 AC10's aliased `read_driver_conf` row. It stays as written; S1's row covers the same member among
  the rest.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-97` — `CONF_READERS` and the `reader call` kind read from it, which S1 stages for every member and S2 grades (the round-12 spec audit's ids 1, 11)
- **consumes-from** `TOOL-dDeclaredLoop-82` — the `conf-read-forms` plant of `budget.py` and AC10's reader-call row, which S1 extends to every declared reader (the round-12 spec audit's id 11)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S15's layout, a scratch module beside a scratch `loop_lib.py` in one directory, in which S1 writes (the round-12 spec audit's id 11)

## 4. Design

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 76 S3 (line 44) runs `derive_conf_reads` over each plant's own module file and names each hit as
  `<file>:<line> <kind>`.
- The `conf-read-forms` plant of `budget.py` stages the rule's forms. 82 AC1 (line 271) stages a conf
  constant, 82 AC10 (line 314) a bash string and `rdc(tree, ["MEMORY_ROOT"])` after
  `from loop_lib import read_driver_conf as rdc`, 86 AC13 (line 324) three more constant forms, and 87 S3
  five binding rows. No row stages a call of a reader other than `read_driver_conf`.
- 86 S15 (line 119) places each `conf-read-forms` scratch module beside a scratch `loop_lib.py` in one
  scratch directory, because 86 S13 (line 109) has `derive_conf_reads` read the conf constants from the
  `loop_lib.py` beside the scanned module and refuse where it is missing.
- 80 S1 (line 32) passes over a function whose name, split on `_`, holds `fixture` or `plant`. The row's
  staged functions are named so they stay in the population.
- 97 S2 has the rule read its own module's `CONF_READERS`. The plant runs the real `loop_lib`
  in-process, so the scratch `loop_lib.py` needs no reader functions.
- `tools/loop/` is absent at base, so every function this unit touches is sibling-minted.

### The row, after this unit

```
conf-read-forms, row "declared readers seen":
    members = loop_lib.CONF_READERS ; empty -> fail "CONF_READERS is empty"
    write <scratch>/reader_calls.py beside <scratch>/loop_lib.py:            # 86 S15's layout
        import loop_lib ; import loop_lib as ll
        for i, m in enumerate(members):
            from loop_lib import m as r<i>
            def call_<i>_a(tree): return loop_lib.m(tree)
            def call_<i>_b(tree): return ll.m(tree)
            def call_<i>_c(tree): return r<i>(tree)
    hits = derive_conf_reads(<scratch>/reader_calls.py)                      # in-process, the real rule
    for each written call line without a (line, "reader call") hit:
        fail "declared reader not answered: <m> as <spelling>"
    print "declared readers seen: <3 * len(members)> calls — <members>"
```

### Write set

This pass writes `tools/loop/budget.py` (S1 to S3). It mints no public module-level `def`, so
`memory/map/generated/symbols.json` does not move. The build README's regions are the generator's
render.

### Files touched (estimate)

- `tools/loop/budget.py`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **A staged-break criterion alone (the report's fix as written).** It is observed once, at the close,
  and the next change to the rule is not re-observed. A row runs on every plant run, so the property
  stays checked.
- **A row with a typed list of reader names.** That is a second list beside `CONF_READERS`, and it would
  pass a rule that misses a member the list forgot. The row reads the tuple.
- **One spelling per member.** Alias resolution (82 S10) and attribute callees are separate branches of
  the rule, and a regression in either would pass a one-spelling row.
- **A row inside the `no-own-conf-read` plant's version-skew copy (92 S7).** That plant grades the
  plant's own module, and its copy exists to stage a `tree_lib` skew. `conf-read-forms` is the rule's
  form fixture and already owns the scratch layout this row needs.

## 5. Production-readiness checklist

- security — the plant fails where the rule misses a declared reader, so the no-own-conf-read
  certificate (72 S3) cannot pass over a reader call it does not see.
- perf / scale — one small file and one `ast.parse` per plant run, in the scratch directory the plant
  already uses.
- error / empty / loading states — an empty tuple fails by name. The row adds no case to 86 S13's and 88
  S33's refusals.
- observability — the pass line names the count and the members, and a failure names the member and its
  spelling.
- risks — the row proves what the tuple names and nothing more. A reader left out of the tuple is
  `TOOL-dDeclaredLoop-99`'s to catch.
- testing — AC1 to AC3 as plant runs, staged breaks and a probe of `budget.py`.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none: no adopter-facing command or flag moves.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs in `tools/loop/`, it exits 0,
  and its output holds `declared readers seen: 6 calls` naming `read_driver_conf` and `read_tree_conf`.
  Red when: the row is absent, or passes on a population that matched nothing.
  figure: 6 is DERIVED as three spellings times `len(loop_lib.CONF_READERS)` at observation time.
- **AC2** — Take a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, in which `derive_conf_reads` matches the literal pair `parse_conf` and
  `read_driver_conf` in place of `CONF_READERS`. Then `python budget.py --fixture --plant conf-read-forms`
  in the copy's `loop/` exits non-zero printing `declared reader not answered: read_tree_conf`. In a
  second copy whose `CONF_READERS` is `()`, it exits non-zero printing `CONF_READERS is empty`.
  Red when: the plant stays green on a rule that misses a declared reader, the report's consequence for
  id 11.
  fixture: both copies are made at observation time.
- **AC3** — When a `python -c` probe parses `budget.py` in `tools/loop/`, the function holding the row
  reads `CONF_READERS` and holds no str constant `read_tree_conf` or `read_driver_conf`.
  Red when: the row types its own list of reader names.

## 7. Gates

`recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop leg this pass keeps green, outside the base manifest, declared by the unit that
mints it: `loop budget fixtures`, not a leg at HEAD.

New arm: tools/loop/budget.py · covers AC1 AC2 · the declared readers seen row of the conf-read-forms plant, staged with the rule's callee set restored to the literal pair and with an empty CONF_READERS · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Observe the rule's reader set by a one-time staged break or by a lasting row (id 11)?** (a) the
  report's criterion, a scratch `budget.py` gaining a `read_tree_conf` call, observed once; (b) a plant
  row that stages a call of every declared reader on every run. (a) is 97 AC3 and is observed at the
  close only. (b) satisfies (a)'s observation and keeps it on every later run, with no new leg.
  RESOLVED (agent, 2026-10-24, delegated): (b), S1 to S3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-12 spec audit's id 11 (HIGH, item H1,
  shared with ids 1 and 19).

## 10. Reuse audit

The seam is the `conf-read-forms` plant of `tools/loop/budget.py` (82 AC1 and AC10, 86 S15), extended
by one row in its own scratch layout. The rule it grades is 76's `derive_conf_reads` as 97 leaves it,
called in-process, never re-implemented.
`python tools/codebase-map/reuse_lookup.py "check that every function which opens a conf file is listed in a declared tuple"`
ranked `check`, `load_conf`, `parse_conf`, `opened`, `read_conf` and `read_conf_key`. None of these
stages calls for a syntax rule to grade, so no existing seam fits the row beyond the plant it joins. The
memory-recall query returned the round-12 report's H1, 76's spec, 80's fixture boundary and 82's
sketch.

Recall terms used: derive_conf_reads reader call read_driver_conf read_tree_conf parse_conf no-own-conf-read plant callee set conf readers tuple
