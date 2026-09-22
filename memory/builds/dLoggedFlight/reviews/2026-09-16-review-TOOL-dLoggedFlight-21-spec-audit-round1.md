**Serves:** spec-audit TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24

# dLoggedFlight — spec audit of units 21 to 24, round 1

*Node `d`, 2026-09-16, on `branch/unattended-build-transparency-ea83a5` at HEAD `e89add11`. The
subjects are the four units the previous spec audit promoted at its BOUNDED exit: unit 21 at rev-2, from
that audit's B1; unit 24 at rev-1, from its H3 with its M1 folded in; unit 22 at rev-2, from its B2; and
unit 23 at rev-1, from its H1 and H2. This is ROUND 1 of this subject set, and `.unattended.conf`
declares a bound of one round (`REVIEW_ROUNDS="1"`). The pass was Tier-2 and adversarial: four primed
finder lenses, then a skeptic stage of five batches prompted to REFUTE each finding, then one synthesis,
which is this record. The previous spec audit is
[its record](2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md). The labels B1, H1 and so on
are this record's own, and a label that record used is cited with its record named. Code lines are cited
at `ba3bd9fd`, the read point all four specs declare, so a fix can amend a spec's citations in the spec's
own frame. Unit 16's build commit `e89add11` has since moved `selftest.py`, `model.py`, the kit README
and the map dossier, and left `record.py` unchanged. "What this synthesis re-derived" gives the HEAD
line for each citation a fix edits. The severities are this synthesis's adjudication, not the finders'
grades.*

**Reviewed subjects, each pinned at the blob it was read at — ROUND 1:** `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-21.md@d3b58d330d29a8078cffd504066fca5a1fa5d264`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-24.md@a65857d61dfeb63ee8539b88871d88ad170e790d`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-22.md@2d2fbcbe37faff00893ab79bf1d12634cf5fb8c7`, `memory/builds/dLoggedFlight/spec/2026-09-16-spec-TOOL-dLoggedFlight-23.md@398f6c99bd669f50060c164850dfe56b2a2f4de6`.

## Verdict: BLOCKED

One blocker stands, and it spans units 22 and 24.

- **B1.** The `opened-by` and `closed-by` vocabularies are observed today by one per-value loop that
  edits the model's `window`. Unit 24 renders both facts from `record_window` instead, so that loop's
  edit stops reaching the render and its `last-activity` check reds. Neither unit names the loop. Unit 22
  then makes its derived vocabulary list include both vocabularies, and one render carries one closer.
  Unit 22 AC4's "on the real schema it passes" and unit 24 AC3's two remaining closers cannot both be
  met by any arm the two specs authorize.

Four highs stand beside it. H1 and H2 show that unit 22's inventory, which its §4 calls the complete one
B2 asked for, misses assertions whose counts and values the retirement changes, and that its AC1 count
cannot hold on the fixture its own S5 describes. H3 shows that every record the unattended Skill commits
takes `record_window`'s `last-activity` branch, which no criterion of unit 24 observes, and that for a
LANDED or ABORTED record the committed window is not the one a re-render or the leg derives. H4 shows
unit 22's new `withheld rows` fact renders `0` for a source nobody read, which unit 9 S4 at rev-7
already ruled out.

Unit 21 drew no item. The owner's source rule is not challenged by any finding. What fails, for the third
consecutive spec audit, is the inventory of what reads the things a unit retires or re-routes, now
together with the reach of the staged REDs meant to back it. Every item has a fix the specs can state
without a new mechanism, and the verdict is BLOCKED because of B1 alone.

The tally is 1 BLOCKER, 4 HIGH, 6 MEDIUM and 1 LOW, over 12 items folded from 21 confirmed findings.
Unit 22 carries B1 in part and H1, H2, H4, M1, M2, M5, M6 and L1. Unit 24 carries B1 in part and H3.
Unit 23 carries M3 and M4. M5's fix lands in unit 20, which is outside this subject set. Precision was
0.50; see "Review shape".

## Run integrity

- Lenses: **4 of 4** returned, **0 died**.
- Skeptic batches: **5 of 5** returned, **0 died**.
- Verdicts: **0** contradictory ones demoted to unverified, **0** spurious ones discarded, **0**
  duplicates.
- Unverified findings: **0**.

Every stage returned, so for this lens set the run is complete. A zero below comes from the lens set
itself, not from an agent that died. Even so, a zero is not evidence of absence. Unit 21 drew no item, and
the 21 refuted reports were not handed to this synthesis, so this record cannot say which surfaces they
covered or how closely unit 21 was examined.

## Review shape

- Raw findings **42**, confirmed **21**, refuted **21**, unverified **0**, precision **0.50**.
- Precision sits at the ~0.5 floor `AGENTS.md` §8 sets, not below it. It rose from 0.27 and then 0.35 in
  the previous two spec audits. This synthesis did not see the refuted set, so it cannot say which lens
  produced the refutations.
- Adjudicated here: **1 BLOCKER, 4 HIGH, 6 MEDIUM, 1 LOW**, over 12 items. Counted by raw finding, the
  split is 4, 7, 9 and 1.
- Six folds take 15 raw findings into 6 items: B1 (23, 16, 25, 38), H1 (15, 27, 37), H3 (24, 1), M1 (6,
  31), M2 (7, 42) and M3 (11, 12). H2 (26), H4 (35), M4 (29), M5 (17), M6 (41) and L1 (10) are one finding
  each. The pipeline counted 0 duplicates because it counts byte-identical reports only, so this merging
  is the synthesis's decision. Finding 15's third point, the `closed-by` members in the derived list, is
  carried by B1 rather than H1.
- Raised by fold: 16 and 25 were filed high and 38 was filed medium, and each takes B1's BLOCKER. 42 was
  filed low and takes M2's MEDIUM. No finding was lowered.
- B1 is held at BLOCKER on the ground both previous spec audits used: two written criteria that cannot
  both pass, here unit 22 AC4 and unit 24 AC3, with the arm that would reconcile them owned by neither
  unit. H1 and H2 are held at HIGH, not BLOCKER. Each is an omission or a mis-stated figure a builder can
  repair without breaking another written criterion, and the suite that exposes it runs at VERIFYING.
  They are still the class the previous B2 was raised for, recurring in the unit written to close it,
  which is why M6 matters.

## Findings

| Label | Severity | Unit | Address | Raw | Defect |
|---|---|---|---|---|---|
| B1 | BLOCKER | 22, 24 | 22 §2 S5, §6 AC4; 24 §2 S3, §6 AC3 | 23, 16, 25, 38 | the provenance vocabularies lose the only arm that reaches both closers, and the derived list requires both |
| H1 | HIGH | 22 | §2 S5 table, §4, §10, §6 AC5 | 15, 27, 37 | the inventory reads retired names, and misses assertions on counts and values retired rows carry |
| H2 | HIGH | 22 | §6 AC1, §2 S5 `build_class_model` row | 26 | AC1's count of 1 per retired kind cannot hold on a base model that already holds those kinds |
| H3 | HIGH | 24 | §2 S2 and S4, §4, §6 AC1 to AC3 | 24, 1 | every committed record closes by `last-activity`, which no criterion observes |
| H4 | HIGH | 22 | §2 S1, §5 error and empty states | 35 | `withheld rows` renders `0` for a source the model never read |
| M1 | MEDIUM | 22 | §6 AC3 | 6, 31 | the grep cannot fail on two of its named targets, and reds on stale bytecode |
| M2 | MEDIUM | 22 | §2 S3 and S4, §4 Files touched, §5 user docs | 7, 42 | README and module prose describing retired classes, a rule and a copied list is left standing |
| M3 | MEDIUM | 23 | §2 S1 and S3, §6 AC1 and AC3 | 11, 12 | no staged RED reaches the slot derivation or two of the three sentinel encodings |
| M4 | MEDIUM | 23 | §2 S2, §6 AC1 | 29 | the pre-check admits sentinels whose difference is a public duration |
| M5 | MEDIUM | 22, 20 | 22 §2 S1 and S4; 20 §2 S7, §6 AC5 | 17 | the layout removal refuses unit 20 AC5's fixture before the source rule can |
| M6 | MEDIUM | 22 | §3 Non-goals, last bullet | 41 | the reader-inventory gate is handed to the owner with no parked entry |
| L1 | LOW | 22 | §6 AC4 and AC1, §2 S5, §4 | 10 | the derived `shaped` list's liveness is claimed and never staged |

### B1 — BLOCKER — unit 22 §2 S5 and §6 AC4; unit 24 §2 S3 and §6 AC3 — raw 23, 16, 25, 38

**Defect.** `window opened by` and `window closed by` are Summary facts, so a record carries one value
of each. Their vocabularies are observed today by one loop in `test_record_ac4_classes`
(`tools/runlog/selftest.py:4309-4313`). It re-renders `dict(m, window=dict(m["window"], ...))` and asserts
that `git`, `terminal-write` and `last-activity` each reach the file. The typed vocabulary lists at
`:4297-4300` and `:4837-4842` leave `opened-by` and `closed-by` out on purpose. Each spec breaks one half:

- Unit 24 S3 renders both facts from `record_window`. `dict(m, window=...)` carries `record_window` over
  unchanged, so the loop's edit no longer reaches the render. The class model comes from the landed
  fixture, whose LANDED write is committed, so its `record_window` closes by `terminal-write` and the
  `last-activity` check reds. Unit 24 names no arm edit. Neither name it retires, `driver` or
  `terminal-end`, appears in the loop, so the build brief's grep for retired names does not find it.
- Unit 22 S5 replaces both typed lists with all of `RECORD_SCHEMA["vocab"]`, which adds `opened-by` and
  `closed-by`, and AC4 reds when the lists are typed. `test_schema_ac1_render_then_grade` grades one
  record and has no per-value loop, and a single record carries a single `window closed by` value. Unit
  22's S5 row for `test_record_ac4_classes` names the typed lists and the shaped map, not the loop.

**Impact.** Once unit 24 narrows `closed-by` to `terminal-write` and `last-activity` (its AC3 reds if
`terminal-end` stays), no arm the specs authorize observes both members. Unit 22 AC4's "on the real
schema it passes" then needs either a typed exclusion, which AC4's Red-when forbids, or more renders,
which S5 does not specify. The `runlog selftest` gate both units name reds on an arm neither unit owns.
Units run no suite before VERIFYING, so nothing catches this during the build. This is the pair of
criteria that cannot both pass that the previous audit held at BLOCKER as its B2.

**Fix.** One decision, written in unit 24, because unit 22 consumes from it (orders 22, then 23):

1. Unit 24 gains a scope item, observed by AC3, that retires the `dict(m, window=...)` loop. It observes
   the two vocabularies by rendering real models built through `build_run_model`: the landed fixture,
   which closes by `terminal-write`, and the same fixture left non-terminal, which closes by
   `last-activity`, each asserting `window opened by: git`. Count the change in the floor raise.
2. Unit 22 S5 states how its derived list reaches a vocabulary only a fact carries: either the union of
   cells over the renders item 1 names, or a derived list that skips fact-only vocabularies and names
   unit 24's arm as their observer. Add the loop to S5's table. Add a hands-off Edge between units 22 and
   24 on `test_record_ac4_classes`, which both now edit.

**Left-shift.** A re-render arm asserts that its mutation moved the render where it should reach, before
it asserts a value. Put that in a shared helper, and any arm whose mutation stops reaching the render reds
by itself, whatever renamed the field it edits. Per charter §7, run the helper over every `dict(m, ...)`
re-render in `selftest.py` before wiring it, and print which copies move the render and which do not.

### H1 — HIGH — unit 22 §2 S5 table, §4, §10 and §6 AC5 — raw 15, 27, 37

**Defect.** §4 calls S5's table "the inventory B2 asked for". §10 says a probe built it by listing each
arm that reads a retired row kind, the refusal, the commitment or a typed vocabulary: a probe by NAME. It
cannot see an assertion on a COUNT or a VALUE that a retired row carries, and five such assertions red
after the build with every row of the table edited as written:

1. `- values withheld: 4` (`selftest.py:4318-4319`). Two of the four intruders ride retired rows: the
   `command` on a `verb` row (`:4252`) and the `free text` on a `workflow` label (`:4255`). S1 drops
   retired events before rows are built, so the count becomes 2.
2. The vocabulary-short liveness block (`:4323-4332`) indexes `sch["vocab"]["push-decision"]`, which S4
   deletes, so it raises `KeyError`. Its `- values withheld: 5` falls with the intruders.
3. The shaped-value map (`:4302-4305`) takes its `utc` value, minute 12, from the appended `push` rows
   only (`:4233-4235`), and its `sha` value, `a` twelve times, from the `gate` rows' head only
   (`:4238-4239`). S5's row changes only the `duration` value.
4. `test_schema_ac1_render_then_grade`'s `- values withheld: 5` (`:4850`) becomes 3. S5's row moves that
   arm's UUID carrier to a ledger `ref` and does not restate the count.
5. `test_record_ac6_cap`'s widest-record assertion, `505 · shown` (`:4417`), counts the five wide
   `workflow` rows `build_big_model` adds (`:4349-4351`). S5's row keeps the `500 · shown 60 · elided 440`
   fact and does not mention this one.

**Impact.** Unit 22 rev-2's AC5 reads the floor comment and the file's definitions, and the suite that
grades the arms is its `New arm:` line. That suite reds or raises on each assertion above, and AC5's
Red-when, "an arm still reads a retired row, column, vocabulary or function", names none of them, since
several read a count rather than a retired name. The unit written to close B2's class reproduces it.

**Fix.** Add a row to S5's table for each of the five, with its replacement:

- Move the `command` and `free text` intruders onto kept carriers the renderer reads, such as a
  `dispatch` unit cell, a ledger `ref` or a kept `commit` row's cell, or restate each withheld count with
  its reason.
- Retarget the liveness block to a kept vocabulary a table carries, such as `anomaly-kind` or
  `review-exit`.
- Take the shaped map's `utc` and `sha` values from kept rows, such as a `commit` row's time and sha.
- Restate `test_schema_ac1`'s withheld count, and replace `505` with the widest model's kept-row count.

List the five in AC5's Red-when as assertions to re-read.

**Left-shift.** Derive those literals from the fixture instead of typing them: `values withheld` equals
the number of intruders the builder placed on read fields, counted where it places them, and the widest
`events` total equals the kept rows the builder made. A retirement that moves a carrier then moves the
expectation with it. For the spec audit, add a documented check: a retirement's inventory probe
simulates the retirement on each shared builder, by filtering the retired kinds and re-rendering, and
diffs every literal an arm asserts. That is the probe finding 27's skeptic ran.

### H2 — HIGH — unit 22 §6 AC1, against the §2 S5 `build_class_model` row — raw 26

**Defect.** `build_class_model` starts from the landed fixture's real model (`selftest.py:4225-4228`).
That model's timeline already holds the fixture's six driver verbs, from `--preflight` to `--landed`
(`:2189-2194`), its gate lines and its landing push. S5's row says the builder "appends the kept kinds,
plus one event of each retired kind", which leaves those base events in place. AC1 requires the
`withheld rows` fact to read "a count of 1 for each member of `RETIRED_EVENTS`". AC1 states the number
with no `figure:` sub-field, which `memory/TEMPLATE-SPEC.md:101-105` requires of a stated figure.

**Impact.** The skeptic probed the real landed model and found verb 6, gate 2 and push 1 before
anything is appended. Built as S5 says, `verb`, `gate` and `push` read more than 1, so AC1 cannot pass.
A builder who strips the base events instead changes the other readers of `build_class_model`, which are
`test_record_ac4_classes` (`:4293`) and `build_schema_fixture` (`:4760`).

**Fix.** Either have AC1 derive each expected count as the base model's count of that kind plus one,
read from the model at observation time and marked `figure: DERIVED`, or have S5's row drop retired kinds
from the base timeline before appending and name the two other readers that change. H4 changes what the
fact renders for an unread source, so write this count after H4's rule.

**Left-shift.** The spec-token checker that refused unit 22 rev-1's suite-run AC5 can also red an AC
that states a count over a fixture built from a real model and carries no `figure:` sub-field. Run it
over the tree's specs first, since "a count" is a prose judgement and the predicate may red innocent
criteria.

### H3 — HIGH — unit 24 §2 S2 and S4, §4, §6 AC1 to AC3 — raw 24, 1

**Defect.** `record_window` is built from committed record commits (`derive_record_commits`,
`tools/runlog/model.py:1372`), while `terminal` is read from the working-tree `RUN.md`
(`model.py:1348-1354`). The unattended Skill renders the record before it commits the run-state write the
verb just staged, at all three placements (`tools/unattended/SKILL.template.md:838-846`): "Render,
re-index and stage before you commit it". So every committed record takes `derive_window`'s else branch
(`model.py:414-422`):

- The `--close` placement renders at LANDING, which is in `PHASES_CLOSED` but not `PHASES_TERMINAL`
  (`model.py:77-80`), so the record closes by `last-activity`.
- The `--landed` and `--abort` placements render with `terminal` true and no terminal write yet
  committed. The committed record reads `terminal: yes` beside `window closed by: last-activity`, and
  its closing bound is the last record commit before the terminal write. After that commit lands, the
  schema leg and any re-render find the terminal write and derive `terminal-write`. No later placement
  re-renders.

Every AC that reads the rendered bounds uses the landed fixture with its LANDED write committed (AC1:
"whose HEAD holds every record commit"). AC3's non-terminal half reads only the provenance fact, and AC4
has no window. So S2's `last-activity` branch, the closing time as `end` less one second, and S4's
non-terminal clause are marked "Observed by" and never observed.

**Impact.** Two consequences. First, a build that renders the half-open `end` passes every AC, putting a
commit time plus one second in the Summary, which is the value §4 rejects as no public time. Second, for
the record the process commits at LANDED or ABORTED, S4's "a re-render reproduces them" and §4's "the
render and the leg now read one derivation" are false. The committed window, duration and closer
disagree with the leg's window for the same run, permanently.

**Fix.** Add a scope item and ACs over two fixtures built through `build_run_model`, not by editing
fields: the landed fixture stopped at LANDING, and the landed fixture with its LANDED write staged but
not committed. On each, the rendered closing bound equals the last record commit's committer time,
`duration` equals that less the start, and a later commit naming no unit leaves both byte-identical.
Stage RED with a renderer copy that prints the half-open `end`. Then decide the staged-terminal case in S4
and §5 risks: either render the closing bound and `window closed by` as `-` while `terminal` is true and
no terminal write is committed, or state the one-commit lag and drop the two claims above.

**Left-shift.** An arm that replays the Skill's placement order on the landed fixture: stage the phase
write, render, commit, re-render, and assert the committed render equals the re-render except where a
declared lag says otherwise. That gates the class "a render reads committed history that the commit it
rides has not yet made", which every git-derived slot inherits.

### H4 — HIGH — unit 22 §2 S1 and §5 error and empty states — raw 35

**Defect.** S1's `withheld rows` fact renders each retired kind "followed by its count", and §5 says a
run with no retired events renders "every count `0`", with no condition on whether the kind's source was
read. Unit 9 S4 at rev-7 folded M6 of the first closing diff review and ruled that "An UNKNOWN value is
absent too, never the value that reads clean" (unit 9 spec line 83). The renderer implements that ruling
for the transcript counts through `COUNTED_STATES` (`record.py:109`, the comment at `:627-632`), and
Coverage's `idle gaps` fact renders `-` when gaps were not judged (`record.py:279-281`). The kit README
states it as a paragraph of its own (`tools/runlog/README.md:302-306`). The retired kinds come from
sources whose coverage can read unknown. `compact`, `limit` and `workflow` enter only from transcript
extracts (`model.py:1579-1586`). `idle` exists only when the transcripts read `present` (`:1598`). `gate`
and `push` come from their journals, and `verb` from the driver journal. Unit 22 names neither the
ruling nor `COUNTED_STATES`, and no AC observes an unread source.

**Impact.** Built as written, a run whose transcripts read `not-local` commits `0` for `compact`,
`limit`, `workflow` and `idle`. A dead or absent gates or pushes journal commits `gate 0` and `push 0`.
Each reads as a clean run in a public record, which §5 itself frames as "what happened per kind". That is
M6's defect, reintroduced by a new fact.

**Fix.** In S1, render each kind's count as `-` unless its source reads a state in `COUNTED_STATES`:

- the transcripts for `compact`, `limit` and `workflow`;
- the driver journal for `verb`;
- the gates journal for `gate`;
- the pushes journal for `push` and `push-refused`.

Render `idle` as `-` when idle gaps were not judged. Replace §5's "every count `0`" with that rule. Add an
AC over a model with transcripts `not-local` and a `dead` gates journal, red when a `0` renders for a
kind whose source was not read. Cite unit 9 S4 rev-7, and add an Edge to unit 16, which owns
`COUNTED_STATES`' current use.

**Left-shift.** Stop restating the rule per fact. Let `RECORD_SCHEMA` declare, for every count a fact
renders, the source it is counted from. One arm then renders a model with every source outside
`COUNTED_STATES` and reds on any declared count that renders a digit, and a new count fact with no
declared source reds by that fact. Dry-run it over today's facts before wiring.

### M1 — MEDIUM — unit 22 §6 AC3 — raw 6, 31

**Defect.** Two separate faults in one grep.

- AC3 greps for `scan_owner_times`, `UTC_TOKEN_RE` and `TWIN_ROW_RE`. Two of the prose locations S3
  retires name none of them: the dossier bullet (`memory/map/features/runlog.md:217-220`) and the module
  docstring clause "outside every owner turn's second" (`record.py:47-48`). The README paragraph
  (`tools/runlog/README.md:285-291`) names one of them once, at `:289`. AC3 lists the dossier as a grep
  path, and on it the grep cannot fail.
- `grep -rn` over `tools/runlog` recurses into the gitignored `tools/runlog/__pycache__`. Run today, it
  prints `Binary file ... matches` for `record.cpython-312.pyc`, `record.cpython-314.pyc` and
  `selftest.cpython-312.pyc`. The suite recompiles under one interpreter, so the other version's stale
  bytecode keeps matching after a correct build.

**Impact.** The refusal's prose can survive in the dossier, the docstring and most of the README
paragraph while AC3 passes. On this node, AC3 also reds on a correct source tree. Either way AC3's
verdict does not depend on what it names.

**Fix.** Observe with `git grep -n -e scan_owner_times -e UTC_TOKEN_RE -e TWIN_ROW_RE -e "owner turn's
second" -- tools/runlog memory/map/features/runlog.md`, red on any hit. This synthesis dry-ran it at
HEAD: the phrase hits the dossier, the README paragraph, the docstring clause and the AC9 arm S5 retires,
and nothing else.

**Left-shift.** The spec-token checker can red a `grep -r` over a kit directory in an AC observation,
naming `git grep` as the replacement, because untracked bytecode makes the verdict depend on the node.
For the spec audit, the previous audit's L1 already asked that a retirement AC grep the mechanism's prose
as well as its identifiers. This is that check not binding a second time, so it belongs with M6's gate.

### M2 — MEDIUM — unit 22 §2 S3 and S4, §4 Files touched, §5 user docs — raw 7, 42

**Defect.** S3 lists only the refusal's prose for removal. Other passages describe what S1 and S4 retire,
and no S item or AC covers them:

- `tools/runlog/README.md:293-299` lists "a verb token", "a list of check numbers" and "a workflow label"
  among the shaped classes, and says the `label` class admits a lowercase UUID.
- `:305-306` says a Timeline `rc` is written only beside an END reading `exit=clean`, the rule
  `derive_clean_rc` implements and S1 retires.
- `:444-446` names "The pre-push hook's decisions" as a copied list, which retires with `PUSH_DECISIONS`.
- `record.py:89-93` says "THREE LISTS ANOTHER FILE OWNS", the push decisions among them. S4 rewrites the
  `forbidden` comment at `:291-296` and not this one.

This synthesis dry-ran a grep for the finders' phrases at HEAD and found two more passages, which are not
counted as findings: the dossier's sentence on "the record's copies of the pre-push hook's decisions"
(`memory/map/features/runlog.md:181` at HEAD), and the module docstring naming "a verb token" as a shaped
class (`record.py:7`). The same dry run showed that `workflow label` wraps across two README lines, so a
one-line grep for it cannot fail. §5 lists "user docs — the kit README's record section" with no S item
behind it.

**Impact.** After the build, the README, the dossier and two module comments describe classes, a rule
and a copied list that no longer exist, and nothing in the spec can fail on them. This is the class of the
previous audit's L1, and of the `amendment-leaves-its-other-half-standing` gotcha.

**Fix.** Extend S3 or S4 to name each of the six passages and its rewrite:

- The README's schema paragraph and the `record.py:7` docstring drop `verb`, `checks` and `label`, and
  the UUID sentence names the path class's file segment.
- The `rc` sentence retires with `derive_clean_rc`.
- The README residue bullet, the dossier sentence and the `record.py:89-93` comment drop the push
  decisions and count two lists.

Add an AC observed with `git grep -n -e "verb token" -e "check numbers" -e "THREE LISTS" -e "pre-push
hook's decisions" -e "Timeline .rc."` over the README, `record.py` and the dossier, red on any hit, with
no phrase that wraps.

**Left-shift.** Gate the pair instead of the prose: the README's schema paragraph points at
`RECORD_SCHEMA["shaped"]` instead of listing its classes, or a self-test arm compares the listed names to
the schema's keys through a glossary. Charter §6 already says a value stated beside the source that owns
it rots.

### M3 — MEDIUM — unit 23 §2 S1 and S3, §6 AC1 and AC3 — raw 11, 12

**Defect.** Two halves of unit 23's claims have no staged RED.

- **Slots.** S1 says the arm holds no typed slot list, and §1 says a new time-bearing slot joins the
  check without an edit. AC3 stages only fixture cuts, a removed review round and kept rows cut to
  `TIMELINE_EDGE`, against slots that exist today. A typed list holding those two slots passes both.
  AC4's schema copy changes `time_classes`, which exercises S5's class half, not the slot derivation.
- **Encodings.** S3's class-blind scan covers three encodings of each sentinel: ISO form, epoch integer
  and `HH:MM:SS`. Of AC1's three staged REDs, the journal-window `duration` is caught by the duration
  rule, and the commit row carrying a journal time is a `utc` token caught by the `utc` rule. Only the
  `run` count set to a sentinel epoch needs the class-blind scan, and only its integer encoding.

**Impact.** A typed slot list passes every AC. So does a class-blind scan that matches integers only.
§4 names a typed population as how the class escaped four times, and the scan exists for a time in a
class nobody declared, yet unit 23 carries no "Red when the list is typed" clause of the kind unit 22 AC4
carries.

**Fix.** AC3 adds a schema copy declaring one extra `utc` slot the fixture never fills, red when the copy
passes and naming that slot. It also reds when the arm's slot list is typed. AC1 adds two staged REDs, one
for `HH:MM:SS` and one for the ISO form. This synthesis corrects the finder's carriers here. No shaped
class of today's schema but `utc` admits a colon (`record.py:117-152`), so a sentinel placed in a path,
unit or `ref` value is withheld before it renders, and that staged RED could not fail. Stage each
encoding on a schema copy that widens one class, such as `label`, to admit it, and assert the encoding
reached the text before grading.

**Left-shift.** A documented spec-audit check: for each scope clause that enumerates alternatives
(slots, classes, encodings), count the staged REDs that exercise each alternative, and flag any with
none. In code, the liveness M4 proposes applies here too.

### M4 — MEDIUM — unit 23 §2 S2, against §6 AC1's first staged RED — raw 29

**Defect.** The renderer computes `duration` as end less start (`record.py:624`), so a renderer reading
the model's sentinel window writes a difference of two sentinels. S2's pre-check excludes each sentinel
from the public times, and from a public time plus a public difference plus zero or one second. It never
excludes a difference of two sentinels from the set of public differences, which S3's duration rule
accepts. Every public time in the landed fixture is a whole minute (`derive_minute`,
`selftest.py:1903`). The model window runs from the `--preflight` START at minute 1 to the `--landed` END
at minute 27 (`:2189-2194`). The git window runs from the start commit at minute 2 to the LANDED write at
minute 28 (`:2173-2186`). If every journal event carries the same second offset, `int(end - start)` is
1560 s, exactly the git duration.

**Impact.** AC1's first staged RED, a Summary `duration` read from the journal-bounded window, passes
under a fixture that satisfies S2 as written. The break unit 23 was promoted to catch, the previous
audit's H1, goes green.

**Fix.** Extend S2's pre-check: no difference of two sentinels, and no sentinel less a public time,
equals a non-negative difference of two public times. The arm asserts this before the staged REDs run.

**Left-shift.** Every staged RED asserts, before its verdict, that the broken copy's graded output lies
outside the set the rule accepts, here that the broken `duration` is not already a public difference. A
break the rule cannot see then reds as a dead probe instead of passing, which is charter §7's rule that a
probe that cannot move says so.

### M5 — MEDIUM — unit 22 §2 S1 and S4, against unit 20 §2 S7 and §6 AC5 — raw 17

**Defect.** S1 and S4 remove `verb` from the Timeline row layouts. `check_table_row` already refuses a
row whose event kind has no layout, under rule `cell`, and returns before its class checks
(`record.py:1141-1145`). Unit 20 AC5's fixture is "a verb row with a time", and its Red-when is only
"the record is accepted". Unit 22 is ordered 23 and unit 20 is ordered 24.

**Impact.** Once unit 22 lands, the `cell` refusal rejects AC5's fixture whether or not S7's source rule
exists, so AC5's staged break cannot red and the source rule goes unobserved. AC5's body names the
source rule, but neither the staged observation nor the Red-when tells the two refusals apart.

**Fix.** In unit 20 AC5, use a kept `commit` row whose `source` cell reads `driver`, a `SOURCE_NAMES`
member only the source rule refuses, and add "or the refusal names a rule other than the source rule" to
Red-when. Unit 20 is outside this subject set. Folding this there moves its rev, and by BUILD-METHOD M4
a spec whose rev moved by anything but its own review's fold is unreviewed again.

**Left-shift.** A Red-when for a refusal names the rule the refusal must name, never "is accepted" alone.
The spec-token checker can red that shape. For the spec audit, add a documented check: when a unit
removes a layout, vocabulary or class, grep every open spec's AC fixtures for the removed member.

### M6 — MEDIUM — unit 22 §3 Non-goals, last bullet — raw 41

**Defect.** The bullet hands the gate that would flag a spec retiring a name without naming its readers
to the owner, under M3's second veto. The spec audit of units 14 and 15 proposed it as a documented
check, and B2's left-shift in the audit of units 14, 16 and 20 raised it to a candidate gate because that
check did not bind. BUILD-METHOD M3 says a veto-2 outcome "COLLAPSES onto the park rule"
(`memory/guides/BUILD-METHOD.md:90-94`). The build README's Parked decisions reads "None yet."
(`memory/builds/dLoggedFlight/README.md:60-62`). RUN.md's Parked section holds no entry for it, and
`memory/backlog/TOOL.md` and `memory/DECISIONS.md` carry no row for it.

**Impact.** The class behind both blockers of the previous audit, and behind B1 and H1 here, has no home
in the open and parked list M9 builds for the owner. Charter §7 says a confirmed finding is not done until
a gate or a documented check covers its class.

**Fix.** Park the gate decision, not the finding: add an entry to the build README's Parked decisions
naming the predicate, the dry run over the tree that charter §7 requires, and the M3 veto-2 reason, or
file a backlog row in `memory/backlog/TOOL.md`. Cite that home in the §3 bullet as the fold's rev bump.

**Left-shift.** A hygiene check that a spec §3 or §8 passage handing a decision to the owner under an M3
veto has a matching Parked-decisions entry in its build. It is a change to `memory/HYGIENE.md`, a
governance carrier, so it is itself the owner's. Dry-run it before wiring, because the phrase is prose.

### L1 — LOW — unit 22 §6 AC4 and AC1, against §2 S5 and §4 — raw 10

**Defect.** S5's row for `test_record_ac4_classes` says both derived lists, `vocab` and `shaped`, red on a
member no render reaches. §4's rejected alternative rests on the `shaped` half redding on `verb`,
`checks` and `label`. AC4 stages only a `vocab` copy that keeps `push-decision`. The skeptic added a
reason the claim may be false: a derived shaped check would most naturally ask whether some cell
fullmatches the class regex, and `label` (`[a-z0-9-]{1,40}`) and `checks` (`[0-9]{1,3}(?:,[0-9]{1,3})*`)
fullmatch ordinary cells such as `git` or an ordinal, so such a check never reds on them. The finding's
second half, that AC1 observes only the count-1 fixture, is weak, since a fixed template cannot drop a
member, and H4 rewrites that fact anyway.

**Impact.** An arm that derives `shaped` but cannot red on an unreached class passes AC4, and §4's reason
for dropping three classes goes unverified.

**Fix.** Add to AC4 a schema copy whose `shaped` keeps `verb`, red naming `verb`. State in S5 that the
shaped liveness decides a class was reached by the slot that declares it, not by any cell fullmatching
its regex. H4's unknown-source AC covers the zero-count half.

**Left-shift.** Each derived list gets its own staged RED, one per list and not one per arm. This is
M3's documented check applied to unit 22.

## Classes across the set

- **An inventory by name misses readers by value.** B1, H1 and M5. Unit 22's table found every arm that
  names a retired thing, and missed a loop that edits a field unit 24 stops reading, five literals a
  retired row carries, and another spec's fixture that the removed layout refuses first. This is the
  third consecutive spec audit whose blocker is a retirement's reader inventory. M6 is why nothing
  structural has caught it yet.
- **A staged RED that cannot fail on the break it names.** M1, M3, M4, M5 and L1. Each AC names a break,
  but its fixture, its carrier or its predicate makes the break invisible to the rule, so the RED passes
  or reds for another reason. The first closing review's B1 and the previous audit's M2 and M3 were the
  same shape one level up.
- **A render reads committed history ahead of the commit it rides.** H3. It is new in this audit, and
  every git-derived slot inherits it.
- **An unknown count rendered as a clean zero.** H4, a regression of M6 of the first closing diff review
  in a fact written after it.
- **A retired mechanism's prose left standing.** M2, after the previous audit's L1.

## Disposition

The rule is `memory/guides/BUILD-METHOD.md` M4 and the unattended Skill's BOUNDED state, not this
record's choice. At a one-round bound this subject set exits BOUNDED, and every confirmed item is
disposed by severity. B1 and H1 to H4 are promoted to units whose mechanisms close them, audited as specs
by a fresh harness invocation, and the round records `--disposition promote`. M1 to M6 and L1 fold into
their specs as rev bumps with §9 lines. M5's fold lands in unit 20, and M6's fold parks the gate decision
while the finding itself is folded, not parked.

Two groupings may save the promotion a round:

- **B1 and H3 share `record_window`'s two closers.** One unit whose arm renders real models at each of
  the Skill's placements (terminal write committed, terminal write staged, LANDING) observes B1's
  vocabularies and H3's bounds together.
- **H1, H2 and L1 share `build_class_model` and the literals asserted over it.** One unit that derives
  those expectations from the fixture closes all three. H4 changes the `withheld rows` fact that H2
  counts, so H4's rule should be written before H2's expected values.

## Synthesis observations, outside the tally

- **The lenses read rev-1 of units 21 and 22.** The record is pinned at their rev-2 blobs, and each
  spec's own rev-2 line says it was made while this audit read rev-1. Unit 21's rev-2 changed citation
  spelling only. Unit 22's rev-2 moved AC5 from a suite run to reading the floor comment and the file's
  definitions, with the suite moved under `New arm:`. No confirmed item addresses the moved text.
  Findings 15 and 27 quote AC5's Red-when, which rev-2 kept word for word. Not counted.
- **Citations drift at HEAD.** All four specs cite `ba3bd9fd`, as they declare. At `e89add11`, unit 22
  S3's `tools/runlog/README.md:285-291` reads `:296-302`, and the dossier bullet sits one line lower. The
  working tree also holds an uncommitted `tools/runlog/model.py` edit from unit 14's build, dispatched at
  16:21Z, so HEAD lines will move again. Not counted.
- **This audit runs beside a build.** RUN.md at `9bca3722` records BUILDING for units 16, 14, 21, 24, 22,
  20 and 23 with this audit beside it. Unit 16 is committed at `e89add11` and unit 14 is dispatched.
  BUILD-METHOD M4 reviews every spec before its code. Units 24, 22 and 23 carry confirmed items, so
  dispatching them before this disposition lands builds specs this record found defective. Unit 21 drew no
  item. Not counted.

## What this synthesis re-derived

- All four subject blobs equal `git rev-parse HEAD:<path>` at `e89add11`.
- `git diff --stat ba3bd9fd e89add11 -- tools` touches `extract.py`, `model.py`, `selftest.py`, the kit
  README and `tools/unattended/SKILL.template.md`, and not `record.py`.
- B1: the loop at `selftest.py:4309-4313` (HEAD `:4329-4333`), the typed lists at `:4297-4300` and
  `:4837-4842` (HEAD `:4317-4320` and `:5021-5026`), `opened-by` and `closed-by` at `record.py:156-157`.
- H1: intruders at `selftest.py:4252` and `:4255` (HEAD `:4272`, `:4275`); `values withheld: 4` at
  `:4319` (HEAD `:4339`); the liveness block at `:4325-4332` (HEAD `:4345-4352`); the shaped map at
  `:4302` (HEAD `:4322`); push and gate rows at `:4233-4239` (HEAD `:4253-4259`); `values withheld: 5` at
  `:4850` (HEAD `:5034`); `505 · shown` at `:4417` (HEAD `:4437`); wide workflow rows at `:4349-4351`
  (HEAD `:4369-4371`); `PUSH_DECISIONS` and `GATE_VERDICTS` at `record.py:95-100`.
- H2: `build_class_model` at `selftest.py:4221` (HEAD `:4241`), its callers at `:4293` and `:4760`, the
  landed fixture's driver lines at `:2189-2194`; the `figure:` writing rule at `TEMPLATE-SPEC.md:101-105`.
- H3: `terminal` at `model.py:1354` (HEAD `:1382`), `record_commits` at `:1372` (HEAD `:1400`),
  `derive_window` at `:402` (HEAD `:404`), the phase tuples at `:77-80` (HEAD `:79-82`); the three
  placements at `SKILL.template.md:838-846` (HEAD `:840-848`).
- H4: `COUNTED_STATES` at `record.py:109`, the unknown-count comment at `:627-632`, `idle gaps` at
  `:279-281`; the transcript-only kinds at `model.py:1579-1586` and `idle` judged at `:1598`; unit 9 spec
  line 83 and its rev-7 line at 322; the README's unknown-value paragraph at `:302-306` at `ba3bd9fd`.
- M1: the grep reproduced today, printing three `Binary file` lines; the proposed `git grep` dry-run at
  HEAD.
- M2: README `:293-299`, `:305-306` and `:444-446` at `ba3bd9fd`; `record.py:7` and `:89-93`; the
  dossier's `:181` and the wrapped `workflow label`, both from a dry run at HEAD.
- M3: the class regexes at `record.py:117-152`, none but `utc` admitting a colon.
- M4: `dur` at `record.py:624`; the fixture's commit minutes at `selftest.py:2173-2186` and driver minutes
  at `:2189-2194`, re-derived from the source lines and not by running the fixture.
- M5: `check_table_row`'s unknown-kind refusal at `record.py:1141-1145`; unit 20's S7 and AC5 text and
  its order 24.
- M6: the M3 collapse sentence at `BUILD-METHOD.md:90`; the README's "None yet."; no row in the TOOL
  backlog or `DECISIONS.md`.

Three claims come from verification and were not re-derived here: that the landed model holds verb 6,
gate 2 and push 1 before `build_class_model` appends (H2); that a simulated retirement takes
`values withheld: 4` to 2 and removes the minute-12 `utc` and the twelve-`a` sha from the text (H1); and
that no RUN.md Parked entry names the reader-inventory gate beyond the section this synthesis read (M6).

## What this pass did not cover

- The 21 refuted findings are not reproduced or characterized here.
- No code exists for units 21 to 24. The specs were audited against the tools at `ba3bd9fd` and `e89add11`.
- Unit 21 drew no item, and that is not evidence it is sound (see "Run integrity").
- How units 21 to 24 interact with units 14, 16 and 20 once built was examined only where B1, H1, H4 and
  M5 touch it.
- The owner's source rule was taken as given.
- No gate was run over the specs or this record. This record is not yet bound into the build index. The
  four specs' `gen:spec-records` regions and the README's records line need re-rendering in the commit
  that lands it.
