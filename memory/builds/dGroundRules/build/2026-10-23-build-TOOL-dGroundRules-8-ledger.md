# TOOL-dGroundRules-8 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-8

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit, with this unit's edit in the worktree: the planted cases through the kit's own fixture CLI,
run for the one case `reader-coverage`, its eleven repositories under the system temp directory,
short-named and removed by the case, and the real-tree criteria through `python -c` probes of
`check_reader_coverage`. The New arm's RED-first observation is the close's.

**Evidences:** TOOL-dGroundRules-8
- AC1 — `python check_policy.py --fixture reader-coverage` — run as `python tools/policy/check_policy.py --fixture reader-coverage`, exit 0, 11 assertions, 0 wrong: "case landed-no-reader: red · check_reader_coverage · graded 1 · reader coverage: fixture.planted (owner bPlanted, landed at 268b6106) has no reader".
- AC2 — `python check_policy.py --fixture reader-coverage` — "case unlanded: green · ... graded 0 · reader coverage: graded 0 of 1 catalogue key(s); landed owners: none · reader coverage: graded 0, so this arm checked nothing at 4a3afdd2" and "case no-build: green · ... graded 0", the same two lines; neither grades the key.
- AC3 — `python check_policy.py --fixture reader-coverage` — "case reader-python: green · ... graded 1", "case reader-cli: green · ... graded 1" and "case reader-js: green · ... graded 1", each "landed owners: bPlanted". With `READER_SHAPES` cut to its second row in a `python -c` probe, `reader-python` and `reader-js` printed WRONG; cut to its first, `reader-cli`, `pattern-read` and `pattern-only-sibling` did.
- AC4 — `python check_policy.py --fixture reader-coverage` — "case not-a-reader: red · ... graded 1 · reader coverage: fixture.planted (owner bPlanted, landed at 30c5f8ad) has no reader". A probe with the test-file pattern matching nothing and the own-module path derived from the wrong directory printed "case not-a-reader: green · ... WRONG".
- AC5 — `python check_policy.py --fixture reader-coverage` — "case history-not-tree: red · ... fixture.planted (owner bPlanted, landed at 1c0d3e0f) has no reader" and "case tree-not-history: green · ... graded 0 · ... landed owners: none". A probe grading every catalogue owner as landed printed WRONG for `tree-not-history`, `unlanded` and `no-build`.
- AC6 — `python check_policy.py --fixture reader-coverage` — "case pattern-read: green · ... graded 1" and "case pattern-only-sibling: red · ... graded 2 · reader coverage: fixture.* (owner bPlanted, landed at ed7a94d4) has no reader", no finding for `fixture.exact`. A probe dropping the sibling exclusion printed "case pattern-only-sibling: green · ... WRONG".
- AC7 — `graded 0` — `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; print(c.check_reader_coverage('.'))"` from the repository root printed "reader coverage: graded 0 of 267 catalogue key(s); landed owners: none", "reader coverage: graded 0, so this arm checked nothing at ed497191" and `(0, [])`. The arm as the leg runs it, `run_arm(arm_reader_coverage, ".", KIT)` printed the same two lines and "policy-check: arm_reader_coverage · 0 finding(s) · 0 of 267 catalogue key(s) graded for a reader".
- AC8 — `policy-file.on-invalid` — the same probe with `landed={'dGroundRules'}` printed "graded 5 of 267 catalogue key(s); landed owners: dGroundRules" and four findings, `runtime.agents-in-flight`, `budgets.*`, `budgets.enforce` and `budgets.pinned`, and none for `policy-file.on-invalid`, read by `parse_key("policy-file.on-invalid")` at `tools/policy/policy.py` lines 521 and 543. The four are units 9 and 10's readers, which this branch has not built yet.

Owed at the close, observed by no command in this pass:

- The New arm line of §7, `tools/policy/check_policy.py`'s `--fixture reader-coverage`: RED on a staged break of `check_reader_coverage` and GREEN restored.
- AC8 for all five keys, once units 9 and 10 are built: the probe with `landed={'dGroundRules'}` must report no finding.
- The §7 legs over the built tree, `govkit selfcheck`, `lexicon naming predicates`, `encoding posture (text IO names its encoding)` and `kit epoch (shipped bytes move, the version moves)`, and the `policy check` and `policy fixtures` legs. `python tools/lexicon/lexicon.py --check`, the naming lexicon a builder may run, printed "lexicon OK". `adopter-fresh-target` gains a line for `arm_reader_coverage`; in a fresh target with no `main` the landed revision refuses, which the README's "Each arm in an adopter" row names, until TOOL-dGroundRules-21 announces the arm.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: --fixture reader-coverage, `graded = list(rows)` -> unlanded, no-build, tree-not-history `check_reader_coverage · WRONG: graded 1` (3 of 11), reds AC2 AC5. GREEN `79 assertion(s) executed · 0 wrong`.
