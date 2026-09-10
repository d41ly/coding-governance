# TOOL-aBatchedArm-1 — batch the gate self-test's arms by tree state

**Status:** OPEN · rev-2 · 2026-09-10 · node a · Tier-2 · base e9ed269b · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-prompt-TOOL-aBatchedArm-1.md](../prompts/2026-09-10-prompt-TOOL-aBatchedArm-1.md) | research | — |
| [2026-09-10-review-TOOL-aBatchedArm-1-spec-audit-round1.md](../reviews/2026-09-10-review-TOOL-aBatchedArm-1-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/check-unattended.test.sh` spends 293 full-program invocations to make 377
assertions, and 83 % of those invocations feed at most one of them. Group arms whose breaks do not
interfere onto ONE tree and ONE invocation, so the suite reaches its verdict in under 20 minutes
without deleting an assertion.

## 2. Scope (IN)

- **S1** — add one assertion helper, `emitted <check-numbers> <output>`, which grades the SET of
  check numbers a captured run emitted against the set the batch expects. It runs the batch with
  `GOV_UNATTENDED_REPORT=1`, REDS when a `^unattended-report:` skip line names any check the group
  asserts against, and strips those lines from `$out` before the verbatim assertions see it. Its
  failure message prints the expected set, the observed set, and any skip lines it saw. Observed by
  **AC1**, **AC2** and **AC7**.
- **S2** — convert the batchable arms from one-reset-one-run-one-assertion into groups: one
  `reset_tree`, the group's mutations applied in sequence, one `out=$(run)`, one `emitted` call, then
  the group's existing `hit`/`miss`/`same` assertions against `$out` VERBATIM. Observed by **AC3**.
- **S3** — leave un-batched, each on its own tree, every arm whose break can truncate the run,
  relocate it, or leave a control without a witness. The list, and it is the unit's load-bearing
  declaration: the three check-1 branches that `exit` at `check-unattended.sh:114`, `:198` and
  `:385`; every arm asserting on exit code alone; every arm asserting the output is EMPTY; the
  anchor, PATH-stub and remote-rewriting arms; **every `miss` and `same` arm whose check number no
  group-mate makes fire**; and the whole-run EQUALITY arms together with the non-empty baseline they
  compare against (`_f1_clean` at `check-unattended.test.sh:360`, read by `:371` and `:378`).
  Observed by **AC4** and **AC7**.
- **S4** — re-measure and re-declare `FLOOR_ASSERTIONS` and both per-shard floors against the
  converted suite, with the reading beside each number. Observed by **AC5**.
- **S5** — record the new wall-clock reading on a frozen clone and update the row in
  `tools/run-gates/selftest-budgets.txt` with the reading it was taken from. Observed by **AC6**.

## 3. Non-goals (OUT)

- **The structural group linter.** It is the left-shift for five of round 1's six findings and it is
  a SEPARATE MECHANISM under M2, so it is `TOOL-aBatchedArm-2` and not a scope item here.
- **Porting to `tools/lib/lib-selftest.sh`.** Closed by `TOOL-aPooledSweep-3`: that harness takes one
  POSITIVE substring and this suite asserts 101 negatives and 27 equalities. Re-opening it starts
  with the vocabulary `TOOL-aPooledSweep-7` enumerates, and that is a different build.
- **A declarative arm table with a partition solver and recorded goldens.** Rejected in §4 on the
  measurement: the helper reaches the same target with a local edit per group and leaves every
  assertion byte-identical, which is what keeps the equivalence proof available.
- **Cutting spawns further.** `TOOL-aTracedSpawn-2` bounds it at roughly 2 s per invocation of real
  non-spawn work.
- **Raising `SHARD_ARITY` above 2.** A live owner ruling of 2026-08-29 permits it; named as the
  follow-up if AC6 misses.
- **Repairing the suite's pre-existing RED.** `TOOL-aQuenchedHarness-9` and `TOOL-aHoistedPass-38`
  own those. This unit must not change any arm's verdict, red ones included.

**BINDING PRIOR.** `TOOL-dScriptedRepeat-15` S3, CLOSED, ratified this classification for this exact
file: "SCOPING IS CLASSIFIED ON WHAT AN ARM ASSERTS ABOUT ABSENCE. An arm that asserts something is
PRESENT (`hit`) may be scoped… An arm asserting something is ABSENT (`miss`) or comparing an exit
code (`same`) may NOT: scoping its region away makes it pass vacuously." Batching is scoping by
another route, so the ruling binds here unchanged. rev-1 did not cite it and its S3 contradicted it.

### Edges

- **consumes-from** `none`
- **hands-off** `TOOL-aBatchedArm-2` — the group linter that mechanically enforces S3's partition,
  which this unit states as a rule and cannot enforce per group.

## 4. Design

### Data model

A batch is a contiguous run of arms delimited as today by `reset_tree`. The only new state is the
expected check-number set, written as the helper's first argument.

```
reset_tree; mutA; mutB; mutC
out=$(run)
emitted "4 10 14" "$out"
hit  "$out" "<A's own failure text>"
hit  "$out" "<B's own failure text>"
miss "$out" "<C's near-miss text under check 14>"
```

### The admissibility rule, which is what makes `emitted` load-bearing for a control

**A group's `miss` or `same` assertion against check N is admissible ONLY when N is in that group's
`emitted` set.** The check's own firing is then the liveness assertion that the branch was reached at
all, which §7 of the charter demands of every signal. A control whose check no group-mate makes fire
has no witness and runs on its own tree, by S3.

Without this rule the mechanism is unsound, and round 1 proved it rather than argued it. `fail()` at
`check-unattended.sh:93` is the SOLE emitter of `UNATTENDED check N` — one hit in the file. Every
SKIP goes through `report()` at `:761`, gated on `GOV_UNATTENDED_REPORT` at `:760`, and there are 15
such sites covering checks 15, 23, 24 and 31. So a check pushed onto a skip path by a group-mate
prints nothing on the default channel and is byte-identical, to every assertion in this suite, to a
check that correctly stayed silent. For a `miss` control the consequence is total: its check number is
legitimately absent from the expected set, `emitted` cannot tell dark from silent, and the arm stays
GREEN over a branch never evaluated. AC3 cannot see it either, because green stays green.

101 of 377 assertions are `miss` and 27 are `same` (measured at BASE; 249 + 101 + 27 = 377). 40 of the
101 sit in `reset_tree`-delimited blocks carrying no `hit` at all, so they have no positive witness
even before any batching.

### Why the set and not a count

A count catches truncation and misses collateral. The eight-break probe of 2026-09-10 staged eight
breaks and emitted four checks, because one break tripped check 1 whose branch `exit`s. A count would
have caught that; it would NOT catch a break that additionally fires an unrelated check.

**The uniqueness proof rev-1 leaned on measured the WRONG SIDE.** That all 178 branch signatures are
unique under `check-arms.py`'s normaliser is a fact about the CHECKER: it bounds `emitted`'s
attribution, so a fired check number maps to one branch. It says nothing about the TEST side, where
the arms live. Measured there at BASE: between 20 and 36 distinct assertion texts are carried by 46
to 101 separate arms, depending on whether trailing-quote forms are counted — the report found the
lower figure, this author's looser matcher the higher, and BOTH are above zero, which is what matters.
`a run-state file's generated markers are malformed` is the text of four arms, at `:467`, `:984`,
`:1310` and `:1313`. Several duplicate sets are ADJACENT blocks, which is exactly what "a contiguous
run of arms" would group. Group two arms carrying one text and a single break satisfies both `hit`s.

**What `emitted` does NOT check**, stated because a structural check reads as a semantic one to
everybody who did not write it: that a check fired for the reason its arm intended. Two branches under
ONE check number are indistinguishable to it. That is why the per-branch `hit` lines stay exactly as
they are, why the admissibility rule above is separate from `emitted` itself, and why
`TOOL-aBatchedArm-2` exists to grade the LINKAGE the rule describes.

### Alternatives rejected

**A declarative arm table plus an offline partition solver and recorded golden sets.** This was the
author's own earlier recommendation. Rejected because it rewrites 377 assertions to reach a target a
one-helper edit reaches, and a rewritten assertion is what made `TOOL-aPooledSweep-3` close the port:
the equivalence proof is a per-assertion diff, and only an edit leaving assertion text untouched keeps
it available.

**A tree-state memo on `run()`.** Measured rather than argued: 293 invocations visit 262 distinct
states, so memoising repeats buys about 10 % and does not approach the target.

### Rollout

The conversion lands in tranches, each verified by AC3's equivalence diff before the next begins. A
tranche that changes any arm's verdict is reverted rather than argued with. `TOOL-aBatchedArm-2`
lands BEFORE the first tranche, because the conversion is mechanical and nothing downstream re-asks
whether a group's controls still witness anything.

### Files touched (estimate)

`tools/unattended/check-unattended.test.sh`, `tools/run-gates/selftest-budgets.txt`, and this build's
records.

## 5. Production-readiness checklist

- security — N/A. The suite grades a checker against a scratch fixture; batching changes scheduling.
- perf / scale — the whole unit. The figure is the suite's wall clock on a frozen clone.
- error / empty / loading states — a malformed `emitted` argument REFUSES by name; the empty-output
  and equality arms stay unbatched by S3.
- observability — `emitted`'s failure prints expected, observed AND the skip lines it saw, because a
  helper that can tell dark from silent and does not say which hands the operator the same ambiguity
  one level up.
- risks — the batching premise is false where callers short-circuit (`TOOL-aDrainedSluice-5` N17,
  reproduced 2026-09-10) and unsound for controls without the admissibility rule (round 1). S3 is the
  mitigation, AC4 and AC7 are its observations, and `TOOL-aBatchedArm-2` is the gate.
- testing — AC3 is the safety property; it must be observed non-empty on a deliberately mis-grouped
  tranche before it is trusted.
- migration — none. Reverting is restoring the file.
- user docs — N/A. Developer-facing; the suite's header carries the batching contract.

## 6. Acceptance criteria

- **AC1** — When a batch's tree fires exactly the checks its `emitted` call names, the helper passes
  and increments the assertion counter by one.
  Red when: the helper is silent on a mismatch, which is the green-by-absence shape this suite refuses.
- **AC2** — When a break is added to a batch WITHOUT updating its `emitted` argument, the suite reds
  and the failure names both the expected and the observed set. Staged and observed before landing,
  per `AGENTS.md` §7.
  Red when: the run passes, or the message names only one side of the comparison.
- **AC3** — When `check-unattended.test.sh` runs before and after the conversion, the set of `FAIL`
  lines is byte-identical and the executed assertion count `n` is equal.
  `figure:` DERIVED at observation time from the two logs, never pinned here.
  `cost:` two runs each side on a frozen clone.
  Red when: a `FAIL` line appears, disappears or changes text, or `n` moves for any reason other than
  the `emitted` calls S1 adds — whose count is stated separately in the ledger.
  **Not a per-assertion inventory**, because the helpers at `check-unattended.test.sh:57-59` are
  silent on a pass. A swap where one arm starts failing and another stops moves the `FAIL` set, so
  the pair of observables is sufficient and is the strongest available.
- **AC4** — When every arm S3 names is located in the converted file, each sits alone between its own
  `reset_tree` and the next.
  `fixture:` the suite's own scratch repo; no new fixture is needed.
  Red when: any of them is found inside a group.
- **AC5** — When the converted suite runs unsharded and at each shard index, the executed assertion
  count meets the re-declared `FLOOR_ASSERTIONS` and per-shard floors, each carrying its reading.
  Red when: a floor is carried across from the unconverted suite, which is a number and not a floor.
- **AC6** — When the converted suite runs UNSHARDED on a frozen clone on an idle box, it completes in
  under 20 minutes, measured with `date +%s` around it and recorded.
  `figure:` DERIVED from that run and written into `tools/run-gates/selftest-budgets.txt`.
  Red when: the unsharded run exceeds 20 minutes, which sends the unit to the `SHARD_ARITY` follow-up
  in §3 rather than to a lowered target.
  **Unsharded is the subject on purpose.** §1 sets the target on the suite's verdict, the whole-suite
  claim exists only in a run with no `--shard` argument (`check-unattended.test.sh:3161-3162`,
  `run-unattended-gates.sh:157-158`), and the declared argv in `selftest-budgets.txt:114` is
  unsharded. rev-1 graded the longer shard, which is a different subject.
- **AC7** — When a group carries a `miss` or `same` assertion against a check its `emitted` set does
  not name, the suite REDS naming that arm.
  Red when: such a group runs green, which is the round-1 blocker exactly.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `testsuite counts self-test` · `line-length gate selftest`

New arm: `tools/unattended/check-unattended.test.sh` · a batch whose `emitted` argument omits a check
its tree fires, and a group carrying a `miss` against an unnamed check, each staged and observed RED
then unstaged · floor to move: `FLOOR_ASSERTIONS`, `FLOOR_SHARD_1`, `FLOOR_SHARD_2`, re-measured
under S4.

## 8. Open questions

- **F1 · How many arms fit a batch before interference dominates?** The candidate population is NOT
  the 237-of-298 block figure rev-1 quoted: that counts `reset_tree` BLOCKS, and the partition is over
  ASSERTION CLASSES, of which 128 of 377 are `miss` or `same` and are excluded by S3 unless witnessed.
  A true statement about the wrong denominator. RESOLVED (agent, 2026-09-10, delegated): the group
  size is whatever `emitted` and the admissibility rule accept, found by widening until it reds and
  stepping back one; the measured distribution goes in the build record, not here as a pinned figure.
- **F2 · Does the conversion need the pre-existing RED repaired first?** No. AC3 compares the `FAIL`
  set, so a stable red is as good an oracle as a green. RESOLVED (agent, 2026-09-10, delegated):
  proceed against the red baseline and record its `FAIL` set as the artifact AC3 diffs against.

## 9. Revision log

- rev-2 · 2026-09-10 · §2 S1 · §2 S3 · §3 · §4 · AC3 · AC6 · AC7 · F1 · folded spec-audit round 1
  (BLOCKED, 3 blockers, 2 highs, 1 medium). The three blockers were one hole: `emitted` and AC3 were
  both blind to the 101 `miss` controls, so a batched control could pass over a branch never
  evaluated. Added the admissibility rule and the S3 exclusion; cited `TOOL-dScriptedRepeat-15` S3,
  which had already ratified that classification for this file and which rev-1 contradicted;
  corrected the uniqueness proof, which measured the checker side and was quoted as if it bounded the
  test side; retargeted AC6 from the longer shard to the unsharded run; corrected AC3 to the `FAIL`
  set plus the executed count, since the helpers are silent on a pass and no per-assertion inventory
  exists. Added `TOOL-aBatchedArm-2` as the gate and named it in §3 and the Edges.
- rev-1 · 2026-09-10 · initial draft. Records the reversal of this author's own earlier
  recommendation: a declarative arm table with a partition solver was proposed to the owner before
  `TOOL-aPooledSweep-3` and `TOOL-aTracedSpawn-2` had been read, and §4 rejects it on those readings.

## 10. Reuse audit

- **The seam is the suite's own assertion-helper block**, `tools/unattended/check-unattended.test.sh`
  lines 57 to 59, where `hit`, `miss` and `same` already share one counter and one failure idiom;
  `emitted` is a fourth helper in that block and not a new mechanism beside it. The sibling
  `tools/unattended/check-pass-order.test.sh:29-31` carries the same three helpers in a fork-free
  `case` spelling, which is the shape to copy if `emitted` is ever made fork-free too. Verified at
  source rather than cited: the reuse probe reports `unscanned layers: .sh` and can see no shell
  seam at all, so a "no seam fits" resting on it alone would have been unfounded.
- **The retrieval arguments, verbatim:**
  `python tools/codebase-map/reuse_lookup.py "batch staged breaks into one fixture and assert the emitted failure set"`
  and
  `python tools/memory-recall/query.py "why do the kit self-test suites re-run the whole program once per arm instead of batching, and what was decided about porting them to a pooled harness" --terms "selftest arm fixture batching pooled harness invocation spawn shard budget port reset_tree assertion floor"`.
  The second surfaced `TOOL-aPooledSweep-3`, `TOOL-aPooledSweep-7`, `TOOL-aTracedSpawn-2` and
  `TOOL-aDrainedSluice-5` N17; none was reachable by the first. It did NOT surface
  `TOOL-dScriptedRepeat-15` S3, which round 1's lenses found and which is the binding prior in §3 —
  recorded because a probe that misses the ratified precedent for the exact file under change is a
  probe whose result must not be read as coverage.
