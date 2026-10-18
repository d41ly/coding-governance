# Brief — aScoutedSeam: DEPL-aScoutedSeam-1 follows TOOL-aScoutedSeam-3 rev-5, and TOOL-aScoutedSeam-1 back under its ceiling

**Serves:** research DEPL-aScoutedSeam-1 TOOL-aScoutedSeam-1

## The prompt

> first, record the prompt-writing method that improved the result, then go with 1, then 2. But also, add testing 'low' effort vs 'medium' in scope, based on the same or further improved prompting method to see the difference.

## The brief

### Goal
Carry the TOOL-aScoutedSeam-3 rev-5 fold into the two specs it left inconsistent or oversized. DEPL-aScoutedSeam-1
stops telling adopters to set a `high` diff level, and TOOL-aScoutedSeam-1 gets back under the 49152-byte
spec ceiling. This pass touches the specs only: no product code, and no commit.

### Items
1. **DEPL-aScoutedSeam-1, S4 adopter checklist (around line 116):** delete the item that tells adopters to
   add `[effort.stages.reuse] diffCheck = "high"`. TOOL-aScoutedSeam-3 rev-5 runs diff mode at the agent
   type's own level, `medium`, with no policy override. The measured reason is
   `2026-10-18-build-TOOL-aScoutedSeam-1-12-judge-and-low.md`. If an adopter still needs a step for diff
   mode, it is the one rev-5 names; verify that against the TOOL-aScoutedSeam-3 spec before writing it.
2. **DEPL-aScoutedSeam-1, the matching spots:** update the edge at line 145 (it consumes the `diffCheck`
   stage key, and no policy line), and the criteria and §5/§10 text that count the checklist items or
   the policy line (lines 230, 233 and 257). The checklist count changes; restate it.
3. **TOOL-aScoutedSeam-1:** cut at least 600 bytes with no change of meaning. The overflow is 282 bytes, and
   the rest is headroom for later rows. The generated records region grew by five rows, because the
   records `-1-10` to `-1-12` belong to TOOL-aScoutedSeam-1's numbered series. The generated region
   cannot be edited. Cut authored text: resolved forks can shrink to their ruling and the record that
   decided it, and repeated rationale can point at its record. Do not touch scope items, criteria or the
   gate line.
4. **§9 in each spec:** one revision line naming what moved.

### Acceptance
Both specs carry their §9 line, and DEPL-aScoutedSeam-1 no longer names `diffCheck = "high"`.
TOOL-aScoutedSeam-1 is at most 48552 bytes after the main loop re-renders the indexes.
`python tools/check-spec-tokens.py`, `python tools/memory-tree/gen_build_index.py --check` and
`--check-format` pass.

### Gates
memory hygiene · spec tokens (a spec's own names resolve) · build README slot contract

### Non-goals
- No product code, and nothing under `tools/`, `skills/` or `.claude/`.
- No edit to TOOL-aScoutedSeam-3, KICK-aScoutedSeam-1 or TOOL-aScoutedSeam-2.
- No change to unit ids, order or titles, and no commit, which is the main loop's.

### Limitations
The records region of TOOL-aScoutedSeam-1 is generated, and its size is measured after the re-render.

### Reuse
The resolved-fork shape already used in TOOL-aScoutedSeam-1 §8, and TOOL-aScoutedSeam-3 rev-5's S6 and S7 text.

## Owner confirmation

Asked: option 2, folding the measured diff mode into TOOL-aScoutedSeam-3, was the owner's pick. This brief
carries that fold's direct consequences: DEPL-aScoutedSeam-1's checklist line it made stale, and the spec ceiling
its records pushed TOOL-aScoutedSeam-1 over.
Answer: "first, record the prompt-writing method that improved the result, then go with 1, then 2. But also, add
testing 'low' effort vs 'medium' in scope, based on the same or further improved prompting method to see the difference."
