# TOOL-aBriskPreflight-7 — preflight and the wiring check each declare a wall-clock ceiling and name a breach

**Status:** CLOSED · rev-3 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 4 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md](../build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 |
| [2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh](../build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh) | research | — |
| [2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log](../build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log) | research | — |
| [2026-10-11-build-TOOL-aBriskPreflight-7-ab-run.sh](../build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-run.sh) | research | — |
| [2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log](../build/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log) | research | — |
| [2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh](../build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh) | research | — |
| [2026-10-12-build-TOOL-aBriskPreflight-7-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aBriskPreflight-7-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-7-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-7-build-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-7-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-7-spec-brief.md) | research | — |
| [2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md](../reviews/2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md) | diff-review | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-10 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's item: cost becomes a verdict. Today the wiring check is killed only at the 3600 s
`GATE_BOUND` and preflight as a whole has no ceiling, so a slow run waits in silence. After this
unit the wiring check is killed at its own declared ceiling and check 4 refuses naming it, and a
preflight over its own declared ceiling prints a named breach line but still writes its record —
the owner's ruling "Name it, refuse only wiring", because a refused preflight costs a whole re-run.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.sh` declares three file constants, each a double-quoted
  whole number so `core_of` in `tools/unattended/check-unattended.sh` can read it the way it reads
  `REMOTE_BOUND` and `RUNAWAY_CEILING`. `WIRING_CEILING` and `PREFLIGHT_CEILING` are in seconds.
  `CEILING_SPAWN_MS` is the per-spawn cost, in milliseconds, that both were derived to tolerate. They
  are assigned on the lines after `read_bound_key GATE_BOUND`, which is after `. "$CONF"`, so a conf
  assigning any of the three names is overwritten and no conf channel exists. Each carries a comment naming its
  inputs as PINNED or DERIVED and naming this unit's id. Observed by AC2 and AC8.
- **S2** — The wiring child runs under the smaller of `WIRING_CEILING` and `GATE_BOUND`. A new
  `derive_wiring_bound` computes that bound and which of the two it is, fork-free, and both places
  that start the child call it: `init_preflight_probes`, which `TOOL-aBriskPreflight-4` adds, and
  the synchronous form `check_wiring` keeps for a start that could not capture. Each sets the bound
  through `RB_BOUND` around that one start and clears it on the next line, as the gates-green arm
  does at `tools/unattended/unattended.sh:10640`. `check_wiring` reads the kill where it reads it
  today. When the child was killed and the ceiling was the smaller bound, check 4 refuses with the
  wording in §4 "The refusal" and prints the captured output indented beneath it, as the existing
  kill branch does. When `GATE_BOUND` is the smaller or the equal bound, today's refusal fires byte
  for byte. Observed by AC1, AC3 and AC9.
- **S3** — The driver takes a fork-free start stamp, `DRIVER_T0_US`, right after `set -u`, its first
  statement, and marks it readonly so the sourced conf cannot move it. A new `print_preflight_breach` is called at
  the `--preflight` dispatch arm after `verb_preflight` returns, on every return path. It compares the
  elapsed wall with `PREFLIGHT_CEILING` and, when the wall is over, prints the line in §4 "The breach
  line" on stdout. It never calls `fail`, never sets `status`, adds nothing to `RUNLOG_CHECKS` and
  writes no file. Observed by AC4, AC5, AC6 and AC12.
- **S4** — A new `measure_spawn_cost`, called only on the two breach paths and at most once per
  driver process, times five spawns of the external `true` with the fork-free clock. It sets
  `SPAWN_COST` to whole milliseconds per spawn, or to an unmeasured phrase naming why. Both the
  refusal and the breach line print it beside `CEILING_SPAWN_MS`. Observed by AC1 and AC4.
- **S5** — On a host with no working `timeout -k`, a second NOTE, printed after the constants are
  assigned, names the wiring ceiling as inert too. The existing NOTE at
  `tools/unattended/unattended.sh:423` keeps its bytes. Observed by AC7.
- **S6** — The values. A committed instrument under this build's `build/` folder reads committed
  after-arm rows and prints the three constant lines exactly as the driver spells them, by the
  formula in §4 "The values". The driver carries what it prints and nothing typed beside it.
  Observed by AC8.
- **S7** — `tools/unattended/README.md` gains a section on the two ceilings: what each does on a
  breach, the formula and its inputs, the per-spawn allowance, and why no conf key exists. Observed
  by AC11.
- **S8** — The driver suite gains the arms §7 declares, `tools/memory-tree/check-arms.py` finds the
  new check-4 branch armed, and `memory/map/generated/symbols.json` is regenerated for the three new
  functions. Observed by AC9 and AC10.

## 3. Non-goals (OUT)

- No `.unattended.conf` key for either ceiling, and no environment override. A key owes a row in
  the protocol's key table, and the protocol is a governance carrier this build may not edit; an
  environment read is a new public surface (§8 F2).
- No change to `GATE_BOUND`, its default, its reader, or the protocol row at
  `tools/unattended/PROTOCOL.template.md:469`. That row says `GATE_BOUND` bounds `GATE_CMD` and
  `WIRING_CHECK`, and it stays true: `GATE_BOUND` still bounds the wiring check, and the ceiling is a
  second, smaller kill beside it. Verified against the template at writing.
- No kill and no refusal for preflight's own total. That is the owner's ruling, not a gap.
- No change to what `check-wiring.sh` checks or how fast it runs (units 1 to 3), and none to the
  order in which preflight starts its bounded probes (unit 4). The other bounded children preflight
  waits on — the lander's two probes and the profile command — keep `GATE_BOUND` alone.
- No ceiling on `--close` or on any verb but `--preflight`.
- No fork-count arm, which aSparedSpawn-8 plans, and no spawn-count ceiling (§8 F5).
- The unattended kit's version bump. The build makes one bump per touched kit, after that kit's last
  move, and the main loop makes it at the close.
- No value raised to fit a slow reading, and the 60 s target plays no part in either value: it is the
  goal, not a bound.

### Edges

- **consumes-from** `TOOL-aBriskPreflight-3` — the `WIRING_CHECK` preflight runs, decided by
  measurement: the whole `--check`, with the straggler inventory's own 60 s bound inside it, and the
  arm-windows instrument that measures that wait. The wiring ceiling's value is derived from that
  check's wall, spawn count and straggler window, so without it the value would be derived from a
  check preflight does not run.
- **consumes-from** `TOOL-aBriskPreflight-4` — the shape of the wiring call once the bounded probes
  start together: `init_preflight_probes`, which starts the wiring child and is where this unit sets
  the bound, and `check_wiring`, which reads it and is where this unit reads the kill. Without it
  this unit edits the sequential `check_wiring` the base carries.
- **hands-off** external — a conf channel for either ceiling. It owes a protocol key-table row in a
  governance carrier, so an adopter whose wiring check legitimately runs longer than the declared
  ceiling has no override until the owner adds one.

## 4. Design

### The two ceilings and where they live

Both are file constants in the driver, on `REMOTE_BOUND`'s argument at
`tools/unattended/unattended.sh:138`: a ceiling raisable from the environment leaves no diff behind.
They sit after `read_bound_key GATE_BOUND` (`tools/unattended/unattended.sh:618`), so the conf,
sourced at `tools/unattended/unattended.sh:550`, cannot reassign them. The second NOTE of S5 sits
beside them, guarded by `GATE_BOUND_LIVE`, because `WIRING_CEILING` does not exist yet where the
first NOTE prints.

Their comments cite this unit's id and say the rows sit in its build record. They spell no path
outside the kit, because a kit file names nothing outside itself by literal.

### The wiring bound and the refusal

`derive_wiring_bound` sets `WIRING_BOUND` to `WIRING_CEILING` when that is below `GATE_BOUND`, and
to `GATE_BOUND` otherwise, and sets `WIRING_BOUND_BY` to `ceiling` or `gate` to say which. A
`GATE_BOUND` of 0 — which the conf reader refuses and only a hermetic test sets — counts as no
bound, so the ceiling alone applies. It is one helper with two callers because the bound is read
when the child STARTS, which after unit 4 is `init_preflight_probes`, while the kill is read in
`check_wiring`; two spellings of the comparison would be two answers to one question. The kill
branch keeps its present condition: status 124 or 137, `GATE_BOUND_LIVE` is 1, and the bound is
positive. It then chooses the refusal by `WIRING_BOUND_BY`. Unit 4 measures `RB_TOOK` from the
child's own start to its read, and `check_wiring` is the first read after the start, so the printed
figure is the ceiling's.

### The refusal

The ceiling's refusal, as `fail 4` receives it:

```
the declared wiring check ran past its own ${WIRING_CEILING}s wall-clock ceiling and was killed after ${RB_TOOK}s, so preflight refuses its cost rather than waiting it out; the ${GATE_BOUND}s GATE_BOUND is no longer this check's only kill. One spawn cost ${SPAWN_COST} at the kill against the ${CEILING_SPAWN_MS}ms the ceiling allows, so a figure far above that is this host's load and one near it is the check's own cost: $WIRING_CHECK
```

Every interpolation is a plain variable, so `check-arms.py` can cut each literal slice. The captured
output follows, indented four spaces, as at `tools/unattended/unattended.sh:2741`. The `GATE_BOUND`
refusal at `tools/unattended/unattended.sh:2737` is untouched.

### The preflight wall and the breach line

`DRIVER_T0_US` is taken right after `set -u` with the idiom `write_runlog_start` already uses at
`tools/unattended/unattended.sh:13427`: `EPOCHREALTIME` with its separator stripped, or
`printf -v … '%(%s)T' -1` times one million where that variable is absent. Both are fork-free.
`print_preflight_breach` reads the clock the same way, so the stamp and the compare share one
spelling. It compares in microseconds and prints the wall to a tenth of a second. The dispatch arm
becomes `--preflight) verb_preflight "$SLUG" "$KID"; print_preflight_breach ;;`. No shell `exit` is
reachable from the verb, read at writing: the driver's and the library's sit in startup code and in
`read_bound_key`, which runs before any verb. So every refusal reaches the compare.

```
unattended: preflight over its ceiling — it took ${wall}s against its own ${PREFLIGHT_CEILING}s wall-clock ceiling. One spawn cost ${SPAWN_COST} here against the ${CEILING_SPAWN_MS}ms the ceiling allows, so a figure far above that is this host's load and one near it is preflight's own cost. This line judges cost only: the exit status and the run-state file are what the checks above decided.
```

A stamp that is not a whole number prints this instead, so a compare that could not run says so:

```
unattended: preflight ceiling not compared — the driver's start stamp is not a whole number, so this run's wall is unknown rather than within its ${PREFLIGHT_CEILING}s ceiling
```

Under the ceiling it prints nothing. The run log's END line already carries `dur_us` for every
preflight.

### The spawn-cost figure

`measure_spawn_cost` resolves the external `true` once on `PATH`, outside the timed window, then
times five spawns of it with the fork-free clock. That is the shape of the build's host-state
instrument, so the figure compares with that instrument's `spawn5` divided by five. It caches its
result in `SPAWN_COST` for the process. Without `EPOCHREALTIME` it sets
`an unmeasured amount (this bash has no EPOCHREALTIME)`. With no external `true` on `PATH` it sets
`an unmeasured amount (no external true on PATH)`. The ceiling also allows a worst per-fork cost,
which neither line prints; one figure keeps the sentence readable.

### The values

Two subjects: the wiring check as `.unattended.conf` declares `WIRING_CHECK` at the pass — the
whole `--check`, by unit 3's decision — and the whole `--preflight`. For each subject:

| Input | What | Source | Kind |
|---|---|---|---|
| W | the slowest of at least three untraced after-arm runs | `run-timed.sh` rows | DERIVED |
| S_m | that run's per-spawn cost, `spawn5` / 5 | the `host label=` row written just before it | DERIVED |
| K_m | that run's per-fork cost, `fork` | the same row | DERIVED |
| E, K | execs and forks of one traced after-arm run, same subject, same tree | `trace-spawns.py` | DERIVED, host-independent |
| U | for each wait run under its own declared timeout whose time the counter cannot attribute to a counted spawn, that timeout less the wait's window in the traced run, floored at 0 | below | DERIVED |
| S_w | the larger of 2.5 s and every S_m in the rows | the prompt record, 2026-10-11 | 2.5 s PINNED |
| K_w | the larger of 0.91 s and every K_m in the rows | this build's `hook-base` row, 2026-10-11 | 0.91 s PINNED |

```
ceiling          = the next multiple of 30 at or above  W + E * max(0, S_w - S_m) + K * max(0, K_w - K_m) + U
CEILING_SPAWN_MS = S_w * 1000, rounded to a whole number
```

U's waits. For the wiring check it is the straggler inventory, which `check-wiring.sh` runs under
its own `timeout 60` and whose cost is python's own git calls, which the counter cannot see. Its
window comes from unit 3's arm-windows instrument over the traced run. For preflight it is that same
wait, plus each remote observation the driver runs under `REMOTE_BOUND`, its window taken from the
committed gap analyzer's per-function wall over the traced preflight run. A traced window runs
slower than an untraced one, so U errs small; the slowest-of-three W and the spawn term carry the
rest.

**The margin, and why.** The margin over the measured wall is what every counted spawn and fork
would add if each cost the worst recorded on this node instead of what it cost when measured. A
healthy run breaches only on a host slower per process than any reading on record, or when the code
spawns, forks or waits more than it did when measured — the regression a ceiling exists to name. The
slowest of three readings absorbs run-to-run spread at one host state. The round-up to 30 s keeps
the figure comparable by eye; it adds at most 29 s and is not a margin to rely on.

**What it cannot see.** E and K are lower bounds: the counter's docstring says it cannot count a
program started by a program that is not bash, such as a git hook or a python subprocess. U covers
the two such waits whose bound is known. Any other uncounted cost — the lander probes' and the
profile command's own work, which `GATE_BOUND` alone bounds — is projected at its measured cost, not
the worst. Concurrent children, after unit 4, are projected as if serial, so the preflight value is
looser than its critical path needs. Looser is quieter, never noisier.

**An arithmetic check on committed rows, not a value.** `cw-base-traced` has W 568.3 s, E 387 and
K 355. The nearest host row, `pf-real-base`, has S_m 0.794 s and K_m 0.08 s. The straggler window
was 71.5 s at BASE (unit 3's reading), past its 60 s timeout, so U is 0. The formula gives
568.3 + 387 × 1.706 + 355 × 0.83 + 0 = 1523.2, so 1530 s. That wall is traced, at BASE, beside a
neighbouring run's host row, so it only checks the arithmetic.

**Where the rows come from.** The build's own A/B supplies them if it has committed after-arm rows
of both subjects by the time this unit's pass begins. Otherwise this pass takes them, at the commit
where units 1 to 6 are terminal and before its own edits, with the committed instruments. The labels
are `cw-after-<n>`, `pf-after-<n>`, `cw-after-traced` and `pf-after-traced`, and every timed row
follows its own `host label=` row. Each traced label also gets one row per U wait, naming the wait,
its timeout and its window. The wiring subject's traced run may be unit 3's `cw-u12-traced` when no
later commit touched `tools/check-wiring.sh`. The preflight subject is the `pf-real-base` form the
baseline record names, re-run with the run's recorded keepalive id. The driver treats that as an
idempotent re-preflight (TOOL-aBranchedMandate-8), and a refused one writes nothing.

**The rows this pass read (rev-2).** The A/B committed two untraced after-arm preflights, `ab-AN-1`
and `ab-AN-2` in `…-7-ab-rows.log`, each after its own host row and each carrying `preflight OK`. A
third is not taken: one whole preflight ran 856 s to 1042 s on this host, past the pass's 600 s
command bound, so the preflight subject has TWO untraced rows and the wiring subject three. The
wiring rows, `cw-after-1` to `cw-after-3`, are taken by this pass on the A/B's new-arm clone, whose
`tools/check-wiring.sh` is the tip's, and sit in `…-7-ceiling-rows.log` with their host rows. The
traced counts are `cw-u12-traced` for the wiring subject (unit 3's record, AC4: 137 execs, 193
forks; no commit since `2a64d49be` touched `tools/check-wiring.sh`) and `pf-fixture-new-traced` for
preflight (the build brief: 653 execs, 762 forks), a run refused at check 4 by the dormant hook mode
unit 10 fixed. The U windows: the straggler inventory's 69.0 s in `cw-u12-traced` (unit 3's arm
windows) for both subjects, since unit 3's instrument reads only a trace whose first process is the
wiring script; and for preflight the two remote reads under `REMOTE_BOUND` in
`pf-fixture-new-traced`, 6.0 s and 9.5 s from the `observe_remote` row to its caller's next row, plus
the claim write, which that refused run never reached, at a window of 0, so its whole 60 s counts.
Each such figure is one row of `…-7-ceiling-rows.log` naming its source; the instrument reads both
files.

**The instrument.** A shell file under this build's `build/` folder, named by hygiene check 5's
grammar for this unit, with no function definitions so the lexicon leg has nothing to grade. It
reads the rows, applies the formula, and prints exactly three lines: `WIRING_CEILING="<n>"`,
`PREFLIGHT_CEILING="<n>"` and `CEILING_SPAWN_MS="<n>"`. It exits 1 naming the subject when rows are
missing, or when a value is at or above the `GATE_BOUND` that `.unattended.conf` declares (3600 at
writing). Then the unit parks: a wiring ceiling at or above that bound can never fire first, and a
preflight ceiling there names nothing sooner than the bound the owner called silent.

A later change to either value is a rev bump of this spec with new rows. The instrument's diff
against the driver refuses a retyped constant.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `print_preflight_breach` | shell function | `sh.function` — `print` is declared; `--suggest` answered OK |
| `measure_spawn_cost` | shell function | `sh.function` — `measure` is declared; `--suggest` answered OK |
| `derive_wiring_bound` | shell function | `sh.function` — `derive` is declared; `--suggest` answered OK |
| `WIRING_CEILING`, `PREFLIGHT_CEILING`, `CEILING_SPAWN_MS` | file constants | none declared for shell constants |
| `DRIVER_T0_US`, `SPAWN_COST`, `WIRING_BOUND`, `WIRING_BOUND_BY` | driver globals | none declared for shell variables |

### Files touched (estimate)

`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`
`tools/unattended/README.md`
`memory/map/generated/symbols.json`
`memory/builds/aBriskPreflight/build/` (the ceilings instrument and the after-arm rows, if this pass
takes them)

### Rollout

Live, with no flag. The charter lands risky behaviour dark, but every dark form here needs a conf
key, which is a non-goal, or an environment read, which §8 F2 vetoes. The owner's ruling asks for
the refusal itself. The in-place verification the dark rule exists for happens before landing: the
values are derived from real readings on this tree, and the arms observe both lines on fixtures.

### Alternatives rejected

Each fork's losers, with the test or veto that rejected them, are in §8, and §10 lists them with
their tests as BUILD-METHOD M12 asks.

## 5. Production-readiness checklist

- security — no new write path or surface. The unit adds two file constants, a fork-free stamp, a
  compare, and five spawns of `true` on a breach path only. The conf cannot raise a ceiling and
  cannot move the stamp. No conf key, flag or environment read is added.
- perf / scale — no spawn is added on a path that does not breach (AC12). A breach costs five
  spawns, once per process.
- error / empty / loading states — with no working `timeout -k` both kills are inert, and the second
  NOTE says so for the ceiling. An unreadable stamp prints the not-compared line. A spawn probe with
  no `EPOCHREALTIME` or no external `true` prints an unmeasured phrase with its reason.
- observability — the refusal and the breach line name the ceiling, the measured wall, the
  per-spawn cost and the allowance. The run log's END line carries `dur_us` for every preflight.
- risks — a host slower per spawn than any reading recorded on node a refuses a healthy wiring
  check. The line prints the spawn figure, so it reads as load, and the remedy is a value re-derived
  through a rev bump, never a retyped one. An adopter whose wiring check legitimately runs longer
  than gov's ceiling is refused with no conf override (§3 Edges). The counts are lower bounds, so
  the projection under-counts spawns started by git or python. A fixture preflight slower than the
  real `PREFLIGHT_CEILING` would print one extra line in an arm; none is near it at writing.
- testing — three arm groups in the driver suite, run sliced in the pass, the harness-arms checker,
  and the instrument's diff against the driver.
- migration — none. Adopters receive the constants at the kit's next version, and a project whose
  wiring check exceeds the ceiling is refused at its next preflight (risks).
- user docs — the new section in `tools/unattended/README.md`.

## 6. Acceptance criteria

- **AC1** — When a slice of the driver suite runs — its prologue and the new wiring-ceiling block
  only, written under the run's scratchpad with its kit directory pinned to `tools/unattended/` —
  the block's copy of the driver has `WIRING_CEILING` rewritten to `"2"` through `mutate`. Run as
  `--preflight tRun --keepalive-id k1` over a conf with `GATE_BOUND="600"` and a `--check` stub that
  sleeps 30 s, it prints `the declared wiring check ran past its own 2s wall-clock ceiling and was
  killed after`, the clause `the 600s GATE_BOUND is no longer this check's only kill`, the clause
  `at the kill against the`, and `--preflight refused; the run-state file is unchanged`. The
  fixture's `tRun/RUN.md`, which the suite's pristine tree already carries, hashes as it did before
  the run, and the `killed after <n>s` figure is under 25.
  Red when: the copy is the driver at the pass's parent, where the rewrite is a fixture no-op and
  the stub's 30 s passes check 4 and writes the record; or the refusal names `GATE_BOUND`.
  fixture: `mkconf` at `tools/unattended/unattended.test.sh:210`, the copied-driver idiom at
  `tools/unattended/unattended.test.sh:11719`, and the 30 s window measured at
  `tools/unattended/unattended.test.sh:8470`.
  cost: about a minute on node a under load, most of it the fixture's git work.
- **AC2** — When AC1's block runs again with `WIRING_CEILING="9999"` appended to the fixture's
  committed `.unattended.conf`, the refusal still names the `2s` ceiling.
  Red when: the constants are assigned before `. "$CONF"`, so the conf's value wins and the stub
  passes check 4.
- **AC3** — When the same block runs with `WIRING_CEILING` rewritten to `"20"` and a stub sleeping
  1 s, the output carries `unattended: preflight OK` and no `check 4 FAILED`. When the existing
  block at `tools/unattended/unattended.test.sh:8525` runs sliced against the built driver, with
  `GATE_BOUND` at 2 and a 60 s sleeper, it still prints `the declared wiring check did not answer
  within the declared 2s bound` and does not print `wall-clock ceiling`.
  Red when: the ceiling stands in for `GATE_BOUND` rather than the smaller of the two being the
  bound, so a 2 s `GATE_BOUND` names the ceiling or waits for it.
- **AC4** — When a slice runs the new breach block — a driver copy with `PREFLIGHT_CEILING`
  rewritten to `"1"` through `mutate` and a `--check` stub sleeping 3 s on a clean fixture — the
  output carries `unattended: preflight OK`, then `unattended: preflight over its ceiling — it took`
  with a wall of at least 3.0, `its own 1s wall-clock ceiling` and `here against the`. `RUN.md` is
  written and staged in the fixture's `tRun` folder, and the driver exits 0. The same fixture run
  through an unmodified copy prints no `preflight over its ceiling`.
  Red when: the driver at the pass's parent prints no breach line, the breach changes the exit
  status, or the record is missing.
- **AC5** — When AC4's copy runs over the same fixture left dirty by one untracked file, the output
  carries the check 2 refusal, `--preflight refused; the run-state file is unchanged` and the
  breach line, and the exit status equals that of the same dirty fixture run through an unmodified
  copy, which prints no breach line.
  Red when: the compare runs only on the success path, or it moves the exit status.
- **AC6** — When a driver copy has its `DRIVER_T0_US` assignment rewritten through `mutate` to a
  value that is not a number, a preflight over the clean fixture prints `unattended: preflight
  ceiling not compared — the driver's start stamp is not a whole number` and exits 0.
  Red when: an unreadable stamp prints nothing, prints a breach, or aborts the verb under `set -u`.
- **AC7** — When `bash tools/unattended/unattended.sh --version` runs with a directory first on
  `PATH` whose `timeout` script exits 1, stderr carries the existing `GATE_BOUND` NOTE unchanged and
  the second NOTE naming `WIRING_CEILING`'s value as inert.
  Red when: the shimmed host prints only the `GATE_BOUND` NOTE, so an inert ceiling reads as a live
  one.
- **AC8** — When the ceilings instrument runs, its three lines are byte-identical to the output of
  `grep -E '^(WIRING_CEILING|PREFLIGHT_CEILING|CEILING_SPAWN_MS)=' tools/unattended/unattended.sh`.
  The wiring subject has at least three untraced rows and the preflight subject at least two (§4
  "The rows this pass read"), each after its own host row, and each subject one traced count row
  and at least one row per U wait. Both ceilings are below the declared `GATE_BOUND`.
  Red when: a constant was typed rather than derived, a timed row has no host row, a U wait has no
  window row, or a value reaches the bound, which the instrument refuses with exit 1.
  figure: every value is DERIVED at the pass from the rows the instrument names. S_w and K_w carry
  the PINNED floors of 2.5 s and 0.91 s, measured on node a, 2026-10-11.
  fixture: no after-arm row exists today; the A/B or this pass writes them (§4 "The values").
- **AC9** — When `python tools/memory-tree/check-arms.py --check` runs, it exits 0. With the new
  arm's assertion of the refusal's longest literal slice deleted from the working copy, it names
  the check-4 branch; restoring the line restores exit 0.
  Red when: the new `fail 4` branch has no arm quoting its literal slices.
- **AC10** — When `python tools/codebase-map/gen_map.py --check` and
  `python tools/lexicon/lexicon.py --check` run, both exit 0.
  Red when: `symbols.json` was not regenerated after the three functions landed, or a new name
  leads with a verb the declaration does not carry.
- **AC11** — When `grep -n -E 'WIRING_CEILING|PREFLIGHT_CEILING|CEILING_SPAWN_MS' tools/unattended/README.md`
  runs, it prints lines from one section naming both ceilings, what each does on a breach, the
  formula's inputs and why no conf key exists.
  Red when: the README does not name the ceilings, so an adopter meets a new refusal with no page
  describing it.
- **AC12** — When the committed spawn counter
  `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`
  counts one traced fixture preflight through a copy of the driver at the pass's parent and one
  through a copy of the built driver, in one fixture with `WIRING_CHECK="true"`, forks and execs are
  equal.
  Red when: the stamp, the compare or the effective-bound choice adds a command substitution or an
  external command on a path that does not breach.
  cost: two traced fixture preflights, a few minutes on node a under load.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `remote literals (kit code names no remote)` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

The pass verifies with AC1 to AC12 only. The listed legs run once, at the close, after the last
unit is terminal.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · a driver copy inside the fixture whose WIRING_CEILING line is rewritten through mutate, and a --check stub sleeping past it under a 600 s GATE_BOUND, run against the driver at the pass's parent, where the rewrite is a fixture no-op and the stub passes check 4 · none

New arm: tools/unattended/unattended.test.sh · covers AC4 AC5 AC6 · a driver copy whose PREFLIGHT_CEILING line is rewritten to 1 s and a 3 s --check stub, on a clean and on a dirty fixture tree, against the driver at the pass's parent, which prints no breach line · none

New arm: tools/unattended/unattended.test.sh · covers AC7 · a PATH directory whose timeout exits 1, against the driver at the pass's parent, whose only NOTE names GATE_BOUND · none

## 8. Open questions

- **F1 — Where is the wiring check's ceiling declared, and who reads it?** "Its own declared
  ceiling" can be read two ways. Options: (a) a constant inside `check-wiring.sh` that the script
  enforces on itself; (b) the driver reads a constant out of the file the `WIRING_CHECK` command
  names; (c) a driver constant applied to whatever `WIRING_CHECK` names; (d) a conf key. (d) fails
  veto 1 on §3's first non-goal and veto 2, since the protocol is a governance carrier. (b) fails
  veto 2: a constant name the driver reads out of another kit's file is a new cross-kit surface, and
  a kit file names nothing outside itself by literal. (a) satisfies fewer criteria: the driver cannot
  name a ceiling it cannot read, so check 4's refusal could not name it for an arbitrary
  `WIRING_CHECK`; and a self-kill needs an in-script watchdog, whose backgrounded child is the shape
  `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` records. (c) survives and covers any
  adopter's check. Recommendation: (c).
  RESOLVED (agent, 2026-10-11, delegated): (c). The ceiling is declared for the wiring check by the
  one program that can kill it and name it.
- **F2 — How does a test reach a breach without waiting out a real ceiling?** Options: (a) the arm
  runs a copy of the driver inside the fixture with the constant rewritten through `mutate`, the
  idiom the drift-delta close arm already uses; (b) a lower-only environment seam the shipped driver
  reads, in the shape of `GATE_BACKSTOP_MARGIN`; (c) hermetic extraction of the functions alone.
  (b) fails veto 2: an environment variable the shipped driver reads is a new public surface,
  precedent or not. (c) satisfies fewer criteria, because it cannot observe `preflight OK`, the
  record written, or the record not written. Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a). A constant absent from the copy reds as a fixture
  no-op, so the arm cannot pass against a driver that has none.
- **F3 — Does a breach line carry a load figure beside the wall?** Options: (a) one per-spawn cost
  measured at the breach, beside the allowance the ceiling was derived with; (b) the wall and the
  ceiling only. (a) costs five spawns on a breach path only and answers the open shape
  `TOOL-aGradedMandate-12` filed: a wall-clock verdict on this fleet must say whether it is reading
  load or regression. No veto applies. Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a).
- **F4 — Where does preflight's wall start?** Options: (a) a stamp at the driver's first
  statement; (b) a stamp at `verb_preflight`'s entry; (c) bash's `SECONDS`. A probe rules out (c):
  `SECONDS=1000 bash -c 'echo $SECONDS'` printed 1000 and `EPOCHREALTIME=5 bash -c 'echo
  $EPOCHREALTIME'` printed the real clock, on node a, bash 5.3.9, 2026-10-11. So `SECONDS` is
  imported from the environment and an inherited value would shift the figure, while
  `EPOCHREALTIME` is not. A bash that did not import it would have printed 0, so the probe could
  have come out the other way. (b) under-reports by the driver's startup — the library, the conf
  and the `timeout` liveness spawn — which the A/B's external clock counts, so the compared figure
  and the source of its value would be two quantities.
  RESOLVED (agent, 2026-10-11, delegated): (a).
- **F5 — What formula turns readings into a value?** Options: (a) the measured wall scaled by
  S_w / S_m; (b) a fixed multiple of the measured wall; (c) the count-based projection in §4 "The
  values"; (d) a spawn-count ceiling in the shape of `TOOL-aThawedCorpus-3`. (d) fails veto 1 on the
  owner's ruling: the wiring ceiling is a kill, and a count is known only after the child finishes.
  (b) has no derivable multiple: the per-spawn cost moved 5x within one loaded session (the prompt
  record) and about 36x between quiet and loaded (21 ms against 0.75 s), so any fixed multiple
  either breaches every loaded run of a quiet reading or carries no reason. (a) loses on the
  committed rows: `cw-base-traced`'s 568.3 s decomposes into 336 s of process creation (387 execs at
  0.794 s, 355 forks at 0.08 s) and 232 s that is not, about 41 percent. (a) multiplies that residual
  by a ratio set by whichever host state the reading happened in, 3.1x here and about 119x from a
  quiet one. (c) adds only the process term, so it does not depend on the host state of the reading.
  Recommendation: (c).
  RESOLVED (agent, 2026-10-11, delegated): (c).
- **F6 — Does the refusal ship dark?** Options: (a) live; (b) behind a default-off switch. (b) needs
  a conf key, a non-goal, or an environment read, which F2 vetoes. The owner's ruling asks for the
  refusal itself. Recommendation: (a), with the reason recorded in §4 "Rollout".
  RESOLVED (agent, 2026-10-11, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the spec brief
  `2026-10-11-prompt-TOOL-aBriskPreflight-7-spec-brief.md`.
- rev-2 · 2026-10-11 · INPROGRESS for the build pass. §4 gains "The rows this pass read" and AC8
  takes two untraced preflight rows, not three: a whole preflight on this host outruns the pass's
  600 s command bound, so the A/B's two new-arm rows are the preflight subject's, and the traced
  counts and U windows are named with their sources.
- rev-3 · 2026-10-11 · AC1 grades the fixture's `tRun/RUN.md` as byte-identical rather than absent:
  the suite's pristine tree carries one, so "no `RUN.md` exists" was false of the fixture before any
  run, and the sliced arm read it present on the built driver.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a wall-clock ceiling on a bounded child and
refuse naming it when the kill fires"` ranked `run_bounded` (a seam, in
`tools/unattended/unattended.sh`), `read_bound_key` and `check_gate_wall` in
`tools/unattended/lib-unattended.sh`, and name-stem neighbours. The seams this unit extends, each
verified in source at writing:

- `run_bounded` and its per-call `RB_BOUND` override at `tools/unattended/unattended.sh:211`, set
  and cleared around one call as the gates-green arm does at `tools/unattended/unattended.sh:10640`.
- The `check_wiring` kill branch at `tools/unattended/unattended.sh:2736`, extended with a second
  refusal rather than a second branch shape.
- The file-constant precedent: `REMOTE_BOUND` at `tools/unattended/unattended.sh:144` and
  `RUNAWAY_CEILING` at `tools/unattended/unattended.sh:847`, both read by `core_of` in
  `tools/unattended/check-unattended.sh`.
- The fork-free clock idiom of `write_runlog_start` at `tools/unattended/unattended.sh:13427`.
- In the suite: the copied-driver idiom at `tools/unattended/unattended.test.sh:11719`, `mutate` at
  `tools/unattended/unattended.test.sh:189`, and the driver's own `killed after` figure as the
  instrument (TOOL-aClosedDocket-3).

`check_gate_wall` compares a wall with a ceiling, but its inputs are the bar profile's, so it is
cited and not reused. No existing seam fits the spawn-cost probe: `reuse_lookup.py` named none, and
the only spawn timer in the tree is this build's host-state instrument, a records file the driver may
not call.

The recall probe returned `TOOL-aThawedCorpus-3`, whose N1 says no wall-clock ceiling on this node
(913 s against 29 s for one commit), and `TOOL-aGradedMandate-12`, whose open candidates are CPU time
or a load figure beside the elapsed one. It also returned `TOOL-aProvenReuse-6` (wall-clock arms
flake under load) and `TOOL-dRetiredFork-30` (a ceiling below a healthy run kills a passing leg).
They disagree with the owner's ruling, which chose wall clock. This unit answers N1 by projecting the
value to the worst recorded per-process cost (§8 F5) and by taking `TOOL-aGradedMandate-12`'s second
candidate for its two lines (§8 F3). Its arms assert the driver's own figure, never the harness clock.

Candidates rejected, with the test that rejected each (M12): §8 F1 (a), (b) and (d), by vetoes and
by the refusal having to name the ceiling; §8 F2 (b) by veto 2 and (c) by what it cannot observe;
§8 F4 (c) by the `SECONDS` import probe and (b) by the startup it leaves out; §8 F5 (a) by the
41 percent non-process residual of `cw-base-traced`, (b) by the 5x and 36x spreads, and (d) by
veto 1.

Recall terms used: `python tools/memory-recall/query.py "what decided how a bounded preflight child
is killed and how a wall-clock ceiling breach is reported" --terms "run_bounded GATE_BOUND
REMOTE_BOUND ceiling wall-clock preflight check_wiring WIRING_CHECK refusal breach cost verdict file
constant"`
