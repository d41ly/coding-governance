# KICK-dKeptSession-49 — acceptance ledger

**Serves:** journal KICK-dKeptSession-49

No merge bar, no self-test suite, no gate leg and no `check_policy.py --fixture` run ran in this
pass. The `policy fixtures` leg and the other legs the spec's section 7 names were not run as
commands. The criteria were observed on win32 at the pass's base `d3b51e46` by probes of the unit's
own code: a scratch script that builds AC1's fixture with `build_landed_repo` exactly as the new
`mirror-pre-unit-stale` branch does, its scratch repository and bare remote under `%TEMP%`, and runs
`node policy-mirror.js get hooks.bypass --explain` there through the edited reader and through a
copy of the reader at the base beside it; and `tr`, `grep` and `git diff` over the tree. The unit
adds no function, only the constant `MIRROR_KIT_INPUTS`.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` run of the new
`mirror-pre-unit-stale` case among them, and of `mirror-presets-stale`, whose own copy loop this
unit removed for `MIRROR_KIT_FILES`; and the RED-first observation of the `New arm:` line in
`tools/policy/check_policy.py`, the case on its staged break, a copy of `policy-mirror.js` that
lists only the mirror's recorded keys, and green once restored.

## S2 — unit 40's wording, superseded

Unit 40 is CLOSED, so neither its spec nor its ledger is written (F1, resolved (b)). These three
passages of `2026-10-26-spec-KICK-dKeptSession-40.md` read as S1 of this unit says:

- Its S2: "and `policy-mirror.js`, which compares every key of `legacy_blobs`, reads a changed store
  STALE with no edit". Superseded: the JS reader is edited, and compares the names of its own
  `MIRROR_KIT_INPUTS` by the kit's prefix before every other recorded key.
- Its §4 Evidence, for the JS reader: "Neither holds a list of its own, so neither is edited."
  Superseded for `policy-mirror.js`, which now holds a list of its own; the guard half stands
  (this unit's §3).
- Its §4 Migration: "A mirror rendered before this unit carries no `presets.toml` entry, so
  `policy-mirror.js` reads it stale once and the reader answers". Superseded in its cause: a
  pre-unit mirror reads stale because the reader expects the store, not because the mirror names it.

**Evidences:** KICK-dKeptSession-49
- AC1 — with strict's `hooks.bypass` set to `allowed` in the copy's store alone and pushed, the edited reader exited 0 printing `allowed`, its stderr line opening `policy: hooks.bypass · preset · mirror stale at <L8>; `.
  The reader at the base, over the same repository, exited 0 printing `refused` with no `mirror
  stale at`, the defect the criterion's red names (DERIVED, that probe). The copy carried
  `presets.py` and `presets.toml` from `MIRROR_KIT_FILES`, so the read did not refuse for want of
  the module.
- AC2 — with the store unchanged, the edited reader exited 0 printing `refused`, its stderr line opening `policy: hooks.bypass · preset · mirror stale at <L8>; `.
  The reader at the base printed `refused` with no `mirror stale at`: it read the pre-unit mirror
  FRESH because the omitted input had not moved (DERIVED, that probe). After both reads
  `arm_mirror_landed` found 0 findings over the 3 keys the policy file sets (DERIVED, that probe).
- AC3 — the squeezed `tools/policy/README.md` piped into `grep -c "the helper reads a mirror whose recorded id differs at L"` printed `0`, and into `grep -c "MIRROR_KIT_INPUTS"` printed `1` (DERIVED, that probe).
  The same pipes over the README at the base printed `1` and `0` (DERIVED, that probe).
- AC4 — the squeezed ledger piped into `grep -c "compares every key of"` and into `grep -c "Neither holds a list of its own"` each printed `1`, and `git diff --name-only d3b51e46 HEAD --` over unit 40's spec and its acceptance ledger printed nothing (DERIVED, that probe).
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `mirror-pre-unit-stale`: the reader lists only the mirror's recorded keys
