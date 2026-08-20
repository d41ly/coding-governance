# TOOL-dScriptedRepeat-11 — authoring a playbook: creation, and owner-instructed amendment

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling

## 1. Goal

Own the owner's FIRST stated verb — with no playbook, research the topic and the code it must relate
to, then spec and create one from the template — as a `prompt`-mode run that produces a playbook, and
give owner-instructed AMENDMENT the same home.

## 2. Scope (IN)

- **S1.** THE CREATION PATH is a `prompt`-mode run, not a playbook-mode one. It has no `playbook:` to
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
- **S4.** THE ORDERING PROPERTY, and it is the reason this is a separate run rather than a first pass
  of a playbook run. The playbook must be OLDER than the BASE of any run that names it. A creation run
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
- **S7.** Arms: a creation run's diff is NOT graded by unit 8 (it is not playbook mode); a playbook
  that fails unit 3's gate cannot land; a playbook-mode run naming a playbook committed by an earlier
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
  `bash tools/unattended/check-playbook.sh` grades that playbook from the moment it is tracked.
- **AC2** — When that same run's diff is evaluated, `bash tools/unattended/check-playbook.sh` does NOT
  apply the scope refusal, because the mode is not the playbook mode. Observed, not assumed.
- **AC3** — When a playbook fails unit 3's gate, `bash tools/run-gates/run-gates.sh` REDS and the
  playbook cannot land. Staged and observed.
- **AC4** — When a later run's build README names that playbook, `--preflight` resolves it at BASE and
  does not refuse — the end-to-end join between this unit and unit 4.
- **AC5** — When a single run both creates a playbook and then names it in its own build README,
  `bash tools/unattended/unattended.sh --preflight` REFUSES, because the playbook does not resolve at
  that run's BASE. Observed; this is S4's ordering property expressed as a refusal that already exists
  rather than one this unit adds.
- **AC6** — When a `prompt`-mode run reaches `--close`, `pieces-complete` and `set-checks-recorded` are
  both MET-and-announced rather than blocking, via `bash tools/unattended/unattended.sh --close`.

## 7. Gates

`bash tools/unattended/check-playbook.sh` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — does a creation run need its own directive?** `prompt` mode's two scoped handles bind research
  and a solution test, which is most of what authoring a playbook owes. What they do not bind is
  CONFORMANCE to unit 2's canon — but unit 3's gate does that mechanically, and a directive duplicating
  a gate is the gloss-that-grew-into-a-condition defect the directive design names. Recommendation: no
  new directive. RESOLVED (agent, 2026-08-20, delegated): no new directive; the gate is the enforcement.
- **F2 — should an amendment run be required to cite the proposals it acts on?** It would join the
  improvement loop end to end. Against: it is a convention a gate cannot check without reading intent,
  and unit 9's proposals already carry the step they amend. Recommendation: state it in the Skill as a
  CHECK with its reason, not as a gate. Deferred to unit 10's prose, not open.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft, written as the fold of the M4 spec audit's F17. The audit found
  that the owner's first stated verb had no owning unit in the roster of ten and was structurally
  refused by unit 4's preflight; this unit is that hole closed. It also receives F9's redirect, which
  removes the playbook from unit 8's exemption set by giving amendment a home outside the mode.

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
