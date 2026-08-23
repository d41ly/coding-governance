# TOOL-dScriptedRepeat-15 — the kit's self-test suite becomes affordable, and the number that says so is measured rather than argued

**Status:** SPECCED · rev-1 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

`check-unattended.test.sh` takes ~53 minutes. It is the compensating check for seven merge-bar legs
this build removed, so an unaffordable one is worse than the legs were: the exemption was traded for a
check nobody will run. Bring it under the 900 s ceiling `run-unattended-gates.sh` already declares for
it, without removing an arm or weakening one.

**The ceiling is the acceptance criterion, and it already exists.** The runner reds on breach today
and says so on every invocation. This unit is done when that red goes away for the right reason.

## 2. Scope (IN)

- **S1 — PROFILE FIRST, and this is the first build step rather than a note.** Three cost claims have
  been made about this suite in two days and two were wrong: "~28x more work than the question needs"
  (it is ~2x), and "~23 min of per-arm fixture reset" (a reset is **59 ms**, so all resets together
  are ~14 s of a 3199 s run — 0.4%). What IS measured: **243 checker invocations at ~13.2 s each
  inside the fixture** (3199 s ÷ 243), which is essentially the whole cost. Before any change, profile
  ONE invocation inside the suite's own fixture and record where its 13.2 s goes.
- **S2 — the lever the profile names, and only that one.** The candidates, in the order the evidence
  currently favours them:
  - subprocess count per run — the checker spawns `git`, `grep`, `awk` and `sed` per build record and
    per declaration key, and on MSYS a spawn is tens of milliseconds;
  - `--only`/`--skip` at each call site, already built and verified, which halves an invocation;
  - the shard split, measured at 1565 s against 692 s, which is imbalance rather than total work.
- **S3 — every call site passes the scope matching what its arm asserts.** `run()` gains an optional
  scope argument; an arm asserting a check-28 message passes `--only 28`, one asserting anything else
  passes `--skip 28`. An arm that asserts BOTH keeps the full run and says why in a comment.
- **S4 — the suite's own liveness survives the change.** `FLOOR_ASSERTIONS` and the per-shard floors
  are re-measured on the changed suite, and the executed count must not fall: a scoped invocation must
  run the same arms, not fewer.

## 3. Non-goals (OUT)

- **Not restructuring the checker into independently runnable checks.** Checks 1 through 27 share
  state — a later one reads a count an earlier one computed — and `--only 14` is refused today for
  exactly that reason. Untangling that is its own unit and this one must not start it.
- **Not removing or merging arms to hit the number.** The ceiling is there to force the cost down, not
  the coverage. An arm deleted to make a budget is the failure this whole build has been about.
- **Not touching the other four suites.** They are 6 s to 140 s and inside their ceilings.

## 4. Design

`run()` today is `bash "$SCRIPT" 2>&1`. It becomes `bash "$SCRIPT" ${RUN_SCOPE:-} 2>&1` with
`RUN_SCOPE` set per arm-block rather than per arm, so a block of consecutive check-28 arms declares
the scope once and a reader sees which region they are in.

The profile in S1 decides everything after that. If subprocess count dominates, the fix is inside
`check-unattended.sh` and benefits every caller including the merge bar's own `unattended kit gate`
leg — which is the outcome worth wanting, because that leg runs on every bar.

## 5. Production-readiness checklist

- **Security** — none. No new input, no new write path.
- **Observability** — `run-unattended-gates.sh` already prints per-suite seconds against the ceiling;
  the profile from S1 lands in the build's bar-cost record so the next reader inherits the numbers
  rather than re-deriving them. That record already exists and has been wrong twice; it gets the
  correction.
- **Testing** — the suite is its own test. The risk is a scoped invocation silently running FEWER
  arms, which S4's floors catch.
- **Migration/rollback** — `RUN_SCOPE` empty restores today's behaviour exactly, so rollback is one
  assignment.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/run-unattended-gates.sh --selftests` prints `ok` for the gate
  selftest with a reading under its declared 900 s ceiling, and the runner's OVER BUDGET line is
  absent for it.
- **AC2** — the assertion count `tools/unattended/check-unattended.test.sh` executes is >= its count
  at `abd0f026`. Scoping must not lose an arm, and its `FLOOR_ASSERTIONS` is re-measured to the new
  count.
- **AC3** — the profile from S1 is written into
  `memory/builds/dScriptedRepeat/build/2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md`
  naming where one invocation's time goes, with the two superseded claims marked superseded rather
  than deleted.
- **AC4** — a staged break in a check-28 rule still reds through an arm that now passes `--only 28`,
  and a staged break in a check-1..27 rule still reds through one that passes `--skip 28`. One of each
  observed in `tools/unattended/check-unattended.test.sh`, so the scoping is proven not to have
  blinded the arm it scopes.
- **AC5** — `bash tools/unattended/check-unattended.sh` with no argument is byte-identical in output
  to today's, so the merge-bar leg is untouched by this unit.

## 7. Gates

`bash tools/run-gates/run-gates.sh` and `bash tools/unattended/run-unattended-gates.sh --all`.

## 8. Open questions

- **F1 — if the profile says the cost is subprocess count inside the checker, does this unit fix the
  checker or stop at scoping?** Fixing the checker helps the merge bar too and is the better answer;
  it is also a bigger change to a file six review rounds just churned. RESOLVED (agent, 2026-08-23,
  delegated): fix whatever the profile names, and if that is the checker, land it as its own commit
  with its own staged-RED so the two changes can be reverted independently.

## 9. Revision log

- rev-1 · 2026-08-23 · drafted. The measurement in S1 replaces two earlier cost claims, both of which
  were made before anyone measured and both of which were wrong.

## 10. Reuse audit

`--only`/`--skip` already exist on the checker and are verified. `run-unattended-gates.sh` already
declares and enforces the ceiling. Nothing new is built until S1 says what to build.
