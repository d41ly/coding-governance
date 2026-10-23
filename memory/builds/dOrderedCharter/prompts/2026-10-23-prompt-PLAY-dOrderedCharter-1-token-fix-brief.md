**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37

# Token-fix brief — the spec-token check over the first spec pass

Fix every hit `python tools/check-spec-tokens.py` reports over the staged dOrderedCharter specs, so no hit names a
dOrderedCharter spec, changing nothing else.

- Each `[path]` hit is a backticked path-shaped token in a §6 Acceptance criterion (or another graded section) that
  `git ls-files` does not track. Cite a file the build run will create, a `rev:path`, a fixture path or an example
  literal by BASENAME, or without a slash, in §6; full paths stay in §2 and §4 and Files touched, which the join does
  not read. Correct a path that is simply wrong to the tracked one.
- Each `[hands-off]` hit: the bullet hands a token to a sibling whose own spec never names it. Name it in the sibling
  where it reads or builds that token, or correct the bullet.
- Each `[carries]` hit: clause `cl-dClosedLoop-0046`'s token is in none of its carriers. PLAY-dOrderedCharter-16's
  §3 Non-goals first bullet says the move is PLAY-dOrderedCharter-18's; extend that bullet to name the moved names
  and their importers in backticks: check 27's eight, the id grammar's `grammar_for`, `anchor_at` and `repo_root`
  that `backlog.py`, `corpus_ids.py`, `merge-rows.py` and `transition_audit.py` import, `recall_conf.resolve` and
  its `Conf.digest`, and `extract.grammar_for`, which `gen_build_index.py` imports.
- Two memory-hygiene hits over the same staged specs (`bash tools/memory-tree/check-memory-hygiene.sh --staged`):
  check 2, PLAY-dOrderedCharter-14 links `<file>.md` as a relative Markdown link, which resolves to nothing: write it
  as code or as text, not a link; check 25, PLAY-dOrderedCharter-1's §2 item S6 retires a named thing and carries no
  `**Readers:**` clause: write `**Readers:** by name:` with the readers that spell the name, then `by value:` with its
  value's readers or `NO VALUE READERS` and a reason, each reader found by a grep you run. Re-run that check too and
  report checks 2 and 25 clean.
- The specs are uncommitted at rev-1 and unaudited, so edit them in place with no rev bump. Touch no deviation record.
- Do not commit, do not stage, and do not run the build-index generator. Re-run the check, and report its exit code
  and the count of hits still naming a dOrderedCharter spec (zero is the target).

## The hits, verbatim

- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md [path] `help/charter.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md [path] `tools/playbook/load_sets.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md [path] `tools/playbook/load_sets.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md [path] `tools/playbook/load_sets.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-13.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-13.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-13.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md [path] `tools/lib/auto_memory.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md [path] `tools/playbook/memory_index.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md [path] `tools/playbook/memory_index.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md [path] `tools/playbook/memory_index.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md [path] `../outside.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md [path] `tools/playbook/memory_index.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md [path] `tools/memory-tree/import_walk.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md [path] `tools/playbook/check_layers.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md [path] `tools/playbook/check_layers.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md [path] `tools/playbook/check_layers.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-17.md [path] `tools/playbook/check_layers.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-18.md [path] `tools/memory-tree/id_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-18.md [path] `tools/memory-tree/id_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/lib/coverage_join.py)` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/memory-tree/coverage_join.py)` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/playbook/tag_index.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/lib/common_dir.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/playbook/positional-refs.txt` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `json.load(open('tools/gate-legs.json',` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-2.md [path] `tools/memory-tree/build_records.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-2.md [path] `help/charter.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `json.load(open('tools/gate-legs.json',` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-21.md [path] `tools/playbook/load_sets.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-21.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-22.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-22.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-22.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-23.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-24.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-24.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-27.md [path] `tools/playbook/load_sets.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md [path] `json.load(open('tools/gate-legs.json',` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md [path] `tools/playbook/writing_practice.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md [path] `tools/playbook/writing_practice.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md [path] `tools/playbook/unpinned-facts.txt` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md [path] `tools/playbook/doors.toml` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md [path] `tools/playbook/writing_practice.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md [path] `tools/lib/envelope.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md [path] `[.claude/agents/gov-builder.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md [path] `memory/guides/NEW.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md [path] `tools/playbook/practices.toml` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/upgrade_steps.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/steps/adopter_rules_to_overlay.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `tools/govkit/upgrade_steps.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md [path] `help/upgrade-steps.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md [path] `tools/playbook/overlay.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-33.md [path] `tools/playbook/pins.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-33.md [path] `.governance/journal/stale-edges.tsv` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/fixtures/composition.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/practice_census.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `tools/playbook/practices.toml` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [path] `help/composition.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md [path] `help/overlay-rows.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `parser=tools/playbook/fixtures/row_kind.py#read_witness` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md [path] `help/overlay-rows.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md [path] `help/reference/orphan.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md [path] `tools/govkit/docs_leg.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md [path] `tools/govkit/docs_leg.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md [path] `tools/govkit/docs_leg.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md [path] `tools/govkit/docs_leg.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-4.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-4.md [path] `[/AGENTS.md]` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-4.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md [path] `help/charter.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `skills/session-kickoff/card-compaction.fixture.sh` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `.claude/orientation-card.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `@.claude/orientation-card.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `.gemini/settings.json` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `tools/lib/envelope.sh` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `.claude/orientation-card.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `tools/lib/envelope.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-13.md [handoff] `PLAY-dOrderedCharter-13>PLAY-dOrderedCharter-8:LEVELS[1]` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [handoff] `PLAY-dOrderedCharter-15>PLAY-dOrderedCharter-1:resolve_practices` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [handoff] `PLAY-dOrderedCharter-15>PLAY-dOrderedCharter-32:--manifest overlay` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [handoff] `PLAY-dOrderedCharter-15>PLAY-dOrderedCharter-33:Mark` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md [handoff] `PLAY-dOrderedCharter-15>PLAY-dOrderedCharter-33:Successor` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md [handoff] `PLAY-dOrderedCharter-20>PLAY-dOrderedCharter-3:INSTRUCTION_PATHSPECS` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md [handoff] `PLAY-dOrderedCharter-32>PLAY-dOrderedCharter-31:write_overlay_units` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md [handoff] `PLAY-dOrderedCharter-32>PLAY-dOrderedCharter-34:read_overlay` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md [carries] `carries <- stale:cl-dClosedLoop-0064` — pins cl-dClosedLoop-0064@8b8552ab, and the clause's text in the view hashes 42692e4c (a stale pin)
- dOrderedCharter [carries] `carries <- token:cl-dClosedLoop-0046` — cl-dClosedLoop-0046's token `backlog.py` appears in none of its carriers (memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md)
- dOrderedCharter [carries] `carries <- token:cl-dClosedLoop-0046` — cl-dClosedLoop-0046's token `corpus_ids.py` appears in none of its carriers (memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md)
- dOrderedCharter [carries] `carries <- token:cl-dClosedLoop-0046` — cl-dClosedLoop-0046's token `extract.grammar_for` appears in none of its carriers (memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md)
- dOrderedCharter [carries] `carries <- token:cl-dClosedLoop-0046` — cl-dClosedLoop-0046's token `merge-rows.py` appears in none of its carriers (memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md)
- dOrderedCharter [carries] `carries <- token:cl-dClosedLoop-0046` — cl-dClosedLoop-0046's token `transition_audit.py` appears in none of its carriers (memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md)
