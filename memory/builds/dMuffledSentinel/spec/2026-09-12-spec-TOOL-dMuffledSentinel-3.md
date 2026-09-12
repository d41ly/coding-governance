# TOOL-dMuffledSentinel-3 — the drift-audit and unattended versions move with the bytes unit 2 changed

**Status:** CLOSED · rev-2 · 2026-09-12 · node d · Tier-1 · base 551a555e · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-12-build-TOOL-dMuffledSentinel-3-1-acceptance-ledger.md](../build/2026-09-12-build-TOOL-dMuffledSentinel-3-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dMuffledSentinel-2` changed what `tools/drift-audit/drift_report.py` and
`tools/unattended/check-pass-order.sh` do and left `KIT_DRIFT_AUDIT_VERSION` at 1.9 and
`KIT_UNATTENDED_VERSION` at 1.18. An adopter pulling it cannot tell the new vintage from the old by
version, and inCMS's `kit-versions` leg refuses exactly that. Move both versions.

## 2. Scope (IN)

- **S1** drift-audit goes to 1.10: `KIT_DRIFT_AUDIT_VERSION` and every `gov:kit drift-audit@` stamp
  under `tools/` that carries 1.9. Observed by AC1.
- **S2** unattended goes to 1.19: `KIT_UNATTENDED_VERSION` in all four scripts that carry it, every
  `gov:kit unattended@` stamp in its templates, and the rendered copies re-made with the kit's own
  adopt script. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- No behaviour change. The bytes that moved in unit 2 are what these versions now name.
- No version rule for these kits. A gate that makes gov bump on change is a separate question.

### Edges

none

## 4. Design

The stamps are text, so the change is mechanical and the check is whether every carrier agrees. The
kit version markers leg is what grades that agreement, and the unattended kit's own adopt `--check`
is what grades its rendered copies against their templates.

## 6. Acceptance criteria

- **AC1** — `tools/check-kit-versions.sh` exits 0 with every drift-audit carrier at 1.10.
  Red when: a carrier still says 1.9.
- **AC2** — `tools/check-kit-versions.sh` exits 0 with every unattended carrier at 1.19.
  Red when: one of the four `KIT_UNATTENDED_VERSION` lines or a template stamp still says 1.18.
- **AC3** — `bash tools/unattended/adopt-unattended.sh --check` exits 0 after the rendered copies are re-made.
  Red when: a rendered copy still carries the old stamp.

## 7. Gates

`kit version markers` · `unattended skill wiring` · `drift-audit wiring` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-12 · §2 S1 S2 · opened after inCMS's `kit-versions` leg refused the pull of unit 2.
- rev-2 · 2026-09-12 · S1 · the drift workflows' `meta.version` joins S1's carriers, found by AC1's first
  run. Status CLOSED, every criterion met.
