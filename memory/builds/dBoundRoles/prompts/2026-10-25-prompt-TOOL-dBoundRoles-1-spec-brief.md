**Serves:** research TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26

# Spec brief — dBoundRoles, the twenty-six units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dBoundRoles/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dBoundRoles/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every entry of "Shared interfaces", and the scout record your units cite:
   `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-a.md` (units 1, 2, 6, 14, 15,
   18, 19, 20, 26), `-b.md` (3, 4, 5, 10, 11, 12, 13, 17, 23, 24) and `-c.md` (7, 8, 9, 16, 21, 22, 25). Each holds a
   seam table row per clause, with path:line at `748b309f`, plus a shared-interfaces list this brief settles.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), the gap register `B/…-gap-register.md` (the packet's
Gaps cite each gap's line), `B/…-roles.md` (`[guard]`, `[trust]`, RL-1 to RL-8, the roster rows), `B/…-layer-roles.md`
(the static block, the work order, the `[roster]` table and its matrix arms), `B/…-flow-roles.md`,
`B/…-flow-roles-adoption.md` (FA-1 to FA-7 and its numbered items), `B/…-systems.md` (`[design-role-shapes]`, the
single carry), `B/…-research-roles-anatomy.md`, `-coverage.md`, `-interactions.md`, `-priorart.md`,
`B/…-research-role-shapes-a.md` and `-b.md`, `B/…-research-handoffs-design.md`, `B/…-research-orientation-trust.md`,
`B/…-research-scoutedseam-apply.md`, `B/…-layer-runtime.md`, `B/…-night-pass-two.md` (points 1, 2, 4 and 7; NT-8,
NT-10, NT-12, NT-21, NT-27), `B/…-stall-and-loop.md` (P39, item 7), `B/…-memory-plan.md` (`[sites]`, `[gates]`), and the
fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an instrument,
v2, the as-built view or the packet: the packet's Non-goals.

## Only dTrueNorth is built; every other parent is specced and DEFERRED

dGroundRules (the policy file `.governance/policy.toml`, its reader `resolve(key, repo, rev)` at TOOL-dGroundRules-2
S6 and its CLI `policy.py get <key> [--rev]` at S7, the JS mirror `readPolicy` at TOOL-dGroundRules-5 S5, the
catalogue `tools/policy/catalogue.toml` at TOOL-dGroundRules-1 S3, the guarded paths and `guard.py --staged` at
TOOL-dGroundRules-6 S1-S4, `runtime.agents-in-flight` and agent-cap's rule 7 at TOOL-dGroundRules-10),
dOrderedCharter (the kinds register `tools/playbook/kinds.toml` at PLAY-dOrderedCharter-7 S4, the record factory at
-7 S7, `TAG_RE` and `tools/playbook/namespaces.toml` at -19 S1/S2, the overlay units at -32 S1/S8, levels at -34 S2,
composition at -35 S1-S10 and widening at -36 S1-S7, the `answers` edge at -28 S1), dSafePassage (`[[upgrade]]` and
`[[retired]]` rows at TOOL-dSafePassage-1 S1-S3, the step gate's classes at -10), dFairHearing (the hook pack layout
at TOOL-dFairHearing-16 S4, agent-cap rules 0, 2 and 5 moved there), dDeclaredLoop (the loop kit, the item
declaration `resolve_item_declaration` at TOOL-dDeclaredLoop-9 S2, the item kind at -24, the refusal row at -14 S2,
the upstream block at -29 S5 and the `fork` establishes kind at -29 S3, the `ratification` mark at -19, `stage` moved
out of `workflows.toml` at -1 S4), dPlacedRequest (the orientation return block and `placement.py` at
TOOL-dPlacedRequest-4 S1-S5) and dWitnessedBar (`gov-tester` at TOOL-dWitnessedBar-23, the legacy ledger at -13 and
`seed` at -15 S4). None of that code exists at HEAD `4ed9e567`: cite the parent spec id and section a unit calls,
never re-spec it, and say in §8 that the build run re-grounds on it and stops the unit if the section is still
absent then.

## Every spec, whatever its unit

- Path `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-<n>.md`; H1
  `# TOOL-dBoundRoles-<n> — <title>`, an EM DASH, never a colon.
- Status header `OPEN`, `rev-1`, `2026-10-25`, `node d`, `Tier-2`, `base 4ed9e567`, `streams tooling`, the `order`
  verb your roster row names, and `advances TOOL-dBoundRoles-27` (the build's own open ask; the build run's last
  unit closes it). Copy a landed sibling's line shape, e.g.
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md` line 3, with `OPEN` for its status.
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below). A unit carrying a clause in parts writes
  `part <k>/<n>` instead of `whole`, and every part of that clause is carried by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `748b309f`: verify each line number against source before citing.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a choice the README's `may: PLAY-dClosedLoop-3` grant
  lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open question: a FACT-QUESTION names its probe
  and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` and `.claude/roles.json` from `tools/roles/`, `memory/guides/*.md` from
  their kit templates, and `tools/workflows/*.js` from their `.template.js`: name the source as the edit and the
  render as its copy.
- A later build's surface named in your clause (dShippedRelease's and dTendedCadence's deployer and maintainer
  definitions for unit 1, dConvergedCharter's seed retirement for units 16 and 21, dWellOiledMachine's session
  binding record for unit 3, dFurnishedOrders' remaining trust clauses for unit 13) is a stand-in or a join that build
  arms: spec the stand-in this build ships and name the hand-over, never the later build's mechanism (packet
  Non-goals, Later builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` shows (Serves, Departs
  from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with `<k>` = your
  unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and `author-recorded`
  (the README's deviation-values rule). Do not commit it.
- An ask your spec owes another build (a parent spec's row that disagrees with yours, say) is NOT filed by you: name
  it in your return and the main loop files it as a row in that build's `BACKLOG.md` (the README's writes rule).
- Write nothing outside `memory/builds/dBoundRoles/spec/` and `memory/builds/dBoundRoles/build/`; temp files go
  under the scratch path your harness names.

### What the earlier spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python policy.py get …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours (a later unit never hands off to an earlier one).
  The edge list in "Edges" is the one to declare; add an edge only when your spec truly reads or produces it, and say
  so in your return so the other writer adds the reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a hook) owes a `**Readers:**` clause naming
  every reader by path and by value (hygiene check 25), each found by `git grep` over the tree.
- **No link-shaped text**, `[x](y)`, anywhere outside a real link, backticks included (hygiene check 2).
- **A §8 mark's parenthesis is closed**: `RESOLVED (agent, 2026-10-25, delegated)`, provenance after the paren.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); the gate reads tracked files only, so run it in a throwaway clone
  under your scratch path with your specs committed there. A red it prints on your files is yours to fix. The main
  loop runs `check-spec-tokens.py` after every writer returns.

## Where HEAD or a parent differs from a clause — settle each in its unit, never silently

- **D1 · `item=` has no writer (unit 17).** PLAY-dOrderedCharter-28 (lines 94 and 109) hands "the marker's `item=`"
  to dDeclaredLoop, and no dDeclaredLoop spec writes it; v2's clause cl-dClosedLoop-0182 gives it to this build. Unit
  17 owns the marker field and names the disagreement in its return, so the main loop files an ask in
  dOrderedCharter's `BACKLOG.md`.
- **D2 · the house efforts (unit 16).** `tools/roles/house/policy.toml` seeds `gov-orienter` and `gov-builder` at
  `xhigh`; the clause sets the orientation scout at medium and the builder at high (RS-2). The clause decides; no
  deviation is owed for moving the seed.
- **D3 · `gov-session` stays (units 4, 18).** The night pass two's point 4 and NT-21 move `gov-session`'s retirement
  to Runtime (dWellOiledMachine). Unit 4 makes the prompt writer the task author, and unit 18 renames only the two
  reviewers; neither deletes `gov-session`.
- **D4 · agent-cap's rules (unit 25).** TOOL-dGroundRules-10 retires rules 1, 3 and 4 and adds rule 7 (settings at or
  under the agent limit); TOOL-dFairHearing-16 moves rules 0, 2 and 5. Rules 6 and 7 reach this build, and no spec
  names rule 7's home. Unit 25 moves both into the roles pack, so "once its last rule has moved" holds, and derives
  the rule set from `agent-cap.js` at the build run's base rather than from this list.
- **D5 · the field escape's cause is unknown (unit 8).** `research-orientation-determinism.md:56-60` records 34 typed
  gate runs, 9 denials, and a replay that exits 2, "cause not determined". Unit 8's first fork is a FACT-QUESTION whose
  probe is a replay of those runs' recorded tool inputs through `scratch-guard.js` at each run's commit, with the
  payload's real `agent_type`, `cwd` and `CLAUDE_PROJECT_DIR` (scout C's hypothesis: the arm landed at `3a40e7daf`
  before root resolution through `CLAUDE_PROJECT_DIR` at `791ee13e5`, so runs in that window armed nothing). Run the
  probe if a scratch clone allows it; the spec closes whichever exits the probe convicts, and each convicted cause
  is a planted payload in §6.
- **D6 · slot names.** Existing role stems stay as they are (`gov-orienter` is the orientation scout,
  `gov-researcher`, `gov-reuse-scout`, `gov-spec-writer`, `gov-builder`, `gov-skeptic`, `gov-synthesizer`), so no
  adopter rename is owed beyond the reviewers' merge (unit 18's clause). New stems are `gov-prompt-writer`,
  `gov-planner`, `gov-architect` and `gov-reviewer` (the merge of `gov-spec-reviewer` and `gov-diff-reviewer`, one
  reviewer with a lens per step, RL-1); the tester is `gov-tester`, TOOL-dWitnessedBar-23's.

## Shared interfaces — one spelling for every writer

Fixed so twenty-six specs by five writers agree on the interface axis (M2). A writer who finds one wrong says so in
its §8 as a fork and settles it there by the rungs; it never silently respells one. "Owned by" is the unit that specs
the interface; every other unit named reads it as written here.

- **I1 · the role definition fields.** Gov's role rows stay in each `tools/roles/agents/<slot>.agent.md` front
  matter, read only through `parse_front_matter` (`roles_lib.py`), and are described by a kind file
  `tools/roles/role-schema.toml` (`[kind] name = "role"`, mirroring TOOL-dDeclaredLoop-24's `item-schema.toml`). New
  keys, one spelling each: `layer` (unit 1), `acts-as` (`item` or `cycle`, unit 1), `never` (each entry
  `<limit> — <enforcer>`, the R13 `enforced-by` spelling, unit 2), `return` (the typed return template, unit 2),
  `budget` (the static block's ceiling, replacing `BODY_CEILINGS`, unit 15), `gates` (the gate grant, unit 21),
  `shapes` (the shape kinds a role runs in, unit 16). `FRONT_MATTER_KEYS` gains each key once. Owned by unit 2.
- **I2 · the tags.** `role.<slot>` (`role.gov-builder`), `role.adopter.<name>` for a repository's role;
  `field.<family>.<name>` for a `reads` key (`task:title` becomes `field.task.title`) and `field.stage.<key>` for a
  harness stage key; `workflow.<name>` and `workflow.adopter.<name>`. Rows in PLAY-dOrderedCharter-19 S2's
  `tools/playbook/namespaces.toml`, extractors beside TOOL-dDeclaredLoop-18's in its tag index. An item's actor stays
  `role:<slot>` (TOOL-dDeclaredLoop-24 S6). `role` and `field` owned by unit 14; `workflow` by unit 20.
- **I3 · the roster.** The twelve core roles and their slots per D6, plus `deployer` and `maintainer` registered as
  expansion roles through the distribution, integrations and observability layer contracts, with no definition file
  here. Owned by unit 1.
- **I4 · the role index `.claude/roles.json`.** Today's shape `{gates, harnesses, roles: {<slot>: {agent, gates,
  workflow, writes}}}`, written only by `render_roles_index` (`render_agents.py`) and read by `loadRoleIndex`
  (`scratch-guard.js`) and the spawn guard. Additions: per role `role-sha` (unit 6), `layer` (unit 1) and `shapes`
  (unit 16); top level `classes` (unit 9). Owned by unit 6.
- **I5 · the marker line.** `<!-- gov:handoff role=<slot> build=<slug> unit=<id|-> item=<item.step.name|-> path=<rel>
  role-sha=<12hex> task-sha=<12hex> -->`, `item=` optional in the regex for legacy lines, every reader moved to named
  groups. `MARKER_RE` (`roles_lib.py`) is the parser; the JS copy lives in whichever file holds the spawn guard
  (`agent-cap.js` until unit 25 moves it). Owned by unit 17.
- **I6 · role-sha.** One `derive_section_sha` in `roles_lib.py`, moved from `handoff.py`, hashing exactly the `## Role`
  section bytes; compared at spawn against the index's `role-sha`. Owned by unit 6.
- **I7 · the static block budget.** The bytes `render_agent_file` returns after the front matter, `## Charter`
  included; the ceiling is the role's `budget`; R5 is the one grader. Owned by unit 15.
- **I8 · policy reads.** Every key through TOOL-dGroundRules-2 S6's `resolve` or S7's `policy.py get <key> [--rev]`
  (Python, located through `roles_lib.resolve_kit_dir`) and TOOL-dGroundRules-5 S5's `readPolicy` (JS); a key's row
  goes in `tools/policy/catalogue.toml` through TOOL-dDeclaredLoop-6 S4's `new policy-key`. Harnesses take values as
  JSON args the way `efforts` travels today. No unit reads `.governance/policy.toml` with `tomllib` directly.
- **I9 · effort and model.** `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, `roles.effort.default`,
  `roles.model.<role>.<harness>`. A stage reads its stage key, then its role's key, then `roles.effort.default`,
  then the role's declared value, then the house file's `[effort]` while it stays a fallback. `default` is reserved
  as a role name. `EFFORT_LEVELS` (`roles_lib.py`) is the one level list; medium is the floor (unit 23). Owned by
  unit 21.
- **I10 · the workflow stage rows.** Each `[[workflow]]` entry in `tools/roles/workflows.toml` keeps its name and
  gains `kind` (`single`, `per-unit`, `panel`, `twin`, `experiment`; unit 16) and ordered `[[workflow.stages]]`
  tables, each with `key`, `role`, `fan`, `cap`, `effort`, `receives` and `returns` (unit 22); entry-level
  `checklist`, `orientation`, `merge` and `twin` (unit 16). The table stays `stages`, never `stage`, so it never trips
  TOOL-dDeclaredLoop-1's `stage` grep. A stage's `cap` is at or under `runtime.agents-in-flight` (TOOL-dGroundRules-10).
  The `{key: slot}` map `harness-args` prints is derived from the rows. Owned by unit 22.
- **I11 · the gate grant.** A role front-matter key `gates`, the list the index already carries per role, the
  trailing `?` optional marker kept; the house file's `[gates]` read only where a role sets none. Owned by unit 21.
- **I12 · the work order.** Rendered per item by `render_handoff` (`handoff.py`): the item (`item.<step>.<name>`,
  TOOL-dDeclaredLoop-9 S2), its inputs as content (I13), its `allowance` (a list of repo-relative path prefixes in the
  `ROUTED_PATHS` grammar), its return template (I1 `return`), its witness; hashed into the marker's task-sha and bound
  to its act by the session's binding record, which until dWellOiledMachine is the marker plus the card. Its record
  kind is `record-kind.work-order`. Owned by unit 3.
- **I13 · fact keys.** `blob:<path>@<blob12>:<lo>-<hi>`, `record:<id>@<sha12>`, `cmd:<argv12>:<out12>`, each with a
  class `witnessed`, `decided` or `claimed`, derived by one `derive_fact_key` in `roles_lib.py` and re-cut at act
  launch. Owned by unit 13.
- **I14 · `answers`.** A record return carries `**Answers:** <prompt path> task-sha=<12hex>` beside `**Serves:**`; a
  harness return carries a required schema field `answers` with the same value. Owned by unit 17.
- **I15 · the task frame.** Every block of a work order is added in `render_handoff`, in aScoutedSeam's skeleton
  order: the role and its job's kind, the material, the boundaries, the population, the upstream rows, the row
  contract, the added rows, the no-stop line, and the return contract last. Owned by unit 23.
- **I16 · the typed return channel.** Harness returns stay schema-forced (`UNIT_SCHEMA`, `FINDING_SCHEMA`); a
  direct spawn's return is checked against its role's `return` by one `validate_return` in `roles_lib.py`, called
  from a SubagentStop check; a residual failure is retried up to `roles.retries`. Owned by unit 5.
- **I17 · the refusal return.** `outcome: refused`, `rule`, `remedy`, `actor` one of `self`, `producer`, `driver`,
  `owner`, `build:<slug>`; the same fields extend TOOL-dDeclaredLoop-14 S2's `refusal` row rather than starting a
  second record. Owned by unit 26.
- **I18 · `run.on-owner-question`.** Values `best-effort-recorded`, `park-item`, `park-build`, `stop-run` (v2:1231),
  one reader; unit 26's "endings only once a build's budget is spent" is a branch of it. Owned by unit 11.
- **I19 · the fork record.** The §8 mark and record tail `options: <o1> > <o2> > … · pick: <oN> · admitted-by:
  <principle tag>`, graded beside `check_mark` (`check-memory-hygiene.sh`). Owned by unit 11.
- **I20 · the orientation return.** `disposition · reason · evidence · observations`, spelled exactly as
  TOOL-dPlacedRequest-4 S3/S4's block; unit 12 binds it to I16 and adds the driver step, never re-specs the grammar.
- **I21 · upgrade steps.** `[[upgrade]]` rows in a kit descriptor and `[[retired]]` rows in
  `tools/govkit/registry.toml` (TOOL-dSafePassage-1 S1/S2); step ids `roles/<verb-phrase>`, and agent-cap's
  `agent-cap/spawn-guard-to-roles-pack`; step-gate classes `role` and `workflow` beside dSafePassage-10's `agent`.
- **I22 · overlay rows.** `.governance/instructions.toml`: unit 19 writes level-5 `[[unit]]` rows selecting
  `role.<slot>` through `write_overlay_units` (PLAY-dOrderedCharter-32 S8); unit 20 writes `[[role]]` and
  `[[workflow]]` tables composed through `read_overlay_rows` and `compose_rows` (PLAY-dOrderedCharter-35 S1).
- **I23 · write classes.** `WRITES = none spec product review records` (`check_roles.py`) stays the vocabulary; the
  index's `classes` map is rendered from `WRITE_FOLDERS`, so the hook never carries a second path literal. Owned by
  unit 9.
- **I24 · the roles pack.** `tools/roles/spawn-guard.js` with `spawn-guard.fragment.json`, matcher `Workflow|Agent`,
  laid out like TOOL-dFairHearing-16 S4's pack file; admission compares a harness file's working-tree blob with its
  blob at the landed revision (`derive_landed_revision`, TOOL-dGroundRules-2 S1). Owned by unit 25.

## Owned nodes

| Node | Unit |
|---|---|
| `tag-namespace.role`, `tag-namespace.field` | 14 |
| `tag-namespace.workflow` | 20 |
| `record-kind.work-order` | 3 |
| `policy-key.roles.retries` | 5 |
| `policy-key.driver.reads`, `policy-key.prompts.author`, `policy-key.roles.no-spawn` | 10 |
| `policy-key.run.on-owner-question` | 11 |
| `policy-key.instructions.task-charter` | 15 |
| `system.role-shapes` | 16 |
| `policy-key.roles.effort.<role>`, `policy-key.roles.effort.<workflow>.<stage>`, `policy-key.roles.effort.default`, `policy-key.roles.model.<role>.<harness>` | 21 |

Each node is one `**Carries:** node:<node>` line, one per line, in its unit's spec.

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one. A writer who finds an edge false removes it from its
own spec and says so in its return.

| Producer → consumers | Token |
|---|---|
| 14 → 1, 20 | `role.<slot>` |
| 14 → 3, 22 | `field.<family>.<name>` |
| 2 → 1, 15, 21, 26, 20 | `role-schema.toml` |
| 1 → 4 | `gov-prompt-writer` |
| 1 → 18 | `gov-reviewer` |
| 21 → 22, 16 | `resolve_stage_efforts` |
| 21 → 23 | `roles.effort.default` |
| 22 → 16, 20 | `workflow.stages` |
| 16 → 20, 25 | `shapes` |
| 17 → 6, 3 | `item=` |
| 17 → 5 | `answers` |
| 6 → 25 | `role-sha` |
| 13 → 3, 24 | `derive_fact_key` |
| 3 → 7, 4 | `allowance` |
| 9 → 7 | `classes` |
| 5 → 12, 26 | `validate_return` |
| 10 → 4 | `prompts.author` |
| 23 → 24 | `render_handoff` |
| 11 → 26 | `run.on-owner-question` |

## The units

**Writer groups and build order.** The `order` value is the build order: the tags and the role schema before the
roster that fills them, the effort keys and stage rows before the shapes named over them, the marker grammar before
the index that hashes it and the work order that carries it, the write classes before the shell gate that classes
targets with them, the typed return before the roles whose returns it validates, the prompt writer's authorship key
before its frame and the frame before its anchor check, the forks' reader before the refusal branch over it, the
composition once gov's rows are stable, the overlay move and the reviewers' rename after it, and agent-cap's move
last, once every rule it carries has a home. The build harness (`tools/workflows/unattended-build.js`) splits the 26
orders into five writer groups of up to six consecutive orders and hands each writer its group; author every unit of
your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 14 (1), 2 (2), 1 (3), 21 (4), 22 (5), 16 (6) |
| 2 | 15 (7), 17 (8), 6 (9), 13 (10), 3 (11), 8 (12) |
| 3 | 9 (13), 7 (14), 5 (15), 10 (16), 4 (17), 23 (18) |
| 4 | 24 (19), 12 (20), 11 (21), 26 (22), 20 (23), 19 (24) |
| 5 | 18 (25), 25 (26) |

Six Tier-2 specs is a long pass: keep each spec to what its clause and its shared interfaces need, cite the scout
record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done. The gaps named
per unit are the packet's Gaps rows the unit closes, a reading the writer verifies.

- **TOOL-dBoundRoles-14** — Items 14. The `role` and `field` namespaces (I2): two rows in `namespaces.toml`, their
  extractors, and the join that widens the rule-tag binding (`check_rule_tags`) to `role.<slot>`; `READ_KEYS` stays
  the one vocabulary, emitted in both spellings during the migration, and the harness stage keys get `field.stage.`
  tags. Scout A row 14; TOOL-dDeclaredLoop-18 S1-S6 is the pattern to copy.
- **TOOL-dBoundRoles-2** — Items 2 (gap-roles-03, gap-roles-04). The static instructions as structured fields (I1):
  `role-schema.toml`, the `never` list with every limit paired to its enforcer (R13 widened from one `mandatory`
  line to every never-list line), the ceiling of tools, write classes and gate legs, and the typed `return`
  template; `render_agents.py` renders the fields. Scout A row 2.
- **TOOL-dBoundRoles-1** — Items 1 (gap-roles-01, gap-roles-02, gap-roles-07, gap-roles-14). The roster sorted by
  layer (I3, D6): `layer` and `acts-as` on every role, the new role files, the deployer and maintainer registered as
  expansion roles with no definition here, the reviewer's maintenance-run and loop lenses as expansion lenses, and the
  P28 matrix arm keeping core items to core roles (calling TOOL-dDeclaredLoop-24 S4's `check_item_composition`). Scout
  A row 1.
- **TOOL-dBoundRoles-21** — Items 21. The four key families and their resolution order (I9), `default` reserved, the
  gate grant a role field (I11), and every reader re-pointed in the same unit: `resolve_stage_efforts`, R12,
  `handoff.py`'s `stage-efforts` and `harness-args`, and the gate check, each seen red as the clause states. Scout C
  row 21.
- **TOOL-dBoundRoles-22** — Items 22. Workflow entries as data (I10): ordered stages naming role, fan, cap, effort
  and the rows received and returned, the five kinds kept as named defaults over them, a scenario's entries and role
  rows composed per build, seen on a planted two-stage entry of mixed roles and red on a stage cap above the limit.
  Scout C row 22; TOOL-dDeclaredLoop-6 S8's `new workflow` factory must learn the keys, an ask you name.
- **TOOL-dBoundRoles-16** — Items 16 (gap-roles-18). The shapes over unit 22's rows: `kind`, fan, checklist,
  orientation template, merge, twin rule and the agent cap bounded by `runtime.agents-in-flight`, the experiment
  kind's cases, variants, scorer or blind judge and re-runs taken from aScoutedSeam's benchmark (dFairHearing's), the
  orientation scout at medium and the builder at high (D2), and every registry reader rewritten in the same unit
  (`systems.md`'s consumer list). Scout C row 16.
- **TOOL-dBoundRoles-15** — Items 15 (gap-roles-19, gap-roles-20). The single carry (`render_handoff` stops appending
  the charter blocks where the backend loads the static block) read from `instructions.task-charter` and the harness
  kind, refusing `always` there; the budget measured over the whole rendered block (I7); both seen red as the clause
  states. Scout A row 15.
- **TOOL-dBoundRoles-17** — Items 17 (gap-roles-23). `item=` on every work order's marker (I5, D1), `answers` on every
  return (I14), and today's unmarked handoffs and returns seeded as a legacy population through `test.seed`
  (TOOL-dWitnessedBar-15 S4) so only new ones are refused, per the memory plan's `[sites]`. Scout B row 17.
- **TOOL-dBoundRoles-6** — Items 6 (gap-roles-06, gap-orient-07). The role index and agent files outside every role
  class (extending TOOL-dGroundRules-6's guarded paths), a tree with no index refused by both hooks instead of
  unarmed, and `role-sha` compared at spawn (I4, I6). Scout A row 6.
- **TOOL-dBoundRoles-13** — Items 13 (gap-roles-11, gap-orient-07). The trust mechanism's part this clause carries
  (P29): inputs handed as content, each fact keyed and classed (I13) and re-cut fresh at act launch; the brief and
  spec handed by path in `unattended-unit.js` become content. The rest of P29 is dFurnishedOrders'. Scout B row 13.
- **TOOL-dBoundRoles-3** — Items 3 (gap-roles-05, gap-roles-08). The work order rendered per item (I12), hashed into
  the spawn marker and bound to its act by task-sha and the session's binding record stand-in. Owns
  `record-kind.work-order`. Scout B row 3.
- **TOOL-dBoundRoles-8** — Items 8 (gap-orient-09). The field escape explained by the replay FACT-QUESTION (D5) and
  each convicted exit closed. Scout C row 8.
- **TOOL-dBoundRoles-9** — Items 9 (gap-orient-09). The `none` and `review` write classes enforced in the role arm
  (I23): `review` admits only the build's reviews folder, `none` refuses every repository write. Scout C row 9.
- **TOOL-dBoundRoles-7** — Items 7 (gap-roles-03). Shell writes held to the work order's `allowance`: a Bash and
  PowerShell check beside `checkRoleGate`, its scanner widened to the measured shapes (`sed -i`, an interpreter's
  write call, `git apply`), each target classed by unit 9's map. Scout C row 7.
- **TOOL-dBoundRoles-5** — Items 5 (gap-roles-04). Returns through a schema-forced channel on both routes (I16),
  residual failures retried by `roles.retries`. Scout B row 5.
- **TOOL-dBoundRoles-10** — Items 10. `driver.reads`, `prompts.author` and `roles.no-spawn`, each a policy key with
  its values (v2's `[policies]` rows) read through I8 and enforced where scout B names the seam; a value with no seam
  at HEAD is a stand-in naming its hand-over. Scout B row 10.
- **TOOL-dBoundRoles-4** — Items 4 (gap-roles-02, gap-roles-05). The prompt writer (`gov-prompt-writer`) composing
  every role's task from the driver's details, under `prompts.author`; `gov-session` stays (D3). Scout B row 4.
- **TOOL-dBoundRoles-23** — Items 23 (gap-roles-27). The default frame (I15), every list in the output bounded, work
  orders carrying the upstream rows (TOOL-dDeclaredLoop-29 S5) and returns answering them, and the effort floor:
  medium by default, below medium only by the owner's write to `.governance/policy.toml` under its guard and proof
  (TOOL-dGroundRules-6), each red and green case as the clause states. Scout B row 23.
- **TOOL-dBoundRoles-24** — Items 24 (gap-roles-28). The prompt writer's framing checked at render: every anchor it
  points at resolves to a fact key the work order hands (I13), seen red on a planted anchor to nothing. Scout B row 24.
- **TOOL-dBoundRoles-12** — Items 12. The orientation scout's return carrying the placement disposition and its
  reason (I20) through the typed channel, the driver recording it and running `placement.check` (TOOL-dPlacedRequest-4
  S1-S5). Scout B row 12.
- **TOOL-dBoundRoles-11** — Items 11. Every fork resolved by the role that meets it and recorded (I19), or held as
  `run.on-owner-question` says (I18), its options only those the core admits, ranked most feature-rich first and
  then most expandable, seen red on the two planted forks the clause names (LR-3). Scout B row 11.
- **TOOL-dBoundRoles-26** — Items 26 (gap-roles-31). The typed refusal return in every role's template (I17), the
  outcome table routing a remedy the refused actor cannot perform to that actor at once and never re-offering the
  item to the refused agent, and `run.on-owner-question`'s best effort choosing only among endings once a build's
  budget is spent, seen on a planted refusal of each actor kind. Scout A row 26.
- **TOOL-dBoundRoles-20** — Items 20 (gap-roles-24, gap-roles-25). A repository's roles and workflow entries in the
  `workflow` namespace beside gov's, `BODY_CEILINGS` a role field and `WORKFLOW_NAMES` the workflow registry, the
  actor patch, the fixed set and the widening directions, harness paths resolved in the install, and every seen-red
  case the clause lists, each as its own criterion. The longest clause: carry it whole or in parts across specs of
  this unit's id only if one spec cannot hold it under the size cap. Scout A row 20.
- **TOOL-dBoundRoles-19** — Items 19. The house text files moved into the overlay as level-5 units selecting their
  role (I22), with their own upgrade step (I21); `house/policy.toml` keeps the route the shapes give it. Scout A row 19.
- **TOOL-dBoundRoles-18** — Items 18. Its own upgrade steps (I21): an adopter's rendered agents renamed as
  `gov-spec-reviewer` and `gov-diff-reviewer` merge into `gov-reviewer`, the role index re-rendered, and every key the
  merge touches re-keyed (policy rows, house overlays, overlay `select`). Scout A row 18.
- **TOOL-dBoundRoles-25** — Items 25 (gap-roles-25, gap-roles-30). The spawn guard and harness admission moved into
  the roles pack (I24, D4), admission comparing a harness file with its landed blob, and `tools/hooks/agent-cap.js`
  retired with an upgrade step (I21) once its last rule has moved, its readers inventoried by value in a
  `**Readers:**` clause, the charter's agent-cap line among them. Scout C row 25.
