**Serves:** spec-audit TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-15

# dLoggedFlight — spec audit of the two promoted units, round 1

*Node `d`, 2026-09-16, on `branch/unattended-build-transparency-ea83a5` at HEAD `a6f9d52e`. The
subjects are the two units that closing diff review round 2 promoted at its NON-CONVERGENT exit: unit
14 from R2-B1 and unit 15 from R2-H1. This is ROUND 1 of their spec audit, and `.unattended.conf`
declares a bound of one round. The pass was Tier-2 and adversarial: four primed finder lenses, then a
skeptic stage of five batches prompted to REFUTE each finding, then one synthesis, which is this
record. Round 2 of the closing review is
[its record](2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md), and its labels keep
their `R2-` prefix here. The labels B1, H1 and so on are this record's own. Every code line cited
below was re-read at `a6f9d52e`. No file under `tools/` or `.githooks/` differs between that commit
and `37d4b899`, the head round 2 read, so a line either record cites is the same line. The severities
are this synthesis's adjudication, not the finders' grades. What this synthesis measured itself is
listed under "What this synthesis re-derived".*

**Reviewed subjects, each pinned at the blob it was read at — ROUND 1:** `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-14.md@11a64af559d7089ca685d9539cc7a6c3fa5a539d`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-15.md@53ae51c96983e0bc7f9aa6f558ec074e26496ac6`.

## Verdict: BLOCKED

One blocker stands. Unit 14 withholds the transcript counts under `partial`. Unit 9, a closed unit,
renders them under `partial`, and a self-test arm pins that. Unit 14's own every-session test withholds
in the exact case that arm asserts integers for. So the two criteria cannot both pass, and unit 14
names neither the rule it reverses nor the arm it reds.

Five highs stand beside it. Each unit leaves open a path of the leak it was promoted to close:

- H1. In unit 15, the Summary commitment's `last` time is the held line's time.
- H2. In unit 15, a `verdict=NONE` gate line still closes the window's rendered end, plus one second.
- H3. Unit 15's class gate enumerates row kinds only, so it cannot see H1 or H2.
- H4. Unit 14's independent refusal compares whole seconds, and the measured leak ends minutes after
  the turn.
- H5. On the shipped default no session is named, so unit 14's independent refusal has nothing to
  re-read.

The design of each unit holds. Unit 14 reads the live transcript before the cache and gives the cache a
freshness key. Unit 15 holds and counts the rows an owner act causes. What fails is enumeration: each
rule runs over a narrower population than the leak runs through. Every high is a scope line or a
predicate a fix can state, and none needs a mechanism the build lacks. The verdict is BLOCKED because
B1 leaves the builder a decision about another unit's ratified rule that the spec never makes.

The tally is 1 BLOCKER, 5 HIGH, 4 MEDIUM and 0 LOW, over 10 items folded from 13 confirmed findings.
Precision was 0.27, below the retune floor; see "Review shape".

## Run integrity

- Lenses: **4 of 4** returned, **0 died**.
- Skeptic batches: **5 of 5** returned, **0 died**.
- Verdicts: **0** contradictory ones demoted to unverified, **0** spurious ones discarded, **0**
  duplicates.
- Unverified findings: **0**.

Every stage returned, so for this lens set the run is complete. A zero below comes from the lens set
itself, not from an agent that died. Even so, a zero is not evidence of absence. The 35 refuted reports
were not handed to this synthesis, so this record cannot say which surfaces they covered.

## Review shape

- Raw findings **48**, confirmed **13**, refuted **35**, unverified **0**, precision **0.27**.
- Precision is below the ~0.5 floor that `AGENTS.md` §8 sets. The charter's answer is to tighten scope
  or priming before adding agents. The subject was two short specs, and 35 refutations suggest lenses
  primed wider than their subject. This synthesis did not see the refuted set, so it cannot say which
  lens produced them.
- Adjudicated here: **1 BLOCKER, 5 HIGH, 4 MEDIUM, 0 LOW**, over 10 items. Counted by raw finding, the
  split is 3, 6, 4 and 0.
- Two folds take 5 raw findings into 2 items: B1 (14, 26, 40) and H2 (16, 4). Raw 4 has a second
  clause about AC2's red. That clause corroborates M1 and is counted once, under H2. The other 8 raw
  findings are one item each. The pipeline counted 0 duplicates because it counts byte-identical
  reports only, so this merging is the synthesis's decision.
- One item was raised. B1's three members were each filed high, and B1 is raised to BLOCKER on the
  ground round 1 of the build's spec audit used for its own B1 and B4: a pair of criteria that cannot
  both pass, one of which can pass only by reversing a ratified rule the spec does not name. No finding
  was lowered.
- Unit 14 carries B1, H4, H5, M3 and M4, which is 7 raw findings. Unit 15 carries H1, H2, H3, M1 and M2,
  which is 6.

## Findings

| Label | Severity | Unit | Address | Raw | Defect |
|---|---|---|---|---|---|
| B1 | BLOCKER | 14 | §2 S2 and S3, §6 AC2, §3 Edges | 14, 26, 40 | withholds counts under `partial`, which unit 9 S4 and AC10 render |
| H1 | HIGH | 15 | §2 S1 to S5, §6 AC1 and AC2, §5 | 29 | the commitment's `last` is the held line's time |
| H2 | HIGH | 15 | §2 S3, §6 AC1, §5 | 16, 4 | a `verdict=NONE` gate line still closes the window's rendered end |
| H3 | HIGH | 15 | §2 S5, §4 ¶2, §6 AC5 | 31 | the class gate's population is row kinds, and timed facts have no kind |
| H4 | HIGH | 14 | §2 S5, §4 ¶1, §6 AC5 | 27 | the independent refusal compares seconds, and the measured leak ends minutes later |
| H5 | HIGH | 14 | §2 S5 and S4 | 28 | on the shipped default no session is named, so S5 re-reads nothing |
| M1 | MEDIUM | 15 | §6 AC2 | 18 | AC2's window-end red cannot fire against unchanged code |
| M2 | MEDIUM | 15 | §2 S3, against unit 8 §2 S2 | 41 | S3 does not say whether the model's window moves or only its rendering |
| M3 | MEDIUM | 14 | §2 S3 against S4, §6 AC3 | 21 | S3's every-named-session test is vacuous on the discovered path |
| M4 | MEDIUM | 14 | §2 S4, §4 ¶2 | 35 | the discovered path takes every earlier run's sessions of the build |

### B1 — BLOCKER — unit 14 §2 S2 and S3, §6 AC2, §3 Edges — raw 14, 26, 40

**Defect.** Under S2, a session whose only source falls short of the window reads `partial`. S3 then
withholds the owner-turn, usage and attributed-call facts unless every named session's source covers
the window's end. It says they render `-` "as the M6 fold renders them for `not-local`". AC2 requires
that `-`.

**The rule it collides with.** Unit 9 S4, at rev-7 (its spec line 85), renders those counts as `-`
only where the transcripts' coverage reads neither `present` nor `partial`. `tools/runlog/record.py:109`
implements that as `COUNTED_STATES = ("present", "partial")`, and its comment calls `partial` a lower
bound. The arm `test_record_ac10_unknown_counts` (`tools/runlog/selftest.py:4689-4723`) builds a
fixture whose second named session has no local transcript. That fixture reads `partial`, and the arm
asserts every count renders as an integer.

**Why the pair cannot both pass.** In that arm's fixture the second session has no source at all, so
no source of it covers the window's end. S3's literal test withholds there, and the arm demands
integers. Renaming the state does not help, because S3 tests sessions, not the state's name. Unit 14's
only Edge to unit 9 concerns the refusal. S3's own gloss cites the `not-local` rendering and leaves out
the `partial` carve-out. So a builder either fails AC2 or reds unit 9's arm, and either way rewrites a
closed unit's accepted behaviour with no spec authority. Two more texts would be left behind. One is
the runlog Skill's "No local transcript" paragraph (`tools/runlog/SKILL.template.md:73`), which names
only `not-local`. The other is round 2's recorded fix for R2-M2, which keys its marker on the same
`COUNTED_STATES` test.

**Why BLOCKER.** All three members were filed high. The raise is explained under "Review shape".

**Fix.** Decide in S3 and write the decision down. There are two options:

1. Give a stale or field-less extract a coverage outcome the renderer withholds and `COUNTED_STATES`
   does not hold: a new state, or a per-session covers-window flag. `partial` keeps unit 9's
   lower-bound meaning. Restate S3's test over the sessions that have a source.
2. Supersede unit 9 S4's `partial` clause and AC10's near-miss arm by name. Add a unit 9 rev line, an
   Edge naming the count rule, and `tools/runlog/SKILL.template.md` in Files touched.

Either way, name `tools/runlog/record.py` in AC2's Red-when, and point the R2-M2 fold at the same
predicate.

**Left-shift.** Add one arm, owned by whichever unit holds the decision, that renders three `partial`
shapes side by side: a stale extract, a field-less extract, and a named session with no source. It
asserts each one's counts against the single predicate, so two units cannot pin opposite answers for
one state. Add a documented spec-audit check: when an S item changes an identifier that another unit's
AC pins, `COUNTED_STATES` here, the spec carries an Edge to that unit naming the rule. A candidate gate
would grep each spec's backticked identifiers against the other specs' ACs. Per charter §7, run that
predicate over the tree and print hits and near-misses before wiring it.

### H1 — HIGH — unit 15 §2 S1 to S5, §6 AC1 and AC2, §5 — raw 29

**Defect.** The Summary `commitment` fact renders `first {utc}` and `last {utc}`
(`tools/runlog/record.py:196`). `measure_commitment` (`record.py:936-972`) sets `last` to the time of
the latest line in the model's `journal_lines`. Those lines include every in-window driver line and
every joined gate line (`tools/runlog/model.py:1718-1719`). In AC2's run, whose last event is the unclean
END, `last` is that END's second. In AC1's run it is the END or the NONE gate line, 10 ms after the
interrupt. S1 to S4 hold rows and the window's end, and no S item touches the commitment. S5's gate
never reads a Summary fact (H3).

**Impact.** Both outcomes are wrong.

- When the held line falls in the turn's own second, `scan_owner_times` matches the UTC token and a
  production render is refused. AC1 requires "refuses nothing". AC1 can still pass, but only because
  `render_record` defaults to `commitment=None` (`record.py:878`), while `record --write` passes a real
  commitment (`record.py:921`). The fixture is therefore not the production shape.
- When the held line falls across a second boundary, the refusal misses it. The record then publishes
  the interrupt's time to within the producer's latency. That is R2-H1's leak through a sibling path,
  so §5's "removes the last measured path" is false.

**Fix.** Add a scope line for the commitment's `first` and `last` when either falls on a held line.
Withhold or coarsen it in a form `check_commitment` can still verify. That function recomputes and
compares all four fields, `last` included (`record.py:1035-1036`), so the new scope line must say how
verify changes too. Make AC1 and AC2 render with a real commitment, and assert that no commitment time lies within
`OWNER_ACT_BAND_S` of the turn.

**Left-shift.** Add a whole-record band arm. It renders AC1's fixture with a real commitment and scans
every UTC token in the text, not a list of rows. The fixture's only in-band events are held kinds, so
the arm can assert that no token lies within `OWNER_ACT_BAND_S` of the turn. Stage it RED against rev-1
as specified. The same arm catches H2, and its population is the one H3 asks for.

### H2 — HIGH — unit 15 §2 S3, §6 AC1, §5 — raw 16, 4

**Defect.** S3 keeps only an unclean END from closing a non-terminal window's rendered end. S1 names the
`verdict=NONE` gate line as owner-caused too, and S3 ignores it. `tree_ts` takes every gates-journal line
of a held tree whatever its verdict (`model.py:1450-1453`). That feeds `last_event` (`:1459`), and
`derive_window` sets a non-terminal end to `latest + 1.0` (`:420-422`). In AC1's fixture the NONE gate
line comes 10 ms after the interrupt. When it is the last event, the Summary `window` and `duration`
facts (`record.py:181`) place the interrupt to about one second.

**Impact.** The rendered end falls in the turn's second plus one, or plus two across a boundary.
`scan_owner_times` compares exact seconds, so it misses. AC1 checks rows only and stays green. The path
R2-H1 named at `model.py:1459` stays open for a line S1 itself calls owner-caused.

**Fix.** Widen S3: no event of an `OWNER_CAUSED_KINDS` kind closes a non-terminal window's rendered end.
Say whether the one second is still added to the next event, and which window moves (M2). Add a clause
to AC1: neither the window's end nor the duration lies within `OWNER_ACT_BAND_S` of the turn. Add an arm
in which a NONE gate line is the last event.

**Left-shift.** Add the H1 whole-record band arm, with a fixture variant whose last event is the NONE
gate line.

### H3 — HIGH — unit 15 §2 S5, §4 ¶2, §6 AC5 — raw 31

**Defect.** S5's arm enumerates "the kinds the renderer emits a UTC for" from `record.py`'s layout
table, and requires each kind to be in exactly one of the two sets. The table keys rows by kind in the
Timeline events table, which has 13 row kinds. Its skeptic refuted one part of raw 31. The Anomalies table
(`record.py:268-269`) declares a `utc` column beside an `anomaly-kind` column, so `killed-verb` is
reachable. The rest stands. The schema carries times that have no kind at all:

- the Summary `window` and `commitment` facts;
- the Timeline `elided` fact;
- the `utc` column of the `rounds` table;
- the `utc` column of the Coverage `sources` table.

**Impact.** A new timed fact or column is invisible to the gate. That is exactly where this unit's held
times already leak (H1, H2). §4's "the next timed kind reds until it is classified" holds only for a new
Timeline row kind. Unit 15 §4 presents the gate as what stops a third fold of one class, and the gate
inherits the narrowing that causes it.

**Fix.** Define the arm's population explicitly as every `utc`-shaped slot in `RECORD_SCHEMA`: each
`{utc}` in a fact template and each `utc` column of a table. Expand a column keyed by `anomaly-kind` or by
a Timeline row kind through its vocabulary. Every other slot is classified by its section and label.
Say so in S5 and AC5.

**Left-shift.** The arm is the gate. Before landing it, stage a copy of the schema that adds one
`{utc}` fact label, and confirm the arm reds. That observes its failing case, as charter §7 requires.

### H4 — HIGH — unit 14 §2 S5, §4 ¶1, §6 AC5 — raw 27

**Defect.** S5 passes independently read owner turns to `scan_owner_times`. That function
(`record.py:830-875`) refuses a UTC token only when it falls in a turn's own second. It refuses an idle
row only when the row's start plus its duration falls in that second or the next. Round 2 measured
R2-B1's gaps ending "within two minutes after" a real owner turn that the stale extract did not hold.
The leak's precision is the reply latency, not the second. Unit 15 S4 keeps the same-second comparison
"for every other time", which includes idle rows. Unit 14 §4 rejects widening the band.

**Impact.** The backstop cannot refuse the measured regression shape. AC5 says "an idle row ending
beside a turn", which admits a fixture ending in the turn's own second, and that fixture goes green. §4's
claim that "a future regression in the model's turns is caught at render" is false.

**Why round 2's O2 does not bind the fix.** This is the synthesis's own reasoning, and no skeptic saw
it. `derive_idle_gaps` (`model.py:817-842`) already holds any gap that contains a turn the model knows,
or lies within `IDLE_OWNER_GUARD_S` of one. That constant equals `IDLE_GAP_S`, 900 s (`model.py:92`,
`:98`). A refusal that compares idle rows with independently read turns at that same guard can
therefore fire only where the model and the transcript disagree. It does not refuse ordinary records,
which was O2's objection to a band on every time.

**Fix.** In S5, refuse an idle row when an independently read turn lies inside it or within
`IDLE_OWNER_GUARD_S` of either end. Pin AC5's fixture to gaps ending more than one second, and less than
the guard, after the turn. Reconcile unit 15 S4's "every other time" so that it excludes idle rows.

**Left-shift.** Give AC5 two endings, 30 s and 600 s after the turn, each staged RED against the current
`scan_owner_times`. Add a near miss in which the model's turns equal the transcript's, and assert that
nothing refuses. That near miss is the mutation test of the control.

### H5 — HIGH — unit 14 §2 S5 and S4 — raw 28

**Defect.** S5 re-reads turns only "when a named session's transcript is local". S4 extends S1 and S2 to
discovered sessions, but not S5. The model exposes only journal-named sessions (`sessions=sids`,
`model.py:1703`), and `sids` comes from the `sess.*` fields of the driver's lines (`model.py:645`,
`:1489`). The kit ships `RUNLOG_SESSION_VARS=""` (`tools/unattended/unattended.sh:343`), so an adopter on
the default records no `sess.*` field and names no session. The discovered branch of
`resolve_run_sessions` (`model.py:699-708`) keys its extracts internally and never exposes their ids.
This repo is not on the default: its own `.unattended.conf:311` names `CLAUDE_CODE_SESSION_ID`. The
finding does not reach this tree's own runs, and it does reach every adopter that has not set the key.

**Impact.** The route is round 2's first reachability route: a mid-run `extract --discover`, then the
close render. On that route S1 and S4 do fix the model, because the live transcript wins. The
independent check is still absent, so a regression in S4 goes uncaught. That is the guard-shares-a-variable
shape §4 ¶1 says this unit removes. S5's sentence "When no transcript is local, S3 has already withheld
every value the refusal guards" is scoped to named sessions too (M3).

**Fix.** Have the model record every session id it read, discovered ones included, beside
`coverage.transcripts`. Make S5 re-read every such session whose transcript is local. Add an AC5 variant
with no session named in the journal.

**Left-shift.** Add that AC5 variant, staged RED. In the arm, assert that the set of independently read
turns is non-empty. Then a refusal that read nothing cannot pass as a refusal that found nothing, which
is charter §7's rule that a probe unable to move says so.

### M1 — MEDIUM — unit 15 §6 AC2 — raw 18, and the first clause of raw 4

**Defect.** AC2 reds when "the anomaly or the window end carries the unclean END's time". Without the
fix, a non-terminal end is already `float(latest) + 1.0` (`model.py:422`). When the unclean END is the
last event, the rendered end is one second after it and never its own time. The window-end half of the
red therefore cannot fire against the code S3 exists to fix. Only the anomaly half can red: that
anomaly takes the END's time today (`model.py:1136`). AC2 also drops S3's "non-terminal" qualifier.

**Fix.** State AC2 against S3's rule. In a non-terminal fixture, the rendered end equals the last event
that is not held, plus 1.0 s, and `end_from` names that event. Red when the end lies within
`OWNER_ACT_BAND_S` of the unclean END.

**Left-shift.** At build, stage each AC's red against unchanged code before writing the fix. Make the
arm assert equality with the exact expected value, not inequality with one value. As a spec-audit
check: for each "Red when: X carries Y" clause, ask whether unchanged code already fails to produce Y.

### M2 — MEDIUM — unit 15 §2 S3, against unit 8 §2 S2 — raw 41

**Defect.** S3 changes a ratified window rule and does not say which window it changes. `record.py`
renders the model's own window end (`build_summary_facts` reads `w.get("end")`), so the code has no
separate rendered end. Unit 8 S2 lists the sources that never move a non-terminal end ("Three sources
never move it", its spec line 65). It bounds every derived set by one predicate, `check_in_window`.
Commit `f82ce189` recorded a Decided line keeping that single predicate rather than admitting a terminal
END.

**Impact.** Each reading does harm that no AC observes.

- If the model's window moves, the unclean END and a killed bar's NONE gate line leave every bounded
  set: timeline, gates and `journal_lines`. An interrupt more than a second after the last remaining
  event then classes as `post-close` under unit 8 S9 (its spec line 245).
- If only the rendered value moves, the record has two window ends, and the commitment still carries
  the held time (H1).

**Fix.** State whether `derive_window` and `check_in_window` move. Amend unit 8 S2's list of excluded
sources with a rev line. Add AC2 clauses for the S9 owner position and for the commitment's `last` when
the unclean END is the last journal line.

**Left-shift.** Add an arm that places an interrupt turn after a killed verb's END and asserts its S9
position under the rule chosen.

### M3 — MEDIUM — unit 14 §2 S3 against S4, §6 AC3 — raw 21

**Defect.** S3 gates idle judgement and the transcript facts on "every named session's source". S4
defines the discovered path as the case where "no journal names one". On that path no session is named,
so S3's condition is vacuously true. AC3 checks only that the state reads `partial`.

**Impact.** Implemented literally, a stale discovered extract still has its idle gaps judged and its
counts rendered, because `partial` is in `COUNTED_STATES`. That is the R2-B1 leak on the heuristic path.
Reaching it needs a render with no local transcript, for example one made after the transcript left the
machine, because S1 reads a local transcript first. That narrower reach is why this is MEDIUM.

**Fix.** Quantify S3 over every session the model reads, named or discovered. Extend AC3: with a stale
discovered extract and no transcript, idle gaps read not judged and the three facts render `-`.

**Left-shift.** Add that AC3 extension as an arm, staged RED against a literal implementation over
`sids`.

### M4 — MEDIUM — unit 14 §2 S4, §4 ¶2 — raw 35

**Defect.** The discovered branch of `resolve_run_sessions` (`model.py:699-708`) takes every store
extract whose `slugs` names the build, with no window filter. The sessions of the build's earlier runs
come in with it. S4 applies S2's per-session freshness test to all of them.

**Impact.** Once an earlier run's transcript is purged, its extract can never be refreshed, and its
`extracted_at` falls before every later run's window end. Every later discovered-path run of that build
then reads `partial` and withholds all its transcript facts permanently. Where those transcripts are
still local, S1 re-extracts every past session of the build on every render. §4's cost claim, that "a
render reads only the run's named sessions", is false on this path, which is the default one (H5).

**Fix.** In S4, keep only the discovered sessions whose events intersect the run's window before S1 and
S2 apply. Add an AC3 arm with an old, stale, out-of-window session of the same slug.

**Left-shift.** Add that arm, and have the coverage block report how many sessions the render read, so a
render that reads a build's whole history shows the count.

## Classes across the set

- **The population is narrower than the leak.** H1, H2, H3, H5 and M3 each apply a correct rule to fewer
  sessions, lines or slots than the leak runs through. This is the third appearance of the class, after
  closing round 1's B1 and R2-H1. Unit 15 §4 offers its class gate as the stop, and H3 shows the gate
  inherits the narrowing. A fix that derives its population from the schema's `utc` shape, rather than
  from a named list, is what this class keeps asking for.
- **A check that cannot fail on the shape it exists for.** H4's backstop compares seconds against a
  minutes-wide leak, and M1's red names a value unchanged code never produces. Both are charter §7's
  could-not-fail shape, one level up from code.
- **A change to a rule another unit pins, with no Edge naming it.** B1 changes unit 9's count rule, and
  M2 changes unit 8's window rule. Each spec already carries an Edge to that unit for another reason, and
  that Edge made the missing one easy to overlook.

## Disposition

The rule is `memory/guides/BUILD-METHOD.md` and the unattended Skill's BOUNDED state, not this record's
choice. At a one-round bound, this subject exits BOUNDED, and every confirmed finding is disposed by
severity. B1 and H1 to H5 are promoted to units whose mechanisms close them, and the round records
`--disposition promote`. M1 to M4 fold into their specs as rev-2 bumps with §9 lines. The promoted specs
are then audited by a fresh harness invocation, never by this round.

Two groupings may save the promotion a round. H1, H2 and H3 share one fix, the schema-wide `utc`
population, and could be closed by one mechanism. H4 and H5 both sit in S5. M2's window decision should
be made with H2's fix and not apart from it.

## Synthesis observations, outside the tally

- Both specs state `base 4cf0944d`. That commit is the merge-base with `origin/main` and the second
  parent of reconcile merge `de64de53`, and `git ls-tree 4cf0944d tools/runlog` is empty. None of the
  code the specs cite exists at their stated base, so a reader resolving a line at that base finds no
  file. No skeptic saw this, and it is not counted. The fold may want to restate the base.

## What this synthesis re-derived

- Both subject blobs equal `git rev-parse HEAD:<path>` at `a6f9d52e`.
- `git diff --stat 37d4b899 HEAD -- tools .githooks` is empty.
- B1: `COUNTED_STATES` at `record.py:109`. The AC10 arm at `selftest.py:4689-4723` asserts integers
  under `partial` with a second named session. Unit 9's spec line 85 reads "neither `present` nor
  `partial`". Line 73 of the Skill template opens the "No local transcript" paragraph on `not-local`.
- H1 and M2: `measure_commitment` at `record.py:936-972`, and `check_commitment` comparing all four
  fields at `:1035-1036`. `render_record` defaults to `commitment=None` at `:878`, and the write path
  passes one at `:921`. `journal_lines` is at `model.py:1718-1719`.
- H2 and M1: `derive_window`'s `+ 1.0` at `model.py:420-422`. `tree_ts` takes gate lines of every
  verdict at `:1450-1453`, and `last_event` is at `:1459`. `killed-verb` takes `e["end"]` at `:1136`.
- H3: the schema's UTC slots are the `window`, `commitment` and `elided` fact templates, 13 Timeline row
  kinds, and the `utc` columns of the `rounds`, `anomalies` and `sources` tables.
- H4: the second and next-second comparisons at `record.py:830-875`. `IDLE_OWNER_GUARD_S` equals
  `IDLE_GAP_S`, 900, at `model.py:92` and `:98`. Round 2's "within two minutes after" measurement.
- H5 and M4: `sessions=sids` at `model.py:1703`, the discovered branch with no window filter at
  `:699-708`, and the blank default at `unattended.sh:343`. This repo's `.unattended.conf:311` sets the
  key. Round 2's record gives the `extract --discover` route at its lines 177-180.
- M2: unit 8's spec line 65 ("Three sources never move it") and line 245 (`post-close`), and the Decided
  line of `f82ce189`.

One claim comes from verification and was not re-derived: that round 2's recorded fix for R2-M2 keys
its marker on `COUNTED_STATES`.

## What this pass did not cover

- The 35 refuted findings are not reproduced or characterized here.
- No code exists for units 14 and 15. The specs were audited against the tools at `a6f9d52e`.
- Unit 15's F1 band of 180 s was not re-measured. The 142 s latency it rests on is round 2's figure.
- How units 14 and 15 interact once both are built was examined only where H4 and H5 touch it. Unit 15
  consumes unit 14's turns.
- No gate was run over the specs. This record is not yet bound into the build index. The two specs'
  `gen:spec-records` regions and the README's records line need re-rendering in the commit that lands
  it.
