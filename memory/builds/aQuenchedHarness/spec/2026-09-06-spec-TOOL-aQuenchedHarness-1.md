# TOOL-aQuenchedHarness-1 — the bar's own wall, so a wedged run dies with a verdict

**Status:** OPEN · rev-2 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-5 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |

<!-- /gen:spec-records -->

## 1. Goal

Give `tools/run-gates/run-gates.sh` a whole-run wall-clock wall, so a bar that wedges is killed and
REDs naming what was still running, instead of stalling an unattended build for hours. Today the only
bound is per-leg, so a run's worst case is the sum of every ceiling it can reach.

## 2. Scope (IN)

- **S1** — a `wall=<s>` knob on `tools/run-gates/gate-profiles.txt`, in the same grammar as `width`
  and `timeout`, read by the same `KNOWN_KNOBS` path. `0` means off, and off is a state the profile
  line REPORTS rather than a silence.
- **S2** — the wall is armed when the first leg is dispatched, not at process start: the turnstile
  wait is a queue, not a run, and folding it into the wall would kill a bar for waiting its turn. The
  wait has its own bound, `TS_MAXWAIT`.
- **S3** — on breach the runner kills the outstanding legs, writes a RED summary NAMING every leg
  that had not returned, and exits non-zero. A wall breach is a VERDICT, never a skip and never a
  green, which is `gate-profiles.txt`'s governing invariant applied to this knob.
- **S4** — ONE MECHANISM, stated once. The wall is a watcher that sleeps, writes a breach marker, and
  kills the process GROUP of every outstanding leg. It does not use `timeout`, and rev-1's claim that
  it reuses the per-leg ceiling's `timeout -k` path was wrong: that call at `run-gates.sh:1110` wraps
  exactly one command, not a pool. The per-leg ceiling is untouched by this unit.
- **S5** — `WALL_LIVE` is set by a probe OF THE WALL'S OWN MECHANISM, not of `timeout`. At startup the
  runner arms a sub-second wall over a sleeping child that has itself spawned a grandchild, and
  observes whether the group kill reaches both. `CEILINGS_LIVE` stays a separate flag set by its own
  separate probe. A host where the group kill cannot reach a surviving grandchild — the MSYS
  condition `memory/builds/aPacedTurnstile/reviews/2026-08-20-review-TOOL-aPacedTurnstile-2.md`
  blocker B1 records — reports the wall INERT, which reading `timeout`'s probe could never do.
- **S6** — `GATE_WALL=<s>` overrides the selected row's value alone, mirroring `GATE_JOBS`.
- **S7** — arms in `tools/run-gates/run-gates.test.sh`: a leg that outlives the wall; an untimed
  control proving the elapsed time is the wall and not the leg; an off (`wall=0`) run; a run whose
  wall is INERT; and a leg whose child spawns a grandchild that outlives it, asserted killed.

## 3. Non-goals (OUT)

- Not the per-leg ceiling. That exists, this unit does not touch it, and `TOOL-aQuenchedHarness-2`
  owns its evidence.
- Not the turnstile. Its wait bound is `TS_MAXWAIT` and its live-holder defect is
  `TOOL-aQuenchedHarness-8`, which lands first.
- Not a per-leg budget verdict — cost policing is units 4 and 6. A wall is a HANG bound.
- Not a wall value nobody would meet in practice. Choosing the number is a declaration this unit makes
  with the reading beside it.

## 4. Design

### Data model

`gate-profiles.txt` rows gain a third knob. The row grammar is unchanged — knobs are a comma-joined
list — so the parser change is one `case` arm beside `width` and `timeout`, and the declared
`KNOWN_KNOBS` string grows by one member. The canary PINS that set separately, which is what forces
an author to read the table's governing-invariant paragraph before adding a knob.

### The wall

One background watcher, started when the first leg is dispatched, sleeping in short increments so it
can be reaped cheaply when the pool drains normally. On expiry it writes a breach marker into the
run's work directory and kills the process group of every outstanding leg; the pool's reaper reads
the marker and renders the RED summary. The marker is a FILE rather than a variable, because a
watcher that shares a variable with the pool it watches is not a watcher (charter §7).

### Two flags, two probes

`CEILINGS_LIVE` answers "can `timeout -k` run here", and the per-leg ceiling is what consumes it.
`WALL_LIVE` answers "does a group kill from a watcher reach a leg's descendants here", and only the
wall consumes it. Rev-1 pinned the second to the first "rather than a second probe", which certified
a mechanism the wall does not use in both directions: a host with no `timeout` would have declared a
working watcher INERT, and a host where the group kill cannot reach a grandchild would have reported
the wall live. That is the reassuring-zero class, inside the unit that cites it.

### Inventory

- `wall` — the profile knob, in `tools/run-gates/gate-profiles.txt`; graded by the canary's pin.
- `GATE_WALL` — the environment override.
- `WALL_LIVE` — the wall's own liveness flag, set by its own probe, named beside `CEILINGS_LIVE` and
  deliberately not derived from it.
- The breach marker file, under the existing per-run work directory; no new location.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/gate-profiles.txt` ·
`tools/run-gates/run-gates.test.sh` · `AGENTS.md`'s merge-bar section, one sentence.

### Alternatives rejected

A wall enforced by the CALLER — the pre-push hook, or the unattended driver's `GATE_BOUND` — was
rejected: that bound exists at 3600 s and did not prevent the stalls, because it covers only the bar
`--close` runs and not a bar a session starts itself. A bound only some callers apply is a bound the
bar does not have.

## 5. Production-readiness checklist

- security — N/A: no new input, no new write path outside the existing work directory.
- perf / scale — one watcher process per run, sleeping, plus one startup probe; against a bar
  measured in thousands of spawns.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — wall off, wall INERT, wall breached. Each has its own printed
  line and none of them is silence.
- observability — the profile line reports `width`/`timeout`/`ceilings` and gains `wall`, so the run
  says what bound it is under before the first verdict.
- risks — a wall that fires on a legitimately slow bar turns a passing run red, which is
  `TOOL-dRetiredFork-40`'s recorded failure for ceilings. Mitigated by sizing it against recorded
  leg-sums and by the override, and by landing `TOOL-aQuenchedHarness-8` FIRST so the wall is sized
  against an uncontended bar rather than against two bars running as one.
- testing + left-shift gates — S7's arms, in the existing canary, graded against an untimed control
  rather than against a message.
- migration / rollback — `wall=0` on every row is the rollback and is behaviour-identical to today.
- user docs — one sentence in `AGENTS.md`'s bar section and the knob's own justification comment.

## 6. Acceptance criteria

- **AC1** — When a fixture leg sleeps past the declared wall, `bash tools/run-gates/run-gates.sh`
  exits non-zero and its summary NAMES that leg as still running, rather than reporting a leg failure.
- **AC2** — When the same fixture runs with `GATE_WALL=0`, it completes normally, proving the arm
  measures the wall and not the leg.
- **AC3** — When the wall fires, the elapsed time measured by the arm in
  `tools/run-gates/run-gates.test.sh` is bounded by the wall and compared against an untimed control
  run in the same arm, so a bound applied through a pipe cannot pass.
- **AC4** — When the wall's own startup probe cannot kill a grandchild, the run prints that the wall
  is `INERT` and the profile line says so; and when `timeout -k` is absent but the group kill works,
  the wall is reported LIVE while `ceilings` is reported INERT — two flags, two verdicts.
- **AC5** — When a knob is added to `gate-profiles.txt` without updating `KNOWN_KNOBS`, the
  `run-gates canary` leg reds, so the pin cannot drift.
- **AC6** — When a fixture leg spawns a grandchild that outlives it and the wall fires, the arm in
  `tools/run-gates/run-gates.test.sh` finds the grandchild dead, asserted by pid rather than by the
  summary's wording.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the `run-gates canary` leg, which owns the knob pin ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for that canary at the Definition of Done, since
it is a held self-test leg.

## 8. Open questions

- **F1 — what value does each profile row declare?** RESOLVED (agent, 2026-09-06, delegated): a
  per-row figure, declared against the recorded leg-sum for that width and carrying the reading
  beside it. A single figure cannot be right for a cost that is node-relative, which
  `TOOL-aCollapsedScan-4` records; and shipping it off everywhere would land a knob that has never
  fired, which charter §7 refuses.
- **F2 — is the wall sized before or after `TOOL-aQuenchedHarness-8`?** RESOLVED (agent, 2026-09-06,
  delegated): after. Unit 8 takes `order 1` and this unit `order 2`, because every recorded leg-sum
  in the tree today was measured under a bar that may have been sharing the machine with a second
  bar it reaped. Sizing a wall against those numbers would bake the defect into the bound.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.
- rev-2 · 2026-09-06 · folded spec-audit round 1. H3: the wall and the per-leg ceiling are now ONE
  mechanism each rather than one claim spanning both — S4 states the watcher does not use `timeout`,
  and S5 gives `WALL_LIVE` its own probe of the group kill with a grandchild, so a host with no
  `timeout` no longer declares a working watcher inert and a host where the group kill cannot reach a
  descendant no longer reports the wall live. AC4 rewritten to name both directions, AC6 added for
  the grandchild. §5 and §8 F2 record that this unit is sized AFTER unit 8, because today's leg-sums
  were measured under bars that may have been running two at a time.

## 10. Reuse audit

The seam this unit extends is `tools/run-gates/run-gates.sh`'s existing per-run machinery — the
profile knob parser at `KNOWN_KNOBS`, the per-run work directory, the marker-file idiom and the
summary renderer. It does NOT extend the per-leg `timeout -k` path, and saying so is the correction
rev-2 makes: that call wraps one command and the wall bounds a pool, so reusing its liveness probe
was reuse of the wrong thing. `tools/codebase-map/reuse_lookup.py` returned
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seam for this area, carrying
decisions `TOOL-aPacedTurnstile-1` through `-16`; that build's own review record supplied the MSYS
group-kill condition S5's probe now tests for. The profile table's governing-invariant paragraph was
read before adding a knob, as it instructs.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
