# TOOL-aEvidencedLens-18 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-18

The completion of unit 15's observation of the diff-kind `resume:probe` prompt. The driver is unit
15's `u15-check.js`, present in the run's scratch directory and copied unchanged beside this unit's
renders, so it was reused and not rebuilt. Its two arg sets are unit 15's: `r1+checklist+specs`
(round 1, two checklist lines, two specs) and `r2+priorFindings` (round 2, one prior finding), each
with `base` 40×`b` and `head` 40×`c`. It runs every arg set before it exits, so a red on the first
does not hide the second.

Both renders come from the object database: `base.js` is `git show 028b5cac:tools/workflows/tier2-review.js`
and `head.js` is `git show HEAD:tools/workflows/tier2-review.js`, read at the pass's HEAD `4c45d0b20`
and re-read at `81af00218`, this unit's rev-3 spec commit, where the harness blob is the same. The
last commit to move the harness is `e9028d73d`, unit 12's.

Staged breaks, each a scratch copy of `head.js` with one occurrence asserted:

- `broken1.js` — unit 15's step-1 break, line 709: `forward slashes (a relative answer` became
  `backward slashes (a relative answer`.
- `broken3.js` — S2's break, line 720, step 3's directory line where the mask writes `<KEY>`:
  `<the first 12 hex of the head sha>` became `<the first 16 hex of the head sha>`.
- `head-plus1.js` — `head.js` with one byte, `x`, appended, to observe the S1 tie red.

Prints by render and arg set, read from each run's `result.key`:

- BASE `r1+checklist+specs` `aada6477` · BASE `r2+priorFindings` `30f26c60`
- HEAD `r1+checklist+specs` `6380ce0a` · HEAD `r2+priorFindings` `62ba7747`

**Evidences:** TOOL-aEvidencedLens-18
- AC1 — BASE blob `54cf03a30ce84f777247baeca5ce54a3a6410540`: `git hash-object base.js` equals `git rev-parse 028b5cac:tools/workflows/tier2-review.js`. HEAD blob `3faf86625e6007a6174d21f93134b6d4ddc3f051`: `git hash-object head.js` equals `git rev-parse HEAD:tools/workflows/tier2-review.js`, at `4c45d0b20` and again at `81af00218`. The tie reds on a mismatch: `head-plus1.js` hashed to `e06cb593d10e880d97121c9f75f3b0bb2ddea66d`, which differs from the HEAD blob. Then `node u15-check.js --mask-class base.js head.js`: GREEN, rc 0, exactly one `resume:probe` prompt per run, BASE and HEAD byte-identical in both arg sets, and a `<KEY>` count of 1 in each of the four runs.
- AC2 — `node u15-check.js --mask-class base.js broken3.js`: RED, rc 1, `RED (2)`, naming `resume:probe differs under the class mask` in `r1+checklist+specs` and in `r2+priorFindings`, first difference at byte 708 in step 3's line beside the `<KEY>` token, and the `<KEY>` count still 1 in all four runs. `node u15-check.js --mask-class base.js broken1.js`: RED, rc 1, `RED (2)`, naming `resume:probe` in both arg sets, first difference at byte 225, counts 1.
- AC3 — `node u15-check.js --mask-key base.js head.js`: RED, rc 1, `RED (4)`, red on BOTH arg sets, each naming `resume:probe differs under the key mask` with its own HEAD print left standing, `6380ce0a` for `r1+checklist+specs` and `62ba7747` for `r2+priorFindings`, first difference at byte 731; each arg set also reds the zero-token clause, since the key is never spelled whole in the probe. The four prints `aada6477`, `30f26c60`, `6380ce0a` and `62ba7747` are pairwise distinct.
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` without `--staged`, over the working tree carrying this pass's spec edits, ran 52 s and printed no check 12 failure, so the reciprocity join is green. Spec 15 at rev-3 carries **consumes-from** `TOOL-aEvidencedLens-12` and `TOOL-aEvidencedLens-1`; spec 12 at rev-5 and spec 1 at rev-4 each carry the **hands-off** back to `TOOL-aEvidencedLens-15`; each of the three has a §9 line naming §3. That run's two reds were check 9, the build README not yet re-rendered for those revs, which this commit re-renders, and check 23 naming the CLOSED units 1 to 9, 12 and 14, none of which has a journal record; neither 15 nor 18 is named.
- AC5 — `git show --name-only d239695c6 ad25d88c3`, unit 15's two pass commits, lists neither `memory/LIVE.md` nor `memory/ledger/2026-10.md`. This unit's `--dispatch` rows in the build's `RUN.md`, at `1e33ac76` and at `4c45d0b2`, both list the two indexes. With units 19 and 20 open the build stays SPECCED and `gen_build_index.py --write` moved neither row, and `git diff --cached --name-only` before this pass commit listed neither index, so the pass writes neither, as spec rev-3's S5 and AC5 state.
- AC6 — this record, under the build's `build/` folder, carries the journal Serves line and this Evidences block, naming both blobs with their hash-object equalities, the four prints by render and arg set, the four token counts, and the outcomes of AC2 to AC5 above, so check 23 reads it.
