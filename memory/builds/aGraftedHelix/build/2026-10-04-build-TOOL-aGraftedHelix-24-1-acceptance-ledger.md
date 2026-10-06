# Acceptance ledger — TOOL-aGraftedHelix-24

**Serves:** journal TOOL-aGraftedHelix-24

Node `a`, 2026-10-05. The build commit is `73dc1dbf`, over the spec's rev-6 commit `c7fc071d`, which
renumbered the claim checks to 107 and 108, kept unit 23's arms as built, and aged the lease stamp
in AC1's fixture before any code. No merge bar and no self-test suite ran in this pass. The criteria
were observed by slices under `tools/unattended/` of the suite's prologue, the claim block's `gh_`
helpers and unit 20's prior-session helpers, each followed by one block, with fixtures under the
short `%TEMP%` root the prologue takes. The new interruption block executed 46 against the
prologue's own 20, green against the kit. Unit 20's block executed 71, green, and unit 23's block
executed 180, green, both against the moved add. Each red was observed against a copy of the
driver beside the kit's library, or a copy of the slice; the kit's driver was never edited for a
break. The slices and copies were deleted after the last run. The whole suite is the main loop's
at VERIFYING, and the block count, 26 with its two `mutate` calls, is the evidence for its
raised floors.

**Evidences:** TOOL-aGraftedHelix-24
- AC1 — `mktemp` — over a record whose `lease-utc` was aged ten minutes and committed, the s2 call
  whose claim push exited 124 under the shim left the shim's fired marker, `session: s2`,
  `prior-session: s1`, `lease-utc` at its pre-call value and the claim at s1; the next s2 call with
  no shim exited 0 with no check 108, left the claim at s2, the set empty and no unstaged run-state
  file. Over a fresh base with the remote away, the shimmed call left the same record; a second s2
  call still away exited 0 with no check 108 and left the set s1 and the claim s1; a third with the
  remote restored did as the 124 leg's second. Red under the parent's driver, whose add follows
  `write_lease`: both legs' sets read empty and both landing calls exited 1 with check 108. Red
  under a copy moving back the unreadable-claim path's add alone: the away leg alone redded, the
  124 leg stayed green. Red under a shim keyed on a session line that never appears: the fired
  marker was absent and `lease-utc` moved ten minutes in both legs.
- AC2 — `CLAUDE_CODE_SESSION_ID` — unit 23's sequences a and c run `--beat` with it unset and
  sequence b its `--dispatch` under s2, as unit 23's build wrote them; re-run in that block's slice
  against the moved add, each `--beat` printed `renewed`, the `--dispatch` exited 0 with no check
  108, and the claim named s2 with the set at s1 after each. Their red under the set read at the
  `--resume` row only is unit 23's ledger's, observed at its build; the arm is unchanged here.
- AC3 — `--hold` — unit 23's AC4 arm runs `--hold` under s2 after the incomplete s2 call, commit and
  push; re-run against the moved add it printed no `unattended: claim not written` line and left the
  claim `held`. Its red under the set read in holder mode only is unit 23's ledger's, unchanged here.
- AC4 — `UNATTENDED check 107 FAILED` — unit 23's sequence-d restart, as its rev-6 built it, stops
  short of d's closing call and asserts the line `prior-session: s1 s2` and the claim at s1 before
  the s3 restart under a new pid and keepalive; re-run against the moved add, the restart took the
  run over with no check 107 and left the claim at k3 and s3. Its red under the whole-value
  comparison is unit 23's ledger's, unchanged here.
- AC5 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base c7fc071d2` printed
  `epoch: unattended · clean · 1.72`, naming no carrier left behind;
  the unattended version moved 1.71 -> 1.72 in 27 files.
