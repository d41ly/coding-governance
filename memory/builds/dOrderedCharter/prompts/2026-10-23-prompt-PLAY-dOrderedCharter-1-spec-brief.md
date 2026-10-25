**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37

# Spec brief — dOrderedCharter, the thirty-seven units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here, and built by the build run after it. Read, in this order, before your first line:

1. The packet, `memory/builds/dOrderedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins,
   Gaps, Policy keys, Obligations and Later builds sections bind every unit.
2. The build README, `memory/builds/dOrderedCharter/README.md`: its build-level rules bind every spec, the fork rule
   above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit is Tier 2: each is a new or
   changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your units' rows under "The units", every entry of "Shared interfaces", and the scout record your units cite:
   `memory/builds/dOrderedCharter/build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md` (units 1-6, 8,
   9, 11-15, 20, 21, 27), `-b.md` (7, 10, 16-19, 22, 24-26, 28) and `-c.md` (23, 29-37). Each holds a seam table
   row per clause, with path:line at `3ca963bb6`.

The design sources the clauses compress are under `memory/builds/dClosedLoop/build/` (`B/` below): architecture v2
`B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (grep your clause id for its paragraph and the
`[policies]` rows at v2:1142-1145, 1242-1246, 1349-1359), `B/…-foundations.md` (R1-R6, F1, K1-K4),
`B/…-layer-instruction.md` (R-A to R-I), `B/…-systems.md` (`[design-tags]`, `[cross]`, IW-1, IW-2),
`B/…-layer-library.md` and `B/…-layer-expansions.md` (slots, EX-1), `B/…-memory-plan.md` (`[frame]`, `[practice]`,
`[sites]`, `[edges]`, `[doors]`), `B/…-adopter-instructions.md`, `B/…-flow-roles-adoption.md`, `B/…-night-pass.md`,
`B/…-night-pass-two.md`, `B/…-whole-audit.md` and its fold brief `B/2026-10-20-build-PLAY-dClosedLoop-1-fold-brief-w1.md`
(C1-F*), and the fork rungs in `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946. You never
edit an instrument, v2, the as-built view or the packet: the packet's Non-goals.

## Two parents are specced, not built

dGroundRules (the policy file `.governance/policy.toml`, its one reader, `budgets.*` and the minimal guard,
`cl-dClosedLoop-0007` to `-0012`) is `status: OPEN` with no unit built, and dSafePassage (the `[[upgrade]]` and
`[[retired]]` step kind, the docs leg `tools/govkit/usage.toml`) landed its specs and is DEFERRED to its build run
(`memory/builds/dSafePassage/README.md`). The chain builds them before this build's build run. So every spec here
cites the parent's frozen v2 clause, or its landed spec by id and section, as the interface, and names the call it
makes; the build run re-grounds against the landed parent. Never spec the parent's mechanism, never add a fourth
shell copy of `read_policy_key`, and never invent a policy route: a policy key this build owns is read through
dGroundRules' reader once it lands, with the catalogue default v2 states until then, and the spec says so in one
line.

## Every spec, whatever its unit

- Path `memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-<n>.md`; H1
  `# PLAY-dOrderedCharter-<n> — <title>`, an EM DASH, never a colon.
- Status header `DRAFT`, `Tier-2`, `base ce13efbe`, `streams playbook`, the `order` verb your roster row names, and
  `advances PLAY-dOrderedCharter-38` (the build's own open ask; the build run's last unit closes it).
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
  The seams in "The units" are a scout's reading at `fcb17844`: verify each line number against source before
  citing it.
- §8 forks: settle each by the README's rungs (execution plan
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 900-946), in the §8
  mark shape `memory/TEMPLATE-SPEC.md` states. A rung 5 or 6 choice cites its ruling (ER:240, ER:388, ER:328 or P0.8
  row 5) and carries `widens:` and `relaxes:`, each a value or `none`; a choice the README's `may:
  PLAY-dClosedLoop-3` grant lifted carries `grants: PLAY-dClosedLoop-3 <change>`. Never leave an open question: a
  FACT-QUESTION names its probe and you run it.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run. A
  rendered file is never the edit: `AGENTS.md` is rendered from `coding-governance-agents.template.md` by
  `tools/playbook/`, `.claude/agents/*.md` from `tools/roles/agents/`, `memory/guides/*.md` from their kit templates,
  and `tools/workflows/*.js` from their `.template.js`: name the source as the edit and the render as its copy.
- A later build's surface named in your clause (dDeclaredLoop, dTotalRecall, dWellOiledMachine, dWitnessedBar,
  dBoundRoles) is a stand-in or a join that build arms: spec the stand-in this build ships and name the hand-over,
  never the later build's mechanism (packet Non-goals, Later builds named).
- A departure from your clause (stricter, looser, or a different mechanism) is a deviation record you write beside
  your spec, `memory/builds/dOrderedCharter/build/2026-10-23-build-PLAY-dOrderedCharter-<n>-deviation-<k>.md`, in
  the grammar `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` shows (Serves,
  Departs from, Hand-off, Before, After, Cause, Reason, Evidence, Risk, Approver, Follow-through, Caused-by), with
  `<k>` = your unit number times 10 plus 1, 2, … so no two writers collide. Approver values: `report` and
  `author-recorded` (README). Do not commit it.
- Write nothing outside `memory/builds/dOrderedCharter/spec/` and `memory/builds/dOrderedCharter/build/`; temp
  files go under the scratch path your harness names.

## Shared interfaces — one spelling for every writer

Fixed so thirty-seven specs by five writers agree on the interface axis (M2). A writer who finds one wrong says so in
its §8 as a fork and settles it there by the rungs; it never silently respells one. "Owned by" is the unit that
specs the interface; every other unit named reads it as written here.

- **S1 · the moved grammar.** `tools/memory-tree/id_grammar.py`, exporting `grammar_for`, `anchor_at`, `Grammar`,
  `repo_root`, `resolve`, `Conf` with `Conf.digest`, and check 27's eight names (scout B, shared interface 1), each
  moved from `tools/memory-recall/extract.py` and `recall_conf.py`, which then import them from memory-tree. Owned
  by unit 18, which makes the move AND re-points every by-path reader in the same unit (its clause); unit 16 lands
  after it and owns the dependency check. Units 17 and 28 import from it. Unit 18 settles in §8 which kit version
  `Conf.digest` folds once it moves (the transition audit's cache key).
- **S2 · the join factory.** `compute_coverage` with `resolve_compare_base`, `derive_baseline_additions` and
  `drop_touched_exemptions`, moved to `tools/lib/coverage_join.py` with a `PARITY_ROWS` row in
  `tools/lib/resolve-python.test.sh` and `map_lib` re-exporting them for `install.deprecation-window` releases.
  Owned by unit 19; units 7, 10, 22, 29 and 36 join both ways through it and never re-derive a join.
- **S3 · the common-dir resolver.** `common_git_dir` canonicalised from `tools/memory-recall/query.py` into
  `tools/lib/common_dir.py`. Owned by unit 19 (the index at `<git-common-dir>/gov/index.db` is its next instance).
- **S4 · the tag grammar and the namespace registry.** `tag := <ns>.<seg>(.<seg>)*`, `seg := [a-z0-9][a-z0-9-]*`,
  at most 64 B, no name whose first segment is a namespace word, the words read from the registry and never typed
  beside it. The registry is `tools/playbook/namespaces.toml`, one `[[namespace]]` row with `ns`, `owner` (a chain
  build), `layer`, `source` (its declaring source), `extractor`, `role` (`selects` or `describes`),
  `purpose-source` and `join-armed-by`. The grammar, the registry file, the index and `gov tag` are owned by unit
  19; unit 10 registers its eight namespaces as rows and owns the shape check, the both-ways joins and the lexicon
  hand-off; unit 22 owns the `purpose-source` and `owner` fields' checks. The instruction layer's modules live in
  `tools/playbook/` (systems `[design-tags]` Owners: "the instruction layer, kit `playbook`").
- **S5 · `gov tag`.** No `gov` entry point exists. The verbs are `show`, `where`, `refs`, `check` and `bundle`,
  in `tools/playbook/gov_tag.py`, invoked as `python tools/playbook/gov_tag.py <verb> <address>`; unit 19 settles in
  §8 whether a `gov` launcher ships now or the module stands in. Units 25 and 26 add verbs or arms to it.
- **S6 · the edge grammar.** One `**Edges:**` line at column 0, `type=target[,target]` pairs separated by ` · `;
  a target holds no space, comma or bracket; a section is `<doc>#<seg>`; a pinned target `<tag>@<hash8>` is legal
  only for `amends` and `supersedes`, and `<id>@<hash8>` only for `carries-clause` (memory-plan `[sites]`,
  `[frame]`). The registry is `tools/playbook/edges.toml`, one `[[edge]]` row per type with its inverse derived.
  Owned by unit 24 (registry, grammar, parser); unit 28 applies it at every memory-plan site and reuses
  `design_lib.CARRY` and `derive_clause_hash` for the pinned forms; units 15, 20, 29, 32 and 35 write edges in it.
- **S7 · the pin hash.** `<hash8>` is `derive_clause_hash`'s normaliser (`tools/memory-tree/design_lib.py`),
  factored into one shared function the first unit that needs it outside clauses extracts (unit 24). Units 28, 32,
  33 and 35 call it; none writes a second normaliser.
- **S8 · the ladder.** Integer levels 0 to 7 and the word "level" only, the charter at level 0 and the platform
  above it (layer-instruction R-G). One constant, `LEVELS`, in `tools/playbook/instruction_units.py`. Owned by
  unit 13; units 2, 3, 4, 5, 8 and 9 read it.
- **S9 · the statement types.** A closed set `directive`, `constraint`, `definition`, `pointer`, `policy-value`,
  `fact` (layer-instruction R-D). Owned by unit 12, with the check and the render provenance lock
  `.governance/instructions.lock` (one row per rendered target: path, blob, unit tag@hash, renderer version), which
  moves provenance out of loaded text. Units 9, 20 and 3 read both.
- **S10 · the instruction unit row.** `<kit>/instructions.toml`, one `[[unit]]` row with `tag`, `level`, `type`,
  `scope`, `trigger`, `budget`, `source`, `origin`, `owner`, `usage`, `help`, `required-by`, `enforced-by`,
  `class` and `edges` (S6), read by one reader in `tools/playbook/instruction_units.py`. `enforced-by` is spelled as
  `tools/roles/check_roles.py` spells it; `class` is `fixed` or `open`, derived where the schema declares it and
  read `fixed` when undeclared. Owned by unit 9; unit 20 owns the schema and grammar check and the one renderer;
  units 1, 11, 14, 15, 21, 32 and 35 read it.
- **S11 · the one renderer.** `tools/playbook/render_playbook.py` is the renderer of record; it absorbs playbook
  parity, the playbook render wiring, the roles render wiring and the agent-instructions wiring (clause 0050), each
  instruction file held to one renderer and the render gate armed with a shrink-only legacy list read under
  `instructions.legacy`. Owned by unit 20; unit 31 writes the adopter upgrade step that moves agent-instructions'
  wiring to it; unit 37's pages and unit 3's envelopes are its outputs.
- **S12 · the typed build-folder record factory.** The deviation record's reader in
  `tools/memory-tree/deviation_join.py` (name grammar, `**Key:**` fields, closed sets, `read_record`) extracted
  into one factory at its second instance, in the record kit's own module. Owned by unit 7, whose exception record
  is `<date>-build-<unit id>-exception-<n>.md`; unit 2's override record is `<date>-build-<unit id>-override-<n>.md`
  and unit 15's change record `<date>-build-<unit id>-change-<n>.md`, each a kind of the factory, written through
  the stand-in door memory-plan `[doors]` lists until dTotalRecall's record door adopts it.
- **S13 · the change record's fields.** `mark` (`editorial` or `semantic`), `successor` (a tag, a list for a
  split, `none` for a retirement) and a derived `status` (`active`, `retired:<tag>[,<tag>]`, `retired:none`).
  Owned by unit 15 (the writer, `instructions.edit`); unit 33 owns the `editorial`/`semantic` mark's checks and
  `instructions.stale`; units 20, 31, 34 and 35 read it.
- **S14 · the overlay.** `.governance/instructions.toml`, the repository's own rows in S10's grammar, tagged
  `repo.<seg>` for prose units; a kind row puts `adopter` in the owner seat (`role.adopter.<name>`,
  `item.<step>.adopter.<name>`, `leg.adopter.<name>`); a patch row carries an `amends` or `supersedes` edge pinned
  `<tag>@<hash8>`, `add`/`remove` on set fields and a value on scalars. Owned by unit 32 (file, home, `repo.`
  units); unit 35 owns the row mechanism over every kind and `instructions.exclude`; unit 36 the row checks;
  unit 34 composition. The overlay is written only through unit 15's command.
- **S15 · the practice catalogue.** `tools/playbook/practices.toml`, one `[[practice]]` row with `tag`
  (`practice.<name>`; the short `<name>` stays in a role's `rules:` value), `line` and `reach.<step>`. Owned by
  unit 1 with `charter.practices`; units 2, 21, 29 and 30 add or read rows.
- **S16 · the envelope.** `[<doc> · Level <n> · <direction>]` … `[/<doc>]`, one helper carried inline as a
  `# >>> name — canonical copy` block with a parity row, because roles and playbook are copy-installed. Owned by
  unit 3 with the gate; units 2, 4, 5 and 20 emit it.
- **S17 · the drive table.** `[[drive]]` rows in each adopted kit's `kit.toml` with `stage`, `role`, `command`
  and `when`, composed into the charter's drive section and checked both ways. Owned by unit 6; unit 23 writes its
  sentence through it.
- **S18 · budgets.** Caps are `budgets.<load-point>` keys with `budgets.enforce` (`warn` or `refuse`), owned by
  dGroundRules (v2:1346-1348); until that reader lands, `tools/template-size-limits.txt` rows are the carrier and
  the spec names the hand-over. `instructions.checks` (`refuse`, `warn`, `record`; default `refuse`) governs only
  the missing-required-unit refusal, never the size budget (gap-found-34). Owned by unit 11; units 6, 27 and 34
  read it.
- **S19 · the card file.** A per-worktree, gitignored `.claude/orientation-card.md`, re-rendered by each
  session-start hook in the session's own tree and imported by the charter's entry file as a second `@` line.
  Owned by unit 8; unit 4's replay renders the instruction map beside it.
- **S20 · the layer row and the slot states.** `layer = "<tag>"` in each `kit.toml`, beside `requires_if`, and
  `optional = [{ part, point, fallback }]`; every optional slot renders one of `filled`, `searched-empty` or
  `not-installed: <fallback>` (layer-library `[consult]`). Owned by unit 16; unit 17 makes each found edge a slot.
- **S21 · the tags leg pack.** Legs in `tools/gate-legs.json` carrying a new `"pack": "tags"` key, never an
  overloaded `chunk`. Owned by unit 19; units 24, 25, 26, 28 and 29 add legs to it. dWitnessedBar owns packs as a
  namespace later: name it as the join that build arms.
- **S22 · the delta report states.** `unchanged`, `amended`, `replaced`, `excluded`, `stale`, `orphaned`, in the
  verdict-line shape of `govkit.py`'s `cmd_update`. Owned by unit 34; units 33 and 35 emit them.

## Owned nodes

| Node | Unit |
|---|---|
| `policy-key.charter.override` | 2 |
| `record-kind.override` | 2 |
| `policy-key.charter.practices` | 1 |
| `policy-key.core.bypass` | 7 |
| `policy-key.core.exceptions` | 7 |
| `record-kind.exception` | 7 |
| `policy-key.instructions.checks` | 11 |
| `policy-key.instructions.edit` | 15 |
| `policy-key.instructions.proof` | 15 |
| `policy-key.instructions.exclude` | 35 |
| `policy-key.instructions.stale` | 33 |
| `policy-key.instructions.legacy` | 20 |
| `system.instruction-writing` | 20 |
| `system.tags` | 19 |
| `policy-key.tags.slice` | 19 |
| `policy-key.tags.retired-cites` | 19 |
| `policy-key.tags.bare-refs` | 19 |
| `tag-namespace.doc` | 19 |
| `tag-namespace.unit` | 19 |
| `policy-key.tags.positional` | 26 |
| `policy-key.tags.bundle` | 25 |
| `policy-key.tags.bundle-rows` | 25 |
| `tag-namespace.reader` | 10 |
| `tag-namespace.level` | 10 |
| `tag-namespace.layer` | 10 |
| `tag-namespace.practice` | 10 |
| `tag-namespace.principle` | 10 |
| `tag-namespace.kind` | 10 |
| `tag-namespace.kit` | 10 |
| `tag-namespace.repo` | 10 |

## The units

**Writer groups and build order.** The `order` value is the build order. Primitives land before their features:
the moved grammar before the dependency check, the join factory and the tag grammar before every registry that
joins, the record factory before its three kinds, the ladder, statement types and unit rows before the renderer,
the renderer before the charter it renders, and the overlay before the mechanisms that patch it. The build harness (`tools/workflows/unattended-build.js`) splits the 37 orders into five writer groups of consecutive orders and hands each writer its group; author every unit of your group, in order, and nothing else:

| Writer | Units (order) |
|---|---|
| 1 | 18 (1), 16 (2), 17 (3), 19 (4), 10 (5), 22 (6), 24 (7), 28 (8) |
| 2 | 26 (9), 25 (10), 7 (11), 13 (12), 12 (13), 9 (14), 20 (15), 15 (16) |
| 3 | 1 (17), 3 (18), 6 (19), 2 (20), 11 (21), 27 (22), 21 (23), 5 (24) |
| 4 | 4 (25), 8 (26), 14 (27), 30 (28), 29 (29), 23 (30), 32 (31), 33 (32) |
| 5 | 35 (33), 36 (34), 34 (35), 31 (36), 37 (37) |

Eight Tier-2 specs is a long pass: keep each spec to what its clause and its shared interfaces need, cite the scout record's seam rows rather than re-deriving them, and write each spec to disk as soon as it is done.

- **PLAY-dOrderedCharter-18** — Items 18. S1's move and every by-path reader re-pointed in the same unit, the
  inventory derived by a query over `tools`, `skills` and `.githooks` and never typed, `tools/runlog/extract.py`
  kept out of it, `tools/check-kit-versions.sh` in it (scout B). The staged break in the moved module reds
  `check-verdict-epoch.sh` (DA-H4).
- **PLAY-dOrderedCharter-16** — Items 16 (gap-found-17). S20; the layer register, contract, factory and gate; the
  core-never-depends-on-an-expansion check over every edge kind the clause lists, each seen red on a planted edge,
  the AST walk lifted from `check-verdict-epoch.sh` at its second instance; EX-1's arm seen red on a planted pair.
- **PLAY-dOrderedCharter-17** — Items 17. Each edge the check finds made an S20 slot with a named fallback, or
  moved into the core, at the nine sites scout B lists; gotchas' check 18 resolving ids on a scratch clone without
  memory-recall.
- **PLAY-dOrderedCharter-19** — Items 19 (gap-found-20, gap-found-33). S2, S3, S4's grammar and registry, S5, S21;
  the SQLite index keyed as the clause states, rebuilt from nothing to identical rows, seen on the planted
  two-path blob and two-worktree dirty cases; the `doc` and `unit` namespaces; `tags.slice`, `tags.retired-cites`
  and `tags.bare-refs` each seen on its planted case; the codebase-map leg red on the move without the re-export.
- **PLAY-dOrderedCharter-10** — Items 10 (gap-found-09, gap-found-21). S4's eight namespace rows and their
  both-ways joins over non-empty populations, the shape rules each seen red on a planted tag (`practice.repo.x`
  among them), the later namespaces' joins named as armed by their builds, the lexicon handed the namespace words.
- **PLAY-dOrderedCharter-22** — Items 22. S4's `purpose-source` and `owner` fields and the chain registry's
  purpose field; their existing entries reviewed by dTotalRecall's PM-5 unit, which reads `memory.map-purpose`.
- **PLAY-dOrderedCharter-24** — Items 24 (gap-found-25, gap-mem-35). S6's registry, grammar and parser, S7's
  shared normaliser; one closed set of typed edges, inverses derived, selectors open.
- **PLAY-dOrderedCharter-28** — Items 28. S6 at every site the memory plan names, its new types, native-id
  classes and pinned forms, reusing `design_lib.CARRY` and `derive_clause_hash`.
- **PLAY-dOrderedCharter-26** — Items 26 (gap-found-22, gap-found-26). file:line citations joined to the
  positional population `tags.positional` holds, as `path#symbol` or a blob-pinned line, a shrink-only keyed list.
- **PLAY-dOrderedCharter-25** — Items 25. `gov tag bundle` under `tags.bundle` and `tags.bundle-rows`, manifest
  or inline under the byte budget the call names.
- **PLAY-dOrderedCharter-7** — Items 7 (gap-found-07, gap-found-08). The principle registry and meta-check (a
  `enforces` key on `tools/gate-legs.json` rows joined through S2), the kinds register with each kind's owning
  build, the conformance-gate contract, S12's factory and the exception register, `core.*`, and the factories
  and gates for instruction units, practices, Skills and layers.
- **PLAY-dOrderedCharter-13** — Items 13. S8, and every design carrier R-G names re-pointed to it.
- **PLAY-dOrderedCharter-12** — Items 12 (gap-found-11). S9: the grammar, its check and the sidecar lock.
- **PLAY-dOrderedCharter-9** — Items 9 (gap-found-09). S10: the registry and its reader; documents rendered from
  units.
- **PLAY-dOrderedCharter-20** — Items 20 (gap-found-23). S11, the schema and grammar check, the work-order
  template, each unit's status derived from its change record (S13), the render gate with `instructions.legacy`,
  and the one-fact check over units.
- **PLAY-dOrderedCharter-15** — Items 15 (gap-found-15). The instruction manifest and `instructions.edit`'s
  command with `instructions.proof`, each `instructions.edit` value given its arm, witness and planted red,
  `flow-only` refused at load until dDeclaredLoop lands, every write refused until dDeclaredLoop's guard lands;
  S12's change record; instruction packs extending `charter.practices`.
- **PLAY-dOrderedCharter-1** — Items 1 (gap-found-02). S15 and `charter.practices`.
- **PLAY-dOrderedCharter-3** — Items 3 (gap-found-01). S16 for every registered document, and the gate.
- **PLAY-dOrderedCharter-6** — Items 6 (gap-found-05). S17, each subagent's role line repeated in its handoff,
  the charter held inside 32 KiB measured against S18's caps, the `template-size-limits.txt` rows held and any
  raise argued in its change record under that file's four conditions.
- **PLAY-dOrderedCharter-2** — Items 2 (gap-found-04, gap-flow-02, gap-found-18). The charter re-founded in its
  level-0 envelope, the override rule with `charter.override` and its S12 record, the decision principles ranked
  above the practices, the project block from the overlay, the `up —` micro-format naming where a credential
  lives (seen red on today's `pw` field), and `SECTION_ONE_RE` with the roles `rules:` join and the review
  harness prompts re-pointed to practice tags in the same unit, proven by a role render.
- **PLAY-dOrderedCharter-11** — Items 11 (gap-found-10, gap-found-34). Load sets per reader and item, S18, seen
  red on a planted load set missing a unit a role's `required-by` names; injected load points measured.
- **PLAY-dOrderedCharter-27** — Items 27. The `code` slot budgeted in each role's load set; `memory.code-budget`
  is dFurnishedOrders' key, read with its catalogue default until it lands.
- **PLAY-dOrderedCharter-21** — Items 21. Each practice's reach per step (S15) rendered as step-scoped units
  handed in work orders.
- **PLAY-dOrderedCharter-5** — Items 5 (gap-found-03). Ranked S16 envelopes in every subagent handoff, the
  charter carried once.
- **PLAY-dOrderedCharter-4** — Items 4. The instruction map re-injected on compact and resume through the
  existing replay fragment, never a third SessionStart entry.
- **PLAY-dOrderedCharter-8** — Items 8 (gap-orient-13). S19 at level 1, subagents' slices through the brief and
  the subagent-start hook, agent-instructions' wiring standing in for other harnesses until dWellOiledMachine,
  never an override file, after the primary-to-worktree compaction fixture passes.
- **PLAY-dOrderedCharter-14** — Items 14 (gap-found-14). Memory instructing nothing: the index measured at
  session start, its directives detected, a standing directive promoted into a unit through unit 15's command.
- **PLAY-dOrderedCharter-30** — Items 30 (gap-tool-19). The portable practice as an S15 row replacing `[bytes]`
  and `[cross-os]`, each rule paired with its named leg (the floor's in dSafePassage).
- **PLAY-dOrderedCharter-29** — Items 29. The one writing practice's checks over records as well as units,
  today's unpinned facts a keyed list until dWitnessedBar registers it.
- **PLAY-dOrderedCharter-23** — Items 23. A build run unattended by default from its request: the `[land]` rule
  and the drive section's sentence (S17).
- **PLAY-dOrderedCharter-32** — Items 32 (gap-found-19, gap-found-29, gap-found-31). S14's file, home and `repo.`
  units, gov's own rules moved into gov's own overlay.
- **PLAY-dOrderedCharter-33** — Items 33 (gap-found-30). The `editorial`/`semantic` mark on each gov change record
  (S13), pins and drift, `instructions.stale`.
- **PLAY-dOrderedCharter-35** — Items 35. S14's row mechanism for every kind a later build registers, `owned`
  admitting the `adopter` segment, `instructions.exclude`, one fixture kind naming no later build's kind.
- **PLAY-dOrderedCharter-36** — Items 36. The row checks over every registered kind, widening directions
  declared per field, the fixture kind's planted reds.
- **PLAY-dOrderedCharter-34** — Items 34. Composition and its report (S22): the project block from level-0 units
  and the level-3 to level-5 units in a marked part of their documents, the seeded template retired.
- **PLAY-dOrderedCharter-31** — Items 31. Its own upgrade steps through dSafePassage's step kind: agent-instructions'
  wiring moved to the one renderer, the seeded template converted into the overlay; scout C's interface 10 names
  the `[[retired]]` row mismatch to settle in §8.
- **PLAY-dOrderedCharter-37** — Items 37. Reference pages rendered by S11 from each registry's rows, extending
  dSafePassage's docs leg (TOOL-dSafePassage-13) and `tools/govkit/usage.toml`, never a copy.
