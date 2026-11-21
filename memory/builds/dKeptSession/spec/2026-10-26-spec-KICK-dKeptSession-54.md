# KICK-dKeptSession-54 — an unassigned derived row keeps dGroundRules' refusal in `get`, and its value is read through the caps module

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 5 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-54-deviation-541.md](../build/2026-10-26-build-KICK-dKeptSession-54-deviation-541.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md](../build/2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-4-orders-5-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-4-orders-5-reground-brief.md) | research | KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 21 at HIGH**, report item **H7**, which no other id shares.

At rev-2 `KICK-dKeptSession-34` said an unassigned derived row reads with source `default` and its
derived value, while `read_default_value` raises `DerivedDefault` for every `{ derived = ... }`
default (`tools/policy/policy.py#read_default_value`) and `get` refuses it as any `Refusal`. This
unit restated the answer as the code gives it. `KICK-dKeptSession-34` rev-3 now states that answer
itself and builds it: the refusal in `get`, the unassigned class of `preset-every-key`, and the cap
read through the caps module in `preset-derived-cap`. So this unit builds nothing. It is the
observation that id 21 is answered, made against unit 34's cases once unit 34 lands (order 4), one
step before this unit's order 5.

## 2. Scope (IN)

- **S1** — id 21. The answer. For a derived row the named preset leaves unassigned, `get` refuses
  with dGroundRules' `DerivedDefault` reason and prints no `preset` source, and no computation of a
  derived value is added to `get`. Carried by `KICK-dKeptSession-34` S1; this unit observes it.
  Observed by AC1.
- **S2** — id 21. The cap's value, read as `python budgets.py resolve` reads it, the caps module
  being the one reader of a derived cap (`tools/policy/policy.py#DerivedDefault`). Carried by
  `KICK-dKeptSession-34` S3; this unit observes the `get` half of that case's repository. Observed
  by AC2.
- **S3** — id 21. The `preset-every-key` case's unassigned derived rows expect `get`'s
  `DerivedDefault` refusal, never a `default` source with a value. Carried by
  `KICK-dKeptSession-34` S2; this unit observes it. Observed by AC1.
- **S4** — id 21. The ledger. This unit's acceptance ledger answers AC1 and AC2 with the output of
  unit 34's two cases at unit 34's landing; no file of the policy kit changes for this unit.
  Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Any code or fixture case: `KICK-dKeptSession-34` rev-3 builds both cases and states the answer.
- The mode column of the cap's `budgets.py resolve` row under strict: `KICK-dKeptSession-34` S3 and
  `KICK-dKeptSession-58`.
- Which rows are unassigned: `KICK-dKeptSession-33`'s rule.
- A reader for derived defaults in `get`. `DerivedDefault`'s docstring names the caps module as the
  one reader of such a row; adding a second is the defect avoided.
- The report's left-shift checklist entry, that every criterion's command is checked against the
  verb's refusals at the base. No clause of this build names that checklist.

### Edges

- **consumes-from** `KICK-dKeptSession-34` — `read_preset_value`'s answer for an unassigned derived row and the `preset-every-key` and `preset-derived-cap` cases, which this unit observes (id 21)
- **consumes-from** external — dGroundRules' `DerivedDefault` refusal in `read_default_value` and `budgets.py resolve`, unchanged
- **hands-off** `KICK-dKeptSession-56` — the observed cases, against which the batch's item for id 14 makes AC1 this unit's deciding criterion
- **hands-off** `KICK-dKeptSession-58` — the `preset-derived-cap` case's `budgets.py resolve` read, whose compare on value and source and whose mode that unit and unit 34 state (id 9)
- **hands-off** `KICK-dKeptSession-62` — the observed cases' leg, which the batch's S1 records against unit 34's arm (id 2)

## 4. Design

### Evidence

Read at HEAD `c2a407b0`, 2026-11-21.

- `class DerivedDefault(Refusal)`: "`get` and the mirror refuse it as any Refusal, and the caps
  module alone reads it as no file value" (`tools/policy/policy.py#DerivedDefault`).
- `read_default_value` raises `DerivedDefault` when `check_derived(row["default"])` holds, its reason
  carrying `DERIVED_WHY` (`tools/policy/policy.py#DERIVED_WHY`).
- `resolve_caps` reads `budgets.<cap>` with `unset=policy.DerivedDefault`
  (`tools/policy/budgets.py#resolve_caps`), and `budgets.py resolve` prints one
  `<cap>\t<value>\t<mode>\t<source>` row per request (`tools/policy/budgets.py#main`).
- Probed in this tree: `python tools/policy/policy.py get roles.effort.default` and `get` on the
  `budgets."AGENTS.md"` cap each exit 2 with the `DerivedDefault` reason, while `python
  tools/policy/budgets.py resolve --explain AGENTS.md` prints its row with source `default`.

### What carries rev-2's items

| rev-2 item | Carried by |
|---|---|
| S1, the refusal in `get` | `KICK-dKeptSession-34` S1 |
| S2, the cap read by `budgets.py resolve` | `KICK-dKeptSession-34` S3, value and source compared |
| S3, `preset-every-key`'s unassigned rows | `KICK-dKeptSession-34` S2 |
| S4, unit 34's text superseded | void: unit 34 rev-3 states the answer itself |

### Inventory

No identifier is minted.

### Migration

None.

### Files touched (estimate)

None: every file rev-2 named is `KICK-dKeptSession-34`'s at its rev-3.

### Alternatives rejected

- **Building rev-2's restatement beside unit 34's.** Two units would build one mechanism in one
  file, the second a copy of the first.
- **Retiring this unit.** A status change this re-grounding does not make; the observation keeps id
  21's answer joined to the unit the audit promoted for it.

## 5. Production-readiness checklist

- security — none: no code path changes.
- perf / scale — none.
- error / empty / loading states — the refusal is dGroundRules', unchanged.
- observability — `get --explain` is not reached for such a row; the refusal names the row.
- risks — none new.
- testing — the two observations of §6, over unit 34's cases.
- migration — none.
- user docs — none: `help/policy.md#how-to-use-it` already says `get` refuses a key whose default
  is derived until the file sets it, and `help/size-caps.md` gives `budgets.py resolve` as the way to
  ask a cap's value.

## 6. Acceptance criteria

- **AC1** — When `python check_policy.py --fixture preset-every-key` runs after
  `KICK-dKeptSession-34` lands, it passes, and each preset's line reads `roles.effort.default` and
  one census cap of `budgets.*` as refused with the `DerivedDefault` reason, never a `preset` source.
  Red when: an unassigned derived row reads any value through `get`, under a `preset` or a `default`
  source.
  fixture: unit 34's `run_preset_every_key` class, absent from the tree until unit 34 lands.
- **AC2** — When `python check_policy.py --fixture preset-derived-cap` runs, it passes, and in its
  strict repository `python policy.py get` on the case's cap key exits 2 with the `DerivedDefault`
  reason.
  Red when: `get` answers the cap under the preset.
  fixture: unit 34's `preset-derived-cap` case, absent from the tree until unit 34 lands.

## 7. Gates

`policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H7 (id 21).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-58`, `KICK-dKeptSession-62`
  mirrored, the other ends of the edges the round-2 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S1 S2 S3 S4 · §3 · §4 · §5 · AC1 AC2 · §7 · §10 · re-grounded at HEAD
  `c2a407b0` by `2026-11-21-prompt-KICK-dKeptSession-4-orders-5-reground-brief`; carries, order and
  status kept. `KICK-dKeptSession-34` rev-3 now carries rev-2's S1 to S3, so each is reduced to its
  observation of unit 34's cases and S4's supersession of unit 34's text is void. Narrowed: no code,
  no case and no arm is built here, so Files touched is empty, the `New arm:` line goes to unit 34,
  and AC2 observes only the `get` half of `preset-derived-cap`. Every line citation became a
  `path#symbol` citation.

## 10. Reuse audit

No code is written, so no seam is extended: the mechanism is `KICK-dKeptSession-34`'s, over
dGroundRules' `DerivedDefault` route and the caps module's `budgets.py resolve`
(`tools/policy/policy.py#read_default_value`, `tools/policy/budgets.py#resolve_caps`). `python
tools/codebase-map/reuse_lookup.py "read a derived default cap value through the caps module"` ranked
`read_text`, `read`, `read_bytes` and `read_policy_value` by name stem only; `read_policy_value`
reads through `get`, which refuses a derived row, so it is no second reader. The recall query below
returned TOOL-dGroundRules-62, units 33 and 34 and this spec, and unit 34 rev-3 is where the answer
now lives.

Recall terms used: `python tools/memory-recall/query.py "what does the preset step answer for a key whose default is derived" --terms "read_preset_value DerivedDefault derived default budgets resolve caps get refuse preset-every-key preset-derived-cap"`
