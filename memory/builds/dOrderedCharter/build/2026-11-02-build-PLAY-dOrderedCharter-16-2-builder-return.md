# dOrderedCharter — unit 16's builder returns

**Serves:** journal PLAY-dOrderedCharter-16

Runs wf_1a98f5d3-bd0 and wf_945c6430-4f6, summarized from their returns.

- wf_1a98f5d3-bd0 returned `DIVERGENCE:` before any write: rev-3 counted 29 kit descriptors at `ce13efbe`, and the
  pinned base holds 30, `tools/policy/kit.toml` included. The spec writer revised spec 16 to rev-4 and spec 17 to
  rev-3 under `prompts/2026-11-02-prompt-PLAY-dOrderedCharter-16-divergence-brief.md`.
- wf_945c6430-4f6 built rev-4 as pass commit `cc767f77a` (53 files): `tools/playbook/layers.toml` with 12 layer rows,
  `layer =` on all 30 descriptors, `tools/playbook/check_layers.py`, `tools/memory-tree/import_walk.py` lifted out of
  `check-verdict-epoch.sh`, the plant arm in `adopt-playbook.sh --selftest`, and the leg `layer dependencies (the core
  never depends on an expansion)` with its rows. Deviation 163 (`report`) records the extra helpers and how edges are
  read.
- The leg reads red over the tree, 58 edges, until PLAY-dOrderedCharter-17's pass, as §4 Rollout and F3 intend.
- Observed by probe: AC1 to AC10 as the ledger records.
- Owed by the checklist: the `playbook render selftest` leg's guard in `tools/gate-legs.json` names only the
  playbook kit and now reads memory-tree's `import_walk.py` (class held-suite-guard-misses-a-sibling-kit). The write
  gate refused the edit once the spec was CLOSED; it is handed to PLAY-dOrderedCharter-17's brief.
- Owed at the close, RED then GREEN: the new leg on a deleted `optional` row after unit 17; the plant arm in
  `adopt-playbook.sh --selftest`; arm 5g in `check-verdict-epoch.test.sh`. Also AC1's before/after run of the
  verdict-epoch gate, and AC8's all-allowed reading after unit 17.
- The builder's first `--dispatch` hit its 590 s bound; the re-run in the background took 10m45s.
