# TOOL-aEvidencedLens-14 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-14

Check 19 walks a terminal record when either scan hits. The pass commits `091f81b0f` and `7f756f612`
record no direct-check figures: the first adds three `round walk:` arms to `check-unattended.test.sh`,
written and not run, and the second makes AC3's staged break prove its leg alive. No
`check-unattended.sh` run over a scratch fixture was made for this ledger. The greps were re-run at
HEAD `3bf1726b5`; `tools/unattended/check-unattended.sh` moved after the pass in `029b0522a` and
`efad4cee4`.

**Evidences:** TOOL-aEvidencedLens-14
- AC1 — `1 -> 2` — the arm `round walk: AC1 - an owner raise merged into a terminal record's run names no round write` and its fixture assertion carry it; its red against the pass-start leg is read at a suite run. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC2 — `2 -> 3` — `round walk: a run raise beside an owner raise fails check 19 once` carries it. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC3 — `REVIEW_ROUNDS="3"` — `round walk: an evil run merge fails check 19 once` and `round walk: a walk that drops the merge itself names nothing`, with `7f756f612`'s liveness `hit` that the broken library still names AC2's `2 -> 3`. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC4 — `maywr\$` — the grep printed line 2490, `if [ -n "$maywr$mayrw" ] && [ "$maywalk" = 1 ]; then`, at HEAD; over `091f81b0f~1` it printed nothing, the condition there reading `"$maywr"` alone. The comment block above it opens `THE WALK'S TRIGGER IS SHARED BY EVERY SCAN THAT SHARES THE WALK`.
- AC5 — `round walk:` — `grep -c` printed 7 over `tools/unattended/check-unattended.test.sh` at HEAD and 0 over `091f81b0f~1`.
