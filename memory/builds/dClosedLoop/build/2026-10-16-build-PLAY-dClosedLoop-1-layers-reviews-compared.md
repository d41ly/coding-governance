# Research: layers 1 to 4, each reviewed twice at Tier 2, compared

**Serves:** research PLAY-dClosedLoop-1

Before the Knowledge layer, the owner asked for two Tier-2 rounds on each of layers 1 to 4, "same as
Runtime" (the session log's `Events`, 2026-10-15). This record compares each layer's two rounds defect
by defect, and sets the four comparisons beside the runtime layer's. It also plans the fold. Six
defects contradict answers the owner settled, so they go to the owner first, in `[forks]`.

## [runs] The eight rounds

- **Subjects:** each layer's record, at the blob HEAD held at `3611a60e9`, where all eight rounds ran:

  | Layer | Subject | Blob |
  |---|---|---|
  | instruction | `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md` | `3cfd547af6f355c5df687331f71a945f56a2e140` |
  | flow | `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md` | `7031c90f195ce746943196d2dc570b84dd753b63` |
  | flow | `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md` | `43e9cf4b27292b535aa24a2680a73cd663a62e34` |
  | roles | `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md` | `081ef3c1a150617101b948c3f276900abd0a2dd5` |
  | memory | `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md` | `bb5dd4e2d648746f6656f7e766261aaea8964b96` |

- **Harness:** the runtime rounds' harness: `tools/workflows/tier2-review.js`, with five lenses
  (`gov-spec-reviewer`), five skeptic batches (`gov-skeptic`) and synthesis (`gov-synthesizer`). Every
  role ran at medium effort.
- **Runs and reports:**

  | Layer | Run A | Run B | Reports |
  |---|---|---|---|
  | instruction | `wf_261507e4-5ca` | `wf_c5538013-6cc` | `reviews/2026-10-15-review-PLAY-dClosedLoop-1-instruction-{a,b}.md` |
  | flow | `wf_1532dea2-2f7` | `wf_782666f6-e98` | `reviews/2026-10-15-review-PLAY-dClosedLoop-1-flow-{a,b}.md` |
  | roles | `wf_478254d1-ce0` | `wf_08c634a0-1b4` | `reviews/2026-10-15-review-PLAY-dClosedLoop-1-roles-{a,b}.md` |
  | memory | `wf_b6756400-d03` | `wf_ec731bfc-925` | `reviews/2026-10-15-review-PLAY-dClosedLoop-1-memory-{a,b}.md` |

  Memory's run A first launched as `wf_c5046686-f17`. That run stopped with the session before any
  agent completed, and was relaunched with the same args.
- **The args:** `make_args.py` wrote all eight from each layer's subjects, specs and section tags.
  - A layer's two runs differ only in the run label ("this is run A"), the report path and the
    scratch path.
  - The flow and roles contexts each add one sentence. The owner holds a revisit of the flow layer's
    relations to the other layers, and of the roles layer's mechanical shape. A finding about either is
    still reported, as input to that revisit.
  - The instruments record holds the script, and each layer's round B args.
- **The admission:** the runtime rounds' one-off opt-in, in the working tree only. It was restored once
  the eighth round returned (the session log's `Events`).
- **The ledger:** the roles kit derived every agent and returned line. The session log holds them, and
  the instruments sum their output from there.

## [method] How the rounds were compared

The runtime comparison's `[method]` applies unchanged:
- every finding of both rounds, confirmed or refuted, is placed on the defect it names;
- a finding that names two defects lands on both;
- a round finds a defect when one of its findings on it was confirmed;
- the defect takes the highest grade any confirmed finding on it got, the skeptic's where one was given.

There are four additions:
- **One map per layer**, under `[map-<layer>]`. The comparison script now takes the map's section tag
  as an argument. On the runtime record's own map, its output is unchanged.
- **A bundled finding carries its grade to every defect it lands on.** One memory defect is high only
  through a bundle's second clause: `kind-list-incomplete`, through B21, whose grade rests on
  `record-idempotence`.
- **A refuted finding's twin is looked up on the first row that holds it.** So each map puts a
  finding's main defect first.
- **The tables are derived.** `summarize_layers.py` runs the comparison over all five maps and prints
  `[summary]`'s two tables. Each layer's output matched its earlier run line for line.

## [summary] Five layers side by side

| Layer | Findings A / B | Confirmed A / B | Precision A / B | Out A / B |
|---|---|---|---|---|
| runtime | 60 / 61 | 56 / 57 | 0.93 / 0.93 | 212.2k / 218.0k |
| instruction | 48 / 47 | 44 / 36 | 0.92 / 0.77 | 220.2k / 230.3k |
| flow | 69 / 46 | 60 / 45 | 0.87 / 0.98 | 258.4k / 222.8k |
| roles | 47 / 54 | 37 / 43 | 0.79 / 0.80 | 196.8k / 240.8k |
| memory | 61 / 58 | 52 / 51 | 0.85 / 0.88 | 300.7k / 282.0k |
| all five | 285 / 266 | 249 / 232 | 0.87 / 0.87 | 1188.3k / 1193.9k |

| Layer | Defects | Both | A only | B only | A alone covers | B alone covers | Overlap | Chapman: found by neither | High defects | High, one round only | Shared, graded alike | Refuted, with a confirmed twin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| runtime | 59 | 32 | 14 | 13 | 78% | 76% | 0.54 | 6 | 8 | 2 | 28 of 32 | 6 of 8 |
| instruction | 48 | 19 | 15 | 14 | 71% | 69% | 0.40 | 10 | 5 | 0 | 14 of 19 | 7 of 15 |
| flow | 57 | 28 | 15 | 14 | 75% | 74% | 0.49 | 7 | 8 | 2 | 18 of 28 | 6 of 10 |
| roles | 33 | 17 | 6 | 10 | 70% | 82% | 0.52 | 3 | 2 | 1 | 15 of 17 | 11 of 21 |
| memory | 68 | 34 | 15 | 19 | 72% | 78% | 0.50 | 8 | 6 | 1 | 22 of 34 | 10 of 16 |
| all five | 265 | 130 | 65 | 70 | 74% | 75% | 0.49 | 35 | 29 | 6 | 97 of 130 | 40 of 70 |

- **Overlap** is the defects both rounds found, over all the defects either found.
- **Chapman: found by neither** is Chapman's estimate of the population, less the defects found. It
  assumes every defect was equally findable by each round. Easy defects are found by both, which
  inflates the overlap, so read it as a floor.
- **High, one round only** counts the high defects one round missed outright. A defect both rounds
  found but graded differently counts in **Shared, graded alike** instead.

## [patterns] What the five comparisons show

- **One round finds three quarters of what two find.**
  - Alone, a round covers 69% to 82% of its layer's defects, and 74% and 75% over all five layers.
  - The two rounds overlap at 0.40 to 0.54.
  - About 35 defects lie beyond both rounds across the five layers, 29 of them in layers 1 to 4.
  - The second round costs what the first does. Over the five layers it added 70 defects to round A's
    195, about a third more.
- **High defects slip past a single round.** Six of the 29 high defects were found by one round only.
  - Round A missed four: runtime's `cycle-spawns` and `structured-output`, roles' `repair-staleness`
    and memory's `v14-refusal-exists`.
  - Round B missed two: flow's `bar-attribution-unjoined` and `lander-exit-classes`.
  - The instruction layer's five high defects were found by both.
- **Adjudication is the noisier half.**
  - On identical args, a layer's two rounds confirmed at different rates: 0.92 and 0.77 on the
    instruction layer, 0.87 and 0.98 on the flow layer.
  - 40 of the 70 refuted findings sit on a defect that another finding confirmed, often in the other
    round. One skeptic refuted what another confirmed.
  - The two rounds graded 97 of the 130 shared defects alike.
  - dFairHearing's settled changes aim at exactly this: batches by address, a grade per id, twins shown
    to the synthesizer, and fix verdicts by class (`build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md`,
    `[answers]`).
- **Four classes of defect recur in every layer.**
  - **A record left stale by a later layer.** A settled layer amends v2 and the register, but not the
    earlier layer records it contradicts. Examples: `kit-layer-map-stale` and `runtime-deferral-stale`
    (instruction), `gap-flow-10-owner` (flow), `flow-roles-steps-stale` (roles), and `stale-lexicon-owner`
    and `stale-gap-tool-03` (memory).
  - **An existing seam left unnamed.** The design specifies new machinery beside a shipped mechanism
    that already does the work. Examples: `existing-budgets` and `roles-tag-join` (instruction),
    `owner-controls-exist` and `write-set-seams` (flow), `handoff-seam` (roles), and
    `v14-refusal-exists`, `reuse-affordance-seam` and `supersession-seam` (memory).
  - **Readers inventoried by name, not by value.** A retirement or rename counts its readers by name,
    and misses those that depend on the value. Examples: `section-number-readers` (instruction),
    `item-count-readers` (flow), and `spec10-token`, `reuse-probed-readers` and `decision-id-readers`
    (memory).
  - **A check proven by its first green run.** Examples: `join-population` and `grammar-red-case`
    (instruction), `matrix-arms-unseen` (roles), and `annotation-green-vacuous` and
    `flip-acceptance-unfailable` (memory).
- **Six defects contradict a settled answer.** They are `[forks]`' LR-1 to LR-6.

## [fold] The fold plan

The layers fold oldest first: instruction, flow, roles, then memory. Each later record is then folded
against its predecessors' corrected text. The main loop folds, as it folded the runtime layer.

Each defect takes one of four dispositions, written into its map row's `disposition` cell:
- **Amend:** the layer record states the fix, under a dated `Revised:` line. This covers:
  - stale statements;
  - wrong figures;
  - unnamed seams;
  - inventories by name;
  - design-level rules the record omits, such as `record`'s idempotence or the path by which a layer
    registers a record kind.
- **Gap:** the fix is unit-level, such as exact grammar inputs, thresholds or fixtures. The owning
  chain build carries it as a registered gap, with the defect's evidence.
- **Fork:** the fix would change an owner-settled answer. The six are in `[forks]`.
- **None:** the defect is refuted-only, and its row cites the skeptic's reason.

Four rules bound the fold:
- **The owner's revisits stay the owner's.** A defect that turns on the flow layer's relations to the
  other layers, or on the roles layer's mechanical shape, is folded as a fact. It is also handed to the
  revisit the owner holds. The fold does not redesign either.
- **A later layer's change reaches every earlier record.** Each stale statement gets its dated
  `Revised:` line, in every record that states it.
- **v2 and the register move in the same pass.** Where a fold touches them, the gap-ownership join and
  the preset check run again, each seen red first, as before.
- **The fold gets its own review.** Fold text is unreviewed surface. One light diff review (three
  lenses) runs over the fold's commits before the Knowledge layer opens.

## [forks] Asked, 2026-10-16

**LR-1. "`instructions.checks` lets `velocity` soften P27's load-set check to warn. Foundations C6 says
no switch turns a principle or its check off. Which holds?"**
- Behind it: `principle-check-switchable` (instruction).
- Offered:
  - Soften, never off (Recommended): warn and record still run the check and show every breach. C6 is
    amended to say a principle's check may soften by policy, but never be skipped. Velocity keeps warn.
  - Principles always refuse: a check that enforces a principle refuses under every preset.
    `instructions.checks` governs only the checks no principle names, and velocity loses warn on P27.
  - Only by owner exception: softening a principle's check is an entry in C6's owner-guarded exceptions
    register, never a preset value.

**LR-2. "Under `roles.trust=keyed`, P29 has a role act on `claimed` facts, which are an upstream agent's
judgment. P23 acts on no claim whose weakest source an agent typed. Which scopes which?"**
- Behind it: `p29-vs-p23` (roles).
- Offered:
  - Claimed facts guide, never decide (Recommended): a role works from every keyed fact. Nothing that
    changes state rests on a claimed fact without P23's re-derivation: a verdict, a position, a landing
    or a gate. P23 governs decisions, and P29 governs inputs.
  - Keyed is enough: a claimed fact whose key recomputes is acted on fully, and P23 is amended to exempt
    handed facts.
  - Witnessed only by default: `roles.trust` defaults to `witnessed-only`, so claimed facts arrive as
    evidence. `keyed` stays allowed.

**LR-3. "Under `run.on-owner-question=best-effort-recorded`, the default, the supervisor resolves owner
items itself. Nothing keeps an owner gate out of that: one of `autonomy`'s gates, or an owner breakpoint.
What happens when an unattended run reaches one?"**
- Behind it: `owner-gate-vs-question` (flow), found high by both rounds.
- Offered:
  - The build parks, the run goes on (Recommended): a gate is never a question. The build waits for the
    owner's disposition while the run works on other builds. A new key, `run.on-owner-gate`, holds
    `park-build` as its default, with `stop-run` allowed.
  - The run stops: the whole run halts at the first owner gate.
  - As `run.on-owner-question` says: a gate is an owner question, and best-effort resolves it and
    records the choice.

**LR-4. "`strict` and `guarded` set `build.closes=after-release-verifies`, which needs integrations. The
policy check refuses that value on a core-only install, so both presets fail their own check there. What
should happen?"**
- Behind it: `presets-fail-build-closes` (flow).
- Offered:
  - Fall back, reported (Recommended): a preset value whose expansion is absent resolves to the key's
    default, and the policy check reports the fallback instead of refusing. Installing the expansion
    restores the value. The rule covers every expansion-dependent preset value, through a new key,
    `policy.on-missing-expansion`: `fallback-reported` by default, `refuse` allowed.
  - Presets set core values: `strict` and `guarded` set `at-landing`, and an adopter with integrations
    raises it.
  - Presets need the expansion: `strict` and `guarded` refuse to apply on an install without
    integrations.

**LR-5. "F4-6 refuses an ask filed without an acceptance, on the premise that every core filer can state
one mechanically. Owner-raised, surfaced, expansion and supervisor-written asks cannot. backlog.py's V14
already refuses an ask filed since `ASK_CUTOFF` that carries neither `accept` nor a `seen … run`. What
may an acceptance be?"**
- Behind it: `ask-filer-coverage` and `v14-refusal-exists` (memory).
- Offered:
  - Mechanical where possible, stated otherwise (Recommended): core filers state one of the four
    mechanical forms. Every other filer states an `accept` line, as V14 takes today, and the ask's
    closing must cite it. Refusal stays the default, and V14 is the seam it extends.
  - Mechanical only: the four forms or nothing. Owner-raised and surfaced asks are restated in a
    mechanical form, or refused.
  - Refuse core filers only: the refusal applies to core flow filers. Owner, surfaced and expansion
    asks are filed and graded.

**LR-6. "F4-1 made reuse entries ranked instruction units. Only the instruction command changes those,
and agents may only propose (`instructions.edit`). Yet the build that ships a feature must carry its
entry for the `gov:feature` check, and the contract also lists the entry as a record kind that `record`
writes. How does a build's reuse entry land?"**
- Behind it: `reuse-entry-two-doors` and `reuse-entry-proposal-path` (memory).
- Offered:
  - Proposed with the build (Recommended): the builder proposes the entry through the instruction
    command, and the build's checks count the proposal. The owner's disposition of it is an owner item,
    and the entry renders into work orders once accepted. Its one door is the instruction command.
  - A record, not an instruction: `record` writes the entry, and it is handed as a fact, not a
    directive. This reverses F4-1's "instruction units".
  - The owner commands each one: the build parks at its landing until the owner commands the entry.

## [answers] Answered, 2026-10-16

The owner took the recommended option on LR-1, LR-2, LR-5 and LR-6, and another on LR-3 and LR-4.

| Fork | Answer | Key | Default | Also allowed |
|---|---|---|---|---|
| LR-1 | Soften, never off | none: C6 is amended, and `instructions.checks` stands | — | — |
| LR-2 | Claimed guides, never decides | none: P29 is amended, and `roles.trust` stands | — | — |
| LR-3 | As `run.on-owner-question` says | none: the offered alternatives are that key's own values | — | — |
| LR-4 | Presets need the expansion | `policy.on-missing-expansion` | `refuse` | `fallback-reported` |
| LR-5 | Mechanical, else stated | none: `asks.acceptance` stands, and an acceptance gains a definition | — | — |
| LR-6 | Proposed with the build | none: the choice is structural | — | — |

What each answer changes, applied by the fold:
- **LR-1:** foundations C6 is amended. A principle's check may soften by policy to `warn` or `record`.
  Both still run the check and show every breach, and no switch skips it. `velocity` keeps `warn`.
- **LR-2:** v2's P29 is amended. A producing role works from every keyed fact. A `claimed` fact guides
  the work, but nothing that changes state rests on it without P23's re-derivation: a verdict, a
  position, a landing or a gate. P23 governs decisions, and P29 governs inputs.
- **LR-3:** an owner gate is an owner item, resolved as `run.on-owner-question` says.
  - Under `best-effort-recorded`, the supervisor's choice is recorded as the gate's witness. The
    owner's own disposition is the other witness it may have.
  - An adopter who wants gates held sets `park-item`, `park-build` or `stop-run`, the alternatives
    LR-3 offered. `strict` already sets `park-item`.
  - Best effort never accepts an instruction proposal. `instructions.edit` is a guard that presets
    never touch, so a proposal stays open until the owner disposes of it (LR-6).
- **LR-4:** a preset whose value needs an absent expansion is refused when it is selected, so `strict`
  and `guarded` need integrations. `policy.on-missing-expansion` holds that rule.
  - Its default is `refuse`.
  - `fallback-reported` is allowed: such a value resolves to the key's default, and the policy check
    reports the fallback.
  - Presets never set the key, since it governs how a preset applies.
- **LR-5:** a core filer states one of the four mechanical acceptances. Every other filer states an
  `accept` line, and the ask's closing must cite it. Refusal stays the default. dTotalRecall extends
  backlog.py's V14 and its `ASK_CUTOFF`, which already refuse an ask without one. F4-6's "as today" is
  corrected.
- **LR-6:** the builder proposes the reuse entry through the instruction command. The build's
  `gov:feature` check counts a proposed entry. The owner's disposition of it is an owner item, and the
  entry renders into work orders once accepted. The record kind list drops the reuse entry, so its one
  door is the instruction command.

## [map-instruction] The instruction layer's findings, placed

Run A is `wf_261507e4-5ca` and run B is `wf_c5538013-6cc`. The ids are each report's appendix ids.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `tag-spelling` | R-B fixes no tag spelling: example tags carry no namespace, and item and policy names collide (`design.reentry`, `build.scope`) | 1, 35 | — | amend; `layer-instruction` `[revised]` |
| `example-item-names` | R-B's example item tags are spelled differently from the settled items (`plan.intake` for `plan.input`, `build.unit-commit` for `build.unit-pass`) | — | 8 | amend; `layer-instruction` `[revised]` |
| `kit-layer-map-stale` | the kit-to-layer map v2 points to is stale: `next`, runlog's journal grammar, the research kind, unattended as "the executor", process-monitor and the reuse lookup all moved in later layers | 2, 32 | 14, 33 | amend; `layer-instruction` `[revised]` |
| `runtime-deferral-stale` | [settled] still defers Runtime's build to the re-cut, and [layers] calls the turnstile and the lander homeless runtime items, though dWellOiledMachine exists and Deploy keeps both | 12, 21, 32 | 14, 26, 33 | amend; `layer-instruction` `[revised]` |
| `stale-figures` | counts written before later layers: 94 keys, P1 to P26, a 67 KB largest guide | 21 | 16 | amend; `layer-instruction` `[revised]` |
| `skills-layer-split` | R-F files Skills and kits under different layers from the kit table, names a layer that does not exist, and keeps deploy-governance as a core entry that Distribution and the memory layer place elsewhere | 3, 18 | 28 | amend; `layer-instruction` `[revised]` |
| `harness-injected-loads` | R-C's refusing render and R-H's memory-index budget cannot reach loads the harness injects from outside the repository: the auto-memory index and the Skill and agent lists | 4, 44 | 32, 39 | amend; `layer-instruction` `[revised]` |
| `act-session-load-point` | the load-point inventory has no row for Runtime's act session, and the ladder gives its static block no level | 5, 38 | 29 | amend, gap; `layer-instruction` `[revised]` |
| `codex-override` | Codex reads one instruction file per directory, so an override file replaces the charter; the 32 KiB cap covers the combined text; and nothing refreshes the override, since Codex has no SessionStart | 6, 14, 39 | 31, 40 | amend, gap; `layer-instruction` `[revised]` |
| `harness-load-point-owner` | three places claim the per-harness load points: R-K's literal table, [layers]' Distribution row and the kit table, while Runtime gives them to registered harness adapters | 33 | 40 | amend; `layer-instruction` `[revised]` |
| `agent-instructions-seam` | the agent-instructions kit already wires each harness's instruction file and measures Codex's 32 KiB limit, and R-K neither names nor matches it | 26 | 24 | amend; `layer-instruction` `[revised]` |
| `join-population` | dOrderedCharter arms the both-ways joins before the builds that populate steps, items and roles exist, with no non-empty assertion | 7 | — | amend; `layer-instruction` `[revised]` |
| `charter-before-policy` | dOrderedCharter's units consume policy keys whose file, reader and guard land with dDeclaredLoop, its child | — | 6 | owed; `layer-instruction` `[revised]` |
| `write-path-bypass` | validation sits in the instruction command alone: edits at structured sources, merges, adopter overlays and kit installs bypass it, the lock is local, and partial failure is unspecified | 8, 43 | 44 | amend; `layer-instruction` `[revised]` |
| `knowledge-in-core-render` | the one-way rule covers work-order fields only, while the memory layer renders Knowledge's gotcha classes into every role's static block, a core render | 9 | — | amend; `layer-instruction` `[revised]` |
| `effectiveness-citations` | R-J measures effectiveness and prunes units from returns that cite unit tags, but no return schema has the field and "followed" is agent-typed, which P23 never acts on | 10, 48 | 46 | amend; `layer-instruction` `[revised]` |
| `effectiveness-seam` | runlog's prose measure already checks final messages against the micro-format units, and R-J does not name it | — | 23 | none; `layer-instruction` `[revised]` |
| `heading-grammar` | R-D lets headings be directives or scope statements, while v2's P11 says headings are directives | 11 | — | amend; `layer-instruction` `[revised]` |
| `gap-count-mismatch` | [uncovered] proposes eight gaps and [settled] registers nine, and gap-found-17 appears in no [uncovered] entry | 13 | — | amend; `layer-instruction` `[revised]` |
| `skill-description-count` | "nine Skill descriptions" is wrong for this tree: seven project Skills, session-kickoff through a symlink, user Skills beside them, and deploy-governance not a Skill | 15 | 13 | amend; `layer-instruction` `[revised]` |
| `hook-injected-loads` | text hooks inject (SubagentStart context, Stop block reasons, deny reasons, SessionStart output) is a load point outside the unit registry, its grammar and its budgets | 16, 41 | — | amend, gap; `layer-instruction` `[revised]` |
| `lexicon-dependency` | R-B's tag registry depends on the lexicon, a Knowledge expansion, against P28 | 17 | 27, 45 | amend; `layer-instruction` `[revised]` |
| `trigger-read-bytes` | the trigger-read byte figure counts guides no pointer names, and the kickoff engine's bytes are executed code, not loaded text | 19 | — | amend; `layer-instruction` `[revised]` |
| `crlf-byte-counts` | the byte counts were taken on a CRLF working copy, and R-C never says which bytes a budget measures | 20 | — | amend; `layer-instruction` `[revised]` |
| `existing-budgets` | gap 2 and R-C ignore the per-load-point byte budgets already declared, gated and ratcheted over six load points | 22, 31 | 11, 18 | amend; `layer-instruction` `[revised]` |
| `retired-summed-budget` | R-C's summed budget over a session's reads is what TOOL-dSpentCeiling-1 retired, uncited | 23 | — | amend; `layer-instruction` `[revised]` |
| `tag-registry-seams` | R-B mints item tags without naming the unattended driver's DIRECTIVES_CORE and DOD_CORE handle registries | 24 | — | amend; `layer-instruction` `[revised]` |
| `roles-tag-join` | the record says rule tags key the renderer and nothing else, but the roles kit already joins rule tags to roles and selects each role's units by tag | 29 | 10, 17 | amend; `layer-instruction` `[revised]` |
| `section-number-readers` | retiring numbered sections breaks readers keyed on them: roles_lib finds the rules under `## 1.`, and the hygiene gate and review prompts grade by section number | 29, 47 | 20 | amend; `layer-instruction` `[revised]` |
| `one-source-roles-list` | the charter's role list and the harness's agent list are already rendered from one source | 25 | — | amend; `layer-instruction` `[revised]` |
| `grammar-check-seams` | R-D designs a grammar check from scratch beside the existing instruction gates: check-microformats, format-guard, check-playbook-parity's § arm and others | 27 | 19 | amend; `layer-instruction` `[revised]` |
| `ladder-renumber-carriers` | the renumbered ladder leaves foundations R2's envelope and gate, v2's revision notes and [fit]'s "rank 3" on the old values | 28 | 38 | amend; `layer-instruction` `[revised]` |
| `card-rank-or5` | the card at level 1 below the charter departs from OR-5's priority 1 beside it | — | 15 | none; `layer-instruction` `[revised]` |
| `provenance-marker-readers` | moving provenance out of loaded text names none of the markers' readers: the template marker, the playbook region, the install receipt | 30 | 21, 37 | none; `layer-instruction` `[revised]` |
| `microformats-fence` | re-assembling the charter retires the micro-formats fence, which four readers key on and format-guard fails open without | — | 35 | none; `layer-instruction` `[revised]` |
| `governing-document-rename` | renaming "governing document" to "instruction unit" leaves v2's dOrderedCharter row and foundations C3 on the old name | 36 | — | amend; `layer-instruction` `[revised]` |
| `gap-found-17-stale` | gap-found-17 still says runtime machinery has no layer or build | 37 | — | amend; `layer-instruction` `[revised]` |
| `owner-proof` | the instruction write path takes no proof that its caller is the owner, unlike the policy path's `policy.proof` | 40 | 34 | amend; `layer-instruction` `[revised]` |
| `load-set-contents` | R-C's load set omits the task and the handed facts, its refusal has no caller action and no unit, and its "too little" refusal cannot fail | 42 | 42 | amend; `layer-instruction` `[revised]` |
| `grammar-red-case` | the grammar check is proven red only on planted prose, not on the defect kinds the record found | 45 | 41 | amend; `layer-instruction` `[revised]` |
| `grammar-template-type` | the closed grammar has no type for a template skeleton or a literal format block | 46 | — | none; `layer-instruction` `[revised]` |
| `reuse-entries-units` | the memory layer's reuse entries are level-3 units of strength MUST or SHOULD in per-feature sidecars, which this record's grammar, ladder and manifest admit nowhere | — | 1 | amend; `layer-instruction` `[revised]` |
| `command-items-units` | R-B requires a unit for every item, but command items have no model to read one, so those units bear no load | — | 2 | amend; `layer-instruction` `[revised]` |
| `scope-selection` | R-B's scope tags and R-C's load-set selectors disagree: some namespaces load nowhere, and a unit naming no role reaches only the driver | 34 | 3 | amend; `layer-instruction` `[revised]` |
| `principle-check-switchable` | P27's enforcer can be switched to warn by `instructions.checks`, which foundations C6 forbids for a principle's check | — | 4 | fork, amend; `layer-instruction` `[revised]` |
| `layer-conformance-gate` | P28's enforcer, the layer contract's conformance gate, has no kind, factory or chain row behind it | — | 5 | amend; `layer-instruction` `[revised]` |
| `policy-level` | policy values sit at level 2 yet render inside the charter's level-0 envelope | — | 7 | amend; `layer-instruction` `[revised]` |
| `help-move-owner` | R-E sends explanation to `help/`, and no chain row owns the move | — | 9 | amend; `layer-instruction` `[revised]` |
| `node-registry-card` | the node registry leaves the loaded charter, but the card's node cell is derived from that very table | — | 12, 36 | amend; `layer-instruction` `[revised]` |
| `worktrees-placeholder` | "Worktrees: none yet" is the WORKTREE_SCRIPT placeholder, still true, and derive-at-render already exists | — | 22 | amend; `layer-instruction` `[revised]` |
| `instruction-paths` | the record never says which paths are instruction files, which Runtime's one-door invariant needs | — | 30 | amend; `layer-instruction` `[revised]` |
| `tag-lifecycle` | the write boundary checks no referential integrity on removal or rename, and tags have no lifecycle | — | 43 | amend; `layer-instruction` `[revised]` |
| `handed-content-grammar` | the grammar never says whether it applies to handed content, or how quoted text is fenced from directives | — | 47 | amend; `layer-instruction` `[revised]` |
| `instruction-command-seams` | R-I's new command names none of the render, check and overlay seams that already serve the same text | — | 25 | none; `layer-instruction` `[revised]` |

## [map-flow] The flow layer's findings, placed

Run A is `wf_1532dea2-2f7` and run B is `wf_782666f6-e98`.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `multi-actor-items` | five items name two actor kinds, against "one actor per item" and P24, and the only derived check still passes | 1 | 31 | pending |
| `self-typed-review-witnesses` | the breakpoint program's role items are proven by the acting agent's own typed output | 2 | — | pending |
| `exit-witness-all-items` | an exit witness made of every item's witness cannot pass when conditional items never run | 3 | — | pending |
| `breakpoint-placement` | each step places its review breakpoint differently, and nothing says where the flow resumes after `review.dispose` | 4 | 12 | pending |
| `autonomy-gates-missing` | the owner gates `autonomy` declares appear in no step's breakpoints, and Deploy's gate mixes an autonomy value with a preset name | 5, 53, 62 | 6, 26 | pending |
| `owner-gate-vs-question` | an owner breakpoint can be resolved by `run.on-owner-question`, since neither record separates an owner gate from an owner question | 6 | 37 | pending |
| `superseded-parent` | a superseded or paused parent has no dependent rule: `deploy.parents` and `deps.on-parent-withdrawn` cover landed and withdrawn only | 7, 41, 61 | 39 | pending |
| `parents-test-decides` | `deploy.parents` always holds, with no behaviour for `deps.landing: test-decides`, velocity's value | 48, 61 | — | pending |
| `withdraw-program-missing` | withdraw, supersede, pause and resume have no items or program, and work in flight when they arrive is unhandled | 8, 50, 60 | 38 | pending |
| `pause-leases` | pause says nothing of the paused build's leases, which the supervisor expires | — | 40 | pending |
| `review-findings-entry` | findings and reds sent back through Design have no `design.input` kind | 9 | 8 | pending |
| `landing-review-route` | the landing review's findings and a red after the push route to a new unit with no Deploy-to-Design transition | 10, 64 | 44 | pending |
| `deploy-close-reconcile` | `deploy.close` has four effects in one item, no order, and no idempotence or reconcile declaration | 47, 65 | 44 | pending |
| `red-routes-ignore-policy` | `test.attribute` routes ignore `verdict.blocks` and `verdict.red-route`, so under strict and guarded a build has no route out of Test | 11, 18, 30 | 2, 3, 14 | pending |
| `unreachable-items` | no route reaches `build.scope`, `build.recommend`, `test.recommend` or `review.cost`, several outcomes route nowhere, and no item declares its dependencies | 12, 66 | 4 | pending |
| `ask-acceptance` | core items file asks with no mechanical acceptance, which the memory layer's `asks.acceptance` refuses | 13 | — | pending |
| `first-unwitnessed-item` | "the first unwitnessed item" has no meaning once steps are dependency programs answering with a frontier | 14, 49 | — | pending |
| `scope-refusal-stuck` | a `build.scope` refusal leaves the stray commit, and the default route loops on the same history | — | 43 | pending |
| `maintain-superseded-text` | the body still says Maintain stays core, against [settled] | 15 | — | pending |
| `gap-13-14-unstated` | gap-flow-13 and gap-flow-14 are registered but stated nowhere in the record | 16 | 46 | pending |
| `bar-attribution-unjoined` | the tester types a red's class that the bar already computes mechanically, and the two are never joined | 17, 29 | — | pending |
| `lander-rewrites-merge` | Test and Deploy re-specify the landing merge, while the lander's `--prepare` mints versions and regenerates into it, so the graded tree is not the pushed one | 19, 59 | 20 | pending |
| `verdict-tree-build-tip` | `verdict.tree` allows build-tip, yet `test.merge` always merges and `deploy.current` requires equality | 20 | — | pending |
| `presets-fail-build-closes` | the policy check refuses `after-release-verifies` without integrations, yet strict and guarded set it, so both fail on a core install | 21, 38, 43 | 1, 25 | pending |
| `hook-actor-kind` | hook-witnessed items are labelled command actors, which Runtime runs rather than awaits, and the verdict's writer is the runner, not a hook | 22, 46 | 15 | pending |
| `ask-row-shape` | S-2 misstates today's ask row: status is folded from dispositions, and severity and acceptance are rare | 23 | 19 | pending |
| `lease-ref-history` | witnesses rest on a lease ref's history, but the ref is a parentless commit replaced at each swap and deleted at close | 24 | — | pending |
| `merge-read-as-additions` | the build's range checks read a conflict-resolution merge of the default branch as the build's own work | 25 | 18 | pending |
| `class-set-undefined` | `review.lens` needs a registered core class set that no record defines, while the existing gotchas catalogue is demoted to an expansion | 26, 37 | 24 | pending |
| `deployer-producing-role` | layer-flow names the deployer as Deploy's producing role, while flow-steps makes core Deploy roleless and signals-only | 27, 39 | 10, 26 | pending |
| `reasoning-item-count` | [uncovered] counts three driver-reasoning items where [audit] and the register count four | 27, 52 | 11 | pending |
| `audit-b-count` | return b's summary count differs from its findings section | 28 | — | pending |
| `design-audit-no-fold` | the review program cannot run the Design spec audit's rounds: nothing folds an unbuilt spec, and `review.dispose` loops by the closing review's key | 32 | 7, 28 | pending |
| `design-rounds-carrier` | S-1 mints round keys beside the existing `REVIEW_ROUNDS` carrier and its loop states, uncited | 31 | — | pending |
| `review-harness-seam` | the breakpoint program rebuilds tier2-review.js's pipeline as separate items and drops its uncertain verdict | 33 | 21 | pending |
| `owner-controls-exist` | gap-flow-10 says no pause, resume or withdraw command exists, though unattended ships `--hold`, `--resume` and `--abort` | 34 | 22 | pending |
| `write-set-seams` | `build.unit-lease` and `build.scope` re-specify the driver's write-set declaration and check | 35 | 27 | pending |
| `lander-seams` | `deploy.core` and `deploy.record` name none of the lander's post-merge bar and landing marker | 36 | — | pending |
| `tests-without-cadence-dup` | `tests.without-cadence` duplicates `tests.landing-levels` | 40 | — | pending |
| `tests-without-cadence-semantics` | `wait-for-expansion` is undefined without the expansion, and `run-at-landing` sets no time bound | — | 45 | pending |
| `gap-flow-10-owner` | the record keeps gap-flow-10 and the owner's controls with dDeclaredLoop, which RT-3 moved to dWellOiledMachine | 42, 67 | 9, 22, 46 | pending |
| `tag-policy-collision` | item tags `build.scope` and `design.reentry` are spelled like policy keys, which [settled] said would be kept apart | 44 | 5 | pending |
| `policy-lists-incomplete` | each step's policy list omits keys its own items read | 45 | 7 | pending |
| `unbounded-loops` | every route back is unbounded, and no non-converging loop becomes an owner item | 54 | 41 | pending |
| `intake-hook-crash` | `entry.intake` rests on a prompt-submit hook outside Runtime's surface, with no crash behaviour, and none is wired today | 55 | 34 | pending |
| `intake-owner-scope` | nothing says which sessions' prompts are the owner's intake, so an act session's prompt could become the mandate | 56 | 35 | pending |
| `intake-secrets` | verbatim intake has no secret scan, redaction or size cap, beside a scanner the tree already ships | 57 | 36 | pending |
| `lander-exit-classes` | `deploy.land` routes two outcomes where the lander has five exit classes, including landed ungated | 58 | — | pending |
| `owner-disposition-witness` | the owner's disposition is "hook-written", while unattended owner items are answered through the mailbox or a terminal | 63 | — | pending |
| `unverified-block-stuck` | under `review.unverified=block` nothing can unblock: no round is scheduled and the owner has no disposition | 63 | 42 | pending |
| `item-count-readers` | the new item population updates none of the records that assert the old counts | 68 | — | pending |
| `mailbox-prune-orphan` | moving Maintain to an expansion orphans pruning a closed build's mailbox ref | 69 | — | pending |
| `turnstile-not-queue` | the turnstile is a host-wide bar semaphore, not a landing queue, and the lander never takes it | — | 16 | pending |
| `reasoning-field-timing` | the recommendation's reasoning field sits in a return that does not exist on the common path, or predates the score | — | 17 | pending |
| `tier-preset-guarded` | [design] omits the guarded preset's `owed-above-tier` spec audit | — | 13 | pending |
| `flakes-quarantine-seam` | `test.flakes` mints a new record beside the bar's nondeterministic class and quarantine, which mean something else | — | 23 | pending |
| `placement-policy-routes` | `entry.place` fixes the scout as placer, leaving `placement`'s other two values, which strict and guarded set, with no route | — | 29 | pending |
| `disposition-set-gaps` | the closed disposition set maps only defer and duplicate: no item retires, refuses or selects an ask | — | 30 | pending |
| `deployer-expansion-mismatch` | release notes go to distribution while the deployer registers under integrations, breaking the expansion-role check | — | 32 | pending |
| `instruction-tag-examples` | the instruction layer's R-B still gives example tags that no defined item carries | — | 33 | pending |
| `recommendation-source-mismatch` | core Deploy hard-codes signals-only while `review.recommendation.source` defaults to reasoning, and `agent-judgment` has no actor | 51 | — | pending |

## [map-roles] The roles layer's findings, placed

Run A is `wf_478254d1-ce0` and run B is `wf_08c634a0-1b4`.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `matrix-keyword-derivation` | the "derived" matrix matches keywords anywhere in prose Actor cells, so items gain false actors and any cell naming a known word passes | 1, 13 | 3, 15 | pending |
| `matrix-prompt-writer` | "every core role acts in a core item" fails on the prompt writer, a core role that appears in no Actor cell | 2, 14, 35 | 2, 16, 35, 36, 50 | pending |
| `matrix-arms-unseen` | only the unmatched-actor arm is implemented or seen red, and only on a synthetic actor; the core-role and P28 arms exist in prose alone | 2, 12, 39 | 2, 36, 51 | pending |
| `sod-agent-id-check` | R3-C's agent-id separation check cannot fail, since every item spawns a fresh agent, and "never sees the reasoning" contradicts velocity's warm verifiers | 3, 36 | 7, 23, 53 | pending |
| `acceptance-unmeasurable` | R3-F's acceptance re-runs role_orientation.py, which has no answered-call measure, misses headless agents and has no parent-had for workflow spawns | 4, 16, 33 | 6, 18, 42, 49 | pending |
| `agent-file-hook` | R3-H's agent-file hook is a second entry outside Runtime's single dispatcher, and agent-scoped hooks were measured to fail open | 5, 17, 28, 32 | 9, 22, 31, 39 | pending |
| `agent-id-binding` | the work order and the answered-call hook bind by agent id, which headless acts lack and which Runtime replaced with task-sha | 6, 37, 44 | 9, 21, 33, 41 | pending |
| `cut-at-launch` | "fresh at the spawn" does not hold: Runtime cuts the work order at act launch, and the Workflow runtime has no shell to re-key at the agent's spawn | 7, 11, 41 | 12, 20, 34, 40 | pending |
| `method-call-figures` | the 805 method calls and their per-file counts disagree with the record's own instrument output, which counts file reads, not calls | 8, 15 | 5, 17 | pending |
| `recall-once-per-session` | "recall is re-verified once" no longer holds once attended sessions start fresh at every item boundary | 9 | — | pending |
| `gaps-count-stale` | [gaps] says eight gaps join the register, while gap-roles-18 joined later | 10 | — | pending |
| `answered-state-calls` | refusing state calls whose answer was handed blocks the call that would find a stale fact once the role's own commit moves HEAD | 11, 42 | 46 | pending |
| `answered-call-fail-open` | the answered-call rule is stated as enforced at the call, though it fails open below CLI 2.1.295, where Read is ungated | 4, 20 | 8, 25 | pending |
| `settled-rule-attribution` | [settled] credits the render refusal to R-A, R-B and R-E, where it is R-C | 21 | — | pending |
| `effort-carrier` | R3-A puts effort in the role definition, though effort lives in the adopter-owned house/policy.toml | 22 | 29, 38 | pending |
| `execution-shape-seams` | gap-roles-18's execution shape is mostly declared already: workflows.toml's agent sets, policy.toml's efforts, gotchas.py's checklist | 23 | 32 | pending |
| `metrics-extractor-seam` | role_orientation.py re-implements runlog's transcript extractor and its tool-call classifier | 24 | 27 | pending |
| `role-step-join-exists` | the role-to-stage relation is already joined both ways by check_roles R6 to R9 over workflows.toml | 25 | 26, 43 | pending |
| `rules-key-binding` | [tags] binds from the unit's side, while today each role's `rules:` key binds the other way and is checked | 26 | 30 | pending |
| `handoff-seam` | "handed, not referenced" is framed as new, though handoff.py's render already resolves each role's declared inputs into content | 27 | 28 | pending |
| `cycle-amendment` | [trust] amends [cycle] while flow-roles still says references, and R3-E reorders the cycle unannounced | 29 | — | pending |
| `protocol-pointer-machinery` | replacing protocol pointers with slices trips the roles kit's carried Protocols section and the rules and self-test that read it | 30, 47 | 37, 54 | pending |
| `body-ceiling` | the static block's growth crosses check_roles' existing per-role body ceilings, and R3-A adds a second carrier | 31 | 44 | pending |
| `keys-agent-typed` | "no agent types a key" sits beside returns that carry agent-typed keys onward | 34 | — | pending |
| `reverify-order-sources` | the re-verification orders are cited at rendered copies, not kit sources, and the inventory misses gov-session and the spec template | 38 | 45, 52 | pending |
| `claimed-fact-staleness` | re-cutting covers only facts a command can recompute, not judgments whose source moved | 40 | — | pending |
| `read-class-undefined` | the answered-call rule names "a read" without saying which tools count or how a partial overlap is treated | 43 | — | pending |
| `over-budget-route` | an item whose handed content exceeds its packet budget, or whose anchor vanished at re-cut, has no route | 45 | 48 | pending |
| `repair-lifecycle` | nothing says when a repair ends against a frozen record, or which of two concurrent repairs wins | 46 | 47 | pending |
| `repair-staleness` | a repaired fact keyed to an immutable return never goes stale, and a re-cut can hand the false original again | — | 10, 47 | pending |
| `p29-vs-p23` | P29 has roles act on claimed, agent-typed facts, which P23's source floor forbids, and neither scopes the other | — | 1, 24 | pending |
| `flow-roles-steps-stale` | flow-roles [steps] still stands as a second typed role-to-step table that contradicts the derived matrix | — | 4 | pending |
| `dboundroles-order` | dBoundRoles owns re-cutting at the spawn, while the executor that does it lands later in dWellOiledMachine | — | 11 | pending |
| `verifier-set-spelling` | the verifier set is the reviewer, skeptic and tester in one place and the reviewer and skeptic in F3-3 | — | 13 | pending |
| `cached-prefix-claim` | "the cached prefix serves every spawn after the first" has no criterion, and act sessions differ in cwd and time | — | 14 | pending |
| `blob-sha-crlf` | the hook's blob SHA is unspecified, and CRLF working copies never hash to the keyed blob | 19 | 19 | pending |
| `cli-version-measurement` | "no AGENTS.md block reaches a role" was measured only on CLI 2.1.295, while act sessions may launch 2.1.292 | 18 | — | pending |
| `roster-fold-item` | the spec writer's folds are in [roster], but no step declares a fold item | — | 16 | pending |
| `adopter-role-overlays` | declaring each role once in the kit leaves out the adopter-owned house overlays and effort policy | — | 38 | pending |

## [map-memory] The memory layer's findings, placed

Run A is `wf_b6756400-d03` and run B is `wf_ec731bfc-925`.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `stale-lexicon-owner` | the record still gives dTotalRecall the lexicon pin, gap-mem-10 and the lexicon handling (`--suggest` unchanged), which the lexicon review moved to dMindYourWords | 8, 20, 44 | 5, 37, 47, 58 | pending |
| `stale-gap-tool-03` | the record still gives gap-tool-03 to dDeclaredLoop, which the runtime layer moved to dWellOiledMachine | 8, 20, 44 | 5, 28, 37, 47 | pending |
| `stale-chain-count` | the record says the chain becomes twelve builds | 20, 44 | 5, 28, 37, 47, 58 | pending |
| `stale-map-tokenizers` | [map] still routes callers through the lexicon kit's tokenizers and lists no definition context, though the lexicon review made the map own extraction | 8, 34 | — | pending |
| `stale-runlog-unchanged` | [tools] keeps runlog unchanged, while the runtime layer moves the journal grammar into the core | 8, 28 | 28 | pending |
| `slug-date-text-stale` | [names] still calls F4-7 open and recommends a shown date after the owner chose none | 36 | — | pending |
| `record-idempotence` | `record` is specified only as an id-minting writer: nothing makes a replayed write idempotent or content-addressed, which the runtime layer's take-over reconcile relies on | 2, 47 | 2, 21, 49 | pending |
| `record-concurrent-mint` | nothing says what `record` does when writers on two clones or nodes mint at once | 47 | 49 | pending |
| `kind-list-incomplete` | the kind list omits kinds other layers write through `record` (return, act, lease, binding, mailbox, journal, run record, backlog, Flow's records), names instances where a class was meant, and gives no path to register a kind | 3, 28, 45, 61 | 15, 21, 32, 47, 50 | pending |
| `ref-homed-kinds` | the registry holds only kinds homed at a path, while the card, leases and the mailbox live on refs | — | 50 | pending |
| `generated-kinds-door` | the generated stores (symbols, callers, annotation index, recall index) are record kinds written by generators, a door beside `record` | — | 4 | pending |
| `scaffold-seams` | `record`'s minting, slug checks and template rendering re-specify `gen_build_index.py --new-build` and `--new-spec`, unnamed | 27 | 32 | pending |
| `runlog-schema-seam` | runlog's `RECORD_SCHEMA`, renderer and `check-records` leg already make the run record a schema-as-data kind, unnamed | 28 | 32 | pending |
| `hygiene-render-seam` | HYGIENE.md is already rendered from a template by `adopt-memory-tree.sh --render` under a `gov:kit` carrier, unnamed | 41 | 44 | pending |
| `hygiene-checks-not-schema` | many hygiene checks are history, size-cap and grandfather checks that no schema generates | — | 11 | pending |
| `check-numbers-stable` | generating the checks keeps no rule for today's check numbers, which comments, gotchas and guides cite | — | 45 | pending |
| `legacy-population` | the schemas, refusals and generated checks never say how they treat the records, asks and front-matter keys that predate them | 12, 49 | 11, 54 | pending |
| `frozen-refs-resolve` | every reference must resolve whatever its lifecycle, though append-only and frozen records legitimately name later-deleted paths | 48 | — | pending |
| `new-stores-concurrency` | the new committed views and row stores have no merge rule for parallel changes and join neither `SHARED_RECORDS` nor `GENERATED_INDEXES` | 60 | 42 | pending |
| `relation-target-unlanded` | nothing says where a relation's target is looked up when it sits on another node's unlanded branch | 60 | — | pending |
| `authority-keys-via-record` | the README schema names only derived keys, so the owner-authority keys the hooks read could be supplied through `record` | 39 | — | pending |
| `derived-keys-front-matter` | the record does not say whether derived keys stay in README front matter, which gen_build_index requires and 16 of 167 READMEs contradict | — | 46 | pending |
| `readme-root-vs-views` | [views] says agents never read a view, while [build] makes the generated README the orientation scout's root, and the `readme` value has no renderer path | 14 | 17, 18 | pending |
| `id-grammar-seam` | the id grammar is already single-sourced in memory-recall's `extract.grammar_for`, imported by memory-tree and drift-audit; [names] proposes a new export without naming or moving it | 29 | 31 | pending |
| `slug-re-carrier` | `BUILD_SLUG_RE` stays a second carrier of the slug grammar beside the `builds.slug-*` keys, its fate unstated | 29, 42 | 35 | pending |
| `flip-acceptance-unfailable` | "turn green, or be named" passes a reader that stays broken, over an enumerated population | 11 | — | pending |
| `flip-values-unnamed` | the grammar-flip proof names no values to flip to, though the breakage depends on the value | 51 | 53 | pending |
| `grammar-change-existing-ids` | nothing says whether a changed slug grammar applies to new mints only or to the existing slugs | 51 | — | pending |
| `slug-style-unenforceable` | `humorous` names no word source and cannot be told from `descriptive` mechanically | 13, 52 | 17 | pending |
| `v14-refusal-exists` | the refusal at filing already ships as backlog.py's V14 under `ASK_CUTOFF` (D12-d), so "only lowers a grade" and F4-6's "as today" are false and the design rebuilds it | — | 30 | pending |
| `ask-filer-coverage` | refusal at filing rests on four filer instances, while owner, surfaced, expansion and supervisor filers state no mechanical acceptance | 12, 50 | 1, 25, 51 | pending |
| `refused-ask-fate` | nothing says what happens to an ask refused at filing | — | 51 | pending |
| `decisions-layer-placement` | [contract] moves major decisions to core while [settled] and v2 [layers] keep decisions in Knowledge | 7 | — | pending |
| `decisions-readers-unnamed` | routing about 188 of 200 rows out of DECISIONS.md names none of its readers or the carriers that send readers there for "why" | 40 | 16, 40 | pending |
| `decisions-append-only` | moving rows out of an append-only index contradicts the rotation rulings, and the rotation seam is unnamed | 33 | — | pending |
| `decision-id-readers` | dossiers' `decisions = [...]`, `DOSSIER_DECISIONS_EMPTY_PIN`, gotchas' `decision:` and the recall bench hold decision ids by value | 33, 55 | 41 | pending |
| `kappa-below-threshold` | the migration counts at kappa 0.8 with no raters named and no disposition below it | 15 | 13, 57 | pending |
| `supersession-seam` | check 27's typed relations and memory-recall's supersession map already do supersession and holds-now, unnamed | 25 | 33 | pending |
| `amends-vs-frozen-spec` | `amends` revises a built unit's frozen spec against P19, and `@rev-N` is in no grammar | — | 8 | pending |
| `reuse-entry-two-doors` | a reuse entry is a record kind only `record` writes and an instruction unit only `instructions.edit` changes, homed in a sidecar neither door owns | 4, 21, 35, 46, 56 | 4, 43 | pending |
| `reuse-entry-proposal-path` | with agents only proposing instructions, the build that ships a feature cannot create the entry its own checks require | 1 | — | pending |
| `reuse-entry-level` | level 3 holds stage methods, not directives, while the entry is delivered at the card and the task | 5 | — | pending |
| `reuse-entry-should` | the entry's "MUST or SHOULD" strength fails the instruction grammar, which allows MUST, NEVER and ALWAYS | — | 3 | pending |
| `reuse-affordance-seam` | each dossier's gated `## Reuse affordance` block already holds the reuse record the sidecar re-creates | 24 | 29 | pending |
| `core-needs-knowledge` | core parts require Knowledge kinds against P28: the `implements <reuse-entry>` relation and the charter's `[records]` reuse-entry rule | 6 | 55 | pending |
| `reuse-field-seam` | the card's `reuse` slot is the existing task-card `**Reuse:**` field handoff.py renders, and the scout's turn from reader to producer is unstated | 6, 26 | 6 | pending |
| `reuse-slot-states` | an empty `reuse` slot cannot tell "no match" from "Knowledge absent, stale or failed" | 54 | 55 | pending |
| `house-index-evidence` | M1c's 16 of 24 came from a small curated digest with a sketch and a census, not the whole-store house index designed | 53 | 20 | pending |
| `reuse-benchmark-rerun` | no acceptance re-runs the reuse benchmark against the built house index | — | 14 | pending |
| `on-demand-no-mechanism` | `reuse.delivery=on-demand` rested on the retired lookup and now has no mechanism | 13, 18 | 17 | pending |
| `foundation-home` | a cross-feature entry's home is "FOUNDATION", a map-root file check 3 refuses | 43 | — | pending |
| `lookup-name-inventory` | the lookup retirement's reader inventory is short and unnamed: about 40 files, 17 documents and the scout's agent files cite the tool | 16, 17, 32, 38 | 38 | pending |
| `spec10-token` | hygiene check 12's §10 arm accepts the token `reuse_lookup` as reuse evidence, and the template and charter require running the tool | 17, 38 | 38, 48 | pending |
| `lookup-map-cli` | unattended finds the stale-dossier reader through `MAP_CLI`, set to reuse_lookup.py, so the retirement silently stops stale-dossier asking | 37 | 39 | pending |
| `reuse-probed-readers` | the `reuse-probed` DoD item and M5 read the lookup and recall logs, and the retirement silences them | 37 | 39, 48 | pending |
| `reuse-obligation-witness` | after the retirement nothing witnesses the reuse-first obligation | — | 19 | pending |
| `ratchets-seam` | shrink-only for `VERB_OFFENDER_PIN` is one drift-audit RATCHETS row, not a lexicon re-engineering | — | 36 | pending |
| `method-callers-floor` | "11 of 1,997" covers import-resolvable calls only: 21,588 method calls stay unresolved, so methods added as definitions get no callers | 19 | 22 | pending |
| `map-cost-untimed` | the 7.8 s is the rejected name-only probe, and the designed pipeline was never timed | 23 | 26 | pending |
| `callers-restale` | a tracked callers file under the freshness check restales on every commit, the reason the map omits fan-in | — | 10 | pending |
| `dossier-anchor-seam` | symbol anchoring ignores the gated `[claims]` table and `measure_dossier_staleness`, and the 28-of-31 figure is path ancestry | 31 | — | pending |
| `inventory-counts` | the record's counts of check files, legs and kits are miscounted | — | 27 | pending |
| `annotation-green-vacuous` | the annotation checks are justified by a first green run over an empty population, and none is seen red | 10, 30, 59 | 9, 24, 52 | pending |
| `dangling-ids-exist` | 35 cited ids resolve nowhere (fixtures, foreign families), drift-audit pins the signal at 2, and no exemption class is designed | — | 24, 34, 52 | pending |
| `resolve-check-seam` | drift-audit's `source_cited_ids_resolving_to_no_record` signal is the resolve check the design proposes as new | 30 | 34 | pending |
| `lexer-blind-spots` | the comment lexer picks profiles by suffix, so extensionless git hooks and docstrings go unseen | 22 | 23 | pending |
| `annotation-grammar-inputs` | the grammar is one example line: block extent, separators, per-language syntax, wrapped heads and literals are unstated | 58 | 56 | pending |
| `feature-anchor-cases` | no rule covers a `gov:feature` anchor that appears many times or sits in a file with no extractor pack | 57 | — | pending |
| `annotation-style-overturned` | the design overturns ANNOTATION-STYLE.md A1 and A2 and naming neither it nor the parity leg that pairs it with a template | — | 44 | pending |
| `follow-through-test` | the follow-through test has no threshold, sample or window, and cannot separate following a pointer from same-build work | — | 12 | pending |
| `pushed-at-read-no-hook` | `annotations.grammar=pushed-at-read` has no read hook in any chain row | 13 | — | pending |
| `gap-owner-order` | fixes designed into dTotalRecall serve gaps owned by builds that land first or have no edge to it | 9 | — | pending |
| `recall-boundroles-order` | dTotalRecall and dBoundRoles each need the other's deliverable, and neither is the other's parent | — | 7 | pending |

## [instrument] The scripts and their runs

`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared-instruments.md` holds:
- the args generator;
- each layer's round B args;
- the comparison script, with its map-tag change;
- the summary script;
- every output this record states;
- the runs that saw each script red.
