# TOOL-aPairedSlots-1 — a `slots=<n>` key on each profile row, set for node a by the two-bar A/B

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base b6cd02bc · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh](../build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md) | research | TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 |

<!-- /gen:spec-records -->

## 1. Goal

How many bars the turnstile admits at once becomes a declared knob: a `slots=<n>` key on each
`tools/run-gates/gate-profiles.txt` row, 1 where a row omits it, overridden by
`GATE_TURNSTILE_SLOTS`, and printed by `--print-profile`. Node a's row takes the value a measured
A/B of two full bars, serial against concurrent, earns under the owner's decision rule.

## 2. Scope (IN)

- **S1 — the row key.** `slots` joins `KNOWN_KNOBS` in `tools/run-gates/run-gates.sh` and is
  parsed with the existing row validator, so a non-numeric or over-long value refuses the bar as
  any malformed knob does. A value of 0 refuses too, with its own message, because a turnstile of
  no slots admits nothing. A row that omits the key resolves `PROF_SLOTS=1`, as does the built-in
  branch with no table. Observed by AC1.
- **S2 — the override.** `GATE_TURNSTILE_SLOTS`, when set, replaces the row's value. A value that
  is not a positive integer of at most 15 digits is IGNORED with one NOTE line naming it and the row
  value used, because this knob only schedules bars and can never skip a leg, which is the same
  rule `GATE_JOBS` follows. Observed by AC2.
- **S3 — where it is printed.** `--print-profile` prints `slots<TAB><n>` after `queue`. The
  profile line gains `, slots <n>` after the mempause field ONLY when the effective value is above
  1, so a run at 1 prints the line it prints today. Observed by AC1, AC3.
- **S4 — the A/B and the value.** The instrument under this build's `build/` runs arms A, B and C,
  each twice, on two frozen clones of one base, and its result rows are committed beside it. Node
  a's row, `capable`, carries `slots=2` only when arm B's or arm C's makespan is no worse than arm
  A's in both repetitions; otherwise it carries no `slots` key and the README's Parked slot records
  the numbers and the reason. Observed by AC4.
- **S5 — the knob classes and the pins.** `GATE_TURNSTILE_SLOTS` joins `BAR_INERT_KNOBS` in
  `.githooks/pre-push.test.sh`, because it decides contention and never a verdict. `slots` joins
  `PINNED_KNOBS` in `tools/run-gates/run-gates.test.sh`. Observed by AC5.
- **S6 — the text.** `gate-profiles.txt`'s KNOBS header gains the `slots=<n>` entry, and
  `tools/run-gates/README.md`'s knob table gains the row, each naming the A/B record. NOT OBSERVED
  — prose, graded by the review, not by a check.

## 3. Non-goals (OUT)

- The semaphore that reads the value (TOOL-aPairedSlots-2) and the width it implies
  (TOOL-aPairedSlots-3). This unit resolves and prints the number; with only this unit built, a
  bar still admits exactly one holder whatever the number says.
- A per-host or per-repository slot declaration. The row is selected by detected hardware, as
  every knob is; a host running repositories that declare different values is the rollout question
  TOOL-aPairedSlots-2 states.
- Re-deriving the TTL, `TS_MAXWAIT` or the wall from the slot count.

### Edges

- **hands-off** `TOOL-aPairedSlots-2` — `PROF_SLOTS`, the resolved and overridden value, which
  the semaphore reads as its slot count.
- **hands-off** `TOOL-aPairedSlots-3` — the arm the A/B chose and its width rule, recorded in the
  A/B record this unit commits.
- **consumes-from** external — aFrugalTurnstile's host-wide turnstile and its `--hold` verb on
  the default branch: the A/B holds the host with it, and the code pass waits for it to land.

## 4. Design

### The A/B

The instrument is `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh`.
`init` builds a bare remote advertising only `main` at the base, and two clones of it, so the
clones are separate repositories that nothing else writes. `plan` runs the arm-runs in a
counterbalanced order, `A1 B1 C1 C2 B2 A2`, so a drift in host load across the hours lands on
every arm rather than on one. Before each arm-run it waits for a quiet host, up to two hours, then
runs the arm under the clone runner's `--hold`, so a bar from a runner that knows the host
turnstile queues behind the arm instead of joining it. Both of the arm's bars then nest under the
hold.

Every bar is `GATE_FULL=1` with self-tests held, the default full bar. Arm A runs clone 1's bar,
then clone 2's, at the profile's width. Arm B runs both at once with `GATE_JOBS` at half that
width. Arm C runs both at once at the full width. The makespan is the seconds from the arm's start
until the later bar exits; each bar's wall is recorded beside it.

A bar PROVES it ran when its `GATE ok` plus `GATE FAIL` lines equal the legs its clone's manifest
does not hold, and its run record carries a verdict. A bar without that proof voids its arm-run,
which is then re-run, never compared. A sampler records foreign bars, bash processes, load average,
CPU and free memory once a minute through every arm-run, so contamination is a column and never an
exclusion made after the fact.

### The decision rule, as the owner wrote it

Let `A_r`, `B_r` and `C_r` be the makespans of repetition `r`. Node a's row carries `slots=2` when
`B_1 <= A_1` and `B_2 <= A_2`, or when `C_1 <= A_1` and `C_2 <= A_2`. When both arms qualify, the
one with the smaller summed makespan is the arm recorded, and its width rule is what
TOOL-aPairedSlots-3 implements: half width for B, full width for C. When neither qualifies, the
row carries no `slots` key.

### Inventory

New names: `PROF_SLOTS` (a shell variable, the resolved count), `slots` (a profile knob and a
`--print-profile` key), `GATE_TURNSTILE_SLOTS` (an environment knob). No function is minted in the
runner. The instrument's functions are snake_case and each leads with a declared verb, the
`sh.function` cell: `print_err`, `measure_expected_legs`, `cmd_init`, `scan_foreign_bars`,
`run_sampler`, `run_bar`, `measure_bar`, `cmd_arm`, `check_quiet`, `cmd_plan` and `main`.

### Rollout

A row without the key reads 1, so every adopter table keeps today's behaviour after a kit update.
Gov's own table is the kit's shipped table, so a `slots=2` on `capable` reaches every adopter host
that selects `capable`; the row comment says so beside the number.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/gate-profiles.txt`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.test.sh`
- `.githooks/pre-push.test.sh`
- `memory/builds/aPairedSlots/build/`

### Alternatives rejected

- **A count derived from cores or RAM.** The earlier measurement found the contended resource is
  per-op latency that does not parallelise, so no hardware figure predicts the answer; only a
  measurement on the host does, and a declared row is where this tree keeps a measured number.
- **Refusing a malformed `GATE_TURNSTILE_SLOTS`.** The row value is the safe fallback and a knob
  that only schedules bars follows `GATE_JOBS`, which clamps rather than refuses.

## 5. Production-readiness checklist

- security — N/A — a count read from a tracked table and an environment knob; no new input surface.
- perf / scale — the whole point; the A/B is the measurement and its rows are committed.
- error / empty / loading states — an absent key reads 1; a malformed row value refuses the bar; a
  malformed override is ignored with a NOTE.
- observability — `--print-profile` and, above 1, the profile line.
- risks — `slots=2` on the shipped `capable` row reaches adopters on capable hosts; stated in the row
  comment and the README.
- testing — AC1 to AC5 in scratch fixtures; the canary's pinned set moves with the knob.
- migration — none; a missing key is the old behaviour.
- user docs — the README knob table and the profile table's header.

## 6. Acceptance criteria

The fixtures are scratch repos under the session scratch, built the way the canary builds one,
with a `gate-profiles.txt` row the arm writes.

- **AC1** — When a fixture row declares `slots=3`, `run-gates.sh --print-profile` prints a
  `slots` line reading 3, and with the key omitted one reading 1.
  Red when: the key is absent from `KNOWN_KNOBS`, and the row refuses as an unknown knob.
- **AC2** — When `GATE_TURNSTILE_SLOTS=2` is set over a row declaring none, `--print-profile`
  prints a `slots` line reading 2; when it is `abc`, it prints the row's value and stderr carries the NOTE.
  Red when: the override is not read, and the value stays 1.
- **AC3** — When a fixture bar runs at the effective value 1, its `gate profile:` line is
  byte-identical to the base runner's on the same fixture, and at 2 it carries `, slots 2`.
  Red when: the field is printed unconditionally, and the value-1 line differs from base.
- **AC4** — When `2026-10-11-build-TOOL-aPairedSlots-1-ab-results.tsv` is read, every arm-run row
  carries `proof yes` on both bars, there are two repetitions of each arm, and the `capable` row's
  `slots` value matches the decision rule over its MAKESPAN rows.
  Red when: a row's proof is `NO`, or the value disagrees with the rule over the committed rows.
  cost: about nine hours of host time for the six arm-runs.
  figure: DERIVED at observation time from the committed rows.
- **AC5** — When `check_knob_classes` in `.githooks/pre-push.test.sh` is sliced and run over the
  changed runner, it prints nothing, and before the classification it names
  `GATE_TURNSTILE_SLOTS`.
  Red when: the knob is left unclassified.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `memory hygiene`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC3 · a fixture row without the key, then with it, then the override · none

## 8. Open questions

- **FACT-QUESTION · F1 — Does node a's `capable` row carry `slots=2`?** The probe is the A/B
  instrument above; the observation is the six MAKESPAN rows; the rule is §4's. Liveness: arm A can
  win, and every bar must carry `proof yes`, so a run that measured nothing cannot decide it.
  Recommendation: whatever the rows say.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "admit more than one gate bar at once with a counting semaphore of beacon slots"`
named no counting-semaphore seam; the knob extends the existing profile-row parse in
`tools/run-gates/run-gates.sh` (`KNOWN_KNOBS` and its validator) and the `--print-profile` verb,
whose reader is `parse_gate_profile` in `tools/unattended/lib-unattended.sh`. Recall qid 921
returned TOOL-aMeteredTurnstile-6 and TOOL-aUnblockedFleet-6, the three-bar measurement this
unit re-runs for two bars.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
