# TOOL-aPromptedMandate-5 — the Skill's prompt start path

**Status:** SPECCED · rev-3 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Give the agent the procedure that turns the owner's prose plus an authorizing parameter into a pushed
anchor and a started run, through exactly one owner turn — the surface the whole ask is actually
about, and the only one the owner touches.

## 2. Scope (IN)

- **S1** — the Skill template gains a **Start a run from a prompt** path, placed AFTER the slug
  path's own preflight fence, entered only when the invocation carries the authorizing parameter AND
  the project declares the published anchor scope.
- **S1b** — **the anchor-scope precondition is rendered, not assumed.** The adopter's `render()`
  gains a seventh placeholder for the conf's `ANCHOR_SCOPE`, and the prompt path opens by naming the
  value THIS project declares. Without it every adopter receives an identical unconditional procedure
  that ends in `fail 6`, with the remedy the path quotes inert — the shipped
  `tools/unattended/.unattended.conf.example` declares the EMPTY value, and `resolve_base`
  short-circuits on its published-scope test before `branch_tip_quiet` is ever reached.
- **S1c** — **the shared step 1 is amended, and so is protocol section 1.** Both affirmatively state
  the opposite of what the prompt path does; see section 4.
- **S2** — the parameter is named and its absence is the ordinary case: prose with no parameter is
  NOT an unattended build, and the Skill says so rather than inferring intent from prose.
- **S3** — the ordered procedure: orient in the `/session-kickoff` manner from the prose · derive
  every field derivable · ONE `AskUserQuestion` if and only if the scope is under-determined · write
  the build README carrying the prose, the answers and `authorized-by: prompt` · commit · push the
  branch · preflight · then the kickoff hand-back at its existing step.
- **S4** — the sufficiency test that decides whether to ask, stated as a rule and not as a feeling:
  the kickoff engine's sealed field set is the checklist, and ACCEPTANCE and GATES are the two whose
  absence is disqualifying — the engine's Step 5b exit 5 already says an unattended run with no
  acceptance check ABORTS rather than guesses.
- **S5** — the step ordering is stated with its reason, the way the existing step 5 is: the owner turn
  is before the push, because after the push the run is authorized and any later question is a stall
  with nobody to answer it.
- **S6** — the render is regenerated and `adopt-unattended.sh --check` stays green, including its
  surviving-placeholder arm.

## 3. Non-goals (OUT)

- **No change to the slug path's PROCEDURE.** It stays the default and the Skill's description keeps
  naming it first. Its shared step 1 IS amended (S1c) — rev-1's blanket "no change to the slug path"
  put the prohibition that blocks this whole unit out of scope, which is exactly where it lives.
- **No inference of intent from prose.** Without the parameter the Skill does not start an unattended
  run, however unattended the prose sounds. The parameter IS the authorization gesture.
- **No second AskUserQuestion, anywhere, ever.** Not on a resume, not after a compaction, not when
  research contradicts the prose — those are parks and aborts, which the protocol already owns.
- Not the research and test work itself; M12 owns that and unit 4 binds it.

## 4. Design

### The procedure, and why this order

The invocation is the Skill name, the authorizing parameter, and the prose.

1. **Orient** — Steps 0 to 4 of the kickoff engine, from the prose. The engine is a project
   declaration and may be absent; where it is, orientation is the agent's own and the Skill says
   which fields it must end up holding.
2. **Decide whether to ask** — S4's test. One call, every gap in it, four options maximum per the
   call's own limit, exactly as the waiver turn already does.
3. **Write the build folder** — README with front matter carrying the slug, the streams value and
   `authorized-by: prompt`; the owner's prose verbatim under its own heading; the clarifications and
   their answers; and a roster of the units as far as they are known. The roster is allowed to be
   provisional: measured, a roster that grows after preflight draws no refusal on the branch anchor.
4. **Commit, then push the branch.** Both, in that order, and the Skill states the refusal the agent
   will meet if it skips the push — check 32, verbatim, because a named refusal the agent has already
   read is one it does not have to diagnose.
5. **Preflight**, which now records the prompt mode (unit 1).
6. **The kickoff hand-back**, at the Skill's existing step and for its existing reason.

**After any later roster change: commit AND PUSH before the next authorization read.** The roster
comparison is satisfiable on the branch anchor only because the run re-pushes — protocol section 1
says the BASE there is a tip the run itself pushed, so it can re-satisfy the comparison against its
own new bytes, and the reproduction record says the same. A roster grown and committed but NOT
re-pushed is the normal post-research state, and it wedges `--close` at `authorization-reachable`,
with the driver's override refusal forbidding a way past it and nobody present to interpret it.

### Where the ask sits, and why no criterion could see it

The one owner turn is step 2 — before the commit, the push and preflight. **At that moment no
run-state file exists**, so the kickoff engine's Step 5b exit 5, which S4 cites, does not reach: its
header scopes it to a run that was actually started as one. Neither `--abort` nor `--park` is
available either; both refuse because there is no run-state file. **The pre-preflight
disqualification is therefore its own rule:** no run has started, so the agent stops without writing
anything — nothing staged, no run-state file, no abort verb. Exit 5's parked-then-proceed resolution
begins only AFTER preflight, and S4 says so rather than borrowing an authority that does not reach.

### The two carriers that forbid this path, and how they are amended

Both are affirmative statements, not omissions, and neither is the already-priced section 1 cost 1 —
cost 1 NAMES the self-authorization hole; these two assert it is closed.

**(a) `SKILL.template.md` step 1**, in the SHARED "Start a run" section, states that the build folder
is the authorization, that you do not write one and neither does the owner, and that preflight
refuses a build folder you created because a run that authorizes itself has no authorization. The
qualifying paragraph below it covers the PUSH and never retracts the authorship prohibition.
**Fold:** rewrite step 1 to name the ANCHOR rather than the author — a build folder that resolves at
the anchor this project declares is the authorization; where that anchor is the branch tip, the run
may author it, and protocol section 1 says what it costs.

**(b) protocol section 1's bullet** that the authorization is asserted and never written by the run,
plus the sentence beside it naming the owner's act as the slug invocation and nothing else.
**Fold:** make both anchor-scoped, in BOTH copies (leg check 10 byte-compares them).

**RATIFIED (owner, 2026-08-18): the protocol may be amended, and the authorization parameter is what
that consent is for.** The amendment is therefore in scope rather than a scope increase to be
avoided.

**What the amendment may NOT reach, stated because the ratification does not bound it and a build
without a bound drifts.** The amendment is to section 1's DESCRIPTION of the authorization — the
bullet's wording and the sentence naming the owner's act. It is not a change to the authorization
MECHANISM: `check_authorization`, `resolve_base`, `observe_anchor` and leg check 13 stay exactly as
they are, per this build's headline finding and unit 1's non-goals. The distinction matters here more
than anywhere else in the build, because a run that may rewrite the rules it is authorized under has
no rules. Protocol section 9 already lists "a run that edits this kit and commits it" among what the
kit does NOT close; the ratification consents to an amendment an owner asked for, and does not widen
that entry.

Leaving either unamended ships a document that carries a flat prohibition and, further down, the
procedure that violates it — from which an agent learns that a stated rule in this Skill can be
ignored.

### Why the owner turn lands before the push

The push is what makes the build folder an anchor. Everything written before it is provably older
than the authorization; everything after it is contemporaneous with a run that is already authorized.
Placing the one owner turn before the push therefore makes "the clarification happened at session
start" a property of the commit graph rather than a claim in a transcript — which is the same move
protocol section 1 makes for the mandate itself, and is stronger than the driver-side refusal that
guards the waiver turn.

### The under-determination test

The Skill states it as a closed question over the kickoff engine's sealed field set, obtained from
the checker's own task-skeleton verb rather than restated (the Skill already names `/session-kickoff`
with no placeholder behind it, so this needs no conf key) — a second spelling here would drift
against the manifest, which is the defect this kit spent a build removing. Disqualifying absences are
ACCEPTANCE and GATES; every other gap is askable, and if the owner declines to answer, parkable.

### Alternatives rejected

- **Ask nothing, ever, and abort on under-determination.** Rejected: the ask explicitly allows one
  turn at session start, and an abort where a question would do wastes the whole run.
- **Ask per gap.** Rejected for the reason the waiver turn already gives: the owner is walking away,
  and a multi-round conversation at that moment is what this kit exists to remove.
- **Let the driver take the prose on argv.** Unit 1, section 3.

### Files touched (estimate)

`tools/unattended/SKILL.template.md` (the new path AND the shared step 1) ·
`.claude/skills/unattended/SKILL.md` (rendered, byte-compared) ·
`tools/unattended/adopt-unattended.sh` (the seventh placeholder in `render()`) ·
`tools/unattended/.unattended.conf.example` (the key is already declared there empty; its comment
gains the prompt-path consequence) · `tools/unattended/PROTOCOL.template.md` and
`memory/guides/UNATTENDED-PROTOCOL.md` (section 1's bullet) ·
`tools/unattended/check-unattended.sh` (S5's PER-PATH ordering arm) ·
`tools/unattended/check-unattended.test.sh`.

### The ordering arm must be per-path

Leg check 18 orders the FIRST `unattended.sh --preflight` in the template against the FIRST
`/session-kickoff`. The new path names both tokens again — its first step is to orient in the
`/session-kickoff` manner. Placed before the slug path, that mention becomes the first match and
check 18 reds falsely; placed after, check 18 keeps grading the slug path alone and is silently blind
to the new one. **The second outcome is the one nobody notices**, which is why S1 pins the placement
AND the arm anchors each path's lines within its own section rather than across the file.

## 5. Production-readiness checklist

- security — the parameter is the authorization GESTURE and not the authorization; the anchor is
  still the pushed build folder, and the protocol's boundary section is unchanged
- perf / scale — N/A
- a11y / i18n — N/A
- error / empty / loading states — prose with no parameter (not an unattended run); parameter with no
  prose (refuse, nothing to scope); under-determined prose (ask once, then abort if ACCEPTANCE or
  GATES is still missing)
- observability — the prose and the answers are in the build README at BASE, which is where the
  wrap-up derives scope from
- risks — an agent asking a second time later (the Skill states the prohibition and M10 already binds
  it); the render carrying a surviving placeholder, which is a separate question from template parity
  and has its own arm in the wiring check; the ordering arm being written over prose the agent can
  satisfy while doing the steps in the wrong order
- testing + left-shift gates — a leg arm for the step ordering, the wiring check's placeholder arm,
  and unit 6's cross-component arm exercising the whole path
- migration / rollback — additive; the slug path is untouched
- user docs — the Skill IS the doc

## 6. Acceptance criteria

- **AC1** — When the rendered `.claude/skills/unattended/SKILL.md` is read, it carries a prompt start
  path whose steps are ordered orient, **ask at most once**, write, commit, push, preflight, kickoff
  hand-back. The ask is IN the ordered list: rev-1 omitted it, and a render that asks after the push
  satisfied every rev-1 criterion while destroying the provenance property section 4 argues for.
- **AC2** — When `bash tools/unattended/adopt-unattended.sh --check` runs, the render matches the
  template and the conf, and carries no surviving brace-shaped placeholder.
- **AC3** — When a fixture Skill orders the push after preflight, `bash tools/unattended/check-unattended.sh`
  fails by name.
- **AC4** — When the refusal text the Skill quotes for an unpushed branch is compared against the
  one `tools/unattended/unattended.sh` emits, a leg arm finds them equal rather than trusting them.
- **AC5** — When the prompt path is read, it names exactly one `AskUserQuestion` and states that no
  later verb may take an answer.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs over this repo, it exits 0, and
  leg check 18 still resolves to the SLUG path's own two lines rather than to the prompt path's.
- **AC7** — When the prompt path is rendered against a conf declaring no anchor scope, the Skill
  names that value and tells the agent this path is unavailable — rather than printing a procedure
  that ends in `fail 6`.
- **AC8** — When `.claude/skills/unattended/SKILL.md` is grepped, no unconditional
  refusal-of-a-run-authored-build-folder sentence survives in step 1, and the amended step 1 names
  the anchor.
- **AC9** — When `bash tools/unattended/check-unattended.sh` runs, leg check 10 finds section 1's
  amended bullet byte-identical in `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md`.
- **AC9b** — When the cumulative diff is read at close, `tools/unattended/unattended.sh`'s
  `check_authorization`, `resolve_base` and `observe_anchor` and `check-unattended.sh`'s check 13 are
  unchanged from `base 6517579f` — the amendment reached the protocol's description and not its
  mechanism.
- **AC10** — When the S5 ordering arm runs, it asserts the first `AskUserQuestion` line precedes the
  first push line WITHIN the prompt path's own section, in check 18's first-match line-number shape.

## 7. Gates

`bash tools/unattended/adopt-unattended.sh --check` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/adopt-unattended.test.sh` ·
`bash tools/check-wiring.sh --check` · `bash tools/run-gates.sh`

## 8. Open questions

none — the forks below are RESOLVED.

- **May this build amend the binding protocol's section 1?** — RESOLVED (owner, 2026-08-18): yes;
  the protocol can be amended, and that is what the authorization parameter exists for. Raised
  because rev-1 promised not to touch the slug path and the M4 audit found the prohibition living
  there. The agent-set BOUND on what the amendment reaches is in section 4 and is not part of the
  ratification.
- **Carrier for the anchor-scope precondition** — RESOLVED (agent, 2026-08-18): a rendered seventh
  placeholder plus a precondition sentence, over a bare prose warning. A warning an adopter reads is
  not a warning their render carries; the placeholder makes the Skill state THEIR conf's value.
- **The parameter's spelling** — RESOLVED (agent, 2026-08-18): a `--build` argument, taken at the
  Skill level and never reaching the driver. The parameter's EXISTENCE is owner-requested (the ask
  names it), so only the spelling was agent-resolved and M3 veto 2 is not engaged. The name says what it authorizes; the driver's own argv
  surface does not grow, per unit 1's non-goals.
- **Where the one owner turn sits** — RESOLVED (agent, 2026-08-18): before the push, per section 4.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the M4 spec audit, which returned BLOCKED on this unit twice. The
  published-anchor precondition appeared in no spec while the path ships in a KIT template whose
  example conf declares the empty value (ids 18, 29) — S1b added. The Skill's shared step 1 and
  protocol section 1 both affirmatively forbid the path, and rev-1's non-goal put them out of scope
  (ids 2, 19, 32, 41) — S1c added. Also: the ask was absent from AC1's ordered list (id 12); check
  18's placement was unstated and silently blind in one direction (id 24); Step 5b exit 5 does not
  reach the pre-preflight moment (id 26); the roster re-push obligation was dropped from the prior
  record's conclusion (id 43).
- rev-3 · 2026-08-18 · owner ratified the section 1 amendment (the authorization parameter is the
  consent for it). Added the agent-set bound on what the amendment may reach — description, not
  mechanism — and AC9b to observe it.

## 10. Reuse audit

Satisfied for the SET in unit 1's reuse audit. The seams extended are all existing: the Skill
template's waiver turn is the pattern for the one-owner-turn discipline (single call, grouped
questions, default-deny, "from the next command onward there is nobody to ask"); the Skill's existing
kickoff-ordering rule, already gated by a leg check, is the pattern for S5's ordering arm; and the
kickoff engine's Step 5b already enumerates how each interactive exit resolves with no owner turn,
including exit 5's ABORT on a missing acceptance check, which S4 cites rather than restates.
