# TOOL-aTrimmedWait-12 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-12

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time, over the spec at rev-1, from the worktree root, after
`git merge --no-ff --no-commit 5d48501da` on the pre-merge tip `7c3e4d4e5` and the eight
resolutions, and before the merge commit this ledger rides. `$SCRATCH` is the run's scratch
directory. The probe `bash "$SCRATCH/t12.sh" HEAD MERGE_HEAD` is §4's text verbatim. The stamp
probe is §4's text verbatim, run as `python -I "$SCRATCH/t12-stamp.py" "$PWD/tools/memory-tree"`:
the spec's relative `tools/memory-tree` argument made the probe's first `--write` exit 2, since the
generator path it builds is relative and the probe runs it with the fixture as its cwd.

**Evidences:** TOOL-aTrimmedWait-12

## The criteria

- AC1 — `git rev-parse MERGE_HEAD` printed `5d48501da9e5e07b0796bd935aaf4eae8cd4b804`, and both
  `git diff --name-only --diff-filter=U` and `git grep -n '^<<<<<<< '` printed nothing. The
  after-commit half, `git rev-list --merges -n 1 HEAD` and `git rev-list --parents -n 1` over it,
  is owed to the main loop, per the criterion's permission line.
- AC2 — `grep -nE '^memory/builds/a(ClearedLedger|BriskDeclaration|LightenedLoop|TwinnedPass|TrimmedWait)/README[.]md$' memory/project/readme-contract.txt`
  printed five lines, 241 to 245, in that order. <!-- PINNED 2026-11-16 -->
  `python tools/memory-tree/gen_build_index.py --check-format` is owed to the main loop: the
  scratch-guard refused it to this role as the leg "build README slot contract".
- AC3 — `git diff --cached -U0 -- memory/guides/SESSION-KICKOFF.md` printed one `+last-audit:` line,
  `+last-audit: 2026-11-16T03:07:18+02:00 @ 7c3e4d4e5fd723848b4eed249e9859b652623947`, ending `@ `
  and the full `git rev-parse HEAD` of the pre-merge tip, with a datetime later than
  `2026-11-15T15:05:35+02:00`. Its one `-` line is the replaced stamp,
  `-last-audit: 2026-11-15T15:05:35+02:00 @ c83653a2606aa2b0ea164a9ddb814a1213d24123`, and no other
  `+` or `-` content line printed.
- AC4 — the probe printed `skill measured 10716 row 10716`. <!-- PINNED 2026-11-16 -->
  `grep -cE 'RAISED 10580 -> 10744, 2026-11-14|RAISED 10580 -> 10628, 2026-11-14|^# MERGED at TOOL-aTrimmedWait-12' tools/template-size-limits.txt`
  printed 3, and `grep -c '^- \*\*TOOL-aTrimmedWait-12\*\* - ' memory/DECISIONS.md` printed 1. <!-- PINNED 2026-11-16 -->
  The figure 10716 is DERIVED by the probe's `tr -d '\r' | wc -c` over the merged Skill.
- AC5 — `python -m py_compile tools/memory-tree/gen_build_index.py` exited 0, and the probe printed
  `cw lost ours 1 main 14`, `cw order stamp-decline-before` and `cw written 2 selftest 3`. <!-- PINNED 2026-11-16 -->
- AC6 — the stamp probe printed `stamp decline rc=1 left=False`, `stamp undo rc=1 left=False`,
  `stamp landed rc=0 left=True` and `stamp write rc=0 left=True`.
- AC7 — `grep -c '^FLOOR_ASSERTIONS=750$' tools/memory-tree/check-memory-hygiene.test.sh` printed 1, <!-- PINNED 2026-11-16 -->
  read over the CR-stripped working copy, and
  `grep -cE "^# MERGED at TOOL-aTrimmedWait-12's|RAISED 707 -> 708 by TOOL-aClearedLedger-6|RAISED 745 -> 749 by TOOL-aTrimmedWait-11" tools/memory-tree/check-memory-hygiene.test.sh`
  printed 3. `bash -n tools/memory-tree/check-memory-hygiene.test.sh` exited 0, and the probe <!-- PINNED 2026-11-16 -->
  printed `partition ours main-helper 0` and `counts check-memory-hygiene.test.sh merged 335 expect 335`. <!-- PINNED 2026-11-16 -->
  The figure 750 is DERIVED as 707 + (708 - 707) + (749 - 707), read with `git show` at `846d51d39`, `5d48501da` and the pre-merge tip.
- AC8 — `bash -n tools/unattended/unattended.sh` exited 0, the probe printed
  `order forks 0 check_unit_spec 1 verb_dispatch 1` and `window refusals-before-start`, and
  `grep -c 'Both call sites read' tools/unattended/unattended.sh` printed 1. <!-- PINNED 2026-11-16 -->
- AC9 — `grep -c -e '^FLOOR_ASSERTIONS=3374$' -e '^FLOOR_SHARD_3=469$' -e '^FLOOR_SHARD_4=431$' tools/unattended/unattended.test.sh`
  printed 3 over the CR-stripped working copy, and
  `grep -c "^# MERGED at TOOL-aTrimmedWait-12's" tools/unattended/unattended.test.sh` printed 3. <!-- PINNED 2026-11-16 -->
  `bash -n tools/unattended/unattended.test.sh` exited 0. The probe printed
  `counts unattended.test.sh merged 3780 expect 3780`, then `region 3 main-LL8`, <!-- PINNED 2026-11-16 -->
  `region 3 main-LL3`, `region 3 ours-TW1`, `region 4 main-TP3` and `region 4 ours-TW5`.
  Each floor is DERIVED as base + (main - base) + (tip - base), read as AC7 reads its figure.
- AC10 — `grep -c '^FLOOR_ASSERTIONS=1051$' tools/workflows/unattended-build.test.sh` printed 1 over <!-- PINNED 2026-11-16 -->
  the CR-stripped working copy,
  `grep -cE "^# MERGED at TOOL-aTrimmedWait-12's|RAISED 950 -> 958 by TOOL-aTrimmedWait-1|RAISED 1028 -> 1039 by TOOL-aTwinnedPass-11" tools/workflows/unattended-build.test.sh`
  printed 3, `bash -n tools/workflows/unattended-build.test.sh` exited 0, and the probe printed <!-- PINNED 2026-11-16 -->
  `counts unattended-build.test.sh merged 1077 expect 1077`. <!-- PINNED 2026-11-16 -->
- AC11 — `grep -c '"id": "extract_hs_lines"' memory/map/generated/symbols.json` printed 0 after the
  §4 regeneration, and `git status --porcelain` showed no `??` line. Owed to the main loop:
  `python tools/run-gates/regen.py --check` and `bash tools/unattended/adopt-unattended.sh --check`,
  which are gate legs this role does not run, and the after-commit
  `git show --remerge-diff --format= --name-only "$(git rev-list --merges -n 1 HEAD)" 2>/dev/null | sort -u`
  piped to
  `grep -vE '^(memory/(guides/SESSION-KICKOFF|DECISIONS|LIVE)[.]md|memory/project/readme-contract[.]txt|tools/template-size-limits[.]txt|tools/memory-tree/(gen_build_index[.]py|check-memory-hygiene[.]test[.]sh)|tools/unattended/unattended([.]test)?[.]sh|tools/workflows/unattended-build[.]test[.]sh|memory/(ledger/|map/generated/|builds/[^/]+/(README[.]md|spec/|build/2026-11-16-build-TOOL-aTrimmedWait-12-)))'`.
  Before the commit, every staged path outside the eight files and the generated outputs was one
  `git diff --name-only HEAD MERGE_HEAD` names, and `.governance/instructions.lock` read identical to main's.
- AC12 — owed to the main loop after the re-stamp commit: `bash skills/session-kickoff/manifest-check.sh`,
  `git merge-tree --write-tree 5d48501da HEAD` and `git merge-base --is-ancestor 5d48501da HEAD`.
- AC13 — owed to the main loop on a frozen clone: `python tools/memory-tree/gen_build_index.py --selftest`.

## Before and after, on this node

The same command, one at a time with nothing else running: a fixture probe that drives the
generator's own `_fixture` through the four AC6 cases (`--write-staged` declined at a missing landed
branch, `--write-staged` undone under an empty `index.lock`, `--write-staged` landing, and `--write`)
and prints each case's exit code, the count of staged paths after it, and its wall time. "Before" is
the generator of the pre-merge tip `7c3e4d4e5`, its whole `tools/` exported by `git archive` to a
short `%TEMP%` path; "after" is the merged worktree's.

- before: decline rc=1 staged=1 in 0.45 seconds, undo rc=1 staged=1 in 0.66 seconds, landed rc=0 staged=3 in 0.89 seconds, write rc=0 staged=1 in 0.36 seconds. <!-- PINNED 2026-11-16 -->
- after: decline rc=1 staged=1 in 0.37 seconds, undo rc=1 staged=1 in 0.77 seconds, landed rc=0 staged=3 in 1.25 seconds, write rc=0 staged=1 in 0.57 seconds. <!-- PINNED 2026-11-16 -->

Every refusal, red and green is identical. The timings are one run each, within run-to-run noise
of each other but for `landed`, whose merged form also reads the render state and writes main's stamp.
