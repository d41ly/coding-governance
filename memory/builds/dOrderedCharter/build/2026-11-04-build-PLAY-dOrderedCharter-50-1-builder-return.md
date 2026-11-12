# dOrderedCharter — unit 50's builder return

**Serves:** journal PLAY-dOrderedCharter-50

Run wf_d06c20b0-eef, summarized from its return.

- Built at rev-5 as pass commit `8a76ad2f4`.
- New probe, `tools/run-gates/owed_rows.py`, run as `--base <rev>` or `--selftest`.
  - It derives five populations from the base: leg added, leg removed, key, path deleted, size.
  - It prints each owed row and each deferred ceiling-evidence row.
  - Its `--help` prints the hand-off rule, naming each writer's command.
- Both KNOWN copies in `run-gates.test.sh` gain `enforces`, with a control pair. The floor goes from 405 to 407.
- `tags positional selftest` gets its subject-pins row and a `[[gate_leg]]` in `tools/playbook/kit.toml`.
- The run-gates kit withholds the probe from adopters.
- `Decided:` trailers:
  - A warn-mode size breach is counted, not owed: 26 changed specs sit over the spec-folder cap in warn mode.
  - The fixture's tool root is named `kits`.
  - The probe imports govkit and `map_lib` after `resolve_kit_dir`.
- Observed by probe:
  - AC2: `--base ce13efbe` exits 0 with four deferred evidence rows. It exited 1 before the descriptor and pin rows.
  - AC3: one fixture case per population, red and green.
  - AC1, AC4 and AC5: `git grep` and `python -c` probes.
- No divergence.
- Owed at the close:
  - The bar and the section-7 legs.
  - RED then GREEN for the `New arm:` line in `run-gates.test.sh`: the `enforces` pair and the selftest.
  - `owed_rows.py --selftest` itself, refused to the builder.
  - AC6's replay after the handed-off units land.
  - Re-measuring govkit selftest's project-owned order pin, currently 34, which the withheld file may move.
  - Four ceiling-evidence rows from a measured bar run: `policy check`, `policy fixtures`, `step-rows-frozen` and
    `tags positional selftest`.
