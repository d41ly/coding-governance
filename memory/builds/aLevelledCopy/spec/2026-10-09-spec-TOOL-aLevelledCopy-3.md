# TOOL-aLevelledCopy-3 — gov's executed hooks are 100755, and check-wiring grades a hook's index mode

**Status:** CLOSED · rev-3 · 2026-10-09 · node a · Tier-2 · base ce9192c0 · streams tooling · order 2 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aLevelledCopy-3-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aLevelledCopy-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md) | journal | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 DEPL-aLevelledCopy-1 |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-2-build-brief.md) | journal | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 DEPL-aLevelledCopy-1 |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1.md) | research | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 DEPL-aLevelledCopy-1 |
| [2026-10-09-review-TOOL-aLevelledCopy-1-closing-diff-round1.md](../reviews/2026-10-09-review-TOOL-aLevelledCopy-1-closing-diff-round1.md) | diff-review | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 DEPL-aLevelledCopy-1 |

<!-- /gen:spec-records -->

## 1. Goal

gov tracks every file under `.githooks/` at mode 100644, so a POSIX git ignores the branch guard,
the commit-msg check and the pre-push bar, and says so only in a hint. This unit marks the four hooks
git executes 100755 in gov's own tree, and adds a `check-wiring.sh` arm that reports a tracked hook
whose index mode is not executable and repairs it under `--fix`, so the defect cannot return
unnoticed in gov or in an adopter.

## 2. Scope (IN)

- **S1** — gov's tree tracks `.githooks/commit-msg`, `.githooks/pre-commit`, `.githooks/pre-push`
  and `.githooks/pre-rebase` at 100755. No other file under `.githooks/` changes mode: the two
  sourced helper files, the `*.test.sh` suites and the python bar self-test stay 100644. Observed by AC1.
- **S2** — `tools/check-wiring.sh` gains a constant listing git's hook names and an arm,
  `check_hook_modes`, which `check_hooks` calls on the hooks directory in effect. It grades every
  TRACKED file in that directory whose basename is a git hook name, by its INDEX mode, read from the
  index of the checkout that supplies the directory. Observed by AC2, AC5 and AC7.
- **S3** — when this worktree supplies the directory, a hook tracked 100644 is `UNWIRED` under
  `--check` and under `--session`, and `--session` never repairs it. Observed by AC2 and AC4.
- **S4** — under `--fix` the arm repairs the index mode without touching the blob, sets the
  working file's exec bit, verifies the repair by re-reading the index, prints a `FIXED` line and
  appends one `hookmode-set` health event per hook repaired. A second run repairs nothing and logs
  nothing. Observed by AC3.
- **S5** — when ANOTHER checkout supplies the directory, the arm grades that checkout's index and
  reports a 100644 hook as `note`, never `UNWIRED`. A directory no checkout tracks is an announced
  `skip`, never `ok`. Observed by AC5 and AC7.
- **S6** — the script's header comment names the new auto-fix, the new health event and what the
  arm does not check. Observed by AC8.
- **S7** — the self-test's `newrepo` fixture stages its `pre-commit` executable in the index on
  every host, so the existing arms do not acquire a mode finding on a `core.fileMode=false` host.
  The new arms join that suite. Observed by AC9.
- **S8** — the defect and the repair are observed on a real POSIX git: a 100644 hook seen not
  running, then running after `--fix`. Observed by AC6.

## 3. Non-goals (OUT)

- Carrying gov's mode onto an adopter's EXISTING index row. That is `govkit update`'s decision and
  DEPL-aLevelledCopy-1's unit; this unit changes gov's tree and the checker only.
- Grading the working file's filesystem exec bit. On a POSIX checkout git derives it from the index
  mode; on Windows it is not observable. The index is the one source both hosts share.
- Grading a hook directory no checkout tracks, such as a deliberate out-of-tree copy. Its modes are
  the filesystem's and its owner's. The arm says it skipped.
- Repairing under `--session` (F1). A SessionStart hook does not stage an index change.
- Making `core.hooksPath` relative in gov's linked worktrees, which today name the primary's
  directory by absolute path. That is TOOL-dUnstalledConvoy-37's ask and stays there.
- Committing the repair on an adopter's behalf. `--fix` stages it; the operator commits.
- Any kit-version bump. One bump per touched kit happens once, after the last unit.

### Edges

- **hands-off** `DEPL-aLevelledCopy-1` — gov's four hooks at 100755 are that unit's real-world input; carrying the bit onto an adopter's existing engine row is its work, not this unit's.
- **hands-off** external — an adopter's OWN hooks (inCMS tracks `post-merge` and `commit-msg` at 100644) read `UNWIRED` here until the adopter runs `--fix` once and commits; that commit is the adopter's.
- **hands-off** external — the single kit-version bump for the check-wiring kit and for whichever kit ships `.githooks/`, after the last unit of this build.

## 4. Design

### Data model

The mode change is index state only: `git update-index --chmod=+x` over the four clean hook files.
The blobs do not move, so no receipt row changes (the receipt grades oids) and `govkit epoch`'s byte
comparison is unaffected. The staged break shows as `git diff --cached --summary -- .githooks`
printing four `mode change 100644 => 100755` lines while `git diff --cached --numstat` prints `0 0`
for each.

The sourcing claims were verified by grep at writing time: `.githooks/pre-commit` and
`.githooks/pre-push` source `straggler-guard.sh` with `.`, `.githooks/pre-rebase` sources it, and
`.githooks/pre-push` sources `gate-env.sh`. Neither is executed by git or run as a program.

### Inventory

| Identifier | Kind | Cell | Lexicon answer (2026-10-09) |
|---|---|---|---|
| `check_hook_modes` | shell function | `sh.function` | OK, leads with `check` |
| `GIT_HOOK_NAMES` | shell constant | none declared | the `sh.constant` cell is undeclared, so it is ungraded |
| `hookmode-set` | health-log event | the health log's token rule | lowercase token, accepted by `add_health_event` |

`GIT_HOOK_NAMES` holds the 28 hook names of githooks(5), derived 2026-10-09 from the git 2.53 man
page on node a's WSL: `applypatch-msg pre-applypatch post-applypatch pre-commit pre-merge-commit
prepare-commit-msg commit-msg post-commit pre-rebase post-checkout post-merge pre-push pre-receive
update proc-receive post-receive post-update reference-transaction push-to-checkout pre-auto-gc
post-rewrite sendemail-validate fsmonitor-watchman p4-changelist p4-prepare-changelist
p4-post-changelist p4-pre-submit post-index-change`. PINNED: a hook git adds later is not graded
until the list grows.

The health log's event set is OPEN. The orientation card's `render_health_cell` counts every
source and event it finds, which the manifest-check self-test pins with arbitrary tokens, so nothing
else needs extending for `hookmode-set`.

### The arm

`check_hook_modes <dir> <shown>` runs from `check_hooks` in two of its three branches:

| `check_hooks` branch | Directory graded |
|---|---|
| `core.hooksPath` set and resolving to a `pre-commit` | the resolved directory, after `check_hook_blobs` |
| `core.hooksPath` unset | `$ROOT/.githooks`, after the set under `--fix`/`--session`, or beside the `UNWIRED` line under `--check` |
| set but resolving to no `pre-commit` | not graded: that branch already refuses |

The flow, in order:

1. **Supplier.** `git -C "$dir" rev-parse --show-toplevel`. A failure means no checkout tracks the
   directory: print `skip     hooks     — <shown> is tracked by no checkout; its modes are the
   filesystem's and are not graded`, and return.
2. **Population.** `git -C "$supplier" ls-files -s -- "$dir"` at stage 0, kept where the basename is
   in `GIT_HOOK_NAMES`. A failed `ls-files` prints `note ... UNKNOWN` and returns; it never prints
   `ok`. Mode 120000 is a symlink and is not graded. The listing runs from inside the directory
   (`git -C "$dir" ls-files -s`), so a path carrying a `/` is a nested file git never runs as a hook
   and is dropped, and `--show-prefix` turns the rest back into checkout-relative paths. A population
   of none prints `skip     hooks     — <top> tracks no hook-named file directly in <shown>, so no mode
   was graded`, never `ok` over nothing.
3. **Own checkout** (`[ "$supplier" -ef "$ROOT" ]`, compared with `-ef` because node a's TEMP is an
   8.3 short name and a string compare is wrong there). For each 100644 hook:
   - `--check` and `--session`: `UNWIRED  hooks     — <path> is tracked 100644; git on a POSIX node
     will not run it. Fix: bash <kit>/check-wiring.sh --fix, then commit the mode change`, counted.
     The kit path is `${KIT_REL:+$KIT_REL/}`, as the eol arm spells its remedy.
   - `--fix`: `git update-index --cacheinfo 100755,<oid>,<path>` with the oid `ls-files -s` just
     printed, then `chmod +x <path>`, then re-read the entry. 100755 prints `FIXED    hooks     —
     <path> staged 100755 (blob unchanged); commit it` and appends `add_health_event
     "$CW_HEALTH_LOG" check-wiring hookmode-set "<path> 100644 -> 100755 · mode fix"`. Anything else
     prints `UNWIRED` with the command to run by hand, counted.
   - No 100644 hook: one `ok       hooks     — every tracked hook in <shown> is executable` line.
4. **Another checkout.** A 100644 hook prints `note     hooks     — <hook> is tracked 100644 in
   <supplier>, which supplies <shown>; that checkout owns the fix`. Never counted. With no 100644
   hook there, it prints the same `ok` line as step 3. This mirrors
   `check_hook_blobs`, whose header records why a sibling checkout's state never gates here: every
   linked worktree of gov names the primary's directory by absolute path, so until the primary takes
   this landing an `UNWIRED` there would refuse every unattended run's `WIRING_CHECK`.

**Severity.** `UNWIRED` is correct in the own-checkout case by the header's vocabulary: the index
mode is repository state every clone checks out, and on a POSIX clone the hooks are dormant. A
Windows node runs them anyway, which is how the defect stayed hidden, and is not a reason to
downgrade it.

### Files touched (estimate)

- `.githooks/commit-msg`, `.githooks/pre-commit`, `.githooks/pre-push`, `.githooks/pre-rebase` —
  index mode only.
- `tools/check-wiring.sh` — the constant, `check_hook_modes`, its two calls, the header comment.
- `tools/check-wiring.test.sh` — `newrepo` stages `pre-commit` with `git add --chmod=+x`; the new
  arms.
- `memory/map/generated/symbols.json` — regenerated with `gen_map.py --write`, because a new shell
  function stales it.
- This build's acceptance ledger under `memory/builds/aLevelledCopy/build/`, which records AC6.

### Rollout

Sequenced after TOOL-aLevelledCopy-2, which also writes `tools/check-wiring.sh` and its header's
health-event list: building after it means appending to the list it leaves, not merging two edits of
one line. This is `order 2`, and no criterion here rests on that unit's work.

gov's primary tree reads `ok` once this lands there. Each linked worktree reads `note` until then,
and `ok` after, because they grade the primary's index. An adopter reads `UNWIRED` for every
hook-named file its own tree tracks 100644 until DEPL-aLevelledCopy-1's update carries gov's bit
onto the engine rows and the adopter runs `--fix` once for its own hooks.

### Alternatives rejected

- **`git update-index --chmod=+x -- <path>` as the repair.** Rejected by measurement (F3): it
  re-hashes the working file, so a hook carrying an unstaged edit has that edit staged by `--fix`.
  `--cacheinfo` with the index's own oid moves the mode and nothing else. The data change in S1
  still uses `--chmod=+x`, because those four working copies are clean.
- **Reading `GOV_WIRING_HOOKS` as the population.** Rejected (F2): it names gov's four hooks, which
  is right for the blob comparison it serves and wrong here. inCMS tracks its own `post-merge` at
  100644 and it is the same defect.
- **Grading the filesystem bit with `[ -x ]`.** Rejected: always true on Windows and on WSL's
  `/mnt/c`, measured below, so it is a probe that cannot red on the host that hid the defect.
- **Repairing under `--session`.** Rejected (F1).

## 5. Production-readiness checklist

- security — the repair is opt-in under `--fix` and writes one index mode bit and one filesystem bit
  on a file `core.hooksPath` already points git at. It runs no hook and executes no configured value.
  It never touches another checkout's index.
- perf / scale — two git spawns per run (`rev-parse`, `ls-files`), plus three per repaired hook.
  The self-test grows by about five fixture repos against its declared 2320 s ceiling.
- error / empty / loading states — a directory no checkout tracks is an announced `skip`; a failed
  `ls-files` is `note ... UNKNOWN`; a repair that does not re-read as 100755 is `UNWIRED` with the
  manual command. None of them prints `ok`.
- observability — `FIXED` lines and one `hookmode-set` event per repaired hook, which the
  orientation card's health cell counts.
- risks — an adopter's `WIRING_CHECK` (`bash tools/check-wiring.sh --check` in gov's
  `.unattended.conf`) reds after the update until its hook modes are committed. That is the defect
  becoming visible, and the hands-off lines above name who clears it. On a `core.fileMode=false`
  host the existing fixtures would acquire mode findings; S7 removes that before any arm reads them.
- testing — direct fixture observations in §6; the regression arms join the check-wiring self-test,
  which the close runs.
- migration — none in gov beyond the S1 commit. An adopter takes the engine rows' bit through
  DEPL-aLevelledCopy-1 and its own hooks through one `--fix` and a commit.
- user docs — the header comment of `tools/check-wiring.sh` is this kit's documentation; S6
  updates it. No `help/` page exists for this kit.

## 6. Acceptance criteria

Every fixture repository below is created under `%TEMP%/<short-name>` with `core.autocrlf=false`,
except AC6's, which must live on a filesystem that honours the exec bit. The checker is invoked as
`bash <worktree>/tools/check-wiring.sh` from inside the fixture. Other arms print their own lines
there, so each criterion greps the `hooks` lines rather than reading the exit status.

- **AC1** — When `git ls-files -s .githooks | awk '$1=="100755"{print $4}'` runs on the unit's
  commit, it prints exactly `.githooks/commit-msg`, `.githooks/pre-commit`, `.githooks/pre-push` and
  `.githooks/pre-rebase`. Before that commit, `git diff --cached --summary -- .githooks` prints four
  `mode change 100644 => 100755` lines and `git diff --cached --numstat -- .githooks` prints `0 0`
  on each. Red when: `gate-env.sh`, `straggler-guard.sh`, a `*.test.sh` or the python self-test is
  100755, a hook is missing, or a blob changed.
- **AC2** — When `--check` runs in a fixture with `core.hooksPath=.githooks` tracking `pre-commit`
  and `post-merge` at 100644, `pre-push` staged with `git add --chmod=+x`, and `gate-env.sh` and a
  suite file named pre-commit.test.sh at 100644, `grep '^UNWIRED  hooks.*tracked 100644'` matches exactly two lines,
  naming `pre-commit` and `post-merge`. Red when: `post-merge` is missed, or `pre-push`, `gate-env.sh`
  or the suite file is named.
- **AC3** — When `--fix` runs in AC2's fixture after a line is appended to `.githooks/pre-commit`
  without staging it, `git ls-files -s` reads 100755 for both hooks with the oid each had before,
  `git diff --cached --numstat` prints `0 0` for both, `git diff --numstat` still shows the appended
  line, and the health log at `git rev-parse --git-common-dir` holds two `hookmode-set` lines. A
  second `--fix` prints no `FIXED    hooks` line and adds no event. Red when: an oid moves, the edit
  is staged, the event count differs from two, or the second run logs again.
  fixture: built fresh by the observation; the tree holds no such repository.
- **AC4** — When `--session` runs in a fresh copy of AC2's fixture, it prints the two `UNWIRED`
  lines and exits 0, `git ls-files -s .githooks/pre-commit` still reads 100644, and the health log
  holds no `hookmode-set` line. Red when: `--session` stages a mode or logs an event.
- **AC5** — When `--check` runs in a linked worktree (`git worktree add`) whose `core.hooksPath`
  names the primary fixture's `.githooks` by absolute path, with `pre-commit` tracked 100644 there,
  it prints a `note     hooks` line naming the primary's toplevel and `pre-commit`, and
  `grep '^UNWIRED  hooks.*tracked 100644'` matches nothing. Red when: the line is `UNWIRED`, or no
  mode line is printed at all.
- **AC6** — When a fixture on WSL's own filesystem (`wsl.exe -e sh -c`, `mktemp -d` there) tracks a
  `.githooks/pre-commit` that exits 1 at 100644 under `core.hooksPath=.githooks`, `git commit`
  succeeds and git prints its ignored-hook hint. After `bash <worktree via /mnt/c>/tools/check-wiring.sh
  --fix` in that fixture, the same `git commit` exits non-zero. Recorded as a line in this build's
  acceptance ledger. Red when: the commit is refused BEFORE `--fix`, which means the fixture's
  filesystem ran the hook anyway and the observation proved nothing, or it succeeds after.
  fixture: WSL's own `/tmp`, which `df -T` reported as tmpfs and which honours the exec bit, outside
  `%TEMP%`, because `/mnt/c` reports every file 0777 and `chmod -x` is a
  no-op there (measured 2026-10-09, node a); the defect half was measured the same day on git 2.53.
  permission: a POSIX host. On a host where `uname` reads MINGW, MSYS or CYGWIN, the self-test's arm
  for this criterion prints that it skipped and why, and counts no pass.
- **AC7** — When `--check` runs in a fixture whose `core.hooksPath` names a directory outside any
  repository that holds a `pre-commit`, it prints `skip     hooks     — ... tracked by no checkout`
  and no `ok` line about hook modes. Red when: the arm prints `ok` over a population it could not
  read.
- **AC8** — When `grep -n 'hookmode-set' tools/check-wiring.sh` runs, it matches the header
  comment's health-event sentence and the `add_health_event` call, and `grep -n 'GIT_HOOK_NAMES'`
  matches the constant and its one reader. Red when: the header still lists only the earlier events.
- **AC9** — When the `newrepo` fixture's commands run on node a, where `git config core.filemode`
  reads `false`, `git ls-files -s .githooks/pre-commit` reads 100755. Red when: it reads 100644, as
  measured on 2026-10-09 with today's `chmod +x` followed by `git add -A`.

## 7. Gates

`check-wiring self-test` · `branch-guard self-test` · `pre-push self-test` · `pre-push bar self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `transition-audit arms` · `straggler-guard arms` · `recall floor` · `recall floor arms`

The close runs these once, in the bar. `.githooks/` and `tools/` are broad guards for the
guards join (more than five legs each, as `check-spec-tokens.py --list` prints), so the hook legs are
named here by judgment: a mode change moves `ls-files -s`, which is what the bar's leg-guard
fingerprint hashes.

New arm: tools/check-wiring.test.sh · covers AC2 · a fixture with hook and non-hook basenames at 100644, staged with git add --chmod so the modes are host-independent · none
New arm: tools/check-wiring.test.sh · covers AC3 · --fix over a hook carrying an unstaged edit, oid and numstat compared before and after, then a second run · none
New arm: tools/check-wiring.test.sh · covers AC4 · --session over the same fixture, the index still 100644 · none
New arm: tools/check-wiring.test.sh · covers AC5 · a linked worktree whose core.hooksPath names the primary's directory · none
New arm: tools/check-wiring.test.sh · covers AC6 · a hook that exits 1, committed before and after --fix; an announced skip on MINGW, MSYS or CYGWIN · none
New arm: tools/check-wiring.test.sh · covers AC7 · core.hooksPath at a directory outside any repository · none

Each arm's failing case is staged during the build by reverting the arm's own change and observing
the arm RED, then restoring it.

## 8. Open questions

- **F1 — Does `--session` repair a 100644 hook, or only report it?** The peer's text asks for
  repair under `--fix/--session`. Option (a): `--session` repairs, which is the most feature-rich.
  Option (b): `--session` reports and `--fix` repairs. The eol arm's recorded rule is that
  `--session` sets an unset git config and nothing bigger; staging an index change in the operator's
  tree at SessionStart widens that write surface, so M3 veto 3 discards (a). Nothing is lost:
  DEPL-aLevelledCopy-1 makes the normal update commit carry the bit for every shipped hook, and
  `--fix` covers an adopter's own hooks. RESOLVED (agent, 2026-10-09, delegated): (b), `--session`
  reports and `--fix` repairs.
- **F2 — Which hook names does the arm grade?** Option (a): read `GOV_WIRING_HOOKS`, gov's four.
  Option (b): the fixed githooks(5) list. (b) reaches an adopter's own hooks, which carry the same
  defect (inCMS `post-merge`), so it satisfies more of the mandate; no veto applies, because the
  write it adds is the same bit under the same opt-in flag. RESOLVED (agent, 2026-10-09,
  delegated): (b), `GIT_HOOK_NAMES` from githooks(5).
- **FACT-QUESTION · F3 — Does `git update-index --chmod=+x -- <path>` change only the mode?**
  Probe: a scratch repo with a committed file, a line appended without staging, then the command,
  then `git diff --cached --stat --summary`. Deciding observation: any insertion in the cached stat
  means it staged content. Liveness: the same probe with `--cacheinfo 100755,<index oid>,<path>`
  must print the mode change with zero insertions, so the probe can produce either reading. Measured
  2026-10-09 on git 2.54.0.windows.1: `--chmod=+x` staged the appended line, `--cacheinfo` staged
  the mode alone. RESOLVED (agent, 2026-10-09, delegated): the repair uses `--cacheinfo` with the
  oid `ls-files -s` printed.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft from the build's spec brief, with F1 to F3 resolved under the
  mandate and the AC6 fixture's filesystem measured.
- rev-2 · 2026-10-09 · build: §4 The arm states two cases rev-1 left unwritten. A supplier that
  tracks no hook-named file in the directory is a `skip`, because rev-1's "no 100644 hook: ok" read
  literally printed `ok` over an empty population, the vacuous class AC7 exists to refuse. Another
  checkout with no 100644 hook prints the step-3 `ok` line. The listing's run-from-the-directory
  shape is written down. Status CLOSED.
- rev-3 · 2026-10-09 · §6 AC6: the `fixture:` line names WSL's own `/tmp`, tmpfs by `df -T`, in
  place of WSL ext4, which the run that observed AC6 did not use. A record correction from the
  closing review's L5 (finding id 19); no criterion moves and the status stays CLOSED.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "grade a tracked git hook's index file
mode and repair a non-executable hook"` ranked only generic name-stem neighbours, none of which grades
a file mode; no existing seam fits the grading itself. The arm extends three seams found by reading
`tools/check-wiring.sh`: `check_hooks` as its caller and owner of the hooks-dir resolution,
`check_hook_blobs` for the own-checkout versus another-checkout rule and its `note` severity, and
`add_health_event` with `resolve_health_log` for the self-heal record, called exactly as the
`hookspath-set` branch calls them. `gov_tree_mode` in `tools/govkit/govkit.py` reads a mode from
gov's tree for the deployer and is DEPL-aLevelledCopy-1's seam, not this one. The recall probe's
hits that bind this unit: the aScouredKit wave-3 cross-OS review's F1, which first recorded the
100644 hooks; the dCarriedReceipt spec's F1, which chose gov's tree mode for a new row; and
TOOL-dUnstalledConvoy-37, the absolute `core.hooksPath` ask that S5's `note` severity respects. The
path probes added two gotchas the design answers: `hookspath-resolves-into-another-checkout` (S5)
and `fixture-passes-by-finding-nothing` (AC6's Red-when clause and AC7).

Recall terms used: `python tools/memory-recall/query.py "how does gov handle executable bit file
mode of git hooks on POSIX nodes and check-wiring repair" --terms "exec bit 100755 100644 hook mode
gov_tree_mode check-wiring hooksPath POSIX update-index chmod non-executable"`
