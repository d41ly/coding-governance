# DEPL-dCarriedReceipt-3 — `intake` honours `--answer prefix=`

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-DEPL-dCarriedReceipt-1-adopter-measurements.md](../build/2026-08-24-build-DEPL-dCarriedReceipt-1-adopter-measurements.md) | research | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-12 |
| [2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |

<!-- /gen:spec-records -->

## 1. Goal

`cmd_intake` emits the literal `prefix = "tools"` at `govkit.py:3206` regardless of any supplied
`--answer prefix=`. The one committed non-default descriptor in the fleet — NicoCares'
`.governance/deploy.toml`, which reads `prefix = "scripts"` — is therefore a file the tool that owns
it could not have written. Filed as the first of the thirteen defects in DEPL-aFerriedDossier-3 and
as ABL-dReadoptedConvoy-3 on the adopter side; it is two lines, and `-9`'s needle map is keyed off
`prefix`, so a wrong value there produces a wrong map rather than a refusal.

## 2. Scope (IN)

- **S1** — `cmd_intake` emits `prefix = "<value>"` from `answers["prefix"]` when supplied, and
  `"tools"` when not.
- **S2** — `prefix` joins the `derived` set in `needed_answers`, so it does not become a newly
  *required* answer that breaks every existing intake invocation.
- **S3** — one arm in `selftest.py` per branch: supplied and omitted.

## 3. Non-goals (OUT)

- **Not** validating the prefix against the target's tree, and **not** rejecting a prefix that no
  kit uses. `intake` records an owner decision; measuring it against reality is `-4`'s job.
- **Not** touching `target_context`'s `[kit.<id>]` override resolution (`:548`), which already works
  and which NC depends on.
- **Not** the other twelve defects in DEPL-aFerriedDossier-3; they are `-1`, `-7`, `-11`, `-12` and
  `-15`, or already fixed upstream.

## 4. Design

### Data model

`deploy.toml`'s `prefix` key is unchanged in shape. Only its source changes, from a literal to the
answer stream.

### Alternatives rejected

- *Make `prefix` a required answer.* Every existing scripted intake would start refusing, and the
  default is correct for most adopters. Derived-with-a-default is the shape the rest of the answer
  set already uses.

### Files touched (estimate)

`tools/govkit/govkit.py` (2 lines), `tools/govkit/selftest.py` (2 arms).

## 5. Production-readiness checklist

- security — N/A: `prefix` is already interpolated into resolved destinations, which are contained
  by the existing traversal guard; this unit does not widen what may be written.
- perf / scale — N/A.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — an empty `--answer prefix=` falls back to `tools` rather than
  emitting `prefix = ""`; asserted by AC3.
- observability — the intake summary already reports the count of answers recorded; `prefix` joins it.
- risks — none identified beyond a mistyped prefix, which `-4` then reports as total coverage loss
  rather than silently mis-installing.
- testing + left-shift gates — two `selftest.py` arms; RED-first observation is AC1.
- migration / rollback — none. NC's existing descriptor already carries the correct value by hand
  and is unaffected.
- user docs — `WIRE-INTO-PROJECT.md`'s intake step gains the flag in its example.

## 6. Acceptance criteria

- **AC1** — Before the change, `govkit.py intake --target <scratch> --kits gate-lint --answer prefix=scripts`
  writes a `deploy.toml` containing `prefix = "tools"`. Observe this RED first.
- **AC2** — After the change, the same command writes `prefix = "scripts"` and the run reports the
  answer as recorded.
- **AC3** — Omitting the answer still writes `prefix = "tools"`, and `--answer prefix=` with an
  empty value also writes `"tools"` rather than an empty string.
- **AC4** — `python tools/govkit/govkit.py selfcheck` exits 0 and `needed_answers` does not list
  `prefix` as missing for any registry entry.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs. Adds two arms; adds no new leg.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold).

## 10. Reuse audit

Wires through the existing answer stream — `needed_answers` and the `[answers]` emission in
`cmd_intake` — rather than adding a parallel channel for one key. `prefix` is already a first-class
token in `target_context` (`:535`) and `resolve_tokens` (`:516`); this unit only stops the writer
from ignoring it, so no seam is created and none is duplicated.
