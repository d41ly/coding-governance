# TOOL-dDeclaredLoop-94 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-94

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-4 of the spec, over the working tree, by the first dispatch, which started from the base
`5031e98fd`. The `push-merge-tree-fatal` plant of `guard.py` ran alone by `--fixture --plant`, standing in
for the `loop guard fixtures` leg; the `conf-read-forms` plant of `budget.py` ran alone the same way,
standing in for the `loop budget fixtures` leg; `python -I -c` probes of `build_failure_detail`, and of
`load_tree_lib` in a scratch copy of the loop, lib and memory-tree folders, stood in for nothing a leg runs.
The sweep re-run at the base held every design claim: `build_failure_detail(` counts 5 PINNED in
`guard.py`; the loader caught `LookupError`, then `ImportError` and `SyntaxError`, and refused at the first
missing name; the three `tree_lib` rows of the `conf-read-forms` plant held. The one new name,
`run_unstartable_lines`, a nested def, passed the lexicon's suggest verb, so the offender pin does not
move. No shell file, shared record, help page or watched kickoff path is written.

The guard plant, timed by direct CLI back to back on a busy box, read worst-of-two 19.53 PINNED seconds
before the build and 22.65 PINNED seconds after it, so the delta of 3 PINNED seconds, rounded up, joined the
row's proxy note, 97 PINNED seconds, and 1.5 times it passing the old budget moved the `loop guard fixtures`
row to 146 PINNED seconds, under its manifest ceiling. An earlier pair read 36.08 PINNED seconds before and
10.10 PINNED seconds after, so the box's noise exceeds the grade's cost. The budget plant read 1.06 PINNED
seconds after the build, under a whole second of delta over the spec's reading, so its row does not move.

Owed to the close: every leg section 7 names; and RED-first, on its two `New arm:` lines, the
`push-merge-tree-fatal` plant with `build_failure_detail` taking the message whole, and the
`conf-read-forms` plant with `load_tree_lib`'s base catch and first-name refusal restored.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant conf-read-forms` with every function the unit's pass changed in
`tools/loop/loop_lib.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-94
- AC14 — `start failed: a` — the probe answered `start failed: OSError`, `start failed: [Errno 5]`, `start failed: boom`, `start failed: [Errno 2] No such file`, `start failed: a` and `start failed: b`.
- AC15 — `all held` — `python guard.py --fixture --plant push-merge-tree-fatal` exited 1 and printed `10 of 10 scenario(s) held · all held` PINNED, its row `graded, start failed, two lines` held naming `the clean re-merge failed: start failed: a` and its row `graded, start failed, two lines, the second line` held; no output line is `b`.
- AC16 — `derive_docstring_ids, derive_constant_charges` — in the scratch copy with both defs renamed the probe exited 1 printing one line naming `derive_docstring_ids, derive_constant_charges`; with the raise appended instead it exited 1 printing `memory-tree kit: RuntimeError: fx stand-in — govkit update --kits memory-tree` and no `Traceback`; `python budget.py --fixture --plant conf-read-forms` exited 0 printing its `raising` and `lacking both` rows, each naming `govkit update --kits memory-tree`, and `held`.
