# TOOL-aFrugalTurnstile-8 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-8

No merge bar and no self-test suite ran in this pass. AC1 to AC8 ran as ONE scratch fixture under
`%TEMP%`: a bare remote, a work repo with the lander copied to `tools/push-main.sh`, no pre-push hook
wired, and a stub `post-merge.sh` in `tools/run-gates/` that sleeps 8 s and writes its argv to a
marker, each case committing its own `.githooks/gate-env.sh` and landing, the markers read after one
13 s wait. RED first: the same fixture over `git show bef97330:tools/push-main.sh` landed every case
with rc 0, printed no post-merge line and left every marker absent, so no start record existed. GREEN
against the change: the lines and markers below. AC9 ran as the two `diff` compares it names. The
pm1 to pm9 arms added to `tools/push-main.test.sh` encode the same cases and were syntax-checked
with `bash -n`, not run: the close owes the §7 legs, `push-main self-test` whole among them, plus the
map, lexicon and install-prefix legs over the new function.

**Evidences:** TOOL-aFrugalTurnstile-8

- AC1 — `--remote origin` — the capture returned in 5 s with rc 0, and the marker read `8a19f9c0… --remote origin`, the landed sha
- AC2 — `post-merge bar started on <sha8> — pid` — one such stderr line; `gate-post-merge.start` held `sha` equal to HEAD, `pid`, `winpid`, `log` naming an existing file, and `by push-main`
- AC3 — `remote CI runs it` — one line, and no marker after the wait
- AC4 — `grep -c 'post-merge'` — 0 over the lander's output, and no marker
- AC5 — `outside 'local ci'` — the line named `yes`, and no marker
- AC6 — `grep -c 'post-merge'` — 0 both where R declared `local` and the landed commit deleted it, and with `GATE_POST_MERGE=local` exported over a tip declaring nothing; the dirty-tree run refused with rc 2 and printed no post-merge line; no marker in any
- AC7 — `no run-gates kit holding post-merge.sh` — printed with rc 0, and the remote's main equalled the landed sha
- AC8 — `--land --slug tB` — from a linked worktree after `--prepare --slug tB`, the marker held the prepared merge's sha, `git rev-parse HEAD` in that worktree
- AC9 — `diff` — the slice compare against `.githooks/pre-push` printed nothing; a scratch copy with `hit=1` changed to `hit=2` printed the differing line
