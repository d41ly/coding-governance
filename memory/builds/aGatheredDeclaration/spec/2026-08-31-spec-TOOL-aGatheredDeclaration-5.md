# TOOL-aGatheredDeclaration-5 — the turnstile beacon ships DISABLED

**Status:** OPEN · rev-2 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 |

<!-- /gen:spec-records -->

## 1. Goal

Flip the gate turnstile — the beacon that serialises one bar per repository and therefore enqueues
parallel pushes behind each other — from ships-enabled to ships-disabled, enabled by an owner
declaration. It is the mechanism that put a `push-main.sh` landing behind three dead tickets for
6858 s, and every adopter inherits it on arrival.

## 2. Scope (IN)

- **S1** — `[bar].turnstile`, declared in `gate-legs.toml`, shipping `false`.
- **S2** — `GATE_TURNSTILE` keeps its current meaning as the per-machine override and now takes the
  declared value in its absence. **The declared value reaches the guard MARSHALLED to the byte `0`
  or `1`**, per `TOOL-aGatheredDeclaration-2`'s loader rule, never as a TOML word. Both guards
  (`run-gates.sh:420` and `:726`) compare a string against `0`, so substituting a TOML `false`
  verbatim compares the word `false` against `0`, which is TRUE, and ships the mechanism ENABLED —
  the exact inversion of this unit's goal, arriving with the declaration visibly wired.
- **S3** — the adopter seed declares `turnstile = false`, so arriving at a target never enables it.
- **S4** — the `queued_from` vocabulary keeps its `off` member, which already records a DASH rather
  than a zero for a probe that never ran. Shipping disabled makes `off` the ordinary state rather
  than an exception, and the summary says so once rather than on every leg.
- **S5** — the turnstile suite keeps every arm and gains one: with the turnstile declared off, a
  second concurrent bar RUNS rather than queuing, and neither run's beacon or ticket appears.
- **S6** — `tools/run-gates/README.md`'s turnstile section states the new default and what turning
  it on buys, so an owner enabling it is choosing rather than inheriting.

## 3. Non-goals (OUT)

- Fixing the turnstile. `TOOL-aBoundedCeiling-12` (a dead WAITER is never reaped, only a dead
  holder) and `TOOL-aReapedTicket-4` (`ts_try_reap` uses a bare `rm -rf` where the design prescribed
  a rename) are both real and both stay OPEN. Shipping the mechanism off reduces their blast radius
  to owners who opted in; it does not repair them, and this spec does not claim it does.
- Deleting the turnstile. It solves a real problem — two full bars on one box thrash — for an owner
  who wants it.
- `tools/push-main.sh`. It holds no beacon of its own; verified against source at this revision. The
  queueing the prompt names reaches it through `.githooks/pre-push` invoking the runner.

## 4. Design

### Data model

One resolution, printed on the profile line:

| source | value |
|---|---|
| `GATE_TURNSTILE` env | outranks everything, `0` disables |
| `[bar].turnstile` | the declared default, shipping `false` |
| neither | `false` |

### Rollout

One line's default changes and one declaration is added. Rollback is `GATE_TURNSTILE=1`.

**Why this is safe to ship off, stated rather than assumed.** The turnstile FAILS OPEN by design
already: its wait is bounded at a declared multiple of the TTL and on expiry the run drops its
ticket and proceeds unqueued. So a repository with it off is in a state the mechanism already
reaches on its own whenever the bound expires, and that path is exercised. What is genuinely lost is
the thrash protection, and that is a wall-clock cost on a contended box rather than a correctness
one — the turnstile never contributes to the exit code.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/gate-legs.toml` ·
`tools/run-gates/run-gates.turnstile.test.sh` · `tools/run-gates/README.md` ·
`tools/run-gates/kit.toml` (the `[gate_runner_seed]` block).

### Alternatives rejected

**Fix the waiter reaping first, then leave it on.** It is the better engineering answer and it is
the wrong answer to this ask: the owner asked for the mechanism to ship off, and a repair leaves
every adopter still inheriting a queue they did not ask for. The two are not exclusive — the repair
stays on the backlog and lands for the owners who turn it on.

**Disable it only in the adopter seed, keeping gov enabled.** Rejected as two answers to one
question: gov dogfoods its own kits, and a default gov does not run is a default nobody tests.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — two concurrent bars on one box now both run. On node `a` at width 8 that is up to
  sixteen scratch repos resident. Named as the cost; the profile table's RAM threshold exists for
  exactly this and is unchanged.
- a11y, i18n — N/A.
- error / empty / loading states — an unresolvable common dir already records `unresolved` and is
  UNARMED; that is untouched.
- observability — the profile line names the turnstile state and its source. `queued_from` records
  `off` with a DASH, which already exists.
- risks — thrash on a contended box, above. The mitigations that already exist are the bounded wait
  and the fail-open.
- testing + left-shift gates — S5's arm, observed RED first.
- migration / rollback — `GATE_TURNSTILE=1`.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When `[bar].turnstile` is `false` — the SHIPPED state, not an absent key — and
  `GATE_TURNSTILE` is unset, no beacon directory is created under the git common dir and no ticket
  is written, asserted in `tools/run-gates/run-gates.turnstile.test.sh` by the absence of both
  paths after a scratch run.
- **AC1b** — When `[bar].turnstile` is `true` and `GATE_TURNSTILE` is UNSET, a beacon AND a ticket
  ARE created and a second concurrent bar queues, asserted in
  `tools/run-gates/run-gates.turnstile.test.sh`. This is the middle row of the resolution table:
  without it, a runner that ignores the declaration entirely and flips the `run-gates.sh:420`
  literal to `0` satisfies every other criterion. Observed RED first.
- **AC1c** — When the loader reads `[bar].turnstile`, the value reaching the guard is exactly the
  byte `0` or `1`, byte-compared, so a declared `false` can never present as a truthy word.
  Observed RED first.
- **AC2** — When the turnstile is off and a beacon is PLANTED by hand, a run does not queue behind
  it and does not delete it, asserted in `tools/run-gates/run-gates.turnstile.test.sh` — the planted beacon survives, which is what
  distinguishes "disabled" from "reaped everything".
- **AC3** — When `GATE_TURNSTILE=1`, every existing turnstile arm still passes, asserted by running
  `tools/run-gates/run-gates.turnstile.test.sh` with that variable exported.
- **AC4** — When the turnstile is off, the run record's `queued` and `queued_from` keys are present
  and read `-` and `off`, asserted by reading the run record rather than the stream.
- **AC5** — When `bash tools/run-gates/adopt-run-gates.sh --check` runs against a freshly seeded
  target, the seeded declaration carries `turnstile = false`, asserted in
  `tools/run-gates/adopt-run-gates.test.sh`.
- **AC6** — When the profile line is printed, it names the turnstile state and where the value came
  from, asserted by grepping the first line of `bash tools/run-gates/run-gates.sh` captured output.

## 7. Gates

`run-gates turnstile` · `run-gates canary` · `run-gates gov canary` · `run-gates adopter e2e` ·
`run-gates wiring`. No new leg.

## 8. Open questions

- **F1 — should the turnstile arms run at all when the mechanism ships off?** A suite whose subject
  is disabled by default is a suite whose arms all take the enabled path via `GATE_TURNSTILE=1`, and
  that is a fixture that no longer resembles the shipped configuration. Recommendation: keep every
  arm and export the variable, AND add S5's arm for the shipped default, so the suite covers both
  states rather than only the one it was written for.
  RESOLVED (agent, 2026-08-31, delegated): both states. This is the `fixture-passes-by-finding-
  nothing` class read forward — a suite that only ever exercises the non-default path proves nothing
  about what ships.

## 9. Revision log

- rev-1 · 2026-08-31 · initial draft.
- rev-2 · 2026-08-31 · folded round-1 spec audit findings F18 and F19. rev-1's S2 prescribed
  substituting the declared value into a `!= 0` string test, which would have shipped the
  turnstile ENABLED on a declared `false` while every criterion stayed green — the inversion is
  now closed by marshalling and by AC1c. AC1b was added because no criterion proved the
  declaration enabled anything, which is the same could-not-fail shape this unit's own F1 names.

## 10. Reuse audit

The seam is `tools/run-gates/run-gates.sh:420` and `:726`, the two `[ "${GATE_TURNSTILE:-1}" != 0 ]`
guards — verified against source at this revision. Both take the declared value; nothing else in the
turnstile moves.

`python tools/memory-recall/query.py "why are gate ceilings enforced by default and why is the
run-gates turnstile beacon enabled by default" --terms "ceiling timeout leg manifest turnstile
beacon queue run-gates profile concurrency GATE_FULL selftest sharding adopter"` — 40 hits. The
design record is `memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md` and
the incident records are `TOOL-aBoundedCeiling-12` (6858 s behind three dead pids, cleared by hand)
and `memory/builds/aReapedTicket/`, whose whole subject is the queue's missing liveness. **A hit can
be stale, so the two open defects were re-read against source**: `ts_alive` still guards the beacon
alone, and `ts_try_reap` still ends in a bare `rm -rf`. Both remain OPEN and §3 says so.

No gov seam exists for "a declared default for a runtime mechanism" beyond the profile table, which
unit 2 is already generalising into `[bar]`. This unit adds a key to that table rather than a
mechanism.
