# TOOL-dWitnessedBar-45 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-45

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19, in a scratch
target at `%TEMP%/w45b`: a `git init` given `govkit.py intake` and `govkit.py apply --kits run-gates`
and committed, which landed the kit's committed bytes and no govkit, then this pass's `regen.py`,
`leg_factory.py` and `kit.toml` copied over the landed ones and committed. Before the overlay, at
`%TEMP%/w45a`, the same tree showed the defect: `regen.py --check` exited 1 naming the factory's item
STALE on a `leg-factory: refused · no govkit kit holding govkit.py` line, and `--conform` exited 2. The
`New arm:` of spec section 7, section 8 of `tools/run-gates/adopt-run-gates.test.sh`, was written and
its commands probed one by one outside the suite; it still owes its RED-first observation, which the
main loop makes at the close, and so does every leg that section names.

**Evidences:** TOOL-dWitnessedBar-45
- AC1 — `regen.py --list` — exited 0 printing the factory's row skipped, `[[generated]]` and
  `{kit}/../gate-legs.json` followed by `its when exists:{prefix}/govkit/govkit.py does not hold`,
  and `1 declared`; `regen.py --check` exited 0, its one item, the pass-leg field, fresh. In gov's tree `build_items`
  over the tracked descriptors still made the factory's write an item, the `when` holding there.
  `check_when` refused `exists:`, `exists:{bogus}/x`, `nonsense` and `.unattended.conf:KEY`, and read
  the conf form as before.
- AC2 — `import leg_factory` — `python -c "import leg_factory"` in the target's kit dir exited 0;
  `leg_factory.py --write` exited 2 printing `no govkit kit holding govkit.py in this install` and
  `looked in` with the receipt and the two probe paths, and no traceback; `--check`, `--list`
  and `new` exited 2 the same way. `--sources` does not exist yet: TOOL-dWitnessedBar-28 adds it.
- AC3 — `fresh: not graded here — no govkit` — `run_conform` over the target printed it,
  `enforces: not graded here — no govkit` and `conform · green`, exit 0, over the three untouched
  `[[gate_leg]]` rows. With a `subject = "maybe"`, a `{gate_file}` argv token and a declared `pass_leg`
  planted and committed, it exited 1 naming the `subject`, `token` and `derived` arms. In gov's
  path, over the leg factory's own fixture, `run_conform` exited 0 and, with `practice.unheard`
  planted, named the `enforces` arm, exit 1.
