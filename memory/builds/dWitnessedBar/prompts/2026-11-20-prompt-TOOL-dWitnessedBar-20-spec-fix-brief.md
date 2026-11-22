**Serves:** journal TOOL-dWitnessedBar-20

# Brief — dWitnessedBar: TOOL-dWitnessedBar-20's third caller of the graded check

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 20's first builder stopped before writing code: S5 names two
callers of `check_legacy_graded`, and a third, a fixture case the new rule turns red, is not named.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
every caller of `check_legacy_graded` is named with its expectation and a builder can build it as written over HEAD.

### Items

1. Read the builder's return, `build/2026-11-19-build-TOOL-dWitnessedBar-20-1-builder-return.md`, whole.
2. Name `tools/policy/check_policy.py#run_census_source_receipt` as a caller and reader of `check_legacy_graded` in
   S5's Readers, and re-run S2's by-name sweep with `check_legacy_graded` in its pattern; list any further reader it
   finds.
3. Choose that case's expectation under the new rule: (a) a source-mode answer pairs with `graded` false in a tree that
   tracks no registration and holds no home, or (b) the case commits the registry and plants the home so `graded`
   stays true. Add the policy kit README's `census-source-receipt` paragraph to S10, and an acceptance criterion or
   case note that observes the choice. The choice is a fork for item 4.
4. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. Prefer the option that removes text. Leave
   carried clause tokens byte-identical; blob-pin only code-file line citations.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-20`,
`python tools/check-spec-tokens.py --spec <path>`, `python tools/playbook/writing_practice.py check pinned-facts` and
`python tools/memory-tree/gen_build_index.py --check-coverage`, and fix every finding about this spec they name. Write
no numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

The four commands report nothing against this spec; the spec carries the next rev and one revision-log line naming
this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-20. No product code. The status header keeps its status.

### Limitations

The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md` alone.

### Reuse

The spec's §10 seam; TOOL-dSafePassage-103's `census-source-receipt` case as the caller's origin.
