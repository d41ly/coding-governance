# TOOL-aGradedMandate-7 — the promotion clause counts only ids that are non-WONTDO at HEAD

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

When a review loop exits `NON-CONVERGENT` or `CEILING`, every blocker still standing is promoted to
a unit of the build — "specced at its tier and built. Not parked, not waived, not re-reviewed". The
leg's promotion clause discharges that by counting NEW unit ids at HEAD that the run's BASE lacked,
and never looks at their status. Three thin specs flipped to `WONTDO` satisfy it, and
`build-complete` sees no non-terminal row. This unit makes the count status-aware.

## 2. Scope (IN)

- **S1** — In the `check 2` awk END block, derive `newids` from ids that are present at HEAD, absent
  at BASE, AND whose row status is neither `CLOSED`-by-retirement nor `WONTDO`. A promoted blocker
  that was retired is not a promotion.
- **S2** — The status is read from the same generated region the id extraction already reads, so no
  second parse and no second source.
- **S3** — Restate the clause's own message as a LOWER BOUND: it demands at least one surviving id
  per exited SUBJECT, not one per standing blocker, and the message says so rather than implying a
  stronger claim. The blocker-sum form is deliberately NOT built — see §3.
- **S4** — Add `not retired` to the forbidden-disposition enumeration in the Skill template, which
  reads exhaustive and omits the cheapest exit. That edit lands in `TOOL-aGradedMandate-8`'s single
  render and is named here only so the pair is traceable.

## 3. Non-goals (OUT)

- **No blocker-SUM arm.** Comparing `newids` against the sum of standing blockers would red
  `memory/builds/aPrimedKeepalive/RUN.md` on the default branch today, over a finished record no
  verb may rewrite, and the review's skeptics found the rule itself arguable: M4 does not obviously
  forbid one unit covering two closely related blockers. An unlandable gate over a contested rule is
  two reasons not to build it.
- **No per-subject attribution.** The region records ids, not which subject promoted them, and the
  clause's own header already says the honest claim is the counting one.
- **No change to the shrink test or the ceiling test**, both of which are correct.

## 4. Design

### Data model

No new fact. `rs_now`-style extraction already exists in the check's neighbourhood: the id set at
HEAD is derived by `grep -oE` over the region, and `unit_rows`'s `| WONTDO |` filter is the status
predicate used by `nonterminal_units` and by check 24's own retire loop.

### Inventory

| Site | Change |
|---|---|
| `check-unattended.sh` check 2 | the `rv_now` derivation gains a status filter; the END message widens |
| `check-unattended.test.sh` | a WONTDO-promotion arm, an honest-promotion arm |

The filter is applied where `rv_now` is built rather than inside awk, because awk receives only the
computed count and giving it the rows would duplicate the region parse.

### Migration

Verified before wiring: the predicate is run over the real tree and prints hits and near-misses. The
only record that exits without converging and could be affected is `aPrimedKeepalive`, whose promoted
units are not `WONTDO`, so the tightened count still discharges it.

### Alternatives rejected

Counting only ids whose status is `CLOSED`. Rejected: a promotion recorded on a run that later
aborts is still a promotion, and a status test that demands completion would conflate this clause
with `build-complete`.

## 5. Production-readiness checklist

- security — N/A. A tighter read of tracked bytes.
- perf / scale — N/A. One added `grep` in a pipeline that already runs per record.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — an unreadable BASE roster already reports "cannot be observed"
  rather than passing, and that arm is untouched.
- observability — the message states the lower-bound qualifier explicitly, so a reader cannot infer
  a per-blocker guarantee the check does not make.
- risks — tightening a live clause over a tracked corpus; mitigated by running it over the tree
  before wiring and recording the result.
- testing + left-shift gates — two arms, each observed RED first.
- migration / rollback — reverting the filter restores the id-only count.
- user docs — the Skill enumeration, carried in `TOOL-aGradedMandate-8`.

## 6. Acceptance criteria

- **AC1** — When a fixture's review loop exits `NON-CONVERGENT` and the only id its HEAD roster
  gained is `WONTDO`, `bash tools/unattended/check-unattended.sh` fails check 2 naming that record.
- **AC2** — When the gained id is `INPROGRESS` or `CLOSED`, the check passes.
- **AC3** — The `check 2` message for an exited subject contains the words naming it a lower
  bound, so a reader is not told a per-blocker guarantee exists.
- **AC4** — Running the tightened `rv_now` derivation over the tree at HEAD prints zero new hits,
  recorded in this build's journal record.
- **AC5** — `bash tools/unattended/check-unattended.sh` is green on the tree at HEAD after the
  change.

## 7. Gates

`unattended kit gate` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F6 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is check 24's own retire loop at `tools/unattended/check-unattended.sh:1627`, which already
spells the status predicate as `grep -E '\| WONTDO \|'` over the region rows before extracting ids.
This unit reuses that exact spelling in check 2 rather than inventing a second status test, so the
two clauses cannot disagree about what a retired unit looks like.

`nonterminal_units` in the driver spells the complementary predicate for the same region. The two
files are copy-installed standalone, so the shared spelling is the reuse available here; a shared
helper is not, and that constraint is the kit's own and is stated in `declared_list`'s header.
