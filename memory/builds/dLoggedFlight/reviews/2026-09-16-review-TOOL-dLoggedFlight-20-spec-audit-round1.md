**Serves:** spec-audit TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20

# dLoggedFlight — spec audit of units 14, 16 and 20, round 1

*Node `d`, 2026-09-16, on `branch/unattended-build-transparency-ea83a5` at HEAD `15dee87a`. The
subjects are unit 20 at rev-1, the owner's ruling that the committed record carries no journal or
transcript time, which supersedes units 15, 17, 18 and 19; unit 16 at rev-1, promoted from the previous
spec audit; and unit 14 at rev-3, which that ruling moved after its last audit by something other than
that audit's fold. This is ROUND 1 of this subject set, and `.unattended.conf` declares a bound of one
round (`REVIEW_ROUNDS="1"`). The pass was Tier-2 and adversarial: four primed finder lenses, then a
skeptic stage of five batches prompted to REFUTE each finding, then one synthesis, which is this record.
The previous spec audit is
[its record](2026-09-16-review-TOOL-dLoggedFlight-14-spec-audit-round1.md). The labels B1, H1 and so on
are this record's own, and any label that record used is cited with its record named. Every code line
cited below was re-read at `15dee87a`. No file under `tools/` or `.githooks/` differs between
`a6f9d52e`, the head that record read, and `15dee87a`. The severities are this synthesis's
adjudication, not the finders' grades.*

**Reviewed subjects, each pinned at the blob it was read at — ROUND 1:** `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-16.md@487b558587fa49b499500f0c008bd693a1ba1070`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-14.md@04d9b9f9c73b16afb93ba836d833d9079ae16591`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-20.md@62b1e6e630adb74c77a87445e2fbea249b37d6a0`.

## Verdict: BLOCKED

Two blockers stand, and both sit in unit 20. Each is a change to something a closed unit ratified and a
self-test arm pins, made without naming the rule, the arm or the consumer.

- **B1.** Unit 20 cuts the commitment to its digest and line count. `verify` parses the `first` time
  and recomputes from it, so every new record fails `verify`, and unit 9's verify arm reds. Unit 18
  rejected exactly this cut, and unit 20 does not answer that rejection.
- **B2.** Unit 20 stops rendering verb, gate and push rows and deletes `scan_owner_times`. Four existing
  arms read those, and one of them is the arm unit 16 AC4 says must pass unedited. Unit 16 AC4 and unit
  20 AC2 are owed to the same post-build gate run, and they cannot both pass.

Three highs stand beside them. H1 and H2 show that unit 20's own population check reproduces the class
the unit exists to close: it reads `utc` tokens and not `duration` tokens, and its fixture need not reach
the slots that render only under conditions. H3 shows the Summary window is a third derivation of the
run's window, open to HEAD for a build's last run, where a git-only derivation already exists.

The owner's source rule itself is not challenged by any finding. What fails is the inventory of what
reads the things unit 20 retires, and the population of its own backstop. Every item has a fix the spec
can state without a new mechanism. The verdict is BLOCKED because B1 and B2 each leave a builder to
choose which of two ratified criteria to break.

The tally is 2 BLOCKER, 3 HIGH, 3 MEDIUM and 1 LOW, over 9 items folded from 16 confirmed findings.
Unit 20 carries 8 items. Unit 14 carries M3. Unit 16 carries no item of its own, and its AC4 is the
other half of B2. Precision was 0.35, below the retune floor; see "Review shape".

## Run integrity

- Lenses: **4 of 4** returned, **0 died**.
- Skeptic batches: **5 of 5** returned, **0 died**.
- Verdicts: **0** contradictory ones demoted to unverified, **0** spurious ones discarded, **0**
  duplicates.
- Unverified findings: **0**.

Every stage returned, so for this lens set the run is complete. A zero below comes from the lens set
itself, not from an agent that died. Even so, a zero is not evidence of absence. Unit 16 drew no item of
its own, and the 30 refuted reports were not handed to this synthesis, so this record cannot say which
surfaces they covered or whether unit 16 was examined closely.

## Review shape

- Raw findings **46**, confirmed **16**, refuted **30**, unverified **0**, precision **0.35**.
- Precision is below the ~0.5 floor that `AGENTS.md` §8 sets. It rose from 0.27 in the previous spec
  audit. The charter's answer is still to tighten scope or priming before adding agents. This synthesis
  did not see the refuted set, so it cannot say which lens produced the refutations.
- Adjudicated here: **2 BLOCKER, 3 HIGH, 3 MEDIUM, 1 LOW**, over 9 items. Counted by raw finding, the
  split is 4, 6, 5 and 1.
- Six folds take 15 raw findings into 6 items: B1 (38, 29), B2 (39, 30), H1 (1, 20, 43), H3 (40, 31),
  M1 (25, 9) and M2 (41, 6). H2 (2), M3 (16) and L1 (10) are one finding each. The pipeline counted 0
  duplicates because it counts byte-identical reports only, so this merging is the synthesis's decision.
- Raised by fold: 29 and 30 were filed high and take their item's BLOCKER. 43 was filed medium and 31
  was filed medium, and each takes its item's HIGH. 9 was filed low and takes M1's MEDIUM. No finding was
  lowered.
- B1 and B2 are held at BLOCKER on the ground the previous spec audit used for its B1: a pair of criteria
  that cannot both pass, one of which can pass only by reversing a ratified rule the spec does not name.
  Finding 38's skeptic noted that a count-only `verify` can probably be built, so the severity might sit
  below blocker. It is held because no spec authorizes building it, and unit 9's AC5 arm reds either way.

## Findings

| Label | Severity | Unit | Address | Raw | Defect |
|---|---|---|---|---|---|
| B1 | BLOCKER | 20 | §2 S3, §6 AC3, §3 Edges, §4 Alternatives | 38, 29 | the commitment loses `first`, which `verify` parses and recomputes from |
| B2 | BLOCKER | 20, 16 | 20 §2 S2 and S5, §6 AC2 and AC6, §7; 16 §2 S4, §6 AC4 | 39, 30 | retires rows and a function four arms read, one of which unit 16 pins unedited |
| H1 | HIGH | 20 | §2 S1, S3 and S6, §4 ¶1, §6 AC1 and AC3 | 1, 20, 43 | the population check reads `utc` tokens only, and a `duration` carries a journal time |
| H2 | HIGH | 20 | §2 S2 and S6, §6 AC1 and AC2 | 2 | the sentinel fixture need not reach the slots that render only under conditions |
| H3 | HIGH | 20 | §2 S3, §6 AC3, §10, §3 Edges | 40, 31 | a third window derivation, open to HEAD, where a git-only one exists |
| M1 | MEDIUM | 20 | §2 S3, §4 Inventory | 25, 9 | `window opened by` and `window closed by` keep naming journal closers |
| M2 | MEDIUM | 20 | §2 S8, §6 AC7, §3 Edges | 41, 6 | AC7 cannot see the old routing, and there is no Edge to unit 12 |
| M3 | MEDIUM | 14 | §2 S4, §6 AC7 | 16 | S4's in-window clause for an extracted local session has no observation |
| L1 | LOW | 20 | §2 and §4 Files touched | 10 | the gotcha still describes the refusal S5 removes |

### B1 — BLOCKER — unit 20 §2 S3, §6 AC3, §3 Edges, §4 Alternatives rejected — raw 38, 29

**Defect.** S3 says "The commitment renders its digest and line count, never a line's time", and AC3
requires that. `COMMITMENT_RE` (`tools/runlog/record.py:115`) requires `first (\S+) · last (\S+)` after
the line count. `check_commitment` (`record.py:993`) refuses a line that does not fullmatch it, then
passes `first` to `measure_commitment` as the floor it recomputes from (`record.py:1035`, the floor at
`:961-964`), and compares all four fields (`:1036`). Unit 9 S5, a closed unit, defines the commitment as
including "first and last timestamps" and says `verify` hashes lines "from the committed first" timestamp
on. Unit 18 §4 rejected dropping these fields because "`first` is the verify floor". Unit 20 names none of
`verify`, `check_commitment`, `measure_commitment`, unit 9 S5, unit 9 AC5 or unit 18's rejection. The
`RECORD_SCHEMA` commitment template also still carries `first {utc} · last {utc}`.

**Impact.** Built as written, every record rendered after this unit fails `COMMITMENT_RE`, so `runlog.py
verify` raises "the commitment line is not the schema's shape" and exits 2 on every one. The commitment
is then never checkable. `test_record_ac5_verify` (`tools/runlog/selftest.py:4422`) asserts
`lines 6 · ` followed by a further field (`:4433`), so that arm reds. The previous spec audit's H1 fix
already required that any change to these times say how `verify` changes. A builder must either keep a
journal time, against unit 20, or break `verify`, against unit 9.

**Fix.** Add an S item that redefines the commitment and `verify` together:

1. The new commitment template, and the matching `COMMITMENT_RE`.
2. What anchors the recompute once `first` is gone. One option is the first `count` lines of the model's
   `journal_lines` in time order.
3. Unit 18 S5's case, a line earlier than the old floor, under the new anchor.

Supersede unit 9 S5's "first and last timestamps" clause and its AC5 arm by name, with a unit 9 rev line.
Add an Edge naming `measure_commitment` and `check_commitment`, and an Alternatives line answering unit
18's rejection. Add an AC: under the new template, `verify` reads `match` on an untouched journal and on
one with a line appended, and `mismatch` on an edited one.

**Left-shift.** Add a render-then-parse arm over every `RECORD_SCHEMA` template that has a parser
constant beside it. It renders the fixture, parses each such line with its regex, and reds on a template
the parser cannot read. `COMMITMENT_RE` is the one known today. A template change and its parser can then
no longer drift apart in a spec or in code.

### B2 — BLOCKER — unit 20 §2 S2 and S5, §6 AC2 and AC6, §7; unit 16 §2 S4, §6 AC4 — raw 39, 30

**Defect.** Unit 20 retires things that existing arms read, and lists none of those arms:

- `test_record_ac10_unknown_counts` (`selftest.py:4689`) ends by asserting the `rc` cell of a `--close`
  verb row on the Timeline (`:4749-4755`). S2 stops rendering verb rows, so the rows it collects are
  empty and the check reds.
- `test_record_ac9_owner_times` (`selftest.py:4601`) calls `scan_owner_times` (`:4661`), which S5
  deletes. AC6's grep covers `record.py` only, so it passes while the arm has no function to call.
- `test_record_ac4_classes` (`selftest.py:4289`, the check at `:4297-4300`) and
  `test_schema_ac1_render_then_grade` (`selftest.py:4822`, the check at `:4837-4842`) require every member
  of the `gate-verdict` and `push-decision` vocabularies in the rendered cells. Those vocabularies appear
  only in the Timeline `push`, `push-refused` and `gate` row layouts (`record.py:213-215`), which S2
  removes. The `event` vocabulary's journal members go the same way.

Unit 16 S4 says the AC10 arm "stand[s] unedited", and unit 16 AC4 is red when
`test_record_ac10_unknown_counts` "needs an edit to pass". Unit 20 makes that edit necessary. Unit 20
supersedes only units 15, 17, 18 and 19, and declares no change to unit 9 AC9, AC10 or AC4, or unit 10
AC1. Its §7 says the assertion floor (`ASSERTION_FLOOR = 1291`, `selftest.py:114`) is "raised by the arm
count", when arms must be removed.

**Impact.** `runlog selftest` goes red when unit 20 lands, and its floor has to fall. Unit 16 AC4 and
unit 20 AC2 are observed in the same post-build gate run, since units run no gates and the bar runs once
after every unit is built. They cannot both pass. This is the shape the previous spec audit raised to
BLOCKER as its B1.

**Fix.** Add a scope item in unit 20 that lists each arm it retires or rewrites, and what replaces each:

- unit 9 AC9, which retires with the refusal;
- the verb-row half of unit 9 AC10, moved to the local model or dropped;
- the vocabulary checks of unit 9 AC4 and unit 10 AC1, narrowed to the vocabularies that still render;
- the vocabularies `RECORD_SCHEMA` drops, and the `build_big_model` timeline counts of unit 9's AC6 cap
  arm, which rest on journal rows.

Re-declare `ASSERTION_FLOOR` with a reason. Add unit 9 and unit 10 rev lines recording the supersession.
Restate unit 16 S4 and AC4 so "unedited" covers only the counts half of the AC10 arm, or add an Edge
between units 16 and 20 that orders the edit.

**Left-shift.** This is the second consecutive spec audit whose blocker is this shape, so the documented
check the previous record proposed did not bind. Make it a candidate gate: for each spec, collect the
backticked identifiers in its scope items that it removes or stops rendering, grep `selftest.py` and the
other specs' AC text for them, and require every hit to be named in the spec. Per charter §7, run that
predicate over the tree first and print hits and near misses, because "removes" is a prose judgement and
the predicate may red innocent specs.

### H1 — HIGH — unit 20 §2 S1, S3 and S6, §4 ¶1, §6 AC1 and AC3 — raw 1, 20, 43

**Defect.** S1 declares sources for every `utc` and `duration` slot, so the spec treats a duration as a
time. S6 and AC1 read only `utc` tokens. The schema's `duration` shape is `[0-9]{1,12}s`
(`record.py:142`), which is not a `utc` token. S3 says the Summary duration is the difference between
the commits and is "Observed by AC3", but AC3's then-clause names only the window and the commitment.
`build_summary_facts` computes `dur` from the model window's start and end (`record.py:624`), which is
the journal-bounded window. §4 ¶1 says "a slot that escapes the declaration still fails", which is false
for the duration class.

**Impact.** A build that moves only the `window` strings to commit times, and declares the duration slot
`git`, passes the declaration check and every AC while rendering a journal-derived duration. Where the
rendered start equals the model's git-opened start, the start plus the duration is the journal-derived
end. That is the time-plus-duration recovery the previous closing review recorded as its round-1 B1, and
the class `memory/gotchas/withheld-value-recovered-from-a-derived-one.md` names.

**Fix.** Widen S6 and AC1 to every shaped time token in the markdown and the Data twin, `utc` and
`duration`. Each duration must equal a difference of two fixture commit or run-state times, and no
rendered `utc` plus a rendered `duration` may equal a sentinel. Add to AC3: the Summary duration equals
the last era commit's committer time minus the first's, red when it differs. Pin §5's empty-era case:
with no commits in the era, both the window and the duration render `-`.

**Left-shift.** Stage AC1 RED with one duration taken from a journal event. Derive the arm's token
classes from `RECORD_SCHEMA`'s shaped classes that S1 declares, never from a typed pair, so a third
time-bearing class cannot fall outside the check the way `duration` did.

### H2 — HIGH — unit 20 §2 S2 and S6, §6 AC1 and AC2 — raw 2

**Defect.** AC1's sentinel arm reads only the slots its fixture happens to render, and nothing requires
the fixture to reach the conditional ones. The Timeline `elided` fact renders only once the timeline
passes twice `TIMELINE_EDGE`, which is 30 (`record.py:78`, `:710`). S2 says "The elided line's times come
from the rows kept. Observed by AC2", but AC2 says nothing about the elided fact. §4 claims the sentinel
arm catches a slot that escapes the declaration, which holds only for slots the fixture fills. The
skeptic narrowed this: AC3 covers the commitment's times, AC4 covers the Anomalies and Coverage columns,
and review rounds are read from run-state rows (`record.py:572-576`). The elided fact remains uncovered.

**Impact.** A build that computes the elided range from the unfiltered timeline puts two journal times in
every long run's record, and a fixture of 60 rows or fewer passes AC1 and AC2. That is the fixture that passes
by finding nothing, and the prior rounds found their leaks in exactly such conditional slots.

**Fix.** Name AC1's required fixture population: timeline events past the elision bound, a commitment, at
least one anomaly per kind, a review round, and each journal source. Add an AC2 clause that the elided
fact's times equal kept-row times, red when either equals a sentinel.

**Left-shift.** Add a liveness assertion to the sentinel arm: every time-bearing slot `RECORD_SCHEMA`
declares rendered at least one token, red naming the slot that rendered nothing. The slot list is
derived from the schema, so a new conditional slot joins the check without an edit.

### H3 — HIGH — unit 20 §2 S3, §6 AC3, §10 Reuse audit, §3 Edges — raw 40, 31

**Defect.** S3 takes the window from "its first and last commits in the run's era". The era does not
bound the run. `derive_run_eras` leaves `t1` None for a build's last run (`tools/runlog/model.py:349-357`),
so its era is open to HEAD. `era_commits` holds every descendant of the start commit on both the run
branch and the default branch (`model.py:1374-1375`). A git-only window already exists: `check_run_states`
derives each run's window through `derive_window(float(run["t"]), "git", phases, terminal)` over
`derive_record_commits` (`record.py:1412-1423`). That function is shared "so the two cannot bound a run's
writes differently" (`model.py:393-399`). The Reuse audit names none of these seams, and there is no Edge
to unit 10 S6.

**Impact.** A re-render after the default branch moves on, or of a run whose successor started days
later, shows a window and duration reaching unrelated later commits. The end moves with every re-render,
which unit 8 S2 rejected. The own-commit form of this defect was already fixed once, as M4 of the first
closing review (`model.py:1473-1477`). The rendered window would also disagree with the window the schema
leg grades for overlap.

**Fix.** Render the window from the derivation `check_run_states` uses: `derive_window` with
`start_from="git"` over `derive_record_commits`, with no `last_event`. Name that derivation and unit 10 S6
in the Reuse audit and the Edges. State what the duration renders under it. Add AC3 arms: the rendered
window equals the leg's window for the same run, and a later commit on the default branch leaves it
unchanged.

**Left-shift.** The equality arm is the gate. Stage it RED against an era-bounded implementation with one
later default-branch commit in the fixture, so the arm is observed failing on the shape M4 once shipped.

### M1 — MEDIUM — unit 20 §2 S3, §4 Inventory — raw 25, 9

**Defect.** The Summary keeps `window opened by` and `window closed by` (`record.py:182-183`), rendered
from the model window's `start_from` and `end_from` (`record.py:644-645`). The `closed-by` vocabulary is
`terminal-end`, `terminal-write` and `last-activity` (`record.py:157`). `terminal-end` names a driver END
line and `last-activity` the latest event plus one second (`model.py:414-422`). S3 neither retires nor
redefines these facts, no AC observes them, and §4's Inventory declares no vocabulary change.

**Impact.** The record prints commit-derived bounds beside a provenance fact naming a journal close, which
is a false statement in the public record and in any Skill answer built on it. The alternative is an
implementer widening a closed vocabulary the spec never declared.

**Fix.** In S3, either retire both facts from the committed Summary and keep them in the local model, or
state the vocabulary they render under S3's window and list that change in the Inventory. Add an AC3 arm
asserting the values, red when a journal-derived closer renders.

**Synthesis note, not seen by a skeptic.** Decide this with H3. Under the git-only derivation H3 proposes,
`start_from` is always `git`, and `end_from` is `terminal-write` or `last-activity` computed from
run-state commits only (`model.py:416-422` with `term_end` and `last_event` None). The facts could then
stay with `terminal-end` retired from `closed-by` and `driver` from `opened-by`.

**Left-shift.** The vocabulary liveness list in `test_record_ac4_classes` (`selftest.py:4297`) is typed,
and it omits `opened-by` and `closed-by`. Derive it from `RECORD_SCHEMA["vocab"]` instead, so a member no
render can reach reds and forces the decision this item asks for.

### M2 — MEDIUM — unit 20 §2 S8, §6 AC7, §3 Edges — raw 41, 6

**Defect.** AC7's only observation is a grep for the new phrase `no event times`. Its Red-when names the
old routing, which no such grep can see. `tools/runlog/SKILL.template.md` still routes "what it did
between two times" to "the record's Timeline" first (line 61), and its description says "from the run's
committed record first" and quotes "what did it do between 09:01 and 10:52" (lines 4-7). S8 reverses unit
12's ratified routing, and unit 20 has no Edge to unit 12. Unit 16 carries its Edge to unit 12 for this
same file, and unit 12 rev-4 carries the reciprocal hands-off.

**Impact.** A build that adds the sentence and leaves the description and the table row passes AC7. The
Skill then gives two answers to one question, and its trigger text still sends time questions to the
committed record first. That is the class `memory/gotchas/amendment-leaves-its-other-half-standing.md`
records.

**Fix.** Add a consumes-from Edge to unit 12 naming the description and the question table, with a unit
12 rev line. Extend S8 and AC7: the rendered Skill's "between two times" row reads first from the local
`model` timeline, and the description no longer sends a time question to the committed record first. Red
when either still names the record's Timeline as the first source for a time.

**Left-shift.** A documented spec-audit check: an AC that observes an amendment greps for the old text's
absence as well as the new text's presence. Stage AC7 RED against the current Skill with the sentence
added and the row left.

### M3 — MEDIUM — unit 14 §2 S4, §6 AC7 — raw 16

**Defect.** S4's local-transcript rule has two clauses. A session is dropped unread when its files'
latest modification time is before the window's start, and "once extracted, it is kept only when an event
lies inside the window". AC7's local-transcript arm uses files modified before the start, so it reaches
only the first clause. AC3's local session is the run's own, with events in the window. No arm has files
modified at or after the start and every event before it.

**Impact.** A session whose tree files were touched after the window's start, by a copy or a checkout,
but whose events all precede it, is extracted and kept. The Coverage `sessions` extracted count is
inflated, and every AC passes. S4's "Observed by AC3 and AC7" is false for half the rule.

**Fix.** Add an AC7 arm: an earlier session with its transcript local, files modified at or after the
window's start, and every event before it. It is extracted once and excluded from the extracted count,
red when it is counted.

**Left-shift.** A documented spec-audit check: a scope rule written as several clauses carries one arm
per clause, and each arm's fixture is the one that separates its clause from the others.

### L1 — LOW — unit 20 §2 (absent item), §4 Files touched — raw 10

**Defect.** Under its fix section, `memory/gotchas/withheld-value-recovered-from-a-derived-one.md` says in
the present tense that `tools/runlog/record.py` "refuses the whole record" on an owner-second match (line
46). That is the refusal S5 removes. No S item updates the gotcha, and it is not in Files touched. The
superseded unit 15 carried this update in its S6. The finding's skeptic confirmed that
`gotchas.py --for-paths tools/runlog/record.py` selects this gotcha.

**Impact.** After unit 20 lands, the checklist handed to reviewers of `record.py` describes a guard that no
longer exists.

**Fix.** Add an S item and a Files-touched entry that rewrite the gotcha's fix section to the source
rule. Add an AC: a grep for `refuses the whole record` in that file finds nothing.

**Left-shift.** A documented spec-audit check: for a unit that removes a mechanism, run
`python tools/memory-tree/gotchas.py --for-paths` over its Files touched and read each selected gotcha
for that mechanism. A symbol grep would not catch this one, because the gotcha describes the refusal in
prose and never names `scan_owner_times`.

## Classes across the set

- **A retirement with no inventory of its readers.** B1, B2, M2 and L1 each remove or change something
  (a commitment field, row kinds and a function, a routing, a documented guard) and name none of what
  reads it: `verify`, four arms, the Skill's description and table, a gotcha. The previous spec audit's B1
  and M2 were the same class, a change to a rule another unit pins with no Edge naming it. This is its
  second consecutive blocker, which is why B2's left-shift proposes a gate rather than another documented
  check.
- **The population is narrower than the class.** H1 and H2 are this class's fourth appearance, after the
  first closing review's B1, R2-H1 of the second, and the previous spec audit's H1 to H3. Unit 20 §4 says
  the class ends here because the population is the rendered text. Its check still enumerates a token
  class and a fixture, one level down.
- **A check that cannot fail on the break it names.** M2's grep for new text, M3's unobserved clause, and
  H2's "Observed by AC2" for a fact AC2 never reads.
- **Two derivations of one fact.** H3 and M1: the window and its provenance, derived once for the schema
  leg and again, differently, for the render.

## Disposition

The rule is `memory/guides/BUILD-METHOD.md` and the unattended Skill's BOUNDED state, not this record's
choice. At a one-round bound this subject set exits BOUNDED, and every confirmed item is disposed by
severity. B1, B2 and H1 to H3 are promoted to units whose mechanisms close them, audited as specs by a
fresh harness invocation, and the round records `--disposition promote`. M1 to M3 and L1 fold into their
specs as rev bumps with §9 lines.

Three groupings may save the promotion a round. B1 is self-contained: the commitment and `verify`
together. B2, H1 and H2 share one inventory, of what unit 20 retires and of every time-bearing slot the
schema declares, and could be one unit whose arm is derived from `RECORD_SCHEMA`. H3 and M1 share the
window decision, so M1's fold should state its vocabulary against H3's chosen derivation rather than
ahead of it.

## Synthesis observations, outside the tally

- All three specs state `base 4cf0944d`, where `tools/runlog` does not exist. The previous record raised
  this and it is unchanged. No skeptic saw it, and it is not counted.
- AC6's grep for `scan_owner_times` names `tools/runlog/record.py` only. `tools/runlog/README.md:289` and
  `selftest.py:4661` also name it. B2 covers the arm, and the README is in Files touched, but AC6 as
  written would pass with either left. Not counted.

## What this synthesis re-derived

- All three subject blobs equal `git rev-parse HEAD:<path>` at `15dee87a`.
- `git diff --stat a6f9d52e 15dee87a -- tools .githooks` is empty.
- B1: `COMMITMENT_RE` at `record.py:115`, `check_commitment` at `:993`, the `first` floor passed at
  `:1035` and the four-field comparison at `:1036`, the floor filter at `:961-964`. Unit 9 spec lines
  95-100 give S5's first and last timestamps and the floor. Unit 18 spec line 123 gives "`first` is the
  verify floor". The AC5 arm's `lines 6 · ` regex is at `selftest.py:4433`.
- B2: the AC10 arm's `--close` verb-row check at `selftest.py:4749-4755`, the AC9 arm's call at `:4661`,
  the vocabulary checks at `:4297-4300` and `:4837-4842`, `ASSERTION_FLOOR = 1291` at `:114`. The
  `gate-verdict` and `push-decision` vocabularies appear only in the row layouts at `record.py:213-215`.
  Unit 16 spec line 51 ("stand unedited") and line 163 ("needs an edit to pass").
- H1: the `duration` shape at `record.py:142`, `dur` computed from the model window at `:624`.
- H2: `TIMELINE_EDGE = 30` at `record.py:78`, the `elided` fact at `:710`, review rounds read from
  run-state rows at `:572-576`.
- H3: `derive_run_eras` at `model.py:349-357`, `derive_record_commits` and its shared-bound docstring at
  `:393-399`, `era_commits` at `:1374-1375`, the M4 comment at `:1473-1477`, and `check_run_states`'
  git-only window at `record.py:1412-1423`.
- M1: `closed-by` at `record.py:157`, the facts at `:182-183` and `:644-645`, `derive_window`'s closers at
  `model.py:414-422`. The typed liveness list at `selftest.py:4297` omits `opened-by` and `closed-by`.
- M2: the Skill template's description at lines 4-7 and the table row at line 61. Unit 12 rev-4's
  hands-off to unit 16 at its spec line 65.
- M3: unit 14 spec lines 40-42 (S4's two clauses) and 146-151 (AC7).
- L1: the gotcha's "refuses the whole record" at its line 46, and no occurrence of `scan_owner_times` in
  it.

Two claims come from verification and were not re-derived: that `gotchas.py --for-paths
tools/runlog/record.py` selects the L1 gotcha, and that the AC6 cap arm's `build_big_model` counts rest on
journal rows.

## What this pass did not cover

- The 30 refuted findings are not reproduced or characterized here.
- No code exists for units 14, 16 and 20. The specs were audited against the tools at `15dee87a`.
- How units 14, 16 and 20 interact once built was examined only where B2 and M3 touch it. Unit 16's own
  scope drew no confirmed item, and that is not evidence it is sound (see "Run integrity").
- The owner's source rule was taken as given. Whether commit and run-state times near an owner turn are
  acceptable, which unit 20 §4 ¶2 argues, was not audited.
- No gate was run over the specs. This record is not yet bound into the build index. The three specs'
  `gen:spec-records` regions and the README's records line need re-rendering in the commit that lands it.
