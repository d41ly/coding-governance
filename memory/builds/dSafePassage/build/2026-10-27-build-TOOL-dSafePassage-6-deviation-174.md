# TOOL-dSafePassage-6 deviation 174 — selfcheck arm 11 stands down in a govkit copied without its generator

**Serves:** deviation TOOL-dSafePassage-6

- **Departs from:** TOOL-dSafePassage-6@rev-6 [§4 The selfcheck arm]
- **Hand-off:** spec-to-code
- **Before:** arm 11 of `selfcheck` calls `check_shim_parity(root)` and `check_shim_windows(root)` and prints `shims: <n> row(s) graded · <k> open · <c> closed` on every run.
- **After:** arm 11 prints that line on every run where `shims.py` sits beside `govkit.py`, as it does in gov's own tree; where it does not, it prints `shims: arm 11 stood down, graded nothing: no shims.py beside <dir>` and grades nothing.
- **Cause:** builder discovery
- **Reason:** `tools/govkit/selftest.py` runs `selfcheck` in scratch govs that copy only `govkit.py` and `upgrade_steps.py`; an arm importing `shims.py` unconditionally would crash every one of them, and one reading a missing `shims.toml` as a refusal would red each scratch selfcheck those arms expect clean. The stand-down says it graded nothing, so it never reads as a graded zero.
- **Evidence:** `tools/govkit/govkit.py`, the arm's `_sh_src.is_file()` branch; in gov's tree `python tools/govkit/shims.py --check` prints `shims: 0 row(s) graded · 0 finding(s)`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-6, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-6
