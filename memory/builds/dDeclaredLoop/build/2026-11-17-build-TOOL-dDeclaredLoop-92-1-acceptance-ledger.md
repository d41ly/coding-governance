# TOOL-dDeclaredLoop-92 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-92

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-5 of the spec, over the working tree, by the first dispatch, which started from the base
`ccb8a5a89`. The `push-merge-tree-fatal` plant of `guard.py` ran alone by `--fixture --plant`, standing in
for the `loop guard fixtures` leg; `python -I -c` probes of `build_failure_detail`, of the parsed
`loop_witness.py` and of `read_clean_env` in a scratch copy of the loop folder, with an `awk` and `cmp`
compare of the two `git_env_leaks_py` spans, stood in for the `loop computed witness` leg and the inline
parity leg. The sweep re-run at the base held every design claim: eight modules import `read_clean_env`
from `loop_witness.py`, which calls it too; `build_failure_detail(` counts 5 PINNED in `guard.py`; the
one `read_memory_tree` patch sits in `budget.py`; no help page names the three terms. The lexicon offender
pin is untouched since the pass mints no function, the two new plant rows raising through a generator's
`throw` in a lambda; `GIT_ENV_LEAKS` sits in the undeclared `py.constant` cell, the suggest verb exiting 2.
No shell file, shared record or watched kickoff path is written.

The plant, timed before and after by direct CLI, read worst-of-two 9.76 and 10.39 PINNED seconds, so the
delta of 1 PINNED second, rounded up, joined the row's proxy note, 94 PINNED seconds, and 1.5 times it
passing the old budget moved the `loop guard fixtures` row to 141 PINNED seconds, under its manifest
ceiling.

Owed to the close: every leg section 7 names; and RED-first, on its two `New arm:` lines, the
`push-merge-tree-fatal` plant with `build_failure_detail` restored to its base spelling, and the
`git_env_leaks_py` parity population with one member of the `loop_witness.py` copy edited.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.
Not observed: the arm in `tools/lib/resolve-python.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-92
- AC8 — `False` — the `ast` probe of `loop_witness.py` found no `Import` or `ImportFrom` naming `tree_lib`, no str constant `tree_lib.py`, and no call of `read_memory_tree` or `load_tree_lib` in `read_clean_env`; the two `git_env_leaks_py` spans, each piped through `tr -d '\r'`, compared equal under `cmp`, 19 PINNED lines each; in a scratch copy of the loop folder the spec's probe printed `False` and exited 0, and with the base's `loop_witness.py` in the same copy it raised `LookupError` naming `tree_lib.py`.
- AC16 — `start failed: OSError` — the probe answered `start failed: OSError`, `start failed: [Errno 5]`, `start failed: boom` and `start failed: [Errno 2] No such file`; `python guard.py --fixture --plant push-merge-tree-fatal` exited 1 and printed `8 of 8 scenario(s) held · all held` PINNED, its rows `graded, start failed, no message` and `graded, start failed, an errno alone` held naming `the clean re-merge failed: start failed: OSError` and `the clean re-merge failed: start failed: [Errno 5]`.
