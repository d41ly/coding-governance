**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16

# Spec brief — dRankedPlan, the sixteen units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dRankedPlan/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dRankedPlan/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite: `memory/builds/dRankedPlan/build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md` (units 1, 7, 8, 11,
   12, 13, 14, 16) and `-b.md` (units 2, 3, 4, 5, 6, 9, 10, 15). Each holds a seam row per clause with path:line at
   `0689e7fa1`, a list of places where a parent spec and source disagree, and the open forks with the rung that
   settles each.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, the `[policies]`
rows at v2:1172, :1224 and :1283-1286, the presets at v2:1478-1610, and the row at v2:1779), `B/…-research-plan.md`,
`B/…-walkthrough.md` (P1-P4 at :318-391, the planned units), `B/…-flow.md` (FL-P2 and the levels table at :98-145),
`B/…-flow-steps.md` (the Plan items at :164-237, [probe] at :604-628, `review.pin` at :570), `B/…-flow-roles.md`
(FR-1, FR-12), `B/…-orientation.md` (OR-2 at :259-263), `B/…-layer-runtime.md` (the adapter capability table at
:829-844), `B/…-night-pass.md` (points 2, 3 and 6), `B/…-night-pass-two.md` (NT-1, NT-2), the gap register
`B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by line), and the
fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an instrument,
v2, the as-built view or the packet: the packet's Non-goals.

## The parents are specced, not built

dDeclaredLoop, dTotalRecall and dBoundRoles, this build's parents, landed their specs and are DEFERRED to their build
runs. dDeclaredLoop owns the loop kit `tools/loop/` (stage tags, the item registry `loop.toml` and `loop_items.py new`
(TOOL-dDeclaredLoop-24 S6), the transition record and `write_transition` (-3), the position engine and `next` (-7),
the move table with row B6 `designing → planning` (-13), the disposition record (-16), owner gates and
`derive_breakpoints` with `check_owner_disposition` (-19), scenarios and `select_scenarios` (-27), and `plan.exit`).
dTotalRecall owns the record kinds registry `record_kinds.py new` (TOOL-dTotalRecall-1 S9), the record writer
`gov_record.py new <kind>` (-2), the `code` record `code_file`/`code_edge` (-8) and the read-set budget
`check_read_set` with `record show <id>#<tag>` (-9). dBoundRoles owns the role catalogue: `gov-planner` and the `plan`
workflow entry (TOOL-dBoundRoles-1 S2, S4). Their own parents are specced too: dPlacedRequest (the request stand-in
`<git-common-dir>/requests/<key>.md` with `.typed` and `check_request_consent`, TOOL-dPlacedRequest-19 S2, S5; the
probe trigger `probe.py trigger`, -7 S3; the placement record's `scenarios:`, -10; the `no-ready-card` kickoff
stand-in, -3 S5), dKeptSession (the card's cells), dGroundRules (the one reader `resolve` at
`tools/policy/policy.py:752`, `policy.py get <key>`, `tools/policy/policy-shim.sh get <key>` from bash),
dOrderedCharter (the kinds register and the record-file factory, PLAY-dOrderedCharter-7 S4, S7; the `id#tag` form,
-24) and dFairHearing (`review_pin.py`'s kind-to-preset map, TOOL-dFairHearing-3 S8).

None of `tools/loop/`, `gov_record.py`, `record_kinds.py`, `review_pin.py` or `gov-planner.agent.md` exists at HEAD.
`tools/policy/` does, and the six keys this build owns already have catalogue rows (`tools/policy/catalogue.toml:204`,
`:531`, `:896-918`): no unit writes a catalogue row, each reads its key. So every spec cites the parent's spec by id
and section, or its frozen v2 clause, as the interface, and names the call it makes. Never spec a parent's mechanism,
never add a second reader of a policy key, a second record writer or a second gate. Where a parent's surface is
absent at the build run's base, the spec names the stand-in this build ships and registers it as a `[[stand-in]]` row
(TOOL-dDeclaredLoop-13 S8).

## Every spec, whatever its unit

- Path `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-<n>.md`; H1
  `# TOOL-dRankedPlan-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order <k>
  · advances TOOL-dRankedPlan-17`, on ONE line, with `<k>` your unit's order below. `OPEN` is the status token:
  `DRAFT` is not in `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py`). The shape is
  `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-13.md` line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for each node the owned-node table gives your unit,
  `**Carries:** node:<node>`. A unit carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every
  part is carried by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 4, 5, 14, 15, 16) still names its key words in backticks where they are code.
- Each clause's own "seen on" and "seen red on" cases are acceptance criteria, each observed RED on its planted case
  and green without it, by a probe or fixture of the unit's own code a pass can run. "Each value seen on its planted
  case" means one planted policy file per value of the key, each observed. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `0689e7fa1`: verify each line number before citing it.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. The scout records name each fork they saw and the rung that settles it; settle
  those, and any you find. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a `relaxes:` value joins a record with `**Bound:**`,
  `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a choice the README's
  `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open
  question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md` from their kit templates,
  `tools/workflows/*.js` from their `.template.js`, and the installed kickoff skill from `skills/session-kickoff/`:
  name the source as the edit and the render as its copy.
- `skills/session-kickoff/SKILL.md` has about 120 bytes of headroom under its size row
  (`tools/template-size-limits.txt`), and TOOL-dPlacedRequest-3 S5/S6 already spend prose there: put a kickoff
  behaviour in `manifest-check.sh` (a card cell, a rule), never in `SKILL.md` prose.
- A later build's surface named in your clause (dCalibratedLens's Plan lenses, dWellOiledMachine's intake hook and
  adapter capability table, dTendedCadence's `maintain.fixes`) is a stand-in or a join that build arms: spec the
  stand-in this build ships and name the hand-over, never the later build's mechanism (packet Non-goals, Later
  builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dRankedPlan/build/2026-10-26-build-TOOL-dRankedPlan-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dKeptSession/build/2026-10-26-build-KICK-dKeptSession-2-deviation-21.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec that must change for your clause to hold (scout B's two: no `loop.toml` `[[workflow]]` row for
  `plan` is owed by any parent, and TOOL-dPlacedRequest-3 §8 F8's `entry.intake` fixed row is never armed) is never
  edited: state the needed change in §8 as an ask for that build, its target build, its accept line, and your
  return names it. The main loop files every such ask once, after the writers return, so no two writers mint an id
  in one foreign family (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dRankedPlan/spec/` and `memory/builds/dRankedPlan/build/`; temp files go
  under the scratch path your harness names.

### What the last five spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python ratify.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. Name the token exactly as "Shared interfaces" spells it; the other writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours. The table under "Edges" is the set to declare;
  add an edge only when your spec truly reads or produces it, and say so in your return so the other writer adds the
  reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a sentence a fixture asserts) owes a
  `**Readers:**` clause naming every reader by path and by value (hygiene check 25), each found by `git grep` over
  the tree. Check 25 reads any retirement word ("drops", "retired", "replaces") beside a backticked token in §2: use
  one only where you mean it.
- **No link-shaped text**, a bracketed label followed by a parenthesised target, anywhere outside a real link,
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dRankedPlan` after every writer returns.

## Owned nodes

Each node is named by exactly one spec, as `**Carries:** node:<node>`.

| Node | Unit |
|---|---|
| `record-kind.plan`, `item.plan.record` | 16 |
| `policy-key.plan.unplaced` | 1 |
| `policy-key.plan.ratification` | 9 |
| `item.plan.exit` | 10 |
| `policy-key.plan.authority`, `item.plan.input`, `item.plan.dedupe`, `item.plan.research`, `item.plan.place`, `item.plan.lease` | 2 |
| `policy-key.plan.triage`, `item.plan.triage-rule`, `item.plan.triage-judge`, `record-kind.triage`, `record-kind.dupes` | 3 |
| `policy-key.kickoff.runs` | 8 |
| `policy-key.plan.kickoff` | 7 |

## Shared interfaces — one spelling for every writer

Fixed so sixteen specs by six writers agree on the interface axis (M2). Each row names its owner, the unit whose spec
defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked "proposed" has
no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one wrong says so
in its return and writes a deviation record rather than a second spelling.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The priority key | `priority: <n>` in a build README's front matter beside `parents:`, a positive integer, lower first, at most once, a non-conforming value refused by name; ties broken by `opened:` then slug; parsed beside `parents` in `parse_front_matter` (`tools/memory-tree/gen_build_index.py`) on the `order` verb's strict-parser model (proposed) | 1 | walkthrough:338 (P1); v2:1779; `ORDER_RE`, `_parse_order` |
| I2 | The plan view | `<MEMORY_ROOT>/PLAN.md`, generated by `gen_build_index.py --write` beside `LIVE.md`, one row per non-terminal build in plan order (priority, then `parents:` topological, then I1's tie-break): `\| Build \| Priority \| Parents \| Status \| Dormant \| Plan \|`; a build with no `priority:` listed under an `## Unplaced` heading and judged by `plan.unplaced` (`warn`, `refuse-new`, `review-only`) (proposed) | 1 | flow.md:135; flow-steps:186; `render_live` |
| I3 | The plan record | kind `record-kind.plan`, registered by `record_kinds.py new plan` (TOOL-dTotalRecall-1 S9) and written by `gov_record.py new plan` (TOOL-dTotalRecall-2); ONE file per build, `memory/builds/<slug>/build/<date>-build-<FAMILY>-<slug>-1-plan.md`; fields in `deviation_join.py`'s `FIELD` form `- **<Name>:** <value>`, named `Scope`, `Affected systems`, `Open questions`, `Probes owed`, `Read sets`, `Scenario`, `Scenario reason`; priority and parents stay in the README front matter only (proposed) | 16 | layer-memory.md:407; flow.md:98-145 (FL-P2) |
| I4 | The artifact levels | a data table the check reads, declaring `card` above `plan` above `brief`, each fact's one home and the levels that render it; `check_brief_derived` reds a brief record that types a plan field (I3's field names, `priority:`, `parents:`) (proposed) | 16 | flow.md:130-145; gap-flow-03 |
| I5 | The brief skeleton | `BRIEF_SKELETON` (`skills/session-kickoff/manifest-check.sh`), the one source the unattended grader `check_prompt_brief` (`tools/unattended/unattended.sh`) reads at BASE; a brief's plan-level fields rendered from I3, never typed | 16 | `manifest-check.sh` `BRIEF_SKELETON`; `BRIEF_FIVE` |
| I6 | The ratification predicate | `read_plan_ratification(slug) -> (value, witness)` in `tools/loop/ratify.py`, run as `python tools/loop/ratify.py <slug>`, reading `plan.ratification` through `resolve` and answering for `request` from the session's intake log, its owner-origin intake alone counting, never a relayed one (proposed) | 9 | FR-1 (flow-roles:173-199); v2:1224 |
| I7 | The intake log | dWellOiledMachine's `entry.intake` prompt-submit hook, PM-9; until it lands, TOOL-dPlacedRequest-19 S2/S5's `<git-common-dir>/requests/<key>.md` with `.typed` and `check_request_consent`, a `[[stand-in]]` row naming the hand-over | 9 | v2:401; TOOL-dPlacedRequest-19 S2, S5 |
| I8 | The fallback | under `plan.ratification: request` with no intake installed or an adapter not declaring the prompt-submit event, `plan.exit` falls back to TOOL-dDeclaredLoop-19's owner gate, released by -16's disposition record, its witness the literal `intake not installed` | 10 | clause 0378; v2:433-436 (RC-9) |
| I9 | The adapter capability read | `read_adapter_capabilities(harness)` answering the event set an adapter row declares; a row or table that is absent declares nothing ("measured and never claimed"); the planted Codex-shaped adapter declares no `prompt-submit` (proposed) | 10 | layer-runtime:829-844; `runtime.harnesses` (catalogue.toml) |
| I10 | The planner role and the Plan workflow | slot `gov-planner`, actor `role:gov-planner`, workflow `plan` (TOOL-dBoundRoles-1 S4); the triager is the same slot (flow-steps:183); the `item.plan.*` rows registered by `loop_items.py new` (TOOL-dDeclaredLoop-24 S6) with tags spelled `item.plan.input`, `item.plan.dedupe`, `item.plan.triage-rule`, `item.plan.triage-judge`, `item.plan.record`, `item.plan.research`, `item.plan.place`, `item.plan.lease`, `item.plan.exit` | 2 | flow-steps:180-190 |
| I11 | The ratified order | `check_ratified_order(slug)`: between ratifications the planner adds rows to I2 and never reorders the rows the last ratification fixed, under `planner-drafts-owner-ratifies`; `planner-within-themes` and `owner-orders` as their values say (proposed) | 2 | v2:1283; R2.4 |
| I12 | The triage rules and records | declared rules as `[[triage-rule]]` rows (home settled by unit 3's §8), each label recording the rule that set it on the `SEV · <id> · <level> · <why>` row (`render_sev_row`, `tools/memory-tree/backlog.py`); record kinds `record-kind.triage` and `record-kind.dupes` by `record_kinds.py new` (proposed) | 3 | walkthrough:350-353, :380-383; flow-steps:181-182 |
| I13 | The dormancy threshold | `LIVE_DORMANT_DAYS` (`.memory-tree.conf`), the one threshold; a dormant build disposed only by an owner-ratified disposition record (TOOL-dDeclaredLoop-16), shown in I2's `Dormant` column | 4 | walkthrough:346-347; `render_live` |
| I14 | Policy reads | `python tools/policy/policy.py get <key>`, or `bash tools/policy/policy-shim.sh get <key>` from bash; never `.governance/policy.toml` read directly | each key's owner | TOOL-dGroundRules-2 S6 |
| I15 | The card cells | `plan — next <slug> · <plan.kickoff value>` and `kickoff — <kickoff.runs value> · full` or `· re-orient`, in `render_card`'s line form (`skills/session-kickoff/manifest-check.sh`), each with its `skipped:` forms (proposed) | 7 (plan), 8 (kickoff) | `render_card`'s `live —` cell |
| I16 | The read sets | I3's `Read sets` field: `<item tag>: <id>#<tag>, …; <item tag>: …`, each key budgeted by `check_read_set` (TOOL-dTotalRecall-9 S6) at `plan.exit` (proposed) | 11 | PLAY-dOrderedCharter-24; research-memory-structure-b:126 |
| I17 | The probes owed | I3's `Probes owed` field, each probe triggered by `probe.py trigger --cause point --at item.plan.exit` (TOOL-dPlacedRequest-7 S3), `plan.exit` refused while one has no `probe` record (proposed) | 12 | night-pass:118-175; flow-steps:604-628 |
| I18 | The intent fields | I3's `Affected systems` (kits derived from the `code` record's `code_file` rows, TOOL-dTotalRecall-8 S6/S7, and checked against them) and `Open questions` (fork tags); `Scope` arms TOOL-dPlacedRequest-8 S4's `scope-paths` seed (proposed) | 13 | night-pass:202-213, :396-397 |
| I19 | The scenario field | I3's `Scenario`, `<tag>+<tag>` (TOOL-dPlacedRequest-10 S1, TOOL-dDeclaredLoop-27 S8), set from the placement record and revisable at Plan with `Scenario reason`; a later re-pick only through I20 | 14 | NT-2 (night-pass-two:99-106) |
| I20 | The plan revision | a plan revision is `item.plan.record`'s outcome `revised` (TOOL-dDeclaredLoop-15 F2) on the build's ONE plan record: a `## Revisions` region of entries `- **Revision <n>:** <what changed in the ratified plan> · <why>`, ratified as the plan is through I6, the move row B6 `designing → planning` (TOOL-dDeclaredLoop-13) recorded by `write_transition`, and Design re-entered on the ratified revision (proposed) | 15 | flow-steps:223, :235-237, :742; FR-12 |
| I21 | Plan Review | the plan record and its revision as a review subject, mapped to the preset `review.pin` passes by `review_pin.py` (TOOL-dFairHearing-3 S8), run until dCalibratedLens lands its Plan lenses; "a tree that holds no Plan lens" observed on the lens catalogue holding no plan row | 6 | v2:707 (C5-F14); flow-steps:570 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 16 → 14, 13, 11, 12, 15, 6 | `record-kind.plan` |
| 16 → 7 | `BRIEF_SKELETON` |
| 1 → 2, 4, 5, 7 | `PLAN.md` |
| 9 → 10, 2, 3, 15 | `read_plan_ratification` |
| 2 → 3, 15, 6 | `gov-planner` |
| 14 → 15 | `Scenario reason` |
| 4 → 5 | `LIVE_DORMANT_DAYS` |
| 15 → 6 | `## Revisions` |
| 8 → 7 | `render_card` |

## The units

**Writer groups and build order.** The `order` value is the build order: the levels and the plan record kind before
every field that lives in it; the priority key and the plan view before every unit that reads the order; the
ratification predicate before the fallback, the planner, triage and the revision that read it; the planner before
triage; the plan record's four fields; then triage, dormancy, the live mapping, the revision and Plan Review; the
two kickoff units last, reading the view and the card. The build harness splits the 16 orders into six writer groups
of consecutive orders; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 16 (1), 1 (2), 9 (3) |
| 2 | 10 (4), 2 (5), 14 (6) |
| 3 | 13 (7), 11 (8), 12 (9) |
| 4 | 3 (10), 4 (11), 5 (12) |
| 5 | 15 (13), 6 (14), 8 (15) |
| 6 | 7 (16) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dRankedPlan-16** — Items 16 (gap-flow-03). I3, I4, I5: the artifact levels declared as data, one plan record
  per build holding its concrete details, the brief derived from the plan, the spec and the stage's facts and never
  authored, each fact with one home a lower level renders and never restates; seen red on a planted brief that types
  a plan field. Settle by §8 where the levels live and whether `BRIEF_SKELETON` loses fields (scout A F16a-c: probe
  `check_prompt_brief` on a changed skeleton before choosing). TOOL-dPlacedRequest-21 F2's README stand-in for the
  plan record is re-pointed here. Scout A row 8.
- **TOOL-dRankedPlan-1** — Items 1 (gap-plan-01). I1, I2: `priority:` beside `parents:` and the generated plan view,
  and `plan.unplaced`'s three values each seen on its planted case. Settle the priority grammar and the view's home
  (scout A F1a, F1b). Scout A row 1.
- **TOOL-dRankedPlan-9** — Items 9 (gap-plan-03). I6, I7: the session's intake log, `entry.intake`'s prompt-submit
  hook (dWellOiledMachine's, PM-9) as a stand-in until it lands, its owner-origin intake alone read as the request's
  ratification by `plan.ratification`; the four values of the key each seen on its planted case. Scout B row -9.
- **TOOL-dRankedPlan-10** — Items 10. I8, I9: `plan.exit` under `plan.ratification: request` falls back to
  dDeclaredLoop's owner gate until the intake kind lands and the harness's adapter declares the prompt-submit event,
  held for the owner's disposition, witness `intake not installed`, kept per harness whichever of this build and
  dWellOiledMachine lands first; seen on a planted Codex-shaped adapter that reaches Plan's exit through it. Settle
  scout B F10a-c. Scout B row -10.
- **TOOL-dRankedPlan-2** — Items 2. I10, I11: the planner and triager role and the Plan workflow, `plan.authority`'s
  three values each seen on its planted case. The `plan` workflow's `loop.toml` row is owed by no parent: settle by
  §8 F2b (spec it here, or an ask). Scout B row -2.
- **TOOL-dRankedPlan-14** — Items 14. I19: the scenario field, set from the placement and revisable by the planner at
  Plan with its reason, a later re-pick only at a step boundary through I20. Scout A row 7.
- **TOOL-dRankedPlan-13** — Items 13 (gap-plan-08). I18: affected systems derived from the `code` record and checked,
  open questions as fork tags. Settle scout A F13a-c, the fork-tag grammar above all. Scout A row 6.
- **TOOL-dRankedPlan-11** — Items 11. I16: each role item's memory read set sized at Plan as `id#tag` keys. Scout A
  row 4.
- **TOOL-dRankedPlan-12** — Items 12. I17: `plan.record` declaring the probes owed before Design. Scout A row 5.
- **TOOL-dRankedPlan-3** — Items 3 (gap-plan-02, gap-plan-06). I12: triage as `plan.triage` says, by
  `plan.triage-rule`'s declared rules with the planner judging what no rule decides under `rules`, drafted and held
  for the owner to ratify in batches under `owner-batches`, the legacy backlog archived with only new asks triaged
  under `archive-legacy`, each value seen on its planted case. Settle scout B F3a-c. Scout B row -3.
- **TOOL-dRankedPlan-4** — Items 4 (gap-plan-05). I13: dormancy disposal — a dormant build disposed, not merely
  labelled, by an owner-ratified move the plan view shows; hand the safe-fix name to dTendedCadence's
  `maintain.fixes`. Settle scout B F4a-b. Scout B row -4.
- **TOOL-dRankedPlan-5** — Items 5. The live-build mapping carried out: each live build mapped to the chain build
  that absorbs it or kept, under the owner's ratification, recorded per build. Settle the population (v1's 23 rows
  or `memory/LIVE.md` at base, scout B F5a, a rung 2 probe) and the record (F5b). Scout B row -5.
- **TOOL-dRankedPlan-15** — Items 15 (gap-flow-04). I20: the plan revision record, seen on a planted fork the goal
  cannot survive whose revision Design receives. Design's re-design inventory is dIndexedDesign's (gap-flow-25): a
  non-goal. Scout B row -15.
- **TOOL-dRankedPlan-6** — Items 6 (gap-plan-04). I21: Plan Review, run until dCalibratedLens's Plan lenses land
  with the lenses of the preset `review.pin` passes from dFairHearing's catalogue, seen on a tree that holds no Plan
  lens. Scout B row -6.
- **TOOL-dRankedPlan-8** — Items 8. I15's `kickoff —` cell: the full kickoff only where `kickoff.runs` says
  (`no-ready-card`, `opening-a-build`, `every-session`, `plan-absorbs`), arming TOOL-dPlacedRequest-3 S5's
  `no-ready-card` stand-in with the key's value. Settle scout A F8a-b. Scout A row 3.
- **TOOL-dRankedPlan-7** — Items 7 (gap-plan-07). I15's `plan —` cell: kickoff using the plan as `plan.kickoff`
  says, `offer-next`, `binding` and `advisory` each seen on its planted case, and attended briefs gated as run-built
  ones are. Settle scout A F7a-c. Scout A row 2.
