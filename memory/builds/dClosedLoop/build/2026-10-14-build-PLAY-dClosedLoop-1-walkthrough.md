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
