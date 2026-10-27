**Serves:** research TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20

# Spec stage returns — dFurnishedOrders, the five writers and the committer

The structured returns of the six agents of `unattended-build.js` run `wf_681d731e-31c`, extracted from its journal by script.

## dFurnishedOrders · TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 · spec-write

run wf_681d731e-31c/a58a90ba78a7e153d

**authored:** ["TOOL-dFurnishedOrders-10", "TOOL-dFurnishedOrders-11", "TOOL-dFurnishedOrders-12", "TOOL-dFurnishedOrders-17"]

**alreadyPresent:** []

**refused:** []

**summary:** I wrote all four specs in my group, in roster order. Each is Tier-2, OPEN, rev-1, base 2193e25d, and carries its `order` verb (13, 14, 15, 16) and `advances TOOL-dFurnishedOrders-21`. Each has the ten sections, its `**Carries:**` lines (clause plus owned nodes), every §8 fork marked `RESOLVED (agent, 2026-10-26, delegated)` with `widens:`/`relaxes:`, and a §10 with the probe result and the recall terms. Nothing is committed and the index is not regenerated. I ran hygiene checks 2, 12 and 25 in a throwaway clone with all current sibling specs present: none of my four specs had a finding. The exit code of 1 comes only from siblings' in-progress specs (units 1, 2, 3, 6, 8, 15, 19, 20). The clone is deleted. No deviation records were needed: none of the four departs from its clause.

Files:
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-10.md
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-11.md
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-12.md
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-17.md

**Unit 10 (role metrics).**
- I ran the D7 probe: runlog's `CLASSES` has no state, locate or method class, and a read of a method document classes as `read`.
- The spec adds an in-memory `derive_orientation_class` arm to `tools/runlog/extract.py`. It reads calls through runlog's own segment and git-subcommand readers, using the instrument's three patterns.
- "Accepted against the baseline" is a call-for-call parity check against the instrument's `klass` code, extracted from layer-roles.md:743-810. The one divergence is named.
- Rows are written by `write_role_metrics` at `agents --write`, beside the agent ledger.
- It reuses the load of runlog's `extract.py` that unit 3 adds to `handoff.py`. It uses unit 6's `read_answered_calls(root, session_id)` and unit 9's `derive_role_matrix(items, index)` with the shapes those specs fix.

**Unit 11 (memory, code-notes, legacy and house-index slots).**
- The memory slot is the block TOOL-dTotalRecall-9 S8's `reads:` list fills (D4). It renders not-installed until `record_find.py` resolves.
- The code-notes slot is capped at 2 KB and filled by unit 18; its `render_code_notes_slot(rows, rest)` call shape matches unit 18's spec.
- The legacy slot has four states, adding `not-seeded` to `render_slot`. It goes to roles whose `writes` is `product`, uses the item seed (J17) as its write set, and is capped by `retrofit.slot-bytes`.
- The house index goes to the reuse scout only, first under `handed` or `pointer` and absent under `off`. It is always not-installed for now, since dLinkedLibrary has no spec.

**Unit 12 (map slot).**
- `derive_role_set` reads a `ROLE_SETS` table.
- A FACT-QUESTION showed that `layer` cannot separate structural from working roles: all 12 core roles carry `layer.roles`.
- Under `structural-roles` the slot also needs the item to declare `map = "base"`.
- The not-installed line names the unfolds each `memory.map-unfold` value would give, so all three values are visible before the renderer lands.

**Unit 17 (code slot).**
- Roles are gated by `memory.code-roles` through `derive_role_set`, and the seed comes from J17.
- The rows are ranges only, with body lines dropped and counted. They are cut by unit 11's `derive_slot_cut` under `memory.code-budget`, where `k` means 1,024 bytes.
- The query over the code record is not specced, because the packet keeps dTotalRecall's surfaces as stand-ins. The spec fixes only the row grammar and the reader verb it expects, and names the hand-over.
- `gov-researcher` joins `structural-roles`. The prompt writer gets its actor's `map` and `code` slots through `render --for`.

**Interface changes siblings should know about:**
- J14 gained an `agent` column (unit 10 §8 F4). Without it, a second `--write` doubles counts or a retried task-sha loses a row. No sibling reads J14.
- J16's "read off `layer`" is respelled: only `every-role` is derived, from `acts-as`; the other two sets are declared (unit 12 §8 F1/F2).
- I added one edge outside the brief's table: `TOOL-dFurnishedOrders-11` hands `derive_slot_cut` to `TOOL-dFurnishedOrders-17`. Both ends are declared, in specs I wrote.
- The lexicon accepted every name I minted. It refused `count_orientation_classes` (it suggested `measure_`); I did not use that name.

**Asks for the main loop to file:**
- dTotalRecall `BACKLOG.md` (D2): TOOL-dTotalRecall-14 §3 line 96 gives the `map` slot's delivery, its unfolds and `memory.project-map` to dBoundRoles. Clause cl-dClosedLoop-0203 gives them to this build (unit 12).
- dOrderedCharter `BACKLOG.md` (D2): PLAY-dOrderedCharter-17:72 says "dBoundRoles renders the slots", but clauses 0195 and 0203 give slot rendering to this build (units 4 and 12).
- dTotalRecall `BACKLOG.md`: TOOL-dTotalRecall-8 §3 gives the `code` slot and `memory.code-budget` to dBoundRoles, but clause 0208 gives them here. Its `code` record should land a `neighbourhood` reader that prints unit 17's §4 row grammar.
- dTotalRecall `BACKLOG.md` (D4): TOOL-dTotalRecall-9 S8 should write its `reads:` list as the body of unit 11's `### memory` slot through `render_slot`, not as a separate block.

## dFurnishedOrders · TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-9 · spec-write

run wf_681d731e-31c/ad9c149a22becd25e

**authored:** ["TOOL-dFurnishedOrders-7", "TOOL-dFurnishedOrders-14", "TOOL-dFurnishedOrders-6", "TOOL-dFurnishedOrders-9"]

**alreadyPresent:** []

**refused:** []

**summary:** I wrote all four specs in my group. Each is Tier-2, OPEN, rev-1, base 2193e25d, with the `order` verb from the roster (9, 10, 11, 12) and `advances TOOL-dFurnishedOrders-21`. Nothing is committed and the index was not regenerated. Files, all under C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/:
- 2026-10-26-spec-TOOL-dFurnishedOrders-7.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-14.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-6.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-9.md

I wrote no deviation records: no unit departs from its clause.

**Hygiene result.** I ran `check-memory-hygiene.sh --only 2,12,25` in a throwaway clone with every spec in the folder committed. One red is on my files: check 12 flags a one-sided edge, because unit 6's `consumes-from TOOL-dFurnishedOrders-8` (`### Method slices`) has no matching `hands-off TOOL-dFurnishedOrders-6` in unit 8. The edge is real: unit 6's method-document class reads unit 8's `### Method slices` block. I can't write unit 8's spec, so please add that one-line `hands-off` to it. The other reds in that run are on other writers' specs (1, 2, 3, 8, 20).

**What each spec decides that siblings need to know:**
- **Unit 7 (repairs).** A repair is a `repair` row in the return. Each value of `roles.on-contradiction` maps to an actor in TOOL-dBoundRoles-26's existing refusal table, so there is no second route table. Filing happens through a new driver verb, `unattended.sh --repaired`. It reuses the driver's existing ask auto-file (`write_ask_rows`, `derive_ask_seq` and `read_roster_family` in `unattended.sh`), which the scouts had missed. The repair's keys ride the backlog's free `data` clause. On D10, ids are minted through TOOL-dTotalRecall-3's counter where it is installed, else by `derive_ask_seq`, keyed by the repair's content hash. This does not close PLAY-dClosedLoop-32: an id the producer's run mints on an unpushed branch can still collide, so the main loop needs to dispose of that.
- **Unit 14 (range matching).** The lexicon flags `match` as an undeclared verb, so J11's `match_answered_range` is spelled `check_answered_range` (Python) and `checkAnsweredRange` (JavaScript). Unit 6 uses the same spelling. Both copies are held to one shared case table. The JavaScript copy and `deriveCallRead` live in a new `tools/roles/answered-calls.js`. `SHELL_READERS` (cat, head, tail, `sed -n`, grep) sits beside `scanCommandHeads` in scratch-guard.js. The carry hands a repaired fact in place of the original when the keys match exactly, and as a `### repair:<ask id>` block when the cut fact is wider.
- **Unit 6 (the hook).** It handles all three answered classes from P29 item 10: handed ranges, whole method documents whose slice is handed, and state calls, limited to four read-only git commands. A verifier is exempt when its `verifies` value (read from unit 5's index field) names the input class the read is handed under. On its own failure the hook records `hook-failed`, exits 0 below CLI 2.1.295 and exits 1 at or above it. Whether a failure then blocks the call is left to `runtime.hook-failure` (owned by dWellOiledMachine). The hook reads the session's records through `read_answered_calls(root, session_id)`, which returns `(records, malformed)`, or `None` when the session has no file.
- **Unit 9 (role matrix).** `derive_role_matrix(items, index)` returns `{steps, roles, kinds, undeclared}`, and `loop_items.py matrix --json` exposes it to units 10 and 2. `check_role_coverage` is arm 2, the check that every core item role acts in at least one core item. Each role's static block gets a `## Items` block.

**Asks the main loop should file in dBoundRoles' `BACKLOG.md`:**
1. **D1:** TOOL-dBoundRoles-13 §3 gives the answered-call hook to dWellOiledMachine, and v2:423 and v2:1965 send RC-7's design to dBoundRoles. Clauses 0197 and 0205 put both here, in units 6 and 14.
2. **Arm 2:** TOOL-dBoundRoles-1 §3 names TOOL-dBoundRoles-20 as the owner of the "every core role acts in a core item" arm. TOOL-dBoundRoles-20 S7 only reads that arm and never specs it. Unit 9 builds it.

**Shared-interface edits outside the brief's lists:**
- Unit 6 adds `readWorkOrderText` to scratch-guard.js's exports, extracted from TOOL-dBoundRoles-7 S4's work-order locator now that the locator has a second caller.
- Unit 7 makes `write_ask_rows`' `gates-green:` message prefix name the calling verb instead.

## dFurnishedOrders · TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-16 · spec-write

run wf_681d731e-31c/a88b75584b1a2afd6

**authored:** ["TOOL-dFurnishedOrders-20", "TOOL-dFurnishedOrders-18", "TOOL-dFurnishedOrders-2", "TOOL-dFurnishedOrders-16"]

**alreadyPresent:** []

**refused:** []

**summary:** I wrote all four Tier-2 specs in my group, in roster order. Nothing is committed and the index was not regenerated. Each spec has status OPEN, rev-1, base 2193e25d, streams tooling, its roster `order` (17, 18, 19, 20) and `advances TOOL-dFurnishedOrders-21`. Each has the ten sections and a `**Carries:**` line at its clause hash. Unit 18 also carries node:policy-key.annotations.delivery and unit 2 carries node:policy-key.prompts.batch.

**Checks run.** Hygiene checks 2, 12 and 25 were run in a short-path throwaway clone with every current spec committed, and showed no red on these four files (the clone is deleted). The reds it printed are on sibling specs: unit 6's one-sided edge with unit 8, unit 8's S7 and its section set, and Readers-clause reds on units 1, 3, 4, 15 and 19. By hand I also confirmed four things: every §7 leg name is in tools/gate-legs.json; every leg a Files-touched path trips is on the leg line (this added the two playbook legs and `govkit acceptance matrix` to unit 18); no backticked path in any §6 criterion is untracked; and every tracked path:line citation is in range. check-spec-tokens.py was not run; that is the main loop's job.

**Specs (all under memory/builds/dFurnishedOrders/spec/):**
- **2026-10-26-spec-TOOL-dFurnishedOrders-20.md.** Problems whose subject meets an item's seed are handed in the work order as `finding` rows.
  - The fetch half of `read_claims` is pulled out as `read_gov_namespace`, the second instance of that read.
  - A new inline verb `--problems-for <item>` takes seed paths on stdin. A path subject meets the seed through the driver's `overlaps`, which a gate arm keeps equal to `check_writes_intersect`.
  - The `### problems` block goes through `render_slot`. `read_upstream_rows` is widened so each `problem#<problem id>` row must be answered once.
- **2026-10-26-spec-TOOL-dFurnishedOrders-18.md.** `derive_load_set` gains a `features` argument and `derive --feature`; while no `feature` namespace is registered it reports `unarmed`.
  - `render_order_instructions` renders the feature-selected units by `instructions.slices`. `read_code_notes` feeds the gov_tag bundle rows to unit 11's `render_code_notes_slot`.
  - `annotations.delivery` is `work-order`, `on-demand` or `off`; under `off` there is no block.
  - The order's features stay empty until dLinkedLibrary's house index hands them over.
- **2026-10-26-spec-TOOL-dFurnishedOrders-2.md.** `--unit` can be repeated under `--for`, giving one `### input:work-order:<unit id>` block per unit.
  - A batch is one role's tasks at one `--item`. It is checked against unit 9's `loop_items.py matrix` verb and capped by `read_agent_limit`.
  - The prompt writer's return gains `tasks:list?`. `check_batch_tasks` refuses a return that misses a unit, adds one outside the batch, or names one twice.
- **2026-10-26-spec-TOOL-dFurnishedOrders-16.md.** `derive_attended` is the one place attendance is decided: the `attendance` setting includes `ask-live`, or the session's newest turn is the owner's, read through a new `runlog.py turns` verb. If either can't be read, the item is held.
  - An attended fork at `--dispatch` or gate at `--phase` is held by `write_owner_hold` and asked live.
  - `--fork-state` reuses the parsing `plan_state` already does to tell whether a fork was decided.
  - `placement.py place --late` places a late answer as an `amend` with `reenters: <unit id>#<F-id>` and draws `route-back` on `flow.rework-budget`. An answer that re-enters nothing is refused.
  - The unattended Skill line carries `grants: PLAY-dClosedLoop-3`.

**Edges and new names.** Every edge I declared is in the brief's table, and each producer's hands-off tokens appear in my specs: 4→20 and 4→18 `render_slot`; 19→20 `render_return_schema`; 8→18 `instructions.slices`; 11→18 `### code-notes` and `render_code_notes_slot`; 9→2 `derive_role_matrix`. I added no edge outside the table. The lexicon accepted every new function name; I changed `hold_owner_item` and `place_late_answer` to `write_owner_hold` and `write_late_placement` (in the end, `check_late_answer`). No deviation records were needed.

**Sibling disagreements for the main loop to fix:**
- Unit 11 S2 says `### code-notes` appears "in every work order", but the clause's `annotations.delivery = off` means no block (unit 18 F4).
- Unit 4's `ORDER_SLOTS` gains `instructions` for unit 18 (F3).
- Units 11 and 17 should share unit 20's `read_item_seed`, one seed call per render (unit 20 F5).
- Unit 19's `read_upstream_rows` is widened to the `### problems` rows (unit 20 S6).
- The brief's J20 names the `check_writes_intersect` subprocess; unit 20 uses its gated shell twin `overlaps` instead (F1).
- The brief's "one stage's fan" is read in unit 2 as the item's step, because stage rows exist only on harness entries (F1).

**Asks owed to other builds:**
- **dBoundRoles:**
  - TOOL-dBoundRoles-11 S5's caller-passed `--attended` flag is retired in favour of `derive_attended`.
  - TOOL-dBoundRoles-11 S6 has no branch for the `owner` answer; unit 16 adds it.
  - TOOL-dBoundRoles-4 cites `read_transcript` at handoff.py:825-828, but it is at :835 at base.
- **dPlacedRequest:**
  - The placement block of TOOL-dPlacedRequest-4 S4 gains a `reenters:` line.
  - TOOL-dPlacedRequest-1's move of run claims onto leases may move `read_claims`.
- **dOrderedCharter:**
  - PLAY-dOrderedCharter-11 S1 gains a `features` argument.
  - PLAY-dOrderedCharter-25 §3 says dTotalRecall arms `feature`, while clause 0209 says dLinkedLibrary.

## dFurnishedOrders · TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-19 · spec-write

run wf_681d731e-31c/af7e10d794a5cf92e

**authored:** ["TOOL-dFurnishedOrders-1", "TOOL-dFurnishedOrders-13", "TOOL-dFurnishedOrders-3", "TOOL-dFurnishedOrders-19"]

**alreadyPresent:** []

**refused:** []

**summary:** I wrote all four Tier-2 specs in my group, in roster order. Each one's status header reads OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling, plus its roster `order` verb (5, 6, 7, 8) and `advances TOOL-dFurnishedOrders-21`. I also wrote one deviation record. Nothing is committed and I did not regenerate the index.

I ran hygiene checks 2, 12 and 25 in a throwaway clone with my specs committed, alongside the sibling specs my edges join (units 7, 10, 14, 15, 20). The run was clean. Before that, check 25 had flagged words like "dropped" and "deleted" in §2 as retirements; I reworded those items. The four spec files run 14 to 22 KB each. Every proposed name passed `lexicon.py --suggest` except `select_notices`, which the lexicon refused; I folded that filtering into `derive_notices` and `derive_mcp_notices`.

Files (all under C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/):
- spec/2026-10-26-spec-TOOL-dFurnishedOrders-1.md
- spec/2026-10-26-spec-TOOL-dFurnishedOrders-13.md
- spec/2026-10-26-spec-TOOL-dFurnishedOrders-3.md
- spec/2026-10-26-spec-TOOL-dFurnishedOrders-19.md
- build/2026-10-26-build-TOOL-dFurnishedOrders-19-deviation-191.md (D5: stricter than TOOL-dDeclaredLoop-29@rev-2 S6, Risk stricter)

What each unit decides:
- **Unit 1:** pulls `measure_claim_staleness` out of `measure_dossier_staleness` and adds a new `map_diff.py --stale-records` verb. The kickoff append (`check_card_recall`) re-checks the card's recalled records once and writes `RECALL — stale <record> stale=<path>@<blob12>` or `RECALL — unchecked: <why>`. The fact line gains the optional `stale=` attribute. The orient workflow becomes `driver = "agent"`, and `gov-orienter` becomes mandatory with R13's `unenforced — <why>` escape.
  - The kickoff engine `SKILL.md` measures 18310 of its 18432-byte row. §8 F3 raises the row to 19456 under the run-may-raise terms in `template-size-limits.txt`, only if the pass actually crosses the row.
- **Unit 13:** the append places and shape-checks the scout's cell against TOOL-dTotalRecall-14 S5's header grammar. It writes `not installed` while `gov_map.py` is absent and refuses an invented cell.
- **Unit 3:** one recognizer in runlog `extract.py` and a new `notice` member of `KINDS`. The ledger persists notices as a suffix inside `<outcome>`, so the charter's `returned` micro-format does not change (§8 F1). `handoff.py` loads `extract.py` by file, the same route unit 10 uses. The default `none` keeps it dark.
- **Unit 19:** a `[return.establishes]` arm, and four new functions in `roles_lib`: `read_establishes`, `read_upstream_rows`, `render_return_schema` (draft-07, with the `maxItems` + `contains` shape from the prior-art probe) and `check_return_schema` (refuses any keyword outside a closed set, no new dependency). It adds a `handoff.py return-schema` verb, a `### return-schema` work-order block, and a `returnRows` argument on `unattended-unit.js`. Retries go through TOOL-dBoundRoles-5's existing route.

Shared-interface changes siblings must follow:
- **J8:** the card cell is spelled `project-map —`, not `map —` (unit 13 §8 F1), because PLAY-dOrderedCharter-4 prints an instruction-map `map —` block on replay. No sibling spec spells J8.
- **J9:** a third notice class, `other`, recorded only under `all` (unit 3 §8 F2, a FACT-QUESTION settled by a census of local transcripts). The two classes unit 10 counts are unchanged.
- **J6:** `stale=<path>@<blob12>` also admits `@absent` when the moved source is gone at HEAD. Units 7 and 14 read this mark.
- **J3:** unit 19 uses unit 15's lexicon respelling `derive_return_arms` in place of `compose_return_arms`.

Edges:
- Unit 1 hands off `gov-orienter` to unit 13, and `stale=` to units 7 and 14.
- Unit 3 hands off `notice` to unit 10.
- Unit 19 consumes `derive_return_arms` from unit 15 and hands off `render_return_schema` to units 7 and 20.
- The reciprocal lines already present in specs 7, 10, 14, 15 and 20 match these tokens.
- I added no edge beyond the brief's table.

Asks for the main loop to file (I filed none):
- In dDeclaredLoop's BACKLOG.md (D5): TOOL-dDeclaredLoop-29 S6 lets a dropped, invented or doubled row stand on a `record` edge. cl-0210 fails and retries it on every edge (deviation 191).
- TOOL-dBoundRoles-5 §3 and TOOL-dDeclaredLoop-29 §3 each hand the per-order return schema to the other; unit 19 now owns it, so both specs need correcting.
- PLAY-dOrderedCharter-4's replay `map —` block and the project-map cell need distinct names; unit 13 resolved this on its own side.

Parent dependencies (the build run re-grounds on these and stops the unit if a section is still absent):
- Unit 1 needs TOOL-dBoundRoles-13 S3/S4.
- Unit 19 needs TOOL-dBoundRoles-5 S1/S3/S6, TOOL-dDeclaredLoop-29 S3/S5 and unit 15.
- Unit 13 treats TOOL-dTotalRecall-14 as a stand-in and renders not installed until it lands.

## dFurnishedOrders · TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-4 · spec-write

run wf_681d731e-31c/af779422cc88556c5

**authored:** ["TOOL-dFurnishedOrders-8", "TOOL-dFurnishedOrders-5", "TOOL-dFurnishedOrders-15", "TOOL-dFurnishedOrders-4"]

**alreadyPresent:** []

**refused:** []

**summary:** All four units in my group are authored as Tier-2 specs, each OPEN rev-1 at base 2193e25d with its order verb (8=1, 5=2, 15=3, 4=4) and `advances TOOL-dFurnishedOrders-21`. Nothing is committed and no index was regenerated. I wrote no deviation records, because no unit departs from its clause.

I ran hygiene checks 2, 12 and 25 in a throwaway clone with the specs committed there, and they exit 0. I did not run check-spec-tokens.py, but I removed by hand every path in a §6 criterion that does not exist yet. All §8 forks are RESOLVED (agent, 2026-10-26, delegated) with `widens: none · relaxes: none`. In each unit one fork says the build run re-grounds on the unbuilt parents and stops the unit if one is still absent.

Specs:
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-8.md
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-5.md
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-15.md
- C:/projects/coding-governance/.claude/worktrees/unattended-furnished-orders-b4ef78/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-4.md

**Names changed from the brief (sibling specs must follow):**
- **J3 is renamed.** The lexicon refuses `compose_return_arms` (`compose` is not a declared verb, and the `lexicon naming predicates` leg would red on it). Unit 15 names the factory `derive_return_arms`, recorded as a FACT-QUESTION fork. Its hands-off lines to units 7 and 19 carry both names, so those writers can find either, but they should read `derive_return_arms`.
- **J21's second step id is renamed.** `workflows/retire-prebuild` is not a legal id, because the workflows kit's descriptor id is `review-harness`. Unit 4 uses `review-harness/retire-prebuild`, also a FACT-QUESTION fork.

**Design choices other writers should know:**
- **D6 (slice source).** dOrderedCharter is an ancestor of this build, so PLAY-dOrderedCharter-19's `doc.<name>#<seg>` section tags and `gov_tag.py where` will exist at the build run. Unit 8 addresses slices by those tags and cuts the text in the roles kit, stopping at the next `## ` heading outside a fenced block. `extract_chunks` lost two probes: its heading test ignores fences, and its 2400-character cap splits M2.
- **Budgets.** Unit 8's handed slices, unit 5's `## Trust` block and unit 15's probe line each re-derive every role's `budget` by TOOL-dBoundRoles-15's Pricing rule, so the authored body gains no byte.
- **Roster at build time.** There will be 13 role files. TOOL-dBoundRoles-18 merges the two reviewers into `gov-reviewer`, so units 8 and 5 key on that name.
- **D3 (unit 4).** `SPEC_COMMIT_CHECKLIST` falls back to its own `--for-diff HEAD~1..HEAD` literal. The universal classes ride the core field. `### bug-classes` goes in the `boundaries` frame slot. A caller that passes a retired `checklist` or `prebuild` key is refused.
- **Unit 5's cold verifier context** withholds only the commit-message read in `tier2-review`. It reaches the workflow script as a render-time token, `{{VERIFIER_CONTEXT}}`, the same way `{{FANOUT_CAP}}` does.
- **`render_slot`'s `point` is the bare slot name** (for example `map`), checked against `ORDER_SLOTS`. Units 11, 12, 17, 18 and 20 should call it that way. Unit 11 adds `not-seeded` to `SLOT_STATES`.

**Edges I added beyond the brief's table.** Both stay inside my group, both are declared on both ends, and both run from an earlier order to a later one:
- 8 hands off to 5 on `## Trust`: unit 8 deletes the re-verification orders, and unit 5's block states the rule that replaces them.
- 8 hands off to 4 on `doc.build-method#m6-passes-commits-parallelism`: `gov-builder` carries that M6 slice, which unit 4 edits.

**Grants used (`grants: PLAY-dClosedLoop-3`):**
- Unit 8 rewrites TEMPLATE-SPEC's verification rule.
- Unit 4 edits BUILD-METHOD M5, M6 and M8, the unattended Skill and verbs file, and TEMPLATE-SPEC's recurring sub-heads.

**Where scout B disagreed with the source:**
- `MEMORY_TREE_DIR` is also read by `SKILL.template.md:67` and by the conf stamp, so the adopter keeps it.
- Scout B missed two readers: the memory-tree kit's `[[contract]]` consumer at `kit.toml:439`, and M8's pointer at `BUILD-METHOD.template.md:253`. Unit 4 now names both.

**Asks for the main loop to file (I filed none):**
- D2, from unit 4: PLAY-dOrderedCharter-17's non-goal at line 72 says "dBoundRoles renders the slots". Clause 0195 gives slot rendering to this build, so this is an ask in dOrderedCharter's BACKLOG.md.
- From unit 15: TOOL-dPlacedRequest-7's item table names the tester's actor `role:tester`, while TOOL-dWitnessedBar-23 S7 writes `role:gov-tester`. Unit 15 makes the four tester items use one spelling. This is an ask in dPlacedRequest's BACKLOG.md.
- No parent spec claims `instructions.slices`, so unit 8 owes no ask. v2:442's line saying the key is dBoundRoles' contradicts only v2 itself.

## dFurnishedOrders · specs · commit

run wf_681d731e-31c/a585edffb23068314

**committed:** false

**sha:** 1a3ce03ddcff1e7f247492580378726c072cc3e7

**why:** The pre-commit hook refused the commit, so `git commit --only` exited non-zero. Nothing was committed, and HEAD is still 1a3ce03dd.

The cause is in the generator. `python -B tools/memory-tree/gen_build_index.py --write` printed this and rendered nothing (the delta was empty): "build-index: memory/builds/dFurnishedOrders/README.md: front matter declares 'status: OPEN' but 20 spec(s) carry a status header — the build status is DERIVED from them, and two answers to one question is exactly the drift this index removes. Delete the 'status:' key."

The hook then reported:
"HYGIENE check 9 FAILED — generated build index differs from a fresh render:
build-index: render owed under --staged — memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-1.md is staged as A, and an added or deleted path moves the record set
build-index: memory/builds/dFurnishedOrders/README.md: front matter declares 'status: OPEN' but 20 spec(s) carry a status header ... Delete the 'status:' key.
pre-commit: a gate failed — fix or 'git commit --no-verify' to override deliberately."

The fix is to delete line 8, `status: OPEN`, from the front matter of memory/builds/dFurnishedOrders/README.md. This stage may not edit that file and did not retry.

`set -e` did not stop the block when the commit failed, so the last two lines still ran. They showed all 20 specs staged as `A`, and they are still staged. The unrelated untracked file memory/builds/dFurnishedOrders/build/2026-10-26-build-TOOL-dFurnishedOrders-19-deviation-191.md was not staged.

The checklist is empty because step 6 has no new commit to run over.

**specs:** [{"id": "TOOL-dFurnishedOrders-8", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-8.md"}, {"id": "TOOL-dFurnishedOrders-5", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-5.md"}, {"id": "TOOL-dFurnishedOrders-15", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-15.md"}, {"id": "TOOL-dFurnishedOrders-4", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-4.md"}, {"id": "TOOL-dFurnishedOrders-1", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-1.md"}, {"id": "TOOL-dFurnishedOrders-13", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-13.md"}, {"id": "TOOL-dFurnishedOrders-3", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-3.md"}, {"id": "TOOL-dFurnishedOrders-19", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-19.md"}, {"id": "TOOL-dFurnishedOrders-7", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-7.md"}, {"id": "TOOL-dFurnishedOrders-14", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-14.md"}, {"id": "TOOL-dFurnishedOrders-6", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-6.md"}, {"id": "TOOL-dFurnishedOrders-9", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-9.md"}, {"id": "TOOL-dFurnishedOrders-10", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-10.md"}, {"id": "TOOL-dFurnishedOrders-11", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-11.md"}, {"id": "TOOL-dFurnishedOrders-12", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-12.md"}, {"id": "TOOL-dFurnishedOrders-17", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-17.md"}, {"id": "TOOL-dFurnishedOrders-20", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-20.md"}, {"id": "TOOL-dFurnishedOrders-18", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-18.md"}, {"id": "TOOL-dFurnishedOrders-2", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-2.md"}, {"id": "TOOL-dFurnishedOrders-16", "path": "memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-16.md"}]

**summary:** The spec commit was refused, so nothing was committed and HEAD is still 1a3ce03dd. The build-index generator would not render while memory/builds/dFurnishedOrders/README.md still declares `status: OPEN` in its front matter, so pre-commit check 9 failed. All 20 specs were found and are still staged, and no spec was edited. The fix is to delete that `status:` key, then rerun the stage.

**checklist:** 

