# Walk-through — each chain build's design as presented to the owner, the forks asked, and the answers

**Serves:** research PLAY-dClosedLoop-1

The owner asked to walk the chain "design by design" before approving it (round 5, R5.3). Each
section holds one chain build's design exactly as presented, then the forks put to the owner with
their answers verbatim. A design changed by an answer is revised in place under a dated `Revised:`
line, so the presented text stays readable beside the change. Policy names and gap keys are those
of `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md` and the gap register.

## 1. dDeclaredLoop — the Spine: the loop declared once

**Purpose.** Land the contract every other chain build implements, before any of them (`[contract]`,
`[consistency]`). After it lands, "which stage does this serve, what does it hand off, what proves
the hand-off, and what is this repo's policy" each has one answer, in one file, read by one reader.

**Seams it extends, verified 2026-10-14.**
- `tools/roles/workflows.toml` (4,092 B): ten workflows with a `stage` number 0 to 7, a driver, a
  harness, roles, `enforced-by` and a trigger. It already orders the loop's middle: `orient` 1,
  `reuse` 2, `spec-write` 3, `spec-review` 4, `build` 5, `closing-review` 6, `gate-bar` 7.
- `tools/roles/house/policy.toml` (1,167 B): already a per-repo owner policy, holding role and stage
  efforts and each role's gate allowlist.
- `.governance/deploy.toml` (5,496 B): govkit's deployment answers, the place a deploy-time choice
  is recorded today.
- `memory/map/features/*.md`: every dossier's TOML fence, where a `stage` claim would sit, under the
  map's both-directions coverage ratchet.

**Planned units.**
1. **The loop definition.** A machine-readable table of the seven stages: order, entry and exit
   artifact kinds, the witness and its class, the owner gate per autonomy level, the review key, the
   roles and the workflows mapped onto each stage. `tools/roles/workflows.toml`'s stage table moves
   into it; the roles kit keeps role definitions and names stages by id.
2. **The policy file, its schema and one reader.** One authored per-repo file holding every owner
   switch in the v1 catalogue plus `hooks.bypass`; schema and defaults from the loop definition; a
   generated JSON mirror for the Node hooks and bash, held to it by a parity leg; the roles kit's
   efforts move into it.
3. **The policy guard and the default floor.** `policy.guard` and its three modes; the four default
   floor invariants (a binding verdict before the default branch moves, every policy change and
   transition recorded, the guard protecting its own switch, no witness reading actor-typed state);
   `hooks.bypass` as a policy, default `allowed`, every use recorded.
4. **The transition record.** Each stage transition recorded where history can witness it, carrying
   the agent's review recommendation and its reason, plus a micro-format line for the final message.
5. **Stage claims and the coverage gate.** A `stage` claim on every dossier, gate leg, role,
   workflow and hook; a leg that reds an unclaimed part and a stage with no witness.
6. **The witness-class rule.** Every declared witness names its class (history, hook record,
   remote verdict); the actor class is refused, and today's actor-class witnesses sit on a
   shrink-only list, each owned by the stage build that removes it.
7. **The charter's loop section.** Rendered from the loop definition and the policy file: one line
   per stage contract, and the repo's current policy values, inside the template's size gate.
8. **Policy at deployment.** govkit's intake asks the policy questions and writes the policy file,
   so a choice can be declared at deployment or switched later, as round 1 asked.

**Gaps owned.** gap-spine-01, gap-spine-02, gap-spine-06, gap-design-01.

**Parents.** dClosedLoop. **Children.** dLeasedFleet, dWitnessedBar, dRankedPlan, dIndexedDesign.

**Risks.** It touches four kits' contracts (roles, playbook, codebase-map, govkit), so every unit is
Tier-2; the charter's size gate bounds unit 7; the hooks read policy on every tool call, so unit 2's
mirror must cost no process spawn.

### Forks asked, 2026-10-14

**S1. Loop home: "Where should the loop definition live?"** Offered: New loop kit (Recommended);
Grow the roles kit; In the charter template.
Answer, in the owner's words: "The loop is the foundation of this product, it has to span and
integrate with the entire kit. Charter is the first step - it's  the first thing loaded into most
agents, so it has to clearly outline how the kit works and is used, then hand off the loop -> it's
unclear what's better in this case, what are the upsides/downsides between growing the roles kit vs
new loop kit?"
Effect: not decided; the trade-off is owed to the owner (below), and the charter is named the
loop's first step: what every agent loads first must say how the kit works and is used, then hand
off to the loop.

**S2. Policy file: "Where should the one policy file live?"** Offered: `.governance/policy.toml`
(Recommended); Extend house/policy.toml; A deploy.toml section.
Answer: `.governance/policy.toml` (Recommended).

**S3. Owner proof: "Under the default owner-only guard, how does a policy change prove that you
made it?"** Offered: Harness refusal + TTY CLI (Recommended); Signed commits; Both, signing
optional.
Answer: Harness refusal + TTY CLI (Recommended).

**S4. Transitions: "Where should stage transitions be recorded?"** Offered: Commit trailers + view
(Recommended); Per-build transition log; Card and micro-format only.
Answer, in the owner's words: "All three by default, policy can be owner-adjustable by opt-out per
option".
Effect: three records of one transition, each an opt-out policy option. To keep one fact in one
place, the commit trailer is the source; the per-build log and the micro-format line are each held
to it by a check, so three copies can never disagree silently.

### The trade-off owed for S1

| | Grow the roles kit | A new loop kit |
|---|---|---|
| Seam | `workflows.toml` already holds stage order, drivers, harnesses, roles, `enforced-by` and triggers, and `roles_lib` is already its one reader: nothing moves | the stage table moves out of `workflows.toml`, and its seven code readers are re-pointed: `roles_lib.py`, `handoff.py`, `check_roles.py`, `render_agents.py`, `adopt-roles.sh`, `kit.toml` and `tools/check-wiring.sh` (measured with `git grep -l workflows.toml`), plus three docs |
| Identity | the product's foundation sits inside a kit named for agent roles; gates, records, policies, deploy and cadence are not roles | the foundation is named for what it is, and every kit depends on it, the direction `[core]` asks for |
| Dependencies | kits with no agent in them (run-gates, drift-audit, deploy) would depend on the roles kit to read their stage or policy | every kit depends on the loop kit; the roles kit becomes one consumer |
| Contention | the roles kit is the subject of node `a`'s live build aOrientedCast (OPEN, 33 ids, active) | no overlap with any live build |
| Surface | no new kit, adopter, self-test or govkit entry | one new kit: a descriptor, an adopter, a self-test, a registry entry, a dossier and its legs, against an owner goal of curbing growth |
| Adopters | arrives with an existing kit's update | one more kit to install, which govkit can make a `requires` of every other |

A third shape splits the two along the line the loop itself draws: the loop kit owns WHAT each
stage takes in, hands out and proves, and the policies; the roles kit keeps WHO does the work, its
workflows naming loop stages by id. The roles kit then shrinks rather than grows, and the move
lands after aOrientedCast closes.

### Follow-up forks, 2026-10-14

**S1b. "Given those trade-offs, how should the loop definition be housed?"** Offered: Loop owns
what, roles who (Recommended); Grow the roles kit; One kit: loop absorbs roles.
Answer: Loop owns what, roles who (Recommended).

**S5. "Should the charter's front door (how gov works and is used, then the hand-off to the loop) be
rewritten in the Spine build instead of waiting for Convergence?"** Offered: Front door in the Spine
(Recommended); Keep it at Convergence.
Answer: Front door in the Spine (Recommended).

### Revised: 2026-10-14, after S1b, S2 to S5

The Spine's units become:
1. **The loop kit and its definition** (`tools/loop/`): the seven stages, their contracts,
   witnesses, owner gates per autonomy level and review keys. The roles kit keeps the agent roles,
   its workflows naming loop stages by id; the stage table moves out of `workflows.toml` after
   aOrientedCast closes, its seven code readers re-pointed in the same unit.
2. **`.governance/policy.toml`**, its schema, one reader, a generated JSON mirror for the Node hooks
   and bash with a parity leg, and the roles kit's efforts moved in.
3. **The guard and the default floor**: harness refusal of agent writes to the policy file; a CLI
   that changes policy only after an interactive terminal confirmation and stamps a trailer; a push
   gate that checks the trailer; the four floor invariants; `hooks.bypass` allowed by default, every
   use recorded.
4. **The transition record, three ways, each opt-out**: the commit trailer as the source; a
   per-build log and a micro-format line, each checked against the trailers.
5. **Stage claims and the coverage gate**, unchanged.
6. **The witness-class rule**, unchanged.
7. **The charter's front door**, moved here from Convergence: the charter opens with what gov is and
   how it works and is used, then hands off to the loop, its stage lines and the repo's current
   policy values rendered from the loop definition and the policy file, inside the size gate.
8. **Policy at deployment**, unchanged.

## 2. dLeasedFleet — Concurrency: who holds what, across nodes and sessions

**Purpose.** Make concurrent multi-node work visible by default and refusable by policy: every
build and unit in flight is held by a lease that names its node, its session and its write set,
and an overlap is announced before work collides (`leases`: `warn` by default, `refuse` by policy).

**Seams it extends, verified 2026-10-14.**
- Run claims: `refs/gov/runs/<slug>`, written by compare-and-swap in `tools/unattended/unattended.sh`
  (`:2070-2186`), on only where `.unattended.conf` sets `RUN_CLAIMS=on`; the `held` verdict never
  ages (`:2182`), and `node` is written from `USERNAME` (`:2410`): 17 of 17 records carry a user name,
  none a fleet tag; 8 of 17 are held, the oldest last beat 2026-10-07.
- The node registry, `tools/playbook/fleet.toml`, and its `--claim-node` verb.
- The overlap probe, `check_cross_run_overlap` (`unattended.sh:3409`), which always returns 0, and
  the kickoff card's `overlaps —` cell that prints it.
- Slug uniqueness, `check_slug_claimed` (`tools/memory-tree/gen_build_index.py:3478`), local history
  only.

**Planned units.**
1. **The lease.** One ref grammar for builds and units, carrying the fleet tag from the registry,
   the session, the branch, the declared write set, a heartbeat and an expiry, written by
   compare-and-swap. Unattended run claims migrate onto it, so one mechanism remains.
2. **Acquisition and release.** A build lease at Plan's exit, a unit lease at the Design to Build
   hand-off, in both modes; renewed on activity; released when the unit or build goes terminal or
   lands.
3. **Overlap.** At acquisition, and when a write set grows, overlap with live leases is evaluated;
   `warn` prints it on the card and in the transition record, `refuse` blocks the write; an expired
   lease can be taken over, with the takeover recorded.
4. **Fleet identity and uniqueness.** Every lease names its fleet tag, never a user name; slug and
   id uniqueness is checked against the remote's refs and unmerged branches, not local history.
5. **Offline behaviour.** When the remote is unreachable, the stated policy for leases decides
   whether work proceeds, and what reconciles on reconnection.

**Gaps owned.** gap-conc-01, gap-conc-02.

**Parents.** dDeclaredLoop. **Children.** dRankedPlan, dScopedBuild.

**Risks.** Every lease write is a network round trip, so renewal must not ride every tool call; a
lease is state the agent's own session writes, so its witness is the remote ref's history, not the
agent's word.

### Forks asked, 2026-10-14

**C1. "What should hold a lease?"** Offered: Builds and units (Recommended); Builds only; Units
only. Answer: Builds and units (Recommended).

**C2. "How should a lease stay alive?"** Offered: Activity-renewed, 24 h (Recommended); Fixed TTL,
manual renew; No expiry. Answer: Activity-renewed, 24 h (Recommended).

**C3. "What counts as an overlap between two write sets?"** Offered: Kit directories
(Recommended); Exact files; Whole builds. Answer, in the owner's words: "Kit directories, but all
of these policies, including the previous ones, should be fully owner-switchable."

**C4. "What happens when the remote is unreachable and a lease can't be read or written?"**
Offered: Warn, reconcile later (Recommended); Refuse until reachable; Follow the leases policy.
Answer, in the owner's words: "Warn by default, but should be owner-switchable".

### The meta-rule C3 states, applied backwards

Every BEHAVIOUR this walk-through settles is an owner-switchable policy: the answer is the
default, and the options offered are its allowed values. A STRUCTURAL choice (where a file lives,
which kit owns a table) is not a policy, because no repository could switch it without a
different product. Applied to the walk so far:

| Fork | Policy key | Values | Default |
|---|---|---|---|
| S3 | `policy.proof` | tty-cli, signed, both | tty-cli |
| S4 | `transitions.record` | any subset of trailer, log, micro-format | all three |
| C1 | `leases.granularity` | build-and-unit, build, unit | build-and-unit |
| C2 | `leases.renewal`, `leases.expiry-hours` | activity, fixed, none; hours | activity; 24 |
| C3 | `leases.overlap` | kit-dirs, files, builds | kit-dirs |
| C4 | `leases.offline` | warn, refuse, follow-leases | warn |

S1, S1b, S2 and S5 are structural and stay decisions.

## 3. dWitnessedBar — Test: a local verdict worth trusting, and gates reliable enough to keep

**Purpose.** Decide locally whether a change may land, in a way the pushing agent cannot quietly
fake, and make the gates reliable enough that bypassing them stops being necessary. Round 5 set
the order: `hooks.bypass` stays allowed until gate reliability is fixed, so reliability is this
build's first goal, measured, not asserted.

**Seams it extends, verified 2026-10-14** (the Test research record holds the citations).
- `tools/run-gates/run-gates.sh` and `tools/gate-legs.json`: 140 legs, 70 held (`subject=kit` or
  `chunk=selftests`) and 70 run by default; guards, profiles, per-leg ceilings, the turnstile, one
  serial retry for a timed-out leg, and `GATE_ATTRIBUTE`, which labels a red OWN, INHERITED, MIXED,
  CONTENDED or DEAD PROBE but changes no exit code.
- `.githooks/pre-commit` (a hand-named leg list) and `.githooks/pre-push` (scoped or full, a recorded
  full green reused, refusal tokens).
- `tools/run-gates/gate-fingerprint.sh`: a tree digest whose at-a-rev form hashes `$rev^{tree}`,
  content-addressed and reproducible on any node.
- `tools/run-gates/post-merge.sh` and `refs/gov/bar-red`, declared in 0 of 3 trees.
- `tools/run-gates/ceiling-evidence.txt`: 119 rows, all from node `a`; 21 legs have none.
- The landing nodes the unattended protocol names (`LANDING_NODES`), the seed of a peer verifier.

**Planned units.**
1. **Gate health, measured.** A per-leg record of passes, reds, flakes, inherited reds and wall
   time, gathered from every node, and a reliability bar stated as numbers: the condition under
   which the owner can flip `hooks.bypass` to `refused` with evidence.
2. **Bypasses recorded.** Every hook bypass is logged with its command and reason, and the next bar
   over the bypassed tree records whether it was in fact green, so bypass rate and cost feed gate
   health.
3. **Attribution that decides.** A red the base already has stops blocking an unrelated push; it is
   reported and filed as an ask against the build that owns it. Which labels block is a policy.
4. **The hook-written verdict.** Pre-push records the verdict for the tree it graded, keyed by tree
   hash and readable by every node; nothing but the hook writes it.
5. **Held self-tests off the push path.** The 70 held legs run on the peer verifier when one is
   declared, else on Maintain's cadence, which files their reds; never as a 42-minute wait at the
   push.
6. **The peer-node verifier.** The lander publishes a candidate ref; a declared fleet node other
   than the pusher re-runs the bar and the held legs for that tree and records the verdict; under
   `verdict = peer-node` the default branch moves only on that verdict. The remote-CI backend is a
   designed slot.
7. **Seen red, recorded.** A new or changed leg's first red observation is recorded, so `[gate]`
   has a witness.
8. **Flakes.** A leg that reds and then greens on one tree is recorded as a flake; past a threshold
   it is quarantined, reported but not blocking, with an ask filed.
9. **The adopter's product-test contract.** A repository declares its product tests by level,
   path selection, ceiling and flake policy, asked at intake; the bar runs and grades them by that
   declaration.
10. **Housekeeping the research found.** The pre-commit list derived from the manifest; cost
    evidence from every node; a recorded whole-bar wall time.

**Gaps owned.** gap-test-01 to gap-test-09.

**Parents.** dDeclaredLoop. **Children.** dScopedBuild, dShippedRelease, dTendedCadence.

**Risks.** Unit 3 changes what blocks a push, the most sensitive behaviour in the product; unit 6
needs a second node awake to land under `peer-node`; ten units is large enough that the build may
split at its own kickoff.

### Forks asked, 2026-10-14

**T1. "What should block a push by default?"** Offered: Own reds only (Recommended); Every red;
Own reds, mixed reported. Answer, in the owner's words: "Own reds, mixed reported by default.
Owner-adjustable."

**T2. "Where should the 70 held self-tests (84% of the bar's cost) run by default?"** Offered: Peer
node, else cadence (Recommended); At the push, selected; On demand only. Answer: On demand only.

**T3. "How should a flaky leg be handled by default?"** Offered: Record, then quarantine
(Recommended); Record only; Retry only. Answer, in the owner's words: "Record, then quarantine.
This and all previous policies are user-adjustable. This should apply to future choices as well."

**T4. "What should gov give an adopter for testing its own product?"** Offered: Declared levels +
selection (Recommended); Also ship test runners; Leave it to the adopter. Answer: Also ship test
runners.

### Revised: 2026-10-14, after T1 to T4

- Unit 3 blocks on OWN reds only; MIXED and CONTENDED are reported and filed, not blocking.
- Unit 5 keeps the held legs on demand by default; the peer verifier and Maintain's cadence are
  allowed values the owner can switch to.
- Unit 9 widens: besides the declared product-test contract, the build ships runner adapters with
  gov's guardrails built in, growing from `tools/pytest-parallel-guardrails/`.
- T3 confirms the meta-rule for every later fork: each answer is a default, each offered option an
  allowed value, and the rule is not asked again.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| T1 | `verdict.blocks` | own-mixed-contended, every-red, own-only | own-only |
| T2 | `verdict.held` | peer-or-cadence, push-selected, on-demand | on-demand |
| T3 | `verdict.flakes` | quarantine, record, retry-only; threshold | quarantine |
| T4 | `tests.product` | declared, declared-with-runners, none | declared-with-runners |

## 4. dRankedPlan — Plan: an ordered, ratified plan, a drained backlog, and dormant work disposed

**Purpose.** Give the loop its first stage: intent from any source (an owner prompt, an ask, a
Maintain finding, a Loop Review proposal) becomes a placed, ordered, ratified item, and nothing
live sits unplaced, unlabelled or abandoned.

**Seams it extends, verified 2026-10-14** (the Plan research record holds the citations).
- `tools/memory-tree/backlog.py`: the ask and disposition grammar, severities, the READY grader.
- Each build's `BACKLOG.md`, the generated family views under `memory/backlog/`, and
  `gen_build_index.py --asks`, `--ready` and `--new-build`.
- `memory/LIVE.md`'s dormancy and landed-unclosed labels.
- The build README's authored `parents:` front-matter key, rendered into the generated
  `gen:build-edges` region: cross-build dependencies exist as a grammar, declared by 11 of 167
  READMEs. Inside a build, units are ordered by the `order` verb of their spec status headers, which
  985 specs declare. No build declares a priority (0 of 167). Measured with `grep` over
  `memory/builds/*/README.md` and the spec status headers.
- `/session-kickoff`'s card, brief and route; `tools/roles/workflows.toml`, where no stage precedes
  `orient`; `memory/guides/UNATTENDED-ASKS.md`'s ask-driven runs.

**Planned units.**
1. **The plan record.** Each build declares its priority beside its `parents:` edges; the plan view
   is generated from those declarations; ratification is an owner-authorized change to them.
2. **The planner and triager role, and the Plan workflow** ahead of `orient`: drafts order,
   severities and acceptances from prompts, asks and Maintain's findings.
3. **The placement predicate.** Every non-terminal build and every open BLOCKER or HIGH ask is
   placed in the plan or disposed.
4. **The triage drain.** The 435 unlabelled asks, and the 297 deferred onto one owner-triage ask,
   receive a severity and an acceptance.
5. **Dormancy disposal.** A build dormant past the threshold is deferred as one of Maintain's safe
   fixes (round 2), and the plan view shows it.
6. **The live-build mapping, carried out** as round 3 decided and v1 tabulates.
7. **Plan Review.** A lens over order, dependencies, duplicates, overlap with live work and
   readiness, opt-in by default, with the stage-exit recommendation.
8. **Kickoff reads the plan**, and attended briefs are gated as run-built ones are.

**Gaps owned.** gap-plan-01 to gap-plan-07.

**Parents.** dDeclaredLoop, dLeasedFleet. **Children.** dTendedCadence.

**Risks.** Unit 4 asks the owner to ratify hundreds of labels, so its batching decides whether it
ever finishes; unit 6 changes the status of other nodes' builds and runs only with the owner's
ratification.

### Forks asked, 2026-10-14

**P1. "Where should the plan's order live?"** Offered: Front matter + generated view
(Recommended); One authored plan file; Both, checked. Answer: Front matter + generated view
(Recommended).

**P2. "What should happen to live work that isn't placed in the plan?"** Offered: Warn everywhere
(Recommended); Refuse new builds; Report in Plan Review only. Answer: Warn everywhere
(Recommended).

**P3. "How should the existing backlog (435 unlabelled asks, 297 of them deferred onto one
owner-triage ask) be triaged?"** Offered: Drafted, ratified in batches (Recommended); Auto-label by
rules; Archive the legacy, triage new. Answer: Auto-label by rules.

**P4. "How should kickoff use the plan?"** Offered: Offer the next item (Recommended); Plan is
binding; Plan is advisory. Answer: Offer the next item (Recommended).

### Revised: 2026-10-14, after P1 to P4

Unit 4 becomes a rule-based labeller: rules over an ask's age, source, citations and the code
assign severity and draft acceptance with no owner step, and the owner reviews only results graded
HIGH or BLOCKER. The rules are declared and owner-switchable, and every label records the rule
that set it, so a wrong rule is found by its label, not by re-reading 435 asks.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| P1 | structural | — | front matter plus a generated view |
| P2 | `plan.unplaced` | warn, refuse-new, review-only | warn |
| P3 | `plan.triage` | owner-batches, rules, archive-legacy | rules |
| P4 | `plan.kickoff` | offer-next, binding, advisory | offer-next |

## 5. dIndexedDesign — Design: a ready spec set, coherent across builds, reviewed by policy

**Purpose.** Make the Design stage's exit a fact computed from the specs rather than a status an
agent types, make collisions between live designs visible before anyone builds, and keep the
spec's claims about reuse and alternatives honest.

**Seams it extends, verified 2026-10-14** (the Design research record holds the citations).
- `plan_state` in `tools/unattended/unattended.sh` (`:4411`): computes MISSING, THIN, FORKED or READY
  from the spec; `--dispatch` refuses only MISSING and THIN.
- `checkBuildable` in `tools/hooks/scratch-guard.js` (`:870-912`): admits a route on status and tier
  alone, and INPROGRESS is a value the agent writes; TOOL-dNarrowedAnchor-1 is INPROGRESS and
  FORKED today.
- `read_files_touched` and `check_cross_run_overlap` (`unattended.sh:3389`, `:3409`): the join the
  index needs exists, pointed only at unmerged remote refs.
- `memory/TEMPLATE-SPEC.md` (sections, §8 forks, §10 reuse), `memory/guides/BUILD-METHOD.md` (M1
  to M5, M12), `tools/check-spec-tokens.py`, hygiene check 12.
- `tools/workflows/tier2-review.js`'s five spec lenses, and agent-cap rule 0, which refuses an
  undeclared audit.

**Planned units.**
1. **The hand-off witness.** Design to Build is admitted when the unit's state, derived from its
   committed spec, is READY: no open fork, not thin, not missing. INPROGRESS becomes derived from
   the transition record instead of typed.
2. **The design index.** A generated join of every live spec's Files touched, at the granularity
   `leases.overlap` names, across builds on the default branch and the remote's unmerged branches;
   an overlap no spec acknowledges in its §3 Edges is announced at spec-write and kickoff.
3. **Design review by policy.** `review.design` opt-in by default with its effort, the stage-exit
   recommendation, and the audit opt-in guard re-pointed at the policy file.
4. **Honest reuse and alternatives.** A spec's §10 carries the probe it ran and that probe's output
   digest, which a check re-derives; a Tier-2 spec that chose between mechanisms records the ones it
   rejected.
5. **Research with a home.** The research workflow gets a harness and its records a binding, as this
   build's own research did by hand; the reuse scout's finding is recorded.
6. **Agreement and tier checks.** The deterministic half of M2's sub-spec agreement, and the tier
   rule as a predicate over the change's class.

**Gaps owned.** gap-design-02 to gap-design-07, gap-design-09.

**Parents.** dDeclaredLoop. **Children.** dScopedBuild.

**Risks.** Unit 1 can strand units that are INPROGRESS today in a FORKED state, so it lands with a
list of them and their owners; unit 4's digest must survive line-ending differences between nodes.

### Forks asked, 2026-10-14

**D1. "What should the Design-to-Build hand-off require by default?"** Offered: Derived READY
(Recommended); READY plus a Tier-2 audit; Status and tier, as today. Answer: Derived READY
(Recommended).

**D2. "When two live designs touch the same area and neither acknowledges it, what's the
default?"** Offered: Warn at spec-write and kickoff (Recommended); Refuse until acknowledged; Index
view only. Answer: Warn at spec-write and kickoff (Recommended).

**D3. "Spec audits have never come back clean (0 of 254; 170 BLOCKED), and specs are much of why
57% of commits are records. What should happen to the spec format?"** Offered: Measure, then trim
(Recommended); Lighter format now; Keep the format. Answer, in the owner's words: "Measure first
and emit recommendations. Specs should definitely be measured and perhaps reworked, but trimming
should not be the only option. Specs should be redesigned to ensure they give precise,
deterministic, structured instructions to build more precise, better features. Specs should come
with clear designs, boundaries, definitions."

### Revised: 2026-10-14, after D1 to D3

A seventh unit joins, and it is the build's largest:

7. **The spec, redesigned as a structured contract.** Measure the current format first: which
   sections the 254 audits' findings land in, which sections builders diverge from, how often a
   unit is reworked after its spec, and what a spec costs to write and to audit; emit
   recommendations from that measurement. Then redesign the spec so it hands a builder precise,
   deterministic, structured instructions: definitions of the terms it uses, the design, the
   boundaries (what the unit may touch, its invariants, what it must not change), the interfaces it
   takes and produces, and acceptance as observations with their commands. Those parts become
   structured fields the builder follows and the checks read; prose explains them, never replaces
   them. The new format is trialled against the old on real units before it becomes the default,
   and both formats stay readable while the corpus migrates.

The measurement half of unit 7 belongs to this build, not to Review's value ledger: spec quality is
a Design-stage question, and the ledger's gate, rule and bug-class prices are Review's.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| D1 | `design.handoff` | derived-ready, ready-plus-audit, status-and-tier | derived-ready |
| D2 | `design.overlap` | warn, refuse, index-only | warn |
| D3 | structural | — | measure, recommend, redesign as a structured contract |

## 6. dScopedBuild — Build: one exit contract for both modes, scope bound to the unit, one worktree each

**Purpose.** Make attended and unattended builds finish under the same contract, witnessed by
committed history at the push, and make each unit's write scope and workspace its own.

**Seams it extends, verified 2026-10-14** (the Build research record holds the citations).
- `DOD_CORE` in `tools/unattended/unattended.sh` (`:868`), the 13-item definition of done whose
  `closing-review-recorded` needs RUN.md's pinned base (`:11662-11665`).
- `tools/memory-tree/routed_commits.py`: a product commit must name a specced unit, any unit.
- `checkRouted` and `checkBuildable` in `tools/hooks/scratch-guard.js` (`:1113-1200`): any routed,
  buildable unit admits any write under `ROUTED_PATHS`; Bash and PowerShell writes pass.
- `.claude/skills/build/SKILL.md`, `tools/workflows/unattended-unit.js`, the gov-builder role;
  `tools/workflows/tier2-review.js` for the closing review.
- `memory/guides/BUILD-METHOD.md` M6 to M9; the charter's `[isolate]`, which no tool implements.

**Planned units.**
1. **One exit contract.** `DOD_CORE` generalised to both modes, with the build's base derived from
   history (the parent of its first pass commit) instead of RUN.md, evaluated at the push.
2. **Scope at the push.** A commit's product paths must fall inside its unit's declared write set
   at the granularity `leases.overlap` names (kit directories by default), behind a cutoff for
   history: 7.2% of past commits stray at kit level.
3. **The closing review, recorded.** `review.build` is owed by default (round 2): a build whose
   units close in the pushed range needs a review record naming a commit in that range.
4. **A worktree per unit.** The harness creates and removes one per unit dispatch, so disjoint units
   run in parallel without git's index lock.
5. **A write gate that reads derived state.** The gate admits a write when the unit's derived state
   and its lease allow it, not on a route and status the agent typed; shell writes are covered.
6. **The per-pass checklist, witnessed.** The bug-class checklist run after each pass leaves a
   trailer, or the step is dropped as unenforceable.

**Gaps owned.** gap-spine-03, gap-conc-03, gap-build-01 to gap-build-04.

**Parents.** dIndexedDesign, dLeasedFleet, dWitnessedBar. **Children.** dConvergedCharter.

**Risks.** Unit 5 replaces the write gate's decision path, which every product write crosses;
unit 4 multiplies worktrees on Windows, where removal leaves skeletons the cleanup kit knows.

### Forks asked, 2026-10-14

**B1. "When a commit writes outside its unit's declared kit directories, what's the default at the
push?"** Offered: Warn and file an ask (Recommended); Refuse at kit level; Report only. Answer:
Warn and file an ask (Recommended).

**B2. "Where should a unit's work happen?"** Offered: One per unit (Recommended); Only for parallel
units; Shared, as today. Answer, in the owner's words: "shared by the default, owner-adjustable."

**B3. "When is the closing review owed?"** Offered: Once per build (Recommended); Per unit; Per
landing. Answer: Once per build (Recommended).

### Revised: 2026-10-14, after B1 to B3

Unit 4 ships the per-unit worktree as an allowed value, not the default: units share the build's
worktree unless the owner switches `build.worktree`; the harness's parallel dispatch still needs
disjoint write sets, which the lease's write set now states.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| B1 | `build.scope` | warn-and-ask, refuse, report | warn-and-ask |
| B2 | `build.worktree` | per-unit, parallel-only, shared | shared |
| B3 | `review.build.when` | per-build, per-unit, per-landing | per-build |

## 7. dShippedRelease — Deploy: landing, distributing gov, and releasing an adopter's product

**Purpose.** Give Deploy all three of its senses a contract: a landing that records what moved and
on what verdict; gov's kits released and kept current in every adopter; and an adopter's own
product released, deployed, verified and rolled back by tooling gov ships (round 1: ship deploy
tooling; round 3: a generic engine plus adapters, the first fitted to incms).

**Seams it extends, verified 2026-10-14** (the Deploy research record holds the citations).
- `tools/push-main.sh` (attended, `--prepare`, `--land`, `--carry`; kit mints; regeneration; the
  post-merge bar), `.githooks/pre-push`, `tools/run-gates/post-merge.sh` and `refs/gov/bar-red`.
- `tools/govkit/govkit.py` (selfcheck, intake, plan, apply, check, update, adopt, epoch, mint,
  contribute), `tools/govkit/registry.toml` and its entries, the per-kit `adopt-*.sh`, the receipt
  (`.governance/install.json`, `install.sums`) and `tools/run-gates/check-receipt.py`, which checks
  integrity, not currency; `skills/deploy-governance/`.
- incms's own deploy surface, built outside gov: `infra/deploy.sh`, `infra/deploy-native.sh`,
  `infra/fleet-roll.sh`, `infra/docker-compose.yml`, `infra/systemd/`, `infra/nginx/`, and the
  workflows `release.yml` (a signed GHCR image pair and a signed channel manifest),
  `sign-release.yml` and `restore-drill.yml`.
- `memory/builds/aDeployScout/spec/governance-deployer-research.md`, whose CI riding was never built.

**Planned units.**
1. **The landing record.** Each landing records the SHA, the builds and units it carried and the
   verdict it moved on; landing review is opt-in with the stage-exit recommendation; the autonomy
   level decides whether the owner authorizes it.
2. **Kit releases with notes.** A kit mint carries release notes generated from the units that
   changed the kit since its last version.
3. **The deploy engine** (a new kit): declared environments and their promotion order, a versioned
   and signed release artifact, a deploy step, a verify step, a rollback step, and optional canary
   and fleet-roll steps; every step writes its verdict for the SHA.
4. **The first adapter**, fitted to incms: signed container images, compose and systemd hosts,
   rolling fleet updates, restore drills; incms becomes its first consumer.
5. **The fleet register and currency watch.** A register of adopters and the gov commit each runs;
   Maintain's cadence reports how far behind each is; outbox orders are graded.
6. **Lander hardening.** A killed hook detected rather than reported afterwards; hooks-path drift
   refused; the lander kit versioned, with its dependency on the bar's kit declared.
7. **Emitted CI, optional.** For an adopter that has CI, govkit can emit a job that runs the bar and
   the deploy engine's verify; a designed slot for gov itself.
8. **A runbook derived from the descriptors**, replacing 163 KB of narrative with generated pages.

**Gaps owned.** gap-deploy-01 to gap-deploy-08.

**Parents.** dWitnessedBar. **Children.** dConvergedCharter.

**Risks.** Unit 3 is a new product surface for systems gov does not run, so it needs the strongest
review of the chain; unit 4 changes how a production adopter ships, so it lands in incms only with
that repository's own owner go.

### Forks asked, 2026-10-14

**DP1. "Where should the deploy engine run by default?"** Offered: Landing node, after verdict
(Recommended); In the adopter's CI; Operator-run. Answer: Landing node, after verdict
(Recommended).

**DP2. "Who approves a promotion into production by default?"** Offered: You approve prod
(Recommended); Auto on green verify; You approve every environment. Answer, in the owner's words:
"Auto on green by default, owner-adjustable".

**DP3. "What happens by default when a deploy's verify step fails?"** Offered: Roll back, file an
ask (Recommended); Halt and alert; Roll forward only. Answer, in the owner's words: "Roll forward by
default, owner adjustable".

**DP4. "How should adopters stay current with gov by default?"** Offered: Pull + currency watch
(Recommended); Push update branches; Pull only, as today. Answer: Pull + currency watch
(Recommended).

### Revised: 2026-10-14, after DP1 to DP4

The engine promotes through every environment, production included, on a green verify, and a
failed verify is recorded for its SHA and fixed forward; owner approval of production and
automatic rollback ship as allowed values. Because nothing stops a bad release by default, the
verify step's record is the one place a failure is seen: it files an ask and joins the loop
metrics, so roll-forward never means unrecorded.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| DP1 | `deploy.runs` | landing-node, adopter-ci, operator | landing-node |
| DP2 | `deploy.promotion` | owner-approves-prod, auto-on-green, owner-approves-each | auto-on-green |
| DP3 | `deploy.on-verify-fail` | rollback-and-ask, halt-and-alert, roll-forward | roll-forward |
| DP4 | `deploy.currency` | pull-and-watch, push-branches, pull-only | pull-and-watch |

## 8. dTendedCadence — Maintain: a cadence, a mandate, safe fixes, and detectors that are owned

**Purpose.** Give the loop a stage that runs without anyone asking: on a cadence, under a
maintenance mandate, it applies the declared safe fixes (round 2), binds every detector to a pin
and an owner, closes what is finished or abandoned, and files the rest into Plan.

**Seams it extends, verified 2026-10-14** (the Maintain research record holds the instruments).
- `tools/drift-audit/drift_report.py`: 27 signals with liveness assertions, 15 nonzero today, most
  report-only, two dead probes.
- `tools/process-monitor/reap.py`, `tools/branch-reconcile/branch_reconcile.py` (`/cleanup`): the
  actuators for reaping and pruning, each run by hand today.
- Recipe mode in `tools/unattended/` (`check-playbook.sh`, `PLAYBOOK-TEMPLATE.template.md`; the
  `playbook-mode` dossier, status `building`; dScriptedRepeat SPECCED): an authorization discipline
  for repeatable work.
- The unattended kit's keepalive and resume ticks registered through `CronCreate`, which live only
  as long as a session does.
- `memory/LIVE.md`'s dormancy label; 89 live `RUN.md` files, 10 of them for merged work.

**Planned units.**
1. **The maintenance recipe.** A playbook in recipe mode: run the detectors, apply the safe fixes
   the mandate allows, draft triage under Plan's rules, file every other finding as an ask, record
   the run.
2. **The cadence and its host.** Where and how often the recipe runs is a policy; the build ships
   the hosts the owner keeps.
3. **The safe-fix set**, declared and owner-switchable: reap stale processes, prune landed branches
   and worktrees through `/cleanup`'s write mode, regenerate stale outputs, defer builds dormant past
   the threshold, land records-only fixes, close finished run records; the currency probe and the
   backlog's rule-based labelling ride the same run.
4. **Detectors with owners.** Every drift signal carries a pin and the stage that owns its breach; a
   breach is handled by policy; dead probes are fixed or removed.
5. **Map freshness.** Dossiers older than their paths are refreshed or proposed for refresh.
6. **The maintenance record.** Each run records what it checked, what it fixed and what it filed,
   so the Loop Review can read the loop's health over time.

**Gaps owned.** gap-maint-01, gap-maint-02, gap-maint-05 to gap-maint-08.

**Parents.** dWitnessedBar, dRankedPlan. **Children.** dCalibratedLens.

**Risks.** A run that mutates with no owner turn must stay inside its declared fix set, so the set
is checked against what the run's commits touched; with no always-on host, a cadence is only as
regular as the host the owner picks.

### Forks asked, 2026-10-14

**M1. "With no always-on server, where should the maintenance cadence run by default?"** Offered:
At session start (Recommended); OS scheduler on a node; Cloud routine. Answer, in the owner's
words: "At session start, other options in-scope owner-adjustable".

**M2. "How often should maintenance run by default?"** Offered: Daily (Recommended); Weekly; Every
session. Answer: Daily (Recommended).

**M3. "When a detector breaches its pin, what's the default?"** Offered: File an ask for its stage
(Recommended); Red a leg; Report only. Answer: File an ask for its stage (Recommended).

### Revised: 2026-10-14, after M1 to M3

Unit 2 ships three hosts, not one: the session-start host is the default, and the OS scheduler and
the cloud routine are in scope as switchable values, the cloud host limited to what it can reach
from the remote. A maintenance lease, from dLeasedFleet, keeps two nodes from running the same
day's maintenance.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| M1 | `maintain.host` | session-start, os-scheduler, cloud-routine | session-start |
| M2 | `maintain.cadence` | daily, weekly, every-session | daily |
| M3 | `maintain.on-breach` | file-ask, red-leg, report | file-ask |

## 9. dCalibratedLens — Review: review where it pays, recommended everywhere, and a loop that prunes itself

**Purpose.** Give every stage a review the owner can switch on and size, make every transition
carry the agent's reasoned recommendation, and give the loop its one missing feedback: a Loop
Review that reads what each gate, rule and bug class has caught and cost, and retires what does not
pay (round 3: value ledger plus retirement plus budgets).

**Seams it extends, verified 2026-10-14.**
- `tools/workflows/tier2-review.js` (finder lenses, batched skeptics, one synthesis; spec and diff
  modes) and `memory/guides/REVIEW-PROTOCOL.md`; the diff reviewer, spec reviewer, skeptic and
  synthesizer roles; agent-cap rule 0, the audit opt-in guard.
- `GATE_ATTRIBUTE`'s OWN label, the nearest thing to "this gate caught something"; the per-node
  gate ledger; `tools/run-gates/ceiling-evidence.txt` for cost.
- The 122 bug classes under `memory/gotchas/` and `tools/memory-tree/gotchas.py`; the charter's
  `[left-shift]` rule, today the loop's only way of correcting itself.
- The transition record (dDeclaredLoop), the gate-health record (dWitnessedBar) and the maintenance
  record (dTendedCadence): the metrics the Loop Review reads.

**Planned units.**
1. **Review by policy, per stage and effort.** `review.<stage>` and its effort read by every review
   harness; the closing review owed by default, everything else opt-in.
2. **The stage-exit recommendation.** A micro-format line and a trailer carrying the agent's
   recommendation and reason before every transition; advice by default, binding by policy.
3. **Lenses for the stages that have none.** Plan (order, dependencies, duplicates, readiness), Test
   (seen red, arms, cost, flakes), Deploy (what landed against the plan, release notes against the
   epoch, adopter updates), Maintain (fixes inside the declared set, detectors owned).
4. **The value ledger.** For each gate leg, charter rule and bug class: what it caught (an OWN red,
   a review finding citing it), what it cost (wall time, tokens), and when it last caught anything;
   shared across nodes, not per node.
5. **The Loop Review.** A periodic retrospective over stage cycle times, review yield, bypass counts,
   records overhead and surface size against budgets; it files proposals (retire, merge, demote a
   gate, rule or class; change a stage contract) into Plan.
6. **Budgets and review cost.** Owner-switchable caps on legs, guide bytes and registry rows, and a
   records-overhead ceiling; review batching and lens selection guided by the recommendation.

**Gaps owned.** gap-review-01 to gap-review-03, gap-maint-03, gap-design-08.

**Parents.** dTendedCadence. **Children.** dConvergedCharter.

**Risks.** A retirement removes a guard, so the ledger's catch count must be one nobody can inflate
or deflate from their own session; the ledger starts empty, so nothing should retire before it has
a full window of evidence.

### Forks asked, 2026-10-14

**R1. "How often should the Loop Review run by default?"** Offered: Monthly (Recommended); Weekly;
Every N landings. Answer, in the owner's words: "Weekly by default, owner-adjustable".

**R2. "When the Loop Review finds a gate, rule or bug class that caught nothing in its window,
what's the default?"** Offered: Propose, you ratify (Recommended); Demote, then propose; Report
only. Answer: Propose, you ratify (Recommended).

**R3. "How long a window without a catch makes something a retirement candidate by default?"**
Offered: 60 days (Recommended); 90 days; 30 days. Answer, in the owner's words: "60 days def,
owner-adjustable".

**R4. "What should the governing-surface budgets be by default?"** Offered: Cap at today's size
(Recommended); Shrink targets; Measure, no caps. Answer, in the owner's words: "rederive the caps,
currently it's uncertain how meaningful the caps are. Caps often get in the way of work but it's
clear caps are needed to prevent bloat."

### Revised: 2026-10-14, after R1 to R4

Unit 6 becomes **caps re-derived from evidence**. Inventory every cap the product enforces today
(the charter's 48 KiB size gate, the build README slot budgets, the guide and dossier caps, the
kickoff card's 8,192-byte cap, the entry budgets, the shrink-only pins), measure for each how often
it blocked work and how often it stopped growth that would otherwise have landed, and re-derive
each value and its mode from that evidence: a hard cap where bloat is the real risk, a soft cap
that warns and asks for a recorded reason where blocking costs more than it saves. New budgets on
legs, guide bytes, registry rows and records overhead are derived the same way, never typed.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| R1 | `review.loop.cadence` | weekly, monthly, every-n-landings | weekly |
| R2 | `review.loop.retire` | propose-ratify, demote-then-propose, report | propose-ratify |
| R3 | `review.loop.window-days` | days | 60 |
| R4 | `budgets.*` | each cap's value and mode, hard or soft | re-derived from evidence |

## 10. dConvergedCharter — Convergence: one product, its parts consolidated, the superseded retired

**Purpose.** Finish the convergence the earlier builds make possible: the charter regrouped around
the loop with gov's own rules split into gov's overlay, the protocol text consolidated and derived,
record kinds consolidated against the records-overhead metric, superseded legs, rules and builds
retired through the Loop Review, and every adopter moved onto the converged loop. The charter's
front door already moved to the Spine (S5).

**Seams it extends.** The charter template and its renderer (`coding-governance-agents.template.md`,
`tools/playbook/`, the 48 KiB size gate and its high-water); the guides under `memory/guides/`
(301 KB) and `WIRE-INTO-PROJECT.md` (163 KB); the memory tree's record kinds
(`memory/HYGIENE.md`); govkit's `update` and the receipts; every earlier chain build's outputs.

**Planned units.**
1. **The charter regrouped.** Section 1's rules grouped by the stage they govern, each one line
   tagged with its stage; rules that govern only gov move to gov's overlay; the current policy
   values rendered.
2. **Protocol text derived.** Every guide sentence that states a fact the loop definition, a policy
   or a kit descriptor already holds is replaced by a rendered pointer; prose stays only for
   rationale, per stage, inside a re-derived budget.
3. **Records consolidated.** Record kinds that answer one question merge; bookkeeping folds into
   the pass commit where it can; the records-overhead metric is brought under its ceiling.
4. **Superseded parts retired.** Legs, rules, bug classes and builds that the chain made redundant
   are retired through the Loop Review's ratified proposals, never by assertion.
5. **Adopters migrated.** Each adopter moves to the converged loop through govkit, with its own
   owner's go.

**Gaps owned.** gap-spine-04, gap-spine-05, gap-maint-04.

**Parents.** dScopedBuild, dShippedRelease, dCalibratedLens, and through them every chain build.

**Risks.** It edits every governing surface at once, so it lands in small units behind the Loop
Review's ratifications; adopters run production systems and migrate only on their owners' go.

### Forks asked, 2026-10-14

**CV1. "Where should the charter's gov-only rules go?"** Offered: Gov's overlay (Recommended);
Shipped, tagged gov-only; Leave them as they are. Answer, in the owner's words: "any adopter rules
(including gov's own - gov is an adopter just like any other) should render from its own
set/overlay. However, charter is the foundation - project-specific global rules should render as a
separate block."

**CV2. "What should happen to the 301 KB of guides and the 163 KB runbook?"** Offered: Derive and
consolidate (Recommended); Index only; Rewrite per stage. Answer, in the owner's words: "Derive and
consolidate, any non load-bearing prose should be gone. Any protocol/method/runbook should only
carry clear facts/definitions/policies/descriptors. In addition, any '§' references should be
retired and structure should be transitioned to TAGS (eg. '[Task];[Orientation]) which clearly
define sections and survive reordering."

**CV3. "How should records be consolidated (57% of commits touch only memory/)?"** Offered: Merge by
evidence (Recommended); One record per stage; Leave records as is. Answer: Merge by evidence
(Recommended).

### Revised: 2026-10-14, after CV1 to CV3

- **Every adopter is an adopter, gov included.** The charter is the shared foundation; each
  repository's own rules render from its own overlay as a separate project block beneath it. Gov's
  rules move to gov's overlay like any adopter's.
- **Protocol text carries facts, definitions, policies and descriptors only.** Prose that bears no
  load is removed, not condensed.
- **Tags replace `§` references.** Sections are named by tags that define them and survive
  reordering (the owner's example: `[Task]`, `[Orientation]`), as the charter's rules already are
  (`[yagni]`, `[reuse]`). Because the Spine writes the charter's front door and Design redesigns
  the spec, the tag grammar and its resolver land in the SPINE, the spec redesign uses them, and
  Convergence migrates every remaining `§` reference. The grammar's resolver is a check: a tag
  reference that names no section reds, so tags cannot dangle the way positional references do.
- **Interpretation to confirm at chain approval:** other positional section references, such as
  numbered method steps (`M5`), numbered spec sections and numbered hygiene checks, carry the same
  defect the owner named for `§`, so Convergence inventories them as candidates for tags.

| Fork | Policy key | Values | Default |
|---|---|---|---|
| CV1 | structural | — | foundation plus a per-repo overlay block, gov included |
| CV2 | structural | — | derived facts only; tags replace `§` |
| CV3 | structural | — | merge record kinds by evidence |

## Chain approval, asked after architecture v2 (2026-10-14)

**A1. "Approve the ten-build chain as walked (architecture v2)?"** Offered: Approve (Recommended);
Approve, splitting the big ones; Not yet ("Something needs another pass first. Say what under
Other."). Answer: Not yet, with no area named.
Effect: the chain is not approved; no spec is written and no chain build opens until the owner
names what needs another pass and it has had one.

**A2. "You asked for § references to be replaced by tags. Do other positional references count
too: numbered method steps such as M5, numbered spec sections, numbered hygiene checks?"** Offered:
Yes, all positional refs (Recommended); Only §. Answer: Yes, all positional refs (Recommended).
Effect: v2's open interpretation is confirmed. Every positional section reference is migrated to a
tag by Convergence, and new text from the Spine onward uses tags only.
