# TOOL-dLoggedFlight-26 — every count and value the record arms assert over a shared fixture builder is derived from what the builder placed, on row kinds the record keeps

**Status:** SPECCED · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-27 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-22` retires eight Timeline row kinds, and its S5 table is the inventory of the arms
that read them. A probe by NAME built that table, so it cannot see an assertion on a COUNT or a VALUE
that a retired row carries. The spec audit of units 21 to 24, round 1, confirmed five such assertions
as H1, a HIGH, each of which reds once unit 22 is built as written:

1. `- values withheld: 4` in `test_record_ac4_classes` (`tools/runlog/selftest.py:4344-4345`). Two of
   the four intruders ride retired rows: the `command` on a `verb` row (`:4278`) and the `free text` on a
   `workflow` label (`:4281`).
2. The vocabulary-short liveness block (`:4350-4358`) indexes `push-decision`, which unit 22 S4 deletes,
   and asserts `- values withheld: 5`.
3. The shaped-value map (`:4328-4331`) takes its `utc` value, minute 12, from the appended `push` rows
   (`:4259-4263`), and its `sha` value, twelve `a`s, from the `gate` rows' head (`:4264-4265`).
4. `- values withheld: 5` in `test_schema_ac1_render_then_grade` (`:5257-5258`).
5. `test_record_ac6_cap`'s `500 · shown 60 · elided 440` (`:4414-4416`) and its widest record's `505`
   (`:4443-4445`), which counts the five wide `workflow` rows `build_big_model` adds (`:4376-4377`).

Each is a literal typed beside a builder that placed its carrier. This unit moves every intruder onto a
row kind unit 22 keeps, and derives every such literal from what the builder placed, so a later
retirement that moves a carrier moves the expectation with it.

Every code line cited here was read at `f7bf9d2f` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The carriers. In `build_class_model` (`tools/runlog/selftest.py:4247`) the `command` intruder
  moves to the `units` cell of an appended `commit` row, and the `free text` intruder moves to the
  `unit` cell of an appended `brief` row. The `session` intruder stays on a `dispatch` row's `unit`, and
  the `absolute path` on a `decision` ledger entry's `ref`. Every intruder on a read field then rides a
  row kind or table that `TOOL-dLoggedFlight-22` keeps. Observed by AC1.
- **S2** The placements. `build_class_model` returns `read_placed` as a fifth value: one entry per
  intruder it puts on a field the renderer reads, naming the row kind or table and the field, appended
  at the line that places it. Its two callers, `test_record_ac4_classes` (`:4319`) and
  `build_schema_fixture` (`:5168`), take it, and `SCHEMA_FX` keeps it beside the model. Observed by AC1.
- **S3** The withheld counts. `test_record_ac4_classes` expects `values withheld` to read
  `len(read_placed)`. `test_schema_ac1_render_then_grade` expects it to read `len(read_placed)` plus
  the one UUID carrier that arm adds. Observed by AC1 and AC2.
- **S4** The liveness block. It drops the last member of `anomaly-kind` from a schema copy, a
  vocabulary a kept table carries, in place of `push-decision`. It expects that member in no cell, and
  `values withheld` to read `len(read_placed)` plus the number of `anomaly-kind` cells that carry the
  member in the unmodified render, counted from that render through `parse_record_markdown`. Observed by
  AC4.
- **S5** The shaped map. Its `utc` value is `derive_iso` of the model's first `commit` event's time,
  and its `sha` value is that event's sha shortened by `derive_short_sha`, in place of minute 12 and
  twelve `a`s. The map's other values are `TOOL-dLoggedFlight-22`'s to change. Observed by AC1.
- **S6** The cap arm. `test_record_ac6_cap` reads each `events` expectation from the model it renders.
  The event count is the number of timeline entries whose kind the Timeline row layouts of
  `RECORD_SCHEMA` declare. At the nominal bounds, `shown` is twice `TIMELINE_EDGE` and `elided` is the
  difference, and the widest record's leading count is its model's event count. Observed by AC2.
- **S7** The simulated retirement. Before this unit's commit, the build renders both builders' models
  with every kind `TOOL-dLoggedFlight-22` S1 retires filtered out of the timeline, and checks that each
  expectation S3, S5 and S6 derive still matches the render. Observed by AC3.
- **S8** The documented check. A class record,
  `memory/gotchas/retirement-inventory-misses-readers-by-value.md`, names the class: an inventory of what
  reads a retired thing, found by name, misses an assertion on a count or value the retired thing
  carries. Its instances are this audit's B1 loop, H1's five literals and M5's fixture. Its check for a
  spec audit is S7's: simulate the retirement on each shared builder and diff every literal an arm
  asserts. Its anchors are `memory/builds/` and `tools/runlog/selftest.py`, and the gotchas index is
  re-rendered. Observed by AC5.

## 3. Non-goals (OUT)

- The retirement itself, the typed vocabulary lists and the map's `duration`, `verb`, `checks` and
  `label` values. `TOOL-dLoggedFlight-22` owns them.
- The `withheld rows` counts. `TOOL-dLoggedFlight-27` owns that fact and derives its expectations.
- A hygiene check that refuses a spec whose retirement inventory is by name only. It changes
  `memory/HYGIENE.md`, a governance carrier, so M3's second veto makes it the owner's, and it is parked
  in the build's run-state file on 2026-09-16. S8 is the half this unit can carry.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-25` — `test_record_ac4_classes` with its window loop removed,
  which this unit edits next.
- **hands-off** `TOOL-dLoggedFlight-22` — carriers on kept kinds and derived expectations, so that
  unit's retirement moves no literal an arm asserts.
- **hands-off** `TOOL-dLoggedFlight-27` — `read_placed` and the class model, over which that unit derives
  the `withheld rows` counts.

## 4. Design

A retirement edits a builder, and an arm asserting a literal over that builder is a second copy of what
the builder placed. Deriving the literal at the placement makes the builder the one source, so the next
retirement's inventory needs to find the builder rather than every number beside it.

Moving the intruders ahead of unit 22 also separates two proofs that were tangled. The withheld count
proves the renderer withholds a read field. It should not depend on which row kinds survive a
retirement.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `read_placed` | builder return value | none |
| `retirement-inventory-misses-readers-by-value` | gotcha class record | `memory/gotchas/` |

### Files touched (estimate)

`tools/runlog/selftest.py`, `memory/gotchas/retirement-inventory-misses-readers-by-value.md` and
`memory/gotchas/INDEX.md`.

### Alternatives rejected

- Add the five assertions to unit 22's S5 table with typed replacements, the audit's direct fix:
  rejected by M3's rule, since the class recurs on the next retirement and the audit's left-shift closes
  it here.
- Keep the intruders on `verb` and `workflow` rows and restate each count after unit 22: rejected, since
  the count then records a retirement rather than the renderer's withholding.
- Count withheld values by re-rendering with withholding disabled: rejected, since that arm would share
  the renderer's predicate with the thing it grades.

## 5. Production-readiness checklist

- security — the four intruders stay on read fields, so every withholding path they prove is kept.
- perf / scale — N/A — test code and one class record.
- error / empty / loading states — an arm whose derivation reads zero placements reds, since the
  class model always places four.
- observability — each failure names the expectation and the placements it was derived from.
- risks — a derivation that reads the renderer's own counter would pass vacuously; S3 reads the
  builder's list instead.
- testing — AC1 staged RED on a builder copy; AC3 is the simulated retirement.
- migration — N/A — test code only.
- user docs — N/A — no user-facing surface; the class record is the documented check.

## 6. Acceptance criteria

- **AC1** — When `test_record_ac4_classes` renders `build_class_model`'s model, `values withheld` reads
  `len(read_placed)`, no entry of `read_placed` names a `verb` or `workflow` row, and the shaped map's
  `utc` and `sha` are the model's first `commit` event's.
  Red when: a count or value differs, or an intruder rides a retired kind. Staged RED by a builder copy
  that places one more intruder on a read field without recording it in `read_placed`.
  figure: DERIVED — every expected number is computed from the builder's placements at observation time.
- **AC2** — When `git grep -n -e '"- values withheld: [0-9]' -e '500 · shown' -e '505 · shown' -- tools/runlog/selftest.py`
  runs, it finds nothing, and `test_schema_ac1_render_then_grade` and `test_record_ac6_cap` compute each
  expectation from the model they render.
  Red when: the grep finds a typed literal, or an expectation is not read from the rendered model.
- **AC3** — When S7's probe renders `build_class_model`'s and `build_big_model`'s models with the kinds
  `TOOL-dLoggedFlight-22` S1 retires filtered out, every expectation S3, S5 and S6 derive matches the
  render.
  Red when: an expectation that held on the unfiltered model fails on the filtered one. The widest
  record's overflow liveness is exempt, since unit 22 S5 widens a kept row for it.
  cost: a one-time probe at build, recorded in the acceptance ledger and not kept as an arm, since after
  unit 22 the filter removes nothing.
- **AC4** — When the liveness block drops the last `anomaly-kind` member on a schema copy, that member
  is in no cell and `values withheld` reads the count S4 derives, and
  `git grep -n 'vocab"\]\["push-decision"\]' -- tools/runlog/selftest.py` finds nothing.
  Red when: the member renders, the count differs, or the grep finds the old block.
- **AC5** — When `python tools/memory-tree/gotchas.py --for-paths tools/runlog/selftest.py` runs, it
  lists `retirement-inventory-misses-readers-by-value`.
  Red when: the record is absent from the list.

## 7. Gates

`runlog selftest` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's builder copy recording no placement · floor unchanged unless the rewritten arms change the assertion count, re-declared with a comment naming this unit if they do

## 8. Open questions

- **F1** Where does H1 close? Options: typed rows added to unit 22's S5 table; expectations derived
  from each builder's placements in a unit of their own; both. RESOLVED (agent, 2026-09-16, delegated):
  derived expectations in their own unit, landing before unit 22, since M4 promotes a HIGH to a unit
  whose mechanism closes it and a typed row is the shape H1 found.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H1 of the spec audit of units 21 to 24, round 1, at
  the loop's BOUNDED exit, with the audit's left-shift for H1 as its mechanism.

## 10. Reuse audit

The seams are `build_class_model`, `build_big_model`, `build_schema_fixture` and `parse_record_markdown`
in `tools/runlog/selftest.py`, and the gotcha catalogue read by `tools/memory-tree/gotchas.py`, all
existing. `tools/codebase-map/reuse_lookup.py "derive a test expectation from what a fixture builder
placed"` returned name-stem candidates, `build_run_model` and `expected_by_target` in
`tools/memory-recall/bench.py` among them, and none derives an arm's expectation from a builder's
placements, so no existing seam fits. The recall query returned this build's own audit and spec
records, and rows that match on words only: `TOOL-aWalkedCorpus-3`'s recall floor, derived as a
one-retirement worst case over a corpus rather than a fixture, and `PLAY-aCandidStub-1`, which refutes
moving the charter's §10 checklist into `gotchas/` and warns that a generic record's derived anchors
select nothing. S8's record names two concrete anchors for that reason. Neither row derives an arm's
expectation.

Recall terms used: inventory retirement readers literal fixture builder withheld count placement derived expectation selftest arm
