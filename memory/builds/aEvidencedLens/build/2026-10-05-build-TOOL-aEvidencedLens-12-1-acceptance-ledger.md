# TOOL-aEvidencedLens-12 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-12

The spec skeptic line folds evidence by line breaks only, so a pipe survives. The sources: the pass
commit `e9028d73d`, whose body records the direct checks of `u12-check.js`, a scratch driver run in the
pass and not the suite; the main loop's VERIFYING run of the tier2-review self-test in a frozen clone
at `0c8dd1761`, which printed `---- 239 passed, 1 failed ----`, the one FAIL being the rubric arm, an
extractor defect fixed in `5a1643c8d`, whose re-run printed `---- 240 passed, 0 failed ----`; and greps
and direct checks re-run on the tree at `5a1643c8d`. The direct comparison is `ledger-cmp.js`, the
scratch `runReview` driver described in this build's `TOOL-aEvidencedLens-1` ledger, over
`git show e9028d73d~1:` of `tools/workflows/tier2-review.js`, blob `6097cc6d`, and
`git show e9028d73d:` of it, blob `3faf8662`.

**Evidences:** TOOL-aEvidencedLens-12
- AC1 — `pre-u12.js` — the pass commit records that the verify line carries `cmd: git ls-files | grep -c spec -> 11` with no escaped pipe, the two-line evidence on one line, and a line-break-only evidence as `-`, while `pre-u12.js` carries the escaped pipe and reads the line break as blank. The VERIFYING run printed `ok` for both `spec evidence:` arms: a pipe in evidence reaches the verify line unescaped, byte for byte, and a line break folds to one space; and evidence that is only a line break reads as a dash.
- AC2 — `check-workflow-syntax.js` — the pass commit records the 12 diff-kind prompts byte-identical to `pre-u12.js` and the syntax check exiting 0. `ledger-cmp.js` unmasked over the pass-start and pass renders: `resume:probe` 1/1, `find:` 5/5, `verify:` 5/5 and `synth` 1/1 byte-identical in both arg sets, keys equal. At `5a1643c8d`, `node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`.
- AC3 — `renderCell` — the pass commit records that a reason `a | b\nc` renders as `a \| b c` in every appendix row, and that a staged `renderCell` without the escape renders `a | b c`, RED. The VERIFYING run printed `ok` for `ledger: the appendix is rendered by the harness: a pipe and a line break in a cell leave the row count unchanged`. The byte-identity of that row to `pre-u12.js` was observed only inside the pass.
- AC4 — `spec evidence:` — the pass commit records `grep -c "spec evidence:"` at 0 before and 4 after, and `FLOOR_ASSERTIONS` 229 to 231, the arm adding 2. The VERIFYING run printed `ok` for both `spec evidence:` lines. No source here holds a VERIFYING run against `pre-u12.js`; the RED reading is the pass's own AC1 check over it.
- AC5 — `function renderPromptLine` — at `5a1643c8d`, `--print-cap` printed 5, the template with `{{FANOUT_CAP}}` replaced by 5 compared byte-identical to `tools/workflows/tier2-review.js` by `cmp`, and `grep -c "function renderPromptLine"` over the render printed 1. The pass commit records the same render equality at its own commit.
- AC6 — `renderPromptLine` — the pass commit records 2 occurrences in `memory/map/generated/symbols.json`, 0 before; at `5a1643c8d`, `grep -c '"renderPromptLine"'` over it printed 2.
