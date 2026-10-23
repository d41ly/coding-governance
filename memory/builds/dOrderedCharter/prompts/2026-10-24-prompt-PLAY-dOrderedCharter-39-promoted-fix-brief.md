**Serves:** research PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49

# Promoted-fix brief — the round-1 promotions, before their commit

Fix the eleven specs the round-1 spec audit's disposal added, `PLAY-dOrderedCharter-39` to `-49`, so
`python tools/check-spec-tokens.py` names no dOrderedCharter spec, changing nothing else.

- The audit record is renamed to `memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`,
  the name hygiene check 5's recording grammar requires. Re-point every citation of the harness's name,
  `2026-10-23-review-PLAY-dOrderedCharter-spec-round1.md`, to it.
- Each `[path]` hit below: cite a file the build run will create by BASENAME in §6, full paths staying in §2, §4 and
  Files touched, as the token-fix pass did; correct a path that is simply wrong.
- The `[size]` hit: `PLAY-dOrderedCharter-49` is 53135 B against the 49152 B ceiling in
  `tools/template-size-limits.txt`. Trim it under the ceiling with every finding id, criterion and fork kept, by
  tightening prose, never by splitting it: M4 admits a second batch unit only on disjoint write sets.
- The specs are uncommitted at rev-1, so edit them in place with no rev bump. Touch no deviation record and no spec
  numbered 1 to 37.
- Do not commit, do not stage, do not run the build-index generator. Report each file changed and spec 49's size.

## The hits, verbatim

- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-40.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-40.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-40.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-41.md [path] `tomllib.load(open('tools/govkit/entries/playbook.kit.toml','rb'))['block']` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-41.md [path] `help/charter.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md [path] `tools/memory-tree/build_records.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-43.md [path] `@.claude/orientation-card.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-44.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-45.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-46.md [path] `tools/playbook/overlay.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md [path] `tools/playbook/positional.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md [path] `tools/notes.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-48.md [path] `tools/playbook/positional.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-48.md [path] `tools/playbook/positional-producers.txt` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-48.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/gov_tag.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/instruction_units.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/instructions_edit.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/memory-tree/id_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/practices.toml` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `help/overlay-rows.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `help/charter.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `help/composition.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `help/upgrade-steps.md` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/fixtures/row_kind.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `.governance/instructions.lock` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/lib/coverage_join.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/edge_grammar.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/edge_checks.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/writing_practice.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `memory/project/chain.toml` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/playbook/core.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [path] `tools/lib/auto_memory.py` — not tracked by git ls-files
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md [size] `size <- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md` — 53135 bytes, 3983 over the spec ceiling 49152; split the spec or move history out of it
