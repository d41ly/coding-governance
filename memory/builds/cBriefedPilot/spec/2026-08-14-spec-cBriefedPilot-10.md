# TOOL-cBriefedPilot-10 — the last owner turn, and why it is the last one

**Status:** OPEN · rev-1 · 2026-08-14 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

Turn a waiver flag on the invocation line into a confirmed, reasoned owner decision, taken through
one `AskUserQuestion` before the run goes unattended — and make the Skill state plainly that this is
the last question it may ask.

## 2. Scope (IN)

- **S1** — a step A in `tools/unattended/SKILL.template.md`, between the method read and the
  keepalive, that fires only when the invocation named at least one handle.
- **S2** — ONE `AskUserQuestion` call batching every named handle, not one call per handle.
- **S3** — DEFAULT-DENY. A handle named on the invocation line but not confirmed with a reason is NOT
  waived. The flag requests the question; the answer grants the waiver.
- **S4** — each confirmed pair is carried into the preflight invocation as
  `--waive <handle> --reason "<text>"`.
- **S5** — one sentence stating that from preflight onward M10 binds and there is nobody to ask, so
  no later step may take an owner turn.
- **S6** — the step names the interaction for each handle whose waiver has one: `land-once-done` owes
  an override at close, `reuse-first` reds the full bar.

## 3. Non-goals (OUT)

- **Driver-side validation.** Unit 3 owns the five refusals. The Skill asks; the driver refuses.
- **Any question after preflight.** That is the property this unit exists to establish, and unit 3's
  ordering branch is what enforces it mechanically.
- **A parser for the flag syntax.** The agent reads the invocation line; no script parses it before
  preflight. Adding one would be a second mechanism for what the agent already does.
- **Asking when no handle was named.** The default path takes no owner turn at all, which is the
  whole point of `/unattended <slug>`.

## 4. Design

### Why one question and not eleven

`AskUserQuestion` takes up to four questions per call and each carries options. Batching the named
handles into one call keeps the owner turn to a single interaction; a per-handle loop would make
waiving three directives a three-round conversation at the exact moment the owner is trying to walk
away.

Where more than four handles are named, the step asks in one call per group of four rather than per
handle, and says so.

### Why default-deny

A flag is a request, not a grant. The owner's own framing is that the agent "walks the user through"
— which only means anything if the walk-through can end in "no". Default-deny also makes the
degenerate case safe: an agent that mis-parses the invocation line and invents a handle gets a
question, not a silent waiver.

The reason is required because the record is required. A waiver with no reason is indistinguishable
from a waiver nobody meant, and unit 3 refuses it at the driver anyway — so a Skill that let one
through would only produce a refusal the owner is no longer present to read.

### Why this is the last owner turn

The Skill says it, and unit 3's ordering branch means it. `--waive` is accepted by `--preflight`
alone and only while no run-state file exists, so after preflight there is no verb that could take an
answer. M10's "never ask: there is nobody to answer, so a question is a stall" then holds for the
rest of the run without contradiction.

### Files touched (estimate)

`tools/unattended/SKILL.template.md` · the rendered `.claude/skills/unattended/SKILL.md`.

### Alternatives rejected

- **Asking after preflight**, so the run-state file exists to record into. Rejected: it puts an
  interactive stop inside the unattended window, which is the failure Step 5b of the kickoff engine
  was written to remove.
- **A `--waive-all` convenience flag.** Rejected: it is a global waiver with one reason, which is the
  shape the design refused when it rejected a conf-declared registry.

## 5. Production-readiness checklist

- security — the reason text reaches a tracked file; the driver's newline and bypass-flag refusals
  are the controls, and they are unit 3's.
- perf / scale — one interaction, only when a flag was named.
- a11y · i18n — N/A.
- error / empty / loading states — an unanswered or declined question leaves the handle unwaived,
  which is the safe state by construction.
- observability — every granted waiver becomes a parked line at preflight.
- risks — an agent could skip the question and pass `--waive` directly. Nothing observes that, and
  the build README records it under protocol §9's boundary rather than claiming a control.
- testing + left-shift gates — leg check 18 asserts the Skill's step ORDER (unit 14); the question
  itself is agent behaviour and is not gateable.
- migration / rollback — additive; an invocation with no flag is unchanged.
- user docs — this IS the user doc.

## 6. Acceptance criteria

- **AC1** — When the invocation names no handle, the rendered Skill's step A is skipped and no owner
  turn is taken.
- **AC2** — When the invocation names two handles, the Skill instructs ONE `AskUserQuestion` covering
  both.
- **AC3** — The rendered Skill states that a named-but-unconfirmed handle is not waived.
- **AC4** — The rendered Skill states that no step after preflight may ask a question.
- **AC5** — `bash tools/unattended/adopt-unattended.sh --check` is green and the render carries no
  surviving brace-shaped placeholder.

## 7. Gates

`unattended skill wiring` · `unattended adopter e2e` · the full bar. Leg check 18's order assertion
arrives with unit 14.

## 8. Open questions

**Does the step ask about a handle the owner did NOT name?** A run could reasonably surface
`reuse-first`'s hazard unprompted. Recommendation: no — an unprompted question is an owner turn the
owner did not ask for, and the Skill's table already carries the warning at the moment it is read.
Resolver: agent, if the owner does not take it.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds C2 and D1's ordering half.

## 10. Reuse audit

No existing seam fits, and the evidence is that nothing in this repo takes an interactive turn from
inside a skill. `skills/session-kickoff/SKILL.md` uses `AskUserQuestion` for genuine forks and is the
nearest precedent for the SHAPE — derive what you can, ask only what you cannot — but it asks during
an attended session and has no unattended-window constraint to respect. That constraint is this
unit's own, and it is discharged by unit 3's ordering branch rather than by anything reusable.

The `--waive` surface it hands to is unit 3's; the table it reads from is unit 9's.

Recall terms used: unattended skill owner turn waiver flag confirm ask question default deny reason
preflight last turn never ask.
