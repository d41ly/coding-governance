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
- AC9 — `--pending-run wf_0a1b2c3d-4e5` — run by hand in a scratch fixture built the way the driver
  suite's prologue builds one: the hold wrote `hold-run: wf_0a1b2c3d-4e5`, `--status` printed
  `pending run wf_0a1b2c3d-4e5` between the resume and reason lines, the `--resume` take-over printed
  `relaunch the deferred review FIRST — pending run wf_0a1b2c3d-4e5`, and after a second `--hold`
  with no flag the fact read empty, `--status` printed no pending run and a later take-over printed
  no relaunch.
- AC10 — `--pending-run` — in the same fixture a value carrying ` · `, one carrying a newline and a
  65-character one each exited 1 on `UNATTENDED check 55 FAILED — --pending-run takes a workflow run
  id of 1 to 64 letters, digits, underscores and dashes`, and `git hash-object` of the run-state file
  was unchanged after each.
- AC11 — `bash tools/workflows/check-protocol-parity.test.sh --check` — after `--render`, the leg's
  read-only form printed `in parity — 2 rendered pair(s) match their templates`, with the durability
  paragraph in `memory/guides/REVIEW-PROTOCOL.md` and the deferred branch in both
  `tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-build.js`;
  `bash tools/unattended/adopt-unattended.sh --check` printed `in sync`, and the rendered Skill names
  `--pending-run` twice.
- AC13 — `tools/workflows/tier2-review.js` — `git show origin/main:tools/workflows/tier2-review.js`
  after a fetch in this pass read `version: '1.8'`, as BASE does; the staged diff of the file moves
  exactly one line carrying `version: '`, from 1.8 to `1.9` in `meta.version`, the
  `gov:kit tier2-review@` marker and the `gov:kit review-harness@` marker alike. The
  `check-kit-versions.sh` half is the post-build bar's.
- AC14 — `wc -c < memory/guides/REVIEW-PROTOCOL.md` — 17479 at the parent and 18068 with this unit,
  589 bytes larger against the 700 priced in S8, and under the 61440 its class declares.
