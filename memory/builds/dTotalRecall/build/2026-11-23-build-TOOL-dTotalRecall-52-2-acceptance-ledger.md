# TOOL-dTotalRecall-52 — acceptance ledger, build pass 2

**Serves:** log TOOL-dTotalRecall-52
**Caused-by:** TOOL-dTotalRecall-52

No merge bar, no self-test suite and no gate leg ran in this pass. The builder re-applied pass 1's draft over
base `7d07249b5` (spec rev-7) and ran each probe below at the pass tip on node d, 2026-11-23; §7's gates are
owed to the close, and §7 declares no new arm.

**Evidences:** TOOL-dTotalRecall-52
- AC1 — `check` — the probe from `tools/lib/` printed the fields `path`, `section`, `check`, `verbatim` holding `section`, 78759 rows (DERIVED 2026-11-23, this probe), no malformed row, and the values `causes` and `kind-schema` alone.
- AC2 — `gained` — unit 62's §4 probe from `tools/memory-tree/` printed `True` and `compare_to_base` answered no findings, the merged home absent at `8b8b1374c4fc` (merge-base of HEAD and origin/main); `git grep -n absorbs -- tools/govkit/registry.toml` printed nothing.
- AC3 — `legacy-records` — the rev-7 grep printed nothing, worktree and index alike, and `git ls-files memory/project` lists no `legacy-records.txt`.
- AC4 — `--plant none` — the probe printed 10796 record rows and 56828 section rows, summing to the home's 67624 `causes` rows, and 11135 keys, the home's `kind-schema` rows (each DERIVED 2026-11-23, this probe and `memory/project/record-kinds-legacy.txt`); the fixture printed `record causes: record-kinds-legacy · 2 record row(s) (-), 0 section row(s)`. The suite's own assertion of that line is owed to the close (`memory hygiene`).
- AC5 — `tomllib` — the `tomllib` probe read one registration, `record-kinds-legacy`, and no `legacy-records`; the home's 67624 `causes` and 11135 `kind-schema` rows equal the old homes' row counts at the pass base `7d07249b5`, and the row sets equal the base homes' rows with `check` inserted third (DERIVED 2026-11-23, a set comparison).
- S1 — `--seed-legacy` — `record_kinds.py --seed-legacy` at the tip printed four TAB fields per row, `check` third: `kind-schema` rows then `causes` rows (DERIVED 2026-11-23). It is the seed, not the home: the folded home keeps the 139 widened comment-headed rows (unit 51's widen-7), which the seed does not print, and the seed prints records written after the base seed, which are graded, not legacy.
