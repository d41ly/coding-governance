# KICK-dKeptSession-40 — acceptance ledger

**Serves:** journal KICK-dKeptSession-40

No merge bar, no self-test suite, no gate leg and no `check_policy.py --fixture` run ran in this
pass. The `policy fixtures` leg and the other legs the spec's section 7 names were not run as
commands. The criteria were observed on win32 at the pass's base `40c5217f` by probes of the unit's
own code: `run_mirror_landed("mirror-presets-stale")` called from a `python -c` script in
`tools/policy/`, building its scratch repository and bare remote under `%TEMP%` as the case does,
with `GOV_REMOTE`, `GOV_DEFAULT_BRANCH` and the `GIT_*` variables unset as `run_fixture` unsets
them; the kit's own CLI in gov's checkout; and `grep`. The two new names, `derive_kit_rel` and
`derive_mirror_inputs`, are `derive_` verbs, and `python tools/lexicon/lexicon.py` exited 0.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` run of the new
`mirror-presets-stale` case among them; the RED-first observation of the `New arm:` line in
`tools/policy/check_policy.py`, the case on its staged break, a copy of the kit whose input list
omits the store, and green once restored; and AC4, whose render this pass does not write:
`.governance/policy.json` sits outside the write set the main loop declared, a generated output
beside its generator `policy.py`, so the landing's `regen.py --write` or the main loop renders it.

**Evidences:** KICK-dKeptSession-40
- AC1 — `grep -n "def derive_kit_rel\|def derive_catalogue_rel" policy.py` in `tools/policy/` printed both definitions, and `derive_catalogue_rel`'s body is the one line `return derive_kit_rel(CATALOGUE)`.
  `git rev-parse --show-prefix` is read in `policy.py` by `derive_kit_rel` for a kit file, the two
  list readers that take a `kit` argument apart.
- AC2 — `policy-mirror.js get hooks.bypass --explain` at L exited 0 printing `allowed`, its stderr line `policy: hooks.bypass · preset · mirror stale at <L8>; preset strict at <L8>, upstream/main, the landed revision`, and `arm_mirror_landed` found nothing.
  That closing arm read 0 finding(s) over the 3 key(s) the policy file sets (DERIVED, that probe:
  `preset`, `policy-file.on-invalid` and `runtime.agents-in-flight`); the case returned 3
  assertions, 0 wrong (DERIVED, that probe).
- AC2, red side — with `policy.derive_mirror_inputs` replaced in process by one answering `LEGACY_INPUTS` alone, the mirror read FRESH and the helper answered `refused`.
  That is strict's value at L, with no `mirror stale at`; 3 assertions, 1 wrong (DERIVED, that
  probe). The copy's own `policy.py` is gov's file, so AC3's red needs the arm's staged break and is
  owed.
- AC3 — in that case's repository the copy's `policy.py mirror --print` exited 0, its `legacy_blobs` naming `.agent-cap.conf`, `.governance/instructions.toml` and `tools/policy/presets.toml` (DERIVED, that probe).
- AC4, owed — `python tools/policy/policy.py mirror --print` in gov's checkout records `tools/policy/presets.toml` under `legacy_blobs`, and `python tools/policy/policy.py mirror --check` exits 1 naming `legacy_blobs` (DERIVED, that probe at 40c5217f).
  gov's committed mirror predates the input until it is rendered, which this pass does not write.
- AC5 — `grep -n "legacy_blobs" policy.md` in `help/` printed the guard section's one line, which names the policy kit's `presets.toml` and opens the list of its three inputs.
  The fanout conf and the instruction overlay follow it in that list.
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `mirror-presets-stale`: the input list omits the store
