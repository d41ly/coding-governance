# Acceptance ledger — TOOL-aHastenedSweep-4

**Serves:** journal TOOL-aHastenedSweep-4

Built against spec rev-2 in one pass commit, on node a, in the run's worktree at `274b26480`, with
units 1, 2 and 3 beneath it. The spec's claims about current code were re-read at that tip before the
first edit: the corpus classifier block's launch with unit 3's `GOV_INDEX_SET_STDIN=$_IXH` prefix and
here-string, the claimant marker nearest above its status line, the catalogue block's launch, status
and offender-key lines, `walk` returning one dict literal, and both `importlib` loads in `gotchas.py`.

The observations below are each criterion's own command, run by hand with the change in place before
the commit. F1 and F2 were built at `%TEMP%/hs4f` by a probe script under the run's scratchpad in the
spec's shape: F1 an armed orphan pin with no orphan and one class record naming no gate, F2 that plus
a memory README citing an id nothing defines and one invariant record. `bash -n` over both shell files
and `python -m py_compile` over both modules exited 0, and the lexicon's `--suggest` answered OK for
`cmd_check_with_ids` and `_load_corpus_ids` as `py.function`. No suite, gate leg or bar ran in the pass.

As an extra fixture-level parity probe, the whole hygiene output in F1 and in F2 was captured with
the three engine files at the parent commit and again with this unit's, from the same kit path: both
pairs were `cmp`-equal with equal exit codes. It stands in for nothing the close owes.

Owed to the main loop at the close:
- AC9, the live-tree A/B: the full hygiene run from the parent's `tools/` and from this unit's,
  `cmp`-equal with equal exit codes, recorded here under a `Pass: none` commit.
- AC7's `check-arms.py --check`, refused to this role by the role hook, so it runs with the legs §7
  lists.
- The three `New arm:` lines' red then green: the `gotchas.py --selftest` arm red with the frame's
  rc fields swapped and again with the verb's memo assignment removed; the `corpus_ids.py --selftest`
  arm red with `walk` returning its stored object, with the memo on at import, and with a key on
  `root` alone; the hygiene suite's split arm red with the two blocks assigned to each other's
  variables, and its `FLOOR_ASSERTIONS` raise observed.

**Evidences:** TOOL-aHastenedSweep-4
- AC1 — `frame F1 same 0 1` — the scratch `t4-frame.py` over F1 printed it, and over F2 printed
  `frame F2 same 1 1`: each framed block equals that verb's standalone capture less its trailing
  newlines, and each rc field its exit code.
- AC2 — `ls-files 2` — the scratch `t4-walk.py` over F2, counting the `git ls-files` calls of every
  `corpus_ids` module the verb loads, printed it; with the verb's memo assignment made inert as the
  staged break it printed `ls-files 3`.
- AC3 — `conf keyed yes` — the scratch `t4-memo.py` over a copy of F2 printed `default None`,
  `frozen yes`, `hit yes`, `off sees new` and `conf keyed yes`, in that order.
- AC4 — `GOV_INDEX_SET_STDIN=` — the xtrace run in F2 held one `gotchas.py --check-with-ids` launch
  and no standalone launch of either verb. Bash 5.3 traces the prefix assignment on its own line
  directly above the launch line, and that line read `GOV_INDEX_SET_STDIN=1`. Under `--only` with the
  seven numbers the trace held no `--check-with-ids` line and one launch of each standalone verb.
- AC5 — `--offenders` — the unscoped run in F2 exited 1 and printed the orphan id line and the
  ungated record line; with `--offenders` each was keyed under its own block's range.
- AC6 — `raise RuntimeError` — staged as the first line of `cmd_check_with_ids` in a copy of the kit,
  the F2 run exited 1, printed the traceback, launched the verb once and nothing else, and
  `--offenders` keyed the traceback under the corpus classifier's range. Restored, AC5 held.
- AC7 — `py_compile` — `bash -n` and `python -m py_compile` exited 0, and the two `grep -cxF` probes
  for the `_gotrc` and `_idsrc` status lines each printed 1. `check-arms.py --check` is owed above.
- AC8 — `imports = ["ask_shell", "main"]` — the `kit.toml` clause above `consumer = "gotchas.py"`
  reads it, the kit README's `gotchas.py` row names `--check-with-ids`, and `gotchas.py --nope`
  printed a usage line naming it.
- AC9 — `cmp` — NOT OBSERVED in this pass: the live-tree A/B is the main loop's at the close, as the
  criterion's permission line assigns.

## Close observations, by the main loop

The live-tree A/B, run by the main loop: the shipped kit at `f25308f01` overlaid on `tools/memory-tree/` in a detached worktree frozen at the subject commit, against that commit's own kit, both over the same tree, stdout, stderr and exit code each compared with `cmp`. Every run shared node a with other work, so the walls are contended (PINNED, 2026-11-15 and 2026-11-16).
- The whole run at `cf64f39df`: shipped 907.8 s, changed 244.9 s, 173 lines, identical (PINNED). This is AC9's observation.
- The whole `check-memory-hygiene.sh` run at `e30d94df9`, every unit of the build in: shipped 663.3 s, changed 239.2 s, 173 lines each, stdout, stderr and exit code identical (PINNED).
The hygiene suite's arms were observed through a slice: the suite's prologue, its `_b1` fixture and the new arm blocks, run from the kit directory, 13 assertions green at `0c1935569` (PINNED). Each staged break was applied to the working copy, the slice or selftest run, and the file restored with `git checkout --`.
- The split arm went red with the two blocks swapped in the split; green at the tip.
- `gotchas.py --selftest` went red with the frame's rc fields swapped and with `_WALK_MEMO = {}` removed from `cmd_check_with_ids`; green at the tip.
- `corpus_ids.py --selftest` went red with `walk` returning its stored object, with `_WALK_MEMO` set to a dict at import, and with the key on `root` alone; green at the tip.
