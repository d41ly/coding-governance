# TOOL-aEvidencedLens-4 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-4

A spec fold round reads its diff, and a moved subject is graded rather than fixed at BLOCKER. The
sources: the pass commit `49d4139c8`, whose body records `u4-check.js`, a scratch stub run with 24
spec assertions over AC1 to AC5 green and 17 of them RED against `pre-u4.js`, a `--compare` over four
diff-kind runs byte-identical in every probe, find, verify and synth prompt, schema and log, a scratch
slice of the suite body with 49 assertions where 10 of the 12 new ones were RED on `pre-u4.js` and the
other two are the proceed controls, and the AC7 figures; the main loop's VERIFYING run of the
tier2-review self-test in a frozen clone at `0c8dd1761`, which printed `---- 239 passed, 1 failed ----`,
the one FAIL being the rubric arm, an extractor defect fixed in `5a1643c8d`, whose re-run printed
`---- 240 passed, 0 failed ----`; and greps and direct checks re-run on the tree at `5a1643c8d`. The
direct comparison is `ledger-cmp.js`, the scratch `runReview` driver described in this build's
`TOOL-aEvidencedLens-1` ledger, over `git show 49d4139c8~1:` of `tools/workflows/tier2-review.js`,
blob `42899455`, and `git show 49d4139c8:` of it, blob `5affc8fd`.

**Evidences:** TOOL-aEvidencedLens-4
- AC1 — `prevBlob` — the VERIFYING run printed `ok` for the four prelude arms: `fold: a malformed prevBlob at round 2 -> refused`, `fold: a well-formed prevBlob at round 1 -> refused`, `fold: a well-formed prevBlob at round 2 -> proceeds` and `fold: a diff review ignores a bad prevBlob`. They evaluate the extracted prelude, so no agent can be traced.
- AC2 — `FOLD DIFF` — the VERIFYING run printed `ok` for `fold: a round-2 spec run carries each subject's FOLD DIFF line in every find: and verify: prompt` and `fold: a WARNING names the subject lacking prevBlob, and RUN INTEGRITY says 2 of 3`.
- AC3 — `first-round review` — the VERIFYING run printed `ok` for `fold: a round-2 run with neither input is a DEGRADED fold review, warned and in RUN INTEGRITY, never first-round`. The round-1 half, its slice byte-identical to the same slice under `pre-u4.js`, was observed only inside the pass's `u4-check.js` run.
- AC4 — `hash-object` — the VERIFYING run printed `ok` for `fold: a moved and an unusable blob: the WARNING, the MOVED SUBJECT line and RUN INTEGRITY name each`, `fold: the spec probe asks for hash-object per subject with blobs optional, and no prompt carries the fixed BLOCKER`, `fold: a null probe reads as the resume probe died, never as no move` and `fold: a live probe with no blobs key leaves every subject UNCHECKED, not died`.
- AC5 — `prevBlob` — the VERIFYING run printed `ok` for `fold: the review key moves with prevBlob`. `ledger-cmp.js` over the pass-start and pass renders returned EQUAL keys for both diff-kind arg sets; the round-1 spec args carrying no `prevBlob` were observed equal only inside the pass.
- AC6 — `check-workflow-syntax.js` — `ledger-cmp.js` unmasked over the pass-start and pass renders: `resume:probe` 1/1, `find:` 5/5, `verify:` 5/5 and `synth` 1/1 byte-identical in both diff-kind arg sets. At `5a1643c8d`, `node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`, `check-verifier-fanout.sh` and `check-review-join.sh` each exited 0, and `grep -c prevBlob` printed 18 over the template and 18 over the render.
- AC7 — `fold:` — the pass commit records `grep -c "fold:"` at 0 before and 13 after, and `FLOOR_ASSERTIONS` 205 to 217, 12 assertions. The VERIFYING run printed `ok` for every `fold:` line, 14 of them with the two `TOOL-aEvidencedLens-21` added. No source here holds a VERIFYING run against `pre-u4.js`; the RED reading is the pass's slice, 10 of 12 RED there.
