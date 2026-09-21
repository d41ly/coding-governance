# TOOL-dLoggedFlight-27 — the Timeline's `withheld rows` fact counts each retired kind from a declared source, and renders `-` for a source the model did not read

**Status:** CLOSED · rev-3 · 2026-09-20 · node d · Tier-2 · base 4cf0944d · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-dLoggedFlight-1-runlog-2f11f32d.md](../build/2026-09-20-build-TOOL-dLoggedFlight-1-runlog-2f11f32d.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30 |
| [2026-09-20-build-TOOL-dLoggedFlight-27-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-dLoggedFlight-27-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30 |
| [2026-09-20-review-TOOL-dLoggedFlight-25-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-dLoggedFlight-25-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-22` at rev-2 retires eight Timeline row kinds and adds a `withheld rows` fact that
renders each retired kind followed by its count. The spec audit of units 21 to 24, round 1, confirmed
two defects in that fact.

H4, a HIGH. The fact renders a count whether or not the kind's source was read, and unit 22's §5 says a
run with no retired events renders every count `0`. `TOOL-dLoggedFlight-9` S4 at rev-7 ruled that an
UNKNOWN value is absent, never the value that reads clean, and the renderer implements that ruling for
the transcript counts through `COUNTED_STATES` (`tools/runlog/record.py:109`, the test at `:627-635`).
The retired kinds come from sources whose coverage can read unknown. `compact`, `limit` and `workflow`
enter only from transcript extracts (`tools/runlog/model.py:1663-1669`). `idle` exists only when idle
gaps were judged, which needs the transcripts `present` (`model.py:1682`, `:1690`). `gate`, `push` and
`push-refused` come from their journals, and `verb` from the driver journal. So a run whose transcripts
read `not-local`, or whose gates journal is dead, would commit `0` for kinds nobody counted.

H2, a HIGH. Unit 22 AC1 requires a count of 1 for each retired kind over `build_class_model`, which
starts from the landed fixture's real model (`tools/runlog/selftest.py:4251-4253`). That model already
holds the fixture's driver verbs, gate lines and landing push before anything is appended, so AC1
cannot pass, and it states the number with no `figure:` sub-field.

This unit owns the fact. Each count declares the source it is counted from, a count whose source was not
read renders `-`, and every expected count is derived from the model the arm renders.

Every code line cited here was read at `f7bf9d2f` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The fact. The Timeline gains `withheld rows`, whose template reads each member of
  `RETIRED_EVENTS` in that constant's order, each followed by `{int}`. A kind's count is the number of
  events of that kind on the model's timeline, which the model has already bounded to the run's window.
  This takes `TOOL-dLoggedFlight-22` rev-2 S1's fact clause; that unit keeps the retirement and the
  dropping of retired events before rows are built. Observed by AC1.
- **S2** The declaration. `RECORD_SCHEMA["count_sources"]` maps each `{int}` slot of nine facts to the
  source it is counted from, keyed by section, label and position:
  - `withheld rows`: `transcripts` for `compact`, `limit` and `workflow`; `driver` for `verb`; `gates`
    for `gate`; `pushes` for `push` and `push-refused`; and `idle` for `idle`;
  - the Summary's `owner turns`, `usage main`, `usage agent`, `usage workflow` and `attributed calls`:
    `transcripts` for every slot;
  - the Coverage's `sessions`, both slots: `transcripts`. And `journal starts`, both slots, and
    `unjoined starts`: `driver`, since the join they count is `derive_journal_join` over the driver
    journal's own invocations (`tools/runlog/model.py:1492`).

  `idle` names the Coverage `idle` entry's judgement rather than a coverage state, and that judgement
  is NARROWER than `COUNTED_STATES` by exactly one state: it needs the transcripts `present`
  (`tools/runlog/model.py:1682`) while a counted slot admits `partial` too. The asymmetry is
  deliberate. A `partial` extract is a lower bound and says so in Coverage, so a count from it is
  still a count; an unjudged run carries no idle rows at all, so its idle count would be a zero
  nobody measured. Observed by AC2 and AC4.
- **S3** The rule. A declared slot renders `-` unless its source's coverage state is in
  `COUNTED_STATES`, or, for `idle`, unless idle gaps were judged. `build_summary_facts`' `known` test
  (`tools/runlog/record.py:632-635`) is replaced by that lookup, so the five Summary facts keep their
  present behaviour and the rule is stated once. Observed by AC2 and AC3 for the five facts' VALUES.
  The REPLACEMENT — the old spelling gone from the renderer, and the lookup rather than the old test
  deciding each value — is observed by `TOOL-dLoggedFlight-30`: the two predicates agree on every
  model these criteria build, so no criterion here can tell them apart, which is H2 of the spec audit
  of units 25 to 27.
- **S4** The declaration check. `check_count_sources(schema)` refuses, naming the slot, an entry keyed
  to no `{int}` slot of a fact, a source that is neither in `SOURCE_NAMES` nor `idle`, and an `{int}` slot
  of the nine facts with no entry. A kind added to `RETIRED_EVENTS` therefore adds a slot that refuses
  until its source is declared. It also PRINTS, as an inventory rather than a refusal, every `{int}`
  slot of `RECORD_SCHEMA` outside those nine that carries no entry — so the undeclared population is
  enumerated on every run, a newly undeclared count shows up in the diff, and no prose has to carry a
  description of a derived set. The self-test arm calls it. Observed by AC4.
- **S5** The expectations. The arm observing S1 renders a copy of `build_class_model`'s model whose
  driver, gates, pushes and transcripts coverage read `present` and whose idle gaps are judged, and
  derives each kind's expected count from that model's timeline at observation time, never a typed
  number. This replaces unit 22 rev-2 AC1's count of 1. The three Coverage facts S2 adds are derived
  the same way, from that model's own join and session counts rather than from a number in the arm.
  Observed by AC1.
- **S6** The model-fields arm. `test_record_model_fields` reads its workflow run in `withheld rows`,
  expecting the model's `workflow` event count where that model's transcripts read a counted state and
  `-` otherwise, read from the model. Unit 22 retires that arm's rendered workflow row. Observed by AC5.
- **S7** The docs. The kit README's paragraph on unknown values names `count_sources` and the
  `withheld rows` fact, and the runlog dossier's PROSE names `check_count_sources`. A dossier cannot
  CLAIM a Python symbol: its `[claims]` block carries no symbol tier, the symbol tier feeds the recall
  corpus and never the ratchet (`tools/codebase-map/map_extractors.py:128`), and `[paths] globs`
  already covers `tools/runlog/**`. NOT OBSERVED: prose. What the `codebase-map coverage + freshness`
  leg grades at the close is that the regenerated map artifacts are committed in the same commit,
  which is a different assertion and is worth stating as itself.
- **S8** The real-model arm. `test_record_ac1_real_model` renders the idle fixture's model twice —
  once whole, once with every retired kind taken off its timeline — and asserts that the two
  Timelines are EQUAL. This unit's fact is the one Timeline value those two renders must DIFFER on,
  so that comparison narrows to the Timeline's tables and its `events` count, which still may not
  move, and gains the assertion that `withheld rows` does. That is the fact's liveness over a REAL
  model, and the arm was found by VALUE rather than by name: nothing in it spells the fact's label.
  Observed by AC6.

## 3. Non-goals (OUT)

- Which kinds retire, and dropping their rows. `TOOL-dLoggedFlight-22` owns both.
- Declaring a source for every count the record renders. What stays OUT is the counts read from git,
  the run-state file or the build folder — `own commits`, `units served` and `sources present` — since
  their sources cannot read unknown, so no `-` rule applies to them. The three Coverage counts that DO
  come from the transcripts and the driver journal are IN, at S2: `sessions`, `journal starts` and
  `unjoined starts` each committed a clean zero with its source unread, which is M3 of the spec audit
  of units 25 to 27. Of the Coverage `{int}` slots only `idle gaps` already read `-`, by a different
  mechanism — the model leaves `near_owner` None when the gaps are unjudged, which `derive_count`
  renders absent. The arm's header states that an undeclared `{int}` slot outside S2's nine facts is
  not graded, and S4 prints that population on every run rather than leaving it to this sentence.
- The time slots and their sources. `TOOL-dLoggedFlight-20` owns them.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-16` — `COUNTED_STATES` as that unit leaves it, with `stale`
  outside it, which S3 reads unchanged.
- **consumes-from** `TOOL-dLoggedFlight-26` — `build_class_model` with its intruders on kept kinds, over
  which S5 derives the counts.
- **consumes-from** `TOOL-dLoggedFlight-22` — `RETIRED_EVENTS`, the retired kinds dropped before rows
  are built, and its S1 fact clause, which moved here.
- **hands-off** `TOOL-dLoggedFlight-30` — the `count_sources` lookup that replaces the `known` test,
  whose replacement that unit observes on the renderer and by re-pointing a declared source, which no
  criterion here can see.

## 4. Design

The fact exists to say what happened per kind in place of the rows. A count from a source nobody read
says something that did not happen, so the fact carries the same unknown rule as every other count from
those sources, and the rule reads a declaration rather than being restated per fact.

The five Summary facts move onto the declaration too. They already render `-` by one hand-written test,
and a second hand-written test for a second fact is how the rule would drift between them.

The three Coverage counts from those same sources move with them, and that is what makes the first
paragraph's claim true rather than nearly true: `sessions` from the transcripts and the two journal
starts from the driver journal rendered a clean zero with their source unread, exactly like the fact
this unit was promoted for. A concession that misdescribes its own excluded population is a decision
nobody made, so the population is now spelled in §3 by name.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `count_sources` | schema key | `RECORD_SCHEMA` |
| `RETIRED_SOURCES` | module constant | `record.py`, beside `RETIRED_EVENTS` |
| `check_count_sources` | function | `py.function`, led by `check` |
| `derive_int_slots` | function | `py.function`, led by `derive` |
| `derive_counted_sources` | function | `py.function`, led by `derive` |
| `build_counted_values` | function | `py.function`, led by `build` |
| `build_withheld_template` | function | `py.function`, led by `build` |
| `withheld rows` | Timeline fact label | `RECORD_SCHEMA` fact template |

### Files touched (estimate)

`tools/runlog/{record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`, with the
regenerated map.

### Alternatives rejected

- Render every count, reading `0` as unread: rejected by `TOOL-dLoggedFlight-9` S4 at rev-7.
- Retire the `withheld rows` fact: rejected by M3's rule, since the fact is what a reader keeps of the
  retired rows.
- A per-fact `known` test beside the existing one: rejected, since two hand-written tests of one rule
  is the drift S3 removes.
- Strip the base model's retired events so each count is 1, the audit's second route for H2: rejected,
  since `build_class_model` has other readers, and a derived count needs no edit to them.

## 5. Production-readiness checklist

- security — no new value reaches the record; a count is an integer or `-`.
- perf / scale — one lookup per declared slot; one count per retired kind.
- error / empty / loading states — a run with no retired events renders `0` only for a kind whose
  source was read, and `-` otherwise.
- observability — `withheld rows` beside the Coverage table says both what happened and what was read.
- risks — a new count fact outside S2's nine is not graded, as §3 states; S4 prints that population
  on every run so the ungraded set is enumerated rather than described.
- testing — each AC staged RED on a renderer copy or a schema copy.
- migration — no run record is committed in this tree.
- user docs — the kit README's paragraph on unknown values.

## 6. Acceptance criteria

- **AC1** — When `render_record` renders S5's copy of `build_class_model`'s model, the `withheld rows`
  fact lists every member of `RETIRED_EVENTS` in order, each followed by the number of that kind's
  events on the rendered model's timeline.
  Red when: a member is missing, out of order, or its count differs, or the arm types a count.
  figure: DERIVED — each count is read from the model's timeline at observation time.
- **AC2** — When `render_record` renders a copy of that model whose transcripts read `not-local`, whose
  gates journal reads `dead`, whose pushes journal reads `absent` and whose idle gaps are not judged,
  `withheld rows` reads `-` for `compact`, `limit`, `workflow`, `idle`, `gate`, `push` and `push-refused`,
  and a count for `verb` while the driver reads `partial`. The Coverage `sessions` slots read `-` on
  that copy, and `journal starts` and `unjoined starts` read counts while the driver is `partial`.
  With the driver `absent` too, `verb`, `journal starts` and `unjoined starts` read `-`, and every
  slot of the five Summary facts reads `-`. On a third copy whose transcripts read `partial` with the
  idle gaps unjudged, `compact`, `limit` and `workflow` read counts while `idle` reads `-` — the one
  cell where the judgement and `COUNTED_STATES` disagree, from a single source read, and the cell
  `test_record_ac10_unknown_counts` already fixtures at `tools/runlog/selftest.py:4809`.
  Red when: a digit renders for a slot whose declared source was not read, `verb` reads `-` while
  the driver is `partial`, or on the third copy `idle` renders a digit or the three transcript kinds
  read `-`. Staged RED twice: a renderer copy that ignores `count_sources` for `gate`, and a copy
  that maps `idle` onto the transcripts coverage state like the rest, which reds on the third copy
  while the first two still pass.
- **AC3** — When `git show HEAD -- tools/runlog/selftest.py` is read at this unit's build commit, no
  count assertion of `test_record_ac10_unknown_counts` is in its hunks, and that arm's `not-local` model
  renders the five Summary facts as it expects.
  Red when: one of its count assertions is edited, or a Summary fact renders differently on that model.
- **AC4** — When `check_count_sources` reads `RECORD_SCHEMA`, it refuses nothing. On a copy without the
  `gate` entry, a copy naming the source `ledger`, a copy with an entry keyed to no slot, and a copy
  whose `RETIRED_EVENTS` gains a member, it refuses naming that slot.
  Red when: any staged copy passes.
- **AC5** — When `test_record_model_fields` renders its model, `withheld rows` reads that model's
  `workflow` event count where its transcripts read a state in `COUNTED_STATES`, and `-` otherwise.
  Red when: the value differs from the one read from the model, or the arm types it.
- **AC6** — When `test_record_ac1_real_model` renders the idle fixture's model and the same model
  with every retired kind taken off its timeline, the Timeline's tables and its `events` count are
  equal across the two renders and their `withheld rows` facts differ.
  Red when: a table or the event count moves, or the two `withheld rows` facts are equal.
  figure: DERIVED — both values are read off the two renders at observation time.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC2's renderer copy ignoring `gate`'s entry, AC2's copy mapping `idle` onto the transcripts coverage state, and AC4's four schema copies · floor raised by the arm count

## 8. Open questions

- **F1** Where is the unknown rule for the new counts stated? Options: a per-kind test inside the fact's
  renderer; a declared source per count slot read by one lookup; retire the fact. RESOLVED (agent,
  2026-09-16, delegated): a declared source per slot, the audit's left-shift for H4, covering the five
  Summary facts that already carry the rule, since one declaration cannot disagree with itself.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H4 and H2 of the spec audit of units 21 to 24,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-22` rev-2 S1's `withheld rows` clause,
  its AC1 count and its §5 empty-state line.
- rev-2 · 2026-09-20 · S2 · S3 · S4 · S5 · S7 · §3 · §4 · §5 · §7 · AC2 · the disposal of the spec audit of
  units 25 to 27, round 1. Promoted elsewhere: H2 to `TOOL-dLoggedFlight-30`, which observes that the
  `known` test is gone from the renderer and re-points a declared source, so §3 declares the handoff.
  Folded: M2, S2 states that the `idle` judgement is narrower than `COUNTED_STATES` by one state and
  why, and AC2 gains the transcripts-`partial` cell where the two disagree with a staged copy that
  maps `idle` onto the coverage state; M3, the three Coverage counts from the transcripts and the
  driver journal join S2's declaration, S5 derives them, §3 names the excluded population by fact
  instead of misdescribing it, and S4 prints every undeclared `{int}` slot as an inventory; M4, S7
  stops saying a dossier CLAIMS a Python symbol and states what the map leg actually grades.
- rev-3 · 2026-09-20 · S8 · AC6 · §2 Inventory · the build pass. Inventorying the readers of the
  counts this unit adds, as rev-2's own §9 asks, turned up one more found by VALUE:
  `test_record_ac1_real_model` compares two whole rendered Timelines, so the fact makes an arm that
  spells neither `withheld rows` nor `count_sources` red. S8 narrows that comparison and turns the
  difference into the fact's liveness over a real model; AC6 observes it.

## 10. Reuse audit

The seams are `COUNTED_STATES` and `build_summary_facts` in `tools/runlog/record.py`, the model's
coverage block in `tools/runlog/model.py`, and `build_class_model` in `tools/runlog/selftest.py`, all
this build's. `tools/codebase-map/reuse_lookup.py "an unknown count renders absent when its source was
not read"` returned name-stem candidates only, `render_record` and `read_journal` among them, and no
seam declares a source per count, so S2 extends `COUNTED_STATES`' existing use rather than a new seam.
The recall query returned M6 of the first closing diff review, which set the rule for the transcript
counts, `TOOL-dLoggedFlight-9` S4's ruling, and this audit's H4.

Recall terms used: unknown count COUNTED_STATES coverage not-local dead journal withheld rows reads clean zero transcripts
