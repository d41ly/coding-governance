# TOOL-aFrugalTurnstile-2 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-2

No merge bar, no runner and no self-test suite ran in this pass. One driver script built scratch
repositories under a short temp root, with a tracked stand-in runner at `tools/run-gates/` that writes
its run record and appends one line to a marker file outside the repo, a tracked wrapper bar
declared in `.unattended.conf`, and the real `gate-fingerprint.sh`. It drove the hook from
`bef97330` and then the working file directly with a ref line on stdin, moving the remote by
`--no-verify` pushes. The base copy wrote no record and covered nothing, so AC1, AC2, AC3, AC9, AC10,
AC12, AC16 and AC17 were RED on it as written. AC4, AC14 and AC15 were RED on a staged break of the
working hook, the STUB, doc-only and own-rc guards removed, which wrote a record in each case. AC13
was RED on a slice with its HEAD and clean-tree conditions replaced by `false`. AC18 to AC20 were RED
on a break that skipped `check_bar_base`: it adopted both refused records and counted the lag from M.
AC5 to AC8 have no RED at base, which neither writes nor reads a record; each altered record was
shown not to cover by an unaltered control on the same merge, which did cover. The close still owes
the new arms in `.githooks/pre-push.test.sh` and the DEC covered arm in
`.githooks/pre-push.runlog.test.sh`, with its exit-table row and the raised floor, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-2
- AC1 — `kind full` — after X's green push the record held the ten keys in S1's order by `cut -f1`,
  `sha` X, `tree` X's tree, `kind full`, `by pre-push` and the vetted `bar`; the base left none.
- AC2 — `pre-push: covered on main push` — the --no-ff merge of X was covered by this git dir's
  record at X, the marker stayed at 1, exit 0; the base ran a FULL bar and the marker went to 2.
- AC3 — `it graded tree` — one more byte after the merge printed `not covered` naming both trees and
  the marker gained one line.
- AC4 — `the bar is the declared STUB` — a `GOV_GATE_CMD_TEST` push wrote no `gate-bar-green` and
  printed the declined line; the staged break wrote one.
- AC5 — `gate-bar-green` — with `verdict RED` and exit 1 the push was blocked and no record existed.
- AC6 — `it was earned by bar` — a record whose `bar` named `bash tools/other.sh` was not covered
  and the marker went 0 to 1; the unaltered control covered with the marker unchanged.
- AC7 — `self-tests HELD` — an empty `selftests` under `GATE_SELFTESTS=1` was not covered and the
  bar ran.
- AC8 — `could not be read` — an empty record `tree` was not covered and the bar ran.
- AC9 — `this git dir` — with no `gate-bar-green` and a `gate-full-green` naming X with the
  fingerprint and blob, the merge was covered `by run-gates` with the marker unchanged; the base
  scoped and ran the bar.
- AC10 — `a scoped green against base` — a `kind scoped` record on the adopted full green covered;
  on another `base` it printed that clause naming both shas and the bar ran scoped.
- AC11 — `decision=covered` — after AC2, `pre-push-bar` held three fields `default` and the runner
  path, and the last `pushes.log` line read `ev=end exit=clean decision=covered`.
- AC12 — `gate-bar-green.shared` — a push from a `git worktree add` tree left the common dir's copy
  `cmp`-identical to the worktree's record; the base left none.
- AC13 — `write_bar_green` — the sed-range slice wrote nothing with HEAD moved or an untracked file
  present and wrote on the clean control; the staged slice wrote in both cases.
- AC14 — `red on inherited legs only` — the inherited red landed rc 0 under `land`, printed the
  declined own-verdict line and wrote no `gate-bar-green`; the staged break wrote one.
- AC15 — `doc-only` — a `GATE_DOC_PATHS` push scoped docs-only and green printed `this push was
  scoped doc-only` and wrote nothing; the staged break wrote a `kind scoped` record.
- AC16 — `1` — the grep printed `1` on the working hook and `0` at `bef97330`.
- AC17 — `scoped gate` — the wrapper bar's FULL push at M wrote a `kind full` record; M plus one
  commit scoped from `full bar green` M with `GATE_BASE` M at the bar. The base was FULL on both.
- AC18 — `kind scoped` — the record at M on `base` B, with B's `kind full` record in `.shared`,
  scoped from M with the bar given M, "counted from its base" B, 4 landings; the break said 2.
- AC19 — `base` — with no full green naming its base the record was refused, "its base … is no full
  green this push can adopt", and the push was FULL; with B's record present B was adopted instead.
- AC20 — `GATE_FULL_MAX_LAG` — M two landings back on a base 16 back was refused, the base named
  "16 first-parent landings behind the tip (bound 10)", and the push was FULL.
