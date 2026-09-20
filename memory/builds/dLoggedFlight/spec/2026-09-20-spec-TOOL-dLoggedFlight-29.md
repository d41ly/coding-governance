# TOOL-dLoggedFlight-29 — each placement model is returned beside the repository state it was built from, and the arm re-derives the model from that state

**Status:** CLOSED · rev-4 · 2026-09-20 · node d · Tier-2 · base 4cf0944d · streams tooling · order 30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-dLoggedFlight-1-runlog-2f11f32d.md](../build/2026-09-20-build-TOOL-dLoggedFlight-1-runlog-2f11f32d.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-30 |
| [2026-09-20-build-TOOL-dLoggedFlight-29-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-dLoggedFlight-29-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-30 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 25 to 27, round 1, confirmed H1, a HIGH, in `TOOL-dLoggedFlight-25`.

That unit's S2 makes one discipline its centre: `build_placement_models` builds its three models
through `build_run_model` from the history `build_landed_fixture` makes, "never by editing a model
field", and says the discipline is observed by AC1. AC1 grades rendered values — the two provenance
facts, the closing bound and the duration — and its `figure: DERIVED` note governs where the
EXPECTATION comes from, not how the model was built. AC2's one structural probe is a single exact
literal, `git grep -n 'window=dict(m\["window"\]' -- tools/runlog/selftest.py`, which matches the
spelling of the loop that unit retires and nothing else; at `63a37d1c` the module holds exactly one
such re-render, at `tools/runlog/selftest.py:4354`.

So a builder that produces its `pending` model as a keyword copy of the `landing` model with
`terminal` set passes AC1, AC2, AC3 and AC5 unchanged — the closer is derived from `terminal` and the
window's `end_from`, so the shortcut renders exactly the values S3 names — and AC4's replay is a
separate arm over the fixture history that never calls the builder. That is the defect the previous
audit's B1 found, an arm that keeps passing while the render stops reading the edited field,
reintroduced inside the unit whose stated purpose is to remove it.

This unit makes the builder's claim assertable: each model comes back beside the repository state it
was built from, and an arm re-derives the model from that state and compares.

Every code line cited here was read at `63a37d1c` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The paired return. `build_placement_models` returns, beside each model, the repository state
  that model was built from: the fixture repository, the journal root it read, the commit its history
  was cut at, and which run-state write was staged or committed in the working tree for that
  placement, named by its blob. One entry per placement, keyed by the names `TOOL-dLoggedFlight-25` S2
  gives them — `landed`, `landing` and `pending`. Every one of those four is READ BACK OUT OF GIT by
  the arm, so a state that merely labels a repository reds rather than passing as one that describes
  it. Observed by AC1.
- **S2** The re-derivation. `test_record_placement_states` re-runs `build_run_model` over each
  returned state and compares the result with the model the builder returned, field by field through
  `dataclasses.asdict`. A model the builder shortcut then differs from the model its own claimed
  state produces, whatever field was edited. Every FIELD is compared; what a comparison cannot read is
  the sub-keys `MODEL_UNREPRODUCIBLE` declares, one per reason, because `cost.wall_s` measures the
  build and not the repository and a comparison reading it would red on a correct builder. The
  declaration is held in both directions: a masked sub-key the model does not carry reds. Observed by
  AC1 and AC2.
- **S3** The declared builders and the source probe. `HISTORY_BUILT_BUILDERS`, a constant in the
  runlog kit's self-test module, names every builder whose models are claimed to come from a real
  history; at this unit that is `build_placement_models` alone. `check_built_from_history` reads each
  named builder's own source through `inspect.getsource` and refuses a keyword re-render of a model
  or an assignment into a model field, and refuses a member the module does not define. It prints how
  many builders it read and how many syntax nodes those sources carried, and reds on either at zero.
  `check_built_from_history` reads only the declared builders' source, so the `dataclasses.asdict` at
  `tools/runlog/selftest.py:4727` is outside it by construction; the predicate underneath it,
  `scan_model_edits`, takes a parsed function and is what AC3 also runs over a mutated copy of the
  shipped builder's source. Observed by AC3.
- **S4** The floor. `ASSERTION_FLOOR` rises by this unit's assertion count, with a RAISED comment
  naming this unit and the arithmetic that reaches the new value. Observed by AC4.
- **S5** The docs. The kit README's self-test paragraph states that a fixture builder claiming a real
  history returns the state it used, and that the arm re-derives from it. No dossier claim is added —
  these are Python symbols, the dossier's `[claims]` block carries no symbol tier
  (`tools/codebase-map/map_extractors.py:128`), and its `[paths] globs` already covers
  `tools/runlog/**`. NOT OBSERVED: prose.

## 3. Non-goals (OUT)

- The three placements, the closer and every rendered value. `TOOL-dLoggedFlight-25` owns them, and
  this unit adds no criterion over a rendered fact.
- The placement replay and `PLACEMENT_LAG`. That unit's S5 owns both; this unit grades how the models
  reach the replay, not what the replay compares.
- Every other fixture builder in the suite. The probe reads a DECLARED set and says so, and a builder
  outside it is not graded — widening the set is a later unit's work, not this arm's silent reach.
- The one-sided `ASSERTION_FLOOR` comparison. Making the floor an equality edits a constant every
  open unit touches, so it is the owner's call and sits in the backlog, not here.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-25` — `build_placement_models`, the three placement states
  and `build_landed_fixture`'s history, whose construction this unit makes assertable; with no
  builder there is nothing to pair a state with.

## 4. Design

A builder that CLAIMS its models come from a history should assert it rather than state it. Turning
the claim into data — the state each model was built from — lets the arm re-derive, and a builder
that shortcuts reds by itself whatever field it edited. That is the difference from another grep:
AC2's probe matched one spelling, and a keyword copy with `terminal` set is a different spelling of
the same defect. A spelling list cannot enumerate the next shortcut; a re-derivation does not have to.

The source probe is the cheap half, and it is scoped to a declared set for the reason charter §7
gives for a declared population: asserted in both directions, so a member the module does not define
reds too, and an exemption cannot silently widen. Run over the tree before wiring, per charter §7:
at `63a37d1c` the module holds one keyword re-render of a model, `tools/runlog/selftest.py:4354`,
which `TOOL-dLoggedFlight-25` S4 removes, and one `dataclasses.asdict` at `:4727`, a near-miss that
must not red and which the declared-source scoping excludes.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `test_record_placement_states` | function | `py.function`, led by `test` |
| `check_built_from_history` | function | `py.function`, led by `check` |
| `scan_model_edits` | function | `py.function`, led by `scan` |
| `build_masked_model` | function | `py.function`, led by `build` |
| `build_placement_models_field_edit` | function | `py.function`, led by `build` |
| `build_placement_models_rerender` | function | `py.function`, led by `build` |
| `build_placement_models_read_only` | function | `py.function`, led by `build` |
| `HISTORY_BUILT_BUILDERS` | constant | `py.constant` |
| `MODEL_FIELDS` · `MODEL_TYPES` · `MODEL_UNREPRODUCIBLE` | constants | `py.constant` |

### Files touched (estimate)

`tools/runlog/selftest.py` and `tools/runlog/README.md`.

### Alternatives rejected

- Extend AC2's grep with the shortcut spellings, the audit's second route: rejected by M3's rule,
  since the population of spellings is open and H1 is what one exact literal already cost.
- Re-derive inside `build_placement_models` and compare there: rejected, since the builder would
  then grade itself with the state it chose, which is the guard-shares-a-variable shape.
- Assert each model against a typed expectation per placement: rejected, since a typed expectation
  over a fixture is the class `TOOL-dLoggedFlight-26` exists to remove.
- Run the source probe over every function in the module: rejected, since a predicate over the whole
  module reds the legitimate `dataclasses.asdict` neighbours and the declared set makes the
  population answerable in both directions.

## 5. Production-readiness checklist

- security — N/A — test code only, over synthetic fixtures.
- perf / scale — three extra `build_run_model` calls over the fixture repository, one per placement,
  and one source read per declared builder.
- error / empty / loading states — a placement that returns no state reds; a declared builder the
  module does not define reds.
- observability — a mismatch names the placement, the field and both values; the probe names the
  builder and the line it refused.
- risks — a comparison that silently compares nothing would pass every placement, which is why AC2
  asserts the compared field count against the model's own.
- testing — AC1 staged RED on a builder copy that edits a field, AC2 on a comparison copy that
  compares an empty field set, AC3 on a constant copy, two builder copies, and the SHIPPED builder's
  own source with one field edit inserted into it.
- migration — N/A — test code only.
- user docs — the kit README's self-test paragraph.

## 6. Acceptance criteria

- **AC1** — When `test_record_placement_states` runs, each model `build_placement_models` returns is
  accompanied by the repository state it was built from, that state is confirmed against git — the
  repository is AT the commit the state names, and the run-state write is staged or committed exactly
  where the state says, by blob — and `build_run_model` re-run over that state produces a model equal
  to the returned one field for field.
  Red when: a returned model differs from the model its own state produces, a placement carries no
  state, or a state names a commit or a write the repository does not hold. Staged RED by a builder copy that produces `pending` as a keyword copy of the `landing`
  model with `terminal` set, which must red here while `TOOL-dLoggedFlight-25` AC1 still passes on
  the same copy — that contrast is the evidence this criterion is load-bearing.
  figure: DERIVED — every compared field is read from the re-derived model at observation time.
- **AC2** — When `test_record_placement_states` compares, the compared field set is the model's own
  field set as `dataclasses.asdict` returns it, it is not empty, and all three placements are
  compared. Every sub-key masked inside a field is NAMED by `MODEL_UNREPRODUCIBLE` with its reason and
  is carried by the model.
  Red when: the compared field set is empty or smaller than the model's, fewer than three placements
  are compared, or a field or sub-key is skipped without the arm naming it. Staged RED by a comparison
  copy that compares an empty field set, which must red rather than reporting three clean placements.
- **AC3** — When `check_built_from_history` reads every builder `HISTORY_BUILT_BUILDERS` names, it
  finds no keyword re-render of a model and no assignment into a model field, and it prints the
  number of builders it read and the syntax nodes it walked. On a constant copy naming a builder the
  module does not define, on a `build_placement_models` copy that assigns into a model field, and on
  one that keyword re-renders a model, it refuses naming that builder; on a builder that only reads a
  model through `dataclasses.asdict` it refuses nothing. The predicate is ALSO run over the SHIPPED
  `build_placement_models` source with one model-field assignment inserted into it, which must be
  refused while the unmutated source is clean — the small copies alone would prove the predicate only
  for small copies.
  Red when: any staged copy passes, the near miss is refused, the mutated shipped source is accepted,
  the mutation did not reach the text, or the printed builder or node count is zero.
- **AC4** — When `ASSERTION_FLOOR` in the runlog kit's self-test module is read after S4, its newest
  RAISED comment names `TOOL-dLoggedFlight-29` and its arithmetic reaches the declared value. The
  suite run that grades the count itself is this spec's `New arm:` line.
  Red when: the floor moves with no comment naming this unit, or the comment's arithmetic does not
  reach the value declared beside it.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's field-editing builder copy, AC2's empty-field-set comparison copy, and AC3's constant copy, its two builder copies and the shipped builder's own source with one field edit cut into it · floor raised by this unit's assertion count

## 8. Open questions

- **F1** How is "built from a history, never by editing a model field" observed? Options: extend
  AC2's grep with the shortcut spellings; return the state each model was built from and re-derive;
  a source probe over a declared set of builders. RESOLVED (agent, 2026-09-20, delegated): the
  returned state with the re-derivation, and the source probe beside it, by M3's feature-rich rule.
  The grep alone is what H1 found insufficient, and the two together grade the behaviour and the
  shape. §4 records why the others lost.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from H1 of the spec audit of units 25 to 27, round 1,
  at the loop's BOUNDED exit, with that finding's left-shift as its mechanism.
- rev-4 · 2026-09-20 · the bug-class checklist over the ledger commit selected
  `amendment-leaves-its-other-half-standing`, and it was a hit: rev-3 extended AC3 and left two
  clauses written under rev-2 standing. S3 still described a probe that prints a builder count alone
  and named `check_built_from_history` as the only reader of source, and section 7's `New arm:` line
  still listed one builder copy. Both now match AC3. No code moved for this rev.
- rev-3 · 2026-09-20 · the bug-class checklist over the rev-2 commit selected
  `staged-break-substitutes-a-synthetic-value`, and it reached AC3: its two staged copies are eight
  lines each while the shipped builder is thirty, so refusing them proved the predicate for the
  copies. AC3 and section 5 now add a staged break cut into the SHIPPED builder's own source, and the
  arm asserts the mutation reached the text and that the unmutated source is clean.
- rev-2 · 2026-09-20 · built. Two divergences the build measured. `RunModel.cost.wall_s` is set from
  `time.perf_counter()` at `tools/runlog/model.py:1820`, so a field-by-field comparison written as
  rev-1 spelled it would have red on a CORRECT builder every run; S2 and AC2 now declare the mask,
  one named sub-key with its reason, held in both directions, and the compared FIELD set is still the
  model's own and whole. A probe over a synthetic fixture read 36 model fields and found `cost.wall_s`
  the only one that did not reproduce, `cost.git_calls` included. Second, rev-1's state was a value
  the arm trusted; S1 and AC1 now hold all four of its parts against git, since a state nothing checks
  is a label and the re-derivation would then run over whatever repository the builder handed it.

## 10. Reuse audit

The seams are `build_placement_models` and `build_landed_fixture` in the runlog kit's self-test
module and `build_run_model` in `tools/runlog/model.py`, all this build's.
`tools/codebase-map/reuse_lookup.py "a fixture builder returns the repository state its model was
built from"` returned name-stem candidates, `build_run_model` and `build_reference_index` among them,
and no seam returns the state a fixture was built from or re-derives a fixture to compare, so no
existing seam fits. The recall query returned this audit's H1, `TOOL-dLoggedFlight-25` §4's own
sentence on why a field-editing re-render went unseen, and `TOOL-dPolishedVitrine-9`, an open backlog
row about a fixture built by `git archive` into a repository with no history — the same class from
the other side, a fixture whose claimed provenance the arm cannot check.

Recall terms used: fixture builder placement model history edited field re-render window closer replay derived arm
