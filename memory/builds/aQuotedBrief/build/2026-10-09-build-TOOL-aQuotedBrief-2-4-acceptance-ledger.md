# TOOL-aQuotedBrief-2 — acceptance ledger

**Serves:** journal TOOL-aQuotedBrief-2

Node a, 2026-10-09. No suite and no bar ran in this pass. The arms in `unattended.test.sh`'s region
three, after the prompt-record arms, were run as a SLICE: the suite's prologue plus the new block,
in a temp script under the kit directory, deleted before the commit. Against this pass's driver it
printed `SLICE n=34 st=0` (20 prologue assertions and the block's 14). Against the pre-pass driver
(the HEAD blob) it printed 6 FAIL lines: AC3's three and AC1's three. AC2, AC4 and AC5 admit, so
each was observed red against a copy of this pass's driver with that criterion's clause staged out:
the generated-index loop removed (AC2, 2 FAIL lines), the first-preflight guard removed (AC4, 2), the
local-default exclusion removed (AC5, 2).

The gotchas pass over the first commit (`porcelain-diff-names-a-rename-by-its-destination`) found
that rename detection listed a file moved into the build folder by its destination only, which
passed. Spec rev-4 adds `--no-renames` and a rename arm beside AC1: the slice then printed
`SLICE n=36 st=0`, and against the first commit's driver the rename arm printed its one FAIL line.

**Evidences:** TOOL-aQuotedBrief-2
- AC1 — `--preflight tBr` on a prompt-mode build-folder commit above a commit adding `stray.txt` printed check 114 ending `the commit and the first such path: <short sha> stray.txt`, no `preflight OK`, and no `RUN.md` (slice, red on the pre-pass driver, which wrote `RUN.md`)
- AC2 — the build-folder commit alone, carrying a re-rendered `memory/LIVE.md` with `GENERATED_INDEXES="memory/LIVE.md:gen.py"` on the default branch, printed `preflight OK` and no check 114 (slice, red with the generated-index loop staged out)
- AC3 — `--preflight tFresh`, a slug-mode README on the default branch, with one commit adding `stray.txt` on the run branch, printed check 114 naming that sha and file and the recovery line `git -C <worktree-root>/tFresh checkout unit -- memory/builds/tFresh/` (slice, red on the pre-pass driver)
- AC4 — `--preflight tRun`, whose `RUN.md` exists, with the same carried commit printed `preflight OK` and no check 114 (slice, red with the first-preflight guard staged out)
- AC5 — a commit adding `local.txt` on a local `main` ahead of `origin/main`, then a build-folder commit on the run branch: `--preflight tFresh` printed `preflight OK` and no check 114 (slice, red with the local-default exclusion staged out)
- AC6 — `grep -n "git worktree add" memory/guides/UNATTENDED-VERBS.md` hit line 552, inside the prompt path's step 2 under `Then, before step 3, start clean`, which tells the run to work from the new tree by absolute path or `git -C`; the prompt path carries no stop-on-dirty instruction, and the render is in sync with the template (`adopt-unattended.sh --check`)
