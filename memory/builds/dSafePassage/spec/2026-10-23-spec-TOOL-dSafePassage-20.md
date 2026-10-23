# TOOL-dSafePassage-20 — the reader's `unlanded` is recorded as `null` at the step record's one writer

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-20-deviation-66.md](../build/2026-10-23-build-TOOL-dSafePassage-20-deviation-66.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 3** at HIGH, its item **D-4**. TOOL-dSafePassage-1's reader returns
`introduced` as the string `unlanded` for a row the default branch does not hold (its spec, §4,
lines 177-178), TOOL-dSafePassage-2 writes the reader's value into the progress row (§4, line 171),
and TOOL-dSafePassage-3's writer refuses an `introduced` that is neither 40-hex nor `None` (§4, line
112), so every walk over an unlanded row raises `Refusal`. That is gov first's main path: in the
prepared merge every new step is unlanded against the default branch. This unit is id 3's
promotion: one spelling across the four units, fixed at the one place every record passes, the
writer, so the reader keeps printing `unlanded` and the receipt keeps recording `null`.

## 2. Scope (IN)

- **S1** — One sentinel. The reader's `unlanded` is the module constant `UNLANDED` in
  `tools/govkit/upgrade_steps.py`, which `read_steps` returns and `upgrade_steps.py list` prints, so
  the string is spelled once. Observed by AC4.
- **S2** — The writer takes the reader's value. `resolve_recorded_introduced(value)` beside
  `set_step_state` returns a 40-hex value unchanged, `None` for `UNLANDED` or `None`, and raises
  `Refusal` naming the value for anything else. `set_step_state` calls it first, so its validator sees
  only its own domain, and the stored domain stays 40-hex or `null` (TOOL-dSafePassage-3 §4). A later
  record with the landed commit replaces the `null`, as the writer's keep-a-known-commit rule already
  allows. Observed by AC1 and AC2.
- **S3** — The arm feeds every output kind. A `tools/govkit/selftest.py` arm reads the rows
  `read_steps` returns over a scratch clone holding one landed row and one unlanded row (the shape of
  TOOL-dSafePassage-1's AC3), and passes each row's `introduced` through `set_step_state` on a schema-4
  receipt: no `Refusal`, the landed row recorded with its commit and the unlanded one with `null`.
  Observed by AC3.

## 3. Non-goals (OUT)

- The reader's derivation of `introduced` and its print of `unlanded`: TOOL-dSafePassage-1.
- Changing the walk or gov first. Both pass the reader's value to the writer unchanged, which is
  now legal.
- Filling a `null` once the row lands. The writer's rule already keeps a known commit and takes a
  known one over `null`.

### Edges

- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state` and its validator, the writer this unit's mapping sits in front of; without it there is no boundary to translate at
- **consumes-from** `TOOL-dSafePassage-1` — `read_steps` and its unlanded value, the reader whose every output kind the arm feeds through; without it there is no sentinel to map
- **hands-off** `TOOL-dSafePassage-8` — the source-mode walk in the prepared merge, which records every step this landing introduces with a null introducing commit through this mapping

## 4. Design

### Data model

| `introduced` handed to `set_step_state` | Recorded |
|---|---|
| a 40-hex commit | that commit |
| `UNLANDED`, the reader's `unlanded` | `null` |
| `None` | `null`, or the row's known commit kept |
| anything else | `Refusal` naming the value |

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the constant `UNLANDED` and the function
`resolve_recorded_introduced` (cell `py.function`, verb `resolve`, OK by
`python tools/lexicon/lexicon.py --suggest resolve_recorded_introduced --as py.function` on
2026-10-23). No conf key, no gate leg, no policy key. The new `raise Refusal` site is an anchor of
`tools/govkit/refusal_join.py`, armed by the §7 arm, and its `BRANCH_PIN` floor moves by one.

### Migration

None: no receipt at the base records a step.

### Rollout

Live at landing. It builds at order 2, after TOOL-dSafePassage-1 and TOOL-dSafePassage-3 (order 1), and
before TOOL-dSafePassage-8 (order 3). It shares `tools/govkit/upgrade_steps.py` with the other order-2
units, so the build run sequences those passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `tools/govkit/refusal_join.py`

### Alternatives rejected

- **The walk and gov first map the value before they call the writer**, the report's example. That
  is two copies of one mapping, and a third caller, the reverse walk, would need its own; the writer
  is the one boundary every record crosses (charter `[security]`, validate once at the write
  boundary).
- **The reader returns `None` for an unlanded row.** `upgrade_steps.py list` and TOOL-dSafePassage-1's
  AC3 print `unlanded`, and a `None` there cannot be told from a reader that found no commit.

## 5. Production-readiness checklist

- security: the writer's domain is unchanged; the mapping narrows a known sentinel and refuses the
  rest.
- perf / scale: one comparison per record.
- error / empty / loading states: an unknown value refuses with its text named.
- observability: `list` still prints `unlanded`; the receipt records `null`.
- risks: a later sentinel added to the reader would refuse at the writer until mapped, the loud
  direction.
- testing: the arm of S3 and the probes of §6.
- migration: none.
- user docs: N/A — TOOL-dSafePassage-3's receipt section already says an unlanded step records `null`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `resolve_recorded_introduced` on a 40-hex string, on `UNLANDED`, on `None` and on `"main"`, it
  returns the string, `None`, `None`, and raises `Refusal` naming `main`.
  Red when: `"main"` is mapped to `None` rather than refused.
- **AC2** — When the probe calls `set_step_state(receipt, "s1", "unlanded", "applied")` on a schema-4
  receipt, the row reads `"introduced": null`; a second call with a 40-hex commit for `s1` records
  that commit.
  Red when: the first call raises `Refusal`, as the writer does at the base of this build.
- **AC3** — When the §7 arm builds a scratch clone with one row landed on `main` and one on an
  unmerged branch and passes `read_steps`' rows through `set_step_state`, no `Refusal` is raised, the
  landed row records its 40-hex commit and the unlanded row `null`.
  Red when: any output kind of the reader is refused by the writer.
- **AC4** — When `git grep -n -F '"unlanded"' -- tools/govkit/upgrade_steps.py` runs, it prints the
  one line assigning `UNLANDED`.
  Red when: the reader or the writer spells the string a second time.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the arm passes every output kind of the reader through the writer, its failing case staged by a writer copy that calls its validator before the mapping · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by one

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 3 (HIGH, item
  D-4).

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-3's writer `set_step_state` and its validator, at the write
boundary every record crosses, with TOOL-dSafePassage-1's reader as the value's source.
`python tools/codebase-map/reuse_lookup.py "map a reader sentinel value to null at the receipt writer
boundary"` ranked `read`, `read_text`, `write`, `write_text` and `map_root`, name-token matches; no
existing seam fits beyond the two specs, which are unbuilt at the base.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
