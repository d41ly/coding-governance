# TOOL-dGroundRules-38 — the guard trace keeps no read under the source's git directories, so its verdict does not depend on where `.git` sits

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-38-deviation-26.md](../build/2026-10-23-build-TOOL-dGroundRules-38-deviation-26.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-38-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-38-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 18 at HIGH**, item **H2**, which no other id shares.
`TOOL-dGroundRules-26` S1 copies the source's index in process, and `TOOL-dGroundRules-34` S1 copies
its exclude file in process. In a primary checkout, which remote CI's `actions/checkout` and the main
checkout both are, those files are `.git/index` and `.git/info/exclude`, under the top level, so
`TOOL-dGroundRules-33` S2 keeps them and the leg prints `guard-trace · WRONG` for each. In a linked
worktree, where a build pass runs and S4's sweep looks, they sit outside the top level and the leg is
green. This unit is id 18's promotion: `add_source_read` keeps no path under the source's git
directory or its common directory, both resolved once by git. It repairs `TOOL-dGroundRules-33`,
which sits at order 11, so it builds at order 12.

## 2. Scope (IN)

- **S1** — The directories. When `--fixture` installs `add_source_read`, `read_source_git_dirs(top)`
  runs `git -C <source top level> rev-parse --path-format=absolute --git-dir --git-common-dir` and
  returns both lines, resolved. A `rev-parse` that fails is the run's `WRONG` naming `rev-parse`, and
  no case runs. Observed by AC3, AC4.
- **S2** — The rule. `add_source_read` keeps no resolved path that sits under either directory, in
  a primary checkout, where they are one directory under the top level, and in a linked worktree,
  where they differ and sit outside it. Observed by AC1, AC2.
- **S3** — The readers named. The in-process copy of the index (`TOOL-dGroundRules-26` S1) and of
  the exclude file (`TOOL-dGroundRules-34` S1) are the two reads S2 keeps out today; the
  hands-off edge in `TOOL-dGroundRules-34` §3 names the trace as a reader of that unit's copy.
  Observed by AC1, AC2.

## 3. Non-goals (OUT)

- Ignored paths: `TOOL-dGroundRules-36`. `check-ignore` does not report a path under `.git`, so the
  set-aside there cannot stand in for this rule (§4 Evidence).
- Bytecode caches: `TOOL-dGroundRules-35`. A guard entry under `.git`: `TOOL-dGroundRules-37` reds it,
  since git lists no file there.
- Moving either in-process copy into a subprocess, which would hide the read from the trace rather
  than state why it is not a source read.

### Edges

- **consumes-from** `TOOL-dGroundRules-33` — `add_source_read`, whose kept set S2 narrows, and the `--fixture` hook installation S1 extends
- **consumes-from** `TOOL-dGroundRules-34` — S1's in-process copy of the source's exclude file, one of the two git-directory reads S2 keeps out of the trace
- **hands-off** `TOOL-dGroundRules-52` — S3's claim, AC1 in a clone at the commit under test, and S1's deny branch, which that unit observes (ids 5, 15 and 8 of the round-1 spec audit of units 35 to 43)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `b9f7b5c4e`, on git 2.54.0.

- In this linked worktree, `git rev-parse --path-format=absolute --git-dir --git-common-dir`
  printed `C:/projects/coding-governance/.git/worktrees/unattended-dgroundrules-0e6f4a` and
  `C:/projects/coding-governance/.git`, both outside the worktree's top level.
- `git -C C:/projects/coding-governance rev-parse --git-path index` printed `.git/index`, under that
  checkout's top level (`TOOL-dGroundRules-34` §4 Evidence).
- In the main checkout, `git check-ignore --stdin -v` over `.git/index` and `.git/info/exclude`
  printed nothing for either.
- The review's `--legs-for` query printed `.git/index (not tracked at HEAD)` and `no guarded leg`,
  and the same for `.git/info/exclude` (review id 18).

### The rule

```text
--fixture, before the first case:
    git_dirs = read_source_git_dirs(source top level)   # rev-parse --path-format=absolute,
                                                        # --git-dir and --git-common-dir, resolved
    sys.addaudithook(add_source_read)

add_source_read(event, args):                  # TOOL-dGroundRules-33 S2, this unit's line marked +
    (unit 33's event, mode and resolve steps)
+   if p sits under any of git_dirs: return
    (unit 33's top-level and temporary-directory tests)
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `read_source_git_dirs` | py.function | `tools/policy/check_policy.py` |

`lexicon.py --suggest read_source_git_dirs --as py.function` answered OK on 2026-10-23.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A literal `.git` segment test.** It misses a common directory named anything else, and a
  `GIT_DIR` set by the caller; git's own answer covers both.
- **Keep only paths git tracks.** It holds here too, but it blinds the trace to a new source file a
  case reads before its commit (`TOOL-dGroundRules-36` §4 Alternatives rejected).

## 5. Production-readiness checklist

- security — N/A: one read-only `rev-parse`; nothing is written.
- perf / scale — one `rev-parse` per `--fixture` run and one prefix test per `open` event.
- error / empty / loading states — a failed `rev-parse` is a named `WRONG` before any case runs.
- observability — none added; a git-directory read simply no longer reaches the join.
- risks — a source repository whose git directory holds a real source file is not a layout git
  produces.
- testing — AC1 to AC4, in a primary clone and in a linked worktree.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: a gov-only leg.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. `check_policy.py` names the
policy kit's file under the kit, as `TOOL-dGroundRules-33` §6 does. A primary clone sits under
`%TEMP%/<short name>`, because a long path fails a clone on this node. Literal commands are spelled
whole here and named by the criteria:

```text
PRIMARY     = git clone -q <this repository> "$TEMP/gr38" && cd "$TEMP/gr38"
UNEXCLUDE   = in that clone's check_policy.py, read_source_git_dirs staged to return ()
DIRS_PROBE  = python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c;
              print(*c.read_source_git_dirs('.'), sep='\n')"
```

- **AC1** — When `PRIMARY` runs and then `python check_policy.py --fixture adopter-fresh-target`
  runs inside the clone, it prints no `guard-trace` line naming `.git/`.
  Red when: the leg's verdict differs between a primary checkout and a linked worktree.
  cost: one clone and one installing case, tens of seconds.
- **AC2** — When `PRIMARY` and `UNEXCLUDE` run and then the AC1 command runs, it prints
  `guard-trace · WRONG .git/index`.
  Red when: a git-directory read reaches the join with nothing to say so.
- **AC3** — When `DIRS_PROBE` runs in this repository's linked worktree, it prints two different
  directories, the second being the main checkout's `.git`; run inside the `PRIMARY` clone, it
  prints the clone's `.git` twice.
  Red when: the common directory, where a linked worktree's exclude file lives, is not excluded.
- **AC4** — When `--fixture adopter-fresh-target` runs with the working directory set to a
  directory under `%TEMP%` that is not a repository, and the kit is named by its absolute path, it
  prints the same verdict as from the repository root.
  Red when: the directories are asked of the caller's working directory, not of the source.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the trace;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture`, the `guard-trace` join) · covers AC1 AC2 · a primary clone of the built tree, then the git-directory rule staged out there · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 18 (HIGH, item H2) of the round-1 spec
  audit of units 33 and 34, from the review's sound fix, with `rev-parse` and `check-ignore` run in
  this worktree and the main checkout on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.

## 10. Reuse audit

The seams extended are `add_source_read` (`TOOL-dGroundRules-33` S2) and git's own answer for where
a repository's directories sit, `rev-parse --path-format=absolute --git-dir --git-common-dir`, the
flag `TOOL-dGroundRules-34` S28 already requires of every `--git-path` call in the snapshot.
`python tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"`
ranked `git`, `run_git`, `read_git_output` and `build_git_env`, which run git and resolve no git
directory for a caller: no existing seam fits. The recall probe returned `TOOL-aGraftedHelix-45`,
a location probe asked from a moved directory, which is this class's sibling, and this audit's H2;
both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how does a file-access trace treat bytecode
caches, ignored paths and the git directory" --terms "audit hook trace pycache bytecode gitignored
guard-trace policy fixtures legs-for git-dir worktree"`
