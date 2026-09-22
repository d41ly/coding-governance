# DEPL-dGaugedVintage-12 — the prefix ratchet records identity, not only a count

**Status:** CLOSED · rev-2 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 8 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-12-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-12-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-dGaugedVintage-7` made `tools/check-install-prefix.sh` count occurrences instead of hit lines,
which closed one blind spot and left the other: the ledger records HOW MANY root-prefix literals a
shipped file carries and never WHICH kits they name, so exchanging one kit's path for another's holds
the count level and passes.

## 2. Scope (IN)

- **S1** — The emitter records the sorted, de-duplicated set of kit names each file's occurrences
  refer to, as a THIRD tab-separated field on the existing row: `<path>\t<count>\t<kits>`.
- **S2** — The comparison asserts that field. A file whose count is unchanged while its kit set moves
  reds, naming both sets.
- **S3** — The ledger is re-measured in the same change, because every row gains a field and a
  half-written ledger reds every session in between.
- **S4** — A fixture for the swap: one kit's path exchanged for another's at equal count, observed
  RED before S2 lands and green after the ledger records the new identity.

## 3. Non-goals (OUT)

- Arm 1's `RE` (`:63`). It is waived per `<path>:<line>` and its granularity is a different
  migration, deferred by `DEPL-dGaugedVintage-7` §3 with its reason.
- Changing WHAT counts as a hit. The regex is untouched; only what the ledger stores about each hit
  changes.
- Reducing the carried count. This unit measures more precisely; draining is separate work.
- Making the checker prefix-parametric. `DEPL-dCarriedReceipt-15` owns that.

## 4. Design

### Data model

The ledger row is `<path>\t<count>` today and becomes `<path>\t<count>\t<kits>`, where `<kits>` is a
comma-joined ASCII-sorted set. The comparison's awk reads `pin[$1]=$2` and `now[$1]=$2`; a third
field is INERT until a second comparison joins it, which is the work — the field alone buys nothing.

### Inventory

| Site | Today | After |
|---|---|---|
| the emitter pipeline | `grep -oHE` then an awk tally on `$1` | the same, plus a `(path, kit)` pass |
| a ledger row | `<path>\t<count>` | `<path>\t<count>\t<kits>` |
| the comparison awk | `UNRECORDED` / `ROSE` / `SLACK` on the count | plus `SWAPPED` on the kit set |

### Migration

Determinism matters more than brevity here: the kit set is built from a SORTED intermediate stream so
the same tree always yields the same row, whatever order `grep` walked the files in. An unsorted
join would make the ledger churn between runs and the ratchet unusable.

### Alternatives rejected

Keying each row on `(path, kit)` instead of adding a field: it changes the row identity the
comparison's three verdicts are written against, so every one of them would need re-reasoning for a
change that is really about one extra assertion.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one extra sort over the hit stream; the population is the cost and is unchanged.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a file with zero hits still emits no row, exactly as today, so the
  zero goal state is unchanged.
- observability — the `SWAPPED` verdict names both kit sets, not just that they differ.
- risks — a subtly wrong awk program grading the shipped surface. Mitigated by S4's observed RED and
  by AC5's byte-for-byte reproduction check.
- testing + left-shift gates — S4, observed RED first.
- migration / rollback — every row gains a field; S3 lands it in the same change.
- user docs — none; the emitter's header is the doc and states what the third field is.

## 6. Acceptance criteria

- **AC1** — When one kit's path is exchanged for another's at equal count in a shipped file,
  `bash tools/check-install-prefix.sh` exits non-zero and names that file with both kit sets.
- **AC2** — AC1's arm is observed RED before S2 lands: the same swap at `HEAD` today exits 0.
- **AC3** — When the tree is unchanged, `bash tools/check-install-prefix.sh` exits 0 against the
  re-measured ledger.
- **AC4** — When a file gains a literal for a kit it already names, the count rises and
  `bash tools/check-install-prefix.sh` still reports `ROSE` rather than `SWAPPED`, so the two
  verdicts stay distinguishable.
- **AC5** — `bash tools/check-install-prefix.sh --write-ratchet` reproduces the committed ledger
  byte-for-byte, so the file cannot drift from the emitter that produced it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `install-prefix (shipped surface)` leg, and
`bash tools/check-install-prefix.test.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft, filed by `DEPL-dGaugedVintage-7` when its S3 was not built.
- rev-2 · 2026-09-01 · BUILT and CLOSED. Every criterion met with no amendment — the first unit in
  this build for which that is true. Acceptance ledger at
  `build/2026-09-01-build-DEPL-dGaugedVintage-12-acceptance-ledger.md`.

## 10. Reuse audit

- No existing seam fits, and the evidence is that
  `python tools/codebase-map/reuse_lookup.py "record which kit each root prefix occurrence names"`
  returns only `repo_root`, `map_root`, `kit_rel` and `require_adopted_root` — path resolvers, none
  of which counts or records anything. The emitter and its comparison live inline in
  `tools/check-install-prefix.sh` and this unit extends them in place, which is correct for a gate
  that is one predicate over one population.
- Recall terms used: `ratchet shrink-only count identity swap backlog row status token spec header
  terminal join stale`
