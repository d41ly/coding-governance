**Serves:** research TOOL-aLightenedLoop-6

# Stamp fold — TOOL-aLightenedLoop-6: the render stamp's key race joins the repair unit

## The prompt

> Unit 6's spec writer found a sibling of review item M3 in unit 1's code: `cmd_write` in gen_build_index.py derives the render-stamp key AFTER the render, so an edit landing between the render and the key derivation would be stamped as already rendered, and the next `--check --staged` would wrongly skip. The push-boundary full render still catches it. Fold this fix into unit 6?

Answer: "Fold into unit 6 (Recommended)"

## The brief

### Goal
Add a ninth item to TOOL-aLightenedLoop-6's spec: `cmd_write` in `tools/memory-tree/gen_build_index.py` must never stamp a render with a key derived from a tree that moved after the render read it. Bump the rev and add a §9 line naming this record.

### Items
1. S-new: derive the render stamp's key from the same inputs the render read. Either derive it before the render and refuse to stamp when a re-derivation after the render differs, or use another order that closes the window. A moved tree writes no stamp, so the next `--check --staged` renders in full. The fix takes the same shape as M3 in the driver.
2. An arm with its staged break: a `--write` whose inputs move between the render and the stamp leaves no stamp, and it goes red when the stamp is written anyway.
3. Move this race from §3's hands-off edge into scope.

### Acceptance
The spec's §8 has no unresolved item. It carries a rev bump and a §9 line naming this record, and a `New arm:` line for item 2. `python tools/check-spec-tokens.py --spec <path>` exits 0 on it.

### Gates
The spec-token check and memory hygiene, as the role's gates.

### Non-goals
No other change to the spec, and no code.

### Limitations
The build brief's limitations hold: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`. The owner's `[class]` override for the staged stamp stands.

### Reuse
`tools/memory-tree/gen_build_index.py#derive_render_key` and `tools/memory-tree/gen_build_index.py#resolve_render_stamp`, from unit 1.
