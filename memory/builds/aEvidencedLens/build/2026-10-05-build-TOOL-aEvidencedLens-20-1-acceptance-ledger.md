# TOOL-aEvidencedLens-20 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-20

The minors batch of unit 18's spec audit, observed at the pass's HEAD `b156dafae`. Every scratch
file lives in the run's scratch directory, outside the tree. The driver is unit 15's `u15-check.js`,
present in the scratch and copied unchanged from unit 19's copy, `cmp`-clean against unit 15's, so
it was reused and not rebuilt. `broken.js` is unit 15's step-1 break, present in unit 15's scratch
and reused; it is `cmp`-clean against a rebuild by the recorded edit, `head.js` with step 1's
`forward slashes (a relative answer` changed to `backward slashes (a relative answer`, one
occurrence asserted on each side. Unit 18's two pass commits are `54794c10c`, carrying its `Pass:`
trailer, and `81af00218`, its rev-3 spec commit.

Renders, each saved with `git show` from the object database, the form unit 18's ledger names:
`base.js` from `028b5cac` and `head.js` from `HEAD`, tied with plain `git hash-object` to BASE blob
`54cf03a30ce84f777247baeca5ce54a3a6410540` and HEAD blob `3faf86625e6007a6174d21f93134b6d4ddc3f051`.
That form runs the line-ending filters, so it ties no line-ending bytes; the filter-off tie is unit
19's.

Staged breaks, each a scratch copy:

- `head-x.js` — `head.js` with one byte, `x`, appended.
- `u15-check-exit1.js` — `u15-check.js` with `process.exit(1)` inserted after the first `red++`
  inside its arg-set loop, one insertion asserted.
- the scratch clone `%TEMP%/u20c`, at `b156dafae`, whose harness working copy took one appended byte;
  removed after the reading.

**Evidences:** TOOL-aEvidencedLens-20
- AC1 — spec 18 reads `rev-4`, one above the `rev-3` its pass closed at. Its §1 says unit 15's ledger already carried the four prints and the per-arg-set key-mask reds and lacked S1's tie and S2's step-3 break; its §4 second Evidence bullet places `inputPrint` at `tools/workflows/tier2-review.js:696-697` and `round` in `deriveReviewKey` at `:702` only; its rev-4 §9 line states the filters-on S1 form with the filter-off tie as unit 19's, S5 as holding only if no promotion followed and two did, and `broken1.js` as unit 15's `broken.js`. This ledger names the break `broken.js` throughout.
- AC2 — the derived build status with this unit flipped to CLOSED is CLOSED, since `derive_status` in `tools/memory-tree/gen_build_index.py` returns CLOSED when no unit holds a precedence token and every other unit is CLOSED; the rendered status in `memory/LIVE.md` and `memory/ledger/2026-10.md` was SPECCED. They differ, so this unit's `--dispatch` row at `b156dafa` in the build's `RUN.md` declares both indexes, and `git diff --cached --name-only` before this pass's one commit listed both, each moved by `gen_build_index.py --write`, which dropped the build's `memory/LIVE.md` row and turned its shard row from SPECCED to CLOSED, and no other index. Unit 18's dispatch rows at `1e33ac76` and `4c45d0b2` both declared both indexes; `git show --name-only` of `54794c10c` lists the build README, `RUN.md`, its ledger and specs 1, 12, 15 and 18, and of `81af00218` the build README and spec 18, so neither of its commits wrote either index.
- AC3 — unit 18's AC1 assertion over `head-x.js`: RED, naming `head-x.js`, `git hash-object` printed `e06cb593d10e880d97121c9f75f3b0bb2ddea66d` against `git rev-parse HEAD:tools/workflows/tier2-review.js` `3faf86625e6007a6174d21f93134b6d4ddc3f051`, beside the two GREEN equalities for `base.js` and `head.js`. In the clone, the clean working copy hashed with `--no-filters` to the HEAD blob; after one byte was appended, `git status` showed it modified, a `git show HEAD:tools/workflows/tier2-review.js` save hashed with `--no-filters` to `3faf86625e6007a6174d21f93134b6d4ddc3f051`, the rev-parse blob, and the dirty working copy hashed to `e06cb593d10e880d97121c9f75f3b0bb2ddea66d`, so it did not tie. The clone was removed.
- AC4 — precondition: `git show --name-only d239695c6 ad25d88c3`, unit 15's two pass commits, lists the build README, `RUN.md`, unit 15's ledger and spec 15 for `d239695c6` and unit 15's ledger for `ad25d88c3`, and neither `memory/LIVE.md` nor `memory/ledger/2026-10.md`.
- AC5 — spec 1 reads `rev-4`, spec 12 `rev-5` and spec 15 `rev-3`. The rev-4 §9 line of spec 1 and the rev-5 line of spec 12 each name `TOOL-aEvidencedLens-15`, and spec 15's rev-3 line names `TOOL-aEvidencedLens-12` and `TOOL-aEvidencedLens-1`.
- AC6 — unit 18's ledger records BASE `r1+checklist+specs` `aada6477`, HEAD `r1+checklist+specs` `6380ce0a`, BASE `r2+priorFindings` `30f26c60` and HEAD `r2+priorFindings` `62ba7747`, pairwise distinct, and `node u15-check.js --mask-class base.js head.js` re-printed the same four by render and arg set, GREEN, rc 0. `node u15-check.js --mask-key base.js head.js`: RED, rc 1, `RED (4)`, red on both arg sets. `node u15-check-exit1.js --mask-key base.js head.js`: rc 1, red on `r1+checklist+specs` only, and `r2+priorFindings` never ran, the defect unit 18's AC3 stop clause names.
- AC7 — `node u15-check.js --mask-class base.js broken.js`: RED, rc 1, `RED (2)`, naming `resume:probe differs under the class mask` in `r1+checklist+specs` and in `r2+priorFindings`, first difference at byte 225, and each `<KEY>` count 1 on both sides of both arg sets.
- AC8 — this record, under the build's `build/` folder, carries the journal Serves line and this Evidences block, one line for each of AC1 to AC7, so check 23 reads it.
