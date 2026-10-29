**Serves:** journal TOOL-dSafePassage-82

# TOOL-dSafePassage-82 — acceptance ledger

The unit as built, at spec rev-6, from the second pass's saved change
(`TOOL-dSafePassage-82-wip2.patch`, its `RUN.md` rows, README region and spec-header edit left out),
which applied cleanly at `b76cc74f0`: that commit and the patch's base `eacd4e83e` differ in records
only, so no product line the patch touches moved. The second pass had added, to the first pass's
saved work, S3's release-0 fixture files and their reader in `tools/govkit/upgrade_walk.py`, the
floor program in govkit's steps directory and the floor row's argvs, `tools/gate-legs.json`'s prose,
the suite line in `tools/lib/resolve-python.test.sh`; S4's second run in arm 39 and arm 40's full
message; S6's registry row; S7's re-stamp; S8's map. This pass re-stamped S7 to its own parent and
re-ran every probe below over the applied tree.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11) over this worktree's working copy, by the spec's own probes written to the run's
scratchpad, by the units' own fixture CLIs and by `git grep`. The install-prefix class was measured
by a scratch copy of the leg's counter (its `BAN_PY` block, run with the kit names `git ls-files`
derives) over the files this build changed since `60d90cb7`, by the second pass: 22 spellings on 19
lines before the remaining edits, and after them only the three lines of
`tools/run-gates/ceiling-evidence.txt` (115, 134, 146) S3 leaves to the owner's ask
TOOL-dSafePassage-85. The leg reds on exactly those at the close until the owner rules, as AC11 says.
The product tree that measurement read is the one this pass commits, so it was not re-run.

Where the build met what the spec does not say: the fixture rows are read before the pinned clone
exists, so `read_fixture_rows` resolves each `path` and a nested `shim`'s `from` and `to` against
gov's own tool root, which is the clone's by the walk's own construction (it runs the clone's
engine at `HERE`'s path relative to gov). `deploy.toml` is resolved against `derive_tool_root` of the
clone itself. A gov plant's `old` text keeps its `{prefix}` unresolved, since it is matched against
`kit.toml`'s bytes. `upgrade_walk.py`'s third site, the tree-clean grader's evidence path, was added
by a sibling and is in scope by §2's class rule; its kit name is held in a local name.

Owed at the close: AC11, the six legs, by the main loop; the §7 legs at the bar; and the three
`New arm:` lines' RED-first observations.

**Evidences:** TOOL-dSafePassage-82
- AC1 — `python <scratch>/enc_probe.py tools/govkit/govkit.py tools/govkit/shims.py tools/govkit/upgrade_steps.py tools/lib/python_floor.py` printed `tools/govkit/govkit.py 35`, `tools/govkit/shims.py 0`, `tools/govkit/upgrade_steps.py 0`, `tools/lib/python_floor.py 0`; the new floor program, `upgrade_walk.py` and `docs_leg.py` each printed 0.
- AC2 — `git grep -nE "(['\"])origin\1|remote\.origin\.|refs/remotes/origin/" -- tools/govkit/upgrade_steps.py tools/govkit/upgrade_walk.py` printed nothing, exit 1.
- AC3 — `python tools/govkit/upgrade_steps.py fixture isolation --plant local-url-userinfo` exited 1 printing `... remote.gk-fixture.url in .git/config, so nothing was spawned ...`, and neither `gk-planted-user` nor `gk-planted-secret` (count 0). `--plant local-ext-transport` exited 1 printing `rc 128: fatal: transport 'ext' not allowed` and `isolation: ext-transport canary: absent`; its `-stub` twin printed `ext-transport canary: present · ext-transport`.
- AC4 — `python tools/govkit/upgrade_walk.py --list` exited 0; its 19 `plant`, `gov_plant`, `condition` and `arm` lines equal, by `diff`, the lines `<scratch>/ac4_expect.py` renders from the three fixture files at `83817478f`, among them `upgrade-walk: plant · engine-edit · path tools/memory-tree/README.md · expect carried`. `read_arm_rows` resolved the held shim to `tools/check-kit-versions.sh` and the missing plant to `tools/upgrade-walk-no-such-file.md`; the resolved `deploy.toml` equals its `83817478f` bytes.
- AC5 — `python <scratch>/usage_probe.py` printed `rows 38 38 moved [] literal 0`.
- AC6 — `read_steps` gives lib/python-floor-3.15 the argvs `['python', '{gov}/govkit/steps/python_floor.py', 'preflight']`, its `down` the same program, and `grep -c 'lib/python-floor.sh' tools/govkit/steps.toml` printed 0. The program's `preflight` printed the `python-floor:` line at 3.15.2 and exited 0, under `-I` as well; with `GOV_PYTHON` and `PATH` naming fakes that report 3.14 it exited 1 with the resolver's refusal, `resolve_python: no usable python launcher at the floor 3.15 ...`. `run_step_isolated(row, "witness", <gov>, <gov>)` returned `ok 0`, and again with 3.12 fakes on `PATH` and `GOV_PYTHON` at the floor.
- AC7 — `grep -cP '^tools/lib/python-floor\.sh\texit\t' memory/project/unarmed-branches.txt` printed 4; the two full-message counts over `tools/push-main.test.sh` printed 1 each, arm 39's added run being `TMPDIR="$tmp/tmpdir39" bash "$lander"` from main.
- AC8 — `python <scratch>/fnsubst_probe.py tools/push-main.test.sh` printed `'resolve_python': 1` (4 at `83817478f`); `grep -cF '| grep -c .' tools/lib/resolve-python.test.sh` printed 3; the `merge-rows.test.sh` `var-pipe` row's third field printed 42. The rewritten seven-statement count, run over `python_floor.py check --rev 3708a705`, held at 7 and counted 6 over its first six lines.
- AC9 — `git diff 83817478f -- memory/project/fork-ceilings.txt` printed nothing; the five rows stay the ask TOOL-dSafePassage-85's.
- AC10 — `bash -n` exited 0 on both files; `grep -cF "| sed 's/^/  /'" tools/push-main.sh` printed 4. The no-fork indent matched the `sed` form byte for byte (`od -c`) over a CRLF text, one line, a blank line and an empty string.
- AC11 — owed: the main loop runs the six legs; four are expected green, the spawn budget red on its five rows and install-prefix red on the three `ceiling-evidence.txt` lines, both until the owner rules on TOOL-dSafePassage-85.
- AC12 — `last-audit:` re-stamped to `2026-10-29T04:33:39+02:00 @ b76cc74f06d8805e67ecf46319decd8911605f11`, the pass's parent; `last-body-change:` untouched; the manifest is staged with `tools/gate-legs.json`.
- AC13 — `python tools/codebase-map/gen_map.py --write` rewrote `symbols.json` alone (the second pass); `--check` exited 0 at this pass, and the file names `main` in `tools/govkit/steps/python_floor.py`.
