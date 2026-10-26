**Serves:** research TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25

# Spec brief — dLinkedLibrary, the twenty-five units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dLinkedLibrary/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dLinkedLibrary/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite: `memory/builds/dLinkedLibrary/build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-a.md` (units 1, 2, 3,
   5, 6, 13, 22, 24, 25), `-b.md` (4, 7, 11, 12, 17, 18), `-c.md` (14, 15, 16, 19, 20, 21) and `-d.md` (8, 9, 10,
   23). Each holds a seam row per clause with path:line at `771408f94`, and the places where a record and source
   disagree.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), the memory-layer, library-round, systems-round,
retrofit-round, night-pass and night-pass-two records (LB-*, AN-*, RF-*, NP-*, NT-*, FK-*, IA-*, SA-*), the gap
register `B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by line),
and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never edit an
instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-<n>.md`; H1
  `# TOOL-dLinkedLibrary-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order <k> ·
  advances TOOL-dLinkedLibrary-26`, with `<k>` your unit's order below. `OPEN` is the status token: `DRAFT` is not in
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py`). The shape is
  `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-13.md` line 3.
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for a unit that owns a node, `**Carries:** node:<node>` (the owned-node
  table below). A unit carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every part is carried
  by a spec of this build.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 5, 6, 10, 11, 19, 24) still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close. A policy key's non-default value is seen by a planted
  `.governance/policy.toml` naming that value, read through dGroundRules' one reader (`resolve`).
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `771408f94`: verify each line number before citing it. Unit 3
  retires `reuse_lookup.py` in the build run; the spec run still runs it, because it is the probe M5 names today.
- §8 forks: settle each by the README's rungs (the execution plan lines 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a `relaxes:` value joins a record with `**Bound:**`,
  `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a choice the README's
  `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open
  question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md` and `memory/HYGIENE.md`
  and `memory/TEMPLATE-SPEC.md` from their kit templates, `tools/workflows/*.js` from their `.template.js`, the
  `/unattended` and `/build` Skills from their templates, and the installed kickoff skill from
  `skills/session-kickoff/`: name the source as the edit and the render as its copy.
- A parent's surface (dTotalRecall's record find, record door, relation graph, README routing and level 0;
  dDeclaredLoop's loop kit and `Decided:` reader; dOrderedCharter's kinds register, record factory and charter
  renderer; dFairHearing's scorer factory and benchmark cases; dBoundRoles' `experiment` kind) is specced and NOT
  built. Cite the parent's spec by id and section as the interface and name the call you make; never re-spec it,
  never add a copy of it. Where your unit cannot run until it lands, say so in §2 as a build-run precondition, and
  where the clause names a stand-in, spec the stand-in and register it as a `[[stand-in]]` row
  (TOOL-dDeclaredLoop-13 S8).
- A policy key this build owns (the owned-node table) gets its catalogue row in `tools/policy/catalogue.toml`, landed
  by dGroundRules, through the factory dOrderedCharter specs (`core.py new policy-key <name> … --owner
  dLinkedLibrary`, TOOL-dDeclaredLoop-6 S4) once it lands, else by the catalogue's own row grammar at HEAD, and is
  read through `resolve` (Python), `readPolicy` (JS) or `policy.py get` (shell); its allowed values and default are
  the packet's Obligations row, verbatim.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dLinkedLibrary/build/2026-10-26-build-TOOL-dLinkedLibrary-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec that must change for your clause to hold is never edited: state the needed change in §8 as an ask for
  that build, its target build, its accept line, and your return names it. The main loop files every such ask once,
  after the writers return, so no two writers mint an id in one foreign family (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dLinkedLibrary/spec/` and `memory/builds/dLinkedLibrary/build/`; temp files go
  under the scratch path your harness names.

### What the last spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python annotations.py …`) and keep its
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
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- **A cited id leading a table cell defines it** (hygiene check 13): cite a foreign id inside prose, never as the
  first token of a table cell.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dLinkedLibrary` after every writer returns.

## The parents are specced, not built

Every parent surface this build calls is specced and DEFERRED at HEAD (the four scout records list each by spec id):
dTotalRecall (`record-kinds.toml` and `record_kinds.py new`, `gov_record.py` and the record door, `record_extract.py`
with `extract_feature` and `extract_marker`, `gov_map.py`, the `code` record `code_record.py` with its definition key
`<path>::<qualified name>` and body hash, `policy_value.py`), dOrderedCharter (`tools/playbook/core.py`,
`namespaces.toml`, `edges.toml`, `edge_grammar.py`, `id_grammar.py`, `instructions_edit.py`, the charter renderer's
`entry-files` scope, `instructions-legacy.txt`), dDeclaredLoop (`tools/loop/loop.toml`, `commit_trailers.py`),
dFairHearing (`replay_scorer.py`, the benchmark's held-out cases), dWitnessedBar (`legacy_ledger.py` and `[[ledger]]`
registrations, `test.seed`), dSafePassage (`[[retired]]` rows in `tools/govkit/registry.toml`) and dBoundRoles (the
`experiment` kind). None of those files exists at HEAD. dGroundRules is landed: `tools/policy/policy.py` (`resolve`
at `:752`), `tools/policy/catalogue.toml`, `tools/policy/policy-mirror.js` (`readPolicy` at `:132`). Every policy key
this build owns already has its catalogue row there, owner dLinkedLibrary: fill a missing summary, never add a
second row.

Where a scout found that a design record, a parent spec or source disagree (each record's "Disagreements" section),
v2's clause governs; a parent spec it contradicts gets an ask (the rule above), never an edit.

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.decisions.major`, `policy-key.reuse.propose`, `record-kind.decision` | 1 |
| `policy-key.reuse.delivery` | 2 |
| `record-kind.recall-index` | 3 |
| `policy-key.annotations.grammar`, `policy-key.annotations.resolve-scope`, `record-kind.annotation-index` | 4 |
| `policy-key.annotations.lookup`, `system.annotations` | 7 |
| `record-kind.baseline`, `record-kind.census`, `record-kind.ruling`, `policy-key.retrofit.decisions`, `policy-key.retrofit.practice-pending`, `policy-key.retrofit.reconstruct`, `item.adopt.census`, `item.adopt.practices`, `item.adopt.decisions`, `item.adopt.decisions-ratify`, `item.adopt.reconstruct` | 8 |
| `record-kind.research-return` | 13 |
| `policy-key.memory.code-enrich` | 15 |
| `record-kind.gotcha` | 22 |
| `item.adopt.instructions` | 23 |

## Shared interfaces — one spelling for every writer

Fixed so twenty-five specs by five writers agree on the interface axis (M2). Each row names its owner, the unit whose
spec defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked
"proposed" has no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one
wrong says so in its return and writes a deviation record rather than a second spelling.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The reuse entry | `memory/map/features/<feature>.reuse.toml` beside its dossier and `memory/map/conventions/<name>.reuse.toml`, fields `tag`, `needs`, `anchors`, `date`, `build`, `decision`; a level-3 instruction unit in PLAY-dOrderedCharter-20's schema, proposed through `instructions_edit.py` (PLAY-dOrderedCharter-15 S2) and rendered once the owner accepts it (proposed) | 1 | layer-memory:625-640; scout A row 1 |
| I2 | The two-rater agreement | `derive_kappa(rows_a, rows_b)` beside the routing rubric in `tools/memory-tree/decision_rubric.py`, one function, called by unit 8's `adopt.decisions` (proposed) | 1 | layer-memory:703-708; scout D interface 12 |
| I3 | Record-kind rows | `research-return` (13), `decision` (1), `gotcha` (22), `census`, `baseline`, `ruling` (8), `annotation-index` (4), `recall-index` (3), each through TOOL-dTotalRecall-1 S9 `record_kinds.py new <name>`, node `record-kind.<name>`, tag `record.<name>` | each kind's unit | TOOL-dTotalRecall-1 §4 |
| I4 | The research-return marker | the clause's `kind: research-return`, written within `BIND_HEAD_LINES` (`tools/memory-tree/tree_lib.py:401`) of each research return; the line's exact form is unit 13's §8 to settle, and unit 6 selects on it (proposed) | 13 | layer-library:245-250 |
| I5 | Bug-class fields | front-matter keys `cause:`, `language:`, `platform:`, `from: <review>#<finding id>` (22) and `gate: <leg name>`, `planted: <path>` (24), parsed by `gotchas.parse_front_matter` (`tools/memory-tree/gotchas.py:233`); status `derive_gate_status(rec, legs)` answering `gated`, `partly-gated` or `ungated` (24) (proposed) | 22, 24 | layer-library:195-205; night-pass-two `[p6-gotchas]` |
| I6 | The `decides` edge and the trailer reader | the edge type `decides` from `edges.toml` (PLAY-dOrderedCharter-24 S1, widened by -28 S1), written on a decision row as one `decides=<target>` segment in PLAY-dOrderedCharter-24 S2's edge-target form (proposed); `Decided:` trailers read only through dDeclaredLoop's `commit_trailers.decided(commit)` (TOOL-dDeclaredLoop-23 S4), never a third parse | 22 | memory-plan `[cycle]` :206-226 |
| I7 | The supersession map | `id_grammar.derive_supersession_map` (PLAY-dOrderedCharter-18 S1), never `tools/memory-recall/extract.py`'s copy | cited | PLAY-dOrderedCharter-18 S1 |
| I8 | The library views | `tools/memory-tree/library_views.py` with `render_view(name)` and `check_view(name)`, called from `gen_build_index.py`'s check and write paths as `render_asbuilt_view` is (`gen_build_index.py:1474`); views `memory/views/research.md` (6), `memory/views/holds-now.md` and `memory/views/reuse.md` (5), byte-compared; `memory/views/` admitted by HYGIENE check 3's sanctioned set (proposed) | 6 | scout A interface 10 |
| I9 | The note grammar | `gov:note <tag>[,<tag>…] — <definition ≤80> → <target> [refs=<ref>[,…]]`, `<target>` a unit tag, a path or a command and `<ref>` an id or a path, `gov:feature <tag>`, `gov:end <tag>`; one parser, `parse_note_line`, in `tools/memory-tree/annotations.py`, which PLAY-dOrderedCharter-28 S5's code-site adapter calls rather than re-parsing `refs=` | 4 | systems.md:318-320; night-pass.md:256 |
| I10 | The annotation checks | functions in `annotations.py` behind one CLI, `python annotations.py check`, each arm a named function: `check_grammar`, `check_resolve`, `check_feature_anchors` (4), `check_marker_words` (12), `check_note_spans` (17); the `annotations` leg (7) runs that CLI and nothing else (proposed) | 4 | systems.md:344-358 |
| I11 | The `annotations` leg | one row in `tools/gate-legs.json`, name `annotations`, shaped like the `recall floor` row; the read hook `tools/memory-recall/recall-opened.js` widened to shell reads (AN-2) | 7 | systems.md:339-343, :607-631 |
| I12 | Policy reads | `resolve(<key>)` in Python, `readPolicy(<key>, {repo})` in a hook, `python tools/policy/policy.py get <key>` in shell; the keys as the packet's Policy keys spell them; `memory.code-languages`, `flow.rework-budget`, `flow.on-exhausted`, `instructions.legacy`, `annotations.delivery` and `review.left-shift` are read, never owned | each key's owner | `tools/policy/policy.py:752` |
| I13 | The marker namespace | members `marker.<word>`, one per existing `gov:` word with the check that reads it, over TOOL-dTotalRecall-9 S1's `extract_marker` and namespace row in `namespaces.toml`; an unregistered `gov:` word refused by `check_marker_words`; `note`, `feature`, `end` (4, 17) and `legacy` (23) join as members | 12 | systems.md:322-331; scout B census |
| I14 | The region factory | `tools/lib/region.py` with `REGION_OPEN`, `REGION_CLOSE`, `read_region(text, open, close)` and `apply_region(text, open, close, body)`, and its shell twin `region` in `tools/lib/region.sh`; the contract: one open and one close line, column 0, one trailing CR stripped, close after open, else a refusal; copy-installed kits carry it inline under a `PARITY_ROWS` row of `tools/lib/resolve-python.test.sh` (proposed) | 18 | `gen_build_index.py:2166`; `check-unattended.sh:211` |
| I15 | Ledger populations | `[[ledger]]` rows in TOOL-dWitnessedBar-13 §4's field names; populations `annotation-resolve-legacy` and `untouched-long-blocks` (11) and `instructions-legacy` (23, keyed `site · path`, TOOL-dWitnessedBar-18) | 11 | TOOL-dWitnessedBar-13 §4 |
| I16 | The feature node | tag `feature.<name>`, `<name>` the dossier header's `feature` value, the same tag a `gov:feature <tag>` anchor writes (19); the `feature` row of `namespaces.toml` carrying `role = "selects"` (20) | 19, 20 | memory-plan.md:88; PLAY-dOrderedCharter-19 S2 |
| I17 | The code reader | `tools/memory-tree/gov_code.py` with verbs `show`, `callers`, `tests`, `where`, standing in for `gov code`; `gov map code` is `gov_map.py code` (TOOL-dTotalRecall-14 S2); `where` on a git-grep primitive `grep_words(root, words, pathspecs)` extracted into `tools/lib/` from `tools/drift-audit/drift_report.py:2119` at its second instance (proposed) | 14 | research-code-orientation.md:85-112 |
| I18 | The definition key and body hash | `<path>::<qualified name>` and `code_row.hash` (TOOL-dTotalRecall-8 S2, S7), cited, never re-spelled; a row with no derivable extent carries no hash and is never fresh | cited | TOOL-dTotalRecall-8 |
| I19 | The code replay | the `code-replay` row of `replay_scorer.py`'s `INSTANCES` (TOOL-dFairHearing-12 S1), reading the transcript readers TOOL-dTotalRecall-17 S1 names | 16 | scout C row 16 |
| I20 | The origin field | values `written`, `reconstructed@<sha8> <sources>`, `imported:<path>`; a `- **Origin:** <value>` line the record door derives and refuses, never typed; ranked `written` above `imported` above `reconstructed` | 8 | retrofit.md:445-470 |
| I21 | The adopt program | `python tools/playbook/core.py adopt <verb>`, `<verb>` one of `census`, `practices`, `decisions`, `reconstruct`, `instructions`, never `govkit adopt` (which writes the install receipt, `govkit.py:12611`); its items `item.adopt.*` as `[[item]]` rows of `tools/loop/loop.toml` (proposed) | 8 | flow-steps.md:702-718 |
| I22 | The progress cell | the card line `retrofit — <k> populations · <seeded>→<now> · drained <d> this period · reads <share>`, with `reads not installed`, `not seeded` and `retrofit — skipped: <why>` forms, above `recent —` (proposed) | 10 | retrofit.md:516-521 |
| I23 | The legacy block | `<!-- gov:legacy src=<path> -->` … `<!-- /gov:legacy -->`, one pair per harness file after the project block, written through I14 (proposed) | 23 | adopter-instructions.md:180-184 |
| I24 | The house index | `tools/codebase-map/house_index.py`, ported from M1c's `render_house_index` (a build record, never imported); `load_corpus` and `seed_affordances` moved from `reuse_lookup.py` into `map_lib.py` first; its output the reuse scout's record `<date>-build-<unit id>-reuse-scout[-<x>].md` bound `**Serves:** research <ids>` (proposed) | 2 | layer-memory:716-744 |
| I25 | The lookup's retirement | `SPEC10_SCOUT_CUTOFF` beside `SPEC10_EVIDENCE_CUTOFF` (`.memory-tree.conf:162`), blank meaning off; `MAP_CLI` re-pointed, with the stale-dossier reader (`unattended.sh:10557`) given its own declaration so the re-point does not switch it off (proposed) | 3 | scout A disagreement 2 |
| I26 | Shared records | `memory/DECISIONS.md` (1, 22, 25) changes by supersession or pointer rows only, `ROW_DUPLICATE_PIN` (`.memory-tree.conf:693`) only downward; `gen_map._README` (`tools/codebase-map/gen_map.py:92-134`, edited by 3 and 25) re-renders `memory/map/README.md` once, after both | 25 | DECISIONS.md:5-6 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 18 → 17, 23 | `read_region` |
| 12 → 4, 7, 23 | `marker` |
| 22 → 24 | `cause:` |
| 22 → 1, 5, 17 | `decides` |
| 13 → 6 | `research-return` |
| 6 → 5 | `library_views.py` |
| 1 → 5, 4, 2 | `reuse.toml` |
| 1 → 8 | `derive_kappa` |
| 19 → 20, 4 | `feature.<name>` |
| 4 → 17, 11, 7 | `parse_note_line` |
| 17 → 7 | `check_note_spans` |
| 11 → 7 | `annotation-resolve-legacy` |
| 21 → 14 | `degraded` |
| 14 → 15, 16 | `gov_code.py` |
| 8 → 9, 23 | `origin` |
| 8 → 10 | `baseline` |
| 9 → 2 | `reconstructed` |
| 2 → 3 | `house_index.py` |

## The units

**Writer groups and build order.** The `order` value is the build order: the record corrections first, because they
touch the files later units edit; the region factory and the marker namespace, the primitives the annotation units
read; the bug-class fields and the `decides` edge before the gate status, the views and the edge extractors that
read them; the research marker before the research view, which lands the view seam the decision views reuse; the
reuse entries and the rater before the views, the both-ways anchor check, the house index and the adopt program;
the feature node before its selector and its anchors; the note grammar before the spans, the legacy populations and
the leg that assembles them; the ctags rows before the code reader, the reader before enrichment and the replay; the
retrofit kinds before the origin check, the progress cell and the instruction block; the house index before the
lookup's retirement. The build harness splits the 25 orders into five writer groups of consecutive orders; author
every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 25 (1), 18 (2), 12 (3), 22 (4), 24 (5) |
| 2 | 13 (6), 6 (7), 1 (8), 5 (9), 19 (10) |
| 3 | 20 (11), 4 (12), 17 (13), 11 (14), 7 (15) |
| 4 | 21 (16), 14 (17), 15 (18), 16 (19), 8 (20) |
| 5 | 9 (21), 10 (22), 2 (23), 3 (24), 23 (25) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dLinkedLibrary-25** — Items 25 (gap-mem-11). I26. Each of the eight records corrected at its source, one
  acceptance criterion per record, each a probe that reads the source and the record and sees them agree: the map
  README's path (re-render from `gen_map._README`), `backlog.py`'s "ships dark" docstring, the DEPL section's rows of
  other families (supersession and evacuation, TOOL-cSpliceWarden-4), the three duplicated ids with the pin lowered,
  the spec template's security-model line, the typed README statuses of builds that have a spec, the
  `ANNOTATION-STYLE` guide and template (moved together, `kit-dogfood-parity.test.sh:61`), and `HYGIENE.md`'s
  unused `note` kind with `gotchas.KINDS`. Re-count each figure at HEAD; scout A's "Clause 25 sources" lists them.
- **TOOL-dLinkedLibrary-18** — Items 18 (gap-mem-33). I14: the factory, every region parser re-pointed (the
  register's five, `check_roles.py`'s roles-catalogue region, govkit selftest's `scan_hold_region`, and the unlisted
  ones scout B found), each re-pointed parser's verdict unchanged on its own suite's cases, and the contracts that
  disagree today (substring, `str.find`, column-0) settled by §8 to the one contract. Scout B row 18.
- **TOOL-dLinkedLibrary-12** — Items 12. I13: a member per existing `gov:` word, re-counted at HEAD (scout B counted
  19 words and two fragments), each naming the check that reads it; an unregistered word refused, seen red on a
  planted one. Scout B row 12.
- **TOOL-dLinkedLibrary-22** — Items 22 (gap-mem-39, gap-tool-17). I5's `cause:`, `language:`, `platform:` and
  `from:` on every bug class, backfilled over the 151 records; I6's `decides` on every decision row; `Decided:`
  trailers read as decision rows through I6's one reader, re-pointing `tools/runlog/model.py:592`'s parse. Settle by
  §8 how 213 rows gain `decides` without rewriting a landed row (DECISIONS.md:5-6). Scout A row 22.
- **TOOL-dLinkedLibrary-24** — Items 24 (gap-mem-14, gap-mem-45). I5's `gate:`, `planted:` and
  `derive_gate_status`: gated only where the class names a leg in the leg manifest and a planted case the leg is seen
  to refuse; a gated class left off every checklist, the review's among them (dFairHearing-15 S6's `--all-ungated`
  calls it); a syntactic class gated at its second occurrence; anchors marking where it bit. Seen red on a class
  marked gated whose leg is absent and on one whose planted case passes the leg. Scout A row 24.
- **TOOL-dLinkedLibrary-13** — Items 13 (gap-mem-15). I3's `research-return` row and I4: the dated backfill over the
  existing returns, 72 at `1b759b620`, re-counted at HEAD with `research_count.py`'s predicate. Scout A row 13.
- **TOOL-dLinkedLibrary-6** — Items 6 (gap-mem-15). I8: the research view over the `research-return` kind, the seam
  units 5 reuses. Scout A row 6.
- **TOOL-dLinkedLibrary-1** — Items 1 (gap-mem-02, gap-mem-03). I1, I2, I3's `decision` row: decisions split by kind,
  reuse entries proposed with their build under `reuse.propose` and rendered once accepted, the major-decision log,
  the routing of today's rows (213 at HEAD, the clause says 200: re-count, and a deviation record if the population
  moves) by two raters at kappa 0.8 or better, below it the rubric revised and re-run, each re-run on the build's
  rework budget ending as `flow.on-exhausted` says, and the `[records]` rule reworded in
  `coding-governance-agents.template.md` (a governance carrier: the grant line). `decisions.major`'s three values.
  Scout A row 1.
- **TOOL-dLinkedLibrary-5** — Items 5. I8: the holds-now view over I7 and the reuse view over I1, beside
  dTotalRecall's README routing and relation graph, which this unit reads and never renders. Scout A row 5.
- **TOOL-dLinkedLibrary-19** — Items 19. I16: the dossier header (`parse_dossier`, `map_lib.py:1022`) as the
  feature node, its prose moved into units and records as NP-16 settles, the 32 dossiers migrated. Scout C row 19.
- **TOOL-dLinkedLibrary-20** — Items 20. I16's `role = "selects"` on the `feature` row, armed when the namespace
  registers (NP-13); the dead-selector join that names `reader` and `practice` literally (PLAY-dOrderedCharter-10 S4)
  needs to read `role` instead: an ask, or a factory this unit extracts at the third instance. Scout C row 20.
- **TOOL-dLinkedLibrary-4** — Items 4 (gap-mem-08, gap-mem-17). I9, I10, I3's `annotation-index`: the grammar, the
  generated index, the resolve check over notes alone or every comment reference as `annotations.resolve-scope`
  says, `gov:feature` anchors checked both ways with I1's entries, the shipped-evidence signal (drift-audit Signal
  2) re-checked first; `annotations.grammar`'s three values, `pushed-at-read` firing on shell reads too. The planted
  reds layer-memory:802-824 names. PLAY-dOrderedCharter-28 §3 hands this grammar to dTotalRecall: an ask. Scout B
  row 4.
- **TOOL-dLinkedLibrary-17** — Items 17 (gap-mem-31, gap-mem-32, gap-mem-39). Typed edges from annotations, front
  matter, dossiers and decision rows as adapters in PLAY-dOrderedCharter-28 S5's table; `decides` on decision rows
  read from unit 22; the span rule over I14's contract, each refusal (unterminated note outside a definition, orphan
  `gov:end`, crossed or nested tags, mismatched tag) seen red on a planted file; the span share re-measured with the
  map's extractors, the hybrid losing at 80% or more. Name who adds definition extents (TOOL-dTotalRecall-13). Scout B
  row 17.
- **TOOL-dLinkedLibrary-11** — Items 11 (gap-mem-18). I15: the resolve check's legacy (the scalar pin at
  `tools/drift-audit/drift_signals.py:308` becoming a keyed shrink-only population) and the untouched long blocks
  (over 12 lines, keyed by path and anchor) registered as ledger populations. Scout B row 11.
- **TOOL-dLinkedLibrary-7** — Items 7 (gap-mem-12, gap-mem-19). I10, I11: the leg; `annotations.lookup`'s three
  values (AN-1); the read hook on shell reads (AN-2); the follow-through test with its threshold, sample size and
  window fixed in the spec before it runs, and a measure separating following a pointer from working on the same
  build. Scout B row 7.
- **TOOL-dLinkedLibrary-21** — Items 21 (gap-mem-34). The ctags pack only: TOOL-dTotalRecall-8 S10 and AC8 already
  spec the `memory.code-languages` switch, the stop on a missing ctags and the meta columns; cite them, spec the
  pack's rows and its stub-driven criteria (ctags is not installed on node d). Scout C row 21.
- **TOOL-dLinkedLibrary-14** — Items 14. I17: `gov map code`, `gov code show`, `callers`, `tests` and `where`, `git
  grep` the engine of `where` and the floor for a language with no extractor; the level-0 counted `code` line is
  TOOL-dTotalRecall-14 S8's, cited. Scout C row 14.
- **TOOL-dLinkedLibrary-15** — Items 15 (gap-mem-29). Purposes from docstrings and headers first, an agent pass for
  the rest as `memory.code-enrich` says (`symbol-hash-slots`, `in-code-notes`, `derived-only`), keyed to I18's body
  hash and stale when it moves, joined both ways with a pending population. Scout C row 15.
- **TOOL-dLinkedLibrary-16** — Items 16. I19: the replay's losing test extended to code, with the `code` slot and
  without it; no dBoundRoles spec carries that slot: settle by §8 (render it from the code record by the research's
  candidate B rule, or an ask). Scout C row 16.
- **TOOL-dLinkedLibrary-8** — Items 8 (gap-mem-24, gap-mem-25). I3's `census`, `baseline`, `ruling` rows, I20, I21:
  `adopt.census`, `adopt.practices` through `retrofit.practice-pending`, `adopt.decisions` through
  `retrofit.decisions` with I2's raters, a split candidate kept `reconstructed` and not major, ratified only under
  `docs-owner-ratifies` or `docs-and-trailers` (seen on a planted split candidate, FK-4-6), `adopt.reconstruct` under
  `retrofit.reconstruct`, a declined decision kept `rejected`. Carry the clause in parts if one spec cannot hold it.
  Scout D row 8.
- **TOOL-dLinkedLibrary-9** — Items 9 (gap-mem-25). I20: the origin check re-derived from history, `origin` among the
  fields every slice renders, the digest's ranking handed to unit 2, red on a planted `written` record. Scout D row
  9.
- **TOOL-dLinkedLibrary-10** — Items 10 (gap-mem-24). I22: the progress cell, from the ledger's counts; no "cell
  point" exists, so settle by §8 where the cell registers (`render_card` today, dFurnishedOrders' composer later).
  Scout D row 10.
- **TOOL-dLinkedLibrary-2** — Items 2 (gap-mem-03). I24, `reuse.delivery`: the house index in M1c's shape delivered
  through the card's `**Reuse:**` field, accepted by re-running aScoutedSeam's benchmark and its twelve held-out
  cases (refusing, naming the clone it lacks, without the incms and nicocares clones), passing only at 16 of 24 and
  8 of 12 or better. Scout A row 2.
- **TOOL-dLinkedLibrary-3** — Items 3 (gap-mem-09, gap-mem-22). I3's `recall-index`, I25: `reuse_lookup.py` and its
  agent retired, every reader rewritten by name and by value (scout A lists 38 files and the code importers), check
  12's §10 arm seen red on a planted spec citing `reuse_lookup` past the new cutoff, the `[[retired]]` row (dSafePassage
  -1 S2's row takes an entry or step id: settle the file list by §8 or an ask), memory-recall narrowed to what `record
  find` does not answer, its bench and union as dBoundRoles' `experiment` instance (no dBoundRoles spec carries it:
  an ask). Scout A row 3.
- **TOOL-dLinkedLibrary-23** — Items 23 (gap-deploy-26). I23, I15's `instructions-legacy`: at install an adopter's
  own instruction files rendered verbatim as a legacy block after the project block, admitted at install only and
  shrink-only after, under `refuse` admitted only with every paragraph ruled, every harness file wired at once and
  none overwritten, each paragraph proposed as a repository unit, an amendment or a drop; seen on a fixture holding
  `CLAUDE.md`, `GEMINI.md` and Copilot instructions, red on today's installer
  (`tools/agent-instructions/adopt-agent-instructions.sh:114-115`), on a planted legacy-list row and on a planted
  strict install carrying an existing `CLAUDE.md`. Settle by §8 where an adopter's legacy rows live, since the gov
  engine's list file is overwritten by an update. Scout D row 23.
