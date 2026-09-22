# TOOL-dScriptedRepeat-11 — authoring a playbook: creation, and owner-instructed amendment

**Status:** CLOSED · rev-6 · 2026-08-21 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md](../build/2026-08-21-build-TOOL-dScriptedRepeat-5-11-acceptance-ledger.md) | journal | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 |
| [2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md](../reviews/2026-08-21-review-TOOL-dScriptedRepeat-5-diff-round1.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round2.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round3.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round4.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round5.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 |
| [2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md](../reviews/2026-08-22-review-TOOL-dScriptedRepeat-5-diff-round6.md) | diff-review | TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 |

<!-- /gen:spec-records -->

## 1. Goal

Own the owner's FIRST stated verb — with no playbook, research the topic and the code it must relate
to, then spec and create one from the template — as a `prompt`-mode run that produces a playbook, and
give owner-instructed AMENDMENT the same home.

## 2. Scope (IN)

- **S1.** THE CREATION PATH is a `prompt`-mode run, not a `recipe`-mode one. It has no `playbook:` to
  name, so unit 4's preflight would refuse it; and its diff is entirely outside any declared output
  glob, so unit 8 would red it. Both refusals are correct — a run that MAKES a playbook is not a run
  that FOLLOWS one, and the mode set already carries the right member for research-then-author work.
- **S2.** THE LOOP is the build method's research→test→choose section, which `prompt` mode's two scoped
  directives already bind. No new method section and no new directive: the obligation exists, the
  pointer exists, and the mode that carries it exists. This unit's contribution is stating that a
  playbook is the ARTIFACT that loop produces, not a new discipline for producing it.
- **S3.** THE OUTPUT is a playbook conforming to unit 2's canon and unit 3's gate, committed to the
  tree. Unit 3's leg grades it from the moment it is tracked, so a playbook that does not validate
  cannot land — which is what makes a later run's `playbook:` reference safe without re-validating.
- **S4.** THE ORDERING PROPERTY, QUALIFIED BY ANCHOR, and it is the reason this is a separate run
  rather than a first pass of a playbook run. The playbook must be OLDER than the BASE of any run that
  names it. **Under `default-branch` this has a machine half** — unit 4's first refusal fires, because
  the BASE is a merge-base the run cannot move. **Under `published` it does not**, and this repo
  declares `published`: there the BASE is a tip the run itself pushed, so a create-and-follow run
  resolves its own `playbook:` and unit 4's refusal never fires. Under that anchor S4 is a documented
  CHECK with no machine half, stated the way unit 10 S5 states the attended path's. The real backstop
  there is a DIFFERENT mechanism and worth naming: unit 8 no longer exempts the playbook, so a
  `recipe`-mode run editing or creating one REDS on the unattended path. A creation run
  commits and lands the playbook; a later run's build README names it and resolves it at that run's
  own BASE. A single run that authored its playbook and then followed it would be authorizing its own
  instructions, which is the property unit 8's refusal and unit 9 §3 both exist to prevent.
- **S5.** AMENDMENT rides the same path. Fork 6's proposals accumulate on the run-state file of the
  runs that discovered them; acting on them is an owner-instructed `prompt`-mode run that reads the
  surfaced proposals, edits the playbook, and lands it. Unit 8's exemption set therefore does NOT need
  the playbook in it, and unit 9's prohibition on a run editing its own checklist holds without an
  exception.
- **S6.** THE SKILL SECTION, in unit 10's S0 routing preamble: a reader arriving with no playbook is
  routed here rather than into a preflight that will refuse them.
- **S7.** Arms: a creation run's diff is NOT graded by unit 8 (it is not `recipe` mode); a playbook
  that fails unit 3's gate cannot land; a `recipe`-mode run naming a playbook committed by an earlier
  creation run passes unit 4's resolution at BASE; a run that both creates and follows a playbook is
  refused.

## 3. Non-goals (OUT)

- No new authorization mode. `prompt` is the mode for a run whose solution is not given, which is
  exactly a run that must research a topic before it can write instructions about it.
- No new build-method section, no new directive. S2.
- No automated playbook GENERATION from an existing corpus. Unit 2's re-derivation mode writes a
  candidate canon for comparison; turning a body of past work into a playbook is a research act this
  path performs, not a transform the kit ships.
- No amendment inside a piece-producing run. S5.

## 4. Design

### Why this is a run and not a pass

The audit found that the ask's first verb had no owning unit and was structurally refused by unit 4's
preflight — a genuine hole in the decomposition rather than a deferred decision. The fix could have
been a first pass inside a playbook run. It is not, for one reason: a run that authors its own
instructions and then follows them has no external check on either half. Splitting them means the
playbook passes unit 3's gate and lands under whatever review the project applies, and only then can a
run be authorized against it.

That also makes the two verbs the owner named — create, and follow — visible as different acts with
different authorizations, which is what a mode declaration is for.

### Why amendment lands here too

Unit 9 forbids a run editing the checklist it is judged by, and the previous revision of unit 8
exempted the playbook from the scope gate anyway, on a premise unit 9 denies in the same build. With
amendment routed here the contradiction disappears: proposals are RECORDED by the runs that discover
them and ACTED ON by a later authoring run, which is the same shape this repo already uses for a
backlog row.

### What a creation run does NOT get

It gets no `pieces-complete`, no set checks, and no output-scope refusal, because it produces no
pieces. Under unit 6 S2 and unit 7 S5's term zero those items are MET-and-announced for a `prompt`-mode
run, which is exactly the branch the audit forced and is the first place it pays for itself.

## 5. Production-readiness checklist

- security — a creation run writes a document another run will execute against. Protocol §9's reduction
  applies: nothing here makes the playbook trustworthy, and the control is that it lands through the
  project's ordinary review and gate path rather than appearing mid-run.
- perf / scale — N/A.
- a11y — N/A.
- i18n — a playbook's prose is unconstrained; its declaration block is ASCII.
- error / empty / loading states — a creation run that produces a playbook failing unit 3's gate cannot
  land, and the gate names which check failed.
- observability — the playbook's `curated:` line records who ratified it and when, which is the only
  provenance a later run can read.
- risks — the largest is that a creation run is an ordinary `prompt`-mode run and therefore carries no
  playbook-specific discipline at all. That is deliberate: the discipline it owes is the research loop,
  which its mode already binds.
- testing + left-shift gates — S7, with the both-create-and-follow refusal as the arm that protects
  S4's ordering property.
- migration / rollback — this unit adds a Skill section and arms; it adds no code path of its own.
- user docs — unit 10's S0 preamble and this path's Skill section.

## 6. Acceptance criteria

- **AC1** — When a run authors a playbook and commits it under `authorized-by: prompt`,
  `bash tools/unattended/check-playbook.sh` grades that playbook from the moment it is tracked, with NO
  build README naming it — the tree-derived membership predicate of unit 3 S1 is what makes that
  observable, and the seam-derived one it replaced could not.
- **AC2** — When that same run's diff is evaluated, `bash tools/unattended/check-playbook.sh` does NOT
  apply the scope refusal, because the mode is not `recipe` mode. Observed, not assumed.
- **AC3** — When a playbook fails unit 3's gate, `bash tools/run-gates/run-gates.sh` REDS and the
  playbook cannot land. Staged and observed.
- **AC4** — When a later run's build README names that playbook, `--preflight` resolves it at BASE and
  does not refuse — the end-to-end join between this unit and unit 4.
- **AC5** — When a single run both creates a playbook and then names it in its own build README under
  the `default-branch` anchor, `bash tools/unattended/unattended.sh --preflight` REFUSES, because the
  playbook does not resolve at that run's BASE. Observed in a scratch tree declaring that anchor.
- **AC5b** — When the SAME run is performed under `ANCHOR_SCOPE="published"`, preflight does NOT refuse
  — observed, because this repo declares `published` and a spec whose protective arm cannot fire in its
  own dogfood tree is an assertion about nothing. `bash tools/unattended/check-playbook.sh` REDS instead,
  via unit 8's non-exempt playbook, and that is the backstop S4 names under this anchor.
- **AC6** — When a `prompt`-mode run reaches `--close`, `pieces-complete` and `set-checks-recorded` are
  both MET-and-announced rather than blocking, via `bash tools/unattended/unattended.sh --close`.

## 7. Gates

`bash tools/unattended/check-playbook.sh` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none — every fork below is RESOLVED in place, and THIS UNIT'S EXISTENCE is RATIFIED by the owner
(2026-08-21). Round 1 of the spec audit said adding a creation path needed an owner ruling and I
added it without one; the ruling was taken afterwards rather than assumed, and the parked entry in
the aborted run's record carries the question as it was put. The owner ratified the unit AS SPECCED,
which includes S4's anchor qualification: under `published` the ordering property has no machine
half and unit 8's non-exempt playbook is the backstop.

- **F1 — does a creation run need its own directive?** RESOLVED (agent, 2026-08-20, delegated): NO;
  the gate is the enforcement. `prompt` mode's two scoped handles already bind research and a solution
  test, and the one thing they do not bind — CONFORMANCE to unit 2's canon — is what unit 3's gate
  checks mechanically. A directive duplicating a gate is the gloss-that-grew-into-a-condition defect
  the directive design names.
- **F2 — should an amendment run be required to cite the proposals it acts on?** RESOLVED (agent,
  2026-08-20, delegated): stated in the Skill as a CHECK with its reason, never as a gate. A gate
  cannot check it without reading intent, and unit 9's proposals already carry the step they amend, so
  the join exists even when the citation does not.

## 9. Revision log

- rev-6 · 2026-08-21 · BUILT, with TWO acceptance criteria overtaken by unit 8's withdrawal and one
  defect found by insisting on observation.

  **AC2 and AC5b named a backstop that does not exist.** Both rest on unit 8's output-scope refusal —
  AC2 on its not applying to a `prompt`-mode run, AC5b on its redding a `recipe`-mode run that edits
  a playbook. Unit 8 is withdrawn, so neither can be observed and neither was faked.

  **And S4's own statement of the anchor split was wrong, in the direction that matters.** S4 says the
  ordering property has no machine half under `published`. Measured: `resolve_base` takes the SECOND
  anchor only when the build README fails to resolve at the merge-base, so a run whose build folder
  predates it keeps `default-branch` semantics and keeps the refusal whatever the scope declares. The
  arm asserting the opposite was written, run, and came back red — which is the only reason this is
  a correction rather than a claim that shipped.

  The state that IS unprotected is narrower and worth naming exactly: a run authoring BOTH halves,
  its own build folder and its own playbook, under `published`. Its BASE is the tip it pushed and
  that tip carries the playbook it just wrote. That is the `published` anchor's cost 1 reaching one
  step past what the protocol spelled out — a run that can author its own authorization can author
  the instructions it is judged against too — and the protocol now records the reach. The Skill
  states the CHECK against that state and not against a general one, because a rule aimed at the
  wrong state teaches the wrong habit.

  **AC6 found a live defect.** The piece-scoped items' term zero is MET for a non-recipe run and sets
  an announcement, under a comment reading "a silent pass is indistinguishable from coverage" — and
  `verb_close` printed that announcement under the UNMET arm only. The skip was therefore silent: the
  exact defect the announcing branch was written to prevent, one level up from where it was written,
  and invisible to every arm units 6 and 7 shipped because none of them read the close's output.
  Fixed, plus `DOD_OUT` is now cleared BEFORE each `dod_met` call rather than only after a print, so
  a MET item with nothing to say cannot inherit the previous item's text.

  **S2 and S6 landed as specced and cost almost nothing**, which was the prediction: this unit adds a
  Skill section and arms, and no code path of its own beyond the one-line close fix above.
- rev-5 · 2026-08-21 · the owner RATIFIED this unit's existence, which round 1 of the audit said was
  their call and which the previous revision carried as a park. Header gains the `ratified` pointer
  its ten siblings had; nothing about the mechanism moved.
- rev-4 · 2026-08-20 · folded the round-2 spec audit, which returned BLOCKED at precision 0.625 over
  the fold range. Every change here repairs a place where two sentences in this build ordered opposite
  implementations and neither was marked the loser.
- rev-3 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-2 · 2026-08-20 · owner ratified `recipe` as the authorization mode value; every reference to
  the mode (never to the playbook DOCUMENT, which keeps its name) renamed. Unit 1 S3b states the
  distinction once.
- rev-1 · 2026-08-20 · initial draft, written as the fold of the M4 spec audit's F17. The audit found
  that the owner's first stated verb had no owning unit in the roster of ten and was structurally
  refused by unit 4's preflight; this unit is that hole closed. It also receives F9's redirect, which
  removes the playbook from unit 8's exemption set by giving amendment a home outside the mode.

### What was built, against what was specced

- The Skill's creation section states the routing, the loop's owner, the gate that grades an unbound
  playbook, and the ordering property SPLIT BY ANCHOR — including the sentence a reader most needs
  under `published`: land the playbook first, then start the run that follows it.
- The amendment path is stated with F2's citation obligation as a CHECK carrying its reason, never as
  a gate, because no gate can read intent.
- Arms landed for AC1, AC5, AC5b and AC6, with AC5 now covering BOTH scope values over one tree —
  the pair is the evidence that the scope does not move this refusal. AC3 was already covered by
  unit 3's staged-break probes and no new arm was added for it. AC2 and AC4 are not armed: AC2's
  subject is withdrawn, and AC4's end-to-end join is what the existing `tRecipeOk` pass arm observes.

## 10. Reuse audit

This unit builds almost nothing, and that is the finding rather than a weakness. The creation loop is
the build method's research→test→choose section, already written and already bound by `prompt` mode's
two scoped directives — the seam exists because the previous mode build put it there for exactly this
shape of work. The AUTHORIZATION is `prompt` mode, unchanged. The VALIDATION is unit 3's leg, which
grades any tracked playbook without knowing who wrote it. The ORDERING property is enforced by a
refusal unit 4 already specifies, so AC5 observes an existing mechanism rather than a new one. What
this unit contributes is the ROUTING and the statement that creation and following are different acts —
which is why the audit could find the gap by reading the roster rather than by reading code. Recall
terms used: prompt mode research test choose directive scoped playbook creation amendment authoring
ordering base resolve refusal routing preamble skill path.
