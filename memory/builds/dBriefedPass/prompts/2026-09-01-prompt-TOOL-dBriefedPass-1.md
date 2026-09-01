# The owner's prompt, verbatim

**Serves:** research TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5

Handed to `/unattended` as the `--prompt` value on 2026-09-01, node `d`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself and is taken
verbatim. Recorded here rather than in the build README for the three reasons that file's own heading
canon, byte ceilings and marker matcher impose — and this build is partly ABOUT that gap, so the
record is also its first instance.

```text
New work session in the unattended kit. Having tested out the kit through several sessions, a major
problem surfaced: unattended builds (any mode) do not always closely follow their protocol. Steps may
be mixed up by the individual work units - build can run BEFORE they are specced with spec written
postfactum, and it is UNCLEAR what actual instructions an agent starts building with.
**Proposed solution**: the use of `Workflow` (or `Agent` if workflows are not available) harness on
every build pass.
A harness that drives the entire build from start to finish following one strict checklist protocol
of build steps to execute, depending on the mode it's running in:

* a. Orientation. Normally ground in project code, memory recall, reuse audit, lexicon. Derive as
much information from the user prompt as possible. Full set of relevant instructions are compiled at
this point (prompt) so the next step reorients only with the relevant information. Handed off to a
WORKFLOW on the next step (prompt unattended mode).
* b. Design. A design pass to lay the foundation of how a feature fits into the project and what's
needed to make it integrate seamlessly. Research is conducted at this point, use of web search is
encouraged. Build README.md is created (needs integration with the template and its gates), design
pass should be integrated into the readme file. Build README and a prompt are handed off to the next
'Workflow'. (prompt unattended mode)
* c. Specs. The build is planned and specced. Agents are handed a prompt from the last step and are
pointed at the build's README.md file with the build design. Build order is decided, spec are
written, and adversarially reviewed. Each spec gets a handoff prompt written + its spec file and
handed off to the next step's Workflow (or Agent if workflows are not available). Agents are well
oriented with relevant information through this approach. (prompt unattended mode)
* d. Build. The specs are written, sitting in their build folder (either worktree or main is fine).
The order is decided prior to build execution, laid down in the README file. Each spec is its own
`Workflow` (or `Agent`) running in their build's order. Each unit is handed a handoff prompt and its
spec, nothing else. Keeping agents well oriented only in relevant facts. Harness watches for the
allowed order and instructs agents if something's off. If a build is expanded through new findings,
harness drives them through a new-finding exclusive workflow - Spec/Review/Order in the
build/Prompt/Build. New findings are never built before being specced, and agents should be clearly
instructed by the harness. All building happens only by first orienting with a Unit's spec. (prompt,
slug modes. How does this fit into playbook?)
* e. Closing adversarial. Happens once all build steps are complete, no open specs are left. Two
review passes at most by default (overridable by the owner), if any findings are promoted to build
units they are driven by the same `Workflow` (`Agent`) as before - Spec/Review/Order in the
build/Prompt/Build.
* f. Final bookkeeping, gates, merge to local main only.

Ground yourself in the code and memories relevant to this task, review its viability, research the
most efficient and flexible implementation and execute per the protocol.
```

## How this run read it

**Two defects, not one.** The prompt names them together and they have different remedies. Defect A
is that pass ORDER is unenforced. Defect B is that an agent's governing instructions are not a
record. A harness addresses A by construction and B by convention; only a driver refusal addresses A
against a run that does not use the harness, and only a tracked artifact addresses B at all.

## The clarifications taken at the run's one owner turn

Both were asked in a single `AskUserQuestion` on 2026-09-01, before the build folder was written, and
both took the recommended option.

**Q1 — the review-round cap.** Step (e) proposes "two review passes at most by default". The shipped
`--review` loop deliberately carries no round cap: the protocol refused one with a measurement (over
the tracked corpus the clean exit occurs zero times, so a cap "would only move the stall earlier"),
and terminates on CONVERGENCE instead. **Answer: keep convergence, no cap.** The harness calls
`--review` each round and obeys its verdict; nothing in this build adds a second termination rule.

**Q2 — binding force.** The harness can be the mandatory route or a recommended one. **Answer:
mandatory, plus a history-based gate** — the protocol binds the harness AND a merge-bar leg refuses
a build whose unit was committed before a conforming spec existed at that commit's parent. This is
the owner's authorization for the carrier edits units 3 and 5 make.

## What the prompt asks for that this build does NOT deliver, and why

**Steps (a) and (f) cannot move into a harness, and this is structural rather than a scoping
choice.** The keepalive store is in-memory and session-scoped, so only the main loop can schedule and
reap it; `--preflight` must run before the kickoff hand-back; the single owner turn has to happen in
a session a human can answer. Landing, `--close` and `--landed` are likewise main-loop acts. The
harness therefore covers (b) through (e), and the run-state file remains the join between the two
halves. Recorded here so a later reader does not read the prompt as an unmet requirement.

**"How does this fit into playbook?"** — recipe mode produces declared CONTENT against a playbook's
own checklist, and its per-piece and set records already carry the ordering that mode needs. The
harness is scoped to `prompt` and `slug` modes, which are the ones whose units are specs. Unit 5
states that scope in the protocol rather than leaving it inferred.
