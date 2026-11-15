# TOOL-aMeasuredDrag-5 — procmon-hook decides its throttle before any process spawn, resolving the common dir by reading files

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-5-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-5-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-5-red-fix-2.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-5-red-fix-2.md) | red-fix | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-5-1-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-5-1-builder.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/process-monitor/procmon-hook.js` runs on every Bash and PowerShell tool call, and on the
throttled path, which is nearly every call, it still spawns `git rev-parse --git-common-dir` to find
its stamp. This unit makes `resolveStamp` read the `.git` pointer files instead, so the throttled path
starts no process. The stamp stays in the git common dir, so every worktree of one repo shares it.
Findings sessionhooks-3 and spawns-1 of the 2026-11-15 performance review, both CONFIRMED.

## 2. Scope (IN)

- **S1** — `resolveStamp(root)` keeps its name, signature and caller. Its body reads files and
  spawns nothing. When `<root>/.git` is a directory, that directory is the common dir. When it is a
  file, its `gitdir:` line names the worktree git dir, resolved against `root`. That dir's
  `commondir` file, when present, names the common dir, resolved against the worktree git dir;
  absent, the worktree git dir is the common dir. The answer is `<common dir>/procmon-stamp` only
  when the resolved common dir exists as a directory. Every other case, a failed read included,
  answers `null`, as the git failure did. Observed by AC1, AC2 and AC3.
- **S2** — the header comment at `tools/process-monitor/procmon-hook.js@293e9e0dc8b8:21-24` and the
  `resolveStamp` comment at `:71-76` say what the early-exit path does after this unit: it reads the
  conf and the `.git` pointer files, stats the stamp, and starts no process. NOT OBSERVED: a comment;
  the closing diff review reads it.
- **S3** — the arm `test_throttled_path_spawns_nothing` in
  `tools/process-monitor/adopt-process-monitor.test.sh` runs the hook from a linked-worktree layout of
  its clean fixture, with no git reachable on `PATH`. It keeps its name and its one assertion, so the
  suite's assertion count does not move. Observed by AC2, and by the `New arm:` line in §6.

## 3. Non-goals (OUT)

- What the hook prints, when it censuses, and its exit status, wherever git is on `PATH`. AC1 holds
  the transcript byte-identical.
- Filtering the desktop app's own idle rows out of the census, the other half of sessionhooks-3.
  It moves a printed line, which this build's goal forbids.
- A per-root fallback stamp when no common dir resolves, which the earlier finding D15 of
  `memory/builds/aReapedSpinner/reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round1.md`
  proposed. A non-repo root stays unthrottled, as it is today.
- Moving `readThrottleSeconds` after the stamp `stat`. The window is needed to judge the stamp, and
  reading the conf starts no process.
- One shared JavaScript common-dir resolver. This is the third copy of the walk, beside
  `tools/memory-recall/recall-opened.js#gitCommonDir` and `tools/hooks/scratch-guard.js#resolveCommonDir`.
  A canonical inline block with a parity row is a new gate, so it is a separate unit, outside this
  build.
- The kit version. `tools/push-main.sh@c7cd70b96d5b:26-31` mints it at the landing, so a branch owes
  no bump.
- Any adopter repository, and any help page: no page under `help/` names the monitor (grep over
  `help/`, 2026-11-15).

## 4. Design

### Evidence

Read at `6d98c39ca`. No file under `tools/` differs between it and the base `aebbb4a7`.

- `main` calls `resolveStamp` at `tools/process-monitor/procmon-hook.js@293e9e0dc8b8:105`, before
  the throttle test at `:110`. `resolveStamp` spawns git at `:79` with a 10 s timeout (PINNED,
  `:81`), and answers `null` on any failure (`:85-87`). A `null` stamp skips the throttle at `:110`.
- `writeStamp` creates the stamp's parent with `mkdirSync(..., { recursive: true })` (`:159`). That
  is why S1 answers a stamp only under a common dir that exists: a pointer naming a missing path
  must not make the hook create one.
- `tools/memory-recall/recall-opened.js@17e45cf9b889:61-76` (`gitCommonDir`) is the walk S1 copies.
  It resolves a relative `gitdir:` against the tree root and `commondir` against the worktree git
  dir, which is git's own rule. It does not wrap its reads in `try`; the hook must, because it fails
  open on every path (`:26`).
- The adopter writes the conf at the git toplevel (`tools/process-monitor/adopt-process-monitor.sh@9563ac998981:192`
  and `:219`), and `resolveRoot` answers the directory holding the conf. So `root` is a toplevel,
  where `<root>/.git` exists, in every adopted layout.
- This worktree's `.git` is a file naming `C:/projects/coding-governance/.git/worktrees/project-performance-review-a0e38f`,
  whose `commondir` reads `../..`. S1 resolves that to the primary tree's `.git`, the directory git
  answers.
- The fixture below, run by this writer at `6d98c39ca` against the hook as it stands, printed the
  transcript AC1 compares, and its last step printed `process-monitor: could NOT run` with git off
  `PATH`: the spawn failed, the stamp was `null`, and the census ran despite a fresh stamp.

### The change

`resolveStamp` becomes one `try` block. It `stat`s `<root>/.git`; for a file it matches
`/^gitdir:\s*(.+)$/m` and resolves the worktree git dir with `path.resolve(root, m[1].trim())`; it
reads `commondir` when `fs.existsSync` finds it and resolves it with `path.resolve(gitdir, ...)`;
it answers `path.join(common, 'procmon-stamp')` when `fs.statSync(common).isDirectory()`, else
`null`. The `catch` answers `null`. `execFileSync` stays imported for the census at `:116`.

### What this does not check

- An inherited `GIT_DIR` or `GIT_COMMON_DIR`. Git honoured them; the file read does not. A hook
  launched with one set now stamps under its own root's common dir. No arm stages it.
- A conf placed below the toplevel. Git walked up to the repository; the file read looks only at
  `<root>/.git`, so such a layout answers `null` and stays unthrottled. The adopter's `--check`
  refuses a conf that is not at the toplevel.
- The stamp path's spelling. Git answered forward slashes and the file read answers the platform's
  separators; both name one file, which is what AC1's shared-stamp steps observe.
- S3's fixture is a hand-written pointer, not `git worktree add`. AC1 covers the real layout once,
  in this pass.

### Files touched (estimate)

- `tools/process-monitor/procmon-hook.js`
- `tools/process-monitor/adopt-process-monitor.test.sh`

## 5. Acceptance criteria

Every command runs from the worktree root in Git Bash. `$S` is the session's scratchpad, spelled
absolute. The fixture repository sits under the `md5` folder of `%TEMP%`, because a clone under the
scratchpad's long path fails on Windows. Save the probe below as `$S/md5-probe.sh`, and the hook at
the pass commit's parent as `$S/hook-before.js` with `git show HEAD^:tools/process-monitor/procmon-hook.js`.
The probe builds a primary tree and a linked worktree with `git worktree add`, scopes both confs to an
empty directory, and runs the hook with a python name that cannot exist.

```bash
H=$1; F="$(cygpath -u "$TEMP")/md5"; rm -rf "$F"; mkdir -p "$F/empty"
git init -q "$F/main" && git -C "$F/main" -c user.name=t -c user.email=t@t commit -q --allow-empty -m x
git -C "$F/main" worktree add -q "$F/wt" 2>/dev/null
E=$(cd "$F/empty" && pwd -W)
for d in main wt; do
  sed "s|^PROCMON_ROOTS=.*|PROCMON_ROOTS=\"$E $F/empty\"|" .process-monitor.conf > "$F/$d/.process-monitor.conf"
done
GC=$(git -C "$F/main" rev-parse --path-format=absolute --git-common-dir); NODE=$(command -v node)
hook() {
  printf '{"hook_event_name":"%s"}' "$2" | CLAUDE_PROJECT_DIR="$F/$1" \
    PROCMON_PYTHON=nonesuch-python-shim PATH="$3" "$NODE" "$H" 2>&1; echo "[$1 $2 rc=$?]"
}
hook wt SessionStart "$PATH"; test -f "$GC/procmon-stamp" && echo "[stamp in the common dir]"
hook main PostToolUse "$PATH"; hook wt PostToolUse "$PATH"
rm -f "$GC/procmon-stamp"; hook main PostToolUse "$PATH"
hook wt PostToolUse /nonexistent
```

- **AC1** — When `bash "$S/md5-probe.sh" "$S/hook-before.js" | head -7` and
  `bash "$S/md5-probe.sh" tools/process-monitor/procmon-hook.js | head -7` both run, `diff` of the two
  prints nothing. Both carry `[stamp in the common dir]`, and both print nothing above
  `[main PostToolUse rc=0]` and `[wt PostToolUse rc=0]`: a stamp written from the worktree throttles
  the primary tree.
  Red when: S1 ignores `commondir`, so the stamp lands in the worktree's own git dir, the
  `[stamp in the common dir]` line is missing, and the primary tree's run prints `could NOT run`.
  figure: PINNED. The before transcript is the one this writer's run at `6d98c39ca` printed.
- **AC2** — When `bash "$S/md5-probe.sh" tools/process-monitor/procmon-hook.js` runs, its last line
  is `[wt PostToolUse rc=0]` with nothing printed between it and the line above. Against
  `$S/hook-before.js` the same step prints `process-monitor: could NOT run — spawnSync nonesuch-python-shim ENOENT`
  first.
  Red when: the throttled path still spawns git, which fails with `PATH` naming no directory, so the
  stamp is `null`, the census runs, and the shim's failure prints.
- **AC3** — When `grep -n "'git'" tools/process-monitor/procmon-hook.js` runs it prints nothing.
  When the hook is timed over 10 throttled runs from the fixture's worktree, each hook in turn, beside
  10 runs of `/usr/bin/true` and 10 of `node -e 0`, the after total is below the before total.
  Red when: a git spawn survives on the throttled path, and the totals stay level.
  figure: the after total is DERIVED at observation. The before figures were measured by this writer
  on node a at `6d98c39ca`:
  2.43 s per 10 throttled runs, PINNED at `6d98c39ca`.
  0.34 s per 10 runs of `/usr/bin/true`, PINNED at `6d98c39ca`.
  1.31 s per 10 runs of `node -e 0`, PINNED at `6d98c39ca`.

  ```bash
  F="$(cygpath -u "$TEMP")/md5"; NODE=$(command -v node)
  for H in "$S/hook-before.js" tools/process-monitor/procmon-hook.js; do
    time (for i in 1 2 3 4 5 6 7 8 9 10; do printf '{"hook_event_name":"PostToolUse"}' \
      | CLAUDE_PROJECT_DIR="$F/wt" PROCMON_PYTHON=nonesuch-python-shim "$NODE" "$H" >/dev/null; done)
  done
  time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)
  time (for i in 1 2 3 4 5 6 7 8 9 10; do "$NODE" -e 0; done)
  ```

  The probe's last step leaves the stamp fresh, and the conf's window is 300 s (PINNED,
  `.process-monitor.conf@60c3d42027a9:78`), so run this within that window of AC2.

## 6. Gates

`process-monitor adopter selftest` · `process-monitor wiring` · `kit epoch (shipped bytes move, the version moves)`

The adopter selftest runs every hook arm, S3's included. The wiring leg reads the hook entries the
adopter installs. The epoch leg grades the hook's shipped bytes at the push boundary, where the
lander's mint dates them.

New arm: tools/process-monitor/adopt-process-monitor.test.sh · covers AC2 · the hook restored to its pass commit's parent bytes with `git show`, so the git spawn fails off `PATH` and `test_throttled_path_spawns_nothing` reads `could NOT run` · none

S3's arm builds the worktree layout by hand, with no git process, because a `git` command in a suite
can be steered by an inherited `GIT_DIR`. It writes `$WORK/cleanwt/.git` holding
`gitdir: $CLEAN_GD/worktrees/cleanwt`, writes `../..` into `$CLEAN_GD/worktrees/cleanwt/commondir`,
copies the clean fixture's conf beside it, and runs `"$(command -v node)" "$HOOK"` with
`CLAUDE_PROJECT_DIR="$WORK/cleanwt"`, `PROCMON_PYTHON=nonesuch-python-shim` and `PATH=/nonexistent`,
right after `test_stamp_is_written_after_the_run` has left the stamp fresh. The layout follows
`tools/unattended/gate-guard.test.sh`, which writes a `commondir` the same way.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from the build brief `2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief`,
  item 5, grounded at `6d98c39ca`, whose `tools/` tree matches the base `aebbb4a7`.

## 9. Reuse audit

The seam is `resolveStamp` in `tools/process-monitor/procmon-hook.js`, edited in place, with the
walk of `tools/memory-recall/recall-opened.js#gitCommonDir` carried inline. The process-monitor kit
is copy-installed and cannot require another kit's file, and `recall-opened.js` runs its `main` on
load. `python tools/codebase-map/reuse_lookup.py "resolve the git common dir by reading the .git file, gitdir and commondir without spawning git"`
ranked no JavaScript common-dir resolver; its seams were Python readers and `resolve_kit_dir`. Recall
returned D15 of the aReapedSpinner closing diff review, the same finding at 2026-09-08 with no unit
that closed it, and KICK-dKeptSession-21, which names `tools/hooks/scratch-guard.js#resolveCommonDir`
as the git-free walk. D15's left-shift arm puts a stub `git` script on `PATH`. S3 empties `PATH`
instead, because node on Windows does not run a script shim from `PATH`, as the census-bound arm's
comment in the same suite records for a `.cmd`.

Recall terms used: `python tools/memory-recall/query.py "how does the process monitor hook throttle its census and where is the stamp kept across worktrees" --terms "procmon throttle stamp common dir worktree gitdir commondir spawn hook census recall-opened"`
