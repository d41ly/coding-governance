# TOOL-aFrugalTurnstile-7 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-7

No merge bar and no self-test suite ran in this pass. AC1 to AC7, AC9, AC11 and AC12 ran one scratch
fixture script, extended from TOOL-aFrugalTurnstile-11's, under a short temp root: a bare remote with
the red ref staged by a forced push, a work clone whose hooks dir holds a copy of the hook, a
stand-in runner and a tracked wrapper bar that append to a marker file, and a git shim first on
`PATH` logging every argv, with `GATE_TURNSTILE_DIR` pointed at a scratch dir. Each case ran the
hook at base bef97330 first, or at the previous commit a90b2d820 for AC11 and AC12 (base has no bar
records), then the working hook. At base, AC1 and AC5 scoped from the full green with no
`ls-remote`, AC4's `--decide` printed nothing, and AC6's `--decide` printed nothing in all three
states and added a journal pair each time. At a90b2d820, AC11's red on the covering record's own sha
left the push covered, and AC12's written record named the scoped sha as its base. All RED. On the
working hook every case was GREEN. AC3 is a no-change criterion, so it ran green on both. AC8 and
AC10 are a `diff` and two greps over the working tree. The new arms in `.githooks/pre-push.test.sh`
and the two exempt rows in `.githooks/pre-push.runlog.test.sh` are written and not run; the close
owes every §7 leg, the pre-push self-test and the pre-push run-log line suite among them.

**Evidences:** TOOL-aFrugalTurnstile-7
- AC1 — `pre-push: FULL gate` — with `GATE_POST_MERGE=local` at R and the red one landing past the full green, the push read FULL naming the red's short sha, the stub bar recorded `full=1`, and the shim log held one `ls-remote` line; base scoped.
- AC2 — `pre-push: scoped gate` — with the full green a strict descendant of the red, the push printed the `post-merge bar:` cleared line naming the red and the adopted green, then scoped.
- AC3 — `GATE_POST_MERGE` — with no `GATE_POST_MERGE` at R with the ref present, the shim log counted 0 and the decision line matched the base hook's shape, scoped from the same full green.
- AC4 — `full ` — with the push URL set by `git remote set-url --push` to a missing path, `--decide` printed one line naming refs/gov/bar-red as unreadable (`git ls-remote exited 128`), exit 0; base printed nothing.
- AC6 — `sha1sum` — in the none, scoped and covered states `--decide` printed one line each (`full `, `scoped ` and the 40-hex full sha, `covered ` and the scoped record path), exit 0, the git dir's sums were unchanged after the warm-up, no refusal or bar file, no journal line and no marker line.
- AC7 — `pre-push-refusal` — a dirty tree and a tip not equal to HEAD each exited 1 with an empty stdout and no refusal file; one argument and a tip naming no commit each exited 2 with the usage line on stderr.
- AC8 — `remote_ladder_sh` — the `diff` of the two awk-extracted blocks, the hook's and `tools/lib/resolve-remote.sh`'s, printed nothing.
- AC9 — `GOV_REMOTE` — with two remotes, a detached HEAD and no remote named, `--decide` exited 2 naming GOV_REMOTE; with `origin` given it printed a scoped line, exit 0.
- AC10 — `.githooks/pre-push` — each of the two header greps over `.githooks/pre-push` printed one line, at lines 33 and 42, the second being `WHAT THE POST-MERGE READ DOES NOT CHECK`.
- AC11 — `pre-push: covered` — with the covering record at L and the red at L the push read `pre-push: FULL gate` naming the red and the marker gained a line; with the red at L's parent it printed the cleared line and `pre-push: covered`, marker unchanged; in the scoped state `--decide` printed the same 40-hex sha the stub bar recorded as `GATE_BASE`.
- AC12 — `gate-bar-green.scoped` — after a full push, a scoped push and a scoped push from that scoped record, the written record named the first push's full green as `base`, and a fourth push scoped from that record; at a90b2d820 the record's base was the scoped sha and the fourth push fell back to the full slot.
