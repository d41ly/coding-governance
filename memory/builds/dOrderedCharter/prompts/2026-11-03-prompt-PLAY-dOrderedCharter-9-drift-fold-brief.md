**Serves:** research PLAY-dOrderedCharter-38

# Brief: fold drift sweep C into specs 9, 20, 15 and 50

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03, approving the run's drift sweep (`prompts/2026-11-03-prompt-PLAY-dOrderedCharter-38-owner-speedup.md`). The sweep's
reviewer read specs 9, 20, 15 and 50 against the tree at `06e612222` and returned the findings below, every one with a tree path
and line. This pass folds them before those units dispatch, so their builders do not hand back a divergence.

## The brief

### Goal

Revise specs 9, 20, 15 and 50 so each matches the tree at HEAD on every finding below.

### Items

1. Fold every finding below into its spec. Re-verify each cited path and line at HEAD before writing it: units may
   have landed since the sweep read the tree.
2. A finding marked NEW MECHANISM is a fork: decide it by M3, and record the loser and the observation that rejected
   it (M12) in §8, delegated.
3. **A new leg's own rows.** Every new leg's rows are written in its own pass, the way unit 26 rev-7 writes
   `tags positional selftest`'s. Those rows are the dossier claim in `memory/map/features/playbook.md` (with
   `memory/map/generated/*`, which the map generator rewrites), the `tools/govkit/subject-pins.tsv` row, and the claiming row.
   - For a leg an adopter cannot carry, the claiming row is an `[[exempt_leg]]` row in `tools/govkit/registry.toml`,
     as units 16, 19 and 28 wrote at `:707`, `:711` and `:715`.
   - Otherwise it is a `[[gate_leg]]` row in the kit's `kit.toml`.
   - Files touched lists those paths, and §7 names the legs they trip. Check them with
     `python tools/check-spec-tokens.py --legs-for <path>`.
4. **`enforces` into `principle.*`.** The main loop decided this across the sweep. Unit 7, at order 11, adds `principle` to the
   `enforces` row's `to` in `tools/playbook/edges.toml` in its own pass. Units 13 and 12 consume that through a §3 Edges line.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-03, with the status kept `DEFERRED`.
- Add one §9 line naming this brief.
- §7's leg line names every leg whose guard a Files-touched path trips.
- No AC observes a suite, a bar or a gate leg.
- Stay under the 47000-byte authored budget.
- An H1 names another build's unit as "<build>'s unit N", never by its id.

For the run:

- Writes stay in specs 9, 20, 15 and 50 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question. A fork that no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check. The main loop re-renders the packet, renders the index and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev, each §8 decision with its loser, and any finding you did not fold, with the reason.

**The findings.**

Cross-cutting: new legs in 20 and 15 omit the owed rows (dossier claim memory/map/features/playbook.md + memory/map/generated/, tools/govkit/subject-pins.tsv, the claiming descriptor or [[exempt_leg]] row) and the legs those paths trip (recall floor, recall floor arms, govkit selftest, govkit refusal join, codebase-map coverage + freshness) — mirror spec 26 rev-7. read_policy_value is tools/playbook/policy_value.py:72 (unit 19, 9cb93347d): returns (stdout lines, explain line), raises PolicyRefused(key, line) (:63-69) — no "exit 2". "S7's normaliser" is design_lib.derive_pin_hash (tools/memory-tree/design_lib.py:173). The playbook kit id is `playbook-render` (tools/playbook/kit.toml:7), never the directory.

**Spec 9.**
- 9-1 NEW MECHANISM (fold S1/S3/Files touched/AC4): unit 28's third manifest parser read_unit_edges (tools/playbook/edge_grammar.py:308-333, called by read_tree_edges :576-592 for every tracked *instructions.toml, own tomllib.loads) reads the selector as `select` (UNIT_FIELDS edge_grammar.py:85; edges.toml:61 instructs declared-at "the unit's select"; help/tags.md:204), while tag_index.derive_unit_rows (tag_index.py:275-289) and spec 9 S1 read `scope`. It iterates enforced-by per element, so S1's one-string form `none — <why>` yields one edge per character. AC4's grep finds parses at edge_grammar.py:562,577,592 and tag_index.py today → reds. Pick one spelling, point read_unit_edges at read_units/Unit (or one text-level parser), handle the string enforced_by, add edge_grammar.py (and help/tags.md if the spelling changes) to Files touched.
- 9-2 NEW MECHANISM: extract_unit(ctx, path, text=None) (tag_index.py:292-298) is called per blob with blob text (base-revision reads) — a working-tree read_units(root) cannot serve it; its population is any path named instructions.toml except the overlay (:297), not S2's <prefix>/*/instructions.toml; the extractor version is the SHA-256 of its own module only (derive_extractor_versions :155-169, resolve_extractor_module :145-152), so delegating to instruction_units.py serves stale rows. Give the reader a text-level entry (e.g. parse_unit_rows(text, path)) both call; move the extractor into instruction_units.py (re-point namespaces.toml:28, add to Files touched) or state how the version covers the dependency; align the populations. Decide by M3.
- 9-3 S4/§3: cite policy_value.read_policy_value + PolicyRefused (cross-cutting); re-aim consumes-from to unit 19.
- 9-4 S2 "unit 24's parser" for `edges`: parse_edge_lines(text, path) (edge_grammar.py:220) is for Markdown lines; list entries are checked inline at :323-325 with TYPE_RE (:68) + derive_target_fault (:201). Name those or mint one shared entry parser read_unit_edges also calls (ties to 9-1).
- 9-5 §4 example uses role.*; namespaces.toml registers doc unit reader practice level layer principle kind kit repo; check_edges reds unregistered (edge_grammar.py:430-437); spec 49 AC9 (:412) expects that red. Use reader.every (readers.toml:7) or say the AC5 fixture registers role.
- 9-6 §10: load_workflows tools/roles/roles_lib.py:339→:364; WORKFLOW_KEYS tools/roles/check_roles.py:92→:94.

**Spec 20.**
- 20-1 owed rows/legs for its two new S10 legs (cross-cutting).
- 20-2 S4 reds an instruction file no renderers.toml row claims; the data model claims none of .claude/rules/product.md, the seven .claude/skills/*/SKILL.md, skills/{deploy-governance,session-kickoff}/SKILL.md; product.md has no renderer (git grep -l "rules/product.md" -- tools/ is empty). Say which row a hand-written legacy-listed file gets (e.g. renderer = "hand", or a legacy listing is the claim) and list every population's row.
- 20-3 AC5's grep prints only comment lines adopt-agent-instructions.sh:8,:18 and is unchanged by the re-point; adopt-roles.sh calls render_agents.py (:20, :323). Grep for `render_playbook.py --render-scope`/`--check-render` present and `render_agents.py --write` + `_wire_pointer_or_copy` writes gone.
- 20-4 AC9 `--kit playbook` → `--kit playbook-render` (cross-cutting).
- 20-5 S8/S2/§3: policy reader and normaliser (cross-cutting).
- 20-6 AC10 note says the policy kit is untracked; git ls-files tools/policy lists 15. Drop the reason.
- 20-7 §10 render() render_playbook.py:979→:1024.

**Spec 15.**
- 15-1 NEW MECHANISM: extractors register only as one `extractor` string per namespaces.toml row (read_namespaces tag_index.py:136, load_extractors :179, one row per ns :133); `unit`'s extractor is tag_index:extract_unit (namespaces.toml:28) claiming only instructions.toml paths; no table holds a successor/redirect (schema tag_index.py:72-85); show prints tag, path, kind, text only (gov_tag.py:77-86). Decide by M3 how it registers (new namespace row owing unit 22's purpose field, or extract_unit also claiming change records) and where the redirect lives (e.g. the retired row's text); add namespaces.toml to Files touched if a row is added.
- 15-2 S7: promoted-from has writer "instructions.edit" (edges.toml:237-244); check reds a writer-typed edge whose site differs (edge_grammar.py:415-417); no reader assigns that site (sites :254-386); read_header_edges reads only Caused-by/Made-by (HEADER_RE :83). S7 adds a change-record edge reader tagging site = "instructions.edit"; edge_grammar.py joins Files touched.
- 15-3 owed rows/legs for leg `instruction edits (manifest checks)` (cross-cutting).
- 15-4 AC6 `--manifest playbook` → `--manifest playbook-render`.
- 15-5 point.instructions.* → point.instruction.* (layers.toml:9-14 spells point.<layer>.<seg>; layer.instruction :20 declares point.instruction.name-check).
- 15-6 S5 policy reader (cross-cutting); render_playbook.py:78-79 resolve_kit_dir cite is still right but not the reader called.
- 15-7 S7 normaliser (cross-cutting).
- 15-8 §10/AC12: merge-rows key tools/memory-tree/merge-rows.py:271→:232; .gitattributes merge=rows lines 77,78,84, comment 67 (spec 61-78); AC12 "untracked until it builds" false.

**Spec 50 (rev-4).**
- 50-1 S5/AC4: unit 19/16/28's legs are claimed by [[exempt_leg]] rows in tools/govkit/registry.toml:707,711,715; tools/playbook/kit.toml holds only playbook render wiring/selftest (:69, :79). Choose [[gate_leg]] or [[exempt_leg]] from the leg's subject and point AC4 at that file.
- 50-2 AC5 is already true pre-build (its git grep prints the line in all ten handed-off specs 3,7,12,13,15,20,25,31,49,55 plus spec 50's own :206 = 11). Observe something this pass creates; exclude spec 50.
- 50-3 §4 Evidence/§1: tools/template-size-limits.txt is still tracked; the row is :162 value 10369; tools/policy/caps.toml:82-90 reads it. Fix the evidence and reason.
- 50-4 lines: KNOWN run-gates.test.sh 244,580→364,700 (already holds `pack`); signature pair 589-597→709-717; govkit.py pin writer 3005-3022→2712-2742, pin read 2749-2762, "a NEW leg" :2765, check 7h 2944-2946→:2690, read_descriptors 13238→13622 signature (root, reg, r: Report); map_lib.py claimant_index 1613→1506.

### Acceptance

- Each finding above is either folded, or listed in the return with the reason it was not.
- Each revised spec's Status line is one rev higher, and its §9 holds the new line.

### Gates

The spec-token check, run over the tree by the next `--dispatch`.

### Non-goals

- No code.
- No spec outside the four above.
- No finding about another spec.

### Limitations

The items above, "For the run".

### Reuse

Unit 26 rev-7's owed-row shape (its Files touched, §7 and AC12). `tools/playbook/edge_grammar.py`'s readers and checks.
`tools/playbook/policy_value.py`.
