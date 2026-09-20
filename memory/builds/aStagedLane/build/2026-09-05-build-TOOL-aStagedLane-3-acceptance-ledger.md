**Serves:** journal TOOL-aStagedLane-3

# Acceptance ledger — TOOL-aStagedLane-3, the sliced spec fan

**Evidences:** TOOL-aStagedLane-3

Every arm is in `tools/workflows/unattended-build.test.sh`, which reports `95 arms, exit 0`.

- **AC1** — arm *"fan: three slices spawn three writers"* (`3 slice(s) -> 3 writer(s)`), with
  *"writer 0 spawned"* and *"writer 2 spawned"*. The criterion is the TOTAL bound, not the slice
  count: three slices at a cap of five chunk to groups of one, so the two readings coincide here and
  AC8 covers where they do not.
- **AC2** — `bash tools/workflows/unattended-build.test.sh` — arm *"brief: writer 0 is handed its own unit's brief"*, with *"is NOT handed another
  group's brief"* and a third group's, asserted against writer 0's own composed prompt.
- **AC3** — `bash tools/workflows/unattended-build.test.sh` — arm *"fallback: the unit with no brief is named"*. A silent fallback and a deliberate
  omission are otherwise indistinguishable, and a mistyped key would hand back the old behaviour with
  no signal.
- **AC4** — `bash tools/workflows/unattended-build.test.sh` — arms *"one dead writer: reported as DEGRADED"*, *"its unit lands in refused"*, *"the
  stage still completes"*; and the second half, *"ALL writers dead: THROWS"* with *"BUILD is never
  reached"*. The all-dead path is the one the old guard stopped covering: it tested a falsy return,
  and a merged object is always truthy.
- **AC5** — `bash tools/workflows/check-verifier-fanout.sh` reports
  `clean — 4 workflow script(s) obey the ≤5-verifier rule`, and
  `node tools/workflows/check-workflow-syntax.js` exits 0. That first leg pipes the file to
  `agent-cap.js` itself, which is why this criterion no longer asks for a separate invocation.
- **AC6** — `bash tools/workflows/check-review-join.sh` exits 0 and reports no ref-keyed join for
  this file. It does NOT count the new wave: that gate's own trailer disclaims per-wave counting, and
  the criterion was rewritten to ask it the question it answers.
- **AC7** — `bash tools/workflows/unattended-build.test.sh` — arm *"writers: told to author and NOT commit"* and *"told the caller commits once after
  them"*, over the composed writer prompt.
- **AC8** — `chunk(x, ceil(N/K))` — arms *"above cap: seven slices become four writers, never seven"*, *"no writer beyond the
  cap is ever spawned"*, *"one wave, and it is at or under the cap"*. FOUR, because
  `chunk(x, ceil(N/K))` splits by SIZE: seven slices at a cap of five give groups of two, hence four
  groups. The rule is the bound, not the equality.
- **AC9** — `bash tools/workflows/unattended-build.test.sh` — arm *"writers: told not to run the index generator"*. This is half of clause 3 of the
  disjointness proof and had no observation of any kind before the round-2 spec audit.
- **AC10** — `bash tools/workflows/unattended-build.test.sh` — arms *"header: the one-agent claim is scoped to BUILD"*, *"it names the ratified verdict
  it does not contradict"*, *"it says why — the writers do not commit"*.

## What this ledger does not claim

**The fan has never actually run.** Every arm above drives the harness through its test double, which
records what would have been spawned; no real multi-writer spec pass has executed. The disjointness
argument is a proof about the code, not an observation of a race that did not happen — and
`TOOL-cBriefedPilot-28` remains open precisely because experiments E3 and E4 were never run. This
unit does not run them and does not claim to.

What it does claim is narrower and checkable: the writers are told to author and not commit, so this
stage does not reach the commit contention `TOOL-cBriefedPilot-21` ratified `parallelism route: none`
on. BUILD dispatch stays strictly sequential, asserted by its own arm.
