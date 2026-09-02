# TOOL-dRetiredFork-11 — `.githooks/pre-push` derives its install prefix

**Status:** OPEN · rev-3 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

`.githooks/pre-push` hardcodes `tools/` at five functional sites and ships VERBATIM to every
push-main adopter, so the defect ships too. `TOOL-aBoundedCeiling-7` records the consequence:
forcing predicates 6 and 7 — the diff touches the leg manifest, and the recorded manifest blob
differs — match NOTHING at any other prefix, so a manifest-wide change lands there scoped against a
green earned on a different leg set. Green-by-absence, in the hook that decides whether the
authoritative bar is owed. NicoCares carries the fix as `nc carve-out 14/20`.

## 2. Scope (IN)

- **S1** — Adopt NicoCares' two-line prefix probe, which is layout-agnostic, defaults to `tools` and
  is correct in gov's tree unchanged.
- **S2** — All five functional sites read through it: the leg-manifest path, the gate-fingerprint
  path, and the three remaining spellings.
- **S3** — A path that resolves to nothing is a REFUSAL, never a non-match. The two are
  indistinguishable today and that is what makes the failure silent.
- **S4** — An arm in `.githooks/pre-push.test.sh` running the hook against a fixture installed at a
  non-`tools` prefix and observing predicates 6 and 7 FIRE, observed RED first.
- **S5** — Close `TOOL-aBoundedCeiling-7` in `memory/backlog/TOOL.md` in the same commit.

## 3. Non-goals (OUT)

- Reading the prefix from `deploy.toml`. The hook must work in a tree with no receipt, which is
  swydee's state and every fresh clone's.
- Any change to what the hook decides. Only where it looks, never whether it forces.

## 6. Acceptance criteria

- **AC1** — When the leg manifest changes in a fixture installed at `scripts/`, the hook's forcing
  predicate 6 FIRES; the pre-change hook matched nothing and did not force.
- **AC2** — When the recorded manifest blob differs at that prefix, predicate 7 fires. Observed via `bash .githooks/pre-push.test.sh`.
- **AC3** — When the prefix resolves to nothing, the hook REFUSES naming the failed resolution. Observed via `bash .githooks/pre-push.test.sh`.
- **AC4** — In gov's own tree, `bash .githooks/pre-push.test.sh` passes with its arm results
  byte-identical to the pre-change run.
- **AC5** — `bash tools/check-install-prefix.sh` reports `.githooks/pre-push` at a lower carried
  count than its current ratchet row of 2.

## 7. Gates

`push-main self-test` · `install-prefix (shipped surface)` · `pre-push self-test` · `testsuite counts (every bar self-test prints one)`.

## 8. Open questions

none - deriving the prefix is this build's stated rule for a path fix, and the
alternative it forbids is a new config key. This section is present
because a section 8 with neither an item nor a `none` form is a refusal, not a pass, and both
this spec's readers grade it that way.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
- rev-2 · 2026-09-02 · folded spec-audit round 2, finding 27. §7 named the wiring suite; this unit touches
  `.githooks/pre-push`, which `pre-push self-test` grades and which its own criteria already invoke.
- rev-3 . 2026-09-02 . added the section 8 `none` declaration both readers require;
  no design content changed.
