# TOOL-dDerivedDocket-29 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-29

The review harness writes every lens and skeptic-batch result under a review key before returning,
reuses what a re-run finds there, and exits `deferred-platform` on any dead agent; the build harness
returns that deferral instead of throwing, and `--hold` records the Workflow run it was held on.
AC1 to AC7 run through `tools/workflows/tier2-review.test.sh` and AC8 through
`tools/workflows/unattended-build.test.sh`, and each carries a `permission:` line deferring the
observation to a run the orchestrator makes after this commit; AC12 is observed by the build's
closing review and AC13's leg half by the post-build bar. None of those gets a line here. The same
behaviour was watched in this pass by independent scratch drivers, not by the suites: every AC1 to
AC7 case over stub agents, two staged breaks (an optional verdict `path`, reuse matched on the file
name alone) flipping AC1 and AC3, and AC8's deferred double returning `exit: 'deferred-platform'`
where the same double without the field still throws.

**Evidences:** TOOL-dDerivedDocket-29
- AC1 — `tools/workflows/tier2-review.test.sh` — the `tier2-review self-test` leg of the post-build
  bar at 364278a8 exited 0 on `PASS (60 assertions)`, and its AC1 lines held: every `find:` prompt
  names `review-lenses/<key>/find-<lens>.json`, every `verify:` prompt names
  `review-lenses/<key>/verify-<first id>-<last id>.json`, both kinds order the write before the
  return, and the diff finding, spec finding and verdict schemas each list `path` in required
- AC2 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its
  `tier2-review self-test` leg held the AC2 lines: the first run defers pending the two dead lenses,
  and the re-run with identical `args` spawns exactly `find:seams find:regressions` and completes,
  reporting two lenses reused
- AC3 — `tools/workflows/tier2-review.test.sh` — the same leg held the AC3 lines: a lens file under
  the old key is dispatched for another round, head sha, resolved base sha, `context`, `byDesign`
  and `priorFindings`, each beside a control under its own key that is reused; one moved spec-audit
  subject blob dispatches its lens; and a file with the right name and another `key` is dispatched
- AC4 — `tools/workflows/tier2-review.test.sh` — the same leg held the AC4 lines: a dead probe
  dispatches all four lenses, and the log says nothing could be reused
- AC5 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 the same leg
  held the AC5 lines: the verify prompt names the batch print its file must carry, a verify file with
  the key and the matching print is reused, and the right ids over a print of other claims are
  dispatched
- AC6 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 the same leg
  held the AC6 lines: every lens dead returns deferred-platform, blockers null and the four `find:`
  labels pending; two dead with nothing found returns deferred, those two pending, and a note that is
  neither clean nor partial; one dead with every finding refuted returns deferred; and the no-death
  control returns complete and clean
- AC7 — `tools/workflows/tier2-review.test.sh` — the same leg held the AC7 lines: one dead skeptic
  batch returns deferred, blockers null, that batch pending, and no synthesis runs; a dead synthesis
  returns deferred with synth pending; and a synthesis leaving one confirmed id out returns complete
  beside `blockers: null`
- AC8 — `tools/workflows/unattended-build.test.sh` — the `unattended-build self-test` leg of the same
  bar exited 0 on `PASS (512 assertions)`, and its DP lines held: a deferred audit is a RESULT, not a
  throw, the non-integer refusal does not fire first, and it returns exit deferred-platform naming
  the Audit stage and the pending labels, with the empty `roster`, and no `agent:audit:record` agent
- AC9 — `--status` — run by hand in a scratch fixture built the way the driver suite's prologue
  builds one: `--hold` with `--pending-run wf_0a1b2c3d-4e5` wrote `hold-run: wf_0a1b2c3d-4e5`,
  `--status` printed `pending run wf_0a1b2c3d-4e5` between the resume and reason lines, the
  `--resume` take-over printed `relaunch the deferred review FIRST — pending run wf_0a1b2c3d-4e5`,
  and after a second `--hold`
  with no flag the fact read empty, `--status` printed no pending run and a later take-over printed
  no relaunch.
- AC10 — `--pending-run` — in the same fixture a value carrying ` · `, one carrying a newline and a
  65-character one each exited 1 on the numbered refusal
  `UNATTENDED check 55 FAILED — --pending-run takes a workflow run id of 1 to 64 letters`, and
  `git hash-object` of the run-state file was unchanged after each.
- AC11 — `bash tools/workflows/check-protocol-parity.test.sh --check` — after `--render`, the leg's
  read-only form printed `in parity — 2 rendered pair(s) match their templates`, with the durability
  paragraph in `memory/guides/REVIEW-PROTOCOL.md` and the deferred branch in both
  `tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-build.js`;
  `bash tools/unattended/adopt-unattended.sh --check` printed `in sync`, and the rendered Skill names
  `--pending-run` twice.
- AC12 — `git rev-parse --git-common-dir` — the build's closing diff review ran through
  `tools/workflows/tier2-review.js` with 4/4 lenses and 5/5 skeptic batches returned, and left
  `review-lenses/diff-review-r1-869209edc6f8-364278a8b104-108311a6/` under that directory holding
  `find-correctness.json`, `find-regressions.json`, `find-seams.json`, `find-security.json` and five
  `verify-<first id>-<last id>.json` files, 1-3 through 13-15; each of the nine carries a `key` field
  equal to the directory's name, round 1 over base 869209ed and head 364278a8 as the record states
- AC13 — `tools/workflows/tier2-review.js` — `git show origin/main:tools/workflows/tier2-review.js`
  after a fetch in this pass read `version: '1.8'`, as BASE does; the staged diff of the file moves
  exactly one line carrying `version: '`, from 1.8 to `1.9` in `meta.version`, the
  `gov:kit tier2-review@` marker and the `gov:kit review-harness@` marker alike. The
  `check-kit-versions.sh` half is the post-build bar's.
- AC14 — `wc -c < memory/guides/REVIEW-PROTOCOL.md` — 17479 at the parent and 18068 with this unit,
  589 bytes larger against the 700 priced in S8, and under the 61440 its class declares.
