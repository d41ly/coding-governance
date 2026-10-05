# TOOL-aEvidencedLens-15 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-15

The BASE observation of the diff-kind `resume:probe` prompt under the class mask, taken after
`TOOL-aEvidencedLens-12` landed (`e9028d73d`, the last commit to move `tools/workflows/tier2-review.js`).
The driver is `u15-check.js` in the run's scratch directory, outside the tree: `u13-check.js`'s
`runReview` AsyncFunction shape with the same all-returning stubs, comparing the `resume:probe` label
only. Per run, `print` is the last `-`-separated field of `result.key`; `--mask-class` replaces the
whole key and then every remaining `print` with `<KEY>`, `--mask-key` replaces the key alone. A run
with no `resume:probe` label, or more than one, is a harness fault (rc 2); a mask writing zero
`<KEY>` tokens into the probe reds by name.

Blobs of `tools/workflows/tier2-review.js`, each read with `git rev-parse <rev>:tools/workflows/tier2-review.js`:

- BASE `028b5cac` — `54cf03a30ce84f777247baeca5ce54a3a6410540`, saved to the scratchpad as `base.js`
  by `git show` from the object database.
- pass HEAD `e4e3528c0` — `3faf86625e6007a6174d21f93134b6d4ddc3f051`, saved as `head.js` by `git show`;
  the working copy is clean against it, and AC1 is green against both.

Arg sets, both diff-kind and the same as unit 13's, `base` 40×`b` and `head` 40×`c`, `repo /tmp/r`, `context ctx`:

- `r1+checklist+specs` — round 1, `checklist ['- one class', '- another class']`, `specs ['a.md', 'b.md']`.
- `r2+priorFindings` — round 2, `priorFindings [{ ref: 'p.js:9', claim: 'PRIOR-MARK' }]`.

Prints, BASE against HEAD: `r1+checklist+specs` `aada6477` against `6380ce0a`; `r2+priorFindings`
`30f26c60` against `62ba7747`.

**Evidences:** TOOL-aEvidencedLens-15
- AC1 — `node u15-check.js --mask-class base.js tools/workflows/tier2-review.js`: GREEN, rc 0. Each
  render produced exactly one `resume:probe` prompt per arg set, the two were byte-identical under the
  class mask in both arg sets, and the `<KEY>` token count was 1 on each side of each arg set (four
  runs, four counts of 1). The same run against `head.js` from the object database: GREEN, same counts.
- AC2 — `node u15-check.js --mask-key base.js tools/workflows/tier2-review.js`: RED, rc 1, naming
  `resume:probe differs under the key mask` in both arg sets with the print left standing, HEAD print
  `6380ce0a` (round 1) and `62ba7747` (round 2), the first difference at byte 731 in step 3's
  directory line; the key-only mask also wrote 0 `<KEY>` tokens on every side, so it reds the
  could-not-pass clause too. The key is never spelled whole in the diff-kind probe.
- AC3 — `node u15-check.js --mask-class base.js broken.js`, where `broken.js` is a scratch copy of
  `head.js` with step 1's `forward slashes (a relative answer` changed to `backward slashes (a relative
  answer` (one occurrence, asserted): RED, rc 1, naming `resume:probe differs under the class mask` in
  both arg sets, the first difference at byte 225, with the token counts still 1.
- AC4 — this record, under the build's `build/` folder, names both blobs of `tools/workflows/tier2-review.js` read with `git rev-parse`, BASE `54cf03a3` and pass HEAD `3faf8662`, all four prints, the token counts of AC1, and the outcomes of AC2 and AC3 above; it carries the journal Serves line and this Evidences block, so check 23 reads it.
