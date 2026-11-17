# TOOL-dDeclaredLoop-68 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-68

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-4 of the spec, over the working tree: the `normalise`, `normaliser-missing`, `bash-syntax`,
`probe-rerun` and `timeout-grandchild` plants run alone by `--fixture`, standing in for the
`loop computed witness` leg; a `python` probe rebinding `run_normaliser` in process to print each raw
output, the roots and the written program; and the `grep` probes, standing in for the `docs` and
`kit/dogfood doc parity` legs. The section 5 sweep re-run at this pass's base held every figure and
design claim it states: the `run_witness_commands(` lines, the importers, the encoding and size-cap rows,
the conf count, the budget row and the help anchors' fingerprints all read as the spec pins them, and
`lib-attribute.sh` and the module's re-run path were unmoved since the spec's re-read. The three new
functions each lead with a declared verb by the lexicon's suggest verb. The refusal label for a bash
that never ran a step is deviation 682.

Owed to the close: every leg section 7 names, the `loop computed witness` leg's time read once against
its budget row (left unmoved: the plants alone took 8, 1, 4, 9 and 6 PINNED seconds), and the RED-first
observation of the `tools/loop/loop_witness.py` arm over AC1, AC3 and AC4 on its staged break. The
`timeout-grandchild` plant's call, which now holds the normaliser's bash under the same short bound, read
4.0 PINNED seconds inside its ten-second window.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/loop_witness.py --selftest` with every function the unit's pass changed in
`tools/loop/loop_witness.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-68
- AC1 — `e3b0c44298fc` — `python loop_witness.py --fixture --plant normalise` printed `exit 0 6911d22ae925` for both re-runs and PASS, exit 0; the probe showed each raw output open with a `/tmp/lw-` line from bash's `pwd`, which only the third root's rule stripped, and both `.norm` files hashed the bytes of three empty lines and `took`, never the empty output.
- AC2 — `write_normaliser` — `grep -c write_normaliser loop_witness.py` printed 5 PINNED and `git grep -n '"sed"' -- tools/loop/` printed nothing.
- AC3 — `9a271f2a916b` — `--plant bash-syntax` printed `exit 0 · 9a271f2a916b`, and `--plant probe-rerun` read `confirmed` at the pinned commit, `refuted` at the later one and `inconclusive` at `0badc0de`, each plant exiting 0.
- AC4 — `witness: normaliser unavailable` — `--plant normaliser-missing` printed the refusal naming the places `resolve_kit_dir` looked, one worktree listed, and the in-process `rerun` exiting 1 with its `rerun · inconclusive · ` line and the reason on stderr, exit 0.
- AC5 — `hashed exactly as` — `grep -c` printed 0 over `help/loop.md`, `never normalised` 0 over `loop_witness.py`, and `normaliser-missing` 1 PINNED over each of `help/loop.md` and `tools/loop/README.md`.
- AC6 — `grep -n write_normaliser` — printed one grammar line over each of `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md`, alike, the second re-rendered by `adopt-memory-tree.sh --render`.
