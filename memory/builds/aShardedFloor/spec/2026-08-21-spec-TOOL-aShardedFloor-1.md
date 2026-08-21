# TOOL-aShardedFloor-1 — record the turnstile queue wait in the run record

**Status:** OPEN · rev-1 · 2026-08-21 · node a · Tier-2 · base 36d0ad3b · streams tooling

## 1. Goal

The turnstile queue wait is printed to stdout and recorded nowhere, so a bar that spent 20 minutes
queued is indistinguishable afterwards from one that spent none. Record it in the run-record header
and the summary file, as a value and a state, without moving a single byte of the stdout line two
consumers already pin.

## 2. Scope (IN)

- **S1** — one wait string built ONCE, after the turnstile resolves, from variables already in
  scope, exactly as `PROF_LINE` is built once and emitted at several sites.
- **S2** — two paired header keys, `queued` and `queued_from`, following the header's own
  `value`/`_from` grammar (`base`/`base_from`, `full`/`full_from`, `profile_row`/`profile_from`).
  `queued_from` is a CLOSED four-word vocabulary: `held` · `expired` · `unresolved` · `off`.
- **S3** — the same string as its own line in `gate-last-summary.txt` on green runs, red runs, and
  the RED-only durable copy. Unconditionally: a line that is sometimes absent means two things.
- **S4** — one fidelity fix. `TS_WAITED` is not refreshed on the acquire path, so the recorded
  number understates by up to a full tick. Recording a number that is quietly wrong, and giving it
  durable authority, is worse than today's state where nobody can cite it at all.
- **S5** — four arms in `run-gates.turnstile.test.sh`, one per state, each observed RED against a
  staged break before it is believed.

## 3. Non-goals (OUT)

No new stdout bytes and no edit to the `gate queue: waited ${TS_WAITED}s` format string — it is
pinned by `profile_bar.py`'s `$`-anchored regex and by `run-gates.turnstile.test.sh`, and **if either
needs editing, this unit has been violated.** No `schema` bump. No new gate leg. No teaching
`profile_bar.py` to read the header: it launches the runner itself and already sees every wait it
can be in a position to see.

## 4. Design

The mechanism, its line numbers and the reasoning are §"Unit D" of
[the research record](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md), which is not restated
here. Three points bind the builder and are stated because they are where this unit goes wrong:

**The value is a dash when it is unmeasurable.** `-` for `off` and `unresolved`, the runner's own
idiom for an input it could not measure. This is the dead-probe rule applied to a wall clock: a `0`
emitted when the turnstile was disabled is a reassuring number about a probe that never ran.

**The keys go OUTSIDE the run-envelope printf block.** The four-key envelope arm selects by name, so
keys placed inside would leave that arm green and only its comment lying.

**`queued_from` earns its place on a TWO-way ambiguity, not three.** With `-` emitted for `off` and
`unresolved`, a `queued 0` can only mean held-and-uncontended, because an `expired` run requires
`n >= TS_MAXWAIT` which is `TS_TTL * 4`. The second key carries the `held`/`expired` split a bare
integer cannot, and separates `off` from `unresolved`.

## 5. Production-readiness checklist

- security — N/A: the header is already `chmod 600` and carries no new class of value.
- perf / scale — two printfs and one string; the leg it adds arms to is 232.5 s and the bar is
  floor-bound at 812–926 s, so span movement is zero by construction, not by measurement noise.
- a11y · i18n — N/A.
- error / empty / loading states — the whole point: `off` and `unresolved` emit a dash, never a zero.
- observability — this unit IS the observability fix.
- risks — the strongest temptation is appending the state word to the stdout line, which reds the
  very leg that measures the turnstile. The state lives in the header and the summary.
- testing + left-shift gates — four arms, four states, each with its staged break recorded.
- migration / rollback — additive keys; every reader selects by key name, so old readers are inert.
- user docs — `tools/run-gates/README.md`'s queue clause, which is now half the story.

## 6. Acceptance criteria

- **AC1** — a contended run's header carries `queued` > 0 and `queued_from` = `held`.
- **AC2** — an uncontended run carries `queued` 0 and `queued_from` = `held`, and that 0 equals the
  stdout line's number on the SAME run. The cross-check is the guard against the two emissions
  drifting and is the reason both are fed from one variable.
- **AC3** — a `GATE_TURNSTILE=0` run carries `queued` = `-` and `queued_from` = `off`, and a grep for
  a literal `queued<TAB>0` on that run returns nothing.
- **AC4** — a run that burned the bounded wait carries `queued_from` = `expired` with n > 0, observed
  on a purpose-built heartbeat-refresher fixture. The existing TTL fixture CANNOT reach this branch:
  it plants a static heartbeat, so the run reaps at t≈2 s against a `TS_MAXWAIT` of 4 and ends
  `held`. **If that fixture is cut, this criterion is cut with it and `expired` is named as an
  unarmed arm in the header's own "does NOT check" section.** Do not keep an acceptance bullet no
  fixture can reach.
- **AC5** — `git diff -U0` contains no hunk touching the `gate queue: waited` echo, and none touching
  the `schema` printf. Stated by CONTENT rather than by line number, because the fidelity fix shifts
  every line below it.
- **AC6** — the four-key run-envelope arm in `tools/run-gates/run-gates.evidence.test.sh` passes
  unmodified across both `tools/run-gates/gate-profiles.txt` rows.
- **AC7** — `gate-last-summary.txt` carries the line on green AND red runs, and the durable
  RED-only copy carries it too.
- **AC8** — each of the four arms observed RED against a staged break, with the RED text naming a
  literal slice of that arm's own failure message. For AC1's arm the break that matters is the
  UNDERSTATEMENT: keep the printfs, revert the fidelity fix, and confirm the arm reds on a stale
  value — not merely on an absent one. Witness: the staged-break RED text of
  `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC9** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` GREEN.

## 7. Gates

`bash tools/run-gates/run-gates.sh` diff-scoped, then full at the push boundary. Specifically:
`run-gates turnstile`, `run-gates evidence`, `run-gates canary`, `run-gates gov canary`,
`testsuite counts`, `codebase-map coverage + freshness`, `kickoff-manifest ratchet`, `memory hygiene`.
This unit adds no gate leg; it adds arms to a suite the manifest already runs.

## 8. Open questions

none — the two questions this unit had are RESOLVED and recorded here. (1) *Does `schema` bump?* No,
resolved by grep: the field has no reader, every real reader selects by key name, and a bump could
not be armed because nothing observes the field. Resolver: this session, under the standing
authority to settle forks the specs already state. A backlog row is owed: implement the predicate or
delete the field. (2) *Where do the arms live?* `run-gates.turnstile.test.sh`, not
`run-gates.evidence.test.sh`, because the latter carries `TOOL-aScannedThrottle-7`'s load-dependent
5-second bound and new fixtures there buy a flake in the leg that grades the run record.

## 9. Revision log

- rev-1 · 2026-08-21 · initial, from the design pass recorded at
  [`build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md`](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md).
  Four design lenses, then skeptics prompted to refute, then one synthesis; 13 of 16 design claims
  were refuted and corrected before this spec was written. The corrections that reached this unit:
  the header keys belong outside the envelope block, the `queued_from` justification is two-way and
  not three-way, and the `expired` state needs a fixture the existing suite cannot provide.

## 10. Reuse audit

**The seam is `PROF_LINE`** at `tools/run-gates/run-gates.sh:374-375` — one run-envelope fact that
several audiences need, built once as a string and emitted at several sites so the copies cannot
drift. `QUEUE_SUMMARY` is that same shape built at the turnstile's exit instead, for the one reason
`PROF_LINE` cannot absorb the wait: `PROF_LINE` is echoed BEFORE the turnstile block, and folding the
wait into it would delay the profile line by the entire queue wait. The second seam is the header's
own `value`/`_from` pairing — this is a fourth instance of a pattern that already has three.

**The probe declared its own blindness, and that refusal is the useful output.**
`python tools/codebase-map/reuse_lookup.py "record how long a run waited in a queue into its own run record"`
ranked 30 candidates, all python/js/dossier, and reported *"recall partial: layers bash have no
symbol extractor — a matching seam THERE would not appear above."* Every file this unit touches is
bash, so both seams above come from the hand check that refusal demands.

**Recall terms used**, because composing them is the expensive half and a reground re-runs the query:
`python tools/memory-recall/query.py "has this repo decided before how the gate run record records a wait, and what constrains adding a header key" --terms "run-record header key schema turnstile queue wait profile line summary gate-last-summary additive forward-compatible dispatch envelope"`
