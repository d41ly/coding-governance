---
slug: aProbedUnit
node: a
opened: 2026-09-14
streams: tooling
roster: TOOL
parents: aRatifiedRulings
authorized-by: prompt
ids: TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7
---

# aProbedUnit — unattended units stop stalling: no bar in a pass, bounded commands, an audit probe, a fixed scratch root, one audit round

## The problem this build exists to solve

Unattended unit builds stall for hours. Four causes, all observed on nodes `a` and `d` this week:
a unit runs the full bar with self-tests inside its pass (up to 12 h, blocking the build); a unit
sits on one command nobody bounds (a 6 h `rm`); `$TMPDIR` is EMPTY in the shell, so a backup written
to `$TMPDIR/x` lands at the filesystem root and the cleanup waits on an approval nobody answers; and
every spec audit with a blocker re-arms a second round. The prompt is the mandate; its bytes are the
record under `prompts/`.

## Expected improvements

- No gate, suite or bar runs inside a unit pass; the bar runs ONCE, at `--close`.
- Every command a unit runs is bounded, and a non-code command that stalls is skipped and named.
- `--audit` reports a dispatched unit idle past a declared bound, with the remedy; the keepalive runs it.
- Every unit is handed its session scratchpad path; the scratch-guard denies an empty temp variable, `/tmp`, and root litter.
- One spec-audit round by default; blockers and highs promoted, mediums and lows folded.

## Detriments if this is not built

- Builds keep blocking on a single unit for half a day, on this repo and on every adopter.
- The `$TMPDIR` incident recurs on any Windows node the moment a fixer writes a backup.
- Every spec audit with one blocker costs a second full lens fan.
- The owner keeps reading stall post-mortems instead of landings.

## Build-level rules

- **Every unit ships to adopters through its kit.** A fix in a rendered or copy-installed file lands in the template AND its render in one commit, so this repo and an adopter get the same bytes.
- **Owner answers, 2026-09-14, one turn.** PROMOTE keeps M4's meaning: a blocker or high becomes a UNIT. The one-round bound covers SPEC subjects only; the closing diff review keeps its convergence loop. `UNIT_STALL_BOUND` defaults to 1800 s. The scratch-guard denies `/tmp` writes too, and allows the CLI's scratch base under the temp root.
- **No self-test suite runs inside a pass of THIS build either.** Unit 6 stages its own red case by running the single arm, never `unattended.test.sh` whole. The compensating `run-unattended-gates.sh` run is the closing pass's, once, on a frozen clone.
- **Vocabulary changes land in every carrier in one commit**: driver, leg, harness, tests, VERBS, SKILL, protocol, and the build method where a rule moves — a paraphrase left behind is the two-answers class.
- **A pass observes the grep or the single arm; the leg or suite half of any criterion is the close's.** Its ledger row reads `observed at --close`, never OBSERVED by a pass that did not run it. (Round-1 audit, cluster A.)
- **Classification at open**: all seven MISSING; specced by the harness's SPEC stage.

## Parked decisions

(none yet)

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aProbedUnit-1` | PLANNED | no gate, suite or bar runs inside a unit pass; the bar runs once at close |
| 2 | `TOOL-aProbedUnit-2` | PLANNED | every command a unit runs is bounded; a stalled non-code command is skipped and named |
| 3 | `TOOL-aProbedUnit-3` | PLANNED | `--audit`: the dispatched-unit stall probe, and the keepalive that runs it |
| 4 | `TOOL-aProbedUnit-4` | PLANNED | every harness agent is handed the session scratchpad path and told to use it |
| 5 | `TOOL-aProbedUnit-5` | PLANNED | scratch-guard denies an empty temp variable, `/tmp`, and a new entry at the POSIX root |
| 6 | `TOOL-aProbedUnit-6` | PLANNED | `REVIEW_ROUNDS` bounds a spec-audit subject; the `BOUNDED` exit |
| 7 | `TOOL-aProbedUnit-7` | PLANNED | disposal by severity: blockers and highs promoted, mediums and lows folded, on any confirmed finding |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 7 unit(s) · node a · opened 2026-09-14 · streams tooling
ids TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aProbedUnit-1 — no gate, suite or bar runs inside a unit pass; the bar runs once, at the close](spec/2026-09-14-spec-TOOL-aProbedUnit-1.md) | 1 | 2 | SPECCED | rev-2 | 2026-09-14 |
| [TOOL-aProbedUnit-2 — every command a unit runs is bounded; a stalled non-code command is skipped and named](spec/2026-09-14-spec-TOOL-aProbedUnit-2.md) | 2 | 1 | SPECCED | rev-2 | 2026-09-14 |
| [TOOL-aProbedUnit-3 — `--audit <slug>`, the dispatched-unit stall probe, and the keepalive that runs it](spec/2026-09-14-spec-TOOL-aProbedUnit-3.md) | 3 | 2 | SPECCED | rev-2 | 2026-09-14 |
| [TOOL-aProbedUnit-4 — every harness agent is handed the session scratchpad, as a required `scratch` argument](spec/2026-09-14-spec-TOOL-aProbedUnit-4.md) | 4 | 2 | SPECCED | rev-2 | 2026-09-14 |
| [TOOL-aProbedUnit-5 — scratch-guard denies an empty temp variable, `/tmp`, and a new entry at the POSIX root](spec/2026-09-14-spec-TOOL-aProbedUnit-5.md) | 5 | 2 | SPECCED | rev-2 | 2026-09-14 |
| [TOOL-aProbedUnit-6 — `REVIEW_ROUNDS` bounds a spec-audit subject; the `BOUNDED` exit](spec/2026-09-14-spec-TOOL-aProbedUnit-6.md) | 6 | 2 | SPECCED | rev-3 | 2026-09-14 |
| [TOOL-aProbedUnit-7 — disposal by severity, on any confirmed finding](spec/2026-09-14-spec-TOOL-aProbedUnit-7.md) | 7 | 2 | SPECCED | rev-2 | 2026-09-14 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aProbedUnit-1` | no |
| 2 | `TOOL-aProbedUnit-2` | no |
| 3 | `TOOL-aProbedUnit-3` | no |
| 4 | `TOOL-aProbedUnit-4` | no |
| 5 | `TOOL-aProbedUnit-5` | no |
| 6 | `TOOL-aProbedUnit-6` | no |
| 7 | `TOOL-aProbedUnit-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aRatifiedRulings](../aRatifiedRulings/README.md)
<!-- /gen:build-edges -->
