# TOOL-dTotalRecall-116 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-116
**Caused-by:** TOOL-dTotalRecall-116

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-2 over base
`270795c1b71a986b04a5cb60751138f2f441e9db`, 2026-11-25 local, in one commit. The plants ran over the working tree's
`record_find.py`, the fixture probes over its copy in their own repositories. §7's legs and the `New arm:` RED-first
observation of `tools/memory-tree/check-memory-hygiene.test.sh`'s three blob plants are owed to the close.

`check_blob_path` over a record name holding brackets answered no for a neighbour's blob and yes for its own, and
refused naming git for an object git lacks (DERIVED 2026-11-25, the pass's probe). With `check_blob_path` cut to a
constant yes in a scratch copy, `blob-foreign-record` and `blob-foreign-text` each exited 0 (DERIVED 2026-11-25, that copy).

**Evidences:** TOOL-dTotalRecall-116
- AC1 — `python record_find.py --fixture --plant blob-unknown-key` — printed `refused show: key NO-SUCH-KEY names no record of the served view` and `fixture blob-unknown-key · exit 2` (DERIVED 2026-11-25, that run).
- AC2 — `--plant blob-foreign-text` — and `--plant blob-foreign-record` each printed `is no version of` and `exit 2` (DERIVED 2026-11-25, those runs).
- AC3 — `--plant unheld-blob` — printed `the second`, never `the third`, and `exit 0`, and the probe read a `path` ending `deviation-1.md` for that address (DERIVED 2026-11-25, those runs).
- AC4 — `read_section` — raised `FindError` for `NO-SUCH-KEY` and for the builder-return stem at the blob of `README.md`, and answered the stem at its own file's blob with its text, lines 1 to 46 of its own path (DERIVED 2026-11-25, the probe over this worktree, 261 s cold and then 78 s and 57 s).
- AC5 — `grep -c 'run_find_plant blob-' tools/memory-tree/check-memory-hygiene.test.sh` — printed 3, `FLOOR_ASSERTIONS` went from 830 to 836 by the six added assertions, and the `shell-role` row holds 3750, the measured count, widened by `2026-11-25-build-TOOL-dTotalRecall-116-widen-29` (DERIVED 2026-11-25). The floor is counted by reading; the suite's own run is owed to the close.
- AC6 — `DEC-tFix-1` — at the blob of `memory/DECISIONS.md` read that path at line 5, at the archived file's own blob read the archived path at line 3, and once the archive was edited and committed its former blob read `memory/DECISIONS.md` with the former text (DERIVED 2026-11-25, the fixture probe).
