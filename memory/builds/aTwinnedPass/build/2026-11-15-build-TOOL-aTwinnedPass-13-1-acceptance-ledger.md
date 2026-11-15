# TOOL-aTwinnedPass-13 — acceptance ledger

**Serves:** journal TOOL-aTwinnedPass-13

Built against spec rev-1 in one pass, in the branch's own worktree. No merge bar, no self-test suite
and no gate ran in this pass. `git rev-parse main` printed `a76c6afe7f70b384b7cce7d6bf56e6aed62a2f82`,
and `git merge --no-ff --no-commit a76c6afe7` conflicted in exactly the four files the spec names, so
the pass went on. Each conflict hunk was resolved as §4 "The resolutions" writes it, the four files
were staged by name, and `regen.py --write`, `gen_build_index.py --write` and `gen_map.py --write`
ran in that order. Regen moved `memory/LIVE.md` and `memory/ledger/2026-11.md`, staged by name; the
two later writes moved nothing, and `git status --porcelain` showed no `??` line and no unstaged path.

The observations below are each criterion's own command, or §4's probe `t13.sh` run once from the
worktree root as `bash t13.sh HEAD MERGE_HEAD` after the resolution and before the commit. The
role's hook refused `gen_build_index.py --check-format` as the leg "build README slot contract", so
that check and AC8's three `--check` commands are the close's.

Owed to the main loop at the close:
- AC2's `python tools/memory-tree/gen_build_index.py --check-format`;
- AC8's before-commit `gen_build_index.py --check`, `gen_map.py --check` and
  `adopt-unattended.sh --check`, and its after-commit `--remerge-diff` filter;
- AC1's after-commit parents and AC9's `merge-tree` and `--is-ancestor`;
- the legs of the spec's Gates section, the four self-test legs named as tripped and not observed.

**Evidences:** TOOL-aTwinnedPass-13
- AC1 — `git rev-parse MERGE_HEAD` — printed `a76c6afe7f70b384b7cce7d6bf56e6aed62a2f82`, and
  `git diff --name-only --diff-filter=U` and `git grep -n '^<<<<<<< '` each printed nothing. The
  after-commit parents are the close's.
- AC2 — `grep -nE '^memory/builds/a(LightenedLoop|TwinnedPass)/README[.]md$' memory/project/readme-contract.txt`
  — printed lines 243 and 244, `aLightenedLoop` first. `--check-format` is the close's.
- AC3 — `node --check tools/workflows/unattended-unit.js` — exited 0. The probe printed
  `cut passBase same` and `cut unattended same`, and `grep -c 'Declare the write set with'` printed 0.
- AC4 — `grep -c -e '^FLOOR_ASSERTIONS=3348$' -e '^FLOOR_SHARD_3=451$' -e '^FLOOR_SHARD_4=423$'` — <!-- PINNED 2026-11-15 -->
  printed 3; the `MERGED` grep printed 1, the two raise-comment grep printed 2, and `bash -n` exited
  0. `git show` at `aebbb4a72`, `a76c6afe7` and the pre-merge tip printed 3329, 3335 and 3342, so the <!-- PINNED 2026-11-15 -->
  sum is 3348. The probe printed `counts unattended.test.sh merged 3762 expect 3762`, then <!-- PINNED 2026-11-15 -->
  `region 3 main-LL8`, `region 3 main-LL3` and `region 4 ours-TP3`.
- AC5 — `grep -c '^FLOOR_ASSERTIONS=1043$'` — printed 1; the `MERGED` grep printed 1, the two <!-- PINNED 2026-11-15 -->
  raise-comment grep printed 2, and `bash -n` exited 0. `git show` at the three revisions printed 950,
  954 and 1039, so the sum is 1043. The probe printed <!-- PINNED 2026-11-15 -->
  `counts unattended-build.test.sh merged 1071 expect 1071`. <!-- PINNED 2026-11-15 -->
- AC6 — `git diff --quiet a76c6afe7 -- tools/workflows/unattended-build.js tools/workflows/unattended-build.template.js`
  — exited 0, and the `git grep` for `Declare the write set with` outside the suites printed nothing.
- AC7 — the probe — printed `window writes 0`, and `grep -c 'NOTHING IN THE WINDOW WRITES THE TREE'`
  printed 1.
- AC8 — owed to the close: the role refuses the three `--check` commands as gate legs, and the
  `--remerge-diff` filter reads the commit.
- AC9 — owed to the close: it reads the commit.
