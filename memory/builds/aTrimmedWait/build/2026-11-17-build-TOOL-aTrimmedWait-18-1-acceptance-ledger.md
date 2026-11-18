# TOOL-aTrimmedWait-18 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-18

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time, over the spec at rev-1, from the worktree root, after
`git merge --no-ff --no-commit 8eda4a5a0` on the pre-merge tip `0159e06eb`, the five resolutions and
S7's hook edit, and before the merge commit this ledger rides. `git rev-parse main` printed
`8eda4a5a0028fdf15c540293fdf462a110532667` before the merge, and the merge named exactly the five
conflicted files §2 names. `$SCRATCH` is the run's scratch directory. The probe
`bash "$SCRATCH/t18.sh" HEAD MERGE_HEAD` is §4's text verbatim.

## The criteria

**Evidences:** TOOL-aTrimmedWait-18
- AC1 — `git rev-parse MERGE_HEAD` printed `8eda4a5a0028fdf15c540293fdf462a110532667`, and both
  `git diff --name-only --diff-filter=U` and `git grep -n '^<<<<<<< '` printed nothing. The
  after-commit half, `git rev-list --merges -n 1 HEAD` and `git rev-list --parents -n 1` over it,
  is owed to the main loop, per the criterion's permission line.
- AC2 — `grep -nE '^memory/builds/a(MeasuredDrag|LightenedLoop|TwinnedPass|PiecewiseGrade|HastenedSweep|TrimmedWait)/README[.]md$' memory/project/readme-contract.txt`
  printed six lines, 243 to 248, in that order. <!-- PINNED 2026-11-17 -->
  `python tools/memory-tree/gen_build_index.py --check-format` is owed to the main loop: the
  scratch-guard refused it to this role as the leg "build README slot contract".
- AC3 — `git diff --cached -U0 -- memory/guides/SESSION-KICKOFF.md` printed one `+last-audit:` line,
  `+last-audit: 2026-11-17T05:07:41+02:00 @ 0159e06eb96d8edf007e03dfcbdafe6aa034b117`, ending `@ `
  and the full `git rev-parse HEAD` of the pre-merge tip, with a datetime later than
  `2026-11-17T01:27:47+02:00`, and one `+last-body-change:` line naming the same sha. Its only other
  content lines are the two `-` lines they replace, this branch's
  `-last-audit: 2026-11-16T03:15:41+02:00 @ 01aad17473c8887505f2ae4f905c2e32ed55bb9b` and
  `-last-body-change: c83653a2606aa2b0ea164a9ddb814a1213d24123`.
- AC4 — `python -m py_compile tools/memory-tree/gen_build_index.py` exited 0, the probe printed
  `main() memo-then-dispatch`, and
  `grep -c '^        if mode == "--write-staged":' tools/memory-tree/gen_build_index.py` printed 1, <!-- PINNED 2026-11-17 -->
  read without the criterion's `$` anchor because this checkout's `.py` working copy is CRLF.
- AC5 — `grep -c '^FLOOR_ASSERTIONS=784$' tools/memory-tree/check-memory-hygiene.test.sh` printed 1, <!-- PINNED 2026-11-17 -->
  and `grep -cE "^# MERGED at TOOL-aTrimmedWait-1[28]'s|RAISED 719 -> 742 by TOOL-aHastenedSweep-7|RAISED 745 -> 749 by TOOL-aTrimmedWait-11" tools/memory-tree/check-memory-hygiene.test.sh`
  printed 4. `bash -n tools/memory-tree/check-memory-hygiene.test.sh` exited 0. The probe printed <!-- PINNED 2026-11-17 -->
  `counts check-memory-hygiene.test.sh merged 344 expect 344` and <!-- PINNED 2026-11-17 -->
  `floor check-memory-hygiene.test.sh FLOOR_ASSERTIONS merged 784 expect 784 (tip 750 main 742 base 708)`. <!-- PINNED 2026-11-17 -->
  The figure 784 is DERIVED as 750 + (742 - 708), read with `git show` at the pre-merge tip, `8eda4a5a0` and `5d48501da`.
- AC6 — `grep -c -e '^FLOOR_ASSERTIONS=3406$' -e '^FLOOR_SHARD_1=737$' -e '^FLOOR_SHARD_3=469$' -e '^FLOOR_SHARD_4=431$' tools/unattended/unattended.test.sh`
  printed 4, and <!-- PINNED 2026-11-17 -->
  `grep -cE "^# MERGED at TOOL-aTrimmedWait-18's|RAISED 3348 -> 3377 by TOOL-aPiecewiseGrade-6|RAISED 3374 -> 3377 by TOOL-aTrimmedWait-13" tools/unattended/unattended.test.sh`
  printed 3. `bash -n tools/unattended/unattended.test.sh` exited 0. The probe printed <!-- PINNED 2026-11-17 -->
  `counts unattended.test.sh merged 3822 expect 3822` and nine `floor unattended.test.sh` lines, <!-- PINNED 2026-11-17 -->
  each with `merged` equal to `expect`: `FLOOR_ASSERTIONS` 3406 (tip 3377 main 3377 base 3348), <!-- PINNED 2026-11-17 -->
  `FLOOR_SHARD_1` 737 (tip 737 main 734 base 734), `FLOOR_SHARD_2` 229, `FLOOR_SHARD_3` 469 <!-- PINNED 2026-11-17 -->
  (tip 469 main 451 base 451), `FLOOR_SHARD_4` 431 (tip 431 main 423 base 423), `FLOOR_SHARD_5` 297, <!-- PINNED 2026-11-17 -->
  `FLOOR_SHARD_6` 127, `FLOOR_SHARD_7` 311 and `FLOOR_SHARD_8` 646, each of the last four unmoved on every side. <!-- PINNED 2026-11-17 -->
  Each floor is DERIVED as tip + (main - base), read as AC5 reads its figure.
- AC7 — `grep -c '^FLOOR_ASSERTIONS=1051$' tools/workflows/unattended-build.test.sh` printed 1, and <!-- PINNED 2026-11-17 -->
  the probe printed `counts unattended-build.test.sh merged 1077 expect 1077` and <!-- PINNED 2026-11-17 -->
  `floor unattended-build.test.sh FLOOR_ASSERTIONS merged 1051 expect 1051 (tip 1051 main 1043 base 1043)`. <!-- PINNED 2026-11-17 -->
  The figure 1051 is DERIVED as AC6's figures are.
- AC8 — `bash -n .githooks/pre-commit` exited 0, and the probe printed
  `hook resolver-sources 1 resolve_hook_python 5 hy_r 0`. <!-- PINNED 2026-11-17 -->
- AC9 — after §4's regeneration a second `python tools/run-gates/regen.py --write` printed
  `regen: 15 declared · 15 written · 0 file(s) moved` with `moved: none` at each of its three stages, <!-- PINNED 2026-11-17 -->
  and `git status --porcelain` showed no `??` line and no unstaged path. Before the commit, the
  staged tree differed from `git merge-tree --write-tree HEAD MERGE_HEAD`'s outside `memory/` only in
  `.githooks/pre-commit`, `tools/memory-tree/check-memory-hygiene.test.sh`,
  `tools/memory-tree/gen_build_index.py` and `tools/unattended/unattended.test.sh`, and
  `.governance/instructions.lock` read identical to main's. Owed to the main loop:
  `python tools/run-gates/regen.py --check` and `bash tools/unattended/adopt-unattended.sh --check`,
  which the scratch-guard refused to this role as gate legs, and the after-commit
  `git show --remerge-diff` half, per the criterion's permission line.
- AC10 — owed to the main loop after the re-stamp commit: `bash skills/session-kickoff/manifest-check.sh`,
  `git merge-tree --write-tree 8eda4a5a0 HEAD` and `git merge-base --is-ancestor 8eda4a5a0 HEAD`.

## Before and after, on this node

S7 is the one edit that changes behaviour-bearing code beyond a conflict hunk. The same command ran
before and after it, one at a time with nothing else running:
`bash "$SCRATCH/t18_fx.sh" "$PWD" "$TEMP/t18fx" 10`. It takes `hook_py` and `resolve_hook_python`
verbatim from the merged hook, and runs the render's resolver condition in its pre-S7 inline form
("old") and its S7 form ("new") over four fixture repositories: the real tracked resolver, no
tracked resolver, a resolver whose `resolve_python` fails, and a counting resolver reached after
the policy guard's own `resolve_hook_python` call.

- old: real rc=0 py set, none rc=1, broken rc=1, counted rc=0 py set with 2 resolutions. <!-- PINNED 2026-11-17 -->
- new: real rc=0 py set, none rc=1, broken rc=1, counted rc=0 py set with 1 resolution. <!-- PINNED 2026-11-17 -->
- timed, the guard's resolution then the render's, over the real resolver: old 10 runs in 6201 ms, new 10 runs in 4023 ms. <!-- PINNED 2026-11-17 -->

Every refusal and every green is identical. The one difference is the count of python resolutions
in a run that reaches both the policy guard and the render, which is what S7 removes.
