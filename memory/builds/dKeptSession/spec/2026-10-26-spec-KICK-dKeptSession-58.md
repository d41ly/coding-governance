# KICK-dKeptSession-58 — the derived cap's row compared on its value and source, its mode read as strict sets it

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 6 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 |
| [2026-10-26-build-KICK-dKeptSession-58-deviation-581.md](../build/2026-10-26-build-KICK-dKeptSession-58-deviation-581.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 9 at HIGH**, report item **H2**, which no other id shares.

`KICK-dKeptSession-54` S2 and AC2 expect `budgets.py resolve <cap>` under `preset = "strict"` to
print the same row as with no preset named. The row is `<cap>\t<value>\t<mode>\t<source>`, and its
mode comes from `budgets.enforce`, which strict sets to `refuse` (`KICK-dKeptSession-32` AC1) while
the default is `warn`. So AC2 reds on a correct build, and a builder who greens it must make the caps
module ignore strict's switch. This unit compares the columns the preset leaves alone and reads the
mode as strict sets it. It repairs `KICK-dKeptSession-54` and builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — id 9. The compare. The `preset-derived-cap` case of `tools/policy/check_policy.py` reads
  `python budgets.py resolve --explain <cap>` for one census cap twice, with no preset named and under
  `preset = "strict"`, and asserts the two rows' value and source columns are equal. Observed by AC1.
- **S2** — id 9. The mode. Under strict the row's mode column reads `refuse`, and the `--explain`
  line on stderr names the rule `budgets.enforce is refuse`; with no preset it reads `warn` and
  `budgets.enforce is warn`. Observed by AC1 and AC2.
- **S3** — id 9. The sibling text superseded by name. `KICK-dKeptSession-54` S2's "expects the row
  the same command prints with no preset named", §4's table row "the same cap | `budgets.py resolve
  <cap>` | the row it prints with no preset named" and AC2's "prints the same row" read as S1 and S2
  here. Answered in unit 54's acceptance ledger. Observed by AC1.

## 3. Non-goals (OUT)

- `policy.py get`'s refusal of the derived row: `KICK-dKeptSession-54` S1, unchanged, and its AC2's
  second half stands.
- What strict assigns: `KICK-dKeptSession-32` and `KICK-dKeptSession-33`.
- The report's left-shift checklist entry, that a same-output criterion names the columns it
  compares. No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-54` — the `preset-derived-cap` case and its `budgets.py resolve` read, whose compare this unit narrows to value and source (id 9)

## 4. Design

### Evidence

- `budgets.py` at `3c8c4718a`: `mode, rule = ("refuse" if enforce.value == "refuse" else "warn"),
  f"budgets.enforce is {enforce.value}"` (line 252); `resolve` prints
  `{a.cap}\t{value}\t{a.mode}\t{a.source}` (line 391) and, under `--explain`, `budgets: <cap> ·
  <rule> · <reason>` on stderr (line 394).
- `budgets.pinned` is on v2's never list, so strict leaves it unassigned and the pin branch (line
  248) is not taken.
- spec-32 AC1: strict makes `budgets.enforce` read `refuse` with source `preset`.

### The rows

| Preset | value | mode | source | `--explain` rule |
|---|---|---|---|---|
| none | the cap's derived value | `warn` | as resolved | `budgets.enforce is warn` |
| `strict` | the same | `refuse` | the same | `budgets.enforce is refuse` |

### Inventory

No identifier is minted.

### Migration

None.

### Files touched (estimate)

- `tools/policy/check_policy.py`: S1 and S2 in the `preset-derived-cap` case

### Alternatives rejected

- **Running the compare under a preset that leaves `budgets.enforce` unassigned.** It never shows the
  cap's row under strict, the posture unit 34 exists for.
- **Comparing whole rows and pinning `budgets.enforce` in the fixture's policy file.** The file's
  literal would then decide the mode, so the case reads no preset at all for that column.

## 5. Production-readiness checklist

- security — none: one fixture case's expectations.
- perf / scale — one more `budgets.py` run per case.
- error / empty / loading states — a refused read prints the reader's refusal on stderr, which the
  case reports as a red.
- observability — the `--explain` rule names the switch that set the mode.
- risks — none new.
- testing — the criteria of §6 and the arm in §7.
- migration — none.
- user docs — none: `help/policy.md` already says `budgets.enforce` sets a breach's mode.

## 6. Acceptance criteria

The fixture is unit 34's `preset-derived-cap` scratch repository under `%TEMP%`.

- **AC1** — When `python check_policy.py --fixture preset-derived-cap` runs, it passes, having read
  `budgets.py resolve --explain <cap>` with no preset and under strict, the value and source columns
  equal and the mode `warn` then `refuse`.
  Red when: a copy comparing whole rows reds on the mode, or a copy of `budgets.py` ignoring the
  preset's `budgets.enforce` passes.
- **AC2** — When `python budgets.py resolve --explain <cap>` runs in that repository under strict,
  stderr carries `budgets.enforce is refuse`.
  Red when: the rule names `warn`, so strict's switch never reached the caps module.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy fixtures` leg runs the case once dGroundRules has landed it; the arm line
below declares it.

New arm: tools/policy/check_policy.py · covers AC1 AC2 · the `preset-derived-cap` case read with no preset and under strict, staged red by a copy of `budgets.py` that reads `budgets.enforce` from the default alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-2 promotions' audit, H2 (id 9).

## 10. Reuse audit

The seam reused is dGroundRules' `budgets.py resolve --explain` (`tools/policy/budgets.py:252`,
`:391` and `:394` at `3c8c4718a`), whose rule line already names the switch; nothing is minted.
`python tools/codebase-map/reuse_lookup.py "compare selected columns of a tab separated cap row"`
ranked `rows`, `row` and `extract_row` by name stem only; the policy kit is not at this base, so no
existing seam in the tree fits and the branch's caps module is the one reused.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
