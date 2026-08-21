# TOOL-aShardedFloor-1 — record the turnstile queue wait in the run record

**Status:** CLOSED · rev-2 · 2026-08-21 · node a · Tier-2 · base 36d0ad3b · streams tooling

## 1. Goal

The turnstile queue wait is printed to stdout and recorded nowhere, so a bar that spent 20 minutes
queued is indistinguishable afterwards from one that spent none. Record it in the run-record header
and the summary file, as a value and a state, without moving a single byte of the stdout line two
consumers already pin. **Discharges `TOOL-aScannedThrottle-2`**, whose subject is this verbatim.

## 2. Scope (IN)

- **S1** — one wait string built ONCE, after the turnstile resolves, from variables already in
  scope, exactly as `PROF_LINE` is built once and emitted at several sites.
- **S2** — two paired header keys, `queued` and `queued_from`, following the header's own
  `value`/`_from` grammar (`base`/`base_from`, `full`/`full_from`, `profile_row`/`profile_from`).
  `queued_from` is a CLOSED four-word vocabulary: `held` · `expired` · `unresolved` · `off`.
  **Three are reachable by a fixture; `unresolved` is not** — see AC10.
- **S3** — the same string as its own line in `gate-last-summary.txt` on green runs, red runs, and
  the RED-only durable copy. Unconditionally: a line that is sometimes absent means two things.
- **S4** — one fidelity fix, **GUARDED**. `TS_WAITED` is last refreshed inside the wait loop and the
  acquire path breaks without refreshing, so a CONTENDED run understates by up to a full tick.
  Refresh before that break **only when the run actually queued**, predicated on `ts_announced`.
  Taken UNCONDITIONALLY, as the design brief prescribes, it breaks this unit's own §3: on an
  uncontended acquire the first loop iteration spawns `ls`, `sort`, `head`, `basename` and `mkdir`
  before the claim resolves, `ts_now` truncates to whole seconds, and that window sometimes crosses
  a second boundary — after which stdout reads `waited 1s` where an arm asserts
  `^gate queue: waited 0s$`. Measured on this node: 4 of 60 first-iteration acquires crossed, before
  load, and this leg runs inside a concurrent bar where process creation is 25x slower.
  **The residual, named rather than hidden:** when the first iteration reaps a stale holder, the
  reap path skips both the refresh and the announce, so the understatement this item exists to fix
  survives there. Closing it needs a second predicate and is NOT in this unit.
- **S5** — arms in `run-gates.turnstile.test.sh`, one per REACHABLE state plus the uncontended-zero
  control, each observed RED against a staged break before it is believed. Its `FLOOR_ASSERTIONS`
  rises to a stated ABSOLUTE value: the suite compares with `-ge`, so arms left under an unraised
  floor are stranded rather than red.
- **S6** — `tools/run-gates/README.md`'s queue clause, which is now half the story.

## 3. Non-goals (OUT)

No new stdout bytes and no edit to the `gate queue: waited ${TS_WAITED}s` format string — it is
pinned by `profile_bar.py`'s `$`-anchored regex and by `run-gates.turnstile.test.sh`, and **if either
needs editing, this unit has been violated.** No `schema` bump. No new gate leg. No teaching
`profile_bar.py` to read the header: it launches the runner itself and already sees every wait it
can be in a position to see. No fix to the reap-path residual S4 names.

## 4. Design

The mechanism, its line numbers and the reasoning are §"Unit D" of
[the research record](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md), which is not restated
here, **except that S4's guard OVERRIDES what that section prescribes.** Three points bind:

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
- risks — two. Appending the state word to the stdout line reds the very leg that measures the
  turnstile; the state lives in the header and the summary. And the fidelity fix taken
  unconditionally makes an UNCONTENDED run's value nondeterministic — S4's guard is the
  mitigation, written into scope rather than left to the builder.
- testing + left-shift gates — four arms, four states, each with its staged break recorded.
- migration / rollback — additive keys; every reader selects by key name, so old readers are inert.
- user docs — `tools/run-gates/README.md`'s queue clause, which is now half the story.

## 6. Acceptance criteria

- **AC1** — a contended run's header carries `queued` > 0 and `queued_from` = `held`, graded as a
  RANGE the harness itself observed — above 0 and at most the elapsed the fixture measured — never
  a tick-exact number, because `tools/run-gates/run-gates.turnstile.test.sh` documents its own
  timing sensitivity.
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
- **AC4b** — **the S4 guard, observed.** Across repeated runs a first-iteration UNCONTENDED
  acquire still reports `waited 0s` on stdout and `queued 0` in the header. This is what
  distinguishes the guarded fix from the brief's unguarded one; without it the unit ships a flake
  in the very arm §3 forbids touching.
- **AC5** — `git diff -U0` contains no hunk touching the `gate queue: waited` echo, and none touching
  the `schema` printf. Stated by CONTENT rather than by line number, because the fidelity fix shifts
  every line below it.
- **AC6** — the four-key envelope arm in `tools/run-gates/run-gates.evidence.test.sh` passes
  unmodified for both `tools/run-gates/gate-profiles.txt` rows THAT ARM exercises, `capable` and
  `minimal`. The table has three rows; `modest` is deliberately not exercised — a stated skip,
  never coverage.
- **AC7** — `gate-last-summary.txt` carries the line on green AND red runs, and the durable
  RED-only copy carries it too.
- **AC8** — each of the four arms observed RED against a staged break, with the RED text naming a
  literal slice of that arm's own failure message. For AC1's arm the break that matters is the
  UNDERSTATEMENT: keep the printfs, revert the fidelity fix, and confirm the arm reds on a stale
  value — not merely on an absent one. Witness: the staged-break RED text of
  `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC9** — `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.turnstile.test.sh` is raised to a
  stated ABSOLUTE value covering the new arms. Absolute, not a delta, because
  `TOOL-aShardedFloor-4` raises the same pin and whichever lands second must state the number it
  expects.
- **AC10** — `unresolved` is declared UNARMED in the suite header with its reason: reaching it
  needs the common-dir resolution to fail while the runner is already past its own repo guard,
  and breaking a linked worktree's `commondir` makes `git rev-parse --show-toplevel` fail too, so
  the runner exits 2 first. No fixture in that suite can produce it. This applies AC4's own rule
  to the state AC4 did not cover.
- **AC11** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` GREEN.

## 7. Gates

`bash tools/run-gates/run-gates.sh` diff-scoped, then full at the push boundary. Specifically:
`run-gates turnstile`, `run-gates evidence`, `run-gates canary`, `run-gates gov canary`,
`testsuite counts`, `codebase-map coverage + freshness`, `kickoff-manifest ratchet`, `memory hygiene`.
**This unit adds no manifest row, no descriptor row and no new checking surface** — only arms to a
suite the manifest already runs, and one raised floor.

## 8. Open questions

none — the forks below are RESOLVED.

(1) *Does `schema` bump?* NO, resolved by grep: the field has no reader, every real reader selects by key name, and a bump could
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
- rev-2 · 2026-08-21 · M4 spec audit folded, record [`reviews/2026-08-21-review-TOOL-aShardedFloor-1.md`](../reviews/2026-08-21-review-TOOL-aShardedFloor-1.md), verdict BLOCKED, 40 confirmed of
  65. The blocker against this unit was **F2**: S4's fidelity fix, taken as the brief prescribes,
  makes an uncontended run's queue value nondeterministic and flakes the byte-pinned arm §3
  declares this unit violated for touching. The guard, its predicate and its named residual are
  now IN scope, and AC4b observes it. Also folded: `unresolved` is unreachable and is declared
  unarmed (F14); the turnstile floor must rise to a stated absolute (F13); AC6 attributed the
  two-ness to the ARM rather than to the profile table, which has three rows (F23); the
  discharged backlog row is named (F21); AC1 is graded as a range (F2); and §8's resolutions are
  re-marked in the template's grammar (F11).

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
