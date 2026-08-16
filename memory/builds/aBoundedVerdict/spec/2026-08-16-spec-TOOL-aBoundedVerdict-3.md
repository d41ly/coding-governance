# TOOL-aBoundedVerdict-3 — every remaining place a run would wait for the owner gets a disposition

**Status:** OPEN · rev-3 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

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

`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` ·
`tools/memory-tree/README.md`, receiving the displaced paragraph ·
`tools/unattended/SKILL.template.md` and the rendered Skill · possibly `memory/TEMPLATE-SPEC.md`'s
open-questions section, for the fact-question mark · `memory/gotchas/vacuous-selector-empty-population.md`
if §8's F4 is taken · `memory/guides/SESSION-KICKOFF.md` (the manifest re-stamp; the method and the
kickoff engine are both on its watch list) · the kit version constants for whichever kits move, and
their marker files.

### The method document's size budget — measured, and not what rev-1 said

Rev-1 called this "the largest displacement demand of any unit in this build" against the wrong
instrument. Measured at base: `memory/guides/BUILD-METHOD.md` is 236 lines and 16466 bytes against a
gated cap of 61440 bytes and 750 lines for a `memory/guides/` file — 31% of the cap. The 20 KB and
250-line figures are the method's own line-8 self-declaration, which no gate reads for a guide.

The displacement obligation is therefore EDITORIAL — M1's growth rule, machine-checked by nothing —
and it is real for that reason and not because a gate would catch it. S2, S4, S5 and S6 are four
rules and will not fit in the 14 lines M1's own budget leaves, so the displacement is identified and
made in the same commit.

The MECHANICAL budget is the charter read-path ceiling: 70262 bytes measured against 86476, so
**16214 bytes of headroom**. This unit spends from it twice, growing both the method and the
unattended protocol, and it is not the only spender — the full set is stated ONCE in the build
README's cross-unit rules rather than in each spec, because two specs each naming the total and each
other is how a shared budget gets spent twice. The builder re-measures with the corpus reporter
before spending.

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
- **AC7** — When the kickoff engine is unchanged, `bash tools/unattended/check-unattended.sh` still
  finds at least the declared floor of interactive exits.
- **AC8** — `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

`tools/unattended/check-unattended.sh` and its two siblings ·
`tools/unattended/adopt-unattended.sh --check` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/kit-dogfood-parity.test.sh` · `tools/memory-tree/check-method-carriers.sh` ·
`tools/check-kit-versions.sh` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — does S1's reading of the authorization need the owner's ratification?** It concludes that
  committing a build folder approves the scope of every spec inside it, which is a widening of what
  the grant is read to mean even though it creates no new grant. Options: ratify it explicitly, the
  way the four costs of the current grant were ratified; treat it as already covered by the
  class-wide grant; or narrow it, so only a spec at a status past awaiting-approval counts as
  approved, which reintroduces the deadlock §4 rejects. Recommendation: put it to the owner as a
  named cost, in the same shape the protocol's existing cost list uses.
- **F2 — where does the fact-question mark live in a spec?** Options: a prefix on the fork's own
  bullet, which puts it where the resolution mark already goes and where another unit in this build
  is hardening the predicate; or a separate sub-head. Recommendation: the bullet prefix, and it is
  worth coordinating with that unit so one predicate reads both marks.
- **F3 — is S3's "every remaining unit depends on it" test derivable?** Nothing in the tree records
  inter-unit dependencies; the build README's authored order carries them in prose. Options: leave
  the test to the run's judgment, which is what every other ordering decision already is; or add a
  dependency field to the README front matter, which is a new mechanism and belongs to its own unit.
  Recommendation: judgment, and a backlog row for the field.
- **F4 — does `memory/gotchas/vacuous-selector-empty-population.md` gain an anchor naming the build
  method?** Without one, the counter-rule S6 writes is prose no checklist ever surfaces to a reviewer
  touching the method. With one, every future diff touching the method carries that class. Options:
  add the anchor, which is one backticked path in the record's body and puts the record in this
  unit's Files touched; or leave it, and rely on the rule being read in the method itself where it
  binds. Recommendation: add it — the record already fires for the hygiene gate, and the method is
  where the rule now lives.

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
