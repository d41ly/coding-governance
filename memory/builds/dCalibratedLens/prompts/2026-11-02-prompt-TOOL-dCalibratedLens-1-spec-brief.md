**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17

# Spec brief — dCalibratedLens, the seventeen units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dCalibratedLens/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys and Obligations sections bind every unit.
2. The build README, `memory/builds/dCalibratedLens/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your unit's row under "The units", and "Shared interfaces", which every writer reads.

Both parents are SPECCED AND UNBUILT: dFairHearing (`memory/builds/dFairHearing/spec/`) and dTendedCadence
(`memory/builds/dTendedCadence/spec/`). A primitive a parent spec defines is read as that spec spells it, and your
spec names the parent unit it waits on; it never re-specs it. The design sources the clauses compress are under
`memory/builds/dClosedLoop/build/` (`B/` below): v2 `B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, the
review system record `B/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md`, the night pass and night pass two
records, the layer records, the gap register lines the packet's Gaps cite, and the fork rungs in
`B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an instrument, v2, the
as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-<n>.md`; H1
  `# TOOL-dCalibratedLens-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** DRAFT · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling ·
  order <k> · advances TOOL-dCalibratedLens-18`, the `order` your roster row names; TOOL-dCalibratedLens-18 is the
  build's own open ask, which the build run's last unit closes.
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below).
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see still names its key words in backticks where they are code.
- Each clause's own "seen red on" and "each value seen on its planted case" cases are acceptance criteria, each
  observed RED on its planted case and green without it, by a probe or fixture of the unit's own code a pass can
  run. No criterion names the merge bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite
  arm goes on a `New arm:` line in §7, and the main loop observes it at the close.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams below are a scout's reading at `4ccde40d9`: verify each line number against source before citing it.
- §8 forks: settle each by the README's rungs (execution plan lines 900-946), in the §8 mark shape TEMPLATE-SPEC
  states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and carries `widens:` and
  `relaxes:`, each a value or `none`. Never leave an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run.
  `tools/workflows/tier2-review.js` is RENDERED from `tools/workflows/tier2-review.template.js`
  (`check-protocol-parity.test.sh --render`), as `memory/guides/REVIEW-PROTOCOL.md` is from
  `tools/workflows/REVIEW-PROTOCOL.template.md` and `.claude/agents/*.md` from `tools/roles/agents/`: name the
  template as the edit and the render as its copy.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-<n>-deviation-<k>.md`, in
  the grammar `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README). Do not commit it.

## What exists, and what waits

At `8bec4cefd` only two primitives this build reads are BUILT: dGroundRules' policy kit (`tools/policy/`: all six
keys this build owns are rows of `tools/policy/catalogue.toml`, with `budgets.py` and `guard.py`) and dSafePassage's
step gate (`tools/govkit/step_gate.py`, `tools/govkit/surface-classes.toml`). Every other seam below exists only as a
landed DEFERRED spec of dDeclaredLoop, dWellOiledMachine, dTotalRecall, dLinkedLibrary, dOrderedCharter,
dFurnishedOrders, dPlacedRequest, dTendedCadence or dFairHearing: `tools/loop/`, `tools/runtime/`,
`record-kinds.toml`, `library_views.py`, `kinds.toml`, `shape_run.py`, `lenses.toml` and `replay_scorer.py` are all
absent. Your spec names each such unit in a `**Waits on:**` sentence of §4 and in §3 as a build-run precondition;
it never specs that primitive itself. Where NO landed build or parent spec provides what your clause reads (the
unit rows below flag each as a PRIMITIVE GAP), your §8 settles by the rungs whether your unit provides it inside its
own scope or the build files an ask on the owning build; an ask is filed by the main loop, so your §8 mark states its
text and target and you write no other build's file.

## Shared interfaces — one spelling for every writer

Fixed so seventeen specs by six writers agree on the interface axis (M2). A writer who finds one wrong says so in
its §8 as a fork and settles it there; it never silently respells one.

- **S1 · the value ledger.** A generated library view `<MEMORY_ROOT>/views/value-ledger.md`, a `VIEWS` row
  `value-ledger` in `tools/memory-tree/library_views.py` (TOOL-dLinkedLibrary-5 S1, S5), record kind `value-ledger`,
  never typed. NOT `memory/ledger/`, which `gen_build_index.py` owns. Row shape
  `| kind | id | since | cost | catches | false-reds | last-catch | window | state |` (layer-expansions:261,
  `loop.price`). Written only by `python tools/loop/loop_review.py price`, which regenerates the view; each
  `loop-review` record keeps the snapshot it priced (layer-expansions:80). Row kinds and their providers:
  `kind=shape` (unit 7), `kind=probe` (unit 9), `kind=item` (unit 12), `kind=cap` (unit 15). Owned by unit 2,
  which defines the view, the row grammar and the `price` verb; units 7, 9, 12 and 15 each add one row provider and
  code no second writer.
- **S2 · the keep record.** Kind `keep`, keyed (ledger kind, id, date), the latest governing (layer-expansions:212,
  :263): an owner's decision to keep a priced item the Loop Review proposed retiring. Owned by unit 5.
- **S3 · the Loop Review module.** `tools/loop/loop_review.py`, beside `breakpoints.py`, `probe.py` and `scenario.py`
  in the loop kit (TOOL-dDeclaredLoop-19 S1, TOOL-dPlacedRequest-7 S3, TOOL-dDeclaredLoop-27 S5), one verb per item:
  `lease`, `gather`, `price`, `propose`, `file`, `record`. Its argv is the cadence row's `run`. Owned by unit 3,
  which ships the module, `lease`, `gather`, `file` and `record`; `price` is unit 2's and `propose` unit 5's, each a
  verb added to the same module.
- **S4 · the record kind `loop-review`.** A row in `tools/memory-tree/record-kinds.toml`:
  `tag = "record.loop-review"`, `layer = "layer.observability"`, `form = "fields"`,
  `writer = "loop_review.py record"`, homed at `<MEMORY_ROOT>/loop-review/`, one file per period key, at
  `point.memory.record-home` (TOOL-dTendedCadence-6 S6, S8, the `maintenance-record` sibling). Owned by unit 3. Every
  unit whose clause says the Loop Review reads, proposes or raises something adds a FIELD to this record, named in
  its spec, and a step to `gather` or `propose`; none adds a second record kind.
- **S5 · the items.** `[[item]]` rows in `tools/loop/loop.toml` tagged `item.loop.lease`, `item.loop.gather`,
  `item.loop.price`, `item.loop.propose`, `item.loop.file`, `item.loop.record`, each with actor, does, witness,
  routes and needs (layer-expansions:259-264; the row form TOOL-dDeclaredLoop-20 S1's `item.review.*`). `loop.*` is
  the item namespace and `review.loop.*` the policy keys; never mix them (layer-expansions:79).
- **S6 · the lease and period.** A cadence row at `point.cadence-items` in `tools/runtime/points.toml`
  (TOOL-dWellOiledMachine-59 S1), `name = "loop-review"`, `period-key = "review.loop.cadence"`, the form
  TOOL-dTendedCadence-2 S1's `maintain` row takes; lease ref `refs/gov/leases/run/loop-review/<period>` taken by
  `run_cadence_period` (TOOL-dWellOiledMachine-13 S6), the program reading its key from `GOV_CADENCE_KEY`. Period
  forms: `weekly` → `2026-W44`; `monthly` → `2026-11`; `every-n-landings` → `n<k>.<landing-sha12>`, the k-th window
  of n landings counted from landing records. `derive_period` (TOOL-dWellOiledMachine-13 S5) knows only `daily`,
  `weekly` and `every-session`: unit 3's §8 settles how `monthly` and `every-n-landings` get theirs. Owned by unit 3.
- **S7 · the lens kind and namespace.** `[[kind]]` row `kind.lens` in `tools/playbook/kinds.toml`; `[[namespace]]`
  row `ns = "lens"`, `owner = "dCalibratedLens"`, `layer = "layer.flow"`, source the `key` of each `[[lens]]` row of
  `tools/workflows/lenses.toml` (TOOL-dFairHearing-13 S1) and of a repository's overlay
  `.governance/instructions.toml`, extractor `tag_index:extract_lens`; a step-gate class `id = "lens"` in
  `tools/govkit/surface-classes.toml` with reader `step_gate.py:read_lens_members`; tags `lens.<key>`. The template
  is TOOL-dDeclaredLoop-27 S1, S2. Owned by unit 13; units 1 and 14 read it.
- **S8 · the policy route.** Every key is read with `python tools/policy/policy.py get <key>` (or `policy-shim.sh
  get <key>` from shell): `flow.promote`, `review.<stage>.effort`, `review.loop.cadence`, `review.loop.retire`,
  `review.loop.window-days`, `review.loop.catch-source`, and `budgets.*` (dGroundRules' census). A loop item WRITES
  NO POLICY VALUE: it proposes, and the owner writes through the guarded command (dDeclaredLoop's), as
  TOOL-dWellOiledMachine-51 S3 does for `build.spend-cap`. The one exception is the raise shape `guard.py`'s
  `check_raise_shape` already admits for a measured-file cap, argued in its change record (the packet's
  Obligations, v2:1346).
- **S9 · the measured-value factory.** `derive_measured_value(rows, field, min_rows)` in `tools/loop/measure.py`,
  nearest-rank p90 over the rows, refusing below `min_rows`, PRINTING a suggestion for the owner and never writing
  it. One function for this build's clauses 4, 6 and 16 (the charter's `[reuse]` rule at the third instance);
  `tools/run-gates/derive-ceilings.py`, TOOL-dWellOiledMachine-51 S3 and -53's `derive_estimate_hours` stay their
  kits' own (kits import no siblings). Owned by unit 4; units 6 and 16 call it.
- **S10 · the instruction-eval suite.** An instance `instruction-eval` in `INSTANCES` of
  `tools/workflows/replay_scorer.py` (TOOL-dFairHearing-12 S1), its cases as known-set files under
  `tools/workflows/evals/` in TOOL-dFairHearing-1's known-set format, and a held leg `instruction-eval` in
  `tools/gate-legs.json` whose `guard` lists the instruction units. Owned by unit 10.
- **S11 · the unit-tag citation.** Nothing today records which instruction units an agent loaded, followed or broke
  (gap-found-16). One field, `units: [<tag>, …]`, on a role agent's return and on a review finding, read by the
  Loop Review. Owned by unit 5, which settles in §8 where the field is written; unit 10 reads it to add a case.

## Owned nodes

| Node | Unit |
|---|---|
| `record-kind.value-ledger` | 2 |
| `item.loop.price` | 2 |
| `policy-key.review.loop.catch-source` | 2 |
| `record-kind.loop-review` | 3 |
| `item.loop.lease` | 3 |
| `item.loop.gather` | 3 |
| `item.loop.file` | 3 |
| `item.loop.record` | 3 |
| `policy-key.review.loop.cadence` | 3 |
| `policy-key.review.loop.window-days` | 3 |
| `item.loop.propose` | 5 |
| `policy-key.review.loop.retire` | 5 |
| `policy-key.review.<stage>.effort` | 1 |
| `tag-namespace.lens` | 13 |
| `policy-key.flow.promote` | 14 |

## The units

**Build order.** The `order` value is the build order. Primitives land before their features: the ledger and the
Loop Review before every row provider and every reading, the factory before its callers, the lens kind before the
lenses that use it. 2 (order 1), 3 (2), 7 (3), 9 (4), 12 (5), 15 (6), 4 (7), 6 (8), 16 (9), 17 (10), 5 (11),
10 (12), 11 (13), 8 (14), 13 (15), 1 (16), 14 (17).

- **TOOL-dCalibratedLens-2** — Items 2 (gap-maint-03 in part). S1: the view, its row grammar, the `price` verb, the
  `catches` column read from the source `review.loop.catch-source` names (`verdict-records` default,
  `node-journal`; v2:1345: another node cannot see a node's journal), each value seen on its planted case. Owns
  `item.loop.price`, `record-kind.value-ledger`, `policy-key.review.loop.catch-source`.
- **TOOL-dCalibratedLens-3** — Items 3 (gap-review-02). S3, S4, S5, S6: the Loop Review as a cadence step, run as
  `review.loop.cadence` says, its lease keyed by the selected period, each value (`weekly`, `monthly`,
  `every-n-landings`) seen on its planted case; the window `review.loop.window-days` (default 60) every reading
  uses. PRIMITIVE GAP: `derive_period` has no `monthly` or `every-n-landings` form. Owns the seven nodes the table
  gives it.
- **TOOL-dCalibratedLens-7** — Items 7 (gap-review-11). `kind=shape` rows priced from the shape-run rows
  `review.cost` writes for review acts (TOOL-dDeclaredLoop-20 S3 over `renderShapeLine`, parsed by
  TOOL-dTotalRecall-11's `shape_run.py`) and the journal reconcile writes for every other act
  (TOOL-dWellOiledMachine-19 S6).
- **TOOL-dCalibratedLens-9** — Items 9. `kind=probe` rows: probe cost from the probe act record's `Tokens-*`
  (TOOL-dWellOiledMachine-32 S8), and compactions per item kind from `class=compaction` journal lines joined to the
  act record's `Item` (TOOL-dWellOiledMachine-16 S3), as a sizing signal. PRIMITIVE GAP: the probe record carries no
  cost field.
- **TOOL-dCalibratedLens-12** — Items 12. `kind=item` rows: cost per item kind from trace rows through
  `read_act_records` (TOOL-dWellOiledMachine-53), a sibling of TOOL-dWellOiledMachine-51 S2's `derive_build_spend`;
  the `trace.cost` row is at `tools/policy/catalogue.toml` :1602 (WOM-32 S8's :1572 is stale).
- **TOOL-dCalibratedLens-15** — Items 15 (gap-review-19). `kind=cap` rows: each size breach priced by its bytes and
  its reads, and the Loop Review raising an owner item for a breach that persists or grows across reviews, counting
  only new or grown breaches. PRIMITIVE GAP: `check_cap` (`tools/policy/budgets.py`) prints a breach and nothing
  persists it; no journal class or record carries one, and "reads" has no producer.
- **TOOL-dCalibratedLens-4** — Items 4 (gap-review-03). S9, and `budgets.*` values re-derived from evidence and
  review cost: read through `resolve_caps`, a raise only through `check_raise_shape` with its DECISIONS row, every
  other movement proposed to the owner (v2:1346; the owner's FK-7-1, FK-9-2).
- **TOOL-dCalibratedLens-6** — Items 6. Each role's `memory.item-budget` derived from its p90 over 30 sliced work
  orders under `measured` (TOOL-dTotalRecall-9; bytes from TOOL-dTotalRecall-12 S9's slice manifest), through S9
  and the guarded policy command, the owner's own setting for a role winning (MS-2). PRIMITIVE GAP: the guarded
  command is dDeclaredLoop's and unbuilt, and a per-role value is not a cap `guard.py` admits.
- **TOOL-dCalibratedLens-16** — Items 16. The stall and loop classes of `JOURNAL_CLASSES`
  (TOOL-dWellOiledMachine-16 S3) trended per scenario, item and rule; `flow.rework-budget`, the deadlines and the
  thresholds re-derived through S9 once 30 builds have run under them; seen red on a planted class journaled and
  left out of the trend (the trend joins the tuple both ways).
- **TOOL-dCalibratedLens-17** — Items 17. Node beats (TOOL-dWellOiledMachine-52's `render_node_beat`) and the pools'
  ledgers trended, and the reservation estimate per item kind re-derived from `trace.cost`.
  TOOL-dWellOiledMachine-53's `derive_estimate_hours` already derives it: this unit trends it and writes no second
  deriver.
- **TOOL-dCalibratedLens-5** — Items 5 (gap-found-16, gap-design-08 in part). S2, S11: instruction effectiveness
  from returns and findings that cite unit tags; the `propose` verb pruning units that bear no load and tightening
  those broken often, as `review.loop.retire` says (`propose-ratify` default, `demote-then-propose`, `report`), each
  value seen on its planted case; a charter amendment proposed for a rule whose override records recur
  (PLAY-dOrderedCharter-2 S4's override kind, through `instructions_edit.py`, PLAY-dOrderedCharter-15). PRIMITIVE
  GAP: no return or finding grammar cites a unit tag. Owns `item.loop.propose`, `policy-key.review.loop.retire`.
- **TOOL-dCalibratedLens-10** — Items 10 (gap-review-14). S10: re-run as a held leg when an instruction unit
  changes; a confirmed finding whose cause is an instruction adds a case.
- **TOOL-dCalibratedLens-11** — Items 11 (gap-review-15, gap-review-16). The delivery metrics as `loop-review`
  fields, from `build_run_model` (`tools/runlog/model.py`) and the run record, landings from
  DEPL-dShippedRelease-1, and the owner queue's depth read with no bound (TOOL-dWellOiledMachine-48's owner items).
  PRIMITIVE GAP: no reading of owner-queue depth, and change failure rate and time to restore name no source record.
- **TOOL-dCalibratedLens-8** — Items 8. The not-in-view cause as a value of TOOL-dFairHearing-8 S8's disposition
  column (the stand-in for dDeclaredLoop's `review.dispose`), computed from the author's slice manifest, the map and
  the `code` slot (TOOL-dFurnishedOrders-17); the Loop Review's reading of its share, proposing the map's retirement
  if it does not fall by 15 points over 38 confirmed findings. TOOL-dTotalRecall-17 S7 files the
  slice-manifest-only ask here on a `lose`, and its non-goals hand the 38-finding measure to this unit.
- **TOOL-dCalibratedLens-13** — Items 13 (gap-review-17). S7, `review.opt-in` (TOOL-dFairHearing-3 S9) choosing a
  repository's lenses from its overlay, the lens kind's fixed set declared and the five lens slots among it, and
  lens tags joined to the step gate; seen on a planted repository lens swapped into a run, and red on a planted
  patch adding a sixth slot, a planted exclusion of a lens `review.opt-in` names (naming the key), and a planted
  lens tag removed with no change record, green on one naming its successor (`read_fixture_successors`). Owns
  `tag-namespace.lens`.
- **TOOL-dCalibratedLens-1** — Items 1 (gap-review-01). Lenses for Plan, Test, Deploy and Maintain as `lenses.toml`
  rows drawn from dFairHearing's catalogue, run at `review.<stage>.effort` through dDeclaredLoop's breakpoints
  (TOOL-dDeclaredLoop-19 `derive_breakpoints`), extending TOOL-dIndexedDesign-3's step 1a and
  `resolve_stage_efforts` (`tools/roles/roles_lib.py`), as TOOL-dIndexedDesign-3 F7 hands it here. Owns
  `policy-key.review.<stage>.effort`.
- **TOOL-dCalibratedLens-14** — Items 14 (gap-review-18). Lens removal by a swap (TOOL-dFairHearing-3's `optIn`) or
  by excluding a default lens, its slot then filled by an opt-in; a repository lens recording a replay result when
  one ran and never owing one; and scenario promotion as `flow.promote` says (`loop-proposes` default,
  `owner-only`, `off`): the Loop Review proposing a scenario from a recorded change two or more builds carried
  (TOOL-dDeclaredLoop-28 S3's `flow.adapt` records), ratified through `instructions.edit` with `promoted-from`
  edges (PLAY-dOrderedCharter-15), into `tools/loop/scenarios.toml` (TOOL-dDeclaredLoop-27 S4); builds in flight
  moving only at a step boundary and only if they comply; a declined proposal recorded, keyed by the change's
  content, and not proposed again until a build carries a changed form; each value seen on its planted case, a
  declined proposal the next review does not raise among them. Owns `policy-key.flow.promote`.
