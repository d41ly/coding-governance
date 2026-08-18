---
slug: aPromptedMandate
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-3 TOOL-aPromptedMandate-4 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6 TOOL-aPromptedMandate-7
---

# aPromptedMandate — an unattended run starts from the owner's prose, not from a landed slug

Node `a` · opened 2026-08-18 · streams tooling.

The owner's ask: `/unattended` should accept natural language plus a parameter that authorizes a
FULLY unattended build — research, test, design, spec, adversarial spec review, build, adversarial
diff review — rather than only the slug of a build someone already specced.

## Start here

**The authorization needs no new mechanism, and that is the headline finding.** The obvious reading
of the ask is that prose-plus-a-flag becomes a new authorization primitive. It does not have to be.
This repo already declares `ANCHOR_SCOPE="published"`, under which a build folder the run itself
authored, committed and pushed resolves at the tip the remote advertises for the run's own branch.
Measured end to end against a live bare origin on node `a`, 2026-08-18:

| Step | Observed |
|---|---|
| run authors its own build folder, branch NOT pushed | `check 32 FAILED — the remote advertises no tip for the branch this run is on` |
| same tree, branch pushed | `preflight OK · anchor-kind: run-branch` |
| the gate leg over that same tree | exit 0 — checks 9 and 13 both silent |
| roster grows after preflight (what research does) | no refusal; only the ordinary unmet-DoD blocks |

So the run CAN author its own scope and still be accepted by both the driver and the bar. Protocol §1
already prices this exactly — cost 1, "a run can authorize ITSELF in two commands" — and the owner
already accepted it when the second anchor landed. **This build opens no new hole; it uses one the
record says is open, and makes the fact that it was used legible.**

What is therefore NOT in this build: any change to `check_authorization`, to `resolve_base`, to the
anchor observation, or to leg check 13. The reproduction above is the evidence for leaving all four
alone.

**What IS missing** is everything the ask needs on top of authorization: a way to tell a
prose-started run apart from a slug-started one after the fact, phases for the research and test
work, a method section stating the research→test→choose loop, directives binding it, and a Skill
path that walks the owner's prose to a pushed anchor through exactly one owner turn.

## The one owner turn

The ask allows a clarification turn at session start and nowhere else. The kit already has that
shape — the directive-waiver turn at step 2 of the Skill, enforced by a driver refusal
(`--waive` is accepted by `--preflight` alone) rather than trusted. The prompt path reuses the
discipline and gets a stronger enforcement than a driver flag could give it: the owner's prose and
every clarification are written into the build README **before** the anchor push, so they are at
BASE. A run cannot have taken an answer later than a commit it is authorized by.

## Units

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aPromptedMandate-1` | 2 | the prompt-mode declaration, and where it is carried |
| 2 | `TOOL-aPromptedMandate-2` | 1 | the RESEARCHING and TESTING phases |
| 3 | `TOOL-aPromptedMandate-3` | 2 | the build method's research→test→choose section |
| 4 | `TOOL-aPromptedMandate-4` | 2 | the two mode-scoped directives |
| 5 | `TOOL-aPromptedMandate-5` | 2 | the Skill's prompt start path |
| 6 | `TOOL-aPromptedMandate-6` | 1 | the driver-then-leg cross-component arm |

Unit 6 closes `TOOL-aStandingWrit-8`, which is open on exactly the gap this build's own evidence
had to fill by hand: the kit has driver arms, leg arms and Skill-parity arms, and zero arms that run
the driver and THEN the leg over one tree.

## What the spec audit changed

The M4 audit returned **BLOCKED** at rev-1 — 26 confirmed defects, 23 refuted, precision 0.53. All
six specs moved to rev-2. The record is
[`reviews/2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md`](reviews/2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md).

**The headline finding survived intact** — no confirmed defect asks for a change to
`check_authorization`, `resolve_base`, `observe_anchor` or leg check 13, and the four measurements
above were re-checked against source by more than one lens. What the audit found is that the
design's precondition and its cost were measured, understood, and then **not carried into the
artifacts an adopter and an agent actually receive**:

| | The gap at rev-1 | Where it landed |
|---|---|---|
| **B1** | The published-anchor precondition appears in NO spec, yet the path ships in a kit template whose example conf declares the empty value. Every adopter at the default would receive a procedure ending in `fail 6` with its own quoted remedy inert. | unit 5 S1b — a rendered seventh placeholder |
| **B2** | The Skill's shared step 1 and protocol §1 both *affirmatively* state that a run may not author its build folder. Rev-1 put the slug path out of scope; the prohibition lives there. | unit 5 S1c — both carriers amended; **owner ratified the §1 amendment 2026-08-18** |
| | A three-field directive entry breaks leg arms A and B; the `--waive` test rev-1 named needed no change at all. | unit 4 S7 — one splitter, enumerated against source |
| | The mode reader as specced was dead: the existing awk `exit`s on its first hit, and AC1+AC2 both pass over a dead reader. | unit 1 §4 + AC2b |
| | Unit 6's roster arm asserted on output `--close` discards — it could never fail. | unit 6 S2b — a verdict-keyed pair |

The refuted 23 are recorded too, so a later reader does not re-raise them. Seven pairs split on the
same territory: in every case the refuted form over-claimed ("unbuildable", "nothing catches it")
while the confirmed form named a narrower thing that was genuinely missing.

**The fold itself is unreviewed**, by M4's stop rule: fixes are folded once, and reviewing resumes
only if the design moves again.

**B2 went to the owner** rather than being ratified by the agent, because rev-1 had promised not to
touch the carrier the defect lives in and amending a binding contract is M3 veto 2 territory. The
answer: the protocol can be amended, and the authorization parameter is what that consent is for.
Unit 5 rev-3 carries it, together with an agent-set bound the ratification does not state — the
amendment reaches section 1's DESCRIPTION of the authorization, never its MECHANISM, because a run
that may rewrite the rules it is authorized under has no rules.

<!-- roster:units -->
| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aPromptedMandate-1` | 2 | the prompt-mode declaration, and where it is carried |
| 2 | `TOOL-aPromptedMandate-2` | 1 | the RESEARCHING and TESTING phases |
| 3 | `TOOL-aPromptedMandate-3` | 2 | the build method's research→test→choose section |
| 4 | `TOOL-aPromptedMandate-4` | 2 | the two mode-scoped directives |
| 5 | `TOOL-aPromptedMandate-5` | 2 | the Skill's prompt start path |
| 6 | `TOOL-aPromptedMandate-6` | 1 | the driver-then-leg cross-component arm |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 6 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-3 TOOL-aPromptedMandate-4 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6 TOOL-aPromptedMandate-7

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aPromptedMandate-1 — the prompt-mode declaration, and where it is carried](spec/2026-08-18-spec-aPromptedMandate-1.md) | SPECCED | rev-2 | 2026-08-18 |
| [TOOL-aPromptedMandate-2 — the RESEARCHING and TESTING phases](spec/2026-08-18-spec-aPromptedMandate-2.md) | SPECCED | rev-3 | 2026-08-18 |
| [TOOL-aPromptedMandate-3 — the build method's research→test→choose section](spec/2026-08-18-spec-aPromptedMandate-3.md) | SPECCED | rev-3 | 2026-08-18 |
| [TOOL-aPromptedMandate-4 — the two mode-scoped directives](spec/2026-08-18-spec-aPromptedMandate-4.md) | SPECCED | rev-2 | 2026-08-18 |
| [TOOL-aPromptedMandate-5 — the Skill's prompt start path](spec/2026-08-18-spec-aPromptedMandate-5.md) | SPECCED | rev-3 | 2026-08-18 |
| [TOOL-aPromptedMandate-6 — the driver-then-leg cross-component arm](spec/2026-08-18-spec-aPromptedMandate-6.md) | SPECCED | rev-2 | 2026-08-18 |

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-18-build-TOOL-aPromptedMandate-1-anchor-reuse-reproduction.md](build/2026-08-18-build-TOOL-aPromptedMandate-1-anchor-reuse-reproduction.md) | research | TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 |
| [2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md](reviews/2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md) | spec-audit | TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-3 TOOL-aPromptedMandate-4 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-18-spec-aPromptedMandate-1.md](spec/2026-08-18-spec-aPromptedMandate-1.md)
  - [2026-08-18-spec-aPromptedMandate-2.md](spec/2026-08-18-spec-aPromptedMandate-2.md)
  - [2026-08-18-spec-aPromptedMandate-3.md](spec/2026-08-18-spec-aPromptedMandate-3.md)
  - [2026-08-18-spec-aPromptedMandate-4.md](spec/2026-08-18-spec-aPromptedMandate-4.md)
  - [2026-08-18-spec-aPromptedMandate-5.md](spec/2026-08-18-spec-aPromptedMandate-5.md)
  - [2026-08-18-spec-aPromptedMandate-6.md](spec/2026-08-18-spec-aPromptedMandate-6.md)
- **`build/`**
  - [2026-08-18-build-TOOL-aPromptedMandate-1-anchor-reuse-reproduction.md](build/2026-08-18-build-TOOL-aPromptedMandate-1-anchor-reuse-reproduction.md)
- **`reviews/`**
  - [2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md](reviews/2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md)
<!-- /gen:build-docs -->
