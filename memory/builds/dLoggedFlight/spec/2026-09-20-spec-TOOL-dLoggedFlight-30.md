# TOOL-dLoggedFlight-30 — the replaced `known` test is observed gone from the renderer, and one arm re-points a declared source to prove the lookup decides the value

**Status:** CLOSED · rev-2 · 2026-09-20 · node d · Tier-2 · base 4cf0944d · streams tooling · order 31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-dLoggedFlight-30-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-dLoggedFlight-30-1-acceptance-ledger.md) | journal | — |
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
  `HERE` kit directory the suite already derives from its own `__file__` in
  `tools/runlog/selftest.py` — cited by NAME, since rev-1's line number was off by one before a byte
  of this unit landed — and asserts the renderer defines no `derive_known` and holds no
  `known = (cov` test, so the five Summary facts' slots are decided by the `count_sources` lookup
  `TOOL-dLoggedFlight-27` S2 declares and by nothing beside it. Observed by AC1.
- **S2** The re-pointed source. On a schema copy whose `owner turns` slots are declared to come from
  `gates` rather than `transcripts`, the arm renders a model whose transcripts read a counted state
  and whose gates journal reads `dead`, and expects `owner turns` to read `-` while `attributed
  calls` still reads its counts. With the two coverage states swapped — the gates journal counted and
  the transcripts `not-local` — it expects the reverse. Only the lookup can produce that pair: the
  replaced test reads the transcripts for all five facts and cannot make two of them disagree. The
  staged RED is that test RESTORED, as a wrapper around the renderer's own lookup, and it is graded
  TWICE: it moves all five facts together under the re-pointed declaration, AND it leaves S3's two
  renders byte-identical. That second reading is the equivalence H2 named, run rather than argued.
  Observed by AC2.
- **S3** The unchanged behaviour. Over the same two models with the UNMODIFIED schema, the arm
  expects the five Summary facts exactly as `test_record_ac10_unknown_counts` in
  `tools/runlog/selftest.py` expects them — cited by NAME, since rev-1's line number had already
  moved — read from that arm's own model rather than typed,
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
| `scan_replaced_spellings` | function | `py.function`, led by `scan` |
| `read_summary_counts` | function | `py.function`, led by `read` |
| `read_model_counts` | function | `py.function`, led by `read` |
| `build_source_state_copy` | function | `py.function`, led by `build` |
| `build_repointed_schema` | function | `py.function`, led by `build` |
| `render_under_schema` | function | `py.function`, led by `render` |
| `REPLACED_SPELLINGS` · `RENDERER_ANCHOR` | constants | `py.constant` |

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
- perf / scale — one source read, one fixture, and six renders: two per schema state and two more
  under the staged break, which is graded against both states.
- error / empty / loading states — the arm reds if the renderer module cannot be read from `HERE`,
  rather than treating an unreadable file as an absent spelling.
- observability — a failure names the fact, the declared source, the coverage state and both values.
- risks — an absence check passes when the renderer is renamed rather than replaced; S2's
  re-pointing is what makes the passing case mean the lookup decides the value.
- testing — AC1 staged RED on each of two copies of the renderer's own source, one per replaced
  spelling cut back in; AC2 on a copy of the renderer that restores the replaced test over the five
  Summary facts, graded both for redding AC2 and for leaving AC3 green.
- migration — N/A — test code only.
- user docs — the kit README's paragraph on unknown values.

## 6. Acceptance criteria

- **AC1** — When `test_record_known_replaced` reads the renderer module through the suite's `HERE`
  directory, that module defines no `derive_known` and holds no `known = (cov` test.
  Red when: either spelling is present, or the module cannot be read and the arm passes anyway.
  Staged RED against a copy of that source with a replaced spelling cut back in, one copy per
  spelling. Every criterion of `TOOL-dLoggedFlight-27` passes on such a copy by construction, since
  none of them reads a source at all, which is §1's finding; the copies are text and are never
  imported or executed.
- **AC2** — When the arm renders a model whose transcripts read a counted state and whose gates
  journal reads `dead`, against a schema copy declaring `owner turns` sourced from `gates`,
  `owner turns` reads `-` and `attributed calls` reads its counts; with the two coverage states
  swapped, `owner turns` reads its counts and `attributed calls` reads `-`.
  Red when: both facts move together in either render, which is what the replaced test would do.
  Staged RED against a renderer copy that ignores `count_sources` for the five Summary facts by
  restoring the replaced test over them, with the liveness that the SAME copy leaves AC3's two
  renders unchanged — so the break is seen to red this criterion and pass that one.
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

New arm: `tools/runlog/selftest.py` · AC1's two renderer copies keeping a replaced spelling and AC2's renderer copy restoring the replaced test over the five Summary facts · floor raised by this unit's assertion count

## 8. Open questions

- **F1** How is the replacement of the `known` test observed? Options: an absence grep over the
  renderer; an arm that re-points a declared source so the new path decides the value; both.
  RESOLVED (agent, 2026-09-20, delegated): both, by M3's feature-rich rule. The grep alone cannot
  tell a rename from a replacement, and the re-pointing alone leaves a second copy of the rule
  standing beside the declaration. §4 records why each half is insufficient.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from H2 of the spec audit of units 25 to 27, round 1,
  at the loop's BOUNDED exit, with that finding's left-shift as its mechanism.
- rev-2 · 2026-09-20 · built. Two amendments, both made before the code they describe. S2 and AC2
  name the staged RED as the replaced test RESTORED rather than any renderer that ignores the
  declaration, and add the liveness that the SAME break leaves S3's renders unchanged: a break seen
  to red one criterion and pass the other is the equivalence argued in §4, measured instead. AC1's
  staged copies are TEXT splices of the renderer's source that are never imported or executed, so
  "every criterion of `TOOL-dLoggedFlight-27` still passes on that copy" holds by construction
  rather than by a run — that unit's criteria read no source at all, which is §1's finding.
  Then the four other halves those two amendments left standing, found by the
  `amendment-leaves-its-other-half-standing` entry of the bug-class checklist over the code commit:
  §5's testing line and its render count still described rev-1's single staged copy; the Inventory
  named the arm alone and not the six helpers and two constants it arrives with; and S1 and S3 each
  cited a `selftest.py` line number, one of which was off by one at rev-1 and the other of which had
  already moved, so both now cite by NAME.

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
