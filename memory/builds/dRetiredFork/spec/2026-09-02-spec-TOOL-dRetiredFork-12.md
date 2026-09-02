# TOOL-dRetiredFork-12 — `playbook.fixture.md` becomes `rendered`

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/playbook.fixture.md` hardcodes `tools/unattended/` in its outputs, grain, records
and legs, and ships `role = "engine"` — verbatim, no placeholder pass — so `check-playbook.sh` exits
1 for any adopter at another prefix and the suite above it cannot follow a variable the fixture does
not have. This is `TOOL-dScrubbedConduit-2`, whose row already names the obstacle, and it is what
blocked `TOOL-aGradedDoorway-2` from finishing `check-playbook.test.sh`. inCMS carries it as
`KIT_PLAYBOOK_FIXTURE_DELTA`: five pointers repathed, zero content divergence.

## 2. Scope (IN)

- **S1** — Retag the fixture to `role = "rendered"` with `placeholders = ["KIT_DIR", "TOOL_ROOT"]`
  in `tools/unattended/kit.toml`, and replace its five literal spellings with the tokens.
- **S2** — Route it through the kit's own render step, so the rendered artifact is produced by the
  adopter the descriptor already declares rather than by a new mechanism.
- **S3** — A parity arm asserting the rendered fixture at the default prefix is byte-identical to
  today's committed bytes, which is the regression proof.
- **S4** — Unblock `check-playbook.test.sh`: its 37 recorded literal sites can now read through
  `KIT_REL`, which `TOOL-dRetiredFork-13` performs. This unit lands the precondition, not the sweep.
- **S5** — Close `TOOL-dScrubbedConduit-2` in `memory/backlog/TOOL.md`.

## 3. Non-goals (OUT)

- The `check-playbook.test.sh` sweep itself. It is `TOOL-dRetiredFork-13`, sequenced after this one,
  and the split is why this unit is order 2 and that one order 3.
- A general body-substitution channel in `govkit apply`. Measured at `tools/govkit/govkit.py:4340`:
  `apply` writes `blob_at(...)` straight to `dp.write_bytes(data)` with no substitution anywhere, and
  rendering is performed by each kit's own `[adopt] argv`. Changing that is a deployer contract
  change and belongs to `DEPL-dRetiredFork-3`, not here.

## 4. Design

### Data model

Two tokens only, `KIT_DIR` and `TOOL_ROOT`, matching the pair the memory-tree kit's three rendered
templates already declare. No new token alphabet.

### Migration

An adopter holding the old `engine` copy has bytes that assert an OID. On the pull, the row changes
role, so the receipt's identity for it changes too — which is precisely the class
`DEPL-dRetiredFork-3` must handle, and the reason this unit's landing must be verified against a
receipt-carrying fixture and not only against gov's tree. inCMS's row would otherwise REVERT
silently on a re-pull, because `engine` asserts the recorded OID.

### Alternatives rejected

Leaving the fixture as `engine` and waiving the prefix gate for it. That is the status quo dressed
as a decision: the suite above it stays unrunnable at any foreign prefix and
`TOOL-aGradedDoorway-2` stays INPROGRESS forever.

## 5. Production-readiness checklist

- security — N/A. A fixture is data read by a test.
- perf / scale — one render at adopt time.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an unresolved token is a REFUSAL, never an emitted literal brace.
  That rule is the whole value of the render channel and must be asserted, not assumed.
- observability — the render step names the tokens it filled.
- risks — a role change alters the receipt identity for an installed file at both adopters. This is
  the highest-risk item in the unit and is why S3's parity arm and a receipt-fixture run are both
  required before landing.
- testing + left-shift gates — S3's parity arm plus `check-playbook.sh` at two prefixes.
- migration / rollback — reverting the role is a descriptor edit plus restoring the literals.
- user docs — `tools/unattended/README.md` names the fixture as rendered and its two tokens.

## 6. Acceptance criteria

- **AC1** — When rendered at the default prefix, `tools/unattended/playbook.fixture.md` is
  byte-identical to its committed bytes at `b0108f13`.
- **AC2** — When rendered at `scripts/unattended`, `bash tools/unattended/check-playbook.sh` exits
  `0`; before this unit it exited 1.
- **AC3** — When a token is unresolved, the render REFUSES and emits no file. The token set is declared in `tools/unattended/kit.toml`.
- **AC4** — `bash tools/check-install-prefix.sh` reports the fixture's carried count at `0`.
- **AC5** — `bash tools/check-kit-versions.sh` exits `0` after the unattended bump.
- **AC6** — Against a receipt-carrying fixture, a `govkit update` run reports the role change rather
  than silently reverting the file.

## 7. Gates

`unattended kit gate` · `install-prefix (shipped surface)` · `kit version markers` · `govkit selfcheck` ·
`kit/dogfood doc parity`.

## 8. Open questions

- **F1 — does the role change need a receipt migration, or does `adopt --re-adopt` cover it?**
  `--re-adopt` re-measures from scratch and would classify the file correctly, but it also discards
  every other row's recorded base. Recommendation: make `DEPL-dRetiredFork-3` handle a role change
  in place, and treat `--re-adopt` as the fallback the runbook names rather than the plan.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from `TOOL-dScrubbedConduit-2` and the inCMS
  `KIT_PLAYBOOK_FIXTURE_DELTA` row.

## 10. Reuse audit

The seam is the memory-tree kit's three `role = "rendered"` rules in `tools/memory-tree/kit.toml`,
which already declare the exact `["KIT_DIR", "TOOL_ROOT"]` placeholder pair this unit adopts —
`reuse_lookup.py` reports `render-doc` and the rendered-template family as the corpus's existing
answer, so this extends a live pattern rather than inventing a channel.

Recall terms used: `playbook.fixture`, `rendered`, `engine`, `placeholder`, `KIT_DIR`, `TOOL_ROOT`,
`prefix`, `check-playbook`, `adopter`, `receipt`, `role`, `carried`.
