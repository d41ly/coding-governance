# TOOL-aBoundedVerdict-3 — every remaining place a run would wait for the owner gets a disposition

**Status:** SPECCED · rev-8 · 2026-08-20 · node c · Tier-2 · base 098bebd9 · streams tooling · ratified 2026-08-17

## 1. Goal

The kickoff engine gives each of its six interactive exits a no-owner-turn disposition, but three
places a run reaches AFTER kickoff have none: a unit whose status says it awaits owner scope
approval, a fork whose only surviving option trips the method's second or third veto, and a fork
that is a plain question of fact. Give each one a stated disposition, so a run that meets them
proceeds, parks or halts rather than stopping with nothing written.

## 2. Scope (IN)

- **S1** — a disposition for the awaiting-approval status, in three cases. A unit whose spec is
  REACHABLE from the run's pinned base carries the same owner act that authorized the run, and is
  treated as scope-approved by it. A unit whose spec the run itself authored is governed by the
  method's existing authoring rule and is not awaiting anything. A unit present at base under a
  status naming an EXTERNAL PREREQUISITE halts with the external-prerequisite halt code — NOT the
  awaiting-approval one, whose owner turn is to approve or amend scope and which would tell a
  returning owner to do the wrong thing. `TOOL-aBoundedVerdict-2` carries that member and lands
  first.
- **S2** — the method's fork section states the collapse its own text already implies but never
  spells: under a mandate, a fork whose only surviving option trips the second or third veto has no
  delegated resolver, so the sentence that follows applies and it is parked. Today a reader reaches
  "these are owner turns" and stops, and the park sentence is a line further on about a different
  condition.
- **S3** — a fork that is parked because no resolver exists is parked through the park verb, and the
  run continues with the units that do not depend on it. When every remaining unit depends on it, the
  run halts with the fork-unresolvable halt code.
- **S4** — a declared FACT-QUESTION subclass of fork, and the procedure for resolving one without an
  owner: the spec must name the probe, the observation that decides it, and a liveness assertion
  showing the probe can produce a negative result. The winner is taken from the observation only when
  it falls out with no further judgment; otherwise the fork is not a fact question and S2 governs.
  **The MARK that flags such a fork in a spec's §8 is not defined here.** Its grammar is
  `TOOL-aBoundedVerdict-4`'s, spelled in that unit's own scope and its single case table beside the
  resolution mark, because that unit owns the predicate that has to read both. This spec CITES it and
  restates nothing: F2 resolved the placement to the bullet prefix, -4 lands earlier in the dependency
  order so the definition exists before this unit's rule refers to it, and a mark defined in two
  documents is exactly the drift the method's pointer rule exists to prevent.
- **S5** — the bound on probing. A probe reads and measures over artifacts that already exist. It
  does NOT build an arm of the fork, for two stated reasons: building an arm is not one of the
  method's five pass kinds, so it inherits no commit, regrounding or gate discipline; and it puts
  code before fork resolution, which the method's own words call a rewrite rather than a decision.
- **S6** — the counter-rule, because the evidence demands it: an observation that decides a fork by
  making a signal read zero is refused by name, on this repo's own vacuous-selector class. One of
  the corpus's forty-six real forks was deliberately resolved AGAINST the better measurement for
  exactly that reason, and a testing rule that did not carry the exception would have got it wrong.
- **S7** — the carriers. S1 and S3 are the unattended protocol's; S2, S4, S5 and S6 are the method's
  fork section. Neither restates the other, and the method's pointer rule decides which side each
  sentence lands on.
- **S8** — the protocol's list of costs the build-folder grant carries gains a FIFTH entry, in that
  list's own shape: a spec reachable at the pinned base is scope-approved by the same act, so an
  owner who commits a build folder holding a spec they deliberately left unapproved has approved it.
  Ratified by the owner on 2026-08-17 (§8 F1). The list exists so a widening lands on the record
  rather than in a reader's inference, and this is the first entry added to it since it was written.

## 3. Non-goals (OUT)

- **No general rule that a fork is resolved by testing.** Of forty-six resolved forks read in full
  across ten specs, three were decidable by a mechanical test alone and about sixty-seven percent are
  not testable at all — they turn on placement, severity, thresholds, document authority, scope and
  product judgment. The owner chose the narrow subclass over the general rule on that measurement.
- No new pass kind, no built arm, no wall-clock or token budget for probing. S5 forbids the case a
  budget would have bounded, which removes the need for the budget.
- No change to the vetoes themselves, to what they cover, or to the ratify rule's ordering. This unit
  states the consequence of a veto firing under a mandate; it does not move the veto.
- No seventh kickoff exit. The three sites here are reached during the build, not at kickoff, so the
  engine's enumeration and its shrink-only floor are untouched.
- No change to what the authorization grants. S1 reads the existing class-wide grant to its
  conclusion; it does not widen it.

## 4. Design

### The awaiting-approval hole, measured

The playbook's Definition of Ready requires scope approval before building. The status token meaning
"complete, awaiting owner scope approval" is defined in the spec-format document. Neither the phrase
nor the token appears anywhere in the five carriers an unattended run reads, and the planning verb
branches on the status token in exactly one place — for the two terminal tokens — so a unit awaiting
an approval that will never arrive prints as ready to build. The run therefore either builds an
unapproved unit or stops with no rule telling it to.

S1 resolves it by reading the authorization the run already has. The build folder committed before
the run's branch existed is the owner's act; a spec inside it, reachable at the pinned base, is part
of that same act. The protocol already records that this grant is class-wide and that the narrowing
is the slug the owner typed — S1 is that property applied to one more question, not a new grant.

The residual cost is real and is named rather than hidden: an owner who commits a build folder
containing a spec they deliberately left unapproved has approved it under this rule. That is the same
cost the protocol already accepted and documented for the grant as a whole, and §8 carries it as a
fork rather than burying it here.

### Alternatives rejected

- **A fifth classification state in the method's decompose section.** The classification vocabulary
  is the method's and the planning verb computes it, so a fifth state is one method edit and one verb
  edit — cheap. Rejected because it deadlocks the run it is meant to unblock: the method requires a
  run to author a missing spec, an authored spec that is complete is written at exactly this status,
  and a fifth state that halts on it would halt every run that authored anything.
- **Treat the awaiting-approval status as a halt unconditionally.** Same deadlock, reached faster.
- **A conf key naming which statuses the mandate approves.** A project-level answer to a question
  that is about what an authorization MEANS, not about how a project spells things. Rejected on the
  kit's own rule for what belongs in a declaration.
- **A general testing rule with a token or wall-clock budget.** Rejected by the owner on the
  three-of-forty-six measurement. The budget would also have been unmeasurable: a discarded arm
  commits nothing, so no counter reading the repository could ever see the spend.
- **Leaving the veto collapse implicit.** The park sentence exists and the disposition is technically
  derivable. Rejected because the research read it wrongly on the first pass and had to be corrected
  by a skeptic — a rule two careful readers disagree about is not stated.

### Inventory

| Site | Today | After |
|---|---|---|
| a unit awaiting owner scope approval | no rule in any carrier; planning verb prints it ready | approved by the mandate when reachable at base; otherwise a halt with a named code |
| a fork tripping veto two or three | "these are owner turns", with the park sentence a line away about another condition | explicitly parked, through the park verb |
| a parked fork the rest of the build needs | nothing | the run halts with a named code |
| a fork that is a plain fact question | no procedure | probe, liveness assertion, resolve on the observation |
| a probe that decides by making a signal read zero | nothing | refused by name |

### Files touched (estimate)

- `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` — S1, S3 and S8.
- `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` — S2, S4, S5, S6.
- `tools/memory-tree/README.md` — receives the displaced paragraph.
- `tools/unattended/SKILL.template.md` and the rendered `.claude/skills/unattended/SKILL.md`.
- `memory/gotchas/vacuous-selector-empty-population.md` — the method anchor, no longer conditional:
  §8's F4 is RESOLVED to ADD it.
- `memory/backlog/TOOL.md` — the dependency-field row §8's F3 defers to a backlog row rather than a
  scope item. F3 resolves to judgment plus that row, so the row is part of this unit's landing commit
  and the file belongs in this list.
- `memory/guides/SESSION-KICKOFF.md` — the manifest is re-stamped in the same commit, because
  `memory/guides/BUILD-METHOD.md` is on its watch list.
- The kit version bump for each kit that moves, enumerated rather than named: for the unattended kit
  the constant AND its same-line `gov:kit` marker in both `tools/unattended/unattended.sh` and
  `tools/unattended/check-unattended.sh`, the marker in every tracked
  `tools/unattended/*.template.md`, and the re-render; for the memory-tree kit the same shape over its
  own constant and every tracked `tools/memory-tree/*.template.md`, which is a DERIVED population and
  includes templates this unit does not otherwise edit. `tools/check-kit-versions.sh` pairs all of
  them, and naming one file is one carrier short of what it forces.

`memory/TEMPLATE-SPEC.md` is NOT in this list. Rev-8 removes it: the fact-question mark's grammar is
`TOOL-aBoundedVerdict-4`'s (S4), so the spec-format document is that unit's carrier to edit, and two
units writing one definition is the drift both are trying to avoid.

### The method document's size budget — read at build time, carried here as an obligation

Rev-1 called this "the largest displacement demand of any unit in this build" against the wrong
instrument. Rev-2 fixed the instrument and introduced a worse defect: a SNAPSHOT. Its line count and
byte count were exact when written, went stale inside four days, and disagreed with a sibling spec
measuring the SAME tree at the same commit — two specs, one file, two answers. Rev-8 deletes every
figure from this section. Two instruments bind and neither one is spelled in this spec:

- **The method's OWN declared cap**, stated in its M1 section. It is the STRICTER of the two and it is
  the one that binds this unit. Read the live pair and the cap together, at build time:
  `wc -lc memory/guides/BUILD-METHOD.md` and M1's own budget line.
- The hygiene gate's cap for any file under `memory/guides/`, declared in `.memory-tree.conf`. Far
  looser, and not the constraint here.

Two consequences, and both are obligations rather than numbers. **The displacement is MANDATORY.**
The headroom against the method's own cap is now a handful of lines, S2, S4, S5 and S6 are four
rules, and no arithmetic makes four rules fit in a handful of lines — so the paragraph to displace is
identified and moved in the SAME commit, which is what AC5 observes. **Raising that cap is not this
unit's to take.** It is a stated constraint of a governance carrier, which M3's veto 2 makes an owner
turn, and M1 itself records that the last raise was exactly that. A run that finds the displacement
insufficient parks the shortfall; it does not edit the cap.

The MECHANICAL budget is the charter read-path ceiling, and this spec carries no figure for that
either. Rev-6 removed a total measured against a ceiling that has since been retired — a number that
was true once and then quietly stopped being, which is the exact failure mode the "stated ONCE" rule
exists to prevent, reproduced by a spec that stated the rule. The live pair comes from
`python tools/memory-tree/corpus_ids.py --report`, read before spending. This unit spends from it
twice, growing both the method and the unattended protocol; the spender SET is the build README's and
is not counted here.

## 5. Production-readiness checklist

- security — S1 reads an authorization to a further conclusion. The conclusion is stated, the
  residual is named in §4 and forked in §8, and no new grant is created.
- perf / scale — N/A. Document rules; the one machine touch is a reachability check the driver
  already performs for the authorization.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a unit at a status naming an external prerequisite, a fork with no
  surviving option, and a probe that cannot produce a negative result are three distinct outcomes
  with three distinct dispositions.
- observability — every disposition writes something: a park entry, a halt code, or a resolution mark
  in the spec naming the resolver and the authority. A disposition that wrote nothing would be
  indistinguishable from a run that forgot.
- risks — the largest is S1's residual, which widens what the mandate is read to approve. Second is
  that S4 is a rule an agent follows rather than a machine enforces, so a run can call any fork a
  fact question; the mitigation is that the spec must NAME the probe and its liveness assertion,
  which leaves the claim on the record where a review can refute it.
- testing + left-shift gates — none of this is machine-checkable, and the spec says so rather than
  inventing a gate. The left-shift is the resolution mark's attribution shape, which another unit in
  this build makes enforceable.
- migration / rollback — no on-disk migration. Rollback is reverting the prose, and no artifact
  written under these rules becomes unreadable.
- user docs — the protocol, the method and the rendered Skill, all three under parity gates.

## 6. Acceptance criteria

- **AC1** — When the protocol is read, it states the disposition for a unit at the
  awaiting-approval status in all three cases §2 enumerates, and
  `bash tools/unattended/adopt-unattended.sh --check` reports the installed protocol in sync with
  `tools/unattended/PROTOCOL.template.md`.
- **AC1a** — When the protocol pair is read after S8's edit, the build-folder grant's cost list
  carries the new entry — a spec reachable at the pinned base is scope-approved by the same act — in
  BOTH `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md`, in that
  list's own shape; the list's entry count is exactly ONE higher than the same list at the pinned
  base, both counted at build time rather than compared against a figure written here; and
  `bash tools/unattended/check-unattended.sh` check 10, the protocol byte-diff, reports the two halves
  identical. Without the count arm the criterion passes on an edit that merely rewords an
  existing entry. S8 is the one item in this unit the owner explicitly ratified (§8 F1) and rev-7 left
  it with nothing observing it at all.
- **AC2** — When the method's fork section is read, the collapse for vetoes two and three is stated
  in the same paragraph as the vetoes, and `bash tools/memory-tree/kit-dogfood-parity.test.sh` is
  green.
- **AC3** — When the fork section of `memory/guides/BUILD-METHOD.md` is read, the fact-question
  subclass names its three requirements — the probe, the deciding observation, and the liveness
  assertion — and states the built-arm prohibition with its two reasons.
- **AC4** — When the fork section of `memory/guides/BUILD-METHOD.md` is read, the vacuous-selector
  counter-rule is stated and cites `memory/gotchas/vacuous-selector-empty-population.md` by path.
  The observation is that citation, NOT a gotchas run: a record's anchors are derived from the
  backticked tokens in its OWN body, that record's tokens name the hygiene gate and its adopter, and
  the class is not universal — so `gotchas.py --for-paths` over the method resolves it neither before
  nor after this unit, and rev-1's criterion was unsatisfiable by any edit in scope. Giving the
  record a method anchor is a separate decision, changing what every future diff touching the method
  is checklisted for, and it is §8's F4.
- **AC5** — When the method file is measured after the additions, its line count is no higher than
  before, the displaced paragraph is absent from `memory/guides/BUILD-METHOD.md` and present in
  `tools/memory-tree/README.md`, and `python tools/memory-tree/corpus_ids.py --report` shows the read
  path still under its ceiling.
- **AC6** — When the run-state file, the protocol and the method are cross-read, no rule in this
  unit appears in two of them. The observation is a literal grep: the sentence stating the veto
  collapse appears in `memory/guides/BUILD-METHOD.md` and is absent from
  `memory/guides/UNATTENDED-PROTOCOL.md`, and the sentence stating the awaiting-approval disposition
  is present in the protocol and absent from the method. `bash tools/memory-tree/check-method-carriers.sh`
  stays in §7 because the Skill template and its render are declared carriers, but it CANNOT witness
  this criterion — its population loop skips every tracked path under the memory root, which is where
  all three carriers live, and its own header states it is structural only.
- **AC7** — When the three dispositions are read back, each one is written in the protocol or the
  method per S7, and NONE of them appears in the kickoff engine's enumeration of interactive exits —
  so the engine's exit floor is unchanged for the STATED reason §3 gives (no seventh exit; the three
  sites are reached during the build, not at kickoff) rather than by accident, and
  `bash tools/unattended/check-unattended.sh` still finds at least that floor. Rev-8 replaced the old
  AC7, which asserted only the second half: it was green today, green on an empty diff, and green on a
  wrong implementation of S1–S8, because this unit changes no kickoff exit and the engine is not in
  Files touched. The absence half is what makes the arm distinguish this unit's work from no work.
- **AC8** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is green.

## 7. Gates

`tools/unattended/check-unattended.sh` and its two siblings ·
`tools/unattended/adopt-unattended.sh --check` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/kit-dogfood-parity.test.sh` · `tools/memory-tree/check-method-carriers.sh` ·
`tools/check-kit-versions.sh` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — does S1's reading of the authorization need the owner's ratification?** It concludes that
  committing a build folder approves the scope of every spec inside it, which is a widening of what
  the grant is read to mean even though it creates no new grant. Options: ratify it explicitly, the
  way the four costs of the current grant were ratified; treat it as already covered by the
  class-wide grant; or narrow it, so only a spec at a status past awaiting-approval counts as
  approved, which reintroduces the deadlock §4 rejects. **RESOLVED (owner, 2026-08-17): ratify it as
  a named cost.** S8 below carries the consequence: the reading joins the protocol's existing list of
  costs the build-folder grant already carries, as a fifth entry, in that list's own shape. Narrowing
  was refused because it reinstates the deadlock — the method requires a run to author a missing spec,
  and an authored complete spec is written at exactly this status.
- **F2 — where does the fact-question mark live in a spec?** Options: a prefix on the fork's own
  bullet, which puts it where the resolution mark already goes and where another unit in this build
  is hardening the predicate; or a separate sub-head. Recommendation: the bullet prefix, and it is
  worth coordinating with that unit so one predicate reads both marks.
  RESOLVED (agent, 2026-08-20, delegated): the BULLET PREFIX, and the coordination is a hard
  constraint rather than an aspiration — `TOOL-aBoundedVerdict-4` hardens the §8 predicate in this
  same build, so a mark it does not recognise turns a fact-question into an unresolved fork and
  blocks the spec from ever going terminal. Mechanism-only; the sub-head option costs a second
  place for a reader to look for one answer.
- **F3 — is S3's "every remaining unit depends on it" test derivable?** Nothing in the tree records
  inter-unit dependencies; the build README's authored order carries them in prose. Options: leave
  the test to the run's judgment, which is what every other ordering decision already is; or add a
  dependency field to the README front matter, which is a new mechanism and belongs to its own unit.
  Recommendation: judgment, and a backlog row for the field.
  RESOLVED (agent, 2026-08-20, delegated): JUDGMENT, with the dependency field filed as a backlog
  row this unit writes. Mechanism-only. The richer option is discarded by veto 2 — a dependency
  field in the README front matter is a new mechanism in a schema the generator and two legs read,
  which is its own unit and not a clause inside this one.
- **F4 — does `memory/gotchas/vacuous-selector-empty-population.md` gain an anchor naming the build
  method?** Without one, the counter-rule S6 writes is prose no checklist ever surfaces to a reviewer
  touching the method. With one, every future diff touching the method carries that class. Options:
  add the anchor, which is one backticked path in the record's body and puts the record in this
  unit's Files touched; or leave it, and rely on the rule being read in the method itself where it
  binds. Recommendation: add it — the record already fires for the hygiene gate, and the method is
  where the rule now lives.
  RESOLVED (agent, 2026-08-20, delegated): ADD the anchor. Mechanism-only and the feature-rich
  survivor: one backticked path puts the class on the checklist of every future diff touching the
  method, which is the whole left-shift this repo asks of a confirmed finding. The alternative
  leaves the counter-rule as prose no checklist surfaces.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Records that the fact-question subclass is the owner's chosen
  narrowing of a general testing rule, taken on the three-of-forty-six measurement, so §3's first
  non-goal is a decision rather than a scope omission.
- rev-2 · 2026-08-16 · folded the M4 spec audit's first round. No blocker; the rules themselves
  survived verification and the two highs were acceptance criteria that certify nothing. AC4 named a
  gotchas run that resolves the class neither before nor after this unit, because a record's anchors
  come from its own body — the observation is now the citation, and giving the record a method anchor
  becomes F4. AC6 named a gate whose population loop skips every path the three carriers live under
  and whose own header says it is structural only — the observation is now a literal grep, and the
  gate stays in §7 for the write set it does reach. The size-budget paragraph and AC5 measured the
  method against a self-declaration no gate reads; both are restated on the gated cap and the
  read-path headroom, with the share this unit spends named against the other unit that spends it.
  S1's third case routed an externally-blocked unit into the scope-approval code, whose owner turn is
  the wrong one; it now names the member `TOOL-aBoundedVerdict-2` adds for it.
- rev-3 · 2026-08-16 · folded round 2. No finding landed against this unit's rules. The read-path
  paragraph named itself and one sibling as the budget's only spenders when there are four; the
  spender set moves to the build README so it is stated once, and this spec names only its own
  double share. `TOOL-aBoundedVerdict-2`'s awaiting-approval member was narrowed in the same round to
  the residual S1's three cases leave, so the two now cite each other in both directions.

- rev-4 · 2026-08-17 · §8 F1 RESOLVED by the owner: the reading that a spec reachable at the pinned
  base is scope-approved by the same act that authorized the run is RATIFIED as a named cost, and S8
  is added to carry it into the protocol's existing cost list as a fifth entry. Narrowing was refused
  because it reinstates the deadlock §4 rejects.
- rev-5 · 2026-08-17 · M7 REGROUND onto the new merge base. One claim moved: the read-path headroom
  is 14354 B, not 16214, because the unattended protocol grew 1103 B under this spec. No rule in this
  unit was affected.
- rev-6 · 2026-08-19 · re-read against the close-path audit and `TOOL-aBoundedVerdict-1` rev-6. **No
  scope item changes**, and that is the finding rather than an omission: the three dispositions here are
  about FORKS and STATUSES, and S3's "continue with the units that do not depend on it" test is
  meaningful at a fork in a way it was not at the closing review — which is exactly why the audit's
  medium 25 landed on unit 1's S8 and not here. Two cross-references added by this rev, both to
  mechanisms this unit's dispositions now depend on and neither of which existed when it was ratified:
  the HALT disposition reaches `--abort`, which requires both agent-attested keys first, and those keys
  have no writer until `TOOL-aBoundedVerdict-15`'s `--attest` verb lands — so this unit's halt path is
  reachable only by a hand-edit today, and that dependency is named rather than assumed. And the review
  side of "a thing the run cannot resolve" is now `TOOL-aBoundedVerdict-1` S9's park case, which is this
  unit's rule applied to a blocker; the two must stay phrased as a SCOPE test rather than a difficulty
  test, or both become an escape from ordinary work.

- rev-7 · 2026-08-20 · M3 fork sweep, before any code. F2, F3 and F4 RESOLVED under the delegated
  rule. F3's richer option — a dependency field in the README front matter — was discarded by veto 2
  as a new mechanism in a schema other readers share, and survives as the backlog row this unit
  writes. F2's resolution is recorded as a CONSTRAINT on `TOOL-aBoundedVerdict-4` rather than a
  preference: the two units share one predicate and a mark it cannot read is a spec that never goes
  terminal. §8's first non-blank line is now the machine-legal `none` form.

- rev-8 · 2026-08-20 · folded the M4 spec audit's second round: H7, H18, M7, M8.
  **H7 — the size section was a snapshot, and it had gone stale twice.** "236 lines and 16466 bytes"
  was a retired base's measurement; the same tree measured at the DECLARED base gave a different pair,
  which the sibling spec states, so two specs in one build disagreed about one file. The derived "14
  lines M1's own budget leaves" reproduced in NO era — not at the retired base, not at the declared
  one, not at HEAD. Every figure is deleted and replaced by the commands that produce them
  (`wc -lc memory/guides/BUILD-METHOD.md` plus M1's own budget line, and
  `python tools/memory-tree/corpus_ids.py --report` for the read path). The section also had the
  binding instrument WRONG: it argued the displacement was merely editorial because no gate reads the
  method's self-declaration, when that declaration is the stricter of the two caps and is what binds
  this unit. It is now stated as two obligations instead: the displacement is MANDATORY, because the
  headroom is a handful of lines against four new rules, and raising the cap is an OWNER TURN under
  M3's veto 2 — a run short on room parks the shortfall rather than editing a governance carrier's
  stated constraint. The "one of seven spenders" count went with the rest; the spender set is the
  README's.
  **H7's second half — D4.** S4 now CITES `TOOL-aBoundedVerdict-4`'s FACT-QUESTION mark grammar
  instead of leaving it undefined or restating it, and the dependency points forwards to the unit built
  earlier. `memory/TEMPLATE-SPEC.md` is REMOVED from Files touched as the consequence: the mark's
  definition is -4's carrier, and two units writing one definition is the drift F2's coordination
  exists to prevent.
  **M7** — S8, the only item here the owner explicitly ratified, had no acceptance criterion at all.
  AC1a observes it: the new entry present in BOTH protocol halves, the list's entry count exactly one
  higher than at the pinned base (counted at build time, no figure written into the spec), and the
  byte-diff clean. The count arm is the load-bearing half — without it a reworded existing entry
  passes.
  **M8** — AC7 was green before any work: it passed today, on an empty diff, and on a wrong
  implementation of S1–S8. Taken the REPLACE branch rather than the DELETE one, because replacing
  widens nothing — the new arm observes files already in the write set plus a read-only absence in the
  engine — while deleting would drop the only observation that §3's no-seventh-exit non-goal held. AC7
  now asserts the three dispositions are written in the protocol or the method and are NOT enumerated
  as kickoff exits, so an unchanged floor means something.
  **H18** — `memory/backlog/TOOL.md` was committed to by §8's F3 and declared in no list; it is in
  Files touched now, along with the F4 anchor that stopped being conditional when the sweep resolved
  it, and the kit version bump enumerated by site rather than abbreviated to "the kit version
  constants".

- rev-8 · 2026-08-20 · **built, and the displacement this unit needed is DONE rather than deferred.**
  The method was at 283 of its own 290-line cap with four paragraphs to add, and a cap raise is an
  owner turn under M3 veto 2 — so M12's PROCEDURE moved to the memory-tree kit's README, into the
  displaced-sections home that already held M5's probe taxonomy. What stayed in M12 is what changes
  what an agent does next: what the section is for, that it adds no pass kind, and M3's limit on the
  run's authority. The justification is the method's OWN budget rationale — it is re-read whole at
  every pass boundary, so rarely-reached procedure is exactly what displacement is for, and M12 is
  reached only by a prompt-authorized run that found no seam. Method 283 -> 270 lines before the
  additions, 290 after; read path 108505 -> 107524 B.
  **S2's collapse is the rule I had to derive by hand two passes earlier.** Resolving
  `TOOL-aBoundedVerdict-21` F3 required knowing that a veto leaving ONE survivor is not a licence to
  take the vetoed option — and the method said "vetoes 2 and 3 are owner turns" three lines above a
  park sentence about a different condition. I reasoned it through and recorded the reasoning; now the
  method states it, so the next run does not have to. That is the whole content of this scope item and
  it was worth more than the two lines it costs.
  **S4 CITES the fact-question grammar rather than spelling it**, per the build decision that the unit
  owning the predicate owns the grammar — and the citation is a PARAPHRASE, not an id: the method's
  template lives under `tools/`, so a non-terminal spec id there would take the citation drift signal
  from 2 to 3 and break a shrink-only pin. That is the third time this run that writing a comment
  about a unit nearly cited the unit.
  **S8's fifth cost is stated in the list's own shape**, with the refused alternative and its reason:
  narrowing scope-approval to a status past awaiting-approval deadlocks, because the method requires a
  run to author a missing spec and an authored complete spec is written at exactly that status — a run
  would author a unit it could then never build.
  Not in scope and not done: no new gate. S1, S3 and S8 are protocol prose; S2, S4, S5 and S6 are the
  method's. The carriers split exactly as S7 says.

## 10. Reuse audit

`python tools/memory-recall/query.py` over the fork and owner-turn question returns the decision that
the mandate buys exactly one of the kickoff engine's six interactive exits and that the rest resolve
by aborting or parking — which is the precedent S1 through S3 extend to three sites the engine does
not cover. The seams reused are the authorization reachability check, which S1 reads rather than
re-implements, and the park verb another unit in this build supplies. No new machinery is created
here at all: this unit is entirely rules, and its one machine dependency is a check that already
runs.

Recall terms used, recorded for the reground: fork veto owner turn park disposition scope approval
SPECCED mandate reachable base fact question probe liveness vacuous selector.
