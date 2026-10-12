# Arm inventory — the three suite files TOOL-aSparedSpawn-8 converted

**Serves:** journal TOOL-aSparedSpawn-8

S11's comparison, taken by `2026-10-11-build-TOOL-aSparedSpawn-8-arm-inventory.sh` beside this file over
each S10 suite as it stands at `4d2240a1d` — the pass commit's parent carries the same bytes, the unit's spec commits sitting between — and over the converted file the pass commit
carries. The extractor derives each file's assertion helpers from the file — the functions whose body
increments the counter its `PASS (<n> assertions)` line prints, closed over the functions that call
one — and keys every call by helper and first argument, each expansion in that argument read as one
`$...` token. Equal multisets mean no assertion line vanished or doubled in the conversion.

| file | assertion calls, parent | after | multiset diff | helpers found |
|---|---|---|---|---|
| `tools/workflows/unattended-build.test.sh` | 756 | 756 | none | `has` `hasnt_` `same` and the runners that call them: `run_wf` `returns` `build_layout` `check_layout` `run_dispose` `run_gh33` `run_merged_build` `run_merged_review` |
| `tools/unattended/stop-guard.test.sh` | 170 | 170 | none | `print_ok` `print_bad`, and `check_same` `check_hit` `check_miss` `run_hook` through them |
| `tools/memory-tree/transition-audit.test.sh` | 136 | 136 | none | `ok` `bad` |

`FLOOR_ASSERTIONS` did not move in any of the three: 566, 121 and 64 at the parent and after.

The extractor's own failing case was staged: deleting the one `check_same "AC2 line decision"` line
from a scratch copy of the converted `stop-guard.test.sh` made the diff print exactly that pair and
exit 1, and a file whose counter no function increments refused with 2.

**Owed at VERIFYING:** the `PASS (<n> assertions)` figure of one run of each suite at the parent and
at the pass commit, on frozen clones, which only a suite run can produce and a pass may not make.
