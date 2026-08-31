# TOOL-aUnblockedFleet-6 — the merge bar's turnstile stops eating the unattended close's deadline

**Status:** WONTDO · rev-2 · 2026-08-31 · node a · Tier-2 · base 117de044 · streams tooling · order 3 · ratified 2026-08-31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aUnblockedFleet-1-diff-closing.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-1-diff-closing.md) | diff-review | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 |
| [2026-08-31-review-TOOL-aUnblockedFleet-6-specs-round2.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-6-specs-round2.md) | spec-audit | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 |

<!-- /gen:spec-records -->

## 1. Goal

> **RETIRED (WONTDO), 2026-08-31, by spec-audit round 2.** All three mechanisms below were refuted
> against source, and the review loop was NON-CONVERGENT (3 blockers in both rounds) so a corrected
> design could not be re-reviewed. The PROBLEM this unit names is real and survives as a parked
> decision in `RUN.md` and a backlog row; what is retired is this design, not the finding. Successor:
> none authored — the property the fix needs was identified only in round 2 and rests on a
> measurement (the cost of a CONTENDED bar) nobody on this fleet has taken. §9 records the three
> refutations.

Removing the two run-state checks unblocks a run from STARTING. It does not unblock it from CLOSING:
`run-gates.sh` holds a repo-wide turnstile keyed on the git common dir, so two concurrent `--close`
bars in one clone serialize, and the queue wait is charged against the run's own `GATE_BOUND`. The
second run then fails `gates-green` for pure contention, unattended, with nobody to read it. Bound
the queue wait strictly inside the gate bound, so a queued bar falls through the turnstile's existing
fail-open path instead of being killed.

## 2. Scope (IN)

- **S1** — `tools/run-gates/run-gates.sh` accepts an explicit `GATE_TURNSTILE_MAXWAIT` override for
  the bounded queue wait, defaulting to the current derivation (`TS_TTL * 4`) when unset. One knob,
  defaulted to today's behaviour, so no existing caller changes.
- **S2** — the override is validated as a positive integer and IGNORED with a printed notice if it is
  not, because a malformed bound that silently becomes zero would make every bar run unqueued and
  disable the turnstile entirely — the failure this whole mechanism exists to prevent, arriving
  through its own configuration path.
- **S3** — `tools/unattended/unattended.sh` exports `GATE_TURNSTILE_MAXWAIT` when it runs `GATE_CMD`
  for the `gates-green` item, derived from `GATE_BOUND` rather than declared: `GATE_BOUND / 4`. A
  derived value cannot drift from the bound it must sit inside, and a second declared knob could be
  set larger than the bound it exists to fit within.
- **S4** — the export is scoped to that one invocation, not to the whole driver process. `--preflight`
  runs `WIRING_CHECK` under the same `run_bounded`, and that check does not run a bar; exporting
  globally would put an unrelated knob into every child of the driver.
- **S5** — when the bar IS killed by `GATE_BOUND`, the existing `DOD_OUT` message gains one clause
  naming the queue: the driver reads `<git-common-dir>/gate-queue-status`, which `run-gates.sh:686`
  already writes with `position` and `waited` while queued, and reports whether the kill landed while
  the bar was still waiting for another bar. Distinguishing "a leg failed", "the bar never returned"
  and "the bar never STARTED" is the difference between an operator hunting a failing leg and one
  reading a contention notice.
- **S6** — `.unattended.conf`'s `GATE_BOUND` comment gains the derivation, because an adopter reading
  that key must be able to see that it now sets a second bound.

## 3. Non-goals (OUT)

- Making the turnstile itself concurrent, sharded, or per-worktree. Its own header records the
  measurement that justifies it — three full bars at once, CPU at 39%, width 24 running 26% SLOWER
  than width 8 — so the contended resource does not parallelise and serializing is correct.
- Raising `GATE_BOUND`. It is a HANG detector sized against a 26-minute bar by
  `TOOL-aBoundedCeiling-6`, which was written after a 3h19m hang. Sizing it to absorb queue time
  would restore exactly the blindness that record exists to remove.
- Shrinking `GATE_TURNSTILE_TTL`. It would shrink `TS_MAXWAIT` as a side effect and get the number
  right for the wrong reason: that constant is the beacon staleness bound, so lowering it makes a run
  reap a live holder's beacon and two bars run anyway.
- Any change to how the bar itself schedules legs, or to `GATE_JOBS`.

## 4. Design

### The mechanism, as measured

`run-gates.sh:419` defaults `GATE_TURNSTILE` to 1. `:434` derives `TS_TTL` as `PROF_TIMEOUT * 3`, or
`GATE_TURNSTILE_TTL` defaulted to 1800 when the profile row sets no timeout. `:438` derives
`TS_MAXWAIT = TS_TTL * 4`, so at least 7200s. `unattended.sh:2845` runs the bar as
`run_bounded $GATE_CMD`, and `run_bounded` at `:189` is `timeout -k 5s "$GATE_BOUND"`. This project
declares `GATE_BOUND=3600`.

So the queue wait and the bar's own execution share one 3600s budget, and the queue alone may consume
7200s. This repository's own charter records a 26-minute floor on a full bar, which is the
first-order case: run A holds the turnstile for ~1560s, run B queues behind it, and B needs
1560 + 1560 = 3120s before its own bar even finishes — inside 3600 only if nothing else is slow.
Two bars either side of the profile's median put B over the bound and `gates-green` reads unmet.

### Why the fix is a bound and not a retry

`run-gates.sh:664-668` already FAILS OPEN at `TS_MAXWAIT`: it drops the queue and runs unqueued,
loudly, with the reason printed. That path exists because "a turnstile that can wedge a bar is worse
than two bars" — its own words. The defect is not that the fail-open is missing; it is that the
fail-open threshold sits OUTSIDE the deadline that kills the process first, so the escape hatch can
never be reached. Moving the threshold inside the deadline makes an existing, tested, deliberate path
reachable. That is strictly smaller than adding a retry, a lock handoff, or a second scheduler.

### Alternatives rejected

**Start the driver's clock at turnstile acquisition** by launching the bar in the background and
polling its output for an acquisition marker. Rejected: it couples the unattended kit to
`run-gates.sh`'s output format, and the two kits are copy-installed independently — an adopter may
hold one and not the other, so the driver may not parse another kit's stdout.

**Have `--close` wait for the turnstile to be free before starting the bounded bar.** Rejected: the
driver would have to reimplement the beacon, the nonce and the staleness rules to read that state
honestly, which is `second-implementation-is-not-a-second-opinion` — and it races, so the residual
wait it fails to remove is still a whole bar.

**Set `GATE_TURNSTILE=0` for unattended closes.** Rejected: it does not queue at all, so it
reintroduces the measured 26%-slower contention on every concurrent close, which is the state the
turnstile was built to remove.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | `TS_MAXWAIT` honours `GATE_TURNSTILE_MAXWAIT`, validated; header states the new knob |
| `tools/unattended/unattended.sh` | the `gates-green` invocation exports the derived value; the bound-kill message gains the queue clause |
| `.unattended.conf` | `GATE_BOUND`'s comment states the derived second bound |
| `tools/run-gates/run-gates.turnstile.test.sh` | arms for the override, its default, and its malformed value |
| `tools/unattended/unattended.test.sh` | an arm for the queue clause on a bound kill |

## 5. Production-readiness checklist

- security — N/A; a scheduling bound, no trust boundary.
- perf / scale — this is the perf unit. It shortens a pathological wait and lengthens nothing.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — S2 is the malformed-value case and S5 is the killed-while-queued
  case. Both are the states this unit exists to make legible.
- observability — S5. A bound kill currently says "the bar never returned", which is true and
  useless; after this it says whether the bar ever started.
- risks — the `two-guards-one-question-two-answers` class, which is precisely what this unit closes:
  `GATE_BOUND` and `TS_MAXWAIT` ask one question — how long may this wait — and answer it
  differently, and their conjunction is unsatisfiable. Landing units 1 and 2 WITHOUT this unit
  relocates the fleet wedge rather than removing it, which is why this unit sits at order 3, before
  the carriers.
- testing + left-shift gates — the turnstile suite already exists and is the seam; three arms added.
- migration / rollback — revert; the knob defaults to today's derivation so an un-set caller is
  byte-identical.
- user docs — S6 plus unit 3's protocol edit, which gains one sentence.

## 6. Acceptance criteria

- **AC1** — When `GATE_TURNSTILE_MAXWAIT=120 bash tools/run-gates/run-gates.sh` runs against a held
  beacon, the run drops the queue and prints the existing `turnstile WAIT EXPIRED after` notice
  within ~120s rather than after `TS_TTL * 4`.
- **AC2** — When `GATE_TURNSTILE_MAXWAIT` is unset, `TS_MAXWAIT` still derives to `TS_TTL * 4`,
  asserted by an arm — the default-preserved control, without which AC1 passes over a runner that
  broke every existing caller.
- **AC3** — When `GATE_TURNSTILE_MAXWAIT=nonsense` is set, the runner prints its ignore notice and
  uses the derived value, asserted by an arm. The malformed value must not become zero.
- **AC4** — When `--close` runs the bar, the child process environment carries
  `GATE_TURNSTILE_MAXWAIT` equal to `GATE_BOUND / 4`, asserted by a stub `GATE_CMD` that echoes the
  variable.
- **AC5** — When the bar is killed by `GATE_BOUND` while `<git-common-dir>/gate-queue-status` exists
  and records a non-zero wait, the `gates-green` message names the queue and the waited seconds,
  asserted by a `hit` arm in `unattended.test.sh` over a stubbed gate command and a planted status
  file.
- **AC6** — When that status file is ABSENT, the message keeps its existing wording exactly,
  asserted by a `miss` arm — the control that stops AC5's clause from being unconditional.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `run-gates turnstile`, `unattended kit gate` and
`drift-audit records` binding. `drift-audit records` is named because this unit rewrites headers
inside `PRODUCT_GLOBS` and the `non_terminal_specs_cited_by_product_source` ratchet is at its
ceiling — see unit 1 §7 for the landing-order rule that governs all of units 1, 2, 3 and 6.

## 8. Open questions

none — the fork was which of four mechanisms bounds the wait, decided in §4 by the observation that
`run-gates.sh` already has a deliberate fail-open path that the deadline makes unreachable.
RESOLVED (agent, 2026-08-31, delegated): make the existing fail-open threshold reachable by bounding
it inside `GATE_BOUND`, deriving the value rather than declaring a second one.

## 9. Revision log

- rev-2 · 2026-08-31 · RETIRED. Spec-audit round 2 refuted every mechanism, each verified against
  source before the retirement: **(a)** S5, AC5 and §10 name `<git-common-dir>/gate-queue-status`,
  but `run-gates.sh:686` writes `$gd`, which `:95` sets from `git rev-parse --git-dir` — the
  PER-WORKTREE directory. On the sibling-worktree layout this build exists for, the driver would stat
  a path nothing writes, and AC5 plants the file itself so the arm would have been green over a dead
  feature. **(b)** `run-gates.sh:692` removes that file on BOTH exits from the wait loop, before the
  bar runs, so the state S5 reports is unreachable and S3 and S5 answer one question incompatibly.
  **(c)** the `GATE_BOUND / 4` derivation yields a 900s queue bound against a measured ~1560s bar, so
  a queued close NEVER acquires: it always times out and runs contended, which is `GATE_TURNSTILE=0`
  by another name and is what this spec's own §3 rejected. Round 2 also found a second consumer of
  `TS_MAXWAIT` this spec never named — `ts_sweep_queue`'s cutoff at `:515` — whose safety property at
  `:494-496` holds only while every bar shares one bound, so a 900s close would sweep a live waiter's
  ticket and wedge a bystander. The correct property, named by round 2 and not designed here:
  `GATE_BOUND` minus the queue bound must exceed a CONTENDED bar.
- rev-1 · 2026-08-31 · authored under the aUnblockedFleet mandate, promoted from spec-audit round 1
  blocker B1 via `--rescope --act add`. The audit found a safety property the removal loses that the
  build's own §4 measurement did not reach, because that measurement probed the run-state registry
  and this contention lives in the merge bar.

## 10. Reuse audit

The seam is the turnstile block at `tools/run-gates/run-gates.sh:415-441` and its existing
`GATE_TURNSTILE_TTL` override, which is the pattern S1 copies exactly: an env knob with a derived
default, read once at the top of the block. The second seam is `<git-common-dir>/gate-queue-status`,
already written at `:686`, which S5 READS rather than adding a new breadcrumb — the file exists and
nothing consumed it.

`python tools/codebase-map/reuse_lookup.py "bound how long a queued merge bar waits for another bar"`
was run for this unit specifically rather than inherited from unit 1, because the behaviour is a
different one and reusing unit 1's query would be a probe that never asked this question. It returned
the `run-gates` affordance seam and no competing implementation.

Recall terms: `turnstile beacon queue git-common-dir GATE_BOUND run_bounded gates-green contention
serialize maxwait ttl close deadline`. It returned `TOOL-aBoundedCeiling-6` (the 3h19m hang that
motivated `GATE_BOUND`) and the turnstile unit's own records. Both are cited above; neither
anticipated the interaction, which is why this unit exists.

**Verified against source at writing time**: `GATE_TURNSTILE` default at `:419`, the `TS_TTL` and
`TS_MAXWAIT` derivations at `:434-438`, the fail-open at `:664-668`, the queue-status write at
`:686`, `run_bounded`'s `timeout -k 5s` at `unattended.sh:189`, the `gates-green` invocation at
`:2845` and its bound-kill message at `:2852`, and `GATE_BOUND=3600` in `.unattended.conf`.
