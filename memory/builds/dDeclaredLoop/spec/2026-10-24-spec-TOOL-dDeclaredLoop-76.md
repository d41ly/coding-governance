# TOOL-dDeclaredLoop-76 — the loop readers' no-own-conf-read rule is graded on the syntax tree, and the root's source is a value

**Status:** CLOSED · rev-6 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 37 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-76-deviation-761.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-deviation-761.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-76-deviation-762.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-deviation-762.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 |
| [2026-11-17-build-TOOL-dDeclaredLoop-76-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-76-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-76-deviation-763.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-76-deviation-763.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-76-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-76-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-76-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-76-reground-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-76-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-76-build-brief.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-79 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dDeclaredLoop-72` AC4 then
counted the two conf names over `tools/loop/budget.py` and `tools/loop/breakpoints.py` and required 0,
while `TOOL-dDeclaredLoop-75`, building later, requires those names in the same two files: its S5 and S30
put `.unattended.conf` in the two module docstrings (AC5, AC30), and its S7 and S8 print the conf a root
came from (AC7, AC8). Built in order, the five criteria could not all hold.

72's rev-6 restated its AC4 to a count of the reader calls `read_design_conf`, `read_driver_conf` and
`parse_conf` in those two files, so a docstring naming a conf no longer reds it. Two halves of the finding
are still open. 75 AC8's held line ends `root from .unattended.conf` or `root from .memory-tree.conf`, and
AC7's first line names the conf: both need the root's source as a value, and 72 S1's resolver answers a
bare root. And AC4's count cannot tell a docstring or a comment naming a reader from a call of it, while
72's hands-off to this unit asks for the property graded on the syntax tree, a plant observing what AC4's
grep states, which units 80, 82, 86, 95, 97 and 99 then extend.

This unit gives both readers the root's source as a value from 72's one resolver, and grades the
no-own-conf-read property on each module's syntax tree. It builds at order 37, after 72 at order 36, and
repairs `TOOL-dDeclaredLoop-72`.

## 2. Scope (IN)

- **S1** — `resolve_memory_root_source(tree)` in `tools/loop/loop_lib.py` answers `(root, source)`, each
  of 72 S1's returns paired with the conf its branch read (§4 "The source"): `.unattended.conf` where that
  file exists, `.memory-tree.conf` where it does not and the memory-tree conf sets `MEMORY_ROOT`, and
  `default` where neither supplied the root. It holds 72 S1's body, its normalisation and its per-process
  read, and raises 72 S2's `ValueError` with its text as 72 states it. `resolve_memory_root(tree)` answers
  that pair's root, so every caller 72 §4 "The callers" names keeps its call and its answer.
  Observed by AC3.
- **S2** — `derive_conf_reads(path)` in `tools/loop/loop_lib.py` parses a module with `ast` and answers
  one `(line, kind)` per conf read, sorted by line (§4 "The rule"). Kind `reader call` is a call whose
  callee, a `Name` or an `Attribute`, is named `read_design_conf`, `read_driver_conf` or `parse_conf`, the
  three names 72 AC4 counts. Kind `conf name` is a string constant ending `.memory-tree.conf` or
  `.unattended.conf` that is not the docstring of the module, of a class or of a function, an
  `async def` included; an f-string's literal part is such a constant and counts. A module that does not
  parse raises its `SyntaxError`, never an empty list. Observed by AC2.
- **S3** — The plant `no-own-conf-read` joins `PLANTS` in `tools/loop/budget.py` and in
  `tools/loop/breakpoints.py`, a case of `run_budget_plant` and of `run_breakpoint_plant`: it runs S2 over
  the module's own file, the one its `__file__` names, prints one `<file>:<line> <kind>` line per hit, and
  is `held` where S2 answers none and `MISSED` naming the count otherwise. The plant `root-source` joins
  `PLANTS` in `tools/loop/budget.py` the same way, observing S1 (§4 "The plants"). Observed by AC1, AC3.
- **S4** — 72 AC4's reader-call half is observed on the syntax tree: at this pass S3's plant names no
  `reader call` hit in either module, and a docstring or comment naming a reader is no hit. The close
  records 72 AC4 beside this unit's AC1. Observed by AC1, AC4.
- **S5** — The carriers. The breakpoints fixture sentence of `help/loop.md`, under "Where a build stops
  for a review or for you", names `no-own-conf-read` among the module's plants, the one that reads the
  module's own file and no scratch repository. The table of `loop_lib.py` functions in
  `tools/loop/README.md` gains one row for each of S1 and S2. Observed by AC5.

## 3. Non-goals (OUT)

- What either reader prints or documents: 75 S5, S7, S8 and S30, unchanged, built over S1's source value
  and inside S2's rule, as this unit's hands-off bullet to 75 records.
- Which root wins, and when the two confs disagree: 72 S1 and S2, unchanged.
- The fixture boundary that passes over the plants writing the confs: `TOOL-dDeclaredLoop-80` S1 and S2,
  at order 38. Until it lands, S3's plant names those plants' lines (§8 F3).
- A source for each unset-key branch beyond §4 "The source", a conf name mid-string, an aliased call, a
  cross-module conf constant and the docstring set shared through the memory-tree kit's `tree_lib`:
  `TOOL-dDeclaredLoop-82` S15, S10, S1 and S8.
- The reader-call names read from one declared tuple: `TOOL-dDeclaredLoop-97`.
- A spec-set check that reds a later-ordered spec requiring a token in a file where an earlier sibling's
  criterion asserts its absence, the finding's left-shift: the class is recorded at the close; AC4 is this
  pair's observation.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root` in `tools/loop/loop_lib.py`, whose body S1 pairs with its source, its two plants per module, and rev-6 AC4's reader-call property, which this unit grades on the syntax tree
- **hands-off** `TOOL-dDeclaredLoop-75` — `resolve_memory_root_source`, from whose `source` S7's `--explain` line and S8's held line print the conf, and S2's rule, inside which S5's and S30's docstrings name it; that pass re-runs the `no-own-conf-read` plant
- **hands-off** `TOOL-dDeclaredLoop-80` — the `no-own-conf-read` plant's population, which that unit bounds at a function-name fixture boundary so the plants writing the confs sit outside it (the round-5 spec audit's id 20), and AC1's exit 0 over both unmodified modules, owed at its pass commit
- **hands-off** `TOOL-dDeclaredLoop-82` — `derive_conf_reads`, `resolve_memory_root_source`, the `root-source` plant and §4, which that unit widens to cross-module conf constants, mid-string names and aliased calls, gives a source for every branch, and amends (the round-5 spec audit's ids 1, 10, 11, 12, 17, 30)
- **hands-off** `TOOL-dDeclaredLoop-86` — AC1's exit-0 half, which this revision already owes at 80's pass commit as that unit's S4 asks, and S2 and §4's sketch, which it restates to a constant containing a conf name (the round-6 spec audit's ids 11, 12)
- **hands-off** `TOOL-dDeclaredLoop-95` — `resolve_memory_root_source`, whose `.memory-tree.conf` read that unit moves onto `read_tree_conf` (the round-11 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-97` — S2's reader-call callee set and §4's sketch "The rule", which that unit reads from `CONF_READERS` and restates (the round-12 spec audit's id 1)

## 4. Design

### Evidence

Read at branch `unattended-declared-loop-d56bf0`, tip `689e1b07d`, through `git archive` into a scratch
copy, unless named otherwise. `tools/loop/` is absent from this worktree's main. `resolve_memory_root` and
`read_driver_conf` are not built at that tip: they are read on the committed specs of
`TOOL-dDeclaredLoop-72` rev-6 and `TOOL-dDeclaredLoop-70` rev-3.

- 72 rev-6 AC4 counts `read_design_conf`, `read_driver_conf` and `parse_conf` with `grep -c` over the two
  files, and `read_memory_root` across the kit; its edge to this unit asks for a plant observing what that
  grep states (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-72.md`, §6 AC4 and §3).
  S2's `reader call` names are those three for that reason.
- 72 rev-6 §4 "The resolution" returns the driver conf's root where `.unattended.conf` is a file, else the
  memory-tree conf's `MEMORY_ROOT`, else `memory`, refusing first where both confs name different roots.
- 75 rev-9 AC5 and AC30 need `.unattended.conf` in `budget.__doc__` and `breakpoints.__doc__`; AC7 needs
  the line `root records · from .unattended.conf`, and AC8 a held line ending `root from .unattended.conf`
  or `root from .memory-tree.conf`. A literal can name only one of AC8's two endings.
- At the tip, a probe of S2's rule over the two modules finds one hit in each and no reader call: the
  constant `".unattended.conf"` in a path join a driver plant appends to, inside
  `tools/loop/budget.py#run_budget_plant`, in its nested driver case, and inside
  `tools/loop/breakpoints.py#run_breakpoint_plant`. 72 S4's plants and the plants of 63 and 64 add conf
  names to the two modules' fixture code before this pass, and S3's `root-source` plant spells the
  expected sources. The plant therefore cannot be `held` over the live modules at this pass;
  80 S1 draws the boundary that passes over them at order 38 (§8 F3).
- `tools/memory-tree/gen_build_index.py#scan_glob_readers` already builds the set S2 needs: the ids of the
  docstring constants of the module and of every `FunctionDef`, `AsyncFunctionDef` and `ClassDef`, read
  as the first statement's string constant. No module under `tools/loop/` imports `ast` at the tip.
- Each module's `run_selftest` runs every member of its `PLANTS` through
  `tools/loop/loop_lib.py#run_selftest_cases`, each owed `held`, and its `main` dispatches
  `--fixture --plant <case>` for a member and joins `PLANTS` into its usage line. A plant case that needs
  no scratch repository is a branch of the case dispatch, as `budget.py`'s `value` case is.
- `tools/loop/loop_lib.py#read_builds_dir` finds the memory-tree kit through `resolve_kit_dir` from the
  loop kit's own folder, so a resolver read runs in a scratch folder under the host temp directory.
- Neither `loop budget fixtures` nor `loop breakpoint fixtures` carries `pass_leg` in
  `tools/gate-legs.json`. `doc.build-method#m6-passes-commits-parallelism` has the main loop run the pass legs after a unit pass and the
  bar once, after the last unit is terminal.

### The source (S1)

```
resolve_memory_root_source(tree):          # 72 S1's body, each return paired with its branch
    mt = normalise(read_design_conf(tree).get("MEMORY_ROOT") or "")
    if (tree / ".unattended.conf") is a file:
        ua = normalise(read_driver_conf(tree, ["MEMORY_ROOT"]).get("MEMORY_ROOT") or "") or "memory"
        if mt and mt != ua:
            raise ValueError(72 S2's text)
        return ua, ".unattended.conf"
    if mt:
        return mt, ".memory-tree.conf"
    return "memory", "default"

resolve_memory_root(tree):
    return resolve_memory_root_source(tree)[0]
```

`.unattended.conf` present without `MEMORY_ROOT` answers the driver's default with the source
`.unattended.conf`, the branch that answered. `.memory-tree.conf` present without the key answers
`default` here; 82 S15 makes it name that conf.

### The rule (S2)

```
derive_conf_reads(path):
    tree = ast.parse(read(path), path)
    docs = { id(first statement's str constant) for the Module and every ClassDef, FunctionDef and
             AsyncFunctionDef whose body opens with one }          # scan_glob_readers' set
    for node in ast.walk(tree):
        Call whose func is a Name or an Attribute named read_design_conf, read_driver_conf or parse_conf
                                                                    -> (line, "reader call")
        Constant str ending ".memory-tree.conf" or ".unattended.conf", id(node) not in docs
                                                                    -> (line, "conf name")
    answer the hits sorted by line
```

### The plants

Each prints the module's own plant lines, then `held` or `MISSED <why>`, as the module's other plants do.

- `budget.py`, `no-own-conf-read`. A branch of `run_budget_plant`'s case dispatch, beside `value`, writing
  no scratch tree: `derive_conf_reads` over the module's `__file__`, one `loop: fixture · conf read ·
  budget.py:<line> <kind>` line per hit, and a miss naming the count where there is one.
- `breakpoints.py`, `no-own-conf-read`. The same branch of `run_breakpoint_plant`, its lines opening
  `breakpoints:`.
- `budget.py`, `root-source`. Three folders under the plant's scratch, each `git init` so its work-tree top
  is itself: the first holding `.unattended.conf` as `MEMORY_ROOT=records`, the second `.memory-tree.conf`
  as `MEMORY_ROOT=records`, the third neither. For each, `resolve_memory_root_source` and
  `resolve_memory_root` are printed, and a miss is named where the pair or the root is not AC3's. A
  `read_driver_conf` refusal is a miss naming it.

Both plants sit inside a function whose name holds the token `plant`, so 80 S1's boundary covers them
with no move.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `resolve_memory_root_source` | Python function in `tools/loop/loop_lib.py` | `py.function`, verb-first |
| `derive_conf_reads` | Python function in `tools/loop/loop_lib.py` | `py.function`, verb-first |
| `no-own-conf-read`, `root-source` | `PLANTS` names: the first in each of the two modules, the second in `budget.py` | none |
| `reader call`, `conf name` | hit kinds S2 answers | none |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for both functions, run
in the scratch copy of the tip on 2026-11-16: each leads with a declared verb, `resolve` and `derive`.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/breakpoints.py`
- `tools/loop/README.md`
- `help/loop.md`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`

### Alternatives rejected

- **Narrowing 72 AC4 alone.** Done by 72 rev-6, and 75 AC8's two endings still need the source; a reader
  would then probe for `.unattended.conf` itself, a path join S2 rightly counts.
- **Rewording 75's criteria to drop the literals.** The docstrings are where 75's ids 4 and 17 put the
  rationale, and the printed source is what id 42 asks for; removing them reopens those findings.
- **Admitting a conf name in any call argument but `open` and `Path`.** A module-level `CONF = ".unattended.conf"`
  read later through a name would pass; the constant rule sees it.
- **Guessing the source from the root.** Two trees with one root and different confs answer one source,
  the break AC3 stages.
- **Extracting the docstring set into the memory-tree kit's `tree_lib` now** (§8 F4). That is 82 S8, the
  round-5 audit's id 17, at order 41.

## 5. Production-readiness checklist

- security — a read-only parse of the kit's own modules; S1 reads what 72 S1 reads and refuses what it
  refuses.
- perf / scale — one `ast.parse` of one file per `no-own-conf-read` run, milliseconds; `root-source` starts
  one bash, for the one folder holding `.unattended.conf`.
- error / empty / loading states — a module that does not parse is a plant miss naming the file and the
  parse error, never zero hits; a `read_driver_conf` refusal in `root-source` is a miss naming it.
- observability — each hit names the file, the line and its kind; each `root-source` folder prints its
  pair.
- risks — a read composed at run time, `"." + "unattended.conf"`, passes S2, the gap `scan_glob_readers`
  states for its own needle; S1 makes such a read unnecessary. From this pass to 80's pass commit both
  fixture legs exit non-zero on `no-own-conf-read` alone (§8 F3). Until 82 S8 lands the docstring set has
  two copies (§8 F4).
- testing — AC1 to AC5 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: no record or conf moves, and no `[[upgrade]]` row is owed.
- user docs — `help/loop.md`, S5.

### The sweep

Read at the tip `689e1b07d` in the scratch copy; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `resolve_memory_root`, 72's, its body held by S1 | its callers 72 §4 "The callers" names: `tools/loop/adapt.py`, `tools/loop/budget.py`, `tools/loop/loop_transition.py` and the opening read in `tools/loop/breakpoints.py` | the name, signature and answer hold; the pass re-derives the callers with `git grep -n -w resolve_memory_root -- tools/loop` at its base and edits none |
| the same | 72's plants `unattended-root` and `confs-disagree` in both modules, and 64's `pre-placement-records-root` | the root and 72 S2's refusal text are unchanged; AC3 re-runs both `confs-disagree` plants |
| `PLANTS` of `budget.py` gains two, of `breakpoints.py` one | each module's `run_selftest` and `main`, its usage line included | both read the dict; no usage row or flag moves, so the anchors' fingerprints in `help/loop.md` hold |
| the same | the legs `loop budget fixtures` and `loop breakpoint fixtures`, which run `--selftest` | non-zero on `no-own-conf-read` alone from this pass to 80's pass commit, recorded (§8 F3); neither is a pass leg, and the bar runs once at the close |
| the same | their rows in `tools/run-gates/selftest-budgets.txt`, 476 seconds PINNED and 179 seconds PINNED, both proxies | each re-priced from a timed run of the added plants beside the row's own, PINNED with date and node by that file's rule; neither manifest ceiling of 300 seconds PINNED is raised |
| the same | the two legs' `[[exempt_leg]]` rows in `tools/govkit/registry.toml`, their rows in `tools/govkit/subject-pins.tsv`, their `tools/govkit/usage.toml` rows | the rows name no plant; no leg, verb or flag is added |
| the same | the breakpoints fixture sentence of `help/loop.md`, which lists that module's plants | S5 adds the name |
| S1 and S2 minted in `tools/loop/loop_lib.py` | `memory/map/generated/symbols.json` and its three siblings, under `codebase-map coverage + freshness` | `python tools/codebase-map/gen_map.py --write` regenerates them |
| the same | the lexicon offender pin | both names lead with a declared verb (§4 "Inventory") |
| shipped bytes | `install-prefix (shipped surface)` and `kit epoch (shipped bytes move, the version moves)` | the new lines name confs and module files, never a kit path; the loop kit's `KIT_LOOP_VERSION` is owed at the lander, as for 52 and 72 |
| this spec's citations | `memory/project/positional-refs.txt`, its two rows for this spec, rev-5's line citations into `tools/govkit/refusal_join.py` and `tools/gate-lint/encoding_posture.py`, under `positional (the citation check alone)` | this revision cites symbols only, so the commit landing it runs `python tools/playbook/positional.py shrink`, which takes the two rows out |
| this spec's text | 75, 80, 82, 86, 95, 97 and 99 quote S2, AC1 or §4's sketch; 97 and 99 cite S2 and the sketch by line; 86 S4 and AC4 ask AC1 to owe its exit 0 at 80's pass commit; 86 S17 and AC17 and 82 S2 and S16 rewrite S2 and the sketch | AC1 now owes that exit 0 there, so 86 S4 holds; the rule 80, 82, 95 and 97 extend is unchanged but for `read_design_conf`, which 97's tuple restatement keeps beside `parse_conf`; each sibling's re-ground owns its own text |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:tools/loop/budget.py" | grep -n 'unattended\.conf\|memory-tree\.conf'      # one, in run_budget_plant
git show "$B:tools/loop/breakpoints.py" | grep -n 'unattended\.conf\|memory-tree\.conf' # one, in run_breakpoint_plant
git grep -c -e read_design_conf -e parse_conf -e read_driver_conf "$B" -- tools/loop/budget.py tools/loop/breakpoints.py   # no match
git grep -l "import ast" "$B" -- tools/loop                                              # no match
git show "$B:tools/gate-legs.json" | grep -e '"loop budget fixtures"' -e '"loop breakpoint fixtures"'   # no pass_leg
git show "$B:tools/run-gates/selftest-budgets.txt" | grep -e '^loop budget fixtures' -e '^loop breakpoint fixtures'
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-76.md'   # 2
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'                                 # the driver's token, ceiling 343
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'                                    # "1215"
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
git grep -n -e "76 S2" -e "76 AC1" -e "76 §4" "$B" -- memory/builds/dDeclaredLoop/spec/
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED; both minted
  functions lead with a declared verb.
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead.
- The refusal ceilings and families: no `*.sh` is edited, and `tools/memory-tree/check-arms.py#branches`
  and `tools/memory-tree/check-arms.py#scan_refusal_sites` read tracked `*.sh` files alone. The driver's
  ceiling stays 343 PINNED and `tools/unattended/unattended.families.txt` does not move.
- Help anchors: no verb or flag is added, so no usage row and no anchor.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added,
  `tools/memory-tree/check-verdict-epoch.sh` names no loop module, no `[[upgrade]]` row is owed, and no
  file the `watch:` line of `memory/guides/SESSION-KICKOFF.md` names is edited.

### Dependency

`TOOL-dDeclaredLoop-72` (order 36, committed rev-6) is read for `resolve_memory_root`, its rule, refusal,
callers and plants, and AC4; `TOOL-dDeclaredLoop-70` (order 36, committed rev-3) for
`read_driver_conf(tree, names)` and its refusal. Both build before this unit, and this unit builds over
their landed code. `TOOL-dDeclaredLoop-19` and `TOOL-dDeclaredLoop-30` are CLOSED and built the two legs;
`TOOL-dDeclaredLoop-71` (rev-3) writes nothing. At order 34 `TOOL-dDeclaredLoop-53` (rev-3), and at
order 35 `TOOL-dDeclaredLoop-63` (rev-3) and `TOOL-dDeclaredLoop-64` (rev-4), add plants to
`breakpoints.py`, which S3's plant scans as it finds them. `TOOL-dDeclaredLoop-33` (rev-7) and
`TOOL-dDeclaredLoop-56` (rev-6) edit `tools/loop/README.md`, `help/loop.md` and `selftest-budgets.txt` at
other rows and sections. At order 37, `TOOL-dDeclaredLoop-65` writes `tools/loop/position.py` and
`TOOL-dDeclaredLoop-68` writes `tools/loop/loop_witness.py` and `tools/lib/resolve-python.test.sh`,
disjoint from this unit. At order 38 `TOOL-dDeclaredLoop-80` (rev-5) bounds the plant and
`TOOL-dDeclaredLoop-67` edits `budget.py` and `breakpoints.py` after this unit. `TOOL-dDeclaredLoop-34`
is deferred against ask TOOL-dDeclaredLoop-113 and `TOOL-dDeclaredLoop-33`'s numeric direction against
ask TOOL-dDeclaredLoop-114; neither moves a read this unit makes. The reuse probe and the recall query
ran on this worktree's main at `179486e8f`, which holds no loop kit; every other claim was read on the
branch tip.

## 6. Acceptance criteria

Each `python budget.py` and `python breakpoints.py` command below runs in the loop kit's folder.

- **AC1** — When `python budget.py --fixture --plant no-own-conf-read` and the same plant of
  `breakpoints.py` run at this pass commit, each prints one `<file>:<line> <kind>` line per hit and none
  is a `reader call`; a `python -c` probe mapping each named line to its enclosing top-level function
  through `ast` prints, for every hit, a function that seeds or asserts a scratch tree, the population
  `TOOL-dDeclaredLoop-80` S2 moves inside its boundary. In a scratch copy of the kit folder whose
  `budget.py` gains the line `(root / ".unattended.conf").read_text()` in the body of
  `read_budget_value`, the copy's plant names that line and `conf name`.
  Red when: the plant greps substrings, S2 skips a path join of a conf name, or a hit sits in a reader.
  fixture: the exit 0 over both unmodified modules is owed at `TOOL-dDeclaredLoop-80`'s pass commit and
  recorded there, as 86 S4 and 79 S10 state; at this pass the plant's exit and each hit are recorded.
- **AC2** — When a `python -c` probe calls `derive_conf_reads` on a scratch module whose module, function
  and `async def` docstrings each name `.unattended.conf` and which holds nothing else, it answers an
  empty list; on one holding `parse_conf(text, {})`, `ll.read_driver_conf(tree, ["MEMORY_ROOT"])`,
  `read_design_conf(tree)`, `tree / ".memory-tree.conf"` and `print(f"from .unattended.conf")` it answers
  five hits, three `reader call` and two `conf name`; on a module that does not parse it raises
  `SyntaxError`.
  Red when: a docstring counts as a read, an f-string literal part or an attribute call does not, or a
  parse failure answers no hits.
- **AC3** — When `python budget.py --fixture --plant root-source` runs, it prints `held`:
  `resolve_memory_root_source` answers `(records, .unattended.conf)`, `(records, .memory-tree.conf)` and
  `(memory, default)` in the three folders, and `resolve_memory_root` answers the same root in each; and
  `--plant confs-disagree` of each module still prints `held`.
  Red when: the source is guessed from the root, so two folders with one root answer one source, or the
  delegate drops 72 S2's refusal.
- **AC4** — When the main loop runs the `no-own-conf-read` plant of both modules after
  `TOOL-dDeclaredLoop-75`'s pass, at the close, each exits 0 while `grep -c ".unattended.conf"` over the
  two files prints at least 1.
  Red when: 75's printed lines carry the conf as a literal instead of S1's source value.
  fixture: 75 builds at order 39, after 80, so this is observed at the close and not at this pass.
- **AC5** — When `grep -c "no-own-conf-read"` runs over the loop kit's help page, help/loop.md, and
  `grep -c "resolve_memory_root_source"` and `grep -c "derive_conf_reads"` over the kit's README,
  tools/loop/README.md, each prints at least 1.
  Red when: a plant or a library function ships and its page does not name it.

## 7. Gates

`docs` · `help page commands` · `help reference pages` · `install-prefix (shipped surface)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The plants run under the built legs `loop budget fixtures` (`TOOL-dDeclaredLoop-30`) and
`loop breakpoint fixtures` (`TOOL-dDeclaredLoop-19`), which sit outside the base manifest the leg line is
joined against; from this pass to 80's pass commit both exit non-zero on `no-own-conf-read` alone (§8 F3).

New arm: tools/loop/budget.py · covers AC1 AC3 · the no-own-conf-read and root-source plants, staged by a path join of a conf name in a reader of a scratch copy and by a resolver answering the root alone · none
New arm: tools/loop/breakpoints.py · covers AC1 · the no-own-conf-read plant over its own module, staged the same way · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Narrow 72 AC4, or give 75 the source as a value?** The fix offers either. (a) grade "no conf
  read" on the syntax tree; (b) return `(root, source)` and print through it; (c) both. (a) alone leaves
  75 AC8's two endings with no source; (b) alone leaves 72 AC4 a count blind to docstrings and comments.
  (c) satisfies every criterion of both specs. RESOLVED (agent, 2026-10-24, delegated): (c).
  widens: none · relaxes: none
- **F3 — How does this pass meet the conf names its modules' plants already write?** (a) the plant joins
  `PLANTS` now, names those lines at this pass and owes exit 0 at 80's pass commit; (b) the plant joins
  `--fixture` and `--selftest` holds it out until 80 adds it; (c) 80's fixture boundary folded into this
  unit. (b) is a skip read as coverage until a later unit remembers to undo it; (c) takes an audited
  unit's mechanism and its plant moves into this one, which 86 §8 F2 refused. (a) leaves both fixture
  legs non-zero between orders 37 and 38; neither is a pass leg and the bar runs once, at the close after
  80. Recommendation: (a), 86 §8 F2's own pick. RESOLVED (agent, 2026-11-16, delegated): (a).
  widens: none · relaxes: none
- **F4 — Copy `scan_glob_readers`' docstring set, or extract it first?** (a) S2 builds the same set
  inline and 82 S8 extracts it into the memory-tree kit's `tree_lib` at order 41, both walks then calling
  it; (b) this unit extracts it now. (b) takes 82's id 17 and a second kit's write into this unit's
  mechanism, and the loop kit would reach that kit from a library function at this pass. (a) leaves two
  copies of a four-line set for four orders, named in §5 risks. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-4 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-80 and TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-95, written by the round-11 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-97, written by the round-12 spec audit's disposal; nothing else moved.
- rev-6 · 2026-11-16 · §1 to §10 · S1 to S5 · AC1 to AC5 · §8 F2, F3, F4 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `689e1b07d` and on the committed specs of TOOL-dDeclaredLoop-72
  rev-6, TOOL-dDeclaredLoop-70 rev-3, TOOL-dDeclaredLoop-75 rev-9, TOOL-dDeclaredLoop-80 rev-5 and
  TOOL-dDeclaredLoop-86 rev-7, per the brief `2026-11-16-prompt-TOOL-dDeclaredLoop-76-1-spec-writer`: the
  goal restated over 72 rev-6's reader-call AC4; S1 written on 72's resolution, each return paired with
  its source and `resolve_memory_root` answering the pair's root; S2's reader calls the three names 72
  AC4 counts, the docstring set `scan_glob_readers`' own, a parse failure raised; S3's plants placed as
  plant cases; AC1 records the plants' own conf names at this pass and owes exit 0 at 80's pass commit,
  as 86 S4 asks (F3); AC3 re-runs 72's `confs-disagree` plants; S5 and AC5 carry the plant and the two
  functions to help and the kit README; the copied docstring set (F4); the leg named by its built name
  and unit; line citations made symbol citations; the sweep.

## 10. Reuse audit

The seams are 72's `resolve_memory_root`, whose body S1 holds and pairs with its branch so no second
resolver is minted, the docstring set `tools/memory-tree/gen_build_index.py#scan_glob_readers` already
builds, which S2 mirrors until 82 S8 shares it (§8 F4), and each module's `PLANTS` run through
`tools/loop/loop_lib.py#run_selftest_cases`, which the two plants join with no new runner.
`python tools/codebase-map/reuse_lookup.py "classify a module's conf reads by walking its syntax tree, skipping docstrings"`,
on this worktree's main at `179486e8f`, ranked `read_text`, `read`, `tree`, `walk`, `load_conf`,
`parse_conf`, `read_conf` and `read_design_conf`; none classifies a module's conf reads, so no existing
seam fits the rule itself, and a grep for `get_docstring` and `body[0].value` across `tools/` finds the
docstring set in `scan_glob_readers`.
`python tools/memory-recall/query.py "the loop readers grade their own conf reads on the syntax tree and print the root's source" --terms "<the terms below>"`
returned this spec, `TOOL-dDeclaredLoop-97`, `TOOL-dDeclaredLoop-80` and `TOOL-dDeclaredLoop-99`, and no
other conf-read rule.

Recall terms used: derive_conf_reads resolve_memory_root_source no-own-conf-read root-source docstring ast conf name reader call budget breakpoints fixture boundary
