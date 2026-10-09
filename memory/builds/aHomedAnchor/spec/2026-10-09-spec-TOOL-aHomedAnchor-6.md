# TOOL-aHomedAnchor-6 — the closing review's driver and doc minors, batched

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base 40a976d9 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aHomedAnchor-6-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aHomedAnchor-6-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close every MEDIUM and LOW of round 1 whose write set is the driver, its suite and the protocol and
verbs carriers: M1, M3, M4, M5, M6, M7, M8, M9, L1, L2, L5, L6, L7 and L8 of
`memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md`.

## 2. Scope (IN)

- S1. M1: fail 71 refuses an `asks:` mandate on the local anchor in `slug` mode, with its own
  message; protocol section 1's "What stays" names `asks:`. Observed by AC1.
- S2. M4 and L7: `resolve_base`'s local branch falls through to the strict anchor when the README is
  not committed at HEAD, so `check_authorization`'s fail 6 names the missing README. Observed by AC2.
- S3. M5: an arm observes an honest local record reading met. Observed by AC3.
- S4. M6: two arms grade the fail 18 widening under `scope local` on a default-branch record, an
  orphan base refused and an ancestor of HEAD admitted. Observed by AC4.
- S5. M7: an arm re-preflights a local slug over a retired record and reads the new base. Observed by
  AC5.
- S6. M8: an arm commits `SPEC_AUDIT_DEFAULT` on the run branch only, under `scope local`, and reads
  the audit not owed. Observed by AC6.
- S7. L1: `trusted_base` maps an absent local base to HEAD only for `--preflight`, through a third
  argument `preflight`; a take-over refuses with fail 16. Observed by AC7.
- S8. L2: `TB_IGNORE_RECORD=0` is initialised beside `PK_ITEM`, after the conf is sourced.
  NOT OBSERVED: an initialisation, read in review.
- S9. L5, L6 and L8: protocol section 1 states the per-mode spec-audit rule and amends cost 2; the
  verbs file's recipe step 0 names `local`. Template and copy together. NOT OBSERVED: prose, graded
  by the parity legs.
- S10. M3 is closed by `TOOL-aHomedAnchor-3`'s render and M9 by `TOOL-aHomedAnchor-5`'s arms; this
  unit records that and builds nothing for them. NOT OBSERVED: a disposition.

## 3. Non-goals (OUT)

The leg: `TOOL-aHomedAnchor-7`. Narrowing the fail 18 widening: M6 asks for arms, not a narrower
clause, and the owner accepted the local anchor's own base.

### Edges

- **consumes-from** `TOOL-aHomedAnchor-3` — M3's closure
- **consumes-from** `TOOL-aHomedAnchor-5` — M9's closure

## 4. Design

Each item is the fix the review's skeptic judged sound, at the site it names. The new refusal reuses
fail 71's number, as fail 78 and fail 89 did for theirs. This unit and `TOOL-aHomedAnchor-7` have
disjoint write sets; the run builds both inline, in sequence.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`

## 5. Production-readiness checklist

- security — M1 closes a self-mandate on the local anchor; L1 removes a fallback.
- perf / scale — N/A — no new git call on any path but the refusals.
- error / empty / loading states — AC2's missing README now names itself.
- observability — N/A — refusal texts only.
- risks — N/A — every change narrows or arms.
- testing — AC1 to AC7, arms observed by a slice at VERIFYING.
- migration — N/A.
- user docs — the protocol and verbs carriers in S9.

## 6. Acceptance criteria

- **AC1** — When a local slug README carries `asks:`, `--preflight` prints fail 71's
  `the BASE came from the local anchor` text. Red when: the mandate is pinned.
- **AC2** — When the README is written but not committed under `scope local`, `--preflight` prints
  fail 6's `no build README at the pinned BASE`. Red when: the generic fail 16 answers instead.
- **AC3** — When a local record's base is a proper ancestor of HEAD, `--authorization` prints
  `authorization-reachable — met`. Red when: the local path refuses an honest run.
- **AC4** — When a default-branch record under `scope local` pins an orphan base, `--authorization`
  prints `is not an ancestor of the base this history derives`, and with an ancestor of HEAD it does
  not. Red when: either direction flips.
- **AC5** — When a local slug is re-preflighted over a retired record, the new `RUN.md` pins
  `base:` equal to the new HEAD. Red when: the finished run's base is taken.
- **AC6** — When `SPEC_AUDIT_DEFAULT` is committed only on the run branch under `scope local`,
  `--preflight` prints `spec-audit — not owed`. Red when: the run-branch conf opts the run in.
- **AC7** — When a take-over `--resume` meets a local record with no `base:` line, it prints fail
  16's `the record pins none`. Red when: it re-verifies at HEAD.

## 7. Gates

`unattended kit gate` · `unattended protocol size` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · local-scope fixtures on an unpushed branch · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from the round 1 minors batch.

## 10. Reuse audit

Each fix extends the site the review names; no existing seam fits anything new. Recall terms used:
`--terms "ANCHOR_SCOPE local trusted_base resolve_base fail 71 asks mandate D12-a take-over
allow-degenerate SPEC_AUDIT_DEFAULT"`.
