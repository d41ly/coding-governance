# DEPL-dSealedTally-1 — landed sources join the verify-and-rollback pass

**Status:** CLOSED · rev-4 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-DEPL-dSealedTally-1-1-acceptance-ledger.md](../build/2026-09-04-build-DEPL-dSealedTally-1-1-acceptance-ledger.md) | journal | — |
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round1.md) | diff-review | DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round2.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round2.md) | diff-review | DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md) | spec-audit | DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md) | spec-audit | DEPL-dSealedTally-5 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round3.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round3.md) | spec-audit | DEPL-dSealedTally-5 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit update --write` can land a declared source the receipt has never named, and that write is
the only one in the verb that sits outside the pass which verifies the target afterwards and rolls
the target back when verification fails. Bring it inside, so every byte `update` writes into a
repository gov does not own is covered by the same guard.

## 2. Scope (IN)

- **S1** The write path ADDS a `derive_unclaimed_candidates(set())` call between
  `tools/govkit/govkit.py:6286` and the snapshot at 6319, and the function returns `(dest, eid)`
  PAIRS rather than bare dest paths, so `touched_kits` and `baseline` at 6347-6352 widen from it and
  a landed-only kit is baselined PRE-WRITE. The existing call at 6276 is NOT that source: it sits
  inside `if not write:` and the branch returns at 6285, so a `--write` run never reaches it. That
  call site is UPDATED to unpack the new shape, since it survives and still prints bare paths.
- **S2** The landing block SPLITS. Its decision-and-write half moves to sit above
  `written_paths = ...` at `tools/govkit/govkit.py:6806`, appending its `snap_rows` entries where
  the pass that reads them has not yet run. Its `unclaimed sources:` tally and per-path lines at
  7187-7195 STAY below the verify-and-rollback pass, so they render the POST-rollback `_landed_new`
  rather than a list the rollback is about to shorten.
- **S3** A landed entry is restorable. Its pre-state is `absent`, so the restore DELETES the file,
  removes its index entry, and removes the receipt row the landing minted at 7134.
- **S4** A landed destination is added to `written_paths`, so the closing tally does not classify it
  untouched, and a rolled-back landing is removed from `_landed_new` so the summary does not report
  a landing that was undone.
- **S5** The rollback of a landed file is contained by the same `demand_contained_dest` guard the
  existing rollback path calls, under a reason string naming the landing.
- **S6** A staged-RED arm in `tools/govkit/selftest.py`: a kit whose ONLY change is a landed source,
  with its `run_kit_check` forced to fail, leaves the target as it was and reaches its own rollback
  report rather than a traceback.
- **S7** The rollback report prints a landed entry under its own verb, `removed <path>`, never
  `restored` — a landed path had no index entry to restore. The order's "was restored to the index
  entry it had" sentence is conditioned on a non-landed entry being present, and BOTH of the
  report's empty-case fallbacks fire only when the `restored` list AND the new `removed` list are
  empty, so a run that removed something never prints "nothing to restore".

## 3. Non-goals (OUT)

- Not changing WHICH sources the landing block decides to land. `derive_unclaimed_candidates` and
  its four refusals are settled by `DEPL-dRatifiedSeam-1` and are not reopened here.
- Not moving the landing block's write half EARLIER than the write loop's end. It needs
  `withdrawn_rows`, which the write loop builds, so `tools/govkit/govkit.py:6806` is the earliest
  position available. The rev-1 non-goal said the block could not move at all and attributed the
  move to `DEPL-dSealedTally-2`; both were wrong and are deleted.
- Not adding a rollback for the receipt re-stamp. That is already outside this pass for every row
  kind and is not a regression this unit introduces.

## 4. Design

### Data model

`snap_rows` entries carry `kit`, `row`, `paths`, `fields` and `index`. A landed file has no receipt
row at snapshot time, so entries get an explicit `origin` key: `"table"` for every existing entry
and `"landed"` for the new ones, and the restore branch switches on it.

A landed entry's `row` key holds the receipt row the landing MINTS at
`tools/govkit/govkit.py:7134`, not a sentinel and not `None` — that is the object the restore must
remove from the receipt's file list, so it has to be reachable from the entry. Its `fields` is
empty and its `index` maps the destination to `None`, the marker the snapshot already uses for a
path with no index entry.

### Inventory

Four positions matter, and the block that has to split is why there are four rather than three.

| What | Line | When |
|---|---|---|
| `derive_unclaimed_candidates`, read-only preview | 6276 | inside `if not write:`, returns at 6285 |
| the SAME classifier, called on the write path | new, 6286-6319 | before the snapshot — supplies S1 |
| `snap_rows`, `touched_kits`, `baseline` | 6319-6352 | before the write loop |
| landing block's decision-and-write half, MOVED | to 6806 | after the write loop, before the pass |
| verify-and-rollback pass | 6806-6980 | reads `snap_rows` and `baseline` |
| landing block's `unclaimed sources:` tally, STAYS | 7187-7195 | after the pass — renders the final list |

The new call runs with an EMPTY withdrawal set, because `withdrawn_rows` does not exist that early.
For S1 the empty set is safe in the direction it errs: it can only NAME a kit that turns out not to
need a baseline, and baselining a kit the run does not touch costs one `run_kit_check` and grades
nothing wrongly. It cannot MISS a kit, which is the direction that would reintroduce the `KeyError`.

`baseline[eid]` at 6811 becomes `baseline.get(eid)` with a named refusal, so the next unit that
widens `touched_kits` gets a message rather than a `KeyError` inside a foreign repository.

### Migration

For `origin == "landed"` the restore branch DELETES rather than restores, and skips two things the
table branch does: the `ROLLBACK_FIELDS` restore, which would write receipt fields for a row that
should cease to exist, and the `withdrawn_rows` removal at 6924-6925, which is about rows the run
withdrew and has nothing to say about a row the run minted. It removes the minted row from the
receipt's file list in the same branch that deletes the file, and removes the destination from
`_landed_new`. No persisted shape changes: `snap_rows` is built per run and never stored.

### Rollout

One code path, no flag. The behaviour it adds is a rollback that previously did not happen, so
nothing that used to be restored stops being restored.

### Files touched (estimate)

`tools/govkit/govkit.py` (~95 lines: the `origin` key; the return-shape change and its surviving
preview consumer at 6276; the new write-path call; the landing block's SPLIT, write half to 6806 and
tally left at 7187; the restore branch; the `written_paths` and `_landed_new` updates; the report's
`removed` verb and its two empty-case fallbacks; the `baseline.get` refusal).

`tools/govkit/selftest.py` (~90 lines, one arm per criterion rather than a lump sum: the staged-RED
landed-only arm, the passing-check arm, the index assertion, the receipt-row assertion, the
`demand_contained_dest` monkeypatch recording its `where` argument, the report-text assertions for
`removed`/`restored`, the summary-and-tally assertion, and the preview-still-prints-a-bare-path arm).

### Alternatives rejected

Recomputing `touched_kits` AFTER the landing. Rejected on the mechanism rather than taste: a
baseline taken after the landing writes grades post-write state as the baseline, so `was == now`
holds for every landed-only kit and the rollback this unit exists to add is silently disabled. That
is a check that cannot fail, which is the class this build is draining.

Moving the landing block WHOLE to 6806, which is what rev-2 and rev-3 said. Rejected because the
block carries its own `unclaimed sources:` summary print, and moving that above the pass makes it
render a list the rollback is about to shorten — so S4's stated purpose would be unreachable by S2's
own instruction.

## 5. Production-readiness checklist

- security — the restore is a DELETE in a foreign repository, so it goes through
  `demand_contained_dest` exactly as the existing rollback does. No new escape surface.
- perf / scale — the snapshot grows by the number of landed files; the baseline may widen by kits
  the new call names and the run does not touch, bounded by the claimed kit set.
- a11y — N/A — a CLI verb with no rendered surface.
- i18n — N/A — operator-facing English strings.
- error / empty / loading states — a run that lands nothing adds no entries and behaves identically;
  the report's two empty-case fallbacks are covered by S7 so neither fires on a run that removed
  something.
- observability — the rollback report enumerates what it restored and, now, what it removed, under
  two distinct verbs so a deleted landing cannot read as a restored file.
- risks — data-loss is the whole subject. The mode being closed is a landed file surviving a failed
  verification. The mode being introduced is a DELETE, controlled by containment and by the
  `lexists` precondition that made the landing legal in the first place.
- testing + left-shift gates — S6's arm is the left-shift; it fails before the change. The
  `baseline.get` refusal is the second, aimed at the next widener rather than at this unit.
- migration / rollback — no persisted shape changes, so reverting the commit is the rollback.
- user docs — N/A — no user-facing page.

## 6. Acceptance criteria

- **AC1** — When a kit's only change is a landed source and its check is forced to fail, a
  `--write` run leaves the destination absent AND reaches its own rollback report rather than a
  traceback, proved by the new arm in `tools/govkit/selftest.py`.
- **AC2** — When that same `tools/govkit/selftest.py` fixture runs with its check PASSING, the
  landed file survives and is staged, so the rollback is not firing on success.
- **AC3** — When a landed file is rolled back, `git ls-files -s <dest>` in the target reports no
  entry, asserted by the AC1 arm alongside its `lexists` check.
- **AC4** — When a landed file is rolled back, the post-rollback receipt names no landed path,
  asserted against the receipt's file list in `tools/govkit/selftest.py`.
- **AC5** — When a landed entry is rolled back, `demand_contained_dest` is CALLED with the reason
  string S5 names, observed by an arm in `tools/govkit/selftest.py` that monkeypatches the guard to
  record its `where` argument. Deleting the call is not the observation: an arm built that way
  cannot fail for the right reason, because the landing refuses an escaping destination before
  anything is written, so the guard has no hostile input to catch.
- **AC6** — When the `snap_rows` append, or the `origin == "landed"` restore branch, is removed by
  mutation in a scratch copy of `tools/govkit/govkit.py`, the AC1 arm FAILS — two named mutation
  subjects, recorded as observed staged breaks rather than asserted.
- **AC7** — When the AC1 rollback completes, the run's `unclaimed sources:` summary lists no
  rolled-back destination and the closing tally does not report it untouched, asserted against the
  captured stdout in `tools/govkit/selftest.py`. This is what proves S4 and the S2 split together:
  a tally moved above the pass would still name the destination.
- **AC8** — When the AC1 rollback completes, the captured report contains `removed <dest>`, does NOT
  contain `restored <dest>`, omits the index-entry sentence when every rolled-back entry is landed,
  and contains no "nothing to restore" line.
- **AC9** — When `update` runs READ-ONLY after the return-shape change, its preview still prints a
  bare path per landed candidate, asserted in `tools/govkit/selftest.py` — the shape change must not
  leak a tuple into operator output.
- **AC10** — When `python tools/govkit/selftest.py` runs, it exits 0 and its arm count is at least 8
  greater than the count observed at the head of `order 2`, captured in §9 when this unit's pass
  opens rather than pinned to a constant four units share.

## 7. Gates

`govkit selftest` · `memory-hygiene` · `bash tools/run-gates/run-gates.sh` with
`GATE_FULL=1 GATE_SELFTESTS=1`, which is what a DoD owes for kit work.

## 8. Open questions

- **F1 — does a landed file's rollback also unstage it?** The landing calls `git add`, so a rollback
  that only unlinks leaves a staged path pointing at nothing. Options: `git rm --cached` the path,
  or `git reset -- <path>`. Recommendation: `git rm --cached`, because the file is being removed
  entirely and `reset` would restore an index entry from `HEAD` for a path `HEAD` does not carry.
  RESOLVED (agent, 2026-09-04, delegated): `git rm --cached`, per the recommendation — `reset` is
  wrong for a path with no `HEAD` entry, which is every landed file by construction. AC3 is what
  grades it; rev-1 resolved this fork and then observed nothing.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, grounded against `tools/govkit/govkit.py` at `0f19429a`.
- rev-2 · 2026-09-04 · folded the spec audit's B1, B2, H1, H6, H7, H8, H10, H5 and M1. B1: the
  landing block runs at 7013, after the pass at 6808 that was supposed to read its appends, so
  rev-1's mechanism could not deliver S1, S2 or S4 — the block moves to 6806 and the false §3
  non-goal is deleted. B2: a landed-only kit had no pre-write baseline; S1 widens `touched_kits`.
  H6, H7 and H8 add the `written_paths`, field-restore and receipt-row consequences. H10 rewrote
  AC5. H5 replaced the shared arm-count constant. M1 moved the order from 2 to 3.
- rev-3 · 2026-09-04 · folded round 2's B1, H1 and L1. B1: rev-2's own fix pointed at the
  `derive_unclaimed_candidates` call at 6276, which sits inside `if not write:` and returns at 6285.
  H1 made AC5 a monkeypatch observation. L1 added S7.
- rev-4 · 2026-09-04 · folded round 3, which came back with MORE blockers than round 2, so the
  subject is NON-CONVERGENT and this is the disposal fold — the loop stops here and every standing
  blocker is folded, per the build method. B1 was damage rev-3's own line-anchored edit did: it ate
  AC6's bullet head, leaving an orphan continuation under AC5 and destroying the unit's only
  staged-break criterion. AC6 is restored with two named mutation subjects. B2: moving the block
  WHOLE carries its `unclaimed sources:` print above the pass, so S4's purpose was unreachable by
  S2's own instruction — the block now SPLITS, and AC7 is what proves the split. H1 rejoined a
  bullet the same edit had cut in half and put S7 in its numbered place. H2, H3 and H4 added AC8,
  AC7 and AC9 for three scope items nothing graded. M1 and M2 corrected the `selftest.py` budget and
  cited the classifier by its definition at 6203 rather than by a dead call site. M3 extended S7 to
  both empty-case fallbacks. L1 restored a clause rev-3 had truncated.

## 10. Reuse audit

The seam is `tools/govkit/govkit.py`'s verify-and-rollback pass, built by
`DEPL-dCarriedReceipt-14` and cited by `python tools/codebase-map/reuse_lookup.py "verify and roll
back files a deploy wrote into a target repository"`, whose ranked candidates named
`target_context` and `check_target_reads_subject` in that same file. This unit EXTENDS that pass
rather than adding a second one.

It also reuses the classifier `derive_unclaimed_candidates`, DEFINED at
`tools/govkit/govkit.py:6203`, by adding a write-path call rather than deriving the landed set
twice. That reuse is not free: it costs a return-shape change, and the preview consumer at 6276 must
be updated to unpack it, which AC9 grades.

`memory/backlog/DEPL.md` carries `DEPL-dRatifiedSeam-2` as the row this unit closes, and no other
OPEN DEPL row names the rollback pass in `tools/govkit/govkit.py`.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
