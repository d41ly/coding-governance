**Serves:** spec-audit TOOL-dDerivedDocket-37

# dDerivedDocket — spec audit of topic group G6, the hands-off payload join, round 2

*Node `d`, 2026-09-20. The second Tier-2 adversarial pass over the one G6 spec, the spec-token join
over a hands-off bullet's payload tokens (unit 37). This is a FOLD review, regrounded on `fb07ca25`:
origin/main moved 210 commits past the original BASE `abac6d59`, HEAD merges it in, and the spec
re-verified its claims there and moved its header base under a section 9 line reading `regrounded on
fb07ca25`. Code claims below are judged at HEAD. The pass was aimed at the text nobody has reviewed
— every section 9 line dated after the round-1 record of 2026-09-16, which for this spec is the
rev-2 fold, the rev-3 regrounding and the four extensions dated 2026-09-20 — and at whether each
round-1 fix holds. Four primed finder lenses ran and all four returned; a skeptic stage prompted to
REFUTE each finding ran in five batches and all five returned; then this synthesis. The sources were
the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md`
with its roster and edge tables, and the round-1 record
`memory/builds/dDerivedDocket/reviews/2026-09-16-review-TOOL-dDerivedDocket-37-spec-audit-g6-round1.md`.
Sibling specs outside G6 were read wherever an edge or an interface named them. Every finding below
was re-checked against source at HEAD before it was written down, and the sites read are named in
each entry; where a claim rests on a tool's behaviour rather than on its text, the probe that
measured it is given with its output.*

**Round: 2.** Range at base `fb07ca25`, the subject pinned at the blob it was read at:
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-37.md@5b17ef766973334ff3b3b0fc5178d0177c4353e6`

## Verdict: CLEAN WITH FIXES

No blocker stands, and all nine of round 1's distinct defects are folded — this round found no
defect in eight of the nine fixes. What stands is one HIGH defect carried by two finding ids and two
MEDIUM defects carried by one id each: three items, four raw confirmed findings.

The one defect worth reading first is H1, and it is the round-1 fold's own shadow. Round 1's H2
moved this unit from order 39 to order 6 so its real-tree pass would grade a live population instead
of an emptied one, and S6 and AC6 now require a graded bullet count above zero on this unit's own
commit. That requirement forces the cutoff key backwards: `SPEC_HANDOFF_CUTOFF="2026-09-14"` has to
reach specs already written. But a new cutoff key in `.memory-tree.conf` is governed by a relation
the owner ratified at `TOOL-aJoinedCanon-1` section 8 F1 — the value sits strictly past both the
newest spec filename date on any ref and the setting commit's own date — and this value fails both
clauses. No section of the spec names that ruling, and no section records a departure from it. The
spec is not unbuildable because of it; it is unwritable as directed, because S3 orders the key's
header comment "in the idiom of `SPEC_LEGLINE_CUTOFF`", and that idiom's why-this-date slot IS the
relation this value breaks.

The two mediums are both the house's dominant class in a new place. M1 is a deliverable with no
observer: S7 loads the checker's header docstring with the whole new limits paragraph and closes
"Observed by AC8 and AC11", but neither criterion reads a byte of that docstring. M2 is a criterion
whose third state rides its own second state's failure, so the defect its Red-when names — a waiver
keyed on the bare token rather than on the edge — passes all three states green.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero count below
is evidence rather than an artefact of a missing lens. Two ids, 8 and 15, describe one defect from
two addresses and are merged into H1; the pipeline's duplicate count of 0 comes from its own
exact-match dedupe, which does not see a restatement.

## Review shape

Raw 18, confirmed 4, refuted 14, unverified 0. Precision 0.22, the lowest of this build's eleven
audit runs and less than half the ~0.5 floor charter section 8 sets. Round 1 over this same spec
already read 0.41 and inferred the fan was too wide for one small subject; this round halves that
again over a spec that is now largely folded. The inference holds and hardens: a one-spec group that
has already converged does not earn four lenses. The 14 refuted findings are not reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 1 | 2 |
| MEDIUM | 2 | 2 |
| LOW | 0 | 0 |
| Total | 3 | 4 |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the G1 to G5
reports and this group's round 1 used, so the six groups' counts compare.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  layer which stays inert or broken while its suite reads green.
- MEDIUM covers a contradiction with a bounded consequence, a declaration a spec owes, and a rule
  whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small.

Against the finders' ratings, nothing moves. Both ids behind H1 came in rated high and stay there;
both mediums came in rated medium and stay there. The one call worth stating is why H1 is not a
BLOCKER, since the finding's own text argues a fork contradicting an owner ruling "is not a run's to
take". It is not a blocker because one of the two routes out is entirely inside the run's authority:
re-deriving the value by the register's relation needs no owner turn. It costs the retroactive grade
and forces S6 and AC6's above-zero clause to be re-cut, which is a spec edit this run may make. Only
the other route, keeping the date as a recorded departure, needs the owner. A defect with a route
the run can take alone is HIGH by this scale.

## Findings index

| Id | Severity | Entry | Address |
|---:|---|---|---|
| 8 | HIGH | H1 | §2 S3; §6 AC6; §5 risks |
| 15 | HIGH | H1 | §8 F3; §2 S3; §5 risks |
| 3 | MEDIUM | M1 | §2 S7 first sentence; §6 AC8 and AC11 |
| 4 | MEDIUM | M2 | §6 AC5 third sentence |

The one spec path is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-37.md`.
Every section sign and bare line number below refers to it at blob `5b17ef76`.

## Blockers

None. No finder rated a finding BLOCKER, and none is adjudicated one here. The nearest is H1, and
the paragraph above says why it stops short.

## High

### H1 — the new cutoff key sits behind both clauses of a ratified relation, and no section records the departure (8, 15)

**Address.** §2 S3 (the key and its header comment), §8 F3 (the fork that chose the date), §6 AC6
and §2 S6 (the above-zero clause that forces it), §5 risks (the sentence that affirms the outcome
the relation exists to prevent).

**What is wrong.** `SPEC_HANDOFF_CUTOFF="2026-09-14"` breaks both clauses of the cutoff relation the
owner ratified at `TOOL-aJoinedCanon-1` section 8 F1. The relation is recorded on the
`REV_SCOPE_CUTOFF` row at `.memory-tree.conf:131-139` — "every cutoff it introduces sits strictly
past the newest spec filename date on any branch, and past a date this fleet can still write into" —
and restated with both clauses spelled out, with the three reading commands, on the
`SPEC_DIRECT_CUTOFF` row at `:252-265`. Clause (a) demands a value past the newest spec filename
date on any ref; this value EQUALS this build's own spec filename date. Clause (b) demands a value
past the setting commit's own date; this value precedes it, since the commit lands 2026-09-20 or
later.

The break is not incidental, it is load-bearing, which is what makes this the fold's own shadow.
Round 1's H2 moved the unit from order 39 to order 6 precisely so its pass would grade a live
population, and the fold wrote that into S6 and AC6 as a graded bullet count above zero on this
unit's own commit. A relation-conforming cutoff grades zero bullets on landing day, by the relation's
own design — `.memory-tree.conf:143-146` states that cost for `REV_SCOPE_CUTOFF` and the
`SPEC_DIRECT_CUTOFF` row states it again. So the round-1 fix and the ratified relation are in direct
tension, and the spec resolves the tension silently, in favour of the fix, without naming the rule it
is overriding.

Nothing in the tree records a departure. §8 F3 weighs only 2026-09-14 against 2026-09-08 on coverage
and branch reach, and never names the ruling, the register or the one precedent that went the other
way (`ACCEPTANCE_LEDGER_CUTOFF`, taken so a check ships exercised on real units — this unit's exact
rationale — and weighed and rejected at that same F1). Grepped at HEAD, `SPEC_HANDOFF_CUTOFF` occurs
in exactly two files: this spec and this group's round-1 review. No sibling spec of this build
mentions the key or the relation.

**Why it bites, concretely.** S3 directs the builder to write the key's header comment "in the idiom
of `SPEC_LEGLINE_CUTOFF`" including "why this date". That idiom's why-this-date slot, at
`.memory-tree.conf:239`, reads "the build-wide ruling `REV_SCOPE_CUTOFF` above records, re-derived at
LANDING". The builder cannot write that header without either restating a relation this value breaks
or contradicting the register with no recorded authority. S3 also appeals to the checker's own header
as its authority for the ISO refusal, and that same header at `tools/check-spec-tokens.py:47-48`
states the relation as the file's rule for every cutoff key it reads: "A set key that is not strictly
past the day it was committed is REFUSED before grading: the register's rule is a relation to the
fleet working day, and a value carried across a day boundary is stale by construction."

No leg reds today only because the mechanical clause-(b) refusal at `tools/check-spec-tokens.py:294-320`
is hard-coded to `DIRECT_KEY`. Measured at HEAD, the two keys that file reads both satisfy the
relation — `git log -1 --format=%cs --pickaxe-regex -S'^SPEC_LEGLINE_CUTOFF="?2026-09-08"?$' --
.memory-tree.conf` returns `2026-09-07`, and the same query for `SPEC_DIRECT_CUTOFF="2026-09-15"`
returns `2026-09-14` — so the assertion is silent only because it is narrow, not because this key
would survive it. The left-shift below widens it, and widening it refuses this unit's key before
grading, which is exactly why the departure has to be decided now rather than discovered at the leg.

The exposure is real and not hypothetical in shape. The `spec tokens (a spec's own names resolve)`
leg in `tools/gate-legs.json` carries NO guard, so it runs on every bar. Clause (a) has no tree-side
form by the register's own note at `.memory-tree.conf:263-265` — "a bar grades one tree, not the
fleet" — so a spec dated 2026-09-14 onward on a node whose branch this tree has not fetched reds the
bar at its merge, unmeasurably from here. §5 risks then affirms that outcome as correct: "a straggler
branch from another node could merge a spec dated on or after the cutoff whose hands-off disagrees
with its sibling. That reds the bar at the merge, which is the join working." That is the sentence
the ruling exists to make false. I scanned every local and remote ref: no LIVE spec outside this
build is dated in the window today, so nothing visible reds — but that is a reading of one tree, and
clause (a) is the clause that reads the fleet.

**Fix.** In §8 F3, add the ruling and the register as cited options: name `TOOL-aJoinedCanon-1`
section 8 F1, `.memory-tree.conf:131-139` and `:252-265`, and the `ACCEPTANCE_LEDGER_CUTOFF`
counter-precedent. Then take one of two routes and say which.

- **Re-derive by the relation.** Compute the value by the register's two clauses at the build commit
  and again at landing, and accept the day-one zero population that the LEGLINE and DIRECT rows each
  state as their cost. The three motivating hits are already fixed, so nothing is lost but the
  retroactive grade. S6 and AC6's above-zero clause must then be re-cut — AC6 would observe the
  arm-on report line and the self-test fixtures rather than a live count — or the unit re-ordered,
  which reopens §8 F4. This route is the run's to take alone.
- **Keep 2026-09-14 as a recorded DEPARTURE.** Take the register's clause (a) reading across every
  local and remote ref and every `git worktree list` worktree, with the three commands the
  `SPEC_DIRECT_CUTOFF` row spells; state the in-flight population it exposes; write the departure and
  its reason into the key's header comment IN PLACE OF the relation, so S3 stops saying "in the idiom
  of `SPEC_LEGLINE_CUTOFF`" for a slot it cannot fill; and rewrite §5 risks so the straggler exposure
  reads as the departure's accepted cost rather than as the join working. Because a fork contradicting
  an owner ruling is not a run's to settle — this spec's own §8 F4 refuses option (c) on exactly that
  ground — this route parks the choice for the owner in `memory/builds/dDerivedDocket/RUN.md`, beside
  the eight decision rows already there.

**Left-shift.** Move the relation assertion out of the `SPEC_DIRECT_CUTOFF` special case and into
`read_cutoff_key` in `tools/check-spec-tokens.py`, so EVERY cutoff key that file reads is asserted
against its own setting commit, not just the one whose build happened to write the check. The
predicate was run over the real tree for this report before proposing it, as charter §7 requires: at
HEAD it reds nothing — `SPEC_LEGLINE_CUTOFF` 2026-09-08 set on 2026-09-07 and `SPEC_DIRECT_CUTOFF`
2026-09-15 set on 2026-09-14 both pass strictly — so it is a zero-false-positive ratchet today. It
would red `SPEC_HANDOFF_CUTOFF="2026-09-14"` at this unit's own commit, which is the point: the gate
turns a silent departure into a refusal a writer must dispose. State in its header what it does not
check, namely clause (a), which has no tree-side form. This is unit-shaped and belongs in its own
unit, not in this one.

## Medium

### M1 — S7's leading deliverable is the checker's docstring, and neither criterion it names reads it (3)

**Address.** §2 S7, first sentence and its closing "Observed by AC8 and AC11"; §6 AC8; §6 AC11.

**What is wrong.** S7 opens "The checker's header docstring gains the fifth join, its population and
its limits", and then loads that docstring with the whole new limits set: consumes-from is not
graded, neither check grades a Tier-1 consumer's edges, an `external` bullet has no sibling, the join
proves a sibling NAMES a token and never that it does the work. S7 closes "Observed by AC8 and AC11".
Neither criterion touches the docstring. AC8 observes `bash skills/session-kickoff/manifest-check.sh`
check 5 and the dossier `memory/map/features/spec-tokens.md` naming five joins. AC11 observes
`wc -c` and `git diff --numstat` over `memory/guides/SESSION-KICKOFF.md`. No section 7 leg reads it
either. The docstring can ship unwritten with every leg green.

**Why it matters more than a doc nit.** That docstring is where charter §7's rule that a gate's own
header states what it does NOT check is discharged for this checker, and the file says so in its own
words at `tools/check-spec-tokens.py:9-10`: "WHAT IT DOES NOT CHECK, stated here because a structural
check reads as a semantic one to everybody who did not write it". At HEAD the header reads "The
fourth join, `bar`, reads two of the three rather than minting a fourth" and enumerates four join
rows — `legs`, `paths`, `cites`, `bar`. Ship the unit with the docstring untouched and the next
reader of the file sees a four-join header in front of a five-join program, with the new join's
limits stated nowhere. That is the false-confidence case the rule exists for, arriving through the
gate that was written to prevent it.

The spec demonstrably knows prose needs an explicit criterion: AC8's own Red-when concedes that the
map freshness leg "grades claims rather than prose" and therefore grades the dossier's five-joins
claim by hand. It grades the parallel docstring claim nowhere while asserting both are observed. It
is also cheap to close the same way, and the spec's own §2 S9 shows the house convention for a
deliverable nobody observes: an explicit NOT OBSERVED line with its reason. This deliverable carries
neither.

**Fix.** Extend AC8 rather than minting a criterion: at this unit's commit, the module docstring of
`tools/check-spec-tokens.py` carries a fifth join row keyed `handoff` beside `legs`, `paths`, `cites`
and `bar`, naming its population — a `**hands-off**` bullet's backticked payload in a LIVE spec dated
at or after `SPEC_HANDOFF_CUTOFF` — and its stated limits, that consumes-from is ungraded and that
naming is not doing the work. Red when: the docstring still describes four joins, so the file's own
header understates what it grades. The rest of AC8 is unchanged, and no arm, no leg and no figure
moves.

**Left-shift.** The tempting gate is a same-file join: every backticked path-shaped token in a §2
scope item must appear in at least one §6 acceptance bullet of the same spec. Both populations are
already parsed by `tools/check-spec-tokens.py`, so it mints no new reader. I ran the candidate
predicate over this build's 39 specs before proposing it, and it does not earn a gate: 207
path-shaped scope tokens, 82 of them absent from section 6, and the sample is mostly correct prose —
glob patterns (`memory/builds/*/BACKLOG.md`), placeholders (`backlog/<FAMILY>.md`) and files named as
context rather than as deliverables. A 40% red rate over correct specs is the same verdict §3 already
records for the S-item citation proxy at 101 unmatched of 214, and for the same reason. So this class
stays a REVIEW check, not a gate, and the honest left-shift is a documented one: add to
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` its sibling form — a scope item
that names an observer which observes a DIFFERENT artefact — and run it at spec-audit time by reading
each "Observed by" list against the named criteria's actual witnesses. The measurement above is the
evidence that the mechanical form was tried and priced, which is what stops the next round proposing
it again.

### M2 — AC5's third state passes on the second state's failure, so the defect its Red-when names ships green (4)

**Address.** §6 AC5, third sentence, against §5 testing and §6 AC7.

**What is wrong.** AC5's three states are cumulative over one scratch repo. §5 testing states it —
"The new arms build one scratch repo per criterion, six for thirteen calls, and a criterion's later
state edits that repo's files in place" — and AC7's distribution confirms AC5 gets three of the
thirteen arm calls ("three for each of the next two", which are §7's fourth and fifth `New arm:`
rows, AC4 and AC5).

State 1 waives `EXMP-tOne-1>EXMP-tOne-2:--frob` and the fixture exits 0. State 2 adds `--frob` to the
second spec, so the waiver goes stale and the checker exits 1 printing `STALE WAIVER`. State 3 then
reads "A third spec's bullet to the second, naming `--frob` unnamed, still exits 1" — but state 2
already left the second spec NAMING `--frob` and the stale waiver row unretired. So the third spec's
bullet produces no handoff hit at all, and the exit 1 the criterion asserts is the state-2 stale
waiver, whatever the waiver keys on.

An implementation that matched on the bare token — the exact defect AC5's Red-when names, "the waiver
matches on the token alone, so one row silences the token in every edge", and the whole point of S5's
`<source uid>><target uid>:<token>` key — passes all three states. State 1 matches and exits 0, state
2 goes stale and exits 1, state 3 rides that same stale hit. The criterion asserts an exit code and
never a key: nothing in it requires the output to name `EXMP-tOne-3>EXMP-tOne-2:--frob`, and nothing
requires the output to be free of `STALE WAIVER`. The arm still counts toward the 55 floor AC10 and
AC7 grade, so the one-row-silences-every-edge class ships with its criterion green.

**Fix.** Make state 3 stand alone. Revert the second spec so it does NOT name `--frob`, add a third
live spec with H1 uid `EXMP-tOne-3` whose hands-off bullet to `EXMP-tOne-2` also names `--frob`, and
assert the checker exits 1 PRINTING the key `EXMP-tOne-3>EXMP-tOne-2:--frob` while the AC1 edge stays
waived. Assert the printed key, not the exit code alone. The arm count does not move, so S8, AC7,
AC10 and §5's cost figures are untouched.

**Left-shift.** This one is cheap and mechanical, and the suite already has the affordance: `arm()`
in `tools/check-spec-tokens.test.sh:52` takes an optional fourth argument, an expected output
substring. Add a suite-shape lint — in `tools/check-testsuite-counts.sh` or as a direct assertion the
suite makes about itself — that every `arm` call expecting rc 1 passes that fourth argument, so a
negative arm can never assert an exit code alone. I ran the predicate over the suite at HEAD before
proposing it: of 38 `arm` calls, 21 expect rc 1 and all 21 already carry an expected substring, so the
ratchet reds nothing today and costs nothing to land. State plainly in its header what it does not
check: it forces a discriminating assertion to EXIST, and cannot force the substring to be the right
one — a builder who passes `STALE WAIVER` at AC5 state 3 still satisfies it. The remaining half is the
review class, "a later state of a cumulative fixture inherits the previous state's failure", which
belongs beside the criterion-asserts-what-its-own-command-cannot-show gotcha.

## Round-1 fixes: what this round found against them

All nine of round 1's distinct defects are folded, and this round found no defect in eight of the
nine fixes.

- **H1**, AC7's witness running nothing, so the floor could stay at 20 while arms landed. Fixed and
  re-fixed at rev-3: AC7 now witnesses with a static `grep -c '^arm "'` against the `FLOOR_ASSERTIONS`
  pin, and new AC10 witnesses the suite's own printed count at the post-build bar. The arithmetic
  reproduces at HEAD — the suite makes 38 `arm` calls with `FLOOR_ASSERTIONS=42` and four direct
  assertions, so 38 plus 13 is AC7's 51 and 51 plus 4 is the 55 AC10 asserts — and AC7's per-row
  distribution sums correctly to thirteen. No finding this round.
- **H2**, built last, grading a population the build has already closed. Fixed: header `order 6`, new
  §4 Rollout, §8 F4, and S6 and AC6 requiring a graded count above zero. The fix is sound on its own
  terms. It is also what forces the cutoff backwards, which is H1 above — the fix moved the unit's
  population into already-written specs and the cutoff rule it had to break did not come with it.
- **H3**, the target resolved by filename where check 12 keys by H1 uid. Fixed: S1, S2, S5 and §4 The
  selection key both ends by H1 uid at any depth, with new AC9 staging a family-less tailed filename
  in a `units` sub-folder. No finding this round.
- **M1**, `grade_handoffs` leading with an undeclared verb. Fixed: §4 Inventory renames to
  `scan_handoffs`, adds `read_spec_uids`, records the `--suggest` answer, and §7 gains
  `lexicon naming predicates`. No finding this round.
- **M2**, S6 and §5 growing a shrink-only registry. Fixed: the waiver route is dropped except under
  an offset rule that retires another row in the same commit, and §3 names the registry high-water
  gate out of scope. The registry header at `memory/project/spec-token-waivers.txt:3-5` confirms the
  shrink-only rule the fold now respects. No finding this round.
- **M3**, no decision about the shipped example carrier. Fixed: new §8 F5 resolves to gov's conf only,
  with a §3 external edge to `TOOL-aJoinedCanon-13`. No finding this round.
- **L1**, every `New arm:` row saying no floor moves while S8 said it rises. Fixed twice — rev-2 gave
  the rows counts, and the closing 2026-09-20 pass rewrote all six third fields in words and MOVED the
  arithmetic to AC7 where a criterion owns it. No finding this round.
- **L2**, the reciprocity claim that check 12 does not make for Tier-1. Fixed: §3 and §8 F2 narrow it
  to Tier-2 specs dated on or after `SPEC_EDGES_CUTOFF` with a producer dated on or after
  `SPEC_HANDOFF_CUTOFF`, and S7 names the remainder. No finding this round.
- **L3**, S1's bullet shape narrower than check 12's. Fixed: §8 F6 takes check 12's accepted shape,
  cited line for line in §4 The selection, so no skipped bullet is left to count. No finding this
  round.

The two mediums this round adds are both in text written after the round-1 record: M1's S7 passage
and its AC11 observer come from the two closing consolidation passes of 2026-09-20, and M2's AC5 sits
against the §5 testing fixture rule the rev-2 third pass wrote. That is consistent with this build's
measured pattern, where the fold text has carried most of the defects. The rate, though, has
collapsed: round 1 found 15 confirmed over 37 raw, this round finds 4 over 18.

## Convergence and disposition

**Convergence** under `memory/guides/BUILD-METHOD.md` M4: confirmed findings fell from 15 to 4,
distinct defects from 9 to 3, the blocker count held at 0, and the high count fell from 3 defects (7
ids) to 1 defect (2 ids). Every count moved strictly down, so by the loop's own measure this subject
has converged again.

**It was already terminal.** `memory/builds/dDerivedDocket/RUN.md` records the round-1 disposition at
2026-09-16T13:42:40Z as `CLEAN WITH FIXES · blockers 0 · CONVERGED`, and M4 says CONVERGED is
terminal for its subject, rev bumps included: a finding confirmed on it afterwards, in the fold text,
takes the severity rule's disposition and never another round. So no G6 round 3 runs on these
findings, whatever their severity, and `.unattended.conf`'s `REVIEW_ROUNDS="1"` says the same from
the other side.

**The disposition by M4's severity rule, and one call belongs to the orchestrator.** M2 and M1 are
MEDIUM and FOLD into the spec as a rev-4 bump with a §9 line; both are paragraph-sized edits with no
new mechanism. H1 is HIGH, which M4 PROMOTES to a unit whose mechanism closes it — but H1's own fold
is a spec edit and, on one of its two routes, an owner question, so promoting it would mint a unit to
carry a date and a header comment. The orchestrator should decide whether H1 takes the FOLD
disposition despite its severity, and record the decision; this record does not make that call for
it. H1's LEFT-SHIFT, unlike H1 itself, IS unit-shaped and should be promoted on its own merits: the
relation assertion widened from `SPEC_DIRECT_CUTOFF` to every cutoff key `tools/check-spec-tokens.py`
reads, measured at zero false positives on this tree.

One ordering note for whoever folds. If H1 is resolved by the first route, re-deriving the value by
the relation, then S6 and AC6's above-zero clause goes with it and §8 F4's order resolution should be
re-read in that light. Fold H1 before M1 and M2, because a re-cut AC6 changes which criteria S7's
carriers hang from.

## Left-shift, by class

1. **A cutoff key that breaks the register's relation, silently** (H1). The mechanical clause-(b)
   assertion exists and is hard-coded to one key. Widening it to every cutoff key
   `tools/check-spec-tokens.py` reads costs nothing at HEAD, measured, and turns this class from a
   review finding into a refusal before grading. Unit-shaped. Its header must state that clause (a),
   the ref-wide reading, has no tree-side form and stays a documented check.
2. **A deliverable whose named observer observes something else** (M1). The mechanical form was
   priced over this build's 39 specs at 82 unmatched of 207 and is too noisy to gate, the same
   verdict §3 already reached for the S-item citation proxy. It stays a review check, recorded as a
   sibling form under `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`. At
   spec-audit time the documented check is to read each "Observed by" list against what those criteria
   actually run.
3. **A cumulative fixture whose later state inherits the earlier state's failure** (M2). Half of it
   gates cheaply: every `arm` call expecting rc 1 passes an expected-output substring, which reds
   nothing at HEAD (21 of 21 already comply). The other half — that the substring discriminates the
   right hit — is a review check, because only the criterion's author knows which hit the state is for.
4. **A fold fix that breaks a rule outside its own spec** (H1, as a class). Round 1's H2 reordered the
   unit and the reorder required a retroactive cutoff; nothing in the fold loop asked what governs
   cutoffs. The documented check for a fold that moves an `order`, a date or a population: re-read the
   register that owns the value the move forces, and cite it in the fork that took it.

## Outside the confirmed set

Three observations came out of re-measuring this spec's claims for this report. None was put to a
skeptic, so none is counted above.

- **§4 Rollout's 81 bullets and §10's 109 are different populations, and the spec does not say so in
  either place.** §4 Rollout measures what S6 grades at this unit's step, when units 1 to 5 have
  closed their specs; §10 measures the whole live tree at `94fd2f54`. Both are plausible and neither
  is wrong, but a reader comparing them finds two counts of "the same" join 28 apart. One clause in
  §10 naming its population would settle it.
- **AC7's `grep -c '^arm "'` is an anchored literal, and the suite's arms all match it today.** I
  re-ran it at HEAD: 38, matching the spec's figure. Worth noting only because the criterion's
  robustness depends on the suite never indenting an `arm` call, which nothing enforces.
- **The `**hands-off** external` edge in §3 is not graded by this unit's own join**, by S1's own skip
  rule. That is consistent and intended, but it means the external edge to `TOOL-aJoinedCanon-13` —
  the one edge this spec declares — is the one edge the mechanism it specifies cannot check. It is
  not a defect; it is worth one sentence in S7's limits paragraph, which M1's fix is already opening.

## What this round did not cover

- Units other than 37 were read only where this report cites them. The sibling specs' own group
  reviews own their text.
- The design record and the owner mandate still contain nothing about unit 37, because the unit
  postdates both. Whether the adoption was right was judged against protocol section 11 alone, as
  round 1 did.
- The self-test suite was not run. The brief holds it for the post-build bar, and every criterion
  that observes it carries a `permission:` line saying so.
- Re-measured at HEAD for this report:
  - the checker's header docstring and its four join rows (`tools/check-spec-tokens.py:1-58`) (M1);
  - the dossier's title and its four-joins prose (`memory/map/features/spec-tokens.md:5`, `:49`) (M1);
  - the cutoff relation as recorded (`.memory-tree.conf:131-139`, `:239`, `:252-265`) and as asserted
    (`tools/check-spec-tokens.py:294-320`), plus the pickaxe readings for both live keys (H1);
  - the `spec tokens` leg's absent guard and the `spec-tokens self-test` leg's 300 s ceiling in
    `tools/gate-legs.json` (H1, AC10);
  - the suite's 38 `arm` calls, its `FLOOR_ASSERTIONS=42`, the `arm()` signature at `:52` and the
    21-of-21 rc-1 substring compliance (M2, the round-1 H1 fix);
  - the scope-token-versus-section-6 candidate predicate over this build's 39 specs (M1's left-shift);
  - the waiver registry's shrink-only header (the round-1 M2 fix);
  - `SPEC_HANDOFF_CUTOFF`'s occurrences across `memory/` and `tools/`, which are this spec and this
    group's round-1 record and nothing else (H1);
  - `memory/builds/dDerivedDocket/RUN.md`'s eight parked decision rows and its G6 CONVERGED row
    (Convergence and disposition).
