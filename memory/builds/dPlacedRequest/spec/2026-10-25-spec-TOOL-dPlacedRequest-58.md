# TOOL-dPlacedRequest-58 — every attempt of the placed race starts with no handshake file an earlier attempt left

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 30 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md) | research | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-59 |
| [2026-10-25-build-TOOL-dPlacedRequest-58-deviation-581.md](../build/2026-10-25-build-TOOL-dPlacedRequest-58-deviation-581.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-59 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md`)
confirmed **finding 20 at HIGH**, its item **H2**, which holds no other finding.
`TOOL-dPlacedRequest-52` §4's race sketch ends each attempt `touch $h/release; wait for A (bound);
clear $h/once $h/held $h/release`. `TOOL-dPlacedRequest-56` §4 restates that sketch for its fresh
attempts and drops the clear, and 56 S3 names only the clone, the bare remote and the stored files as
per-attempt fresh state. `$h` is the arm's handshake directory, outside the unit-19 clone
(`TOOL-dPlacedRequest-48` S1 and §4), so a fresh clone does not reset it. 48's stub holds only when
`mkdir "$h/once"` succeeds: on attempt 2 the stale `$h/once` means A never holds, and the stale
`$h/held` makes the arm's wait return at once, so B runs against an A outside its window. 56 AC3
forces exactly that retry by delaying B 11 s on attempt 1, so it judges an unplaced race. This unit
repairs `TOOL-dPlacedRequest-56`, at order 29, so it sits at order 30: each attempt resets the
handshake and proves it did before A starts.

## 2. Scope (IN)

- **S1** — The reset restored. After A is waited for, or killed and waited for at its bound, the arm
  clears `$h/once`, `$h/held` and `$h/release`. 56 S3 names `$h` among the per-attempt fresh state,
  56 §4's sketch carries the clear as 52 §4 has it, and 52 S4 and §4, as 56's pass restates them,
  keep it. The built arm in `tools/unattended/unattended.test.sh` carries it. Observed by AC1 and
  AC2.
- **S2** — The reset asserted. Before each attempt's A starts, the arm fails `request race state not
  reset` when any of the three exists, so a `$h/held` the arm then sees was written by this attempt's
  A. 56 AC3 names that line as its red. Observed by AC1.

## 3. Non-goals (OUT)

- No change to the stub, its bounds or its write set: `TOOL-dPlacedRequest-48`'s.
- No change to the fresh clone, the discard bound or the health-log read: 56 S3 and S4, and the absent
  log's value is finding 22's item of `TOOL-dPlacedRequest-59`.
- No new bug-class record: `memory/gotchas/fixed-sleep-does-not-place-a-signal.md` names the class of
  a race judged without its placement, and the closing review's left-shift decides any other
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-56` — S3, §4's per-attempt sketch, AC3 and the arm its pass builds, which this unit gives the handshake reset; without them there are no retried attempts to reset
- **consumes-from** `TOOL-dPlacedRequest-52` — S4 and §4's race sketch as unit 56 restates them, which keep the clear
- **consumes-from** `TOOL-dPlacedRequest-48` — the stub's write set, `$h/once` and `$h/held`, which S2's assertion names whole beside the arm's own `$h/release`
- **hands-off** `TOOL-dPlacedRequest-59` — 56 §4's per-attempt sketch and the arm with the reset, in which that unit's item for finding 22 sets the absent health log's count

## 4. Design

### The placed race, per attempt, as this unit leaves it

```
attempt 1..3:
  any of $h/once $h/held $h/release present -> fail "request race state not reset"
  fresh unit-19 clone and bare remote; m = lines in the health log
  A in background; wait for $h/held (30 s bound), else fail "request race never placed"
  stamp th; B to its end; stamp tb
  touch $h/release; wait for A (bound), else kill A and wait
  clear $h/once $h/held $h/release
  tb - th <= NODE_LOCK_BOUND and no node-lock-broken past line m -> judge AC1's asserts, stop
  else -> discard this attempt
every attempt overran -> fail "request race placed past the lock bound"
```

The three paths are the whole handshake: the stub writes `once` and `held` (48 S1) and the arm
writes `release`. The assertion runs on attempt 1 too, where it reads a fresh `$h`.

### Evidence

- 52 §4 "The placed race, bounded" holds `clear $h/once $h/held $h/release`; 56 §4 "The placed race,
  per attempt (S3, S4)" holds no `clear`. Read 2026-10-25.
- 48 S1: the stub's first call under `requests/` takes `mkdir "$h/once"`, touches `$h/held` and waits
  for `$h/release`; `mkdir` on an existing directory fails, so a stale `once` skips the hold.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md`: S3, §4, AC3 and its
  §9 line
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md`: S4, §4 and its §9
  line
- `tools/unattended/unattended.test.sh`: the placed-race arm

### Alternatives rejected

- **A fresh `$h` per attempt.** 48 §4 gives the arm and its stub one `$h`, so a new directory would
  have to reach the stub each attempt, for the same three paths the clear removes.
- **`$h/held`'s mtime against the attempt's start stamp (the review's AC3 extension).** S2's absence
  assertion implies it, with no clock and no `stat` resolution to trust.

## 5. Production-readiness checklist

- security — none in product: the handshake lives in the arm's scratch directory.
- perf / scale — three `rm -f`-sized removals and one existence test per attempt.
- error / empty / loading states — a leftover handshake fails the arm, named (S2).
- observability — the failure line names the reset, never a lock defect.
- risks — an A killed at its bound leaves its stub child polling `$h/release`, which the arm touched
  before the wait, so the stub ends within its own bound.
- testing — the probes of §6 and the arm of §7.
- migration — none: the arm is new in this build.
- user docs — none: test code and criteria.

## 6. Acceptance criteria

- **AC1** — When 56's placed-race arm runs with B delayed 11 s on attempt 1 only, attempt 2's A holds
  and the arm passes; a scratch copy of the arm without the clear fails `request race state not
  reset` on attempt 2; and 56's AC3 bullet names `request race state not reset`.
  Red when: an attempt starts over the last one's handshake and judges a race it never placed.
  fixture: unit 19's clones, built by the arm.
- **AC2** — When the race sketches of 52 §4 and 56 §4 are each extracted from their `### The placed
  race` heading to the next `###` and squeezed by `tr -s '[:space:]' ' '`, each holds `clear $h/once
  $h/held $h/release`, and 56's S3 bullet names `$h`.
  Red when: a spec restating a sibling's sketch drops a line of it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 · the reset and its assertion, staged against a copy of the arm without the clear · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How does each attempt start with no handshake file (S1)?** (a) Clear the three paths after A
  ends, as 52 §4 has it, and assert their absence before A starts; (b) a fresh `$h` per attempt. (b)
  must carry a new directory to the stub each attempt for the same three paths. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound, with the absence assertion as its
  observation. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-5 promotions, finding
  20 (HIGH, item H2).
- rev-2 · 2026-10-25 · S1 reworded "removes" to "clears": it empties the arm's scratch handshake
  per attempt and retires no named thing, so it owes no **Readers:** clause (hygiene check 25).

## 10. Reuse audit

The seam extended is 52 §4's own reset line, restored where 56 restated the sketch without it, and the
arm unit 56 builds. `python tools/codebase-map/reuse_lookup.py "clear the handshake files a stub wrote
before the next retry attempt"` ranked `before`, `corpus_files` and `ask_filed_in`, name stems only,
none a retry reset: no existing seam fits beyond the arm itself. `python tools/memory-recall/query.py
"how does a retried race attempt reset the handshake files its stub left"` returned
`TOOL-dPlacedRequest-48`, this audit's H2, `TOOL-dPlacedRequest-52` and `TOOL-dPlacedRequest-56`, the
units this one reads; none disagrees with source.

Recall terms used: placed race retry attempt handshake stub held once release reset fresh clone
