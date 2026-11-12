# dOrderedCharter — unit 6's builder return

**Serves:** journal PLAY-dOrderedCharter-6

Runs wf_3431b0d6-93a and wf_5187a6e2-875, summarized from their returns.

- The first run handed back a divergence before any write: under the selection rule, the gate-bar row seeded in the run-gates kit could
  never reach gov's charter, and a selected flat entry with no shipped descriptor would refuse a render. Spec 6 rev-10 resolved both.
- Built at rev-10 as pass commit `8221b660d`.
- What the unit landed:
  - 18 drive rows across eight kit descriptors, the gate-bar row in push-main; every role and all five start situations covered.
  - The charter template's drive section, composed by `render_playbook.py` from each selected kit's rows; 11 shipping rules for the flat
    entries' descriptors; `AGENTS.md` re-rendered at 19197 of 20480 bytes.
  - `instruction_units.py drive --list` and `drive --check`, with six plants; unit 3's `plant_envelope_text` renamed `write_envelope_text`,
    which returns the lexicon to its pin.
  - The handoff's `### Drive` block, the size gate's codex-cap check with its arm, the `budgets.py home` verb with its policy case, and
    the help pages.
- Observed by probe: AC1 to AC8. AC5's probe used `--role gov-builder`, since the CLI refuses the spec's `--role builder`.
- The policy kit's version markers moved from 1.3 to 1.4 because the spec's section on the cap home verb says so, against the brief's rule
  that a branch bumps no kit version.
- Owed at the close: RED then GREEN for the policy case, the size-gate arm and the six plants; the section-7 legs; the tags leg; the
  roles suites' handoff pins, the playbook render selftest, and the govkit selfcheck over the new shipping rules.
- Left open: a render that finds drive rows but no roles kit orders them by kit with no note; `drive --check` flags it.
