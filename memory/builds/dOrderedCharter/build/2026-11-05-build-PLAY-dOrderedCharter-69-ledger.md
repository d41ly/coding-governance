# PLAY-dOrderedCharter-69 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-69

Each line is a probe this pass ran at rev-1 of the spec, from the worktree root with the pass applied. The
plants ran through their own CLIs by hand and never through `adopt-playbook.sh` or any `--selftest`, which a
role does not run. Each arm's RED-first observation, the legs section 7 names and the merge bar are the main
loop's at the close. Before the code changed, a hand probe over a disposable main-plus-linked-worktree repository
under `%TEMP%` showed the leak: under the linked worktree's exported `GIT_DIR`, the `statements` plant exited 1
and left `core.bare` reading `true`, the `two-versions` plant printed `DIFFER` and replaced the outer sentinel
`index.db` with a SQLite file, and the edge grammar's `resolve-tag` plant exited 2 opening the outer sentinel.
This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-69
- AC1 — `fixture · green` — `python tools/playbook/instruction_units.py fixture --plant git-env` exited 0 printing its three `ok` lines (the child `statements` fixture exits 0, core.bare reads false, the outer index is unchanged) and `instruction-units: fixture · green · 0 expectation(s) failed`.
- AC2 — one line — `grep -n "set_env_aside(GIT_ENV_LEAKS)" tools/playbook/instruction_units.py` printed one line, inside `run_fixture`.
- AC3 — `tags: plant git-env · both children green, core.bare false, the outer index unchanged` — `python tools/playbook/gov_tag.py --fixture --plant git-env` exited 0 printing exactly that line.
- AC4 — one line per file — the grep over `tools/playbook/edge_grammar.py` and `tools/playbook/gov_tag.py` printed one line each, inside each `run_fixture`; AC3's plant ran `edge_grammar.py --fixture --plant resolve-tag` as its second child, green.
