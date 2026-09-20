# Acceptance ledger — TOOL-dLoggedFlight-22

**Serves:** journal TOOL-dLoggedFlight-22

Tier-2 · node d · 2026-09-20 · the build pass of the retirements, against spec rev-4. The spec moved
in this pass: rev-4 adds three readers the rev-3 inventory still missed and the arm that takes the
record half of the one arm this unit retires whole. Section 9 records each.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: the runlog self-test module
was not run, imported or copied under any name, and neither was any other suite, gate leg or bar. The
change was observed instead by one throwaway Python script kept outside the repository, which imports
the kit's `record` and `model` modules alone and builds a SYNTHETIC model carrying one event of every
retired kind, three intruders on kept kinds, an anomaly per kind with a time, an epoch per source and
an owner turn. That is the substituted-value class stated plainly: the probe grades the real renderer
over a model of the same shape, never over `build_class_model` or the landed fixture, whose only
definitions sit in the suite module this pass may not reach. Every arm below is therefore owed to the
post-build run with the break that stages it RED, except AC3 and AC6, which are `git grep` commands
run here.

## The criteria

**Evidences:** TOOL-dLoggedFlight-22

- AC1 — `render_record` over a synthetic model holding one event of every `RETIRED_EVENTS` kind —
  observed in this pass. The rendered Timeline carried `brief`, `commit`, `dispatch`, `merge` and
  `phase` rows and nothing else, and that set equalled both `TIMELINE_EVENTS` and the kinds the
  schema's Timeline row layouts declare, so all three were pinned to one another. `values withheld`
  read `3`, the three intruders the model put on a `commit` row's `units` and on a `dispatch` and a
  `brief` row's `unit`, and not one dropped event. The liveness was measured rather than assumed:
  rendering the SAME model with every retired event taken out of it moved neither the row set nor the
  withheld count, so the drop is what the renderer does and not what the fixture failed to carry.
  Owed: `test_record_ac4_classes` for the class model and `test_record_ac1_real_model` for the idle
  fixture's real model, staged RED by returning one retired kind to the Timeline row layouts of
  `RECORD_SCHEMA`, which puts its rows back and leaves the pinned triple disagreeing.
  MET at the post-build run: `test_record_ac4_classes` and `test_record_ac1_real_model` are both
  GREEN, inside `runlog selftest`'s `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC2 — `render_record` over that same model, reading the two table headers — observed in this pass.
  The Anomalies table rendered `#`, `kind`, `subclass` and the Coverage table `#`, `source`, `state`,
  `lines`, `bad`. Every Anomalies row still led with its ordinal, checked against `1..n` over the
  model's own list. The liveness: that model held a time on every anomaly and an epoch on every
  source, so both columns dropped a value there was something to render for. The Anomalies aggregate's
  key columns moved with the header, from `(2, 3)` to `(1, 2)`, which the probe exercised through the
  unaggregated table only — the aggregated path is owed to `test_record_ac6_cap`. Owed:
  `test_record_ac4_classes` and `test_record_ac6_cap`, staged RED by restoring either column to the
  schema, which makes the rendered header a column wider than the arm's.
  MET at the post-build run: `test_record_ac4_classes` and `test_record_ac6_cap` are both GREEN,
  inside `runlog selftest`'s `1543 passed, 0 failed (1543 assertions, floor 1543)`, so the
  aggregated path holds too.
- AC3 — `git grep -n -e scan_owner_times -e UTC_TOKEN_RE -e TWIN_ROW_RE -e "owner turn's second" -- tools/runlog memory/map/features/runlog.md` —
  MET, run in this pass: exit 1, nothing printed. The second half was observed too: a model whose
  `commit` event carries the exact time of an owner turn it holds rendered its record, and that time
  is in the record, where the retired refusal would have raised instead. `record.py` defines neither
  `scan_owner_times` nor `derive_clean_rc` any more, read off the imported module with `hasattr`.
- AC4 — `read_class_values` over the rendered record, and two staged schema copies — observed in this
  pass, replicated in the probe. Every shaped class but `digest`, which the probe does not commit a
  journal for, was reached at a SLOT that declares it: a table column, a Timeline row layout or a fact
  template's placeholder, with the class regexes taken from the leg's own `build_record_checks` rather
  than a second copy. The two breaks reproduced: a schema copy keeping `push-decision` named both of
  its members as unreached, and a copy keeping `verb` named `verb` — twice, once with the retired
  regex that matches no rendered cell and once with a regex that matches several, the second being the
  discrimination the criterion asks for, since a grader reading cells would have called that one
  reached. Owed: `test_record_ac4_classes`, whose vocabulary list is `sorted(RECORD_SCHEMA["vocab"])`
  and whose union spans the class model's render and the three `build_placement_models` makes, staged
  RED by either copy.
  MET at the post-build run: `test_record_ac4_classes` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC5 — `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-22.md` S5 and S6 against
  the suite source — the floor reads 1385 with a `LOWERED 1392 -> 1385 by TOOL-dLoggedFlight-22`
  comment naming every arm and half that moved, the module defines no `test_record_ac9_owner_times`,
  and each arm in S5's table is edited as the table says. The floor's own reader was exercised here by
  a script that replicates `parse_floor_raise` over the suite's source TEXT: it found the new move,
  its `to` equalled the declared floor, its block named a unit id, and its arithmetic
  `4 + 3 + 1 + 11 + 1 - 21 - 3 - 2 - 1 = -7` evaluated to the delta. **The 1385 is DERIVED BY HAND,
  not read off a run**, because no pass may run the suite; it is a lower bound, so a hand count under
  the true total still passes and one over it fails. Owed: the whole suite at that floor, and
  `test_record_placement_windows`, staged RED by typing a figure the arithmetic does not reach.
  MET at the post-build run: `runlog selftest` printed
  `1543 passed, 0 failed (1543 assertions, floor 1543)`, so the whole suite ran at its floor and
  `test_record_placement_windows` is GREEN. The hand-derived 1385 has since been raised to 1543 by
  the units after this one, and executed equals floor exactly, so no step of that hand arithmetic
  ever put the floor above the true total.
- AC6 — `git grep -n -e "verb token" -e "check numbers" -e "THREE LISTS" -e "pre-push hook's decisions" -e "Timeline .rc." -e "rc of an END" -- tools/runlog/README.md tools/runlog/record.py memory/map/features/runlog.md` —
  MET, run in this pass: exit 1, nothing printed. It reds honestly: its first run after the record.py
  edit printed one hit, a sentence this pass had just written using the phrase `pre-push hook's
  decisions` to say the list had retired, which was rephrased.

## What else the pass carried

- **Three readers the rev-3 inventory missed, and all three by VALUE.** `test_fresh_ac4_three_shapes`
  picks the Coverage row for the transcripts out of `scan_record_rows` by a cell COUNT of six, which
  S2 makes five; nothing in it names a column, a class or a retired identifier. `parse_floor_raise`
  matches only the word `RAISED`, and S6's floor is the first in this suite to move DOWN, so the
  reader would have found the previous raise and graded a figure nothing declares. And
  `test_record_placement_windows` types `TOOL-dLoggedFlight-25` while grading whichever unit moved the
  floor last — already broken by `TOOL-dLoggedFlight-26`, which moved the floor and left the literal
  behind. That third one is this build's own class one level up, and it now reads the id out of the
  comment. Its arithmetic grader takes a negative total.
- **The retired arm's own liveness had a population of two.** `test_zz_model_idle_invariant` asserts
  that the models the arms built include at least two holding both an idle gap and tool calls;
  `test_model_ac19_idle` and `test_record_ac9_owner_times` were the two, so retiring the second outright
  would have left that liveness over a population of one — the exact defect
  `memory/gotchas/green-bar-over-a-population-of-one.md` names. `test_record_ac1_real_model` takes the
  record half of the retired arm and keeps that fixture's model in the count. This was reasoned from the
  source, not measured: no pass may run the suite to read `MODEL_SEEN` back. If some other arm already
  fed a second such model, the new arm is redundant rather than wrong.
- **The `cell` and `uuid` refusal carriers moved to kinds the record keeps.** The `cell` variant rides
  a `commit` row's `source`; the `uuid` and `data escape` variants ride a Decisions entry whose `ref`
  is a path under the build folder, whose file segment the `ref` class admits as a lowercase UUID.
  Both were observed on the probe: the `ref` class accepted that path and refused a free name, the
  renderer withheld the UUID and counted it as the placements plus one, and the leg refused a `gits`
  source cell under the `cell` rule and accepted the clean record with nothing refused.
- **The cap arm's widening moved from a retired row to a kept one.** `build_big_model(wide=True)` used
  to widen 20-character verb names and append five 40-character workflow labels; it now fills each
  `commit` and `merge` row's `units` cell with every unit id the model owns. Observed on the probe over
  a 500-row commit-heavy model: at the nominal bounds the record overflows, after halving it fits, and
  it says it now shows fewer than the nominal 60 rows. A plain 500-row model still renders
  `500 · shown 60 · elided 440` at the nominal bounds, which is what `measure_timeline_events` derives
  for that arm. The widest record's event count falls from 505 to 500 by derivation, with no figure to
  re-declare, because the five appended workflow rows went with the kind.
- **What the probe does not prove.** It grades the real renderer over a synthetic model. It does not
  grade `build_class_model`, the landed fixture's history, `build_placement_models`' three states, or
  any arm's own text. Four properties of the real fixtures were therefore reasoned about rather than
  measured, and all four land at the post-build run: that the class model's render reaches every member
  of `opened-by` and `closed-by` across the union with the placement renders; that its first `phase`
  event's phase, its ledger entry count and its `record_window` duration are the shaped values those
  slots carry; that the landed fixture's `commit` and `merge` events carry `FX_UNIT1` in their `units`
  cell; and that the plain 500-row cap model still fits at the nominal bounds with kept kinds alone.
  ANSWERED: all four hold. `runlog selftest` printed
  `1543 passed, 0 failed (1543 assertions, floor 1543)`, which is every arm that grades the class
  model's render and the placement renders, the landed fixture's `units` cells and the plain
  500-row cap model; none of them failed.
- **`build_placement_models` is now called twice a run**, once by `test_record_placement_windows` and
  once by record AC4's union. Three more fixture histories per run is the price of reaching a
  vocabulary only a Summary fact carries, which F2 ratified in rev-3 against a typed exclusion.
- **The dossier edit is byte-NEGATIVE by measurement**: 20435 bytes before this unit and 20358 after,
  against check 6's cap of 20480. The owner-time refusal's Gaps bullet was replaced by one naming what
  the record now omits, and the copied-lists sentence lost the push decisions. Check 6 is held under
  the pre-commit `--staged` run, so both figures were measured with `wc -c`. Units `-20`, `-23` and
  `-27` still owe prose there, against 122 bytes of headroom.
- **No claim was added or removed in the dossier**, so `memory/map/generated/symbols.json` moves alone:
  the retired identifiers left a file the `tools/runlog/**` glob already claims, and `RETIRED_EVENTS`,
  `RETIRED_FIELDS`, `read_class_values` and `test_record_ac1_real_model` arrive under the same glob.
- **Three identifiers arrive**, `RETIRED_EVENTS` and `RETIRED_FIELDS` as constants and
  `read_class_values` as a function leading with the declared verb `read`; the new arm leads with
  `test` like every other. No kit version moves and no other kit was touched.
- **This pass's own prose is unreviewed surface.** No audit runs beside it, so the spec's rev-4, the
  README and dossier rewrites and this ledger are read for the first time at the closing diff review.

## Owed to the post-build gate run

- `runlog selftest` — at a floor of 1385: `test_record_ac1_real_model`, `test_record_ac4_classes`,
  `test_record_ac6_cap`, `test_record_model_fields`, `test_record_copied_sets`,
  `test_record_ac10_unknown_counts`, `test_record_placement_windows`, `test_fresh_ac4_three_shapes`,
  `test_schema_ac1_render_then_grade` and `test_schema_ac2_refusals`, plus every arm that grades the
  class model's record through `build_schema_fixture` — `test_schema_ac4_cost_and_index` and
  `test_schema_ac5_runs` — whose staged variants are built by predicate off bytes that now carry eight
  fewer Timeline rows and two fewer table columns. The floor itself is the figure most likely to be
  wrong, and it is wrong in the safe direction only if it is under.
- `runlog record schema` — the leg compiles `RECORD_SCHEMA` itself, so the dropped vocabularies,
  shaped classes and columns reach it as data; no committed record exists in this tree to regrade.
- `lexicon naming predicates` — `read_class_values` and the two constants.
- `codebase-map coverage + freshness` — the regenerated `symbols.json` rode this commit with the
  dossier edit.
- `memory hygiene` — check 6 over the dossier at 20358 bytes, check 21 over this ledger's bindings and
  check 23 over its criterion lines.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`,
so every arm listed above is GREEN and the floor question is settled: executed equals floor
exactly, so the figure was never above the true total. `runlog record schema` is GREEN in 0.7 s
and `lexicon naming predicates` in 3.9 s. The run's one RED, `govkit selftest`, is on none of
these legs: its 30 failing assertions are the IDENTICAL set `origin/main` carries, pre-existing,
untouched by this build and being fixed in a separate session. It is not called green here.
