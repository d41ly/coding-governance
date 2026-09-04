# TOOL-dSealedTally-1 — `--landed` writes phase and anchor together, after every check

**Status:** SPECCED · rev-3 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md) | spec-audit | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md) | spec-audit | DEPL-dSealedTally-1 DEPL-dSealedTally-5 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/unattended.sh` sets `phase LANDED` at line 2357, before the checks that can refuse
it and before `set_fact landed-anchor` further down the same function. A refused `--landed`
therefore exits 1 leaving a record that is terminal, missing its anchor, red on the unattended
leg's check 15 forever, and unrepairable — check 26 refuses `--park` and `--phase` on a finished
record, so no verb can undo what the verb did. Write the facts together, after validation, so a
refusal leaves the record untouched.

## 2. Scope (IN)

- **S1** The `phase LANDED` write moves to sit immediately before `stage_or_fail` at
  `tools/unattended/unattended.sh:2428` — that is, after the `units-at-landing` write whose
  continuation ends at 2427 — so no statement that can return non-zero runs between the terminal
  write and the staging call. The four fact writes it moves below are `landed-anchor` at 2405,
  `unpushed-at-landing` at 2409, and `units-at-landing` at 2425-2427.
- **S2** `phase` and `landed-anchor` are written TOGETHER at that point, which is the fix the corpus
  already decided at `TOOL-dScaffoldedMirror-22`: a refusal leaves the record with neither, rather
  than with one and not the other.
- **S4** A hermetic probe, built from `tools/unattended/unattended.test.sh`'s own setup per the
  standing do-not-run instruction, proving a `--landed` refused on the marker leaves the phase at
  `LANDING` and writes no `landed-anchor`.
- **S5** The same probe against the UNPATCHED driver, showing the phase reaching `LANDED` with the
  anchor absent — the staged-RED half, without which the arm is an assertion about nothing.
- **S6** A second refusal arm covering a `--landed` refused by a fact write LATER than the marker
  gate, since five more failure sites follow it; the phase must survive those too.

## 3. Non-goals (OUT)

- **Not fixing `TOOL-dUnstalledConvoy-38`.** That row is a DISTINCT defect in the same family: check
  34 compares the marker against the run's own HEAD, which a `--no-ff` merge landing can never
  satisfy, because the run's HEAD is the merge's second parent. Its predicate wants "the marker's
  commit is on the remote default branch AND has the witness as an ancestor". Deliberately out: it
  changes what the check MEANS, where this unit changes only when the record is written. That row
  stays OPEN and is not partly closed by this unit.
- **Not admitting a `--landed --repair`.** `TOOL-aGroundedOrientation-4` offers it as one of three
  fix candidates. Out of scope because it is a new verb surface for records already wedged, where
  this unit stops new ones being created. The four wedged records named across those rows were
  hand-completed and are not re-wedged by anything here.
- **Not hoisting the idempotence guard.** Rev-2’s S3 claimed `-38` needed it moved; re-derived,
  `refuse_if_terminal` already runs at `tools/unattended/unattended.sh:2255`, before every write in
  `verb_landed`. Whatever `-38` observed, it is not this verb, and asserting a half was closed without
  re-deriving it is how a spec claims coverage it does not have.
- Not making the lander runnable from a worktree.
- Not running the unattended self-test suites. Standing owner instruction, 2026-08-23.

## 4. Design

### Data model

None. `set_fact` writes keys in the run-state file's generated half and the keys are unchanged; only
WHERE the two calls sit changes.

### Inventory

The write-before-check sites, from the three OPEN rows plus this unit's own reproduction:

| Site | Line | What follows it today |
|---|---|---|
| `set_fact phase LANDED` | 2357 | the marker gate at 2373, five further fact writes, the staging call |
| `set_fact landed-anchor` | ~1890 region | unreachable once the marker gate returns 1 |
| check 26 idempotence guard | after the write | evaluated after the verb's own write, per `-38` |

### Migration

A record already wedged at `LANDED` with no anchor is NOT repaired by this unit — the four known
ones were hand-completed and are recorded as such in their rows. This unit stops the fifth.

### Rollout

Two statements move and become adjacent. The behaviour change is strictly a refusal writing less
than it used to, so nothing that previously succeeded changes.

### Files touched (estimate)

`tools/unattended/unattended.sh` (~20 lines: the two `set_fact` calls moved to 2427, the guard
ordering, and a comment stating why the ordering is load-bearing — the next reader's instinct is to
hoist the phase write back beside the anchor selection it belongs to conceptually).
`memory/builds/dSealedTally/build/` (the committed hermetic probe).

### Alternatives rejected

Writing the phase first and REVERTING it on refusal, and the roll-back-on-failure candidate
`TOOL-aGroundedOrientation-4` lists. Rejected: a compensating write is a second place the terminal
phase is decided, and a run killed between the write and the revert leaves exactly the state being
fixed. Not writing until the decision is made has no such window.

## 5. Production-readiness checklist

- security — N/A — no write path outside the run's own record.
- perf / scale — N/A — two shell statements move.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the refusal path is the case being fixed; the success path is
  byte-identical.
- observability — a refused `--landed` leaves a record whose phase matches its exit code, and the
  unattended leg's check 15 stops accumulating permanent reds on `main`.
- risks — the risk of the CURRENT code is measured, not hypothetical: four instances across three
  nodes, one of which sat red on `main` for two days before anyone noticed. The change has no new
  risk direction.
- testing + left-shift gates — S4, S5 and S6 are the left-shift, run as a hermetic probe rather
  than through the suite, per the standing instruction.
- migration / rollback — reverting the commit is the rollback; no record is rewritten.
- user docs — `memory/guides/UNATTENDED-VERBS.md` describes the checks but not their ordering, so no
  doc change is owed. Verified against that file at `0f19429a`.

## 6. Acceptance criteria

- **AC1** — When `--landed` is refused by the lander-marker gate, the run-state file is
  BYTE-IDENTICAL to what it was before the invocation, proved by a hermetic probe built from
  `tools/unattended/unattended.test.sh` and committed under this build's `build/` folder. Byte
  identity is the criterion `TOOL-dTieredTribunal-28` decided, and it is stronger than "phase reads
  LANDING with no anchor" because it also covers the other three fact writes.
- **AC2** — When that same probe runs against the unpatched `tools/unattended/unattended.sh`, the
  phase reaches `LANDED` with the anchor absent, recorded as an observed staged break.
- **AC3** — When `--landed` succeeds with a marker naming HEAD, it writes `phase: LANDED` AND
  `landed-anchor` and exits 0, proved by the probe's positive arm — so the move did not disable
  either write.
- **AC4** — When `--landed` is refused by a fact write LATER than the marker gate, the phase still
  reads `LANDING`, proved by a probe arm forcing one of the five later sites to fail.
- **AC5** — When `bash tools/unattended/run-unattended-gates.sh --checks` runs, it exits 0, which is
  the sanctioned non-self-test verification for this kit.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs, the `unattended kit gate` leg is green.
- **AC7** — When `stage_or_fail` at 2428 is forced to fail, the record is COMPLETE and terminal but
  unstaged, and the probe asserts exactly that — the one residual this ordering keeps, accepted
  because an unstaged complete record is repairable by `git add` where a wedged one is repairable
  by nothing.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory-hygiene` ·
`bash tools/unattended/run-unattended-gates.sh --checks`. The kit's `*.test.sh` suites are NOT run:
standing owner instruction, and the compensating check is AC1's committed hermetic probe.

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
- rev-2 · 2026-09-04 · folded the spec audit's B4 and H13. B4: three OPEN rows in
  `memory/backlog/TOOL.md` already recorded this defect across four measured instances and decided a
  wider fix, and rev-1's §10 cited none of them — the unit would have landed strictly narrower than
  the corpus had already decided. S2 now adopts the recorded fix of writing both facts together, S3
  adds the guard-ordering half `TOOL-dUnstalledConvoy-38` observed, and §3 states which of their
  asks are deliberately out. H13: the phase write moves to 2427 rather than merely below the marker
  gate, because five more failure sites follow it; AC4 covers them.
- rev-3 · 2026-09-04 · folded round 2’s B3, H4, M1 and M2, and this subject went NON-CONVERGENT at
  one blocker in both rounds, so the loop STOPS here with disposition FOLD per the build method.
  B3: rev-2 declared a CLOSED population of four backlog rows and missed a fifth,
  `TOOL-dTieredTribunal-28`, whose decided byte-identical criterion no AC graded — AC1 is now that
  criterion. H4: rev-2’s S3 claimed a guard needed hoisting that already runs at 2255, deleted and
  explained in §3. M1 adds AC7 for the one residual the ordering keeps. M2 corrected two addresses
  in the table rev-2 had added in order to fix addressing.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "write a run-state fact after validating it"` surfaced
`.unattended.conf` as this kit's shared-seam affordance and no closer candidate, which is consistent
with touching no new surface. The seam is `set_fact` in `tools/unattended/unattended.sh`, already the single writer for run-state
facts — this unit reuses it unchanged and moves two call sites, which is why no new helper appears.

`memory/backlog/TOOL.md` carries FOUR rows on this defect and rev-1 cited none of them, which is the
audit's B4. They are `TOOL-dScaffoldedMirror-22` (line 231, three instances, and the source of the
decided fix this unit adopts), `TOOL-aGroundedOrientation-4` (line 273, a fourth instance on node
`a`), `TOOL-dUnstalledConvoy-38` (line 212, the distinct no-ff predicate defect, deliberately out
per §3), `TOOL-dTieredTribunal-28` (line 262, a fifth OPEN row and the source of AC1’s
byte-identical criterion), and `TOOL-dRatifiedSeam-2`, which is this build’s own source row and is a
SIXTH filing of what line 231 already recorded. Closing this unit closes 231, 262, 273 and
`dRatifiedSeam-2`; 212 stays OPEN.
OPEN.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
