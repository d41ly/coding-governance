# Acceptance ledger — TOOL-aNimbleMend-9

**Serves:** journal TOOL-aNimbleMend-9

Built against spec rev-2 in one pass commit. Each line is a probe of the changed code the builder made in the pass: the two plants of `build_records.py` run directly, the criterion's own commands, and the suite's nine new assertions run alone, outside the suite, over a scratch repository. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section, the suite's raised assertion floor, which is a count made by reading, and the RED-first observation of the spec's two new arms.

**Evidences:** TOOL-aNimbleMend-9
- AC1 — `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` — printed a `typed-kinds · red-fix ·` line ending `· bound` and a PASS line counting 5 typed kinds bound, exit 0; the hyphen in the kind reads through the name grammar. (PINNED, 2026-11-12)
- AC2 — `Commit` — the plant's `door` case passed the 8-character rev alone and the written record held the fixture commit's full 40-hex sha, its `Files` the commit's two paths in sorted order. (PINNED, 2026-11-12)
- AC3 — `--leg` — the three `refusal` cases, a commit with no trailer, a leg no trailer names and a rev that names no commit, each printed exit 1 and an unchanged count of 1 record. (PINNED, 2026-11-12)
- AC4 — `1 fix commit(s) · 1 record(s) · 0 owed` — the plant's clean case printed exit 0 and that summary over one fix commit and its record. (PINNED, 2026-11-12)
- AC5 — `red-fix-join` — the plant staged J4, J3, J2, J6 and J5 by editing or doubling the record and J1 by committing once more on an unrecorded fix; each case printed exit 1 and its row with the record or the sha it names, and the plant's PASS line counted 14 cases. (PINNED, 2026-11-12)
- AC6 — `join red-fix --staged` — with an unrecorded fix at HEAD the full form printed the `owed` line and exited 0, the staged form exited 1 naming the sha under J1, and after `git add` of the record the staged form exited 0.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh --only 31` — printed one `check 31:` line, `red-fix join · 0 fix commit(s) · 0 record(s) · 0 owed`, then the liveness line naming check 31, exit 0. Over a scratch repository the check failed on an unrecorded fix below HEAD and passed once its record was staged; that arm's RED-first observation inside the suite is the main loop's, at the close. (PINNED, 2026-11-12)
- AC8 — `red-fix` — the criterion's grep printed 5 for each file and its diff showed no line naming the kind on one side only. (PINNED, 2026-11-12)
