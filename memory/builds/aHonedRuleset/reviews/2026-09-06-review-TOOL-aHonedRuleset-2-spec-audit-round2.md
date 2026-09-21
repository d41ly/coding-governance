**Serves:** spec-audit TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6

# aHonedRuleset — spec audit of units 2–6, round 2

*Node `a`, 2026-09-06. Four finder lenses read the rev-3/rev-4 fold text of the five specs, a
skeptic pass was run to REFUTE each candidate, and this is the consolidation. Every surviving claim
about source was re-run against the tree before it was kept. This round grades the SPECS, not the
tree; the one round-1 item re-checked here (`B1`, the build README) is repaired — `python
tools/memory-tree/gen_build_index.py --check` reports `clean (629 artifact(s))` at HEAD. The rest of
round 1 was not re-verified, so this verdict is scoped to the round-2 finding set.*

Subjects, pinned at the blob each was read at:

- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-2.md@0f1910d9ccedfaf35516d8f2d8a57430b8207457`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-3.md@aadd90c854b3ddad234b2c0a8dbb3aacd6167428`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-4.md@6415a907245826ab9a761f17e1f71c5312c8addd`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md@e1e297beaf8ae14592597db17853dda30db893b2`
- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-6.md@c9bcf3bec4af4fba034757052ea14f49f132a6ac`

## Verdict: CLEAN WITH FIXES

Eleven findings survived. None blocks a landing outright: every one of them is a spec edit, and no
unit is gated on an unsigned fork the way round 1 found. Three are HIGH, and all three share one
shape — **a criterion or a rationale that cannot observe the thing it exists to observe**. Two of
those (H1, H2) leave a unit's only dogfood of its own fix unobservable; the third (H3) is a gate this
build will actually trip if all six commits land without a second stamp key nobody in the set names.

Six MEDIUM findings and two LOW ones follow. Nine of the eleven are the same class in different
clothes: acceptance sets that grade a subset of their scope. That is this repo's own `gate the CLASS,
not the instance` rule inverted, and it is worth reading the eleven as one pattern rather than eleven
accidents.

---

## Review shape

Raw findings 29, confirmed 11, refuted 18, unverified 0. Precision 0.38.

Precision below ~0.5 is the charter's own signal to tighten scope and priming before adding agents
(§8). Four lenses over five prose specs produced a lot of style-grade noise that the skeptic pass
correctly killed; the finder brief for a round 3 should say plainly that a wording preference is not
a finding, and should hand the lenses the rev logs so they stop re-reporting resolved forks.

## Run integrity

- Lenses: **4 of 4 returned, 0 DIED.**
- Skeptic batches: **5 of 5 returned, 0 DIED.**
- Contradictory verdicts demoted to unverified: **0.** Spurious verdicts discarded: **0.**
  Duplicates: **0.**

No lens died, so the zero counts in this run are evidence rather than silence, and the "also checked
and clean" list at the bottom means what it says.

---

## Findings

| # | sev | unit | address | one line |
|---|---|---|---|---|
| H1 | HIGH | 5 | §6 AC8 | the criterion names a file its own pattern provably cannot match |
| H2 | HIGH | 5 | §4 "The parity row" | the rationale is false about the parity mechanism, and stands in for a missing constraint |
| H3 | HIGH | set-wide | §2 S8 and its four copies | the re-stamp names `last-audit` only; `last-body-change` appears nowhere in the build |
| M1 | MED | 3 | §2 S3 vs §6 AC4/AC5/AC14 | three carriers in scope, one observed |
| M2 | MED | 4 | §6 AC7 | absence-only criterion; the replacement sentence is never observed present |
| M3 | MED | 5 | §2, §4 vs §8 F1 and §6 AC2 | the ratified high-water bump is in no scope item and no files-touched row |
| M4 | MED | 4 | §2 S1 | the "only:" list omits two phrases the parity gate pins |
| M5 | MED | 4 | §7 vs §6 AC9 | five armed self-test legs, no criterion that runs them |
| M6 | MED | 5 | §10 | the reuse audit still says two PAIRS rows; rev-3 collapsed it to one |
| L1 | LOW | 4 | §4 "Files touched (estimate)" | margin arithmetic hangs off a fork branch that was closed |
| L2 | LOW | 4 | §2 S9, §8 F2 | a line pin on a backlog row, wrong at the spec's own base |

---

### H1 — unit 5 AC8 cannot reach the file it names

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md`, §6 AC8** (covering §2
S12).

AC8 lists `memory/guides/SESSION-KICKOFF.md` among its grep paths but carries only the two ABSTRACT
spellings `merge-base <remote>/<default> HEAD` and `merge-base <local-default> HEAD`. Verified at
base, that file's line 22 reads:

```
- Stamp rule: sha = `HEAD` on `main`, else `git merge-base origin/main HEAD`; datetime always advances.
```

The concretised spelling. Neither alternative can match it. §4's own inventory grep carried a third
alternative, `merge-base origin/main HEAD`, for precisely this carrier; AC8, added at rev-3, dropped
it while keeping the filename.

**Impact.** S12 — the re-instantiation of this repo's own manifest, and the unit's only dogfood of
the fix it ships — has no criterion that can fail. A commit B that rewrites both homes and leaves
line 22 still prescribing the merge-base passes AC8 (the pattern never matches), passes AC10
(`manifest-check.sh` grades the stamp, not the body prose), and passes everything else. The defect
the unit exists to remove stays live in the file the unit re-stamps twice. This is an error inside a
criterion, not a missing criterion.

**Fix.** Add the concretised alternative to AC8's pattern, as §4's inventory grep already spells it,
or give S12 a criterion of its own: assert the new rule text is present in
`memory/guides/SESSION-KICKOFF.md` and that `merge-base origin/main HEAD` is absent from it.

**Left-shift.** Give the spec lint an anti-vacuity arm for acceptance greps, the same shape
`check-playbook-parity.sh` already uses for PAIRS: run every AC-quoted grep at the spec's declared
base, and red when a path named in the criterion matches none of the pattern's alternatives. A
criterion that matches nothing at base and asserts nothing-after is a criterion that cannot fail, and
that is mechanically detectable.

### H2 — unit 5 §4 states a false fact about the parity mechanism, and that falsehood replaces a constraint

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md`, §4 "The parity row"**
(rev-3 fold text), plus a missing scope item in §2 S11.

§4 says of the new PAIRS row that "the loop already strips whitespace, so neither side's line
wrapping matters and `head -1` is not a problem". The loop, verified at
`tools/check-playbook-parity.sh:135-136`:

```sh
sval=$(eval "$sx" < "$sfile" 2>/dev/null | head -1 | tr -d '[:space:]')
oval=$(eval "$ox" < "$ofile" 2>/dev/null | head -1 | tr -d '[:space:]')
```

The extraction is a `sed` substitution applied per LINE, `head -1` then keeps ONE line, and `tr`
strips whitespace only inside that line. A value split across a wrap resolves to nothing and cannot
be rejoined. Sibling `TOOL-aHonedRuleset-4` S2 states the correct rule as scope — "each intact on a
single line, because the gate's extractions are sed substitutions applied line by line and a phrase
split across a wrap resolves to nothing". Unit 5 asserts the opposite.

**Impact.** S11 rewrites the exact line the new row extracts from. `MANIFEST-TEMPLATE.md:29-31` is
today a three-line wrapped bullet whose continuation at :30 already carries a second backticked `git
merge-base` expression, and no scope item or AC binds the rewritten sha expression to one physical
line or pins the anchor text the extraction keys on. If the rewrite wraps between anchor and value,
the anti-vacuity arm reds `playbook parity` in commit B — after AC4's RED has already been banked —
and the builder has to invent an anchor the spec never specified. The other failure is a
delimiter-only pattern: after commit B the compared value is the four-byte `HEAD`, and `head -1`
would happily take the first backticked token on any earlier line of a file dense with them.

**Fix.** Delete the "line wrapping matters" sentence. State the extraction pattern and the literal it
anchors on (e.g. keyed on `Stamp rule: sha = `). Add a scope item to S11 requiring the sha expression
and its anchor to stay on one physical line in both homes. Add an AC that runs the row's stated-side
extraction alone against `MANIFEST-TEMPLATE.md` and asserts a NON-EMPTY value equal to the expected
sha — the shape unit 4's AC2 already uses.

**Left-shift.** Two, and both are cheap. Give `check-playbook-parity.sh` a `--dry-run <pairs-file>`
mode so a candidate row can be exercised at spec time instead of at commit time. And add a gotcha row
keyed to diffs touching `tools/check-playbook-parity.sh` or any parity-pinned carrier: *extractions
are per-line and `head -1` cannot rejoin a wrap; pin the value to one physical line*. That makes
`python tools/memory-tree/gotchas.py --for-diff` print the rule to the next author who touches these
files.

### H3 — the whole set re-stamps `last-audit` and nothing re-derives `last-body-change`

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md` §2 S8 and S12, and its
four copies — unit 2 S5, unit 3 S7, unit 4 S6, unit 6 S3 — plus §6 AC12.**

`grep -rn last-body-change memory/builds/aHonedRuleset/` returns ZERO hits. No unit, no criterion, no
RUN record names the second stamp key, and no non-goal withholds it.

Check 9 is real and unwaivable (`skills/session-kickoff/manifest-check.sh:398-403`):

```sh
c9n=$(git rev-list --count --no-merges "$LBC..HEAD" -- "${WATCH[@]}" 2>/dev/null || echo 0)
...
if [ "$c9n" -ge 10 ]; then fail 9 ...
```

Measured at HEAD against the live `watch:` list, the counter is **3**. This build lands six commits
that each stage a watched pathspec: unit 6 (`memory/guides/BUILD-METHOD.md`), unit 2 (the template),
unit 3 (`SKILL.md`, `.unattended.conf`, `BUILD-METHOD.md`), unit 4 (the template), unit 5 commit A
(`SKILL.md`, `manifest-check.sh`) and commit B (`manifest-check.sh`). That lands the counter at **9,
one commit of margin**, while `aHoistedPass` is in flight against the same ten pathspecs. Check 9 is
excluded from the staged pre-commit leg, so it reds only at the full bar — which is exactly where
every unit's DoD and AC12 run.

Independently of the counter: unit 5's S12 rewrites `memory/guides/SESSION-KICKOFF.md:22`, which is
manifest BODY prose rather than the audit block, and the checker's own retrofit text defines
`last-body-change` as the sha where the BODY was last revised. The build revises the body while
naming only `last-audit`.

**Prior art, all four verbatim as cited.** `memory/builds/aThawedCorpus/reviews/2026-08-27-review-TOOL-aThawedCorpus-4-diff-round1.md`
F1 is a BLOCKER on this exact defect at 11 watched commits and states that "`last-audit` does not
clear check 9: the two keys measure different events".
`memory/builds/aGroundedOrientation/reviews/2026-08-27-review-TOOL-aGroundedOrientation-1-diff-review-round1.md`
F1 is the same defect and the same fix. `memory/builds/aProvenReuse/reviews/2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round1.md`
names it as a second carrier the specs do not name. And the concurrent build's own
`memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-2.md:284-296` states the rule:
advance `last-body-change` only if the §B re-audit actually changes the body, and re-derive both
counters at the moment of the commit rather than trusting a written line.

Ruled a blocker twice, restated by a sibling build in flight, and absent here. It is HIGH rather than
BLOCKER only because 9 < 10 — the build clears the wall by one commit, and any seventh watched commit
from either build takes that margin away.

**Fix.** In S8 — the item units 2, 3, 4 and 6 copy verbatim — state that before each commit the
builder re-derives `git rev-list --count --no-merges <last-body-change>..HEAD -- "${WATCH[@]}"`, and
that `last-body-change` advances in the same commit whenever the §B re-verify actually changed the
body OR the count would reach 10. Add a clause to AC12 asserting `bash
skills/session-kickoff/manifest-check.sh` exits 0 with no check-9 failure after commit B, the last of
the six.

**Left-shift.** This class has now cost three reviews, so gate it rather than remember it. Two legs,
either of which would have caught it: (a) a spec lint that reds any spec whose files-touched table
names a `watch:` pathspec unless the spec names BOTH stamp keys; (b) a WARN arm in the staged
pre-commit leg that prints the check-9 count once it reaches 7, so the wall is visible three commits
before it is hit instead of at the full bar. (b) is four lines and helps every future build, not just
this one.

---

### M1 — unit 3 S3 corrects three carriers and §6 observes one

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-3.md`, §2 S3, against §6
AC4/AC5/AC14.**

S3 requires the `KICKOFF_EXITS` meaning corrected in three prose carriers plus a rewritten failure
text. AC14 — the round-1 fold for A7 — greps only `tools/unattended/.unattended.conf.example`. Both
of the other two are verified false-after-the-move at base:
`tools/unattended/PROTOCOL.template.md:464` ("how many interactive exits that engine resolves") and
`.unattended.conf:52-54` ("how many interactive exits the engine enumerates"). Neither has a
criterion. AC4's check 22 grades key-name presence and is green on wrong prose — AC14's own rationale
says so, citing `check-unattended.sh:1379-1381` — and AC9's render parity only makes the render match
a stale template. The fourth clause is unobserved too: AC5 asserts only that check 12 prints `5
against 6`, never that the message names the protocol, and `check-arms.py` catches a message edited
without its assertion, not a message left unedited.

**Impact.** Round 1 named one instance and the fold gated that instance rather than the class. A
build can land with two of the three documented meanings still telling a reader the floor counts the
ENGINE — the semantic half §4 itself calls "sharper" than the mechanical one — and with the check-12
message still pointing the next debugger at the wrong document, which is the one thing §5's
observability line says must not happen. Spec 3's own AC13 exists for exactly this shape, so the
omission is measured against the author's own standard.

**Fix.** Widen AC14 into a class check: a single `grep -rn 'engine'` over the `KICKOFF_EXITS`
row/comment in all three of `tools/unattended/PROTOCOL.template.md`,
`tools/unattended/.unattended.conf.example` and `.unattended.conf` returning nothing. Add to AC5 that
the printed check-12 failure names `UNATTENDED-PROTOCOL.md`.

**Left-shift.** Land the widened grep as a permanent arm in `tools/unattended/check-unattended.sh`,
not as a one-shot criterion, so a future edit that reintroduces "engine" in any of the three reds. A
correction verified once and never gated is a correction with a half-life.

### M2 — unit 4 AC7 observes only absences

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-4.md`, §6 AC7** (covering §2
S5 and S8).

AC7 observes that `passes unmarked` is gone from three files and that the parity phrase is still
present once. Nothing observes that S5's and S8's replacement sentences state the receiver-sizing
fact they were written to state. AC7 is the only criterion that reaches `tools/hooks/README.md`, and
it is purely an absence check; AC8 only observes the file in `git diff --stat`; AC11 observes the
backlog row.

**Impact.** Deleting `tools/hooks/README.md:117` outright — or replacing it with a different wrong
sentence — passes every criterion while violating S8. The unit then closes `TOOL-dFramedEntrypoint-1`
(AC11) on a fix half of which was never observed to exist. The spec's own §5 risk line names the
hazard ("S5 and S8 must say the same thing, and nothing gates the agreement of two prose carriers")
and then does not gate it. The charter half is better covered — AC7 keeps `array LITERAL of ≤5
elements` at exactly one occurrence and AC1/AC2 keep the `lens-array bound` extraction non-empty —
but the README half rests on an absence alone, which is the green-by-absence shape §7 bans.

**Fix.** Add a positive clause to AC7: a grep for the pinned phrase of the replacement (e.g. `is a
receiver`, or whatever wording is agreed) returns 1 in both `coding-governance-agents.template.md`
and `tools/hooks/README.md`, so the correction is observed PRESENT rather than only the wrong
sentence observed absent.

**Left-shift.** Spec lint: an acceptance criterion whose only assertion about a file is a count of
zero must be paired with a positive assertion about the same file. That is grep-able over the §6
block, and it generalises past this build — it is the acceptance-criteria form of the charter's
green-by-absence rule, which today is gated for tests and ungated for the specs that plan them.

### M3 — unit 5's ratified high-water bump is in no scope item and no files-touched row

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md`, §2 (S1–S13) and §4
"Files touched", against §8 F1 and §6 AC2.**

F1's ruling reads `RESOLVED (owner, 2026-09-04): bump the high-water down, in the same commit, to the
post-S3 measurement`, and "The bump rides commit A". AC2 grades it. But no scope item S1–S13 names
`tools/template-size-highwater.txt`, and the six commit-A rows of §4's files-touched table do not
include it. F1 also forecloses the escape that unit 3 does it: "unit 5 is the LAST unit in this build
to touch that file — a `--bump` taken at order 2 records a figure order 3 immediately supersedes".
Rev-3's log confirms the omission is unintentional — it records "AC2 gains the high-water clause"
with no matching scope or table edit.

**Impact.** The two sections a builder actually works from describe a commit A that AC2 fails, and
the ruling's own words live only in §8. A builder reconciling table against criterion has to guess
which is authoritative.

**Fix.** Add a scope item to §2's commit-A block — the `skills/session-kickoff/SKILL.md` row of
`tools/template-size-highwater.txt` is re-recorded to the post-S3 `wc -c` via `bash
tools/check-template-size.sh --bump skills/session-kickoff/SKILL.md` — and give it a row in the
commit-A half of §4's table, citing F1.

**Left-shift.** Spec lint, mechanical and cheap: every file path named in a §6 criterion must appear
in either a §2 scope item or the §4 files-touched table. This one lint would also have caught part of
M1 and all of M5.

### M4 — unit 4 S1's "only:" list deletes two parity-pinned phrases

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-4.md`, §2 S1**, against §2
S2/S5 and the §4 candidate text.

S1 reads "so the surviving text carries only:" followed by eight named elements. Neither the
resolvable-K clause nor the array-literal clause is among them, and both are required to survive by
three other places in the same spec: S2 ("Every one of the five phrases
`tools/check-playbook-parity.sh` extracts from this bullet survives verbatim"), S5 (the array-literal
clause is rewritten, not deleted), the §4 PAIRS table (`resolved-K ceiling` = `cannot resolve to an
integer ≤5`, `lens-array bound` = `array LITERAL of ≤5 elements`, both pinned at charter line 240),
and the §4 candidate text, which carries both. The §4 inventory verdicts for fragments I and J are
COMPRESS and REWRITE `to the pinned token` — survivors, not casualties.

**Impact.** A builder implementing S1 literally deletes two of the five parity-pinned phrases, reds
`playbook parity` with `an extraction matched NOTHING` on two rows, and leaves the charter half of
`TOOL-dFramedEntrypoint-1` uncorrected against AC7. S2 and §4 would catch it, which caps the damage
at a wasted cycle — but S1 as written is wrong about what the bullet keeps.

**Fix.** Extend S1's list with the two clauses as §4 grades them — fragment I compressed to `cannot
resolve to an integer ≤5`, fragment J rewritten to `an array LITERAL of ≤5 elements is a receiver it
can size` — or replace "only:" with "only the following, plus every phrase S2 pins".

**Left-shift.** Run the parity extractions over the spec's own fenced candidate text at spec time —
the same `--dry-run` mode H2 asks for. A candidate block that loses a pinned phrase would then red in
the spec, where the fix is one line, rather than at the commit.

### M5 — unit 4 arms five self-test legs and no criterion runs them

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-4.md`, §7, against §6 AC9.**

§7 states the DoD owes one `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` run because S8 arms
five guarded `tools/hooks/` self-test legs. AC9 names only the plain `bash
tools/run-gates/run-gates.sh`, which holds every `chunk = selftests` leg — §7 says so itself ("which
the ordinary bar and `GATE_FULL=1` both hold"), so AC9 structurally cannot reach them. Every other §7
leg unit 4 lacks a dedicated criterion for is on the default bar, which makes these five the only §7
obligation no criterion observes. The sibling comparison is unflattering: unit 3 AC7 grades `bash
tools/unattended/check-unattended.test.sh` and unit 5 AC9 grades `bash
skills/session-kickoff/manifest-check.test.sh`, both off-bar suites.

**Impact.** The unit is fully acceptable with the five armed legs never executed — the green-by-
absence shape this whole build audits for — and the set is inconsistent with itself on one
obligation. Partial mitigation: §7 does write the run as owed, so a builder who reads §7 runs it. But
the acceptance set is what a verify pass grades.

**Fix.** Add a criterion: `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` exits green with
`agent-cap self-test`, `scratch-guard self-test`, `verifier fan-out self-test`, `review-join
self-test` and `hook destinations self-test` reported as RUN rather than skipped.

**Left-shift.** Same lint as M3, one clause wider: every gate leg named in §7 must be named by a §6
criterion unless `tools/gate-legs.json` shows it unguarded and off the `selftests` chunk. The
manifest already holds every fact that decision needs.

### M6 — unit 5's reuse audit contradicts its own executable scope

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-5.md`, §10 "Reuse audit"**,
against §2 S7 and §4 "The parity row".

§10 still reads "Two rows join it and no new mechanism is built" while S7 says "one row joins
`PAIRS`", §4 devotes a paragraph to why a second row over the no-remote fallback cannot be green in
commit A, and the rev-3 log records "its parity subsection went from two rows to ONE". §8 F2's
RESOLVED line even flags the change ("The row count fell from two to one").

**Impact.** §10 is the section a later session greps to learn what a unit added to `PAIRS`. As
written it contradicts the executable scope, and a builder who follows it lands a second row whose
anti-vacuity arm reds `playbook parity` in commit A — the exact failure §4 wrote its paragraph to
prevent. §10 is a live statement, not a frozen fork record, so nothing excuses it.

**Fix.** Change §10 to "One row joins it and no new mechanism is built", and note that the count
moved from two to one at rev-3 per §4's parity subsection.

**Left-shift.** Not mechanical, so make it procedural and cheap: the rev-fold step gains a mandatory
whole-spec grep for any noun whose count the fold changed, with the grep recorded in the rev log. Add
"a fold changed a count in one section and left it stated in another" to the build's own recurring-
class list, which is where §10 of the charter says project-derived classes belong.

---

### L1 — unit 4's margin arithmetic hangs off a closed fork

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-4.md`, §4 "Files touched
(estimate)".**

The paragraph computes "the margin is 21 bytes, down from 178" from "the smallest of them, 48399" —
which is the if-unit-2-drops-its-86-byte-connective branch. Unit 2's §8 F2 was RESOLVED on 2026-09-04
as `keep the connective — the recommendation stands. S2 ships as written at 86 bytes`. Under the
ratified plan the smallest landing is 49144 − 126 − 533 = **48485**, and the margin over the 48378
high-water is **107 bytes**, five times the stated figure.

**Impact.** Bounded — AC4 is stated against base and nothing in the build depends on the number — but
it is a wrong number, not a style call. A later session sizing a fourth cut against "21 bytes of
margin" will believe the carrier is one small edit from dropping under its high-water when it is not.

**Fix.** Delete the two dead unit-2 branches from the paragraph and restate the margin from the
ratified path only: 48485 landing, 107 bytes above the 48378 high-water.

**Left-shift.** Fold this into M6's procedural check: when a fork resolves, re-derive every figure
downstream of it in every sibling spec, and say in the rev log which figures were re-derived. The
mechanical half is already available — `tools/check-template-size.sh` reports the live margin, so a
spec that states one can be asked to cite the command rather than the number, which is the charter's
own "point at the source, or gate the pair".

### L2 — a line pin on a backlog row, wrong at the spec's own base

**`memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-4.md`, §2 S9 and §8 F2
RESOLVED (rev-4 fold text).**

`TOOL-dFramedEntrypoint-1` is addressed as `memory/backlog/TOOL.md:40`. At this build's base
`102e98f0` the row is line **39** and line 40 is `TOOL-dScriptedRepeat-15`; at HEAD the row is line
**42** and line 40 is `TOOL-dHonouredPark-3`, a CLOSED neighbour that would read plausibly to a
builder following the address. So the pin was already wrong when it was written, not merely stale
since. Two corrections to the original report of this: §8 F2 does not carry the bad address, only S9
does, and AC11 correctly greps by id — which is what keeps this LOW.

**Impact.** The backlog is the one mutable record type and rows are added above, so a line pin on a
backlog row is stale by construction. A builder following the address to flip a status edits the
wrong row, and both neighbours are plausible-looking CLOSED entries.

**Fix.** Drop the `:40` from S9 and address the row by id alone, the way AC11 does.

**Left-shift.** One grep as a hygiene arm: red any tracked record containing
`memory/backlog/<FAMILY>.md:<digits>`. Backlog rows are mutable and move; a line pin into one is
always wrong eventually and is never worth writing. This is the cheapest gate in the whole report and
covers a class this repo will otherwise keep committing.

---

## Also checked and clean

Because no lens died, these zeroes are evidence rather than silence:

- No two units claim the same region of the same file for an edit; the ordering constraint in the
  build's step plan holds against the specs' declared write sets.
- Every path named across the five specs exists at base.
- The parity mechanism claims in unit 4 (S2's single-line rule, the five PAIRS phrases) reproduce
  against `tools/check-playbook-parity.sh` — it is unit 5 that disagrees with the source, not unit 4.
- Check 9's threshold, its exclusion from the staged leg, and the live `watch:` list all reproduce as
  H3 states; the counter at HEAD is 3.
- Round-1 B1 is repaired: `gen_build_index.py --check` reports clean at HEAD.

## Cheapest ordering out of CLEAN WITH FIXES

H3 first — it is set-wide, it is one sentence in S8 copied to four siblings plus one AC clause, and
it is the only finding here that ends in a red gate. Then H1 and H2, both in unit 5 and both in
sections a rev-5 fold touches anyway. M3, M4, M5 and M6 are single-sentence edits. M1 and M2 need a
wording decision (what the replacement sentence says) before their criteria can pin it, so they pair
naturally. L1 and L2 are two deletions.

The four left-shift gates worth building regardless of this build are: the AC anti-vacuity arm (H1),
the check-9 early WARN in the staged pre-commit leg (H3), the "every path in a criterion appears in
scope or files-touched" lint (M3, M5), and the backlog line-pin grep (L2). Between them they cover
six of the eleven findings and every one of them is small.

## Round

**Round: 2.** No blockers. Eleven fixes, all inside the specs; no unit is gated on an unsigned fork,
which is the material change from round 1.
