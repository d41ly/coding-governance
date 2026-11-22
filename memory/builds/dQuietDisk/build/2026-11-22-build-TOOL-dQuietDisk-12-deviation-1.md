# TOOL-dQuietDisk-12 deviation 1 — the widened row carries its measured count, the key's inputs are the ones present, and the new arm prints only on failure

**Serves:** deviation TOOL-dQuietDisk-12

- **Departs from:** `TOOL-dQuietDisk-12@rev-3` [S8, the `FX_INPUTS` paragraph of section 4, the section 7 `New arm:` line]
- **Hand-off:** spec-to-code
- **Before:**
  - S8 has the row widened through the ledger factory's door and never by hand.
  - Section 4 has `FX_INPUTS` list the suite file, the hook, four policy-kit files and `gate-fingerprint.sh`, each under `$SRC`.
  - Section 7 names a new arm in the suite. AC8 has the base and this commit print the same `ok` and `FAIL` lines.
- **After:**
  - The door ran once and wrote `2026-11-22-build-TOOL-dQuietDisk-12-widen-11`, raising the count by one. The pass then set the count to the measured 2584 and changed nothing else in that row.
  - The prologue adds each of those seven paths to `FX_INPUTS` only when it names a file.
  - The new arm prints a `FAIL` line when it is red and nothing when it holds.
- **Cause:** builder discovery
- **Reason:**
  - `tools/memory-tree/ratchet.py#run_widen` raises a count by exactly one per call. Units 7, 13 and 28 set their rows the same way, each under one record.
  - `git hash-object --stdin-paths` fails on a missing path, and a failed key fails every templated call. An adopter whose install lacks a policy kit would then lose the bg sets, which copy no policy file. A missing file is one the tree halves cannot copy either, so leaving it out drops nothing a template is built from.
  - An `ok` line printed only at this commit would make AC8's same-lines comparison red by its letter. An arm silent on GREEN keeps both statements true, and its RED still prints.
- **Evidence:** all probes ran in this pass, in the session scratch directory (PINNED):
  - `python tools/gate-lint/sh_hygiene.py --shell-role --measure` printed 2584 for `.githooks/pre-push.test.sh`. `git diff -- memory/project/shell-role.txt` changes that row only.
  - With all seven files present the prologue listed 7 inputs, and a scratch copy of them gave a stable key that moved when one byte of the hook changed.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-12
