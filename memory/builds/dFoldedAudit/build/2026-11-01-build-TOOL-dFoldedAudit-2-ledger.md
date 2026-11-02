# TOOL-dFoldedAudit-2 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-2

The acceptance criteria were observed by this unit's builder over the tree of this commit, on fixture R of §6 and on the suite's reduced layout, by scratch probes of the driver and the gate as CLIs. No gate, suite or bar ran in this pass. Each `New arm:` line of §7 is written and is the close's to observe RED on its staged break and GREEN restored, and it records them here under a `Pass: none` commit.

**Evidences:** TOOL-dFoldedAudit-2

Fixture R was a scratch git repository at `%TEMP%/fa2r` on branch `main` with no remote, rebuilt per case. It carried two things §6 does not name and does not exclude. `HALT_FLOOR` and `HOLD_FLOOR` join its conf, because a conf with neither prints two check 2 lines about the floors on every run, which AC1's `no line` would read. `tools/policy/budgets.py` joins the kit copy, because `validate` imports it whenever a policy file is committed. AC9's rotation commit records the live `RUN.md` as `M` beside the archive, which is what a rotation writes and what `read_first_commit_date`'s floor is for: a commit touching the archive alone leaves `check_landed_facts_due`'s last-commit shortcut reading the early date.

- AC1 — `blockers 0 · CONVERGED · highs 1 · minors 2 · folded 3 · promoted 0 · disposition fold` — the call exited 0 and `RUN.md`'s last row ended with this text; committed, the gate printed no check 2 line.
- AC2 — `spec subject(s) S1 record a terminal row with no highs and minors counts or with disposition fold` — the same row in an `EARLY` record printed this through the old clause.
- AC3 — `record disposition fold on a row carrying highs and minors` — the driver refused the slug subject naming `--folded`, and the hand-written row on the slug printed this.
- AC4 — `DISPOSED BY NATURE` — the bounded exit on two blockers exited 0 printing `BOUNDED`, this and `FOLDS`, and the gate printed no check 2 line.
- AC5 — `fall short` — the driver refused printing this, and the hand-written row under `verdict CLEAN` printed `record an exit row past SPEC_FOLD_CUTOFF`.
- AC6 — `at most nine digits` — `--folded 08` printed this; `--folded 1 --promoted 2 --disposition fold` refused naming `--disposition promote`, the zero counts with a fold refused naming `no disposition`, the absent disposition refused naming `--disposition fold`, no refused call wrote a row, and the hand-written row printed `record an exit row past SPEC_FOLD_CUTOFF`.
- AC7 — `which folds nothing` — under a committed `promote-all` the fold printed this; `--folded 1 --promoted 1` refused naming `promote-all`; `--folded 0 --promoted 1 --disposition promote` exited 0 writing `folded 0 · promoted 1 · disposition promote`; `disposal = "fold-all"` refused printing `policy: refused`.
- AC8 — `SPEC_FOLD_CUTOFF is blank or undeclared` — the gate printed this over a blank cutoff; the promote wrote a row ending `highs 1 · minors 0 · disposition promote`, `--folded 0` refused, and with `tools/policy/` deleted the first call exited 0 without printing the reader's no-kit note, so no switch was read.
- AC9 — `--folded 3` — with AC1's counts it exited 0 over the rotation; `--folded 0` refused on an `EARLY` record with a later `DATED` commit, because the record began before the cutoff.
- AC10 — `against a floor of 2` — the gate printed this with one new id, and no check 2 line with two; AC1's row with no new id printed none, with `DISPOSITION_CUTOFF` declared and stripped, the strip's announcement observed.
- AC11 — `SPEC_FOLD_CUTOFF` — with `SPEC_FOLD_CUTOFF="soon"` the gate's check 2 failure named the key and `soon`, on a continuation line of that failure, as every clause feeding `rv_bad` does.
- AC12 — `by its nature, through the chain's next subject` — a further round on terminal S1 refused printing this and wrote no row; under a blank cutoff and on `--subject tFix` it printed `by the severity rule, and never re-rounded`.
- AC13 — `grep -c 'which folds nothing' tools/unattended/unattended.sh` — it printed 1, the line a `fail 37`, and `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh` printed 318 and 264.
- AC14 — `grep -cE -- '^#   unattended[.]sh --review .*--folded <N> --promoted <N>' tools/unattended/unattended.sh` — it printed 1.

Beyond the criteria. The driver and gate at `HEAD` were run against the working copies over one matrix, and the output and the record compared byte for byte, timestamps and the base sha aside: twenty `--review` calls under a blank cutoff, the closing subject under a dated one, and four hand-written rows through the gate at both dates, the blank-cutoff announcement aside. Every comparison was identical, which is §1's last sentence. Rows the criteria do not name were probed too: row 2 on a mid-loop round, row 3's bare call under each rule, row 4, row 5, a promotion under `folds` owing `max(1, p - m)`, and a sum above the findings passing the gate.

Row 3's bare call under `folds` answers through `:12816` and not `:12790`, by §4's `In verb_review` table, which skips the no-disposition refusal there. It names `exits BOUNDED` and `--highs`, which is what `TOOL-dFoldedAudit-3`'s hand-off reads.
