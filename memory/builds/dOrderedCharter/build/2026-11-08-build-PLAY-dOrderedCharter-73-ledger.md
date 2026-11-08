# PLAY-dOrderedCharter-73 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-73

Each line is a probe this pass ran at rev-2 of the spec, from the worktree root with the pass applied. No leg, suite
or `--selftest` ran in the pass, and the role hook refused `core.py fixture` as the `core selftest` leg. The pass
applied the unit 73 builder's work-in-progress patch less its spec, matrix and `requires` hunks, which rev-2 moved
out of scope. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-73
- AC1 — owed as the leg, with a probe — a scan of every `subprocess.run` call in the six Python files S1 names printed no call carrying `text=True` without `encoding=`; `encoding_posture.py` over the tree is the main loop's. In-process calls of `common_dir.py#read_git_stdout`, `id_grammar.py#git` and `core.py#run_fixture_git` each read this branch's HEAD, and `positional.py#run_pin` over a scratch repository pinned a citation of a committed file to its blob and refused a citation of an absent file as no blob at HEAD.
- AC2 — exit 0, then the leg owed — `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` exited 0 printing `build-records: PASS typed-kinds — 4 typed kinds bound, --print-bindings printed no A row`. The role hook refused `python tools/playbook/core.py fixture` as the `core selftest` leg; an in-process call of `core.py#run_fixture` over all ten plants returned 0 with `core: fixture · green · 0 expectation(s) failed`, its door line `rc=0` through `core.py#run_door`. The leg itself is the main loop's.
- AC3 — `1`, the scan owed — `grep -c 'mapfile -t rows' tools/unattended/unattended.sh` printed `1`; `bash -n` passed, and a probe of the drain over a listing with an empty line kept every row, and over an empty listing gave one empty row, which the `""` arm skips. `sh_hygiene.py` over the registry is the main loop's.
- AC4 — owed as the leg, with a probe — a grep for `printf "%s" "$(derive_fx_unit`, `$(dirname -- "$READER_REL")/`, `$(dirname -- "$KIT_REL")/` and the `sed` indent over the four files printed nothing. A probe of the `printf '      %s\n'` expansion matched the `sed` indent byte for byte over a four-line output with an empty line. The spawn-idiom scan is the main loop's.
- AC5 — nothing, exit 0 — the spec's `cmp` command printed nothing and exited 0, and so did the same over `derive_fx_unit b` with the default text.
- AC6 — `2`, the ban owed — `grep -c DERIVED_UNIT_KEYS tools/playbook/instruction_units.py` printed `2`; `check_unit_row`'s key loop over a row carrying `status`, `origin` and `bogus` gave the derived remedy to the first two and `delete it` to the third. `check-remote-literals.sh` is the main loop's.
- AC9 — `0`, the selftest owed — `grep -c 'budgets.py resolve' tools/run-gates/owed_rows.py` printed `0`; `py_compile` passed. `owed_rows.py --selftest` is a selftest flag, the main loop's.
- AC10 — `3` — `grep -cE 'arm\(s\) failed"; exit 1' tools/playbook/adopt-playbook.sh` printed `3`. The three pinned rows in `memory/project/unarmed-branches.txt` are the main loop's.
- Naming — `lexicon.py --suggest derive_fx_unterminated --as sh.function` printed `OK`; `--as py.constant` for `DERIVED_UNIT_KEYS` answered that no such cell is declared, as the spec's inventory states.
