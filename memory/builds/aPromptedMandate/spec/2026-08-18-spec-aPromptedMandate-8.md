# TOOL-aPromptedMandate-8 — the canary's timeout must not assert a cause it cannot see

**Status:** SPECCED · rev-1 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Stop the run-gates canary from reporting a starved host as a spinning clamp. Its clamp arm reads a
`timeout` expiry as proof the clamp failed, and that exit code carries no such information.

## 2. Scope (IN)

- **S1** — on a timeout, the arm runs a **live control**: the same fixture at a known-good width. The
  clamp is blamed only when the control FINISHES; when the control also expires, the arm reports a
  host that could not complete the fixture and says the clamp is unproven either way.
- **S2** — the two outcomes carry DIFFERENT messages, so a reader can tell which happened. The
  current single message asserts the stronger of the two.
- **S3** — the starved-host outcome is a FAILURE of the arm, not a silent pass. An arm that cannot
  decide has not decided, and treating "cannot tell" as green is how a canary stops being one.
- **S4** — the backlog row `TOOL-aPromptedMandate-10` closes, naming this unit.

## 3. Non-goals (OUT)

- **Not raising the timeout.** A larger budget moves the threshold and keeps the wrong inference; the
  arm would still assert a cause from a clock.
- **No change to the clamp itself.** `run-gates.sh`'s clamp is correct and this build has not touched
  it. The defect is in what the CANARY concludes.
- **No change to run-gates' output surface.** Printing the resolved width would let the arm observe
  the clamp directly and is the better long-run design, but it changes the runner to serve a test and
  is a separate unit. Named here so the cheaper fix is not mistaken for the complete one.

## 4. Design

### What the current arm claims, and what it knows

`tools/run-gates.test.sh:201-202` runs the fixture under `timeout 60` and, on `trc=124`, prints
*"never terminated — the clamp let it spin"*. Exit 124 means only that the budget expired. The
timeout is NOT defensive noise — its own comment records that a 20-digit `GATE_JOBS` once made the
runner spin with zero legs executed, so without it this arm would hang the bar. The bound is right;
the inference from it is not.

MEASURED here, 2026-08-18: with four concurrent full bars on this node the arm reported the spinning
message for `GATE_JOBS` of `0`, `-3` and `nonsense`; run in isolation on a fresh `TMPDIR` the same
canary exits 0. Three malformed widths do not all start spinning and then all stop.

### The live control

```
run at width $w under the budget
  finished  -> assert GREEN 4/4, as today
  expired   -> run the SAME fixture at a known-good width under the SAME budget
                 control finished -> the clamp is the difference. Report it spun.
                 control expired  -> the host could not finish the fixture at any width.
                                     Report THAT, and fail: the arm did not decide.
```

The control is the discriminator M12 asks for — the smallest artifact that could refute the claim,
run before the claim is made. It costs one extra fixture run only on the path that is already slow.

**Why the control fails rather than skips.** A starved host makes this arm unable to answer, and an
arm that reports green when it could not look is the `fixture-passes-by-finding-nothing` class with
the fixture blamed on the machine. Failing loudly keeps the canary honest and tells the operator to
re-run somewhere quieter — which is what actually happened here.

### Files touched (estimate)

`tools/run-gates.test.sh` (the clamp arm) · `memory/backlog/TOOL.md` (close the row).

## 5. Production-readiness checklist

- security — N/A
- perf / scale — one extra fixture run, only on the already-slow path
- a11y / i18n — N/A
- error / empty / loading states — the three outcomes (clamped, spun, undecidable) are distinct and
  each has its own message
- observability — the operator learns which of the two causes applies, which is the whole point
- risks — a control that is itself flaky would blame the host for a real clamp defect; mitigated by
  using a width the same file already exercises everywhere else
- testing + left-shift gates — the canary IS a gate leg, and this unit is what makes its verdict
  mean what it says
- migration / rollback — additive within one arm; reverting is deleting the control branch
- user docs — the arm's own comment, which already records why the timeout exists

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates.test.sh` runs on an unloaded host, it exits 0 as it does today.
- **AC2** — When the clamp arm's subject run expires and the control FINISHES,
  `bash tools/run-gates.test.sh` reports the clamp spun, in its existing words.
- **AC3** — When both the subject run and the control expire, `bash tools/run-gates.test.sh` reports
  the host could not complete the fixture, does NOT claim the clamp spun, and FAILS.
- **AC4** — When `bash tools/run-gates.test.sh` runs, its printed assertion count has grown and
  `bash tools/check-testsuite-counts.sh` stays green.
- **AC5** — When `memory/backlog/TOOL.md` is read, `TOOL-aPromptedMandate-10` is closed naming this
  unit.

## 7. Gates

`bash tools/run-gates.test.sh` · `bash tools/check-testsuite-counts.sh` · `bash tools/run-gates.sh`

## 8. Open questions

none — the fork below is RESOLVED.

- **Raise the budget, observe the width, or add a control** — RESOLVED (owner, 2026-08-18): fix the
  canary's timeout, as this unit. A raised budget keeps the wrong inference; observing the resolved
  width is better and changes the runner to serve a test, so it is named as a follow-up in §3 rather
  than taken here.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft, after the owner ratified fixing the canary first.

## 10. Reuse audit

Satisfied for the SET in unit 1's reuse audit. The live-control shape is REUSED, not invented: the
row-keyed merge driver's suite runs a live `git merge-file` control per case for exactly this reason
— to tell a defect in the subject from a property of the environment — and this build's own M12 states
the general rule that a test whose result cannot change the verdict is a rehearsal. The `timeout`
bound and its 20-digit-`GATE_JOBS` history are read from the arm's own comment rather than
rediscovered, which is what keeps this unit from re-litigating why the bound exists.
