**Serves:** spec-audit TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3 TOOL-aStagedLane-4

# aStagedLane — spec audit of the four-unit set, round 2

*Node `a`, 2026-09-04. A Tier-2 adversarial pass over the four specs at rev-3, with the ROUND-1 FOLD
as the primary subject: the prose written to close round 1 is itself unreviewed surface, and that is
where this round's findings were expected to sit. They do. A primed finder fan, a skeptic stage
prompted to REFUTE each finding, one synthesis. Every claim a finding makes about the existing tree
was re-checked at source before it was written here, and the re-check is quoted inline wherever it is
the load-bearing part.*

**Round: 2.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-1.md@a26e5051771376847cacafe616ea29367ae2780b`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md@cfaf6ea23a31d34f413b733fb0cb529d0c651931`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-3.md@b4dd28ccd4fe871003a6ea4ea2e3edfd74006045`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-4.md@914a83a317c9453e1c6f7d6aeed2828e9cfa49ea`

## Verdict: BLOCKED

Two blockers and nine highs. Round 1 returned BLOCKED because every one of its blockers was a false
premise about what the repository contains. The fold corrected those and introduced new ones of the
same class: the single most load-bearing sentence in the fold — unit 4's S6, which rev-3's own
revision log calls "the new defect the audit did not reach" — prices its entire byte budget against
a sentence in `memory/guides/BUILD-METHOD.md` that does not exist. Four independent finders reached
it separately. That is not a coincidence; it is a signal that the fold was written against a
remembered tree rather than a read one.

## Shape of the run

Raw 48, confirmed 19, refuted 29, unverified 0. Precision 0.40 — below the ~0.5 floor §8 names, which
says to tighten scope or priming before adding agents rather than to widen the fan. The 19 confirmed
findings collapse to **13 distinct defects** after merging duplicates: four finders independently hit
unit 4's phantom plan-verb mention, two hit unit 1's dead `skipped_norun`, two hit unit 3's slice-
grouping contradiction, and two hit unit 1's unsourced cost figure. The merge is recorded per row
below; the counts in this section are the raw ones and the table's are the adjudicated ones.

## The two re-put owner rulings

Both were re-put under the standing mandate because round 1 showed both rested on premises the tree
contradicts. Both re-resolutions are examined here as their own subject.

**Unit 1 F2 — the range anchor.** The re-put is warranted: neither original option disclosed that
both anchors put the flagrant case outside the range, and that is exactly M3's ground for revisiting.
The veto application is correct — the full walk fails AC5's ceiling, which is a gate already written
in this spec, so veto 1 discards it, and the surviving pair is not a real choice because the third
option is the first plus a bounded probe. The mark shape conforms to `memory/TEMPLATE-SPEC.md:119`:
`RESOLVED (agent, 2026-09-04, delegated): <pick>`. **But the resolution's own cost argument is
unsourced and measured over the wrong population** — finding 6 below. The ruling stands; the number
it rests on does not.

**Unit 4 F2 — the charter sentence.** The re-put is warranted for the same reason and the veto
chain is applied correctly: option 1 is discarded by veto 1 (§3's third non-goal), option 2 twice
over by veto 1 (`AGENTS.md` at 64506 bytes against a declared 64512, verified) and by veto 2's
governance-carrier clause, which M3 says the delegation explicitly does not reach. Withdrawal trips
no veto and leaves no follow-up. The mark shape conforms. The recorded reasoning is true of the tree
at every point I checked. **This re-resolution is the one thing in the fold I have no finding
against** — and it is also what makes finding 1 fatal rather than merely wrong, because withdrawing
S5 left S6 as the whole of the unit's remaining risk surface.

## Findings

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| 1 | BLOCKER | 4 | §2 S6, §2 S1 | Budget arithmetic priced against a sentence that does not exist |
| 2 | BLOCKER | 4 | §3 non-goal 2 vs §8 F1 vs unit 2 S5 | Three documents disagree on who owns the mode semantics |
| 3 | HIGH | 4 | §2 S6 | Unnamed, unobserved deletion from a governance guide is the only funding left |
| 4 | HIGH | 1 | §2 S2c vs §3 non-goal 2 | Pre-anchor search drops the record-surface exclusion — a false-positive engine |
| 5 | HIGH | 1 | §2 S3, §6 AC3 | `skipped_norun` is structurally pinned at zero — DEAD PROBE, blessed by AC3 |
| 6 | HIGH | 1 | §2 S2c, §5 perf | The only cost bound cites a figure §4 does not hold, over the wrong population |
| 7 | HIGH | 3 | §2 S3b vs §2 S2, §1, §6 AC2 | One writer per slice, or per group of slices? Both are stated |
| 8 | HIGH | 3 | §2 S4 (no criterion) | Half of the disjointness proof's clause 3 ships unobserved |
| 9 | HIGH | 3 | §2 (absent), §4 | No scope item retires the header this unit makes false |
| 10 | HIGH | 3 | §2 S3c, §4 | "The spec template mandates a backlog row per spec" is false |
| 11 | HIGH | 4 | §7, §6 AC3b | The named hygiene leg does not measure the budget it is claimed to measure |
| 12 | MED | 2 | §2 S3, §6 AC3 | Two of three verdict outcomes have no criterion — including the dangerous one |
| 13 | MED | 2 | §2 S4b, §6 AC8 | `--rescope` replacement rewrites a clause attended mode never composes |

---

### 1 — BLOCKER — unit 4, §2 S6 and §2 S1 (fold text; consequences in §6 AC3b, AC4, AC7)

*Merges four independently confirmed findings.*

S6 is the fold's headline addition and rev-3's revision log calls it "the new defect the audit did
not reach". Its funding plan is one sentence: "S1 REPLACES the mandate qualifier on the guide's
existing plan-verb mention rather than adding a sentence, and S2 is spent from what S1 returns."
S1 carries the same premise: "without the mandate qualifier the guide's only current mention
carries."

There is no such mention. Verified at source:

- `grep -n -- '--plan' memory/guides/BUILD-METHOD.md` returns nothing.
- `grep -n -i plan memory/guides/BUILD-METHOD.md` returns exactly one hit, line 38's word
  "planned", inside a sentence about what the generated units region answers.
- `grep -n unattended memory/guides/BUILD-METHOD.md` returns four hits, and the only driver
  invocation among them is line 204: `` `git log --oneline -5` — under a mandate, `bash
  tools/unattended/unattended.sh --resume <slug>` `` — a different verb, in M7's regrounding reading
  list, not in the M2 detect paragraph S1 edits. Rewriting that line would break the regrounding
  instruction.
- `grep -- '--plan' tools/memory-tree/BUILD-METHOD.template.md` returns nothing either, so the
  byte-compared half does not hold it in the guide's place.

So S1 replaces nothing and returns zero bytes. Both S1 and S2 are pure additions against the
headroom S6 measures exactly right: 24553 bytes of 24576 and 317 lines of 350, both confirmed by
`wc`. **23 bytes.** The literal `tools/workflows/unattended-build.js` that AC7 demands is 35 bytes
on its own, before the two mode words AC7 also demands and before whatever prose carries them.

The consequences are not cosmetic. AC3b (≤24576 bytes) and AC4/AC7 (the detect and passes
paragraphs must name the verb and both modes) cannot all be satisfied, so by S6's own terms the unit
PARKS — and S6 presents parking as the unlikely branch rather than the arithmetic one. Unit 4 is a
documentation-only unit; a park is the whole unit gone. Meanwhile a builder reading S6 goes looking
for a sentence to edit and finds M7's `--resume` line, which is the nearest match and the wrong one.

Note the shape: the spec's own §1 concedes the detect step "tells a run to read the build README's
units table and classify by hand", which is a statement that the guide names no verb — S6
contradicts the unit's own goal paragraph.

**Fix.** Correct S1 to state that the guide carries no plan-verb mention today and that its only
driver mention is `--resume` at :204 in M7. Re-price S1 and S2 as pure additions and state the
byte cost of each. Then take one of two exits explicitly: name the specific M11-duplicated rule
whose deletion funds them, with a scope item performing it and a criterion observing it (see finding
3); or declare in §2 that this unit's expected disposition is PARK pending an owner budget turn.
Do not leave the park conditional on arithmetic the spec gets wrong.

**Left-shift gate.** The class is "a spec prices an edit against text that is not in the tree". A
cheap gate exists: a check that every backtick-quoted `--<verb>` literal and every `path/to/file`
literal appearing in a spec's §2 scope items resolves — the verb against the driver's own verb
table, the path against `git ls-files`. It would have caught all four of round 1's blockers and
this one. Scope it to `memory/builds/*/spec/*.md` and report near-misses, per §7's rule about
running a candidate predicate over the real tree first.

---

### 2 — BLOCKER — unit 4, §3 non-goal 2 against §8 F1's resolution, and against unit 2 §2 S5

Both texts are current at rev-3 and are exact opposites about the same thing.

- §3, non-goal 2: "Not restating the harness's mode semantics. Unit 2's file header owns them; this
  unit points."
- §8, F1 RESOLVED (owner, 2026-09-04): "keep it a pointer; the method carries the mode semantics.
  S4 stands and the carriers row does not move."

F1's chosen option was explicitly "keep the header short enough to stay a pointer and put the mode
semantics in the method". The non-goal says the header owns them. One of these is an **owner ruling**
and the other is a non-goal that veto 1 makes binding on every subsequent resolution — a delegated
run cannot pick between them, and rev-3's revision log never reconciles them.

Unit 2 then builds the third position: S5 requires the harness header to enumerate five named losses
(the `--review` round record, `--dispatch`'s order refusal, `--dispatch`'s write-set record,
`--brief`'s record, `--rescope`'s amendment row), each classified as refusal or record, plus the S7
caller-dependence — and AC6 observes it. That is the mode semantics, in the header, which is what
F1 ruled against. And `memory/project/method-carriers.txt:19` currently asserts of that same file:
"It states no rule the method does not." Unit 2's S5 header breaks that assertion, while unit 4's S4
hedges — "If unit 2's header additions make it state a rule, the row is re-classified in this unit"
— which contradicts F1's "the carriers row does not move".

This is load-bearing on finding 1's arithmetic, not a wording preference. Under F1's ruling the
method must carry the mode semantics, which is far more than 23 bytes and forces the park. Under
non-goal 2 the method merely names the two modes, which might fit. The implementer cannot know which
document to build.

**Fix.** Pick one owner and make all three agree in one rev. The recommended pick is F1's ruling,
since it is the owner's and the only one of the three with ratified authority: delete or invert
non-goal 2, state in S2 how much of the semantics the passes paragraph carries and price that
against S6, and resolve S4 unconditionally rather than with an "if" — including an explicit answer on
whether unit 2's five-loss header re-classifies the carriers row. If the answer is that it does, that
is a carriers edit unit 4 must scope, not hedge.

**Left-shift gate.** `tools/memory-tree/check-method-carriers.sh` already grades the carriers
registry. Extend it, or add a sibling leg, that reds when a spec's §3 non-goal and its §8 `RESOLVED`
mark contain contradictory assertions about the same file — hard in general, cheap in the specific
case that matters: red when a `RESOLVED` mark names a file that a §3 non-goal in the same spec also
names, and require the spec to carry an explicit reconciliation line. Cheaper still and worth doing
regardless: a leg asserting that every file `method-carriers.txt` classifies as a pointer is still a
pointer after a diff touches it.

---

### 3 — HIGH — unit 4, §2 S6 (fold text), no criterion in §6

S6 authorises spending S2's bytes from "any deletion M1's own rule already mandates — a rule stated
both here and in an M11 carrier is 'a defect HERE' whose resolution is deletion". It names no
candidate. §6 (AC1, AC2, AC3, AC3b, AC4, AC7, AC5) contains no criterion identifying what was
deleted or establishing the duplication that sanctions it, and AC3b is a pure size bound satisfied
by any deletion — correct or not.

Combined with finding 1, this becomes decisive rather than untidy: with S1 returning nothing, the
unnamed deletion is the **only** funding for 23 bytes. A builder under byte pressure goes hunting in
a governance guide for something to remove, with nothing observing the choice, inside a run holding
a delegated mandate that M3 says does not reach veto 2's governance-carrier clause.

The weaker half of this finding, recorded for completeness: S6 invokes veto 2 to forbid raising the
budget while not addressing whether deleting a rule from the same guide is itself a
governance-carrier change needing the same owner turn. M1's own rule does mandate deleting a
duplicated rule, so the act is arguably not discretionary — but the spec should say so rather than
leave it inferred.

**Fix.** Name the specific duplicated rule and its M11 carrier in S6. Add a criterion that the
deleted text is identified by name and is present, verbatim in substance, in that carrier. State
explicitly whether the deletion trips veto 2; if it does, park S2 rather than delete.

**Left-shift gate.** A leg over `memory/guides/BUILD-METHOD.md` and its M11 carriers that reports
rules stated in both — the duplication M1's rule targets. Report-only at first, since the predicate
is fuzzy; even a crude one (normalized sentence overlap above a threshold, printing hits and
near-misses) turns "any deletion M1 mandates" from a licence into a list.

---

### 4 — HIGH — unit 1, §2 S2c against §3 non-goal 2

S2c defines the new pre-anchor search as "a whole-token id match" and stops there. The existing
build-commit definition, at `tools/unattended/check-pass-order.sh:174-176`, is "the earliest commit
in BASE..HEAD whose SUBJECT carries this id as a WHOLE TOKEN **and which touched a path outside the
RECORD SURFACE**" — the build folder plus `GENERATED_INDEXES` plus `SHARED_RECORDS`, and
`.unattended.conf:187` sets `SHARED_RECORDS="memory/DECISIONS.md memory/backlog"`. §3's second
non-goal forbids changing that definition.

So S2c either redefines the build commit, violating its own non-goal, or drops the exclusion by
accident. The concrete cost of the second: a commit `backlog(TOOL-xFoo-1): open the row` touching
only `memory/backlog/TOOL.md` normally lands *before* the build folder exists. S2c's search finds it
in the pre-anchor window, calls it a VIOLATION, and reds the merge bar on a build that did nothing
wrong. The pre-anchor window admits only product commits (true positives) or record commits (false
positives), so the omission is decisive rather than cosmetic — this is a false-positive engine on
the one place the leg reports a hard violation rather than a tally.

The script's own comment block records that getting this exclusion wrong "made a CONFORMING run
unlandable", that the shared-records half was omitted once already, and that it was reproduced on
the kit's own fixture. The fold is re-introducing a known, reproduced failure mode.

**Fix.** State in S2c that the pre-anchor search reuses the SAME build-commit predicate — whole-token
subject match AND a path outside the record surface — naming the exclusion set. Add an AC arm: a
pre-anchor commit touching only a `SHARED_RECORDS` path and naming the id must NOT be reported as a
violation.

**Left-shift gate.** This one is a test arm, and it belongs in `check-pass-order.test.sh` under S5:
the fixture already exists in shape. Add the record-only pre-anchor commit as its own arm, observed
RED before the exclusion is written and green after — the "stage the break, confirm RED, unstage"
discipline §7 makes a landing condition for a new gate.

---

### 5 — HIGH — unit 1, §2 S3 (fold text), §6 AC3

*Merges two independently confirmed findings.*

S3 retains `skipped_norun` and gives one reason: "S2b leaves it a residual population — a build
whose `RUN.md` is unreadable for a reason neither S1 nor S2b admits". That population is empty.

Verified in `tools/unattended/check-pass-order.sh`: the counter is initialised at :147 and
incremented at exactly three sites and nowhere else — :160 (no `RUN.md`), :162 (`base:` not
hex-shaped), :163 (sha does not resolve) — and printed at :262 as "with no pinned run BASE". S1
removes the :160 exclusion by grading run-state-free builds. S2b routes :162 and :163 to the folder
anchor by its own wording, "a line that is not hex-shaped, or a sha that does not resolve". Every
failure mode of the `RUN.md` read lands in one of those two: an absent or unreadable `base:` line
yields the empty string, which is not hex-shaped, which is :162.

After this unit the counter can only ever print 0. That is a liveness field pinned at zero, printed
forever beside four fields that move — the DEAD PROBE class this leg's own header block makes
load-bearing and the charter states twice ("a probe that cannot move says so"). AC3 blesses it: it
requires only that the four prior counts are "still present", which a permanently-zero field
satisfies. The leg currently reports `4 with no pinned run BASE`; a reader who watches that drop to
0 and stay there cannot tell a widened population from a broken counter.

**Fix.** Pick one. Retire the count and say in S3 that S1 and S2b close every path to it, adjusting
AC3 so it does not require a dead field. Or name the actual fourth branch that keeps it live — there
is none in the current script, so this means adding one, e.g. a `RUN.md` that exists but cannot be
read at all. Or keep it and have the leg print `0 (no residual path remains)` as an explicit
announcement rather than a bare tally.

**Left-shift gate.** `python tools/memory-tree/check-arms.py` is already in this unit's §7 for the
new branches. The generalisable leg is narrower and worth its own row: for each counter a gate's
liveness line prints, assert at least one reachable increment site exists in the same script. A
counter with zero increment sites is a compile-time-detectable dead probe, and the predicate is a
grep pair.

---

### 6 — HIGH — unit 1, §2 S2c and §5 (perf / scale)

*Merges two independently confirmed findings, one graded medium and one high.*

Both S2c and §5's perf bullet bound the new pre-anchor walk's cost with the same phrase: "which is
5 units across the whole tree at the reading in S4". Two things are wrong with it.

**The figure is not in S4.** §4 of this spec (lines 55-67) carries the 463 s and 134 s timings and
the 90 and 900 ceilings. It carries no unit count of any kind, and no other record in the build
folder holds one. The only cost bound on the mechanism that survived F2's cost-based veto has no
source in the spec that states it.

**The figure measures the wrong population.** `unbuilt` is incremented at :215 and :221, both of
which sit *after* the `RUN.md` gate at :160. So no current reading of that counter can see a
run-state-free build at all — every reading covers unattended builds only. S1 adds three
run-state-free builds inside the 2026-09-01 cutoff (dGaugedVintage, dFoldedVerdict, aSurfacedLexicon)
carrying 20 CLOSED units whose miss rate is simply unmeasured. Records-only units are the ordinary
`unbuilt` shape, which is exactly the class most likely to miss in the new population, so the miss
count is not plausibly zero.

Cost is the ground F2's re-resolution used to discard the full-walk option, and AC5's ceiling is the
criterion this unit is most likely to fail. HEAD is 1969 commits, so a miss on a 2026-09-01 build
walks nearly the whole graph. I discount the more alarming framing — a pre-anchor id scan can be one
`git log --format` per miss, which is cheap — but the spec mandates no such idiom and states no
bound that holds.

**Fix.** Say where the 5 comes from: the command and the date. Re-derive the miss count over the
WIDENED population. If it cannot be measured before S1 lands, say so plainly and bound S2c by
construction instead — cap the pre-anchor probe at a declared commit count and count what it
truncates on the liveness line. Make AC5's reading be taken after S1 *and* S2c land, not after S1
alone.

**Left-shift gate.** The generalisable rule is already the charter's ("NO count of a derived
population is written in prose"), and it is gateable here: a leg that reds when a spec's §5 or §2
states a figure attributed to another section of the same spec that does not contain it. Narrow
predicate, zero false positives, catches exactly this. The cost half is already covered —
`AC5` plus the manifest ceiling — provided the reading is retaken at the right point.

---

### 7 — HIGH — unit 3, §2 S3b against §2 S2, §1 Goal and §6 AC2

*Merges two independently confirmed findings.*

Three statements say one writer holds one slice:

- §1 Goal: "each writer holding a brief for its own slice and nothing else".
- §2 S2: "the spec stage fans one writer per slice".
- §6 AC2: a brief "appears in the writer's prompt and no other slice's brief does".

S3b then mandates the `tier2-review.js:397` shape: `chunk(slices, Math.ceil(slices.length / K))`
with K ≤ 5. Verified at source — `chunk(a, n)` slices contiguously into groups of `n`, and the
comment above :397 states the intent outright: "Bounding the group COUNT makes the batch grow and
the agent count stand still." At six slices, `Math.ceil(6/5) = 2`, so three writers each hold TWO
slices' briefs.

So at slices > K, all three statements above are false of the shape S3b builds, while AC1 (total
never exceeds K) is true of it. The unit's headline property degrades silently to K writers each
holding up to `ceil(N/K)` briefs — and it degrades at exactly the build sizes that motivate the
unit. AC1's fixture uses three slices against K ≤ 5, which chunks to size 1, so every arm the spec
writes runs in the regime where the two readings happen to agree. The implementer has two
incompatible readings and no criterion distinguishes them. Rev-3 rewrote AC1 without revisiting AC2
or S2.

**Fix.** Restate S2 as "one writer per GROUP, where a group is one or more slices", and rewrite the
goal sentence to match. State in S3b what a grouped writer's prompt receives — every brief in its
group, merged. Re-scope AC2 to "the writer's prompt carries the briefs of its own group's slices and
of no slice outside it". Add an arm at slices > K, because AC1's three-slice case never exercises
the grouping.

**Left-shift gate.** A test arm, and it is the same discipline as finding 4: the S6 arms must include
one whose slice count exceeds K, so the merged-group prompt is the shape actually observed. The
class-level gate is the one §7 already names — "gate the CLASS, not the instance" — applied to
fixtures: a fan's test arms must include a case above the cap, or the cap's behaviour is untested.

---

### 8 — HIGH — unit 3, §2 S4, no criterion anywhere in §6

S4 — every writer's prompt forbids running the index generator — has no acceptance criterion.
§6 covers the fan (AC1), the brief (AC2), the fallback log (AC3), the refused and all-dead merge
(AC4), the gates (AC5, AC6) and S3c's author-never-commit prompt (AC7). None observes the generator
prohibition.

§4's "Why the fan is permitted" states that clause 3 of the disjointness proof "needs BOTH S4,
keeping the index generator out of the writers' hands, AND S3c". The fold added AC7 for the S3c half
with the explicit reasoning "no downstream gate reads a prompt" — and did not apply the identical
argument to S4, which is the other half of the same clause. §5's own risks line names a writer
running the generator as the live risk.

So the load-bearing half of clause 3 ships with no observation of any kind, in a spec that has just
demonstrated it knows prompts need one. A writer prompt shipped without the prohibition races the
generated build index across N concurrent writers, and nothing in the bar or the spec would catch
it.

**Fix.** Add a criterion beside AC7: when the composed writer prompt is inspected, it forbids
running the build-index generator by name. Add the corresponding arm to S6.

**Left-shift gate.** The general rule — every §2 scope item is observed by at least one §6 criterion
— is mechanically checkable and would have caught this, finding 12, and rev-2's AC7 gap in unit 4.
A leg over `memory/builds/*/spec/*.md` that parses the `**S<n>**` labels out of §2 and the
`**AC<n>**` labels out of §6 and requires every scope item to be named by at least one criterion is
crude but not vacuous; require the spec to carry an explicit `S<n> — observed by AC<m>` mapping and
red on an unmapped item. This is the single highest-value gate in this report: three of thirteen
findings are instances of it.

---

### 9 — HIGH — unit 3, §2 (absent item), against §4 "How this stage relates to the ratified parallelism route"

No scope item retires the header of the file this unit edits. Verified at
`tools/workflows/unattended-build.js:41-56`: "TWO SHAPES HERE ARE FORCED RATHER THAN CHOSEN… The
shapes it admitted were a bounded PARALLEL fan — which the ratified verdict above forbids — and a
SINGLE call", and case 1 reads "EACH STAGE IS ONE AGENT holding the ordered unit list, rather than
one agent per unit."

Unit 3 makes the spec stage a bounded parallel fan of writers. So case 1 becomes false of the file,
and the header declares the file's own new shape forbidden. Spec 3's S1–S7 and its Files-touched
estimate name the script and its test only; no item amends that header. Meanwhile §4 leans on the
same header as evidence that the ratified verdict "is not contradicted here", reading it as applying
to dispatch alone when it is written about the SHAPE choice for every stage.

After this unit the file's own header describes a tree it no longer matches — the drift class this
repository gates for, in a build whose sibling unit reasons explicitly about not landing a document
that describes a route the tree does not have.

**Fix.** Add a scope item editing that header block: scope the "one agent per stage" claim to the
BUILD stage, record that the spec stage now fans under S3b's bounded receiver, and state why the
ratified verdict does not reach it (S3c's author-never-commit). Add an AC reading the header back,
the way unit 2's AC6 does for its own header.

**Left-shift gate.** `memory/project/method-carriers.txt` already registers this file as a carrier.
The leg to add is a freshness one: when a diff touches a file the carriers registry lists, the diff
must also touch that file's declared claim region, or red. That is the same ratchet shape the
codebase map uses for dossiers, applied to carrier headers.

---

### 10 — HIGH — unit 3, §2 S3c and §4

S3c argues that writers must not commit, partly because "the spec template mandates a backlog row
per spec, so they would contend on `memory/backlog/<FAMILY>.md`, a record clause 3 of the
parallelism rule enumerates BY NAME". §4 repeats it.

That mandate does not exist. `grep -c backlog memory/TEMPLATE-SPEC.md` returns **0** — the spec
template contains no occurrence of the string at all. The only nearby rule is `memory/HYGIENE.md:40`,
which says a single-file build is "one spec file plus its backlog row — no README": a condition on
single-file builds, not an obligation attached to every spec. And this build is its own
counterexample — `grep aStagedLane memory/backlog/TOOL.md` returns nothing, so four specs added
zero rows.

A false premise inside the disjointness proof is the one place this spec set was already blocked on
for exactly this shape. The conclusion survives on the git-index half alone, which is true and
sufficient: M6 does make "a spec authored" a pass and does order a commit at the end of every pass,
so N writers would contend on one git index. This is a correction to the argument, not a redesign.

**Fix.** Delete the backlog clause from S3c and from §4, or re-anchor it to whatever actually
mandates the row and verify that source. Leave the git-index ground as the stated reason writers
author and never commit.

**Left-shift gate.** Same gate as finding 1: a spec's claims about named tracked files should be
checkable. Narrower and immediately buildable — a leg that reds when a spec asserts "<file> mandates
<X>" for a file in `memory/` whose text does not contain a plausible token of X. Report-only,
printing hits and near-misses, per §7's rule about running a candidate predicate over the real tree
before wiring it.

---

### 11 — HIGH — unit 4, §7 Gates, and §6 AC3b

§7 names `check-memory-hygiene.sh` and claims its "guide caps are what S6's 23 bytes are measured
against". They are not. `tools/memory-tree/check-memory-hygiene.sh:63` sets
`GUIDE_CAP_BYTES=61440 ; GUIDE_CAP_LINES=750`, and `.memory-tree.conf` overrides only the INDEX and
DOSSIER caps — I checked both. So the hygiene leg passes this guide up to 60 KiB, two and a half
times the 24576 S6 works against. M1 itself says of its ≤24 KB / ≤350 pair: "No gate enforces the
pair."

§7's false claim is paired with AC5, which asserts that same leg exits 0. A run reading §7 takes a
green hygiene leg as proof the budget held. That is green-by-absence, sitting on the constraint the
spec itself calls "the constraint most likely to stop this unit".

**Fix.** In §7, say that the hygiene leg caps guides at 61440 bytes and 750 lines and does NOT
measure M1's budget, quoting M1's own "No gate enforces the pair". Re-write AC3b as an explicit
manual measurement — `wc -c` and `wc -l` against 24576 and 350 — recorded in the acceptance ledger,
so it is a documented check rather than an implied leg.

**Left-shift gate.** This is the one finding in the report whose fix is a real gate rather than a
sentence, and the gate is trivial: a leg asserting `memory/guides/BUILD-METHOD.md` is ≤24576 bytes
and ≤350 lines, with the template half held to the same pair. M1 has stated the budget since M12
landed and has been raised three times by owner call; that it has never been enforced is why unit 4
is 23 bytes from the wall with nobody having noticed. Cost is one `wc`. Add it whether or not unit 4
lands.

---

### 12 — MEDIUM — unit 2, §2 S3, §6 AC3

S3 specifies three verdict outcomes: zero blockers is terminal, a positive integer is converging, a
non-integer REFUSES. Only the third has a criterion. §6 runs AC1 through AC9, and AC3 alone touches
the verdict — the null refusal. Nothing observes that a blocker count of 0 terminates, or that a
positive count converges.

The verdict computation is the entire substance of attended mode's audit stage, and S3 is a NEW
scope item of this unit. A branch that maps a positive count to terminal reaches BUILD over open
blockers and satisfies every criterion in §6, since AC1 and AC4 both merely require the build stage
to be reached. That is the failure the whole audit stage exists to prevent, and the header of
`unattended-build.js` makes the terminal-verdict gate the file's whole enforcement claim — an
unobserved inverted mapping deletes it silently.

**Fix.** Add a criterion observing both live paths: a returned blocker count of 0 yields the terminal
verdict and the build stage is reached; a positive count yields converging and the caller is told to
loop. Add both arms to S6.

**Left-shift gate.** Covered by finding 8's scope-item-to-criterion mapping leg. Nothing
subject-specific is needed here.

---

### 13 — MEDIUM — unit 2, §2 S4b, §6 AC8

S4b replaces `--rescope` in the BUILD prompt "so M4's PROMOTE disposal stays available". That
disposal clause is never composed in attended mode. Verified at
`tools/workflows/unattended-build.js:473-475`: `const disposal = verdict === 'CONVERGED' ? '' : …`,
and the CONVERGING gate returns before BUILD. Under S3, attended mode reaches BUILD only at zero
blockers, which is CONVERGED, so `disposal` is always the empty string in the mode S4b is written
for.

So the `--rescope` third of S4b rewrites a string that mode never builds, and its stated rationale is
false for it. AC8's clause "its disposal clause names the roster edit rather than `--rescope`" cannot
be observed on a composed attended prompt: it either fails outright or passes because the substring
is absent for the wrong reason — the vacuous-selector class this spec set polices elsewhere. The
`--dispatch` and `--brief` two-thirds of S4b are live and unaffected.

**Fix.** Either give attended mode a terminal-with-standing-blockers verdict in S3, so the clause is
reachable and AC8 can observe it; or drop the `--rescope` replacement from S4b, state plainly that
the disposal clause is unreachable in attended mode, and scope AC8 to the two verbs actually
removed.

**Left-shift gate.** The class is "an assertion that passes because its subject is absent". A general
gate is hard; a cheap specific one is not — for every arm asserting a substring is ABSENT from a
composed string, require a paired arm asserting the surrounding clause is PRESENT, so absence is
distinguishable from the whole clause being empty. Worth a row in the recurring-bug-class checklist
either way.

---

## What the fold got right

Recorded because a review that lists only defects mis-prices the work.

- Both re-puts were correctly identified as necessary, and both mark shapes conform to
  `memory/TEMPLATE-SPEC.md:119`.
- Unit 4's F2 re-resolution is sound end to end: the veto chain, the two byte measurements
  (64506/64512 and 24553/24576), the M3 delegation limit, and the conclusion that withdrawal leaves
  no follow-up. I found nothing against it.
- Unit 1's S3 correctly caught that the liveness line already printed FOUR counts against a comment
  claiming three, and fixes the stale comment in the same commit.
- Unit 1's S4 correctly identified that the ceiling has TWO carriers, named which one binds the
  merge bar, and deletes rather than restores the false "one figure, two readers" parity comment.
- Unit 3's S5 caught a real deleted guard: a merged object is always truthy, so `if (!specced) throw`
  stops firing after the fan. That is the kind of finding this whole exercise is for.
- Unit 4's AC6 replacement is a genuine improvement — the rev-2 criterion was satisfied by the
  unmodified tree and, paired with AC3's lower clause, rewarded editing nothing.

## Left-shift summary

Ranked by value across the thirteen defects, one line each.

1. **Scope-item-to-criterion mapping leg** over `memory/builds/*/spec/*.md` — catches findings 8 and
   12, and would have caught rev-2's AC7 gap in unit 4. Three of thirteen.
2. **Spec-claim resolution leg** — every backtick-quoted verb and path literal in a spec's §2 must
   resolve against the driver's verb table and `git ls-files`. Catches finding 1, all four of round
   1's blockers, and most of finding 10.
3. **`BUILD-METHOD.md` budget leg** — one `wc` pair against 24576/350 on both halves of the compared
   pair. Catches finding 11's real gap, and it should land whether or not this build does.
4. **Dead-counter leg** — every counter a gate's liveness line prints must have at least one
   reachable increment site. Catches finding 5; a grep pair.
5. **Carrier-freshness ratchet** — a diff touching a file the carriers registry lists must touch its
   claim region. Catches finding 9.
6. **Test arms above the cap** — a fan's arms must include a case with more inputs than K. Catches
   finding 7; the same discipline covers finding 4's record-only pre-anchor arm.
