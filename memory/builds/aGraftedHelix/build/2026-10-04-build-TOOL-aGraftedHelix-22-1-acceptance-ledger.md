# Acceptance ledger — TOOL-aGraftedHelix-22

**Serves:** journal TOOL-aGraftedHelix-22

Node `a`, 2026-10-05. The build commit is `3cfe9aa7`, over the dispatch records commit `e399a129`;
the spec needed no revision. No merge bar and no self-test suite ran in this pass. The criteria were
observed by the driver suite's new read-axis refusal arm run ALONE behind the suite's prologue, the
claim block's `gh_` helpers and the cell block's `seed_claim_row`, as a slice under
`tools/unattended/` with its fixtures under a short `%TEMP%` root: 26 executed against the
prologue's own 20, green against the kit. The arm was then observed RED with the read-axis
membership test removed from the driver in place, which the arm's scratch copy inherits; the driver
was restored and its hash checked. The slice was deleted after the last run. The whole suite is the
main loop's at VERIFYING, and the slice count, 6, is the evidence for its raised floors.

**Evidences:** TOOL-aGraftedHelix-22
- AC1 — `CLAIM_READS` — in the slice, a scratch driver whose `CLAIM_READS` lacked `foreign-stale` ran
  `--preflight tFresh --keepalive-id k2` under `CLAUDE_CODE_SESSION_ID=s-new` over a bare origin
  holding a `tFresh` claim of `s-other` under `k-other`, `status: live`, its `beat-utc` 600 s past
  `RESUME_STALE_BOUND`: it printed `UNATTENDED check 93 FAILED` naming `class foreign-stale` and the
  copy's `CLAIM_READS`, the claim ref read the same sha before and after, and
  `memory/builds/tFresh/RUN.md` did not exist. With the membership test also removed, the same call
  printed `claim taken over — tFresh · node other`, the ref moved `b1882041` to `89637a43`, the
  run-state file appeared, and all three assertions redded.
- AC2 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base e399a129e` printed `epoch: unattended · clean · 1.69`,
  naming no carrier left behind; the unattended version moved 1.68 -> 1.69 in 27 files.
- AC3 — `python tools/memory-tree/check-arms.py --report` — at the build commit the row read
  `check 93 branch 1  line 1864  ARMED`, ending
  `by tools/unattended/unattended.test.sh`, and `git grep` of every `unarmed-branches.txt` for a
  check-93 row found none. Red when the arm's assertion was commented out and the branch was pinned
  in `tools/unattended/unarmed-branches.txt`: the row read `PINNED`. Both files were restored.
