# KICK-dKeptSession-60 — acceptance ledger

**Serves:** journal KICK-dKeptSession-60

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `3f35841a`
by the criteria's own commands, run in the policy kit's checkout, and by the same commands over the
base's two files, each read with `git show HEAD:<path>` into the session scratchpad, which is the
red side each criterion names. The unit adds no function, constant or other symbol: two texts move,
and `python tools/lexicon/lexicon.py` exited 0 over the change.

Owed to the close: every leg the spec's section 7 names. The spec declares no `New arm:` line, so
no RED-first observation is owed.

**Evidences:** KICK-dKeptSession-60
- AC1 — `awk '/THE RULE:/,/^$/' README.md` in the checkout printed the paragraph from `THE RULE:` to
  the next blank line, and joined into one line it named `LEGACY_INPUTS`, `derive_mirror_inputs`,
  `MIRROR_KIT_INPUTS` and `mirror-input-parity`, all four (DERIVED, that run). Over the base's
  README the same command's paragraph named `LEGACY_INPUTS` alone, one of the four (DERIVED, that
  run): the criterion's red case, observed at the base.
- AC2 — in the checkout, `grep -c "adds its path here" policy.py` printed 0 (DERIVED, that run);
  `grep -n "THE RULE in" policy.py` printed one line, the last of the comment above `LEGACY_INPUTS`,
  naming `tools/policy/README.md` (DERIVED, that run); and the count of the tuple's literal line,
  `LEGACY_INPUTS = (LEGACY_FANOUT, OVERLAY_REL)`, printed 1 (DERIVED, that run). Over the base's
  `policy.py` the first grep printed 1 and the second matched no line (DERIVED, that run): the
  comment's own rule, the criterion's red case, observed at the base.
- The literal line the `guard-mirror-inputs-join` scenario replaces is unmoved, so its replace still
  finds its text; an in-process probe, `python -c` importing `policy` from the kit, read
  `LEGACY_INPUTS` as `.agent-cap.conf` and `.governance/instructions.toml` and
  `derive_mirror_inputs()` as those two then `tools/policy/presets.toml` (DERIVED, that probe), the
  base's values.
- S3 — not observed, as the spec states: a placement of work, which S1's criterion observes.
