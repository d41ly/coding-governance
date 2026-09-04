# TOOL-dSealedTally-1 — `--landed` writes its terminal phase after every check that can refuse it

**Status:** SPECCED · rev-1 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/unattended.sh` sets `phase LANDED` at line 2357 and performs the lander-marker
check that can refuse at line 2373. So a refused `--landed` exits 1 while the run-state file records
the landing it just refused. Move the write below every check, so a refusal leaves the phase alone.

## 2. Scope (IN)

- **S1** `set_fact "$rel" phase LANDED` moves below the lander-marker gate, so no check that can
  return non-zero runs after the terminal phase is written.
- **S2** The witness computation stays where it is — the marker gate compares against it — so only
  the phase write moves, not the block around it.
- **S3** A hermetic probe, built from `tools/unattended/unattended.test.sh`'s own setup per the
  standing do-not-run instruction, proving that a `--landed` refused on the marker leaves the phase
  at `LANDING`.
- **S4** The same probe run against the UNPATCHED driver, showing the phase reaching `LANDED` — the
  staged-RED half, without which the arm is an assertion about nothing.

## 3. Non-goals (OUT)

- Not changing what `--landed` checks. The anchor selection, the witness rule and the marker
  equality are all correct and are only being re-ordered around.
- Not making the lander runnable from a worktree. That a detached head cannot run
  `tools/push-main.sh` is a real gap, but it is a different mechanism and belongs to its own unit.
- Not auditing the other verbs for the same ordering. `--close` and `--abort` may or may not share
  it; a sweep is a separate unit if the closing review wants one.
- Not running the unattended self-test suites. Standing owner instruction, 2026-08-23.

## 4. Design

### Data model

None. `set_fact` writes one key in the run-state file's generated half and the key is unchanged.

### Migration

None. A run-state file already at `LANDED` is not rewritten by this change; the guard that a run
reaches `LANDED` only from `LANDING` already refuses a second call.

### Rollout

One statement moves. The behaviour change is strictly a refusal writing less than it used to, so
nothing that previously succeeded changes.

### Files touched (estimate)

`tools/unattended/unattended.sh` (~8 lines: the moved `set_fact` call and a comment stating why the
ordering is load-bearing, since the next reader's instinct will be to hoist it back beside the
anchor selection it belongs to conceptually).

### Alternatives rejected

Writing the phase first and REVERTING it on refusal. Rejected: a compensating write is a second
place the terminal phase is decided, and a run killed between the write and the revert leaves
exactly the state being fixed. Not writing until the decision is made has no such window.

## 5. Production-readiness checklist

- security — N/A — no write path outside the run's own record.
- perf / scale — N/A — one shell statement moves.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the refusal path is the case being fixed; the success path is
  byte-identical.
- observability — a refused `--landed` now leaves a record whose phase matches its exit code, which
  is the observability being restored.
- risks — the risk of the CURRENT code is a record claiming a landing nothing observed, which is
  the exact failure this kit exists to prevent. The change has no new risk direction.
- testing + left-shift gates — S3 and S4 together are the left-shift, run as a hermetic probe
  rather than through the suite, per the standing instruction.
- migration / rollback — reverting the commit is the rollback.
- user docs — the verb entry in `memory/guides/UNATTENDED-VERBS.md` describes the checks but not
  their ordering, so no doc change is owed. Verified against that file at `0f19429a`.

## 6. Acceptance criteria

- **AC1** — When `--landed` is refused by the lander-marker gate, the run-state file's `phase:` line
  still reads `LANDING`, proved by a hermetic probe built from `tools/unattended/unattended.test.sh`
  and committed under this build's `build/` folder.
- **AC2** — When that same probe runs against the unpatched `tools/unattended/unattended.sh`, the
  phase reaches `LANDED`, recorded as an observed staged break rather than asserted.
- **AC3** — When `--landed` succeeds with a marker naming HEAD, it still writes `phase: LANDED` and
  exits 0, proved by the probe's positive arm — so the move did not disable the write.
- **AC4** — When `bash tools/unattended/run-unattended-gates.sh --checks` runs, it exits 0, which is
  the sanctioned non-self-test verification for this kit.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs, the `unattended kit gate` leg is green.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory-hygiene` ·
`bash tools/unattended/run-unattended-gates.sh --checks`. The kit's `*.test.sh` suites are NOT run:
standing owner instruction, and the compensating check is AC1's hermetic probe.

## 8. Open questions

- **F1 — does the probe belong in the tracked tree or in scratch?** A probe under `build/` is
  committed evidence a later reader can re-run; a scratch probe leaves only a claim. Options: commit
  it, or run it and record the transcript. Recommendation: commit it, because AC2's staged break is
  the kind of claim that is worthless without a re-runnable artifact.
  RESOLVED (agent, 2026-09-04, delegated): commit it under `memory/builds/dSealedTally/build/`, per
  the recommendation.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Line numbers 2357 and 2373 verified against
  `tools/unattended/unattended.sh` at `0f19429a`, and the defect reproduced with the exit code
  captured directly rather than through a pipe.

## 10. Reuse audit

The seam is `set_fact` in `tools/unattended/unattended.sh`, which is already the single writer for
run-state facts — this unit reuses it unchanged and only moves one call site, which is why no new
helper appears. `reuse_lookup.py` surfaced `.unattended.conf` as the kit's shared-seam affordance,
which is the conf this verb reads `LANDER_MARKER` from and is consistent with touching no new
surface.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
