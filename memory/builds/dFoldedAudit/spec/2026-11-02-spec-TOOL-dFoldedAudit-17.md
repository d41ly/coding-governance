# TOOL-dFoldedAudit-17 — origin/main reconciled into the run branch: the eight conflicted paths merged additively

**Status:** INPROGRESS · rev-1 · 2026-11-02 · node d · Tier-1 · base 8a5328a9 · streams tooling · order 170

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-17-1-spec-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-17-1-spec-return.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-1-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-17-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-17-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The run branch takes `origin/main` by one `git merge`, and each of the eight paths both sides changed
keeps both sides' content. The close's `--prepare` then meets no conflict. The owner asked on
2026-11-02 for the merge to go by git.

## 2. Scope (IN)

- **S1** — The merge, in a scratch clone of the run branch under `%TEMP%`, whose `origin` is the run
  repository's GitHub remote and whose hooks are the tracked `.githooks/`. The clone fetches `origin` and
  runs `git merge --no-ff --no-commit origin/main`. A conflict on any path outside §4's table stops the
  unit before any resolution. Observed by AC1.
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
- **S8** — Generated files are re-rendered, never hand-merged. The merge commit carries the map and the
  build index as their writers render them. `.governance/policy.json` enters the merge commit as one
  parent's blob and is re-rendered in the follow-up commit. Observed by AC10 and AC11.
- **S9** — Every commit runs with `GOV_PYTHON` exported to the Python 3.15 interpreter §4 names, because
  main's resolver floor is 3.15. NOT OBSERVED by a criterion: it is a precondition of the two commits,
  and a hook that resolves no usable launcher refuses the commit (`.githooks/pre-commit:286-288`).
- **S10** — The run branch takes the clone's two commits by fast-forward, and its remote-tracking
  `origin/main` names the merged tip. Observed by AC13.

## 3. Non-goals (OUT)

- Any behaviour change on either side. A defect found in either side's code is reported, not fixed.
- `memory/DECISIONS.md`. The row `TOOL-dFoldedAudit-16` at `memory/DECISIONS.md:244` reads `36 -> 38`
  because it was written before this merge. Its substance, a raise of two for these two keys, holds,
  and the row is not rewritten.
- Re-deriving `SPEC_SUPERSEDE_CUTOFF` or arming `SPEC_FOLD_CUTOFF`. The first is the landing's, and the
  second is the close's.
- A kit version mint. The merge brings main's version markers and the lander mints at landing.
- This unit's status flip, its acceptance ledger and its pass commit. They are the main loop's, after
  the fast-forward.
- Running any suite or the bar inside the pass.
- The parked question of the two unattended suites, recorded in this build's `RUN.md`.

## 4. Design

Line numbers are this tree's at `951f44e4`, PINNED 2026-11-02, unless a line says otherwise. The trial
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

### S1 — the clone

A clone of the local repository names that repository as `origin`. There `origin/main` is local `main`,
`2a6f3975`, and not the GitHub tip the trial measured. So the clone takes the run repository's remote
URL before it fetches. A fresh clone also carries no `core.hooksPath`, and its commits would skip every
hook, so the clone sets it.

```bash
export GOV_PYTHON=C:/Users/d41ly/AppData/Roaming/uv/python/cpython-3.15.0b1-windows-x86_64-none/python.exe
REPO=C:/projects/coding-governance
RUNWT=$REPO/.claude/worktrees/gov-build-m4-spec-audit-694e7b
CL="$TEMP/dFoldedAudit-17-merge"
git clone --branch branch/gov-build-m4-spec-audit-694e7b "$REPO" "$CL" && cd "$CL"
git remote set-url origin "$(git -C "$REPO" remote get-url origin)"
git config core.hooksPath .githooks
git fetch origin
git merge --no-ff --no-commit origin/main
git diff --name-only --diff-filter=U
```

`--no-commit` holds the merge open, so the generated renders and the stamp land in the merge commit.
The builder records `git rev-parse origin/main`. Every figure below is PINNED at `8a5328a9`, and the
last subsection says what re-derives when the tip has moved.

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

The datetime is ISO-8601 with its offset and always advances (`:1405`). Each commit message carries a
`Manifest delta:` line. Main's watched changes are one conf key, the method guide's kit marker, the
inline resolver block in five scripts and four gate legs. No §B line names the resolver floor or those
legs, measured 2026-11-02, so the expected delta is none, and the builder re-reads §B to confirm it.
The stall check then counts 5 non-merge watched commits since `201eb127`, below its 10 (`:1633-1653`).

### S8 — generated files

Before the merge commit, `"$GOV_PYTHON" tools/codebase-map/gen_map.py --write` renders
`memory/map/generated/`, which settles `symbols.json` and the auto-merged `CARDS.md`. Then
`"$GOV_PYTHON" tools/memory-tree/gen_build_index.py --write` renders `memory/LIVE.md` and the build
indexes. Both are staged with the merge. The hooks need this: the codebase-map leg grades the work tree
whenever a `.py` file is staged (`.githooks/pre-commit:280-307`), and hygiene check 9 delegates to the
build index's `--check`.

`.governance/policy.json` is guarded. The policy guard admits a merge path whose staged blob is HEAD's
or `MERGE_HEAD`'s (`tools/policy/guard.py:90-96`), so the merge commit takes `git checkout --ours --
.governance/policy.json`. Either parent's blob is admitted, and the follow-up commit replaces it. The
mirror renders at HEAD and records the catalogue's blob (`tools/policy/policy.py:1382-1426`), and the
merged catalogue is a new blob, so it is stale until a commit holds the merge. The follow-up commit runs
`"$GOV_PYTHON" tools/policy/policy.py mirror --write`, which the guard admits as a render at HEAD.

### S10 — the commits and the fast-forward

| Commit | Subject | Carries |
|---|---|---|
| M | `merge: origin/main into branch/gov-build-m4-spec-audit-694e7b — dFoldedAudit reconciled before its landing` | the resolutions, the renders, the first stamp |
| F | `records(dFoldedAudit): the kickoff manifest re-stamped and the policy mirror re-rendered at the reconcile merge <M8>` | the second stamp, the mirror |

Both end with `Pass: none` and the run's trailer. `--check-commit` admits a `none` trailer
(`tools/unattended/unattended.sh:14087`), and the routed-commits leg does not grade a merge's content
(`tools/memory-tree/routed_commits.py:33-34`). M's body names each resolution in one line.

Then, in the run worktree:

```bash
git -C "$RUNWT" fetch "$CL" HEAD && git -C "$RUNWT" merge --ff-only FETCH_HEAD
git -C "$RUNWT" fetch origin
```

The second fetch moves the shared `refs/remotes/origin/main` only when the clone fetched a later tip.
The close's drift read then compares against the pin the merge took. A refused fast-forward means the
run branch moved since the clone, and the unit stops and reports.

### The probes

Probe P, `twoparent.py` under the clone's scratch, prints each line a side added that the result lacks:

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

Probe D, `pin.py` under the same scratch, reads the pin the way the ratchet does:

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

- **Taking one side of any hand-resolved file.** Each side's lines carry a landed unit's behaviour, and
  probe P is what shows none was lost.
- **Pin 38 with a `37 -> 38` line.** The merged tree arms 38 keys at the merge and 39 at the close, so
  the close would read over the pin.
- **The mirror re-rendered inside the merge commit.** During the merge HEAD is the branch tip, so the
  render is neither a parent's blob nor a render at the commit's own HEAD, and the guard refuses it.
- **One re-stamp only.** The full leg cannot see a stamp inside a merge commit, and the staged leg
  refuses a merge commit without one.

## 5. Acceptance criteria

Run in the clone, with `GOV_PYTHON` exported. `HEAD` is M unless a criterion says F or the run worktree.
Probes P and D are §4's.

```bash
EIGHT=".governance/policy.json .memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/features/spec-tokens.md memory/map/generated/symbols.json tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/drift-audit/drift_signals.py"
SIX=".memory-tree.conf memory/guides/SESSION-KICKOFF.md memory/map/features/spec-tokens.md tools/check-spec-tokens.py tools/check-spec-tokens.test.sh tools/drift-audit/drift_signals.py"
```

- **AC1** — When `git diff --name-only --diff-filter=U` runs right after the merge, it prints exactly the
  eight paths of `$EIGHT`.
  figure: PINNED, measured by `git merge-tree --write-tree` over `951f44e4` and `8a5328a9` on 2026-11-02.
  Red when: the fetched tip conflicts on a ninth path, which stops the unit before any resolution.
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
- **AC6** — When `"$GOV_PYTHON" twoparent.py "$(git merge-base HEAD^1 HEAD^2)" HEAD^1 HEAD^2 $SIX`
  runs, it prints exactly the thirteen lines of §4's probe P table.
  figure: PINNED at `8a5328a9`; a later tip re-derives the table by §4's rule.
  Red when: a line either side added is absent and is not one this design rewrites.
- **AC7** — When `"$GOV_PYTHON" pin.py` runs from the clone's root, it prints `37 39 True`.
  figure: PINNED, main's pin at `8a5328a9`; `37 38 True` at `951f44e4`.
  Red when: the pin is not 39, or no comment within 14 lines names `37 -> 39`.
- **AC8** — When `"$GOV_PYTHON" tools/check-spec-tokens.py | grep -c '^spec-tokens: \(supersede\|ac-order\) join'`
  runs it prints 2, and the same run piped to `grep -c 'REFUSING.*SPEC_\(SUPERSEDE\|AC_ORDER\)_CUTOFF'`
  prints 0.
  permission: scratch-guard refuses a leg's exact argv to a role agent (`tools/hooks/scratch-guard.js:1373-1379`).
  Where it refuses this one, the main loop observes it at the close.
  Red when: `main()` reads one key only, so the other join raises before its line prints.
- **AC9** — When `"$GOV_PYTHON" tools/drift-audit/drift_report.py --check 2>drift.err` runs, `grep -c cutoff_keys_armed drift.err`
  prints 0, and its stdout row for `cutoff_keys_armed` reads 38 with `ok (pin 39, drain it)`.
  permission: this is the `drift-audit records` leg's argv, and AC8's note applies.
  fixture: the base ref is the clone's `refs/remotes/origin/main`, the tip the clone fetched.
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
- **AC13** — When `git merge-tree --write-tree HEAD refs/remotes/origin/main` runs in the run worktree
  after the fast-forward it exits 0, and `git rev-parse HEAD^1^2 refs/remotes/origin/main` prints one sha
  twice.
  figure: PINNED, before this unit it exits 1 and names the eight paths, measured at `951f44e4`.
  Red when: the run branch did not take M and F, or its remote-tracking ref lags the merged tip.

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
