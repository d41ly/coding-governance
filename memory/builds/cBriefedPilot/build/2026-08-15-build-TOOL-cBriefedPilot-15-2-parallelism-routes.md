# Parallelism routes — the hunt D6 blocked on

**Serves:** journal TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-21  <!-- inferred: its own text names unit 21's finding and unit 15 as the reader of it -->

parallelism route: none

Unit 21's recorded finding. Unit 15 reads the verdict token above and takes its branch from it; this
document is the evidence, and it carries OBSERVATIONS rather than conclusions wherever the two can be
told apart.

The owner refused, at P2, to let D6's inversion ship on a clause excusing it where no mechanism
exists. This is the hunt that refusal bought. The answer is that no route clears the standard WHOLE —
but the reason is not the one the design pass assumed, and the correction is worth more than the
verdict.

## The standard

A route survives only when all four hold, each ANSWERED BY AN OBSERVATION. Three of four is recorded
as failing, with the missed criterion named.

- **E1** the layer reaches the pass — the dispatched agent has the eleven directives and the run's
  recorded waivers, by inheritance or by mechanical priming.
- **E2** the budget resets, or is not spent.
- **E3** M6's three conditions can still be met for the pair, condition (3) included.
- **E4** each pass can commit at its own end without the two commits racing one index.

## Per-route observations

### R1 — direct `Agent` spawn from the main loop

`tools/hooks/agent-cap.js` keys the budget on `session_id` + `prompt_id` and claims a numbered slot
with `O_EXCL` at `<git-common-dir>/agent-cap/<session>__<prompt>/slot-N`, `MAX_VERIFIERS = 5`. Read at
source, lines 632 and 654.

Observed: no budget directory exists for this session at all, which is consistent with this run
having dispatched only through `Workflow`. **E2 fails as the design pass stated** — the key includes
a prompt id, and an unattended run has no further owner prompt to mint a new one, so the allowance is
spent once and cannot be replenished inside the run.

### R2 — a `Workflow` sidechain

**The blanket claim in `memory/guides/REVIEW-PROTOCOL.md` is FALSE, and this is the finding.** That
document states a sidechain "inherits no hooks and no `CLAUDE.md`". Measured by dispatching a probe
agent and asking it to report what arrived before it read anything:

- **The project instruction file was inherited IN FULL.** The probe's first message carried a
  `<system-reminder>` containing `CLAUDE.md` and the whole of `AGENTS.md` — the charter, the gate
  suite, the node registry, the leg list. Present BEFORE it read or ran anything.
- **A `SubagentStart` hook DID fire**, arriving as its own message with the verbatim header
  `SubagentStart hook additional context:` and a full behavioural instruction block. Hooks reach a
  sidechain.
- **No `SessionStart`-shaped injection was observed** — no wiring report, no
  `check-wiring.sh --session` output. Reported as not-observed rather than as absent.

So E1's inheritance half HOLDS, against the document. The directives and the run's waivers are not in
`AGENTS.md`, so they still need mechanical priming — which is what this unit's own §8 resolved as
legitimate, on the precedent that M4 already dispatches a pass kind into a sidechain and calls those
agents primed.

**E2 holds.** A sidechain agent is not counted against the per-prompt direct-spawn budget.

**The decisive `PreToolUse` experiment DID NOT RUN, and that is recorded as unmeasured, not as
passed.** The probe found the `Agent` tool absent from its registry entirely — `ToolSearch` with
`select:Agent,Workflow,Task` returned `No matching deferred tools found` — so the hook on matcher
`Workflow|Agent` was never given anything to fire on. In the probe's own words: it did not observe
`agent-cap.js` firing, and did not observe it failing to fire.

That absence is itself the more useful observation. **A sidechain agent cannot fan out at all**, so
the ≤5 arity rule has nothing to bind at that depth: the capability is missing rather than policed,
which is the stronger property. To measure `PreToolUse` reach properly a later attempt needs a hook
on a matcher covering a tool the sidechain DOES hold — `Bash` would answer it.

**E3 and E4 are NOT OBSERVED.** Both are arguable on paper — the orchestrator could own every phase
move so no dispatched pass touches the run-state file, and R5 supplies a checkout shape where two
commits do not share an index. Neither was run. Under the standard, an argument is not an
observation, so R2 is recorded as **failing on E3 and E4**, having cleared E1 and E2.

### R3 — a headless child process

**Dead on this host, and by the cheapest possible test.** `command -v claude` finds nothing: the CLI
is not on PATH in the run's environment, so no child can be started to re-establish the layer. E1
fails at the first step. No amount of reasoning about process isolation would have found this; one
PATH lookup did.

### R4 — the keepalive tick as a budget-resetting turn

The key does include a prompt id, so a new turn would mint a new key. Not tested further, because R1
already fails E2 for a reason R4 does not repair: a keepalive tick arrives on a schedule the run does
not control, so a pass dispatched at tick N cannot be joined by the orchestrator at tick N. Recorded
as untested rather than as failing.

### R5 — one git worktree per concurrent pass

Not a dispatch route. Observed: this repo carries six worktrees, each with its own index under
`.git/worktrees/<name>/index`, so two passes in separate worktrees do not race one index. **R5 is a
viable checkout shape** and is what any surviving dispatch route would need for E4.

### R6 — no route; sequence and park

M6's existing fallback. It is what the verdict selects.

## What this costs, stated plainly

D6 does not land. Under a standing mandate, disjoint passes are still sequenced, and M6's rule stands
as written rather than inverted.

The nearest thing to a survivor is **R2 with R5**, and it fails the standard on two criteria that were
never run rather than on two that failed. That is a real distinction and it should not be smoothed
over: someone re-opening this needs to know the gap is unmeasured evidence, not adverse evidence.

## The correction that outlives the verdict

`memory/guides/REVIEW-PROTOCOL.md` asserts that a sidechain inherits no hooks and no `CLAUDE.md`.
Measured here, both halves of that sentence are wrong: the instruction file arrives in full, and a
`SubagentStart` hook fires and is obeyed. The sentence is load-bearing — it is cited as the reason
sidechain dispatch would void the directive layer, which is the argument that blocked D6 in the first
place — and it is a binding document.

Correcting it is not this unit's to do: that text belongs to the review protocol, and this unit's
non-goals forbid editing the method or the protocol. It is handed to unit 20 as a record and to the
owner as a decision.
