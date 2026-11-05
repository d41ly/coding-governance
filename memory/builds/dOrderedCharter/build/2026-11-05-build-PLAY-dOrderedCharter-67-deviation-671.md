# PLAY-dOrderedCharter-67 deviation 671 — the scanner's `shipped` row reads `project-owned`, as built

**Serves:** deviation PLAY-dOrderedCharter-67

- **Departs from:** `PLAY-dOrderedCharter-67@rev-1` [Acceptance criteria]
- **Hand-off:** spec-to-code
- **Before:** AC7 says that when `python tools/govkit/govkit.py shipped` runs, no row names the new scanner.
- **After:** `shipped` prints one row for it, `run-gates	project-owned	tools/run-gates/py_reads.py`, and no `engine` row names it.
- **Cause:** design defect
- **Reason:** the verb prints every descriptor survivor with its role, `project-owned` included, so the row S4 requires is the row AC7's sentence forbids; no build satisfies both as written. AC7's Red-when is the file shipping, and it does not: `project-owned` is outside the landable roles, and `owed_rows.py` reads the same way one line above it.
- **Evidence:** `python tools/govkit/govkit.py shipped` prints `run-gates	project-owned	tools/run-gates/owed_rows.py` and the scanner's row in the same role; `tools/govkit/govkit.py#cmd_shipped` filters a role only under `--epoch`.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-67
