# TOOL-aPromptedMandate-13 — the canary's timeout must not assert a cause it cannot see

**Status:** CLOSED · rev-2 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Stop the run-gates canary from reporting a starved host as a spinning clamp. Its clamp arm reads a
`timeout` expiry as proof the clamp failed, and that exit code carries no such information.

## 2. Scope (IN)

- **S1** — on a timeout, the arm runs a **live control**: the same fixture at **the width the clamp is
  supposed to yield for that input**. The clamp is blamed only when the control FINISHES; when the
  control also expires, the arm reports a host that could not complete the fixture and says the clamp
  is unproven either way.
- **S2** — the two outcomes carry DIFFERENT messages, so a reader can tell which happened. The
  current single message asserts the stronger of the two.
- **S3** — the starved-host outcome is a FAILURE of the arm, not a silent pass. An arm that cannot
  decide has not decided, and treating "cannot tell" as green is how a canary stops being one.
- **S3b** — **the budget is a variable so both new branches are REACHABLE.** Every branch this unit
  adds fires only when `timeout` expires, and on a healthy host it never does — so as rev-1 specced
  it, the deliverable was untestable and its own acceptance unobservable. The arm reads
  `CLAMP_BUDGET=${CLAMP_BUDGET:-60}`, and the suite exercises both outcomes by setting it against a
  fixture that cannot finish inside it. Without this the unit ships two branches nothing can enter,
  which is the unfailable-check class it was written to remove, one level up.
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
run at GATE_JOBS=$w under the budget
  finished  -> assert GREEN 4/4, as today
  expired   -> run the SAME fixture at the width the clamp SHOULD have produced for $w
                 control finished -> the clamp is the only difference. Report it spun.
                 control expired  -> the host could not finish the fixture at any width.
                                     Report THAT, and fail: the arm did not decide.
```

**The control's width is the clamp's own target, not an arbitrary healthy one.** Read from
`run-gates.sh:81-82`: `case "$JOBS" in *[!0-9]*) JOBS=1 ;; ?????*) JOBS=64 ;; esac` then
`[ "$JOBS" -lt 1 ] && JOBS=1`. So `0`, `-3` and `nonsense` all resolve to **1**, and the two 20-digit
values to **64**. A control at some other healthy width — 4, say, which this file exercises elsewhere
— would differ from the subject in WIDTH as well as in clamp path: on the three values the measured
incident actually fired on, the subject is a SERIAL run and the control 4-wide over the same fixture,
so under the contention that produced the incident the control finishes, the subject expires, and the
arm re-accuses the clamp. Matching the target width leaves the clamp as the only difference, which is
what makes the inference sound in both directions.

The control is the discriminator M12 asks for — the smallest artifact that could refute the claim,
run before the claim is made. It costs one extra fixture run only on the path that is already slow.

**Why the control fails rather than skips.** A starved host makes this arm unable to answer, and an
arm that reports green when it could not look is the `fixture-passes-by-finding-nothing` class with
the fixture blamed on the machine. Failing loudly keeps the canary honest and tells the operator to
re-run somewhere quieter — which is what actually happened here.

### Files touched (estimate)

`tools/run-gates.test.sh` (the clamp arm, the `CLAMP_BUDGET` knob, and the arms that drive both new
outcomes) · `memory/backlog/TOOL.md` (close the row). **NOT**
`memory/project/testsuite-count-waivers.txt` — see AC4.

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
- **AC1b** — When the suite runs with `CLAMP_BUDGET` set small against a fixture that cannot finish
  inside it, both new outcomes are entered and observed — the arm's branches are reachable by the
  harness rather than only by an unlucky host.
- **AC2** — When the clamp arm's subject run expires and the control FINISHES,
  `bash tools/run-gates.test.sh` reports the clamp spun, in its existing words.
- **AC3** — When both the subject run and the control expire, `bash tools/run-gates.test.sh` reports
  the host could not complete the fixture, does NOT claim the clamp spun, and FAILS.
- **AC4** — When `bash tools/check-testsuite-counts.sh` runs, it stays green AND
  `tools/run-gates.test.sh` keeps its row in `memory/project/testsuite-count-waivers.txt`. **No
  assertion count is claimed**: that suite prints none — no counter, no `FLOOR_ASSERTIONS` — and is a
  DECLARED waiver row. Rev-1's "its printed assertion count has grown" was unsatisfiable as written,
  and satisfying it by adding the counter would make the suite comply, which reds the counts gate on
  a waiver row that has stopped shrinking. Retiring that waiver is a different unit's job.
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
- rev-2 · 2026-08-18 · folded the M4 audit. Two blockers: every branch this unit adds was reachable
  only on a real timeout, so the deliverable was untestable (S3b adds the budget knob); and AC4 named
  a printed assertion count this suite does not have and could not gain without reddening the gate
  AC4 requires green. The control's width was left as "known-good" when it must be the clamp's OWN
  target — 1 for `0`/`-3`/`nonsense`, 64 for the 20-digit values — or subject and control differ in
  width as well as clamp path. Renumbered from `-8`, which the backlog already held.

## 10. Reuse audit

Satisfied for the SET in unit 1's reuse audit. The live-control shape is REUSED, not invented: the
row-keyed merge driver's suite runs a live `git merge-file` control per case for exactly this reason
— to tell a defect in the subject from a property of the environment — and this build's own M12 states
the general rule that a test whose result cannot change the verdict is a rehearsal. The `timeout`
bound and its 20-digit-`GATE_JOBS` history are read from the arm's own comment rather than
rediscovered, which is what keeps this unit from re-litigating why the bound exists.


**The id was reallocated at rev-2.** This unit was first minted as `-7`/`-8`, which the backlog
already held for two different findings this same run had filed. The manifest's id protocol says
collision-grep `memory/` before minting and that step was skipped; the spec audit caught it. Nothing
downstream depended on the old number.
