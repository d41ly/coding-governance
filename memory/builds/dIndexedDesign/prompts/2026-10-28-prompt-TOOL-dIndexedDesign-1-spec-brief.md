**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16

# Spec brief — dIndexedDesign, the sixteen units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dIndexedDesign/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dIndexedDesign/README.md`: its build-level rules bind every spec, the fork rule
   above all. Its `BACKLOG.md` holds asks TOOL-dIndexedDesign-18 (unit 16 answers it) and -19 (unit 10 answers it).
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5, M12. Every unit is Tier 2: each is a new
   or changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite: `memory/builds/dIndexedDesign/build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md` (units 1, 2, 3,
   6, 16), `-b.md` (4, 5, 13, 14), `-c.md` (7, 8, 9, 12) and `-d.md` (10, 11, 15). Each holds a seam row per clause
   with path:line at `66934d2d4`, and the places where a record and source disagree.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), the flow-steps record
`B/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md` lines 230-265 (every `design.*` item's row: actor, input,
action, witness, routes), the walkthrough `B/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md` (D1-D3 at :437-469,
the design candidates at :412-426, CV2 at :809-832), the night pass and night pass two records, the ownership record,
the gap register `B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by
line), and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit
an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-<n>.md`; H1
  `# TOOL-dIndexedDesign-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order <k> ·
  advances TOOL-dIndexedDesign-17`, with `<k>` your unit's order below. `OPEN` is the status token: `DRAFT` is not in
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py`). The shape is
  `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-1.md` line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for each node the owned-node table gives your unit,
  `**Carries:** node:<node>`. A unit carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every part
  is carried by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 3, 4, 6, 7, 9, 11, 13, 14) still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. A policy key's non-default value is seen by a planted
  `.governance/policy.toml` naming that value, read through I3; each of its allowed values is a planted case where the
  clause says "each value seen".
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `66934d2d4`: verify each line number before citing it. Record each
  candidate you rejected and the test that rejected it (M12), under `### Alternatives rejected`.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`, ON THE SAME LINE as the ruling; a `relaxes:` value joins
  a record with `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a
  choice the README's `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave
  an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md`, `memory/HYGIENE.md` and
  `memory/TEMPLATE-SPEC.md` from their kit templates, `tools/workflows/*.js` from their `.template.js`, and the
  installed kickoff skill from `skills/session-kickoff/`: name the source as the edit and the render as its copy.
- A parent's surface is specced and NOT built (next section). Cite the parent's spec by id and section as the
  interface and name the call you make; never re-spec it, never add a copy of it. Where your unit cannot run until it
  lands, say so in §2 as a build-run precondition, and where the clause names a stand-in, spec the stand-in and
  register it as a `[[stand-in]]` row (TOOL-dDeclaredLoop-13 S8).
- A policy key this build owns already has its catalogue row in `tools/policy/catalogue.toml` (lines 41, 47, 920-948),
  owner dIndexedDesign: fill a missing summary and drain its name from `tools/policy/unsummarised-keys.txt`, never add
  a second row. Its allowed values and default are that row's, verbatim. Once every unit of this build is terminal,
  the policy kit's reader-coverage arm (`tools/policy/check_policy.py:425-435`, `:518-533`) reds any of the seven keys
  no literal call reads, so the owner unit of each key names that literal reader in its acceptance.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dIndexedDesign/build/2026-10-28-build-TOOL-dIndexedDesign-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec, or a spec of another build, that must change for your clause to hold is never edited: state the
  needed change in §8 as an ask for that build, its target build, its accept line, and your return names it. The main
  loop files every such ask once, after the writers return, so no two writers mint an id in one foreign family
  (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dIndexedDesign/spec/` and `memory/builds/dIndexedDesign/build/`; temp files go
  under the scratch path your harness names.

### What the last spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python plan_streams.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
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
  backticks included (hygiene check 2). Unit 9's tagged heading `## [section.goal] Goal` is link-shaped only if a
  parenthesis follows it: never write one there.
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it, and `widens:` and `relaxes:` on one
  line.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- **A cited id leading a table cell defines it** (hygiene check 13): cite a foreign id inside prose, never as the
  first token of a table cell.
- **An acceptance criterion's ledger token** is written in backticks before the line first wraps (check 23).
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dIndexedDesign` after every writer returns.

## The parents are specced, not built

Every parent surface this build calls is specced and DEFERRED at HEAD; the scout records list each by spec id.
dDeclaredLoop: the loop kit `tools/loop/` and `loop.toml` `[[item]]` rows through the item factory
(TOOL-dDeclaredLoop-24, -12), the stand-ins table (TOOL-dDeclaredLoop-13), `review.<stage>` (TOOL-dDeclaredLoop-19),
the stage-exit recommendation `item.design.recommend` (TOOL-dDeclaredLoop-22), `## Establishes` rows
(TOOL-dDeclaredLoop-29), the `Decided:` reader. dTotalRecall: `record-kinds.toml` and `record_kinds.py new`
(TOOL-dTotalRecall-1 S1, S9), the section table (TOOL-dTotalRecall-9), the stream-plan kind and `check_stream_plan`
(TOOL-dTotalRecall-25). dBoundRoles: the `experiment` shape (TOOL-dBoundRoles-16 §4), the `gov-planner` role and
`plan` workflow (TOOL-dBoundRoles-1 S4). dLinkedLibrary: the house index `house_index.py` and the scout's record
(TOOL-dLinkedLibrary-2 S5-S7), `reuse_lookup.py`'s retirement (TOOL-dLinkedLibrary-3), decision rows with
`decides=` (TOOL-dLinkedLibrary-22, -17), the research-return marker and view (TOOL-dLinkedLibrary-13, -6).
dKeptSession: the `repeat` request (KICK-dKeptSession-18). Reached through those parents, not parents themselves:
dOrderedCharter's edge grammar `edge_grammar.py` (PLAY-dOrderedCharter-24 S2-S3), tag bundles `gov_tag.py bundle`
(PLAY-dOrderedCharter-25 S1) and leg packs (PLAY-dOrderedCharter-19 S12); dWitnessedBar's leg factory
(TOOL-dWitnessedBar-11) and slot lines (TOOL-dWitnessedBar-28 S10); dFairHearing's `replay_scorer.py`
(TOOL-dFairHearing-12); dFurnishedOrders' `### Bug classes` field and `gotchas.py --for-names` (TOOL-dFurnishedOrders-4
S2-S3); dPlacedRequest's placement table (TOOL-dPlacedRequest-4). None of those files exists at HEAD. Where your unit
needs one of them and its build is not this build's ancestor, say so in §8 and route it as the rungs say (a
build-run precondition, an ask, or a stand-in), never by assuming it lands first.

Landed and readable now: dTrueNorth's `tools/memory-tree/design_lib.py` (`read_design`, `read_design_view`,
`parse_binding_lines`, `read_spec_edges`, `read_spec_writes`, `check_writes_intersect`, `read_spec_revisions`) and
`tools/check-spec-tokens.py` (`scan_carries`, `derive_carries_coverage`); dGroundRules' `tools/policy/` (`policy.py`
`resolve` at `:752`, `catalogue.toml`, `policy-mirror.js` `readPolicy`).

Where a scout found that a design record, a parent spec or source disagree (each record's "Disagreements" section),
v2's clause governs; a parent spec it contradicts gets an ask (the rule above), never an edit.

## Owned nodes

| Node | Unit |
|---|---|
| `item.design.ready`, `item.design.exit`, `policy-key.design.handoff` | 1 |
| `item.design.overlaps`, `policy-key.design.overlap`, `record-kind.overlap` | 2 |
| `item.design.research` | 5 |
| `record-kind.spec`, `item.design.unit-spec` | 7 |
| `item.design.input`, `item.design.decompose`, `item.design.reentry`, `item.design.inventory`, `policy-key.design.forks`, `policy-key.design.reentry`, `record-kind.feature-design`, `record-kind.fork`, `record-kind.inventory`, `record-kind.diff`, `record-kind.roster` | 8 |
| `record-kind.playbook` | 10 |
| `record-kind.playbook-set` | 11 |
| `item.design.seams`, `record-kind.seams` | 13 |
| `item.design.streams`, `policy-key.design.streams-when` | 15 |
| `policy-key.design.coverage`, `policy-key.design.coverage.semantic` | 16 |

Units 3, 4, 6, 9, 12 and 14 own no node; each still names the nodes it reads, in prose.

## Shared interfaces — one spelling for every writer

Fixed so sixteen specs by six writers agree on the interface axis (M2). Each row names its owner, the unit whose spec
defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked "proposed" has
no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one wrong says so in
its return and writes a deviation record rather than a second spelling.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The section tag and its reader | tagged heading `## [section.<seg>] <Title>`, `<seg>` the title lower-cased and hyphenated, never the ordinal: `section.goal`, `section.scope`, `section.non-goals`, `section.design`, `section.readiness`, `section.acceptance`, `section.gates`, `section.open-questions`, `section.revision-log`, `section.reuse-audit`; one reader `read_spec_section(text, tag)` in `tools/memory-tree/design_lib.py` that accepts the tagged heading, the legacy `## <n>. <Title>` of either tier, and returns the body; the cutoff key `SPEC_TAGS_CUTOFF` in `.memory-tree.conf`, blank meaning off; the shell kit's awk twin held in agreement by a case table, never an import (proposed) | 9 | scout C interfaces 1-3; TOOL-dTotalRecall-9 S1-S2 |
| I2 | The spec-site edge line | `**Edges:** <type>=<target>[,<target>]` at column 0 under the binding lines, one line per type, parsed only through PLAY-dOrderedCharter-24's `edge_grammar.parse_edge_lines`, called from one adapter `read_spec_edge_lines(text)` in `design_lib.py`; `implements=` targets a unit id, a `feature.<seg>` or a pinned clause `cl-dClosedLoop-NNNN@<hash8>` (the `design_lib.CARRY` shapes); `decides=` targets as TOOL-dLinkedLibrary-22 spells them. Distinct from §3's `### Edges` `consumes-from`/`hands-off` bullets, which stay the unit hand-off grammar (proposed) | 12 | scout C interface 4; PLAY-dOrderedCharter-24 S2 |
| I3 | The policy reader | Python: `read_design_policy(key, root)` in `design_lib.py`, key first and a string literal at every call site, reading by subprocess `policy.py get <key>` (a memory-tree import of the policy kit would close a kit cycle; declared as a `requires_if` row on memory-tree's `kit.toml`); shell: `"$PY" <policy kit>/policy.py get design.<key>` spelled literally; JS: `readPolicy('<key>', {repo})`. Keys and values verbatim from `catalogue.toml` (proposed) | 16 | scout A interface 1 |
| I4 | The design state | tokens `MISSING THIN FORKED READY` plus `UNCARRIED`; `plan_state`'s one-token awk contract (`unattended.sh:4458`) unchanged; a wrapper `derive_ready_state <spec> <cutoff>` printing `plan_state`'s token unless the coverage join returns a finding for that unit's spec, then `UNCARRIED`; the Python side `derive_unit_coverage(root, slug)` beside `derive_carries_coverage` (proposed) | 16 | scout A interface 3; flow-steps:246 |
| I5 | The Design exit | one driver function `check_design_exit <slug>`, called from `verb_phase` when the move enters `BUILDING` and from `--dispatch`; unit 16 lands it reading coverage as `design.coverage` says, unit 1 adds the `design.handoff` arms into it; it is the stand-in for `item.design.exit` until TOOL-dDeclaredLoop-13's row replaces it (proposed) | 16 | scout A interface 4 |
| I6 | The audit pin | `derive_past_pin_ids` (`gen_build_index.py:1621`) and the `@rev-N` grammar (`tree_lib.py:429-432`), cited, never re-read | cited | TOOL-dTrueNorth-5 |
| I7 | The overlap record and its acknowledgement | kind `overlap`, tag `record.overlap`, home `memory/builds/<slug>/build/<date>-build-<unit id>-overlap-<n>.md`, one row per pair `- <unit id> · <unit id> · <path> · acknowledged|unacknowledged`; acknowledgement is a §3 `### Edges` bullet `**overlaps** <unit id>`, read through `read_spec_edges(text, "overlaps")`, the verb added to check 12's verb list; the pair rule is `check_writes_intersect` over `read_spec_writes` and nothing else; the live population is every spec of a non-terminal build whose status is not terminal, DEFERRED included (proposed) | 2 | scout A row 2, interfaces 6, 8, 9; scout D interface 11 |
| I8 | The structured spec | the tagged canon of I1 as the spec's sections; the `spec` row of `record-kinds.toml` (TOOL-dTotalRecall-1 §4) carrying its `sections` column; the measurement instrument and its research record under this build's `build/` folder, never product (proposed) | 7 | scout C row 7 |
| I9 | The feature level | feature id `feature.<seg>`; the feature design record (kind `feature-design`) declaring each interface as `producer`, `consumers`, `contract`; a unit joins its feature by `**Edges:** implements=feature.<seg>`; the diff record (kind `diff`) classifying each interface change `additive` or `breaking` by a structural diff of declared fields; the inventory record (kind `inventory`) giving each completed unit `kept`, `amended <unit id>` or `retired` with its reason; the fork record (kind `fork`) carrying id, resolver, declared class and the ranked options with the pick, joined to the §8 F-item's `RESOLVED` mark (proposed) | 8 | scout C row 8, interfaces 5-6; flow-steps:235-239 |
| I10 | The scout's return | record `<date>-build-<unit id>-reuse-scout[-<x>].md` with its `**Index:** <sha8>` line (TOOL-dLinkedLibrary-2 S6), sections in M1c order `## Needs`, `## Sketch`, `## Anchors`, `## Census` (`- <choice>: <majority> (<n> of <m>)`), `## Matches` (`- MUST|SHOULD <path> :: <symbol> — <how>[; not <copy>]` or `none`), `## Unmet` (`- <need> — searched <what>`), `## Bug classes` (`` - `<name>` — <why> ``), `## Establishes` (`- <row id> · seam · <text>`); caps `MATCH_CAP = 12`, `MUST_CAP = 5`, `BUG_CLASS_CAP = 5` in `house_index.py`; the one reader `read_reuse_scouts(root, slug)` in `tree_lib.py`, widened to return the sections (proposed) | 13 | scout B interfaces 1-3 |
| I11 | The §10 outcome and the alternatives | one reader `read_spec_reuse(text)` in `design_lib.py`, outcomes `seam <record path>`, `no existing seam fits` (the exact phrase `reuse.propose` reads) or `reuse-first`; the alternatives bullet `- <candidate> — lost to <test> · <record path or command>` under `### Alternatives rejected` (proposed) | 4 | scout B interface 4-5 |
| I12 | The experiment factory | `tools/workflows/experiment.template.js` rendered to `experiment.js`, the second experiment harness after TOOL-dLinkedLibrary-2 S11's `reuse-bench.js`, which becomes its first entry; entries declare TOOL-dBoundRoles-16 §4's `[workflow.experiment]` table; a research return is tagged `kind: research-return` (TOOL-dLinkedLibrary-13); the replay scorer instance `bug-class-intent` in `replay_scorer.py`'s `INSTANCES` (proposed) | 5 | scout B row 5, interface 6 |
| I13 | The playbook kinds | kinds `playbook` and `playbook-set`, tags `record.playbook` and `record.playbook-set`, hyphenated; the declaration block keys as `memory/guides/PLAYBOOK-TEMPLATE.md:38-66` spells them, read only through `declared_list` and `declared_scalar`; a playbook keyed by its repo-relative path, the value README `playbook:` and TOOL-dPlacedRequest-4's `playbook:` line already carry; the set identity one function `derive_set_identity <records-root> <run>` in `lib-unattended.sh`; pack value `design`, slot `point.flow.leg-pack`, the new leg `playbook set check` (proposed) | 10, 11 | scout D interfaces 1-7 |
| I14 | The stream plan | TOOL-dTotalRecall-25's stream-plan kind, written by one planner module `tools/memory-tree/plan_streams.py` and one harness `tools/workflows/plan-streams.template.js`; its stream-pairing check calls `check_writes_intersect`, never a new rule; the opt-in signal a README front-matter key `streams: plan` beside `design.streams-when` (proposed, a fork for unit 15) | 15 | scout D row 15, interfaces 9-13 |
| I15 | Record kinds and items | every kind through `record_kinds.py new <name> --tag record.<name>` (TOOL-dTotalRecall-1 S9), node `record-kind.<name>`; every item an `[[item]]` row of `tools/loop/loop.toml` through the item factory (TOOL-dDeclaredLoop-24), node `item.design.<name>` | each node's unit | scout C interfaces 7-8 |
| I16 | The write-set reader | `design_lib.read_spec_writes` and `check_writes_intersect` only; the shell `read_files_touched` and `overlaps` are the sanctioned twins; no fourth reader | cited | scout A interface 7-8 |
| I17 | The coverage lens | a `coverage` entry in `SPEC_LENSES` of `tools/workflows/tier2-review.template.js`, rendered to `tier2-review.js`, run as `design.coverage.semantic` says (proposed) | 16 | scout A row 16 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 9 → 12, 7, 6, 8, 4 | `read_spec_section` |
| 12 → 16, 8 | `read_spec_edge_lines` |
| 12 → 13 | `bundle` |
| 16 → 1, 2, 8, 15, 3 | `read_design_policy` |
| 16 → 1 | `check_design_exit` |
| 7 → 8 | `record-kind.spec` |
| 2 → 6, 15 | `record.overlap` |
| 13 → 4, 14 | `read_reuse_scouts` |
| 5 → 14 | `experiment.js` |
| 10 → 11 | `record.playbook` |

## The units

**Writer groups and build order.** The `order` value is the build order: the section tag and its reader first,
because every unit that reads a spec section reads it through I1; the spec-site edge line, which the coverage join's
clause target and the feature level read; the coverage join with the shared policy reader and the Design exit, then
the hand-off that adds its arms to that exit; the structured spec, the design index and the agreement checks over
it; the feature level, which reads all of them; the scout's return, the experiment factory, the reuse check and the
bug-class step that read it; the playbook kinds; the stream planner, which reads the overlap record; design review by
policy last, because its key's derived default waits on dDeclaredLoop. The harness splits the 16 orders into six
writer groups of consecutive orders; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 9 (1), 12 (2), 16 (3) |
| 2 | 1 (4), 7 (5), 2 (6) |
| 3 | 6 (7), 8 (8), 13 (9) |
| 4 | 5 (10), 4 (11), 14 (12) |
| 5 | 10 (13), 11 (14), 15 (15) |
| 6 | 3 (16) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dIndexedDesign-9** — Items 9 (gap-design-10). I1. Scout C's reader population is the migration's scope: the
  7 live readers that use the number's value (group A, two of which misread Tier-1 today: `runlog/model.py:1449` and
  `review_replay.py:70`), the 23 title-keyed sites that still require `## <n>. ` (group B), and the 4 prompt files;
  each moves to `read_spec_section` or its awk twin behind `SPEC_TAGS_CUTOFF`, and both formats stay readable while
  the corpus migrates (walkthrough:466-467). Readers of other documents (the protocol's §8 and §13, the charter's
  `## 1.`) are OUT. TOOL-dTotalRecall-9's section table keys on the ordinal: file the ask, never edit it. Seen red: a
  Tier-1 spec whose Open questions section `plan_state` and `extract_open_questions` read correctly by tag where the
  ordinal misreads it.
- **TOOL-dIndexedDesign-12** — Items 12. I2. The spec site adapter over `edge_grammar.py` (unbuilt; a precondition);
  the `implements=` clause target is the form unit 16 reads; `decides=` as dLinkedLibrary spells it; `design.seams`
  reading a tag's bundle through `gov_tag.py bundle` (PLAY-dOrderedCharter-25, not an ancestor: route it by the rungs),
  handed to unit 13 as `bundle`. Settle in §8 whether `**Carries:**` stays the clause binding beside `implements=`
  (scout C interface 4); the coverage join must not count one clause twice.
- **TOOL-dIndexedDesign-16** — Items 16 and ask TOOL-dIndexedDesign-18 (`closes`). I3, I4, I5, I17. Extend
  `derive_carries_coverage` and check 29 (`gen_build_index.py --check-coverage`) to read `design.coverage`
  (`refuse`/`warn`/`off`); read the join at each Design exit (I5) and at each spec revision; `design.ready` gains
  `UNCARRIED`; `implements=` with a clause target joins as a carrier; the index renders coverage
  (`render_coverage` exists); the lens per `design.coverage.semantic` (`every-exit`/`with-spec-audit`/`off`). Ask -18:
  the product join already reads the as-built view; the unit's answer is that the Design-exit gate reads
  `derive_carries_coverage` rather than `carries.py`, seen red on a planted pin to the baseline hash of an amended
  clause. Both seen-red cases of the clause: a planted dropped clause, and a planted carrier that keeps every token
  and contradicts its clause, which only the lens sees (a lens case is a `New arm:` the main loop observes). Check 29
  grades nothing under the harness (PLAY-dClosedLoop-20): name how the exit reading covers what it misses.
- **TOOL-dIndexedDesign-1** — Items 1 (gap-design-04). I4, I5, I6. Add `design.handoff`'s three values to
  `check_design_exit` and the `--dispatch` floor: `derived-ready` (READY by I4, so FORKED and UNCARRIED refuse, which
  closes gap-design-04: `--dispatch` admits FORKED at HEAD), `ready-plus-audit` (READY plus a spec-audit record pinning
  the current revision, I6), `status-and-tier` (state the predicate from v2:1287 and flow-steps:246-247). Each value
  seen on its planted case; a planted `ready-plus-audit` hand-off with no audit seen red. PLAY-dClosedLoop-21's
  pin-aware `specs-audited` term shares I6: name it, do not close it unless you take it into scope by M2 AMEND.
- **TOOL-dIndexedDesign-7** — Items 7. I8. Measure first (walkthrough D3, :445-469): which sections findings land in
  (`review_replay.py` SPEC MODE), builder divergence, rework after spec (`read_spec_revisions`), cost; then the
  redesign as definitions, design, boundaries, interfaces and acceptance as fields, trialled against the old format,
  behind `SPEC_TAGS_CUTOFF`. The measurement's instrument and result are a research record; name the observation that
  would make the redesign LOSE (M12). Open ask PLAY-dClosedLoop-22 (binding-line grammar homeless in the template)
  lands in the same template files: take it into `closes` only if your spec carries its accept line.
- **TOOL-dIndexedDesign-2** — Items 2 (gap-design-02). I7. The cross-build join on the default branch (absent at
  HEAD), its arm in `check-spec-tokens.py` at spec-write, the kickoff card's `overlaps —` cell through the driver's
  `--overlaps`, and a `gen_build_index.py` region for the index view; `design.overlap` `warn`/`refuse`/`index-only`,
  each value seen on a planted overlapping roster, an unacknowledged overlap under `refuse` seen red.
- **TOOL-dIndexedDesign-6** — Items 6 (gap-design-09). Check 12 already grades M2's ordering axis and the mirror
  join; add the interface axis and the scope axis over `read_spec_section` and `read_spec_writes`, the tier rule as a
  predicate over the change's class (`SESSION-KICKOFF.md:116-122`), and unpushed specs read from other nodes' pushed
  branches (`check_cross_run_overlap`'s walk). Each new axis seen red on a planted disagreement.
- **TOOL-dIndexedDesign-8** — Items 8 (gap-flow-01, gap-flow-25). I9, I15. The largest unit: if its one-mechanism
  test fails (M2), carry the clause in parts and say so in your return so the main loop adds the units; never carry
  part of it silently. `design.reentry` (set values, never empty) and `design.forks`
  (`agents-feature-rich-expandable`, `preference-forks-park`, `owner-decides-all`) each read through I3, each value
  seen; additive-versus-breaking classified by the diff record (PLAY-dOrderedCharter-36 S5's widening classifier is
  the nearest seam); the re-design inventory of completed work (gap-flow-25).
- **TOOL-dIndexedDesign-13** — Items 13 (gap-design-11). I10. Widen TOOL-dLinkedLibrary-2's return to M1c's contract
  using TOOL-aScoutedSeam-1 §4's line spelling, and file the ask so aScoutedSeam-1 does not land a third grammar; the
  MUST and SHOULD seams handed on as TOOL-dDeclaredLoop-29 `## Establishes` rows; seen red on a return past each cap
  and a MUST that duplicates nothing.
- **TOOL-dIndexedDesign-5** — Items 5 (gap-design-07). I12. Extract the experiment factory at its second instance
  (charter `[reuse]`); the `research` workflow's `harness = "none"` (`tools/roles/workflows.toml:80-87`) becomes it;
  the night pass's point 2 shape (corpus with controls, blinding, variants on one schema, bounded fan, deterministic
  scorer or blind judge, reruns) is the acceptance.
- **TOOL-dIndexedDesign-4** — Items 4 (gap-design-05, gap-design-06). I11. Extend check 12's §10 arm past a new
  cutoff to check the outcome against a recorded probe (a scout record, I10) and each `### Alternatives rejected`
  bullet against its named test; seen red on a §10 citing no probe and on a rejected candidate with no test.
- **TOOL-dIndexedDesign-14** — Items 14. I10, I12. The bug-class step from `memory/gotchas/INDEX.md`'s `kind: class`
  rows at the spec's `base` (`gotchas.load_records_at`), armed only once the replay (I12's `bug-class-intent`) scores
  above the anchor ranking's top five (`cmd_for_paths`, cut to 5) with precision at least 20%, retired unarmed
  otherwise: spec both outcomes as acceptance. dFurnishedOrders is not an ancestor: route TOOL-dFurnishedOrders-4's
  field by the rungs.
- **TOOL-dIndexedDesign-10** — Items 10 (gap-flow-17) and ask TOOL-dIndexedDesign-19 (`closes`). I13. The kind row,
  Design's pack tag on the existing `playbook validity gate` leg, and the `repeat` route resolving a `record-kind.playbook`
  record with TOOL-dPlacedRequest-4's path stand-in pruned in the same landing, seen red on a planted `repeat` naming
  a path no playbook record holds. Fork in §8: the kind's `fence` validator form (scout D disagreement 7) and the
  kind's home (disagreement 8). gap-flow-17's "run 0 times" is the recipe half, not the leg (scout D disagreement 1).
- **TOOL-dIndexedDesign-11** — Items 11. I13. A set check that can go red at the bar (today `check-playbook.sh:668`
  reports set findings and never fails), registered at `point.flow.leg-pack`; the set identity folded into one
  function (two copies at HEAD); seen red on a planted set whose identity disagrees with its pieces.
- **TOOL-dIndexedDesign-15** — Items 15 (gap-design-12). I14, I7. The planner item after `design.overlaps`;
  `design.streams-when` each value planted (`off` runs no planning workflow, `always` one on every build, `opt-in` one
  only where the brief or the owner asks); a planted stream pairing two units whose write sets overlap seen red. Fork
  in §8: what "pairing" means (scout D disagreement 9) and the opt-in signal. TOOL-dBoundRoles-1 S4 gives `plan`
  `harness none`: the change is an ask in dBoundRoles' BACKLOG, never an edit. dWellOiledMachine's pick is unspecced:
  target TOOL-dTotalRecall-25's row.
- **TOOL-dIndexedDesign-3** — Items 3 (gap-design-03). Re-point the audit opt-in from the README `spec-audit:` key to
  the policy key `review.design` (TOOL-dDeclaredLoop-19's `review.<stage>`), its effort `review.<stage>.effort`
  through `tier2-review.js`'s `efforts`, the opt-in guard (fail 89) becoming the policy kit's guarded path, and the
  stage-exit recommendation called from TOOL-dDeclaredLoop-22, never re-specced. `policy.py get review.design`
  refuses on the derived default today (`policy.py:687-698`): state the precondition and what the unit does until it
  lands. The README key's readers (`unattended.sh:3975`, `:4024-4034`, `:4113`, `:4125`) owe a `**Readers:**` clause if
  any is retired.
