# TOOL-aTrimmedWait-10 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-10

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time, over the spec at rev-2, from the worktree root at base
`42e99371c`. The pass commits are `49cdded06` (the builder's commit, Rollout step 1) and `68785cb82`
(the mirror, alone, step 2); this ledger rides the closing commit. The pass probes are saved in the
run's scratch directory: `probe_tw10.py` builds `<f>` as §6 defines it under the short temp path and
runs `<gbi> --write-staged` through its CLI; `probe_tw10_parity.py` builds the same fixture twice,
once with the conf switch for the base kit extracted by `git archive 42e99371c` and once with the
policy key for this pass's kit, and runs both over the same five states; `probe_tw10_forms.sh` runs
each converted shell form beside its old form over the same inputs. The changed code is
`tools/memory-tree/gen_build_index.py#check_staged_write` and
`tools/memory-tree/gen_build_index.py#test_staged_write`.

**Evidences:** TOOL-aTrimmedWait-10
- AC1 — in `<f>` on its branch `master`, with `GOV_DEFAULT_BRANCH=master` and `GOV_REMOTE` empty,
  `python <gbi> --write-staged` exited 0 and printed `build-index: staged memory/builds/tOne/README.md`
  beside `build-index: staged memory/LIVE.md`. The base kit over a conf with no switch line is the
  red the criterion names, `STAGED_RENDER is blank`, read from its source at `42e99371c`.
- AC2 — with `GOV_DEFAULT_BRANCH=policy-absent`, a branch of `<f>` whose tip deletes the policy file,
  and `STAGED_RENDER="1"` in `<f>`'s conf, the run exited 1, printed
  `render NOT staged — memory.staged-render reads off, so the hook does not render`, and
  `git status --porcelain` printed the same bytes before and after.
- AC3 — with `GOV_DEFAULT_BRANCH=no-such-branch` the run exited 1, printed
  `render NOT staged — memory.staged-render did not read:` followed by the policy reader's refusal,
  `refs/heads/no-such-branch names no commit in this repository`, and the porcelain was unchanged. `check_staged_write` called in-process with `read_policy_value`
  stubbed to raise LookupError returned
  `(False, 'no policy kit resolves beside this kit, so memory.staged-render reads off')`.
- AC4 — `python tools/policy/policy.py get memory.staged-render` printed `off` and exited 0. The base
  answer `is not a catalogue key` is the spec's own observation of the same date.
  `grep -c 'read_policy_value("memory.staged-render", root)' tools/memory-tree/gen_build_index.py`
  printed 1, and the row of `tools/policy/catalogue.toml` carries the name, `allowed`, the default
  `off`, the `summary`, the `usage` and the owner of §4 "The key", under the comment line it spells.
- AC5 — `python tools/policy/policy.py lists --check` exited 0 and printed `policy lists: green · 0 finding(s)` <!-- PINNED 2026-11-15 -->
  with no line naming `STAGED_RENDER`, against the spec's base `RED · 2 finding(s)`. <!-- PINNED 2026-11-15 -->
  `git grep -c STAGED_RENDER -- ':!memory/'` printed one row, the file `tools/memory-tree/gen_build_index.py`
  with the count 1, and `git grep -n` puts that line inside `test_staged_write`: the planted `stale`
  conf text of the AC2 off arm.
- AC6 — `grep -c '<!-- usage: policy:memory.staged-render ' help/commit-render.md` printed 1, and
  `grep -c 'memory.staged-render' help/README.md help/policy.md tools/memory-tree/README.md` printed 1
  for each file. `grep -A1 '^## .memory.staged-render.$' help/reference/policy.md` printed the
  heading and the `Documented on` line whose link names `help/commit-render.md`. The anchor's fingerprint
  is the one `python tools/govkit/docs_leg.py --fingerprints` printed, which then named the page.
- AC7 — after step 2, `python tools/policy/policy.py mirror --check` printed `policy: mirror fresh`
  and exited 0, and `grep -c '"memory.staged-render"' .governance/policy.json` printed 1. The guard
  admitted the mirror commit as `equals its render at HEAD`.
- AC8 — `grep -n 'hy_out' .githooks/pre-commit` printed three lines and none holds `| grep`; the
  line holding `HYGIENE check <N> FAILED`, N = 9, outside a comment opens `if [[`.
  `grep -c 'RUNS=$(cat .hy-runs)' .githooks/pre-commit.test.sh` printed 0.
- AC9 — `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --build aTrimmedWait` ended
  `over <N> spec(s) of aTrimmedWait` with `<N>` the build's spec count. <!-- DERIVED from ls memory/builds/aTrimmedWait/spec/*.md -->
  `--only 12 --spec` over this spec ended `over 1 spec(s) of` this spec's path, as at base. <!-- PINNED 2026-11-15 -->
  `grep -c 'c12_sel" | grep -c' tools/memory-tree/check-memory-hygiene.sh` printed 0.
  That pass ran only the scoped form, and its count sat outside the scoped branch, so an unscoped
  `--only` that leaves out check 12 died on `c12_sel: unbound variable`: the fix pass from `5618aceba`
  (brief `2026-11-15-prompt-TOOL-aTrimmedWait-10-fix.md`) observed `--only 2` exit 1 on that line
  before its edit, and moved the count inside the scoped branch. After it, both runs, node a, one at a time:
  the unscoped `bash tools/memory-tree/check-memory-hygiene.sh --only 2` exited 0, printed
  `HYGIENE --only 2 ran checks 2` and no `unbound variable`; the scoped `--only 12 --build aTrimmedWait`
  exited 0 and ended `over <N> spec(s) of aTrimmedWait`, `<N>` the build's spec count. <!-- DERIVED from ls memory/builds/aTrimmedWait/spec/*.md -->
  The fix's arm in `tools/memory-tree/check-memory-hygiene.test.sh`, run as a probe over the arm's
  tree outside the suite, passed against this engine and failed against the `49cdded06` engine on
  the unbound variable; its RED-first observation in the suite is owed to the close.
- AC10 — `grep -c '"$(check_cold23' tools/roles/adopt-roles.test.sh` printed 0,
  `grep -c '$(printf "$TW1_SPEC"' tools/workflows/unattended-build.test.sh` printed 0, and
  `grep -c 'printf -v tw1_in "$TW1_SPEC"' tools/workflows/unattended-build.test.sh` printed 2.
- AC11 — owed to the main loop: `python tools/policy/check_policy.py` and the leg argv of
  `shell hygiene (a fork spent on builtin work)` in `tools/gate-legs.json`, and the `git diff 078eb5c58`
  over the three lists. This pass ran neither leg; it diffed nothing under those lists.
- AC12 — owed to the owner: the commit of `.governance/policy.toml` from a terminal, then
  `python tools/policy/policy.py mirror --write` again and `python tools/policy/policy.py get memory.staged-render --rev HEAD`.
- Verdict parity — `probe_tw10_parity.py` gave the base kit and this pass's kit the same exit and
  the same printed lines for a staged change, a second run, an unstaged memory input and an
  unstaged source file; for a foreign index both declined naming it, the lines differing only in
  the fixture directory's name. The only decline that moved is the switch's own, which S2 moves.
  `probe_tw10_forms.sh` gave each old and new shell form the same answer over every input it ran,
  an empty text, a CRLF text and a missing `.hy-runs` included.
- Timing — the same command, `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --build aTrimmedWait`:
  serially at base it took 19.39 s, 22.47 s and 24.61 s before the edit; <!-- PINNED 2026-11-15 -->
  the node's load rose during the pass, so base and built copies were then interleaved; <!-- PINNED 2026-11-15 -->
  base 42.76 s, built 47.72 s, base 46.47 s, built 36.14 s: noise, no measurable move. <!-- PINNED 2026-11-15 -->
- Owed to the close: the `New arm:` line of §7, observed RED-first by the main loop —
  `test_staged_write` with `check_staged_write` reading the conf key again, where the fixture's
  switch reads blank and AC2's conf line proceeds; the fix pass's unscoped `--only 2` arm of
  `tools/memory-tree/check-memory-hygiene.test.sh`, RED with the count hoisted out of the scoped
  branch as `49cdded06` had it; and the gate legs §7 lists.
