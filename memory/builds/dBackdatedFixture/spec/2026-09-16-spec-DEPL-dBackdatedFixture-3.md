# DEPL-dBackdatedFixture-3 — the `u5a` check arms take their expected figures from the descriptor

**Status:** INPROGRESS · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-DEPL-dBackdatedFixture-1-acceptance-ledger.md](../build/2026-09-16-build-DEPL-dBackdatedFixture-1-acceptance-ledger.md) | journal | DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 |
| [2026-09-16-review-DEPL-dBackdatedFixture-1-closing-diff-round1.md](../reviews/2026-09-16-review-DEPL-dBackdatedFixture-1-closing-diff-round1.md) | diff-review | DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 |
| [2026-09-16-review-DEPL-dBackdatedFixture-1-closing-diff-round2.md](../reviews/2026-09-16-review-DEPL-dBackdatedFixture-1-closing-diff-round2.md) | diff-review | DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 |
| [2026-09-16-review-DEPL-dBackdatedFixture-2-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-dBackdatedFixture-2-spec-audit-round1.md) | spec-audit | DEPL-dBackdatedFixture-2 |

<!-- /gen:spec-records -->

## 1. Goal

Three `govkit check` arms at `tools/govkit/selftest.py:947-952` assert `integrity: 2/2`,
`provenance: 2/2` and `sidecar: 2 line(s) compared against 2 hashed row(s)` over a clean `check-wiring`
install. `TOOL-aReplayedCard-2` gave that kit a third file, so `check` now prints `3/3` and the three
labels are red at `4cf0944d`. The first label says "a DERIVED integrity count" and types the number. The
fix must not derive it from the receipt or `install.sums`: those are what `check` reads, so a receipt
that loses a row would move both sides together. `DEPL-aTetheredConvoy-5` S11 already states the
contract: the expectation comes from the descriptors. It is round 1's HIGH H1, promoted.

## 2. Scope (IN)

- **S1** — The expected figures come from `resolve_entry(govroot, desc, canonical_ctx("check-wiring"))`
  over `tools/govkit/entries/check-wiring.kit.toml`, read once before the three arms. N is the count of
  its `writes` whose role is `engine`; P is the count of those with a `src`; H is the count of all
  `writes` with a `src`. Observed by AC1.
- **S2** — Each arm asserts its figure is non-zero and appears in `check`'s stdout in the shape `check`
  prints: `integrity: N/N`, `provenance: P/P`, `sidecar: H line(s) compared against H hashed row(s)`.
  The arm labels are unchanged. The shape is observed by AC1, AC2, AC3 and AC4. The non-zero floor is
  NOT OBSERVED: every criterion runs with N = P = H = 3, and a zero needs a descriptor that ships no
  file, which no break here constructs. It stays as a guard against a vacuous `N/N` of `0/0`.
- **S3** — No literal count remains in the three arms. Observed by AC1.
- **S4** — When this unit and `DEPL-dBackdatedFixture-1` are built, the suite's closing line reads
  `govkit-selftest: all arms held`. Observed by AC5.

## 3. Non-goals (OUT)

- No change to `check`'s loops in `tools/govkit/govkit.py:3066-3157`.
- No change to the `[-8]` AC3 arm's `provenance: 2/2 resolved`. Its population is frozen at the
  historic vintage `372e6b2a`, which `DEPL-dBackdatedFixture-1` §4 records.
- No guard against a defect inside `resolve_entry` itself. `apply` plans through the same expansion, so
  such a defect moves the expectation and the install together. §5 names that gap.

### Edges

- **consumes-from** `DEPL-dBackdatedFixture-1` — the 27 fixture labels, without which the closing line in S4 cannot read `all arms held`.

## 4. Design

### Data model

Before the `u5a` arms, `_gk = govkit_module()`, `_cw = _gk.load_toml(govroot / "tools" / "govkit" /
"entries" / "check-wiring.kit.toml")`, and `_w = _gk.resolve_entry(govroot, _cw,
_gk.canonical_ctx("check-wiring"))["writes"]`. Then `N`, `P` and `H` are counted from `_w.values()` as
S1 states. Measured on `4cf0944d`: three writes, all `engine`, all with a `src`, so N = P = H = 3 there.
That figure is DERIVED at every run and is written here only as the observation that chose the design.

The descriptor is read from the gov checkout under test, whose tree `apply` also installed from, so the
expectation and the install describe the same bytes.

### Inventory

No new function. No new arm label.

### Files touched (estimate)

`tools/govkit/selftest.py` only, the `u5a` block. About 12 lines added and 6 changed.

### Alternatives rejected

- **Derive from the receipt, the target's files and `install.sums`** (rev-2 of
  `DEPL-dBackdatedFixture-1` before the audit). Rejected by audit finding H1: those are `check`'s own
  inputs, the `memory/gotchas/assertion-between-two-derived-values.md` class.
- **Read the descriptor's literal `claims` list.** Rejected: `claims` may hold globs in other kits and is
  graded against `resolve_entry` by selfcheck rule 4b anyway, so it is a second spelling of one answer.
- **Keep a literal and bump it to 3.** Rejected: it breaks again the next time the kit gains a file.

## 5. Production-readiness checklist

- security — N/A — a test arm; no product write path changes.
- perf / scale — N/A — one descriptor read and one in-process expansion.
- error / empty / loading states — each figure carries a non-zero floor, unobserved, as S2 states.
- observability — each arm's detail stays `check`'s full stdout, which prints all three figures.
- risks — a defect in `resolve_entry` moves the expectation with the install and is not caught here;
  selfcheck's own descriptor arms are where that lives.
- testing — three staged breaks, one per axis, named in §7.
- migration — N/A — no receipt schema, data or adopter change.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `govkit.py check` runs over the clean `u5a` install, all three arms read `ok`, and
  their expected figures are counted from `resolve_entry` with no literal number in the predicates.
  Red when: an arm's expectation is read from `install.json` or `install.sums`, which AC4's break
  exposes.
- **AC2** — When `check`'s engine-row loop in `govkit.py` skips the fragment row, the integrity and
  provenance arms read `FAIL` and the sidecar arm still reads `ok`.
  Red when: those two arms stay green with `check` counting one row fewer than the descriptor ships.
- **AC3** — When `check`'s sidecar block in `govkit.py` drops one parsed `install.sums` line, the
  sidecar arm reads `FAIL`.
  Red when: the sidecar arm stays green with `check` reading one line fewer than the descriptor ships.
- **AC4** — When the `u5a` fixture's receipt loses one row, together with its `install.sums` line and
  its file in the index and worktree, before `check` runs, all three arms read `FAIL`.
  Red when: any of them stays green, which is the receipt-derived design H1 rejected.
- **AC5** — When the unit is built, the three `u5a` labels among the 30 red at `4cf0944d` read `ok`,
  and the suite's closing line is `govkit-selftest: all arms held`.
  Red when: any label still fails.
  cost: one full suite run of about seven minutes, shared with `DEPL-dBackdatedFixture-1` AC4.

## 7. Gates

`govkit selftest` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · `u5a` integrity and provenance arms, staged RED by skipping the fragment row in `check`'s engine-row loop · none
New arm: tools/govkit/selftest.py · `u5a` sidecar arm, staged RED by dropping one parsed line in `check`'s sidecar block · none
New arm: tools/govkit/selftest.py · all three `u5a` arms, staged RED by removing one row, its sums line and its file from the fixture before `check` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · promoted from spec audit round 1's HIGH H1 on `DEPL-dBackdatedFixture-1`, with
  that record's M1 fold: one staged break per figure plus a receipt-shrink break.
- rev-2 · 2026-09-16 · S2 · §5 · folded spec audit round 1 of units 2 and 3 (CLEAN WITH FIXES). L1:
  the non-zero floor is marked NOT OBSERVED, since every criterion runs with a figure of 3.

## 10. Reuse audit

Probe result: the seam is `resolve_entry` in `tools/govkit/govkit.py:284`, already called from the
suite with `canonical_ctx` at `tools/govkit/selftest.py:511`. `reuse_lookup.py` does not index the
suite's closures, so the citation comes from `grep -n resolve_entry` over it. The contract is
`DEPL-aTetheredConvoy-5` S11 in
`memory/builds/aTetheredConvoy/spec/2026-08-16-spec-DEPL-aTetheredConvoy-5.md`.

Recall terms used: `--terms "gov_oid S9 receipt integrity refusal stale_target fixture older vintage
rewind blob_at selftest update"`, the query recorded in `DEPL-dBackdatedFixture-1` §10; the S11 contract
was located from the audit record rather than that query.
