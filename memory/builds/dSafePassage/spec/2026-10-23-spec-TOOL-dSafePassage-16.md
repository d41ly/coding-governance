# TOOL-dSafePassage-16 — the step record's precondition, one predicate beside its one writer, and the schema-4 bootstrap it answers

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-16-deviation-62.md](../build/2026-10-23-build-TOOL-dSafePassage-16-deviation-62.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 TOOL-dSafePassage-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 50** at BLOCKER, merged with id 1 into its item **D-1**: the walk cannot
start `govkit/receipt-schema-4` on a schema-3 receipt. TOOL-dSafePassage-3's writer
`set_step_state` raises `Refusal` on any receipt below schema 4 (its spec, §4 Data model, lines
110-111, pinned by its AC7), and TOOL-dSafePassage-2 hands "how the schema step's own row lands while
the field does not exist yet" to TOOL-dSafePassage-3 (its spec, §3, lines 117-118), which never
answers it. This unit is id 50's promotion, the writer's half of D-1: it answers the hand-off in the
writer's module, with the one path the report's corrected fix leaves, option (a). The writer keeps
its refusal, gains no exception, and exports the precondition it refuses on as one predicate every
caller asks before it writes. Id 1's promotion, `TOOL-dSafePassage-15`, makes the walk ask it.

## 2. Scope (IN)

- **S1** — The predicate. `test_steps_recordable(receipt)` in `tools/govkit/upgrade_steps.py`, beside
  `set_step_state`, returns True exactly when the receipt's `schema` is an `int` of 4 or more and its
  `steps` is a list. It reads the dictionary and writes nothing. Observed by AC1.
- **S2** — One fact. `set_step_state` raises its below-schema-4 `Refusal` by calling
  `test_steps_recordable`, never by a comparison of its own, so the writer refuses exactly the
  receipts the predicate rejects. The refusal text names the rule the predicate states and the
  receipt's `schema`. Observed by AC2 and AC3.
- **S3** — The bootstrap, stated once. `set_step_state`'s docstring and the receipt section of
  `help/upgrade-steps.md` (the section TOOL-dSafePassage-3's S8 writes) say: below schema 4 no step
  row is persisted, so a step's failure or interruption on such a receipt goes to `update`'s output
  and findings only; the `govkit/receipt-schema-4` row is written after that step's post-spawn
  re-read shows schema 4, through the writer, like any other row. Observed by AC4.
- **S4** — The arm. A `tools/govkit/selftest.py` arm runs the predicate and the writer over the five
  receipt shapes of §4 "Data model" and asserts they agree on every one. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- A writer-side exception for the schema step's row. The report's id 50 skeptic rejected that path,
  so the writer refuses below schema 4 for every id, the schema step's included.
- Calling the predicate from the walk, the reverse walk or the rollback's end. Those callers are
  `TOOL-dSafePassage-15`, `TOOL-dSafePassage-18` and `TOOL-dSafePassage-19`.
- `read_step_states` and its refusals, which stay as TOOL-dSafePassage-3 ships them.
- The step program `tools/govkit/steps/receipt_schema_4.py`, its up, down and witness.

### Edges

- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state`, its below-schema-4 refusal and the receipt section of the help page; without them there is no writer whose precondition this unit exports
- **hands-off** `TOOL-dSafePassage-15` — asking the predicate before every record the forward walk would persist, so a schema-3 receipt reaches the schema step's up
- **hands-off** `TOOL-dSafePassage-18` — asking the predicate after each down's re-read, so a down that lowers the receipt below schema 4 writes no row
- **hands-off** `TOOL-dSafePassage-19` — asking the predicate when the rollback's stamp and record are written after the schema step's down
- **hands-off** `TOOL-dSafePassage-35` — the minors batch of the round-1 audit of units 15 to 26, which reads this unit's criteria against the page sentence and the predicate's one call

## 4. Design

### Data model

The five shapes the arm grades, and the predicate's answer:

| Receipt | `test_steps_recordable` | `set_step_state` |
|---|---|---|
| `schema` 3, no `steps` (every receipt `update` writes before the step) | False | raises `Refusal` |
| `schema` 4, `"steps": []` (a fresh `apply`, TOOL-dSafePassage-3 S5) | True | appends the row |
| `schema` 4, no `steps` (a foreign writer's shape) | False | raises `Refusal` |
| `schema` 3, `"steps": []` (a foreign writer's shape) | False | raises `Refusal` |
| `schema` the string `"4"` | False | raises `Refusal` |

The predicate's rule is TOOL-dSafePassage-3's own field rule (its S2: "A receipt below schema 4
carries no `steps`"), read as a precondition rather than restated.

### Inventory

Minted: `test_steps_recordable` in `tools/govkit/upgrade_steps.py`, cell `py.function`, verb `test`
(`python tools/lexicon/lexicon.py --suggest test_steps_recordable --as py.function` printed OK on
2026-10-23). No conf key, no gate leg, no policy key. The refusal site in `set_step_state` is
TOOL-dSafePassage-3's anchor of `tools/govkit/refusal_join.py`, moved by no count here.

### Migration

None. The predicate adds no field and changes no receipt.

### Rollout

Live at landing. It builds at order 2, after TOOL-dSafePassage-3 (order 1), and shares
`tools/govkit/upgrade_steps.py` with TOOL-dSafePassage-2, -4, -7 and -20 at order 2, so the build
run sequences those passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **The writer accepts the schema step's own row below schema 4.** The id 50 skeptic rejected it: a
  writer that writes a field onto a receipt whose schema says the field does not exist is the
  laundering shape TOOL-dSafePassage-3 exists to refuse.
- **Each caller compares `schema` itself.** Three copies of one precondition beside the writer's own
  is the drift the charter's one-fact rule names; a caller that copied the test wrong would write a
  row the writer then refuses mid-walk.

## 5. Production-readiness checklist

- security: no new write path. The predicate reads only; the writer's refusal is unchanged in what it
  refuses.
- perf / scale: one dictionary read per call.
- error / empty / loading states: a receipt with no `schema` key reads False, and the writer refuses
  it as today.
- observability: the refusal text names the rule and the schema read.
- risks: a caller that writes without asking still meets the writer's refusal, the safe direction.
- testing: the `tools/govkit/selftest.py` arm of S4.
- migration: none.
- user docs: the receipt section of `help/upgrade-steps.md`, S3.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `test_steps_recordable` on the five shapes of §4 "Data model", it prints False, True, False, False,
  False in that order.
  Red when: the schema-3 receipt with `"steps": []` or the string schema reads True.
- **AC2** — When the same probe calls `set_step_state(receipt, "govkit/receipt-schema-4", None,
  "applied")` on each of the five shapes, it raises `Refusal` exactly on the shapes AC1 printed False
  for, and appends one row on the other.
  Red when: the writer and the predicate disagree on any shape, so a caller asking the predicate
  could still meet a refusal.
- **AC3** — When `git grep -n -e "def test_steps_recordable" -e "test_steps_recordable(" -- tools/govkit/upgrade_steps.py`
  runs, it prints one definition and a call inside `set_step_state`.
  Red when: `set_step_state` keeps a schema comparison of its own beside the predicate.
- **AC4** — When `git grep -n -e "Before schema 4" -e "govkit/receipt-schema-4" -- help/upgrade-steps.md`
  runs, the receipt section names both, saying no step row is written below schema 4.
  Red when: the page states no bootstrap rule.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `govkit selfcheck` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the arm runs the predicate and the writer over the five receipt shapes, its failing case staged by a copy of the writer whose schema test reads `>= 3` · none

What the arm does not check: whether a caller asks the predicate before it writes, which is each
caller's own criterion in `TOOL-dSafePassage-15`, `TOOL-dSafePassage-18` and
`TOOL-dSafePassage-19`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 50 (BLOCKER,
  item D-1, shared with id 1).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-35`; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-3's writer `set_step_state` in
`tools/govkit/upgrade_steps.py` (its spec, §4 Data model), whose own precondition this unit names.
`python tools/codebase-map/reuse_lookup.py "skip persisting a progress row when the receipt schema is
too old to hold it"` ranked `rows`, `row`, `skip` and `extract_row`, name-token matches with no
receipt precondition among them, so no existing seam fits beyond the writer itself; the writer is
unbuilt at the base, so the probe cannot rank it, which is where the hits and the specs disagree.
The recall probe found `TOOL-cMendedVintage-19`, the rule that a promoted repair sits beside the unit
it repairs, which places this unit at order 2.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
