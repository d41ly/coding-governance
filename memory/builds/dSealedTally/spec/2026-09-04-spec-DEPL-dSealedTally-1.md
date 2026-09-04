# DEPL-dSealedTally-1 — landed sources join the verify-and-rollback pass

**Status:** SPECCED · rev-1 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit update --write` can land a declared source the receipt has never named, and that write is
the only one in the verb that sits outside the pass which verifies the target afterwards and rolls
the target back when verification fails. Bring it inside, so every byte `update` writes into a
repository gov does not own is covered by the same guard.

## 2. Scope (IN)

- **S1** The landing block's writes are represented in `snap_rows`, so a kit whose only change is a
  landed file appears in `touched_kits` and therefore gets a baseline and an after-check.
- **S2** A landed file is restorable by the rollback pass. Its pre-state is `absent`, so the
  restore is a DELETE plus an index removal, not a byte restore.
- **S3** The rollback of a landed file is contained by the same `demand_contained_dest` guard the
  existing rollback path already calls, under a reason string naming the landing.
- **S4** A staged-RED arm in `tools/govkit/selftest.py` that fails before this change and passes
  after: a kit whose ONLY change is a landed source, with its `run_kit_check` forced to fail,
  leaves the target as it was.

## 3. Non-goals (OUT)

- Not changing WHICH sources the landing block decides to land. `derive_unclaimed_candidates` and
  its four refusals are settled by `DEPL-dRatifiedSeam-1` and are not reopened here.
- Not moving the landing block earlier in the verb. Its position after the table walk is what lets
  it consult `rename_dests` and `withdrawn_rows`; moving it is `DEPL-dSealedTally-2`'s subject.
- Not adding a rollback for the receipt re-stamp. That is already outside this pass for every row
  kind and is not a regression this unit introduces.

## 4. Design

### Data model

`snap_rows` entries carry `kit`, `row`, `paths`, `fields` and `index`. A landed file has no receipt
`row` — that is what makes it unclaimed — so the entry it needs is a fourth shape rather than a
fabricated table row. Add an explicit `origin` key: `"table"` for every existing entry and
`"landed"` for the new ones. The restore branch switches on it.

For a landed entry, `fields` is empty and `index` maps the destination to `None`, which the existing
code already spells as the marker `absent`. That is not a special case invented here: the snapshot
already stores `None` for a path with no index entry, and a landed destination is refused unless
`os.path.lexists` says the target does not hold it, so `absent` is its true pre-state.

### Migration

None. `snap_rows` is built per run and never persisted, so no receipt or on-disk shape changes.

### Rollout

One code path, no flag. The behaviour it adds is a rollback that previously did not happen, so the
default-OFF question does not arise: nothing that used to be restored stops being restored.

### Files touched (estimate)

`tools/govkit/govkit.py` (~35 lines: the `origin` key, the landing block appending its own
`snap_rows` entries, and the restore branch that deletes rather than restores).
`tools/govkit/selftest.py` (~45 lines: the staged-RED arm and its mutation control).

### Alternatives rejected

Running the landing block BEFORE the snapshot is built, so its writes are ordinary table rows. It
cannot work: the block consults `rename_dests` and `withdrawn_rows`, and both are products of the
walk the snapshot summarises. Rejected on ordering, not on taste.

## 5. Production-readiness checklist

- security — the restore is a DELETE in a foreign repository, so it goes through
  `demand_contained_dest` exactly as the existing rollback does. No new escape surface.
- perf / scale — the snapshot grows by the number of landed files, typically zero and bounded by
  the declared destination set. No new subprocess calls.
- a11y — N/A — a CLI verb with no rendered surface.
- i18n — N/A — operator-facing English strings, consistent with the rest of the verb.
- error / empty / loading states — a run that lands nothing adds no entries and behaves identically.
- observability — the rollback report already enumerates what it restored; a deleted landing is
  reported in the same list, distinguished by its origin.
- risks — data-loss is the whole subject. The failure mode being closed is a landed file that
  survives a failed verification. The mode being introduced is a DELETE, so containment and the
  `lexists` precondition are the controls.
- testing + left-shift gates — S4's arm is the left-shift; it fails before the change.
- migration / rollback — no persisted shape changes, so reverting the commit is the rollback.
- user docs — N/A — no user-facing page; the verb's own docstring carries the behaviour.

## 6. Acceptance criteria

- **AC1** — When a kit's only change is a landed source and its check is forced to fail, a
  `--write` run leaves the destination absent, proved by the new arm in `tools/govkit/selftest.py`.
- **AC2** — When that same `tools/govkit/selftest.py` fixture runs with its check PASSING, the landed file survives and is
  staged, so the rollback is not firing on success.
- **AC3** — When the change is reverted in a scratch copy, the AC1 arm FAILS, recorded as a staged
  break rather than asserted; the mutation is the removal of the `snap_rows` append.
- **AC4** — When a rollback restores a landed file, the path passes through
  `demand_contained_dest`, proved by an arm giving the landing a destination outside the target.
- **AC5** — When `python tools/govkit/selftest.py` runs, its arm count is strictly greater than the
  1074 it reports at base `0f19429a`.

## 7. Gates

`govkit selftest` · `memory-hygiene` · `bash tools/run-gates/run-gates.sh` with
`GATE_FULL=1 GATE_SELFTESTS=1`, which is what a DoD owes for kit work.

## 8. Open questions

- **F1 — does a landed file's rollback also unstage it?** The landing calls `git add`, so a rollback
  that only unlinks leaves a staged path pointing at nothing. Options: `git rm --cached` the path,
  or `git reset -- <path>`. Recommendation: `git rm --cached`, because the file is being removed
  entirely and `reset` would restore an index entry from `HEAD` for a path `HEAD` does not carry.
  RESOLVED (agent, 2026-09-04, delegated): `git rm --cached`, per the recommendation — `reset` is
  wrong for a path with no `HEAD` entry, which is every landed file by construction.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, grounded against `tools/govkit/govkit.py` at `0f19429a`.

## 10. Reuse audit

The seam is `tools/govkit/govkit.py`'s verify-and-rollback pass, built by
`DEPL-dCarriedReceipt-14` and cited by `python tools/codebase-map/reuse_lookup.py "verify and roll
back files a deploy wrote into a target repository"`, whose ranked candidates named
`target_context` and `check_target_reads_subject` in that same file. This unit EXTENDS that pass
rather than adding a second one: its snapshot is row-keyed, which is exactly why a landed file is
invisible to it, so the fix is a new entry shape in the existing structure.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
