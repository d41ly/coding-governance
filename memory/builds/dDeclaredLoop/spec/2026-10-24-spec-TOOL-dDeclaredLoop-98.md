# TOOL-dDeclaredLoop-98 — the `conf-read-forms` plant proves on every run that the rule answers a call of each declared conf reader

**Status:** CLOSED · rev-2 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-98-deviation-981.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-98-deviation-981.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-98-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-98-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-98-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-98-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-98-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-98-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-98-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-98-reground-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
confirmed finding **id 11 at HIGH**, in its item **H1**. Ids 1 and 19 share that item, and each is its
own unit: `TOOL-dDeclaredLoop-97` (id 1) and `TOOL-dDeclaredLoop-99` (id 19).

Id 11 is the blast radius of H1: the `no-own-conf-read` plant (76 S3) certifies "no own conf read"
(72 S3) only as far as `derive_conf_reads` answers a call of each reader. When rev-1 was written the
instance was a `read_tree_conf` call; 95 rev-3 builds no `read_tree_conf`, so that instance has no
trigger at HEAD (§3). The class stays. The rule's form fixture, the `conf-read-forms` plant of
`tools/loop/budget.py`, stages a call of one reader, an aliased `read_driver_conf` (82 AC10), and no row
stages `read_design_conf` or `parse_conf`. A regression in the rule's reader branch that spares
`read_driver_conf` leaves every row green.

This unit gives `conf-read-forms` a lasting row, `declared readers seen`. On every plant run the row
stages a call of each member of `CONF_READERS` (97 S1) in three spellings and fails unless the rule
answers each as a `reader call`. It builds at order 50 after `TOOL-dDeclaredLoop-97`, which mints the
tuple, and repairs `TOOL-dDeclaredLoop-95`.

## 2. Scope (IN)

- **S1** — The `conf-read-forms` branch of `tools/loop/budget.py#run_budget_plant` gains the row
  `declared readers seen`, set at the end of the branch, after 94 S21's `tree_lib` rows. It reads
  `loop_lib.CONF_READERS` through the branch's own `import loop_lib`, which binds `loop_lib` as a local
  of `run_budget_plant`, so the row sits below that statement. It writes `reader_calls.py` into the
  branch's `with-lib` scratch folder, beside the scratch `loop_lib.py` 82's rows already write there, the
  layout 86 S15 places. The module opens with `import loop_lib` and `import loop_lib as ll`; for the
  member `m` at index `i` it then holds `from loop_lib import m as r<i>` and three one-line functions,
  `call_<i>_a`, `call_<i>_b` and `call_<i>_c`, returning `loop_lib.m(tree)`, `ll.m(tree)` and
  `r<i>(tree)`. No staged function name holds `fixture` or `plant`. The `conf-read-forms` entry of
  `PLANTS` gains the closing words ", then a module calling each conf reader the loop_lib declares, in
  three spellings", naming no conf by its file name. Observed by AC1, AC3.
- **S2** — The row calls `derive_conf_reads` on that module in-process and owes `(line, "reader call")`
  on each call line it wrote. It prints
  `loop: fixture · conf-read-forms · declared readers seen · <k>/<n> calls answered · <members>`, `<n>`
  the lines written, `<k>` those answered, `<members>` the tuple joined by `, ` in its order. Observed by
  AC1.
- **S3** — Each call line with no `reader call` hit is a miss, through the plant's `check`, named
  `declared reader not answered: <member> as <callee>`, `<callee>` being `loop_lib.<member>`,
  `ll.<member>` or `r<i>`. An empty `CONF_READERS` is the miss `CONF_READERS is empty`, so a vacuous
  row cannot hold. A miss makes the plant print its `MISSED` line and exit 1. The row reads the tuple and
  holds no reader name of its own. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- **Rev-1 items settled at HEAD.** Each was read on the branch tip §4 Evidence names.

| Item | Rev-1 ordered | Settled because |
|---|---|---|
| §1's instance | a `loop_lib.read_tree_conf(tree)` call passing the plant | no `read_tree_conf` exists at HEAD and 95 rev-3 builds none (97 rev-2 §3); §1 keeps the class, a declared reader the rule misses |
| AC1's figure | `6 calls`, naming `read_driver_conf` and `read_tree_conf` | 97 rev-2 S1's tuple holds three members, so the row writes nine calls, naming `read_design_conf`, `read_driver_conf` and `parse_conf` |
| AC2's staged pair | the rule matching `parse_conf` and `read_driver_conf`, the miss printed for `read_tree_conf` | the same pair is the built set less `read_design_conf`, so the staged miss names `read_design_conf` |
| AC3's constants | no str constant `read_tree_conf` or `read_driver_conf` | AC3 reads every member of `CONF_READERS` |
| S2's exact hit list | the hits exactly the written call lines | §8 F3: S2 owes a hit on each written line, and over-reporting stays with the exact owed lists of 82's, 86's and 87's rows |
| S2's pass line | `declared readers seen: <n> calls — <members>` | every row of the plant prints `loop: fixture · conf-read-forms · <row> · <result>`, so S2 prints in that shape |
| the sibling-minted loop leg | `loop budget fixtures`, "not a leg at HEAD" | on the branch it is a leg of `tools/gate-legs.json`, absent from main's (§7) |

- The tuple and the rule reading it: id 1's mechanism, `TOOL-dDeclaredLoop-97`.
- Whether the tuple lists every function of `loop_lib.py` that opens a conf: id 19's mechanism,
  `TOOL-dDeclaredLoop-99`. This row proves the rule sees what the tuple names, never that the tuple is
  complete; two members are defined outside `loop_lib.py` (97 S1), and the row parses its module without
  running it, so where a member is defined does not reach it.
- A row in `breakpoints.py`. Both modules' `no-own-conf-read` plants run the same `derive_conf_reads`
  from the same `loop_lib.py`, so one row observes the rule they share. 97 AC3 stages the call in each
  module.
- 82 AC10's `aliased-reader` row. It stays as written; S1's row covers its member among the rest.
- Over-reporting on the row's module, a hit on a line it did not write: §8 F3.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-97` — `CONF_READERS` and the `reader call` kind read from it, which S1 stages for every member and S2 grades (the round-12 spec audit's ids 1, 11)
- **consumes-from** `TOOL-dDeclaredLoop-82` — the `conf-read-forms` plant of `budget.py` and AC10's reader-call row, which S1 extends to every declared reader (the round-12 spec audit's id 11)
- **consumes-from** `TOOL-dDeclaredLoop-86` — S15's layout, a scratch module beside a scratch `loop_lib.py` in one directory, in which S1 writes (the round-12 spec audit's id 11)

## 4. Design

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every read is of
`branch/unattended-declared-loop-d56bf0` at `1bb9bbd62`, its `tools/`, `memory/`, `help/` and three
confs written by `git archive` into the run's scratch directory, since this worktree is cut from main,
which lacks the loop kit. 97 rev-2 was read from the branch tip. The prototype and each staged break ran
in a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` carrying 97 S1 and S2 as 97
rev-2's sketch "The rule, after this unit" writes them.

- `tools/loop/budget.py#run_budget_plant`'s `conf-read-forms` branch writes `with-lib/loop_lib.py`
  binding one conf constant, then 82's five rows into that folder, 86's three, 87's, 89's and 90's
  bindings and 91's module-scope group each in its own folder, the no-`loop_lib` refusal, and 88 S33's and
  94 S21's five `tree_lib` rows. Each row prints `loop: fixture · conf-read-forms · <row> · <hits>` and
  answers through the nested `check`, which appends a miss; the plant prints `held` or `MISSED` and its
  exit is 0 or 1.
- Only the `aliased-reader` row stages a reader call:
  `from loop_lib import read_driver_conf as rdc` and `rdc(tree, ['MEMORY_ROOT'])`, owed
  `[(2, "reader call")]`. No row stages `read_design_conf` or `parse_conf`.
- The branch's one `import loop_lib` statement sits in the 88 S33 rows, so `loop_lib` is a local of
  `run_budget_plant`, unbound above it. DERIVED by `grep -cE "^ +import loop_lib$" tools/loop/budget.py`,
  which prints 1.
- `tools/loop/loop_lib.py#derive_conf_reads` answers `reader call` for a callee, an attribute by its name
  and a name by the last segment `derive_import_aliases` binds, in a literal of `read_design_conf`,
  `read_driver_conf` and `parse_conf`; 97 S2 swaps that literal for `CONF_READERS`. An import of the tip's
  `loop_lib` has no `CONF_READERS`.
- `tools/loop/loop_lib.py#derive_fixture_boundary` passes over a definition whose name, split on `_`,
  holds `fixture` or `plant`. `run_budget_plant` holds `plant`, so the `no-own-conf-read` plant's grading
  of `budget.py` passes over every row, this one included. `call_<i>_a` holds neither.
- `tools/loop/budget.py#PLANTS` is module-level, printed at the start of the plant, and lists each
  `conf-read-forms` row in words. `tools/govkit/usage.toml`'s row `script:{prefix}/loop/budget.py`
  holds the flags alone, so `help/loop.md`'s anchor for it does not read a description.
  `grep -rn conf-read-forms help/ tools/loop/README.md` prints nothing.
- The tip's plant: `python budget.py --fixture --plant conf-read-forms` exits 0 printing `held`, with no
  `declared readers seen` line, in 0.8 s PINNED wall time.
- The prototype, S1 to S3 over 97's tuple: the plant printed
  `declared readers seen · 9/9 calls answered · read_design_conf, read_driver_conf, parse_conf` and
  `held`, exit 0, in 1.2 s PINNED wall time. With the rule's set staged as `("parse_conf",
  "read_driver_conf")` it printed `6/9 calls answered` and exited 1, its `MISSED` line naming
  `read_design_conf as loop_lib.read_design_conf`, `as ll.read_design_conf` and `as r0`. With
  `CONF_READERS = ()` it printed `0/0 calls answered` and exited 1, its `MISSED` line naming
  `CONF_READERS is empty` beside the `aliased-reader` row's miss. Both `no-own-conf-read` plants, of
  `budget.py` and `breakpoints.py`, printed `held`.
- AC3's probe printed `False []` at the tip, `True []` over the prototype, and `False` with the three
  names where the row typed its own tuple.

### The row, after this unit

```
conf-read-forms, at the branch's end (after 94 S21's tree_lib rows and the branch's import loop_lib):
    members = loop_lib.CONF_READERS ; empty -> miss "CONF_READERS is empty"
    lines = ["import loop_lib", "import loop_lib as ll"] ; owed = {}
    for i, m in enumerate(members):
        lines += "from loop_lib import <m> as r<i>"
        for tag, callee in (a, loop_lib.<m>), (b, ll.<m>), (c, r<i>):
            lines += "def call_<i>_<tag>(tree): return <callee>(tree)" ; owed[len(lines)] = (m, callee)
    write_fixture_files(with-lib, {"reader_calls.py": lines})          # 86 S15's layout
    got = derive_conf_reads(with-lib/reader_calls.py)                    # in-process, the real rule
    each owed line without (line, "reader call") in got -> miss "declared reader not answered: <m> as <callee>"
    print "loop: fixture · conf-read-forms · declared readers seen · <k>/<n> calls answered · <members>"
```

### Write set

This pass writes `tools/loop/budget.py` alone: the row in `run_budget_plant` (S1 to S3) and the
`conf-read-forms` entry of `PLANTS` (S1). It adds no `def` and no module-level name, so
`memory/map/generated/symbols.json` does not move. The build README's regions are the generator's
render.

### Files touched (estimate)

- `tools/loop/budget.py`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **A staged-break criterion alone (the report's fix as written).** It is observed once, at the close,
  and the next change to the rule is not re-observed. A row runs on every plant run.
- **A row with a typed list of reader names.** A second list beside `CONF_READERS`, which would pass a
  rule that misses a member the list forgot. The row reads the tuple.
- **One spelling per member.** Alias resolution (82 S10) and attribute callees are separate branches of
  the rule, and a regression in either would pass a one-spelling row.
- **A row inside the `no-own-conf-read` plant's version-skew copy.** That plant grades the plant's own
  module, and its copy stages a `tree_lib` skew. `conf-read-forms` is the rule's form fixture and already
  owns the scratch layout this row needs.
- **The row at the head of the branch, with an `import loop_lib` of its own.** A second import
  statement of the same local; the end of the branch reads the one the 88 S33 rows hold.

## 5. Production-readiness checklist

- security — the plant fails where the rule misses a declared reader, so the no-own-conf-read
  certificate (72 S3) cannot pass over a declared reader's call it does not see.
- perf / scale — one module of `2 + 4 * len(CONF_READERS)` lines and one parse per plant run, in the
  folder the branch already writes; the plant ran in 0.8 s at the tip and 1.2 s in the prototype, PINNED 2026-11-17, against
  the `loop budget fixtures` leg's ceiling of 300 s PINNED in the branch's `tools/gate-legs.json`.
- error / empty / loading states — an empty tuple is a named miss. The row adds no case to 86 S13's or
  88 S33's refusals, and runs after 94 S21's `tree_lib` rows have restored `loop_lib.read_memory_tree`.
- observability — the row's line names `<k>/<n>` and the members, and a miss names the member and its
  callee.
- risks — the row proves what the tuple names and nothing more: a reader left out of the tuple is
  `TOOL-dDeclaredLoop-99`'s to catch, and a hit on an unwritten line is §8 F3's gap.
- testing — AC1 to AC3 as plant runs, staged breaks in scratch copies and a probe of `budget.py`.
- migration — none: no stored data moves.
- user docs — none: no verb, flag, plant name or usage row moves, and `help/loop.md` names no
  `conf-read-forms` row.

### The sweep

Each count is DERIVED by the command beside it, run in the branch tip's archive.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| `run_budget_plant`'s `conf-read-forms` branch | `run_selftest`, which owes `held` from every plant; the `loop budget fixtures` leg, whose argv runs `budget.py --selftest` | the row holds over 97's tuple; the prototype printed `held` |
| the `no-own-conf-read` plants | `budget.py` and `breakpoints.py`, each grading its own module, `grep -rn "derive_conf_reads(" tools/ --include=*.py` printing eight sites in `budget.py` and one in `breakpoints.py` | the row sits inside `run_budget_plant`, which `derive_fixture_boundary` passes over, and the `PLANTS` words name no conf file; the prototype printed `held` for both |
| the `conf-read-forms` description | `PLANTS`, printed at the plant's start; `tools/govkit/usage.toml`'s `script:{prefix}/loop/budget.py` row, flags alone | the plant names in `PLANTS` do not move, so the usage text and the `help/loop.md` anchor do not move |
| a function name | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at the tip; `grep -cE "^ *(async )?def " tools/loop/budget.py` printing 29 before and after in the prototype | no `def` is added; the staged `call_<i>_<tag>` names are text the row writes, so no `--suggest` run is owed |
| the symbol tier | `memory/map/generated/symbols.json` | no `def`, class, `__all__` or module-level name is added |
| this spec's item and criterion ids | 97 rev-2 §4 cites "98 rev-1 S1 to S3"; 100 cites the `declared readers seen` row, `grep -n "98 S[0-9]\|98 AC[0-9]\|declared readers seen" memory/builds/dDeclaredLoop/spec/*.md` | S1 to S3 keep their meaning and the row keeps its name |
| the edges naming this unit | three hands-off bullets, from 82, 86 and 97, `grep -n "^- \*\*hands-off\*\* .TOOL-dDeclaredLoop-98. " memory/builds/dDeclaredLoop/spec/*.md` | rev-2 keeps its three consumes-from bullets, verbs and targets unchanged; 82 and 86 are CLOSED |
| the H1 title | the units row of `memory/builds/dDeclaredLoop/README.md`, a generated region; the `After:` line of `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-98-deviation-981.md` | the title is unchanged |
| positional rows | `memory/project/positional-refs.txt`, `grep -c "spec-TOOL-dDeclaredLoop-98.md" memory/project/positional-refs.txt` printing 0 | rev-2 cites code by symbol and specs by item id, so no row is owed |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` reads tracked `*.sh` files; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts | the pass writes no shell script, and `tools/loop/` holds no `.families.txt` |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md`, `grep "^watch:" memory/guides/SESSION-KICKOFF.md \| grep -c "tools/loop"` printing 0 | `budget.py` is not watched |
| the install-prefix ban, the verdict-epoch delegates, subject pins, upgrade steps, help anchors and usage rows | `tools/check-install-prefix.sh`, `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py`, `help/` | the pass writes no shipped install line, leg, step, verb or flag |

Order: this unit reads `CONF_READERS` and the rule reading it as 97 rev-2 S1 and S2 build them, at
order 50 before this unit; over the tip, without them, the row's `loop_lib.CONF_READERS` raises. It
reads the code units 82, 86, 87, 88, 89, 90, 91 and 94 built, each CLOSED at the tip. 95 rev-3 at order
49 and 96 rev-3 at order 50 write no file. 99 at order 50 writes `tools/loop/loop_lib.py`, no line of
`budget.py`. 100 at order 51 writes `budget.py`'s skew row of the `no-own-conf-read` plant, not this
branch.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant conf-read-forms` runs in `tools/loop/`, it exits 0
  printing `held`, and its output holds
  `declared readers seen · 9/9 calls answered · read_design_conf, read_driver_conf, parse_conf`.
  Red when: the row is absent, as at the tip, where no `declared readers seen` line prints, or it holds
  on a population that matched nothing.
  figure: 9 is DERIVED as three spellings times `len(loop_lib.CONF_READERS)` at observation time.
- **AC2** — Take a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, in which `derive_conf_reads` matches the literal pair `("parse_conf",
  "read_driver_conf")` in place of `CONF_READERS`. Then `python budget.py --fixture --plant
  conf-read-forms` in the copy's `loop/` exits 1, its `MISSED` line holding
  `declared reader not answered: read_design_conf as loop_lib.read_design_conf`. In a second copy whose
  `CONF_READERS` is `()`, it exits 1, its `MISSED` line holding `CONF_READERS is empty`.
  Red when: the plant stays green on a rule that misses a declared reader, the report's consequence for
  id 11.
  fixture: both copies are made at observation time.
- **AC3** — When
  `python -I -c "import ast, sys; sys.path.insert(0, '.'); import loop_lib; f = next(n for n in ast.walk(ast.parse(open('budget.py', encoding='utf-8').read())) if isinstance(n, ast.FunctionDef) and n.name == 'run_budget_plant'); print(any(isinstance(n, ast.Attribute) and n.attr == 'CONF_READERS' for n in ast.walk(f)), sorted({n.value for n in ast.walk(f) if isinstance(n, ast.Constant) and n.value in loop_lib.CONF_READERS}))"`
  runs in `tools/loop/`, it prints `True []`.
  Red when: the row types its own list of reader names, staged in a scratch copy by
  `members = ("read_design_conf", "read_driver_conf", "parse_conf")`, where it prints `False` and the
  three names. At the tip, before 97, the probe ends in an `AttributeError` naming `CONF_READERS`.

## 7. Gates

`recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's leg this pass keeps green, a leg in `tools/gate-legs.json` on the branch and absent from
main's: `loop budget fixtures`, whose `--selftest` runs the `conf-read-forms` and `no-own-conf-read`
plants. `loop breakpoint fixtures` runs the second plant over `breakpoints.py`, which this pass does not
write.

New arm: tools/loop/budget.py · covers AC1 AC2 · the declared readers seen row of the conf-read-forms plant, staged with the rule's callee set restored to the literal pair and with an empty CONF_READERS · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — Observe the rule's reader set by a one-time staged break or by a lasting row (id 11)?** (a) the
  report's criterion, a scratch `budget.py` gaining a reader call, observed once; (b) a plant row that
  stages a call of every declared reader on every run. (a) is 97 AC3 and is observed at the close only.
  (b) satisfies (a)'s observation and keeps it on every later run, with no new leg.
  Recommendation: (b), S1 to S3.
  RESOLVED (agent, 2026-11-17, delegated): (b). widens: none · relaxes: none
- **F3 — Does the row owe the exact hit list, or a hit on each written call line?** (a) a hit on each
  written line, plus the empty-tuple miss; (b) rev-1's exact list, which adds the case of a hit on a line
  the row did not write. (b)'s added case has no staged break this unit can make short of editing the
  rule's other kinds, so it would land never seen red; the exact owed lists of 82's, 86's and 87's rows
  already red an over-report on their forms, the `aliased-reader` row's import line among them.
  Recommendation: (a), S2 and S3.
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: rev-1 S2's exact list, §3

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-12 spec audit's id 11 (HIGH, item H1,
  shared with ids 1 and 19).
- rev-2 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §9 §10 · S1 S2 S3 AC1 AC2 AC3 · re-grounded on the code
  at `branch/unattended-declared-loop-d56bf0` by 2026-11-17-prompt-TOOL-dDeclaredLoop-98-1-spec-writer:
  no `read_tree_conf` at HEAD under 95 rev-3, so AC1 to AC3 read 97 rev-2's three members; S1 places the
  row at the branch's end, below its `import loop_lib`, and extends the `PLANTS` words; S2 prints in the
  plant's row shape and owes a hit per written line (F3); §3's table settles rev-1's moved items; §4
  re-probed on the tip with a prototype and three staged breaks; §5's sweep added; §7 names the branch's
  leg; F1 and F2 re-marked and F3 added.

## 10. Reuse audit

The seam is the `conf-read-forms` branch of `tools/loop/budget.py#run_budget_plant` (82 AC1 and AC10,
86 S15), extended by one row in its own `with-lib` folder, written through
`tools/loop/loop_witness.py#write_fixture_files` and answered through the branch's `check`. The rule it
grades is `tools/loop/loop_lib.py#derive_conf_reads` as 97 leaves it, called in-process, never
re-implemented.
`python tools/codebase-map/reuse_lookup.py "stage a call of each declared conf reader so a plant row proves the rule answers every member"`,
run in the branch tip's archive 2026-11-17, ranked `rows`, `row`, `read_text`, `read`, `read_bytes`,
`load_conf`, `read_git`, `parse_conf`, `read_memory_tree` and `read_design_conf` among its seams. Each
reads or parses a file; none stages calls for a syntax rule to grade, so no existing seam fits the row
beyond the plant it joins. The memory-recall query at rev-1 returned the round-12 report's H1, 76's
spec, 80's fixture boundary and 82's sketch.

Recall terms used: derive_conf_reads reader call read_driver_conf read_design_conf parse_conf CONF_READERS no-own-conf-read conf-read-forms plant callee set write_fixture_files
