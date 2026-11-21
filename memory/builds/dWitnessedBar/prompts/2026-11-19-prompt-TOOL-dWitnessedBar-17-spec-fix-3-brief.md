**Serves:** journal TOOL-dWitnessedBar-17

# Brief — dWitnessedBar: TOOL-dWitnessedBar-17's empty-decisions seed moved off the map generator

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 17's third dispatch was refused at check 49: the rev-8 spec puts the
`dossier-decisions-empty` seed verb in `tools/codebase-map/gen_map.py`, the generator of `memory/map/generated/`, and
the unit's two earlier dispatch rows, which stand until its pass commit, reserve `memory/map/generated/symbols.json`.
A declaration that pairs a generated index with its generator is the one pairing condition 3 forbids.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
its Files touched names no generator of `memory/map/generated/` and `--dispatch` admits it.

### Items

1. Move the `--list-empty-decisions` seed verb out of `tools/codebase-map/gen_map.py` into a codebase-map file the
   kit's descriptor ships with role `engine` (every adopter holds it at `{prefix}/codebase-map/`) that renders no
   generated index: read `tools/codebase-map/kit.toml`'s `[[files]]` rules for the role, and the file's own `main`
   for what it writes. Restate §4 "The pins", S8, AC4, AC10, §8 F10 and Files touched for the new home; drop
   `gen_map.py` from Files touched unless another clause still edits it, and say so if one does.
2. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. Leave carried clause tokens byte-identical;
   blob-pin only code-file line citations.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-17`,
`python tools/check-spec-tokens.py --spec <path>`, `python tools/playbook/writing_practice.py check pinned-facts` and
`python tools/memory-tree/gen_build_index.py --check-coverage`, and fix every finding about this spec they name. Write
no numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

The four commands report nothing against this spec; Files touched names no `gen_map.py`; the spec carries the next
rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-17. No product code. The status header keeps its status.

### Limitations

The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-17.md` alone.

### Reuse

The spec's §10 seam; `tools/codebase-map/map_lib.py#load_map_tree`, which the seed already reads through.
