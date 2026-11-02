**Serves:** research PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-17

# Brief: PLAY-dOrderedCharter-61 — unit 16's layer check repaired, before unit 17 cures what it finds

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 17's builder (run wf_dce016de-13e) returned
`DIVERGENCE:` before writing code: `python tools/playbook/check_layers.py --list` at `97fc1a153` reports 60 red edges
in 22 files, spec 17's §4 names 12, and many of the rest are no dependency at all. Unit 16 is CLOSED, so its check is
corrected by a new unit on top (BUILD-METHOD M4), and spec 17 is revised to consume it.

## The brief

### Goal

Author the spec of PLAY-dOrderedCharter-61, a repair of unit 16's `tools/playbook/check_layers.py`, so the leg reports
only real dependencies of a core file on a non-core kit; and revise spec 17 so its AC1 is the red set left after 61.

### Items

1. **Spec 61's scope — what the check stops reading as an edge.** Each named from the builder's return, and each
   verified against the source line at HEAD before it is written:
   - message or prose text naming a kit (`tools/memory-tree/check-memory-hygiene.sh:1288`, its `.test.sh:260`);
   - a path under `.git/` that shares a kit's name (`.githooks/pre_push_bar_selftest.py:180`,
     `.githooks/pre-push.test.sh:2279`, `:2281`, `:2573`, `:2584`, `skills/session-kickoff/manifest-check.test.sh:1918`,
     `tools/unattended/unattended.test.sh:1540`);
   - an id string shaped like a path (`tools/push-main.test.sh:1270`, `govkit/planted-witness-fails`);
   - a `{kit}/<name>/` fixture pin (`tools/settings-merge.py:620`);
   - the check's own read of `govkit/entries/*.kit.toml` (`check_layers.py:118`, `:129`), which holds the core kits'
     descriptors.
   The predicate is a class rule (charter `[class]`), never a list of these sites: run the candidate over the real tree
   and write the edge counts before and after into §6.
2. **Spec 61's scope — the test-suite and fixture disposition.** Core kits' suites that build fixtures from an optional
   kit (`push-main.test.sh`, `pre-push.test.sh`, `check-install-prefix.test.sh`, `unattended.test.sh`,
   `check-wiring.test.sh`, `manifest-check.test.sh`) and whole-tree resolvers (`tools/check-kit-versions.sh:243-252`,
   `tools/check-wiring.sh:700`, `:1103`). Decide by M3 between at least two mechanisms (for example: a declared test
   class the check grades separately, or an `optional` row per site with a named fallback), record the loser and the
   test that rejected it (M12), and mark it in §8 as a resolved fork, delegated. A choice that trips veto 2 or 3 is
   parked, not taken.
3. **Spec 61 also carries unit 16's owed guard.** The `playbook render selftest` leg's guard in `tools/gate-legs.json`
   gains `{prefix}/memory-tree/import_walk.py` (class held-suite-guard-misses-a-sibling-kit), with the kickoff
   manifest re-stamped in that commit.
4. **Spec 61's header.** Tier-2, status `DEFERRED`, `order 3`, `streams playbook`, `base 8bec4cef`, `advances
   PLAY-dOrderedCharter-38`; §3 Edges `consumes-from PLAY-dOrderedCharter-16` and `hands-off PLAY-dOrderedCharter-17`.
   Every New arm on a `New arm:` line in §7; every AC observable by a probe of the check, never a gate run.
5. **Spec 17.** Add `consumes-from PLAY-dOrderedCharter-61` to §3 Edges; scope AC1 to the edges `check_layers.py
   --list` reports after unit 61; give §4's table and its rule the disposition spec 61 decides for test suites; extend
   Files touched with what the remaining edges reach. Bump its rev with a §9 line naming this brief.

In every spec you write or revise:

- Follow `memory/TEMPLATE-SPEC.md`; §10 names the seam (`tools/playbook/check_layers.py` and the import walk) and the
  recall terms you used.
- Verify every path, count and line you cite against the tree at HEAD.
- Stay under the 47000-byte authored budget.

For the run:

- Writes stay in the new spec file `memory/builds/dOrderedCharter/spec/2026-11-02-spec-PLAY-dOrderedCharter-61.md`,
  spec 17 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the new spec's path, its AC list in one line each, the §8 decision and its loser, and spec 17's new rev.

### Acceptance

- `grep -n '^# PLAY-dOrderedCharter-61'` prints the new spec's H1, and its Status line reads `DEFERRED` with `order 3`.
- `grep -n 'consumes-from\*\* `PLAY-dOrderedCharter-61`'` prints spec 17's edge.
- Spec 61's §6 carries the before and after edge counts of the class rule over the real tree.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 61 and 17; unit 16's spec stays frozen.

### Limitations

The items above, "For the run".

### Reuse

`tools/playbook/check_layers.py` and `tools/memory-tree/import_walk.py` as unit 16 built them (`cc767f77a`); unit 16's
deviation 163, which records how the check reads edges.
