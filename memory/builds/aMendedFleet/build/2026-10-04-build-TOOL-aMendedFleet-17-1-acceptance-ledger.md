# TOOL-aMendedFleet-17 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-17

**Evidences:** TOOL-aMendedFleet-17
- AC1 — `node -e` slice of `extractFindingClasses` out of `tools/workflows/tier2-review.js` — the six claims over the three items returned `[beta-two]`, `[alpha-one, gamma-three]`, `[gamma-three]`, `[]`, `[]` and `[C9]`. Observed RED first: against the parent render the slice threw, finding no such function; with the dedupe removed `C3, C3 z` returned gamma-three twice; with the head anchor removed `see C2 later` returned `[beta-two]`
- AC2 — the same `node -e` slice of `renderCell` and `renderAppendix` — the header read the eight columns then `classes`, the first row ended `| alpha-one gamma-three |` and the second `| - |`. Observed RED first with `classes` dropped from the column list: the header and both last cells failed
- AC3 — `python tools/workflows/review_replay.py --known` the aWindowedPass round-1 closing review, `--candidate` a scratchpad copy whose appendix gained a ninth `classes` column — 26 of 26 known findings MATCHED, recall 1.00, exit 0
- AC4 — `node tools/workflows/check-workflow-syntax.js` after `check-protocol-parity.test.sh --render` — six scripts parsed clean, exit 0; `grep -c extractFindingClasses` reported 2 for both the template and the render
- AC5 — `grep -n classes tools/workflows/README.md` — lines 211 to 221: the ledger's `classes` field, the `C<n>` fallback and the nine appendix columns; no line says eight columns

## What the close owes

The `tier2-review self-test` leg was not run in this pass. Its appendix header pin moved to nine
columns, a new arm asserts the `classes` field and cells, and its assertion floor rose 180 to 181.
The extracted runner was only PARSED, through the `AsyncFunction` constructor rather than
`node --check` (the node-check gotcha), and that parse was observed red on a staged break inside the
new arm. A clean parse proves nothing about the arm's assertions. The
`workflow script syntax`, `review-protocol parity (kit vs dogfood)`, `review-replay selftest`,
`lexicon naming predicates` and `codebase-map coverage + freshness` legs are the close's too. S6 is
observed only by this build's closing diff review, the first live run to write a record.
