# TOOL-aQuenchedHarness-8 — the turnstile stops reaping a live holder, so two bars stop running as one

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md](../build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md) | research | TOOL-aQuenchedHarness-2 |

<!-- /gen:spec-records -->

## 1. Goal

Make the bar's heartbeat mean "this process is alive" rather than "a leg finished recently", so a bar
inside one long leg is not mistaken for a stalled one and reaped. Today it is reaped on every full
bar, the next bar then runs UNQUEUED alongside it, and the resulting contention is what turns an hour
of legs into the owner's six- and nine-hour stalls.

## 2. Scope (IN)

- **S1** — refresh the beacon heartbeat on a TIMER, from a background ticker started when the beacon
  is won and reaped with it, at a cadence derived from `TS_TTL` rather than declared again.
- **S2** — the ticker is the ONLY new liveness writer; leg completion may keep refreshing, because
  two writers of the same fact are harmless where both mean the same thing and one is strictly more
  frequent. What must not survive is the leg-completion site being the only one.
- **S3** — the ticker's own death must be observable: if it cannot start, the run says the turnstile
  heartbeat is degraded and continues, rather than proceeding with a bound nobody is refreshing. A
  reaper that reads a heartbeat nothing writes is not a reaper.
- **S4** — re-derive `TS_TTL`'s meaning in the comment block that derives it. With a timer the bound
  is "how long may a live process go without ticking", which is a small number, not "how long can one
  leg take", which is unbounded. The `ponytail:` comment naming the current cliff is REMOVED with the
  cliff, not left standing beside a fix.
- **S5** — arms in `tools/run-gates/run-gates.turnstile.test.sh`: a holder inside a leg longer than
  `TS_TTL` is NOT reaped; a holder whose process is dead IS reaped; a holder whose ticker was killed
  but whose process lives is reaped after the TTL, because that is the state the bound is for.
- **S6** — the measurement is recorded: the same fixture, before and after, showing a second bar
  acquiring while the first still holds, and not acquiring after.

## 3. Non-goals (OUT)

- Not removing the stale-holder reap. A genuinely wedged holder must still be reapable, or one death
  wedges the repository — which is the failure the reap was added for.
- Not changing `TS_MAXWAIT`'s derivation from `TS_TTL`. It stays a declared multiple; only what the
  TTL MEANS changes.
- Not the per-leg ceiling or the whole-bar wall, which are units 2 and 1.
- Not making the long legs shorter. That is units 5, 6 and 7, and this unit must land whether or not
  they do: a bar of any length must not be reaped for running.

## 4. Design

### The defect, stated from source

`ts_hb` is defined at `tools/run-gates/run-gates.sh:444` and called at exactly one site,
`:1150`, which the code's own comment identifies as a leg completing. `TS_TTL` is
`PROF_TIMEOUT * 3` when the selected profile row declares a per-leg timeout, and every shipped row
in `tools/run-gates/gate-profiles.txt` declares `timeout=0`, so the fallback of `1800` is what every
run actually uses. The longest leg's last recorded reading is far above that. The reaper at `:472`
therefore fires against a live holder on any bar that runs it.

The runner already names this in a `ponytail:` comment beside the derivation, and names the remedy as
setting `timeout=` on the profile row. That remedy is not taken here and the reason is arithmetic:
the per-leg timeout would have to exceed the longest leg, which drives `TS_TTL` to three times that
and `TS_MAXWAIT` to twelve, so the queue's fail-open would move to half a day. Raising the constant
moves the cliff; it does not remove it.

### The fix

A timer decouples the two facts that are currently conflated. Liveness is a property of the PROCESS
and is cheap to assert every few seconds. Progress is a property of the WORK and is what the per-leg
ceiling and the whole-bar wall are for. The reaper wants the first and is reading the second.

### Inventory

- `ts_tick_start` / `ts_tick_stop` — the ticker's lifecycle verbs, beside `ts_hb`.
- `TS_TICK_EVERY` — the refresh cadence, DERIVED from `TS_TTL` and not separately declared.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.turnstile.test.sh` · one build record.

### Alternatives rejected

Raising `GATE_TURNSTILE_TTL` was rejected as the runner's own comment rejects it: a bigger fallback
only moves the same cliff further out, and it would have to move past the longest leg, which grows.
Setting `timeout=` on the profile rows was rejected on the arithmetic above.

## 5. Production-readiness checklist

- security — N/A: one more background process writing one file inside the existing beacon directory.
- perf / scale — one sleeping process per bar; the write is a rename of a few bytes.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — ticker-failed-to-start is a named, reported state (S3), distinct
  from ticker-running and from no-beacon-held.
- observability — the degraded state prints; the turnstile's existing reap messages are unchanged, so
  a reap after this lands is a real one.
- risks — a LEAKED ticker would refresh the heartbeat of a dead holder forever, which is strictly
  worse than today: it converts a recoverable wedge into a permanent one. The ticker is therefore
  bound to the holder by the same trap that releases the beacon, and S5's third arm exercises the
  ticker-dead-holder-alive case explicitly.
- testing + left-shift gates — S5's arms, each observed RED before landing.
- migration / rollback — reverting the two verbs restores today's behaviour exactly; no state format
  changes and the beacon files are unchanged.
- user docs — `AGENTS.md`'s bar section gains one sentence about what the heartbeat now means.

## 6. Acceptance criteria

- **AC1** — When a fixture leg runs longer than `TS_TTL` while a second bar waits, the second bar does
  NOT print `reaping the beacon of a stalled holder`, and acquires only after the first releases.
- **AC2** — When the holder's process is killed outright, a waiting bar still reaps its beacon, so the
  wedge-recovery the reap exists for survives — the arm in
  `tools/run-gates/run-gates.turnstile.test.sh` observes both directions.
- **AC3** — When the ticker is killed but the holder lives, the beacon goes stale and is reaped after
  `TS_TTL`, proving the bound still binds something rather than being defeated by the fix.
- **AC4** — When `ts_tick_start` cannot start, `bash tools/run-gates/run-gates.sh` prints that the
  turnstile heartbeat is degraded, rather than running with an unrefreshed bound.
- **AC5** — When the before/after fixture recorded in
  `memory/builds/aQuenchedHarness/build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md`
  is replayed, the second-bar acquisition happens before the fix and does not happen after it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `run-gates turnstile`, `run-gates canary` and
`run-gates evidence`, the three held suites that grade this file · `GATE_SELFTESTS=1 bash
tools/run-gates/run-gates.sh` at the Definition of Done, because this is kit work.

## 8. Open questions

- **F1 — cadence.** RESOLVED (agent, 2026-09-06, delegated): derive it from `TS_TTL` rather than
  declare it, so the pair cannot drift and this unit introduces no new constant — the same rule
  `TS_MAXWAIT` already follows in the block above it.
- **F2 — does leg completion keep refreshing?** RESOLVED (agent, 2026-09-06, delegated): yes. Both
  writers assert the same fact and the ticker is strictly more frequent, so keeping the existing call
  costs nothing and removing it would be an unrelated edit inside the diff that fixes the reap.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft. Added mid-build by an `--rescope --act add` amendment after the
  unit 2 probe uncovered the mechanism; the measurement is the research record named in §10.

## 10. Reuse audit

The seam is `tools/run-gates/run-gates.sh`'s existing turnstile — `ts_hb`, `ts_try_reap`,
`ts_release` and the trap that arms at the instant the beacon becomes ours. Nothing new is
introduced: the ticker is a second caller of the EXISTING `ts_hb`, bound to the EXISTING release
trap. `tools/codebase-map/reuse_lookup.py` returned `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates]
as the affordance seam, carrying decisions `TOOL-aPacedTurnstile-1` through `-16`, which are this
turnstile's own record and were read before writing. The defect was found by probing
`TOOL-aQuenchedHarness-2` §8 F1, and the measurement is
`memory/builds/aQuenchedHarness/build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md`.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
