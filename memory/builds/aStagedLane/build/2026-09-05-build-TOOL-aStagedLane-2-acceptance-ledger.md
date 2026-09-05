**Serves:** journal TOOL-aStagedLane-2

# Acceptance ledger — TOOL-aStagedLane-2, the attended mode

**Evidences:** TOOL-aStagedLane-2

Every arm is in `tools/workflows/unattended-build.test.sh`, which reports `95 arms, exit 0`. The
suite evaluates the script the way its runtime does — the AsyncFunction shape with stub hooks — and
asserts over the recorded trace. This unit added prompt tracing to that double, because what the
agent is TOLD to run is the whole subject here and no gate downstream of this file reads a prompt.

- **AC1** — `agent:build:tB` — arm *"attended: reaches the build stage"* plus *"attended: no round is recorded through
  the driver"*: `agent:build:tB` present, `agent:audit:record` absent.
- **AC2** — `bash tools/workflows/unattended-build.test.sh` — the default path is exercised by *"default mode: the round IS recorded through the
  driver"* and *"default mode: the BUILD prompt still names --dispatch"*, and by every pre-existing
  arm in the suite continuing to pass unmodified.
- **AC3** — `tier2-review.js` — arm *"attended, null blockers: REFUSES"* and *"names the degraded return"*. The null is
  `tier2-review.js`'s degraded signal by design, and reading it as 0 would make every degraded audit
  look clean.
- **AC4** — `FORKED` — arm *"attended, FORKED unit: refuses"*, naming both the id and the state. The bare
  `FORKED` is supplied directly: `unattended.sh:2144` rewrites a terminal unit's grade to
  `DONE (FORKED)`, so a bare token and a real closed build's roster are jointly unsatisfiable.
- **AC5** — `node tools/workflows/check-workflow-syntax.js` exits 0 and
  `bash tools/workflows/check-verifier-fanout.sh` reports clean.
- **AC6** — `bash tools/workflows/unattended-build.test.sh` — arms *"header: names the --review round record"* through *"header: says the S7 warning is
  caller-supplied, not detected"*, seven assertions over the file's own header text, including that
  M4's blocker-disposal clause is unreachable in this mode.
- **AC7** — `bash tools/workflows/unattended-build.test.sh` — arm *"attended + run-state file: WARNS"*, *"names the slug"*, *"CONTINUES to build"*. The
  owner's ruling was warn-and-continue, against this spec's own recommendation to refuse.
- **AC8** — `bash tools/workflows/unattended-build.test.sh` — arms *"attended prompt: no --dispatch INSTRUCTION"* and *"no --brief INSTRUCTION"*, each
  paired with *"the per-unit build instruction SURVIVES"*. The pairing is the criterion: an arm that
  only checks a substring is ABSENT passes just as well when the whole clause is empty.
- **AC9** — `bash tools/workflows/unattended-build.test.sh` — arms *"attended preamble: the word 'mandate' does not reach any agent"* and *"it says an
  owner is in the loop"*. In this repository a mandate is the authority to merge and push with no
  owner turn, so the unattended preamble is a falsehood in this mode.
- **AC10** — `bash tools/workflows/unattended-build.test.sh` — arms *"attended, 2 blockers: CONVERGING"* and *"BUILD is NOT reached"*, against the
  zero-blocker path covered by AC1. Both live branches, because a branch mapping a positive count to
  terminal would reach BUILD over open blockers and satisfy every other criterion here.
- **AC11** — arm *"attended, DONE (FORKED): SKIPPED, not refused"*, fed the vocabulary `--plan`
  actually emits rather than a hand-written roster of `READY`.
- **AC12** — `bash tools/workflows/unattended-build.test.sh` — arm *"attended, no planState: refuses"* and *"names the field"*.
- **AC13** — `bash tools/workflows/unattended-build.test.sh` — arm *"attended, unknown state: refuses"* and *"names the value it did not recognise"*.
- **AC14** — `bash tools/workflows/unattended-build.test.sh` — arm *"attended, unit AUTHORED this invocation: builds despite entry-time MISSING"*, with
  its control *"MISSING and NOT specced: still refuses"* and the narrower control
  *"MISSING but only alreadyPresent: still refuses"*.

## What this ledger does not claim

Attended mode is deliberately WEAKER than unattended mode and this ledger does not claim otherwise.
Five things are lost, named separately in the file's header because one of them is a record and not a
refusal, and the run-integrity note the harness returns says so in the field a caller reads.

The S7 warning depends on a CALLER-SUPPLIED fact. This script has no filesystem and cannot detect a
run-state file, so a caller that supplies nothing gets no warning at all. That is a real hole, not a
covered one, and no arm here pretends otherwise.
