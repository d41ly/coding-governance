# TOOL-aPrimedIndex-4 — acceptance ledger

**Serves:** journal TOOL-aPrimedIndex-4

No merge bar and no self-test suite ran in this pass. Every criterion was observed through the new
arms 28 to 31 of `tools/push-main.test.sh`, run as a slice: the suite's prologue plus those arms.
Each arm clones the repository at its committed HEAD and pushes it to a bare remote as main. Against
the committed lander (this branch at the unit-3 commit) all four printed `FAIL` in 391 s. They then
ran in `pi4`, a clone of this branch carrying this pass's lander and suite as a local commit, where
all four printed `ok` and the slice printed `push-main.test: all cases ok`.

The regeneration also moved the existing attended-mint arm 26. That arm read the newest commit as the
mint, and a `regen:` commit now follows the mint whenever an output moved. The arm now finds the mint
commit by its subject. It still reds on `for TOOL-tFix-26`, and it reds the same way against the
committed lander: the newest-unit reader names only an id a spec defines (TOOL-aRoutedQuill-12), and
the fixture defines none. That red is inherited and is filed as an ask in this build. Arm 24 passed
against the new lander. The close still owes the lander self-test whole.

**Evidences:** TOOL-aPrimedIndex-4
- AC1 — `tools/push-main.sh --prepare` — arm 28: with one row removed from the clone's `memory/gotchas/INDEX.md` on a branch, `--prepare` produced a merge whose first parent is the advertised tip, whose index equals the tip's, and whose tree is clean. Against the committed lander the merge kept the stale row.
- AC2 — `Pass: none` — arm 29: the attended landing from `main` with the same stale row pushed a tip whose newest commit's subject begins `regen: generated outputs onto origin/main at <tip8>` and carries `Pass: none`. The pushed index equals the tip's, and the pushed tip equals HEAD. Against the committed lander the newest commit was the stale-row commit itself.
- AC3 — `regen.py` — arm 30: with the clone's `regen.py` replaced by one that exits 1, `--prepare` exited 1, printed `the generated outputs could NOT be regenerated` on stderr, and left `feat` checked out at its pre-run sha. Against the committed lander it exited 0 and prepared.
- AC4 — `grep -n "regen" tools/push-main.sh` — arm 31: with `regen.py` removed from the tip and the branch, `--prepare` printed `generated outputs were NOT regenerated — no regen.py beside this lander` and still prepared, exiting 0. The grep shows the header paragraph at lines 35 to 42 and the `run_regen` section.
