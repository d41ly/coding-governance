# Brief — dSweptBranches: a kit that reconciles branches and worktrees, and removes only what landed

**Serves:** research TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5

node d · 2026-10-13 · authorized-by prompt. The owner invoked `/unattended` with `--prompt` and the
value below. It carries whitespace and names no readable file, so it is the prompt itself. Its bytes
are copied here, because the authorization may not point at a file that can change after the run
starts.

## The prompt

```text
A tool and a skill that reconcile and clean up a repository's branches and worktrees, so an owner never has to re-prompt this by hand again. Repo: C:/projects/coding-governance (gov). Fetch first and start from the tip origin/main advertises; 2b852f5f when this was written. It ships as a kit adopters receive through govkit, like drift-audit and runlog.

WHY. On 2026-10-13 an adopter (inCMS, node d) had 71 local branches, 33 remote branches and 60 worktrees. A session spent several hours establishing by hand that 60 branches were merged, 9 more were superseded by later landings, 1 was live in-progress work, and 1 was closed, reviewed work that had never landed and fixed a live production bug. Then it cleaned up. The owner asks for this pass repeatedly, and every session re-derives the method and re-hits the same traps. The method and the traps belong in a tool.

THE TOOL. Read-only by default; it mutates only under explicit write flags. It runs in whatever repo the session is in, resolving the remote and the default branch by the same ladder every kit inlines (GOV_REMOTE, the branch's configured remote, the only remote; GOV_DEFAULT_BRANCH, the remote HEAD, main, master). Remote names vary per node; one adopter node's remote is not called origin.
1. Inventory. Every worktree from `git worktree list --porcelain`: primary, sibling, harness-nested under .claude/worktrees/, detached, prunable, and ones in temp dirs outside the root. Every local branch, every remote branch, and the stash. For each worktree, its dirty state: staged, unstaged, untracked, an in-progress merge or rebase (MERGE_HEAD with unmerged paths), and submodule-pointer drift.
2. Classify every ref and every dirty worktree into one verdict, with its evidence recorded:
   - MERGED: an ancestor of the default branch.
   - EQUIVALENT: `git cherry` shows every commit already applied.
   - SUPERSEDED: each unique commit has a counterpart on the default branch. Match by identical subject, then compare the +/- lines of the two patches. Rebased copies drift by a line or two per patch, which `git cherry` misses. A pre-fold or pre-squash variant counts too when a later landing merge on the default branch names the same unit and covers every file it touched. A run-records-only commit counts when the default branch already shows that build landed.
   - IN-PROGRESS: a non-terminal build record, an unattended run-state file with a live lease, or recent activity under a declared freshness bound. The tool must not depend on any one host app knowing whether a session is running.
   - UNMERGED-LIVE: real unique work that is none of the above.
   - UNKNOWN: anything the predicates cannot decide.
   Merge-tree conflict counts are not a supersession signal: a stale but fully landed branch conflicts heavily. Use `git merge-tree --write-tree` equality with the default branch's tree only as a positive NO-OP proof. A decision row "missing" from the live log may have been rotated into an archive, so search the whole records tree before calling anything unlanded. For uncommitted content (an untracked probe test, an abandoned integration merge), decide whether its substance already landed: the merge's other side is an ancestor of the default branch, or the probe's case exists as a test there.
3. Report. One row per ref or worktree with verdict, evidence, tip, age and the action the tool would take. Byte-stable under no change, and it names every predicate that could not run (a skip announces itself).
4. Write mode, deletes only. A recovery manifest lists every tip and worktree HEAD under the git common dir BEFORE anything is deleted. Worktrees, then local branches, are removed only for MERGED, EQUIVALENT or SUPERSEDED. Remote branches are deleted only under a separate flag, in ONE `git push <remote> --delete`; pre-push hooks skip deletes. The default branch and anything IN-PROGRESS, UNMERGED-LIVE or UNKNOWN are never deleted. A dirty worktree is removed only when its content has its own SUPERSEDED verdict. The tool never merges into, commits on, or pushes the default branch.
5. Windows removal, all measured on that run. `git worktree remove --force --force` fails with "Result too large" on deep node_modules; fall back to rm -rf. Even after a clean removal, the directory often survives as an empty skeleton of pnpm links created under MSYS, whose targets are POSIX paths (/c/...). .NET Directory.Delete and `cmd rmdir /s /q` both refuse those ("The parameter is incorrect"), and a guard hook misread rmdir's /s as a path; GNU `rm -rf`, which never follows links, removes them. Before deleting a skeleton, assert it contains zero regular files (excluding reparse points). Never resolve every link with a spawned readlink per link: it timed out at 600 s over 40 directories. Some empty skeletons stay "Device or resource busy" because an idle desktop session holds them as its cwd: report those, never fail on them.

THE SKILL. It triggers on asks like "clean up branches", "reconcile worktrees", "stale branches" and "is any unmerged work left", and routes through the tool, the way memory-recall routes through its CLI. Attended: it runs the dry report, surfaces UNMERGED-LIVE and UNKNOWN rows at the top as decisions, executes write mode on the owner's yes, and offers to bring an UNMERGED-LIVE branch up to date by merging the default branch into it in its own worktree. On that merge, generated artifacts are re-rendered rather than picking a side, append-only logs are unioned, and the result is gated. Landing still needs the owner's explicit ask and goes through the adopter's own landing path. Unattended: report and safe deletes only, never a merge.

Decided, so the run asks nothing. Reuse rather than duplicate: check-wiring's straggler inventory (the relocation engine's --stragglers) is a narrower cousin. Read it first, and either consume it or state in the README why this is a different population. The unattended kit's run records are the source for IN-PROGRESS and landed-build evidence. Its --settle refuses a LANDING record by design (a later --preflight retires it), so the tool never hand-edits run records. Names come from the lexicon (`lexicon.py --suggest`).

Acceptance: a fixture repo per verdict, each observed RED against a stubbed predicate before the predicate lands. The fixtures:
- a rebased copy with 1–2 lines of drift per patch;
- a pre-fold variant covered by a later landing merge;
- a records-only commit for a landed build;
- a row rotated into an archive;
- a detached worktree holding an in-progress merge whose other side landed;
- a nested harness worktree;
- a temp-dir worktree;
- an untracked probe whose case landed as a test;
- a live run lease;
- an UNMERGED-LIVE branch.
Under write mode the recovery manifest exists before the first deletion, and nothing outside the three deletable verdicts is touched. The report is byte-identical across two runs over an unchanged repo.

Out of scope: landing or pushing anything to the default branch, and the adopter-side pulls.

Also flag, as a separate ask rather than this run's unit: inCMS's memory-local check 21 reads a merge of the default branch into a feature branch as ADDING every memory/ file the default branch gained. Its sibling check 29 already skips merge commits, so a gov-owned check of the same shape should be audited for the same blind spot.

Lessons carried from gov's last runs: every pass commit stages memory/builds/<slug>/RUN.md with its --dispatch and --brief rows. Run python tools/codebase-map/gen_map.py --write after any rename or new function. Bump each touched kit version once, after the last move, and check the carriers with tools/check-kit-versions.sh and `govkit epoch --base <BASE>`. Re-stamp the kickoff manifest's last-audit when a watched path moves. New function names lead with a declared verb (`lexicon.py --suggest`), or the two-sided verb pin moves. Land through tools/push-main.sh, never --no-verify.
```

## The brief

### Goal
A new kit, `branch-reconcile`, ships a read-only CLI that gives every worktree, local branch, remote
branch and stash entry one of six verdicts with its evidence, a write mode that removes only the
three landed verdicts after writing a recovery manifest, and a skill that routes cleanup asks
through it.

### Items
1. The census: the remote ladder, every worktree with its location kind and dirty state, every local and remote branch, the stash, and a byte-stable report that announces each skipped predicate. [planned TOOL-dSweptBranches-1]
2. The verdict ladder: MERGED, EQUIVALENT, SUPERSEDED by its four covering predicates and the merge-tree no-op proof, IN-PROGRESS from run records, build records and freshness, UNMERGED-LIVE and UNKNOWN, over refs and over worktree content. [planned TOOL-dSweptBranches-2]
3. Write mode: the recovery manifest under the git common dir before the first delete, worktrees then local branches, remote branches only under their own flag in one push, and nothing outside the three deletable verdicts. [planned TOOL-dSweptBranches-3]
4. The Windows removal: git's removal, the `rm -rf` fallback, a skeleton removed only when it holds zero regular files, no readlink per link, and a busy directory reported rather than failed. [planned TOOL-dSweptBranches-4]
5. The skill: its triggers, the attended and unattended routes, and the offer to merge the default branch into an UNMERGED-LIVE branch in its own worktree. [planned TOOL-dSweptBranches-5]
6. The side ask: audit gov's checks that read a merge of the default branch as additions. [parked a separate ask by the prompt's own words, filed as TOOL-dSweptBranches-6]

### Acceptance
A fixture repository per verdict, built by the kit's self-test, each predicate's arm observed RED
against unit 1's stub before the predicate lands: a rebased copy with 1 to 2 lines of drift per
patch, a pre-fold variant covered by a later landing merge, a records-only commit for a landed
build, a row rotated into an archive, a detached worktree holding an in-progress merge whose other
side landed, a nested harness worktree, a temp-dir worktree, an untracked probe whose case landed as
a test, a live run lease and an UNMERGED-LIVE branch. Under write mode the recovery manifest exists
before the first deletion, and nothing outside the three deletable verdicts is touched. The report
is byte-identical across two runs over an unchanged repository.

### Gates
`bash tools/run-gates/run-gates.sh` at the close, plus the kit's own `selftest.py`, held on the bar
like every kit self-test and run directly in each pass.

### Non-goals
The tool never merges into, commits on or pushes the default branch, and the skill never lands. No
adopter-side pull. No edit to a run record. No consumption of the relocation engine's straggler
inventory. The side ask is filed, not built.

### Limitations
Stdlib Python and git only, so adopters need no install. Every kit file names nothing outside itself
by literal. The remote ladder is the canonical block from `tools/lib/resolve_remote.py`, inlined
byte-identically. Function names lead with a verb the lexicon declares. The `git merge-tree
--write-tree` proof needs git 2.38 or later, and its absence is a skip that announces itself.

### Reuse
`resolve_remote` in `tools/lib/resolve_remote.py`, inlined as every kit does. The runlog kit's
`kit.toml`, adopter and rendered-skill pattern. The unattended kit's run-state facts `phase`,
`lease-utc`, `host` and `pid`, read as data. `migrate_backlog.py --stragglers` answers a different
question and is not consumed. The reuse probe ranked only name-token neighbours. The recall query
returned the 2026-08-30 worktree bookkeeping finding in `aScouredKit` and no prior tool.

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
