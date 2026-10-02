# TOOL-aRepatriatedFork-45 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-45

Written by the unit pass on node a, 2026-09-30. No merge bar, no self-test runner and no whole suite
ran. The spec's rev-2 committed before any code. Each criterion ran its direct check on the real
tree. The self-test ran as two SLICES in temp scripts inside the kit dir, removed afterwards: its
prologue with sections 1 to 3b and the two sentinel blocks of section 5, then its prologue with
sections 6, 6b and 7, the callers of the changed `mkrepo`.

**Evidences:** TOOL-aRepatriatedFork-45
- AC1 — `bash tools/check-dead-paths.sh --needles` — exits 0 printing 32 needles, among them `incms-2cff5855.receipt.json`, `make_incms_receipt.py` and `parallel-coding-governance.template.md`, and not `BACKLOG.md`. The figure matches the one §4 pinned at `6830f257`
- AC2 — `tools/push-main.sh` — with `# see incms-2cff5855.receipt.json` appended to the working copy, the built gate exits 1 naming `tools/push-main.sh:219`, and the gate as it stands at `6830f257` exits 0 with `24 derived needle(s)`. The plant was then discarded and the file restored byte-for-byte
- AC3 — `bash tools/check-dead-paths.sh` — exits 0, `32 derived needle(s), 14 declared waiver(s), no undeclared carrier`, and `tools/dead-path-waivers.txt` is unchanged
- AC4 — `tools/check-dead-paths.sh` — a scratch copy beside it, with the rename read's awk condition made false, exits 1 printing `the frozen rename sentinel 'parallel-coding-governance.template.md' is not in the derived rename set`
- AC5 — `tools/check-dead-paths.sh` — its "what it does not catch" paragraph names the `memory/` rename exclusion and git's rename-similarity threshold
- AC6 — `tools/check-dead-paths.test.sh` — `git grep -n 'never .git mv.'` over it exits 1 with no output, and `FLOOR_ASSERTIONS` moves from 19 to 22. The first slice passed 12 arms and the second 5. Red first: with the gate at `6830f257` swapped in, the renamed-away carrier arm and the rename sentinel arm fail. With the `memory/` exclusion removed from the built gate, the `BACKLOG.md` arm fails. The whole suite's executed count is the main loop's to record

Other direct checks: `check-install-prefix.sh`, `check-kit-versions.sh`, `govkit.py selfcheck`,
`lexicon.py`, `encoding_posture.py`, `check-arms.py --check` and `check-spec-tokens.py` exit 0. No kit
version moves: the gate and its self-test are exempt in the govkit registry and ship nowhere.
