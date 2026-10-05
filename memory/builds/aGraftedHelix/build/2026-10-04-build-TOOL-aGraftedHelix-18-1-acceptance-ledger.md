# Acceptance ledger — TOOL-aGraftedHelix-18

**Serves:** journal TOOL-aGraftedHelix-18

Node `a`, 2026-10-05. The build commit is `f410b6fa`, over the dispatch records commit `9ee40bd4`;
the spec needed no revision. No merge bar and no self-test suite ran in this pass. The criteria were
observed by the driver suite's new holder-order block run ALONE behind the suite's prologue and the
claim block's `gh_` helpers, as a slice under `tools/unattended/` with its fixtures under a short
`%TEMP%` root: 33 executed against the prologue's 20, green against the kit in 46 s. It was then run
against two driver copies beside the kit: the parent commit's driver, whose claim write precedes
`write_lease`, and a copy of the built driver with the second due test deleted, so the due test
reads the facts before `write_lease`. To show nothing older moved, unit 1's AC7 and AC18 arms with
unit 11's block, and unit 12's cell block, were run the same way over the built driver: 57 and 61
executed, green. The copies and slices were deleted after each run. The whole suite is the main
loop's at VERIFYING, and the slice count, 13, is the evidence for its raised floors.

**Evidences:** TOOL-aGraftedHelix-18
- AC1 — `lease recorded` — over a record and claim preflighted under `CLAUDE_CODE_SESSION_ID=s1`,
  the holder's `--resume tRun --keepalive-id k1` under `s2` exited 0 printing
  `unattended: lease recorded · keepalive k1 · session s1 -> s2`, and the claim on the bare origin,
  read from its commit message, carried `session: s2`; a second identical call exited 0 and printed
  no `UNATTENDED check 90 FAILED`. Red under the parent's driver and under the second-due-test
  break: the claim read `s1`, the second call exited 1, and check 90 printed.
- AC2 — `lease-utc` — with the record's `lease-utc` first set ten minutes back and committed, the
  holder's resume under `CLAUDE_PID=4242` exited 0 printing `pid 999999999 -> 4242`, and the claim's
  `lease-utc` equalled the record's byte for byte; the following call under the same pid exited 0
  and the claim ref's sha did not move. Red under the parent's driver: the claim carried
  `2026-10-05T02:26:44Z` against the record's `2026-10-05T02:36:48Z`, and the following call pushed.
- AC3 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base 9ee40bd40` printed `epoch: unattended · clean · 1.65`,
  naming no carrier left behind; the unattended version moved 1.64 -> 1.65 in 27 files.
