# PLAY-dOrderedCharter-50 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-50

Each line is a probe this pass ran with the pass applied, at rev-5 of the spec: `owed_rows.py --base` from
`tools/run-gates/`, `owed_rows.py --help`, `git grep` over the named files, a `python -c` over the canary's
`keyset_probe` copy of `KNOWN`, and a scratch-script probe that imports `owed_rows`, builds its fixture
repository with `build_fixture_repo` under `%TEMP%` and calls `run_probe` once per planted case. The canary
leg, `govkit selfcheck`, `govkit selftest`, the other gates the spec's section 7 names, `owed_rows.py
--selftest` itself, the merge bar and the `New arm:` line's RED-first observation are the main loop's at the
close: a role agent runs none of them, and the hook refused `--selftest` in this pass. This record cites no
code line.

**Evidences:** PLAY-dOrderedCharter-50
- AC1 — `git grep -n '"enforces"' -- tools/run-gates/run-gates.test.sh` prints both `KNOWN` lines, the arm's and `keyset_probe`'s, each ending `"pack", "enforces"}`; the `keyset_probe` predicate run in a `python -c` over the control pair's two rows exits 0 on `"enforces":["r"]` and 1 on `"enforce":["r"]`. OWED to the main loop: the pair inside the canary leg, and its RED-first observation with the key removed from one copy
- AC2 — `python owed_rows.py --base ce13efbe` from `tools/run-gates/` exits 0 printing four `deferred —` lines, `policy check`, `policy fixtures`, `step-rows-frozen` and `tags positional selftest`, each a leg added since the base with no `ceiling-evidence.txt` row, and `owed_rows: 0 rows owed since ce13efbe · 4 deferred · 26 size breach(es) the switch's warn admits`. Before S5's rows the same run exited 1 naming `tools/govkit/subject-pins.tsv <- tags positional selftest` and the descriptor-or-exempt row for it. `--base HEAD` exits 0, `0 deferred`
- AC3 — `python owed_rows.py --selftest` is refused to a role agent, so the scratch probe stands in: the probe's cases, each `rc` and line as `run_probe` returned them: a tree owing nothing rc=0 `owed_rows: 0 rows owed`; a leg added with no pin and no descriptor rc=1 naming the pin file and the descriptor-or-exempt row; a leg added that no dossier claims rc=1 naming `a dossier's gate-legs claim under memory/map/features/`; a leg removed whose pin and budget rows stay rc=1 naming both; a key outside `KNOWN` rc=1 naming `` `enforce` in each KNOWN copy ``; a deleted script and a renamed one rc=1 naming `unarmed-branches.txt <- drop the row naming kits/fx/gone.sh`; a file of 101 bytes under a refused cap of 100 rc=1 naming it, and 100 bytes after CR-stripping rc=0; disagreeing `KNOWN` copies, an absent `baseline.toml` and a base naming no commit rc=2. OWED to the main loop: `owed_rows.py --selftest`, the canary's arm `1a-owed`, and its RED-first observation by planting a leg with no pin row
- AC4 — `git grep -n "tags positional selftest" -- tools/govkit/subject-pins.tsv tools/playbook/kit.toml` prints the pin row `tags positional selftest<TAB>kit<TAB>selftests` and the descriptor's `name = "tags positional selftest"`. OWED to the main loop: `govkit selfcheck`, which grades the pin and the descriptor's agreement with the manifest
- AC5 — `python tools/run-gates/owed_rows.py --help` prints the rule: run `python tools/run-gates/owed_rows.py --base HEAD` as the LAST probe of the pass, before its commit, and write every owed row in that commit, naming `python tools/govkit/govkit.py selfcheck --write` for a pin row and `python tools/codebase-map/gen_map.py --write` after a dossier claim
- AC6 — OWED to the main loop: the `--base` replay at the parent of each handed-off unit's pass commit, after the last of them lands
