**Serves:** research PLAY-dOrderedCharter-53

# Brief: fold drift sweep B into specs 53, 13, 42 and 12

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03, approving the run's drift sweep (`prompts/2026-11-03-prompt-PLAY-dOrderedCharter-55-owner-speedup.md`). The sweep's
reviewer read specs 53, 13, 42 and 12 against the tree at `06e612222` and returned the findings below, every one with a tree path
and line. This pass folds them before those units dispatch, so their builders do not hand back a divergence.

## The brief

### Goal

Revise specs 53, 13, 42 and 12 so each matches the tree at HEAD on every finding below.

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

- Writes stay in specs 53, 13, 42 and 12 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question. A fork that no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check. The main loop re-renders the packet, renders the index and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev, each §8 decision with its loser, and any finding you did not fold, with the reason.

**The findings.**

Cross-cutting: (a) new legs in 13 and 12 omit the owed rows (dossier claim memory/map/features/playbook.md + memory/map/generated/, tools/govkit/registry.toml, tools/govkit/subject-pins.tsv; the codebase-map pre-commit hook .githooks/pre-commit:280-292 refuses an unclaimed leg) and the legs those paths trip (recall floor, recall floor arms, govkit selftest, govkit refusal join) — mirror unit 26 rev-7's AC12. tools/run-gates/owed_rows.py is absent at HEAD (unit 50 builds it). (b) 13 and 12 write `principle.*` into a leg's `enforces`; edges.toml:63-70 has to=["unit","practice"]. Main-loop decision: unit 7 (order 11, before both) widens `to` with `principle` in its pass (sweep A 7-2); 13 and 12 consume that and say so in §3 Edges.

**Spec 53.**
- 53-1 S1 reads `git blame --porcelain -M HEAD -- <path>`; naming HEAD blames only the committed version, so AC3's uncommitted x.py:3 gets no attribution (probed: without HEAD the uncommitted line reads sha 0000…). Blame the working tree (drop HEAD); state the all-zero sha counts as inside the descendant set.
- 53-2 §7 says neither leg is in gate-legs.json at base; `tags (the resolver's checks)` is now a leg (registry.toml:711, subject-pins.tsv:146). Unit 26 rev-7 routes positional-* plants to `tags positional selftest` (spec 26 S7 :118-125, New arm :335). Route the three positional-* plants there.
- 53-3 New arm names tools/playbook/adopt-playbook.sh (plant rows in its `run_plant_rows tags` table :258; PLANTS tuple gov_tag.py:317) — not in Files touched. Add it (or drop it once re-routed).

**Spec 13.**
- 13-1 S3/AC3/§4: unit 10 built `level` as level.<name> — namespaces.toml:54-60 (source LEVELS in tools/playbook/instruction_units.py, extractor tag_index:extract_level, purpose-source instruction_units.py#LEVELS); tag_index.py:347-364 extract_level yields level.charter … level.records. Re-point S3/AC3 to level.<name> via extract_level; drop or redefine derive_level_tag(s) — no second extractor.
- 13-2 AC3 says shape `seg` of "S4's grammar"; S4 is ladder-terms; the shape is SEG at tag_index.py:65.
- 13-3 Owed rows/legs for leg `instruction ladder (level is the one term)` — cross-cutting (a).
- 13-4 enforces principle.p13/p11 — cross-cutting (b).
- 13-5 §1/§4 Migration "Nothing in the product spells a level today" is stale; at landing `level` moves pending→graded under the tags leg (unit 22 return lists it pending). Add an AC or §7 note.

**Spec 42.**
- 42-1 S3 cites `deviation_named` (tree_lib.py:491) as stem precedent; that regex matches any `-deviation-\d+.md` name. The stem regex is `deviation_name` :492-493. Generalising :491 reds the six tracked `…-execution-return-plan-2..7.md` under AC6. Cite :492-493 and state the deviation-kind narrowing.
- 42-2 gen_build_index.py anchors: import block :187→:188 (RECORD_KIND_TOKENS :189); cmd_print_bindings :682→:691.
- 42-3 deviation_join.py:238-240 will move when unit 7 (order 11) extracts the factory; cite RECORD_NAME by name.

**Spec 12.**
- 12-1 §10 lines: render() :979→render_playbook.py:1024; check_one_line_regions :667→:698, signature now (text, cap=None) -> list; check-playbook-parity.sh S4 arm 316→:438.
- 12-2 §4 example renderer "playbook-render@1.31"; KIT_PLAYBOOK_RENDER_VERSION = "1.33" (render_playbook.py:1887).
- 12-3 Owed rows/legs for leg `instruction grammar (statement types, provenance lock)` — cross-cutting (a).
- 12-4 enforces principle.p11 — cross-cutting (b).
- 12-5 S4 hash "S7's normaliser" — S7 is the leg; the normaliser is unit 24's derive_pin_hash (tools/memory-tree/design_lib.py:173). Name it.
- 12-6 AC5 runs `render_playbook.py --target . --check`, the playbook render wiring leg's check; restate as the unit's own probe.

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
