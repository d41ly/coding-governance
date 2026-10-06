# Acceptance ledger — TOOL-aGraftedHelix-11

**Serves:** journal TOOL-aGraftedHelix-11

Node `a`, 2026-10-05. The build commit is `9bd2f308`, over the spec's rev-4 commit `1d0782aa`. No merge
bar and no self-test suite ran in this pass. The tick criterion was observed by the tick suite's new
session-less beat block run ALONE behind the suite's prologue, and the driver criteria by the driver
suite's new lease-identity block run ALONE behind its prologue and the claim block's `gh_` helpers,
each as a slice under `tools/unattended/` with its fixtures under `%TEMP%`. Each block was run three
ways: against the kit, against a driver copy carrying a staged break, and against the parent
commit's driver, which is the defect finding 39 named. The copies and slices were deleted after
each run. To show nothing older moved, unit 1's and unit 10's claim blocks were run the same way and
executed 176 assertions green, and unit 1's AC12 tick block 5 green; after the take-over and
`--replaces` stamps moved next to their push, unit 1's claim block and the new block were run again
over the committed tree and executed 162 green. The whole suites are the main loop's at VERIFYING,
and the slice counts are the evidence for their raised floors, 6 and 12.

**Evidences:** TOOL-aGraftedHelix-11
- AC1 — `UNATTENDED check 90 FAILED` — with `CLAUDE_CODE_SESSION_ID` unset, the tick over a LIVE
  fixture whose record carries `keepalive`, `session`, `host` and `lease-utc` printed a `renewed`
  beat line and the claim's session read the record's; the holder's `--resume tRun --keepalive-id kT`
  under that session exited 0 and printed no check 90; with the ref deleted the tick created a claim
  reading the record's host, session, keepalive and lease-utc in that order. Red, 4 of 6, under the
  break that read the session from the environment in the copying write, and against the parent's
  driver: `absent` in both claims, and the resume exited 1 with check 90.
- AC2 — `--dispatch` — under `CLAUDE_CODE_SESSION_ID=s-child`, the dispatch of `ARCH-tRun-1` with a
  young beat exited 0 printing `dispatch declared`, and `git ls-remote` printed the same sha before
  and after; with the claim reseeded a third of `RESUME_STALE_BOUND` old it exited 0, the ref moved,
  and the claim's session read `fixture-session`, the record's. Red under the copying-write break:
  `s-child`. Red against the parent's driver twice: the young beat pushed, and `s-child`.
- AC3 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base 1d0782aa5` printed `epoch: unattended · clean · 1.63`,
  naming no carrier left behind.
- AC4 — `lease-utc` — with a `git` shim on `PATH` holding the claim push two seconds,
  `--preflight tRun --keepalive-id k1` printed `preflight OK` and the claim's lease-utc equalled the
  record's byte for byte; the following `--resume tRun --keepalive-id k1` exited 0 and `git ls-remote`
  printed the same sha before and after. Red under the break that handed `write_lease` no stamp at
  `--preflight`: `20Z` against `25Z`, and the resume pushed. Against the parent's driver the two
  stamps differed by the same five seconds.
