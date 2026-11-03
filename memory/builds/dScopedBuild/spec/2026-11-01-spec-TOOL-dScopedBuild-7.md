# TOOL-dScopedBuild-7 — the core checks run by the executor at Build's exit: the exit's graded legs narrowed to the core set, a core-only run of its own, its result recorded

**Status:** DEFERRED · rev-4 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 9 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0405@431edacd whole
**Carries:** node:item.build.core
**Carries:** node:record-kind.core-result
**Carries:** node:item.build.distill

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-6 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-7-deviation-71.md](../build/2026-11-01-build-TOOL-dScopedBuild-7-deviation-71.md) | deviation | — |
| [2026-11-01-build-TOOL-dScopedBuild-7-deviation-72.md](../build/2026-11-01-build-TOOL-dScopedBuild-7-deviation-72.md) | deviation | — |
| [2026-11-01-build-TOOL-dScopedBuild-7-deviation-73.md](../build/2026-11-01-build-TOOL-dScopedBuild-7-deviation-73.md) | deviation | — |
| [2026-11-03-build-TOOL-dScopedBuild-1-crosscheck-returns.md](../build/2026-11-03-build-TOOL-dScopedBuild-1-crosscheck-returns.md) | research | TOOL-dScopedBuild-1 |
| [2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck.md](../build/2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck.md) | research | TOOL-dScopedBuild-1 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-03-prompt-TOOL-dScopedBuild-1-parents-crosscheck.md](../prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-crosscheck.md) | research | TOOL-dScopedBuild-1 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dScopedBuild-1 gives both modes one exit, `check_build_exit`, refusing a red the build's own
commits introduced on every leg until a core set exists (its §8 F1). This unit supplies that set, the
legs whose `enforces` names a principle, narrows the exit's refusal to them, lets an admitted exception
excuse one, and gives the executor `build.core`: a core-only bar in a call of its own, because
`--close` scrubs `GATE_LEGS` from its bar (`unattended.sh:11157-11169`), whose verdict it records and
whose own reds it routes to fix units.

## 2. Scope (IN)

- **S1** — The core set, I18: the rows of the gate-leg manifest whose `enforces` is non-empty
  (PLAY-dOrderedCharter-7 S2), derived at each call by `derive_core_manifest` in
  `tools/unattended/unattended.sh`, which writes those rows, unchanged and in manifest order, to
  `<git dir>/gate-run/<run id>.core-legs.json` and sets `BX_CORE_LEGS` to their names. The manifest is
  the bar's own default, the `gate-legs.json` beside the run-gates kit
  (`tools/run-gates/run-gates.sh:252`), the kit found by the library's
  `resolve_kit_dir "$py" run-gates run-gates.sh "$KIT_DIR"`. No `core` tag or chunk is minted. No
  such row leaves `BX_CORE_LEGS` empty: the core set is `not-installed`. Observed by AC1 and AC2.
- **S2** — The exit's core arm, inside TOOL-dScopedBuild-1's `check_build_exit` (I2). Where the core
  set is installed, its `GR_STATE` `other` row refuses only for a `GR_OWN` leg (TOOL-dScopedBuild-1 S3)
  that is in `BX_CORE_LEGS` and that no admitted exception excuses; a `GR_OWN` leg outside the set
  prints `build-exit: <leg> red at <HEAD8>, own, not a core leg` and does not refuse; an excused one
  prints `build-exit: <leg> excepted — <record stem>`. An exception is admitted when `core.py
  exceptions` (PLAY-dOrderedCharter-7 S9, under `core.exceptions`) names a record whose `Excuses` is
  the leg and whose `Principle` is one of the leg's `enforces`. The arm sets `BX_CORE`, the verdict
  of §4 "The verdict", for S3's record. Not installed, unit 1's table and its not-installed line stand
  unchanged. Because `--close`'s `build-complete` term and `--build-exit` both call this function, the
  narrowing holds in both modes. Observed by AC2, AC3, AC4 and AC5.
- **S3** — `build.core`, `run_build_core <slug>` behind the driver verb `--build-core <slug>`. It
  observes R through `observe_anchor` (`:1974`), as `--build-exit` does, pins a run id, and runs
  `$GATE_CMD` once with `GATE_LEGS` naming S1's file, `GATE_ATTRIBUTE` R, `GATE_RUN_ID` and
  `GATE_FULL=1`, so no leg guard skips a core leg; it then calls `check_build_exit` over that run, so
  the core run and the exit read a red one way. Not installed, it runs no bar. It reads no run-state
  file. A tip whose newest core result already graded it is not re-run: the verb prints that record
  and exits 0, which is what makes its adapter row `idempotent`. Exit 0 on a written or reprinted
  result, 1 when `check_build_exit` refused the run as unusable (`GR_STATE` `none` or `moved`, or no
  rc it reads), 2 on a refusal before the bar. Observed by AC1, AC2 and AC6.
- **S4** — The route. For each core leg S2 refuses, one ask in the build's `BACKLOG.md` through
  `derive_ask_seq` and `write_ask_rows` (`:9780`, `:9984`), I20, as `write_inherited_asks` (`:10020`)
  writes one: subject `CORE LEG <leg> RED, OWN AT <R8>`, accept `<leg> green at the build's tip,
  attributed against the advertised tip`. The ask is the fix unit's way in through Design
  (`flow-steps.md:298`). A run files no ask for a leg an open ask already names. Observed by AC3.
- **S5** — `record-kind.core-result`, the executor-written result: a `core-result` kind registered in
  PLAY-dOrderedCharter-7 S7's factory `tools/memory-tree/build_records.py` and written through its
  `new` verb as `<date>-build-<first roster unit>-core-result-<n>.md` in the build's `build/` folder,
  named for the first roster unit as this build's own scout records are, with
  `**Serves:** journal <every roster unit>` and §4 "The record"'s fields. Observed by AC1 and AC6.
- **S6** — The executor's row: an `[[adapter]]` in `tools/runtime/points.toml` at
  `point = "point.command-adapters"`, `name = "build.core"`, `class = "idempotent"`, its `run` the
  `--build-core` verb, so the supervisor runs Build's `build.core` item through it
  (TOOL-dWellOiledMachine-6 S8). Observed by AC7.
- **S7** — `item.build.distill`'s rows in the range. The record's `**Decision rows:**` field counts
  the lines `git diff <BX_BASE>..<tip> -- memory/DECISIONS.md` adds, `BX_BASE` the base
  `check_build_exit` derives (TOOL-dScopedBuild-1 S4, from `read_first_passes`), so the record shows
  the core run graded a tree holding them (`flow-steps.md:298`, "the decision-log rows included").
  The appender that writes those rows is §8 F3's ask. Observed by AC6.
- **S8** — The verbs guide: `tools/unattended/VERBS.template.md`, copied to
  `memory/guides/UNATTENDED-VERBS.md`, states `--build-core`, its five verdicts and exit codes, and
  the core arm of `--build-exit`'s entry. Observed by AC8.

## 3. Non-goals (OUT)

- Marking legs core: PLAY-dOrderedCharter-7 S2's `enforces` and its meta-check.
- The exception register, its door and what `core.exceptions` admits: PLAY-dOrderedCharter-7 S8 and
  S9. This unit reads `core.py exceptions` and admits nothing itself.
- The executor, its beat and its adapter contract: TOOL-dWellOiledMachine-6 S1 and S8.
- The exit function, its base, `GR_OWN`, the attended Skill's last stage and the `--close` term:
  TOOL-dScopedBuild-1. This unit adds one arm to the function and one verb beside it.
- The decision-log appender `build.distill` names (`flow-steps.md:297`): §8 F3.
- The whole bar `gates-green` runs, and the whole bar `--build-exit` runs: unchanged; S2 narrows what
  their reds refuse, not which legs they run.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — `read_first_passes`, the history-derived base behind `BX_BASE`, which S7 counts the decision rows from
- **consumes-from** `TOOL-dScopedBuild-1` — `--build-exit` and `check_build_exit`, with `GR_OWN`, the exit whose graded legs S2 narrows; without it no exit reads a core red
- **consumes-from** external — PLAY-dOrderedCharter-7's `enforces` (S2), `build_records.py` (S7) and `core.py exceptions` (S9); TOOL-dWellOiledMachine-6's `point.command-adapters` (S8)
- **hands-off** external — the `build.distill` appender, filed as an ask for this build (§8 F3)
- **consumes-from** `TOOL-dScopedBuild-32` — S3's bar call, spelled `run_gate_bar "build-core" "$R" "<core legs file>" -- GATE_FULL=1`, the core manifest an argument rather than an inherited `GATE_LEGS`; without it the core run grades whatever manifest the main loop exported (id 22)
- **hands-off** `TOOL-dScopedBuild-31` — S5's `core-result` record, whose kind that unit registers through the record-kind factory and binds `**Serves:** core-result` (id 20)
- **hands-off** `TOOL-dScopedBuild-35` — S3's run over the red reading alone, S1; S4's asks through `write_gate_asks`, S11; S8's verb wiring, S13; its new functions in `symbols.json`, S17; the asks' log prefix, S34; and AC4's and AC5's fixture, S2 (ids 4, 26, 28, 33, 8, 5)
- **hands-off** `TOOL-dScopedBuild-39` — S5's `core-result` registration, which this unit's builder makes as the per-kind row and the `TYPED_RECORD_KINDS` member together, in TOOL-dScopedBuild-31 S2's spelling, as that unit's S8 rules (id 5)
- **hands-off** `TOOL-dScopedBuild-41` — S5's `TYPED_RECORD_KINDS` member, for which this unit's builder adds `tools/memory-tree/tree_lib.py` to its Files touched and `policy fixtures` to its §7 by a rev bump before building, as that unit's S9 rules (id 18)

## 4. Design

### The run

```
--build-core <slug>
  R = observe_anchor            tip = HEAD
  a core result whose tip is HEAD exists      -> print it, exit 0                     (idempotent)
  derive_core_manifest                         -> empty: no bar; check_build_exit sees not-installed
  GATE_LEGS=<core file> GATE_ATTRIBUTE=R GATE_RUN_ID=<id> GATE_FULL=1 $GATE_CMD        (its own call)
  check_build_exit <slug> R <rc> <run dir>     -> BX_BASE, BX_CORE, the exit's lines   (S2)
  an ask per refused core leg (S4); write the result (S5)
```

Which commits are the build's is `BX_BASE`'s answer and whose red it is R's, never one base for both
(scout A disagreement 1, `run-gates.sh:4349-4353`): a red refuses when it reads OWN at R, its leg is
core and no exception excuses it.

### The verdict

| Row | When | `BX_CORE` | Refuses |
|---|---|---|---|
| 1 | `BX_CORE_LEGS` empty | `not-installed` | as unit 1's table says |
| 2 | bar rc 0 | `clean` | no |
| 3 | `GR_STATE` `land` | `inherited` | no |
| 4 | `GR_STATE` `other`, every core `GR_OWN` leg excused, or none core | `excepted` | no |
| 5 | `GR_STATE` `other`, a core `GR_OWN` leg unexcused | `own-red` | yes |

An unusable record (`moved`, `none`) is unit 1's refusal and writes no result.

### The record

```
# <first roster unit> core result <n> — <slug> at <tip8>

**Serves:** journal <every roster unit id>

- **Range:** <BX_BASE>..<tip sha>
- **Attributed:** <R sha>
- **Bar:** <run id> | none
- **Core:** <n> leg(s) · <names, comma-joined> | not-installed
- **Verdict:** clean | inherited | excepted | own-red | not-installed
- **Reds:** <leg> · <attribution verdict> · <excepted <record stem> | ask <ask id> | not core | inherited>; … | none
- **Decision rows:** <n>
```

`Reds` is one field, its entries `;`-separated, because the factory's `read_record` refuses a field
written twice (PLAY-dOrderedCharter-7 S7). `Serves` is `journal`, a kind `memory/HYGIENE.md` already
closes over ("evidence of what was built"), so no binding kind is minted.

### Inventory

| Name | What | Cell |
|---|---|---|
| `run_build_core` | shell function, `unattended.sh` | `sh.function`, answered OK |
| `derive_core_manifest` | shell function, `unattended.sh` | `sh.function`, answered OK |
| `--build-core` | driver verb | none |
| `BX_CORE`, `BX_CORE_LEGS` | `check_build_exit` output variables | none |
| `core-result` | record kind in `build_records.py` | none |

### Rollout

Live at landing, dark in effect: until PLAY-dOrderedCharter-7 marks a leg, S1 finds no core leg, the
exit keeps unit 1's every-leg reading and `--build-core` records `not-installed`; the first leg to
carry `enforces` arms it with no change here. Build-run preconditions (§8 F4): TOOL-dScopedBuild-1's
`check_build_exit` and `--build-exit`, PLAY-dOrderedCharter-7's `build_records.py` and `core.py`, and
TOOL-dWellOiledMachine-6's `points.toml` for S6's row.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md` (copy of the template above)
- `tools/runtime/points.toml`
- `tools/memory-tree/build_records.py`

### Alternatives rejected

- Narrowing `--close`'s own bar to the core legs. Rejected by `unattended.sh:11157-11169`: the close
  scrubs `GATE_LEGS` because its green is recorded as the whole bar's, so a narrowed call would
  certify a subset as the bar.
- A second verdict reader in `--build-core`. Rejected by I3 and unit 1's one contract: the core run
  calls `check_build_exit`, so the record and the exit cannot disagree on a red.
- A `core` chunk or tag. Rejected by PLAY-dOrderedCharter-7 §8, which rejected "a new `chunk` value
  for core legs" for `enforces`, and by I18's one spelling.
- Reading the exception records with a parser of this unit's own. Rejected by PLAY-dOrderedCharter-7
  S9, which makes `core.py exceptions` the reader of what `core.exceptions` admits.

## 5. Production-readiness checklist

- security — no new write surface beyond a record in the build's own folder and an ask row through
  the landed ask writer.
- perf / scale — one bar over the core legs only, once per tip; a re-run at the same tip costs a read.
- error / empty / loading states — no core leg: `not-installed`; an unusable bar record: exit 1 and no
  result; no exception reader: no leg is excused, and the line says why.
- observability — the record names range, R, the run id, every red and its route.
- risks — a core leg the build breaks that is already red at R reads INHERITED and does not refuse:
  unit 1's rule and `gates-green`'s limit, stated here because the core arm inherits it.
- testing — the driver suite's new arms (§7), a stubbed `GATE_CMD` writing each planted run record.
- migration — none: no conf key, and the exit is unchanged until a leg carries `enforces`.
- user docs — the verbs guide (S8); `help/roles.md`'s exit line is unit 1's.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --build-core` runs over a fixture build whose
  manifest carries no `enforces` row, it runs no bar, exits 0 and writes a `core-result` record whose
  `Verdict` is `not-installed` and whose `Bar` is `none`.
  Red when: a bar runs over an empty core set, or the empty set reads `clean`.
  fixture: a scratch repository under `%TEMP%` with one roster unit, a manifest and a stub `GATE_CMD`.
- **AC2** — When the AC1 manifest gives leg `L` a non-empty `enforces` and the stub records `L` red,
  `OWN` at R, `--build-core` prints `own-red`, the stub saw `GATE_LEGS` naming a file holding `L`'s
  row alone, and the record's `Reds` reads `L · OWN · ask` followed by the filed id.
  Red when: the core run grades the whole manifest, or an own core red is not recorded.
- **AC3** — When the AC2 case runs, the build's `BACKLOG.md` gains one ask naming `L` and R's first
  eight hex digits, and a second run at a new tip with `L` still red files none.
  Red when: an own red routes nowhere, or a rerun duplicates the ask.
- **AC4** — When `bash tools/unattended/unattended.sh --build-exit` runs over the AC2 case, it refuses
  naming `L`; with `L` red and own but a second leg `M` the only core leg, it passes printing
  `not a core leg`; with a planted exception record whose `Excuses` is `L` and whose `Principle` is
  `L`'s `enforces` tag, it passes printing `excepted`.
  Red when: an own core red passes the exit, or an own red on a non-core leg, or an excused one, holds it.
  fixture: PLAY-dOrderedCharter-7 S9's `core.py exceptions` landed; the build run's precondition.
- **AC5** — When the stub records `L` red and `INHERITED` at R, `--build-core` prints `inherited` and
  `--build-exit` passes; with no `enforces` row, an own red on any leg still refuses the exit, as unit
  1's table states.
  Red when: an inherited red holds the exit, or an uninstalled core set stops grading own reds.
- **AC6** — When `--build-core` runs twice at one tip, the second run prints the first record and the
  stub counts one bar; the record's `Range` starts at the sha `routed_commits.py --build-base` prints,
  and its `Decision rows` counts the lines the range adds to `memory/DECISIONS.md`.
  Red when: a rerun at the same tip runs a second bar, or the range starts anywhere but I1's base.
- **AC7** — When `python supervise.py --check-adapters` runs over a `points.toml` holding S6's row, it
  passes the row, and with the row's `class` removed it refuses it.
  Red when: the executor's `build.core` row is not checked as a command adapter.
  fixture: TOOL-dWellOiledMachine-6 S8 landed.
- **AC8** — When `grep -n "build-core"` runs over `tools/unattended/VERBS.template.md` and its copy
  `memory/guides/UNATTENDED-VERBS.md`, each prints the verb's entry naming its five verdicts.
  Red when: the verb ships with no carrier stating it.

## 7. Gates

`unattended kit gate` · `pass-order history` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · a fixture build with a stub `GATE_CMD` writing a run record per planted case, its failing case an own red on a core leg passing `--build-exit` · none

## 8. Open questions

- **F1 — Where does the core narrowing live?** Options: (a) an arm of `check_build_exit`, which both
  `--build-exit` and `--close`'s term call, `--build-core` calling it too; (b) a reader of the
  core-result record at the exit; (c) a verdict of `--build-core`'s own. (b) and (c) are a second
  reading of a red beside unit 1's, the two-answers class, and (b) leaves `--close` without the
  narrowing until a record exists. TOOL-dScopedBuild-1's hand-off says its exit's "graded legs it
  narrows to the core set". Rung 1 for where, rung 3 among the survivors. RESOLVED (agent,
  2026-11-01, delegated): (a). widens: none · relaxes: none
- **F2 — The verb and its guide entry are a public surface and a governance carrier.** Options: (a)
  add `--build-core` and its verbs-guide entry under the README's grant, the clause naming the core
  checks at Build's exit; (b) a script outside the driver, reading `attribution` with a parser of its
  own. (b) breaks I3's one reader. Rung 3 with veto 2 lifted by the grant. RESOLVED (agent,
  2026-11-01, delegated): (a). grants: PLAY-dClosedLoop-3 the `--build-core` driver verb and its
  entry in the unattended verbs guide. widens: none · relaxes: none
- **F3 — `item.build.distill` names an appender** (`flow-steps.md:297`: a decision-log row per major
  resolved fork, as `decisions.major` says) **that TOOL-dLinkedLibrary-1 §3 hands to this build, and no
  clause of the row spells it.** Options: (a) build the appender here; (b) carry the item as the core
  run's coverage of the rows (S7) and file the appender as an ask for this build; (c) carry the node
  by name only. (a) puts a second mechanism in this spec (BUILD-METHOD M2); (c) leaves the hand-off
  silent. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (b), the ask for build dScopedBuild: "THE
  BUILD-DISTILL APPENDER HAS NO UNIT", accept "a unit of dScopedBuild appends a decision-log row per
  resolved fork its class makes major under `decisions.major`, keyed by build and fork id and skipped
  when present, seen red on a planted major fork with no row and on a second row for one key".
  widens: none · relaxes: none
- **FACT-QUESTION · F4 — Does PLAY-dOrderedCharter-7, which this unit calls and the packet does not
  list as a parent, land before this build?** Probe: `grep -m1 "^parents:"` over the READMEs of
  dWitnessedBar and dDeclaredLoop. Observation that decides: dOrderedCharter on a line of a build this
  build descends from. Liveness: a build on no such line prints nothing and is routed as a stand-in.
  Run at writing: dWitnessedBar names dDeclaredLoop, and dDeclaredLoop names dOrderedCharter.
  RESOLVED (agent, 2026-11-01, delegated): a build-run precondition, with S1's `not-installed` the
  state until a leg carries `enforces`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-31, TOOL-dScopedBuild-32, TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (id 5).
- rev-4 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-41,
  the promotions of the round-1 spec audit of units 36 to 39 (id 18).

## 10. Reuse audit

The seams extended are TOOL-dScopedBuild-1's `check_build_exit` (one arm) and `GR_OWN`; the
`gates-green` arm's bar call shape (`unattended.sh:11121-11200`: R from `observe_anchor`, a pinned
`GATE_RUN_ID`, `GATE_ATTRIBUTE`), which `--build-core` repeats for its own call as `--build-exit`
does; `GATE_LEGS`, the bar's manifest override (`run-gates.sh:252`); the ask writers `derive_ask_seq`
and `write_ask_rows` (`:9780`, `:9984`); and the library's `resolve_kit_dir`.
`reuse_lookup.py "run a subset of gate legs attributed against the advertised tip and read whose red
it is"` ranked name-token neighbours only (`read`, `run`, `legs`, `run_git`), an answer recorded
rather than retried. Scout A's rows agree with source at `5f0b11f12` but one: it reads `GATE_LEGS` as
"limited to the core rows", and the runner reads the variable as a manifest path, so S1 writes one.
No manifest row carries `enforces` at HEAD (144 rows, none with the key, counted at writing), so every
red case is planted.

Recall terms used: `python tools/memory-recall/query.py "how does the build exit run only the core checks and refuse an own red" --terms "core legs enforces gates-green attribution OWN INHERITED read_gates_record GATE_LEGS core.exceptions core-result executor"`
