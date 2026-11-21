# KICK-dKeptSession-59 — acceptance ledger

**Serves:** journal KICK-dKeptSession-59

No merge bar, no self-test suite and no gate leg ran in this pass, and the `policy fixtures` leg and
the other legs the spec's section 7 names were not run as commands. The criteria were observed on
win32 at the pass's base `244bfb3f` by the unit's own case: `python tools/policy/check_policy.py
--fixture mirror-input-parity`, the one-case form AC1 and AC2 name, which runs that case and the
guard trace's join over its reads and no other case; and by an in-process probe, `python -c`
importing `check_policy` beside `policy` and calling `run_mirror_input_parity` directly. The unit adds
the function `run_mirror_input_parity`, the constant `MIRROR_KIT_INPUTS_RX` and the `CASES` row
`mirror-input-parity`; `python tools/lexicon/lexicon.py` exited 0 over the change.

Owed to the close: every leg the spec's section 7 names, the full `policy fixtures` run with the new
case among its cases; and the RED-first observation of the `New arm:` line in
`tools/policy/check_policy.py`, the case on its staged break, the checkout's `derive_mirror_inputs`
carrying an input the JS list lacks, and green once the edit is reverted. AC2 below is that break
observed once by this pass; the close's observation is still the main loop's.

**Evidences:** KICK-dKeptSession-59
- AC1 — at the base's tree, `--fixture mirror-input-parity` exited 0 (DERIVED, that run). The case's
  line read the kit's two lists equal, `1 input(s) on each side: tools/policy/presets.toml`, the
  JS literal `["presets.toml"]` spelled by `policy.derive_kit_rel` against
  `policy.derive_mirror_inputs()` less `policy.LEGACY_INPUTS`. The guard trace kept 1 source read
  (DERIVED, that run), policy-mirror.js, and the run closed at 91 assertions with 0 wrong (DERIVED,
  that run).
- AC2 — `derive_mirror_inputs` in the checkout's `tools/policy/policy.py` was edited to return
  `derive_kit_rel("extra.toml")` beside the store, the file backed up to the session scratchpad
  first. The same command exited 1 (DERIVED, that run), its case line a `WRONG` naming
  `tools/policy/extra.toml in derive_mirror_inputs alone`, and the run closed at 91 assertions with
  1 wrong (DERIVED, that run). With the backup restored, `git status --short` naming no change to
  `policy.py`, the command exited 0 again (DERIVED, that run), its line AC1's.
- The other direction, a probe — in process, `policy.derive_mirror_inputs` replaced by one dropping
  the store, `run_mirror_input_parity` answered 1 assertion with 1 wrong (DERIVED, that probe), its
  line naming `tools/policy/presets.toml in MIRROR_KIT_INPUTS alone`.
- S1's refusal of a missing or unparseable literal, a probe — in process, `MIRROR_KIT_INPUTS_RX`
  replaced by a pattern matching nothing, the case answered 1 assertion with 1 wrong (DERIVED, that
  probe), saying the JS file holds 0 such literals, not one; replaced by a pattern capturing the
  literal without its closing bracket, it answered 1 with 1 wrong (DERIVED, that probe), naming the
  `JSONDecodeError`. Neither passed.
- S2 — not observed, as the spec states: a placement unit 49's own Non-goals already make.
