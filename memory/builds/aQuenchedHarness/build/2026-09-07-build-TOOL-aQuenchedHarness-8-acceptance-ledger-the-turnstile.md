# Acceptance ledger — TOOL-aQuenchedHarness-8

**Serves:** journal TOOL-aQuenchedHarness-8

**Evidences:** TOOL-aQuenchedHarness-8

Tier-2 · node a · 2026-09-07. One line per numbered criterion, naming the observation that answered
it. THE SUITES THAT OWN MOST OF THESE ARMS WERE NOT RUN TO COMPLETION: `run-gates canary` and
`run-gates turnstile` were killed part-way to free the box for a clean whole-bar measurement the
owner had asked for. What replaces them, where it does, is a DIRECT observation taken today and named
as such; where nothing replaces them the line says NOT RE-OBSERVED, which is a different claim from
MET and is recorded as one.

- AC1 — MET, OBSERVED IN THE WILD rather than in a fixture. While this session's full bar held the repository, another session started its own bar in a sibling worktree: it reported `another bar holds this repository — queued at position 1 (waited 1s)` and executed ZERO legs while mine executed 47. That is the serialisation this unit exists to protect, holding across a real leg far longer than `TS_TTL`.
- AC2 — NOT RE-OBSERVED. An arm of `tools/run-gates/run-gates.turnstile.test.sh`, killed part-way.
- AC3 — NOT RE-OBSERVED. Also `tools/run-gates/run-gates.turnstile.test.sh`. This is the arm for the TICKER, the mechanism this unit added, so its absence is the most consequential of these.
- AC4 — NOT RE-OBSERVED. Also `tools/run-gates/run-gates.turnstile.test.sh`.
- AC5 — MET at build time and recorded in `memory/builds/aQuenchedHarness/build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md`, the cross-ledger measurement that found the same leg varying 5.5x median and 47.1x worst.
- AC6 — NOT RE-OBSERVED. Also `tools/run-gates/run-gates.turnstile.test.sh`.
- AC7 — NOT RE-OBSERVED. Also `tools/run-gates/run-gates.turnstile.test.sh`.
- AC8 — NOT RE-OBSERVED as an arm. Related evidence from today, not a substitute: after this session's bar completed, `ps -ef` showed no orphaned leg process, and the queued sibling bar acquired the beacon rather than reaping a live one.
