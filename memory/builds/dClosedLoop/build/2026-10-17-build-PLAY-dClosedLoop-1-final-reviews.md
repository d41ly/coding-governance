# The folds' closing review, and the systems and retrofit audit

**Serves:** research PLAY-dClosedLoop-1

The owner asked for two reviews once the debt round's folds and the systems and retrofit fold had landed.
This record holds their runs, and their folds once they return. The args, and the script that wrote them,
are in `build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md`.

## [words] The owner's words, 2026-10-17

> delete the duplicate artifact first, then do both the closing review of the folds and a tier-2 review of the systems and retrofit rounds.

## [runs] The two runs

| Dispatch | Review | Kind | Subject | Round | Report |
|---|---|---|---|---|---|
| 85 | the closing review of the folds | diff review, full | `9b188202a..cdcea2c9b`, without the review reports, the session log and the generated files | 1 | `reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md` |
| 86 | the systems and retrofit rounds | spec audit, full | the systems record at blob `9335a3533` and the retrofit record at blob `cec90968d` | 1 | `reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md` |

## [method] How they run

- **The duplicate artifact first.** The delete of `4UyRaoozVkbK6ECCCBvDg1` needs the owner's confirmation,
  which this session cannot show, so nothing was deleted. The owner deletes it from the artifact's own menu.
- **One at a time.** Each run reaches five agents at once, the review protocol's bound, so dispatch 86
  goes once dispatch 85 returns.
- **Efforts.** Each run takes what `handoff.py stage-efforts` prints for its workflow: the closing review
  runs at high at every stage, and the spec audit at medium.
- **Full intensity.** The closing review runs all five diff lenses, security and intent among them, since
  the folds change the dispatcher's binding, the release hold and the adopter sandbox. A spec audit runs
  only the full set.
- **The closing review's subject** is every commit since the debt round's twelfth review returned: the six
  pairs' folds, the two folds' owed fixes, and the systems and retrofit fold into v2. The comparison
  record's maps and each fold section are its statement of intent. It is round 1, since no review read the
  folds, and the twelve runs' findings are not handed in as a prior set: each map row names the fix to
  check.
- **The spec audit's opt-in.** As for dispatches 61 to 64, the README's `spec-audit:` line is set aside and
  `.unattended.conf` dates `SPEC_AUDIT_DEFAULT` around the audit's dispatch call, in the working tree only.
  Both are restored once the call is admitted, and neither change is committed.

- **What dispatch 86 read** (recorded 2026-10-17, once it returned). Dispatch 86 went once dispatch
  85's return was recorded, and the fold of 85 was written while it ran. The fold wrote both subjects at
  11:44:56Z: a three-line re-run note in the systems record, and the retrofit record's offered-update
  bullet and its dTotalRecall owners row. Each of the five finders read the subjects between 11:35:42Z
  and 11:42:28Z, before that write. Each of the five skeptics found both subjects moved with `git
  hash-object`, and read the pinned blobs from git. So the audit covers the pinned text, and the fold's
  lines in the two subjects are 85's fold text, unreviewed like every fold. The timing probe and its
  output are in the final instruments' `[read-86]`.

## [fold-debt-folds] Dispatch 85's findings, folded 2026-10-17

The folds' closing review returned CLEAN WITH FIXES, 22 of 27 findings confirmed in 20 items
(`reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md`). Ids 9, 15, 16, 17, 20 were refuted. Each item went
here, and each row's classes are its confirmed findings' own, from the ledger:

| Item | Ids | Disposition | Where the fix sits | Its classes |
|---|---|---|---|---|
| H1 | 1 | fork, asked as RT-4 | layer-runtime `[act]`'s decision by binding, once the owner answers | — |
| M1 | 7, 14 | amend | flow-steps' `review.pin`; review-system `[lenses]`; v2's dFairHearing row | — |
| M2 | 8, 25 | amend | v2's dTotalRecall row | — |
| M3 | 2 | amend | layer-runtime `[supervise]`'s fencing, `named-acts` and the `fencing` fixture | — |
| M4 | 3 | amend | layer-runtime `[enforce]`'s preflight population and the `fail-closed` plugin arm | — |
| M5 | 6 | amend | flow-steps' closing review | — |
| M6 | 10 | amend | layer-runtime `[decide]`'s `awaiting` row and the `next` arm | `route-names-an-output-its-actor-never-emits` |
| M7 | 11 | amend | layer-expansions' `kits.offer`; `gap-deploy-13`; retrofit `[seed]`; v2's dShippedRelease row; the foreign-code class's fixture | `foreign-code-runs-on-the-ambient-credential` |
| M8 | 12 | amend | v2's dOrderedCharter row; layer-memory `[names]`; layer-library `[consult]` | `retirement-inventory-misses-readers-by-value` |
| M9 | 13 | amend | the both-runs probe revised in `[probes-final]`; the systems record's re-run; the one-run class | — |
| M10 | 18 | amend | the target-spawn probe's failing arm in `[probes-final]`; `kits.offer`; the foreign-code class | — |
| M11 | 22 | amend | flow-steps' `build.unit-pass` | — |
| M12 | 23 | amend | layer-roles `[matrix]`' counts and its run of 2026-10-17 | — |
| M13 | 24 | amend | review-system `[lenses]`' scorer; v2's dFairHearing row | — |
| M14 | 26 | amend | v2's dTotalRecall row; retrofit `[owners]` | — |
| L1 | 4 | amend | as M12 | — |
| L2 | 5 | amend | layer-runtime's two rows indented; the table-shape probe in `[probes-final]`; the pipe class | — |
| L3 | 19 | amend | `gap-design-05`; the reuse-token probe in `[probes-final]` | — |
| L4 | 21 | amend | the debt record's `[fold-fold-round3]` row; the layers record's `[folded]` and its tally script | — |
| L5 | 27 | amend | v2's dRankedPlan row | — |

- **The one fork.** H1 changes what the runtime design promised for attended sessions, and it rests on
  RT-2 and on the owner's ruling that auto mode stays, so it goes to the owner as RT-4.
- **What M10's probe found beyond the item.** Its revision reads git calls in the target too. Update's git
  writes there fire the target's own hooks, a seventh kind of target-side code today, and `kits.offer`
  now runs git there with `core.hooksPath` pointed at an empty directory.
- **The fold is unreviewed text,** like every fold before it.

## [fold-systems-retrofit] Dispatch 86's findings, folded 2026-10-17

The systems and retrofit audit returned CLEAN WITH FIXES, 62 of 67 findings confirmed in 52 items
(`reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`). Ids 21, 29, 55, 56, 63 were refuted. Every item
was amended, and none changes an owner's answer. Each row's classes are its confirmed findings' own,
from the ledger, beside the class this fold assigns:

| Item | Ids | Disposition | Where the fix sits | Its classes |
|---|---|---|---|---|
| H1 | 17 | amend | retrofit `[ledger]`'s directions and `[owners]`; v2's dWitnessedBar; `[probes-86]`'s registry probe | `ratchet-migration-ignores-how-each-source-grows` |
| H2 | 18 | amend | systems `[design-memory-structure]`'s acceptance and reads outside; `[ms2]` and `[ms2-instrument]`'s third run; v2's dTotalRecall | `criterion-asserts-what-its-own-command-cannot-show` |
| H3 | 27 | amend | retrofit `[seed]`'s seed-if-absent, `[ratchet]`'s `seed laundering` row, `[placement]` | `reseed-at-a-later-sha-launders-the-base` |
| H4 | 28 | amend | retrofit `[ledger]`'s home and `[agreement]`; v2's dWitnessedBar | `shipped-checker-edit-is-an-adopter-contract-change` |
| H5 | 57 | amend | retrofit `[seed]`'s failed seed, `[ratchet]`'s `populated` and `unarmed` rows; flow-steps `[adopt]` | `vacuous-selector-empty-population` |
| M1 | 1, 51 | amend | systems `[cross]`'s budget per slot and the item-budget check; v2's P27 and `memory.over-budget`; layer-roles' route-back; retrofit `[cross]` | `two-answers-to-one-question` |
| M2 | 2 | amend | v2's `[chain]` parents; retrofit `[owners]`' order, `[ratchet]` and `[drain]`'s slot states | `spec-names-code-its-base-lacks` |
| M3 | 3, 48 | amend | retrofit `[owners]`, `[progress]`, `[origin]` and `[seed]`; flow-steps `[adopt]`; v2's dTotalRecall and dShippedRelease; the role matrix's revision | — |
| M4 | 4 | amend | systems `[design-annotations]`' budget and `[design-tags]`' positional references; retrofit `[cross]` | `two-answers-to-one-question` |
| M5 | 5 | amend | retrofit `[cross]`' annotations and `[agreement]` | — |
| M6 | 6 | amend | retrofit `[drain]`'s touch join and `[ratchet]`; v2's dScopedBuild and `build.scope`; flow-steps' `build.scope` | `two-answers-to-one-question` |
| M7 | 7 | amend | v2's dScopedBuild | `fold-text-is-unreviewed-surface` |
| M8 | 8, 34 | amend | systems `[design-annotations]`' delivery, checks and keys; `[agree-annotations]` | `amendment-leaves-its-other-half-standing` |
| M9 | 9 | amend | systems `[design-role-shapes]`' metric, checks and owners; v2's dWellOiledMachine and dCalibratedLens | `route-names-an-output-its-actor-never-emits` |
| M10 | 10, 49 | amend | systems `[design-tags]`' owners; v2's dOrderedCharter, dDeclaredLoop, dWitnessedBar, dWellOiledMachine and dTotalRecall | — |
| M11 | 11 | amend | retrofit `[ratchet]`'s untouched-quiet row and `[origin]` | `fixture-passes-by-finding-nothing` |
| M12 | 12 | amend | systems `[design-memory-structure]`' default load and the auto-memory check; v2's dTotalRecall | `rule-stated-with-no-check-that-fails` |
| M13 | 16, 62 | amend | retrofit `[ratchet]`'s base and merge row, `[drain]`'s range; v2's dWitnessedBar and dScopedBuild | `a-merge-of-the-default-branch-read-as-additions` |
| M14 | 19 | amend | retrofit `[ledger]`'s readers | `retirement-inventory-misses-readers-by-value` |
| M15 | 20, 50 | amend | systems `[answers]`' AN-2, revised | — |
| M16 | 22, 44 | amend | retrofit `[ledger]`'s classes and scalar rule; v2's dMindYourWords; `[probes-86]`'s census | `predicate-designed-without-a-run-over-the-tree` |
| M17 | 23, 64 | amend | systems `[cross]`' index and the freshness check; v2's dOrderedCharter | — |
| M18 | 26, 43 | amend | systems `[design-role-shapes]`' registry; v2's dBoundRoles | — |
| M19 | 30 | amend | retrofit `[ledger]`'s extensions | — |
| M20 | 31, 60 | amend | retrofit `[ledger]`'s classes; `[probes-86]`'s census | `zero-witness-over-an-unnamed-population` |
| M21 | 32 | amend | retrofit `[drain]`'s claims; v2's dScopedBuild | — |
| M22 | 35 | amend | retrofit `[cadence]` and `[never]`; v2's dTendedCadence | `amendment-leaves-its-other-half-standing` |
| M23 | 36 | amend | retrofit `[ledger]`'s deferrals and `[seed]`'s declined candidate; flow-steps `[adopt]` | `owner-item-without-its-reject-outcome` |
| M24 | 38 | amend | retrofit `[ledger]`'s home and `[owners]`; v2's dWitnessedBar | `shipped-checker-edit-is-an-adopter-contract-change` |
| M25 | 40 | amend | retrofit `[cross]` and `[practices]`; v2's `annotations.grammar` | — |
| M26 | 41 | amend | systems `[design-tags]`' leg name and shape check; v2's dWitnessedBar | `a-spelling-change-strands-its-readers`, `predicate-designed-without-a-run-over-the-tree` |
| M27 | 42 | amend | systems `[design-instruction-writing]`' renderers; v2's dOrderedCharter and dConvergedCharter | — |
| M28 | 45 | amend | retrofit `[ledger]`'s merge and `[ratchet]`'s merge row; v2's dWitnessedBar | `merge-keeps-both-sides-of-one-derivation` |
| M29 | 46 | amend | systems `[design-instruction-writing]`' checks; v2's catalogue row and the strict preset | `policy-value-with-no-route` |
| M30 | 47 | amend | retrofit `[seed]`, `[drain]`, `[keys]` and `[never]`; systems `[design-tags]`' resolves; v2's catalogue rows | `policy-value-with-no-route` |
| M31 | 52 | amend | v2's dOrderedCharter | `fold-text-is-unreviewed-surface` |
| M32 | 58 | amend | retrofit `[placement]`, `[seed]` and `[practices]`; v2's dShippedRelease | `foreign-code-runs-on-the-ambient-credential` |
| M33 | 59 | amend | systems `[design-annotations]`' markers and checks; v2's dTotalRecall; `[probes-86]`'s census | `predicate-designed-without-a-run-over-the-tree` |
| M34 | 61 | amend | retrofit `[ledger]`'s rename and `[ratchet]`'s rename row | `path-keyed-row-strands-on-a-rename` |
| M35 | 65 | amend | systems `[design-memory-structure]`' sections and keys check | `predicate-designed-without-a-run-over-the-tree` |
| M36 | 66 | amend | retrofit `[drain]`'s cost, `[cadence]` and `[seed]`'s adopter drain load | `rate-quoted-without-its-denominator` |
| L1 | 13 | amend | as M31 | — |
| L2 | 14 | amend | systems `[ms2]` | `two-answers-to-one-question` |
| L3 | 15 | amend | systems `[cross]`, `[agree-memory-structure]` and the freshness check | — |
| L4 | 24 | amend | retrofit `[drain]`'s cost | — |
| L5 | 25 | amend | systems `[design-memory-structure]`' keys; v2's catalogue row | — |
| L6 | 33 | amend | systems `[design-role-shapes]`' metric; flow-steps' `review.cost` | — |
| L7 | 37 | amend | systems `[design-instruction-writing]`' unit status; v2's dOrderedCharter | — |
| L8 | 39 | amend | retrofit `[ledger]`'s extensions | — |
| L9 | 53 | amend | as M8 | — |
| L10 | 54 | amend | systems `[design-instruction-writing]`' templates; v2's dConvergedCharter | — |
| L11 | 67 | amend | systems `[design-memory-structure]`' verbs; v2's dTotalRecall | — |

- **Two design calls the fold made, neither an owner's answer:**
  - **H4's home.** Each population stays where its check keeps it. The first design moved every one to
    `memory/<layer>/baseline/`, which check 3 refuses, and the move would have stranded M14's and M24's
    readers.
  - **M2's order.** dTotalRecall and dBoundRoles follow dWitnessedBar, and dShippedRelease follows
    dTotalRecall, so each consumer descends from its producer.
- **MS-2 goes back to the owner.**
  - H2's corrected measure counts shell reads, which carry 59.5% of today's memory bytes.
  - Under that measure, three roles' medians are over the 96 KB the owner chose. The owner chose it
    from a table whose every median sat under the cap.
  - It is asked beside dispatch 85's RT-4.
- **The role matrix's instrument was revised** to read flow-steps' new `[adopt]` group (M3). The
  revision before it reds on each new item. The new revision reads 81 items clean, and its planted arms
  still red (layer-roles `[instrument]`).
- **Four new bug classes,** claimed by the build-method dossier:
  - `ratchet-migration-ignores-how-each-source-grows`;
  - `reseed-at-a-later-sha-launders-the-base`;
  - `predicate-designed-without-a-run-over-the-tree`, which four items share;
  - `path-keyed-row-strands-on-a-rename`.
- **The fold is unreviewed text,** like every fold before it.
