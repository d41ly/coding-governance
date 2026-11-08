# PLAY-dOrderedCharter-74 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-74

Each line is a probe this pass ran at rev-1 of the spec, from the worktree root with the pass applied. No leg, suite
or `--selftest` ran in the pass. The ban's eleven general patterns were copied out of
`tools/check-remote-literals.sh` into the run's scratch and run over the one file this unit edits there; that probe
stands in for the `remote literals (kit code names no remote)` leg until the close runs it. The ceiling was checked by
re-applying the headroom rule of `tools/run-gates/derive-ceilings.py#cmd_check` to the row in Python; that stands in
for the `leg ceilings clear their evidenced maximum` leg. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-74
- AC1 — `grep -c 'DERIVED_UNIT_KEYS = ("origin", "status")' tools/playbook/instruction_units.py` printed `1`; the scratch copy of the ban's patterns printed one hit in that file at `fc2572d5d` and none in the worktree; an import of `tools/playbook/instruction_units.py` reads `('origin', 'status')` and both names test as members. `bash tools/check-remote-literals.sh` is the leg's argv, owed to the main loop.
- AC2 — `grep -A8 '"layer dependencies' tools/gate-legs.json` shows `"ceiling": 124`; a Python read of the row against the 3.6s evidence and the 120 / 1.0 margin computed a bound of 123.6 and a pass. `python tools/run-gates/derive-ceilings.py --check` is the leg's argv, owed to the main loop.
- AC3 — `git diff fc2572d5d -- memory/guides/SESSION-KICKOFF.md` changes only the `last-audit:` line, re-stamped at the branch HEAD the pass was built on, in the same commit as `tools/gate-legs.json`; no manifest claim reads a leg ceiling. `bash skills/session-kickoff/manifest-check.sh` is the leg's argv, owed to the main loop.
