# TOOL-dDeclaredLoop-70 — every caller of the phase reading takes the adopter population from one driver-conf reader

**Status:** INPROGRESS · rev-4 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 36 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-70-deviation-701.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-70-deviation-701.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-70-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-70-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-70-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-70-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-70-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-70-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 19 at HIGH**, its item **H3**, alone in that item. `TOOL-dDeclaredLoop-63` gives
`derive_phase_position` the parameter `extra=()` and feeds it only from the `--phase` hold in
`tools/unattended/unattended.sh`, which passes `--extra=$PHASES_EXTRA`. Every caller the driver does not
start gets the empty default and refuses an adopter's phase by name: a hand run of `loop_table.py phase`,
`TOOL-dDeclaredLoop-56` S18's `read_withdrawn_parents`, and `TOOL-dDeclaredLoop-67` S13's held-from
resolution. That is the wedge round 2 graded high, on the paths 63 left out.

This unit takes the fix's second form: the population comes from one place every caller shares. An absent
`extra` reads `PHASES_EXTRA` from the work tree's `.unattended.conf`, sourced as the driver sources it,
through one reader of the driver's conf. It repairs `TOOL-dDeclaredLoop-63`.

## 2. Scope (IN)

- **S1** — The reader, §4 "The reader": `read_driver_conf(tree, names)` in `tools/loop/loop_lib.py`, the loop
  kit's one reader of a value the driver takes from `.unattended.conf`. The conf is that file at the top of
  `tree`'s work tree, the first of `tree` and its parents holding `.git`, else `tree`. The reader sources it
  in bash with the top as the working directory, the bash `tools/loop/loop_witness.py#resolve_bash` finds
  able to see the file, and reads each named value and then a sentinel back, the import shape of the
  unattended kit gate. It answers `{name: value}` for the names the conf sets, `{}` where the file is absent,
  and holds each answer for the process, keyed by the conf and the names. A name outside `[A-Z][A-Z0-9_]*`
  is a `ValueError` before any bash starts. Observed by AC1, AC3.
- **S2** — A read that fails refuses by name, never answering an empty population: no bash resolved, a bash
  that does not start, a non-zero exit, or a stream that does not end in the sentinel each raise
  `tools/loop/loop_lib.py#LoopError` reading `driver conf unreadable: <conf> — <reason>`. Observed by AC3.
- **S3** — The default, §4 "The default": `derive_phase_position(phase, facts, phase_map=None, extra=None,
  tree=".")`. Where the map holds no row of `phase`, the population is `extra` when given, else the
  `PHASES_EXTRA` members `read_driver_conf(tree, ("PHASES_EXTRA",))` answers, split on whitespace; a phase
  the map holds a row of reads its row and starts no read. An explicit `extra`, the empty one included,
  wins. The `phase` verb's `--extra` defaults to `None`, so a run without the flag reads the working
  directory's tree, for `--from` and `--to` alike. Its `adopter phase` marker prints where the map holds no
  row of the phase and the reader answered it, whatever supplied the population. S2's `LoopError` prints as
  the verb's `loop: refused · <why>` line, exit 1. Observed by AC1, AC3.
  **Readers:**
  by name: `tools/loop/loop_table.py`, the phase verb, its reader and its selftest cases, and `tools/loop/loop_parents.py`, the withdrawn-parent read
  by value: `tools/loop/loop_table.py`, whose no-row refusal and adopter marker read the population, and `tools/unattended/unattended.sh`, whose hold passes the value explicitly and reads no default
- **S4** — The callers, §4 "The callers": each is enumerated with what it passes, and none passes an empty
  population it did not read from its own conf. `read_withdrawn_parents` passes `tree=root`, the route's
  `--root`, so a parent's phase reads against the tree that wrote it (§8 F4). The selftest case of
  `TOOL-dDeclaredLoop-52` that reads `DRAFTING` with no row passes `--extra=`, so the case reads no conf of
  the tree the leg runs in. Observed by AC2, AC5.
- **S5** — The arms the `New arm:` lines in §7 declare, §4 "The arms": the scratch-tree cases among the
  selftest cases of `loop_table.py check --selftest`, and the plant `parent-in-extra-phase` of
  `tools/loop/loop_parents.py` with its selftest case. Observed by AC1, AC2, AC3.
- **S6** — The carriers. `help/loop.md` gains one sentence in its phase-map section on the verb's default
  and names the new plant among the parent route's cases; `tools/loop/README.md` gains a row for the reader
  in its table of this library's readers, names it among the library's reaches outside the standard
  library, and names the new plant; the module docstrings of `tools/loop/loop_lib.py` and
  `tools/loop/loop_table.py` say the same. Observed by AC4.

## 3. Non-goals (OUT)

- `check_transition_tables`' own read of `PHASES_EXTRA` (`TOOL-dDeclaredLoop-67` S23): the audit's ids 20
  and 21, batched into `TOOL-dDeclaredLoop-75`, which points it at S1.
- The held-from lookup's code: `TOOL-dDeclaredLoop-67` S13 builds it at order 38 and inherits S3's default by
  calling `derive_phase_position` with no explicit `extra`, as its consumes-from bullet records.
- The subshell's isolation from the caller's environment, and the driver's `ROOT` and `CONF` set inside it:
  `TOOL-dDeclaredLoop-79` S1 and S2 (ids 2, 16, 32).
- The records root read through S1: `TOOL-dDeclaredLoop-72`'s `resolve_memory_root`.
- A `--root` flag on the `phase` verb: the working directory's tree is the driver's own rule, and no clause
  asks for another surface.
- A `--plan` adopter reading: the rev-2 callers table named one, and `TOOL-dDeclaredLoop-63` rev-3 takes it
  out of that unit's scope, since `--plan` prints no phase reading.
- A checklist entry that a parameter added with a default enumerates its callers, the finding's
  left-shift: the class is recorded at the close; §4's table is this parameter's enumeration.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-63` — the `extra` parameter of `derive_phase_position`, the verb's `--extra` and the adopter-phase reading and marker, whose absent value this unit makes the work tree's own population
- **consumes-from** `TOOL-dDeclaredLoop-56` — S18's `read_withdrawn_parents` call, which takes S3's default by passing `tree=root` and no explicit `extra`; 56 lands first in order 36 and this unit writes `tree=root` on that call (§8 F4)
- **hands-off** `TOOL-dDeclaredLoop-67` — S13's held-from lookup, which takes S3's default and passes no explicit `extra`
- **hands-off** `TOOL-dDeclaredLoop-72` — `read_driver_conf`, through which that unit reads the driver's `MEMORY_ROOT`
- **hands-off** `TOOL-dDeclaredLoop-75` — `read_driver_conf`, to which that unit points `check_transition_tables` (ids 20, 21)
- **hands-off** `TOOL-dDeclaredLoop-79` — `read_driver_conf`'s subshell, which that unit isolates from the caller's environment and gives the driver's `ROOT` and `CONF` (ids 2, 16, 32)

## 4. Design

### Evidence

Every claim below was read at the tip of branch `unattended-declared-loop-d56bf0`, `e8018d94`, through `git
show` and in a scratch export of that tree; the worktree this spec was written in is cut from main, which
holds no loop kit.

- `tools/unattended/unattended.sh#load_driver_conf` takes `ROOT` from `git rev-parse --show-toplevel`, moves
  there, sets `CONF` to `$ROOT/.unattended.conf`, assigns `PHASES_EXTRA` blank on its init line and then
  sources the conf; `tools/unattended/unattended.sh#phases` composes `PHASES_CORE` and `PHASES_EXTRA`. gov's
  `.unattended.conf` sets `PHASES_EXTRA` blank.
- The unattended kit gate imports conf values by sourcing `.unattended.conf` in a subshell, `|| exit 9`,
  printing NUL-separated pairs and the sentinel `__CONF_IMPORT_OK__`, and its comment records why the
  sentinel and not the exit code is the verdict (`tools/unattended/check-unattended.sh@2a0e6616ca6f:484-491`).
- `tools/loop/loop_witness.py#resolve_bash` answers the bash that can see a given path, by running each
  candidate, or `None`; `TOOL-dDeclaredLoop-42` S1 runs the witness re-run's commands under it, and
  `tools/loop/position.py#read_handover` and `tools/loop/position.py#run_driver` find the driver's bash
  through it.
- No Python under `tools/loop/` reads `.unattended.conf`: its four mentions are fixture writers in
  `tools/loop/breakpoints.py#run_breakpoint_plant`, `tools/loop/budget.py#run_budget_plant` and
  `tools/loop/loop_witness.py#check_hold_plant`, and the copy in `tools/loop/position.py#write_position_plant`.
  No tracked file under `tools/` or `help/` spells `read_driver_conf` or `derive_phase_position` at the tip.
- `tools/loop/loop_lib.py#resolve_kit_dir` finds a work tree's top as the first of a path and its parents
  holding `.git`; the same idiom sits inline in `breakpoints.py`, `budget.py`, `factories.py` and
  `loop_items.py` beside it.
- `tools/loop/loop_lib.py#LoopError` is a `ValueError` whose message is `<where>: <what>`.
- `tools/loop/loop_table.py#main` runs `check --selftest`'s cases through `run_table_case`, a dispatcher that
  hands every case but `direction-order` to `main`, and `tools/loop/loop_lib.py#run_selftest_cases`.
- `tools/loop/loop_parents.py#read_withdrawn_parents` reads each parent's `RUN.md` under `root` and compares
  its `phase` fact with `ABORTED` literally; `tools/loop/loop_parents.py#run_fixture` runs `route --root
  <scratch>` in process, the working directory unchanged, over the repository
  `tools/loop/loop_parents.py#write_parent_plant` commits.
- `TOOL-dDeclaredLoop-52` rev-3, read on its committed spec: `derive_phase_position(phase, facts,
  phase_map=None)` raises `LookupError` for a phase with no row; the verb prints `refused — phase <PHASE>: no
  row`, exit 1, and `loop: refused · <why>`, exit 1, for a table that does not read; its selftest carries the
  readings of its AC1, `phase --from DRAFTING` among them.
- `TOOL-dDeclaredLoop-63` rev-3, read on its committed spec: `extra=()` read by membership where the map holds
  no row; the verb's `--extra` defaulting to the empty string; the marker `adopter phase`; and the hold
  `check_phase_gates` passing `"--extra=$PHASES_EXTRA"`.
- `TOOL-dDeclaredLoop-31`, CLOSED, wrote no reader: its two readings are `TOOL-dDeclaredLoop-52` S1's qualified
  rows, read through the verb, so the rev-2 row for "31 S7's phase reading" is the verb's row.

### The callers

| Caller | Spec | What it passes | Conf read |
|---|---|---|---|
| the `--phase` hold, `check_phase_gates`, through the verb | `TOOL-dDeclaredLoop-52` S4, 63 S3 | `--extra=$PHASES_EXTRA`, explicit | never |
| the `phase` verb run by hand, `--from` and `--to` | 52 S2, 63 S2 | `--extra` where given, else nothing | the working directory's tree, for a phase with no row |
| the verb's selftest cases | 52 S6, 63 S4, S5 here | an explicit `--extra` on every no-row case, `--extra=` on 52's `DRAFTING` case | only S5's scratch-tree cases |
| `read_withdrawn_parents` | `TOOL-dDeclaredLoop-56` S18 | `tree=root` | the route's `--root` tree, for a parent phase with no row |
| the held-from lookup | `TOOL-dDeclaredLoop-67` S13 | nothing, as the verb | as the verb |
| `check_transition_tables` | 67 S23, `TOOL-dDeclaredLoop-75` S32 | not a caller of the reader | S1 directly, after 75 |

### The reader

```
read_driver_conf(tree, names) -> {name: value}
    names: each matches [A-Z][A-Z0-9_]*, else ValueError
    top  = first of (tree, *tree.parents) holding .git, else tree        # the driver's ROOT
    conf = top/.unattended.conf ; absent -> {}
    memo[(conf, tuple(names))] -> a copy of it
    bash = resolve_bash(conf) ; None -> LoopError "driver conf unreadable", "<conf> — no bash that can see it"
    run [bash, "-c", '__rdc_conf=$1; shift; __rdc_names=("$@")
                      . "$__rdc_conf" >/dev/null 2>&1 || exit 9
                      for n in "${__rdc_names[@]}"; do eval "v=\${$n-__UNSET__}"; printf "%s\0%s\0" "$n" "$v"; done
                      printf "__CONF_IMPORT_OK__\0\0"', "_", conf, *names],
        cwd=top, stdin closed, stdout captured as bytes and decoded as UTF-8
    OSError -> LoopError ... "<conf> — <the error>"
    rc != 0 -> LoopError ... "<conf> — exit <rc>"
    the stream not ending in the sentinel pair -> LoopError ... "<conf> — no __CONF_IMPORT_OK__ sentinel"
    return {n: v for each pair before the sentinel where v != "__UNSET__"}
```

The names are held in an array before the source, so a conf that runs `set --` cannot change which values are
read; a conf that prints is silenced by the redirect, and a conf that exits ends the subshell before the
sentinel. `loop_witness` imports `loop_lib` at module level, so the reader imports `resolve_bash` inside the
function, as `read_builds_dir` imports its conf reader.

### The default

```
derive_phase_position(phase, facts, phase_map=None, extra=None, tree=".")
  as TOOL-dDeclaredLoop-52 §4 "The reader", where it finds no row of `phase`:
  pop = extra if extra is not None
        else read_driver_conf(tree, ("PHASES_EXTRA",)).get("PHASES_EXTRA", "").split()
  phase in pop -> ("none", "none")
  otherwise    -> LookupError naming the phase
```

The verb's `--extra` is `default=None`: absent, it passes `extra=None` and the default `tree`; `--extra=`
passes the empty tuple. The verb prints its marker where the map holds no row of the phase and the reader
answered, which is exactly where the reader answered from the population. Its `except LoopError` path, which
prints `loop: refused · <why>` for a table that does not read, covers the call to the reader.

### The arms

`run_table_case` gains one arm: a case whose argv opens `tree <name>` runs the rest through `main` with the
working directory moved into the scratch work tree `<name>`, restored after. The selftest builds three such
trees under one temporary folder before its cases and removes them after, each a repository from
`tools/loop/loop_witness.py#run_fixture_git` `init` with its conf written by
`tools/loop/loop_witness.py#write_fixture_files`:

| Tree | `.unattended.conf` | Case | Owed |
|---|---|---|---|
| `extra` | `PHASES_EXTRA="STAGING"` | `phase --from STAGING` | exit 0, `phase STAGING · state none · step none · adopter phase` |
| `extra` | same | `phase --from REVIEWING --to STAGING` | exit 0, a line ending `adopter phase · crosses none` |
| `extra` | same | `phase --from STAGNG` | exit 1, `refused — phase STAGNG: no row` |
| `extra` | same | `phase --from STAGING --extra=` | exit 1, `refused — phase STAGING: no row` |
| `broken` | `exit 3` | `phase --from STAGING` | exit 1, `loop: refused · driver conf unreadable:` naming `exit 3` |
| `broken` | same | `phase --from REVIEWING` | exit 0, `phase REVIEWING · state designing · step step.design` |
| `bare` | none | `phase --from STAGING` | exit 1, `refused — phase STAGING: no row` |

The plant `parent-in-extra-phase` joins `PLANTS` of `tools/loop/loop_parents.py`: `write_parent_plant` writes
the parent's `RUN.md` with `phase: STAGING` and the scratch repository's `.unattended.conf` with
`PHASES_EXTRA="STAGING"`, and the selftest gains the case owing `route none`, exit 0. The fixture runs the
route in process with the working directory left where the leg runs, so only `tree=root` reaches the
scratch's conf.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_driver_conf` | Python function | `py.function`, verb-first |
| `tree` | keyword of `derive_phase_position` | none |
| `parent-in-extra-phase` | plant of `loop_parents.py` | none |
| the `tree <name>` case form | selftest dispatch inside `run_table_case` | none |

`python tools/lexicon/lexicon.py --suggest read_driver_conf --as py.function` printed OK, leading with `read`.
It ran in this spec's worktree, cut from main at `179486e8`, whose `.lexicon.conf` differs from the branch tip's
only in `VERB_OFFENDER_PIN` and its comment; the lexicon kit's verb declarations are byte-identical.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/loop_table.py`
- `tools/loop/loop_parents.py`
- `tools/loop/README.md`
- `help/loop.md`
- `memory/map/generated/symbols.json`, with any generated sibling `gen_map.py --write` rewrites

### Alternatives rejected

- **Threading `--extra` from every caller.** The callers the driver does not start would each need their own
  source of the value, which is the two-readers class over again.
- **An environment variable the driver exports.** A hand run or a gate leg has no driver parent and would read
  the empty set, the refusal this unit removes.
- **The memory-tree kit's `parse_conf_line` (`tools/memory-tree/tree_lib.py#parse_conf_line`).** It reads one
  assignment's text, held to bash by a parity arm of `tools/govkit/selftest.py`, and cannot see a value the
  conf computes; `TOOL-dDeclaredLoop-63` rejects parsing the conf's text for that reason. Sourcing is the
  driver's own composition.
- **Reading the conf on every call.** A conf that does not source would then refuse every core phase and every
  parent read; reading only where the map holds no row keeps S2's refusal on the phases it concerns.
- **The loop kit's own work tree as the default.** A plant that runs the kit over a scratch repository, as the
  driver's plants do, would read gov's conf; the driver reads the tree it runs in.

## 5. Production-readiness checklist

- security — sourcing `.unattended.conf` runs project shell, which the driver already does on every verb; it
  runs only for a phase the map holds no row of; each name is held to the variable-name shape before it
  reaches `eval`; stdin is closed and the output is read as data.
- perf / scale — at most one bash per conf and name set per process, after `resolve_bash`'s probe; none for
  a mapped phase, and none on the driver's hold, which passes its value.
- error / empty / loading states — S2 refuses by name; an absent conf and a blank `PHASES_EXTRA` each read no
  adopter phase.
- observability — S2's refusal names the conf and the reason.
- risks — a conf that never returns holds the read as it holds the driver, which sources the same file
  unbounded; a value the caller's environment exports reads as the conf's until `TOOL-dDeclaredLoop-79` S1
  isolates the subshell.
- testing — AC1 to AC3 and AC5 through the arms under §7, observed RED then GREEN at the close; AC4 a docs
  probe.
- migration — none: the reading lands at order 35, and the only caller passing nothing before this unit is a
  hand run and the kit's own selftest.
- user docs — `help/loop.md`'s phase-map section gains the sentence below, and the parent route's cases name
  the new plant:

```
Run without --extra, the phase verb reads PHASES_EXTRA from the .unattended.conf at the top of the work tree
it runs in, sourced in bash as the driver sources it; a conf that does not source refuses the reading of a
phase the map holds no row of, and a phase the map holds a row of never reads the conf.
```

### The sweep

| Changed | Population | What keeps it green |
|---|---|---|
| `tools/loop/loop_lib.py` gains `read_driver_conf` | every loop module importing `loop_lib`, each loop leg, all unguarded; `TOOL-dDeclaredLoop-72`, 75, 76, 79, 82, 97, 98 and 99, which read the name and its `(tree, names)` mapping | a new name beside the others; no existing function moves; the name and signature are rev-2's, which those specs read; it sources a file and imports a module of this kit, so no `requires` edge in `tools/loop/kit.toml` moves |
| `derive_phase_position` gains `tree`, `extra` defaults to `None` | 52's verb and selftest, 63's cases and the hold's call, 56 S18's call, 67 S13's lookup | a phase with a row starts no read; every 63 case passes `--extra`; the hold passes `--extra=$PHASES_EXTRA`; 52's `DRAFTING` case passes `--extra=` (S4) |
| the verb's `--extra` default | `tools/govkit/usage.toml`'s row for the verb, which lists flags and no default; its help anchor | no flag added, so the row and its fingerprint stay |
| `run_table_case` and the selftest's trees | the `loop transition tables` leg, ceiling 120 PINNED at `e8018d94` in `tools/gate-legs.json` | three `git init` runs and two conf reads beside the existing in-process cases |
| `tools/loop/loop_parents.py`, the call and `PLANTS` | the `loop parent routes` leg, ceiling 120 PINNED at `e8018d94`; its eleven existing cases; 56's plants | every existing plant's parent reads a core phase, so no read starts; the new plant adds one scratch repository |
| the `driver-plan` plant of `tools/loop/breakpoints.py` | the `loop breakpoint fixtures` leg | the hold passes its value, so no read starts |
| `help/loop.md` | `docs`, `help page commands` | prose only, no command block; no usage row moves, so no anchor is re-stamped |
| `tools/loop/README.md`, the docstrings | `install-prefix (shipped surface)` | name siblings by file name and the conf by its file name, never a path under the install prefix |
| a subprocess read | `encoding posture (text IO names its encoding)`, `python reads (a name never bound, an import outside its guard)` | output captured as bytes and decoded as UTF-8; the import sits inside the function, as `read_builds_dir`'s does |
| the census and the families | `tools/memory-tree/check-arms.py`'s readers over the driver; `tools/unattended/unattended.families.txt` | no shell file is edited |
| new names | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at `e8018d94` | `read_driver_conf` leads with a declared verb |
| shared records | `SHARED_RECORDS` in `.unattended.conf` | the pass writes neither `memory/DECISIONS.md` nor `memory/project/readme-contract.txt`; no decision row is owed |
| the kickoff manifest | `watch:` of `memory/guides/SESSION-KICKOFF.md` | no watched path is edited, so no re-stamp |
| subject pins, epoch delegates, upgrade rows, the registry, size rows | `tools/govkit/subject-pins.tsv`, `tools/memory-tree/check-verdict-epoch.sh`'s `DELEGATES`, `[[upgrade]]`, `tools/govkit/registry.toml`, `tools/template-size-limits.txt` | no leg added, no memory-tree module edited, no migration, no kit added; no size row names a loop file or `help/loop.md` |
| the codebase map | `codebase-map coverage + freshness`; `recall floor` and `recall floor arms`, whose guard `memory/` takes in the regenerated file | `python tools/codebase-map/gen_map.py --write` records the new function there, the generator's own output; both recall legs run over it at the close |
| this spec's citations | `positional (the citation check alone)`; the five rows of this spec in `memory/project/positional-refs.txt` | this revision cites by symbol and one blob-pinned range; the commit landing it runs `python tools/playbook/positional.py shrink` |
| other units | 97 and 99 cite this spec's rev-2 text by line; 72 reads `read_driver_conf(tree, ["MEMORY_ROOT"])`; 79's sketch extends the rev-2 subshell | each re-grounds at its own order; the reader's name, arguments and answer are rev-2's |

```
B=branch/unattended-declared-loop-d56bf0
git grep -c 'read_driver_conf\|derive_phase_position' "$B" -- tools help          # no hit, exit 1
git grep -n '\.unattended\.conf' "$B" -- tools/loop                               # the four fixture and copy sites
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN='
git show "$B:.memory-tree.conf" | grep -o 'unattended/unattended.sh:[0-9]*:[0-9-]*:[A-Za-z0-9-]*'
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-70.md'
git show "$B:tools/gate-legs.json" | grep -A12 '"loop parent routes"\|"loop transition tables"' | grep ceiling
```

### Budgets and records

- The driver's census, read through `tools/memory-tree/check-arms.py#branches` and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` over the scratch export, is 342 PINNED at `e8018d94`,
  337 branches and 5 sites PINNED, at its ceiling under `TOOL-dDeclaredLoop-19`'s row;
  `TOOL-dDeclaredLoop-52` raises it to 343 PINNED under its landed decision row. This unit edits no shell
  file, so the census and the ceiling stay where unit 52 leaves them.
- The families of `tools/unattended/unattended.families.txt` do not move.
- `tools/unattended/check-unattended.sh` stays at 266 of its 266 PINNED; it is not edited.
- `VERB_OFFENDER_PIN` stays 1215 PINNED: the one new function name leads with `read`.
- The shared records: the pass writes neither `memory/DECISIONS.md` nor `memory/project/readme-contract.txt`,
  and no decision row is owed ahead of it.
- Help anchors: none added or re-stamped; no verb or flag is added.
- The loop kit's version is owed at the lander.

### Dependency

Order 36, beside `TOOL-dDeclaredLoop-56` (rev-5), `TOOL-dDeclaredLoop-71` (rev-2) and `TOOL-dDeclaredLoop-72`
(rev-5), each read on its committed spec. The step lists 56 first and is not parallel, so 56 S18's call in
`read_withdrawn_parents` stands when this unit builds, and S4 adds `tree=root` to it; were 56 to land after,
that argument is 56's, by the hands-off edge, and AC2 is observed at 56's close (§8 F4). Unit 72 builds after
this unit and calls S1. Unit 71 adds a leg for `tools/loop/breakpoints.py`; if its guard names
`tools/loop/loop_lib.py` when this unit builds, that leg is owed on §7's line too.

Order 35's `TOOL-dDeclaredLoop-63` (rev-3) is read on its committed spec: `extra`, the verb's `--extra`, the
marker, its selftest cases and the hold's argument, all of which land before this unit builds. Units 54 (rev-3)
and 64 (rev-4) edit `tools/loop/loop_table.py` and `tools/loop/breakpoints.py` elsewhere, and 55 (rev-3) writes
nothing here. Order 34's `TOOL-dDeclaredLoop-52` (rev-3) is read on its committed spec: the reader, the verb,
its selftest cases and the hold; `TOOL-dDeclaredLoop-33` (rev-6, building) and `TOOL-dDeclaredLoop-53` (rev-3)
touch none of them. Units through order 33 are CLOSED, read on landed code at `e8018d94`;
`TOOL-dDeclaredLoop-34` is deferred against ask TOOL-dDeclaredLoop-113 and shares no file. The code reads, the
census and the reuse probe ran in a scratch export of the branch tip; the counts above ran through `git show`
and `git grep` of the branch; the lexicon suggest ran in this spec's worktree, as §4 "Inventory" says.

## 6. Acceptance criteria

Each `python loop_table.py` and `python loop_parents.py` command below runs that file of gov's loop kit by its
absolute path; the working directory is the one the criterion states, else the top of the repository.

- **AC1** — When `python loop_table.py phase --from STAGING` runs with its working directory a scratch work
  tree whose `.unattended.conf` sets `PHASES_EXTRA="STAGING"`, it prints `phase STAGING · state none · step
  none · adopter phase` and exits 0; `phase --from REVIEWING --to STAGING` there ends `· to STAGING · adopter
  phase · crosses none`; `phase --from STAGNG` exits 1 printing `refused — phase STAGNG: no row`; and `phase
  --from STAGING --extra=` exits 1 printing `refused — phase STAGING: no row`.
  Red when: an absent `--extra` reads the empty tuple, so `STAGING` is refused in a tree that declares it.
- **AC2** — When `python loop_parents.py --fixture --plant parent-in-extra-phase` runs from the top of gov's
  tree, it prints `route none` and exits 0, its scratch parent's run record holding `phase: STAGING` and the
  scratch's `.unattended.conf` setting `PHASES_EXTRA="STAGING"`.
  Red when: the parent read passes no tree, so the population is gov's blank one and the route exits 2
  printing `loop: unarmed` and naming `STAGING`.
  fixture: the call is `TOOL-dDeclaredLoop-56` S18's, which lands before this unit in order 36.
- **AC3** — When `python loop_table.py phase --from STAGING` runs in a scratch work tree whose
  `.unattended.conf` holds `exit 3`, it exits 1 printing `loop: refused · driver conf unreadable:` and naming
  `exit 3`; `phase --from REVIEWING` there prints `phase REVIEWING · state designing · step step.design` and
  exits 0; and in a scratch work tree holding no `.unattended.conf`, `phase --from STAGING` exits 1 printing
  `refused — phase STAGING: no row`.
  Red when: a conf that does not source reads as an empty population, so the first prints `no row`.
- **AC4** — When `grep -c 'as the driver sources it' help/loop.md`, `grep -c 'read_driver_conf'
  tools/loop/README.md` and `grep -c 'parent-in-extra-phase' help/loop.md tools/loop/README.md` run, each
  count is at least 1.
  Red when: the verb's default moves with no page saying so.
- **AC5** — When `python loop_table.py check --selftest` runs with its working directory a scratch work tree
  whose `.unattended.conf` sets `PHASES_EXTRA="DRAFTING"`, it exits 0, its `DRAFTING` case passing.
  Red when: that case reads the working tree's conf, so it prints `adopter phase` and fails.

## 7. Gates

`loop transition tables` · `loop parent routes` · `loop definition` · `loop breakpoint fixtures` · `docs` · `help page commands` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `positional (the citation check alone)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_table.py · covers AC1 AC3 AC5 · the scratch-tree cases among the selftest's and the `DRAFTING` case's `--extra=`, staged against `TOOL-dDeclaredLoop-63`'s empty default, which refuses `STAGING` for lacking a row in every tree · none

New arm: tools/loop/loop_parents.py · covers AC2 · the `parent-in-extra-phase` plant and its selftest case, staged against a parent call passing no tree, which reads the working directory's conf · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Thread the value from every caller, or read it in one shared place?** The fix names both. (a)
  every caller passes it leaves the Python callers no source; (b) one reader all callers default to.
  (a) fails AC2 for the callers the driver does not start, and veto 1 discards it. RESOLVED (agent,
  2026-10-24, delegated): (b). widens: none · relaxes: none
- **F3 — Whose conf does an absent `extra` read?** Options: (a) the conf at the top of an explicit `tree`'s
  work tree, `tree` defaulting to the working directory, the driver's own rule for `ROOT`; (b) the conf of the
  work tree holding the loop kit; (c) the working directory's alone, no `tree` argument. (b) reads gov's conf
  for a kit run over a scratch repository, and (c) reads the wrong conf for a route given `--root`.
  Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F4 — Who writes `tree=root` on the parent read's call?** Options: (a) this unit, over the call
  `TOOL-dDeclaredLoop-56` S18 lands first in order 36, and 56 where it lands after; (b) 56 alone, by the
  hands-off edge; (c) nobody, the parent read taking the working directory's conf. (b) leaves the call 56
  builds before this unit without the argument, since 56's spec predates it, and (c) is the wedge for a route
  run with `--root`. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 19 (HIGH, item H3).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-16 · §1 to §10 · S1 to S6 · AC1 to AC5 · §8 F3 F4 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `e8018d94`, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-70-1-spec-writer`: symbol citations; the reader at the work tree's
  top, through the loop kit's `resolve_bash`, refusing with `LoopError`; the default read only for a phase
  with no row, on unit 63's rev-3 `extra` and `phase --from` verb, the `--plan` row and unit 31's reading out of
  the callers table; the `tree` argument (F3) and the parent call's `tree=root` (F4); the plants move from
  `loop_table.py --fixture` to the selftest's scratch-tree cases and a `loop_parents.py` plant; unit 52's
  `DRAFTING` case pinned to `--extra=`; carriers and the sweep.
- rev-4 · 2026-11-16 · §3 · the edge with `TOOL-dDeclaredLoop-56` reads consumes-from, since 56 builds first and this unit
  writes onto its call, per 56's first builder return; nothing else moves.

## 10. Reuse audit

The seams this unit extends: the driver's composition of its conf (`tools/unattended/unattended.sh#load_driver_conf`),
sourced as the unattended kit gate imports it, with the loop kit's `tools/loop/loop_witness.py#resolve_bash`;
the work-tree top idiom of `tools/loop/loop_lib.py#resolve_kit_dir`; `TOOL-dDeclaredLoop-63`'s
`derive_phase_position` and `phase` verb, each extended in place; `run_table_case` and
`tools/loop/loop_lib.py#run_selftest_cases` for the cases; and `tools/loop/loop_parents.py#write_parent_plant`
for the plant.

`python tools/codebase-map/reuse_lookup.py "read the adopter phase vocabulary from the driver conf"`, run in the
scratch export of the branch tip `e8018d94`, ranked name-stem neighbours (`read_text`, `read`, `load_conf`,
`parse_conf`), the driver's `phases`, and the conf readers `read_conf` (`tools/playbook/render_playbook.py#read_conf`)
and `read_conf_key` (`tools/roles/roles_lib.py#read_conf_key`). Each conf reader parses a line's text and
sources nothing, and no Python reader sources `.unattended.conf`, so no existing Python seam fits and S1 is the
loop kit's first.

Recall terms used: MEMORY_ROOT PHASES_EXTRA unattended.conf memory-tree.conf sourced subshell sentinel driver conf reader two-readers resolve_bash work tree top
