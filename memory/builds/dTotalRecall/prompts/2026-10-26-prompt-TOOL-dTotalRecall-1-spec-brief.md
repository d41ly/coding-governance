**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26

# Spec brief — dTotalRecall, the twenty-six units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dTotalRecall/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every entry of "Shared interfaces", and the scout record your units cite:
   `memory/builds/dTotalRecall/build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md` (units 1-4, 7, 16, 18,
   19, 20, 22, 25), `-b.md` (8, 9, 10, 12, 13, 21, 23, 24) and `-c.md` (5, 6, 11, 14, 15, 17, 26). Each holds a seam
   table row per clause, with path:line at `73eab8dac`.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph, and the
`[policies]` rows the packet's Obligations list by v2 line), the gap register `B/…-gap-register.md` (the packet's
Gaps cite each gap's line), `B/…-layer-memory.md` (`[contract]` 299-363, the kind table 400-480, `[build]` 509-529,
`[names]` 531-560, `[relations]` 561-578, `[asks]` 580-604, the code record 765-785), `B/…-memory-plan.md`
(`[pockets]` 59-131, `[edges]` 171-204, legacy causes 340-349, `[gates]` 360-367), `B/…-systems.md` (the index,
`record find` and `record show` 509-548, the read channels 549-561 and 656-697), `B/…-project-map.md` (`[sort]` 50+,
PM-1/PM-2 390-401, placement, line, tiers and fit 538-614, `[purpose]` 655-672, `[checks]` 672-688, `[test]`
690-709), `B/…-research-project-map-a.md` and `-b.md`, `B/…-research-memory-structure-a.md` and `-b.md`,
`B/…-research-memory-pockets.md`, `B/…-research-memory-builds.md`, `B/…-research-memory-asks-decisions.md`,
`B/…-research-memory-map-reuse.md`, `B/…-lexicon.md` (`[integration]` 421-440), `B/…-research-final-atlas.md`
(83-123), `B/…-night-pass.md` (point 3, 202-206), `B/…-night-pass-two.md` (point 3, 228-270), `B/…-away-pass.md`,
`B/…-whole-audit.md`, the two design instruments `B/2026-10-17-build-PLAY-dClosedLoop-1-map.py` and
`B/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`, and the fork rungs in
`B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 903-946. You never edit an instrument, v2, the
as-built view or the packet: the packet's Non-goals.

## Only dTrueNorth is built; every other parent is specced and DEFERRED

All three scouts read HEAD `73eab8dac` and agree. dTrueNorth's specs are CLOSED. Every spec of dGroundRules,
dOrderedCharter, dFairHearing, dSafePassage, dDeclaredLoop, dPlacedRequest and dWitnessedBar is DEFERRED. These do
not exist at HEAD and are the surfaces this build calls: `.governance/policy.toml` and `tools/policy/`
(TOOL-dGroundRules-2, its reader; -9 S1, the caps census), `tools/playbook/kinds.toml` (PLAY-dOrderedCharter-7 S4),
`tools/memory-tree/build_records.py`, the record factory (PLAY-dOrderedCharter-7 S7/S8),
`tools/playbook/namespaces.toml` and the tag grammar (PLAY-dOrderedCharter-19 S1/S2), the one index
`<git-common-dir>/gov/index.db` with `tools/playbook/tag_index.py` and `gov_tag.py` (PLAY-dOrderedCharter-19 S4/S6),
`read_policy_value` in `tools/playbook/policy_value.py` (PLAY-dOrderedCharter-19 S8), `tools/lib/common_dir.py`
(PLAY-dOrderedCharter-19 S10), `tools/lib/coverage_join.py` (PLAY-dOrderedCharter-19 S9), the `pack` leg key
(PLAY-dOrderedCharter-19 S12), `tools/playbook/edges.toml` (PLAY-dOrderedCharter-24 S1, -28 S1/S2),
`tools/memory-tree/id_grammar.py` (PLAY-dOrderedCharter-18 S1), `doors.toml` (PLAY-dOrderedCharter-29 S5),
`namespaces.toml`'s `purpose-source` and `memory/project/chain.toml` (PLAY-dOrderedCharter-22 S1/S3),
`render_playbook.py --reference` (PLAY-dOrderedCharter-37 S1/S2), `tools/govkit/upgrade_steps.py` and
`tools/govkit/shims.toml` (TOOL-dSafePassage-1 S1/S3, -6), `tools/workflows/replay_scorer.py` (TOOL-dFairHearing-12
S1/S2), `tools/lib/gov-ref.sh` `write_gov_ref` (TOOL-dPlacedRequest-11 S1), `leases.offline` (TOOL-dPlacedRequest-1
S10), the card and lease refs (TOOL-dPlacedRequest-2, -1), `tools/lib/gov-feed.sh` `add_feed_event`
(TOOL-dPlacedRequest-13 S1/S2), and `tools/lib/legacy_ledger.py` with `test.seed`'s `seed_population`
(TOOL-dWitnessedBar-13, -15 S1).

The chain builds its parents first, so each spec CALLS those surfaces as their specs name them: cite the parent
spec id and section in §2 and §10, never re-spec it, and say in §8 that the build run re-grounds on the landed
code. A spec ships a stand-in ONLY where its clause names one (unit 19's root and Made-by stand-ins). Do not write
`consumes-from` edges to another build's units: §3 edges are within this build; a parent surface is a §2 precondition.

## Every spec, whatever its unit

- Path `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`; H1
  `# TOOL-dTotalRecall-<n> — <title>`, an EM DASH, never a colon.
- Status header `OPEN`, `rev-1`, `2026-10-26`, `node d`, `Tier-2`, `base 462d20f3`, `streams tooling`, the `order`
  verb your roster row names, and `advances TOOL-dTotalRecall-27` (the build's own open ask; the build run's last
  unit closes it). Copy a landed sibling's line shape, e.g.
  `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md` line 3, with `OPEN` for its status.
- Binding lines, each at column 0 on a line of its own: `**Carries:** <Items id>@<hash8> whole`, and for the unit
  that owns a node, `**Carries:** node:<node>` (the owned-node table below), one per line.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (units 10, 11, 21, 22, 23, 25) still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and
  the main loop observes it at the close.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in "The units" are a scout's reading at `73eab8dac`: verify each line number against source before
  citing it.
- §8 forks: settle each by the README's rungs (the execution plan lines 903-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`; a choice the README's `may: PLAY-dClosedLoop-3` grant
  lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open question: a FACT-QUESTION names its probe
  and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` and `.claude/roles.json` from `tools/roles/`, `memory/guides/*.md` and
  `memory/HYGIENE.md` from their kit templates (`tools/memory-tree/HYGIENE.template.md`), and
  `tools/workflows/*.js` from their `.template.js`: name the source as the edit and the render as its copy.
- A later build's surface named in your clause (dWellOiledMachine's map load and intake kinds for units 9, 17 and 19,
  dCalibratedLens's not-in-view for unit 17, dIndexedDesign's stream planner for unit 25) is a stand-in or a join
  that build arms: spec what this build ships and name the hand-over, never the later build's mechanism (packet
  Non-goals, Later builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-<n>-deviation-<k>.md`, in the
  grammar `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` shows (Serves, Departs
  from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with `<k>` = your
  unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and `author-recorded`
  (the README's deviation-values rule). Do not commit it.
- An ask your spec owes another build (a parent spec's row that disagrees with yours, say) is NOT filed by you: name
  it in your return and the main loop files it as a row in that build's `BACKLOG.md` (the README's writes rule).
- Write nothing outside `memory/builds/dTotalRecall/spec/` and `memory/builds/dTotalRecall/build/`; temp files go
  under the scratch path your harness names.

### What the earlier spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python gov_record.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours (a later unit never hands off to an earlier one).
  The edge list in "Edges" is the one to declare; add an edge only when your spec truly reads or produces it, and
  say so in your return so the other writer adds the reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a Serves kind) owes a `**Readers:**` clause
  naming every reader by path and by value (hygiene check 25), each found by `git grep` over the tree.
- **No link-shaped text**, `[x](y)`, anywhere outside a real link, backticks included (hygiene check 2).
- **A §8 mark's parenthesis is closed**: `RESOLVED (agent, 2026-10-26, delegated)`, provenance after the paren.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits
  the hygiene gate and the lexicon, no other); the gate reads tracked files only, so run it in a throwaway clone
  under your scratch path with your specs committed there. A red it prints on your files is yours to fix. The main
  loop runs `check-spec-tokens.py` after every writer returns.

## HEAD and the design differ from six clauses — settle each in its unit, never silently

- **D1 · the code record's re-timing "at this build's first unit" (unit 8).** v2:2033 `[owed]` and cl-0219 re-time
  the cold derivation at the build's first unit, so a losing record is never built. The derivation runs through
  unit 13's primitive and lands its kind row in unit 1's registry, so unit 8 is order 3, after both. Unit 8 makes
  the re-timing its first acceptance criterion, observed before any of its other code, over gov's tree and the
  planted adopter-scale fixture, and states the loss route in §8 (over 30 s or over 1 MB loses: the record is not
  built and its readers keep `git grep`). It writes a deviation record from "first unit" (risk equivalent: the two
  units before it build no code-record code).
- **D2 · who owns the record-kind factory (unit 1).** TOOL-dPlacedRequest-1 line 137 says "the `record kind` kind's
  factory is dConvergedCharter's"; cl-0212 makes this build's registry the record-kind factory. The clause binds.
  Unit 1 settles it in §8 by rung 1 and names an ask to dPlacedRequest in its return (the main loop files it).
- **D3 · `depends-on` (unit 6).** memory-plan `[edges]` spells build-to-build ordering `after` and has no `depends-on`
  row; the clause names `depends-on`. Unit 6 registers `depends-on` as the README-site spelling of the `after` edge
  type, not a new type, and says so in §8 (rung 1: the clause names the key, the plan names the type).
- **D4 · "no shared counter" (unit 3).** `memory/HYGIENE.md` line 182 says ids take "No reserve-above-a-marker, no
  shared counter"; cl-0214 mints ids for filers outside a build under an ask family's counter ref. Unit 3 rewrites
  that rule in `tools/memory-tree/HYGIENE.template.md` for filers outside a build only, keeps the per-session rule for
  builds, and cites the open ask PLAY-dClosedLoop-32 (an ask filed into another build's family) as the case its
  counter closes, naming it in `closes` only if its acceptance is fully met.
- **D5 · the atlas page budget (unit 26).** The clause splits "a page past its budget"; v2 carries `help.atlas` alone
  and the budget key `docs.atlas-page-budget` exists only at `research-final-atlas.md:106`. Unit 26 settles it by the
  rungs: a fixed budget constant in the renderer, stated in its spec, is the option that adds no policy key (veto 2);
  a new key is a departure.
- **D6 · the map cache path (unit 14).** `project-map.md:544` spells the cache `<git-common-dir>/gov/index/<tree>.map`,
  which collides with the index file `<git-common-dir>/gov/index.db`. Unit 14 caches at
  `<git-common-dir>/gov/map/<tree>.map`, still beside the index as the clause says; no deviation is owed for a path the
  clause does not spell.

## Shared interfaces — one spelling for every writer

Fixed so twenty-six specs by five writers agree on the interface axis (M2). A writer who finds one wrong says so in
its §8 as a fork and settles it there by the rungs; it never silently respells one. "Owned by" is the unit that specs
the interface; every other unit named reads it as written here.

- **I1 · the record-kind registry.** `tools/memory-tree/record-kinds.toml`, one `[[record-kind]]` row per kind, with
  the columns `name`, `tag`, `layer`, `home`, `id-rule`, `schema`, `writer`, `readers`, `lifecycle`, `check` in that
  order, `purpose` (unit 16) and per-edge `cardinality` (unit 22) after them. Node id `record-kind.<name>`; tag
  `record.<name>` (layer-memory.md:303). The file registers as ONE row of PLAY-dOrderedCharter-7 S4's
  `tools/playbook/kinds.toml`, so there is one register of kinds. Its conformance check is `check_record_kinds` in
  `tools/memory-tree/record_kinds.py`, its leg `record-kinds` in `tools/gate-legs.json`. `memory/HYGIENE.md` is
  rendered from it as a view through `adopt-memory-tree.sh --render`. Owned by unit 1; units 8, 11, 16, 18, 22, 25
  add a row or column; units 2, 7, 19 read it.
- **I2 · the `record` command.** The write door grows PLAY-dOrderedCharter-7 S7's factory
  `tools/memory-tree/build_records.py` rather than adding a third writer; its CLI is
  `tools/memory-tree/gov_record.py` with the verbs `new <kind>` (unit 2), `find` and `show` (unit 9), standing in
  for `gov record` as `gov_tag.py` stands in for `gov tag`. Never name a module `record.py`: it collides with
  `tools/runlog/record.py`. `--new-build` and `--new-spec` in `gen_build_index.py` forward to `gov_record.py new
  build-readme` and `new spec` (unit 20). Owned by unit 2.
- **I3 · the Serves kind vocabulary.** `tools/memory-tree/tree_lib.py:406` `RECORD_KIND_TOKENS` becomes
  `spec-audit diff-review log research deviation`, with `journal` a read-only retired alias read as `log`. No record
  is rewritten. Owned by unit 18; units 19 and 20 read it. Parent specs that write `**Serves:** journal`
  (TOOL-dPlacedRequest-2 S8, -7) keep working through the alias.
- **I4 · claim refs.** The slug claim is `refs/gov/claims/<slug>`, never pruned; an ask family's counter is
  `refs/gov/claims/asks/<FAMILY>-<slug>`, holding the last minted `<seq>`, advanced by a `--force-with-lease` push
  through TOOL-dPlacedRequest-11's `write_gov_ref`; each claim commit's message is the `gov-claim` key/value grammar
  of `tools/unattended/unattended.sh:2411` plus `claimant: <key>`. An unreachable remote follows
  TOOL-dPlacedRequest-1 S10's `leases.offline`. Owned by unit 3; units 2 and 6 read it.
- **I5 · header and edge lines.** `**Serves:**`, `**Made-by:**` and `**Caused-by:**` as `^\*\*Key:\*\* value$`
  (`Caused-by` is already spelled at `tools/memory-tree/deviation_join.py:147`), and a section's edge line
  `**Edges:** <type> <target>[ · <type> <target>…]` with the types of PLAY-dOrderedCharter-28's `edges.toml`. Owned by
  unit 19; unit 2 writes them through the door.
- **I6 · README front-matter schema.** `FRONT_MATTER_KEYS` in `tools/memory-tree/gen_build_index.py`: authored keys
  `slug opened ids parents may spec-audit authorized-by asks slug-grammar` plus the relation keys of I9; `node`,
  `roster` and `streams` derived and refused when typed; `status` refused once a spec exists (ask PLAY-dClosedLoop-31's
  case). Owned by unit 4; units 2, 6 and 20 read it.
- **I7 · the slug and id grammar.** `slug_grammar(root)` in PLAY-dOrderedCharter-18's
  `tools/memory-tree/id_grammar.py`, returning `words`, `style`, `date` and the derived `BUILD_SLUG_RE`, read by every
  slug and id reader; `check-memory-hygiene.sh --print-slug-re` exports it to shell. Each new slug records the
  grammar in force as the README key `slug-grammar: words=<n>-<m> style=<s> date=<d>`. Owned by unit 5; units 3, 4, 6
  and 2 read it.
- **I8 · the policy reader.** `read_policy_value(key, root, rev=None)` (PLAY-dOrderedCharter-19 S8), the key literal
  first, over dGroundRules' reader; each key a row in `tools/policy/catalogue.toml` owned by the unit the owned-node
  table names.
- **I9 · relation keys.** Front-matter keys `depends-on`, `patches`, `amends`, `supersedes`, `implements`, `parents`
  kept as an alias of `depends-on`; types registered in `tools/playbook/edges.toml`, `depends-on` as the README-site
  spelling of `after` (D3); a target on another node's branch is `pending` through the card, lease and claim refs.
  Owned by unit 6; unit 22 reads the types.
- **I10 · edge cardinality.** `cardinality = { per-source = "<n|many>", per-target = "<n|many>" }` declared on each
  `edges.toml` `[[edge]]` row and mirrored into I1's `cardinality` column; checked by `check_edge_cardinality` over
  the merged tree from `tools/run-gates/post-merge.sh`. Owned by unit 22.
- **I11 · the one index.** `<git-common-dir>/gov/index.db` (PLAY-dOrderedCharter-19 S4: `tree_path`,
  `blob_row(blob, extractor, tag, kind, line, end_line, text)`, `path_row`, `dirty_path`, `tree_built`), resolved by
  `tools/lib/common_dir.py`. This build adds tables to it through its `build_index`, never a second file: unit 8's
  `code_row` (definitions with ranges and body hash, imports, calls), unit 21's FTS5 tables. Read by units 9, 14, 15,
  23, 26.
- **I12 · extractor registration.** One `[[namespace]]` row in `tools/playbook/namespaces.toml` with
  `extractor = "<module>:<function>"` per extractor: `code` (unit 8); `section`, `record`, `feature`, `class` (unit
  9). Unit 14 adds the row field `map = "line" | "fold"`, read by units 15 and 26.
- **I13 · the extraction primitive.** `tools/lib/extract_code.py`, block marker `# >>> extract_code — canonical
  copy`, a `PARITY_ROWS` row `extract_code` in `tools/lib/resolve-python.test.sh`; entries
  `extract_text(src, mode, pset, *, sets=None)` (lexicon's signature) and `read_defs_at(root, state, paths=None,
  cache=None)` with `state` one of `worktree`, `index` or a revision. The shell and JavaScript tokenizers move into it
  from `tools/lexicon/lexicon.py`; the map and the lexicon each call it. Owned by unit 13; unit 8 reads it;
  dMindYourWords (cl-0273) must agree.
- **I14 · the FTS builder name.** `bench.build_index` (moved into `id_grammar.py` by PLAY-dOrderedCharter-18 S1) is
  re-spelled `build_fts_rows`, so `tag_index.build_index` stays the one index writer. Owned by unit 21; a departure
  from dOrderedCharter-18's spelling, recorded by unit 21.
- **I15 · the address and anchor grammar.** `record show <id>#<tag>[@blob]` (systems.md:518) over the tag grammar
  `TAG_RE` (PLAY-dOrderedCharter-19 S1). Derived anchors fold a heading by PLAY-dOrderedCharter-19 S3's rule, a
  repeated heading taking `-2`, `-3` in document order, in one function `derive_anchor(heading, seen)` in
  `tools/playbook/tag_index.py`. Owned by unit 10; units 9, 19 read it.
- **I16 · the memory slice cap.** One `[[cap]]` row with `class = "exempt"` in `tools/policy/caps.toml`
  (TOOL-dGroundRules-9 S1), keeping memory slices out of `budgets.enforce`'s refusal. Owned by unit 9.
- **I17 · the feed line.** TOOL-dPlacedRequest-13's six TAB-separated fields `seq ref kind blob commit seen-utc`; a
  record event is `kind = record`, `ref` the landed branch, `blob` the record file's blob. Owned by unit 24; unit 2's
  door appends through `add_feed_event` once the commit lands.
- **I18 · read channels.** `slice | read | shell`, a measure-only extension of runlog's `TOOL_CLASSES`
  (`tools/runlog/extract.py:95`). Owned by unit 12.
- **I19 · the map.** `tools/memory-tree/gov_map.py <ns>[.<seg>]` stands in for `gov map`; line grammar `line`,
  `nsline`, `header` (`project-map.md:551-562`); cache `<git-common-dir>/gov/map/<tree>.map` (D6). Owned by unit 14;
  units 15 and 26 read it. Leg pack key `"pack": "map"` in `tools/gate-legs.json` (unit 15).
- **I20 · the help root and the help-page renderer.** `{help_root}` in `tools/run-gates/regen.py` `TOKENS` and in
  `tools/unattended/lib-unattended.sh`'s `resolve_generated_indexes`; one help-page renderer shared with
  PLAY-dOrderedCharter-37's `help/reference/`, extracted rather than copied. Owned by unit 26.
- **I21 · the replay scorer.** `replay_scorer.py --instance map-replay`, a new instance of TOOL-dFairHearing-12's
  factory carrying the three losing terms. Owned by unit 17.
- **I22 · the legacy population.** `test.seed`'s `seed_population` (TOOL-dWitnessedBar-15 S1), keyed by record path
  and section, rather than a new per-kind cutoff key. Units 1 and 19 read it; V14's `ASK_CUTOFF` stays.

## Owned nodes

| Node | Unit |
|---|---|
| `system.memory-structure`, `record-kind.backlog-row`, `record-kind.design-record`, `record-kind.dossier` | 1 |
| `record-kind.claim` | 3 |
| `record-kind.build-readme`, `policy-key.builds.agent-root` | 4 |
| `policy-key.builds.slug-words`, `policy-key.builds.slug-style`, `policy-key.builds.slug-date` | 5 |
| `record-kind.ask`, `policy-key.asks.acceptance` | 7 |
| `record-kind.code`, `policy-key.memory.code-languages` | 8 |
| `tag-namespace.section`, `tag-namespace.record`, `tag-namespace.feature`, `tag-namespace.class`, `tag-namespace.marker`, `policy-key.memory.item-budget`, `policy-key.memory.load-budget`, `policy-key.memory.over-budget`, `policy-key.memory.superseded-slices` | 9 |
| `record-kind.shape-run` | 11 |
| `system.project-map`, `policy-key.memory.map-budget`, `policy-key.memory.map-overflow` | 14 |
| `policy-key.memory.map-purpose` | 16 |
| `record-kind.view`, `record-kind.registry`, `record-kind.archive`, `record-kind.instrument`, `record-kind.witness` | 18 |
| `policy-key.memory.legacy-anchors` | 19 |
| `record-kind.stream-plan` | 25 |
| `policy-key.help.atlas` | 26 |

Each node is one `**Carries:** node:<node>` line, one per line, in its unit's spec. Thirty-six nodes, each once.

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one. A writer who finds an edge false removes it from its
own spec and says so in its return.

| Producer → consumers | Token |
|---|---|
| 1 → 8, 18, 16, 25, 22, 2, 7, 11 | `record-kinds.toml` |
| 13 → 8 | `extract_code.py` |
| 18 → 19, 20 | `log` |
| 16 → 14 | `purpose` |
| 5 → 4, 6, 3 | `slug_grammar` |
| 4 → 6, 2, 20 | `FRONT_MATTER_KEYS` |
| 6 → 22 | `depends-on` |
| 3 → 2 | `refs/gov/claims/` |
| 2 → 7, 11, 19, 24, 20 | `gov_record.py` |
| 10 → 19, 9 | `derive_anchor` |
| 19 → 20 | `memory.legacy-anchors` |
| 21 → 9, 23 | `build_fts_rows` |
| 9 → 23, 12 | `record find` |
| 17 → 14 | `map-replay` |
| 14 → 15, 26 | `gov_map.py` |

## The units

**Writer groups and build order.** The `order` value is the build order: the registry before every kind that lands
a row in it, the extraction primitive before the code record that derives through it (D1), the registry's columns
before the grammar and schema that the minting door writes against, the claim refs before the door, the door
before every kind written through it, the anchors and the index rows before the extractors that read them, the
replay before the map it may stop, and the acceptance re-measure last, since it measures everything above. The
build harness (`tools/workflows/unattended-build.js`) splits the 26 orders into writer groups of six consecutive
orders and hands each writer its group; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 1 (1), 13 (2), 8 (3), 18 (4), 16 (5), 25 (6) |
| 2 | 5 (7), 4 (8), 6 (9), 22 (10), 3 (11), 2 (12) |
| 3 | 7 (13), 11 (14), 10 (15), 19 (16), 21 (17), 9 (18) |
| 4 | 23 (19), 24 (20), 20 (21), 17 (22), 14 (23), 15 (24) |
| 5 | 26 (25), 12 (26) |

Six Tier-2 specs is a long pass: keep each spec to what its clause and its shared interfaces need, cite the scout
record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **TOOL-dTotalRecall-1** — Items 1 (gap-mem-01). The registry I1 and its conformance gate, red on a planted kind row
  missing its writer and on a planted kind's schema removed with no row (joined to TOOL-dSafePassage-10's step gate);
  templates and checks generated from it and `HYGIENE.md`'s prose rendered as its view; today's kinds registered
  (scout A: `tree_lib.py` `RECORD_KINDS` and `RECORD_KIND_TOKENS`, runlog's `RECORD_SCHEMA`, `deviation_join.py`'s
  field table); dPlacedRequest's `probe` row joining it; gap keys as a native-id class (PLAY-dOrderedCharter-28 S2's
  `[[native]]` rows) with their resolution planted. D2 is settled here.
- **TOOL-dTotalRecall-13** — Items 13. The primitive I13: move `scan_shell_tokens`, `parse_shell_defs`,
  `scan_ts_tokens`, `parse_ts_defs`, `parse_ts_source`, `_python_defs`, `extract_text` and `read_defs_at_sha` out of
  `tools/lexicon/lexicon.py` (scout B), retire the map's `from lexicon import parse_shell_defs` and `map_lib`'s second
  tokenizer, and the drift-audit copy; reading the working tree, the index or a revision.
- **TOOL-dTotalRecall-8** — Items 8 (gap-mem-04, gap-mem-28). The `code` record over I11 and I13, its kind row in I1,
  its extractor in I12, `memory.code-languages` with `builtin+ctags` and `ctags` stopping on a missing ctags; inputs
  bounded as the clause lists; dossiers anchored to symbol keys; the re-timing D1.
- **TOOL-dTotalRecall-18** — Items 18 (gap-mem-37, gap-mem-38). Home, lifecycle, readers, layer on every I1 row;
  readers and writers rendered from the role definitions' `reads:` and `writes:` under a render-parity arm; witness
  rows for the pockets joined to a listing of the git common dir; the view, registry, archive, instrument and witness
  kinds; the `journal` → `log` rename I3 from the scout's inventory by value, every reader in its `**Readers:**`.
- **TOOL-dTotalRecall-16** — Items 16 (gap-mem-27). The `purpose` column on I1, today's kinds and the namespaces and
  chain builds dOrderedCharter-22 adds, reviewed as `memory.map-purpose` (`review`) says: derived with the source
  cited, else one owner ask per namespace, rendered `—` while pending (project-map.md:655-672).
- **TOOL-dTotalRecall-25** — Items 25. The stream-plan kind's I1 row and schema (streams, each an ordered unit list
  reusing `ORDER_RE`'s integer grammar), red on a planted plan whose stream has no order; the writer (dIndexedDesign's
  planner) and reader (Runtime's pick) named as later builds descending from the registration.
- **TOOL-dTotalRecall-5** — Items 5 (gap-mem-06). I7, extending `id_grammar.py`; `BUILD_SLUG_RE` derived; every
  reader the scout lists (about fifteen) re-pointed, found by the parser's own search; new mints only; the scratch
  clone flips (`slug-words` 1 and 3, `slug-style` `descriptive`, `slug-date` `shown` and `in-slug` in a digit and a
  hyphenated form) as its acceptance.
- **TOOL-dTotalRecall-4** — Items 4 (gap-mem-05, gap-mem-40). I6 with unknown keys refused; the routing region by
  purpose in `GEN_REGIONS`; the work order as each agent's root (`builds.agent-root`, `work-order`); a design-only
  build's `ids:` as nodes and the bindings check exempting it, red on a planted design-only row it still reports.
- **TOOL-dTotalRecall-6** — Items 6 (gap-mem-07). I9: parsing from `parse_front_matter`, inversion generalised from
  `plan()`'s `parents:` inversion, the graph rendered in `render_edges`' region, both-way checks, no `depends-on`
  cycle (red on a planted two-build cycle), pending on a planted target on another node's branch. D3.
- **TOOL-dTotalRecall-22** — Items 22 (gap-mem-42). I10, generalised from `asbuilt_view.py`'s `resolve_clause_rows`
  per-target rule rather than copied; red on two records superseding one decision on separate branches, merged clean.
- **TOOL-dTotalRecall-3** — Items 3 (gap-mem-13). I4 over `write_claim`'s CAS (`unattended.sh:2396`);
  `check_slug_claimed` kept as the local pre-check; red by a two-clone concurrent mint against today's local-only
  check; D4.
- **TOOL-dTotalRecall-2** — Items 2. I2: mints ids under the build's claim or lease (I4), idempotent and
  content-addressed (the content key `handoff.py`'s `derive_section_sha` shape), renders templates, refuses invalid
  values from I1's schemas.
- **TOOL-dTotalRecall-7** — Items 7. `asks.acceptance` (`refuse` default, `grade`): V14's predicate in
  `tools/memory-tree/backlog.py` lifted into one function the door and V14 both call; the ask kind's I1 row.
- **TOOL-dTotalRecall-11** — Items 11. The shape-run kind's I1 row, written through the door by parsing
  `renderShapeLine`'s `review-shape` line (`tools/workflows/tier2-review.template.js`), `SHAPE_RE` moving with it.
- **TOOL-dTotalRecall-10** — Items 10. I15's `derive_anchor` with the ordinal suffix; derived anchors not graded for
  uniqueness; a fixture over a record repeating an H2.
- **TOOL-dTotalRecall-19** — Items 19. I5 written by the door; the causes check and the orphan check over I22's
  legacy population; the README or its claim commit as root and `owner` or the build lease as Made-by until
  dWellOiledMachine's intake and binding kinds drain them; Serves lines read as `serves` edges and derived anchors for
  untagged headings as `memory.legacy-anchors` (`derived`) says; red on a planted causeless record and a planted
  orphan, today's tree green.
- **TOOL-dTotalRecall-21** — Items 21 (gap-mem-41). memory-recall's FTS5 tables into I11 keyed by blob, I14; retire
  `corpus_digest`, the per-worktree `cache_dir`, `ensure_cache`'s freshness clauses, `evict_dead_siblings`,
  `evict_over_budget`, `RECALL_CACHE_BUDGET_MB` and `query.common_git_dir`, each with its `**Readers:**`.
- **TOOL-dTotalRecall-9** — Items 9 (gap-mem-20, gap-mem-21). The four extractors in I12; `record find` reshaping
  `query.py` and taking over the `check-recall` leg, reading `memory/archive/` beside live records, its last line
  naming the total past 40 rows; `record show` over I11; section tags per kind; `memory.item-budget`,
  `memory.over-budget` (I16), `memory.superseded-slices` red on a superseded decision handed to a builder; the load
  share under `memory.load-budget` reported at session start, naming PLAY-dOrderedCharter-14 S2-S4 for the card and
  the promotion through `instructions.edit` rather than re-speccing them. The largest clause: keep it whole and terse.
- **TOOL-dTotalRecall-23** — Items 23 (gap-mem-43). `tree_lib.read_blobs_at` and `read_text` extended with an index
  row read for unchanged blobs; an index read and a full read agreeing on a planted tree.
- **TOOL-dTotalRecall-24** — Items 24. I17: `scan_feed_writers` and `check_feed` (TOOL-dPlacedRequest-13 S6/S9)
  extended to commits that touch record paths; red on a planted record write that skips the append and on a
  hand-committed record the live feed lacks; an uncommitted write never in the feed.
- **TOOL-dTotalRecall-20** — Items 20. Its `[[upgrade]]` rows in `tools/memory-tree/kit.toml`: the `journal` alias,
  `--new-build` and `--new-spec` forwarded to I2 by dSafePassage's shim, an adopter's front matter graded against I6
  before unknown keys are refused, and the retag step under `memory.legacy-anchors: retag` modelled on
  `migrate_backlog.py`'s plan/dry-run/write, seen on a planted adopter record.
- **TOOL-dTotalRecall-17** — Items 17. The replay with the map and without, through I21, at the base commits the
  clause names; the three losing terms; a loss routed as the clause says. It runs before unit 14's code: a losing map
  is never built.
- **TOOL-dTotalRecall-14** — Items 14 (gap-mem-26, gap-mem-30, gap-design-01). I19 derived from I11, at most
  `memory.map-budget` (`32k`), degraded in the fixed order or refused as `memory.map-overflow` says, never dropping a
  node; port the instrument's `line`, `render` and `fit`; D6; the `code` line budgeted (v2's map-headroom `[owed]`).
- **TOOL-dTotalRecall-15** — Items 15. The three-way completeness check, index ↔ map ↔ disk, over
  `compute_coverage`'s census; the `map` leg pack; the `[checks]` table's planted reds.
- **TOOL-dTotalRecall-26** — Items 26 (gap-mem-48). `help/atlas/` under `help.atlas` (`committed`): Mermaid pages per
  namespace and the plan per build from I11's node table, never the design records; a `[[generated]]` row at stage 3;
  I20; byte comparison and parity read-back; split by segment past its budget (D5); the design-against-built page;
  the link check; the four planted reds the clause lists.
- **TOOL-dTotalRecall-12** — Items 12. The re-measure over I18's three channels, passing only if thirty days after
  landing the median memory bytes per memory-reading agent are below 33 KB; the slice channel's producer named as a
  later build's.
