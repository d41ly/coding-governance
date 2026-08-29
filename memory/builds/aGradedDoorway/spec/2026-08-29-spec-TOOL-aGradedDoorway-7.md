# TOOL-aGradedDoorway-7 — fold the five expensive legs under a viable wall clock

**Status:** SPECCED · rev-1 · 2026-08-29 · node a · Tier-2 · base ffa01a07e · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Five legs cost 6.1 of the 6.7 hours a full `--editor` bar takes, and one of them costs 4 h 14 m
alone. Make them viable — an adopter's merge bar under 30 minutes and the full suite runnable at
all — without deleting a single assertion.

## 2. Scope (IN)

- **S1** — wire the sharding both unattended suites already ship. `check-unattended.test.sh` and
  `unattended.test.sh` each declare `SHARD_ARITY=2` and accept `--shard <i>/<n>`; the gate manifest
  invokes both bare. Emit one leg per shard.
- **S2** — raise `SHARD_ARITY` past 2 in both suites, which requires auditing each suite's HOIST SET
  (`check-unattended.test.sh` names its own: `anchor_break` and `anchor_restore`) so no arm depends
  on an arm in another shard.
- **S3** — the GATING MEASUREMENT this spec refuses to design past: instrument one `run()` on the
  suite's own fixture and split its ~57 s into process startup, git plumbing, and check bodies.
  Every remedy below is ranked by an inference from that number, and only S3 turns it into a fact.
- **S4** — batch arms by tree state where the mutations are provably independent: one `run()`, many
  assertions against the captured output. 197 of 265 runs currently feed exactly one assertion.
- **S5** — a per-suite budget declared in `tools/gate-legs.json` and enforced, so a leg that grows
  past it fails on cost rather than being discovered by a person six months later.
- **S6** — records: this spec, a decision row, and a backlog row per remedy not taken.

## 3. Non-goals (OUT)

- **Decomposing checks 1-27 so `--only <n>` accepts any n.** This was the author's first
  recommendation and the arithmetic in §4 kills it; it stays here as a rejected alternative with the
  number that rejects it, not as deferred work.
- **Deleting or thinning assertions.** 337 in one suite and 663 in another exist because something
  went wrong once. Cost is a scheduling problem, not a coverage problem.
- **Putting the `optIn` self-tests back on the merge bar.** They are `optIn` for the reason this
  spec measures. What they need is a scheduled run, not promotion.
- **Porting anything to a faster language.** The suites test shell behaviour through shell.
- **Adopter-side workarounds.** These are gov's files; an adopter patching them locally is the fork
  class `TOOL-aGradedDoorway-1` exists to end.

## 4. Design

### Inventory

Measured 2026-08-29 on a 16-core Windows/MSYS node, run `20260829T071408-1451497`, full `--editor`
bar, `INCMS_GATE_HEAVY_JOBS=1`, against the inCMS adopter at `0e956287a`.

| leg | seconds | share |
|---|---|---|
| `unattended-check-test` | 15270 | 63 % |
| `unattended-test` | 3665 | 15 % |
| `playbook-check-test` | 893 | 4 % |
| `unattended-check` | 664 | 3 % |
| `docs-hygiene-test` | 630 | 3 % |
| the other 57 legs | 3070 | 13 % |

Wall clock 24219 s against a leg sum of 24192 s. Those being equal is itself a finding: at
`INCMS_GATE_HEAVY_JOBS=1` the bar costs the SUM of its legs rather than its longest, so a 16-core
box runs one heavy leg at a time. The box measured 36 % CPU throughout — nothing was saturated.

Structure of the two dominant suites:

| suite | full-program runs | tree resets | assertions | shard support |
|---|---|---|---|---|
| `check-unattended.test.sh` | 265 | 268 | 337 | `SHARD_ARITY=2`, unused |
| `unattended.test.sh` | n/a | 252 | 663 | `SHARD_ARITY=2`, unused |

### Data model

The cost of `check-unattended.test.sh` is `265 × (reset_tree + one full 30-check run)`. `run()` is
`bash "$SCRIPT"` with no selector, and an arm cannot ask for less: the checker's only scope flag is
`--only 28`, which refuses anything else because "checks 1-27 share state and are one unit".

Two measurements decide the architecture, and they point in opposite directions from each other,
which is why both are recorded rather than only the convenient one.

**Checks are ADDITIVE on a real corpus.** On the inCMS corpus of 302 builds, `--only 28` costs 103 s
and `--skip 28` costs about 560 s against a full run of 664 s. 103 + 560 is 663. There is almost no
shared fixed cost at corpus scale, so "checks 1-27 share state" is a CORRECTNESS coupling and not a
performance one.

**But the suite does not run at corpus scale.** 15270 s over 265 runs is 57.6 s per run, on a
fixture holding about two builds. If corpus size drove the cost, two builds against 302 would put a
fixture run near 4 s. It is 57 s. **So roughly 53 s of every fixture run is fixed per-invocation
overhead** — process startup, git plumbing, and whatever each check pays before it looks at
anything.

That inference is what kills decomposition. Splitting the checker so each arm runs one check saves
the check BODIES, which at fixture scale are the small half. The lever that matters is the number of
INVOCATIONS, not their granularity. S3 exists because this paragraph is arithmetic on two measured
numbers rather than a third measured number, and the whole ranking below rests on it.

### Rollout

S1 first, because it is free and reversible: two manifest rows become four, and each suite already
implements the flag. S3 next, because it either confirms the ranking or overturns it before any
refactor is paid for. S4 and S2 follow the answer. S5 last, since a budget over a cost nobody has
finished changing would only ratchet in the current number.

### Files touched (estimate)

`tools/gate-legs.json`, `tools/unattended/check-unattended.test.sh`,
`tools/unattended/unattended.test.sh`, and this build's records. S3 adds a throwaway instrument
rather than a shipped file.

### Alternatives rejected

**Decompose checks 1-27 so any `--only <n>` works.** Rejected on the §4 arithmetic: at fixture scale
the check bodies are the small half, so a 30-way split does not buy 30×. It is also the largest and
riskiest change available — untangling shared state across 27 checks of a merge-bar checker — which
makes it the worst ratio of the five candidates. The author recommended this before doing the
division and records the reversal here rather than quietly dropping it.

**Replace `reset_tree` with a template-directory copy.** 268 resets, each a `git reset --hard` plus
`git clean -fd` plus ref surgery, is a real target. Rejected for now on two grounds: the git state
IS part of what several arms assert about (refs, HEAD, remote-tracking), so a copy may not reproduce
it faithfully; and on Windows a recursive copy of a `.git` directory is not obviously cheaper than a
reset. Revisit once S3 says how much of the 57 s is reset versus run.

**Run the suites in a Linux container on Windows nodes.** A spawn under MSYS costs roughly 20-50×
what it costs on Linux, and these suites are nearly pure spawn latency — the same suite is reported
at about 50 minutes upstream against 4 h 14 m here. Rejected as out of scope for a kit: it moves the
problem to every adopter's infrastructure rather than fixing the kit. Recorded because it is the
single largest factor and a reader deserves to know it was considered.

## 5. Production-readiness checklist

- security — N/A. No new surface; sharding changes scheduling, not what is asserted.
- perf / scale — the whole spec. The target is an adopter merge bar under 30 minutes.
- a11y — N/A, no interface.
- i18n — N/A, no user-facing strings.
- error / empty / loading states — a shard index out of range already refuses by name in both
  suites; S2 must keep that refusal exact when the arity moves.
- observability — S5's budget is the observability: a leg that grows past its declared cost fails
  loudly instead of being found by someone's afternoon.
- risks — S2 is the risky one. A shard split that separates an arm from the state another arm
  established produces a GREEN that proves nothing, which is worse than the slow bar it replaces.
  The HOIST SET audit is the control, and it must be observed failing before it is trusted.
- testing and left-shift gates — each suite is its own gate; S1 and S2 are verified by running both
  suites at every shard index and comparing the union of assertion counts against the unsharded run.
- migration / rollback — none. Reverting is restoring two manifest rows.
- help/ docs — N/A for adopters; the kit READMEs gain the shard invocation.

## 6. Acceptance criteria

- **AC1** — When the manifest emits one leg per shard for both suites, the union of assertions
  reported across shards equals the unsharded count exactly: 337 for `check-unattended.test.sh` and
  663 for `unattended.test.sh`. An assertion that appears in no shard is a silent coverage loss and
  must fail this criterion.
- **AC2** — When a full `--editor` bar runs at the default pool rather than `HEAVY_JOBS=1`, wall
  clock is strictly less than the sum of leg seconds. Today they are equal, which is the defect.
- **AC3** — When S3's instrument runs one `run()` of `tools/unattended/check-unattended.sh` against
  the fixture `tools/unattended/check-unattended.test.sh` builds, it reports the 57 s split into
  startup, git plumbing and check bodies, each as a measured number. No remedy after S3 may cite
  the §4 inference once this number exists.
- **AC4** — When `SHARD_ARITY` is raised, an arm deliberately moved into a shard that does not carry
  the state it depends on FAILS. Observed red before the raise is trusted.
- **AC5** — When a suite exceeds its declared budget in `tools/gate-legs.json`, the leg fails and
  names the budget and the measured cost.
- **AC6** — When the merge bar (no `optIn` legs) runs at the default pool, it completes in under
  30 minutes on a 16-core node.

## 7. Gates

`tools/unattended/check-unattended.test.sh`, `tools/unattended/unattended.test.sh` and
`tools/unattended/check-playbook.test.sh` at every shard index; `check-memory-hygiene.sh`;
`govkit selfcheck`. New gate: S5's per-leg budget.

## 8. Open questions

- **Does S3 confirm the ranking?** The §4 inference makes batching and sharding beat decomposition.
  If S3 finds the 57 s is mostly check bodies rather than fixed overhead, the ranking inverts and
  decomposition returns as the primary remedy. Recommendation: run S3 before committing to S4, and
  treat this spec's ordering as provisional until it lands. UNRESOLVED.
- **How far can `SHARD_ARITY` go before the HOIST SET blocks it?** Both suites declare 2. The
  ceiling is set by how many arms depend on state another arm establishes, which nobody has counted.
  Recommendation: count it as part of S2 and let the number decide, rather than picking an arity and
  discovering the coupling. UNRESOLVED.
- **Should the `optIn` self-tests get a scheduled runner?** They are off the merge bar for good
  reason, but `drift-audit-selftest` sat unrun long enough that a 12-arm breakage reached an adopter
  unnoticed. Recommendation: a scheduled run whose absence is itself reported, since a leg nobody
  runs is a leg that rots. UNRESOLVED.

## 9. Revision log

- rev-1 · 2026-08-29 · initial draft, written from the 62-leg timing run and two scope measurements.
  Records a reversal of the author's own earlier recommendation: decomposition was proposed verbally
  before the 15270/265 division was done, and is rejected in §4 on that arithmetic.

## 10. Reuse audit

No seam to wire through: this changes how existing suites are INVOKED, and both already implement
the mechanism. `SHARD_ARITY` and `--shard <i>/<n>` exist in `check-unattended.test.sh` and
`unattended.test.sh` today, complete with an out-of-range refusal, and the only thing missing is
`tools/gate-legs.json` calling them. S1 is therefore reuse in the strict sense — the affordance was
built, shipped, and never invoked. `tools/run-gates/` is the sibling that would host S5's budget,
since it already declares a wall-clock ceiling per leg.
