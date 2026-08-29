# TOOL-aGradedDoorway-7 — fold the five expensive legs under a viable wall clock

**Status:** INPROGRESS · rev-3 · 2026-08-29 · node a · Tier-2 · base ffa01a07e · streams tooling · ratified 2026-08-29

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Five legs cost 6.1 of the 6.7 hours a full `--editor` bar takes, and one of them costs 4 h 14 m
alone. Make them viable — the full suite runnable at all, and the cost of any leg declared rather
than discovered — without deleting a single assertion.

**rev-1 asked for something else, and it was already true.** It set the goal as "an adopter's merge
bar under 30 minutes". A concurrent measurement in the adopter refuted the premise: the 254-minute
run needed TWO non-default operator choices, `--editor` (which re-selects 24 `optIn` legs worth
21 913 s) and `INCMS_GATE_HEAVY_JOBS=1` (which overrides the shipped default of 4). The bar the
pre-push hook actually runs is 38 legs, 2 279 s of leg-sum, floor 664 s, modelling to **16.7 min at
the shipped default width, and identically 16.7 min at width 8 and 16** — floor-bound from width 4
upward, and already inside the limit. There was no merge-bar crisis. There was a flag.

## 2. Scope (IN)

- **S1** — REFRAMED at rev-3, and the original wording was wrong about this repo. It said "the gate
  manifest invokes both bare", which is false for gov: `tools/gate-legs.json` does not carry either
  suite at all, and `tools/unattended/run-unattended-gates.sh:90-91` states that it runs them
  unsharded **on purpose**, because that is the only place a whole-suite claim is made. The manifest
  invoking them bare is the ADOPTER's. What is genuinely gov's to fix is that the shard-join
  predicate lives in `tools/run-gates/run-gates.gov.test.sh:346-403`, the suite explicitly allowed
  to hold claims about this repository — so an adopter who shards a kit suite gets no join
  enforcement at all. BUILT downstream as `ARCH-aBridledVintage-8` S4 and S5, whose
  `scripts/check-shard-join.py` is that predicate ported; the upstream item is to ship it with the
  kit rather than with the canary.
- **S2** — raise `SHARD_ARITY` to 8 in both suites and fix what breaks, per the owner's ruling of
  2026-08-29. The HOIST SET audit is NOT the control here and the spec should not pretend it is:
  AC1 is. A shard that silently drops arms fails the assertion-count identity whatever the split, so
  the empirical route is safe for the reason the criterion exists rather than because the split was
  reasoned about first. Each suite's declared hoist set (`check-unattended.test.sh` names
  `anchor_break` and `anchor_restore`) is the first place to look when one does break. **Ordered
  AFTER S4 at rev-3, on S3's answer.**
- **S3** — BUILT. The gating measurement this spec refused to design past. Recorded in
  `build/2026-08-29-build-TOOL-aGradedDoorway-7-1-s3-cost-split.md`.
- **S4** — batch arms by tree state where the mutations are provably independent: one `run()`, many
  assertions against the captured output. 197 of 265 runs currently feed exactly one assertion.
  **Promoted to the primary remedy at rev-3**, because S3 measured invocations at 90.5 percent of
  the cost and S4 is the only item that removes invocations rather than redistributing them.
- **S5** — a per-suite budget declared in the manifest and enforced, so a leg that grows past it
  fails on cost rather than being found by a person six months later. BUILT downstream as
  `ARCH-aBridledVintage-8` S1 to S3, using gov's own mechanism: a per-row bound falling back to a
  profile default (`tools/run-gates/run-gates.sh:1103-1104`) executed through a file rather than a
  pipe with `timeout -k 5s` (`:1109-1110`). Gov declares a ceiling on 86 of 86 legs already, so
  nothing is owed upstream except the observation that an adopter had none.
- **S6** — records: this spec, a decision row, and a backlog row per remedy not taken.
- **S7** — a scheduled runner for the `optIn` self-tests whose ABSENCE is itself reported, per the
  owner's ruling of 2026-08-29. The failure this closes is not a red: `drift-audit-selftest` sat
  unrun long enough that a twelve-arm breakage reached an adopter unnoticed, and silence was
  indistinguishable from health. BUILT downstream as `ARCH-aBridledVintage-8` S6 in its reporting
  half — every run names the held legs it did not exercise and when each last ran. The SCHEDULING
  half is not built and is not this unit.

## 3. Non-goals (OUT)

- **Decomposing checks 1-27 so `--only <n>` accepts any n.** This was the author's first
  recommendation, the arithmetic in §4 killed it, and S3's measurement then confirmed the kill from
  a stopwatch rather than a division. It stays here as a rejected alternative with the number that
  rejects it, not as deferred work.
- **Deleting or thinning assertions.** 337 in one suite and 663 in another exist because something
  went wrong once. Cost is a scheduling problem, not a coverage problem.
- **Putting the `optIn` self-tests back on the merge bar.** They are `optIn` for the reason this
  spec measures. S7 gives them reporting instead, and promotion to the bar stays refused.
- **Porting anything to a faster language.** The suites test shell behaviour through shell.
- **Adopter-side workarounds.** These are gov's files; an adopter patching them locally is the fork
  class `TOOL-aGradedDoorway-1` exists to end.
- **Changing the per-spawn cost on any node.** S3 measured it at 251 ms here against 19-39 ms on
  node `d`, and named an on-access scanner as the documented cause. The remedy is an exclusion on
  the affected machine, which is a change to system security settings and therefore an owner action.
  It is recorded rather than performed.

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
**That setting is not the shipped default, and rev-1 did not say so.**

Structure of the two dominant suites:

| suite | full-program runs | tree resets | assertions | shard support |
|---|---|---|---|---|
| `check-unattended.test.sh` | 265 | 268 | 337 | `SHARD_ARITY=2`, unused upstream |
| `unattended.test.sh` | n/a | 252 | 663 | `SHARD_ARITY=2`, unused upstream |

### Data model

The cost of `check-unattended.test.sh` is `265 × (reset_tree + one full 30-check run)`. `run()` is
`bash "$SCRIPT"` with no selector, and an arm cannot ask for less: the checker's only scope flag is
`--only 28`, which refuses anything else because "checks 1-27 share state and are one unit".

**Checks are ADDITIVE on a real corpus.** On the inCMS corpus of 302 builds, `--only 28` costs 103 s
and `--skip 28` costs about 560 s against a full run of 664 s. 103 + 560 is 663. There is almost no
shared fixed cost at corpus scale, so "checks 1-27 share state" is a CORRECTNESS coupling and not a
performance one.

**But the suite does not run at corpus scale, and S3 measured what it does instead.** One invocation
against the suite's own fixture, timed directly: `real 128.0 s, user 12.1 s, sys 43.9 s`. Check
bodies are **9.5 percent** of wall. `sys/(user+sys)` is 78.4 percent, which reproduces the same
ratio the adopter measured on the real corpus, so the shape is a property of the workload rather
than of either fixture. A spawn costs 251 ms on this node against 0.053 ms for a shell builtin —
a ratio near 4 700 — which puts roughly 500 process creations behind a single invocation and
agrees with `TOOL-dNarrowedAnchor-1`'s own census of 469.

That kills decomposition on a measurement rather than an inference. A perfect 30-way split that
eliminated every check body returns 9.5 percent, for the largest and riskiest refactor available. It
also **reorders this spec's own scope**: sharding lowers the floor without removing a single spawn,
while S4 removes invocations outright, and invocations are the 90.5 percent. S4 goes before S2.

### Rollout

S1 and S5 landed downstream first, since both are adopter-side and independent of the measurement.
S3 next, because it either confirmed the ranking or overturned it before any refactor was paid for —
it overturned part of it. S4 follows, then S2 against whatever balance S4 leaves. S7's scheduling
half is last, because a schedule over a cost nobody has finished changing would only ratchet in the
current number.

### Files touched (estimate)

`tools/unattended/check-unattended.test.sh`, `tools/unattended/unattended.test.sh`, and this build's
records. S3 added a throwaway instrument rather than a shipped file, and it was deleted. S1's
upstream half touches `tools/run-gates/` and the kit's own README rather than `tools/gate-legs.json`.

### Alternatives rejected

**Decompose checks 1-27 so any `--only <n>` works.** Rejected on the §4 arithmetic and then
confirmed rejected by S3's stopwatch: at fixture scale the check bodies are 9.5 percent of wall, so
a 30-way split does not buy 30x. It is also the largest and riskiest change available — untangling
shared state across 27 checks of a merge-bar checker. The author recommended this before doing the
division and records the reversal here rather than quietly dropping it.

**Replace `reset_tree` with a template-directory copy.** 268 resets, each a `git reset --hard` plus
`git clean -fd` plus ref surgery, is a real target, and S3 measured one reset at 758 ms against a
128 s run — about 0.6 percent, or 200 s across the suite. Rejected on that number as well as on the
two original grounds: the git state IS part of what several arms assert about, so a copy may not
reproduce it faithfully, and on Windows a recursive copy of a `.git` directory is not obviously
cheaper than a reset.

**Run the suites in a Linux container on Windows nodes.** A spawn under MSYS costs 251 ms here
against 19-39 ms on node `d`, and these suites are nearly pure spawn latency — the same suite is
reported at about 59 minutes on node `d` against 4 h 14 m in the adopter here. Rejected as out of
scope for a kit: it moves the problem to every adopter's infrastructure rather than fixing the kit.
Recorded because it is the single largest factor and a reader deserves to know it was considered.

## 5. Production-readiness checklist

- security — N/A. No new surface; sharding changes scheduling, not what is asserted.
- perf / scale — the whole spec. The target at rev-3 is the `--editor` full set, not the merge bar,
  which §1 records as already inside the limit.
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
- help/ docs — N/A for adopters; the reader-facing surface is the kit READMEs, which gain the shard
  invocation.

## 6. Acceptance criteria

- **AC1** — When a manifest emits one leg per shard for both suites, the union of assertions
  reported across shards equals the unsharded count exactly, allowing for each suite's declared
  `PROLOGUE_ARMS`. An assertion that appears in no shard is a silent coverage loss and must fail
  this criterion.
- **AC2** — When a full `--editor` bar runs at the default pool rather than `HEAVY_JOBS=1`, wall
  clock is strictly less than the sum of leg seconds. Equal is the defect, and equal is what the
  measured run produced.
- **AC3** — MET. When S3's instrument runs one `run()` of `tools/unattended/check-unattended.sh`
  against the fixture the suite builds, it reports the split into check bodies, kernel time and
  off-CPU time, each as a measured number. No remedy after S3 may cite the §4 inference, and §4 no
  longer does.
- **AC4** — When `SHARD_ARITY` is raised, an arm deliberately moved into a shard that does not carry
  the state it depends on FAILS. Observed red before the raise is trusted.
- **AC5** — When a leg exceeds its declared budget, the leg fails and names the budget and the
  measured cost. MET downstream: `FAIL:ceiling` is recorded distinctly from `FAIL`, observed on both
  of the adopter's execution paths.
- **AC6** — RESTATED at rev-3 as a REGRESSION GUARD rather than a target, because the measurement
  says it already holds. When the merge bar runs at the default pool with no `optIn` legs, it
  completes in under 30 minutes on a 16-core node; a future change that pushes it over must red
  something rather than be discovered. The adopter's per-leg ceiling is that something.
- **AC7** — When a run does not exercise a held `optIn` leg, it says so and says when that leg last
  produced a verdict. MET downstream. A schedule that reports only its failures is
  indistinguishable from one that never ran, which is the defect S7 exists to close.

## 7. Gates

`tools/unattended/check-unattended.test.sh`, `tools/unattended/unattended.test.sh` and
`tools/unattended/check-playbook.test.sh` at every shard index; `check-memory-hygiene.sh`;
`govkit selfcheck`. New gate: S5's per-leg budget, which gov already carries on 86 of 86 legs.

## 8. Open questions

- **Does S3 confirm the ranking?** The §4 inference made batching and sharding beat decomposition.
  RESOLVED (S3, 2026-08-29): decomposition stays dead and by a wider margin than the inference
  claimed, but the ranking BETWEEN the survivors inverts. Check bodies are 9.5 percent of wall, so
  the lever is invocation count; sharding redistributes invocations and S4 removes them. S4 now
  precedes S2. The owner's ordering instruction — land S1 immediately, run S3 before anything else —
  was followed and this is its answer.
- **How far can `SHARD_ARITY` go before the HOIST SET blocks it?** Both suites declare 2. RESOLVED
  (owner, 2026-08-29): pick 8 and fix what breaks, against the author's recommendation to count the
  coupling first. The objection was that an unaudited split can produce a GREEN proving nothing; the
  answer is that AC1 already forbids exactly that. A rev-3 measurement narrows what to expect: the
  two regions are 34/66 by run count in one suite and 24/76 in the other, so an even 8-way split
  requires re-cutting region two rather than subdividing evenly.
- **Should the `optIn` self-tests get a scheduled runner?** RESOLVED (owner, 2026-08-29): yes, and
  the ABSENCE of a run is itself reported. The reporting half is built; the scheduling half is not,
  and it is named as unbuilt rather than left to be assumed.

## 9. Revision log

- rev-3 · 2026-08-29 · reconciled against two measurements taken after rev-2. §1's goal was
  partly false — the merge bar was never over 30 minutes, and the 254-minute figure required both
  `--editor` and a non-default `HEAVY_JOBS=1`. S1's premise was false for gov specifically, whose
  runner runs these suites unsharded by documented intent; its true upstream content is that the
  shard-join predicate ships only with the gov-only canary. S3 built and its answer folded in: check
  bodies are 9.5 percent of wall, so S4 moves ahead of S2. AC6 restated as a regression guard, AC3
  and AC5 marked met, AC7 met in its reporting half. S5's mechanism named down to the line numbers
  it was copied from.
- rev-2 · 2026-08-29 · all three forks resolved by the owner. S2 reshaped from "audit then raise" to
  "raise to 8 and fix what breaks", against the author's recommendation; the objection and the
  reason it is survivable both stand in §8. S7 added for the scheduled runner.
- rev-1 · 2026-08-29 · initial draft, written from the 62-leg timing run and two scope measurements.
  Records a reversal of the author's own earlier recommendation: decomposition was proposed verbally
  before the 15270/265 division was done, and is rejected in §4 on that arithmetic.

## 10. Reuse audit

No seam to wire through for the sharding: this changes how existing suites are INVOKED, and both
already implement the mechanism. `SHARD_ARITY` and `--shard <i>/<n>` exist in
`check-unattended.test.sh` and `unattended.test.sh` today, complete with an out-of-range refusal.
S5 reuses `tools/run-gates/`'s per-leg ceiling rather than inventing a budget shape, and S1's
downstream half is a port of `tools/run-gates/run-gates.gov.test.sh:346-403` rather than a second
predicate. The one thing with no upstream relative is S7's held-leg coverage report; gov's nearest
is the `pre-push` `selftests` key, which reads coverage in the opposite direction.
