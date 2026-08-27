# TOOL-aReapedTicket-3 — arms for a dead waiter, which the suite has never had

**Status:** SPECCED · rev-1 · 2026-08-27 · node a · Tier-2 · base f1be0b49 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-prompt-TOOL-aReapedTicket-1.md](../prompts/2026-08-27-prompt-TOOL-aReapedTicket-1.md) | research | TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 |

<!-- /gen:spec-records -->

## 1. Goal

Give `run-gates.turnstile.test.sh` the arms it has never had: a queue ticket whose owner is gone. The
suite's fifteen arms all drive fixtures with a live holder, so it is exactly as blind as the runner —
which is why the bar has been green across every landing since `aPacedTurnstile` while the wedge
shipped.

## 2. Scope (IN)

- `tools/run-gates/run-gates.turnstile.test.sh`: new arms covering the two reproductions in the
  prompt record, the sweep's two signals, the negative control that stops a sweep-everything reaper
  passing, and the two reporting criteria.
- Raising `FLOOR_ASSERTIONS`, which is the suite's own shrink-only pin at `:29`.

## 3. Non-goals (OUT)

- Repairing arm 4c, which `TOOL-aBoundedCeiling-8` records as unable to fail — both of its branches
  are `ok`. Real, open, and a different unit: touching it needs its own failing case observed, and
  this build's ruling is that a guard whose failing case has not been observed is not landed.
- Repairing the load-sensitivity `TOOL-dSpentCeiling-8` records for this leg. Also real, also open,
  also a different predicate.
- Any new gate leg. `run-gates turnstile` already exists in `tools/gate-legs.json` with a guard on
  `tools/run-gates/`, so these arms enrol with no wiring.

## 4. Design

### What the suite covers today, and the hole

Fifteen arms. Arms 3, 4, 4b, 4c and 11 are liveness arms and every one of them is about the HOLDER
beacon. Arms 5/6, 6b, 7, 7b and 7c are about FIFO order and the bounded wait, and each drives a
fixture in which a live holder is what the waiter is waiting for. **No arm places a ticket in the
queue whose owner is gone**, which is the entire subject of this build.

### The arms

Numbered to continue the suite's existing scheme rather than renumbering it, since arm numbers are
cited from `memory/backlog/TOOL.md` and from the suite's own header.

- **15 — an interrupted waiter drops its own ticket.** Reproduction 2 from the prompt record,
  inverted. A beacon held by the harness's own pid with a fresh heartbeat so it is never reaped, one
  waiter queued behind it, `timeout -s INT` to the runner, then count the queue. Covers
  `TOOL-aReapedTicket-1` AC1. `SIGTERM` and `SIGHUP` variants cover AC2 — three signals, because a
  trap listing four and asserting one is the arity defect this repository already gates elsewhere.
- **16 — a dead ticket with NO beacon is swept, and the bar acquires.** Reproduction 1 from the
  prompt record. Plant a ticket naming a pid that cannot be alive, run a bar with a scaled TTL, and
  assert it acquires rather than reaching `WAIT EXPIRED`. Covers `TOOL-aReapedTicket-2` AC1.
  **This is the arm that fails today**, and its failing case is already observed and transcribed.
- **17 — the age signal fires against the UNMODIFIED runner.** A ticket whose pid is the harness's
  own — unquestionably alive — and whose NAME carries a stamp older than `TS_MAXWAIT`. Asserts the
  sweep fires and that its printed reason names the AGE, not the pid. Covers AC2. Following arm 4's
  precedent: an arm that disabled the pid branch would prove a mutant sweeps, not that the shipped
  nesting does.
- **18 — a LIVE waiter's ticket is NOT swept.** The negative control, and the arm that makes 16 and
  17 mean anything. Two waiters queued behind a held beacon; after several ticks, both tickets are
  still present. Covers AC3, and it is the arm that stops the sweep-everything reaper §4 of
  `TOOL-aReapedTicket-2` warns about.
- **19 — the queued line does not invent a holder.** Against the arm-16 fixture, assert the stderr
  does NOT claim another bar holds the repository when no beacon directory exists. Covers AC5.
- **20 — a failed ticket write fails open at once.** Make `$TS_Q` unwritable so `: > "$TS_TICKET"`
  fails, and assert the run reaches its legs in well under `TS_MAXWAIT`. Covers AC6.
  **This arm may not be reachable on every host** — a directory this user owns can often still be
  written despite a mode change, and Windows filesystem semantics differ. It therefore uses the
  suite's existing `skipped` helper, which counts toward the total and prints as `SKIP`, rather than
  spending an `ok` on a branch that demonstrated nothing. That helper exists at `:38` precisely for
  this.

### `FLOOR_ASSERTIONS`

At `42`. The header records that it was raised from 28 and states the rule for concurrent raises:
"whichever lands second has to say the number it expects", stated absolutely and never as a delta.
This unit raises it to cover the arms above and follows that rule. The compare is `-ge`, so an arm
left under an unraised floor is stranded rather than red — which is the reason the pin must move with
the arms and not after them.

### Two properties every arm here must have

**Structural, not textual.** `TOOL-aBoundedCeiling-8` records arm 4c grading a source COMMENT rather
than a mechanism, and the charter names that class. `AC4` of `TOOL-aReapedTicket-1` is the one
deliberately structural assertion in this build — it compares LINE NUMBERS between the ticket
creation and the trap site, which is a real ordering property of the file and not a claim about
prose.

**Timing bounds graded against a same-run control, never a literal.** `TOOL-aScannedThrottle-7` and
`TOOL-dSpentCeiling-8` both record this leg redding on fixed wall-clock windows on a box whose
process creation moves 25x under load. Arms 16 and 20 both assert "sooner than the bound", and the
bound is `TS_MAXWAIT` scaled down by the fixture's own `GATE_TURNSTILE_TTL` — so the comparison is
against a number the same run derived, not a literal.

### Files touched (estimate)

- `tools/run-gates/run-gates.turnstile.test.sh` — six arms plus the floor. Roughly 130 lines.

### Alternatives rejected

- **One combined arm for the whole sweep.** Rejected: `AC1` and `AC2` are two signals, and an arm
  that passes on either cannot tell which fired. That is the "satisfied by its own prose" shape one
  level up.
- **Assert the sweep by grepping `run-gates.sh` for the function name.** Rejected outright — that is
  arm 4c's recorded defect, and adding a sixth instance of it while citing its backlog row would be
  hard to explain.

## 5. Production-readiness checklist

- security — N/A. Scratch repositories under `mktemp -d`, torn down by the suite's existing `EXIT`
  trap at `:22`.
- perf / scale — the leg's declared `ceiling` in `tools/gate-legs.json` is 1130 s. These arms add
  roughly six short fixture runs; if the ceiling is breached the manifest value is what moves, and
  the breach is a RED naming the leg, which is the mechanism working.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — arm 20 carries an explicit `skipped` branch; every other arm's
  fixture either establishes or reports that it could not, following the precedent at `:189-194`.
- observability — each arm prints its own `ok`/`FAIL`/`SKIP` line through the suite's counters.
- risks (concurrency, data-loss, rollback hazards) — the leg runs inside a concurrent bar, and its
  own fixtures create beacons in scratch repositories that resolve a DIFFERENT git common dir from
  the real one, which arm 10 already asserts. No fixture may touch the real queue.
- testing + left-shift gates — this unit IS the left-shift for the other two.
- migration / rollback — none.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-gates.turnstile.test.sh` runs against the runner as it
  stands at this build's BASE, arm 16 FAILS. Observed before the arm lands, per §7's rule that a gate
  whose failing case has never been seen is an assertion about nothing; the transcript is in the
  prompt record and the staged break is re-confirmed at build time.
- **AC2** — When the same suite runs against the runner with `TOOL-aReapedTicket-1` and
  `TOOL-aReapedTicket-2` applied, every arm passes and the printed assertion count is `-ge` the
  raised `FLOOR_ASSERTIONS`.
- **AC3** — When an arm cannot establish its fixture, it prints through `skipped` and still counts,
  so the total cannot shrink by an arm quietly failing to arm — the property the suite header states
  at `:34-38`.
- **AC4** — When `bash tools/check-testsuite-counts.sh` runs, this suite still satisfies the executed
  assertion-count shape it derives from `tools/gate-legs.json`.

## 7. Gates

- `run-gates turnstile` — this unit's own subject.
- `testsuite-counts` — `tools/check-testsuite-counts.sh`, which derives its population from
  `tools/gate-legs.json` and grades the count shape.
- `line-length` and `gate-lint`.
- `install-prefix` — `tools/install-prefix-carried.txt:85` carries a count for this suite's path, so
  an edit that changes it must move that pin in the same commit.

## 8. Open questions

- **F1 — does raising `FLOOR_ASSERTIONS` collide with another in-flight raise?** The header names two
  prior raisers and the rule for a concurrent one. The current value is `42`; nothing else in this
  build touches it, and the merge bar's reconciliation is additive.
  RESOLVED (agent, 2026-08-27, delegated): raise it to the count these arms produce, stated
  absolutely, per the header's own instruction.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, written from the reproductions in the prompt record.

## 10. Reuse audit

**The seams are the suite's own fixtures, all of which already exist**: `mk_repo` (`:52`) builds the
scratch repository, `beacon` (`:90`) resolves the common dir absolutely the way the runner does,
`runbg` (`:80`) launches a bar, and `ok`/`nope`/`skipped` (`:33-38`) are the counters. Every arm here
is composed from those four and adds no new fixture helper. That is the reason this unit is arms and
a pin rather than a harness.

The one thing it does not reuse is arm 4c's shape, deliberately, and §4 says why with the backlog row
that records it.

The recall pass is the one recorded in `TOOL-aReapedTicket-1` §10, satisfied once for the SET per M5.
Its hits that bear on THIS unit are three backlog rows rather than a spec: `TOOL-aBoundedCeiling-8`
(arm 4c cannot fail), `TOOL-aScannedThrottle-7` and `TOOL-dSpentCeiling-8` (this leg reds on fixed
wall-clock windows under load). All three were verified against source before being relied on — arm
4c's two `ok` branches are still present at the lines the row names, and the suite still carries no
same-run timing control.
