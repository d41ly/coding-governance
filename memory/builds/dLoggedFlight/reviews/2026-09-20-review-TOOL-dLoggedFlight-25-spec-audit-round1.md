**Serves:** spec-audit TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27

# dLoggedFlight — spec audit of units 25 to 27, round 1

*Node `d`, 2026-09-20, on `branch/unattended-build-transparency-ea83a5` at HEAD `f87bb884`. The
subjects are the three units the previous spec audit promoted at its BOUNDED exit, all at rev-1: unit 25
from that audit's B1 and H3, unit 26 from its H1, and unit 27 from its H4 and H2. This is ROUND 1 of this
subject set, and `.unattended.conf` declares a bound of one round (`REVIEW_ROUNDS="1"`). The pass was
Tier-2 and adversarial: four primed finder lenses, then a skeptic stage of five batches prompted to
REFUTE each finding, then one synthesis, which is this record. The previous spec audit is
[its record](2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md). The labels B1, H1 and so on
are this record's own; a label from that record is cited with that record named, and "M3's rule", which
the specs cite, is that record's own M3 and not this one's. The three specs declare their read point as
`f7bf9d2f`; the code citations BELOW are at HEAD `f87bb884`, where `record.py` and `selftest.py` have
since moved, so "What this synthesis re-derived" gives the line map a fix needs to amend a citation in
the spec's own frame. `record.py`, `model.py` and `selftest.py` are unmodified in the working tree at
that HEAD; `tools/runlog/README.md` and `memory/map/features/runlog.md` are not, and no item below cites
either. The severities are this synthesis's adjudication, not the finders' grades.*

**Reviewed subjects, each pinned at the blob it was read at — ROUND 1:** `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-25.md@08807e756d4b5fd6c3f8a4d931c6184f751c3cd9`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-26.md@13b239bb2c63012b60c683f7c348f37c37a50d39`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-27.md@2b9bb4f43a7c85f8ca35658b8df60c6977bb3653`.

## Verdict: BLOCKED

One blocker stands, in unit 26. Its AC3 requires an observation this run may not make: the probe renders
two builders that exist only inside `tools/runlog/selftest.py`, and the build brief's standing owner
instruction denies every route to them before VERIFYING — the invocation, an import of the suite module,
and a copy of it under another name. AC3's `cost:` line then refuses the brief's own escape, which is to
write a suite-observed criterion as owed to the post-build run. So the builder must either break the
instruction or book AC3 as met without observing it.

Two highs sit beside it, and both are the same shape as each other: a unit declares the discipline that
is its whole reason for existing, says a criterion observes it, and no criterion does. In unit 25 the
discipline is that the three placement models are BUILT from a history rather than edited; in unit 27 it
is that the renderer's hand-written `known` test is REPLACED by the declaration lookup. In both, an
implementation that keeps the old shape passes every written criterion.

The tally is 1 BLOCKER, 2 HIGH, 4 MEDIUM and 1 LOW, over 8 items from 8 confirmed findings — no folds,
one item per finding. Unit 25 carries H1, M1, M4 in part and L1. Unit 26 carries B1. Unit 27 carries H2,
M2, M3 and M4 in part. Precision was 0.27, which is below the floor `AGENTS.md` §8 sets; see "Review
shape". One further observation, which did NOT pass the skeptic stage, is filed separately under "Beside
the finding set" and is not counted in any tally above.

## Run integrity

- Lenses: **4 of 4** returned, **0 died**.
- Skeptic batches: **5 of 5** returned, **0 died**.
- Verdicts: **0** contradictory ones demoted to unverified, **0** spurious ones discarded, **0**
  duplicates.
- Unverified findings: **0**.

Every stage returned, so for this lens set the run is complete. A zero below comes from the lens set
itself and not from an agent that died. Even so, a zero is not evidence of absence: the 22 refuted
reports were not handed to this synthesis, so this record cannot say which surfaces they covered. Unit 26
drew exactly one item, which is the thinnest coverage of the three subjects and is worth knowing when
reading its silence.

## Review shape

- Raw findings **30**, confirmed **8**, refuted **22**, unverified **0**, precision **0.27**.
- Precision FELL from 0.50 at the previous spec audit to 0.27, which is the value the first audit of this
  build scored and is below the ~0.5 floor `AGENTS.md` §8 sets. §8's instruction at that point is
  explicit: tighten scope and priming before adding agents. The three subjects are fresh rev-1 specs
  promoted from confirmed items, so the surface is small and already hardened by one audit — the class
  §8 says manufactures refuted noise. The next pass over this set should prime narrower, not wider.
- Adjudicated here: **1 BLOCKER, 2 HIGH, 4 MEDIUM, 1 LOW** over 8 items. The finder grades were 3 high,
  4 medium and 1 low.
- Two adjudications moved. Raw 9, filed high, takes B1: a written criterion with no route to observation
  under a standing owner instruction is the bar both previous audits used for a blocker, and it is the
  same bar as "two criteria that cannot both pass" with the second party being the brief. Raw 11, filed
  medium, was considered for HIGH and HELD at medium; the ground is stated in M3.
- The severity ladder this record used, so that a reader can check it: BLOCKER is a criterion that cannot
  be met as written without breaking another binding rule. HIGH is a discipline the unit DECLARES, claims
  is observed, and that no criterion observes, where the wrong implementation passes the whole set.
  MEDIUM is a covered rule with a missing cell, a mis-attributed observation, or an excluded population
  whose stated reason is wrong. LOW is an unobserved clause whose failure costs provenance rather than
  behaviour.
- No fold, so raw ids map one to one: B1 is raw 9, H1 raw 1, H2 raw 2, M1 raw 4, M2 raw 21, M3 raw 11, M4
  raw 12 and L1 raw 6. The pipeline counted 0 duplicates, which counts byte-identical reports only.

## Findings

| Label | Severity | Unit | Address | Raw | Defect |
|---|---|---|---|---|---|
| B1 | BLOCKER | 26 | §2 S7, §6 AC3 | 9 | the probe renders two suite-only builders, which the brief forbids this run to reach, and `cost:` refuses the owed-to-VERIFYING escape |
| H1 | HIGH | 25 | §2 S2, against §6 AC1 and AC2 | 1 | "never by editing a model field" has no criterion, and the grep matches only the retired loop's spelling |
| H2 | HIGH | 27 | §2 S3, against §6 AC2 to AC5 | 2 | the `known` test's replacement is unobserved — no criterion reads `record.py` at all |
| M1 | MEDIUM | 25 | §6 AC4, against §2 S5 | 4 | `PLACEMENT_LAG`'s membership is never pinned, so the declared set can widen silently |
| M2 | MEDIUM | 27 | §2 S2 and S3, against §6 AC2 | 21 | the one cell where the idle judgement and `COUNTED_STATES` disagree is unobserved |
| M3 | MEDIUM | 27 | §3 non-goals bullet 2, against §1 and §4 | 11 | the excluded population is misdescribed: three Coverage counts come from the transcripts and the journals |
| M4 | MEDIUM | 27, 25 | 27 §2 S7 and §7; 25 §2 S6 | 12 | a dossier cannot "claim" a Python symbol, so the named leg grades nothing of the kind |
| L1 | LOW | 25 | §2 S4, against §6 AC2 | 6 | the floor's move and its naming comment are claimed as observed by an AC that never mentions them |

### B1 — BLOCKER — unit 26 §2 S7 and §6 AC3 — raw 9

**Defect.** S7 requires that "Before this unit's commit, the build renders both builders' models with
every kind `TOOL-dLoggedFlight-22` S1 retires filtered out of the timeline, and checks that each
expectation S3, S5 and S6 derive still matches the render." Both builders live only in the suite module:
`build_class_model` at `tools/runlog/selftest.py:4264` and `build_big_model` at `:4378`, with no other
definition anywhere under `tools/`. The build brief's "Every unit" block closes every route to them
before VERIFYING, and closes the workarounds by name: the gate-guard hook "denies any `selftest.py`,
`*.test.sh` or `run-selftests.sh` invocation while this run's phase is before VERIFYING", then "Do not
work around it: no import of the suite module, no copy of it under another name". "The pass" step 3
repeats it: "Run no suite and no gate."

The brief does provide an escape, in step 4: "An AC whose observation is a suite arm or a gate leg is
written as owed to the post-build run, naming the arm and its RED break, never as met." AC3's `cost:`
sub-field refuses exactly that — "a one-time probe at build, recorded in the acceptance ledger and not
kept as an arm, since after unit 22 the filter removes nothing."

**Impact.** AC3 is unobservable as written, and the two ways out are both defects. Either the builder
breaks a standing owner instruction, or it writes AC3 as met in the acceptance ledger without observing
it — an acceptance line that is a claim about nothing, which is the shape this build's audit chain has
spent three rounds closing. A hand-written script cannot rescue it either: the expectations "S3, S5 and
S6 derive" are derivations that live inside the arms in `selftest.py`, so evaluating them needs the
module the brief bars. The spec template already carries the field for this case and AC3 does not use it:
`permission:` is "the suite, boundary or credential that observes it is one THIS run may not execute"
(`memory/TEMPLATE-SPEC.md:358`), beside the `cost:` AC3 declares (`:357`).

**Fix.** Two routes; the first is preferred because it keeps the observation.

1. Re-home S7 as a real arm. A filtered-timeline render over both builders, parameterized by
   `RETIRED_EVENTS` so that after unit 22 it filters nothing and still asserts every derived expectation
   holds, with its RED break staged at VERIFYING like every other arm in this unit. AC3 then reads as
   owed to the post-build suite run, naming that arm and its break, per the brief's step 4. Count the
   arm in the floor, which §7's `New arm:` line already anticipates.
2. If the probe must stay a one-shot, S7 names the non-suite seam that supplies the two models, since the
   brief bars both the import and a copy, and AC3 carries `permission:` in place of `cost:`.

**Left-shift.** Gate the class, not this instance. An AC whose observation names a `selftest.py`, a
`*.test.sh` or a gate leg, and which carries neither `permission:` nor an attribution to the spec's
`New arm:` line, is refused by the spec-token checker that already reads acceptance criteria — the same
checker that refused a suite run as an acceptance observation at unit 22's rev-2, extended from "a suite
run is not an observation" to "a suite run is not an observation THIS run can make". Per charter §7, run
the candidate predicate over this build's closed specs first and print hits and near-misses: several
closed units legitimately name a suite under `New arm:`, and those must not red.

### H1 — HIGH — unit 25 §2 S2, against §6 AC1 and AC2 — raw 1

**Defect.** S2's central discipline is that `build_placement_models` builds its three models "through
`build_run_model` from the history `build_landed_fixture` makes ... never by editing a model field", and
it says "Observed by AC1". AC1 grades only rendered values: `window opened by` in all three, `window
closed by` per model, the closing bound and the duration. Its `figure: DERIVED` note governs the
EXPECTATION's provenance — the committer times are read from the fixture repository — not the model's
construction. AC2's only structural probe is one exact literal,
`git grep -n 'window=dict(m\["window"\]' -- tools/runlog/selftest.py`, and that spelling matches the
retired loop and nothing else: at HEAD the file holds exactly one such re-render, at `selftest.py:4354`.
The broader `dict(m, ` probe appears in S4 as a past observation at `f7bf9d2f`, a statement about what
was already true, not as a standing criterion.

**Impact.** `build_placement_models` can produce its `pending` model by editing a field —
`dict(landing_model, terminal=True)` — instead of staging the LANDED run-state write. That shortcut
renders `terminal-pending` with the same closing bound S3 names for `landing`, because the closer is
derived from `terminal` and the window's `end_from`, so AC1, AC2, AC3 and AC5 all pass unchanged. AC4's
replay is a separate arm over the fixture history and never calls `build_placement_models`. The result
is B1's shape from the previous audit — an arm that keeps passing while the render stops reading the
edited field — reintroduced inside the unit whose stated purpose is to remove it.

**Fix.** Add a criterion to AC2 over the new builder: each model `build_placement_models` returns equals
`build_run_model` over its own repository state, or a grep asserting the builder contains no `dict(m` and
no assignment into a model field. Stage RED with a builder copy that produces `pending` by setting
`terminal` on the `landing` model, which must red on the new criterion while AC1 still passes — that
contrast is the evidence the criterion is load-bearing.

**Left-shift.** A fixture builder that claims its models come from a real history asserts it rather than
stating it: the builder returns, beside each model, the repository state it was built from, and the arm
re-runs `build_run_model` over that state and compares. A builder that shortcuts then reds by itself,
whatever field it edited. Per charter §7, run the `dict(m` and field-assignment predicate over
`selftest.py` before wiring it and print hits and near-misses — `:4354` is the only re-render, and
`:4727` is a `dataclasses.asdict` that must not red.

### H2 — HIGH — unit 27 §2 S3, against §6 AC2, AC3, AC4 and AC5 — raw 2

**Defect.** S3 says `build_summary_facts`' `known` test "is replaced by that lookup, so the five Summary
facts keep their present behaviour and the rule is stated once", and cites "Observed by AC2 and AC3". The
test is live at `tools/runlog/record.py:640`,
`known = (cov.get("transcripts") or {}).get("state") in COUNTED_STATES`, with `derive_known` at
`:642-643` driving `owner turns` (`:660`), `attributed calls` (`:661`) and the three `usage` lines
(`:663-664`). No criterion of this spec inspects `record.py` at all. AC2 stages a `not-local` copy and
expects `-`, which `known` already produces today. AC3 reads `git show HEAD -- tools/runlog/selftest.py`
hunks. AC4 reads only the schema: it forces the declaration to COVER the five facts' slots, but never
forces the renderer to READ it. AC5 renders.

**Impact.** An implementation that adds `count_sources` for the `withheld rows` slots and leaves
`known`/`derive_known` deciding the five Summary facts is behaviourally indistinguishable and passes AC1
through AC5 unchanged. Two hand-written statements of one rule then survive — which §4 explicitly
rejects, listing "A per-fact `known` test beside the existing one" among the alternatives rejected
"since two hand-written tests of one rule is the drift S3 removes". The reason the five Summary facts
were pulled onto the declaration at all is the part left unobserved.

**Fix.** Add to AC2 or AC4 a criterion over the renderer: `git grep -n -e derive_known -e 'known = (cov'
-- tools/runlog/record.py` finds nothing. Stage RED by re-pointing one Summary slot's declared source in
a schema copy — `owner turns` to `gates`, say — and requiring that fact to follow the gates coverage
state, which proves the lookup and not the old test decides the value. The build's own convention already
grades this class with exactly such a grep: unit 22's AC3 and AC6, and unit 26's AC2 and AC4.

**Left-shift.** When a unit REPLACES a predicate rather than adding one, its criterion names the replaced
spelling and observes its absence, and one arm re-points the new declaration to prove the new path
decides the value. Behavioural equivalence between the old test and the new lookup is the whole reason a
value-only criterion cannot see the difference, so a value-only criterion is never sufficient evidence of
a replacement. As a documented check for the spec audit: for every "is replaced by" in a scope item,
find the criterion that observes the OLD thing gone.

### M1 — MEDIUM — unit 25 §6 AC4, against §2 S5 and §5 — raw 4

**Defect.** S5 declares the Summary `window`, `duration` and `window closed by` facts members of
`PLACEMENT_LAG`, and forbids membership to `terminal`, `phase`, every other Summary fact, and every
Units, Decisions, Conformance and Anomalies item. AC4 grades the containment in one direction only —
"every fact or table that differs between a render and its re-render is a member of `PLACEMENT_LAG`" —
plus two exclusions in its red-when, `terminal` and `phase`. Nothing pins the constant's actual
membership to the three facts S5 names.

**Impact.** A later author who finds another Summary fact, or a Units, Decisions, Conformance or
Anomalies item, lagging can add it to `PLACEMENT_LAG` and the replay stays green. That is the
declared-set escape hatch S5 exists to close, and it is precisely §5's own stated risk: "a git-derived
slot that lags and is added to `PLACEMENT_LAG` without a true reason". An over-wide declared set
silently widens the surface the declaration was written to narrow, which charter §7 names as the reason a
declared population is asserted in both directions.

**Fix.** Extend AC4 to assert that `PLACEMENT_LAG` equals exactly the three facts S5 declares — or, at
minimum, that its members are disjoint from `terminal`, `phase`, every other Summary fact and every
Units, Decisions, Conformance and Anomalies item. Stage RED on a copy that declares a Units item a
member. S5 already names the exact three, so the pin costs one line.

**Left-shift.** Every declared exemption or lag set in the suite is asserted in BOTH directions: each
member reachable, and each non-member absent. One helper over the suite's declared constants earns that
for every future set, and it is the same rule this repo applies to its own tooling registry — an
exemption naming something that no longer exists reds too (charter §7).

### M2 — MEDIUM — unit 27 §2 S2 and S3, against §6 AC2 — raw 21

**Defect.** S2 routes the `idle` slot to "the Coverage `idle` entry's judgement rather than a coverage
state", and that judgement is strict: `idle = {"judged": tr_state == "present", ...}`
(`tools/runlog/model.py:1682`). Every other declared source is graded against `COUNTED_STATES`, which
holds `present` AND `partial` (`tools/runlog/record.py:110`). So with the transcripts `partial`,
`compact`, `limit` and `workflow` must render counts while `idle` must render `-`, from the same source
read. No criterion reaches that cell: AC1 uses S5's all-`present`, gaps-judged copy; AC2 builds the
all-unread copy, where every transcript-sourced slot reads `-` together; AC3 only re-checks
`test_record_ac10_unknown_counts`' `not-local` model's five Summary facts. §4 never says why the
judgement is narrower than the states, either.

**Impact.** An implementation that maps `idle` onto the transcripts coverage state like the rest passes
AC1, AC2 and AC3 unchanged, and then commits `idle 0` for gaps nobody judged on a `partial` run — H4's
own defect, in the unit that exists to close it, since an unjudged run carries no idle rows at all. The
cell is not hypothetical and is already fixtured: `test_record_ac10_unknown_counts` builds a `partial`
model (`tools/runlog/selftest.py:4809`, read back as `got["partial"]`) in which the transcripts are
counted and idle is unjudged.

Held at MEDIUM rather than HIGH, and the distinction is deliberate: unlike H1 and H2 the rule IS graded —
AC2 observes `idle` reading `-` when the gaps are unjudged — so this is a missing cell in a covered rule
rather than an ungraded discipline.

**Fix.** Add to AC2 a transcripts-`partial` copy of the model, asserting counts for `compact`, `limit`
and `workflow` beside `-` for `idle`, with its red-when naming the reverse. Have S2 state that the
judgement is narrower than `COUNTED_STATES` by one state, and why.

**Left-shift.** Where two predicates decide one rule, an arm exercises the cell where they DISAGREE, and
the spec that declares the second predicate names that cell. As a documented check for a spec audit:
tabulate the states for each declared predicate pair and require a criterion in every row where the two
differ. A pair that agrees everywhere is one predicate wearing two names, which is its own finding.

### M3 — MEDIUM — unit 27 §3 non-goals bullet 2, against §1 and §4 — raw 11

**Defect.** The bullet justifies leaving counts undeclared on the ground that they are "read from git,
the run-state file or the build folder, such as `own commits` and `units served`". Three Coverage facts
are not in that population. `sessions` renders `{int} named · {int} extracted` from the transcripts, with
a zero default (`tools/runlog/record.py:788-790`, over `model.py:1770`). `journal starts` and `unjoined
starts` read the driver journal's join (`record.py:784-787`, over `model.py:1785`, which sets
`journal_starts` unconditionally from `len(joined)` and `len(joined) + len(unjoined)`). Those are the
transcripts and the journals — the exact sources §1 lists as able to read unknown. With the journal dead
the record commits `0 joined of 0 record-creating`; with the transcripts `not-local` it commits
`0 named · 0 extracted`. Only the `idle gaps` `{int}` slot already reads `-`, and by a different
mechanism: the model leaves `near_owner` None when the gaps are unjudged, which `derive_count` renders
absent (`record.py:287-290`, `:791-793`).

**Impact.** §4's claim that "the fact carries the same unknown rule as every other count from those
sources" is false for three facts the record still renders, and the concession that makes the exclusion
look safe misdescribes its own population — so the exclusion was never really decided, it was described
past. The Coverage-table-adjacency defence is not available: it was already rejected for the Summary
counts by M6 of the first closing diff review and by `TOOL-dLoggedFlight-9` S4 at rev-7.

Held at MEDIUM after consideration for HIGH. The three facts are pre-existing behaviour this unit does
not add, which is what separates them from the previous audit's H4, where the unit ADDED the fact that
rendered the clean zero. The corpus's own grade for a concession handed to the owner with no parked entry
is that audit's M6, a MEDIUM. The hold is not because the fix is cheap: rewriting the bullet leaves the
zeros standing, which is why this item needs a parked entry either way.

**Fix.** Either add the three Coverage `{int}` slots to S2's declaration — `transcripts` for `sessions`,
the journals for `journal starts` and `unjoined starts` — and count them among S5's derived facts; or
rewrite the bullet to name them as knowingly-excluded transcript- and journal-sourced counts with the
reason, and park the remainder in the build's run-state file exactly as §3's third bullet already does
for the hygiene check.

**Left-shift.** `check_count_sources` is the natural home for the honest version: have it print every
`{int}` slot in `RECORD_SCHEMA` that has NO `count_sources` entry, as an inventory rather than a refusal.
The undeclared population is then enumerated on every run, a new undeclared count is visible in the diff,
and the prose stops carrying a description of a derived set — charter §7's rule that no count of a
derived population is written in prose, applied to the population itself rather than to its size.

### M4 — MEDIUM — unit 27 §2 S7 and §7 Gates, and the same sentence in unit 25 §2 S6 — raw 12

**Defect.** S7 says `memory/map/features/runlog.md` "claims `check_count_sources`", and that the
`codebase-map coverage + freshness` leg grades that claim at the close. A dossier cannot claim a Python
symbol. The `[claims]` block (`memory/map/features/runlog.md:13-27`) holds gate-legs, kits, git-hooks,
workflow-scripts, skill-engines, rendered-skills, gotcha-classes, guides, backlog-shards and
lexicon-verbs, and `[paths] globs` already covers `tools/runlog/**`. The symbol tier is explicitly outside
the ratchet: it "feeds the recall corpus ONLY and never the ratchet — a new symbol there never fails CI"
(`tools/codebase-map/map_extractors.py:128`). The leg runs `tools/codebase-map/test_codebase_map.py`,
whose checks are inventory-key coverage and staleness, pinned prose headings, the affordance section, the
decisions pin, POSIX keys and generated-artifact freshness — none of which can observe a dossier naming a
function.

Unit 25 §2 S6 carries the same sentence for `derive_window_closer`, so this is the class and not one
instance, and a fix to unit 27 alone would certify coverage that unit 25 still lacks.

**Impact.** Two NOT-OBSERVED lines book a grader that does not exist for the claim they name, which is
the gate-satisfied-by-its-own-prose class charter §7 calls out. What the leg actually grades at the close
is that the generated map artifacts were regenerated in the same commit, which is worth stating, and is a
different assertion.

**Fix.** In both specs, say that the dossier PROSE names the function and is unobserved, and that the
coverage and freshness leg grades the regenerated map artifacts committed in the same commit. Drop
"claims" for a Python symbol, or name the actual inventory key if one was intended.

**Left-shift.** "Claims" is a machine term in this repo: it names a key in a dossier's `[claims]` block.
A documented check for the spec audit, cheap enough to be a grep over the open specs: every "claims X" in
a spec resolves X against the inventory ids in `tools/codebase-map/map_extractors.py`, and a claim that
resolves to no inventory is rewritten as prose. That also catches the inverse, a spec that adds a real
inventory key and never says so — see "Beside the finding set".

### L1 — LOW — unit 25 §2 S4, against §6 AC2 and §7 — raw 6

**Defect.** S4 states that `ASSERTION_FLOOR` "moves by the arms S5 and AC1 to AC5 add, less the loop's
three assertions, with a comment naming this unit. Observed by AC2." AC2 says nothing about the floor: it
reads `RECORD_SCHEMA`'s two vocabularies, requires the three renders to carry every member, and greps for
the retired loop, and its red-when covers the `driver` and `terminal-end` members, an unreached member,
and the loop still being defined. §7's "floor moved by S4" is a gate line, not a criterion.

**Impact.** The floor can be re-declared with no comment naming `TOOL-dLoggedFlight-25`, or set below the
true assertion count, and the check passes either way, because it is a one-sided comparison:
`if total < ASSERTION_FLOOR` (`tools/runlog/selftest.py:6222`). The provenance convention is live for
this same constant — `:112-122` carries RAISED comments naming units 16, 14 and 21 — and is graded for it
by unit 22's AC5, which reds when "the floor falls with no comment naming this unit". Unit 25's move of
the same constant loses that.

**Fix.** Add to AC2 what unit 22's AC5 states for the same constant: `ASSERTION_FLOOR`'s comment names
this unit, and the floor equals the post-edit assertion count. Otherwise mark the clause NOT OBSERVED and
name the leg that grades it — an unobserved clause stated as observed is worse than one stated plainly.

**Left-shift.** A ratchet that catches only a FALL is half a ratchet. The suite reds when
`total != ASSERTION_FLOOR` unless the newest RAISED comment names a unit id and its arithmetic adds up,
so an unattributed or wrong move reds on its own. That edits a constant every open unit touches, so it is
the owner's call rather than a unit's, and it belongs in the backlog rather than in unit 25.

## Beside the finding set

**S-obs 1 — unit 26 §2 S8, §4 Files touched and §7 Gates.** This did NOT pass the skeptic stage: no
finder raised it, and it is recorded here because it is one read from settled, not as a confirmed
finding. Treat it as unverified.

S8 adds `memory/gotchas/retirement-inventory-misses-readers-by-value.md`. Unlike a Python symbol,
`gotcha-classes` IS a ratchet key — the runlog dossier already claims six of them
(`memory/map/features/runlog.md:21-27`) — and `tools/codebase-map/test_codebase_map.py:93-103` reds on an
unclaimed new inventory key, with baseline additions "reserved for the initial backfill" (`:13`). Unit
26's §4 Files touched lists only `selftest.py`, the gotcha record and `memory/gotchas/INDEX.md`, and its
§7 Gates names `runlog selftest` and `memory hygiene` only — not `codebase-map coverage + freshness`,
which units 25 and 27 both name for their dossier edits. So the bar would red at VERIFYING on a leg the
spec never names, over a file the spec's own scope adds. The fix is two lines: add the dossier claim and
the regenerated map to §4, and the leg to §7.

## What this synthesis re-derived

The three specs cite code at `f7bf9d2f`, the read point they declare. This record cites at HEAD
`f87bb884`, where unit 21's build commit and its two follow-ups have moved `record.py` and `selftest.py`
and left `model.py` unchanged. A fix that amends a spec's citation should use the spec's own frame; this
map is for checking the items above against the tree.

| what | the specs' citation, at `f7bf9d2f` | this record, at `f87bb884` |
|---|---|---|
| the window-editing loop | `selftest.py:4335-4339` (25 §1), `:4344-4345` (26 §1) | `selftest.py:4354`, the only `dict(m, ` re-render in the file |
| `COUNTED_STATES` | `record.py:109` (27 §1) | `record.py:110` |
| the `known` test | `record.py:627-635` (27 §1), `:632-635` (27 S3) | `record.py:640`, `derive_known` at `:642-643`, readers at `:660-664` |
| the window facts' render | `record.py:644-645` (25 S1) | `record.py:652-653` |
| the `opened-by` and `closed-by` vocabularies | `record.py:156-157` (25 S1) | `record.py:164-165` |
| `build_class_model` | `selftest.py:4251-4253` (27 §1), `:4247` (26 S1) | `selftest.py:4264` |
| `build_big_model`'s wide rows | `selftest.py:4376-4377` (26 §1) | `selftest.py:4378`, at its definition |
| the idle judgement | `model.py:1682` (27 §1) | `model.py:1682`, unchanged |

Unverified by this synthesis, and named so a later pass knows: the remaining line citations in units 26
§1 and 22's S5 table were not re-derived, since no item above rests on them.
