# Acceptance ledger — TOOL-dLoggedFlight-26

**Serves:** journal TOOL-dLoggedFlight-26

Tier-2 · node d · 2026-09-20 · the build pass of the derived fixture counts, against spec rev-2. The
spec did not move in this pass: rev-2 already carried the round-7 audit's disposal, which handed the
render-level mutation proof to `TOOL-dLoggedFlight-28` and wrote AC3 as owed.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: `tools/runlog/selftest.py`
was not run, imported or copied under any name, and neither was any other suite, gate leg or bar.
The change was observed instead by one throwaway Python script kept outside the repository, which
imported the kit's `model` and `record` modules alone and built a SYNTHETIC model carrying the same
placements the class model now carries. That is the substituted-value class stated plainly: the probe
proves the MECHANISM over a model of the same shape, never over `build_class_model` itself, whose
only definition sits in the suite module this pass may not reach. Every arm below is therefore owed
to the post-build run with the break that stages it RED, except AC5, which has a direct command.

## The criteria

**Evidences:** TOOL-dLoggedFlight-26

- AC1 — `build_class_model` — the builder now returns `read_placed` as a fifth value, one
  `(carrier, field)` entry appended at each line that puts an intruder on a field the renderer reads:
  a `commit` row's `units`, a `dispatch` row's `unit`, a `brief` row's `unit` and the Decisions
  entries table's `ref`. No entry names a `verb` or a `workflow` row, and the two intruders that used
  to ride them moved onto the `commit` and `brief` rows, both kinds `TOOL-dLoggedFlight-22` keeps.
  `test_record_ac4_classes` now expects `values withheld` to read `len(placed)` and takes the shaped
  `utc` and `sha` from the model's first `commit` event through `derive_iso` and `derive_short_sha`.
  Observed on the probe over a synthetic model with those four placements: the rendered count equalled
  the placement count, the derived `utc` and short sha both reached the file, no intruder did, and a
  liveness reading confirmed the derived pair was neither the last row's time nor the carrier commit's
  own sha. The staged RED was reproduced there too: a builder copy placing one more intruder on a read
  field without recording it made the rendered count exceed `len(placed)` by exactly one. Owed:
  `test_record_ac4_classes`, staged RED by that same builder copy.
- AC2 — `git grep -n -e '"- values withheld: [0-9]' -e '500 · shown' -e '505 · shown'` — run over
  `tools/runlog/selftest.py` after the edit, it exits 1 and prints nothing; before it, it printed the
  five literals the spec's section 1 names. `test_schema_ac1_render_then_grade` now reads
  `len(fx["placed"]) + 1`, the builder's placements plus the one UUID carrier that arm appends, and
  `test_record_ac6_cap` computes each `events` expectation from the model it renders — the event count
  through `measure_timeline_events`, which counts the entries whose kind the Timeline row layouts of
  `RECORD_SCHEMA` declare, `shown` as twice `TIMELINE_EDGE` and `elided` as the difference, with the
  unit, anomaly and entry counts read off the model's own lists and the elided-middle row's time read
  off its own timeline. Owed: `test_record_ac6_cap` and `test_schema_ac1_render_then_grade`, staged
  RED by typing any one of those figures back.
- AC3 — `test_record_kind_sweep` — NOT MET IN THIS PASS and not observable in it. The sweep renders
  both shared builders' models with one kind of event removed at a time, and both builders are defined
  only inside the suite module, which the owner's instruction of 2026-09-13 bars every route to before
  VERIFYING. Per spec rev-2 section 9 the arm lands with `TOOL-dLoggedFlight-28`. Owed:
  `test_record_kind_sweep`, staged RED by an arm copy that types the `values withheld` count at the
  whole model's value, so a render with one kind removed disagrees with it. The widest record's
  overflow liveness stays exempt, since `TOOL-dLoggedFlight-22` S5 widens a kept row for it.
- AC4 — `git grep -n 'vocab"\]\["push-decision"\]' -- tools/runlog/selftest.py` — run after the edit
  it exits 1 and prints nothing, so no copy of the old block survives. The block now drops the last
  member of `anomaly-kind`, a vocabulary the Anomalies table carries, and expects `values withheld` to
  read the placements plus the number of `anomaly-kind` cells that carry the member in the unmodified
  render, counted by `measure_class_cells`, which matches each rendered table to the schema table
  whose header it repeats rather than typing a column index. Observed on the probe: the member was in
  no cell of the dropped render, and the rendered count rose from the placement count by exactly the
  cells the unmodified render carried. That count was read there through the record's JSON twin while
  the suite's helper reads its markdown, so the two readers are independent. Owed:
  `test_record_ac4_classes`, staged RED by restoring the member to the copy or by typing the count.
- AC5 — `python tools/memory-tree/gotchas.py --for-paths tools/runlog/selftest.py` — MET, run in this
  pass: it lists `retirement-inventory-misses-readers-by-value`, whose record was written in this
  commit and whose anchors `memory/builds/` and `tools/runlog/selftest.py` are both live paths. The
  catalogue index was re-rendered with `gotchas.py --write` in the same commit, so check 17 has
  nothing stale to find.

## What else the pass carried

- **The probe is a synthetic model, and that is the whole of what it does not prove.** It grades the
  real renderer over a model of the class model's placement shape; it does not grade the class model,
  the landed fixture's history, or the elision and aggregation the real record may reach. Two
  properties of the real fixture were therefore reasoned about rather than measured: its 17 anomalies
  sit under `LIST_BOUND`, so the Anomalies table renders unaggregated and the cells the liveness block
  counts are the cells the withheld count was made from; and its first `commit` row is rendered,
  which the arm's existing shaped `units` expectation already depends on and which the new liveness
  check makes loud if the event is ever absent. Both land at the post-build suite run.
- **Three assertions arrive and the floor moves to 1392**, with the reason beside the constant. They
  are the empty-derivation guard the spec's section 5 asks for and its two livenesses: the builder's
  placements counted against its intruders, the model's timeline asserted to hold the commit event the
  shaped pair is derived from, and the unmodified render asserted to carry the vocabulary member the
  liveness block drops — without which the count that block expects would be the placements alone and
  the whole block would pass over a population of nothing. No new arm, so no decoy check moves.
- **A third caller had to widen.** `test_record_template_pairs` takes the builder's fifth value as
  `_placed` and uses none of it; the spec's S2 names the two callers that TAKE the placements, and the
  arity change reaches every caller whether it wants the value or not.
- **`TOOL-dLoggedFlight-22`'s S5 table already anticipated this.** Its rows for the withheld count,
  the liveness block, the shaped pair and `build_big_model` each read "no edit here" and name this
  unit's S3 to S6 as the mechanism, so nothing in that spec is left describing code this pass
  removed. Its `build_big_model` row widens the `commit` rows' units cell in place of the five wide
  `workflow` rows, which `measure_timeline_events` follows without a figure to re-declare.
- **The carriers were chosen so the two proofs stay separate.** A withheld count proves the renderer
  withholds a read field. It should not also record which row kinds survived a retirement, which is
  what a count over a `verb` row and a `workflow` label was doing.
- The dossier edit is byte-NEGATIVE by measurement: 20448 bytes before this unit and 20435 after,
  against check 6's cap of 20480. The new `gotcha-classes` claim cost 52 bytes and was paid for by a
  duplicated report-only sentence in the redaction paragraph, the word "unusually" in the bounds
  sentence, and a trailing clause in the schema paragraph. Check 6 is held under the pre-commit
  `--staged` run, so both figures were measured with `wc -c`. Units `-20`, `-22`, `-23` and `-27`
  still owe prose there, against 45 bytes of headroom.
- `memory/map/generated/inventories.json` and `MAP.md` move in this commit as well as `symbols.json`,
  because a new file under `memory/gotchas/` is a `gotcha-classes` inventory key and the runlog
  dossier claims it. That is the fold of the spec audit's S-obs 1, recorded in spec rev-2.
- **Two helpers arrive**, `measure_timeline_events` and `measure_class_cells`, both leading with a
  declared verb and both checked with `lexicon.py --suggest ... --as py.function`, so
  `VERB_OFFENDER_PIN` does not move. No module-body constant arrives.
- `tools/runlog/record.py`, the rendered Skill and the kit README were not touched: nothing this unit
  changes is visible outside the suite's own fixtures and arms. No kit version moves.
- **This pass's own prose is unreviewed surface.** No audit runs beside it, so the class record, the
  dossier edit and this ledger are read for the first time at the closing diff review.

## Owed to the post-build gate run

- `runlog selftest` — `test_record_ac4_classes`, `test_record_ac6_cap`,
  `test_schema_ac1_render_then_grade` and `test_record_template_pairs`, at a floor of 1392, plus every
  arm that reads the class model's record through `build_schema_fixture`: `test_schema_ac2_refusals`,
  `test_schema_ac4_cost_and_index` and `test_schema_ac5_runs`, whose staged variants are built by
  predicate off the rendered bytes and now grade a record carrying two more Timeline rows.
- `codebase-map coverage + freshness` — the leg grades that the regenerated artifacts rode the same
  commit as the dossier claim, which they did, and that the new `gotcha-classes` key is claimed.
- `memory hygiene` — checks 17, 18 and 19 over the new class record, and check 23 over this ledger.
