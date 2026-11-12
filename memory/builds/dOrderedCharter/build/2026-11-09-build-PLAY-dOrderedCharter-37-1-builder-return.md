# dOrderedCharter — unit 37's builder return

**Serves:** journal PLAY-dOrderedCharter-37

Runs wf_251b8704-3ac and wf_7a5003b1-6c2, summarized from their returns.

- The first run was refused at `--dispatch` before any write: parked unit 31's open dispatch row still reserved paths this unit needs.
  Spec 31's rev-12 commit `9e16b1b49` carried unit 31's pass trailer and released it.
- Built at rev-7 as pass commit `19648821f`, with no hand-back; spec 37 rev-7 had folded a read-only pre-check against HEAD.
- What the unit landed:
  - `render_playbook.py --reference` and `--reference --check`, rendering the policy, drive and kinds pages from
    `tools/playbook/references.toml`, with a selftest arm `check_reference_arms`.
  - The docs leg's `synopsis` shape, `--fingerprints` and `--run`, which runs every page's fenced commands in a scratch adopter.
  - The drive and kind classes in the step gate, the concept, task and tutorial pages, `run: no` markers on today's pages, and two
    gate legs, `help reference pages` and `help page commands`.
  - Deviations 374, 375 and 376: the legs' registry, subject-pin and dossier rows; the tutorial's five kits and its charter answers
    written as a table; the `expect` marker's block scope.
- Observed by probe in scratch clones: each reference criterion, its plants and the selftest arm; the run arm over every page with a
  planted failing page; the drive and kind plants.
- Left for the later commit after unit 40's rows: the units row and page, every row's `unit` field, the unit-line check, and the
  unit-usage class rows.
- Refusal sites with no arm yet: the reference renderer's declaration, page-path, empty-declaration, fingerprint and reader refusals;
  the fingerprint reader's leg failure; the docs leg's page outside `help/`; the run arm's nothing-ran exit; the three plant writers'
  nothing-to-remove errors.
- Owed at the close: RED then GREEN for the new arms; the docs, step-gate, both new legs, canary, core kinds and tags legs; ceiling
  evidence for both new legs. The docs leg was red at HEAD before this pass on seven rows of `help/charter.md` and `help/roles.md`.
