# PLAY-dOrderedCharter-52 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-52

Each line is a probe this pass ran at rev-3 of the spec, from the worktree root with the pass applied. No leg, suite
or `--selftest` ran in the pass. The new suite group in `tools/memory-tree/merge-rows.test.sh` was not run as a
suite: its enumeration block was cut out by a scratch script and executed against the shipped driver and against a
scratch copy with row 9 removed, and its three table cases were replayed by hand through the driver and through
`git merge-file`. Those probes stand in for the `row-keyed merge driver replay` and `instruction edits selftest` legs
until the close runs them and observes the new arm red on its staged row deletion. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-52
- AC1 — a `python` probe loading `tools/memory-tree/merge-rows.py` through `importlib.util.spec_from_file_location` classified every base, ours and theirs over an absent side and four texts, one in CRLF, with `derive_side_state`, and printed `states reached 14 rows 14`, `state with no row []`, `row no state reaches []`; it also compared `resolve_table` with the pre-unit rule over the same inputs and printed `result moved vs the pre-52 rule []`. The suite group's own block printed nothing and exited 0; over the scratch copy with row 9 removed it printed `FAIL table envelope: the state ('present', 'unchanged', 'deleted') has no row` and exited 1.
- AC2 — `python tools/playbook/instructions_edit.py fixture --plant merge-theirs-delete`, `--plant merge-both-delete` and `--plant merge-theirs-add` each printed `ok · <plant> merges clean ...` and `fixture · green · 0 expectation(s) failed`; the check asserts git's exit 0, the written file equal to ours' edited entry with the deleted tag absent or the added tag once, and the driver's `merge-rows: tables` line in git's words.
- AC3 — a scratch copy of `tools/` with row 9 deleted from `TABLE_ENVELOPE`, its `merge-theirs-delete` plant run: git printed `CONFLICT (content): Merge conflict in tools/alpha/instructions.toml`, the driver printed `merge-rows: CONFLICT — each side changed unit.unit.base apart`, the file held the whole-file body opening `<<<<<<< ours` and closing `>>>>>>> theirs (table conflict: unit.unit.base)`, and the plant printed `fixture · FAILED · 1 expectation(s) failed`.
