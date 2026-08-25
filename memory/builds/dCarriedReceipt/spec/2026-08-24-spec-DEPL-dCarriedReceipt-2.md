# DEPL-dCarriedReceipt-2 — `refuse` becomes `report`, and `attributes` gets a pins arm

**Status:** SPECCED · rev-3 · 2026-08-25 · node d · Tier-1 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-DEPL-dCarriedReceipt-1-adopter-measurements.md](../build/2026-08-24-build-DEPL-dCarriedReceipt-1-adopter-measurements.md) | research | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-12 |
| [2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |

<!-- /gen:spec-records -->

## 1. Goal

Three roles dispatch to `refuse` in `UPDATE_ROLE` (`govkit.py:2864-2866`), which calls `r.fail` and
`continue`s **before** `classify_row` and before `acted.append`. It therefore never prevented a
write — it only made `r.problems` non-empty, which permanently skips the receipt re-stamp
(`:3115`). One `attributes` row in a target makes every future `update` on that target exit 1 and
never advance its `gov_commit`. NC's kit selection includes `kickoff-manifest` and `playbook`, both
of which declare an `lf_pin`, so an onboarded NC would carry exactly such a row. Nothing else in
this build can run until a target can re-stamp.

## 2. Scope (IN)

- **S1** — `UPDATE_ROLE["attributes"]` changes from `refuse` to a new disposition `pins`.
- **S2** — the `pins` disposition recomputes `lf_pins()` (`:1805`) for the receipt's claimed kits at
  `--to`, compares the result against the govkit-owned block in the target's `.gitattributes`, and
  prints `current` or `pins-moved`. Under `--write` it writes an outbox order. It never merges and
  never edits `.gitattributes`.
- **S3** — `gate-leg` and `ci` change from `refuse` to `report`: one printed row each, counted in
  the tally, no `r.fail`.
- **S4** — the existing `selfcheck` arm asserting `UPDATE_ROLE` covers the role enum stays green.

## 3. Non-goals (OUT)

- **Not** teaching `update` to WRITE `.gitattributes` pins. That destination is `apply`'s, and
  DEPL-dSettledRoster-1 is an open ask about how it writes them; this unit must not pre-empt it.
- **Not** emitting or repairing gate legs — that is `-6`.
- **Not** relaxing any other `refuse`. `merged` keeps its block disposition and every unknown role
  keeps refusing by name.

## 4. Design

### Data model

No receipt-shape change. `pins` is a dispatch value only.

### Alternatives rejected

- *Leave `refuse` and let operators pass a flag.* The failure is silent-by-default: the operator
  sees exit 1 with a message about a role, not about a re-stamp that will never happen again.
- *Demote to `skip`.* A skipped row prints nothing, and a target whose `.gitattributes` pins have
  moved would then have no channel at all.

### Files touched (estimate)

`tools/govkit/govkit.py` (~10 lines), `tools/govkit/selftest.py` (3 arms).

## 5. Production-readiness checklist

- security — N/A: this unit removes a write path's refusal, not a guard; nothing new is written.
- perf / scale — N/A: `lf_pins()` is already computed per run by `apply`.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a target with no `.gitattributes` block prints `pins-moved`, not
  a traceback; asserted.
- observability — every `pins`/`report` row prints and is tallied; nothing becomes silent.
- risks — the one real risk is loosening a refusal that was load-bearing. It is not: the refusal
  runs after the write-eligibility branch and before any write, so no byte reachable today becomes
  reachable. Asserted by AC3.
- testing + left-shift gates — three arms in `selftest.py`; the RED-first observation is AC1.
- migration / rollback — none; a receipt written before this unit reads identically after.
- user docs — one line in `WIRE-INTO-PROJECT.md`'s update section naming the two dispositions.

## 6. Acceptance criteria

- **AC1** — Before the change, a fixture target carrying one `attributes` row and one genuinely
  stale `engine` row exits **1** from `govkit.py update --write` and its `install.json` `gov_commit`
  is unchanged. Observe this RED first; it is the defect.
- **AC2** — After the change, the same fixture exits **0**, the engine row is written, and
  `install.json`'s `gov_commit` equals the `--to` sha.
- **AC3** — With the govkit-owned block in the fixture's `.gitattributes` altered in gov, the run
  prints `pins-moved`, still exits 0, writes `.governance/outbox/`, and leaves the target's
  `.gitattributes` byte-identical (`git diff --exit-code -- .gitattributes`).
- **AC4** — `python tools/govkit/govkit.py selfcheck` exits 0, with its role-enum coverage arm
  still asserting every `UPDATE_ROLE` key.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and
`govkit selfcheck` legs. Adds three arms to `tools/govkit/selftest.py`; adds no new leg.

## 8. Open questions

- **F1 — should `gate-leg` and `ci` print one row each, or one aggregate row per kit?**
  Per-row, matching every other disposition; an aggregate hides which leg.
  RESOLVED (agent, 2026-08-24, delegated): per-row, under the full-scope approval.

## 9. Revision log

- rev-3 · 2026-08-25 · round-4 fold: L2 — §4's Files touched said `selftest.py` (2 arms) while §5
  reads "three arms" and §7 "Adds three arms". Two of the three said three, and the two-arm figure
  is the one a builder budgets from, so §4 now reads (3 arms).
- rev-2 · 2026-08-24 · round-3 fold: the re-stamp guard citation: `:3111` is that guard's
  explanatory comment; the `if r.problems:` it names is `:3115`.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold).

## 10. Reuse audit

Wires through the existing `UPDATE_ROLE` dispatch table (`govkit.py:2857`) and the existing
`lf_pins()` seam (`:1805`) — both already have exactly one caller shape and neither is duplicated.
No new mechanism is introduced: `pins` is a fourth value in a table that already carries `table`,
`skip`, `block`, `adopter`, `seed`, `report-reseed` and `refuse`. The outbox order reuses the path
and format `cmd_update` already writes for a three-way conflict (`:3087`).
