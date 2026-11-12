# PLAY-dOrderedCharter-71 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-71

Each line is a probe this pass ran at rev-2 of the spec, from the worktree root with the pass applied. No leg, suite
or `--selftest` ran in the pass: `govkit selfcheck`, `govkit selftest` and `owed_rows.py --selftest` are the main
loop's at the close, with the `New arm:` line's RED-first observation. The population probes import
`tools/govkit/govkit.py` and re-derive the ban's population in process; they stand in for the `govkit selfcheck` leg
until the close runs it. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-71
- AC1 — owed as the leg — an in-process probe re-deriving the ban's population over this tree printed `old 392 new 301`, dropped `tools/playbook/positional-refs.txt` and `tools/playbook/positional-producers.txt` as `project-owned` and `tools/agent-cap-restatement-waivers.txt` as `generated`, and found no adopter name in the 301 that stay; `govkit selfcheck` itself is the main loop's.
- AC2 — owed as the leg — the same probe with `positional-refs.txt` deleted from the playbook-render descriptor's `project-owned` include, in memory and with a liveness assert that the row was found, printed `positional-refs in population: True`; the scratch-worktree `selfcheck` run is the main loop's.
- AC3 — nothing, then `3` — `grep -n "surely as an engine" tools/govkit/govkit.py` printed nothing; `grep -c 'row\["role"\] in EPOCH_ROLES' tools/govkit/govkit.py` printed `3`.
- AC4 — `lexicon OK`, `offenders=1209` — `lexicon.py --check` printed `P1 verb graded=7877 offenders=1209` and `lexicon OK` with `VERB_OFFENDER_PIN="1209"` unmoved (1212 before the renames); `--offenders` printed no row for `fold`, `split_known` or `warn_grown_file` in either renamed file, nor for the three new names.
- AC5 — exit 0 each — `instructions_edit.py fixture --plant merge-unterminated`, `--plant merge-moved` and `--plant merge-written` each exited 0, the last printing `instructions-edit: fixture · green · 0 expectation(s) failed`.
- AC6 — `3`, arm owed — `grep -c "dOC-71 S3" tools/govkit/selftest.py` printed `3`; the arm's RED with S1 reverted and GREEN with it are the main loop's, under the spec's `New arm:` line.
- AC7 — owed — `python -m py_compile` over `tools/run-gates/owed_rows.py` exited 0 and `grep` shows each new name at its definition and its one `cases` row with no old spelling left; `owed_rows.py --selftest` is the main loop's.
