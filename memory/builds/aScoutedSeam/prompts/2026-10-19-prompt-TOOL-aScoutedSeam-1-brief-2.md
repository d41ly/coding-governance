# Brief — aScoutedSeam: TOOL-aScoutedSeam-1's gate line names the leg main's newer guard demands, and the spec stays under its ceiling

**Serves:** research TOOL-aScoutedSeam-1

## The prompt

> can we add a set of cases that will not be specifically tuned for as an extra test group (the prompt case should still account for them), then go through your 1, 2, and 3 suggestions in the order. Once done, compile a final workflow design set that any other session would be able to use and adjust its processes to the best results discovered. Merge and push.

## The brief

### Goal
The landing merge of aScoutedSeam onto local main (`125798c31`) reds the spec-tokens gate on
TOOL-aScoutedSeam-1. Main's gate manifest carries a newer `govkit selftest` leg whose guard covers
`tools/codebase-map/kit.toml`. That file is named in the spec's §4 files-touched list, and the leg is
absent from its §7 gate line. This pass fixes the gate line and keeps the spec under the size ceiling.
It touches the spec only: no product code, and no commit.

### Items
1. **§7:** add `govkit selftest` to the gate line. Verify the leg's exact name and guard in
   `tools/gate-legs.json`, and confirm that `python tools/check-spec-tokens.py` reports no `[guards]` hit
   for this spec afterwards.
2. **Size:** the spec is 49126 B against the 49152 ceiling, and this brief adds a row to its generated
   records region. Cut at least 600 authored bytes, with no change of meaning, so the spec stays under the
   ceiling after the main loop re-renders the indexes. Resolved forks can shrink to their ruling and the
   record that decided it, and repeated rationale can point at its record. Do not touch scope items,
   criteria, or any part of the gate line other than item 1.
3. **§9:** add one revision line naming what moved.

### Acceptance
`python tools/check-spec-tokens.py` reports no unwaived hit, and TOOL-aScoutedSeam-1 is at most 48552
bytes after the main loop runs `python tools/memory-tree/gen_build_index.py --write`.
`gen_build_index.py --check` and `--check-format` pass.

### Gates
spec tokens · memory hygiene · build README slot contract

### Non-goals
- No product code, and nothing under `tools/`, `skills/` or `.claude/`.
- No edit to any other spec.
- No change to unit ids, order or titles, and no commit, which is the main loop's.

### Reuse
The resolved-fork shape already used in TOOL-aScoutedSeam-1 §8, and the cut made under
`2026-10-18-prompt-DEPL-aScoutedSeam-1-brief-2.md`.

## Owner confirmation

Asked: nothing new. This is a direct consequence of the owner's "Merge and push": the landing merge
redded a gate, and the bar must be green at the push boundary.
