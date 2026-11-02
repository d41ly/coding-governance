**Serves:** research PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17

# Brief: unit 16's divergence — the policy kit, the thirtieth descriptor

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 16's builder (run wf_1a98f5d3-bd0) returned
`DIVERGENCE:` before writing code: the spec counts 29 kit descriptors at its base `ce13efbe`, and the pinned base
`8bec4cef` holds 30. The thirtieth is `tools/policy/kit.toml`, added by TOOL-dGroundRules-1 (`c9bd97720`,
2026-10-23), and the layer table the spec reads does not name it.

## The brief

### Goal

Revise spec 16 so it builds against the tree at the pinned base, the policy kit given its layer, and make spec 17
agree.

### Items

1. **The policy kit's layer is Instruction, core.** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`
   `[fit]` places "Policies, principles — one policy file" in the Instruction layer, and core kits read the policy
   kit (`.githooks/pre-push`, `skills/session-kickoff/manifest-check.sh`, `tools/memory-tree/gen_build_index.py`,
   `gotchas.py`, `check-memory-hygiene.sh`, `check-verdict-epoch.sh`, `merge-rows.sh`, `adopt-memory-tree.sh`,
   `tools/playbook/adopt-playbook.sh`, `tools/process-monitor/adopt-process-monitor.sh`, and hooks tests). An
   expansion layer would make each of those a red edge no unit cures, which fails spec 16's own acceptance (M3
   veto 1). Record it in §8 as a resolved fork naming this derivation, with no owner mark.
2. **Spec 16's population.** S2 and AC8 read the descriptor count derived from `git ls-files 'tools/*/kit.toml'` at
   the pass, never a pinned 29; §4's kit-to-layer assignment names the policy kit; Files touched adds
   `tools/policy/kit.toml`.
3. **Spec 17.** Read it for the same 29-kit assumption and for a hands-off list written against 29 kits. Where the
   policy kit's edges change what unit 17 must cure (core to core needs no slot), revise spec 17 to agree; where
   nothing changes, leave it and say so in the return.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-02, the status kept `DEFERRED`, and add one §9 line naming this brief
  and the divergence.
- Verify every path, count and line you cite against the tree at HEAD before writing it.
- Stay under the 47000-byte authored budget.

For the run:

- Writes stay in specs 16 and 17 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: if the layer cannot be written as item 1 derives it,
  write nothing and say why in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev and the lines that now carry the count, the policy kit's layer and spec 17's change.

### Acceptance

- `grep -n 'tools/policy/kit.toml'` prints spec 16's Files touched line and its layer assignment.
- `grep -n '29 descriptors\|29 kit' ` over spec 16 prints nothing.
- Each revised Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 16 and 17; no edit of the layer-instruction record, which is dClosedLoop's.

### Limitations

The items above, "For the run".

### Reuse

The layer table and `[fit]` in the layer-instruction record; spec 16's own §4 Data model.
