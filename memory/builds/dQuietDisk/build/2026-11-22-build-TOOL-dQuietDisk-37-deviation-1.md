# TOOL-dQuietDisk-37 deviation 1 — the attestation fixture's extra sibling and wider scrub, two observations taken in another form, and the kickoff manifest re-stamped

**Serves:** deviation TOOL-dQuietDisk-37

- **Departs from:** `TOOL-dQuietDisk-37@rev-1` [S1, section 4's M1 fixture and Files touched, AC6, AC8]
- **Hand-off:** spec-to-code
- **Before:**
  - Section 4 lists the `run-gates` home of S1's scratch gov as `run-gates.sh`, `gate-profiles.txt`, `gate-fingerprint.sh` and `held_halves.py`, and clears every inherited `GATE_` name and the twelve `GIT_ENV_LEAKS` names from the fixture bar's environment.
  - AC6 has `git grep -n fx-args` print nothing.
  - AC8 has the base race body, with the `sleep 1` builder and the second racer started two seconds late, print `built 1`.
  - Files touched says no path is on the kickoff manifest's `watch:` line.
- **After:**
  - `tools/govkit/selftest.py#check_kit_attestations` also copies `profile_bar.py` into that home. It clears every `GATE_` name and every `GIT_` name that does not open `GIT_CONFIG`, a superset of the twelve, and sets `PYTHONDONTWRITEBYTECODE=1` for the bar.
  - AC6's grep is read over the tree outside `memory/`, as `git grep -n fx-args -- ':!memory/'`.
  - AC8's red was observed with the second racer started six seconds late.
  - The pass commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`, declared through `--dispatch`, with a `manifest-audit: delta none` line.
- **Cause:** builder discovery
- **Reason:**
  - `held_halves.py` imports `parse_verdicts` from `profile_bar.py` beside it, so without the sibling the runner's manifest program and `derive_kit_attestations` both fall back to hashing the whole row, and the first line would grade the fallback rather than the declarative keys.
  - `tools/govkit/selftest.py` carries no copy of the `git_env_leaks_py` block, and a fourth spelling of the twelve names outside the parity table is the drift class that block exists against. Clearing every `GIT_` name but the config pins needs no list. The bytecode switch keeps the runner's import of `held_halves.py` from writing a `__pycache__` into the fixture's tree, an untracked path the bar would see; the bar was not run without it.
  - The spec itself, the closing review round 1 and the records of TOOL-dQuietDisk-12 spell `fx-args`. Those records are frozen history, so the literal grep can never print nothing. The code population is the one S6 names.
  - `tools/run-gates/run-selftests.sh` is on that `watch:` line, and the manifest ratchet refused the commit until the stamp moved. No section B claim derives from the serial export, so the delta is none.
  - On node d one background build of the `sleep 1` builder took about five seconds against 1.2 seconds alone, so a racer two seconds late still entered the builder and printed `built 2`. At three seconds late it printed `built 2` once and `built 1` once. At six seconds it printed `built 1` twice.
- **Evidence:** the AC1, AC6 and AC8 lines of `2026-11-22-build-TOOL-dQuietDisk-37-1-acceptance-ledger`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-37
