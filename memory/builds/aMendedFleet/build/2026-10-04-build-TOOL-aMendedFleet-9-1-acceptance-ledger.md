# TOOL-aMendedFleet-9 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-9

**Evidences:** TOOL-aMendedFleet-9
- AC1 — `read_held_reds` — sliced with `resolve_python` out of `tools/unattended/unattended.sh` into a scratch script and called with this repository's anchor URL and `HELD_CI_WORKFLOW="remote-ci.yml"`: printed `held reader: run 37196051126 at c2ffcf87 · 83 held job(s) read · 15 red`, 83 TAB rows, 15 of them `failure` or `timed_out`, and no CR byte in any row under `cat -A`
- AC2 — `DEAD PROBE` — the same call with https://example.invalid/o/r.git printed the non-GitHub anchor line and 0 rows; with `HELD_CI_WORKFLOW="no-such-workflow.yml"` it printed the runs GET answering HTTP 404 and 0 rows; both returned 0
- AC3 — `write_held_asks` — in a `git clone --local` under `%TEMP%`/h9 whose `.unattended.conf` at R declares `ASKS_CMD` as the generator's `--asks` mode, with `read_held_reds` shadowed to print two red rows and one green row at R: two asks filed with one `SEV · HIGH` and one `KEEP` row each, `gen_build_index.py --asks <id>` read both OPEN and HIGH, stdout carried `re-rendered the generated views for 2 filed ask(s)` with four staged paths, and `python tools/memory-tree/gen_build_index.py --check` exited 0
- AC4 — `reused` — a second `write_held_asks` over the same two reds printed `reused` for both and filed nothing; with the alpha ask's three rows moved into another build's `BACKLOG.md` and committed, a third run printed `reused` for both, naming that other file for alpha
- AC5 — `HELD_CI_WORKFLOW` — blank in the conf committed at R and set to remote-ci.yml in the working tree: `write_held_asks` printed the DARK line naming R and the shadowed reader's call file stayed empty
- AC6 — `BACKLOG.md` — `HELD_CI_WORKFLOW` as the value ../x.yml at R printed the refusal and made no reader call; a backtick name and a name carrying U+001F were each refused by name with a zero line delta in `BACKLOG.md`. Staged breaks, each observed RED first: with the shape test replaced by `false` the bad value reached the reader and an ask was filed; with the name case replaced by a pattern that never matches both names reached `BACKLOG.md`
- AC7 — `git merge-base --is-ancestor` — a red row at a `commit-tree` child of R printed `not an ancestor of R` naming the full sha, with a zero line delta in `BACKLOG.md`
- AC8 — `grep -n write_held_asks tools/unattended/unattended.sh` — the gates-green call is line 7982, a bare statement after the bar loop's `done` and inside no condition, between the save and restore of the bar's `RB_*` capture, so its status reaches neither `DOD_OUT` nor the item's return; every AC2 and AC6 call printed rc 0
- AC9 — `bash tools/unattended/adopt-unattended.sh --check` — printed `in sync` and exited 0; `grep -c HELD_CI_WORKFLOW` printed 2, 1 and 1 over the render, the example and the conf. Staged break: the render reverted to HEAD with the template changed made it exit 1 naming the drifted render

## The suite arm

The new arm in `tools/unattended/unattended.test.sh` and the closing-review F4 arm, whose slice now
takes `write_ask_rows`, were cut out of the suite by line range with its helpers re-declared and run
alone: 36 assertions passed against the working driver, and against HEAD's driver 14 failed, the
three missing functions among them. The whole suite was not run; it is owed at the close.
