# TOOL-dDeclaredLoop-63 — an adopter's extra phase reads as ungated through the driver's own phase set, never refused for lacking a row

**Status:** CLOSED · rev-3 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 35 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-63-deviation-631.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-63-deviation-631.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-63-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-63-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-63-deviation-632.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-63-deviation-632.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-63-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-63-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-63-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-63-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-63-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-63-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 56 at HIGH**, its item **H8**, alone in that item; id 35 is the same defect at
medium grade, item M16, batched into `TOOL-dDeclaredLoop-67`. The driver's phase vocabulary is
`tools/unattended/unattended.sh#phases`, `PHASES_CORE` plus the conf's `PHASES_EXTRA`, and
`tools/unattended/unattended.sh#verb_phase` admits any member of it. `TOOL-dDeclaredLoop-52` (rev-3) maps
`PHASES_CORE` alone: its reader refuses a phase with no row by name, and its `--phase` hold,
`check_phase_gates`, relays that refusal through `fail 82`. So once it lands, every `--phase` move into or out
of an adopter's own phase is refused, wedging that adopter's unattended runs. This unit gives an extra phase a
defined reading taken from the driver's resolved set. It repairs `TOOL-dDeclaredLoop-52`.

## 2. Scope (IN)

- **S1** — The reader, §4 "The reading": `derive_phase_position(phase, facts, phase_map=None, extra=())`
  answers `("none", "none")` for a phase the map holds no row of that is a member of `extra`, and still
  raises `LookupError` naming a phase in neither. A phase the map holds a row of reads its row, whether or
  not `extra` names it. This amends `TOOL-dDeclaredLoop-52` §5's "a phase with no row refuses by name" to
  phases outside the driver's set. Observed by AC1.
- **S2** — The verb, §4 "The verb": `loop_table.py phase` gains `--extra "<space-separated phases>"`, read
  for `--from` and `--to` alike, and prints `· adopter phase` after the reading of a phase answered from
  `extra`; the `crosses` field stays the line's last. The module docstring's usage line names the flag.
  Observed by AC1.
- **S3** — The consumer: `check_phase_gates` in `tools/unattended/unattended.sh` passes
  `"--extra=$PHASES_EXTRA"` to its `run_loop_verb loop_table.py phase` call, the half of `phases()` the conf
  supplies, so the loop kit never derives the vocabulary from conf text. A move into an adopter phase crosses
  no step exit and is admitted; a move out of one counts from the first step, as a move out of `PREFLIGHT`
  does (§8 F2). Observed by AC2.
- **S4** — The arms the `New arm:` lines in §7 declare: the adopter-phase readings among the cases
  `loop_table.py check --selftest` runs, and the adopter-phase observations of the `driver-plan` plant of
  `tools/loop/breakpoints.py`, whose scratch `.unattended.conf` gains `PHASES_EXTRA="STAGING"` (§8 F3).
  Observed by AC1, AC2.
- **S5** — The carriers. The `script:{prefix}/loop/loop_table.py#phase` row of `tools/govkit/usage.toml`
  gains the flag `--extra=`, and `help/loop.md`'s phase-map section gains one sentence on an adopter phase
  and one `--extra` command in its example block, its anchor re-stamped. Observed by AC3.

## 3. Non-goals (OUT)

- The `[[phase]]` check's population, `check_transition_tables` joining over the driver's set: the
  audit's id 35, batched into `TOOL-dDeclaredLoop-67`.
- An overlay through which an adopter maps its own phases to states and steps: no clause names one, and
  an unmapped phase reading as ungated is the defined default the finding asks for.
- The default of `extra` for the callers the driver does not start: `TOOL-dDeclaredLoop-70`'s.
- A `--plan` line printing a phase reading: the rev-2 text asked for one, but `--plan` prints the breakpoint
  lines of `TOOL-dDeclaredLoop-19` S9 and no phase reading, and the `phase` verb prints the reading on ask.
- The protocol sentence in `tools/unattended/PROTOCOL.template.md` and its render: `TOOL-dDeclaredLoop-75`
  S25 lands §5's text.
- `tools/loop/README.md` restating the flag: the usage row and the help page own the verb's flags.
- A checklist entry that a reader of a configurable vocabulary reads the owner's resolved answer, the
  finding's left-shift: the class is recorded at the close; S4 is this reader's adopter fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-52` — `derive_phase_position`, `derive_crossed_exits`, the `loop_table.py phase` verb and its `--phase` consumer `check_phase_gates`, whose reading of an unmapped phase this unit defines
- **hands-off** `TOOL-dDeclaredLoop-67` — the adopter-phase reading, whose population that unit's check of the phase rows matches (id 35)
- **hands-off** `TOOL-dDeclaredLoop-70` — the default of `extra`, which that unit makes the driver's population for every caller (the round-3 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-75` — §5's protocol sentence in the template and its render (the round-3 spec audit's id 35); this pass keeps the `loop transition tables` leg green (id 31)

## 4. Design

### Evidence

Every claim below was read at the tip of branch `unattended-declared-loop-d56bf0`, `fc947748`, in a scratch
export of that tree; the worktree this spec was written in is cut from main, which holds no loop kit.

- `tools/unattended/unattended.sh#phases` prints `PHASES_CORE` and `PHASES_EXTRA`; `#PHASES_CORE` holds 13
  members PINNED, read 2026-11-16 and re-derived by §5 "The sweep". `#load_driver_conf` sets `PHASES_EXTRA`
  blank on its init line before it sources the conf; the key is among `optional_keys` of
  `tools/unattended/kit.toml`, and gov's `.unattended.conf` sets it blank.
- `tools/unattended/unattended.sh#verb_phase` is the one reader of `phases()` in the driver: it refuses a
  phase outside it with `fail 19`. No driver verb prints the set, so the consumer passing the variable it
  already holds is the one read that is the owner's.
- `tools/unattended/unattended.sh#run_budget_verb` joins each value to its flag, so an opening `-` is never
  read as a flag; `TOOL-dDeclaredLoop-19` S10 extracts `run_loop_verb` from it unchanged.
- `tools/loop/loop_table.py#main` parses `move` and `check` through `argparse` and holds no `phase` verb at the
  tip; its `check --selftest` runs a list of cases through `tools/loop/loop_lib.py#run_selftest_cases`.
- `[[step]]` rows of `tools/loop/loop.toml`: `step.plan` to `step.deploy`, orders 1 to 5 PINNED, exits
  `item.plan.exit`, `item.design.exit`, `item.build.exit`, `item.test.exit` and `item.deploy.close`.
- `TOOL-dDeclaredLoop-52` rev-3 §4, read on its committed spec: `derive_phase_position(phase, facts,
  phase_map=None)` raises `LookupError` for a phase with no row; `derive_crossed_exits` reads a `from_step` of
  `none` as order 1 and answers `[]` for a `to_step` of `none`; the verb prints `phase <PHASE> · state <state> ·
  step <tag|none>`, then `· to <PHASE> · crosses <tags|none>` with `--to`, and `refused — phase <PHASE>: no
  row`, exit 1; `check_phase_gates <slug> <from> <to>` calls `run_loop_verb loop_table.py phase
  --from=<from> --to=<to>`, returns 0 on `crosses none`, and refuses through `fail 82` on the verb's refusal or
  a held owner gate at a crossed exit.

### The reading

| Phase | Row | Answer |
|---|---|---|
| one the map holds a row of | its row | the row's state and step, as `TOOL-dDeclaredLoop-52` reads it |
| a member of `extra` with no row | none | `state none · step none · adopter phase` |
| neither | none | refused by name, exit 1 |

```
derive_phase_position(phase, facts, phase_map=None, extra=())
  as TOOL-dDeclaredLoop-52 §4 "The reader", where it finds no row of `phase`:
  phase in extra   -> ("none", "none")
  otherwise        -> LookupError naming the phase
```

`extra` is any iterable of phase names, read by membership. A move into an adopter phase reads `to_step`
`none`, so `derive_crossed_exits` answers `[]`; a move out reads `from_step` `none`, so it counts from the
first step. Neither needs code here: both are `TOOL-dDeclaredLoop-52`'s crossing rule over the answer above.

### The verb

```
python loop_table.py phase --from <PHASE> [--to <PHASE>] [--fact k=v]... [--extra "<phases>"]
phase STAGING · state none · step none · adopter phase                                      exit 0
phase REVIEWING · state designing · step step.design · to STAGING · adopter phase · crosses none
phase STAGING · state none · step none · adopter phase · to BUILDING · crosses item.plan.exit item.design.exit
refused — phase STAGNG: no row                                                              exit 1
```

`--extra` defaults to the empty string and is split on whitespace. The marker follows the reading it
qualifies: after `step none` for `--from`, after `to <PHASE>` for `--to`. It prints where `extra` names the
phase and the map holds no row of it, which is exactly where the reader answered from `extra`. Every line
`TOOL-dDeclaredLoop-52`'s verb prints for a core phase is byte-identical, and `crosses` stays last, the field
`check_phase_gates` reads.

### The consumer

```
check_phase_gates <slug> <from> <to>
  run_loop_verb loop_table.py phase "--from=$from" "--to=$to" "--extra=$PHASES_EXTRA" >/dev/null
```

One argument on `TOOL-dDeclaredLoop-52`'s call, spelled through that unit's named locals; nothing else in
the function moves. A blank `PHASES_EXTRA` passes `--extra=`, which reads no adopter phase.

### The arms

The selftest of `loop_table.py check --selftest` gains five cases, each through the verb: `--from STAGING
--extra STAGING`; `--from STAGNG --extra STAGING`, exit 1; `--from REVIEWING --to STAGING --extra "STAGING
QA"`; `--from STAGING --to BUILDING --extra STAGING`; and `--from REVIEWING --extra REVIEWING`, which reads
the row and prints no marker.

The `driver-plan` plant of `tools/loop/breakpoints.py` appends `PHASES_EXTRA="STAGING"` to its scratch
repository's `.unattended.conf` where it writes that conf, opened with `encoding="utf-8"`, and after
`TOOL-dDeclaredLoop-52`'s phase observations it calls the sourced driver's `check_phase_gates tPos REVIEWING
STAGING` and `check_phase_gates tPos STAGING BUILDING`. Only `phases()` and this call read the key, so no
other observation of the plant moves.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `extra` | parameter of `derive_phase_position` | none |
| `--extra` | flag of the `phase` verb | none |

No function, constant, plant or driver variable is minted.

### Files touched (estimate)

- `tools/loop/loop_table.py`
- `tools/loop/breakpoints.py`
- `tools/unattended/unattended.sh`
- `tools/govkit/usage.toml`
- `help/loop.md`

### Alternatives rejected

- **Parsing `PHASES_EXTRA` out of `.unattended.conf` in Python.** It derives a second time a value the driver
  composes by sourcing the conf, the two-readers class the finding names.
- **A new driver verb printing `phases()`.** A public surface no clause of this build names; the consumer
  already holds the value.
- **Passing `$(phases)` whole.** A fork spent on a value the shell holds, and every core member read as
  extra only to be overruled by its row.
- **The reader answering a third field.** It moves the pair `TOOL-dDeclaredLoop-56` S18, `-67` S13 and `-70`
  read; the verb can tell the marker from the map it already holds.

## 5. Production-readiness checklist

- security — a move into an adopter phase is admitted, as it is before `TOOL-dDeclaredLoop-52` lands; a move
  out of one is held at every unreleased owner gate from the first step on (§8 F2), so an adopter phase is no
  path around a gate; the owner gates of core phases are unchanged.
- perf / scale — one more argument on one call; five in-process selftest cases and two sourced calls in a
  plant that already starts the driver.
- error / empty / loading states — a blank `PHASES_EXTRA` passes `--extra=` and changes nothing; a phase in
  neither set is refused by name, as today.
- observability — the `phase` verb prints `adopter phase` beside the reading it qualifies.
- risks — an adopter phase spelled like a core phase is a core phase: the row wins, and the driver's own
  membership test has the same rule.
- testing — AC1 and AC2 through the arms under §7, observed RED then GREEN at the close; AC3 a docs probe.
- migration — none: the parameter defaults to the empty set, the reading `TOOL-dDeclaredLoop-52` ships.
- user docs — `help/loop.md` gains the sentence and the command below; `TOOL-dDeclaredLoop-75` S25 lands
  the same sentence in the unattended protocol and its render:

```
An adopter phase, a member of PHASES_EXTRA, has no row in the loop kit's phase map: it reads state none and
step none, a move into it crosses no step exit, and a move out of it counts from the first step, as a move
out of PREFLIGHT does.
```

### The sweep

| Changed | Population | What keeps it green |
|---|---|---|
| `derive_phase_position` gains `extra` | `TOOL-dDeclaredLoop-52`'s verb and selftest; `TOOL-dDeclaredLoop-56` S18's `read_withdrawn_parents` and `TOOL-dDeclaredLoop-67` S13's held-from lookup, each calling without it | a keyword after `phase_map` defaulting to the empty set, so every call answers as `TOOL-dDeclaredLoop-52`'s reader does |
| the `phase` verb's `--extra` and its marker | `check_phase_gates`' read of the line; the selftest's core-phase cases | the marker prints only for a phase answered from `extra`; `crosses` stays last |
| `check_phase_gates`' call gains one argument | `verb_phase`; the kit gate's checks 39, 40 and 48; the `--phase` arms of `tools/unattended/unattended.test.sh` and `tools/unattended/runlog-writer.test.sh`; the harness arms leg | no fact read or written and no message added; gov's conf sets the key blank, so every reading is `TOOL-dDeclaredLoop-52`'s; the copied driver of `runlog-writer.test.sh` has no loop kit beside it and reads nothing |
| the `driver-plan` plant | `TOOL-dDeclaredLoop-19`'s leg `loop breakpoint fixtures` and its row in `tools/run-gates/selftest-budgets.txt`; that unit's AC8 and `TOOL-dDeclaredLoop-52`'s AC5 over the same plant | only `phases()` and this call read the key; the row is re-priced by that file's rule only if the timed run passes it |
| the usage row's flags | the `docs` leg's anchor join and command test; `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix` and `recall floor arms`, whose guards name `tools/govkit/` | the anchor re-stamped with the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints; the page's `--extra` command names declared flags alone |
| `help/loop.md` | `docs`, `help page commands` | the command sits in `TOOL-dDeclaredLoop-52`'s block, which carries `<!-- run: no -->` |
| shipped bytes | `install-prefix (shipped surface)` | no line names a path under the install prefix |
| the census and the families | `tools/memory-tree/check-arms.py`'s readers over the driver; `tools/unattended/unattended.families.txt` | no `fail` site and no message is added or edited |
| new names | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at `fc947748` | no function name is minted |
| shared records | `SHARED_RECORDS` in `.unattended.conf` | the pass writes neither `memory/DECISIONS.md` nor `memory/project/readme-contract.txt`; no decision row is owed |
| the kickoff manifest | `watch:` of `memory/guides/SESSION-KICKOFF.md` | no watched path is edited, so no re-stamp |
| subject pins, epoch delegates, upgrade rows, the registry | `tools/govkit/subject-pins.tsv`, `tools/memory-tree/check-verdict-epoch.sh`'s `DELEGATES`, `[[upgrade]]`, `tools/govkit/registry.toml` | no leg added, no memory-tree module edited, no migration, no kit added |
| the codebase map | `codebase-map coverage + freshness` | `memory/map/generated/symbols.json` records a function's id, kind and file, and no symbol is minted, so nothing regenerates |
| this spec's citations | `positional (the citation check alone)`; `memory/project/positional-refs.txt`'s two rows of this spec | this revision cites by symbol; the commit landing it runs `python tools/playbook/positional.py shrink` |
| other units | `TOOL-dDeclaredLoop-70` §4's callers table names a `--plan` adopter reading and its AC1 the rev-2 verb form; `TOOL-dDeclaredLoop-75` S25 and AC25; `TOOL-dDeclaredLoop-67` S23 | unit 70 re-grounds on this revision at order 36; S25's sentence is §5's; S23 reads the population, not this reader |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:tools/unattended/unattended.sh" | grep '^PHASES_CORE="' | wc -w                    # 13
git show "$B:tools/unattended/unattended.sh" | grep -c '\$(phases)'                             # 1
git show "$B:tools/unattended/unattended.sh" | grep -c 'PHASES_EXTRA'                           # 3
git show "$B:.memory-tree.conf" | grep -o 'unattended/unattended.sh:[0-9]*:[0-9-]*:[A-Za-z0-9-]*'
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN='
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-63.md'     # 2
```

### Budgets and records

- The driver's census, read through `tools/memory-tree/check-arms.py#branches` and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` over the scratch export, is 340 PINNED at `fc947748`,
  335 branches and 5 sites PINNED; `TOOL-dDeclaredLoop-19` raises it to 342 PINNED and
  `TOOL-dDeclaredLoop-52` to 343 PINNED, each under its landed decision row. This unit adds no site, so the
  census and the ceiling stay where unit 52 leaves them.
- The families of `tools/unattended/unattended.families.txt` do not move: no message is added or edited.
- `tools/unattended/check-unattended.sh` stays at 266 of its 266 PINNED; it is not edited.
- `VERB_OFFENDER_PIN` stays 1215 PINNED: no name is minted.
- The shared records: the pass writes neither `memory/DECISIONS.md` nor
  `memory/project/readme-contract.txt`, and no decision row is owed ahead of it.
- Help anchors: `script:tools/loop/loop_table.py#phase` re-stamped on `help/loop.md`. No driver verb or
  flag is added, so no driver anchor.
- The loop and unattended kits' versions are owed at the lander.

### Dependency

Order 35, beside `TOOL-dDeclaredLoop-54` (rev-2), `TOOL-dDeclaredLoop-55` (rev-2) and `TOOL-dDeclaredLoop-64`
(rev-3), each read on its committed spec. Unit 54 also edits `tools/loop/loop_table.py`, its terminal sets
and `read_terminal_set`, a region this unit does not touch; where both append selftest cases, the second to
land rebases. Unit 64 also edits `tools/loop/breakpoints.py`, the README path of `read_breakpoints`, never
the `driver-plan` plant. Unit 55 edits `tools/gate-legs.json` and the loop kit's `kit.toml`, shared with
nothing here.

`TOOL-dDeclaredLoop-52` (order 34, rev-3) is read on its committed spec: the reader, the verb, the crossing
rule, `check_phase_gates` and its observations in the `driver-plan` plant, all of which land before this unit
builds. `TOOL-dDeclaredLoop-19` (order 33, rev-3, building) is read on its committed spec: `run_loop_verb`,
`breakpoints.py`, its `driver-plan` plant and the leg `loop breakpoint fixtures`. `TOOL-dDeclaredLoop-33`
(rev-6) and `TOOL-dDeclaredLoop-53` (rev-3), order 34, edit `help/loop.md`, `tools/govkit/usage.toml` and
`breakpoints.py` elsewhere and add no `[[phase]]` row. Units through order 32, and units 50, 51 and 22, are
CLOSED, read on landed code at `fc947748`; `TOOL-dDeclaredLoop-34` is deferred against ask
TOOL-dDeclaredLoop-113 and shares no file. The code reads, the census and the reuse probe ran in a scratch
export of the branch tip; the counts above ran through `git show` of the branch.

## 6. Acceptance criteria

Each `python loop_table.py` command below runs in the loop kit's folder; every other command runs at the
top of the repository.

- **AC1** — When `python loop_table.py phase --from STAGING --extra STAGING` runs, it prints `phase STAGING ·
  state none · step none · adopter phase` and exits 0; `--from STAGNG --extra STAGING` exits 1 printing
  `refused — phase STAGNG: no row`; `--from REVIEWING --to STAGING --extra "STAGING QA"` ends `· to STAGING ·
  adopter phase · crosses none`; `--from STAGING --to BUILDING --extra STAGING` ends `crosses item.plan.exit
  item.design.exit`; and `--from REVIEWING --extra REVIEWING` prints `phase REVIEWING · state designing ·
  step step.design` with no marker.
  Red when: the map is the whole population, so `STAGING` is refused for lacking a row.
- **AC2** — When `python breakpoints.py --fixture --plant driver-plan` runs, it prints `held`, its scratch
  `.unattended.conf` setting `PHASES_EXTRA="STAGING"`: the sourced driver's `check_phase_gates tPos REVIEWING
  STAGING` returns 0, and `check_phase_gates tPos STAGING BUILDING` returns 1 printing `UNATTENDED check 82
  FAILED` and naming `item.design.exit`.
  Red when: the consumer omits `--extra`, so the loop kit refuses the adopter's phase and the first call
  returns 1 naming `STAGING`.
  cost: the driver in a scratch repository, about a minute.
- **AC3** — When `python tools/govkit/docs_leg.py --fingerprints` runs, the row for `loop_table.py#phase`
  names `help/loop.md` among its pages; and `grep -c -- '--extra' help/loop.md` and `grep -c '"--extra="'
  tools/govkit/usage.toml` each print at least 1.
  Red when: the flag ships with the row unchanged, so the page's `--extra` command names an undeclared flag.

## 7. Gates

`loop transition tables` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `scratch-guard self-test` · `tier2-review self-test` · `docs` · `help page commands` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `lexicon naming predicates` · `positional (the citation check alone)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted leg `loop breakpoint fixtures` (`TOOL-dDeclaredLoop-19` S12), which runs AC2's plant, is
kept green too; it is outside the base manifest the leg line is joined against.

New arm: tools/loop/loop_table.py · covers AC1 · the five adopter-phase cases among the selftest's, staged against `TOOL-dDeclaredLoop-52`'s verb, which takes no `--extra` and refuses a phase with no row · none

New arm: tools/loop/breakpoints.py · covers AC2 · the `driver-plan` plant's adopter-phase calls, staged against `TOOL-dDeclaredLoop-52`'s `check_phase_gates`, which passes no `--extra` · none

The unattended kit's own suites are waived for this build's landing by the build README's suite waiver;
AC2 is observed through the loop kit's plant instead.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — What does a move out of an adopter phase cross?** Options: (a) as a move out of `PREFLIGHT`, every
  exit from the first step to the target's, `TOOL-dDeclaredLoop-52`'s rule for a stepless start, unchanged;
  (b) none, the adopter phase read as already past every gate. (b) lets a run step from `REVIEWING` into an
  adopter phase and out into `VERIFYING` with the design and build gates never read, a path around the hold.
  Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 1, unit 52's committed reading
  of a stepless start.
  widens: none · relaxes: none
- **F3 — Where is the driver's consumer observed?** Options: (a) the `driver-plan` plant of
  `tools/loop/breakpoints.py`, which already sources the driver for unit 52's hold, run by a loop kit leg;
  (b) an arm in `tools/unattended/unattended.test.sh`, waived for this build's landing; (c) a one-off scratch
  probe, no lasting arm. (b) and (c) leave the class ungated at the close. Recommendation: (a). RESOLVED
  (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 56 (HIGH, item H8).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-70 and TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-16 · §1 to §10 · S1 to S5 · AC1 to AC3 · §8 F2 F3 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `fc947748`, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-63-1-spec-writer`: symbol citations; the reader and verb on unit 52's
  rev-3 signature, `phase --from` form and exit 1 refusal; the consumer is unit 52's `check_phase_gates`
  through unit 19's `run_loop_verb`, not unit 19's S6; the move out of an adopter phase (F2); the plant
  `phases-extra` becomes selftest cases and `driver-plan` observations (F3); the `--plan` reading leaves scope,
  since `--plan` prints no phase; the usage row, help anchor and protocol sentence text; the sweep.

## 10. Reuse audit

The seams this unit extends: `TOOL-dDeclaredLoop-52`'s `derive_phase_position`, `phase` verb and
`check_phase_gates`, each in place; the driver's `phases()` (`tools/unattended/unattended.sh#phases`) and the
`PHASES_EXTRA` value its consumer already holds; `TOOL-dDeclaredLoop-19`'s `run_loop_verb` and `driver-plan`
plant; and the selftest's cases through `tools/loop/loop_lib.py#run_selftest_cases`.

`python tools/codebase-map/reuse_lookup.py "an adopter phase with no row reads ungated, the driver passing its
extra phases to the loop kit's phase reader"`, run in a scratch export of the branch tip `fc947748`, ranked
name-stem neighbours (`rows`, `read_text`, `resolve_kit_dir`), the driver's `phases`, the composer this unit
reads, and `read_definition` (`tools/loop/loop_lib.py#read_definition`), the definition read the phase map
sits on; no existing seam reads an adopter's phase.

Recall terms used: PHASES_EXTRA PHASES_CORE phases adopter phase map derive_phase_position loop_table check_phase_gates --phase gated step crossed exits
