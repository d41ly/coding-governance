# TOOL-aQuenchedHarness-8 — the turnstile stops reaping a live holder, so two bars stop running as one

**Status:** CLOSED · rev-3 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aQuenchedHarness-8-ticker-landed.md](../build/2026-09-06-build-TOOL-aQuenchedHarness-8-ticker-landed.md) | journal | — |
| [2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md](../build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md) | research | TOOL-aQuenchedHarness-2 |
| [2026-09-07-build-TOOL-aQuenchedHarness-8-acceptance-ledger-the-turnstile.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-8-acceptance-ledger-the-turnstile.md) | journal | — |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |

<!-- /gen:spec-records -->

## 1. Goal

Make the bar's heartbeat mean "this process is alive" rather than "a leg finished recently", so a bar
inside one long leg is not mistaken for a stalled one and reaped. Today it is reaped on every full
bar, the next bar then runs UNQUEUED alongside it, and the resulting contention is what turns an hour
of legs into the owner's six- and nine-hour stalls.

## 2. Scope (IN)

- **S1** — refresh the beacon heartbeat on a TIMER, from a background ticker started when the beacon
  is won, at a cadence derived from `TS_TTL` rather than declared again. **The ticker is DETACHED from
  job control** — `disown` immediately after the `&` — because the turnstile block and the dispatch
  pool are the SAME shell and an undetached ticker is a live job forever. Without the detach,
  `live()` at `run-gates.sh:1266` counts it, `GATE_JOBS=1` never satisfies
  `[ "$(live)" -lt "$JOBS" ]` at `:1275`, and the bare `wait` at `:1304` never returns: the unit that
  exists to stop the bar wedging would wedge every bar, starting with the documented serial rollback.
- **S2** — EVERY TICKER WRITE IS NONCE-GUARDED, the way `ts_release` already is. Each tick re-reads
  `$TS_DIR/nonce` and the ticker EXITS when it is missing or is not `$TS_NONCE`. The precedent is in
  the file being edited and carries its own rationale comment, so this is reuse rather than new
  mechanism.
- **S3** — a second, independent exit: the ticker exits when `kill -0 "$holder_pid"` fails. Belt and
  braces, because no trap runs on `SIGKILL` and `TS_DIR` resolves to the CONSTANT path
  `"$TS_COMMON/gate-bar-beacon"` that every later bar recreates. Without S2 and S3 a SIGKILLed
  holder's orphan refreshes its SUCCESSOR's heartbeat forever, disabling the stale-holder signal
  repo-wide — the "converts a recoverable wedge into a permanent one" outcome, arriving through the
  fix rather than being prevented by it.
- **S4** — the ticker's own death is OBSERVED, in both exit paths: after a normal run and after a run
  whose holder was SIGKILLed, no ticker process descended from that bar survives, asserted by pid.
  §5 says plainly that the release trap covers the signal-catchable exits only and that S2 and S3 are
  the backstop for the rest.
- **S5** — if the ticker cannot start, the run says the turnstile heartbeat is DEGRADED and continues,
  rather than proceeding with a bound nobody is refreshing. A reaper reading a heartbeat nothing
  writes is not a reaper.
- **S6** — re-derive `TS_TTL`'s meaning in the comment block that derives it. With a timer the bound
  is "how long may a live process go without ticking", not "how long can one leg take". The
  `ponytail:` comment naming the current cliff is REMOVED with the cliff.
- **S7** — **arm 4c of `tools/run-gates/run-gates.turnstile.test.sh` is rewritten IN THE SAME
  COMMIT.** S6 retires the comment that arm's only `nope` greps for, so leaving it would land a
  declarable red for the build to discover. That arm is the subject of open row
  `TOOL-aBoundedCeiling-8`, which records that both its branches are `ok` and it therefore CANNOT
  FAIL; this unit's S8 arms replace it and the wrap-up retires the row.
- **S8** — arms in `tools/run-gates/run-gates.turnstile.test.sh`: a holder inside a leg longer than
  `TS_TTL` is NOT reaped; a holder whose process is dead IS reaped; a holder whose ticker was killed
  but whose process lives is reaped after the TTL; a SIGKILLed holder's orphan does not refresh its
  successor's beacon; and a two-leg fixture bar at `GATE_JOBS=1` dispatches and completes under a hard
  outer timeout, asserted on ELAPSED TIME rather than on a message.

## 3. Non-goals (OUT)

- Not removing the stale-holder reap. A genuinely wedged holder must still be reapable, or one death
  wedges the repository — which is the failure the reap was added for, and which
  `TOOL-aBoundedCeiling-12` records costing a landing 6858 s.
- Not changing `TS_MAXWAIT`'s derivation from `TS_TTL`. It stays a declared multiple; only what the
  TTL MEANS changes.
- Not the queue-ticket half. `TOOL-aReapedTicket-4`'s two-waiters-both-delete race is a neighbouring
  defect with its own row and this unit does not absorb it.
- Not the per-leg ceiling or the whole-bar wall, which are units 2 and 1.
- Not making the long legs shorter. That is units 5, 6 and 7, and this unit must land whether or not
  they do: a bar of any length must not be reaped for running.

## 4. Design

### The defect, stated from source

`ts_hb` is defined at `tools/run-gates/run-gates.sh:444` and called at exactly one site, `:1150`,
which the code's own comment identifies as a leg completing. `TS_TTL` is `PROF_TIMEOUT * 3` when the
selected profile row declares a per-leg timeout, and every shipped row in
`tools/run-gates/gate-profiles.txt` declares `timeout=0`, so the fallback of `1800` is what every run
uses. The longest leg's last recorded reading is 3837 s. The reaper at `:472` therefore fires against
a live holder on any bar that runs it. Reproduced in
`memory/builds/aQuenchedHarness/build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md`
§7: a second bar printed `reaping the beacon of a stalled holder (heartbeat 13s old, ttl 6s)` while
the first was alive and working, and both ran.

### The fix, and the three ways it goes wrong

A timer decouples liveness (a property of the PROCESS, cheap to assert often) from progress (a
property of the WORK, which the ceiling and the wall are for). The reaper wants the first and is
reading the second. Three hazards, each with its own scope item because each was found by measurement
rather than by reasoning:

1. **Job control.** The turnstile and the pool share one shell — the runner's own comment at `:1203`
   says dispatch and report run from one shell "so this shell owns every worker and can BLOCK on
   `wait -n`". An undetached ticker is a permanent live job. S1.
2. **SIGKILL.** No trap runs on it, and the beacon directory path is constant, so an orphan tick
   lands on a successor's beacon. S2 and S3.
3. **The arm that watches this.** Arm 4c cannot fail today and greps for a comment S6 deletes. S7.

### The ticker was REJECTED before, and this unit overturns that rejection explicitly

`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md` rejects, in its
Alternatives, "a background ticker process refreshing the heartbeat on its own clock", on two
premises: **one more process per run on a machine measured as spawn-bound**, and **to maintain a
number a leg-sized TTL makes unnecessary**. Its analysis section "Why the reader loop is not a refresh
site" deliberately kept ONE refresh site so the TTL would be sized against a LEG rather than a gap.

**The second premise is refuted by measurement.** The TTL is not leg-sized: the fallback every run
uses is 1800 s and the longest leg is 3837 s, so the very sizing that rejection rests on does not hold
in this tree and has not for some time.

**The first premise survives and is PRICED rather than waved away.** At a cadence of `TS_TTL / 6` —
300 s at the shipped fallback — a bar whose wall clock is 4000 s ticks about 13 times. A tick is one
`sleep` and one `mv`, two spawns, at the 319 ms per-spawn cost measured on this node: about 8 s across
the run, plus one spawn for the ticker itself. Against a bar that makes tens of thousands of process
creations, that is under a quarter of one percent, and the same measurement is what S1's cadence
derivation is set from. `AGENTS.md` §6 requires a ratified record to be superseded rather than
silently reversed; this section and the wrap-up are that supersession.

### Inventory

- `ts_tick_start` / `ts_tick_stop` — the ticker's lifecycle verbs, beside `ts_hb`. Both were checked
  with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` before being written here;
  they are two NEW shell function definitions, so `.lexicon.conf`'s `VERB_OFFENDER_PIN` moves and its
  justification line moves with it, in the same commit.
- `TS_TICK_EVERY` — the refresh cadence, DERIVED from `TS_TTL` and not separately declared.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.turnstile.test.sh` (S8's arms AND arm 4c's
rewrite) · `.lexicon.conf` (the `VERB_OFFENDER_PIN` move and its justification) · one build record.

### Alternatives rejected

**Raising `GATE_TURNSTILE_TTL`** — rejected as the runner's own comment rejects it: a bigger fallback
only moves the same cliff further out, and it would have to move past the longest leg, which grows.

**Setting `timeout=` on the profile rows** — the remedy the runner's `ponytail:` comment names —
rejected on arithmetic: the per-leg timeout would have to exceed the longest leg, which puts `TS_TTL`
at three times that and `TS_MAXWAIT`, a declared `TS_TTL * 4`, near thirteen hours.

**Doing nothing, on the strength of the prior rejection** — rejected in the section above, which
records which premise is refuted and prices the one that survives.

## 5. Production-readiness checklist

- security — one more background process writing one file inside the existing beacon directory, and
  S2's nonce guard is what stops it writing into a directory that is no longer its own.
- perf / scale — priced in §4: about 8 s of spawn cost across a 4000 s bar, under a quarter of one
  percent.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — ticker-failed-to-start (S5), ticker-running, and no-beacon-held are
  three distinct states, each with its own line.
- observability — the DEGRADED line; the turnstile's existing reap messages are unchanged, so a reap
  after this lands is a real one.
- risks — a LEAKED ticker is the hazard and the release trap does NOT cover it: no trap runs on
  `SIGKILL`. S2's nonce guard and S3's pid check are the actual mitigations, and S4 observes both exit
  paths by pid rather than asserting them. Rev-1 claimed the trap was the mitigation; that was wrong
  and this line replaces it.
- testing + left-shift gates — S8's arms, each observed RED before landing, and S7's replacement of an
  arm that could not fail.
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
- **AC6** — When a two-leg fixture bar runs at `GATE_JOBS=1` under a hard outer timeout, it dispatches
  and completes, asserted on ELAPSED TIME. This is the arm that fails against a naive `&` ticker and
  passes with `disown`.
- **AC7** — When a holder is SIGKILLed and a successor bar claims the beacon, the successor's
  heartbeat goes stale within `TS_TTL` even though the orphan ticker is still on the process table,
  asserted by pid and with that pid printed in the failure message.
- **AC8** — When a normal run ends, and when a SIGKILLed run ends, no process started by
  `ts_tick_start` and descended from that bar survives, asserted by pid in both cases.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · every leg whose argv lies under `tools/run-gates/`, DERIVED from
`tools/gate-legs.json` rather than listed here — at HEAD that is `run-gates canary`,
`run-gates evidence`, `run-gates turnstile`, `run-gates gov canary`, `run-gates adopter e2e` and
`profile-bar selftest`, and the derivation is what keeps this line true when the set moves · the
`lexicon naming predicates` leg, which grades the two new `ts_*` definitions and the pin they move ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the Definition of Done, because this is kit
work and every leg above except the lexicon one is held.

## 8. Open questions

- **F1 — cadence.** RESOLVED (agent, 2026-09-06, delegated): `TS_TTL / 6`, derived rather than
  declared, so the pair cannot drift and this unit introduces no new constant — the same rule
  `TS_MAXWAIT` already follows. Six because a single missed tick must not trip the reap, and §4 prices
  the resulting spawn count against the premise that rejected this mechanism before.
- **F2 — does leg completion keep refreshing?** RESOLVED (agent, 2026-09-06, delegated): yes. Both
  writers assert the same fact and the ticker is strictly more frequent, so keeping the existing call
  costs nothing and removing it would be an unrelated edit inside the diff that fixes the reap.
- **F3 — does this unit close `TOOL-aBoundedCeiling-8`?** RESOLVED (agent, 2026-09-06, delegated):
  yes. That row names arm 4c as an arm both of whose branches are `ok`, and S7 rewrites exactly that
  arm because S6 deletes the comment its only `nope` greps for. The wrap-up retires the row and says
  which of this unit's arms replaced it.

## 9. Revision log

- rev-3 · 2026-09-07 · CLOSED. The turnstile serialises bars, observed IN THE WILD today rather than in a fixture: a sibling session's bar queued at position 1 and ran zero legs while this one ran 47. Five of its eight criteria are NOT RE-OBSERVED because the turnstile suite was killed part-way to free the box for a whole-bar measurement, and the ticker's own arms are among them — recorded as unrun, not as met.

- rev-1 · 2026-09-06 · initial draft. Added mid-build by an `--rescope --act add` amendment after the
  unit 2 probe uncovered the mechanism; the measurement is the research record named in §10.
- rev-2 · 2026-09-06 · folded spec-audit round 2, which was this unit's FIRST review — round 1 predated
  it. B1: the ticker is DETACHED, because it and the dispatch pool share one shell, so an undetached
  one makes `GATE_JOBS=1` hang before dispatching a leg and wedges the terminal `wait` at every width.
  B2: every tick is nonce-guarded and pid-checked, because no trap runs on `SIGKILL` and the beacon
  path is constant, so an orphan would refresh its SUCCESSOR's heartbeat forever — §5's rev-1 claim
  that the trap mitigated this was simply wrong. B8: the ticker is a RECORDED rejected alternative in
  `spec-TOOL-aPacedTurnstile-4`; §4 now cites that rejection, states which premise measurement
  refutes, and PRICES the one that survives. H2: S4 observes the ticker's own death by pid in both
  exit paths. H3: the two new `ts_*` definitions move `VERB_OFFENDER_PIN`, now in Files touched, and
  §7 names the lexicon leg. H4 and H5: S7 rewrites arm 4c in the same commit and F3 records that this
  closes `TOOL-aBoundedCeiling-8`. M1: §7's leg list is DERIVED and its HEAD value is six, not three.
  M2: §10 carries a real recall query for this unit's own subject.

## 10. Reuse audit

The seam is `tools/run-gates/run-gates.sh`'s existing turnstile — `ts_hb`, `ts_try_reap`, `ts_release`
and the nonce guard `ts_release` already carries, which S2 reuses verbatim rather than inventing.
`tools/codebase-map/reuse_lookup.py` returned `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the
affordance seam. The recall query for THIS unit's subject, run rather than inherited, returned four
load-bearing records: `spec-TOOL-aPacedTurnstile-4`, which REJECTED this exact mechanism and whose
premises §4 now addresses one by one; `TOOL-aBoundedCeiling-8`, which names arm 4c as unable to fail
and which F3 closes; `TOOL-aBoundedCeiling-12`, which records a killed bar wedging a landing for
6858 s and is why §3 refuses to remove the reap; and `TOOL-aReapedTicket-4`, whose two-waiters race is
a neighbouring defect §3 declines to absorb. Rev-1's §10 carried the build-wide recall line unchanged
and named no turnstile term, which is why it asserted those records were read while missing the one
that rejected its own design.

Recall terms used: `turnstile beacon heartbeat ttl reap stalled holder ticker nonce queue ticket
maxwait dispatch pool`
