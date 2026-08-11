# TOOL-aSealedCaravan-1 — build record

**Status:** CLOSED · rev-1 · 2026-08-10 · node a · Tier-2 · base 16aeb5ef · streams tooling

## 1. Goal

Record what the three-commit rollout of `TOOL-aSealedCaravan-1` actually built, and what it found
that the spec did not predict. Landed on `main` after reconciling nine commits that arrived during the unit; the merge is its own
record and is summarised under section 4.

## 2. Scope (IN)

All thirteen scope items landed, in the three commits section 4 lists. The full bar is green at
41/41 legs (one conditional leg skipped by design).

## 3. Non-goals (OUT)

Nothing was descoped. `DEPL-aSealedCaravan-2` was not started, per its own sequencing.

## 4. Design

### Inventory

| Commit | Items | Note |
|---|---|---|
| `349f9e9` | S11, S6 | five stale records; the drift-audit Skill that named two files that do not exist |
| `6e1d925` | S3, S4, S5, S7, S9, S12 | derived prefixes, rendered templates, check-15 scope, two disarmed guards, the kit launcher |
| `5908ab3` | S1, S2, S8, S10, S13 | the runbook rewrite, the enforcement gate, the cross-kit references |

### What the build found that the spec did not

Four things, each of which changed code rather than prose.

The check-15 widening was **wrong on its first run**, exactly as the charter's trap predicts for a
new predicate. Accepting any token that is the tail of a tracked path reported 17 legitimate
relative links dead, 16 of them written by this kit's own index generator. Relative-to-citer
resolution is now tested before the tail rule, and both halves carry arms.

`adopt-memory-tree.sh` **refused outright** when the kit directory sat outside the tree being
scaffolded. That is the flow the hygiene self-test uses and a legitimate one for an operator running
the shipped adopter from the governance checkout, so the guard now falls back to the declared prefix
and says so on stderr.

The `merge-rows.test.sh` assertion the spec said needed re-scoping **was already path-scoped**. What
it lacked was its complement — that the kit-internal launcher DOES carry the inline resolver — which
is the half an adopter depends on.

`check-wiring.sh`'s merge smoke **rebuilt the driver command by hand** rather than running the one it
blesses. With two launcher shapes taking different argv that is a standing way for the probe to
disagree with the wiring it verifies, so it now runs the configured argv.

### Migration

None. No adopter state changes; existing adopters keep both spellings.

## 5. Production-readiness checklist

- security — N/A: no new write path. The new gate reads tracked files.
- perf / scale — the prefix gate runs over 76 files in well under a second.
- a11y · i18n — N/A: developer tooling, no interface.
- error / empty / loading states — three population guards added (prefix gate, agent-cap parity arm,
  pre-commit legs); each names what it looked for rather than exiting 0 over an empty set.
- observability — every changed guard prints the path it resolved.
- risks — the waiver registry is the one place a future root spelling could enter quietly; it is
  shrink-only and a stale row reds.
- testing + left-shift gates — 9 new arms on the prefix gate, 4 on check-15, 1 on the launcher
  parity, 2 on check-wiring's launcher preference.
- migration / rollback — revert the three commits; nothing external changed.
- user docs — `WIRE-INTO-PROJECT.md`, four kit READMEs, the charter.

## 6. Acceptance criteria

AC1 through AC14 of the spec were exercised. AC1, AC2 and AC13 are covered by the new gate and its
self-test; AC3 through AC8 by the kit self-tests re-run in commit 2; AC9 by the record corrections;
AC10 by the derived `GEN_HEADER`; AC11 by the ratchet's own self-test at its new default path; AC12
by the merge-driver replay; AC14 by the full bar.

## 7. Gates

`bash tools/run-gates.sh` — GREEN, 41/41 (1 skipped). Legs added: `install-prefix (shipped surface)`
and `install-prefix self-test`. `KIT_MEMORY_TREE_VERSION` 2.2 to 2.3.

## 8. Open questions

none. Section 8 of the spec is fully resolved; the owner ratified F1 and F2 and confirmed S9's
packaging on 2026-08-10.

## 9. Revision log

- rev-1 · 2026-08-10 · initial build record, written at the end of the three-commit rollout.

## 10. Reuse audit

The build reused what the spec's audit named: `kit_rel`-shaped prefix derivation in three languages,
the canonical resolver block copied verbatim between its own markers rather than retyped, the
`gate_at`/`first_of` locator idiom for guards whose kit prefix is not fixed, and the existing
prefix-parameterized fixture builders in the kit self-tests. The one new seam is the prefix gate
itself, recorded in `memory/map/features/install-prefix.md` with its reuse affordance.
