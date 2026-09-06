# TOOL-aQuenchedHarness-1 — the bar's own wall, so a wedged run dies with a verdict

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-5 |

<!-- /gen:spec-records -->

## 1. Goal

Give `tools/run-gates/run-gates.sh` a whole-run wall-clock wall, so a bar that wedges is killed and
REDs naming what was still running, instead of stalling an unattended build for hours. Today the only
bound is per-leg, so a run's worst case is the sum of every ceiling it can reach — measured at HEAD
as tens of hours — and the owner's two stalled builds sat inside that window.

## 2. Scope (IN)

- **S1** — a `wall=<s>` knob on `tools/run-gates/gate-profiles.txt`, in the same grammar as `width`
  and `timeout`, read by the same `KNOWN_KNOBS` path. `0` means off, and off is a state the profile
  line REPORTS rather than a silence.
- **S2** — the runner arms the wall at the instant the first leg is dispatched, not at process start:
  the turnstile wait is a queue, not a run, and folding it into the wall would kill a bar for waiting
  its turn. The wait already has its own bound (`TS_MAXWAIT`).
- **S3** — on breach the runner kills the outstanding legs, writes a RED summary NAMING every leg
  that had not returned, and exits non-zero. A wall breach is a VERDICT, never a skip and never a
  green, which is `gate-profiles.txt`'s governing invariant applied to this knob.
- **S4** — the kill goes through the same file-captured, kill-after path the per-leg ceiling already
  uses, because a bound applied through a pipe bounds the verdict and not the clock
  (`memory/gotchas/bounded-through-a-pipe-is-unbounded.md`).
- **S5** — a LIVENESS assertion: the wall is probed with the option set the run actually uses, once,
  and a host where it cannot fire prints that the wall is INERT this run. A bound nobody can observe
  reporting nothing is the class this repo names.
- **S6** — `GATE_WALL=<s>` overrides the selected row's value alone, mirroring `GATE_JOBS`.
- **S7** — arms in `tools/run-gates/run-gates.test.sh` covering: a leg that outlives the wall, an
  untimed control proving the elapsed time is the wall and not the leg, an off (`wall=0`) run, and a
  run whose wall is INERT.

## 3. Non-goals (OUT)

- Not the per-leg ceiling: that exists and is `TOOL-aQuenchedHarness-2`'s subject.
- Not the turnstile wait, which already has `TS_MAXWAIT` and a documented unqueued fallback.
- Not a per-leg budget verdict — cost policing is unit 2 and unit 4, and a wall is a HANG bound.
- Not a default wall value on the `capable` row that anybody would meet in practice on this node;
  choosing the number is a declaration this unit makes with the reading beside it, and raising it
  later is an ordinary declared change.

## 4. Design

### Data model

`gate-profiles.txt` rows gain a third knob. The row grammar is unchanged — knobs are a comma-joined
list — so the parser change is one `case` arm beside `width` and `timeout` and the declared
`KNOWN_KNOBS` string grows by one member. The canary PINS that set separately, which is what forces
an author to read the table's governing-invariant paragraph before adding a knob.

### The wall

One background watcher, started when the first leg is dispatched, sleeping in short increments so it
can be reaped cheaply when the pool drains normally. On expiry it writes a breach marker into the
run's work directory and kills the process group of every outstanding leg, then the pool's reaper
reads the marker and renders the RED summary. The marker is a FILE rather than a variable, because a
watcher that shares a variable with the pool it watches is not a watcher (charter §7).

### Inventory

- `wall` — the profile knob, in `tools/run-gates/gate-profiles.txt`; graded by the canary's pin.
- `GATE_WALL` — the environment override, in `tools/run-gates/run-gates.sh`.
- `WALL_LIVE` — the runner-internal liveness flag, named beside `CEILINGS_LIVE` and set by the same
  single probe rather than a second one.
- The breach marker file, under the existing per-run work directory; no new location.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/gate-profiles.txt` ·
`tools/run-gates/run-gates.test.sh` · `AGENTS.md`'s merge-bar section, one sentence.

### Alternatives rejected

A wall enforced by the CALLER (the pre-push hook, or the unattended driver's `GATE_BOUND`) was
rejected: the driver's bound already exists and did not prevent the stalls, because it covers only
the bar `--close` runs and not a bar a session starts itself. A bound that only some callers apply is
a bound the bar does not have.

## 5. Production-readiness checklist

- security — N/A: no new input, no new write path outside the existing work directory.
- perf / scale — one watcher process per run, sleeping; the cost is one spawn against a bar measured
  in thousands.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing ASCII diagnostics, as the rest of the runner.
- error / empty / loading states — the three states are named: wall off, wall INERT, wall breached.
  Each has its own printed line, and none of them is silence.
- observability — the profile line already reports `width`/`timeout`/`ceilings`; it gains `wall`, so
  the run says what bound it is under before the first verdict.
- risks — a wall that fires on a legitimately slow bar turns a passing run red, which is exactly the
  failure `TOOL-dRetiredFork-40` records for ceilings. Mitigated by sizing it against the ledger's
  loaded readings and by the override, not by argument.
- testing + left-shift gates — S7's arms, in the existing canary, graded against an untimed control
  rather than against a message.
- migration / rollback — `wall=0` on every row is the rollback and is behaviour-identical to today.
- user docs — one sentence in `AGENTS.md`'s bar section and the knob's own justification comment.

## 6. Acceptance criteria

- **AC1** — When a fixture leg sleeps past the declared wall, `bash tools/run-gates/run-gates.sh`
  exits non-zero and its summary NAMES that leg as still running, rather than reporting a leg
  failure.
- **AC2** — When the same fixture runs with `GATE_WALL=0`, it completes normally, proving the arm
  measures the wall and not the leg.
- **AC3** — When the wall fires, the elapsed time measured by the arm in
  `tools/run-gates/run-gates.test.sh` is bounded by the wall and compared against an untimed control
  run in the same arm, so a bound applied through a pipe cannot pass.
- **AC4** — When `timeout -k` cannot run on the host, the run prints that the wall is `INERT` and the
  profile line says so, rather than reporting a bound it does not have.
- **AC5** — When a knob is added to `gate-profiles.txt` without updating `KNOWN_KNOBS`, the
  `run-gates canary` leg reds, so the pin cannot drift.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the `run-gates canary` leg (which owns the knob pin) ·
`GATE_SELFTESTS=1` for that canary at the Definition of Done, since it is a held self-test leg.

## 8. Open questions

- **F1 — what value does each profile row declare?** Options: a single figure across rows; a
  per-row figure scaled with `width`; or off everywhere until a later unit measures. RESOLVED
  (agent, 2026-09-06, delegated): a per-row figure, declared against the ledger's own recorded
  leg-sum for that width and carrying the reading beside it. A single figure cannot be right for a
  cost that is node-relative, which `TOOL-aCollapsedScan-4` already records; and shipping it off
  everywhere would land a knob that has never fired, which charter §7 refuses.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.

## 10. Reuse audit

The seam this unit extends is `tools/run-gates/run-gates.sh`'s existing per-leg bound — the profile
knob parser at `KNOWN_KNOBS`, the single `timeout -k 1s 10 true` liveness probe, and the
file-captured kill-after path the ceiling already uses. `tools/codebase-map/reuse_lookup.py` returned
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seam for this area, carrying
decisions `TOOL-aPacedTurnstile-1` through `-16`. No new mechanism is introduced: the wall reuses the
probe, the marker-file idiom and the summary renderer that are already there. Verified against source
at writing time; the profile table's governing-invariant paragraph was read before adding a knob, as
it instructs.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
