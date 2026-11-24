**Serves:** research KICK-dKeptSession-1

# Brief — dKeptSession: KICK-dKeptSession-1's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-1's builder returned a DIVERGENCE (run `wf_c7d6ba36-6f3`) at rev-5 and committed nothing. Two gaps
the design depends on: (1) the fixture cases that reach the loop kit (`presets-core-only`, and the load halves of
`presets-complete` that need `guard.py`) copy the loop and playbook kits into the scratch repository inside the
`--fixture` process, so the guard trace records each read, and the `policy fixtures` guard in `tools/gate-legs.json`
covers neither `tools/loop/` nor `tools/playbook/layers.toml`, so every such read grades WRONG; the spec's Files
touched calls the `tools/gate-legs.json` edits already satisfied, and they are not. (2) Nothing says what
`arm_presets` does where the loop kit does not resolve, as in `adopter-fresh-target`, whose install closure holds
policy, run-gates and memory-tree only: under S4 the load there exits 2 naming the kit, and with `empty = "finding"`
the arm would red that adopter's `policy check`. Revise the spec to the main loop's rulings below.

### Items

1. F-guard: Files touched gains `tools/gate-legs.json`: the `policy fixtures` guard gains the paths the fixture's copy reads, the loop kit and the playbook kit's `layers.toml` (the narrowest entries that cover every read the guard trace records; a whole-kit entry where the copy is the whole kit). Correct the rev-5 claim that the edit is already satisfied, and name the leg line's legs this path trips.
2. F-unresolved-loop: add to the open-questions section, resolved by the main loop at rung 3: where `resolve_kit_dir("loop", ...)` misses, the arm's two load halves print an announced skip in the shape the loop kit's own cross-kit reads use (`not graded · the loop kit does not resolve`), never a finding, so an adopter without the loop kit reads its `policy check` clean with the halves announced. S5, the readiness checklist and the README's "Each arm in an adopter" row say so, and a criterion observes it in the fresh target.
3. Re-cite every line you change as `path#symbol`, keep the spec within the live-spec size cap, pin every figure with DERIVED or PINNED, and leave no fork open.

### Acceptance

The spec at rev-6 carries both rulings and one revision-log line naming this brief by its file stem;
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-1` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (the spec stays INPROGRESS), and no spec other than
KICK-dKeptSession-1's. Other writers are re-grounding later orders' specs at the same time: read them, never write them.
