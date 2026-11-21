**Serves:** journal TOOL-dWitnessedBar-18

# Brief — dWitnessedBar: TOOL-dWitnessedBar-18's empty-list state settled on the landed converter

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 18's second builder stopped before writing code: §4 Migration
and §5 disagree about what an empty list converts to, and the landed converter agrees with §5.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
every clause about an empty list names one state and a builder can build it as written over HEAD.

### Items

1. Read the builder's return, `build/2026-11-19-build-TOOL-dWitnessedBar-18-2-builder-return.md`, whole.
2. Restate §4 Migration for what `tools/memory-tree/convert_registry.py#derive_converted_text` writes for a home with
   no row (the header and the factory's unarmed line), so it agrees with §5; unit 16's converter is outside this
   unit's write set.
3. Settle S5's `write_empty_lists` on the state a fresh target's empty list holds, so a converted target and a fresh
   one read the same. The choice is a fork for item 5; the state the converter already writes needs no new reader.
4. Say what a list WRITER does when no registration names its population (the return's secondary gap), in one
   clause beside S5's reader refusal.
5. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. Prefer the option that removes text. Leave
   carried clause tokens byte-identical; blob-pin only code-file line citations.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-18`,
`python tools/check-spec-tokens.py --spec <path>`, `python tools/playbook/writing_practice.py check pinned-facts` and
`python tools/memory-tree/gen_build_index.py --check-coverage`, and fix every finding about this spec they name. Write
no numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

The four commands report nothing against this spec; the spec carries the next rev and one revision-log line naming
this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-18. No product code. The status header keeps its status.

### Limitations

The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-18.md` alone.

### Reuse

`tools/memory-tree/legacy_ledger.py#read_home_state`, which names the states a home can read.
