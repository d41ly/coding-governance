# TOOL-dLoggedFlight-30 — the replaced `known` test is observed gone from the renderer, and one arm re-points a declared source to prove the lookup decides the value

**Status:** SPECCED · rev-1 · 2026-09-20 · node d · Tier-2 · base 4cf0944d · streams tooling · order 31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 25 to 27, round 1, confirmed H2, a HIGH, in `TOOL-dLoggedFlight-27`.

That unit's S3 says `build_summary_facts`' `known` test "is replaced by that lookup, so the five
Summary facts keep their present behaviour and the rule is stated once", and cites AC2 and AC3. The
test is live at `tools/runlog/record.py:640`, with `derive_known` at `:642` driving `owner turns`
(`:660`), `attributed calls` (`:661`) and the three `usage` lines. No criterion of that spec inspects
`tools/runlog/record.py` at all. Its AC2 stages a `not-local` copy and expects `-`, which the `known`
test already produces today. Its AC3 reads hunks of the suite module. Its AC4 forces the declaration
to COVER the five facts' slots but never forces the renderer to READ it. Its AC5 renders.

So an implementation that adds `count_sources` for the `withheld rows` slots and leaves
`known` and `derive_known` deciding the five Summary facts is behaviourally indistinguishable and
passes AC1 to AC5 unchanged. Two hand-written statements of one rule then survive, which that unit's
§4 explicitly rejects — "two hand-written tests of one rule is the drift S3 removes" — and the reason
the five Summary facts were pulled onto the declaration at all is the part left unobserved.

This unit observes the replacement: the replaced spelling is gone from the renderer, and one arm
re-points a declared source so that the fact follows the new source's coverage state, which is the
one observation a value-only criterion cannot make.

Every code line cited here was read at `63a37d1c` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The absence. `test_record_known_replaced` reads the renderer module beside it, through the
  `HERE` kit directory the suite already derives from its own `__file__`
  (`tools/runlog/selftest.py:52`), and asserts the renderer defines no `derive_known` and holds no
  `known = (cov` test, so the five Summary facts' slots are decided by the `count_sources` lookup
  `TOOL-dLoggedFlight-27` S2 declares and by nothing beside it. Observed by AC1.
- **S2** The re-pointed source. On a schema copy whose `owner turns` slots are declared to come from
  `gates` rather than `transcripts`, the arm renders a model whose transcripts read a counted state
  and whose gates journal reads `dead`, and expects `owner turns` to read `-` while `attributed
  calls` still reads its counts. With the two coverage states swapped — the gates journal counted and
  the transcripts `not-local` — it expects the reverse. Only the lookup can produce that pair: the
  replaced test reads the transcripts for all five facts and cannot make two of them disagree.
  Observed by AC2.
- **S3** The unchanged behaviour. Over the same two models with the UNMODIFIED schema, the arm
  expects the five Summary facts exactly as `test_record_ac10_unknown_counts`
  (`tools/runlog/selftest.py:4792`) expects them, read from that arm's own model rather than typed,
  so the replacement is evidenced by the re-pointing and never by a changed value. Observed by AC3.
- **S4** The floor. `ASSERTION_FLOOR` rises by this unit's assertion count, with a RAISED comment
  naming this unit and the arithmetic that reaches the new value. Observed by AC4.
- **S5** The docs. The kit README's paragraph on unknown values states that the five Summary facts
  read the declaration and that no second hand-written test of the rule remains. No dossier claim is
  added — these are Python symbols, the dossier's `[claims]` block carries no symbol tier
  (`tools/codebase-map/map_extractors.py:128`), and its `[paths] globs` already covers
  `tools/runlog/**`. NOT OBSERVED: prose.

## 3. Non-goals (OUT)

- `count_sources`, `check_count_sources` and the `withheld rows` fact. `TOOL-dLoggedFlight-27` builds
  all three; this unit observes that the renderer actually reads the first of them.
- `COUNTED_STATES` and the `idle` judgement. `TOOL-dLoggedFlight-16` and unit 27's S3 own them, and
  the cell where the two predicates disagree is that unit's rev-2 fold.
- The Coverage counts' declaration. Unit 27's rev-2 fold adds them; this unit grades the five Summary
  facts the `known` test decided, which is the population H2 names.
- A spec-audit check that finds, for every "is replaced by" in a scope item, the criterion observing
  the old thing gone, which is H2's class left-shift. It needs its rule in
  `memory/TEMPLATE-SPEC.md`, a governance carrier, so BUILD-METHOD M3's second veto makes it the
  owner's; it is parked in the build's run-state file on 2026-09-20.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-27` — the `count_sources` declaration, the lookup that
  replaces the `known` test, and `check_count_sources`; with the lookup unbuilt there is no
  replacement to observe.

## 4. Design

Behavioural equivalence is the whole reason a value-only criterion cannot see a replacement. The
replaced test and the new lookup agree on every model where the declaration names the transcripts,
and that is every model unit 27's criteria build. Evidence therefore has to come from a model where
the two DISAGREE, and the only way to make them disagree is to re-point the declaration — which is
what a declaration is for. Re-pointing is also why this arm proves more than a grep could: it shows
the new path decides the value, not merely that the old path is absent.

The absence check is the other half, and it is the instrument this build already uses for a retired
spelling: unit 22's AC3 and AC6 and unit 26's AC2 and AC4 all name a retired spelling and observe it
gone. What is new here is the target — the renderer, which none of unit 27's criteria read.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `test_record_known_replaced` | function | `py.function`, led by `test` |

### Files touched (estimate)

`tools/runlog/selftest.py` and `tools/runlog/README.md`.

### Alternatives rejected

- Add the absence grep to `TOOL-dLoggedFlight-27` AC2 as a fold, the audit's first fix sentence:
  rejected, since M4 disposes a HIGH by promotion and the re-pointing arm is a mechanism rather than
  a criterion edit.
- Observe the replacement by the five facts' values alone: rejected, since the two predicates agree
  on every such model, which is H2's finding restated.
- Re-point the source in the live schema rather than on a copy: rejected, since the declaration is
  the shipped contract and an arm that edits it in place grades a tree nobody ships.
- Delete `derive_known` in this unit: rejected, since `TOOL-dLoggedFlight-27` S3 already replaces it
  and two units editing one function is the collision this build's one-mechanism rule exists to stop.

## 5. Production-readiness checklist

- security — N/A — test code only, over synthetic fixtures.
- perf / scale — one source read and four renders, two per schema state.
- error / empty / loading states — the arm reds if the renderer module cannot be read from `HERE`,
  rather than treating an unreadable file as an absent spelling.
- observability — a failure names the fact, the declared source, the coverage state and both values.
- risks — an absence check passes when the renderer is renamed rather than replaced; S2's
  re-pointing is what makes the passing case mean the lookup decides the value.
- testing — AC1 staged RED on a renderer copy that keeps the replaced test, AC2 on a renderer copy
  that ignores `count_sources` for the Summary slots.
- migration — N/A — test code only.
- user docs — the kit README's paragraph on unknown values.

## 6. Acceptance criteria

- **AC1** — When `test_record_known_replaced` reads the renderer module through the suite's `HERE`
  directory, that module defines no `derive_known` and holds no `known = (cov` test.
  Red when: either spelling is present, or the module cannot be read and the arm passes anyway.
  Staged RED against a renderer copy that keeps `derive_known` beside the lookup, which must red
  while every criterion of `TOOL-dLoggedFlight-27` still passes on that copy.
- **AC2** — When the arm renders a model whose transcripts read a counted state and whose gates
  journal reads `dead`, against a schema copy declaring `owner turns` sourced from `gates`,
  `owner turns` reads `-` and `attributed calls` reads its counts; with the two coverage states
  swapped, `owner turns` reads its counts and `attributed calls` reads `-`.
  Red when: both facts move together in either render, which is what the replaced test would do.
  Staged RED against a renderer copy that ignores `count_sources` for the five Summary facts.
  figure: DERIVED — every expected count is read from the rendered model at observation time.
- **AC3** — When the arm renders the same two models against the unmodified schema, the five Summary
  facts read exactly what `test_record_ac10_unknown_counts` expects of its own models, read from the
  model rather than typed.
  Red when: a fact differs from the value read from the model, or the arm types one.
- **AC4** — When `ASSERTION_FLOOR` in the runlog kit's self-test module is read after S4, its newest
  RAISED comment names `TOOL-dLoggedFlight-30` and its arithmetic reaches the declared value. The
  suite run that grades the count itself is this spec's `New arm:` line.
  Red when: the floor moves with no comment naming this unit, or the comment's arithmetic does not
  reach the value declared beside it.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's renderer copy keeping `derive_known` and AC2's renderer copy ignoring `count_sources` for the Summary facts · floor raised by this unit's assertion count

## 8. Open questions

- **F1** How is the replacement of the `known` test observed? Options: an absence grep over the
  renderer; an arm that re-points a declared source so the new path decides the value; both.
  RESOLVED (agent, 2026-09-20, delegated): both, by M3's feature-rich rule. The grep alone cannot
  tell a rename from a replacement, and the re-pointing alone leaves a second copy of the rule
  standing beside the declaration. §4 records why each half is insufficient.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from H2 of the spec audit of units 25 to 27, round 1,
  at the loop's BOUNDED exit, with that finding's left-shift as its mechanism.

## 10. Reuse audit

The seams are `build_summary_facts` and `RECORD_SCHEMA` in `tools/runlog/record.py`, the `HERE` kit
directory and `read_fact_counts` in the suite module, and `test_record_ac10_unknown_counts`' models,
all this build's. `tools/codebase-map/reuse_lookup.py "observe that a replaced predicate is absent
from the renderer after a declaration takes it over"` returned name-stem candidates and the runlog
affordance seam `runlog_lib.parse_line`, and no seam observes a replaced predicate's absence or
re-points a declaration to prove the new path decides a value, so no existing seam fits. The recall
query returned this audit's H2 with its left-shift, `TOOL-dLoggedFlight-16` §2's statement that the
`known` test and the model's own `present` test are one predicate each and that no branch is added to
either, and `TOOL-dPromptedSeam-1`'s round-1 record, where a renderer change was specced as new code
with its own staged-failure arm for the same reason.

Recall terms used: known test COUNTED_STATES declaration lookup replaced predicate renderer absence grep behavioural equivalence
