# Acceptance ledger — TOOL-aHastenedSweep-6

**Serves:** journal TOOL-aHastenedSweep-6

Built against spec rev-2 in one pass commit, on node a, in the run's worktree at `6a2b05f0b`. The
spec's claims about current code were re-read at that tip before the first edit: the one-process
launch, its split and its fallback line in `tools/memory-tree/check-memory-hygiene.sh`, the comment
above the corpus classifier block, the frame write, `except` line and docstring of
`tools/memory-tree/gotchas.py#cmd_check_with_ids`, the with-ids arm of
`tools/memory-tree/gotchas.py#cmd_selftest`, unit 3's five and unit 4's two assertions and the floor
with its last RAISED entry in the hygiene suite, the suite's exemption note, the `corpus_ids.py`
docstring bullet and the dossier bullet.

The observations below are each criterion's own command, run by hand with the change in place before
the commit. The scratch probes `t6-onered.sh`, `t6-wrap.sh` and `t6-frame.py` build their fixtures
under `%TEMP%/hs6f` in the `_b1` shape; each staged break ran on a copy of the worktree's `tools/` under
`%TEMP%/hs6k`, a git repository so the install prefix derives. Two further probes ran this unit's own
new code alone, never the suite or the selftest: `t6-suiteblock.sh` extracted the new suite block and
ran it over a `_b1` fixture, printing four `ok` lines and `n=4 st=0`; `t6-armcode.py` extracted the
selftest's `run_framed` through the second new arm and executed it in the module's namespace, printing
`arm ok` for the refactored arm (`with-ids 0 1 same · ls-files 2`) and both new ones. No suite, gate leg
or bar ran in the pass.

Owed to the main loop at the close:
- `check-arms.py --check`, AC7's first command: the role hook refuses it to this builder.
- AC8, the live-tree A/B of the whole hygiene run from the parent's `tools/` and from this unit's,
  under a `Pass: none` commit, as its permission line assigns.
- AC5's figure: the hygiene suite's printed assertion count equals the raised floor.
- Each `New arm:` line's red-then-green: the two one-red arms under `_idsrc` and `_gotrc` exchanged at
  the end of the split; the wrapper arm under the fallback's `_idsrc=1` set to 0, then its `_onepy=1`
  dropped; the floor under unit 3's block wrapped in `if false; then … fi`; and the two new selftest
  arms under `err.getvalue()` dropped from the frame write, then `traceback.print_exc()` moved after
  the redirect.

**Evidences:** TOOL-aHastenedSweep-6
- AC1 — `bug-class-only 17-19 yes 13-16 no` and `id-classifier-only 13-16 yes 17-19 no` —
  `t6-onered.sh` printed both. With `_idsrc` and `_gotrc` exchanged at the end of the split it printed
  `bug-class-only 17-19 no 13-16 yes` and `id-classifier-only 13-16 no 17-19 no`: both lines changed.
- AC2 — `wrap 0 rc 1 keyed 13-16 relaunch 0` and `wrap 2 rc 1 keyed 13-16 relaunch 0` — `t6-wrap.sh`
  printed both. With the fallback's `_idsrc=1` set to 0 it printed `rc 1 no key` at both exits; with
  its `_onepy=1` dropped it printed `relaunch 1` at both.
- AC3 — `with-ids err-first 3 · second same` — `t6-frame.py stderr` printed it. With `err.getvalue()`
  dropped at the frame write it printed `frame-one WRONG` holding only the stdout line; with stdout put
  ahead it printed `frame-one WRONG` holding the stdout line first.
- AC4 — `with-ids raise 1 traceback · second same` — `t6-frame.py raise` printed it. With
  `traceback.print_exc()` moved after the redirect's `with` block it printed `NO-TRACEBACK`; with
  `except Exception` narrowed to `except OSError` the probe ended in
  `RuntimeError: staged in the with-ids arm`.
- AC5 — `FLOOR_ASSERTIONS=719` — `grep -cx` printed 1, and the RAISED line above it names
  `TOOL-aHastenedSweep-3`, `TOOL-aHastenedSweep-4` and `TOOL-aHastenedSweep-6`. The suite's printed
  count against it is owed above.
- AC6 — `in-process traceback` — `grep -c` over `gotchas.py` printed 4; `gotchas.py --check-with-ids`
  counted 1 in the suite and 1 in the dossier; `GOV_INDEX_SET_STDIN=1` counted 1 in `corpus_ids.py`
  and 1 in the shell's comment block above the corpus classifier block.
- AC7 — `git diff -U0` — over the hygiene shell it shows two added comment lines and nothing else;
  `bash -n` on both shell files and `python -m py_compile` on `gotchas.py` and `corpus_ids.py` exited
  0. `check-arms.py --check` is NOT OBSERVED in this pass: owed above.
- AC8 — `cmp` — NOT OBSERVED in this pass: the live-tree A/B is the main loop's at the close, as the
  criterion's permission line assigns.
