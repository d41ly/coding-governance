---
slug: dSealedTally
node: d
opened: 2026-09-04
streams: tooling+deployer
roster: TOOL+DEPL
ids: DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1
authorized-by: prompt
---

# dSealedTally — drain the six findings dRatifiedSeam filed rather than folded

## The problem this build exists to solve

`dRatifiedSeam` closed with six confirmed findings filed instead of built, because each needed a
mechanism or a staged-RED arm that a fold at the end of an already-blocked build could not carry.
Four are in `govkit`'s `update` verb, which writes into a repository gov does not own: a landing that
sits outside the pass guarding against data loss, a rename map populated too late to be consulted, a
count predicate that cannot tell a swap from a rise, and a batched index read with no liveness on
git's exit code. One is in `govkit`'s own self-test, which refuses a vintage rather than grading a
tree. The last is in the unattended driver's terminal verb, which writes `LANDED` sixteen lines
before the check that refuses it.

## Expected improvements

- A landed source is verified and can be rolled back, like every other thing `update` writes.
- A rename destination is decided once, not classified as new because its row exited early.
- The tracked-path check grades paths rather than a total, and still passes a legal rename.
- A batched git read that fails says so instead of reporting every row absent.
- `govkit`'s self-test grades the tree it is handed, on a detached head as on a branch.
- A refused `--landed` leaves the phase alone, so no record claims a landing nothing observed.

## Detriments if this is not built

- `update` keeps a write path outside its own data-loss guard, in a foreign repository, which is
  exactly where the guard was built to matter.
- The dead-probe and could-not-fail classes stay live in the deployer, in a build whose predecessor
  spent its whole diff removing that shape from the same file.
- The bar cannot be run at a merge commit before pushing, which is where the merge protocol asks for
  it, so the run either skips a gate or learns to disbelieve one.
- The kit whose subject is the difference between an observation and a claim keeps a verb that
  records the success it refuses.

## Build-level rules

- **The unattended self-test suites are NOT to be run** — standing owner instruction, 2026-08-23,
  still in force. `TOOL-dSealedTally-1` is verified by a hermetic probe built from
  `unattended.test.sh`'s own setup, and its staged-RED arm is exercised the same way. If only a full
  suite run would settle something, the run says so and hands the owner the command.
- **`DEPL-dSealedTally-1` extends a seam rather than inventing one.** The verify-and-rollback pass
  was built by `DEPL-dCarriedReceipt-14`; its snapshot is row-keyed and `touched_kits` derives from
  it, which is precisely why a landed file is invisible to it.
- **`DEPL-dSealedTally-3` has a REJECTED obvious fix on the record.** `set(before) <= set(after)`
  reds on a legal rename, measured on `tools/demo/content.txt`. An assertion that fires on correct
  work is worse than the gap it closes.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `DEPL-dSealedTally-1` | 2 | landed sources join the verify-and-rollback pass |
| 2 | `DEPL-dSealedTally-2` | 2 | `rename_dests` is populated eagerly, before any row can exit |
| 3 | `DEPL-dSealedTally-3` | 1 | the tracked-path check grades paths, excusing renames and withdrawals |
| 4 | `DEPL-dSealedTally-4` | 2 | `index_read` asserts git's exit code instead of reading a failure as absence |
| 5 | `DEPL-dSealedTally-5` | 1 | the govkit self-test grades the tree, not the commit's ref-reachability |
| 6 | `TOOL-dSealedTally-1` | 2 | `--landed` writes its terminal phase after every check that can refuse it |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 6 unit(s) · node d · opened 2026-09-04 · streams tooling+deployer
ids DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dSealedTally-2 — `rename_dests` is populated eagerly, before any row can exit](spec/2026-09-04-spec-DEPL-dSealedTally-2.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [DEPL-dSealedTally-4 — `index_read` asserts git's exit code instead of reading failure as absence](spec/2026-09-04-spec-DEPL-dSealedTally-4.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-dSealedTally-1 — `--landed` writes its terminal phase after every check that can refuse it](spec/2026-09-04-spec-TOOL-dSealedTally-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [DEPL-dSealedTally-1 — landed sources join the verify-and-rollback pass](spec/2026-09-04-spec-DEPL-dSealedTally-1.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [DEPL-dSealedTally-3 — the tracked-path check grades paths, excusing renames and withdrawals](spec/2026-09-04-spec-DEPL-dSealedTally-3.md) | 2 | 1 | SPECCED | rev-1 | 2026-09-04 |
| [DEPL-dSealedTally-5 — the govkit self-test grades the tree, not the commit's ref-reachability](spec/2026-09-04-spec-DEPL-dSealedTally-5.md) | 3 | 1 | SPECCED | rev-1 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-dSealedTally-2`, `DEPL-dSealedTally-4`, `TOOL-dSealedTally-1` | yes |
| 2 | `DEPL-dSealedTally-1`, `DEPL-dSealedTally-3` | yes |
| 3 | `DEPL-dSealedTally-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
