# TOOL-cSettledDocket-5 — the one self-test leg that reports no count at all

**Status:** OPEN · rev-1 · 2026-08-16 · node c · Tier-1 · base 1da67d9c · streams tooling

## 1. Goal

`skills/session-kickoff/manifest-check.test.sh` prints no assertion summary and carries no counter.
Measured: zero `PASS`/`assertions` output, zero `n=$((n+1))` sites. It is the only self-test leg on
the bar with no executed-count signal, so `TOOL-cBriefedPilot-23`'s floor cannot apply to it and the
stranded-arm class it guards against is unobservable here.

The gate it proves is the kickoff-manifest ratchet, which this session watched refuse three times in
a row for three different reasons. A suite that can go quiet without anyone noticing is a poor proof
of a gate that active.

## 2. Scope (IN)

- **S1** — a counter in the suite's assertion helpers, incremented before the test.
- **S2** — a summary line printing the executed count on success, in the same shape the other three
  suites use, so an operator reading three legs reads one format.
- **S3** — `FLOOR_ASSERTIONS`, pinned shrink-only at the measured count, refusing with the same
  message the other suites use: the arms are UNREACHABLE rather than absent.
- **S4** — an arm proving the floor fires: strand a block past an early exit and observe the refusal.
- **S5** — `TOOL-cBriefedPilot-35` closed.

## 3. Non-goals (OUT)

- **Adding arms.** This unit makes the existing arms countable. Whether the suite covers
  `manifest-check.sh` well enough is a different question, answered by `check-arms.py`, which already
  reports 28 branches and 28 armed for that gate.
- **A shared helper library across the four suites.** They are four files with four fixtures and one
  is installed per-machine via a junction; a shared library is a cross-kit edge this repo declines
  elsewhere for the same reason.
- **Changing what any assertion asserts.**

## 4. Design

### Read the file before assuming a shape

Unlike the other three suites, this one is not known to route every assertion through helpers. The
first build step is to enumerate its assertion sites and classify them helper-vs-inline, exactly the
distinction unit 4 turns on. If they are all inline, this unit is unit 4's shape a second time and
the two should be built together; if there are helpers, it is smaller. The spec deliberately does not
guess, because guessing the shape is what produced unit 4's half-covered floor.

### Why the same message text

`check-arms.py` keys an arm to its branch by the failure text. Three suites already share this
refusal wording; a fourth copy keeps a future reader's grep over the phrase complete, and the phrase
itself is the useful part — it tells the reader to look for a stranded block rather than a deleted
arm, which is the distinction that cost this build a review cycle.

### The junction wrinkle

The kickoff skill is installed per-machine via a junction, and the suite runs from the tracked
`skills/session-kickoff/` copy. Nothing here depends on the junction, but the floor constant lives in
the tracked file so every machine's run reads the same pin.

### Files touched

`skills/session-kickoff/manifest-check.test.sh` only.

## 5. Production-readiness checklist

No new dependency, no new leg — the suite is already on the bar. One counter, one summary line, one
constant, one arm.

## 6. Acceptance criteria

- **AC1** — the suite prints `PASS (` with its executed count on a green run, where today it prints
  no count.
- **AC2** — `FLOOR_ASSERTIONS` is present and equals the measured count at build time.
- **AC3** — stranding a block of arms past an early `exit` makes the suite refuse with
  `arms are UNREACHABLE rather than absent`.
- **AC4** — `bash skills/session-kickoff/manifest-check.test.sh` exits 0, and
  `python tools/memory-tree/check-arms.py` still reports every `manifest-check.sh` branch armed.

## 7. Gates

`bash skills/session-kickoff/manifest-check.test.sh` · `bash skills/session-kickoff/manifest-check.sh` ·
`python tools/memory-tree/check-arms.py` · `bash tools/run-gates.sh`.

## 8. Open questions

none — the one thing this spec refuses to guess is whether the suite's assertions are helper-based or
inline, and §4 makes reading that the first build step rather than an assumption baked into the
design. That is a sequencing instruction, not an unresolved fork.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-35`, filed when unit 23 floored three suites
  and found this one had nothing to floor.

## 10. Reuse audit

The counter shape, the `FLOOR_ASSERTIONS` constant name and the refusal wording are all
`TOOL-cBriefedPilot-23`'s, copied deliberately rather than varied: `check-arms.py` keys on failure
text, and four suites sharing one phrase keeps a grep over it complete. `mutate` is NOT adopted here
— it lives in the two unattended suites and copying it into a third file for one arm would be a third
implementation of a five-line helper, which is worse than the arm doing its own `git hash-object`
comparison inline.
