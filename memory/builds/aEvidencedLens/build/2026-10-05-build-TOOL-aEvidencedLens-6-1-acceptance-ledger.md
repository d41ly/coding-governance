# TOOL-aEvidencedLens-6 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-6

The review returns a per-lens yield over defect clusters, unique defects counted. The pass commit
`eb3980f2e` and its spec amendment `62a1cf2a2` record no direct-check figures. The criteria are read
from the main loop's VERIFYING run of the tier2-review self-test in a frozen clone at `0c8dd1761`,
which printed `---- 239 passed, 1 failed ----`, the one FAIL being the rubric arm, an extractor defect
fixed in `5a1643c8d`, whose re-run printed `---- 240 passed, 0 failed ----`; every `lens yield:` arm
printed `ok` in it. AC7 is a direct check run for this record: `ledger-cmp.js`, the scratch `runReview`
driver described in this build's `TOOL-aEvidencedLens-1` ledger, over `git show eb3980f2e~1:` of
`tools/workflows/tier2-review.js`, blob `5affc8fd`, and `git show eb3980f2e:` of it, blob `6097cc6d`.
AC8's greps were re-run on the tree at `5a1643c8d`.

**Evidences:** TOOL-aEvidencedLens-6
- AC1 — `unique` — `lens yield: each id in its own item reads raw, confirmed, precision, defects and unique 1 per lens` and `lens yield: one item holding all five ids reads defects 1 and unique 0 on every row` printed `ok`.
- AC2 — `uncertain` — `lens yield: a refuted lens reads precision 0 and defects 0, an uncertain one unverified 1 and precision null` printed `ok`.
- AC3 — `defects` — `lens yield: a tally fault nulls defects and unique on every row rather than guessing a split` printed `ok`; the label does not show the tally WARNING the criterion also names.
- AC4 — `returned` — `lens yield: a dead synthesis returns the ledger counts and null defects and unique` and `lens yield: a dead lens keeps its row, returned false, on the deferred return` printed `ok`.
- AC5 — `lensYield` — `lens yield: the no-finding exit carries a row per lens`, `lens yield: the every-refuted exit carries a row per lens` and `lens yield: the every-lens-dead exit carries a returned-false row of zeros per lens` printed `ok`.
- AC6 — `lens yield:` — `lens yield: the spec synthesis prompt carries the marked block, a row per running lens with its precision` and `lens yield: one log line per lens names defects and unique` printed `ok`.
- AC7 — `key` — `ledger-cmp.js` unmasked over the pass-start and pass renders: `find:` 5/5 and `verify:` 5/5 byte-identical in both diff-kind arg sets, round 1 with `checklist` and `specs` and round 2 with `priorFindings`, and the returned keys EQUAL, `…-6380ce0a` and `…-62ba7747`. The `synth` prompt, which the criterion does not name, differs: it gained the LENS YIELD block.
- AC8 — `lensYield` — at `5a1643c8d`, `grep -n lensYield tools/workflows/README.md` printed line 221, which names `defects`, `unique` and the `null` rule, and `grep -c 'carries three fields'` over the same file printed 0.
- AC9 — `intensity: 'light'` — `lens yield: a light run carries a row per running lens and none for a skipped one` printed `ok`.
