# TOOL-aTrimmedHook-1 — acceptance ledger

**Serves:** journal TOOL-aTrimmedHook-1

No merge bar and no self-test suite ran in this pass. AC1 to AC6 were observed by running
`test_staged_render` alone through a slice that imports the module and passes a printing `arm`: 12
arms held in 31 s. Each was observed RED first on a scratch copy of the module: with the id
comparison replaced by `if False:`, the AC2 arm failed; with `ledger` dropped from the structural
set, the AC6 parity arm failed. AC7 ran the staged hygiene leg against a tree with one `RUN.md` line
staged. The close owes the whole `build-index selftest` leg, where `test_staged_render` runs from
`cmd_selftest`.

**Evidences:** TOOL-aTrimmedHook-1
- AC1 — `gen_build_index.py --selftest` — the arm staging a plain line in `memory/notes.md` saw
  `check_staged_render` return False, and the `--check --staged` subprocess printed
  `render SKIPPED under --staged` and exited 0.
- AC2 — `gen_build_index.py --selftest` — the arm staging `now ARCH-tOne-7` saw a render owed; with
  the id comparison disabled it printed FAIL. A `missing:` id staged the same way skipped.
- AC3 — `gen_build_index.py --selftest` — an added `memory/other.md` and a removed
  `memory/notes.md` each saw a render owed.
- AC4 — `gen_build_index.py --selftest` — a README edit, a spec edit and a conf edit each saw a
  render owed, and `check_index_input` answered True for a kit file and False for a sibling-named one.
- AC5 — `gen_build_index.py --selftest` — `rosters()` over the fixture equalled the per-file union
  of `extract_roster_ids`.
- AC6 — `gen_build_index.py --selftest` — every artifact `plan()` returned on the fixture satisfied
  `check_index_input`; with `ledger` dropped from the set the arm printed FAIL.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh --staged` — with one no-id `RUN.md` line
  staged it printed `check 9: render SKIPPED under --staged` in 67 s; with a line staged instead
  that cites a new id of that build (its own slug, sequence 99) it printed no skip, rendered, and
  redded check 9 on the README `ids:` drift that line causes, which is the drift a path list would
  have skipped. This ledger's first draft cited that id verbatim and this unit's own commit redded
  check 9 on it, which is the same class observed in the tree.
