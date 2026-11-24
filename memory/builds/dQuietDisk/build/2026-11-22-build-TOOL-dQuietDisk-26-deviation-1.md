# TOOL-dQuietDisk-26 deviation 1 — the state variables are unset before they are reset, and an empty index makes no attribute call

**Serves:** deviation TOOL-dQuietDisk-26

- **Departs from:** `TOOL-dQuietDisk-26@rev-3` [S3, S8, the file-scope line in section 4's "The three reads after"]
- **Hand-off:** spec-to-code
- **Before:**
  - Section 4's sketch resets the seven state variables by assignment alone, `_LS=""; … _LT_READ=""`, at file scope.
  - S3 runs one `git check-attr --stdin eol merge` over `_LS_NAMES` whenever the listing is usable.
- **After:**
  - `tools/check-wiring.sh` runs `unset` over the seven names and then the sketch's assignment line, both at file scope, before `read_tree_listing`.
  - `tools/check-wiring.sh#read_listed_attrs` makes no call when the usable listing holds no path. It marks the empty read usable, so every attribute read answers empty, as the per-site calls did over an empty index.
- **Cause:** builder discovery
- **Reason:**
  - An assignment keeps a variable's inherited export. AC4's probe exported `_LS` and its siblings into a run over the scratch clone. With assignment alone, the multi-megabyte listing rode into every child's environment. On Windows that overflows the environment block, so no later git or python started: the run spent 2 git processes and printed different lines. With `unset` first the same run spent 26 and printed the clean run's bytes.
  - Over an empty index, `printf` would hand `check-attr` one empty line where the per-site pipe handed it none. No call is the per-site answer.
- **Evidence:** the AC4 line of `2026-11-22-build-TOOL-dQuietDisk-26-1-acceptance-ledger`, for the exported-variable run before and after the `unset`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-26
