# TOOL-aClosedDocket-3 — the bounded-observation arms assert on `RB_TOOK`, not the harness clock

**Status:** OPEN · rev-2 · 2026-08-31 · node a · Tier-2 · base 733552e1 · streams tooling · order 3 · ratified 2026-08-31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aClosedDocket-1.md](../prompts/2026-08-31-prompt-TOOL-aClosedDocket-1.md) | research | TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 |
| [2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md) | spec-audit | TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 |

<!-- /gen:spec-records -->

## 1. Goal

Make the arms that prove `run_bounded` reaches `check_wiring` and the `gates-green` site measure what
the bound measures. They currently time the whole verb from the harness, which includes process
start, git operations and a remote advertisement the bound does not govern, so they fail on a busy
machine while the mechanism they test is working.

## 2. Scope (IN)

- **S1** — the **TWO** arms in `tools/unattended/unattended.test.sh` that wrap a VERB in
  `_t0=$(date +%s) … _t1=$(date +%s)` and assert a ceiling — `:4696` over `--preflight` and `:4709`
  over `--close`, both at `-lt 25` — assert instead on what the DRIVER reports. Rev-1 said three;
  measured, there are four such wrappers and the other two (`:4651`, `:4661`, both `-lt 20`) wrap
  `run_bounded` DIRECTLY. Those two are already measuring inside the bound's own scope, are correct
  as they stand, and are N4.
- **S2** — where a verb's output does not carry that number, the arm asserts on the BREACH MESSAGE
  rather than on elapsed time. That the bound fired is the property under test; how long the
  surrounding harness took is not.
- **S3** — the arms keep a wall-clock assertion as an OUTER SANITY BOUND only, generous enough that
  it cannot fire on a loaded machine and present only to catch a hang, with a comment saying that is
  its whole job. A bound that can fire for two reasons cannot tell you which.
- **S4** — the comment on each arm records the measurement that motivated the change: `--preflight`
  at 35 s and `--close` at 44 s and 66 s against a 25 s assertion under cross-session load, clean on
  an unloaded run of the same shard on one unchanged tree.

## 3. Non-goals (OUT)

- **N1** — changing `run_bounded`, `RB_TOOK`, `GATE_BOUND` or any bound the driver enforces. The
  mechanism is correct; only the arms' choice of instrument is wrong, and `TOOL-aProvenReuse-6`
  measured exactly that.
- **N2** — skipping the arms when a sibling suite is running. It was one of the row's three options
  and it is the worst: a check that stands down under load stands down exactly when a timing defect
  would show.
- **N3** — a fleet-wide suite lock. Cross-session contention is real here, but serialising every
  worktree's suite to fix three assertions prices a lock against a comment.
- **N4** — the two DIRECT `run_bounded` wrappers at `:4651` and `:4661`, and every other
  `_t0=$(date +%s)` site in this suite. The direct wrappers already measure the bound's own scope,
  which is exactly what S1 is moving the other two TOWARD, so changing them would be a change away
  from the fix. None of the rest was measured flaking.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `tools/unattended/unattended.test.sh` | S1–S4 — the three arms and their comments |

### The instrument, and why it is the right one

`run_bounded` records its own elapsed at `tools/unattended/unattended.sh:193` (`RB_TOOK=$(( _e - _s ))`)
and the `gates-green` breach message already prints it. That number is measured INSIDE the bound's
own scope, so it excludes everything the bound does not govern — which is precisely the difference
between the 35 s the harness saw and the bound the driver honoured. Asserting on it is not a looser
test; it is a test of the same claim with the noise removed.

### What a reader must not conclude

That the arms were failing because the bound was broken. They were not: the
`did not answer within the declared` message fired on every one of the three failing runs, so the
bound was observed working each time it was reported violated. The arms disagreed with themselves,
and S2 is what removes the second, weaker claim.

### Alternatives rejected

- **Raising the margin.** The row's second option. It moves the flake without removing it, and the
  new number would be as unmotivated as 25 s was — a pin measured on one machine's load, which is
  `pin-copied-from-another-corpus` in time rather than in space.
- **Skipping under load.** N2.
- **Asserting on the driver's number AND keeping the tight wall clock.** That is
  `two-guards-one-question-two-answers`: two guards asking one question different ways, jointly
  unsatisfiable on a loaded machine, which is the state the suite is in today.

### Rollout

One commit. Test-only; no shipped behaviour moves.

## 5. Production-readiness checklist

- **Security** — N/A. A test file.
- **Performance** — unchanged; the arms run the same commands.
- **Error states** — S3's outer bound still catches a hang, and its comment says that is all it does.
- **Observability** — the failure text names the driver's own number, so a real breach reports the
  figure the bound saw rather than one an operator has to reconcile with it.
- **Testing** — the arms ARE the test. AC2 is what proves they can still fail.
- **Migration/rollback** — revert; test-only.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/unattended.test.sh --shard 2/2` passes on an unloaded machine, and
  passes again with at least one sibling suite running concurrently. The second run is the point:
  the arms flaked three times under exactly that condition and a single green run would not
  distinguish the fix from luck.
- **AC2** — with `run_bounded`'s `timeout` invocation in `tools/unattended/unattended.sh` neutered so
  the bound cannot fire, BOTH arms FAIL and each names the driver's reported figure. The artifact is
  named because rev-1's wording did not name one, and a break that is not named is not reproducible.
- **AC2a** — the same two arms also fail when their new assertion LINE is deleted outright. Round 1's
  H6: the arms carry pre-existing `hit` assertions on the breach message at `:4694` and `:4707`, so
  AC2 alone cannot tell a working new assertion from a deleted one — the `hit` would red either way.
  Deleting the line and observing a DIFFERENT failure is what separates them.
- **AC3** — no arm outside the three named in S1 changes, checked with
  `git diff --stat tools/unattended/unattended.test.sh` and by reading the diff. N4 is the scope
  boundary and this is its observable.
- **AC4** — `bash tools/unattended/check-unattended.sh` exits `0`, so the suite's own arm-count and
  message-literal gates still agree with the edited file.

## 7. Gates

`bash tools/unattended/run-unattended-gates.sh` and `bash tools/unattended/unattended.test.sh`, which
is where this unit lives; `unattended kit gate` on the bar for AC4.
What no gate here checks: that the machine was actually loaded during AC1's second run. That is an
observation this run makes and records, not a predicate — and it is why AC1 names the condition
rather than only the outcome.

## 8. Open questions

- **Q1 — does the suite have a message-literal gate that strands an arm when its text changes?**
  **FACT-QUESTION · RESOLVED (agent, 2026-08-31, delegated):** the probe is
  `bash tools/unattended/check-unattended.sh` before and after the edit, and the observation that
  decides it is whether it names a stranded arm. It can produce a negative — this repo's
  `arm-literal-strands-on-message-edit` class exists because it has fired — so the liveness half
  holds. Answered at build time, before the messages are edited.

## 9. Revision log

- rev-2 · 2026-08-31 · round-1 spec-audit fold. H5: rev-1 said three arms; measured, four wrappers
  exist and only TWO wrap a verb. The other two wrap `run_bounded` directly, already measure inside
  the bound's scope, and moved from unstated to N4. H6: AC2 named no artifact and could not be
  distinguished from deleting the assertion, because a pre-existing `hit` on the breach message reds
  either way — AC2 now names the artifact and AC2a is the discriminator.
- rev-1 · 2026-08-31 · authored by the aClosedDocket run.

## 10. Reuse audit

The seam is `RB_TOOK`, already set by `run_bounded` at `tools/unattended/unattended.sh:193` and
already carried in the `gates-green` breach message. Nothing is built: the arms stop instrumenting
from outside and read the number the mechanism under test already publishes. That is the whole unit,
and finding it is why `TOOL-aProvenReuse-6` could name three options without knowing which was cheap.

`python tools/codebase-map/reuse_lookup.py "recording a telemetry log line when a lookup tool runs so
a later check can observe it"` was the set's map probe; it returned no timing seam, which is correct
— this unit consumes one that already exists rather than adding one.

Recall terms used: `non-convergent review loop blocker promotion spec subject mechanism unit
disposition wall-clock timing assertion flake elapsed bound contention`. The timing half of that
query returned no prior record about instrumenting a bound from inside, so this is the first time the
question is answered in this corpus and the answer is recorded here rather than left in a commit
message.

Where a hit was STALE: none. `RB_TOOK`'s assignment and the breach message that carries it were both
read at source at writing time, rather than taken from the backlog row, which names the options
without naming the variable.
