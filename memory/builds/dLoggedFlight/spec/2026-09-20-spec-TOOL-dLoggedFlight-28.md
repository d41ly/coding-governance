# TOOL-dLoggedFlight-28 — every expectation the record arms derive from a shared fixture builder is re-checked against a render with one kind of event removed

**Status:** CLOSED · rev-2 · 2026-09-20 · node d · Tier-2 · base 4cf0944d · streams tooling · order 29

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-dLoggedFlight-28-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-dLoggedFlight-28-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 25 to 27, round 1, confirmed B1, a BLOCKER, in `TOOL-dLoggedFlight-26`.

That unit's S7 requires the build to render both shared fixture builders' models with every kind
`TOOL-dLoggedFlight-22` retires filtered out, and to check that each expectation its S3, S5 and S6
derive still matches the render. Both builders live only in the runlog kit's self-test module —
`build_class_model` at `tools/runlog/selftest.py:4264` and `build_big_model` at `:4378`, with no other
definition under `tools/`. The build brief's "Every unit" block closes every route to them before
VERIFYING and closes the workarounds by name, and its step 4 escape, an AC written as owed to the
post-build run, is refused by AC3's own `cost:` sub-field. So the observation could only be made by
breaking a standing owner instruction, or booked as met without being made.

The observation is worth keeping, so it becomes an ARM rather than a one-shot probe. Once it is an
arm the retirement filter is the wrong parameter: after `TOOL-dLoggedFlight-22` drops the retired
kinds before rows are built, a filter over those kinds removes nothing and the arm cannot fail. This
unit sweeps the kinds the model's timeline actually holds, one at a time, which subsumes the
retirement case and stays able to fail after every unit of this build has landed.

Every code line cited here was read at `63a37d1c` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The sweep. `test_record_kind_sweep` in the runlog kit's self-test module renders
  `build_class_model`'s model once as its base, then, for each distinct event kind on that model's
  timeline, renders the copy `build_kind_removed(model, kind)` returns and checks that every
  expectation `TOOL-dLoggedFlight-26` S3 and S5 derive still matches its own render. `build_kind_removed`
  returns a model with every event of that kind dropped from the timeline, built through the same
  path the base render reads, never by editing a rendered fact. Observed by AC1.
- **S2** The swept set and its liveness. The arm derives the swept set from the model's own timeline,
  never from a typed list or a retirement constant, and prints each swept kind beside the number of
  events it removed. Three liveness assertions, because a sweep that removes nothing reads exactly
  like a sweep that found nothing wrong: the timeline holds more than one kind; the removals PARTITION
  it, each swept kind taking at least one event and the counts summing to its length with the base
  model left as it was; and every kind the base render shows a Timeline row for moves the rendered
  bytes when it is swept. The third read "every copy's render differs from the base render" until
  rev-2 measured otherwise. An `owner` event is dropped before a row is built and is counted in no
  fact (`tools/runlog/record.py:795`), so removing that kind is invisible to the render BY
  CONSTRUCTION, and an assertion over every copy would have reddened on the one kind the renderer is
  designed to ignore. Observed by AC1 and AC2.
- **S3** The wide model. The same sweep runs over `build_big_model`'s model at the nominal bounds,
  where the expectations are `TOOL-dLoggedFlight-26` S6's derived `events`, `shown` and `elided`
  counts. The widest record's overflow liveness is exempt, exactly as `TOOL-dLoggedFlight-26` AC3
  states it, since `TOOL-dLoggedFlight-22` S5 widens a kept row for it. Observed by AC3.
- **S4** The floor. `ASSERTION_FLOOR` rises by this arm's assertion count, with a RAISED comment
  naming this unit and the arithmetic that reaches the new value. Observed by AC4.
- **S5** The docs. The kit README's self-test paragraph states what the sweep proves and what it does
  not: that no expectation over the two shared builders is a typed literal, and nothing about arms
  over any other fixture. No dossier claim is added — the arm is a Python symbol, the dossier's
  `[claims]` block carries no symbol tier (`tools/codebase-map/map_extractors.py:128`), and its
  `[paths] globs` already covers `tools/runlog/**`. NOT OBSERVED: prose.

## 3. Non-goals (OUT)

- The derivations themselves. `TOOL-dLoggedFlight-26` builds them; this unit mutates their input and
  re-checks them, and a derivation this arm finds wrong is a defect in that unit's code.
- The retirement, `RETIRED_EVENTS` and which kinds retire. `TOOL-dLoggedFlight-22` owns all three,
  and this arm reads none of them, which is what makes it correct before and after that unit lands.
- Typed expectations over any other fixture in the suite. The sweep covers the two builders
  `TOOL-dLoggedFlight-26` derives from, and the arm's header says so.
- A spec-audit check that refuses an acceptance criterion naming a suite or a gate leg while carrying
  neither `permission:` nor a `New arm:` attribution, which is B1's class left-shift. It needs its
  rule in `memory/TEMPLATE-SPEC.md`, a governance carrier, so BUILD-METHOD M3's second veto makes it
  the owner's; it is parked in the build's run-state file on 2026-09-20.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-26` — the derived expectations of its S3, S5 and S6 and the
  `read_placed` list they are derived from, which this arm mutates and re-checks; with typed
  expectations in their place the sweep would assert nothing.

## 4. Design

The probe B1 refused was parameterized twice wrongly. It needed the suite module at a moment the
suite may not run, and the thing it filtered stops existing in the unit that follows. Mutation is the
parameter that survives both: an expectation derived from what a builder placed must track any change
to what the builder placed, and removing one kind of event is the smallest change that can tell a
derivation from a literal. A typed expectation reds on the first swept kind that carries its carrier,
and a derived one follows the render.

The liveness half is not decoration. A sweep whose removals never reach the render is the vacuous
selector this repo reds gates for, and the corpus already carries the same lesson from a different
angle: `DEPL-aTetheredConvoy-5` records that a guard deriving its population from a lossy source
cannot tell zero-of-zero from clean. So the arm prints what it removed and asserts that each removal
moved the rendered bytes.

`TOOL-dLoggedFlight-22` AC5 already re-reads the same five expectations, but it reads the SOURCE and
asks whether each one is written as a derivation. That is a shape check over text. This arm asks
whether the derivation actually tracks its input, which no reading of the source answers.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `test_record_kind_sweep` | function | `py.function`, led by `test` |
| `build_kind_removed` | function | `py.function`, led by `build` |
| `read_sweep_expectations` | function | `py.function`, led by `read` |
| `measure_killed` | function | `py.function`, led by `measure` |

### Files touched (estimate)

`tools/runlog/selftest.py` and `tools/runlog/README.md`.

### Alternatives rejected

- Keep the one-shot probe and declare the two builders under `permission:`, the audit's second route:
  rejected by M3's rule, since the observation is then made by nobody — this run may not make it and
  no arm carries it afterwards.
- Parameterize the arm by `RETIRED_EVENTS`, the audit's first route as written: rejected, since that
  constant's kinds are dropped before rows are built once `TOOL-dLoggedFlight-22` lands, so the
  filter removes nothing and the arm joins the could-not-fail class charter §7 exists against.
- Re-render with the derivations disabled and compare: rejected, since the arm would then share the
  predicate it grades, which is the guard-reads-the-corrupted-state shape.
- Import the suite module from a build-time script under another name: rejected, since the build
  brief bars exactly that by name.

## 5. Production-readiness checklist

- security — N/A — test code only, over synthetic fixtures.
- perf / scale — one render per swept kind on each of the two models; the arm prints the render count
  so the cost is visible rather than inferred.
- error / empty / loading states — a model whose timeline holds one kind sweeps once; an empty swept
  set reds rather than passing silently.
- observability — each failure names the swept kind, the expectation and both values.
- risks — a swept kind no expectation reads passes for that kind and says nothing; S2's
  render-differs assertion, over the kinds the base render shows a row for, is what keeps such a pass
  from reading as coverage, and the partition assertion beside it is what keeps a sweep over one kind
  from reading as a sweep.
- testing — AC1 and AC3 staged RED on arm copies that type an expectation, AC2 on a
  `build_kind_removed` copy that returns the model unchanged.
- migration — N/A — test code only.
- user docs — the kit README's self-test paragraph.

## 6. Acceptance criteria

- **AC1** — When `test_record_kind_sweep` runs over `build_class_model`'s model, the swept set equals
  the distinct event kinds of that model's timeline, and every expectation `TOOL-dLoggedFlight-26` S3
  and S5 derive matches the render of each copy `build_kind_removed` returns.
  Red when: an expectation fails on a copy, a kind on the timeline is not swept, or the swept set is
  empty. Staged RED by an arm copy that types the `values withheld` count at the base render's value,
  which must fail on the first swept kind carrying an intruder while the base render still passes.
  figure: DERIVED — the swept set and every expectation are read from the model at observation time.
- **AC2** — When the arm sweeps, every kind the base render shows a Timeline row for renders a
  document differing from the base, each swept kind removed at least one event, the removal counts
  sum to the timeline's length with the base model unmoved, and `build_kind_removed` is called once
  per swept kind.
  Red when: a rendered kind's copy renders byte-identically to the base, a swept kind removed
  nothing, the counts do not sum to the timeline's length, or the base model moved under the sweep.
  Staged RED by a `build_kind_removed` copy that returns the model unchanged, which reds on all four
  at once rather than passing every expectation.
- **AC3** — When the sweep runs over `build_big_model`'s model at the nominal bounds, the `events`,
  `shown` and `elided` expectations `TOOL-dLoggedFlight-26` S6 derives match each copy's render.
  Red when: one of the three fails on a copy, or the arm types any of them. The widest record's
  overflow liveness is exempt, as `TOOL-dLoggedFlight-26` AC3 states. Staged RED by an arm copy that
  types the event count at the base model's value.
- **AC4** — When `ASSERTION_FLOOR` in the runlog kit's self-test module is read after S4, its newest
  RAISED comment names `TOOL-dLoggedFlight-28` and its arithmetic reaches the declared value. The
  suite run that grades the count itself is this spec's `New arm:` line.
  Red when: the floor moves with no comment naming this unit, or the comment's arithmetic does not
  reach the value declared beside it.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's and AC3's arm copies that type an expectation, and AC2's `build_kind_removed` copy that returns the model unchanged · floor raised by the arm's assertion count

## 8. Open questions

- **F1** What parameterizes the observation B1 leaves unmade? Options: the retirement filter as the
  audit wrote it; the kinds the model's timeline holds, swept one at a time; the two builders named
  under `permission:` with no arm at all. RESOLVED (agent, 2026-09-20, delegated): the per-kind
  sweep, by M3's feature-rich rule. It satisfies what `TOOL-dLoggedFlight-26` S7 wanted, survives
  `TOOL-dLoggedFlight-22`, and is the only one of the three that can still fail once this build has
  landed. §4 records why the others lost.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from B1 of the spec audit of units 25 to 27, round 1,
  at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-26` S7's observation and its AC3, which
  that unit now owes to this arm at the post-build suite run.
- rev-2 · 2026-09-20 · the build pass. S2's and AC2's third liveness narrowed from EVERY copy to the
  kinds the base render shows a row for, because the assertion as written could not pass: a probe
  over a synthetic model of the class model's shape, run against the kit's real renderer, measured an
  `owner` kind's removal leaving the rendered bytes byte-identical, since that kind is dropped before
  a row is built and counted in no fact. A retired kind's removal does move them, through the
  `withheld rows` fact, so the sweep still subsumes the retirement case the audit asked for. The two
  readers the arm needs, `read_sweep_expectations` and `measure_killed`, join the inventory in the
  same bump; the second derives what the `values withheld` count must fall by from the builder's own
  `read_placed` list rather than from a kind-to-placement map typed beside the sweep.

## 10. Reuse audit

The seams are `build_class_model`, `build_big_model` and `render_record`, plus the derived
expectations `TOOL-dLoggedFlight-26` leaves in `test_record_ac4_classes`, `test_record_ac6_cap` and
`test_schema_ac1_render_then_grade`, all this build's.
`tools/codebase-map/reuse_lookup.py "re-check a derived test expectation against a render with one
event kind removed"` returned name-stem candidates only, `render_record` and `check` among them, and
no seam mutates a fixture model and re-checks an expectation against the new render, so no existing
seam fits. The recall query returned this audit's B1, the previous audit's H1 left-shift, which is
where the derivations come from, and `DEPL-aTetheredConvoy-5`'s liveness section, whose rule that a
derived population from a lossy source cannot tell zero-of-zero from clean is why S2 asserts three
liveness facts rather than one.

Recall terms used: derived expectation typed literal fixture builder mutation retirement filter vacuous arm liveness selftest
