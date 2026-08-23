# TOOL-dScriptedRepeat-15 — the kit's self-test suite becomes affordable, and every number here carries the command that produced it

**Status:** CLOSED · rev-4 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

`check-unattended.test.sh` is the compensating check for seven merge-bar legs this build removed, and
it costs tens of minutes. An unaffordable compensating check is worse than the legs were: the
exemption was traded for something nobody will run. Bring it under the ceiling
`run-unattended-gates.sh` declares, without removing an arm or weakening one.

## 2. Scope (IN)

- **S1 — MEASURE FIRST, and this time with the commands recorded.** The cost model has been wrong
  three times: "~28x more work than the question needs" (it is not), "~23 min of per-arm fixture
  reset" (a reset is tens of milliseconds), and "243 invocations at ~13.2 s each" — which was a
  QUOTIENT, 3199 ÷ 243, presented as a measurement, whose divisor the build's own
  `<git-dir>/gate-ledger.tsv` contradicts (846.0 + 2013.7 = 2859.7 s for the sharded pair). The
  first build step produces, on a quiescent tree at one commit:
  - the unsharded wall reading, and `--shard 1/2` and `--shard 2/2` separately, all three side by
    side, with a sentence saying which one AC1 is judged against and why the others differ;
  - a profile of ONE checker invocation taken INSIDE the suite's own fixture, not against the real
    repo — the 22.7 s / 11.7 s pair was a real-repo reading that includes a remote observation and
    must not be transferred onto the fixture population;
  - the per-arm NON-checker git work, which no model has included: the suite makes 101 `sed -i` and
    263 bare `git` calls outside `reset_tree`.
  **Every figure is written with the command that produced it.** A number without its command is what
  produced all three of the wrong ones.
- **S2 — the lever the profile names, and only that one.** Candidates: subprocess count inside the
  checker; per-call-site scoping; nothing else until S1 speaks.
- **S3 — SCOPING IS CLASSIFIED ON WHAT AN ARM ASSERTS ABOUT ABSENCE.** An arm that asserts something
  is PRESENT (`hit`) may be scoped to the region that emits it. An arm asserting something is ABSENT
  (`miss`) or comparing an exit code (`same`) may NOT: scoping its region away makes it pass
  vacuously. Measured: 208 `hit`, 87 `miss`, 22 `same` — 109 arms that must keep the full run or take
  an explicit paired scoped companion.
- **S4 — the scope is passed PER ARM, never per block.** A block-scoped variable leaks into the next
  block on any early return, and rev-1 specced both forms without noticing they differ.

## 3. Non-goals (OUT)

- **Not restructuring the checker into independently runnable checks.** Checks 1-27 share state and
  `--only 14` is refused for that reason.
- **Not removing or merging arms to hit the number.** The ceiling forces cost down, not coverage.
- **Not touching the other four suites**, which are inside their ceilings.
- **Not rebalancing the shards.** They served the removed bar legs, cannot affect AC1's unsharded
  reading, and are out of scope here.

## 4. Design

`run()` gains an optional argument, passed at each call site that qualifies under S3. The 109
absence-asserting arms keep the unscoped call.

**THE ARITHMETIC, AND THE FALLBACK IT FORCES.** Best case from scoping alone, using the audit's
in-fixture-shaped readings rather than the real-repo pair: the ~60% that `--skip 28` retains applied
to the arms that qualify lands the suite at roughly 1500-1900 s against a 900 s ceiling — 1.7-2.1x
over. So scoping alone CANNOT satisfy AC1. Either S2's checker-level fix is taken and is therefore
mandatory rather than conditional, or the unit re-declares the ceiling with the measurement recorded
beside it. AC1 accepts either, and refuses silence.

## 5. Production-readiness checklist

- **Security** — none.
- **Observability** — `run-unattended-gates.sh` prints per-suite seconds against the ceiling. The S1
  profile lands in the bar-cost record with its commands.
- **Testing** — the suite is its own test; the risk is a scoped invocation running fewer arms, which
  AC4 and AC6 catch and which the assertion count CANNOT (see AC2).
- **Rollback** — an unscoped call site restores today's behaviour exactly.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/run-unattended-gates.sh --selftests` reports the gate selftest
  under its declared ceiling with no OVER BUDGET line, EITHER because the cost fell OR because the
  ceiling was re-declared in `tools/unattended/run-unattended-gates.sh` with the S1 reading beside it.
  Silence satisfies neither.
- **AC2** — **the assertion count is NOT the evidence and is not re-derived as a floor.**
  `n=$((n+1))` is the first statement of `hit`, `miss` and `same` in
  `tools/unattended/check-unattended.test.sh`, so the count is invariant under any change to `run()`'s
  argv and a floor derived from it would be a floor over its own subject. `FLOOR_ASSERTIONS` is left
  at its current value and this AC asserts it did not move.
- **AC3** — the S1 readings are written into
  `memory/builds/dScriptedRepeat/build/2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md`
  each with its command, and the record's superseded claims — the 28x figure, the fixture-reset
  figure, the 13.2 s quotient, and the "80 arms × 22 s" line — are marked superseded rather than
  deleted.
- **AC4** — a staged break in a check-28 rule still reds through an arm passing the 28 scope, and a
  staged break in a 1-27 rule still reds through one passing the complement. One of each observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC5** — **byte-identity over a RED corpus, not over silence.** With one staged break in the 1-27
  region and one in the 28 region, `bash tools/unattended/check-unattended.sh` unscoped emits a
  byte-identical failure set and exit status before and after this unit. Comparing a green tree's
  empty output to a green tree's empty output proves nothing, which is what rev-1's AC5 did.
- **AC6** — one `miss` arm and one `same` arm are deliberately given the WRONG scope in a scratch
  copy, and the suite still reds. If it passes, S3's classification is not being applied and the
  vacuity it exists to prevent is live.

## 7. Gates

`bash tools/run-gates/run-gates.sh` and `bash tools/unattended/run-unattended-gates.sh --all`.

## 8. Open questions

- **F1 — if the profile names the checker, does this unit fix the checker or stop at scoping?**
  RESOLVED (agent, 2026-08-23, delegated): §4's arithmetic settles it — scoping alone cannot reach the
  ceiling, so the checker fix is mandatory unless the ceiling is re-declared. Land it as its own
  commit with its own staged-RED so the two are independently revertable.

## 9. Revision log

- rev-4 · 2026-08-23 · the round-7 fold. **BLOCKER 1 was in this unit's own batching and it was the
  serious one.** `_pbatch`'s misaligned-reply fallback filled every slot with the batch's own exit
  status — correct for a body that will not RUN, which exits nonzero, and wrong for a body that ran and
  merely misaligned, which exits 0. `(rc 0, "")` is the PASSING pair in both template arms, so a parser
  broken only for multi-line input left the whole leg at rc 0 with ZERO output, in the loop that is the
  shipped template's only grader. Reproduced exactly: pre-fold rc 0 / 0 lines, post-fold rc 1 / 8 lines.
  The two degraded shapes are separate branches now — empty reply keeps the honest substitute, a
  misaligned one reds once and poisons every slot with 125 so each arm's rc branch fires.
  **The 19-case equivalence corpus missed it, and that is worth more than the fix.** Gutting a parser
  for EVERY input makes the fixed specimen arms fail first, and their noise made the output identical
  either way; the template loop's new silence hid behind it. A staged break must be scoped to the input
  shape the new code handles differently. The arm now does exactly that.
  **LOW 2** — `--help` quoted a ~60-minute budget beside the ceiling this unit had just re-declared, in
  the same file. It DERIVES the figure from the `BUDGET_*` declarations now, so there is no second copy.
  Minted: `fallback-fabricates-the-passing-value`.
- rev-3 · 2026-08-23 · CLOSED. S1 ran and named a lever S2 then took alone; S3 and S4 were NOT taken,
  and that is a decision with numbers behind it rather than an omission. **What S1 found:** the leg is
  not compute-bound — `real 14.4s user 0.33s sys 0.62s` — and the wait is process creation, because
  an on-access antivirus scanner fronts every `exec` on this node at 0.019-0.039 s per spawn. The leg
  made 469 spawns per invocation and the suite makes 243 invocations, so the suite's unit of cost is
  ~114,000 process creations. **What S2 took:** the spawn count, 469 → 220, counted from an execution
  trace in both directions. Three loops that ran a grep or a `bash -c` per (item, file) now read each
  file once. **Why S3/S4 were declined:** with the invocation at ~5.2 s, scoping the arms that qualify
  saves ~320 s more, needs 243 call-site edits, and carries exactly the vacuity risk AC6 was written
  for — and it does not change the outcome, because §4's arithmetic already put AC1 on the re-declare
  branch either way. S2 says "the lever the profile names, and only that one"; the profile named
  subprocess count. **AC6 is therefore moot** and is recorded as not-run rather than as passed, since
  the classification it tests is not applied anywhere. **AC1 took its second branch:** the ceiling is
  re-declared at 1800 s in `tools/unattended/run-unattended-gates.sh` with the derivation beside it.
  **AC5 was met over a 19-case corpus, 18 of them red**, byte-identical in output and exit status.
  **What is NOT observed and is written here rather than left to be discovered:** the suite has not
  been run end to end at this commit, because the owner stopped these suites and that instruction
  stands. The 1342 s figure is derived from two measured terms, not timed.
- rev-2 · 2026-08-23 · the round-1 spec audit's BLOCKER 2, BLOCKER 3 and three highs. The scoping rule
  is rewritten to classify on ABSENCE rather than on the message an arm names, because 109 of the
  suite's arms assert absence and every one of them passes vacuously when its region is scoped away.
  AC2 stops using the assertion count as evidence — `n` increments before any inspection, so that
  count cannot see the defect it was meant to guard. AC5 moves to a RED corpus. §4 states the
  arithmetic from this unit's own scope to the declared ceiling, finds it 1.7-2.1x short, and declares
  the fallback rather than leaving AC1 unreachable. S1 replaces a quotient with three real readings
  and requires each figure to carry its command.
- rev-1 · 2026-08-23 · drafted.

## 10. Reuse audit

`--only 28` / `--skip 28` exist and are verified in four directions. `run-unattended-gates.sh`
declares and enforces the ceiling. Nothing is built until S1 speaks.
