# Acceptance ledger — TOOL-aClearedLedger-9

**Serves:** journal TOOL-aClearedLedger-9

Built against spec rev-1 in this record's own commit, from base ef4498647.
Each line is a probe the builder made in the pass: the unit's own plant, `python tools/memory-tree/build_records.py --fixture --plant red-fix-join`, run once over its scratch repository, and the join run over this tree. No suite, gate leg or bar ran in the pass.
Owed to the close: the legs of the spec's Gates section, and the RED-first observation of its `New arm:` line, staged as that line says. The usage anchor of `help/red-fix-lane.md` for the join verb needed no new fingerprint: `python tools/govkit/docs_leg.py --fingerprints` printed `90d1c185` for it before and after the change, since the verb's flags did not move.

**Evidences:** TOOL-aClearedLedger-9
- AC1 — `path-less at HEAD` — the plant printed that case and `staged, path-less at HEAD`, each with exit 0 and the line `build-records: red-fix join · path-less · 23461e5f · the fixture leg · touches no path, so it owes no record`, the sha the empty commit's. <!-- PINNED 2026-11-13 -->
- AC2 — `path-less below HEAD` — the plant printed the case with exit 0 and the summary `1 fix commit(s) · 1 record(s) · 0 owed · 2 path-less`, the empty commit and the trailer merge both below HEAD. (DERIVED by the join from the fixture's history at run time) <!-- PINNED 2026-11-13 -->
- AC3 — `owes no red-fix record` — the plant printed `refusal · a commit that touches no path · exit 1 · 1 record(s)`, and the case passes only where the door's text holds that phrase; the plant's PASS line followed. <!-- PINNED 2026-11-13 -->
- AC4 — `· J2 ·` — the plant printed `J2, a record naming a path-less commit` with exit 1 and a line holding that token, the fixture record's path and the empty commit's full sha. <!-- PINNED 2026-11-13 -->
- AC5 — `grep -c 'path-less' tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md help/red-fix-lane.md` — printed 5 for the template, 5 for `memory/HYGIENE.md` and 7 for the help page; the two documents' diffs were compared line for line and are the same. <!-- PINNED 2026-11-13 -->
- AC6 — `python tools/memory-tree/build_records.py join red-fix` — exited 0 in this repository, its last line `build-records: red-fix join · 1 fix commit(s) · 1 record(s) · 0 owed · 0 path-less`. (DERIVED from this tree's history at ef4498647)
