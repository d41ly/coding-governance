# Acceptance ledger — TOOL-aHastenedSweep-2

**Serves:** journal TOOL-aHastenedSweep-2

Built against spec rev-1 in one pass commit, on node a, in the pass's own worktree reset to the
dispatch commit `ab3bde2b6`. The §4 evidence holds at that tip: `selectable`'s predicate is the
one §4 quotes, `tracked_set = set(tracked)` sits at line 456 of `tools/memory-tree/corpus_ids.py`
and the per-token `_roots(tracked_set)` call at line 569, and neither module differs from `f25308f0`.

The observations below are each criterion's own probe, run in the worktree with the change in place
before the commit, comparing the changed modules with the shipped copy from `git archive f25308f0
tools` unpacked under the run's scratchpad. `python -m py_compile` over both modules exited 0, and
`python tools/codebase-map/gen_map.py --write` rewrote nothing tracked. No suite, gate leg or bar
ran in the pass.

Owed to the main loop at the close:
- AC3, the live-tree A/B: `gotchas.py --check` and `corpus_ids.py --check`, changed against shipped
  at one commit, `cmp`-identical with the same exit codes, with the four wall times and each
  output's line count recorded here.
- The legs §7 lists, and in the `gotchas selftest` and `corpus-ids selftest` legs the dead-anchor,
  inert-anchor, `selectable` and dead-citation arms §7 names keeping their verdicts. This unit adds
  no arm, so no `New arm:` red-then-green is owed.

**Evidences:** TOOL-aHastenedSweep-2
- AC1 — `selectable` — a probe loading the changed `tools/memory-tree/gotchas.py` and the shipped
  copy through `importlib.util` called each with the five anchors, in order and then reversed, over
  the six paths: every pair of sets was equal. The other/some-gate.sh call returned
  tools/some-gate.sh, deep/nested/some-gate.sh and the backslash spelling, `os.path` being `ntpath`;
  the `INDEX.md` call returned docs/INDEX.md alone, so no anchor basename was kept across calls; no
  call admitted `memory/gotchas/INDEX.md`.
- AC2 — `DEAD_PATH_PIN` — a fixture repository at `%TEMP%/hs2fx`, built by the changed module's
  `_scratch` with tools/kit/check.sh tracked and a `memory/HYGIENE.md` citing kit/check.sh,
  tools/gone/never.sh and nosuchroot/x.md, with `DEAD_PATH_PIN` set to `0`: `checks(walk(root,
  conf))` from the changed module and from the shipped copy printed JSON that `cmp` found equal,
  two findings, naming kit/check.sh and tools/gone/never.sh and not nosuchroot/x.md. The fixture was
  removed after.
- AC3 — `cmp` — NOT OBSERVED in this pass: the live-tree A/B is the main loop's at the close, as the
  criterion's permission line assigns, and its wall times and line counts are recorded here then.

## Close observations, by the main loop

The live-tree A/B, run by the main loop: the shipped kit at `f25308f01` overlaid on `tools/memory-tree/` in a detached worktree frozen at the subject commit, against that commit's own kit, both over the same tree, stdout, stderr and exit code each compared with `cmp`. Every run shared node a with other work, so the walls are contended (PINNED, 2026-11-15 and 2026-11-16).
- `gotchas.py --check` at `59f970047`: shipped 140.0 s, changed 15.7 s, stdout, stderr and exit code identical (PINNED). A first run with the shipped copy outside the repository read the catalogue index as stale, because the index renders the kit's own relative path; the copy was then overlaid at its real path and the outputs matched. This is AC3's observation for `gotchas.py`.
- `corpus_ids.py --check` at `59f970047`: shipped 66.0 s, changed 52.4 s, identical (PINNED). This is AC3's observation for `corpus_ids.py`.
- The whole `check-memory-hygiene.sh` run at `e30d94df9`, every unit of the build in: shipped 663.3 s, changed 239.2 s, 173 lines each, stdout, stderr and exit code identical (PINNED).
- `gotchas.py --selftest` and `corpus_ids.py --selftest` were green at `0c1935569`.
