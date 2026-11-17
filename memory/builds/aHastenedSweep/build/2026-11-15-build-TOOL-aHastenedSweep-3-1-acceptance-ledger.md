# Acceptance ledger — TOOL-aHastenedSweep-3

**Serves:** journal TOOL-aHastenedSweep-3

Built against spec rev-2 in one pass commit, on node a, in the run's worktree at `badcd0833`, the
lease record above the dispatch commit `3a8df2ee7`, with units 1 and 2 merged beneath it. A first
builder of this pass was killed by a session restart before committing; its uncommitted edits were
re-read against the spec, kept, and verified here as if drafted in this pass. The §4 evidence holds
at that tip: the print-mode line follows the one `INDEX_SET` assignment, no line between the python
resolution and the print mode assigns `status` but `fail`, every `fail` call above the print mode
sits in the structure checks that precede it, the size-cap note that also opens `HYGIENE ` prints
only from the cap checks below the print mode, and the hygiene shell's launch of `corpus_ids.py
--check` is the only caller of `check_read_path`'s `ask_shell("--print-index-set", root)`.

The observations below are each criterion's own command, run by hand with the change in place before
the commit over a fresh copy of the suite's `_b1` tree, built at `%TEMP%/ixh3` by a probe script under
the run's scratchpad that writes the same conf, charter, records and two commits the suite does, and
removed after. `bash -n` over both shell files and `python -m py_compile` over `corpus_ids.py` exited 0.
No suite, gate leg or bar ran in the pass.

Owed to the main loop at the close:
- AC7, the live-tree A/B: the full hygiene run at the shipped engine and at this unit's, its corpus
  classifier block `cmp`-equal and the exit codes equal, recorded here under a `Pass: none` commit.
- The legs §7 lists, `check-arms` among them, and in the `memory-hygiene self-test` leg the three
  `New arm:` lines' red-then-green: the hand-down arm red at the shipped engine and with the
  here-string emptied; the failure arms red with `_IXH` ignoring `status`, then ignoring `ONLY`, then
  with the prefix written only when eligible; the standalone arm red with `check_read_path` testing
  `!= "1"`.

**Evidences:** TOOL-aHastenedSweep-3
- AC1 — `corpus_ids: GOV_BASH is set` — `GOV_BASH=<fixture>/no-such-bash bash check-memory-hygiene.sh`
  in the clean tree exited 0 and printed the retired `READ_PATH_CEILING` notice, so the run reached the
  corpus classifier, and printed neither `corpus_ids: GOV_BASH is set` nor the read-path rule's finding
  for an unindexed charter citation.
- AC2 — `answered with findings` — with `memory/stray.md` staged in a copy of the tree, the plain run and
  the run with `GOV_INDEX_SET_STDIN=1` exported each printed the structure check's `FAILED` line for the
  unexpected entry and the `answered with findings` refusal, and each exited 1.
- AC3 — `answered with findings` — `bash check-memory-hygiene.sh --only 16` in that copy printed the
  refusal.
- AC4 — `corpus_ids: GOV_BASH is set` — `python corpus_ids.py --check` in the clean tree, with
  `GOV_INDEX_SET_STDIN` unset and the missing `GOV_BASH`, printed it and exited 1; with the variable set
  to `2` it printed it as well.
- AC5 — `_pyexempt` — the `_pykeys` ERE over `tools/memory-tree/*.py` yields `GOV_INDEX_SET_STDIN`, and
  `grep -n GOV_INDEX_SET_STDIN` over the hygiene suite finds it in `_pyexempt` and in the comment above it.
- AC6 — `GOV_INDEX_SET_STDIN` — `grep -n` over `memory/map/features/memory-tree-hygiene.md` finds it in
  the `--print-index-set` bullet.
- AC7 — `cmp` — NOT OBSERVED in this pass: the live-tree A/B is the main loop's at the close, as the
  criterion's permission line assigns.

## Close observations, by the main loop

The live-tree A/B, run by the main loop: the shipped kit at `f25308f01` overlaid on `tools/memory-tree/` in a detached worktree frozen at the subject commit, against that commit's own kit, both over the same tree, stdout, stderr and exit code each compared with `cmp`. Every run shared node a with other work, so the walls are contended (PINNED, 2026-11-15 and 2026-11-16).
- The whole run at `c0008f704`: shipped 1039.6 s, changed 349.1 s, 173 lines, identical (PINNED). This is AC7's observation; the corpus classifier block is inside the compared bytes.
- The whole `check-memory-hygiene.sh` run at `e30d94df9`, every unit of the build in: shipped 663.3 s, changed 239.2 s, 173 lines each, stdout, stderr and exit code identical (PINNED).
The hygiene suite's arms were observed through a slice: the suite's prologue, its `_b1` fixture and the new arm blocks, run from the kit directory, 13 assertions green at `0c1935569` (PINNED). Each staged break was applied to the working copy, the slice or selftest run, and the file restored with `git checkout --`.
- The hand-down arm went red at the shipped engine and with the here-string emptied, and green at the tip.
- The failure arms went red with `_IXH` ignoring `status` (plain and exported), with it ignoring `ONLY` (the scoped arm), and with the prefix not written on every run (the exported arm); green at the tip.
- The standalone arm went red with `check_read_path` testing `!= "1"`; green at the tip.
