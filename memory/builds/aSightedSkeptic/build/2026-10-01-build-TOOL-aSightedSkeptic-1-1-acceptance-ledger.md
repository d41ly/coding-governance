# TOOL-aSightedSkeptic-1 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-1

`renderBrief(role)` now opens every finder and every skeptic prompt with the repo, the subject, the
context, the round, the by-design list and the prior findings, and a diff skeptic is told to refute a
pre-existing defect. The arm readings come from the main loop's one VERIFYING run of the tier2-review
self-test at 149e89d6, which printed `---- 165 passed, 0 failed ----`, and from the same test file run
against the BASE render at 9fdd0c18 in a frozen clone, which printed `---- 56 passed, 109 failed ----`
and the floor-unreachable line. The greps and the direct checks were re-run on the tree at 95121476,
whose `tools/` is byte-identical to 149e89d6, so they read the build's tip rather than this unit's
own commit 0e1a2ef6.

**Evidences:** TOOL-aSightedSkeptic-1
- AC1 — `a skeptic prompt carries the repo, the range, the context and the by-design list` — the
  VERIFYING run printed `ok` for the arm, and the run against the BASE render printed `FAIL` for it.
- AC2 — `every finder and skeptic prompt opens with the shared brief` — both halves printed `ok`:
  "diff run, 10 prompts, 1 distinct CONTEXT line(s)" and "spec run, 8 prompts, 1 distinct CONTEXT
  line(s)". Against BASE both printed `FAIL`, reading 8 prompts with 2 distinct CONTEXT lines on
  each run.
- AC3 — `a diff skeptic is told to refute a pre-existing defect and a by-design one` — `ok` at
  VERIFYING, `FAIL` against the BASE render.
- AC4 — `a spec-audit skeptic prompt names the repo and every subject at its blob` — `ok` at
  VERIFYING, `FAIL` against the BASE render.
- AC5 — `a fold-round skeptic is shown the prior round's findings` — both halves printed `ok`, the
  verify half ("carries PRIOR-MARK and the duplicate rule") and the find half ("still carries
  PRIOR-MARK and Judge the FIX"). Against BASE both printed `FAIL`. Per the commit's `Decided:`
  trailer the verify half asserts the phrase "refuted as a duplicate", since the bare word already
  sat in the parent's prompt and could not red.
- AC6 — `grep -c "^function renderBrief(role)" tools/workflows/tier2-review.template.js` — printed
  1, and `renderBrief('finder')` and `renderBrief('skeptic')` each counted 1 over the same file. The
  same three greps over `git show 9fdd0c18:` of the file each printed 0.
- AC7 — `deriveReviewKey` — `git diff 0e1a2ef6~1 0e1a2ef6 -U0` of the template, piped through
  `grep -cE "inputPrint|deriveReviewKey|REVIEW_SHAPE"`, printed 0 on this unit's build commit. At
  VERIFYING all 20 arms beginning `AC3` printed `ok`. The 14 of them that predate the build also
  printed `ok` against the BASE render.
- AC8 — `bash tools/workflows/check-verifier-fanout.sh` — exited 0 and printed "clean — 6 workflow
  script(s) obey the ≤5-verifier rule". `check-review-join.sh` exited 0, and
  `node tools/workflows/check-workflow-syntax.js` exited 0 with "6 workflow script(s) parsed clean".
  `--print-cap` printed 5, and the `sed` render piped into `diff` printed 0 lines.
- AC9 — `FLOOR_ASSERTIONS` — the VERIFYING summary read `PASS (165 assertions)` against
  `FLOOR_ASSERTIONS=165`, and `grep -c "FLOOR_ASSERTIONS="` over the test file printed 1. This
  unit's own raise was 77 to 84, stated in 0e1a2ef6's `Decided:` trailer and read back from
  `git show` at that commit. The BASE-render run printed "executed 56 assertions against a floor of
  165", so the floor arm reds when arms are stranded.
