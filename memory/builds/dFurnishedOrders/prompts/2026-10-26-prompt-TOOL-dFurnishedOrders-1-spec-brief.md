**Serves:** research TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20

# Spec brief — dFurnishedOrders, the twenty units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dFurnishedOrders/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dFurnishedOrders/README.md`: its build-level rules bind every spec, the fork
   rule above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every entry of "Shared interfaces", and the scout record your units cite:
   `memory/builds/dFurnishedOrders/build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md` (units 1, 3, 5,
   6, 7, 13, 14), `-b.md` (4, 11, 12, 17, 18, 19, 20) and `-c.md` (2, 8, 9, 10, 15, 16). Each holds a seam table row
   per clause with path:line at `281c336e`, a shared-interfaces list this brief settles, and the disagreements
   between the clauses and the parent specs that "Where a parent differs" below settles.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), the gap register `B/…-gap-register.md` (the packet's
Gaps cite each gap's line), `B/…-roles.md`, `B/…-layer-roles.md` (`[trust]` items 1 to 10, `[matrix]`, R3-F's
metrics and `role_orientation.py` at lines 702-946 with its baseline at 988-1021), `B/…-flow-roles.md` (FR-10),
`B/…-flow-steps.md` (lines 543-547, the attended owner question), `B/…-orientation.md`, `B/…-systems.md`
(`[cross]`, the slot budgets and the slice keys), `B/…-project-map.md` (PM-1, PM-6, the delivery table at 616-632),
`B/…-retrofit.md` (the legacy slot's four states, 378-385), `B/…-compaction-results.md` (CX-2), `B/…-night-pass.md`
(points 1 to 4, NP-8, NP-9), `B/…-night-pass-two.md` (points 4 and 6, NT-10, NT-18, NT-24 to NT-26),
`B/…-research-handoffs-design.md`, `B/…-research-orientation-trust.md`, `B/…-layer-runtime.md` (RT-2, the hook
failure clause), and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You
never edit an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Only dTrueNorth and dGroundRules are built; every other parent is specced and DEFERRED

dGroundRules is built: the policy reader `resolve(key, repo, rev)` (`tools/policy/policy.py:752`), its CLI
`policy.py get <key> [--rev]`, the JS mirror `readPolicy` (`tools/policy/policy-mirror.js:132`), and a catalogue row
in `tools/policy/catalogue.toml` for every one of this build's fourteen keys, so no unit adds a catalogue row: each
reads its key and carries its `node:` line. Specced and DEFERRED, nothing built: dBoundRoles (the parent: the work
order TOOL-dBoundRoles-3, the fact keys -13, the typed return and `validate_return` and `roles.retries` -5, the
static fields and `role-schema.toml` -2, the roster and `layer` -1, the static block and `render_static_block` -15,
the frame `FRAME_SLOTS` -23, the marker's `item=` and `answers` -17, the prompt writer -4, forks and
`run.on-owner-question` -11, the refusal arm `[return.refusal]` -26, the stage rows -22, the roles pack -25),
dDeclaredLoop (the loop kit, items, `## Establishes` and upstream rows at TOOL-dDeclaredLoop-29 S3-S6, the budget
`record_draw` at -30 S3, the hook factory `new hook` at -6 S6), dPlacedRequest (item `map` and `unfolds` at
TOOL-dPlacedRequest-6, the item seed `resolve_item_seed` at -8 S4, `probe` on item outcomes at -7 S8, the problem
register at -12), dWitnessedBar (`gov-tester` at TOOL-dWitnessedBar-23, the legacy ledger at -13), dTotalRecall
(the memory read `--read` at TOOL-dTotalRecall-9 S8, the code record at -8, the project-map renderer `gov_map.py`
at -14), dOrderedCharter (load sets `derive_load_set` at PLAY-dOrderedCharter-11, the slot state line at -17 S9, the
tag bundle at -25), dSafePassage (`[[upgrade]]` rows at TOOL-dSafePassage-1) and KICK-dKeptSession-17
(`attendance`). dBoundRoles holds 59 spec files: ids 27 to 36 are asks, not units. Cite the parent spec id and
section a unit calls, never re-spec it, and say in §8 that the build run re-grounds on it and stops the unit if the
section is still absent then. dLinkedLibrary and dCalibratedLens have no specs: their surfaces are stand-ins only.

## Every spec, whatever its unit

- Path `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-<n>.md`; H1
  `# TOOL-dFurnishedOrders-<n> — <title>`, an EM DASH, never a colon.
- Status header `OPEN`, `rev-1`, `2026-10-26`, `node d`, `Tier-2`, `base 2193e25d`, `streams tooling`, the `order`
  verb your roster row names, and `advances TOOL-dFurnishedOrders-21` (the build's own open ask; the build run's
  last unit closes it). Copy the parent's line shape,
  `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md` line 3, with `OPEN` for its status.
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below), one per line.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 1, 4, 9, 13, 14, 20) still names its key words in backticks where they are code.
- Each clause's own "seen red on" and "seen on" cases are acceptance criteria, each observed RED on its planted case
  and green without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge
  bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in
  §7, and the main loop observes it at the close.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `281c336e`: verify each line number against source before citing.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5)
  and carries `widens:` and `relaxes:`, each a value or `none`; a choice the README's `may: PLAY-dClosedLoop-3`
  grant lifted (a governance-carrier or public-surface change the clause itself names) carries
  `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` and `.claude/roles.json` from `tools/roles/`, `memory/guides/*.md` and
  `memory/TEMPLATE-SPEC.md` from their kit templates, `.claude/skills/*/SKILL.md` from their `SKILL.template.md`,
  and `tools/workflows/*.js` from their `.template.js` where one exists: name the source as the edit and the render
  as its copy.
- A later build's surface named in your clause (dTotalRecall's section extractors, `record show`, renderer and
  `code` record; dLinkedLibrary's house index and `feature.*` selector; dCalibratedLens's value ledger) is a
  stand-in: spec what this build ships until it lands, rendering "not installed" where the clause says so, and
  name the hand-over, never the later build's mechanism (packet Non-goals, Later builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dFurnishedOrders/build/2026-10-26-build-TOOL-dFurnishedOrders-<n>-deviation-<k>.md`, in
  the grammar `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-101.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (the README's deviation-values rule). Do not commit it.
- An ask your spec owes another build (a parent spec's row that disagrees with yours) is NOT filed by you: name it
  in your return and the main loop files it as a row in that build's `BACKLOG.md` (the README's writes rule).
- Write nothing outside `memory/builds/dFurnishedOrders/spec/` and `memory/builds/dFurnishedOrders/build/`; temp
  files go under the scratch path your harness names.

### What the earlier spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist
  at HEAD. In §6 cite a file this build or a parent will CREATE by its basename and keep its full path in §2, §4 and
  Files touched. A command that reads a file takes it as an argument rather than spelling it inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec
  where it reads it, spelled exactly as "Shared interfaces" spells it.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a
  one-sided edge and an edge to a unit whose `order` is earlier than yours. The list in "Edges" is the one to
  declare; add an edge only when your spec truly reads or produces it, and say so in your return.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a flag, a hook, a Skill line) owes a
  `**Readers:**` clause naming every reader by path and by value (hygiene check 25), each found by `git grep`.
- **No link-shaped text**, `[x](y)`, anywhere outside a real link, backticks included (hygiene check 2).
- **A §8 mark's parenthesis is closed**: `RESOLVED (agent, 2026-10-26, delegated)`, provenance after the paren.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- **New names.** Every function, verb and key this brief proposes is a proposal: ask
  `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` before you write it, and if the lexicon refuses
  one, use its suggestion and say so in your return so the sibling that reads it follows.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits the
  hygiene gate and the lexicon, no other); the gate reads tracked files only, so run it in a throwaway clone under
  your scratch path with your specs committed there. A red it prints on your files is yours to fix. The main loop
  runs `check-spec-tokens.py` after every writer returns.

## Where a parent differs from a clause — settle each in its unit, never silently

- **D1 · the answered-call hook's owner (units 6, 14).** TOOL-dBoundRoles-13 §3 hands "the answered-call hook
  comparing a read with its handed key at the call" to dWellOiledMachine; clause 0197 and v2's chain row give it to
  this build, and v2:423 and :1965 send RC-7's lower-level design to dBoundRoles' units while clause 0205 says "in
  its own unit specs". The clauses decide: units 6 and 14 own the hook here, cite v2:1965-1969 as unit 14's
  question list, and name the disagreement in their returns for an ask in dBoundRoles' `BACKLOG.md`.
- **D2 · who renders the slots (units 4, 12).** PLAY-dOrderedCharter-17:72 says "dBoundRoles renders the slots" and
  TOOL-dTotalRecall-14:96 gives the `map` slot's delivery to dBoundRoles; clauses 0195 and 0203 give both to this
  build. The clauses decide; each unit names the disagreement in its return.
- **D3 · the bug-class lookup's retirement (unit 4).** "every call of the lookup by a write set's paths" retires the
  BUILD-side selections: the per-pass checklist (BUILD-METHOD M6, the unattended Skill's bullet, the verbs file's
  bullet, `unattended-unit.js`'s checklist), the default-off `prebuild`, and the build harness's `CHECKLIST` handed
  to units. The REVIEW-side readers stay (NT-25 keeps classes on review): the spec audit's `--for-paths` over Files
  touched, `tier2-review`'s checklist and its by-design block, M8's closing-review checklist over `<BASE>..HEAD`,
  kickoff's `--for-paths` over entrypoints, the charter line TOOL-dFairHearing-15 owns, and `MERGE-BAR.md`. Unit 4
  lists every one under `**Readers:**`, kept or retired, settles in §8 what `SPEC_COMMIT_CHECKLIST`'s fallback to
  `CHECKLIST` becomes and whether the universals ride the core field, and carries the build-method and Skill edits
  under `grants: PLAY-dClosedLoop-3`.
- **D4 · the memory-slice block (unit 11).** TOOL-dTotalRecall-9 S8 already puts `--read <key>` and a `reads:` list
  on `render_handoff`; unit 11's memory slices are that block rendered `not-installed` until S8 lands, never a
  second block.
- **D5 · a dropped, invented or doubled row (unit 19).** TOOL-dDeclaredLoop-29 S6 refuses them only on a `measured`
  edge and records a finding on a `record` edge; clause 0210 fails the return and retries it on every return. Unit
  19 settles it in §8 (the scout's reading: the schema failure holds on every edge, and only `bypassed` gates by
  measurement, night-pass-two.md:316-317), and a stricter rule than the parent's is a deviation record.
- **D6 · `instructions.slices`' owner and source (unit 8).** v2:442 names dBoundRoles; v2:1358, the catalogue and
  the packet's Owned nodes name this build, which decides. The protocol slices themselves are dConvergedCharter's
  (systems.md:422), a later build the packet does not name: unit 8 picks and declares a stand-in in §8 (the
  heading-bounded cut `extract_chunks` in `tools/memory-recall/extract.py`, reached by subprocess, or
  PLAY-dOrderedCharter-19's tag `show`), and names the hand-over.
- **D7 · runlog has no state, locate or method class (unit 10).** Clause 0201 takes "the other classes from
  runlog's extractor"; `derive_tool_class` (`tools/runlog/extract.py`) keeps only four facts of a call by contract
  and has no such class. Unit 10's first fork is a FACT-QUESTION over the real tree; re-homing
  `role_orientation.py`'s regexes as a second classifier is the rejected `metrics-extractor-seam`.
  `role_orientation.py` is not a file: it is code inside `B/…-layer-roles.md:702-946`, and its baseline counts are
  at :988-1021.
- **D8 · `probe` on two surfaces (unit 15).** `probe` on an item's outcomes is TOOL-dPlacedRequest-7 S8's; unit 15
  owns it on every role's return template, and joins the two: a role whose items carry `probe` returns it.
- **D9 · the late answer's budget cause (unit 16).** TOOL-dDeclaredLoop-30 S3's `record_draw` causes are a closed
  set with no late-answer cause; `route-back` with the item's tag needs no widening of a sibling's set, and a new
  cause does. Unit 16 settles it in §8.
- **D10 · an ask filed in a producer's family (unit 7).** A repair ask lands in the producer build's `BACKLOG.md`,
  which is the collision PLAY-dClosedLoop-32 records: unit 7 names how the id is minted so it cannot collide.

## Shared interfaces — one spelling for every writer

Fixed so twenty specs by five writers agree on the interface axis (M2). A writer who finds one wrong says so in its
§8 as a fork and settles it there by the rungs; it never silently respells one. "Owned by" is the unit that specs
the interface; every other unit named reads it as written here.

- **J1 · policy reads.** Python through `resolve(key, repo, rev)` (`policy.py`) or `policy.py get <key>`, located
  through `roles_lib.resolve_kit_dir`; JS through `readPolicy` (`policy-mirror.js`). Never `tomllib` on
  `.governance/policy.toml`. Each key spelled as its catalogue row spells it. Every unit; the parent's I8.
- **J2 · the trust field.** One row in `tools/roles/role-schema.toml` (TOOL-dBoundRoles-2 S1's shape): `verifies`,
  `none` or a list of input classes (`subject` among them); a role whose value is not `none` is a verifier. It
  renders as a `## Trust` block in the static block, after TOOL-dBoundRoles-2 S6's `## Return`, through
  `render_static_block` (TOOL-dBoundRoles-15 S1), never a second composer; `roles.trust` and
  `roles.verifier-context` decide what it says. Read by 6 (a verifier's read of its subject is never answered), 15
  (the tester is a verifier, layer-roles.md:288-289) and 8 (the re-verification orders it replaces). Owned by 5.
- **J3 · the return arms.** `[return.<arm>]` tables in `role-schema.toml`, composed into every role's template by
  one `compose_return_arms`, extracted from TOOL-dBoundRoles-26's `[return.refusal]` at its second instance,
  `[return.probe]`. Units 7 (`[return.repair]`) and 19 (the established rows) add through it. Owned by 15.
- **J4 · the optional slot.** One renderer `render_slot(point, state, body)` in `tools/roles/roles_lib.py`, writing
  PLAY-dOrderedCharter-17 S9's state line `slot <point> · filled|searched-empty|not-installed: <fallback>`, and one
  block head per slot inside the work order's `## Task`: `### memory`, `### code-notes`, `### legacy`,
  `### house-index`, `### map`, `### code`, `### problems`, `### bug-classes`. Unit 11's legacy slot adds the fourth
  state `not-seeded` in the same grammar. Read by 11, 12, 17, 18 and 20. Owned by 4.
- **J5 · the bug classes as a core field.** A spec section naming its bug classes by their record names (the
  `name` front-matter key of `memory/gotchas/*.md`), read by `gotchas.py --for-names <name>…` and rendered into
  `### bug-classes`. Owned by 4.
- **J6 · the stale mark.** One optional attribute on TOOL-dBoundRoles-13's fact line,
  ` stale=<source path>@<blob12>`, the source that moved (layer-roles.md:260-262). Read by 7 and 14. Owned by 1.
- **J7 · the orientation scout.** The slot stays `gov-orienter` (every parent spec spells it so; roles.md:394's
  `gov-orientation-scout` is not adopted), now spawned in a sidechain at session start. Read by 13. Owned by 1.
- **J8 · the card's map cell.** `map — <level-0 map and the build's neighbourhood>` under the card cap, and
  `map — not installed: <why>` until TOOL-dTotalRecall-14's renderer lands, the cell form `render_card` already
  uses. Owned by 13.
- **J9 · the notice record.** A runlog event kind `notice` in `KINDS` (`tools/runlog/extract.py`), class `security`
  or `failure`, persisted on the return's agent-ledger line (`write_agent_ledger`, `handoff.py`) as
  `notices.record` says. Read by 10. Owned by 3.
- **J10 · the repair arm and its ask.** `[return.repair]`: `repair: handed=<key> · found=<one line> · read=<key>`
  (layer-roles.md:292-293); under `roles.on-contradiction = return` the outcome word is `contradicted`; the ask is
  one row rendered by `render_ask_row` (`tools/memory-tree/backlog.py`) in the producer's `BACKLOG.md`, filed
  through one driver door. Read by 14 (a repaired fact handed while its ask is open). Owned by 7.
- **J11 · the answered-range matcher.** `match_answered_range` in `tools/roles/roles_lib.py` with its JavaScript
  copy, deciding whether a call is answered by a handed range at the same blob; the excerpt key extends
  TOOL-dBoundRoles-13's `blob:<path>@<blob12>:<lo>-<hi>` and never respells it; the shell readers are one table,
  `SHELL_READERS`, beside `scanCommandHeads` (`tools/hooks/scratch-guard.js`), shared with TOOL-dBoundRoles-7's
  write scan. Read by 6. Owned by 14.
- **J12 · the answered-call hook and its record.** `tools/roles/answered-calls.js` with
  `answered-calls.fragment.json` (the pack layout of TOOL-dBoundRoles-25 S2), writing
  `<git common dir>/answered-calls/<session_id>.jsonl`, one JSON line per decision with `utc`, `agent_id`, `role`,
  `item`, `tool`, `verdict` (`refused`, `warned`, `recorded`, `hook-failed`) and `anchor`; one reader
  `read_answered_calls` in `roles_lib.py`. The CLI threshold literal is `2.1.295`, the session's version read by the
  `AI_AGENT` rule `manifest-check.sh` uses. Read by 10. Owned by 6.
- **J13 · the role-by-step matrix.** `derive_role_matrix` beside TOOL-dBoundRoles-1 S7's `check_item_roles`
  (`tools/loop/loop_items.py`), rows from the item declarations and the role index, joined both ways (arm 2, every
  core role acts in a core item, is the one no parent carries). Read by 10 and 2. Owned by 9.
- **J14 · the role metrics file.** `role-metrics.tsv`, one row per `role · item · task-sha · class · count`,
  written at `handoff.py agents --write`; its directory is unit 10's §8 fork (a tracked path under the memory tree
  owes hygiene's record grammar). Owned by 10.
- **J15 · the slot budgets.** One key and one answer per slot (systems.md `[cross]`): memory by
  `memory.item-budget` (dTotalRecall's), code notes 2 KB, legacy by `retrofit.slot-bytes`, code by
  `memory.code-budget`, map by the card cap. The house index is handed first, as a pointer or not at all, as
  `roles.orientation.house-index` says. Owned by 11.
- **J16 · the role sets.** `derive_role_set(value)` in `roles_lib.py` over `structural-roles`, `every-role`,
  `working-roles` and `owner-only`, read off TOOL-dBoundRoles-1's `layer`; the working roles are v2:1366's list,
  the structural roles project-map.md:400's. Read by 17. Owned by 12.
- **J17 · the item seed.** TOOL-dPlacedRequest-8 S4's `resolve_item_seed` and its `unarmed — <source>: <why>`
  line; `unarmed` renders the slot `not-installed`. Read by 17 and 20; a parent interface, owned by neither.
- **J18 · rows.** TOOL-dDeclaredLoop-29 S3's `## Establishes` grammar, `- <row id> · <kind> · <text>`, kinds
  `seam criterion interface fork finding repair`, and `<item>#<row id>`; the return schema rendered per work order
  by `render_return_schema`, each row id an allowed value and each required once. A problem is handed as a
  `finding` row with the id `problem#<problem id>` (TOOL-dPlacedRequest-12 S3's id). Owned by 19.
- **J19 · `instructions.slices`.** Values `handed` and `pointer`, read where a role's protocol pointer renders;
  slices travel inside `render_static_block`'s one block. Read by 18. Owned by 8.
- **J20 · the problem reader.** A `--problems-for <item>` read in the driver beside `--register`, listing the
  register the way `read_claims` (`tools/unattended/unattended.sh`) lists a ref namespace, intersecting each
  problem's subject with the item's seed, path subjects through `check_writes_intersect`
  (`tools/memory-tree/design_lib.py`), reached by subprocess. Owned by 20.
- **J21 · upgrade steps.** `[[upgrade]]` rows in a kit descriptor (TOOL-dSafePassage-1 S1), step ids
  `<kit>/<verb-phrase>`; unit 4's are `unattended/retire-pass-checklist` and `workflows/retire-prebuild`.
- **J22 · attended.** `resolve_owner_question(kind, attended, repo, rev)` (TOOL-dBoundRoles-11 S5) is the one
  reader; `attended` derived at one site from `attendance` (KICK-dKeptSession-17) and a live owner turn. Owned by 16.

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.prompts.batch` | 2 |
| `policy-key.notices.record` | 3 |
| `policy-key.roles.trust`, `policy-key.roles.verifier-context` | 5 |
| `policy-key.roles.answered-calls` | 6 |
| `policy-key.roles.on-contradiction` | 7 |
| `policy-key.instructions.slices` | 8 |
| `policy-key.retrofit.slot-bytes`, `policy-key.roles.orientation.house-index` | 11 |
| `policy-key.memory.project-map`, `policy-key.memory.map-unfold` | 12 |
| `policy-key.memory.code-budget`, `policy-key.memory.code-roles` | 17 |
| `policy-key.annotations.delivery` | 18 |

Each node is one `**Carries:** node:<node>` line, one per line, in its unit's spec.

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 8 → 18 | `instructions.slices` |
| 5 → 15, 6 | `verifies` |
| 15 → 19, 7 | `compose_return_arms` |
| 15 → 9 | `gov-tester` |
| 4 → 11, 12, 17, 20, 18 | `render_slot` |
| 1 → 13 | `gov-orienter` |
| 1 → 7, 14 | `stale=` |
| 3 → 10 | `notice` |
| 19 → 7, 20 | `render_return_schema` |
| 7 → 14 | `repair:` |
| 14 → 6 | `match_answered_range` |
| 6 → 10 | `read_answered_calls` |
| 9 → 10, 2 | `derive_role_matrix` |
| 11 → 18 | `### code-notes` |
| 12 → 17 | `derive_role_set` |

## The units

**Writer groups and build order.** The `order` value is the build order: the rendered slices first, so every later
role renders once against the final static block; the trust field, then the tester and the return-arm factory over
it; the slot renderer before every slot; the orientation scout and its card cell; notices; the row schema before the
repair arm that declares rows through it; the repair before the matcher that carries it, and the matcher before the
hook; the matrix and the metrics over the hook's records; then the slots in budget order (memory, map, code), the
problems over the rows and the seed, the instruction selection over the slices and the code-notes slot, the batch
over the matrix, and the owner question last. The build harness (`tools/workflows/unattended-build.js`) splits the
20 orders into five writer groups of four consecutive orders and hands each writer its group; author every unit of
your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 8 (1), 5 (2), 15 (3), 4 (4) |
| 2 | 1 (5), 13 (6), 3 (7), 19 (8) |
| 3 | 7 (9), 14 (10), 6 (11), 9 (12) |
| 4 | 10 (13), 11 (14), 12 (15), 17 (16) |
| 5 | 20 (17), 18 (18), 2 (19), 16 (20) |

Four Tier-2 specs is a long pass: cite the scout record's seam rows rather than re-deriving them, and write each
spec to disk as soon as it is done. The gaps named per unit are the packet's Gaps rows the unit closes, a reading
the writer verifies.

- **TOOL-dFurnishedOrders-8** — Items 8 (gap-roles-12, and gap-roles-10's re-verification orders with unit 5). The
  role files' re-verification orders (`gov-spec-writer.agent.md`, `gov-researcher.agent.md`, `gov-session.agent.md`,
  `gov-builder.agent.md`, and `memory/TEMPLATE-SPEC.md`'s order through its kit template) and the Protocols pointers
  replaced by rendered slices, handed whole or as a pointer as `instructions.slices` says (J19), with
  `roles_lib.CARRIED_SECTIONS`, `check_roles.py`'s R0, R5 and R10 and `render_agents.py`'s self-test arm 4
  re-pointed in the same unit; the slice source per D6; readers by value. Scout C row 8.
- **TOOL-dFurnishedOrders-5** — Items 5 (gap-roles-10, gap-roles-16). Each role's trust profile and context
  temperature declared and rendered (J2): `roles.trust` (`keyed`, `witnessed-only`) and `roles.verifier-context`
  (`cold`, `warm`), every verifier's packet held to what the key allows in `tier2-review`'s verifier stage. Scout A
  row 5.
- **TOOL-dFurnishedOrders-15** — Items 15 (gap-roles-21). The tester agent re-founded from TOOL-dWitnessedBar-23's
  minimal `gov-tester` (WK-1), its allowance (scratch, and the browser where the harness has it, a capability row
  whose table is dWellOiledMachine's, so a stand-in), and the `probe` outcome on every role's return template
  through `compose_return_arms` (J3, D8). Scout C row 15.
- **TOOL-dFurnishedOrders-4** — Items 4 (gap-mem-44). The optional slots in their three states (J4), the bug
  classes as a core field (J5), and the write-set selections retired with their readers inventoried by value and
  their upgrade steps (D3, J21). The build-method and Skill edits are named by the clause: `grants:
  PLAY-dClosedLoop-3`. Scout B row 4.
- **TOOL-dFurnishedOrders-1** — Items 1 (gap-orient-15). The orientation scout composing the card in a sidechain at
  session start (J7), recall re-verified once at entry, a recalled record whose source moved handed as stale (J6),
  reusing `measure_dossier_staleness`'s rule, seen on a planted stale recall. Scout A row 1.
- **TOOL-dFurnishedOrders-13** — Items 13. The orientation scout composing the card's map cell (J8), `not installed`
  until TOOL-dTotalRecall-14 lands. Scout A row 13.
- **TOOL-dFurnishedOrders-3** — Items 3 (gap-roles-09). A return's harness notices persisted with it (J9), by
  `notices.record` (`none`, `security-and-failures`, `all`). Scout A row 3.
- **TOOL-dFurnishedOrders-19** — Items 19 (gap-roles-29). Every role return declaring the rows it establishes, the
  next work orders handing them on as upstream rows, and each work order's return schema rendered from its own rows
  (J18, D5), a dropped, invented or doubled row failing the return and retried as `roles.retries` says, seen red on
  a planted return of each kind. Scout B row 19.
- **TOOL-dFurnishedOrders-7** — Items 7 (gap-roles-17). Repairs recorded in returns and filed as asks against the
  producer's record (J10, D10), `roles.on-contradiction` (`repair-and-record`, `return`, `ask`), modelled on
  TOOL-dBoundRoles-26's refusal route rather than a second route table. Scout A row 7.
- **TOOL-dFurnishedOrders-14** — Items 14. The answered-call hook's range matching, the excerpt keys and a repair's
  carry, designed here (RC-7, D1), its questions v2:1965-1969 (J11). Scout A row 14.
- **TOOL-dFurnishedOrders-6** — Items 6 (gap-roles-13). The answered-call hook (J12, D1): `roles.answered-calls`
  (`refuse`, `warn`, `record`), a verifier's read of its subject and a read the packet does not cover never an
  answered call, and below CLI 2.1.295 each hook failure recorded, seen allowed on a planted verifier read of its
  subject and recorded on a planted hook crash. Scout A row 6.
- **TOOL-dFurnishedOrders-9** — Items 9 (gap-roles-15). The role-by-step matrix derived from the item declarations
  and joined both ways (J13), arm 2 its new arm, rendered per role. Scout C row 9.
- **TOOL-dFurnishedOrders-10** — Items 10. Role metrics per role and item (J14, D7): answered calls from the hook's
  records (J12), the other classes from runlog's extractor, accepted against `role_orientation.py`'s baseline, kept
  in this build's file until dCalibratedLens's value ledger lands and reads it. Scout C row 10.
- **TOOL-dFurnishedOrders-11** — Items 11. The work order's memory slices (D4), code-notes slot and legacy slot,
  each under its own budget and answer (J15), the legacy slot in its four states capped by `retrofit.slot-bytes`,
  and the reuse scout's house index handed first as `roles.orientation.house-index` says, each `not installed` until
  its later build lands, each value seen on a planted work order. Scout B row 11.
- **TOOL-dFurnishedOrders-12** — Items 12. The `map` slot for the roles `memory.project-map` names (J16), with the
  unfolds each item declares, none or all as `memory.map-unfold` says (PM-6), `not installed` until
  TOOL-dTotalRecall-14 lands (D2). Scout B row 12.
- **TOOL-dFurnishedOrders-17** — Items 17 (gap-roles-22). The `code` slot rendered per item from its declared seed
  (J17): the seed's definitions with their ranges, callers, callees, tests and kit siblings, as ranges under
  `memory.code-budget` for the roles `memory.code-roles` names, the map's delivery extended to the researcher and
  the prompt writer, `not installed` until TOOL-dTotalRecall-8's `code` record lands. Scout B row 17.
- **TOOL-dFurnishedOrders-20** — Items 20 (gap-conc-10). The problems whose subject intersects an item's seed handed
  in its work order as rows (J18, J20), read from the problem register when the order is cut. Scout B row 20.
- **TOOL-dFurnishedOrders-18** — Items 18. The work order selecting instruction units by `feature.*` once
  dLinkedLibrary arms that selector (a stand-in that reports `unarmed` through `derive_load_set`), and the
  code-notes slot filled from the tag's bundle, delivered in the work order, on demand or not at all as
  `annotations.delivery` says. Scout B row 18.
- **TOOL-dFurnishedOrders-2** — Items 2. Prompt-writer calls batched by `prompts.batch` (`per-batch`, `per-task`)
  over TOOL-dBoundRoles-4's cycle and the stage `fan` (TOOL-dBoundRoles-22), a batch being one stage's fan of one
  role; the prompt writer's return gains a per-task key. Scout C row 2.
- **TOOL-dFurnishedOrders-16** — Items 16. Owner questions asked live while the build is attended (J22, D9), each
  held like every owner item raised while the owner attends and never decided when raised,
  `run.on-owner-question` deciding only an item raised while the owner is away, and a late answer placed by
  `entry.place` as an amendment that re-enters the item it answers, drawing on `flow.rework-budget`, seen red on a
  planted attended gate decided at raise and on a planted late answer that re-enters nothing. Scout C row 16.
