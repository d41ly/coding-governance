# Acceptance ledger — TOOL-aGraftedHelix-25

**Serves:** journal TOOL-aGraftedHelix-25

Node `a`, 2026-10-05. The build commit is `1f518223`, over the spec's rev-5 commit `13314861`, which
renumbered the claim checks to 107 and 108 and recorded that the add's `|| return 1` already stood
in the driver (unit 23's build wrote it, unit 24's kept it), so this unit moves no driver byte and
lands the arm. No merge bar and no self-test suite ran in this pass. The criterion was observed by a
slice under `tools/unattended/` of the suite's prologue, the claim block's `gh_` helpers, unit 20's
prior-session helpers, unit 24's `check_prior_landed` and the new arm, with fixtures under the
short `%TEMP%` root the prologue takes. The slice executed 30 against the prologue's own 20, green
against the kit. The red was observed against a copy of the driver beside the kit's library; the
kit's driver was never edited for the break. The slice and the copy were deleted after the last
run. The whole suite is the main loop's at VERIFYING, and the arm's count, 10 with its one `mutate`
call, is the evidence for its raised floors.

**Evidences:** TOOL-aGraftedHelix-25
- AC1 — `UNATTENDED check 108 FAILED` — over unit 24's base with `lease-utc` aged ten minutes and
  committed, the s2 call whose claim push exited 124 under the git shim's marker and the `mktemp`
  shim keyed on it printed the `claim not written` announce line and left `session: s1`, an empty
  prior-session set and `lease-utc` at its pre-call value; the next s2 call with no shim exited 0
  with no check 108, left the claim at s2, the set empty and no unstaged run-state file. Red under a
  driver copy with the add's `|| return 1` dropped: the first call left `session: s2` and a moved
  `lease-utc`, and the second exited 1 printing check 108 with the claim left at s1.
- AC2 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base 3e303233e` printed `epoch: unattended · clean · 1.73`,
  naming no carrier left behind; the unattended version moved 1.72 -> 1.73 in 27 files.
