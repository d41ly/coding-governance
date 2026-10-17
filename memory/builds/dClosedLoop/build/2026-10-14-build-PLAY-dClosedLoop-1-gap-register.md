# Gap register — every distance between today's gov and a closed lifecycle loop, with its evidence and its owner

**Serves:** research PLAY-dClosedLoop-1

Derived by the main loop from the six stage-research records in this folder, deduplicated so that
each gap appears once, under the stage whose contract must close it. Severity is the researcher's
unless the row says `(main loop)`. Evidence points at the record and section holding the
measurement; the records hold the file:line citations. The `Owner build` column stays `—` until
the chain opens; the build's acceptance (c) joins that column against the chain READMEs, so every
key below must end up owned by exactly one chain build.

Record shorthand: `plan`, `design`, `build`, `test`, `deploy`, `maintain` name
`build/2026-10-14-build-PLAY-dClosedLoop-1-research-<stage>.md`.

## How the parts interact today: the implicit loop

```text
owner prompt ──► /session-kickoff (card, brief) ──► build README + roster ─────────────► [no plan, no order]
                        │                                                                      ▲
                        ▼                                                                      │ asks, unlabelled,
   reuse probes ──► gov-spec-writer ──► spec (status header) ──► spec audit (opt-in, 3/173)    │ never triaged
                                              │ INPROGRESS, self-set                           │
                                              ▼                                                │
   route on card ──► write gate ──► gov-builder passes ──► closing review (enforced only       │
                                              │              under a mandate)                  │
                                              ▼                                                │
   pre-commit (hand-named legs) ──► pre-push bar (local, bypassable; 70 held legs skipped)     │
                                              │                                                │
                                              ▼                                                │
   push-main lander ──► main ──► remote CI (after the fact, blocks nothing) ──► post-merge     │
                                              │                                (declared in 0/3)
                                              ▼                                                │
   govkit (pull-only) ──► adopters (no CI emitted, no product release contract, 990 behind)   │
                                              │                                                │
                                              ▼                                                │
   SessionStart detectors (drift, procmon, wiring) ──► report only ──────────────────────────────┘
```

The middle of the loop, one unit's Design, Build and Test, is deep: a spec format, a twelve-part
method, role agents, a write gate and a 140-leg bar. The ends are thin or absent: nothing plans
across builds, nothing deploys or verifies a governed product, nothing maintains on a cadence, and
nothing feeds Maintain's findings back into a plan. `tools/roles/workflows.toml` already orders
the middle as stages 0 to 7 (`orient` to `bookkeeping`), and that is the seam a loop definition
extends.

## Cross-cutting themes

- **T1. Deep middle, missing ends.** Plan, Deploy and Maintain carry most of the HIGH gaps.
- **T2. Guards read state the actor writes.** The write gate reads a route and a status the agent
  writes; the build entry trusts a self-set INPROGRESS; review and receipt records are hand-writable.
  The charter's `[class]` rule forbids exactly this, and four of six researchers hit it.
- **T3. The binding verdict is local.** One node's pre-push hook decides; `--no-verify` skips it;
  half the legs never run before a landing; remote CI blocks nothing; the default branch is red today.
- **T4. Two contracts, one loop.** Unattended runs close on a 13-item definition of done; attended
  builds owe the same things in prose.
- **T5. Concurrency is advisory.** The overlap probe always returns 0, claims cover unattended runs
  only and never expire, and 41 live spec pairs from different builds share a path unseen.
- **T6. The loop corrects itself only by adding.** Every confirmed finding becomes a gate or a bug
  class; nothing retires one; the surface grew from 17 to 140 legs in ten weeks.
- **T7. Review lives at two stages.** Design (opt-in) and Build (closing review); none at Plan, Test,
  Deploy or Maintain, and none of the loop itself.
- **T8. The product and gov's own governance are one body.** Adopters get partial contracts: no
  product-test shape, no release contract, no emitted CI, no currency watch.

## Register

| Key | Stage | Sev | Gap | Evidence | Owner build |
|---|---|---|---|---|---|
| gap-found-01 | Foundation | HIGH | No instruction hierarchy: about 25 load-bearing documents (about 551 KB) reach agents by six routes at different times, carry no identity or rank, and state precedence only for kickoff; nothing restores their order after a context reset. Raised by the owner. | foundations step 1, current state | — |
| gap-found-02 | Foundation | HIGH | The charter's practices are one-line rules without reach: no stage contract, role or review lens reads them, and an adopter's methodology has no home but free prose. Raised by the owner. | foundations step 1, current state | — |
| gap-found-03 | Foundation | HIGH | Subagents load no charter (`omitClaudeMd: true`) and receive unranked charter fragments, with nothing ordering charter, role and task. Raised by the owner. | foundations step 1, current state | — |
| gap-found-04 | Foundation | MED | No rule and no record governs a live instruction that conflicts with the charter. Raised by the owner. | foundations step 1, F1-1 | — |
| gap-found-05 | Foundation | HIGH | The charter does not teach an agent how to drive gov for its role: its generated tool lines say what each tool answers, so every agent re-derives how to start and advance the loop from many files. Raised by the owner. | foundations step 1 continued, current state | — |
| gap-found-07 | Foundation | HIGH | No principle declares its enforcement: 22 of the charter's 36 practices are cited by no code file, no leg names the principle it enforces (0 of 140), and nothing stops a principle existing only as prose. Raised by the owner. | foundations core, current state and instrument | — |
| gap-found-08 | Foundation | HIGH | Extensions are hand-made: factories exist for 3 of 13 extension kinds (kit adoption, builds, micro-specs), so a new kit, command, document, policy key, leg, role, workflow, hook or Skill conforms only if its author remembers every rule. Raised by the owner. | foundations core, current state | — |
| gap-found-09 | Foundation | HIGH | Instructions map to almost nothing below them: tags name sections, and only the roles kit's `rules:` key joins each role to the charter's rule tags; checklist items are numbered, and no registry joins an instruction to the step, item, policy or layer it serves, so no loader can select an agent's instructions by its item. Raised by the owner. | layers round one, `[uncovered]`; `AGENTS.md`; the roles kit's `rules:` join (the instruction layer's fold, `roles-tag-join`) | — |
| gap-found-10 | Foundation | HIGH | Load is mostly unbudgeted and unmeasured: six load points carry declared, gated byte budgets, the rest carry none, no load set is computed per reader, a session starts on about 30 KB of repository and user text before the card, a trigger read pulls whole documents (the four unattended guides are 216 KB), and no injected load point is measured. Raised by the owner. | layers round one, `[current]`; `wc -c` on 2026-10-15; `tools/template-size-limits.txt` (the instruction layer's fold, `existing-budgets`) | — |
| gap-found-11 | Foundation | MED | Loaded text is unshaped: nothing checks that a loaded line gives direction; the charter's headings name provenance or a label, it points at a marker the agent never loads, its render provenance loads every session, and typed facts that go stale load at the top level ("Worktrees: none yet" beside 13 worktrees; a model name in the trailer). Raised by the owner. | layers round one, `[charter-today]`; `AGENTS.md` | — |
| gap-found-12 | Foundation | HIGH | Protocols and templates are hand-written monoliths: 409 KB of guides and templates restate the flow's steps in prose, so one rule lives in a guide, a Skill and a checklist at once, and nothing renders a protocol view from the loop's, the roles' and the policies' structured definitions. Raised by the owner. | layers round one, `[current]`; `memory/guides/`, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` | — |
| gap-found-13 | Foundation | MED | Skills are parallel procedures: build, unattended and session-kickoff carry their own procedures (SKILL.md files of 3.6 to 18 KB, session-kickoff with 258 KB of engine files) rather than shortcutting a CLI command into the flow, and every Skill's description loads each session without a trigger contract. Raised by the owner. | layers round one, `[current]`; `.claude/skills/`, `skills/` | — |
| gap-found-14 | Foundation | HIGH | Memory instructs outside the ladder: the auto-memory index (13.2 KB) loads every session under the harness's instruction framing, its feedback entries carry directives, and nothing promotes a standing directive into the instruction layer or holds memory at evidence. Gov never renders the index: the harness writes and injects it from outside the repository, so it can only be measured at session start and its directives detected. Raised by the owner. | layers round one, `[uncovered]`; the harness's session-start injection | — |
| gap-found-15 | Foundation | MED | No write path for instructions: the owner changes an instruction only by editing a source or the template by hand; there is no manifest, no validating command, no recorded change and no instruction preset beyond the practice catalogue. Raised by the owner. | layers round one, `[uncovered]` | — |
| gap-found-16 | Foundation | LOW | No instruction's effect is measured: nothing records which units an agent loaded, followed or broke, so text that bears no load is never found, though P11 says it must not exist. Raised by the owner. | layers round one, `[uncovered]` | — |
| gap-found-17 | Foundation | HIGH | The product has no layer model: kits declare no layer, the core depends on optional kits (the reuse scout's work order carries the map's dossiers; bug classes are core since KN-1), and no layer contract exists, so an expansion cannot be added or removed mechanically. Raised by the owner. Check 27's near-match ranking and the decision log's holds-now view import memory-recall (the library round's review). No check fails when one expansion uses a point another declares (EX-1, the expansion round's review). | layers round one, `[layers]`; flow-roles `[steps]`; v2 `[owed]`; runtime's layer and build since settled (dWellOiledMachine) | — |
| gap-found-18 | Foundation | MED | The `up —` micro-format asks for a password value, inviting a secret into chat. | `AGENTS.md:61`; `coding-governance-agents.template.md:64`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-found-19 | Foundation | MED | No overlay is a separate project block: a repository's own rules render inside the charter's one block, and gov's own overlay says it selects every kit, yet selects 22 of 29. | `AGENTS.md:1-177`; `.governance/deploy.toml:11,18-26`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-found-20 | Foundation | HIGH | No section tag has a resolver, and no citation is checked: 1,438 citations, 788 of them ambiguous. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-found-21 | Foundation | MED | Whole populations carry no tag (gate legs, points, hooks, commands, fields, units), and spellings collide: `build.scope` is an item and a policy. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-found-22 | Foundation | MED | Positional references have no gap and no ratchet: a new `§n`, `Mn` or `check n` lands in live text unchecked. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-found-23 | Foundation | MED | One fact in one place is policed per instance, never as a class. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-found-06 | Foundation | HIGH | No tool names the next step: six adopt scripts print install hints and nothing else ends with the caller's next command, so the loop advances only by agents re-deriving it. Raised by the owner. | foundations step 1 continued, current state | — |
| gap-flow-01 | Flow | HIGH | No feature level between build and unit: the interfaces between a feature's units have no record, so a change that breaks a feature cannot be told from one that touches a unit, and re-design has no granularity but the unit. Raised by the owner. | flow FL-D2, FL-D4, FL-D5 | — |
| gap-flow-02 | Flow | HIGH | The decision principles that resolve unattended forks (the most feature-rich option, then the most expandable, fully recorded) are stated nowhere; M3 names feature-rich only, and nothing ranks them above the charter's adjustable practices. Raised by the owner. | flow FL-D3, FL-D6; `memory/guides/BUILD-METHOD.md` M3 | — |
| gap-flow-03 | Flow | MED | The plan is written up to three times (README, brief, card) and the levels of card, plan and brief are declared nowhere. Raised by the owner. | flow Plan, current state; FL-P2, FL-P5 | — |
| gap-flow-05 | Flow | MED | Built specs are revised retroactively: a closing review's blockers can be folded into an already-built unit as a spec revision (dSweptBranches, "the blockers folded into unit 3 rev-3"), so the trail of what was built against which spec breaks. Raised by the owner. | flow FL-B3; `memory/builds/dSweptBranches/README.md` | — |
| gap-flow-06 | Flow | HIGH | No cross-build coordination: a build cannot reach the session working on a build it depends on, no message survives a session, and a dependency gates nothing. Raised by the owner. | flow interactions FI-2, FI-5, FI-6 | — |
| gap-flow-07 | Flow | MED | A build whose units sit in different steps has no defined step, and a session's card does not follow its build across transitions. Raised by the owner. | flow interactions FI-1, FI-8 | — |
| gap-flow-08 | Flow | MED | Landing order among builds verified at once is undefined; the first landing silently stales the others' verdicts; and no landing queue exists: the turnstile is a host-wide bar semaphore that `push-main.sh` never takes. Raised by the owner. | flow interactions FI-7 | — |
| gap-flow-09 | Flow | MED | A merge conflict between a build and the default branch's tip has no route. Raised by the owner. | flow interactions FI-3 | — |
| gap-flow-04 | Flow | MED | A critical planning issue has no path: no recorded plan revision and no re-design inventory of completed work, though none has occurred in 173 builds. Raised by the owner. | flow FL-P6 and its measurement | — |
| gap-flow-10 | Flow | HIGH | A build can end only by landing: no withdrawn, superseded or merged terminal state exists, the owner's pause, resume and abort exist only for unattended runs (`--hold`, `--resume`, `--abort`) and supersede does not exist, and a dependent held until its parent lands (`deps.landing`) waits forever on a parent that never will. Raised by the owner. | layers round two, `[uncovered]`; flow-roles `[steps]` Deploy; coordination `[design]` | — |
| gap-flow-11 | Flow | MED | Reviews and owner gates are two mechanisms fixed to set points: each step's review sits at one item (`review.<stage>`), owner gates sit at `autonomy`'s points, and neither can be placed at another item boundary. Raised by the owner. | layers round two, `[uncovered]`; flow `[review]` | — |
| gap-flow-12 | Flow | MED | The driver reasons out the review recommendation at Plan, Design, Test and Deploy, against P25 and `driver.reads`: a command scores it, and no role is named to reason it (FL-R3). Raised by the owner. | layers round two, `[audit]`; research flow items a F2, b F-X1; roles `[map]` | — |
| gap-flow-13 | Flow | HIGH | Item declarations are incomplete: items carry more than one actor, many state no witness or no failure route, the records disagree (two disposition sets; checklist text against later settlements), and Deploy has no item for settled behaviours (the parent-landing hold, the core re-check, the `landed` notice). Raised by the owner. | layers round two, `[audit]`; research flow items a F3, F4, F10 to F13, F15 to F21; b F-T1, F-T5 to F-T10, F-D1 to F-D12, F-M1, F-M3 to F-M11, F-R1, F-R3 to F-R10 | — |
| gap-flow-14 | Flow | HIGH | Witnesses typed by the acting agent decide routes or mandates: the tester's class routes a red, the builder's own "checks run" stands for acceptance, the driver's typed disposition places a request, and Maintain's agent-typed intake becomes a patch build's mandate under `patch.ratify: auto`. Raised by the owner. | layers round two, `[audit]`; research flow items a F1, F5, F6; b F-T3, F-D7, F-D8, F-M2, F-R2, F-R7 | — |
| gap-flow-15 | Flow | MED | No transition table is declared: F-D settled one per level, build, feature and unit, with terminal states and backward routes as rows. The build's table is drafted in flow-steps `[transitions]`; the feature and unit tables are not, and no check yet joins each item's `Then` routes to the table both ways, each step's policy list to the keys its routes read, or each filed ask to an acceptance form. Nor does one check that each value a policy catalogues has, in each item that reads its key, a witness arm and a route, walked per preset through the table (the library round's review). | the flow layer's fold, `withdraw-program-missing` | — |
| gap-orient-01 | Orient | HIGH | Placement is unaided and unrecorded: kickoff tells the agent to derive a request's scope itself, an unattended run handed a prompt always opens a new build, and only 6 of 131 recent builds name a predecessor, so a mis-placement cannot be audited; path overlap cannot decide placement (the named predecessor ranked first 0 of 5 times). Raised by the owner. | orientation research, routing; `skills/session-kickoff/SKILL.md:126-131`; `tools/unattended/SKILL.template.md:28-32` | — |
| gap-orient-02 | Orient | HIGH | Nothing binds a session to its build: the route check verifies existence and pairing only, so a route to a terminal build or to another session's build lands, and a resumed route is never re-checked. Raised by the owner. | orientation research, routing; `skills/session-kickoff/manifest-check.sh:995-1001` | — |
| gap-orient-03 | Orient | HIGH | A build's position is read from typed state: a unit's step and pass come from status headers and RUN.md's phase, all 10 INPROGRESS units sat idle 8 days or more, no resolver says which pass is due, and `LIVE.md` inherits 7 of 30 stale non-terminal headers. Raised by the owner. | orientation research, routing (c) and trust | — |
| gap-orient-04 | Orient | HIGH | Orientation is exploratory: a new session spends a median 35 tool calls and 146k fresh input tokens before its first productive write, 20% of them locating the work or re-reading git state; kickoff's Step 1 orders re-deriving what the card printed (median 6 calls), and READY reaches the card in 19 of 64 sessions. Raised by the owner. | orientation research, cost; `skills/session-kickoff/SKILL.md:49-56` | — |
| gap-orient-05 | Orient | HIGH | Claims carry no freshness keys: the card's cells go stale unmarked, the replay's `now —` line read the primary tree instead of the session's worktree, and 4 of 17 run claims disagree with their RUN.md, so a session cannot tell a fresh claim from a stale one without re-deriving it. Raised by the owner. | orientation research, trust; `skills/session-kickoff/manifest-check.sh:499`; this session's compact hook output | — |
| gap-orient-06 | Orient | MED | Resuming costs more than starting: a resume caches the whole context again (median 467k fresh input tokens, against 146k for a new session), and a compaction spends a median 15 calls re-reading content. Raised by the owner. | orientation research, cost | — |
| gap-orient-07 | Orient | MED | Briefs carry pointers, not facts: briefed agents spend 15% of their calls on method documents and 15% locating, agents read their own prompt file 10 times, and `role-sha` is never compared with the role it was rendered from. Raised by the owner. | orientation research, cost P4 and P6; `tools/hooks/agent-cap.js:55-60` | — |
| gap-orient-08 | Orient | HIGH | Work is bound to no checklist item: about 63% of main-loop tool calls follow no protocol step, typed role agents are 4.1% of subagents, a harness branches on free text, and researcher returns are unchecked (5 of 10 ended without a final turn). Raised by the owner. | orientation research, determinism; `tools/workflows/unattended-unit.js:348` | — |
| gap-orient-09 | Orient | HIGH | Allowances escape in the field: the role-gate arm let 34 typed gate runs through though a replay of the same commands is refused, cause unknown, and the `none` and `review` write classes are declared but read by nothing. Raised by the owner. | orientation research, determinism probes 2 and 3; `tools/hooks/scratch-guard.js:101-104` | — |
| gap-orient-10 | Orient | MED | Memory loads unchecked: 12 of the 98 paths the auto-memory names no longer exist, and the dangling-pointer signal only reports. Raised by the owner. | orientation research, trust; `tools/drift-audit/drift_signals.py:470` | — |
| gap-orient-11 | Orient | HIGH | A build's card cannot be found by its build: cards are keyed by session id in the clone's git directory, so a new session, a dead process or another node never finds the card of the build it picks up, and no card exists on the remote. Raised by the owner. | orientation research, preserve; `skills/session-kickoff/manifest-check.sh:311-316` | — |
| gap-orient-12 | Orient | HIGH | A resume delivered no card: in this session the resume hooks printed only the process and wiring checks, though the replay is wired for resume; the cause is unknown. Raised by the owner. | orientation research, preserve (this session's transcript, the resume at 16:21:01Z) | — |
| gap-orient-13 | Orient | MED | The card never reaches the charter's instruction slot: hook output lands as a reminder at the hook point, subagents (`omitClaudeMd: true`) get only the route, and another harness gets nothing. Raised by the owner. | orientation research, preserve; `tools/roles/render_agents.py:132`; https://code.claude.com/docs/en/hooks | — |
| gap-orient-14 | Orient | HIGH | Compaction is ungoverned: nothing persists an item's work in flight before an automatic compaction; the card the compact hook re-injects is the kickoff's, written once and never updated as the build progresses, so it points at none of the records made since; nothing sets what a session does as its window fills; and the summary is read as a source. In this session the summary alone carried 34 of the 55 facts that survived, 1 of 7 identifiers and 1 of 9 measured numbers came back, and the summary misstated one fact about the session. Raised by the owner. | compaction experiment, results (`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-results.md`); this session's compact hook output | — |
| gap-orient-15 | Orient | MED | The orientation scout the design relies on has never run: 0 of 3,283 recorded subagents is a gov-orienter, and a command writes today's card. | the project-map round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`) | — |
| gap-roles-01 | Roles | HIGH | Most checklist items have no role: of 70 items across the steps, 11 are performed by a role, 18 by the main session, 9 by a command and 32 by nobody; no role exists for planning, feature design, testing, deployment, maintenance or the Plan, Test, Deploy and Loop reviews. Raised by the owner. | roles research, coverage | — |
| gap-roles-02 | Roles | HIGH | The main session performs role functions: in 60 days it wrote or edited specs 605 times, product code 565 times, folded review findings 367 times, and wrote plans 336 times and task briefs 74 times. Raised by the owner. | roles research, coverage P2 and P5 | — |
| gap-roles-03 | Roles | HIGH | Role limits are prose: 58 of the 59 prohibitions in role bodies name no enforcer, `writes` is a class rather than an allowance, and shell writes escape every role gate (85 from the main session and 66 from typed roles since the role arm landed). Raised by the owner. | roles research, anatomy probe 3, coverage P4 | — |
| gap-roles-04 | Roles | HIGH | Returns between roles are uncontracted on the direct route: 48 of 48 direct-spawn returns are free text, `returns` is prose no code reads, and no subagent-stop check exists. Raised by the owner. | roles research, prior art probe C, anatomy | — |
| gap-roles-05 | Roles | HIGH | Exchanges between roles are retyped by the main session: 64.5% of a rendered task's bytes are typed input, 71 of 126 direct spawns carried free-text prompts, and 844 of 901 spec fold commits came from no unit. Raised by the owner. | roles research, interactions probes 3, 4 and 7 | — |
| gap-roles-06 | Roles | HIGH | The guard shares state with what it guards: the role index and agent files sit outside every role gate, so a role holding Write could edit them, and a tree with no role index is unarmed. Raised by the owner. | roles research, anatomy; `tools/hooks/scratch-guard.js:99-101` | — |
| gap-roles-07 | Roles | MED | Roles go unused or double up: the orienter, reuse scout and diff reviewer had no spawn in 60 days, the reuse scout's body adds nothing, the spec writer also holds disposal, and the session-handoff template has no agent. Raised by the owner. | roles research, coverage P6 | — |
| gap-roles-08 | Roles | MED | The work order names no checklist item, allowance or witness key, and a builder's divergence returns to "the caller" with no route back. Raised by the owner. | roles research, anatomy; `tools/workflows/unattended-unit.js:269` | — |
| gap-roles-09 | Roles | LOW | A return's harness notices cannot be recorded: the injection guard's matches on researcher returns and the MCP-failure notice lived only in the context and died at the compaction, and nothing can persist them, so `notices.record` has no mechanism for its values other than the default `none`. Raised by the owner. | compaction experiment, results (`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-results.md`), Q07 and Q68 | — |
| gap-roles-10 | Roles | HIGH | Role definitions order re-verification and declare no trust: `tools/roles/agents/gov-spec-writer.agent.md:30` and `gov-researcher.agent.md:33` order every claim about current code verified by reading the code, `gov-session.agent.md:18` makes a sender's records background to re-verify, `memory/TEMPLATE-SPEC.md:106` orders every claim verified against source, `gov-builder.agent.md:19` orders the spec read whole, and no role declares what it may act on without re-checking or which inputs its job verifies. Raised by the owner. | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[current]` | — |
| gap-roles-11 | Roles | HIGH | Work orders hand references, not content: 42.0% of the files directly spawned role agents read were files their parent had read before the dispatch (spec writers 46.8%, researchers 25.8%; 61 agents), and the item cycle hands the prompt writer references to its input records. Raised by the owner. | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[current]` and `[instrument]` | — |
| gap-roles-12 | Roles | MED | Role files point at whole protocol documents: 9 of 9 carry "Protocols — read the one whose trigger holds", and role agents made 811 method-class reads of whole documents, among them `TEMPLATE-SPEC.md` 131, `BUILD-METHOD.md` 130, `SESSION-KICKOFF.md` 59 and `HYGIENE.md` 43. The pointers come from the charter's Protocols section, which the roles kit carries whole (`CARRIED_SECTIONS`). | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[current]` and `[instrument]` | — |
| gap-roles-13 | Roles | MED | Nothing sees or bounds an answered call: state, locate and method calls are 12.7% of 9,980 role calls and 16.9% of the bytes role agents take in, spec writers read their own prompt file 17 times, and no hook compares a call with the work order. | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[current]` and `[instrument]` | — |
| gap-roles-14 | Roles | MED | The roster is not sorted by layer: the settled roster lists the deployer and the maintainer beside the core roles and the reviewer's maintenance and loop lenses as core, and no check keeps core items to core roles (P28). | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[roster]` | — |
| gap-roles-15 | Roles | MED | The role-to-step relation is typed, never derived or joined: the roles round's item map and the step definitions' Actor cells are authored tables, and nothing checks that every actor is declared and every core role acts. | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[matrix]` | — |
| gap-roles-16 | Roles | LOW | Nothing declares what a verifying role receives: a reviewer's or skeptic's packet is whatever its prompt's author put in, so nothing keeps an author's reasoning out of it. | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[trust]` | — |
| gap-roles-17 | Roles | LOW | A handed fact found false has no repair record and no route: only the builder's `diverged` routes back, no role's return can record a repair, and nothing files one against the producer's record. | layer review, roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), `[trust]`; step definitions, `[build]` | — |
| gap-roles-18 | Roles | MED | Role items declare only part of an execution shape: the agent set per workflow and stage (`workflows.toml`), the effort per role and stage (`house/policy.toml`) and the bug-class checklist (`gotchas.py`) are declared, while the orientation template and the merge are chosen per harness or prompt, though aScoutedSeam measured that shape moves recall and cost: one checklist scout at medium matched a two-scout workflow with a judge (12 of 23) on a third of the agents, and a scout that reads a generated house index first solved 16 of 24 against 13. Raised by the owner. | aScoutedSeam benchmark (`origin/branch/deterministic-reuse-workflows-f70c33` at `b0fe68f30`, `memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`); layer review, roles, `[owner-notes]` | — |
| gap-roles-19 | Roles | MED | Every role spawn carries the charter blocks twice. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-roles-20 | Roles | LOW | The static block's budget covers its base body only. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-mem-01 | Memory | HIGH | No memory contract: no registry declares the record kinds with their schemas, writers, readers and checks. Conventions are spread over `HYGIENE.md` (58.5 KB), the spec template, the guides and 21 memory-tree legs; review bodies, build journals and 535 of 565 prompts are free prose; README front matter is open-world, so a misspelled `parent:` is accepted silently. Raised by the owner. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md` | — |
| gap-mem-02 | Memory | HIGH | The decision index holds the wrong things and instructs no one: 28 of 200 rows are major decisions or features others must reuse, 0 carry a reuse instruction, nothing requires a row, recall opened the file 0 times in 121 opens, 47 rows chain a supersession or narrowing, and 79 sit within 20 characters of the 300-character cap. Raised by the owner. Nothing defines a major decision: 160 rows were added in 60 days, beside 1,829 `Decided:` trailers (the library round). | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-asks-decisions.md` | — |
| gap-mem-03 | Memory | HIGH | No reuse instruction reaches an agent: each dossier's `## Reuse affordance` block holds the facts, but no instruction carries them, the task card's `**Reuse:**` field has no producer, and `reuse_lookup.py` solved 0 of 24 cases, ranking test helpers first with a median of 110 candidates shown. Raised by the owner. Nothing proposes an entry when a unit builds a new seam (256 specs in 67 builds say no existing seam fits), `gov:feature` marks 0 code lines, and 4 of 20 stored cards fill `**Reuse:**` (the library round). | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-map-reuse.md`; aScoutedSeam's benchmark | — |
| gap-mem-04 | Memory | HIGH | The codebase map stores no relations: 0 caller edges, a fan-in that counts files mentioning a name, 75.5% of Python's definitions (methods, nested and private functions missing), no Markdown, TOML or JSON symbols, and 1,012 cross-language script invocations unseen. Raised by the owner. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-map-reuse.md` | — |
| gap-mem-05 | Memory | MED | A build's README routes only to specs: nothing routes a reader by purpose, records route only through spec regions, and 77.9% of agent-build pairs never read the README, while 96.4% of build-folder reads go past it. Raised by the owner. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md` | — |
| gap-mem-06 | Memory | MED | Slug and id patterns are spelled per reader: at least eleven readers in seven kits, of which a digit date breaks six and a hyphenated date ten; `BUILD_SLUG_RE` reaches one; the prose rule says two words ("adjective-noun") where the owner says one to three, and nothing checks either. Raised by the owner. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md` | — |
| gap-mem-07 | Memory | MED | Relations between builds are untyped: `parents:` alone (11 builds, 13 edges); no patch, amendment or supersession field, with supersession in prose in 110 builds; no cross-build unit edge; no cycle check. Raised by the owner. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md` | — |
| gap-mem-08 | Memory | MED | Code annotations have no grammar, tags or index: 0 tag lines among 91,661 comment lines, a style guide that refuses a grammar and was read once in 60 days, cited ids followed to their record within 3 calls 2.5% of the time, and nothing that extracts the 6,540 id-bearing comment lines. Raised by the owner. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-annotations.md` | — |
| gap-mem-09 | Memory | MED | memory-recall indexes no code, its chunks arm scores 0.00 at r@5 on its own bench, and 29 of 530 queries (5.5%) were followed by a read of a hit it showed. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-map-reuse.md` | — |
| gap-mem-10 | Lexicon | MED | The lexicon gate absorbs debt: `VERB_OFFENDER_PIN` rose from 412 to 1,087 with one real drain in 60 days, so the pin behaves as a waiver. Revised 2026-10-17: its area is Lexicon since L-4 moved it to dMindYourWords, and its key stays. | layer review, memory, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-annotations.md` | — |
| gap-mem-11 | Memory | LOW | Memory records contradict the code: the map README names a path that does not exist, `backlog.py` says it ships dark with shards by default, the DEPL section of `DECISIONS.md` holds 81 rows of other families, three ids are duplicated, the spec template requires a security model in the decision log where 0 rows have one, and 9 READMEs type their status. Two more: `ANNOTATION-STYLE.template.md` says no gate reads comment citations, though drift-audit's report-only signal does, and `HYGIENE.md` lists a `note` kind the catalogue never uses (the library round). | layer review, memory, `[current]`; dispatches 22, 23 and 24 | — |
| gap-mem-12 | Memory | LOW | The annotation follow-through test decides nothing: it has no threshold, sample size or window, and its measure cannot separate following a pointer from working on the same build, so "if follow-through does not rise" cannot choose the runner-up hook. | the memory layer's fold, `follow-through-test` | — |
| gap-mem-13 | Memory | HIGH | No claim makes a slug unique across clones: `check_slug_claimed` reads the local clone only, and no claim ref exists for a slug or for an ask family, so two clones that have not fetched each other can mint one slug, and with it one id. Revised 2026-10-17, the debt round: the fix owes a claimant key on every claim commit, so `entry.claim` is idempotent; an ask family's ref that each mint advances by a leased compare-and-swap, for every filer outside a build; and no prune of `refs/gov/claims/*`. | the fold's follow-up round, H2 and M6 (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`) | — |
| gap-mem-14 | Memory | LOW | A bug class can anchor on nothing: HYGIENE check 19 only advises on a gotcha record's dead anchor, so a class filed with one is never selected for the changes it describes. | the fold's follow-up round, L4 (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`) | — |
| gap-mem-15 | Memory | MED | No research view: research records are found across builds only through recall, an optional component, or by file name, and 8 of 59 research returns, the research-named records bound as research in 10 builds, are cited from another build. The binding alone also covers design records, logs and registers. Revised 2026-10-17, the debt round: five of those 59 were instruments records, so research returns were 54, 8 cited from another build; at `1b759b620` they are 72 in 10 builds, 9 cited (`research_count.py`, the debt comparison's instruments `[probes-library]`). | the library round's research, `build/2026-10-16-build-PLAY-dClosedLoop-1-research-library-paths.md` | — |
| gap-mem-16 | Memory | MED | Records that belong to no build have no home: maintenance and Loop Review records are keyed by period, release records by SHA and environment, currency observations by adopter. | `memory/HYGIENE.md:17-35`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-mem-17 | Memory | MED | A comment can cite a record that never existed, and no check sees it. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-mem-18 | Memory | MED | Comment load is unbudgeted: comments are 41% of code bytes, and about 29% of commits add a long block. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-mem-19 | Memory | MED | `pushed-at-read` reaches 3 to 5% of code reads, since a Read hook misses reads made through the shell. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-mem-20 | Memory | HIGH | Memory has no index by key or section. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-mem-21 | Memory | MED | No read budget applies per item, and the global one was retired. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-mem-22 | Memory | LOW | Recall's cache is 477 MB for a 67 MB memory tree. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-mem-23 | Memory | MED | The map's touch-drop is wired to nothing: `--drop-affordance-exempt` has no caller in `tools/`, `.claude/`, `.github/` or `.githooks/`, and `WIRE-INTO-PROJECT.md:554` calls the drop mechanical. | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-mem-24 | Memory | MED | Nothing takes a census of a repository's own practices, and no cell shows the retrofit's progress. | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-mem-25 | Memory | LOW | Records carry no origin, so a reconstructed record reads as written. | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-mem-26 | Memory | HIGH | No whole-project view reaches an agent: 37 of 52 items of the systems and retrofit audit, and 30 of 39 in two more reviews, needed a piece their author did not have in view, and `MAP.md` and `CARDS.md` reach no agent (`research-project-map-a.md:203`, `research-project-map-b.md:233`). | the project-map round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`) | — |
| gap-mem-27 | Memory | MED | Nodes carry no declared purpose: kits, legs, hooks, points, record kinds and the tag and policy namespaces have no purpose field, and govkit and lib carry no `kit.toml`. | the project-map round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`) | — |
| gap-tool-01 | Tooling | MED | Gate legs are declared twice: 81 of 140 legs exist only in `tools/gate-legs.json`, beside 67 `[[gate_leg]]` rows in kit packs. | layer review, memory, `[tools]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` | — |
| gap-tool-02 | Tooling | MED | Wiring is judged three ways (check-wiring, eleven `adopt-*.sh --check` legs, `govkit check`) and version lockstep five ways (check-kit-versions, check-placeholders, `govkit epoch`, check-verdict-epoch, and govkit selfcheck's arm 5c at `tools/govkit/govkit.py:2162`, the expansion round's review). All 11 `[check]` argvs also duplicate their own gate legs (the expansion round). | layer review, memory, `[tools]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` | — |
| gap-tool-03 | Tooling | MED | The hook surface spans five kits: hooks, unattended (three hooks), process-monitor and memory-recall each wire their own entries in `.claude/settings.json`. | layer review, memory, `[tools]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` | — |
| gap-tool-04 | Tooling | LOW | 73 files carry hand-kept inline copies of `resolve_python`, though `tools/lib/resolve-python.sh` is the one resolver; the copy-install could generate them. The class is wider: 261 inline markers over 17 primitives (the expansion round). | layer review, memory, `[tools]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` | — |
| gap-tool-05 | Tooling | LOW | Dead or undogfooded tools: the deploy-governance Skill has no reader and 0 loads and repeats govkit's verbs; pytest-parallel-guardrails has 0 runs and one held leg, against "dogfoods every kit it ships". | layer review, memory, `[tools]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` | — |
| gap-tool-06 | Tooling | LOW | `.claude/rules/product.md` misdescribes the gates: check-wiring is not a leg (it runs as a SessionStart hook), and 14 checks run as legs. | layer review, memory, `[tools]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` | — |
| gap-tool-07 | Tooling | MED | Kit descriptors declare no layers, extension points, record kinds or policies, and nothing validates their keys. | 0 of 29 descriptors carry `layers`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-lex-01 | Lexicon | HIGH | No class for forced names: every extracted definition is graded by its leading subtoken alone, so host-forced names (four pytest hooks, `__str__`, a command shim) and 22 names gov's own readers key on count as debt; the only exits are a pin raise or a corpus-wide text waiver, and history shows 19 raises and 0 waivers. Raised by the owner. | kit review, lexicon (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md` | — |
| gap-lex-02 | Lexicon | HIGH | `--suggest` proposes renames that break overrides: `do_GET` to `cmd_get`, `emit` to `print`, `handle` to `run`, `get_queryset` to `read_queryset`, which breaks a Django view, and `setUp` to `set_up`, which silently stops unittest calling it; P29 would hand these answers to builders. Raised by the owner. | kit review, lexicon (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md` | — |
| gap-lex-03 | Lexicon | HIGH | Naming is enforced only as a corpus count at the bar: nothing judges a name at commit or by name, a fixed offender plus a new one nets to zero, and landings absorbed raises instead of holding the equality: 19 raises (+814) in the pin's history. Revised 2026-10-17, the debt round: this row once cited main's 1,088 against 1,087 since `8ddc0a482`, a red gone since `ef9c3fbab`. Raised by the owner. | kit review, lexicon (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md` | — |
| gap-lex-04 | Lexicon | MED | Records are graded: 43 offenders sit under `memory/builds/` and drove the latest raise, +24 net in `301a36664`: 30 arrivals, all aSparedSpawn build records, less 6 departures (Revised 2026-10-17: once read as +24 of +30), and an undeclared record extension refuses the wiring leg (this build's `.html` and `.svg`, declared dark on 2026-10-15). | kit review, lexicon (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md` | — |
| gap-lex-05 | Lexicon | MED | No consistency beyond verbs: 57 objects carry two or more declared acquire-family verbs (`conf` is loaded 11 times, read 3 and parsed twice), and noun variants go unchecked (`sha` 13, `oid` 4, `hash` 4, `digest` 10; `dir` 101, `directory` 1, `folder` 2). Raised by the owner. | kit review, lexicon (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md` | — |
| gap-lex-06 | Lexicon | MED | Exemptions need no reason and nothing checks one: waivers are keyed on a bare name corpus-wide with an optional reason, pins and un-armed cells change by plain edit, `ratified` certifies nothing about verb edits, and VERBS mixes vocabulary with forced names (`init` partly clears `__init__`). | kit review, lexicon (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-prior-art.md` | — |
| gap-lex-07 | Lexicon | LOW | Kit defects: a repeated block header silently replaces the earlier block, four non-names (an IIFE value, three properties) are graded as verbs, `--brief` and `--help` exit 2 though about 130 calls used them, and the Skill, the conf and the README disagree on what the gate does. | kit review, lexicon (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md` | — |
| gap-lex-08 | Lexicon | LOW | The lexicon's two drift signals reach the bar through drift-audit's engine, which imports the optional lexicon kit, instead of as a leg pack the lexicon registers. | `tools/drift-audit/drift_report.py:1182-1213,1245-1279`; the expansion round's review, `build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md` | — |
| gap-rt-01 | Runtime | HIGH | A model session decides every next act: 19 of 20 sessions resumed from a compaction's summary instead of state, the driver refused 47 malformed or out-of-order transitions, one session improvised 17 inline workflows and another more than 25 ad-hoc scripts, and 2 runs were left at BUILDING with all work terminal. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-executor.md` | — |
| gap-rt-02 | Runtime | HIGH | Every enforcement hook fails open: no entry sets `onFailure`, all 31 failures of one burst on 2026-10-14 admitted the call, and pre-commit, commit-msg and pre-rebase trap no signal. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md` | — |
| gap-rt-03 | Runtime | HIGH | Spawned work dies with its session: 4 background agents died with their parent, limits killed 57 agents in 16 Workflow runs and the whole fan in 10, 7 of 12 all-errored runs report `completed`, and a null becomes `committed:false` with no reason. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md` | — |
| gap-rt-04 | Runtime | HIGH | The headless resumer skips permissions (`resume-tick.sh:385`), so with hooks failing open, a resumed session under resource exhaustion would run unguarded. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md` | — |
| gap-rt-05 | Runtime | MED | Fan-out is bounded per prompt, not in flight: the direct budget resets on every notification, and Workflow calls and headless launches are outside the count. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md` | — |
| gap-rt-06 | Runtime | MED | Workspaces are neither allocated nor reclaimed: 8 merged worktrees and 497 stale temp directories remain, the directories' source unattributed, and concurrent agents share one scratch directory. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md` | — |
| gap-rt-07 | Runtime | LOW | Session hooks miss events: no matcher covers `fork`, and SubagentStop, PreCompact, PostCompact and SessionEnd are unwired. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md` | — |
| gap-rt-08 | Runtime | LOW | Node facts go unrecorded: the `claude` binaries and their versions, node d's clock running 8 to 13 s slow, and its `autocrlf` against CI's. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md` | — |
| gap-rt-09 | Runtime | LOW | gov wires none of the five hook events Codex ships. | layer review, runtime, `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md` | — |
| gap-rt-10 | Runtime | LOW | Runtime records contradict the code: the "four-verb driver" has 30 verbs, `/build` claims an identical spec review in both modes, an earlier design record said the spawn guard compares `role-sha`, the Facts line's placeholder "Worktrees: none yet", meaning no bootstrap script, reads as no worktrees while 13 exist, and a keepalive comment says the cron store dies with its session. | layer review, runtime, `[current]`; the four runtime research returns | — |
| gap-rt-11 | Runtime | MED | Codex gets no card: an override file would replace the charter, since Codex reads one instruction file per directory; its 32 KiB limit covers the whole chain it reads; and Codex has no SessionStart, so only the harness adapter's launch input can carry the card. | the instruction layer's fold, `codex-override`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md` | — |
| gap-rt-12 | Runtime | MED | An act session loads the whole charter: `claude -p` reads `CLAUDE.md`, which imports `AGENTS.md`, so driver-scoped units such as the micro-formats reach a role's act, and nothing renders the act's own load set. | the instruction layer's fold, `act-session-load-point` | — |
| gap-rt-13 | Runtime | MED | Hook text is unregistered instruction: SubagentStart context, Stop-hook block reasons, PreToolUse deny reasons and SessionStart output are composed in code, outside the unit registry, its grammar and its budgets. | the instruction layer's fold, `hook-injected-loads` | — |
| gap-rt-14 | Runtime | HIGH | The intake hook sits outside Runtime's enforcement surface: no prompt-submit event is wired, nothing scopes it to attended-bound sessions, and no reader checks its witness when it crashes or never fires, though the intake record is the mandate to land. | the flow layer's fold, `intake-hook-crash`, `intake-owner-scope` | — |
| gap-rt-15 | Runtime | HIGH | The scheduler runs the cadence items that their layers declare, but no extension point takes one, so Maintain, the Loop Review, the kit release and the currency probe have nowhere to register. Command adapters carry no class either: act, reading or fix (the expansion round's review). | layer-runtime `[schedule]`, `[extend]`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-rt-16 | Runtime | MED | Nothing prunes the journals, and six node-local grammars sit beside runlog's. | `tools/runlog/README.md:568`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-rt-17 | Runtime | MED | No adapter declares a grant, and no check covers secrets: the lander's push rides an ambient credential helper, and none of 140 legs scans for a secret. | `credential.helper=manager` from the system gitconfig; `tools/gate-legs.json`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-rt-18 | Runtime | MED | No channel reaches the owner outside a session: no notification hook is wired, and no channel code exists. | `.claude/settings.json`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-rt-19 | Runtime | MED | Harness adapters declare no install targets: 8 descriptor rows write to Claude Code's `.claude/` paths. | `tools/*/kit.toml`, `tools/govkit/entries/`; layer-runtime `[harness]`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-rt-20 | Runtime | MED | Workflow harness prompts are a load point with no grammar, budget or parity. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-rt-21 | Runtime | HIGH | The spawn guard admits any agent-true role in any stage at any effort. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-spine-01 | Spine | HIGH | No stage model: no kit, leg, dossier, role or hook declares the stage it serves, and the loop exists only implicitly. | design §4.1 (0 of 31 dossiers carry a stage); `tools/roles/workflows.toml` covers stages 0–7 only | — |
| gap-spine-02 | Spine | HIGH | Guards read agent-written state across stages, against `[class]`. | build §4 (write gate), design §4.4 (INPROGRESS), test §5 C (pusher-written receipt), deploy §5 C | — |
| gap-spine-03 | Spine | HIGH | Attended and unattended builds run different exit contracts. | build §3, §4 (DoD needs RUN.md) | — |
| gap-spine-04 | Spine | MED | gov's own governance and the shipped product are one body; adopters receive partial stage contracts. (main loop) | test §4, deploy §4; `.claude/rules/product.md` | — |
| gap-spine-05 | Spine | MED | Protocol volume: guides 301 KB, runbook 163 KB, unattended guides about 216 KB. (main loop) | maintain instrument 2; `wc -c` of `memory/guides/` | — |
| gap-spine-06 | Spine | HIGH | No single answer to "what is this repo's policy": per-repo configuration spans at least eight surfaces holding about 160 keys, owner choices mixed with kit mechanics. Added after round 4. (main loop) | design-rounds R4; five dotfile confs hold 138 keys | — |
| gap-spine-07 | Spine | LOW | No policy schema or reader validates a key that selects an extension against the registry: the keys layer-runtime `[extend]` lists take registered names, and nothing refuses an unregistered one. | layer-runtime `[extend]`; dGroundRules's schema and reader, extended by dDeclaredLoop's registry check (RC-1, M2); the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-conc-01 | Spine | HIGH | Cross-build and cross-node overlap is advisory: the probe always returns 0 and sees only pushed refs; no unit or path claim exists. | build §4, design §4.2 (41 pairs across 22 build pairs) | — |
| gap-conc-02 | Spine | MED | Claims never age, name a user rather than a fleet tag, and cover unattended runs only; slug uniqueness is checked against local history only. | plan §4 (8 of 17 held, 17 of 17 user names) | — |
| gap-conc-03 | Spine | MED | `[isolate]` has no mechanism: harness passes share one worktree and meet git's index lock. | build §4 | — |
| gap-plan-01 | Plan | HIGH | No priority, order or dependency record across builds and asks. | plan §4 (absent; TOOL-aBoundedVerdict-7 DEFERRED) | — |
| gap-plan-02 | Plan | HIGH | Triage is never drained: 435 of 521 live asks unlabelled; 297 deferred onto one owner-triage ask open since 2026-10-05; no role owns triage. | plan §4 | — |
| gap-plan-03 | Plan | HIGH | The asks pipeline is not the real intake: 165 of 167 builds came from prompts, and a prompt yields a one-build brief, never a plan. | plan §2, §4 | — |
| gap-plan-04 | Plan | HIGH | Nothing reviews a plan, a backlog or a priority order. | plan §4 | — |
| gap-plan-05 | Plan | HIGH | Dormant work is labelled, never disposed: 21 of 25 live builds dormant. | plan §4; maintain instrument 1 | — |
| gap-plan-06 | Plan | MED | Most OPEN asks are not ready to build: 94 of 218 grade `no`, 132 lack an acceptance. | plan §4 | — |
| gap-plan-07 | Plan | MED | The brief is gated only for units a run built; attended briefs are stated. | plan §4 | — |
| gap-design-01 | Design | HIGH | No record holds an architecture above one unit; the map is an inventory. | design §4.1 | — |
| gap-design-02 | Design | HIGH | Design conflicts between builds are invisible: 25 non-registry shared paths between live specs, 21 with an INPROGRESS side. | design §4.2 | — |
| gap-design-03 | Design | HIGH | Design review is off by default: 3 of 173 builds declare an audit; 503 of 989 Tier-2 specs unaudited. | design §4.3 | — |
| gap-design-04 | Design | HIGH | The hand-off to Build ignores design state: a FORKED unit at INPROGRESS is admitted. | design §4.4 (TOOL-dNarrowedAnchor-1) | — |
| gap-design-05 | Design | MED | Nothing checks that a spec's reuse audit is true; 142 of 978 cite no probe. The audit's outcome is prose: the hygiene check admits three phrasings of a new seam, while the reuse-line trigger reads one (236 specs carry the exact phrase, 256 one of two) (the library round's review). Revised 2026-10-17, the debt round, measured at `1b759b620` over 1,301 specs in 163 builds (`reuse_token_count.py`, the debt comparison's instruments `[probes-library]`): the trigger's exact phrase marks 236 specs in 60 builds; the hygiene check, which admits "no existing seam", "no seam fits" or "reuse-first" in section 10 before its recall terms, grades only specs dated on or after `SPEC10_EVIDENCE_CUTOFF` (2026-09-01) and admits 302 in 55 of them; the same tokens in section 10 at any date mark 333 in 75, and their union with the trigger, a corpus-wide migration's population, is 339 in 76. Revised 2026-10-17, the folds' closing review: this row once credited hygiene with the ungated 333; the revised probe is in `build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md` `[probes-final]`. | design §4.5 | — |
| gap-design-06 | Design | MED | Rejected design candidates are unchecked; 95 of 978 Tier-2 specs record none. | design §4.6 | — |
| gap-design-07 | Design | MED | The reuse stage is neither enforced nor recorded, and research has no harness (7 research records in 173 builds). A 2026-10-16 count finds 59 research-named records bound as research, in 10 builds; the binding alone covers 179 records, design records and logs among them. Revised 2026-10-17: five of the 59 were instruments records; research returns were 54 then, and are 72 in 10 builds at `1b759b620` (`research_count.py`). | design §4.7, §4.8 | — |
| gap-design-08 | Design | MED | Audits never come back clean: 0 of 254, 170 BLOCKED; nothing measures whether specs reach review short of their bar or the bar moves. (main loop) | design §4.3 | — |
| gap-design-09 | Design | LOW | Sub-spec agreement, tier assignment and unpushed specs are prose or invisible. | design §4.9–4.12 | — |
| gap-design-10 | Design | LOW | Spec section numbers mean different sections by tier. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-build-01 | Build | HIGH | Scope is not bound to the unit: 120 of 584 unit-attributed product commits touched files outside their unit (42 of 582 at kit granularity). | build §4 | — |
| gap-build-02 | Build | HIGH | The attended closing review is unenforced: 29 of 59 attended builds with a CLOSED unit carry one, against 86 of 89 unattended. | build §4 | — |
| gap-build-03 | Build | MED | Bash and PowerShell product writes escape the write gate. | build §4 | — |
| gap-build-04 | Build | LOW | The per-pass bug-class checklist is unverified, and agents a harness spawns are uncounted. | build §4 | — |
| gap-build-05 | Build | MED | Baselines are not tied to touch: five kits stay baselined after 14 to 278 touches each, and the per-file count ratchet let 29 of 129 encoding sites persist on edited lines (`research-retrofit-b.md:118`, `research-retrofit-a.md:102`). | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-test-01 | Test | HIGH | Kit self-tests, 70 of 140 legs and 23,494 s of 28,066 s summed maxima, are on no pre-landing path. | test §4 | — |
| gap-test-02 | Test | HIGH | The binding verdict is one node's bypassable hook; remote CI blocks nothing; the default branch reds memory hygiene today. The verdict-backend registry Test declares, and the remote verdict before the landing under `verdict: remote-ci`, are this gap's (the expansion round). | test §4; maintain instrument 4; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-test-03 | Test | HIGH | Adopters get no product-test contract: no test levels, selection, or flake policy; their manifest starts empty. | test §4 | — |
| gap-test-04 | Test | MED | Flakes: one timeout retry only, no quarantine or flake record. The bar reports nondeterminism only for a cached-green leg a reuse run samples, which Test's invocation never draws, and it has no mode that re-runs a red leg on the same tree. Revised 2026-10-17, the debt round: the runner's verdict record carries each held leg's result under every `verdict.held` value, so `test.select` derives a held leg's streak and lifts its hold, and `test.flakes` is the flake record's one writer. | test §4 | — |
| gap-test-05 | Test | MED | A green is not shared across nodes: the stamp is local and no green ref exists. | test §4 | — |
| gap-test-06 | Test | MED | "A gate never seen red is not a gate" has no recorder. | test §4 | — |
| gap-test-07 | Test | MED | The pre-commit leg list is hand-named. | test §4 | — |
| gap-test-08 | Test | MED | Cost evidence is thin: 21 legs have no ceiling evidence, all from one node, and no whole-bar wall time is recorded (records claim 4–7 h). | test §4 | — |
| gap-test-09 | Test | LOW | A stale README example, 8 unguarded held legs, and a PowerShell scan on no leg. | test §4 | — |
| gap-test-10 | Test | HIGH | No catch history is committed: the gate ledger keeps each leg's last state, gate reds live in one node's journal, and no bug class carries a catch field, so nothing can price a gate. | `tools/run-gates/run-gates.sh:5214-5256`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-test-11 | Test | MED | A remote verdict certifies itself: the workflow that produces it, and the bar it runs, are part of the tree they judge, and nothing grades the workflow's text. | `.github/workflows/remote-ci.yml:15-16,96-106`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-test-12 | Test | MED | The hosted bar has been red on every run since 2026-10-13 14:03, and reading why needs an authenticated read of its logs. | integrations B, through the public API; integrations A read 22 of the last 40 push runs red; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-test-13 | Test | LOW | The one live outside reader, the held-CI reader, sits inside the unattended kit with no adapter registration. | `tools/unattended/unattended.sh:9972`; `.unattended.conf:221`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-test-14 | Test | HIGH | No single baseline primitive: 27 registries in at least 6 grammars, with the count ratchet written twice (`research-retrofit-a.md:26`). | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-test-15 | Test | MED | "Shrink-only" is enforced only for the map's baseline: unarmed-branches grew from 9 rows to 159, and drift tracks 5 of the 27 lists by hand (`research-retrofit-a.md:27`). | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-test-16 | Test | MED | A count pin over code acts as a waiver, since a fixed offender plus a new one nets to zero; `VERB_OFFENDER_PIN`, the lexicon's instance, rose from 412 to 1,087 (`research-retrofit-b.md:31`, and `gap-mem-10`). | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-test-17 | Test | LOW | Label keys churn: `b0f5247a9` renamed a key that the baseline's header does not record (`research-retrofit-b.md:237`). | the retrofit round's `[gaps-proposed]` (`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) | — |
| gap-deploy-01 | Deploy | HIGH | An adopter's own release, environments, rollout, rollback and post-deploy verification are not addressed; one adopter built all of it outside gov. The release slot after the landing, its environments and its exit record are this gap's (the expansion round). | deploy §4; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-deploy-02 | Deploy | HIGH | The post-landing verdict is inert: `GATE_POST_MERGE` declared in 0 of 3 trees, `refs/gov/bar-red` absent, CI cannot publish. Its verdict sits in one last-verdict file a later landing overwrites, with no record keyed by the landed SHA. Revised 2026-10-17, the debt round: the per-SHA verdict record carries the verdict and the publication state apart, on every exit path, a failed publication included. | deploy §4 | — |
| gap-deploy-03 | Deploy | HIGH | No CI job is emitted into adopters; one adopter's six workflows never call the bar. | deploy §4 | — |
| gap-deploy-04 | Deploy | HIGH | Adopter currency is unwatched: receipts 990 commits behind after six days; `update` is pull-only; no fleet register. | deploy §4 | — |
| gap-deploy-05 | Deploy | MED | Outbox orders are graded by nothing (one adopter holds 16, five of them rollbacks). | deploy §4 | — |
| gap-deploy-06 | Deploy | MED | Landing and release have no review, no role and no changelog. | deploy §4 | — |
| gap-deploy-07 | Deploy | MED | A killed hook on Windows still lands an ungated push; hooks-path drift is only a note; the lander kit is unversioned with an undeclared dependency. | deploy §4 | — |
| gap-deploy-08 | Deploy | LOW | The runbook is 163 KB of narrative under an existence-only parity check; `[isolate]` ports and the `up —` line are stated only. | deploy §4 | — |
| gap-deploy-09 | Deploy | MED | The lander's outcomes are no interface. Exit 0 covers a gated landing, an ungated stub-vetted one and a no-op push. Exit 1 covers the refusals before the push (a mint or regen failure, a reconcile conflict, a carried commit, the tip moved, and the pre-push hook's gate-red, head-moved, signalled and precondition refusals), a landing whose marker failed, and an unreachable remote. An adapter must read lines, the hook's allow and bar records and the remote to route a landing. | the fold's follow-up round, M2 and M3 (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`) | — |
| gap-deploy-10 | Deploy | MED | `GATE_POST_MERGE=ci` binds nothing: the lander starts no bar under it, and the pre-push hook reads only `refs/gov/bar-red`, though flow-steps names the CI result as the witness. A remote red under `ci` never reaches `refs/gov/bar-red`, and no fallback is named with integrations absent (the expansion round's review). | `tools/push-main.sh:434`; `.githooks/pre-push:1919-1936`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-deploy-11 | Deploy | MED | No release has ever been cut: no release tag, no changelog, and 10 of 29 kit entries declare no version. The version slot in `test.merge`, which `kits.version` fills, is this gap's (the expansion round's review). | `git tag`; `govkit epoch`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-deploy-12 | Deploy | MED | A receipt records gov's source as a local path, so an adopter cannot resolve where its install came from. | `tools/govkit/govkit.py:8020`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-deploy-13 | Deploy | HIGH | govkit's update runs seven kinds of code the target repository authored, with the operator's whole environment and the node's ambient credential: each touched kit's `[check]` argv before and after the write, each `[[contract]]` parity probe, its `[[hole]]` discharge probes, its `[[regenerate]]` argvs, the hook-fragment wiring through its `settings-merge.py`, gained kits' adopters, and the target's own git hooks, which update's git writes in the target fire (`git add`, `rm`, `mv`, `update-index` and `checkout-index`; an index write fires post-index-change, a ref update reference-transaction). `GOVKIT_RERENDER=0` declines four of them and leaves the `[check]` argvs, the parity probes and the git hooks running, so an unattended update into an adopter would run that adopter's code with gov's push rights. The design adds an eighth, dShippedRelease's update hook calling `test.seed` and `adopt`. Revised 2026-10-17: this row once said five kinds, then six, and that the switch left the hole probes running; the target-spawn probe's revision found the git hooks. | `tools/govkit/govkit.py:10015`, `:11214` (`run_kit_check`, run with the target as its working directory at `:5051`), `:10953`, `:11800` (`run_hole_probes`, cwd at `:5012`), `:10986`, `:11094` (`run_fragment_merges`, gated at `:11093`, cwd at `:5888`), `:11114-11119`; `:9658` (`derive_parity_lines`, the parity probe run at `:6065`); the target-spawn probe, first run in `build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared-instruments.md` `[probes-expansions]` and revised in `build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md` `[probes-final]`; `_cmd_apply`'s own warning at `:7360-7363`; `credential.helper=manager` from the system gitconfig; the expansion round's review, `build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md`, its closing review, `reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`, and the follow-up round, `reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md` | — |
| gap-maint-01 | Maintain | HIGH | No cadence: no declared cadence item runs on a schedule. The only scheduled actors are the OS-scheduled resume tick, the desktop durable-restart task and CI's read-only cron, and in-session cron expires after 7 days; corrected by the runtime layer's review. | maintain §4; runtime `[current]` | — |
| gap-maint-02 | Maintain | HIGH | Detectors without owners: 15 of 27 drift signals nonzero, most report-only, 2 dead probes. | maintain §4, instrument 1 | — |
| gap-maint-03 | Maintain | HIGH | The governing surface only grows, and nothing prices or retires a leg, rule or bug class. | maintain §4, instrument 2 | — |
| gap-maint-04 | Maintain | HIGH | Records dominate the work: 1,598 of 2,827 commits in 30 days touched only `memory/`. (main loop) | maintain instrument 3 | — |
| gap-maint-05 | Maintain | MED | Run records and dormant builds never close: 89 live `RUN.md`, 10 non-terminal for merged work. | maintain §4 | — |
| gap-maint-06 | Maintain | MED | The map goes stale: 28 of 31 dossiers older than their paths. | maintain §4 | — |
| gap-maint-07 | Maintain | MED | Ratchets that should shrink do not (3 of 5), timeouts are retried and forgotten, and reaping is manual: procmon-hook only dry-runs the sweep, 44 idle processes were flagged in 60 days and 4 were killed by hand. | maintain §4; runtime `[current]` | — |
| gap-maint-08 | Maintain | LOW | Naming offense rate and dangling ledger pointers are report-only. | maintain §4 | — |
| gap-maint-09 | Maintain | MED | The seven gateable drift signals are change-caused witnesses, yet the core bar reaches them through the observability kit, so a core leg depends on an expansion. Five become core legs, and the two lexicon signals the lexicon's leg pack (`gap-lex-08`). | `tools/gate-legs.json:1034-1049`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-maint-10 | Maintain | LOW | A reading varies with the tree it is taken in: 14 of 108 repeated (head, base, signal) groups differ in value or denominator. | `.git/drift-history.tsv`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-maint-11 | Maintain | LOW | The remote-CI drift signal is dead: it shells to `gh`, absent on this node, and is not asked under `--check`. | `tools/drift-audit/drift_report.py:3333-3341,3385-3390`; the expansion round, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md` | — |
| gap-review-01 | Review | HIGH | Review exists at two stages only; Plan, Test, Deploy and Maintain have none. | every record §3 | — |
| gap-review-02 | Review | HIGH | No review of the loop itself: no retrospective reads the loop's metrics and changes a stage contract. | maintain §3, §4 | — |
| gap-review-03 | Review | MED | Review cost is high: a spec audit runs 11 or 12 agents (9 when this row was written) and about 0.81 M tokens, and that cost is why audits are off by default. | design §5 C3; agent count re-measured by the review system's research, 2026-10-15 | — |
| gap-review-04 | Review | HIGH | Design records are audited by a unit-spec preset: the spec lenses aim at unit-spec sections, and every defect found after the runtime design's two rounds (security, cost, alternatives, assumptions, adopter migration, portability) fell outside them. | review system `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md` | — |
| gap-review-05 | Review | MED | One defect splits across items by grade: same-address pairs with different grades were merged 0 times in 110, and synthesizers named the split 29 times. | review system `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md` | — |
| gap-review-06 | Review | MED | Twins meet different skeptics: ids are assigned by lens and batches are contiguous slices, so only 8% of same-address pairs share a skeptic, and each of the 9 verified refutations by design beside a confirmed twin sat in a different batch. | review system `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md` | — |
| gap-review-07 | Review | MED | Proposed gates have no home: 56% of 721 name nothing and 2% a bug class, and 2 of 5 round-2 reports re-found a defect whose fix had covered the instance, not the class. | review system `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md` | — |
| gap-review-08 | Review | LOW | Duplicates count as refuted, understating precision (0.866 pooled against 0.880 merged), and the orphan-duplicate check runs on the spec kind only. | review system `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md` | — |
| gap-review-09 | Review | LOW | Review records contradict the code: REVIEW-PROTOCOL.md lists retired lenses, allows three to six and calls skeptics default-refute; agent-cap.js says tier2-review has four lenses; the synthesizer's role says it is handed confirmed findings only. | review system `[current]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md` | — |
| gap-review-10 | Review | MED | Left-shift has no witness: 724 of 907 confirmed findings in the 36 review appendices with a classes column carry no class and no disposition, the harness falls back to bare `C<n>` labels, and 13 of 124 class records cite the review that filed them. | the library round's research, `build/2026-10-16-build-PLAY-dClosedLoop-1-research-library-paths.md` | — |
| gap-review-11 | Review | MED | Nothing reads the review-shape line, and it carries no effort or shape. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-review-12 | Review | MED | Twin merges have no item, record kind or check. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |
| gap-review-13 | Review | LOW | The review harness spawns an untyped agent that no stage declares. | the systems round's `[gaps-proposed]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`), from its `[agreement]` | — |

The counts are derived, never typed: a first draft typed 59 rows here over a table holding 56. The
instrument, run against this file, and its output when the register was written:

```bash
grep '^| gap-' <this file> | awk -F'|' '{gsub(/ /,"",$3); gsub(/ /,"",$4); s[$3]++; v[$4]++} END {for (k in s) printf "%s=%d ", k, s[k]; print ""; for (k in v) printf "%s=%d ", k, v[k]; print ""}'
```

```text
Deploy=8 Plan=7 Spine=8 Test=9 Review=3 Build=4 Maintain=8 Design=9
LOW=5 MED=23 HIGH=28
```

Re-measured after round 4 added `gap-spine-06`, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Build=4 Maintain=8 Design=9
LOW=5 MED=23 HIGH=29
```

Re-measured after the foundations revisit's step 1 added the four owner-raised `gap-found-*` rows,
same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=4 Build=4 Maintain=8 Design=9
LOW=5 MED=24 HIGH=32
```

Re-measured after step 1's continuation added `gap-found-05` and `gap-found-06`, same instrument. The
Stage column groups the owner's foundations; `gap-found-06` is owned by the Spine, which builds the
`next` verb:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=6 Build=4 Maintain=8 Design=9
LOW=5 MED=24 HIGH=34
```

Re-measured after the core consistency step added `gap-found-07` and `gap-found-08`, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=8 Build=4 Maintain=8 Design=9
LOW=5 MED=24 HIGH=36
```

Re-measured after the flow walk's Plan and Design stages added four `gap-flow-*` rows, same
instrument:

```text
Deploy=8 Plan=7 Flow=4 Spine=9 Test=9 Review=3 Foundation=8 Build=4 Maintain=8 Design=9
LOW=5 MED=26 HIGH=38
```

Re-measured after the flow walk's Build stage and the flow-interactions round added `gap-flow-05`
to `gap-flow-09`, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=30 HIGH=39
```

Re-measured after the orientation round added `gap-orient-01` to `gap-orient-10`, measured by the four
orientation researchers and the main loop, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Orient=10 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=33 HIGH=46
```

Re-measured after the adopted preservation research added `gap-orient-11` to `gap-orient-13`, same
instrument:

```text
Deploy=8 Plan=7 Spine=9 Orient=13 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=34 HIGH=48
```

Re-measured after the roles round added `gap-roles-01` to `gap-roles-08`, measured by the four roles
researchers, same instrument:

```text
Roles=8 Deploy=8 Plan=7 Spine=9 Orient=13 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=36 HIGH=54
```

Re-measured after the compaction experiment added `gap-orient-14` and `gap-roles-09`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-results.md`), same instrument:

```text
Roles=9 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=6 MED=36 HIGH=55
```

Re-measured after layers round one added `gap-found-09` to `gap-found-17`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`), same instrument:

```text
Roles=9 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Review=3 Foundation=17 Build=4 Flow=9 Maintain=8 Design=9
LOW=7 MED=39 HIGH=60
```

Re-measured after layers round two added `gap-flow-10` to `gap-flow-14`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md`), same instrument:

```text
Roles=9 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Review=3 Foundation=17 Build=4 Flow=14 Maintain=8 Design=9
LOW=7 MED=41 HIGH=63
```

Re-measured after layers round three added `gap-roles-10` to `gap-roles-17`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`), same instrument:

```text
Roles=17 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Review=3 Foundation=17 Build=4 Flow=14 Maintain=8 Design=9
LOW=9 MED=45 HIGH=65
```

Re-measured after round four's opening added `gap-roles-18`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`, `[owner-notes]`), same instrument:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Review=3 Foundation=17 Build=4 Flow=14 Maintain=8 Design=9
LOW=9 MED=46 HIGH=65
```

Re-measured after layers round four added `gap-mem-01` to `gap-mem-11` and `gap-tool-01` to
`gap-tool-06` (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`), same instrument:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Tooling=6 Review=3 Foundation=17 Build=4 Memory=11 Flow=14 Maintain=8 Design=9
LOW=13 MED=55 HIGH=69
```

Re-measured after the lexicon review added `gap-lex-01` to `gap-lex-07`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`), same instrument:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Lexicon=7 Tooling=6 Review=3 Foundation=17 Build=4 Memory=11 Flow=14 Maintain=8 Design=9
LOW=14 MED=58 HIGH=72
```

Re-measured after the runtime layer's review added `gap-rt-01` to `gap-rt-10`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`), same instrument. `gap-maint-01` and
`gap-maint-07` took corrected facts, and their grades are unchanged:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Runtime=10 Lexicon=7 Tooling=6 Review=3 Foundation=17 Build=4 Memory=11 Flow=14 Maintain=8 Design=9
LOW=18 MED=60 HIGH=76
```

Re-measured after the review system's research added `gap-review-04` to `gap-review-09`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md`), same instrument. `gap-review-03` took the
measured agent count, and its grade is unchanged:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Runtime=10 Lexicon=7 Tooling=6 Review=9 Foundation=17 Build=4 Memory=11 Flow=14 Maintain=8 Design=9
LOW=20 MED=63 HIGH=77
```

Re-measured after the instruction layer's fold added `gap-rt-11` to `gap-rt-13`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`, `[revised]`), same instrument.
`gap-found-09`, `gap-found-10`, `gap-found-14`, `gap-found-17` and `gap-rt-10` took corrected facts, and
their grades are unchanged:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Runtime=13 Lexicon=7 Tooling=6 Review=9 Foundation=17 Build=4 Memory=11 Flow=14 Maintain=8 Design=9
LOW=20 MED=66 HIGH=77
```

Re-measured after the flow layer's fold added `gap-flow-15` and `gap-rt-14`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`, `[revised]`), same instrument.
`gap-flow-08` and `gap-flow-10` took corrected facts, and their grades are unchanged:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Runtime=14 Lexicon=7 Tooling=6 Review=9 Foundation=17 Build=4 Memory=11 Flow=15 Maintain=8 Design=9
LOW=20 MED=67 HIGH=78
```

Re-measured after the memory layer's fold added `gap-mem-12`
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`, `[revised]`), same instrument.
`gap-mem-03` and `gap-tool-06` took corrected facts, and their grades are unchanged. The roles layer's
fold added no gap, and `gap-roles-10`, `gap-roles-12` and `gap-roles-18` took corrected facts:

```text
Roles=18 Deploy=8 Plan=7 Spine=9 Orient=14 Test=9 Runtime=14 Lexicon=7 Tooling=6 Review=9 Foundation=17 Build=4 Memory=12 Flow=15 Maintain=8 Design=9
LOW=21 MED=67 HIGH=78
```

Re-measured after the follow-up round added `gap-deploy-09`, `gap-mem-13` and `gap-mem-14`
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`) and the library round added `gap-review-10`
and `gap-mem-15` (`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`), same instrument. The
follow-up round's fold owed this block and left it out, and the library round's review caught it.
`gap-test-04`, `gap-deploy-02`, `gap-mem-02`, `gap-mem-03`, `gap-mem-11`, `gap-mem-15`, `gap-design-05`,
`gap-design-07`, `gap-found-17` and `gap-flow-15` took corrected or added facts, and their grades are
unchanged:

```text
Roles=18 Deploy=9 Plan=7 Spine=9 Orient=14 Test=9 Runtime=14 Lexicon=7 Tooling=6 Review=10 Foundation=17 Build=4 Memory=15 Flow=15 Maintain=8 Design=9
LOW=22 MED=70 HIGH=79
```

Re-measured after the expansion round added twenty gaps, `gap-maint-09` to `gap-maint-11`, `gap-test-10` to
`gap-test-13`, `gap-rt-15` to `gap-rt-19`, `gap-mem-16`, `gap-deploy-10` to `gap-deploy-12`, `gap-spine-07`,
`gap-found-18`, `gap-found-19` and `gap-tool-07`
(`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`), same instrument. `gap-tool-02` and
`gap-tool-04` took added facts, and their grades are unchanged:

```text
Roles=18 Deploy=12 Plan=7 Spine=10 Orient=14 Test=13 Runtime=19 Lexicon=7 Tooling=7 Review=10 Foundation=19 Build=4 Memory=16 Flow=15 Maintain=11 Design=9
LOW=26 MED=84 HIGH=81
```

Re-measured after the expansion round's review added `gap-deploy-13` and `gap-lex-08`
(`build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md`), same instrument.
`gap-test-02`, `gap-test-11`, `gap-deploy-01`, `gap-deploy-10`, `gap-deploy-11`, `gap-rt-15`,
`gap-found-17`, `gap-maint-09` and `gap-tool-02` took added facts, `gap-test-12` and `gap-spine-07`
were corrected, and their grades are unchanged:

```text
Roles=18 Deploy=13 Plan=7 Spine=10 Orient=14 Test=13 Runtime=19 Lexicon=8 Tooling=7 Review=10 Foundation=19 Build=4 Memory=16 Flow=15 Maintain=11 Design=9
LOW=27 MED=84 HIGH=82
```

Re-measured after the debt round moved `gap-mem-10` to area Lexicon, as L-4 had, same instrument.
`gap-lex-02` to `gap-lex-04`, `gap-mem-13`, `gap-mem-15`, `gap-test-04`, `gap-deploy-02`, `gap-deploy-13`,
`gap-design-05` and `gap-design-07` took corrected or added facts in the debt round's folds
(`build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md`), and their grades are unchanged:

```text
Roles=18 Deploy=13 Plan=7 Spine=10 Orient=14 Test=13 Runtime=19 Lexicon=9 Tooling=7 Review=10 Foundation=19 Build=4 Memory=15 Flow=15 Maintain=11 Design=9
LOW=27 MED=84 HIGH=82
```

Re-measured after the systems and retrofit rounds added twenty-six gaps, `gap-found-20` to `gap-found-23`,
`gap-design-10`, `gap-mem-17` to `gap-mem-25`, `gap-roles-19`, `gap-roles-20`, `gap-rt-20`, `gap-rt-21`,
`gap-review-11` to `gap-review-13`, `gap-test-14` to `gap-test-17` and `gap-build-05`
(`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`, `build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`),
same instrument. A join of these 219 keys against v2's chain rows finds each owned by exactly one build:

```text
Roles=20 Deploy=13 Plan=7 Spine=10 Orient=14 Test=17 Runtime=21 Lexicon=9 Tooling=7 Review=13 Foundation=23 Build=5 Memory=24 Flow=15 Maintain=11 Design=10
LOW=33 MED=100 HIGH=86
```

Re-measured after the project-map round added three gaps, `gap-mem-26`, `gap-mem-27` and `gap-orient-15`
(`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`), same instrument. A join of these 222 keys against v2's chain rows finds each owned by exactly one
build:

```text
Roles=20 Deploy=13 Plan=7 Spine=10 Orient=15 Test=17 Runtime=21 Lexicon=9 Tooling=7 Review=13 Foundation=23 Build=5 Memory=26 Flow=15 Maintain=11 Design=10
LOW=33 MED=102 HIGH=87
```
