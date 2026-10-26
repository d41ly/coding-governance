# KICK-dKeptSession-54 — an unassigned derived row keeps dGroundRules' refusal in `get`, and its value is read through the caps module

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 5 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-54-deviation-541.md](../build/2026-10-26-build-KICK-dKeptSession-54-deviation-541.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 21 at HIGH**, report item **H7**, which no other id shares.

`KICK-dKeptSession-34` S1 says an unassigned derived row "reads with source `default`", its §4 table
lists `roles.effort.default` and a `budgets.*` cap at "its derived default" with source `default`,
and its AC2 expects `policy.py get <cap> --explain` to print the cap's derived value. At
dGroundRules' `3c8c4718a`, `read_default_value` raises `DerivedDefault` for every `{ derived = ... }`
default (`policy.py:695-698`), and `get` refuses it as any `Refusal`; only `budgets.py`'s
`resolve_caps` reads such a row, by catching that refusal (`budgets.py:270`), and no spec of this
build changes `get`. So unit 34's AC1 and AC2 cannot pass against the reader it extends, and a
builder who makes them pass must compute a derived value inside `get`, overwriting the
evidence-derived caps and role efforts its own Goal protects. This unit restates the answer as the
code gives it and re-points the criteria. It repairs `KICK-dKeptSession-34` and builds one step
after it (order 5).

## 2. Scope (IN)

- **S1** — id 21. The answer. For a derived row the named preset leaves unassigned,
  `read_preset_value` answers `None`, so `read_default_value` is reached and raises `DerivedDefault`
  unchanged: `policy.py get <key>` refuses with dGroundRules' reason, exit as any refusal, and prints
  no `preset` source. No computation of a derived value is added to `get`. Observed by AC1.
- **S2** — id 21. The cap's value. The `preset-derived-cap` case of `tools/policy/check_policy.py`
  (`KICK-dKeptSession-34` S3) reads its census cap as `python budgets.py resolve <cap>` under `preset
  = "strict"`, the caps module's own reader, and expects the row the same command prints with no
  preset named. Observed by AC2.
- **S3** — id 21. The `preset-every-key` case. Its unassigned derived rows expect `get`'s
  `DerivedDefault` refusal, never a `default` source with a value. Observed by AC1.
- **S4** — id 21. The sibling text superseded by name. `KICK-dKeptSession-34` S1's "so
  `read_default_value` answers next with source `default`", §4's table rows for
  `roles.effort.default` and the `budgets.*` cap, AC1's "`roles.effort.default` with source
  `default`" and AC2's `policy.py get <cap> --explain` read as S1 to S3 here, each answered in unit
  34's acceptance ledger. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Which rows are unassigned: `KICK-dKeptSession-33`'s rule.
- A reader for derived defaults in `get`. dGroundRules' docstring names the caps module as the one
  reader of such a row (`policy.py:213-216` at `3c8c4718a`); adding a second is the defect avoided.
- The report's left-shift checklist entry, that every criterion's command is checked against the
  verb's refusals at the base. No clause of this build names that checklist.

### Edges

- **consumes-from** `KICK-dKeptSession-34` — `read_preset_value`'s answer for an unassigned derived row and the `preset-every-key` and `preset-derived-cap` cases, whose expectations this unit restates (id 21)
- **consumes-from** external — dGroundRules' `DerivedDefault` refusal in `read_default_value` and `budgets.py resolve`, unchanged
- **hands-off** `KICK-dKeptSession-56` — the restated cases, against which the batch's item for id 14 makes AC1's rewrite this unit's deciding criterion
- **hands-off** `KICK-dKeptSession-58` — the `preset-derived-cap` case's `budgets.py resolve` read, whose compare that unit narrows to value and source (id 9)
- **hands-off** `KICK-dKeptSession-62` — the restated cases' arm, whose leg the batch's S1 records (id 2)

## 4. Design

### Evidence

- `class DerivedDefault(Refusal)`: "`get` and the mirror refuse it as any Refusal, and the caps
  module alone reads it as no file value" (`policy.py:213-216` at `3c8c4718a`).
- `read_default_value` raises `DerivedDefault` when `check_derived(row["default"])` holds
  (`:695-698`).
- `resolve_caps` reads `read_key(f"budgets.{seg}", unset=policy.DerivedDefault)`
  (`budgets.py:270`); `budgets.py resolve [--explain] <cap>[=legacy:<n>|=default:<n>] ...` prints one
  `<cap>\t<value>\t<mode>\t<source>` row per request (`budgets.py:356-366`).

### The answers under `preset = "strict"`

| Key | Command | Answer |
|---|---|---|
| `hooks.bypass` | `policy.py get` | `refused`, source `preset` |
| `roles.effort.default` | `policy.py get` | refused, `DerivedDefault`'s reason |
| one census cap of `budgets.*` | `policy.py get` | refused, `DerivedDefault`'s reason |
| the same cap | `budgets.py resolve <cap>` | the row it prints with no preset named |

### Inventory

No identifier is minted.

### Migration

None beyond `KICK-dKeptSession-2`'s.

### Files touched (estimate)

- `tools/policy/check_policy.py`: S2 and S3 in the two cases

### Alternatives rejected

- **`get` computing a derived value.** It writes values over the evidence-derived caps and role
  efforts, the outcome unit 34's Goal rejects, and a second reader of derived rows beside the caps
  module.
- **Keeping AC2 on `get` and marking it NOT OBSERVED.** It leaves a criterion that cannot pass.

## 5. Production-readiness checklist

- security — none: two fixture cases' expectations.
- perf / scale — none.
- error / empty / loading states — the refusal is dGroundRules', unchanged.
- observability — `get --explain` prints the refusal's reason naming the derived default.
- risks — none new.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — none: `help/policy.md` already says a derived default is read by the caps module.

## 6. Acceptance criteria

- **AC1** — When `python check_policy.py --fixture preset-every-key` runs, each preset's line reads
  its assigned keys with source `preset`, each `never` key at its default, and `roles.effort.default`
  as refused with the `DerivedDefault` reason.
  Red when: an unassigned derived row reads any value through `get`, a `preset` or a `default`
  source.
- **AC2** — When the `preset-derived-cap` case runs `python budgets.py resolve <cap>` for one census
  cap under `preset = "strict"`, it prints the same row as with no preset named, and `python
  policy.py get <cap>` in that repository refuses.
  Red when: `get` answers the cap, or the caps module's row moves under the preset.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 · the two cases with their restated expectations, staged red by a copy of `read_default_value` answering a derived row's prose · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H7 (id 21).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-58`, `KICK-dKeptSession-62`
  mirrored, the other ends of the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seams reused are dGroundRules' `DerivedDefault` route and `budgets.py resolve`
(`tools/policy/policy.py:695-698`, `tools/policy/budgets.py:270` and `:356` at `3c8c4718a`); nothing
is minted, and no second reader of derived rows is written. `python
tools/codebase-map/reuse_lookup.py "read a derived default cap value through the caps module"` ranked
`read`, `read_text`, `read_conf` and `read_journal` by name stem only; the policy kit is not at this
base, so no existing seam in the tree fits and the branch's caps module is the one reused.

Recall terms used: `python tools/memory-recall/query.py "what does the preset step answer for a key
whose default is derived" --terms "read_preset_value DerivedDefault derived default budgets resolve
caps get refuse preset-every-key preset-derived-cap"`
