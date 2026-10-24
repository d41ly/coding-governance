**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34

# Spec brief — dDeclaredLoop, the thirty-four units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dDeclaredLoop/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dDeclaredLoop/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every entry of "Shared interfaces", and the scout record your units cite:
   `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md` (units 1-5, 7, 8, 10,
   13-16, 26), `-b.md` (6, 9, 11, 12, 17, 18, 23-25, 27-29) and `-c.md` (19-22, 30-34). Each holds a seam table row
   per clause, with path:line at `87be0d40`.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), `B/…-flow-steps.md` (`[transitions]`, the items and
checklists), `B/…-flow-roles.md`, `B/…-layer-flow.md`, `B/…-layer-runtime.md`, `B/…-flow-roles-adoption.md` (FA-1
to FA-7), `B/…-stall-and-loop.md` (P39, SL-1 to SL-8), `B/…-night-pass-two.md` (NT-1 to NT-10),
`B/…-research-scenarios-design.md`, `B/…-foundations.md`, `B/…-systems.md`, `B/…-memory-plan.md` (`[sites]`),
`B/…-whole-audit.md` (C2-F*), `B/…-final-questions.md` (FQ-3, P41) and the fork rungs in
`B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an instrument, v2, the
as-built view or the packet: the packet's Non-goals.

## Four parents are specced, not built

dGroundRules (the policy file `.governance/policy.toml`, its one reader, `budgets.*` and the minimal guard), dSafePassage
(the `[[upgrade]]` and `[[retired]]` step kind), dOrderedCharter (the kinds register, the typed build-folder record
factory, the tag grammar and namespace registry, the instruction overlay) and dFairHearing (the review harness, its
items and `review.trigger`/`review.dispose` rows) each landed their specs and are DEFERRED to their build runs. The
chain builds them before this build's build run. So every spec here cites the parent's landed spec by id and section,
or its frozen v2 clause, as the interface, and names the call it makes; the build run re-grounds against the landed
parent. Never spec a parent's mechanism, never add a copy of `read_policy_key`, and never invent a policy route: a
policy key this build owns is declared in the catalogue this build's guard reads and read through dGroundRules'
reader once it lands, with the catalogue default v2 states until then, and the spec says so in one line.

## Every spec, whatever its unit

- Path `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`; H1
  `# TOOL-dDeclaredLoop-<n> — <title>`, an EM DASH, never a colon.
- Status header `DRAFT`, `rev-1`, `2026-10-24`, `node d`, `Tier-2`, `base ed497191`, `streams tooling`, the `order`
  verb your roster row names, and `advances TOOL-dDeclaredLoop-35` (the build's own open ask; the build run's last
  unit closes it). Copy a landed sibling's line shape, e.g.
  `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-5.md` line 3.
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below). A unit carrying a clause in parts writes
  `part <k>/<n>` instead of `whole`, and every part of that clause is carried by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. The unattended kit's own self-test suites are waived for this build's
  landing (README rule 8): a criterion they would observe is amended citing that rule.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in "The units" are a scout's reading at `87be0d40`: verify each line number against source before
  citing it.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a choice the README's `may: PLAY-dClosedLoop-3` grant
  lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open question: a FACT-QUESTION names its probe
  and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md` from their kit templates,
  and `tools/workflows/*.js` from their `.template.js`: name the source as the edit and the render as its copy.
- A later build's surface named in your clause (dBoundRoles, dScopedBuild, dWellOiledMachine, dTotalRecall,
  dWitnessedBar, dIndexedDesign) is a stand-in or a join that build arms: spec the stand-in this build ships and name
  the hand-over, never the later build's mechanism (packet Non-goals, Later builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` shows (Serves, Departs
  from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with `<k>` = your
  unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and `author-recorded`
  (README). Do not commit it.
- Write nothing outside `memory/builds/dDeclaredLoop/spec/` and `memory/builds/dDeclaredLoop/build/`; temp files go
  under the scratch path your harness names.

### What the last two spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build will CREATE by its basename (`python position.py …`) and keep its full path in
  §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it inside a
  quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours (a later unit never hands off to an earlier one:
  the earlier unit reads whatever rows exist when it builds, and the later one's rows join as data). The edge list in
  "The units" is the one to declare; add an edge only when your spec truly reads or produces it, and say so in your
  return so the other writer adds the reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file) owes a `**Readers:**` clause naming every reader
  by path and by value (hygiene check 25), each found by `git grep` over the tree.
- **No link-shaped text**, `[x](y)`, anywhere outside a real link, backticks included (hygiene check 2).
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` after every writer returns.

## Shared interfaces — one spelling for every writer

Fixed so thirty-four specs by five writers agree on the interface axis (M2). A writer who finds one wrong says so in
its §8 as a fork and settles it there by the rungs; it never silently respells one. "Owned by" is the unit that
specs the interface; every other unit named reads it as written here.

- **I1 · the loop kit.** A new kit `tools/loop/` (walkthrough.md:119: the loop owns WHAT, roles WHO), its definition
  `tools/loop/loop.toml`, read only through `tools/loop/loop_lib.py`, with its own `kit.toml`, adopter and
  dossier. Owned by unit 1, which also moves the `stage` integer out of `tools/roles/workflows.toml` and re-points
  its seven readers (scout A row 1) in the same unit. Every unit that adds rows, a check or a module adds it under
  `tools/loop/`; the harness `stages` table in `handoff.py` stays in roles.
- **I2 · the tag forms.** `step.<stage>` for `plan`, `design`, `build`, `test`, `deploy`, and
  `step.adopter.<name>`; `item.<step>.<name>` (e.g. `item.build.unit-pass`), `item.<step>.adopter.<name>` and
  `item.adopter.<stage>.<name>`; `policy.<catalogue key>`; `command.<kit>.<verb>`; and unit 27's `scenario.<name>`
  and `scenario.adopter.<name>`. Grammar `seg := [a-z0-9][a-z0-9-]*`, no first segment a namespace word
  (dOrderedCharter-19 S4, systems.md:244-252). The rows go in dOrderedCharter-19's `tools/playbook/namespaces.toml`.
  Owned by unit 18 (`step`, `item`, `policy`, `command`), which settles the `command` form in its §8. Flow-steps'
  bare `plan.exit` is a display name; as a tag it is `item.plan.exit`. A packet node id `policy-key.<key>` is a
  carries.py node, never a tag.
- **I3 · build states.** Lowercase `planning`, `designing`, `building`, `testing`, `deploying`, `paused`, `parked`,
  and the terminals `landed`, `withdrawn`, `superseded`, `incomplete`, `deferred`, `retired`, `refused`, `merged`,
  `answered` (flow-steps.md:721-765). Unattended's UPPERCASE phases (`PHASES_CORE`, `unattended.sh:852`) are not
  states: unit 1 maps each phase and each roles stage integer onto a state or a step in a table in its §4. Owned by
  unit 13 (the tables); unit 15 owns the terminal set and unit 31 the `incomplete` and `parked` endings.
- **I4 · the position answer set.** `act`, `awaiting`, `blocked`, `terminal`, `stuck`, `invalid-input`,
  `stale-remote` (cl-0092). Owned by unit 7; unit 14 reads it.
- **I5 · witness classes.** `history`, `hook-record`, `remote-verdict`, and the refused class `actor`
  (walkthrough.md:45-46); today's `DOD_CORE` `machine`/`agent` (`unattended.sh:868`) maps onto them, `agent` to
  `actor` on a shrink-only list each of whose rows names the build that removes it, and an item with no declared
  class refuses instead of `checker_of`'s silent `machine` (`unattended.sh:1275`). Owned by unit 5; units 2, 9, 13
  and 17 read it.
- **I6 · claim verdicts.** `fresh`, `re-derived`, `evidence`, with a claim key over commit or tree, base, remote refs
  and age (orientation.md:184-201). Owned by unit 8; unit 7 prints every claim it used with its key and verdict.
- **I7 · commit trailers and their one reader.** Keys `Gov-Unit`, `Gov-Item`, `Gov-Act`, `Gov-Session`, `Pass:`,
  `Decided:`, plus `Gov-Transition: <from> -> <to>` (unit 3) and `Gov-Policy:` (unit 2), all registered with the
  `commit` kind. One reader, `tools/lib/commit_trailers.py`, offering the views `union` (subject ids with trailer ids,
  today's `routed_commits.py`), `replace` (the trailer replaces the subject, today's `read_attribution_tokens`) and
  `decided`, carried inline into each copy-installed kit as a canonical-copy block with a `PARITY_ROWS` row
  (`tools/lib/resolve-python.test.sh`). Owned by unit 23. The writers of `Gov-Unit`, `Gov-Item`, `Gov-Act` and
  `Gov-Session` are dWellOiledMachine's; this build writes only `Gov-Transition` and `Gov-Policy`.
- **I8 · the transition record.** Three channels, the set `transitions.record` selects from `trailer`, `log` and
  `micro-format`, never empty: the trailer is the source and a check holds each other channel to it. The log is the
  `transition` kind of dOrderedCharter-7's record factory (`tools/memory-tree/build_records.py`); the micro-format
  line is `transition — <slug> · <from> → <to> · <item tag> · <sha>` in the charter template's micro-format block.
  Its fields are `from`, `to`, `item`, `sha`, and `composition` (unit 26), `scenario` (unit 27) and the budget
  `draw` rows (unit 30). Owned by unit 3, which settles in §8 the factory's name grammar for a build-level record
  that names no unit. Modules and legs say `loop transition`, never bare `transition`: `transition_audit.py` and the
  commit-msg hook already use the word for a backlog-mode merge audit.
- **I9 · the closed disposition set.** One set in the loop definition: placement's `continue`, `amend`, `new`,
  `patch`, `repeat`, `unit`, `breakpoint`, `ask`, `none` (flow-steps.md:124), with Plan's `defer` and
  refuse-as-duplicate mapped into it (research-flow-items-a.md:151-153, F12). The review round's exit `fold|promote`
  (`REVIEW_DISPOSITIONS`, `unattended.sh:999`) and the per-finding report grammar (`class:`, `new:`, `gate:`,
  `none`, dFairHearing-8) are different vocabularies, and the spec says so. The owner's disposition record,
  `record-kind.disposition`, carries one value of the set. Owned by unit 16; units 13, 15, 19 and 31 read it.
- **I10 · policy reads.** Every key this build owns already has its catalogue row: dGroundRules-1 S3 writes one row
  of `tools/policy/catalogue.toml` per v2 `[policies]` row. A unit adds READERS through dGroundRules-2's
  `resolve(key)` and `python tools/policy/policy.py get <key>`, never a row and never a fourth shell parser beside
  `read_policy_key`. Loop bounds and deadlines carry dGroundRules-11's `direction = "raise-loosens"`.
- **I11 · the floor.** v2:1723-1728's four invariants as `floor.verdict-before-move`, `floor.record-changes`,
  `floor.guard-self`, `floor.no-actor-witness`, each on by default and switchable only under the guard. Owned by
  unit 2, which reads unit 3 (record-changes) and unit 5 (no-actor-witness).
- **I12 · the guard and its TTY proof.** Unit 2 wraps dGroundRules-6's minimal guard (`tools/policy/guard.py
  --staged`, `tools/policy/guarded-paths.txt`, the `.githooks/pre-commit` block) and declares the layer-register
  point `point.instructions.guard` dOrderedCharter-15 S4 waits for. dOrderedCharter-15's `instructions_edit.py` is
  the first guarded TTY write command and unit 2's policy command the second: unit 2 extracts their shared part into
  one factory at this second instance, never a copy, and settles its home in §8.
- **I13 · the change record.** dOrderedCharter's S12/S13 `change` kind, `<date>-build-<unit id>-change-<n>.md`, with
  `Mark` and `Successor`. Units 2, 24, 26 and 28 write or read it; none re-specs it.
- **I14 · the needs-graph helper.** One acyclicity function extracted by unit 12 from `derive_install_order`
  (`tools/govkit/govkit.py:911`) and `_scan_cycles` (`tools/memory-tree/backlog.py:1271`) into `tools/lib/`, with
  both callers re-pointed in the same unit and the inline-copy and `PARITY_ROWS` pattern of I7. Units 24, 27 and 33
  call it; unit 33 adds the counted-edge and reachability rules beside it.
- **I15 · the kinds register.** dOrderedCharter-7 S4's `[[kind]]` row in `tools/playbook/kinds.toml` and S6's
  `python tools/playbook/core.py new <kind> <name>`; dOrderedCharter-36's schema, fixed set and widening checks;
  dOrderedCharter-35's `compose_rows`. Units 6, 24, 25 and 27 add rows, never a second register.
- **I16 · the step gate class.** dSafePassage-10 S1's `[[class]]` row in `tools/govkit/surface-classes.toml`; units
  24 (item tags) and 25 (stage tags) add one each.
- **I17 · the composition revision.** dOrderedCharter-46 S1's landed overlay revision plus gov's pack revisions,
  pinned in the claim and on each step's transition record. Owned by unit 26; units 27, 28 and 33 read it.
- **I18 · the review loop bound.** `review.max-rounds` (v2:1255, default 3) replaces `RUNAWAY_CEILING` (8 today,
  `unattended.sh:774`); a round count equal to it is admitted. The round-state tokens `CONVERGED`,
  `NON-CONVERGENT`, `CEILING`, `BOUNDED`, `CONVERGING` keep the driver's test order (`unattended.sh:12607`), and
  dFairHearing-17's `deriveRoundState(priorCounts, count, roundLimit)` receives `review.max-rounds` as `roundLimit`.
  The run-state row `<ts> review · item <subject> · reason <...>` keeps its grammar (`unattended.sh:12632`). Owned by
  unit 21; units 20, 32 and 33 read it.
- **I19 · the budget draw.** `flow.rework-budget` `<base>+<per-unit>` (default `4+2`) and `flow.route-backs`; one
  budget per build on its transition record, each draw an appended row `draw · <cause> · <item> · <spent>/<total>`
  with `<cause>` from `route-back`, `fix-pass`, `review-round`, `re-dispatch`, `research`, `patch:<slug>`
  (flow-steps.md:40-42). Owned by unit 30; units 31, 32 and 33 read it.
- **I20 · endings.** `best-effort-ending`, `park-for-owner`, `close-incomplete`; `incomplete` a terminal and
  `parked` a hold left only by the owner's disposition record. Owned by unit 31, as rows of unit 13's build table.
- **I21 · the recommendation record.** `record-kind.recommendation` through the record factory, written by the items
  `item.<stage>.recommend` (the score) and `item.<stage>.reason` (the producing role's reasoning). Owned by unit 22;
  unit 19 holds `build.recommend`'s route at the gate on it.
- **I22 · the acceptance record.** `record-kind.acceptance`, the executor's re-run of a unit's acceptance; the
  executor itself is outside this build (v2:2014 `[owed]`), so unit 17 declares the record and the witness kinds and
  arms the stand-ins. Owned by unit 17.
- **I23 · breakpoint names.** `breakpoint`, `owner gate`, `owner item`, `spec audit`, `gate review`, `closing
  review`, `landing review` (flow-steps.md:527). Units 19 and 20.
- **I24 · stage claims.** A `stage` claim on every dossier fence, gate leg (a `stage` field on each
  `tools/gate-legs.json` row, the pattern of dOrderedCharter-7 S2's `enforces`), role (derived from its `workflow:`),
  workflow and hook, joined both ways through dOrderedCharter-19 S9's `compute_coverage`. Owned by unit 4.
- **I25 · upgrade steps.** dSafePassage-1's `[[upgrade]]` step kind. Unit 21's move of `REVIEW_ROUNDS` and
  `RUNAWAY_CEILING` into policy keys is the second conf-key-to-policy-key step after dSafePassage-1 S6: unit 21
  extracts the shared step at this second instance. The mapping is `REVIEW_ROUNDS=1` to `review.design.rounds =
  one`, and N>1 to `fixed-count` with `review.design.round-count = N`.
- **I26 · frontier and `next`.** The frontier is a loop-kit function, the unwitnessed items whose needs are
  witnessed; the `next` command is dWellOiledMachine's, and until it lands the stand-in is `unattended.sh --plan`'s
  `next:` line (`unattended.sh:6131`). Owned by unit 14.

## Owned nodes

| Node | Unit |
|---|---|
| `tag-namespace.step`, `tag-namespace.item`, `tag-namespace.policy`, `tag-namespace.command` | 18 |
| `record-kind.commit` | 23 |
| `record-kind.disposition` | 16 |
| `record-kind.acceptance` | 17 |
| `record-kind.transition`, `policy-key.transitions.record` | 3 |
| `policy-key.floor`, `policy-key.policy-file.guard`, `policy-key.policy-file.proof`, `policy-key.policy-file.on-missing-expansion` | 2 |
| `policy-key.deps.on-parent-withdrawn` | 15 |
| `tag-namespace.scenario`, `policy-key.flow.scenario-default`, `policy-key.flow.scenario-conflict` | 27 |
| `policy-key.flow.adapt` | 28 |
| `policy-key.review.follow-up`, `policy-key.review.design.rounds`, `policy-key.review.design.round-count`, `policy-key.review.max-rounds` | 21 |
| `policy-key.deviation.approval` | 34 |
| `policy-key.flow.rework-budget`, `policy-key.flow.route-backs` | 30 |
| `policy-key.flow.on-exhausted` | 31 |
| `item.review.trigger`, `item.review.dispose`, `item.review.fold`, `item.review.cost`, `policy-key.review.blocks`, `policy-key.review.unverified`, `policy-key.review.left-shift`, `policy-key.review.findings` | 20 |
| `item.plan.recommend`, `item.plan.reason`, `item.design.recommend`, `item.design.reason`, `item.build.recommend`, `item.test.recommend`, `item.test.reason`, `item.deploy.recommend`, `record-kind.recommendation`, `policy-key.review.recommendation`, `policy-key.review.recommendation.source` | 22 |
| `policy-key.review.breakpoints`, `policy-key.review.<stage>`, `policy-key.autonomy` | 19 |
| `policy-key.flow.wait-ceiling` | 33 |

Each node is one `**Carries:** node:<node>` line, one per line, in its unit's spec.

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one. A writer who finds an edge false removes it from its
own spec and says so in its return.

| Producer → consumers | Token |
|---|---|
| 18 → 1, 9 | `step.<stage>` · `item.<step>.<name>` |
| 1 → 4, 6, 12, 13 | `loop_lib.py` |
| 23 → 2, 3, 7 | `commit_trailers.py` |
| 16 → 13, 15, 19, 31 | `record-kind.disposition` |
| 5 → 2, 17 | `actor` |
| 12 → 9, 24, 33 | `needs` |
| 9 → 11, 17, 24 | `item.<step>.<name>` |
| 13 → 3, 10, 15, 24, 25, 31 | `loop.toml` transition rows |
| 3 → 2, 10, 26, 30 | `Gov-Transition` |
| 8 → 7 | claim key |
| 7 → 14, 28 | `position` |
| 24 → 6, 25, 29 | `kind.item` |
| 26 → 27 | composition revision |
| 27 → 28, 33 | `scenario` |
| 28 → 33 | `flow.adapt` |
| 21 → 20, 32 | `review.max-rounds` |
| 30 → 31, 32, 33 | `flow.rework-budget` |
| 32 → 20, 31 | `flow.route-backs` |
| 31 → 33 | `flow.on-exhausted` |
| 20 → 19 | `review.dispose` |
| 22 → 19 | `record-kind.recommendation` |

## The units

**Writer groups and build order.** The `order` value is the build order: the namespaces and the loop definition
before every row that uses them, the commit reader before the transition trailer, the transition tables before the
record that writes them, the record before the position engine that reads it, the kinds before the factories that
follow their pattern, the composition before the scenarios and adaptations that pin it, and the review bound, the
budget and the convergence routing before the review program, the gates and the termination check that read them.
The build harness (`tools/workflows/unattended-build.js`) splits the 34 orders into five writer groups of consecutive
orders and hands each writer its group; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 18 (1), 1 (2), 23 (3), 16 (4), 5 (5), 12 (6), 9 (7) |
| 2 | 17 (8), 11 (9), 13 (10), 24 (11), 15 (12), 3 (13), 10 (14) |
| 3 | 2 (15), 8 (16), 7 (17), 14 (18), 4 (19), 6 (20), 25 (21) |
| 4 | 29 (22), 26 (23), 27 (24), 28 (25), 21 (26), 34 (27), 30 (28) |
| 5 | 32 (29), 31 (30), 20 (31), 22 (32), 19 (33), 33 (34) |

Seven Tier-2 specs is a long pass: keep each spec to what its clause and its shared interfaces need, cite the scout
record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dDeclaredLoop-18** — Items 18. I2's four namespaces as `[[namespace]]` rows with their extractors, each
  joining the core's tag-shape check, every catalogue key's name among the `policy` namespace's tags, seen red on a
  planted key whose first segment is a namespace word and green over the catalogue; dOrderedCharter-10 S5 keeps these
  rows red until this unit lands them; `lexicon.py --tags` is dOrderedCharter-10 S6's hand-off.
- **TOOL-dDeclaredLoop-1** — Items 1 (gap-spine-01). I1: the loop kit and its definition keyed by the stage tags,
  the roles kit's stage table moved and its seven readers re-pointed in the same unit (scout A row 1 lists them, with
  `tools/check-wiring.sh` and the docs), never waiting for a live build's close; I3's phase-and-stage mapping table.
- **TOOL-dDeclaredLoop-23** — Items 23 (gap-spine-08, gap-spine-09). I7: the commit node and its kind, the `commit`
  native-id class (dOrderedCharter-28 S2 `[[native]]`), the trailer keys mapped to `serves`, `made-by` and `runs-in`
  through dOrderedCharter-28's `[[trailer]]` rows, one reader with both views, `routed_commits.py`,
  `read_attribution_tokens` and runlog's `read_git_range` re-pointed in one unit, AC2's arms and the commit check run
  on planted `Pass: none`, `Pass: <id>` and subject-id-with-`Pass: none` commits reading the same before and after.
- **TOOL-dDeclaredLoop-16** — Items 16 (gap-flow-13's two disposition sets). I9 and `record-kind.disposition`.
- **TOOL-dDeclaredLoop-5** — Items 5 (gap-spine-02). I5: the witness-class rule, each stage witness of a class, the
  actor class refused, today's actor witnesses on the shrink-only list.
- **TOOL-dDeclaredLoop-12** — Items 12 (gap-flow-13). Each step a program of items with declared needs, every item
  declared with tag, actor, inputs by layer, instruction scope (dOrderedCharter-11's load sets, S10's `scope`),
  allowance, return template, closed outcome set, computed witness and routes, the item audit's tables
  (`B/…-research-flow-items-a.md`, `-b.md`) as input; I14's helper.
- **TOOL-dDeclaredLoop-9** — Items 9 (gap-flow-13). Each step's items declared with one actor, inputs, allowance,
  return schema and witness, the role defaults read through `roles_lib.py`, never copied.
- **TOOL-dDeclaredLoop-17** — Items 17 (gap-flow-14). Witnesses computed rather than typed: acceptance re-run by the
  executor (I22's stand-in), a probe's commands re-run at its pinned SHA, red attribution (`GATE_ATTRIBUTE`,
  `inherited-red`) joined to the verdict; the attest door refusing a computed item.
- **TOOL-dDeclaredLoop-11** — Items 11. Every checklist item named by a semantic tag, its number only display order:
  `DOD_CORE`, `DIRECTIVES_CORE` and BUILD-METHOD's numbered checks mapped onto I2's item tags, a retired number's
  readers re-pointed in the same unit (layer-instruction.md:432-439).
- **TOOL-dDeclaredLoop-13** — Items 13 (gap-flow-15). One transition table per level, build, feature and unit, in the
  loop definition; the engine refusing any transition it lacks; each row naming its exit item by tag; a fixture
  witness standing in for each exit item whose build has not landed (`plan.exit` dRankedPlan, `design.exit`
  dIndexedDesign, `build.exit` dScopedBuild, `test.exit` dWitnessedBar, `deploy.close` dShippedRelease) until that
  build lands and arms it (C2-F8).
- **TOOL-dDeclaredLoop-24** — Items 24 (gap-flow-19). The `item` kind (I15) with its factory and schema, the
  composition checks the clause lists, each seen red on its planted case, item tags joined to dSafePassage's step
  gate (I16).
- **TOOL-dDeclaredLoop-15** — Items 15. The terminal states of the build table, `deps.on-parent-withdrawn`'s three
  values read at every item boundary; `withdrawn` posts and the mailbox are dPlacedRequest's and dWellOiledMachine's,
  so the parent's withdrawal is read through today's stand-in (an ABORTED parent `RUN.md`); `design.inventory` is
  dIndexedDesign's; each value seen red on a planted withdrawn parent read in Design.
- **TOOL-dDeclaredLoop-3** — Items 3. I8 and `transitions.record`, seen on a planted subset and red on an empty set.
- **TOOL-dDeclaredLoop-10** — Items 10. Backward transitions recorded like forward ones: unit 13's backward rows
  written through unit 3's record, no new mechanism (session-model.md:260, flow-steps.md:739-753).
- **TOOL-dDeclaredLoop-2** — Items 2. I11 and I12: the guard, the TTY CLI and the floor, each invariant switched by
  `floor` only under the guard; the guarded policy command admitting the one agent write `budgets.*` names on its four
  conditions (`tools/template-size-limits.txt:16-24`) argued in I13's change record, every other agent write refused
  as `policy-file.guard` says; `policy-file.on-missing-expansion` (v2:1268, gap-spine-07) refusing a value that
  selects an absent expansion; every seen-red and seen-green case of the clause.
- **TOOL-dDeclaredLoop-8** — Items 8 (gap-orient-05). I6: claims keyed and trusted by key and source; the card's
  cells (`derive_claims_line`, `manifest-check.sh:645`) and `--claims` carry keys.
- **TOOL-dDeclaredLoop-7** — Items 7 (gap-orient-03). The position engine (I4): each unit's step, the build's step,
  the next item and its interrupts derived from witnesses, items idempotent by witness and keyed by round or pass
  and input SHAs, the read set and each claim's key and verdict printed; `--plan` and `--status` re-pointed to it
  and the `NEXT_RUNGS` ladder retired with a `**Readers:**` clause.
- **TOOL-dDeclaredLoop-14** — Items 14. The default failure route: the refusal recorded and I26's frontier.
- **TOOL-dDeclaredLoop-4** — Items 4 (gap-spine-01). I24: stage claims and the coverage gate, a leg that reds an
  unclaimed part and a stage with no witness.
- **TOOL-dDeclaredLoop-6** — Items 6. The factories and conformance gates for commands, policy keys, presets,
  stages, hooks, roles and workflows, each a `[[kind]]` row (I15) with its `new` arm and gate; the gates that exist
  (`check_roles.py` R2, R6-R9; `check-hook-destinations.sh`) wrapped, not copied; a kind whose factory a later build
  lands (presets dKeptSession, command adapters dWellOiledMachine) on dOrderedCharter-7's shrink-only pending list.
- **TOOL-dDeclaredLoop-25** — Items 25 (gap-flow-19). A repository's own stages spliced between two adjacent gov
  stages by pinned splice rows (an overlay kind) of unit 13's build table, every seen-red and seen-green case of the
  clause.
- **TOOL-dDeclaredLoop-29** — Items 29. An item's `upstream` field, the commitment rows its return answers `used`,
  `bypassed` or `not-applicable` with a reason, the join computed at the return, a `bypassed` row a routed finding;
  `upstream` a new `reads` family (`roles_lib.py` `READ_KEYS`, `handoff.py`).
- **TOOL-dDeclaredLoop-26** — Items 26. I17: a build's composition pinned per step on its transition record, position
  derived from it inside the step, the move at the next step boundary with witnesses carried by the change records'
  successors (I13), seen on a planted rename under a build positioned on the renamed item.
- **TOOL-dDeclaredLoop-27** — Items 27 (gap-flow-20). The `scenario` kind and namespace, gov's five shipped
  scenarios, admission predicates, `flow.scenario-default` and `flow.scenario-conflict` with every value's arm,
  successor chains acyclic through I14.
- **TOOL-dDeclaredLoop-28** — Items 28 (gap-flow-21). A build's recorded changes under `flow.adapt`, the step-boundary
  comparison of witnessed path against pinned composition (unit 7), `verb_rescope`'s row grammar widened rather than
  a second record, each value's arm.
- **TOOL-dDeclaredLoop-21** — Items 21. I18 and I25: `review.follow-up`, `review.design.rounds` and
  `review.design.round-count`, `REVIEW_ROUNDS` and `RUNAWAY_CEILING` retired in this unit with a `**Readers:**`
  clause naming every reader by name and by value (scout C row 21 lists them, fixtures included), `unattended.sh` and
  `check-unattended.sh` re-pointed, check 19 re-pointed rather than dropped, the arm still red with `unattended.sh`
  deleted in a scratch clone.
- **TOOL-dDeclaredLoop-34** — Items 34. `deviation.approval` read by `check_approver`
  (`tools/memory-tree/deviation_join.py:705`) instead of the `--approval` flag, `owner-all` added, the editorial class
  taken from dOrderedCharter-33's `derive_change_mark`, the re-audit at the new revision, each value seen on its
  planted case and red on an approver below the risk.
- **TOOL-dDeclaredLoop-30** — Items 30 (gap-flow-23). I19, every seen-red and seen-green case of the clause.
- **TOOL-dDeclaredLoop-32** — Items 32. The convergence routing for every `until-*` and `while-*` value on unit 21's
  bound and unit 30's budget, blockers and highs counted, NON-CONVERGENT and CEILING findings promoted to units while
  budget remains and to asks after, never folded.
- **TOOL-dDeclaredLoop-31** — Items 31. I20: `flow.on-exhausted` and its three endings as transition rows, a
  best-effort choice to lap again refused, raising the budget the owner's alone.
- **TOOL-dDeclaredLoop-20** — Items 20. The breakpoint program's items `review.trigger`, `review.dispose`,
  `review.fold` and `review.cost`, with `review.blocks`, `review.unverified`, `review.left-shift` and
  `review.findings`, which `review.dispose` reads; dFairHearing-3 and -8's stand-ins re-pointed, never re-specced;
  BUILD-METHOD M4's batch-every-minor disposal reads `review.findings` (a departure from today's text, recorded).
- **TOOL-dDeclaredLoop-22** — Items 22 (gap-flow-12). I21: the stage-exit recommend and reason items, the score
  computed by a command and the reasoning returned by the step's producing role, `print_spec_audit_line`
  (`unattended.sh:7887`) re-pointed.
- **TOOL-dDeclaredLoop-19** — Items 19 (gap-flow-11). Breakpoints at any item boundary, reviews and owner gates one
  mechanism under `review.breakpoints`, `review.<stage>` and `autonomy`; `run.on-owner-question` is dBoundRoles' and
  `build.ratify` dScopedBuild's, each a stand-in with its hand-over; the README `spec-audit:` opt-in re-pointed to
  `review.<stage>`; seen red on a planted major fork with dScopedBuild unlanded that reaches no gate.
- **TOOL-dDeclaredLoop-33** — Items 33 (gap-flow-24). The static termination check over every composition at the push
  and at each step boundary, every rule and every planted case of the clause, each its own arm; `flow.wait-ceiling`
  the default deadline, and today's hard-coded waits (`CLAIM_WAIT_CEILING`, `tools/push-main.sh:303`) named.
