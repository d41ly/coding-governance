# TOOL-dTrueNorth-9 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-9

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the
two names the pass mints (`--suggest`, one identifier each, both OK for `py.function`). Every
criterion below was observed by a probe of the changed code on `0893e7225`'s working tree: a scratch
script loading `tools/memory-tree/gen_build_index.py` by path, its AC3 fixture a git repository
under the user temp directory, short-named and removed after. A second probe evaluated the three
self-test arm expressions S4 adds, once each, against their wants. The probes stand in for the
`build-index selftest` leg; that leg, `lexicon naming predicates`, `memory hygiene`, `spec tokens (a
spec's own names resolve)`, and the `New arm:` line's RED-first observation against a three-value
`_expand_ids`, are owed to the close.

**Evidences:** TOOL-dTrueNorth-9
- AC1 — `tools/memory-tree/gen_build_index.py` — the probe's `_expand_ids("TOOL-x-1@rev-2 TOOL-x-2..3", alt)`
  with `alt` `TOOL` printed `tuple 2 (['TOOL-x-1', 'TOOL-x-2', 'TOOL-x-3'], [])`, a pair.
- AC2 — `read_idlist(["TOOL-x-1@rev-2", "-3"], alt)` — returned `['TOOL-x-1', 'TOOL-x-3']`, and
  `_read_backlog_verbs` on a header ending `· closes TOOL-x-4 · advances TOOL-x-5` returned
  `{'closes': ['TOOL-x-4'], 'advances': ['TOOL-x-5']}`; neither raised `ValueError`.
- AC3 — `read_bindings` — over the `%TEMP%` fixture repository whose one record reads
  `**Serves:** spec-audit TOOL-tPin-1@rev-2 TOOL-tPin-1@rev-3 TOOL-tPin-2..3`, the record was
  `bound` and its `pins` printed `{'TOOL-tPin-1': 3}`, no range id and the higher revision kept. Its
  `ids` printed `['TOOL-tPin-1', 'TOOL-tPin-1', 'TOOL-tPin-2', 'TOOL-tPin-3']`: the three distinct
  ids with the repeated one kept, the list `_expand_ids` returns at base, which §3 Edges hands to
  `TOOL-dTrueNorth-20` to fold and re-observe.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `gen_build_index.py` selftest, break `u9-three-value-expand`, the three-value `_expand_ids` the line names, 3 of its 3 arms red. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.
