# PLAY-dOrderedCharter-82 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-82

Each line is a probe this pass ran at rev-2 of the spec, over `4bb67cde0` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: each checker the criteria name is the close's, and where a line says
"owed" the main loop observes it after every unit is terminal. The probes ran a criterion's own command, the
renderer's flag over a scratch copy of its kit, or the matrix function with its child swapped for one that fails.

**Evidences:** PLAY-dOrderedCharter-82
- AC1 — `python tools/run-gates/py_reads.py` — owed: a role agent's scratch guard refuses the reads leg.
- AC2 — `python tools/run-gates/py_reads.py --guards "govkit acceptance matrix"` — owed, as for AC1. `git grep -n "import render_playbook" -- tools/govkit/matrix.py` finds no line after the pass.
- AC3 — `python tools/playbook/render_playbook.py --bullet-keys` — exited 0 printing the seven keys in the criterion's order, from the repository root and from the scratch folder outside it (PINNED, at 4bb67cde0 with the pass applied). Its refusal printed `render-playbook: REFUSED —` and exited 1 for a kit copy outside any git repository and for a kit copy in a fixture repository with no template.
- AC4 — `role_roster = "- stated"` — the criterion's `python -c` printed `['adopter_rules = "- stated"', 'node_table = "stated"', 'role_roster = "- stated"']`, and `derive_bullet_placeholders` raised `RuntimeError` naming the exit code and the stderr of a child that exits 3 (PINNED, at 4bb67cde0 with the pass applied).
- AC5 — `python tools/govkit/matrix.py` — owed: a role agent's scratch guard refuses a scratch install.

**Owed to the close.** Every leg of the spec's Gates section. The spec declares no `New arm:` line. Two new refusal
sites carry no arm: the renderer's `--bullet-keys` refusal and the matrix's `RuntimeError` on a child that exits non-zero.
