# TOOL-dTotalRecall-45 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-45

No merge bar, no self-test suite and no gate leg ran in this pass. Every probe ran on node d, 2026-11-22,
from base `f1ddf2410`. The flipped clone is a scratch clone of that base under `%TEMP%` with its remote
removed, on a `main` that commits the pass's four edited modules, then the last row of
`tools/memory-tree/id_grammar.py#_FLIPS` as `run_flip_probe` commits it (`slug-date = "in-slug"` under
`[builds]` in `.governance/policy.toml`, and the build README of `d2026-10-26ClosedLoop` recording
`words=1-3 style=humorous date=in-slug`), then each criterion's own fixture commit. Each red was observed by
running the same probe against the base revision of the module, read with `git show f1ddf2410:<path>`.
The gates of §7 and the `New arm:` RED-first observation are OWED to the close, after the last unit is
terminal.

**Evidences:** TOOL-dTotalRecall-45
- AC1 — `derive_names` — a `python -c` probe in the flipped clone importing its `branch_reconcile.py` answered `['TOOL-d2026-10-26ClosedLoop-3', 'd2026-10-26ClosedLoop']` for `derive_names("TOOL-d2026-10-26ClosedLoop-3 fix")`; the base module answered `d2026` in the same clone, the red. The same probe gave an undeclared family's id (`ZZQ-aFoo-2`) its slug, which `FAMILY_CLASS` admits, and with `_SLUG_GRAMMAR` set to None it took the legacy text between the first and the last hyphen.
- AC2 — `render_spec_skeleton` — `python tools/memory-tree/gen_build_index.py --new-spec TOOL-d2026-10-26ClosedLoop-3 --tier 2` in the flipped clone exited 0 and wrote a header reading `node d`; a `python -c` probe calling `render_spec_skeleton` with `spec_id="TOOL-dFoo-3"` and `slug="xFoo"` over the tree's `memory/TEMPLATE-SPEC.md` got a header reading `node x`, so the node is not read from `spec_id`. The `build-index selftest` leg, whose seven skeleton calls now pass `slug="aFix"` (TOOL-dTotalRecall-45 S2), is OWED to the close.
- AC3 — `scan_records` — a `python -c` probe running the clone's `row_grammar.py#scan_records` over the clone with the committed decision row `TOOL-d2026-10-26ClosedLoop-3` keyed that row's slug `d2026-10-26ClosedLoop`; the base module keyed it `d2026`, the red, and no other row's slug differed between the two (DERIVED 2026-11-22, the probe), none keyed `""`. The new arm in the `row-grammar selftest` was replayed by hand as a copy-install fixture under `%TEMP%`: it printed `['d2026-10-26ClosedLoop']` with the pass's `row_grammar.py`, and `['d2026']` with the base one in its place, so it can red; its RED-first observation inside the suite is OWED to the close.
- AC4 — `git grep -nE "\.split\(['\"]-['\"]\)" -- tools` — at the worktree before the pass commit its output held none of the four sites S4 records (the commit's `Decided:` trailer names each by file and line text); each remaining hit outside a selftest plant indexes `[0]` or is not an id reader, and its enclosing `def` (`drift_report.py#build_live_backlog_rows`, `backlog.py#render_family_view`, `gen_build_index.py#cmd_asks`, the date read of `row_grammar.py`, `gov_tag.py`, `measure_legs.py`) is none of unit 38's ten. `id_grammar.py --readers` listed no hit in the four edited files but the date read it listed at base.
- AC5 — `derive_run_kind` — a `python -c` probe in the flipped clone loading the readers through `load_tree_lib_or_refuse` and `load_run_readers`, as `derive_landed_builds` does, called it for `d2026-10-26ClosedLoop` at a clone commit whose `BACKLOG.md` holds the open ask `TOOL-d2026-10-26ClosedLoop-9` and whose README's `roster:units` pair names `TOOL-d2026-10-26ClosedLoop-1`, which no spec defines: it answered `spec`; the base module answered `build`, the red. The `policy fixtures` leg, whose `reader-coverage-carried` cases run this reader, is OWED to the close.
