**Serves:** research PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23

# Spec brief — dConvergedCharter, the twenty-three convergence units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Owned nodes, Gaps, Policy keys and Obligations sections bind every unit.
2. The build README, `memory/builds/dConvergedCharter/README.md`: its build-level rules bind every spec, the fork rule
   above all. Its `BACKLOG.md` holds ask PLAY-dConvergedCharter-24, which the LAST unit in build order (unit 18) names
   in its header's `closes`; every other unit's header says `advances PLAY-dConvergedCharter-24`.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5, M12. Every unit is Tier 2: each changes the
   governance template's rules, a kit's contract, or several kits at once (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every row of "Shared interfaces" and "Edges", and the scout record your units
   cite, under `memory/builds/dConvergedCharter/build/`: `2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md`
   (units 1, 2, 3, 4, 13, 19), `-6-reuse-scout-b.md` (6, 7, 8, 9, 10, 15), `-11-reuse-scout-c.md` (11, 12, 16, 17, 20,
   21, 22) and `-5-reuse-scout-d.md` (5, 14, 18, 23). Each holds a seam row per clause with path:line at `0d1c1dda4`,
   and a section on where a record and source disagree. Those disagreements are findings you act on.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (this build's `[chain]` row is v2:1785; grep your clause id;
`[policies]` v2:1126-1134 and v2:1295; `[owed]` v2:2006), the gap register
`B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` (each gap the packet's Gaps section names, by line), the fates
record `B/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`, the night pass `B/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`
(points 1, 4, 8), night pass two `B/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md` (point 7), the memory plan
`B/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md` (`[cycle]`), the flow adoption
`B/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md` (FA-1, FA-6, SK-1, SK-2), the final questions
`B/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md` (FQ-5, FQ-6), and the fork rungs in
`B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 36-61 and 900-946. Glob a name you cannot find by
its tail (`ls B/*fates.md`). You never edit an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-<n>.md`; H1
  `# PLAY-dConvergedCharter-<n> — <title>`, an EM DASH, never a colon.
- Status header `**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order <k> ·
  advances PLAY-dConvergedCharter-24`, with `<k>` your unit's order below (unit 18 writes
  `closes PLAY-dConvergedCharter-24` in place of `advances`). `OPEN` is the status token: `DRAFT` is not in
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py`). A landed precedent of the whole shape is any spec under
  `memory/builds/dMindYourWords/spec/` (line 3 for the header).
- Binding lines, each at column 0 on a line of its own under the status line:
  `**Carries:** <Items id>@<hash8> whole`, and for unit 7 alone `**Carries:** node:policy-key.help.explanation`. A unit
  carrying a clause in parts writes `part <k>/<n>` instead of `whole`, and every part is carried by a spec of this
  build: never split a clause without saying so in your return.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks. A clause the
  token arm cannot see (Items 1-6, 10, 13, 19, 20, 22) still names its key words in backticks where they are code.
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in §7, and the
  main loop observes it at the close. A policy key's non-default value is seen by a planted `.governance/policy.toml`
  naming that value; each allowed value of `help.explanation` is a planted case of unit 7.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
  The seams in the scout records are a reading at `0d1c1dda4`: verify each line number before citing it. Record each
  candidate you rejected and the test that rejected it (M12), under `### Alternatives rejected`.
- §8 forks: settle each by the README's rungs (the execution plan lines 36-61 and 900-946), in the §8 mark shape
  `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and
  carries `widens:` and `relaxes:`, each a value or `none`, ON THE SAME LINE as the ruling; a `relaxes:` value joins a
  record with `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a
  choice the README's `may: PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave
  an open question: a FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md`, `memory/HYGIENE.md` and
  `memory/TEMPLATE-SPEC.md` from their kit templates, `tools/workflows/*.js` from their `.template.js`,
  `tools/gate-legs.json` from the kits' `[[gate_leg]]` declarations, the installed Skills under `.claude/skills/` from
  each kit's `SKILL.template.md`, and the installed kickoff skill from `skills/session-kickoff/`: name the source as the
  edit and the render as its copy.
- A parent's surface is specced and NOT built unless the next section says it is built. Cite the parent's spec by id
  and section as the interface and name the call you make; never re-spec it, never add a copy of it. Where your unit
  cannot run until it lands, say so in §2 as a build-run precondition, and where the clause names a stand-in, spec the
  stand-in and register it as a `[[stand-in]]` row (TOOL-dDeclaredLoop-13 S8).
- `help.explanation` already has its catalogue row in `tools/policy/catalogue.toml` (`:998-1001`, owner
  dConvergedCharter) and its name in `tools/policy/unsummarised-keys.txt` (`:72`): unit 7 fills the row's missing
  summary and usage, drains the name with `policy.py lists --write`, and never adds a second row; its allowed values
  and default are that row's, verbatim. Once every unit is terminal the policy kit's reader-coverage arm reds the key
  if no literal call reads it, so unit 7 names that literal reader in its acceptance.
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-<n>-deviation-<k>.md`, in
  the grammar `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README rule 5). Do not commit it.
- A parent spec, or a spec of another build, that must change for your clause to hold is never edited: state the
  needed change in §8 as an ask for that build, its target build and its accept line, and your return names it. The
  main loop files every such ask once, after the writers return, so no two writers mint an id in one foreign family
  (PLAY-dClosedLoop-32).
- Write nothing outside `memory/builds/dConvergedCharter/spec/` and `memory/builds/dConvergedCharter/build/`; temp files
  go under the scratch path your harness names.

### What the last spec runs had to fix after their writers returned — do it first time

- **Paths in acceptance criteria.** `tools/check-spec-tokens.py` reds a path a criterion names that does not exist at
  HEAD. In §6 cite a file this build or a parent will CREATE by its basename (`python fates_join.py …`) and keep its
  full path in §2, §4 and Files touched. A command that reads a file takes it as an argument rather than spelling it
  inside a quoted literal.
- **Hand-off tokens.** A name your §3 hands off to a sibling unit appears, in backticks, in that sibling's spec where
  it reads it. When you hand off to a unit another writer owns, name the token exactly as "Shared interfaces" spells
  it, and that writer names it too.
- **§3 edges are reciprocal and follow the build order.** Every `hands-off` you declare to a unit is a
  `consumes-from` that unit declares back, naming the same token, and the reverse; hygiene check 12 reds a one-sided
  edge and an edge to a unit whose `order` is earlier than yours. The table under "Edges" is the set to declare; add
  an edge only when your spec truly reads or produces it, and say so in your return so the other writer adds the
  reverse.
- **Retiring a named thing** (a conf key, a leg, a function, a file, a Skill, a sentence a fixture asserts) owes a
  `**Readers:**` clause naming every reader by path and by value (hygiene check 25), each found by `git grep` over the
  tree. Check 25 reads any retirement word ("drops", "retired", "replaces") beside a backticked token in §2: use one
  only where you mean it. Units 2, 3, 4, 7, 8, 9, 11, 12, 15, 16, 17, 19, 20 and 21 retire named things.
- **No link-shaped text**, a bracketed label followed by a parenthesised target, anywhere outside a real link,
  backticks included (hygiene check 2).
- **A §8 mark wraps whole.** `deviations.py` reads a `RESOLVED` mark's ruling, `widens:` and `relaxes:` from the mark
  itself: keep each mark one paragraph, with no list or blank line inside it, and `widens:` and `relaxes:` on one line.
- **Size.** A spec stays under 49152 bytes; keep each to what its clause and its shared interfaces need.
- **A cited id leading a table cell defines it** (hygiene check 13): cite a foreign id inside prose, never as the
  first token of a table cell.
- **An acceptance criterion's ledger token** is written in backticks before the line first wraps (check 23).
- **Names you introduce** (a function, a module, a CLI mode, a conf block) are asked of the lexicon first:
  `python tools/lexicon/lexicon.py --suggest <name> --as <cell>`. A spec proposing a name the gate refuses hands the
  builder a red.
- You may run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` over your specs (your role admits the
  hygiene gate and the lexicon, no other); a red it prints on your files is yours to fix. The main loop runs
  `check-spec-tokens.py` and `carries.py --report dConvergedCharter` after every writer returns.

## The parents are specced, not built — with two exceptions

**Built at HEAD (CLOSED), and the scouts' rows correct the packet here:** dGroundRules and dSafePassage. So these are
live code you extend, never re-spec: the policy reader `policy.py get`/`resolve` (`tools/policy/policy.py`), the
catalogue and its lists (`catalogue.toml`, `legacy-homes.txt`, `unsummarised-keys.txt`, `derive_legacy_homes`), the
checker `tools/policy/check_policy.py` (`READER_SHAPES`, `scan_reader_keys`), `policy-shim.sh`, the upgrade-step kind
`tools/govkit/upgrade_steps.py` (`STEP_KEYS`, `RETIRED_KEYS`, `read_retired`, `derive_pending_steps`, `run_step_walk`),
`tools/govkit/steps.toml`, `tools/govkit/shims.py` and `shims.toml` (`KINDS = ("command", "hook", "module")`),
`step_gate.py`, `upgrade_walk.py`, the existing conf-to-policy step `tools/govkit/steps/fanout_cap.py`, the docs leg
`tools/govkit/docs_leg.py`, and `govkit.read_policy_value`. Also live: dTrueNorth's `design_lib.py` and
`check-spec-tokens.py`, the lexicon, the drift audit, `.githooks/` and `tools/run-gates/`.

**Specced and DEFERRED — the interfaces you call, by spec id and section** (the scout rows carry the detail):
- dOrderedCharter: `documents.toml` envelopes (PLAY-dOrderedCharter-3 S1, S6); facts-only `check_statement` and
  `check_document` (-12 S2, S3); units `[[unit]]` in `tools/<kit>/instructions.toml` with the `help` field (-9 S1);
  the write path `instructions.edit` (-15); the one renderer, its scopes and `renderers.toml` `[[target]]`, the slot
  line `<!-- units: <selector> -->` and the legacy list `tools/playbook/instructions-legacy.txt` (-20 S4-S8); tags,
  `doc.<name>#<seg>` and `aliases.toml` (-19 S3, S11); the positional arm and `positional-refs.txt` (-26 S2-S5);
  `[[drive]]` rows (-6 S1); `kind.skill` and its conformance gate (-7 S4-S6); `edges.toml` (-24 S1-S5); tag slices
  `tag_bundle.py` (-25); `rationale-apart` (-29 S6, S8); `references.toml` and `help/reference/` (-37); the overlay
  `.governance/instructions.toml` (-31 S4, -35).
- dTotalRecall: the record-kind registry and factory `record-kinds.toml`, `record_kinds.py new|--check|--population|--template`
  (TOOL-dTotalRecall-1 S1-S9), readers and lifecycle (-18), the alias step (-20), `derive_anchor` (-10), `extract_section`
  (-9), the change feed (-24).
- dWellOiledMachine: the driver and supervisor (TOOL-dWellOiledMachine-25, -28: `/build` and `/unattended` become clients
  of `run`), `gov why` and `gov trace` (-34 S2, S5), intake (-4, -27).
- dShippedRelease: adopters (DEPL-dShippedRelease-31 S2 `read_adopter_rows`; -7 S7 `adopter_reading.py read` and its
  `steps-pending`; -16 `kits.offer`), the release route (-15 S10), the kit wiring leg (-10 S6, S9, S10), the runbook scope
  (-9), house proposals and rulings (-28 S2, S3, key `<source>#<name>`).
- dBoundRoles: `read_policy_setting` and the role `gates` field (TOOL-dBoundRoles-21 S1, S3, S6, S7; -19; -2; -23).
- dCalibratedLens: the loop review's proposers, route and `keep` record (TOOL-dCalibratedLens-3 S7, -5 S6-S8, -14 S8).
- dTendedCadence: Maintain's filing (TOOL-dTendedCadence-8 S6-S7, -15 S2). dFurnishedOrders: the orientation scout
  (TOOL-dFurnishedOrders-1). dRankedPlan: `kickoff.runs` (TOOL-dRankedPlan-8; the scouts found it is not dScopedBuild's).
  dLinkedLibrary: the dossier mover (TOOL-dLinkedLibrary-19 S3), the `feature` selector (-20), edges (-17, -22).
  dWitnessedBar: the line-ending class (TOOL-dWitnessedBar-24 S2), `leg.adopter.*` (-28). dDeclaredLoop: loop items
  (TOOL-dDeclaredLoop-11, -12), `[[command]]` rows (-18), trailers (-23). dPlacedRequest: request keys (-19).

None of the DEFERRED files exists at HEAD. Where your unit needs one, say so in §2 as a build-run precondition, and route
anything else by the rungs, never by assuming it lands first. Where a scout found that a design record, a parent spec or
source disagree, v2's clause governs; a parent spec it contradicts gets an ask (the rule above), never an edit. Where the
clause itself names something source shows wrong (a reader that does not read, a hole of another name), the spec says
what source shows, carries the clause's intent, and writes a deviation record naming the difference.

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.help.explanation` | 7 |

Every other unit owns no node; each still names the nodes it reads, in prose.

## Shared interfaces — one spelling for every writer

Fixed so twenty-three specs by six writers agree on the interface axis (M2). Each row names its owner, the unit whose
spec defines it; every other unit names it exactly as spelled here and cites the owner. A spelling marked "proposed"
has no source yet; the owner may refine it in its spec, and says so in its return. A writer who finds one wrong says so
in its return and writes a deviation record rather than a second spelling. Every new name is asked of `--suggest` first.

| # | Interface | Spelling | Owner | Source |
|---|---|---|---|---|
| I1 | The reader inventory | one function `derive_readers(repo, needle, kind)` with `kind` `path` or `value`, beside `scan_reader_keys` in `tools/policy/check_policy.py`, reusing its exclusions; its output is the spec's `**Readers:** by name: <path:line>…; by value: <path:line>…` clause (TOOL-dWellOiledMachine-28 S1, S4, S7 spell it) and the build run's red arm on a surviving reader (proposed) | 11 | scout C interface 1 |
| I2 | The succession row | `[[retired]]` in `tools/govkit/registry.toml` with `id`, `successor` (or `"none"`), `surfaces`; its commit derived, never typed; read by `read_retired` | live | `registry.toml:190-195`, `upgrade_steps.py:144` |
| I3 | The forwarder | a `[[shim]]` row in `tools/govkit/shims.toml` (`id`, `kind`, `from`, `to`, `closed`), closed only under `install.deprecation-window`; `KINDS` in `shims.py` gains `skill`, so a Skill rename or retirement forwards through one row kind and never a hand-written stub (proposed) | 17 | scout C interface 3; scout B finding 8 |
| I4 | The shell policy read | `policy.py get <key> --rev <sha>` under the inline `resolve_kit_dir`, as `.githooks/pre-push` already calls it for `platforms.provision`; the four `read_policy_key` copies re-point to it, and their byte-identity comments and parity tests move with them (proposed) | 11 | scout C row 11, interface 5 |
| I5 | The folded key names | the catalogue's dotted lower-kebab form (`runtime.agents-in-flight`), each folded key's row carrying a `legacy` field `<home> <KEY>`, so the both-homes reader and the red arm read one map; `tools/policy/legacy-homes.txt` shrinks by `policy.py lists --write` only (proposed) | 11 | scout C interface 9 |
| I6 | The conf-to-policy step factory | one generic step module extracted from `tools/govkit/steps/fanout_cap.py` (the first instance) over (conf, key, policy key, legacy reader), step ids `<entry>/<slug>` as `agent-cap/fanout-cap-to-agents-in-flight` spells them; `fanout_cap.py` becomes its first caller (proposed) | 20 | scout C interface 4 |
| I7 | The adopter reading | `read_adopter_rows(root)` and its `registered` flag (DEPL-dShippedRelease-31 S2), `adopter_reading.py read --key <k>` and its `steps-pending` field (DEPL-dShippedRelease-7 S7) | parent | scout D interface 6 |
| I8 | The ruling key | `<source>#<name>` and one `ruling` record per key, a decline read as a drop (DEPL-dShippedRelease-28 S2, S3) | parent | scout C interface 8 |
| I9 | The key hash | `derive_key_hash(kind, key) -> str`, the first 16 hex of SHA-256 over `"<kind>\t<key>"`, moved to `tools/lib/key_hash.py` from its three copies (inline `drift_report.py:3777`, TOOL-dTendedCadence-15 S2, TOOL-dCalibratedLens-5 S8, which already spells the name); copy-installed kits carry it inline (proposed) | 23 | scout D interface 1 |
| I10 | The release ask's offender key | `<40-hex sha> <E>`, space-separated; the one rendered text `maintain key <hash> · release-verify-failed over its pin · <sha> <E>`, which `release.route` files too (proposed) | 23 | scout D interface 2, disagreement 6 |
| I11 | The record-kind factory | `record_kinds.py new <name> --tag --writer --check --field`, `--population`, `--template`, leg `record-kinds` (TOOL-dTotalRecall-1 S3, S5, S7, S9) | parent | scout B row 6 |
| I12 | The section address | `doc.<name>#<seg>`, `<seg>` from `derive_anchor` (TOOL-dTotalRecall-10 S1); the authored heading `## [section.<seg>] <Title>` honoured by the doc extractor through `extract_section`'s rule, never a third fold (the extractor change is an ask on dOrderedCharter) | 19 | scout A interfaces 1-2, disagreements 1-2 |
| I13 | The alias row and the positional list | `[[alias]] ref = "<doc> <label>" target = "doc.<name>#<seg>"` in `tools/playbook/aliases.toml`; `tools/playbook/positional-refs.txt` rows `<path>\t<ref>` under `tags.positional`, drained, never a second inventory (PLAY-dOrderedCharter-19 S11, -26 S2-S3) | parent | scout A interfaces 3-4 |
| I14 | The line-ending class lines | `*.<ext> text eol=lf` in `.gitattributes` (TOOL-dWitnessedBar-24 S2's class) and the kits' `[[lf_pin]] pattern = …` rows retired into them; what is outside the class (`memory/**/*.md`, the rendered `SKILL.md` rows, the root confs) decided in unit 19's §8 (scout A disagreement 5) | 19 | `.gitattributes:5`, `tools/memory-tree/kit.toml` |
| I15 | The unit row | `[[unit]]` in `tools/<kit>/instructions.toml` (`tag`, `level`, `type`, `scope`, `help`, `edges`), written only through `instructions.edit`; a feature unit scoped `feature.<name>` (PLAY-dOrderedCharter-9 S1, -15; TOOL-dLinkedLibrary-20 S2) | parent | scout A interfaces 5-6 |
| I16 | The prose mover | one `plan` then `apply` verb (a second `apply` writes nothing) extracted from TOOL-dLinkedLibrary-19 S3's `dossier_move.py`, the second instance; units 1 and 7 call it (proposed) | 13 | scout A interface 10 |
| I17 | The legacy list | `tools/playbook/instructions-legacy.txt` under `instructions.legacy` (PLAY-dOrderedCharter-20 S8): units 13, 1, 10, 7 and 9 drain it, and unit 8 retires a renderer only when its last row leaves | parent | scout A, scout B |
| I18 | The renderer scopes | `--render-scope <scope>` and `--check-render --scope <scope>` (PLAY-dOrderedCharter-20 S5), each scope a `[[target]]` row (`paths`, `renderer`, `region`) in `tools/playbook/renderers.toml`; new scopes `protocols` and `skills` (unit 10), `explanation` (unit 7), `readme` (unit 15) (proposed) | 10 | scout B interface 5 |
| I19 | The Skill's command row | `[[drive]]` (`stage`, `role`, `command`, `when`) gaining `skill = "gov-<name>"`; the entry's description rendered `Use when <when>, runs <command>.` by the `skills` scope (proposed) | 10 | scout B interface 7 |
| I20 | The Skill names and the prefix gate | `gov-recall`, `gov-runlog`, `gov-lexicon`, `gov-drift`, `gov-cleanup` (v2:586); `kind.skill`'s population widened to `.claude/skills/*/SKILL.md`, with an arm refusing a gov-rendered Skill without the `gov-` prefix | 9 | scout B interfaces 8-9, finding 7 |
| I21 | The explanation tree | `help/why/`, rendered from each unit's `help` field when `help.explanation` is `rendered` and absent under `registry-only`; outside `help/reference/`, outside `documents.toml` and every load set; read through `govkit.read_policy_value`; the no-lost-rationale arm keyed by a unit edge `explains=<guide path>#<seg>` (the edge type is minted in unit 7's §8, an ask on dOrderedCharter's `edges.toml`) (proposed) | 7 | scout B interfaces 1-4 |
| I22 | The fates table | `tools/govkit/fates.toml`, gov-internal; rows `[[part]]` with `id = "<kit>/<function-slug>"`, `kit`, `function`, `fate`, `where`, `decided`, `paths = [...]` (globs resolved as `surface_paths` reads them); fates the record's `[table]` four plus `KEPT`; materialized from the fates record's `[table]`, which every earlier unit cites by (Kit, Function) until unit 14 lands (proposed) | 14 | scout D interface 3, disagreements 3-4 |
| I23 | The convergence population | `tracked(root)` (`govkit.py:344`) over `tools`, `skills`, `.githooks`, `.claude`, `.github`, `help`, `WIRE-INTO-PROJECT.md` and `coding-governance-agents.template.md`, plus every path a fates row names outside them; unit 20's adopter exit check runs beside it, never as a second population | 14 | scout D interface 4 |
| I24 | The proposal and its decline | the `{"kind","id","action","accept","row"}` shape and one proposer added to `PROPOSERS` (TOOL-dCalibratedLens-3 S7, -5 S6); a decline is the `keep` record keyed `(kind, id)` (-5 S8), no new kind | 4 | scout A interface 9; scout D interface 5 |
| I25 | The cycle's edge types | the `type` column of `tools/playbook/edges.toml` (PLAY-dOrderedCharter-24 S1), as memory-plan `[cycle]` spells them; each hop names its type and the unit that types it (scout D's hop list) | parent | scout D interface 7 |

## Edges — the §3 pairs every spec declares

Each row is one `hands-off` the producer declares and the `consumes-from` each consumer declares back, naming the
token. Every edge runs from an earlier `order` to a later one.

| Producer → consumers | Token |
|---|---|
| 11 → 17, 12, 16, 21 | `derive_readers` |
| 11 → 20 | `legacy-homes.txt` |
| 17 → 16, 9 | `KINDS` |
| 12 → 20, 2 | `tools/unattended/` |
| 5 → 20 | `steps-pending` |
| 20 → 21 | `fanout_cap.py` |
| 20 → 14 | `derive_pending_steps` |
| 23 → 14 | `derive_key_hash` |
| 6 → 3, 7 | `record_kinds.py` |
| 19 → 2 | `aliases.toml` |
| 19 → 13, 7 | `extract_section` |
| 19 → 9 | `.gitattributes` |
| 13 → 1, 7 | `dossier_move.py` |
| 1 → 7 | `instructions-legacy.txt` |
| 10 → 7, 9, 8 | `renderers.toml` |
| 7 → 15 | `help/why/` |
| 7 → 8 | `help.explanation` |
| 4 → 14 | `keep` |

## The units

**Writer groups and build order.** The `order` value is the build order. The census first, since it changes nothing
and gives the owner the populations every later unit rules over; the conf fold, whose reader inventory every
retirement uses; the three retirements of a driver (`/build`, the unattended kit, `/session-kickoff`); adopter
migration, then the upgrade steps that ship the fold and the retirements and whose exit check reads that migration, then
the house seed through the same step factory; the key hash and the release join; records (the kind sweep, then the
merges); tags (the guide anchors and class pins, then the remaining positional references, after the unattended code
they would otherwise migrate is gone); prose (feature prose into units, then the facts-only residue); rendering (the
scopes, the explanation tree, the Skills, the renderers retired with their last documents, the help pages); and the
supersession proposer, the fates exit check and the cycle walk last, because each grades everything above. The harness
splits the 23 orders into six writer groups of consecutive orders; author every unit of your group, in order, and
nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 22 (1), 11 (2), 17 (3), 12 (4) |
| 2 | 16 (5), 5 (6), 20 (7), 21 (8) |
| 3 | 23 (9), 6 (10), 3 (11), 19 (12) |
| 4 | 2 (13), 13 (14), 1 (15), 10 (16) |
| 5 | 7 (17), 9 (18), 8 (19), 15 (20) |
| 6 | 4 (21), 14 (22), 18 (23) |

Cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **PLAY-dConvergedCharter-22** — Items 22 (gap-found-32; IA-6, FA-1). Order 1. The census read: the legs no descriptor
  declares (scout C finding 10: 148 legs, 69 `[[gate_leg]]` rows, 79 `[[exempt_leg]]` rows, so the undeclared set is
  the exempt set `govkit.py:2655-2690` walks), gov's efforts and grants (the house file through `load_policy`), and its
  run conf and gate environment values (`derive_legacy_homes` rows for `.unattended.conf` and `.githooks/gate-env.sh`,
  with their `owner-policy`/`mechanic` marks). Each population rendered as owner items under I8's ruling key, each ruled
  by the owner; the gov-only ones moved to gov's own overlay `.governance/instructions.toml` and policy file only after
  the overlay (PLAY-dOrderedCharter-31, -35), `leg.adopter.*` (TOOL-dWitnessedBar-28) and unit 12 land (a build-run
  precondition), and the run conf's extension keys retired with the unattended kit (unit 12's write, cited here). An
  owner who has not ruled leaves the row as it is: say how the census reports that. Seen red: a planted leg no
  descriptor declares and no exempt row covers.
- **PLAY-dConvergedCharter-11** — Items 11 (RC-3, M7, DA-H5, DA-M6, FA-6). Order 2. I1, I4, I5. Every conf key the
  retrofit does not convert folded into `.governance/policy.toml` with a catalogue row; the reader inventory by key value
  (I1), red on a reader of a folded key still reading its old home, added as a `READER_SHAPES` row; the named readers re-
  pointed: `transition_audit.read_modes` reading both homes keyed by commit (`read_legacy_fanout` and
  `derive_lowered_limit`, `policy.py:767-800`, are the precedent), govkit's conf-key gap checks, kit.toml's `*_keys`, the
  kit-placeholders leg, the four `read_policy_key` copies with their callers, comments and parity tests (scout C finding
  5), and `held_halves.py`, which reads `gate-env.sh` from the working tree (finding 7: only `GATE_WSL_PARITY_RUNS`
  folds). `tools/policy/README.md:212-219`'s "stay as they are" sentence amended. The scratch-clone proof plants
  `park` (gov's value is `land`, finding 6) and sees `.githooks/pre-push --decide` read `land` before the re-point and
  `park` after. The `[effort]` and `[gates]` half waits on TOOL-dBoundRoles-21 (finding 3: the readers are NOT on
  `roles.effort.*` at HEAD); state it as a build-run precondition and write the deviation the clause's "already on"
  claim owes. Seen red: a planted reader still reading the house file, and a planted reader of a folded key reading its
  old home.
- **PLAY-dConvergedCharter-17** — Items 17 (SK-1). Order 3. I2, I3. `/build` retired once TOOL-dWellOiledMachine-25's
  supervisor drives attended builds (precondition): the first `[[retired]]` row this build writes, its readers by
  value through I1 (charter template `:140`, the kickoff card `skills/session-kickoff/SKILL.md:210`, the roles kit's
  `SKILL.template.md`, `adopt-roles.sh`, `kit.toml` install row and probe, the harness wiring), the kept client
  forwarded by a `skill` shim (I3, which this unit adds to `KINDS`) for `install.deprecation-window` releases, then
  removed. Seen red: a planted reader of `/build` surviving the removal on a scratch clone.
- **PLAY-dConvergedCharter-12** — Items 12 (night pass point 1; gap-tool-08). Order 4. I1, I2. The unattended kit, its
  four guides and `/unattended` retired once dWellOiledMachine's driver carries every run (TOOL-dWellOiledMachine-25 and
  -28 preconditions) and after unit 11 (the kit holds a `read_policy_key` copy and run conf keys): every reader by path
  and by value (scout C's 35 files, the gate legs, `tools/template-size-limits.txt`, the `[[exempt_leg]]` rows,
  `tools/policy/caps.toml`, `fork-ceilings.txt`, `method-carriers.txt`, `README.md:57-60`, `.claude/rules/product.md`'s
  "four-verb driver", the charter's protocol line and its renders, `AGENTS.md`), each re-pointed or retired with it;
  the `[[retired]]` row; the spawn-budget leg run on a scratch clone with `tools/unattended/` removed. This build's own
  run is driven by the kit it retires: say how the build run lands this unit last within its own dispatch, or what it
  runs under. Seen red: the scratch clone with a surviving path reader.
- **PLAY-dConvergedCharter-16** — Items 16 (SA-9; gap-orient-21). Order 5. I1, I2, reads I3. `/session-kickoff`
  retired once TOOL-dFurnishedOrders-1 and TOOL-dRankedPlan-8 land (preconditions; scout C finding 2 corrects the
  clause's attribution): `manifest-check.sh` and its fragments moved to a kit home of their own (the entry
  `tools/govkit/entries/kickoff-manifest.kit.toml` is the obvious owner) with readers re-pointed before the directory
  goes, the readers the clause lists (the charter's two lines, the write gate's refusal text in `scratch-guard.js`,
  `memory/guides/SESSION-KICKOFF.md`, the junction rule, the runbook's link step, the two hooks in
  `.claude/settings.json`, the leg rows, the kit entry, the registry glob, check-wiring's link arm), the forwarding stub
  as a `skill` shim row, then the directory removed. The node preflight's dangling-link report extends
  `check_skill_install` (`tools/check-wiring.sh:1887`), which today returns skip or UNWIRED for a missing target and so
  never reports a dangling link (finding 8). Seen red: the removal on a scratch clone where a path reader survives, and a
  planted node whose link targets a removed directory.
- **PLAY-dConvergedCharter-5** — Items 5. Order 6. I7. Adopters migrated onto the ranked charter and the loop by
  driving the walk that exists (`cmd_update`, `derive_pending_steps`, `run_step_walk`), never new engine code; each
  parent's own steps are the content (PLAY-dOrderedCharter-31 S4, TOOL-dBoundRoles-19, TOOL-dTotalRecall-20, the loop
  kit's). `tools/govkit/adopters.toml` holds three rows with no remote, branch or grant, so none is `registered`
  (scout D row 5): the owner registers each adopter, and the spec says what the unit does with an unregistered row
  under the rungs. Preconditions: DEPL-dShippedRelease-31, -7, -16, -25. Seen red: a planted adopter with a step pending
  read as not migrated.
- **PLAY-dConvergedCharter-20** — Items 20 (P38). Order 7. I6, reads I7. The conf fold (unit 11) and the unattended
  kit's retirement (unit 12) shipped as upgrade steps through the factory I6 extracted from `fanout_cap.py`, every
  shim (units 16 and 17's, and its own) removed when its window closes, and the exit check widened: every registered
  adopter at the converged commit with no step pending, or an owner item for that adopter. Preconditions for the exit
  check: DEPL-dShippedRelease-31 and -7. Seen red: a planted adopter with a pending step and no owner item, and a shim
  whose window closed left standing.
- **PLAY-dConvergedCharter-21** — Items 21 (FA-6, P38; gap-roles-26). Order 8. I6, I8. `tools/roles/house/policy.toml`
  retired as a seed: a repository's efforts folded into `roles.effort.*` (`catalogue.toml:296-308`), only those the owner
  has not ruled on through `adopt.declarations` (DEPL-dShippedRelease-28 S2, S3), a declined proposal read as a drop;
  `default` into `roles.effort.default`; `[gates]` into each role definition's gate grant (TOOL-dBoundRoles-21 S6); gov's
  defaults shipped in the role definitions; the readers (`check_roles.py:367`, `handoff.py:480`, `render_agents.py:140`)
  losing the house-file fallback TOOL-dBoundRoles-21 §4 step 4 adds; shipped as an upgrade step through I6. Seen red: a
  planted declined effort the fold leaves unwritten.
- **PLAY-dConvergedCharter-23** — Items 23 (B5-F14). Order 9. I9, I10. The release asks' join: DEPL-dShippedRelease-15
  S10 and TOOL-dTendedCadence-15 S2 spell their keys differently (scout D disagreement 6), so one red verify reaches two
  content keys and files two asks: exactly the clause's red case. This unit moves `derive_key_hash` to
  `tools/lib/key_hash.py` (the third copy, so one factory), fixes the one key and the one rendered text, and owns the
  joined fixture; each half builds against a stand-in for the other's (`[[stand-in]]` rows). `EVENT_PRODUCERS`'
  `release-verify-failed` producer has no carrier (disagreement 5): file the ask. Seen red: a planted red verify under
  roll-forward that files two asks.
- **PLAY-dConvergedCharter-6** — Items 6 (P16). Order 10. I11. Every record kind on dTotalRecall's registry through its
  factory, as a residue sweep: the `memory/**` population minus `record_kinds.py --population`, red on any unregistered
  home. Kinds no spec registers (scout B: `prompt`, `RUN.md`, the `memory/project/*.txt` lists, the ledger files) are
  this unit's; kinds another build's units own (`gotcha`, TOOL-dLinkedLibrary-22; `decision`, TOOL-dDeclaredLoop-31) are
  cited, never registered twice. Preconditions: TOOL-dTotalRecall-1, -2, -18, PLAY-dOrderedCharter-7, -42. Seen red: a
  planted record home no kind registers.
- **PLAY-dConvergedCharter-3** — Items 3 (gap-maint-04). Order 11. Reads I11. Records merged by evidence: no design
  source states the evidence rule (scout A row 3), so §8 settles it by the rungs (each kind's readers, writers,
  lifecycle and commit share from TOOL-dTotalRecall-18 and -24 are the candidate evidence; state the threshold and the
  measurement that decides it). A merge follows the rename-plus-alias precedent (TOOL-dTotalRecall-18 S7, -20 S1) and
  ships its alias as an upgrade step. Seen red: a planted pair of kinds the rule calls one, left unmerged.
- **PLAY-dConvergedCharter-19** — Items 19 (P34, P37; gap-tool-13). Order 12. I12, I13, I14. The guides' positional
  citations migrated to tags, legacy anchors kept as `[[alias]]` rows, a vanished section with no alias red
  (PLAY-dOrderedCharter-29 S8); the authored heading form (I12) asked of dOrderedCharter; the per-directory `eol=lf` pins
  (78 lines; `.gitattributes`) and the kits' `[[lf_pin]]` rows retired into class pins, with the `.md` and confs
  decision in §8 and `check_eol`'s population named; adopter removal as an upgrade step. The execution plan has no P34
  or P37 hit (scout A): cite v2:1044-1061. Seen red: a planted positional citation, and a planted per-directory pin a
  class covers.
- **PLAY-dConvergedCharter-2** — Items 2. Order 13. Reads I12, I13. Every remaining positional reference in live text
  migrated to tags by draining `positional-refs.txt` on unit 19's aliases (`WIRE-INTO-PROJECT.md` 56 lines; tools,
  skills and `.claude` 1,093 lines at HEAD), frozen records getting redirect rows only; after unit 12 removes the
  unattended code that holds `DIRECTIVES_CORE`'s M-number keys (scout A disagreement 4); the live hygiene rule that
  demands a `§n/Sn/ACn` scope token in §9 revision entries (`REV_SCOPE_CUTOFF`, `check-memory-hygiene.sh:111`) re-
  pointed (disagreement 3). Seen red: a planted positional reference in a live file.
- **PLAY-dConvergedCharter-13** — Items 13 (night pass point 4). Order 14. I15, I16. Feature-specific guide prose
  migrated into feature-scoped units (`scope = ["feature.<name>"]`), its rationale into each row's `help`, through the
  mover I16 extracted from `dossier_move.py`. Preconditions: TOOL-dLinkedLibrary-19, -20, TOOL-dTotalRecall-9,
  PLAY-dOrderedCharter-9, -15. Seen red: a planted feature paragraph left in a guide once its unit exists.
- **PLAY-dConvergedCharter-1** — Items 1 (gap-spine-05). Order 15. Reads I15, I16, I17. Protocol text derived to facts
  only, each document in its envelope: the residue after unit 13, written as units through `instructions.edit`, graded
  by `check_document`, and `instructions-legacy.txt` drained of the guides. The envelopes come from PLAY-dOrderedCharter-3
  (no envelope code here). Seen red: a planted non-fact statement in a migrated document.
- **PLAY-dConvergedCharter-10** — Items 10. Order 16. I18, I19. The `protocols` and `skills` scopes of the one renderer
  (PLAY-dOrderedCharter-9, -20 S5), each a `[[target]]` row, the `skills` scope replacing the seven per-kit Skill
  renderers scout B lists; protocol slices and Skill entries rendered from units. Seen red: a hand edit to a rendered
  protocol slice and to a rendered Skill entry, each at render parity.
- **PLAY-dConvergedCharter-7** — Items 7 (FQ-6; gap-found-12, gap-found-36, gap-found-27). Order 17. I21, owns
  `policy-key.help.explanation`. Protocols and templates rendered as tag-sliced views from the loop's checklists, the
  roles, the record schemas and the policies; the hand-written guides retired, their rationale in units' `help` fields
  and rendered into `help/why/` as `help.explanation` says, which no agent loads; no guide retired while a section maps
  to no unit's rationale. The ten guides' current carriers (scout B row 7: four memory-tree templates under kit/dogfood
  parity, REVIEW-PROTOCOL under protocol parity, the four UNATTENDED guides and PLAYBOOK-TEMPLATE rendered by
  `adopt-unattended.sh`, SESSION-KICKOFF and MERGE-BAR hand-written). Both values of `help.explanation`, each a planted
  case. Seen red: the clause's planted retirement of a guide with an unmapped section.
- **PLAY-dConvergedCharter-9** — Items 9 (SK-2; gap-found-13, gap-found-28). Order 18. I20, reads I3, I14, I19. Skills
  converged to level-4 thin entries generated from their command's `[[drive]]` row, named `gov-<name>`, each rename an
  upgrade step with the old name forwarded by a `skill` shim, its readers by path and by value re-pointed (scout B row
  9's `to`, `probe` and `pattern` rows, `.gitattributes` Skill rows after unit 19, the selftests, `WIRE-INTO-PROJECT.md`);
  `shims.read_releases` returns none today (a stand-in). Seen red: a planted stale probe path, and a planted gov-rendered
  Skill without the prefix.
- **PLAY-dConvergedCharter-8** — Items 8. Order 19. Reads I17, I18. The remaining renderers absorbed, each retired with
  its last document: kit/dogfood parity (`kit-dogfood-parity.test.sh:61`), review-protocol parity's document pair
  (its four `.js` pairs stay: the fates record keeps that check, scout B finding 6, so the clause owes a deviation),
  each kit's Skill-wiring `--check` arm, govkit's placeholder render; `tools/lib/render-doc.sh` with them. Settle scout
  B finding 5 (dOrderedCharter keeps two wiring legs by name, dShippedRelease retires both into one) by the rungs, and
  file the ask on the losing parent. Seen red: a renderer retired while a document it renders remains on the legacy list.
- **PLAY-dConvergedCharter-15** — Items 15 (SA-5, FQ-5; gap-found-27). Order 20. Reads I18, I21, I22. The hand-written
  `help/` pages (13 at HEAD, not 2: scout B finding 2), the kit READMEs, root `README.md` and the runbook migrated: each
  with its fates row (the fates record's `[table]` row by (Kit, Function); unit 14 materializes it later), its reference
  half generated by PLAY-dOrderedCharter-37's renderer, the runbook's taken as DEPL-dShippedRelease-9 derives it, its
  how-to half a page under the docs leg, a `readme` scope (I18). Seen red: a hand edit to a rendered page at render parity.
- **PLAY-dConvergedCharter-4** — Items 4 (gap-spine-04). Order 21. I24, reads I2. Superseded parts retired through
  ratified proposals: one proposer in `PROPOSERS`, the route under `review.loop.retire`, a decline as the `keep`
  record, a ratified retirement as a `[[retired]]` row plus an upgrade step. Preconditions: TOOL-dCalibratedLens-3, -5.
  Seen red: a planted superseded part retired with no ratified proposal.
- **PLAY-dConvergedCharter-14** — Items 14 (night pass point 8; gap-tool-09). Order 22. I22, I23, reads I9, I24. The
  fates table materialized as rows with path globs, its join run as convergence's exit check by extending govkit
  selfcheck arm 8's shape (`govkit.py:3415-3453`, `tracked`, `surface_paths`, `derive_vanished_members`), a declined
  retirement amending its row through the ratification record to `KEPT` or a new fate. Seen red: a planted unlisted
  file, a planted surviving `memory/guides/` file, and a planted declined proposal passing on the amended row and red on
  an unamended one.
- **PLAY-dConvergedCharter-18** — Items 18 (the shape audit; `closes PLAY-dConvergedCharter-24`). Order 23. I25. The
  owner's cycle walked by key from a planted build's intake, every hop of the memory plan's `[cycle]` resolved by a key
  (scout D's hop list, each with the unit that types it), red on any hop resolved by search or prose, run as
  convergence's acceptance once every hop's build has landed. `[cycle]` has no intake hop (scout D disagreement 7): the
  intake → request → build hops come from TOOL-dWellOiledMachine-27 S5 and TOOL-dPlacedRequest-19. No seam fits at HEAD
  (scout D row 18): §10 records the probe. Seen red: a planted hop resolved by prose.

## What you return

Per unit: the spec path, each deviation record path, each ask you need filed (target build, text, accept line), each
edge you added beyond the table, each shared interface you refined, and each disagreement with a scout row you found.
At most 1500 words per unit.
