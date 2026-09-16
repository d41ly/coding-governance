# DEPL-dBackdatedFixture-2 — the `[dGV-9]` version-refresh arms grade only the rows the write refreshed

**Status:** OPEN · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-review-DEPL-dBackdatedFixture-2-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-dBackdatedFixture-2-spec-audit-round1.md) | spec-audit | DEPL-dBackdatedFixture-3 |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-dGaugedVintage-9` S1 wrote three `[dGV-9]` arms at `tools/govkit/selftest.py:705-722`. They catch
`update --write` moving a row to new bytes without refreshing its `version`. Under
`DEPL-dBackdatedFixture-1` the `verrefresh` fixture no longer carries `tools/check-wiring.fragment.json`,
so `update --write` lands that file as a NEW row carrying a freshly resolved `version`. That row never
held the sentinel, so it satisfies all three predicates by itself. The arms then pass with the refresh
they guard deleted. This unit scopes the population to the rows the receipt held before the write, and
proves the scoping excludes something. It is round 1's BLOCKER B1, promoted.

## 2. Scope (IN)

- **S1** — `_moved` holds only receipt rows whose `path` was in the receipt before `update --write` and
  whose `version` is no longer `STALE-SENTINEL`. Observed by AC1.
- **S2** — A `[dBF]` liveness arm asserts the write ADDED at least one row whose path was not held
  before, so the S1 scoping excludes a real row rather than nothing. Observed by AC2.
- **S3** — The third `[dGV-9]` arm, `all(commit and sha256)` over `_moved`, also requires `_moved` to be
  non-empty, so it cannot pass vacuously. Observed by AC3.
- **S4** — The three `[dGV-9]` labels are unchanged, and two of them are among the 30 red at
  `4cf0944d`. Observed by AC1.

## 3. Non-goals (OUT)

- No change to `tools/govkit/govkit.py`, including the three `row["version"] = _resolve_ver_at(row)`
  writes at `govkit.py:6814`, `6950` and `7069`.
- No new arm for the other two `version` writes. The `verrefresh` fixture takes the raw-write branch at
  `govkit.py:6814`; the three-way and rename branches are graded elsewhere or not at all, and closing
  that is not this unit.
- No change to the unclaimed-source landing that creates the added row. It is DEPL-dRatifiedSeam-1 S3.

### Edges

- **consumes-from** `DEPL-dBackdatedFixture-1` — the fixture that drops the fragment row, without which no row is added and S2 has nothing to find.

## 4. Design

### Data model

In the `verrefresh` block, after the sentinel loop and before `update --write`, record
`_held = {f["path"] for f in rec["files"]}`. After the write, read the receipt once and compute
`_moved = [f for f in files if f["path"] in _held and f.get("version") != "STALE-SENTINEL"]` and
`_added = [f for f in files if f["path"] not in _held]`. The existing three arms keep their labels
and predicates, grading the scoped `_moved`; the third gains `len(_moved) > 0 and`. One new arm:
`[dBF] LIVENESS the write ADDED a row the sentinel never touched, so the scoping excludes something`,
asserting `len(_added) > 0`, with the added paths in its detail.

### Inventory

No new function. One new arm label, prefixed `[dBF]`.

### Files touched (estimate)

`tools/govkit/selftest.py` only, the `verrefresh` block. About 12 lines added and 4 changed.

### Alternatives rejected

- **Exclude by the fragment's path literal.** Rejected: it names today's added file, so the next file a
  kit gains reopens the hole. Scoping by the pre-write path set covers any added row.
- **Stamp the sentinel after the write as well.** Rejected: it would grade a row the write never had
  to refresh, which is the same disarming from the other side.

## 5. Production-readiness checklist

- security — N/A — a test arm; no product write path changes.
- perf / scale — N/A — one extra set built from rows already read.
- error / empty / loading states — S2 and S3 are the empty-population guards.
- observability — the liveness arm prints the added paths, so a red names what the write did or did
  not add.
- risks — S2 reds if `update --write` over `verrefresh` ever lands nothing new, for instance once
  `check-wiring` stops shipping a file `24f39915` lacked. That red is the fixture reporting that it no
  longer exercises the scoping, which is the intent.
- testing — AC1's staged break is the real regression the arms guard, not a synthetic value.
- migration — N/A — no receipt schema, data or adopter change.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `update --write` runs over the `verrefresh` fixture with the `version` refresh at
  `govkit.py:6814` intact, the first two `[dGV-9]` arms read `ok`. With that line deleted, both read
  `FAIL` while the added row is still present in `install.json`.
  Red when: `_moved` admits a row the receipt did not hold before the write.
- **AC2** — When `update --write` runs over the `verrefresh` fixture, the `[dBF]` liveness arm reads
  `ok` and its detail names `tools/check-wiring.fragment.json`, and under AC1's staged break it still
  reads `ok`.
  Red when: the write adds no row, or the arm is computed from `_moved` instead of the pre-write set.
- **AC3** — When `_moved` is empty, the third `[dGV-9]` arm reads `FAIL`. AC1's staged break empties
  it, because both held rows keep the sentinel, so under that break all three `[dGV-9]` arms read `FAIL`
  while the AC2 liveness arm reads `ok`.
  Red when: the `len(_moved) > 0` guard is removed, and the third arm reads `ok` over an empty `_moved`.

## 7. Gates

`govkit selftest` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · `[dGV-9]` scoping and `[dBF]` liveness, staged RED by deleting the `version` refresh at `govkit.py:6814` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · promoted from spec audit round 1's BLOCKER B1 on `DEPL-dBackdatedFixture-1`,
  carrying rev-2's S4 and AC5 of that spec.

## 10. Reuse audit

Probe result: no existing seam fits beyond the arms themselves. The seam extended is the `verrefresh`
block at `tools/govkit/selftest.py:705-722`, `DEPL-dGaugedVintage-9` S1's arms, and the
`[dGV-9]` ledger at
`memory/builds/dGaugedVintage/build/2026-09-01-build-DEPL-dGaugedVintage-9-acceptance-ledger.md` is its
record. `reuse_lookup.py` does not index closures inside `main()`, so it cannot rank this block.

Recall terms used: `--terms "gov_oid S9 receipt integrity refusal stale_target fixture older vintage
rewind blob_at selftest update"`, the query recorded in `DEPL-dBackdatedFixture-1` §10, which returned
`DEPL-dGaugedVintage-8` and its sibling ledgers.
