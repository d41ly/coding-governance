# TOOL-dWitnessedBar-46 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-46

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the manifest read
with the spec's AC1 `python -c` line after `leg_factory.py --write`, the descriptor counted with `grep -c`
and `tomllib`, and a scratch `git init` at `%TEMP%/w46` holding the kit copied to `tools/memory-tree/`
and the example copied to `.memory-tree.conf`, both staged before `--scaffold`, then committed. The leg
`ratchet (keys, not a scalar)` was observed by calling `ratchet.run_keys_not_scalar` from `python -c`
in that tree, because the role hook refuses the leg's own argv. Check 3 over the seeded home was not
observed: only the hygiene gate runs it, so AC2's check-3 half is owed to the close. The `New arm:` of
spec section 7, the scalar-pins arm of `tools/memory-tree/check-memory-hygiene.test.sh`, was written
and checked with `bash -n` only; it owes its RED-first observation at the close, and so does every leg
that section names.

**Evidences:** TOOL-dWitnessedBar-46
- AC1 — `tools/gate-legs.json` — the spec's `python -c` printed the nine ratchet legs, the seven of S5
  each tagged `leg.gov.<slug>` and `ratchet (keys, not a scalar)` and `ratchet selftest` tagged
  `leg.memory-tree.<slug>`; against HEAD's manifest every other field of all nine rows read equal.
  `grep -c '^\[\[gate_leg\]\]' tools/memory-tree/kit.toml` read 24 at the parent and 17 after, and
  `tools/govkit/registry.toml` held 130 `[[exempt_leg]]` rows at the parent and 137 after, the seven
  naming the moved legs.
- AC2 — `adopt-memory-tree.sh --scaffold` — over the example-made tree it printed `armed
  conf-scalar-pins 5`, exit 0; after the commit `run_keys_not_scalar` printed five `held` rows, each
  `.memory-tree.conf` and one of `DEAD_PATH_PIN`, `LIVE_ROW_PIN`, `ORPHAN_ID_PIN`,
  `ROW_DUPLICATE_PIN` and `SEVERITY_UNLABELLED_PIN`, then `pass · 1 populations graded`, returning 0.
  Five matches `grep -cE '^[A-Z_]+_PIN=' tools/memory-tree/.memory-tree.conf.example`. Owed at the
  close: check 3 passing with `conf-scalar-pins.txt` present.
- AC3 — `unarmed conf-scalar-pins` — with the home removed it printed `ratchet (keys, not a scalar) ·
  unarmed conf-scalar-pins · its home is absent · seed it: python
  tools/memory-tree/legacy_ledger.py seed --population conf-scalar-pins` and returned 1.
- AC4 — `--seed-pins` — run in the committed tree with the home deleted it printed `armed
  conf-scalar-pins 5`, exit 0, the home held the `ROW_DUPLICATE_PIN` row, and `run_keys_not_scalar`
  then returned 0; a second run printed `present conf-scalar-pins`, exit 0, and `cmp` found the home
  byte-identical. `tomllib` read one `[[regenerate]]` row of `tools/memory-tree/kit.toml` whose argv
  ends `--seed-pins`, carrying no `stage`. Outside the criterion: in a tree whose kit is not staged,
  `--seed-pins` printed the seed's refusal and the command to run once the kit is committed, exit 0.
