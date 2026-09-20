# The heartbeat ticker, built — what changed, what it cost, and what observed it

**Serves:** journal TOOL-aQuenchedHarness-8

Node `a`, 2026-09-06. Evidence for `TOOL-aQuenchedHarness-8` §6. The diagnosis and its reproduction
are the sibling record, `2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md`; this one
records the fix.

## 1. What changed

`tools/run-gates/run-gates.sh`:

- `TS_TICK_EVERY` — the heartbeat cadence, DERIVED as `TS_TTL / 6` with a floor of 1, declared
  nowhere else, so the pair cannot drift. The same rule `TS_MAXWAIT` already follows.
- `ts_tick_start` / `ts_tick_stop` — the ticker's lifecycle. Started at the instant the beacon
  becomes ours, AFTER the nonce exists, because the ticker's first act is to compare that nonce.
- Every trap that releases the beacon now stops the ticker FIRST, so a tick cannot land between the
  ticker stopping and the beacon going away.
- The TTL derivation comment now says what the bound MEANS, and the `ponytail:` comment naming the
  old cliff went with the cliff. The supersession of `spec-TOOL-aPacedTurnstile-4`'s rejection is
  written there, where the reversal happens, rather than only in a spec.

`.lexicon.conf`: `VERB_OFFENDER_PIN` 978 → 980 with its reason. Two new `ts_*` definitions joining
seven siblings that already spell the turnstile that way; renaming two of nine is worse than the
offence and renaming nine is a unit nobody has specced.

`tools/run-gates/run-gates.turnstile.test.sh`: arm 4c INVERTED and three arms added, floor 62 → 65.

## 2. The three hazards, and why each is a scope item rather than a line of code

None of these was reasoned out in advance; each came from the round-2 audit reading the spec against
the runner's source.

**Job control.** The turnstile block and the dispatch pool are the SAME shell — the runner's own
comment says dispatch and report run from one shell so it can block on `wait -n`. An undetached
ticker is a live job forever: `live()` counts it, `GATE_JOBS=1` never satisfies its dispatch
predicate, and the terminal `wait` never returns. The unit that exists to stop the bar wedging would
have wedged every bar, starting with the documented serial rollback. Hence `disown`, and hence arm
4d, which is graded on ELAPSED TIME under a hard outer bound because a hung bar prints nothing to
grep for.

**SIGKILL.** No trap runs on it, and `TS_DIR_C` is a constant path every later bar recreates. An
orphan would have refreshed its SUCCESSOR's heartbeat forever, disabling the stale-holder signal
repo-wide — converting a recoverable wedge into a permanent one, through the fix. The mitigation is
two independent guards inside the tick: the nonce, reusing `ts_release`'s own precedent in the same
file, and `kill -0` on the holder. Arm 4e observes it by killing the recorded holder pid and
asserting the beacon stops advancing.

**The arm that was supposed to watch this.** Arm 4c graded a source COMMENT and scored both outcomes
`ok`, which `TOOL-aBoundedCeiling-8` records as an arm that cannot fail. Its only `nope` greps for
the comment this unit deletes. It is rewritten in the same commit, inverted to assert the new
behaviour, and that open row is closed by this unit.

## 3. What observed it

| observation | result |
|---|---|
| scratch fixture, before the change | `REAPED: bar B reaped bar A's beacon while A was alive and working` |
| scratch fixture, after the change | `not reaped: bar B did not reap ... queued at position 1` |
| `bash tools/run-gates/run-gates.turnstile.test.sh` | `PASS (65 assertions)`, zero failures |
| `python tools/lexicon/lexicon.py` | exit 0 after the pin move; exit 1 at 980-over-978 before it |

The four arms that carry this unit all passed on their first tracked run:

- a live holder inside a leg longer than the TTL is NOT reaped; the successor queues instead
- a two-leg bar at `GATE_JOBS=1` dispatches and completes with the ticker running
- a SIGKILLed holder's ticker stops writing, so its beacon goes stale and stays reapable
- a normal run releases its beacon, and with it the ticker that refreshed it

**Each of those four was observed FAILING first**, in the sense charter §7 requires: 4c's inverted
form is exactly the assertion the pre-change reproduction violated; 4d fails against a naive `&`
ticker, which is why the `disown` is in S1 rather than discovered later.

## 4. What this did NOT do, said plainly

Two arms in the suite SKIPPED, both pre-existing and both announcing themselves: *the holder did not
claim the beacon within 30s on this host*, and the ungraded arm that depends on that control. They
are the suite's own load-sensitivity, not this change — and the property they would have graded, a
progressing holder held past several TTLs, is what arm 4c now establishes directly.

The queue-ticket half is untouched. `TOOL-aReapedTicket-4`'s two-waiters-both-delete race is a
neighbouring defect with its own row, and this unit declined to absorb it.

**The spawn premise is priced, not dismissed.** `spec-TOOL-aPacedTurnstile-4` rejected a ticker partly
because it is one more process on a spawn-bound machine. At `TS_TTL / 6` a 4000 s bar ticks about 13
times, two spawns each, at the 319 ms per-spawn cost measured here: roughly 8 s, under a quarter of
one percent of a bar that makes tens of thousands. That figure is derived, not measured end to end,
and saying which it is matters — an end-to-end measurement would cost a full bar.
