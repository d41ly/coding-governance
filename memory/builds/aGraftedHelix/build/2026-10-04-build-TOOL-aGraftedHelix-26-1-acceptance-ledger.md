# Acceptance ledger — TOOL-aGraftedHelix-26

**Serves:** journal TOOL-aGraftedHelix-26

Node `a`, 2026-10-05. The build commit is `db72c39c`, over the spec's rev-3 commit `cf582782`,
which renumbered the claim checks to 108 and 109, made the lease's six guarded lines one guarded
write in a loop, and recorded that the add's single site and the CAS's read guard already stood. No
merge bar and no self-test suite ran in this pass. The criteria were observed by a slice under
`tools/unattended/` of the suite's prologue, the claim block's `gh_` helpers, unit 20's
prior-session helpers and the blocks of units 24, 25 and 26, with fixtures under the short `%TEMP%`
root the prologue takes. The slice executed 75 against 56 before this unit, green against the kit in
93 s. Each red was observed against a copy of the driver beside the kit's library; the kit's driver
was never edited for a break. The slice and the copies were deleted after the last run. The whole
suite is the main loop's at VERIFYING, and the 19 added assertions are the evidence for its raised
floors.

**Evidences:** TOOL-aGraftedHelix-26
- AC1 — `prior-session` — over unit 25's aged base, the s2 call whose claim push exited 124 and
  whose add the once-only `mktemp` shim failed exited 1, printed the check-17 line naming
  prior-session, and left session s1, an empty set and `lease-utc` unmoved. Red under the parent's
  driver and under a copy dropping the add's `fail 17` with its return kept: the call exited 0 and
  printed no check-17 line.
- AC2 — `lease-utc` — unit 24's 124 leg and its unreachable leg each exited 1 and printed
  `UNATTENDED check 17 FAILED — cannot record the lease:`, leaving session s2, prior-session s1 and
  `lease-utc` unmoved. Red under the parent's driver and under a copy dropping the lease write's
  `fail 17` with its return kept: both calls exited 0 with no such line, and the add's arms stayed
  green.
- AC3 — `push` — over a fresh copy of unit 25's aged base with the bare origin away, the git shim
  logged every call and marked the failed claim fetch, the `mktemp` shim fired after it, and the
  call exited 1 with the add's check-17 line, leaving session s1, an empty set, `lease-utc` unmoved
  and no push in the log; the restored s2 call exited 0 with no check 108, left the claim at s2, the
  set empty and no unstaged run-state file. Red under a copy routing the unread claim to a second
  unguarded add: session s2, the set empty, `lease-utc` moved, and the restored call exited 1 with
  check 108 and the claim at s1. Red under a copy routing the unread claim into a CAS with an empty
  expected sha: the CAS's scratch file spent the shim, so the add wrote s1 and the call exited 0
  with session s2; the push count itself stayed 0 there, because no push is reached once that
  scratch file fails, so the no-push assertion was not observed red on its own.
- AC4 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base cf5827828` printed `epoch: unattended · clean · 1.74`,
  naming no carrier left behind; the unattended version moved 1.73 -> 1.74 in 27 files.
