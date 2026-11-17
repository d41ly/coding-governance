# TOOL-aTrimmedWait-18 — the reconcile with local main at 8eda4a5a0: its five conflicts resolved and the coincident floor summed, so the landing merge is clean

**Status:** SPECCED · rev-1 · 2026-11-17 · node a · Tier-2 · base 8eda4a5a0 · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-17-prompt-TOOL-aTrimmedWait-18-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-aTrimmedWait-18-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-aTrimmedWait-18-brief.md](../prompts/2026-11-17-prompt-TOOL-aTrimmedWait-18-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge local main at `8eda4a5a0` into `branch/speedups-9c2e63` and resolve its five conflicts, so the
landing merge of the branch onto local main is conflict-free
(`prompts/2026-11-17-prompt-TOOL-aTrimmedWait-18-1-spec-writer.md`). Both sides' changes stay as each
shipped them. Two places need more than a conflict hunk. The driver suite's total floor reads 3377 on
both sides, so git keeps it silently and the sum is lost. The pre-commit hook's check 9 render still
resolves python the old way, which main retired for one memoized resolution per hook run.

## 2. Scope (IN)

- **S1** — The merge. `git merge --no-ff --no-commit 8eda4a5a0` on the branch, committed once with
  both parents and no conflict marker. The five conflicted files resolve by S2 to S6, and
  `.githooks/pre-commit` takes S7's edit. Every other file keeps git's own merge result, apart from
  the generated outputs S9 re-renders. Observed by AC1 and AC9.
- **S2** — `memory/project/readme-contract.txt` keeps every row: main's `aPiecewiseGrade` and
  `aHastenedSweep`, then this branch's `aTrimmedWait`. Observed by AC2.
- **S3** — `memory/guides/SESSION-KICKOFF.md`. §B is re-read against both sides' watched changes.
  The conflict resolves to this branch's block with `last-audit` at a fresh datetime and the
  pre-merge tip, and `last-body-change` at that same tip, by the stamp rule. One follow-up records
  commit after the merge re-stamps both at the merge itself (§4, "The kickoff manifest").
  Observed by AC3 and AC10.
- **S4** — `tools/memory-tree/gen_build_index.py`, `main()`: main's `_COVERAGE_MEMO = None` stays the
  last line of the `--with-verdicts` `finally`, and this branch's two-line `--write-staged` dispatch
  follows it at its own indent, unchanged. Observed by AC4.
- **S5** — `tools/memory-tree/check-memory-hygiene.test.sh`: main's three raise comments, then this
  branch's four comment lines and its `MERGED` comment, then one new `MERGED` comment, then
  `FLOOR_ASSERTIONS=784`. Observed by AC5.
- **S6** — `tools/unattended/unattended.test.sh`: main's raise comment, then this branch's comment
  block, then one new `MERGED` comment, then `FLOOR_ASSERTIONS=3406` in place of the 3377 git kept.
  Every `FLOOR_SHARD_<n>` keeps this branch's figure, since main raised none. Observed by AC6.
- **S7** — `.githooks/pre-commit`, the check 9 render: the `hy_r` resolver line and its three-term
  launcher test become one call to main's `resolve_hook_python`, so the merged hook keeps main's
  one python resolution per hook run. Observed by AC8.
- **S8** — The auto-merged places where one side reads the other's old behaviour. S6's lost sum and
  S7's resolver are the two found. The rest were checked and need no edit, and
  `tools/workflows/unattended-build.test.sh`'s floor was checked against its two inputs
  (§4, "Where one side reads the other"). Observed by AC6, AC7 and AC8.
- **S9** — The generated outputs are regenerated after the resolution and committed in the merge.
  Observed by AC9.
- **S10** — The landing merge of the branch onto `8eda4a5a0` reports no conflict. Observed by AC10.

## 3. Non-goals (OUT)

- No landing and no push. The main loop makes the landing merge after the bar, and the owner asked
  for no push.
- No kit version bump by hand. `push-main.sh` mints them at the push boundary.
- No behaviour change on either side beyond a conflict, the lost sum and the resolver contradiction.
  S7 moves no verdict of the hook: every path that refused still refuses, and every path that
  rendered still renders.
- No edit to the hook's comments. TOOL-aTrimmedWait-3's comment and main's header both stay true
  after S7.
- No new suite arm, and no arm of either side edited or moved.
- No `FLOOR_SHARD_<n>` raised for main's arms. Main raised none, and a floor below its count reds
  nothing.
- No repair of the driver suite's inherited reds, filed as TOOL-aTrimmedWait-14 to -17.
- No edit to a CLOSED spec, ledger or review record on either side.
- No self-test suite and no bar inside the pass, a sliced suite included.
- No conflict resolved outside the five files. A sixth conflict stops the pass (§4, Rollout).

### Edges

- **consumes-from** external — local main at `8eda4a5a0`, carrying aHastenedSweep's and
  aPiecewiseGrade's landings, and this branch's CLOSED units 1 to 13. This unit reads their specs and
  edits none.
- **hands-off** external — the landing merge onto local main, the merge bar and the suites'
  self-tests at the close, all the main loop's; and the driver suite's inherited reds, filed in
  this build's backlog as TOOL-aTrimmedWait-14 to -17.

## 4. Design

### Evidence

Read on 2026-11-17. "The trial merge" is `git merge --no-ff --no-commit 8eda4a5a0` in a scratch
clone of the branch at `073bfbf68`, with this repository's `merge.rows` and `merge.ours` drivers set.
It named the brief's five conflicted files and auto-merged the rest. Its merge base is `5d48501da`,
TOOL-aTrimmedWait-12's reconcile point.

- The floors, read with `git show` at `5d48501da`, `8eda4a5a0` and the branch tip. In
  `tools/unattended/unattended.test.sh`, `FLOOR_ASSERTIONS` is 3348, 3377 and 3377. Main's one
  comment is TOOL-aPiecewiseGrade-6's `RAISED 3348 -> 3377`, and this branch's last is
  TOOL-aTrimmedWait-13's `RAISED 3374 -> 3377`. The conflict hunk holds only the two comment blocks,
  and git kept one `FLOOR_ASSERTIONS=3377` line below it.
- In that suite every `FLOOR_SHARD_<n>` reads the same at `5d48501da` and `8eda4a5a0`, so main's raise
  to each shard is 0. The tip reads 737, 229, 469, 431, 297, 127, 311 and 646, and the trial kept
  those lines.
- In `tools/memory-tree/check-memory-hygiene.test.sh`, `FLOOR_ASSERTIONS` is 708, 742 and 750. Main's
  34 are TOOL-aHastenedSweep-4's 2, -6's 9 and -7's pin of 23 to the printed count. The pin closes a
  gap both sides inherited from `5d48501da`, so the sum still counts every arm once.
- In `tools/workflows/unattended-build.test.sh`, `FLOOR_ASSERTIONS` is 1043, 1043 and 1051. Main
  added only a resolver block there, so the merged 1051 is already its sum.
- `gen_build_index.py`'s one hunk is the end of `main()`. Main's `_COVERAGE_MEMO = None` closes the
  `--with-verdicts` `finally` (`tools/memory-tree/gen_build_index.py@d96b671c6ca0:9328`), and this
  branch's `if mode == "--write-staged":` sits at the `try` body's indent
  (`tools/memory-tree/gen_build_index.py@7a471064ff37:9666`). `main()` declares
  `global _COVERAGE_MEMO` (`@d96b671c6ca0:9213`).
- Main's hook takes one staged read, `st_list` (`.githooks/pre-commit@f1da447298a0:195`), and one
  memoized resolver, `resolve_hook_python` (`:211`). Its header says "ONE staged read and ONE python
  resolution per hook run" (`:186`). Main moved the policy guard, the red-fix join and the map leg
  onto it (`:244`, `:276`, `:336`). This branch's check 9 render resolves python inline,
  `hy_r=$(git ls-files -- '*resolve-python.sh' | head -n 1)` and `. "./$hy_r" && py=$(resolve_python)`
  (`.githooks/pre-commit@2da7244afea4:238`, `:241`). The trial hook carries both forms.
- No line outside `.githooks/pre-commit` spells `hy_r` or the TOOL-aTrimmedWait-3 render comment, by
  `git grep` over the trial tree.
- Main's watched commits since `5d48501da`, by `git rev-list --no-merges HEAD..8eda4a5a0` over the
  `watch:` paths: TOOL-aMeasuredDrag-7's recall cache budget in `.memory-tree.conf`, -11's and -12's
  resolver memo in `tools/run-gates/run-gates.sh`, `run-selftests.sh`, `check-template-size.sh` and
  `manifest-check.sh`, TOOL-aHastenedSweep-1, -3, -4 and -6 in the hygiene script, and the version
  mint `d4888c6a4`. §B names no budget, resolver or hygiene internals, so the delta is none. Main's
  own `e5758fbac` and `8eda4a5a0` recorded the same delta for its side. This branch's watched changes
  were re-read at `f77c5589d` and `1c19bfc5a`.
- `manifest-check.sh` check 9 counts non-merge watched commits from `last-body-change` to `HEAD`
  (`skills/session-kickoff/manifest-check.sh@4d3d63c0fad1:1963`) and reds at 10. Over the trial's
  history, this branch's `c83653a26` counts 10 and main's `a46ef3919` counts 10, while the pre-merge <!-- PINNED 2026-11-17 -->
  tip `073bfbf68` counts 8. Both sides set `last-body-change` to their stamp's sha at each §B re-read
  (`f77c5589d`, `e5758fbac`).
- Check 5 finds its stamp commit with `git log -G'^last-audit:'` (`:1852`), which under git 2.54 lists
  no merge: `git log --merges -G'^last-audit:' HEAD` printed nothing, though `01aad1747` moved the
  stamp. Both sides changed `tools/memory-tree/check-memory-hygiene.sh` since `5d48501da`, so the merge
  is TREESAME to neither parent there, and `git rev-list -1` over the watch paths (`:1844`) named the
  trial's merge commit itself. TOOL-aTrimmedWait-12's follow-up `1c19bfc5a` is the precedent.
- No `RUN.md` exists under `memory/builds/aTrimmedWait/`, so this is an attended pass.

### The resolutions

Each conflict hunk resolves to the text below. Main's side goes first wherever both sides' lines
stay. A `MERGED` comment follows every comment line of both sides and sits directly above the value.

- `memory/project/readme-contract.txt`: `memory/builds/aPiecewiseGrade/README.md`,
  `memory/builds/aHastenedSweep/README.md`, then `memory/builds/aTrimmedWait/README.md`, below the
  `aMeasuredDrag` row git merged on its own.
- `memory/guides/SESSION-KICKOFF.md`: this branch's five block lines, with
  `last-audit: <ISO-8601 now, offset +02:00> @ <git rev-parse HEAD>` and
  `last-body-change: <git rev-parse HEAD>`. The datetime is later than main's
  `2026-11-17T01:27:47+02:00`, and `HEAD` is the pre-merge tip. The `watch:` and `verify-paths:`
  lines read the same on both sides.
- `tools/memory-tree/gen_build_index.py`: main's line, then this branch's two:

```text
                _COVERAGE_MEMO = None
        if mode == "--write-staged":
            return cmd_write(root, conf, staged=True)
```

- `tools/memory-tree/check-memory-hygiene.test.sh`: main's three `RAISED` comments from 708 to 742,
  this branch's `RAISED 707 -> 745`, `RAISED 745 -> 749` and TOOL-aTrimmedWait-12's `MERGED` comment,
  then:

```text
# MERGED at TOOL-aTrimmedWait-18's reconcile of local main at 8eda4a5a0: this branch's 750,
# plus main's 34 since 5d48501da (TOOL-aHastenedSweep-4's 2, -6's 9 and -7's pin of 23) = 784.
# Counted by reading; OWED: observed at the close.
FLOOR_ASSERTIONS=784
```

- `tools/unattended/unattended.test.sh`: main's `RAISED 3348 -> 3377` comment, this branch's block
  from `RAISED 3329 -> 3347` to `RAISED 3374 -> 3377`, then the comment below. The
  `FLOOR_ASSERTIONS=3377` line under the hunk becomes `FLOOR_ASSERTIONS=3406`.

```text
# MERGED at TOOL-aTrimmedWait-18's reconcile of local main at 8eda4a5a0: this branch's 3377,
# plus main's 29 since 5d48501da (TOOL-aPiecewiseGrade-6) = 3406. Main raised no FLOOR_SHARD_<n>
# since 5d48501da, so each keeps this branch's figure.
FLOOR_ASSERTIONS=3406
```

- `.githooks/pre-commit`, in the check 9 render's `if [ "$hy_rc" != 0 ]` branch: the `hy_r=` line goes,
  and the condition's third term becomes `resolve_hook_python`. The branch then reads:

```bash
    if [ "$hy_rc" != 0 ]; then
      if [[ $'\n'$hy_out == *$'\n''HYGIENE check 9 FAILED'* ]] \
          && gb=$(resolve_kit_gate memory-tree gen_build_index.py) \
          && resolve_hook_python \
          && with_hook_index "$py" "$gb" --write-staged; then
```

On 2026-11-17 all six resolutions were applied to the trial merge's files. `bash -n` passed on the
three shell files, `py_compile` on the generator, and the probe below printed every line §6 names.
The trial was committed in the scratch clone: its `git show --remerge-diff --name-only` named exactly
the six files, `git merge-tree --write-tree 8eda4a5a0 HEAD` exited 0, and check 9's count from the
pre-merge tip read 8.

### Where one side reads the other

- **The coincident floor.** Both sides' driver suites read `FLOOR_ASSERTIONS=3377`, so git merges the
  line clean and the merged floor counts only one side's raise. S6 restores the sum.
- **The hook's second resolver.** This branch's render resolves python inline, the form main replaced
  at every other leg. The merged hook would resolve twice in a run that reaches both the policy guard
  and the render, against main's header. S7 routes the render through `resolve_hook_python`. Its
  outcomes are the old ones: no tracked resolver or no usable launcher returns 1 and the branch
  refuses, and a resolved launcher sets `py`, which `--write-staged` reads.
- **Main's one staged read and this branch's render.** `st_list` is read before any leg, and the render
  stages paths after it. Only the wiring, template and map legs read a flag after the memory leg, and
  their triggers are `.unattended.conf`, the unattended Skill or its template, the charter template,
  and `*.py` or `*.js`. `plan()` over this tree at `073bfbf68` renders 3254 artifacts, every one a <!-- PINNED 2026-11-17 -->
  `.md` under `memory/`, and the `DESIGN_VIEW` is one too, so no render path can trip a later
  trigger. Checked, no edit.
- **Main's coverage memo and the staged write.** The memo is a dict only inside `--with-verdicts`, and
  `--write-staged` never sets it, so `read_carries_coverage` reads through under the staged render.
  Main's `by_slug` grouping in `collect` filters the same `tracked` list by the same prefixes, for
  any caller. Checked, no edit.
- **Main's hand-down and the scoped hygiene run.** `_IXH` is set only when `ONLY` is empty
  (`tools/memory-tree/check-memory-hygiene.sh@82bbde86282f:1204`), and this branch's `--spec` and
  `--build` run only beside `--only`, which sets `ONLY`
  (`tools/memory-tree/check-memory-hygiene.sh@dfa8ff34a8dd:62`). A scoped run never hands down its
  narrowed index set. Checked, no edit.
- **Main's spec-token lock and this branch's driver work.** `check_dispatch_specs` reads no spec-token
  state, and the two refusals this branch lifted, `check_unit_spec` and `check_edge_shape`, run before
  `init_spec_token_check` in the trial `verb_dispatch`, so they take no lock. Main renamed the
  claim-push lock helpers, and no line of the trial tree outside `memory/` spells an old name. Checked,
  no edit.
- **Names this branch retired.** No line main added spells `STAGED_RENDER` or `extract_hs_lines`,
  outside this branch's own planted fixture line. Every inline resolver copy in the trial carries main's
  `GATE_RESOLVED_PY` memo. Checked, no edit.

### The probe

`$SCRATCH` is the run's scratch directory. The probe runs from the worktree root after the resolution
and before the commit. While the merge is in progress `HEAD` is the pre-merge tip and `MERGE_HEAD` is
`8eda4a5a0`. `bash "$SCRATCH/t18.sh" HEAD MERGE_HEAD` reads the resolved files:

```bash
set -u
O=$1; M=$2; D=${3:-.}; B=$(git merge-base "$O" "$M")
R='^[[:space:]]*(hit|miss|same|mutate|has|hasnt_|hasnt|n=\$\(\(n\+1\)\))[[:space:]]'
U=tools/unattended/unattended.test.sh; F=tools/workflows/unattended-build.test.sh; H=tools/memory-tree/check-memory-hygiene.test.sh
for p in $U $F; do
  b=$(git show "$B:$p" | grep -cE "$R"); m=$(git show "$M:$p" | grep -cE "$R")
  o=$(git show "$O:$p" | grep -cE "$R"); r=$(grep -cE "$R" "$D/$p")
  echo "counts ${p##*/} merged $r expect $((m + o - b))"
done
hc() { grep -o 'n=$((n+1))' | wc -l | tr -d ' '; }
echo "counts ${H##*/} merged $(hc < "$D/$H") expect $(( $(git show "$M:$H" | hc) + $(git show "$O:$H" | hc) - $(git show "$B:$H" | hc) ))"
fl() { grep -E "^$1=[0-9]+\$" | cut -d= -f2; }
for p in $U $F $H; do
  for k in $(grep -oE '^FLOOR_(ASSERTIONS|SHARD_[0-9]+)=[0-9]+$' "$D/$p" | cut -d= -f1); do
    b=$(git show "$B:$p" | fl $k); m=$(git show "$M:$p" | fl $k); o=$(git show "$O:$p" | fl $k); r=$(fl $k < "$D/$p")
    echo "floor ${p##*/} $k merged $r expect $((o + m - b)) (tip $o main $m base $b)"
  done
done
G=tools/memory-tree/gen_build_index.py
echo "main() $(sed -n '/^def main(/,/^if __name__/p' "$D/$G" | awk '/^                _COVERAGE_MEMO = None$/ { m = NR } /^        if mode == "--write-staged":$/ && m == NR - 1 { d = NR } /^            return cmd_write\(root, conf, staged=True\)$/ && d == NR - 1 { n++ } END { print (n == 1) ? "memo-then-dispatch" : "misplaced" }')"
K=.githooks/pre-commit
echo "hook resolver-sources $(grep -cF "git ls-files -- '*resolve-python.sh'" "$D/$K") resolve_hook_python $(grep -c 'resolve_hook_python' "$D/$K") hy_r $(grep -cw 'hy_r' "$D/$K")"
```

The `counts` lines compare each merged suite's assertion sites with main's plus this branch's less
the base's, so an arm the merge lost or doubled shows. Each `floor` line compares a merged floor with
the tip's figure plus main's raise since the base. `main()` names the order of the memo reset and the
dispatch. The `hook` line counts the resolver's source lines, the memoized resolver's spellings and
`hy_r`. On 2026-11-17 staged breaks turned each kind red over a copy passed as the third argument:
the driver floor left at 3377 read `merged 3377 expect 3406`, the hygiene floor left at 750 read
`merged 750 expect 784`, the dispatch moved above the memo reset read `misplaced`, and git's own hook
result read `hook resolver-sources 2 resolve_hook_python 4 hy_r 2`.

### The generated outputs

After the resolutions and `git add` of each file, run in order:

```bash
python tools/run-gates/regen.py --write
git add -A
python tools/memory-tree/gen_build_index.py --write
python tools/codebase-map/gen_map.py --write
git add -A
```

`memory/LIVE.md` and the ledger shards carry `merge=ours`, so they hold this branch's render until
the writes above. Before the commit, `git status --porcelain` shows no `??` line. An untracked path
stops the pass and is named.

### The kickoff manifest

The stamp rule is `sha = HEAD`, and each side advanced `last-body-change` to its stamp's sha at a §B
re-read. In the merge commit `HEAD` is the pre-merge tip, so both lines name it. That satisfies the
staged leg, which requires the merge's stamp to differ from `HEAD`'s. It also keeps check 9 green,
where either side's own value would count 10. Check 5 then reds on the merge as its newest watched <!-- PINNED 2026-11-17 -->
commit, because `-G` never lists a merge. The follow-up records commit re-stamps `last-audit` and
`last-body-change` at the merge's full sha, with a later datetime and the same delta line.

### What it does not check

- That each suite executes at least its new floor. 3406 and 784 are DERIVED sums, first observed
  when the suites run at the close on the main loop's frozen clone.
- That a raise counts its own arms. The sums take each side's declared raise. Main's driver suite
  gained 42 assertion sites since `5d48501da` against a raise of 29. A floor below its count reds <!-- PINNED 2026-11-17 -->
  nothing, and the count is the close's.
- That main's 29 sit in a region whose shard floor counts them. Main raised no shard floor, so each
  stays this branch's figure.
- That the merged assertion counts are right inside a block. The `counts` lines catch a lost or
  doubled line, not a wrong one.
- That the merged shell files keep the spawn-idiom rows of `memory/project/spawn-idiom-sites.txt`.
  Main changed only a test-file row, and the `shell hygiene (a fork spent on builtin work)` leg grades
  the merged sums at the close's bar.
- That S7's render path runs green end to end. The branch-guard suite's render arms re-observe it at
  the close.
- That every auto-merged hunk outside the six files is right. AC9 shows the commit kept git's result
  there, and the bar and any closing review read the whole merge.

### Inventory

No identifier is minted: no function, flag, conf key, check number or global. The `MERGED` comments
are prose, and S7 removes the shell variable `hy_r`.

### Files touched (estimate)

- `memory/guides/SESSION-KICKOFF.md`
- `memory/project/readme-contract.txt`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/unattended/unattended.test.sh`
- `.githooks/pre-commit`
- `memory/LIVE.md`
- `memory/ledger/2026-11.md`
- `memory/map/generated/symbols.json`
- `memory/builds/aTrimmedWait/README.md`
- `memory/builds/aTrimmedWait/build/2026-11-17-build-TOOL-aTrimmedWait-18-1-acceptance-ledger.md`

The merge commit also carries every file main changed. The list above is what this unit resolves,
regenerates or writes by hand. `memory/guides/SESSION-KICKOFF.md` is the manifest itself, re-stamped
in the merge and again in the follow-up.

### Rollout

One pass at order 13, in the branch's own worktree. The card must route to this unit with its spec
INPROGRESS before the pass, or the scratch-guard refuses the resolution.

1. `git rev-parse main` must print `8eda4a5a0028fdf15c540293fdf462a110532667`. If it prints anything
   else, stop and return the new sha.
2. `git merge --no-ff --no-commit 8eda4a5a0`. If `git diff --name-only --diff-filter=U` names any
   file outside the five, run `git merge --abort` and return naming it.
3. Resolve the five, make S7's edit, regenerate, run the probe and the checks of §6, and write the
   acceptance ledger.
4. Commit once with both parents. The body names the six resolutions and carries
   `manifest-audit: delta none · watch-commits-since-stamp: <n>`, `n` being
   `git rev-list --count HEAD..MERGE_HEAD -- <watch>` read before the commit. It ends with
   `Pass: TOOL-aTrimmedWait-18` and the commit trailer. No `--no-verify`: a hook refusal is
   returned, not bypassed.
5. One records commit re-stamps `last-audit` and `last-body-change` at the merge commit's full sha,
   with a later datetime and the same delta line, `n` counted from the merge's stamp to `HEAD`.
6. The status flip to CLOSED is the pass's last change, a status-only commit.

### Alternatives rejected

- **Keep git's `FLOOR_ASSERTIONS=3377`.** It counts one side's raise, so a stranded block of either
  side's arms up to 29 lines long passes the floor.
- **Leave the hook's inline resolver.** Main's header would then be false in the file it heads, and a
  run reaching both the policy guard and the render would resolve python twice.
- **Rewrite main's header to admit a second resolution.** It keeps the cost main removed and edits
  main's text to describe it.
- **Keep either side's `last-body-change`.** Each counts 10 watched commits over the merged history,
  and check 9 reds at 10.
- **Re-stamp only at the merge.** Check 5 never reads a merge as its stamp commit, so the full leg
  reds at the close, as TOOL-aTrimmedWait-12 found at `01aad1747`.

## 5. Production-readiness checklist

- security — No new write path, surface or grant. S7 sources the same tracked resolver as before.
- perf / scale — S7 saves one python resolution in a hook run that reaches both the policy guard and
  the render.
- error / empty / loading states — A moved main or a sixth conflict stops the pass before anything
  is committed (Rollout). A resolver that does not resolve refuses the render as before.
- observability — The commit bodies and the `MERGED` comments name every figure.
- risks — A floor sum wrong by a miscount reds its suite at the close. S7 is the one edit beyond a
  conflict hunk, and the branch-guard suite re-observes the render at the close.
- testing — The probe and the direct checks in the pass. The bar and the suites at the close, the
  main loop's.
- migration — None.
- user docs — None owed. No user-facing behaviour changes, and S8 found no doc to correct.

## 6. Acceptance criteria

Each `counts`, `floor`, `main()` and `hook` line comes from one run of
`bash "$SCRATCH/t18.sh" HEAD MERGE_HEAD`, after the resolution and before the commit.

- **AC1** — Before the commit, `git rev-parse MERGE_HEAD` prints
  `8eda4a5a0028fdf15c540293fdf462a110532667`, and both `git diff --name-only --diff-filter=U` and
  `git grep -n '^<<<<<<< '` print nothing. After it, the merge is `git rev-list --merges -n 1 HEAD`,
  and `git rev-list --parents -n 1` over it prints three ids: the merge, the pre-merge tip, then
  `8eda4a5a0028fdf15c540293fdf462a110532667`.
  Red when: the merge is squashed or fast-forwarded, or a marker or unmerged path survives.
  permission: the after-commit half is the main loop's, recorded with the close's observations,
  because the ledger is committed in the merge.
- **AC2** — When `grep -nE '^memory/builds/a(MeasuredDrag|LightenedLoop|TwinnedPass|PiecewiseGrade|HastenedSweep|TrimmedWait)/README[.]md$' memory/project/readme-contract.txt`
  runs, it prints six lines on consecutive line numbers in that order, and
  `python tools/memory-tree/gen_build_index.py --check-format` exits 0.
  Red when: a side's row is lost, doubled or out of order.
- **AC3** — When `git diff --cached -U0 -- memory/guides/SESSION-KICKOFF.md` runs it prints one
  `+last-audit:` line ending `@ ` and the full `git rev-parse HEAD`, with a datetime later than
  `2026-11-17T01:27:47+02:00`, and one `+last-body-change:` line naming that same sha. Its only other
  content lines are the two `-` lines they replace.
  Red when: either line keeps a side's value, names another sha, or the merge moves §B.
- **AC4** — When `python -m py_compile tools/memory-tree/gen_build_index.py` runs it exits 0, the probe
  prints `main() memo-then-dispatch`, and `grep -c '^        if mode == "--write-staged":$' tools/memory-tree/gen_build_index.py`
  prints 1.
  Red when: the memo reset leaves the `finally`, the dispatch moves into it or above it, or either is
  lost or doubled.
- **AC5** — When `grep -c '^FLOOR_ASSERTIONS=784$' tools/memory-tree/check-memory-hygiene.test.sh`
  runs it prints 1, and `grep -cE "^# MERGED at TOOL-aTrimmedWait-1[28]'s|RAISED 719 -> 742 by TOOL-aHastenedSweep-7|RAISED 745 -> 749 by TOOL-aTrimmedWait-11" tools/memory-tree/check-memory-hygiene.test.sh`
  prints 4. `bash -n tools/memory-tree/check-memory-hygiene.test.sh` exits 0. The probe prints a
  `counts check-memory-hygiene.test.sh` line and a `floor check-memory-hygiene.test.sh FLOOR_ASSERTIONS`
  line, each with its two numbers equal.
  Red when: a raise comment is lost, an arm line is lost or doubled, or the floor is not the sum.
  figure: 784 is DERIVED as 750 + (742 - 708), each read with `git show` at the pre-merge tip,
  `8eda4a5a0` and `5d48501da`.
- **AC6** — When `grep -c -e '^FLOOR_ASSERTIONS=3406$' -e '^FLOOR_SHARD_1=737$' -e '^FLOOR_SHARD_3=469$' -e '^FLOOR_SHARD_4=431$' tools/unattended/unattended.test.sh`
  runs it prints 4, and `grep -cE "^# MERGED at TOOL-aTrimmedWait-18's|RAISED 3348 -> 3377 by TOOL-aPiecewiseGrade-6|RAISED 3374 -> 3377 by TOOL-aTrimmedWait-13" tools/unattended/unattended.test.sh`
  prints 3. `bash -n tools/unattended/unattended.test.sh` exits 0. The probe prints a
  `counts unattended.test.sh` line with its two numbers equal, and nine `floor unattended.test.sh`
  lines, `FLOOR_ASSERTIONS` and `FLOOR_SHARD_1` to `FLOOR_SHARD_8`, each with its `merged` and
  `expect` numbers equal.
  Red when: the total keeps git's 3377, a raise comment is lost, a shard floor moves, or an arm line
  is lost or doubled.
  figure: each floor is DERIVED as tip + (main - base), read as AC5 reads its figure.
- **AC7** — When `grep -c '^FLOOR_ASSERTIONS=1051$' tools/workflows/unattended-build.test.sh` runs it
  prints 1, and the probe prints a `counts unattended-build.test.sh` line and a
  `floor unattended-build.test.sh FLOOR_ASSERTIONS` line, each with its two numbers equal.
  Red when: the merge loses or doubles an arm line, or the floor is not the sum.
  figure: 1051 is DERIVED as AC6's figures are.
- **AC8** — When `bash -n .githooks/pre-commit` runs it exits 0, and the probe prints
  `hook resolver-sources 1 resolve_hook_python 5 hy_r 0`.
  Red when: the render keeps its inline resolver, the memoized resolver loses a call site, or a
  second resolver definition appears.
  figure: 1 and 5 are PINNED, measured on the trial's resolution on 2026-11-17. The 5 are the
  definition and four call sites.
- **AC9** — Before the commit, `python tools/run-gates/regen.py --check` and
  `bash tools/unattended/adopt-unattended.sh --check` each exit 0. After it,
  `git show --remerge-diff --format= --name-only "$(git rev-list --merges -n 1 HEAD)" 2>/dev/null | sort -u`
  piped to `grep -vE '^(memory/|tools/memory-tree/(gen_build_index[.]py|check-memory-hygiene[.]test[.]sh)$|tools/unattended/unattended[.]test[.]sh$|[.]githooks/pre-commit$)'`
  prints nothing.
  Red when: a generated output still holds one side's render, or the merge changes a product file
  outside the six against git's own result.
  cost: about two minutes for the regeneration check.
  permission: the after-commit half is the main loop's, as in AC1.
- **AC10** — After the re-stamp commit, `bash skills/session-kickoff/manifest-check.sh` exits 0,
  `git merge-tree --write-tree 8eda4a5a0 HEAD` exits 0, and
  `git merge-base --is-ancestor 8eda4a5a0 HEAD` exits 0.
  Red when: the stamp does not follow the merge, `last-body-change` counts 10 or more watched commits,
  the landing merge would conflict, or `8eda4a5a0` is not in the branch's history.
  permission: the main loop's, as in AC1.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `build README slot contract` · `codebase-map coverage + freshness` · `unattended kit gate` · `tier2-review self-test` · `policy fixtures` · `recall floor` · `recall floor arms` · `memory-hygiene self-test` · `build-index selftest` · `branch-guard self-test` · `unattended-build self-test` · `python resolver (behaviour + inline parity + idiom ban)`

The first five grade this unit's resolutions directly. The next four are owed because a path of the
estimate trips their guard, by `python tools/check-spec-tokens.py --legs-for` at `073bfbf68`, less the
broad guards. The last five are the suites over the files this unit resolves or edits. Per the brief,
the main loop runs the bar once at the close without the self-test suites. Once on a frozen clone of
the branch after the re-stamp commit, it runs those five suites and the driver suite,
`tools/unattended/unattended.test.sh`. The driver suite's inherited reds, filed as
TOOL-aTrimmedWait-14 to -17, are not this unit's. No arm is added or moved, so there is no `New arm:`
line. Both sides' arms are each side's own, already observed red and then green by the units that
wrote them.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-17 · initial draft from `prompts/2026-11-17-prompt-TOOL-aTrimmedWait-18-1-spec-writer.md`,
  grounded at `073bfbf68` and `8eda4a5a0`. The six resolutions and the probe were run on a trial
  merge in a scratch clone, and the trial was committed there to read its remerge diff, its landing
  merge-tree and check 9's count.

## 10. Reuse audit

`resolve_hook_python` in `.githooks/pre-commit` is the seam S7 extends: main's memoized resolver, which
the render now calls instead of a copy of its body. The codebase map does not index the hook, so
`python tools/codebase-map/reuse_lookup.py "reconcile a branch with local main: sum suite assertion floors, keep a memo reset beside a dispatch, one python resolution per hook run"`
ranked generic stems only (`run`, `sum`, `main`, `resolve_python`), and `resolve_python` is the
function the seam wraps. No existing seam fits the rest, a merge resolution with one-off
observations. Of the task's named seams, `verb_dispatch`, `run_spec_token_check` and check 12's
`--only` are read for S8 and not changed. The `--check --staged` render decision and
`check_staged_write` are read for S8's staged-read finding. `plan_state`, `order_verb_of`,
`scan_consumes_cycles`, `derive_spec_token_key`, `scanCommandHeads`, `checkRoleGate` and
`load_session_calls` merged without a conflict and are untouched. `regen.py --write` is the
regeneration step, and the probe is TOOL-aTrimmedWait-12's, with a `floor` line added. The direct
precedents are TOOL-aTrimmedWait-12 for the `MERGED` lines and the follow-up re-stamp, and
TOOL-aTwinnedPass-13 before it.

Recall terms used: `python tools/memory-recall/query.py "how was a reconcile merge with local main resolved when both sides raised one suite floor to the same number" --terms "reconcile merge local main FLOOR_ASSERTIONS MERGED coincidence sum shard kickoff manifest re-stamp last-body-change"`
