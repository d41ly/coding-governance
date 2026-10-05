# TOOL-aEvidencedLens-3 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-3

The spec skeptic confirms by the rubric, re-runs the evidence, and refutes duplicates and by-design
findings. The sources: the pass commit `d262cb8bc`, whose body records `u3-check.js`, a scratch stub
run with 12 spec assertions over AC1 to AC4 plus 3 compare assertions for AC5, 10 of them RED against
the pass-start render, and the AC6 figures; the main loop's VERIFYING run of the tier2-review self-test
in a frozen clone at `0c8dd1761`, which printed `---- 239 passed, 1 failed ----`, the one FAIL being the
rubric arm, an extractor defect fixed in `5a1643c8d`, whose re-run printed
`---- 240 passed, 0 failed ----`; and greps and direct checks re-run on the tree at `5a1643c8d`. The
direct comparison is `ledger-cmp.js`, the scratch `runReview` driver described in this build's
`TOOL-aEvidencedLens-1` ledger, over `git show d262cb8bc~1:` of `tools/workflows/tier2-review.js`,
blob `9d8733a9`, and `git show d262cb8bc:` of it, blob `42899455`. The skeptic-line fold this unit
wrote through `renderCell` was moved to `renderPromptLine` by `TOOL-aEvidencedLens-12`, and the
VERIFYING arms read the later form.

**Evidences:** TOOL-aEvidencedLens-3
- AC1 — `AT ANY RUBRIC SEVERITY` — the VERIFYING run printed `ok` for `spec skeptic: every verify prompt confirms at any rubric severity, names the six refutation cases and the grade default, and drops the old test`.
- AC2 — `evidence: -` — the VERIFYING run printed `ok` for `spec skeptic: one-line, two-line and absent evidence ride the verify line after fix, folded to one line, absent as -`. At `5a1643c8d`, `grep -c "evidence: "` over `tools/workflows/tier2-review.js` printed 3 and over `pre-u3.js` in the scratch 2.
- AC3 — `PROBE POLICY` — the VERIFYING run printed `ok` for `spec skeptic: the verify prompt carries the finders' PROBE POLICY bytes, before Findings to judge:`.
- AC4 — `duplicate of id=` — the VERIFYING run printed `ok` for all four orphan arms: a duplicate of a confirmed survivor in its batch stays refuted, unannounced; and a duplicate of a refuted survivor, of its own id, and of an id in another batch is each demoted to unverified, ledgered, warned and counted in RUN INTEGRITY.
- AC5 — `check-review-join.sh` — `ledger-cmp.js` unmasked over the pass-start and pass renders: `resume:probe` 1/1, `find:` 5/5, `verify:` 5/5 and `synth` 1/1 byte-identical in both diff-kind arg sets, and the keys equal. The VERIFYING run printed `ok` for `spec skeptic: a diff-kind verify prompt carries no evidence field and no probe policy, and its duplicate refutation is not scanned`. At `5a1643c8d`, `node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`, and `check-verifier-fanout.sh` and `check-review-join.sh` each exited 0. The diff-kind orphan run's equal counts and ledger rows across both renders were observed only inside the pass, in its 3 compare assertions.
- AC6 — `spec skeptic:` — the pass commit records `grep -c "spec skeptic:"` at 0 before and 6 after, and `FLOOR_ASSERTIONS` 197 to 205, 8 assertions. The VERIFYING run printed `ok` for all eight `spec skeptic:` lines. No source here holds a VERIFYING run against `pre-u3.js`; the only RED reading is the pass's own, 10 RED against the pass-start render.
