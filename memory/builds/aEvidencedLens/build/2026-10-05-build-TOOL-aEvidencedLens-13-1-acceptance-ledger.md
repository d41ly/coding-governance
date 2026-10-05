# TOOL-aEvidencedLens-13 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-13

The cumulative BASE observation of the diff-kind finder and skeptic prompts, taken after
`TOOL-aEvidencedLens-12` landed (`e9028d73d`, the last commit to move `tools/workflows/tier2-review.js`).
The driver is `u13-check.js` in the run's scratch directory, outside the tree: the `runReview`
AsyncFunction shape of `tools/workflows/tier2-review.test.sh` with its all-returning stubs (the probe
returns no files, each lens one finding, each skeptic confirms), plus the key mask of the spec's §4.
It compares the `find:` and `verify:` labels only; `resume:probe` is `TOOL-aEvidencedLens-15`'s and
`synth` is excluded by design (S2).

Blobs of `tools/workflows/tier2-review.js`, each read with `git rev-parse <rev>:tools/workflows/tier2-review.js`:

- BASE `028b5cac` — `54cf03a30ce84f777247baeca5ce54a3a6410540`, saved to the scratchpad as `base.js`
  by `git show` from the object database.
- pass HEAD `80b7b824f` — `3faf86625e6007a6174d21f93134b6d4ddc3f051`, the working copy clean against it.

Arg sets, both diff-kind, `base` 40×`b` and `head` 40×`c`, `repo /tmp/r`, `context ctx`:

- `r1+checklist+specs` — round 1, `checklist ['- one class', '- another class']`, `specs ['a.md', 'b.md']`.
- `r2+priorFindings` — round 2, `priorFindings [{ ref: 'p.js:9', claim: 'PRIOR-MARK' }]`.

**Evidences:** TOOL-aEvidencedLens-13
- AC1 — `node u13-check.js --mask base.js tools/workflows/tier2-review.js`: GREEN, rc 0. Per arg
  set each side carries 10 labels, 5 of them `find:` (`find:security`, `find:correctness`,
  `find:seams`, `find:verification`, `find:intent`) and 5 `verify:` (`verify:ids-1-1` through
  `verify:ids-5-5`), no label on one side only, and all 10 shared prompts byte-identical once each
  run's key is masked. Keys: round 1 `…-aada6477` at BASE against `…-6380ce0a` at HEAD; round 2
  `…-30f26c60` against `…-62ba7747`.
- AC2 — `node u13-check.js base.js tools/workflows/tier2-review.js`, unmasked: the comparison
  differs on 10 of 10 shared labels in each arg set, and every label's text split on its own run's
  key gives identical segments on both sides, so every differing byte range lies where the masked run
  wrote `<KEY>`; no label carried zero key occurrences.
- AC3 — `node u13-check.js --mask base.js broken.js`, where `broken.js` is a scratch copy of the HEAD
  render with the first diff lens brief's `'Security: trust boundaries` changed to
  `'Security: trust limits` (one occurrence, asserted): RED, rc 1, naming
  `find:security differs with the key masked` in both arg sets and no other label.
- AC4 — this record, under the build's `build/` folder, names both blobs of `tools/workflows/tier2-review.js` read with `git rev-parse`, BASE `54cf03a3` and pass HEAD `3faf8662`, the label counts of AC1, and the outcomes of AC2 and AC3 above; it carries the journal Serves line and this Evidences block, so check 23 reads it.
