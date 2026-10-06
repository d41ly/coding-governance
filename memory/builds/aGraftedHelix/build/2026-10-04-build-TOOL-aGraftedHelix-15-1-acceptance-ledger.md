# Acceptance ledger — TOOL-aGraftedHelix-15

**Serves:** journal TOOL-aGraftedHelix-15

Node `a`, 2026-10-05. The build commit is `af81d6d6`, over the spec's rev-3 commit `f99ef127`, which
replaced the S10 append with a merge before any code: unit 3's parser in the review harness reads one
by-design block per checklist string. No merge bar and no self-test suite ran in this pass. AC1 to AC6
ran as a slice of the build-harness suite, built in the session scratchpad under a name that is not a
`.test.sh`: the suite's prologue, its fixtures, the writers' arm, and every arm from the `NOSUBJ`
fixture through the end of the opt-in audit block, the new GH15 block among them. It drove the
rendered harness through the suite's own stub hooks: 162 arms, all `ok`. Twelve staged copies of the
render each disabled one mechanism, and each turned its arms `FAIL`. A thirteenth re-spelled the
copied by-design head and turned the head-parity arm `FAIL`. Every copy was deleted after its run.

**Evidences:** TOOL-aGraftedHelix-15
- AC1 — `agent:commit:specs:tB` — over a pathless authored unit, the trace read
  `agent:spec:tB:g0 agent:commit:specs:tB agent:audit:subjects:r1`, with one commit line. The
  commit prompt named the rendered `gen_build_index.py --write`, `Pass: none`, `spec(tB): A-tB-1`, the
  H1 locator, the rendered `gotchas.py --for-diff HEAD~1..HEAD` and `FOREIGN`. The log read
  `spec stage: committed 1 spec(s) at` with the sha. The audit's `checklist` read both heads, the label
  between them, items alpha, beta and gamma with alpha once, and one by-design head counting 2. With
  `specAudit` absent the stage ran once, the roster went out, and `specCommit` carried the sha and the
  checklist beside the act-on-it `nextAction`. Red with the stage's `agent(` call deleted in a copy.
- AC2 — `A-tB-1` — the resolver's roster line read `A-tB-1 | spec memory/builds/tB/spec/…`, the
  committed path, and the hand-out's roster carried it as `specPath`. A caller `s1` lost: the prompt
  dropped `| spec s1 |` and the log named `s1 -> <committed path>`. Red with the fill line deleted.
- AC3 — `agent:commit:` — absent when the writers authored nothing, beside the log
  `no commit — the writers authored no unit of this roster`. Absent beside caller `subjects`, beside
  the log `so A-tB-1 is left to the caller to commit`. Red with the de-duplication deleted, which
  names the id twice.
- AC4 — `resumeFromRunId` — each of the five commit doubles ended in `THROW` naming in turn the stage,
  `hook said no`, `sha` with `"abc1234"`, `A-tB-1`, and `A-tB-1` at its foreign path. Each carried
  `WITHOUT` `resumeFromRunId` and `--plan tB --paths`, and none traced `agent:audit:subjects` or
  `workflow:`. The null double with `specAudit` absent named the fresh re-invoke and no `git ls-tree`.
  Red with the sha check, the outside-folder check, and the remedy each disabled in its own copy.
- AC5 — `notAtHead` — a resolver double naming one path ended in `THROW` with
  `not at HEAD, so no blob pins them:` and that path, the fresh re-invoke, and `git ls-tree HEAD`. Under
  `auditIds` it said `subjects` cannot stand beside `auditIds`, with no `git ls-tree`. A resolved
  subject beside a `notAtHead` path threw with no `workflow:` line. A pathless `alreadyPresent` unit
  threw before `agent:audit:subjects`, naming `--plan tB --paths`. An all-refused set threw naming
  `refused every audit unit (A-tB-1`. The resolver prompt named `notAtHead` and the working-tree rule.
  Red with the `notAtHead` branch, the instruction, the pathless refusal and the all-refused refusal
  each deleted in its own copy.
- AC6 — `no spec subjects could be pinned` — the empty resolver double kept that sentence, stated
  `none resolved at HEAD or exists on disk`, and ended in the remedy. The dirty double kept
  `Commit the fold` and named the fresh re-invoke. The clean-round double over no unit threw
  `covered NO unit` with the remedy, with no `git ls-tree` under `auditIds`, and so did caller
  `subjects` over a pathless unit. `grep -c "re-invoke with the same arguments" tools/workflows/unattended-build.js`
  printed `0`, and so did `grep -c "Commit the authored specs and re-invoke" tools/workflows/unattended-build.js`.
- AC7 — `one committer commits once after all of you return` — the traced writers' prompt carried it,
  and the slice's absence arm found no `the caller commits once after all of you`.
  `grep -n "THE SPEC COMMIT (TOOL-aGraftedHelix-15)" tools/workflows/unattended-build.js` printed one
  line, 120. `grep -c "names four install paths" tools/workflows/README.md` printed `0`.
  `grep -n "gen_build_index" tools/workflows/README.md` printed line 38, the install-path sentence.
  `grep -c "the caller commits" tools/workflows/unattended-build.js` printed `0`. The hand-out comment
  opens `THE COMMIT STAGE FILLS` `specPath`, and the `meta` `description` names the ONE commit.
- AC8 — `git status --porcelain tools/workflows/` — printed nothing after the renderer's `--render`
  mode ran once at the build commit. `node tools/workflows/check-workflow-syntax.js` printed
  `6 workflow script(s) parsed clean`. A `Workflow` call JSON naming the render as `scriptPath`, piped
  into `node tools/hooks/agent-cap.js`, exited 0. A scratch copy with an `agent(` call appended in a
  loop printed `BLOCKED by agent-cap`.
- AC9 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — with `cdf8da2f` it
  printed `epoch: review-harness · clean · 1.32`, up from `1.31` at that parent.
  `bash tools/check-kit-versions.sh` printed `kit-versions: clean — 16 declared carrier(s) under tools/`.
  Line 3 of `tools/workflows/unattended-build.js` reads `1.4`, up from `1.3` at that parent.

Left to the main loop's run at VERIFYING, because only a suite observes them: the build-harness
self-test whole, at its floor of 365, the review-harness self-test, and the legs the spec's section 7
names. `python tools/lexicon/lexicon.py` exited 0 at the build commit, and
`python tools/codebase-map/test_codebase_map.py` printed six `ok` lines.
