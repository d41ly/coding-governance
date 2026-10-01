# TOOL-dMendedRecall-1 — acceptance ledger

**Serves:** journal TOOL-dMendedRecall-1

`make_repo` in the memory-recall selftest now copies every top-level `*.py` module of the resolved
memory-tree kit into each fixture, sorted and byte for byte, and the spec-H1 arm reads `spec_ids`
through `_SPEC_IDS_PROBE`, an isolated `-I` child whose one inserted path is the fixture's
memory-tree directory. A scratch reproduction stood in for the `memory-recall kit selftest` leg: it
read the probe constant and `make_repo` out of the edited file with `ast`, never importing it, built
the adopter layout with the real S1 code under `%TEMP%`, and ran the probe over three layouts plus a
control. The leg itself was not run in this pass, and neither were the other four section 7 names.

**Evidences:** TOOL-dMendedRecall-1
- AC1 — `No module named 'backlog'` — with one spec `# TOOL-aQuill-9 — x` seeded under
  `builds/bQuill/spec/` in the fixture's memory root and staged, the probe over the two-file `memory-tree/` exited 1 with
  `ModuleNotFoundError: No module named 'backlog'` as its last stderr line. Over the set S1 derived,
  ten files from `backlog.py` to `tree_lib.py`, it exited 0 and printed `["TOOL-aQuill-9"]`. The
  fixture held no `__pycache__` afterwards and was removed.
- AC2 — `grep -c -F 'glob("*.py")' tools/memory-recall/selftest.py` — printed 1 where HEAD prints
  0. The literal two-name `for f in` line and `import gen_build_index as G` each printed 0 where
  HEAD prints 1, and `grep -c '^SELFTEST_ARMS = 75$'` printed 1 at both, so no arm moved.
- AC3 — `PYTHONPATH` — set to this worktree's `tools/memory-tree` over the two-file layout, the
  `-I` probe still exited 1 with `No module named 'backlog'`. The liveness control ran the same
  probe without `-I` under the same `PYTHONPATH`: it exited 0 and printed `["TOOL-aQuill-9"]`, so
  the host path does leak in when isolation is absent, and `-I` is what closes it.
- AC4 — `memory-recall_kit_selftest.log` — NOT observed green here; the leg is the close's flagged
  bar, as the criterion's own permission clause says. What this pass read is the red it must clear.
  The persisted log of node d's 2026-09-30 23:52 bar carries two `FAIL` rows, the ADOPTER-layout arm
  and the spec-H1 arm with `No module named 'backlog'`, and the tally `79/80 checks passed`, while the
  plain run's spec-H1 arm in that same log reads `ok`. The green reading, with `75 == SELFTEST_ARMS`
  and no `FAIL` row, is owed at the close.

## What this ledger does not evidence

The spec's risk line asked for a grep of the selftest for whole-tree enumerations, because every
fixture now carries eight more files under `memory-tree/`. It found three. `tree()` feeds the
`__pycache__` filter in the empty-corpus arm and the before-and-after diff in the writes-nothing
arm, and neither moves when the fixture holds more files at build time. `git ls-files` appeared
only in the spec-H1 arm, and it now runs inside the probe. The corpus reader selects `.md` files
under the memory root, which `memory-tree/` is not under. None of the five section 7 legs ran in
this pass: `memory-recall kit selftest`, `recall floor`, `recall floor arms`,
`hook destinations self-test` and `install-prefix (shipped surface)` are all the close's. In their
place the diff was grepped for an added `tools/` literal and found none.
