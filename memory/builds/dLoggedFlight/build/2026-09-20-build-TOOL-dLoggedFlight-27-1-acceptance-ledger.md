# Acceptance ledger — TOOL-dLoggedFlight-27

**Serves:** journal TOOL-dLoggedFlight-27

Tier-2 · node d · 2026-09-20 · the build pass of the withheld-rows fact, against spec rev-3. The spec
MOVED in this pass, to rev-3: inventorying the readers of the counts this unit adds, which rev-2's own
section 9 asked for, turned up one more found by VALUE. S8 and AC6 are that fold, written before the
code that needed them.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: `tools/runlog/selftest.py`
was not run, imported or copied under any name, and neither was any other suite, gate leg or bar. The
change was observed instead by one throwaway Python script kept outside the repository, which imported
the kit's `record`, `model` and `extract` modules alone and built a SYNTHETIC model carrying one event
of every retired kind plus a second `gate` and two more `idle`, so no expected count was 1. That is the
substituted-value class stated plainly: the probe grades the real renderer over a model of the right
SHAPE, never over `build_class_model`, whose only definition sits in the suite module this pass may not
reach. Every arm below is therefore owed to the post-build run with the break that stages it RED.

## The criteria

**Evidences:** TOOL-dLoggedFlight-27

- AC1 — `render_record` over a synthetic model — MET on the probe, OWED as an arm. The Timeline's new
  `withheld rows` fact rendered `verb 1 · push 1 · push-refused 1 · gate 2 · compact 1 · limit 1 ·
  idle 3 · workflow 1`, which is every member of `RETIRED_EVENTS` in that constant's order, each with
  the count of that kind's events on the model rendered, read back off the markdown and compared
  against a `Counter` over the model's own timeline. The distinct counts were `1`, `2` and `3`, so a
  typed count of 1 per kind — unit 22 AC1's figure, and H2 of the spec audit — could not have passed.
  The three Coverage counts the unit adds to the declaration rendered the model's own join and session
  figures. Owed: `test_record_ac1_withheld_rows`, staged RED by typing any count beside the builder or
  by reordering the constant, and the liveness that the class model holds MORE retired events than the
  one per kind its builder appends, which is what makes the fixture non-trivial.
  MET at the post-build run: `test_record_ac1_withheld_rows` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC2 — `render_record` over four coverage shapes — MET on the probe, OWED as an arm. With the
  transcripts `not-local`, the gates journal `dead`, the pushes journal `absent` and the idle gaps
  unjudged, seven kinds rendered `-` and `verb` rendered a count off a driver reading `partial`; the
  Coverage `sessions` slots read `-` while both journal-start counts read integers. With the driver
  `absent` too, `verb`, `journal starts` and `unjoined starts` all read `-`, and every slot of the
  five Summary facts did. On a third copy with the transcripts `partial` and the gaps unjudged, the
  three transcript kinds read counts while `idle` read `-` — the one cell where the judgement and
  `COUNTED_STATES` disagree, and `partial` was asserted to be IN `COUNTED_STATES` so that `-` is the
  judgement's decision and not an empty population. Both staged breaks were reproduced on the probe: a
  renderer copy ignoring the declaration for `gate` wrote a digit for a dead journal, and a copy
  mapping `idle` onto the transcripts coverage state reddened on the third copy alone while the first
  two still passed. Owed: `test_record_ac1_withheld_rows`, staged RED by those same two wrappers,
  which the arm installs around `build_counted_values` and `derive_counted_sources` and restores in a
  `finally`.
  MET at the post-build run: `test_record_ac1_withheld_rows` is GREEN there too, on the same 1543
  passed and 0 failed.
- AC3 — `git show HEAD~1 -- tools/runlog/selftest.py` — MET, run in this pass. The build commit's
  hunks over the suite carry no line of `test_record_ac10_unknown_counts`: a grep of that diff for
  `record AC10` and for the function's own name exits 1 and prints nothing, so not one of its count
  assertions was edited, moved or brought in as context. The new arm was deliberately placed above
  `TRANSCRIPT_FACTS` rather than beside that function, because git's three lines of hunk context would
  otherwise have carried its closing count assertion into the diff. Its `not-local` model still renders
  the five Summary facts as it expects: the probe reproduced that cell, with every slot of all five
  reading `-` once the declared source went unread.
- AC4 — `check_count_sources(RECORD_SCHEMA)` — MET on the probe, OWED as an arm. Over the live schema
  it returned an empty refusal list and printed an inventory of 33 `{int}` slots outside the nine facts
  it covers, among them `Summary/own commits[0]`, `Summary/units served[0]` and `Summary/sources
  present[0..1]` — the population section 3 excludes, enumerated rather than described. Each of the
  four staged copies was refused exactly once, naming the slot: the copy without the `gate` entry
  named `Timeline/withheld rows slot 3 declares no source`; the copy naming the source `ledger` named
  that slot and that source; the copy with an entry keyed to `("Summary", "phase", 0)` named
  `Summary/phase slot 0 is no {int} slot of a fact the schema declares`; and the copy whose retired
  kind list gained a member named `Timeline/withheld rows slot 8 declares no source`. Owed:
  `test_record_ac1_withheld_rows`, staged RED by any one of those copies passing.
  MET at the post-build run: the arm is GREEN, on the same 1543 passed and 0 failed.
- AC5 — `test_record_model_fields` — OWED to the post-build run, not observable here. The arm reads
  its workflow run's count back out of `withheld rows`, expecting the model's own `workflow` event
  count where that model's transcripts read a state in `COUNTED_STATES` and `-` otherwise, both read
  from the model rather than typed. Its fixture is the suite's own and cannot be reached in this pass.
  Owed: `test_record_model_fields`, staged RED by typing the count or by dropping the `COUNTED_STATES`
  branch so the `-` case renders a digit.
  MET at the post-build run: `test_record_model_fields` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC6 — `test_record_ac1_real_model` — OWED to the post-build run, not observable here. That arm
  compared two WHOLE rendered Timelines, so this unit's fact was always going to move it, and it
  spells neither `withheld rows` nor `count_sources` — the reader-by-value class. The comparison now
  narrows to the Timeline's tables and its `events` count, which still may not move, and the arm gains
  the assertion that `withheld rows` DOES, which is the fact's liveness over a REAL model. Owed:
  `test_record_ac1_real_model`, staged RED by a renderer that leaves the fact's counts at zero, which
  makes the two renders agree where they must differ.
  MET at the post-build run: `test_record_ac1_real_model` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.

## What else the pass carried

- **The probe is a synthetic model, and that is the whole of what it does not prove.** It grades the
  shipped `render_record`, `check_count_sources`, `build_counted_values` and `derive_counted_sources`
  over a model of the right shape; it does not grade `build_class_model`, the landed fixture's real
  journals, or the halving step a wider record may reach. Two properties were reasoned about rather
  than measured and land at the post-build run: that the class model's coverage rows carry a `state`
  key for every member of `SOURCE_NAMES`, which `measure_coverage` sets unconditionally; and that its
  transcripts row carries `sessions` and `extracts`, which the Coverage fact already reads through
  `.get(..., 0)`.
  ANSWERED: both hold. `runlog selftest` printed
  `1543 passed, 0 failed (1543 assertions, floor 1543)`, so the arms resting on the class model's
  coverage rows and its transcripts row are GREEN and neither reasoned property was wrong.
- **The probe caught a real defect before any arm existed.** `dict(sources, **{key: value})` raises
  `TypeError: keywords must be strings` when the keys are TUPLES, which every `count_sources` key is.
  Two of AC4's four staged copies were written that way and would have killed the whole arm at its
  first line, under a floor that would then have reported an arm gone missing rather than a broken
  one. They are now `{**sources, key: value}`, with the reason written beside them.
- **Nineteen assertions arrive and the floor moves to 1404**, with the arithmetic beside the constant:
  14 in the new arm, its 3 decoy checks, and one each inside two arms that already existed. The
  previous move was a LOWERING to 1385, which no pass has been able to verify by running the suite;
  this pass's arithmetic is relative to that figure and does not re-derive it, so if 1385 was wrong
  this is wrong by the same amount. The post-build run is where both are settled.
  SETTLED: `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`. The
  floor has risen from this unit's 1404 to 1543 with the units after it, and executed equals floor
  exactly, so neither the 1385 this arithmetic was relative to nor the chain built on it ever put
  the floor above the true total.
- **Five helpers arrive, one in the kit and four in the suite**, plus four nested functions inside the
  new arm. Every one was checked with `lexicon.py --suggest ... --as py.function`:
  `build_withheld_template`, `derive_int_slots`, `derive_counted_sources`, `build_counted_values` and
  `check_count_sources` in `record.py`; `read_withheld_rows`, `read_fact_slots`,
  `render_fact_expectation` and `build_schema_copy` in the suite; and `build_state_copy`, `read_shape`,
  `build_ignoring_gate` and `derive_idle_by_coverage` nested in the arm, which the naming leg grades
  too. One module constant arrives, `RETIRED_SOURCES`, and `derive_known` leaves.
- **A retired kind with no declared source reds rather than crashing.** `RETIRED_SOURCES` is read with
  a guard when the declaration is built, so a member added to `RETIRED_EVENTS` and forgotten leaves its
  slot undeclared for `check_count_sources` to refuse by name, instead of raising a `KeyError` at
  import and taking every reader of the module with it.
- **The rule now has one statement and the prose has none.** `build_summary_facts`' `known` test and
  its `derive_known` closure are gone, which is what `TOOL-dLoggedFlight-30` observes on the renderer.
  The `COUNTED_STATES` comment, which said the states were the TRANSCRIPTS', was rewritten in the same
  commit: an amendment that left that half standing would have had one constant described two ways.
- **The kit README names the declaration and refuses to copy it.** Its unknown-values paragraph names
  `count_sources`, the nine facts by name, the `-` rule, the `idle` asymmetry and
  `check_count_sources`, and says in so many words that the per-slot pairing is the declaration's own
  and is not copied there. A first draft did copy it, which is the two-answers class the checklist
  names.
- The dossier edit is byte-NEUTRAL by measurement: `memory/map/features/runlog.md` was 20358 bytes
  before this unit and is 20358 after, against check 6's cap of 20480. The sentence naming
  `check_count_sources` was paid for by three trims inside the same bullet. Check 6 is held under the
  pre-commit `--staged` run, so both figures were measured with `wc -c`. Units `-20` and `-23` still
  owe prose there, against 122 bytes of headroom.
- **No claim was added to the dossier and none was needed.** A dossier cannot claim a Python symbol —
  its `[claims]` block carries no symbol tier — and `[paths] globs` already covers `tools/runlog/**`.
  `memory/map/generated/symbols.json` moves in this commit because the new functions are symbols;
  `MAP.md` and `inventories.json` do not, because no inventory key moved.
- `tools/runlog/SKILL.template.md` and the rendered Skill were not touched: the Skill names the
  record's sections but not the Timeline's facts, so `scan_skill_copies` has nothing new to hold. No
  kit version moves and no other kit was reached.
- **The new counts give no withheld time back, and that was checked rather than assumed.** The
  bug-class checklist selects `withheld-value-recovered-from-a-derived-one` over this diff, and its
  question is which rendered values took a withheld one as an input. A kind's count reads `kind`
  alone and never `t`: it is the length of a filter over the timeline, so no arithmetic over it, over
  `duration`, over the `events` count or over the window bounds places any one retired event. The
  values the retirement withheld are times; what this unit publishes is cardinality, which is why
  `TOOL-dLoggedFlight-22` section 5 could keep it at all.
- **The two staged breaks edit no file, so the stale-bytecode class cannot reach them.** Both wrap a
  shipped function in memory and restore it in a `finally`; nothing is written to `record.py` and
  re-imported, which is the shape that lets a second edit inside one second run the first edit's
  cached bytecode.
- **This pass's own prose is unreviewed surface.** No audit runs beside it, so spec rev-3's S8, AC6
  and section 9, the dossier edit, the README paragraph and this ledger are read for the first time at
  the closing diff review.

## Owed to the post-build gate run

- `runlog selftest` — `test_record_ac1_withheld_rows` (new), `test_record_model_fields` and
  `test_record_ac1_real_model`, at a floor of 1404, plus every arm that renders a record and compares
  it with another render or with its twin: `test_record_ac3_shape`, `test_record_ac4_classes`,
  `test_record_ac6_cap`, `test_record_template_pairs`, `test_record_placement_windows`,
  `test_source_ac7_discovered_reach` and the four `test_schema_*` arms, each of which now grades a
  record carrying one more Timeline fact.
- `lexicon naming predicates` — the five new kit functions, the four new suite helpers and the four
  nested ones, and the `VERB_OFFENDER_PIN` equality that grades them.
- `codebase-map coverage + freshness` — that the regenerated artifacts rode the same commit as the
  dossier edit, which they did.
- `memory hygiene` — check 6 over the dossier's bytes, and check 23 over this ledger.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`,
so every arm listed above is GREEN. `lexicon naming predicates` is GREEN in 3.9 s over the new
names and the `VERB_OFFENDER_PIN` equality, `codebase-map coverage + freshness` in 2.5 s and
`memory hygiene` in 29.1 s. The run's one RED, `govkit selftest`, is on none of these legs: its 30
failing assertions are the IDENTICAL set `origin/main` carries, pre-existing, untouched by this
build and being fixed in a separate session. It is not called green here.
