# Design rounds — every question put to the owner, its options, the answer verbatim, and what it changed

**Serves:** research PLAY-dClosedLoop-1

The owner's answers are the decisions this build records. Each round is written the moment it
returns. Options are quoted as offered, and an answer the owner typed in place of an option is
quoted in their words. The proposal the rounds start from is
`build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v0.md`.

## Round 1 — foundations (2026-10-14, session 1799cb98)

### R1.1 Scope: "What loop does the product govern?"

- Offered: **Any repo's loop (Recommended)**: gov ships the loop itself as the product; any
  adopting repo runs Plan through Maintain under it; gov's own repo becomes adopter zero with a thin
  overlay, and gov-only rules move out of the shipped charter.
- Offered: **Gov's own loop first**: converge gov's own development loop now, and generalise it for
  adopters in a later build.
- **Answer:** Any repo's loop (Recommended).
- **Effect:** v0's P8 holds. The loop is the product; gov's repository is adopter zero; rules that
  govern only gov leave the shipped charter for gov's overlay.

### R1.2 Deploy: "What should the Deploy stage mean for an adopter's own product?"

- Offered: **Contract + declared steps (Recommended)**: gov defines release, deploy, verify and
  rollback; the adopter declares its own steps; emitted CI runs them; gov grades each SHA's verdict
  and never implements deployment itself.
- Offered: **Ship deploy tooling**: as above, and gov also ships kits for environments, promotion,
  canaries and rollback that adopters install.
- Offered: **Landing and distribution only**: Deploy means landing and distributing gov's kits; an
  adopter's product release stays outside gov.
- **Answer:** Ship deploy tooling.
- **Effect:** wider than v0. Gov defines the Deploy contract AND ships deploy kits (environments,
  promotion, canaries, rollback) that an adopter installs, so the Deploy chain build carries a new
  kit family. The kits must stay stack-agnostic, so an adopter's own steps plug into them.

### R1.3 Verdict: "Where should the binding verdict live, meaning the check that decides whether the default branch may move?"

- Offered: **Remote verifier (Recommended)**: the lander pushes to a staging ref; CI runs the full
  bar, the held self-tests and the product tests; only a green verdict moves the default branch.
- Offered: **Local hook stays binding**: pre-push decides; CI's reds block the next push through a
  published ref.
- Offered: **Hybrid by repo**: gov keeps a local binding bar on its Windows nodes; adopters get a
  remote required check.
- **Answer, in the owner's words:** "Local hook by default and remote verifier if declared by owner
  at deployment or through a config switch."
- **Effect:** v0's P3 becomes a per-repo policy. The local hook binds by default; the remote
  verifier binds wherever the owner declares it at deployment (an intake answer) or flips a config
  switch later. Both verdict paths ship, and the stage witnesses must read whichever one binds.

### R1.4 Autonomy: "Which stage transitions should still need you, the owner?"

- Offered: **Three gates (Recommended)**: the owner ratifies the plan's order, gives each build's
  design its go, and authorizes landings or a standing mandate does.
- Offered: **Plan only**: after plan ratification, agents run Design through Deploy under a standing
  mandate.
- Offered: **Every stage**: every stage transition asks the owner.
- **Answer, in the owner's words:** "Three gates by default, but each mode should be
  owner-switchable by repo - plan only, three gates, every stage."
- **Effect:** autonomy becomes a per-repo level with three values, `plan-only`, `three-gates` (the
  default) and `every-stage`, switchable by the owner.

### What round 1 changed

- **New principle P10, policy per repo.** The loop definition carries each policy's default; each
  repository's policy file carries its choices, set at deployment and switchable later; nothing else
  restates them. Two policies so far: where the binding verdict lives, and the autonomy level.
- **Deploy widens** from a contract to a contract plus shipped deploy tooling.

## Round 2 — how the stages run (2026-10-14, session 1799cb98)

### R2.1 Review: "How should Review be owed across the stages?"

- Offered: **Risk-tiered, on (Recommended)**: deterministic checks at every stage; agent review owed
  by risk tier, the Tier-2 spec audit and closing review on by default in both modes, a per-repo
  policy widening or narrowing it.
- Offered: **Every stage, every build**: every stage runs its agent review on every build.
- Offered: **Opt-in as today**: agent reviews only where a build declares them.
- **Answer, in the owner's words:** "Opt-in as today by default, except for the closing review, but
  fully owner-switchable by stage and effort. In addition, an agent reasoning check per stage -
  agents should decide and emit a recommendation whether a review is needed before moving to the
  next step."
- **Effect:** agent review stays opt-in by default at every stage except Build, whose closing review
  is owed by default in both modes. Each stage's review is switchable by the owner, and so is the
  effort it runs at. NEW MECHANISM: at every stage exit the agent reasons about whether a review is
  needed and emits a recommendation before moving to the next stage, so an opt-in review is never
  skipped silently.

### R2.2 Concurrency: "How hard should concurrency control be across nodes and sessions?"

- Offered: **Leases that refuse (Recommended)**: a remote lease with the fleet tag, a heartbeat and
  an expiry before writing; an unacknowledged overlap refused; a per-repo switch relaxing it.
- Offered: **Leases that warn**: leases recorded and shown at kickoff; overlap warns only.
- Offered: **No leases**: today's advisory probe.
- **Answer, in the owner's words:** "Leases that warn by default, but owner-switchable to refusal."
- **Effect:** leases ship in both modes; overlap warns by default; refusal is a per-repo switch.

### R2.3 Maintain: "What may a scheduled maintenance run do without an owner turn?"

- Offered: **Report and file asks (Recommended)**: detectors, triage and dormancy drafts, asks
  filed; anything that changes code, deletes or closes a build waits.
- Offered: **Also apply safe fixes**: as above, plus reaping stale processes, pruning landed
  branches and worktrees, regenerating stale outputs, closing builds dormant past a threshold, and
  landing records-only fixes under a maintenance mandate.
- Offered: **Owner-triggered only**: no schedule.
- **Answer:** Also apply safe fixes.
- **Effect:** wider than v0. Maintain runs on a cadence under a maintenance mandate and applies the
  named safe fixes itself; the set of fixes it may apply is a declared, owner-switchable list.

### R2.4 Plan: "Who orders the plan?"

- Offered: **Planner drafts, you ratify (Recommended)**: a planner/triager role drafts order,
  priorities and dependencies; the order binds once the owner ratifies it; between ratifications
  the planner may add but not reorder.
- Offered: **Planner orders within themes**: the owner sets themes and priorities; the planner
  orders within them.
- Offered: **You order directly**: the owner writes the plan; agents only propose.
- **Answer, in the owner's words:** "Planner drafts, owner ratifies by default, but all three modes
  should be switchable per repo. This should be an overall recurring theme to the product - it
  should be flexible and configurable."
- **Effect:** the plan-authority mode is a per-repo policy with three values; the planner-drafts,
  owner-ratifies mode is the default.

### What round 2 changed

- **P10 becomes the product's central principle: flexible and configurable.** Every policy carries a
  sensible default in the loop definition and is owner-switchable per repo, and where it matters per
  stage and per effort. The policies so far: verdict location, autonomy level, review per stage and
  its effort, concurrency strictness, maintenance fix set, plan authority.
- **A stage-exit review recommendation** is new: the agent emits whether a review is needed before
  each transition, which makes an opt-in review a reasoned choice rather than a default nobody saw.
- **Maintain acts**, within a declared fix set, under its own mandate.

## Round 3 — deploy tooling and convergence (2026-10-14, session 1799cb98)

Asked after reading the adopters' deploy surfaces: `incms` runs signed GHCR container releases, a
compose and systemd host fleet rolled by `infra/fleet-roll.sh`, and restore drills
(`.github/workflows/release.yml`, `sign-release.yml`, `restore-drill.yml`, `infra/deploy.sh`), all
built outside gov; `nicocares` carries a `ci.yml` only.

### R3.1 Deploy kit: "What shape should gov's shipped deploy tooling take?"

- Offered: **Generic engine + adapters (Recommended)**: a stack-agnostic deploy kit (declared
  environments and promotion order, signed release artifacts, health verification, rollback,
  optional canary and fleet-roll steps), its first adapter fitted to what incms already runs, so
  incms is its first consumer.
- Offered: **Extract incms's pipeline**: lift incms's workflows into a kit as-is, generalise later.
- Offered: **Generic engine only**: the engine and the declared-step contract; adapters are the
  adopter's own.
- **Answer:** Generic engine + adapters (Recommended).

### R3.2 Pruning: "How should gov keep its own governing surface from only growing?"

- Offered: **Value ledger + retirement (Recommended)**: every gate, rule and bug class records what
  it caught and what it costs; the Loop Review retires or merges any that caught nothing in a
  declared window; budgets cap legs, guide bytes and registry rows; all owner-switchable.
- Offered: **Budgets only**. Offered: **No pruning**.
- **Answer:** Value ledger + retirement (Recommended).

### R3.3 Live builds: "What happens to the 24 non-terminal builds (20 of them dormant) when the chain opens?"

- Offered: **Map, freeze dormant (Recommended)**: each live build mapped to the chain build covering
  its area; dormant ones set to DEFERRED with their asks re-homed to that chain build; the four
  active ones (aOrientedCast, aRoutedQuill, dPinnedHandoff, dPolishedVitrine) finish on their own
  track; the chain's Plan build carries it out.
- Offered: **Let them finish first**. Offered: **Absorb everything**.
- **Answer:** Map, freeze dormant (Recommended).

### R3.4 Chain: "What shape should the chain of builds take?"

- Offered: **Spine first, then a DAG (Recommended)**: the loop definition and the policy layer land
  first; Test, Plan and Design run as parallel branches; Build follows Design; Deploy and Maintain
  follow Test; Review follows Maintain; Convergence comes last.
- Offered: **Strict sequence**. Offered: **Loop order**.
- **Answer:** Spine first, then a DAG (Recommended).

### What round 3 changed

- The Deploy chain build ships a generic deploy engine and its first adapter, fitted to incms.
- The Loop Review owns a value ledger and retirement, with owner-switchable budgets; records
  overhead joins that ledger as a measured metric with an owner-switchable ceiling.
- The chain is a DAG rooted at the spine, and the Plan chain build executes the live-build mapping.

## Round 4 — the policy layer (2026-10-14, session 1799cb98)

Asked after measuring today's configuration surface: five dotfile confs holding 138 keys
(`.memory-tree.conf` 58, `.unattended.conf` 63, `.codebase-map.conf` 7, `.process-monitor.conf` 6,
`.lexicon.conf` 4), plus `.governance/deploy.toml`, `tools/roles/house/policy.toml` (14) and
`.githooks/gate-env.sh` (6).

### R4.1 Policy home: "Where should the owner-switchable policies live?"

- Offered: **One policy file (Recommended)**: one per-repo, schema-validated file holding every
  switchable policy, its defaults from the loop definition, read through one reader, its current
  values rendered into the charter; kit mechanics stay in kit confs.
- Offered: **Kit confs + generated index**. Offered: **Answers in deploy.toml**.
- **Answer:** One policy file (Recommended).

### R4.2 Policy guard: "Who may change a policy?"

- Offered: **Owner only, gate-checked (Recommended)**: a policy change lands only in a commit
  carrying the owner's authorization, such as a signature, and a gate rejects any other.
- Offered: **Agents with a recorded reason**. Offered: **Agents within a mandate**.
- **Answer, in the owner's words:** "Owner-only gate-checked by default, but switchable mode per
  repo the same way as other switchable policies work"
- **Effect:** the guard is itself a policy, `owner-only` by default, switchable to the other two
  modes. Because changing the guard is a policy change, loosening it under `owner-only` needs the
  owner's authorization: the guard protects its own switch.

### R4.3 Review call: "When an agent's stage-exit check recommends a review, what happens?"

- Offered: **Binds by default (Recommended)**: "review needed" makes the review owed unless waived.
- Offered: **Advice only**. Offered: **Binds above a risk tier**.
- **Answer, in the owner's words:** "Advice only by default, but policy should be owner-switchable"
- **Effect:** the stage-exit recommendation is recorded and shown, and binds nothing by default; a
  policy switch can make it binding, or binding above a risk tier.

### R4.4 Gov verdict: "Gov's own repo is adopter zero. Which binding verdict should gov itself declare?"

- Offered: **Remote verifier for gov (Recommended)**: CI runs the full bar and the held self-tests
  before main moves.
- Offered: **Local hook, the default**.
- **Answer, in the owner's words:** "remote CI is not available to use currently, so we plan for
  local hooks first and foremost"
- **Effect:** the design inverts v0's P3 for now. The local hook is the primary, fully built verdict
  path, and every stage witness must hold without remote CI. The remote verifier stays a declared,
  optional backend for adopters that have CI, built after the local path. The drift signal
  `remote_ci_red_streak` reading DEAD is consistent with CI not running.

### What round 4 changed

- **One policy file per repository**, with the policy guard as its first policy.
- **Local-first witnesses.** With no remote CI, what makes a local verdict trustworthy becomes a
  design problem in its own right: the hooks an agent cannot bypass, the paths only the owner may
  write, and verdict records written by hooks rather than by the agent.
- **Review recommendations advise by default.**

## Round 5 — the floor, the verifiers, the chain (2026-10-14, session 1799cb98)

Asked after architecture v1 (`build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md`) and
a gap-ownership join that found all 57 gaps owned exactly once across its ten builds and reddened on
a planted orphan.

### R5.1 Floor: "Should a safety floor hold no matter what any policy says?"

- Offered: **Minimal floor (Recommended)**: five invariants no policy can switch off: (1) a binding
  verdict always runs before the default branch moves, only its backend a policy; (2) every policy
  change and stage transition recorded; (3) the policy guard protects its own switch; (4) no stage
  witness reads agent-typed state; (5) agents cannot bypass hooks (no `--no-verify`, no hooks-path
  override, no agent writes to hooks, the policy file or verdict refs outside the guard).
- Offered: **No floor**. Offered: **Wider floor**: the five plus the closing review and lease
  refusal.
- **Answer, in the owner's words:** "minimal floor by default, but the --no-verify policy should be
  off by default - gates have been causing problems and should be bypassable until this is
  resolved."
- **Effect:** the floor ships as a default rather than a hard-coded law, in keeping with P10.
  Invariant 5 splits: refusing a hook bypass becomes a policy, `hooks.bypass`, ALLOWED by default
  until gate reliability is fixed; the other four invariants stay in the default floor. The reason
  is itself a finding: gates are a source of friction the Test stage must resolve before refusal
  can be the default. A bypass still falls under invariant 2, so each one is recorded and the Loop
  Review can count it.

### R5.2 Verifiers: "With remote CI unavailable, which verdict backends should the Test build provide?"

- Offered: **Local + peer node (Recommended)**: the hardened local hook first, then a peer-node
  backend; remote CI designed as a slot, built when CI exists.
- Offered: **Local hook only**. Offered: **Local, peer and CI**.
- **Answer:** Local + peer node (Recommended).

### R5.3 Chain: "Approve the ten-build chain?"

- Offered: **Approve as drafted (Recommended)**. Offered: **Merge to seven**. Offered: **Split
  further**.
- **Answer, in the owner's words:** "Prior to approval we walk design by design first."
- **Effect:** the chain is not approved yet. Each chain build's design is walked with the owner,
  one build at a time, before approval; each walk is recorded below as it happens.

### What round 5 changed

- `hooks.bypass` joins the policy catalogue, default `allowed`, every use recorded.
- Gate reliability becomes an explicit goal of the Test build: the condition for flipping
  `hooks.bypass` to `refused`.
- The Test build ships the local hook and the peer-node verifier; remote CI is a designed slot.
- The chain waits for a design-by-design walk-through.
