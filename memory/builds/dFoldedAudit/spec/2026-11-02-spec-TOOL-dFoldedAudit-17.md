# TOOL-dFoldedAudit-17 — origin/main reconciled into the run branch: the eight conflicted paths merged additively

**Status:** INPROGRESS · rev-3 · 2026-11-02 · node d · Tier-1 · base 8a5328a9 · streams tooling · order 170

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-17-1-spec-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-17-1-spec-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-17-2-builder-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-17-2-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-17-3-spec-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-17-3-spec-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-17-4-builder-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-17-4-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-17-5-spec-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-17-5-spec-return.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-1-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-2-builder.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-2-builder.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-3-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-3-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-4-builder.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-4-builder.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-5-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-5-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-6-builder.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-6-builder.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-7-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-7-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-fix-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-fix2-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-fix2-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-fix3-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-fix3-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The run branch takes `origin/main` by one `git merge`, and each of the eight paths both sides changed
keeps both sides' content. The close's `--prepare` then meets no conflict. The owner asked on
2026-11-02 for the merge to go by git.

## 2. Scope (IN)

- **S1** — The merge runs in the run worktree itself, on `branch/gov-build-m4-spec-audit-694e7b`,
  which the shared config gives the hooks path and both merge drivers, `rows` and `ours`. The clean
  worktree fetches `origin`, the GitHub remote, and runs `git merge --no-ff --no-commit origin/main`. A
  conflict on any path outside §4's table, or any failed step before M, stops the unit, and
  `git merge --abort` restores the worktree. Observed by AC1.
- **S2** — `.memory-tree.conf` keeps both blocks unchanged: main's `SPEC_AC_ORDER_CUTOFF`
  (`TOOL-dSafePassage-34`) first, then this build's `SPEC_SUPERSEDE_CUTOFF` (`TOOL-dFoldedAudit-4`).
  Observed by AC2, AC3 and AC6.
- **S3** — `tools/check-spec-tokens.py` keeps both docstring join entries, `supersede` then `ac-order`.
  `main()` reads both cutoff keys and returns 1 when either read refuses. Observed by AC2, AC3, AC4,
  AC6 and AC8.
- **S4** — `tools/check-spec-tokens.test.sh` keeps main's two history lines, re-bases this build's line to
  `203 -> 215`, and sets `FLOOR_ASSERTIONS` to 215. Observed by AC2, AC5 and AC6.
- **S5** — `tools/drift-audit/drift_signals.py` keeps main's `36 -> 37` history line. This build's line
  becomes `37 -> 39` under decision `TOOL-dFoldedAudit-16`, naming both keys, and the pin reads 39.
  Observed by AC2, AC6, AC7 and AC9.
- **S6** — `memory/map/features/spec-tokens.md` keeps both paragraphs, main's criterion-order key first.
  Observed by AC2, AC3 and AC6.
- **S7** — `memory/guides/SESSION-KICKOFF.md` keeps main's `last-body-change`. Its `last-audit` stamp is
  re-taken by the checker's rule twice: at the merge commit on the branch tip, and in the follow-up
  commit on the merge commit's sha. Observed by AC2 and AC12.
- **S8** — Generated files are re-rendered, never hand-merged. The merge commit carries the map and
  every file `gen_build_index.py --write` rewrites, as their writers render them. Those are
  `memory/LIVE.md`, the 2026-11 ledger, the dClosedLoop as-built view and dSafePassage's README
  generated block. Each is a render, not an authored write. `.governance/policy.json` enters the merge
  commit as one parent's blob and is re-rendered in the follow-up commit. Observed by AC10 and AC11.
- **S9** — Every commit runs with `GOV_PYTHON` exported to the Python 3.15 interpreter §4 names, because
  main's resolver floor is 3.15. NOT OBSERVED by a criterion: it is a precondition of the two commits,
  and a hook that resolves no usable launcher refuses the commit (`.githooks/pre-commit:286-288`).
- **S10** — M and F are committed in the run worktree, on the run branch, each ending with the
  charter's trailer. The shared remote-tracking `origin/main` that S1's fetch moved names M's second
  parent. Observed by AC13.

## 3. Non-goals (OUT)

- Any behaviour change on either side. A defect found in either side's code is reported, not fixed.
- `memory/DECISIONS.md`. The row `TOOL-dFoldedAudit-16` at `memory/DECISIONS.md:244` reads `36 -> 38`
  because it was written before this merge. Its substance, a raise of two for these two keys, holds,
  and the row is not rewritten.
- Re-deriving `SPEC_SUPERSEDE_CUTOFF` or arming `SPEC_FOLD_CUTOFF`. The first is the landing's, and the
  second is the close's.
- A kit version mint. The merge brings main's version markers and the lander mints at landing.
- This unit's status flip to CLOSED, its acceptance ledger and its pass commit. They are the main
  loop's, after F, and neither M nor F carries the flip.
- A clone of the run branch, `--no-verify`, or a `GOV_DEFAULT_BRANCH` override of the branch guard.
- Undoing M once it is committed. A refused F stops the unit and is reported, with no reset.
- Running any suite or the bar inside the pass.
- The parked question of the two unattended suites, recorded in this build's `RUN.md`.

## 4. Design

Line numbers are this tree's at `951f44e4`, PINNED 2026-11-02, unless a line says otherwise. Those a
rev-3 sentence adds are the run worktree's at `4d779489`, unless they name main. The trial
merge is `git merge-tree --write-tree --name-only` over `951f44e4` and `8a5328a9`, taken 2026-11-02.

### The conflict set

| Path | Hunks | Kind | Resolution |
|---|---|---|---|
| `.memory-tree.conf` | 1 | conf | both blocks, main's first |
| `tools/check-spec-tokens.py` | 2 | product | docstring: both entries; `main()`: both reads |
| `tools/check-spec-tokens.test.sh` | 1 | suite | main's history, this build's re-based, floor 215 |
| `tools/drift-audit/drift_signals.py` | 1 | pin | main's line, a `37 -> 39` line, pin 39 |
| `memory/map/features/spec-tokens.md` | 1 | dossier | both paragraphs, main's first |
| `memory/guides/SESSION-KICKOFF.md` | 1 | stamps | stamp re-taken, main's `last-body-change` |
| `memory/map/generated/symbols.json` | — | generated | `gen_map.py --write` |
| `.governance/policy.json` | — | generated | a parent's blob, then `policy.py mirror --write` |

Twenty-two other paths both sides changed auto-merge. Each template and render pair among them, the two
Skills, the method guides and the review workflow, gains only main's kit-version marker line on both
halves. So an
auto-merged pair stays a pair, and no render needs a hand step.

Re-read 2026-11-02 at `origin/main` `84acebdc`, the tip the builder's first dispatch fetched
(`memory/builds/dFoldedAudit/build/2026-11-02-build-TOOL-dFoldedAudit-17-2-builder-return.md`).
`8a5328a9` is its ancestor, and `git diff --name-only 8a5328a9 84acebdc` over the table's eight paths
prints nothing, so none of them moved. The figures hold: floor 215, pin 39, `last-body-change`
`201eb127`. `git merge-tree --write-tree --name-only`
over `d9d556dd` and `84acebdc`, in the run repository, names the same eight. The auto-merged set is
twenty-four. The two it gained are `tools/roles/SKILL.template.md` and `.claude/skills/build/SKILL.md`,
and main moves each from `roles@1.10` to `roles@1.11` on its kit marker line alone, so they stay a pair.
A later tip still re-derives by the last subsection's rule.

### S1 — the run worktree

The merge runs in the run worktree, on `branch/gov-build-m4-spec-audit-694e7b`, where units 1 to 16
committed. Pre-commit's branch guard (`.githooks/pre-commit:71-93`) refuses a commit on a non-default
branch only in a primary tree, which it tells by the git dir equalling the common dir (`:75-77`). A
clone is a primary tree, and the guard refused M there in the builder's second dispatch
(`memory/builds/dFoldedAudit/build/2026-11-02-build-TOOL-dFoldedAudit-17-4-builder-return.md`). The
run worktree is a linked worktree: its git dir is `.git/worktrees/gov-build-m4-spec-audit-694e7b` and
its common dir `.git`, measured 2026-11-02, so the guard admits its commits.

The worktree reads the run repository's shared `.git/config`, measured 2026-11-02 with
`git config --show-origin`:

| Key | Value |
|---|---|
| `core.hooksPath` | `C:\projects\coding-governance\.githooks` |
| `merge.rows.driver` | `bash tools/memory-tree/merge-rows.sh %O %A %B %P` |
| `merge.ours.driver` | `true` |
| `remote.origin.url` | `https://github.com/d41ly/coding-governance` |

`.gitattributes` routes `memory/LIVE.md`, `memory/ledger/*.md` and the dClosedLoop as-built record to
`merge=ours` (`.gitattributes:90-91` and `:100`), and the authored indexes to `merge=rows` (`:77-84`).
Both drivers are set, so the merge conflicts on the eight alone, as the trial merge in this repository
showed. `origin` is GitHub, so `git fetch origin` reads main's tip directly and moves the shared
`refs/remotes/origin/main`.

The hooks path is the primary tree's checkout, at local `main` `2a6f3975`. Its `.githooks/` is
byte-identical to the branch's, and main changes only three pre-push files there, so
`.githooks/pre-commit` is the same at the branch, local `main` and `84acebdc`. M and F meet the
pre-commit that main runs. The hook sources the tracked resolver from the work tree it grades
(`.githooks/pre-commit:282-286`), so mid-merge that is the merged `tools/lib/resolve-python.sh` with
main's floor.

The write gate places a target by its own toplevel (`tools/hooks/scratch-guard.js:1142-1144`) and reads
the routed spec in that tree (`:884`). A hand resolution in the worktree therefore meets this spec at
INPROGRESS, and this unit is routed, so the gate admits it. The session-start route line resolves its
tree from `CLAUDE_PROJECT_DIR` or the cwd (`:1473-1478`), and this pass saw it report the spec absent.
That line describes another tree and is not the gate's verdict.

`GOV_PYTHON` names Python 3.15.2. Both sides' resolvers try a caller's override, then `GOV_PYTHON`, then
`python3` (`tools/lib/resolve-python.sh:30`, and line 36 of main's copy at `84acebdc`), so the exported
path is the one the resolver reaches first. `python3` on PATH answers 3.15.2 too, measured 2026-11-02, so the resolver's fallback also clears
the 3.15 floor.

```bash
export GOV_PYTHON=C:/Users/d41ly/AppData/Local/Programs/Python/Python315/python.exe
RUNWT=C:/projects/coding-governance/.claude/worktrees/gov-build-m4-spec-audit-694e7b
P="$TEMP/dFoldedAudit-17-probes"; mkdir -p "$P"
cd "$RUNWT"
test "$(git branch --show-current)" = branch/gov-build-m4-spec-audit-694e7b
test "$(git rev-parse --path-format=absolute --git-dir)" != "$(git rev-parse --path-format=absolute --git-common-dir)"
test -z "$(git status --porcelain)"
git config --get core.hooksPath
git config --get-regexp '^merge\.'
git fetch origin
git merge --no-ff --no-commit origin/main
git diff --name-only --diff-filter=U
```

`--no-commit` holds the merge open, so the generated renders and the stamp land in the merge commit.
The builder records `git rev-parse origin/main`. Every figure below is PINNED at `8a5328a9`, and the
last subsection says what re-derives when the tip has moved. The probes and `drift.err` live in `$P`,
outside the worktree, so `git status` shows the merge's own paths alone.

### The stop

The worktree is clean before the merge, so the merge is its only change. Any failed step before M
leaves `MERGE_HEAD` set. That covers a conflict outside §4's table, a missing driver, a resolution that
does not hold, and a refused M. `git merge --abort` then restores the worktree to the branch tip. That
is the unit's stop, and the builder reports which step failed. Once M is committed no step undoes it.
A refused F leaves M on the branch and F's changes staged, and the builder stops and reports without a
reset.

### S2 to S6 — the hand resolutions

`.memory-tree.conf`: main's `TOOL-dSafePassage-34` block, one blank line, then this build's
`TOOL-dFoldedAudit-4` block from `.memory-tree.conf:979-1010`, each byte-identical to its side. The
supersede comment's "like SPEC_HANDOFF_CUTOFF above it" stays true, since that key still sits above.

Neither key's relation moves. `check_cutoff_relation` (`tools/check-spec-tokens.py:703-735`) dates a
value by `git log -S` over the conf, and pickaxe lists no merge commit. Measured: over `origin/main` it
lists only `56aef62a` for `SPEC_AC_ORDER_CUTOFF`, though landing merges brought that line into main.
So `SPEC_SUPERSEDE_CUTOFF` stays dated by `a3f5150b`, 2026-11-02, and 2026-11-03 stays strictly past.

`tools/check-spec-tokens.py`: the docstring keeps the branch's `supersede` entry, then main's
`ac-order` entry, then the blank line before `REFUSALS`. The reads in `main()` become these, extending
the branch's tuple form at `tools/check-spec-tokens.py:1542-1543`:

```python
    supersede_cut = read_cutoff_key(root, SUPERSEDE_KEY)
    ac_order_cut = read_cutoff_key(root, AC_ORDER_KEY)
    if None in (legline_cut, direct_cut, handoff_cut, guards_cut, supersede_cut, ac_order_cut):
        return 1
```

`read_cutoff_key` answers `None` on a refusal and a string otherwise, so the tuple test returns 1 exactly
when main's `is None` chain did. Every other hunk of both joins auto-merges.

`tools/check-spec-tokens.test.sh`: main's two lines, `199 -> 200` and `200 -> 203`, then this build's
four-line entry from `tools/check-spec-tokens.test.sh:52-55` with its first line re-based, then the floor:

```bash
# RAISED 203 -> 215 by TOOL-dFoldedAudit-4: its twelve supersede-join arms, the phrase in prose, wrapped
FLOOR_ASSERTIONS=215
```

The three continuation lines between those two are the branch's, unchanged. 215 is main's 203 plus this
build's twelve, counted by reading and observed by the suite at the close.

`tools/drift-audit/drift_signals.py`: after main's two-line `36 -> 37` entry, the branch's three lines at
`tools/drift-audit/drift_signals.py:351-353` give way to these four, and the pin reads 39:

```python
    # 37 -> 39 at dFoldedAudit's close, 2026-11-02, under decision TOOL-dFoldedAudit-16, whose 36 -> 38 was
    # written before this branch took origin/main's 37: TOOL-dFoldedAudit-4 arms SPEC_SUPERSEDE_CUTOFF in
    # .memory-tree.conf and TOOL-dFoldedAudit-7 SPEC_FOLD_CUTOFF in .unattended.conf, armed at the close; no key
    # stopped being armed.
    "cutoff_keys_armed": 39,
```

The ratchet compares the pin with its value at `refs/remotes/origin/main`, 37, and wants a comment naming
`37 -> 39` within 14 lines above it (`tools/drift-audit/drift_report.py:268-275`). The armed count,
taken with the signal's own parser over both sides' tracked root confs, is 37 on each side and 38 in
their union. So the row reads `ok (pin 39, drain it)` until the close arms `SPEC_FOLD_CUTOFF`, and 39
against 39 after it.

`memory/map/features/spec-tokens.md`: main's criterion-order paragraph, one blank line, then the branch's
paragraph from `memory/map/features/spec-tokens.md:133-147`.

### S7 — the stamps

The conflict takes the branch's `last-audit` line from `memory/guides/SESSION-KICKOFF.md:5`. The merge
auto-takes main's `last-body-change`, `201eb127`, which the merge makes an ancestor of HEAD.

Two rules of `skills/session-kickoff/manifest-check.sh` then force two re-stamps, as the dSafePassage
reconcile `37b3bf32` and its follow-up `f25d719e` did:

- The staged leg (`:1659-1669`) refuses a commit staging a watched file unless its stamp differs from
  HEAD's. The merge stages main's watched changes, so the merge commit stamps
  `last-audit: <now> @ <the branch tip's full sha>`, the sha `git rev-parse HEAD` answers mid-merge.
- The full leg (`:1525-1545`) wants a stamp change at or after the newest watched commit. Its candidates
  come from `git log -G`, which lists no merge commit, so a stamp inside the merge commit is not seen. The
  follow-up commit stamps `last-audit: <later now> @ <the merge commit's full sha>`.

The stamp's sha is `HEAD` on any branch, the rule `STAMP_SHA_RULE` holds at `:1405`. Its datetime is
ISO-8601 with its offset (`:1442-1443`) and always advances
(`skills/session-kickoff/MANIFEST-TEMPLATE.md:30`). Each commit message carries the kit's record line
(`skills/session-kickoff/SKILL.md:121-122`):

```
manifest-audit: delta none · watch-commits-since-stamp: <n>
```

`<n>` is DERIVED by `git rev-list --count <old-stamp-sha>..HEAD -- <watch…>`, counted before that
commit's re-stamp.

Main's watched changes are two `.memory-tree.conf` changes, the method guide's kit marker, the inline
resolver block in five scripts and four gate legs. The conf changes are the `SPEC_AC_ORDER_CUTOFF`
block S2 resolves, and `docs-undocumented.txt` added to `PROJECT_REGISTRY_EXTRA` by
`TOOL-dSafePassage-13`, at line 925 of main's conf. That addition sits outside the conflicted hunk and
merges clean, and no §B line names the key.

One §B line names the resolver floor. It is `memory/guides/SESSION-KICKOFF.md:219` at `84acebdc`, and
line 223 of the conflicted blob. Main added it in `1f7d1966`, whose parent `201eb127` is the sha its
`last-body-change` names, and it is current at main's tip. So the expected delta stays none, measured
2026-11-02, and the builder re-reads §B to confirm it. The stall check then counts 5 non-merge watched
commits since `201eb127`, below its 10 (`:1633-1653`).

### S8 — generated files

Before the merge commit, `"$GOV_PYTHON" tools/codebase-map/gen_map.py --write` renders
`memory/map/generated/`, which settles `symbols.json` and the auto-merged `CARDS.md`. Then
`"$GOV_PYTHON" tools/memory-tree/gen_build_index.py --write` rewrites these files, each a render and
none an authored write:

| File | Why it moves |
|---|---|
| `memory/LIVE.md` | `merge=ours`, both sides changed it |
| `memory/ledger/2026-11.md` | `merge=ours`, both sides changed it |
| `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` | `merge=ours`, both sides changed it |
| `memory/builds/dSafePassage/README.md`, its generated block | main alone changed it |

The set was measured by the builder's second dispatch on 2026-11-02, and `git diff --name-only` from
the merge base to each side confirms the "both sides" and "main alone" cells. The `ours` driver keeps
the branch's bytes for the first three, and the render re-derives them from both sides' records, as
`.gitattributes:95-96` says of the view. A later tip may move another file the writer owns. Whatever
`--write` rewrites is staged and named in M's body. Both writers' output is staged with the merge. The hooks need this: the codebase-map leg grades the work tree
whenever a `.py` file is staged (`.githooks/pre-commit:280-307`), and hygiene check 9 delegates to the
build index's `--check`.

`.governance/policy.json` is guarded. The policy guard admits a merge path whose staged blob is HEAD's
or `MERGE_HEAD`'s (`tools/policy/guard.py:90-96`), so the merge commit takes `git checkout --ours --
.governance/policy.json`. Either parent's blob is admitted, and the follow-up commit replaces it. The
mirror renders at HEAD and records the catalogue's blob (`tools/policy/policy.py:1382-1426`), and the
merged catalogue is a new blob, so it is stale until a commit holds the merge. The follow-up commit runs
`"$GOV_PYTHON" tools/policy/policy.py mirror --write`, which the guard admits as a render at HEAD.

### S10 — the commits

| Commit | Subject | Carries |
|---|---|---|
| M | `merge: origin/main into branch/gov-build-m4-spec-audit-694e7b — dFoldedAudit reconciled before its landing` | the resolutions, the renders, the first stamp |
| F | `records(dFoldedAudit): the kickoff manifest re-stamped and the policy mirror re-rendered at the reconcile merge <M8>` | the second stamp, the mirror |

Both end with `Pass: none`, then the charter's trailer:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

`--check-commit` admits a `none` trailer (`tools/unattended/unattended.sh:14087`), and the
routed-commits leg does not grade a merge's content (`tools/memory-tree/routed_commits.py:33-34`).
M's body names each resolution in one line.

Both commits land on `branch/gov-build-m4-spec-audit-694e7b` in the run worktree, so nothing follows
them. S1's fetch already moved the shared `refs/remotes/origin/main` to the tip M takes as its second
parent, and the close's drift read compares against that ref. A fetch by another session in between
can move it past that tip, and AC13 then reds.

### The probes

Probe P, `twoparent.py` in `$P`, prints each line a side added that the result lacks:

```python
import subprocess, sys
base, sides, files = sys.argv[1], sys.argv[2:4], sys.argv[4:]
for f in files:
    have = set(open(f, encoding="utf-8").read().splitlines())
    for side in sides:
        diff = subprocess.run(["git", "diff", "-U0", base, side, "--", f], capture_output=True,
                              text=True, encoding="utf-8").stdout
        for line in diff.splitlines():
            if line.startswith("+") and not line.startswith("+++") and line[1:] not in have:
                print(f, side, "|", line[1:])
```

Run on M, it prints exactly the thirteen lines this design rewrites, and nothing else:

| File | Side | The line |
|---|---|---|
| `tools/check-spec-tokens.py` | `HEAD^1` | the branch's `if None in (…, supersede_cut):` |
| `tools/check-spec-tokens.py` | `HEAD^2` | main's two-line `if (legline_cut is None …` |
| `tools/check-spec-tokens.test.sh` | `HEAD^1` | `# RAISED 199 -> 211 by TOOL-dFoldedAudit-4: …` and `FLOOR_ASSERTIONS=211` |
| `tools/check-spec-tokens.test.sh` | `HEAD^2` | `FLOOR_ASSERTIONS=203` |
| `tools/drift-audit/drift_signals.py` | `HEAD^1` | the three `36 -> 38` comment lines and the pin at 38 |
| `tools/drift-audit/drift_signals.py` | `HEAD^2` | the pin at 37 |
| `memory/guides/SESSION-KICKOFF.md` | both | each side's `last-audit` line |

Simulated 2026-11-02 over the merge tree's marked blobs with these resolutions applied, it printed twelve
of them. The thirteenth, the branch's `last-audit` line, is absent only once M re-takes the stamp.

Probe D, `pin.py` in `$P`, run from the worktree's root, reads the pin the way the ratchet does:

```python
import subprocess, sys
sys.path.insert(0, "tools/drift-audit")
import drift_report as d
base = subprocess.run(["git", "show", "refs/remotes/origin/main:tools/drift-audit/drift_signals.py"],
                      capture_output=True, text=True, encoding="utf-8").stdout
old, _ = d._scalar_at(base, "cutoff_keys_armed")
text = open("tools/drift-audit/drift_signals.py", encoding="utf-8").read()
new, at = d._scalar_at(text, "cutoff_keys_armed")
print(old, new, d._justified(text, at, old, new, 14))
```

At `951f44e4` it prints `37 38 True`, and on the simulated resolution `37 39 True`.

### When the fetched tip is not 8a5328a9

The rules hold and the figures re-derive. The floor is main's `FLOOR_ASSERTIONS` plus 12, under a
`<main's> -> <main's + 12>` line. The pin is main's pin plus 2, under a `<main's> -> <main's + 2>` line.
Probe P's table holds main's values in place of 203 and 37. The ledger records the tip and both figures.

### Files touched (estimate)

`.memory-tree.conf`
`tools/check-spec-tokens.py`
`tools/check-spec-tokens.test.sh`
`tools/drift-audit/drift_signals.py`
`memory/map/features/spec-tokens.md`
`memory/guides/SESSION-KICKOFF.md`
`memory/map/generated/symbols.json`
`.governance/policy.json`

The merge also carries every path main moved, and the two writers re-render the generated files above.

### Alternatives rejected

- **A scratch clone of the run branch.** A clone is a primary tree, so on a non-default branch the
  branch guard refuses its commits (`.githooks/pre-commit:77-92`). Its only overrides are `--no-verify`
  and `GOV_DEFAULT_BRANCH`, and either one bypasses the guard rather than meeting it. The second
  dispatch met that refusal at M.
- **Taking one side of any hand-resolved file.** Each side's lines carry a landed unit's behaviour, and
  probe P is what shows none was lost.
- **Pin 38 with a `37 -> 38` line.** The merged tree arms 38 keys at the merge and 39 at the close, so
  the close would read over the pin.
- **The mirror re-rendered inside the merge commit.** During the merge HEAD is the branch tip, so the
  render is neither a parent's blob nor a render at the commit's own HEAD, and the guard refuses it.
- **One re-stamp only.** The full leg cannot see a stamp inside a merge commit, and the staged leg
  refuses a merge commit without one.

## 5. Acceptance criteria

Run in the run worktree, with `GOV_PYTHON` exported and `P` set as §4's S1 block sets it. `HEAD` is M
unless a criterion says F. Probes P and D are §4's.

```bash
EIGHT=".governance/policy.json .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/features/spec-tokens.md memory/map/generated/symbols.json tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/drift-audit/drift_signals.py"
SIX=".memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/features/spec-tokens.md tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/drift-audit/drift_signals.py"
```

- **AC1** — When `git diff --name-only --diff-filter=U` runs right after the merge, it prints exactly the
  eight paths of `$EIGHT`.
  figure: PINNED, measured by `git merge-tree --write-tree` over `951f44e4` and `8a5328a9` on 2026-11-02,
  and over `d9d556dd` and `84acebdc` the same day, both in the run repository with its two merge drivers.
  Red when: the fetched tip conflicts on a ninth path, or the shared config lacks a merge driver, which
  adds the three `merge=ours` paths. Either stops the unit with `git merge --abort` before any
  resolution.
- **AC2** — When `git grep -n -E '^(<<<<<<<|>>>>>>>)( |$)' HEAD -- $EIGHT` runs it prints nothing, and
  `git diff --check HEAD^1 HEAD -- $SIX` and `git diff --check HEAD^2 HEAD -- $SIX` print nothing.
  figure: PINNED, on the unresolved merge tree the grep prints 46 lines and the diff check 21 marker
  lines, and over each parent the grep prints 0, measured 2026-11-02.
  Red when: a conflict marker or a whitespace error survives in a resolved file.
- **AC3** — When `grep -n '^SPEC_AC_ORDER_CUTOFF=\|^SPEC_SUPERSEDE_CUTOFF=' .memory-tree.conf` runs, it
  prints the `"2026-10-23"` line before the `"2026-11-03"` line. When
  `grep -n '^  supersede the supersede join\|^  ac-order the criterion-order join' tools/check-spec-tokens.py`
  runs it prints the supersede line first, and
  `grep -n '^\*\*The criterion-order key\|^\*\*A repair rewrites its sibling' memory/map/features/spec-tokens.md`
  prints the criterion-order line first.
  Red when: a block, an entry or a paragraph is lost, or sits in the other order.
- **AC4** — When `"$GOV_PYTHON" -m py_compile tools/check-spec-tokens.py tools/drift-audit/drift_signals.py`
  runs, it exits 0.
  Red when: a marker or a half-merged `if` leaves either file unparseable.
- **AC5** — When `grep -n 'RAISED 200 -> 203\|RAISED 203 -> 215 by TOOL-dFoldedAudit-4\|^FLOOR_ASSERTIONS=' tools/check-spec-tokens.test.sh`
  runs, it prints those three lines in that order, the last reading `FLOOR_ASSERTIONS=215`.
  figure: DERIVED, main's 203 plus this build's twelve at `8a5328a9`.
  Red when: either side's floor survives, or this build's line still reads `199 -> 211`.
- **AC6** — When `"$GOV_PYTHON" "$P/twoparent.py" "$(git merge-base HEAD^1 HEAD^2)" HEAD^1 HEAD^2 $SIX`
  runs, it prints exactly the thirteen lines of §4's probe P table.
  figure: PINNED at `8a5328a9`; a later tip re-derives the table by §4's rule.
  Red when: a line either side added is absent and is not one this design rewrites.
- **AC7** — When `"$GOV_PYTHON" "$P/pin.py"` runs from the worktree's root, it prints `37 39 True`.
  figure: PINNED, main's pin at `8a5328a9`; `37 38 True` at `951f44e4`.
  Red when: the pin is not 39, or no comment within 14 lines names `37 -> 39`.
- **AC8** — When `"$GOV_PYTHON" tools/check-spec-tokens.py | grep -c '^spec-tokens: \(supersede\|ac-order\) join'`
  runs it prints 2, and the same run piped to `grep -c 'REFUSING.*SPEC_\(SUPERSEDE\|AC_ORDER\)_CUTOFF'`
  prints 0.
  permission: scratch-guard refuses a leg's exact argv to a role agent (`tools/hooks/scratch-guard.js:1373-1379`).
  Where it refuses this one, the main loop observes it at the close.
  Red when: `main()` reads one key only, so the other join raises before its line prints.
- **AC9** — When `"$GOV_PYTHON" tools/drift-audit/drift_report.py --check 2>"$P/drift.err"` runs,
  `grep -c cutoff_keys_armed "$P/drift.err"` prints 0, and its stdout row for `cutoff_keys_armed` reads
  38 with `ok (pin 39, drain it)`.
  permission: this is the `drift-audit records` leg's argv, and AC8's note applies.
  fixture: the base ref is the shared `refs/remotes/origin/main`, the tip S1's fetch set.
  figure: PINNED, 38 armed in the union of both sides' confs, measured 2026-11-02.
  Red when: the pin stays 38 or 37, or its history lacks `37 -> 39`, so a `RATCHET WEAKENED` line prints.
- **AC10** — When `"$GOV_PYTHON" tools/codebase-map/gen_map.py --check` and
  `"$GOV_PYTHON" tools/memory-tree/gen_build_index.py --check` run, each exits 0.
  Red when: a generated file was hand-merged, or rendered before the sources it reads were resolved.
- **AC11** — When `"$GOV_PYTHON" tools/policy/policy.py mirror --check` runs on M it exits 1, and on F
  it exits 0.
  Red when: F leaves the mirror stale, or M already carries a render, which the guard refuses.
- **AC12** — When `grep -n '^last-audit:\|^last-body-change:' memory/guides/SESSION-KICKOFF.md` runs on F,
  the stamp ends in M's full sha and `last-body-change` reads `201eb127cec4700c6f247978ea5c07a178181f2f`.
  On M the stamp ends in `HEAD^1`'s full sha. Then `bash skills/session-kickoff/manifest-check.sh` exits 0 on F.
  permission: this is the `kickoff-manifest ratchet` leg's argv, and AC8's note applies.
  Red when: F still carries M's stamp, which the full leg reds with `fail 5`.
- **AC13** — When `git merge-tree --write-tree HEAD refs/remotes/origin/main` runs on F it exits 0,
  and `git rev-parse HEAD^1^2 refs/remotes/origin/main` prints one sha twice.
  figure: PINNED, before this unit it exits 1 and names the eight paths, measured at `951f44e4`.
  Red when: the run branch does not carry M and F, or the shared remote-tracking ref has moved off the
  tip M merged.

## 6. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `policy check` · `drift-audit records` · `drift-audit selftest` · `codebase-map coverage + freshness` · `memory hygiene` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms`

The guard join owes `memory-hygiene self-test`, `build-index selftest`, `policy fixtures`,
`drift-audit selftest` and the two recall legs. The last three on the line name `.memory-tree.conf` in
their guard, which the join reads as a root and does not owe. `spec-tokens self-test` sits under the broad
`tools/` guard, and the rest carry no guard and read these files. No arm is added or moved. The `spec-tokens self-test`
floor moves to 215, a figure counted by reading, and the main loop observes that suite at the close.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-02 · initial draft.
- rev-2 · 2026-11-02 · S1 · §4 · AC1 · the clone copies the run repository's `merge.rows.driver` and
  `merge.ours.driver` after `core.hooksPath`, since without them it conflicted on three `merge=ours`
  paths besides the eight; AC1's expected set stays the eight, and its red case names a missing driver.
- rev-2 · 2026-11-02 · S9 · §4 · `GOV_PYTHON` names the 3.15.2 interpreter that exists, replacing the
  absent uv path, cited as the first candidate the resolver reaches, with `python3` its passing fallback.
- rev-2 · 2026-11-02 · §3 · the CLOSED flip stated once, as the main loop's after the fast-forward,
  carried by neither M nor F; the build brief's contrary sentence is withdrawn by the re-dispatch note.
- rev-2 · 2026-11-02 · §4 · the conflict set re-read at `origin/main` `84acebdc`: none of the eight paths
  moved since `8a5328a9`, the floor, the pin and `last-body-change` hold, and the later-tip rule stays.
- rev-3 · 2026-11-02 · S1 · S10 · §3 · §4 · AC1 · AC6 · AC7 · AC9 · AC13 · the merge runs in the run
  worktree, since the branch guard (`.githooks/pre-commit:71-93`) refused M in the clone's primary tree.
  The clone, the driver copy and the fast-forward are gone, the probes and `drift.err` sit in `$P`
  outside the worktree, and `git merge --abort` before M is named as the unit's stop.
- rev-3 · 2026-11-02 · S7 · §4 · one §B line names the resolver floor, line 223 of the conflicted blob
  and `:219` on main, added by `1f7d1966` on `201eb127` and current, so the delta stays none; the record
  line is spelled as the kit spells it, with `<n>` derived.
- rev-3 · 2026-11-02 · §4 · S7 · main's `docs-undocumented.txt` addition to `PROJECT_REGISTRY_EXTRA` is
  noted as merging clean, outside the conflicted hunk and named by no §B line.
- rev-3 · 2026-11-02 · S8 · §4 · every file `gen_build_index.py --write` rewrites is named, each a
  render: `memory/LIVE.md`, the 2026-11 ledger, the dClosedLoop as-built view and dSafePassage's
  README generated block.
- rev-3 · 2026-11-02 · §4 · `:1405` re-cited as the stamp-sha rule it holds; the ISO-8601 form is cited
  at `:1442-1443` and the always-advances rule at `MANIFEST-TEMPLATE.md:30`.
- rev-3 · 2026-11-02 · S10 · §4 · both commits carry the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## 9. Reuse audit

The seam is a procedure, not code. The dSafePassage reconcile `37b3bf32`, with its follow-up re-stamp
`f25d719e`, is the precedent for the stamps and the additive conf. `TOOL-aSparedSpawn-32`'s §4 is the
precedent for the order inside the merge, the `Pass: none` merge commit and the two-parent check, which
probe P narrows to the six hand-resolved files. `reuse_lookup.py` ranked only name stems, `git`, `run`
and the row driver `merge` in `tools/memory-tree/merge-rows.py`, and none reconciles a branch. So no
existing code seam fits, and none is built. The handoff's reuse list names this build's earlier seams,
`verb_review`, the DISPOSAL stage, check 2's awk, `deviation_join.scan` and `derive_past_pin_ids`. None
sits on a merge's path.

Reuse probe used: `python tools/codebase-map/reuse_lookup.py "reconcile origin/main into a run branch by one git merge, resolving conflicts additively and re-rendering generated files"`.
Recall terms used: `python tools/memory-recall/query.py "how was origin/main reconciled into a run branch before landing, and how were conflicts on cutoff keys, floors, pins and generated files resolved" --terms "reconcile merge origin/main run branch conflict additively re-rendered never merged last-audit re-stamp FLOOR_ASSERTIONS cutoff_keys_armed policy mirror"`.
