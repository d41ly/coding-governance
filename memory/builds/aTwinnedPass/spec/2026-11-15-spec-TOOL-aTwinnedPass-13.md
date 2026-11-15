# TOOL-aTwinnedPass-13 — the reconcile with local main at a76c6afe7: its four conflicts resolved so the landing merge is clean

**Status:** INPROGRESS · rev-1 · 2026-11-15 · node a · Tier-2 · base a76c6afe7 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aTwinnedPass-13-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-13-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-13-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge local main at `a76c6afe7` into `branch/dazzling-jackson-b895c0` and resolve its four
conflicts, so the landing merge of the branch onto local main is conflict-free
(`prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-brief.md`). Both sides' changes stay as each
shipped them. The one design question is whether main's TOOL-aLightenedLoop-3, which moved the first
`--dispatch` to the main loop, agrees with this build's `passBase` branch. It does, and §4 says why.

## 2. Scope (IN)

- **S1** — The merge. `git merge --no-ff a76c6afe7` on the branch, committed with both parents and no
  conflict marker. The four conflicted files resolve by S2 to S5. Every other file keeps git's own
  merge result, apart from the generated outputs S7 re-renders. Observed by AC1 and AC8.
- **S2** — `memory/project/readme-contract.txt` keeps both rows, main's
  `memory/builds/aLightenedLoop/README.md` first, then `memory/builds/aTwinnedPass/README.md`.
  Observed by AC2.
- **S3** — `tools/workflows/unattended-unit.js`, the `DRIVER_STEPS` ternary. This branch's
  `cfg.passBase !== undefined` branch stays byte for byte. The remaining unattended branch takes
  main's TOOL-aLightenedLoop-3 text as main ships it, in the place main already gave it over the
  base's "Declare the write set ... before you write anything". Observed by AC3.
- **S4** — `tools/unattended/unattended.test.sh`: `FLOOR_ASSERTIONS` becomes 3348, below both sides'
  comment blocks and one `MERGED` line. `FLOOR_SHARD_3` stays at 451 and `FLOOR_SHARD_4` at 423, as
  git merged them, and each side's arms are shown to sit in the region its shard floor counts them
  in. Observed by AC4.
- **S5** — `tools/workflows/unattended-build.test.sh`: `FLOOR_ASSERTIONS` becomes 1043, below both
  sides' comment blocks and one `MERGED` line. Observed by AC5.
- **S6** — The checks the merge raises. Main's `declare` hand-out field and this build's `passBase`
  sentence agree, and no doc this build wrote says the builder makes the first declaration. The
  `verb_dispatch` window comment's claim that nothing in the window writes the tree still holds with
  `check_generated_output` inside the window. Both were checked at writing time, and no edit follows
  from either. Observed by AC6 and AC7.
- **S7** — The generated outputs are regenerated after the resolution and committed in the merge.
  Observed by AC8.
- **S8** — The landing merge of the branch onto `a76c6afe7` reports no conflict. Observed by AC9.

## 3. Non-goals (OUT)

- No landing and no push. The main loop makes the landing merge after the bar, and the owner asked
  for no push.
- No kit version bump by hand. `push-main.sh` mints them at the push boundary.
- No behaviour change on either side beyond what a conflict forces. No edit to
  `tools/workflows/unattended-build.js`, `tools/unattended/unattended.sh`,
  `tools/unattended/lib-unattended.sh` or any doc S6 reads.
- No change to `FLOOR_SHARD_3` or `FLOOR_SHARD_4`, and no comment added beside them. Git merged them
  without a conflict, and AC4 observes that they still count what they say.
- No new suite arm. No arm of either side is edited or moved.
- No edit to a CLOSED spec, ledger or review record on either side.
- Asks `TOOL-aTwinnedPass-6` to `-10` and `-12`.
- No self-test suite and no bar inside the pass, a sliced suite included.
- No conflict resolved outside the four files. A conflict elsewhere stops the pass (§4, Rollout).

### Edges

- **consumes-from** external — local main at `a76c6afe7`, aLightenedLoop's landing, and this
  branch's CLOSED units 1, 3, 4, 5 and 11 at `ea7a44792`. This unit reads their specs and edits none.
- **hands-off** external — the landing merge onto local main and the merge bar at the close, both
  the main loop's.

## 4. Design

### Evidence

Read on 2026-11-15. "The trial merge" is `git merge-tree --write-tree HEAD a76c6afe7` at
`ea7a44792`. It wrote tree `c3b73e286` and named the four conflicted files of the brief. Its merge
base is `aebbb4a72`, so main's side is aLightenedLoop's whole landing.

- The floors, read with `git show` at base, main and the branch tip. In
  `tools/unattended/unattended.test.sh`, `FLOOR_ASSERTIONS` is 3329, 3335 and 3342, `FLOOR_SHARD_3` <!-- PINNED 2026-11-15 -->
  is 445, 451 and 445, and `FLOOR_SHARD_4` is 410, 410 and 423. In <!-- PINNED 2026-11-15 -->
  `tools/workflows/unattended-build.test.sh`, `FLOOR_ASSERTIONS` is 950, 954 and 1039. The trial
  merge holds `FLOOR_SHARD_3=451` and `FLOOR_SHARD_4=423`.
- Each side's raise comments name its parts. Main's 6 are TOOL-aLightenedLoop-3's 5 and -8's 1, all
  in region three. This branch's 13 are TOOL-aTwinnedPass-3's 10 and -5's 3, all in region four.
  Main's 4 in the workflow suite are TOOL-aLightenedLoop-3's `LL3` sites. This branch's 89 there are <!-- PINNED 2026-11-15 -->
  TOOL-aTwinnedPass-1's 50, -4's 28 and -11's 11.
- In the trial merge's driver suite, the region ends are the `fi   # ---- end REGION` lines. Main's
  cache arms (`:7816-7931`) fall in region three and this branch's TP3 block (`:9570-9607`) in
  region four, so each shard floor still counts its own side's raise.
- `tools/workflows/unattended-unit.js@dcac7ab3c0c5:311-327` is the one conflict hunk. Its ours
  side is the `passBase` branch (`:312-319`) followed by the base's two lines (`:320-321`). Its
  theirs side is main's four lines (`:323-326`). The shared tail from "ITS SILENCE IS NOT A
  CLEARANCE" to the `--brief` sentence (`:328-334`) belongs to the last branch only, as at both sides.
- The workflow suite pins the last branch's text: `LL3 AC2` has "The main loop declared this unit's
  write set" in `$childU` and hasn't "Declare the write set with" there
  (`tools/workflows/unattended-build.test.sh@691adc9006cf:1293-1294`). `$childU` is built
  without `passBase` (`:1254`). `TP1 T1` hasn't `--dispatch tB` in the `passBase` prompt (`:1404`).
  The resolution keeps all three true.
- Main's `declare` field is `tools/workflows/unattended-build.js@10022946d155:3040-3049`, inside the
  `dispatch` hand-out and present only in unattended mode. This branch never changed that file or its
  template.
- `verb_dispatch`'s window runs from `init_spec_token_check "$slug"`
  (`tools/unattended/unattended.sh@a9ff4a9ce6f7:14965`) to `run_spec_token_check "$slug"`
  (`:15057`). Its comment (`:14959-14964`) says nothing in the window writes the tree. This branch's
  `_c1_own` and `_c1_gen` sort (`:14907-14911`) runs before the window opens. Inside it,
  condition 1's inner loop calls `check_generated_output` (`:15039`).
- `check_generated_output` calls only `covers`, and `covers` calls only `normpath`
  (`tools/unattended/lib-unattended.sh@eb8c9250a040:720-758`). All three work by parameter expansion
  and write no file.
- Of the four docs the brief names, only two places speak of who declares. The verbs guide's "Before
  dispatching a pass, DECLARE its write set" bullet is main's text unchanged
  (`tools/unattended/VERBS.template.md@c70b591ad682:797`). This branch's parallel sentence orders
  "`--dispatch` and `--brief` for each unit, one records commit, then one harness call per unit
  carrying that commit as `passBase`" (`:826-828`). `tools/unattended/README.md`'s `pass-tree.sh`
  paragraph and `help/pass-legs.md` say nothing about declaring. Outside the suites, the trial tree
  spells "Declare the write set with" only in the conflict hunk's base lines.
- In the trial merge, `memory/guides/UNATTENDED-VERBS.md` and `memory/guides/UNATTENDED-PROTOCOL.md`
  are the same blobs as their templates. The protocol render is 68130 bytes CR-stripped, which <!-- PINNED 2026-11-15 -->
  equals its row in `tools/template-size-limits.txt`.
- `git show --remerge-diff` lists only the files a merge commit changed against git's automatic
  result. Probed on `5ab0c2717`, TOOL-aLightenedLoop-8's merge, under git 2.54. It prints the
  `merge-rows:` driver's line on stderr.
- No `RUN.md` exists under `memory/builds/aTwinnedPass/`, so this is an attended pass:
  `--check-commit` has no open pass to grade, and `.githooks/commit-msg` runs its merge audit.

### Agreement: main's `declare` and the `passBase` sentence

They agree. Both say the main loop makes the first `--dispatch`, before the spawn. Main's `declare`
tells the main loop to run `--dispatch` before each unit's Workflow call. The `passBase` sentence
tells the child that the main loop already declared its write set and recorded its brief at the
records commit it reset to. For a parallel pass the main loop does both. It declares as `declare`
says and records the brief and the records commit as the verbs guide's parallel sentence says.

They differ on one point, and that difference is the design. The child without `passBase` may widen
its own write set with `--dispatch`. The `passBase` child may not, because it runs outside the run's
tree and must not write the run-state file, so only the main loop widens it. The two sentences sit
in different branches of one ternary, so no prompt carries both. No doc this build wrote contradicts
main's text, and no edit follows.

### Agreement: the window comment and `check_generated_output`

The claim holds. The window's only call of this branch's code is `check_generated_output`, and the
Evidence shows it writes nothing. The comment's "the rest reads strings" covers it. No edit follows.

### The resolutions

Each conflict hunk resolves to the text below. Nothing outside the hunks moves.

- `memory/project/readme-contract.txt`, at the hunk:

```text
memory/builds/aLightenedLoop/README.md
memory/builds/aTwinnedPass/README.md
```

- `tools/workflows/unattended-unit.js`: the ours side's eight `passBase` lines, then the theirs
  side's four lines. The ours side's two base lines, from "Declare the write set with" to "before you
  write anything ...", are dropped.
- `tools/unattended/unattended.test.sh`: the theirs side's comment lines, then the ours side's, then
  these three lines in place of both `FLOOR_ASSERTIONS` lines:

```text
# MERGED at TOOL-aTwinnedPass-13's reconcile of local main at a76c6afe7: the base 3329 at aebbb4a72, plus main's 6
# (TOOL-aLightenedLoop-3's 5 and -8's 1), plus this branch's 13 (TOOL-aTwinnedPass-3's 10 and -5's 3) = 3348.
FLOOR_ASSERTIONS=3348
```

- `tools/workflows/unattended-build.test.sh`: the theirs side's comment lines, then the ours side's,
  then:

```text
# MERGED at TOOL-aTwinnedPass-13's reconcile of local main at a76c6afe7: the base 950 at aebbb4a72, plus main's 4
# (TOOL-aLightenedLoop-3), plus this branch's 89 (TOOL-aTwinnedPass-1's 50, -4's 28 and -11's 11) = 1043.
FLOOR_ASSERTIONS=1043
```

Main's side goes first in every file, as the brief orders the readme rows. On 2026-11-15 all four
resolutions were applied to the trial merge's files in the scratch directory. `node --check` passed
on the unit harness, `bash -n` passed on both suites, and the probe below printed every line §6
names.

### The generated outputs

After the four resolutions and `git add` of each file, run in order:

```bash
python tools/run-gates/regen.py --write
git add -A
python tools/memory-tree/gen_build_index.py --write
python tools/codebase-map/gen_map.py --write
git add -A
```

`memory/LIVE.md` and `memory/ledger/2026-11.md` carry `merge=ours` and auto-merged, and
`memory/map/generated/symbols.json` auto-merged. The writes above re-render all three. Before the
commit, `git status --porcelain` shows no `??` line. An untracked path stops the pass and is named.

### The probe, `$SCRATCH/t13.sh`

`$SCRATCH` is the run's scratch directory. The probe runs from the worktree root after the
resolution, before the commit, as `bash "$SCRATCH/t13.sh" HEAD MERGE_HEAD`. While the merge is in
progress `HEAD` is the pre-merge tip and `MERGE_HEAD` is `a76c6afe7`.

```bash
set -u
O=$1; M=$2; D=${3:-.}; B=$(git merge-base "$O" "$M")
R='^[[:space:]]*(hit|miss|same|mutate|has|hasnt_|hasnt|n=\$\(\(n\+1\)\))[[:space:]]'
for p in tools/unattended/unattended.test.sh tools/workflows/unattended-build.test.sh; do
  b=$(git show "$B:$p" | grep -cE "$R"); m=$(git show "$M:$p" | grep -cE "$R")
  o=$(git show "$O:$p" | grep -cE "$R"); r=$(grep -cE "$R" "$D/$p")
  echo "counts ${p##*/} merged $r expect $((m + o - b))"
done
region() { awk -v pat="$1" -v label="$2" 'index($0, pat) && !f { print "region " r + 1 " " label; f = 1 } /^fi   # ---- end REGION/ { r++ }' "$D/tools/unattended/unattended.test.sh"; }
region '  miss "$o" "spec-token cache off"' main-LL8
region '# TOOL-aLightenedLoop-3 AC9:' main-LL3
region '# ---- TOOL-aTwinnedPass-3: CONDITION 1' ours-TP3
U=tools/workflows/unattended-unit.js
pb() { grep -A7 -xF '    : cfg.passBase !== undefined'; }
un() { grep -A3 -F "    : \"The main loop declared this unit's write set with"; }
cmp -s <(pb < "$D/$U") <(git show "$O:$U" | pb) && [ "$(pb < "$D/$U" | wc -l)" = 8 ] && echo "cut passBase same" || echo "cut passBase differs"
cmp -s <(un < "$D/$U") <(git show "$M:$U" | un) && [ "$(un < "$D/$U" | wc -l)" = 4 ] && echo "cut unattended same" || echo "cut unattended differs"
w=$(sed -n '/^normpath() {/,/^}/p;/^covers() {/,/^}/p;/^check_generated_output() {/,/^}/p' "$D/tools/unattended/lib-unattended.sh" \
  | grep -v '^[[:space:]]*#' | sed -e 's#>/dev/null##g' -e 's/->//g' \
  | grep -cE '>|(^|[^A-Za-z_])(git|mkdir|rm|touch|tee|cp|mv)([^A-Za-z_]|$)')
echo "window writes $w"
```

The `counts` lines compare the merged suite's assertion-call lines with main's plus this branch's
less the base's, so an arm the merge lost or doubled shows. The `region` lines name the region each
side's first marker falls in. The `cut` lines compare the two `DRIVER_STEPS` branches with the side
each came from. The `window` line counts redirections and writing commands in the three functions
the window reaches. On 2026-11-15, staged breaks turned each kind red: one TP3 `hit` deleted, the
LL8 `miss` moved below region three's end, the base's two lines kept, and `: > "$1.seen"` added to
`check_generated_output`.

### What it does not check

- That either suite executes at least its new floor. 3348 and 1043 are DERIVED sums. They are first
  observed when a suite runs, and this close runs the bar without the self-test suites.
- That the merged assertion counts are right inside a block. The `counts` line catches a lost or
  doubled line, not a wrong one.
- That the regions hold any arm other than the three markers.
- A write in the window outside `normpath`, `covers` and `check_generated_output`, such as one added
  to the open-pass reader. That is main's code and main's comment.
- That every auto-merged hunk outside the four files is right. AC8 shows the commit kept git's
  result there, and the bar and any closing review read the whole merge.
- Measured registries such as `memory/project/fork-ceilings.txt` and
  `memory/project/spawn-idiom-sites.txt`. Main changed neither, and the bar measures them over the
  merged tree.

### Inventory

No identifier is minted: no function, flag, conf key, check number or global. The two `MERGED`
comment lines are prose.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/unattended/unattended.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `memory/project/readme-contract.txt`
- `memory/map/generated/symbols.json`
- `memory/LIVE.md`
- `memory/ledger/2026-11.md`
- `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-13-1-acceptance-ledger.md`

The merge commit also carries every file main changed. The list above is what this unit resolves,
regenerates or writes by hand. The regen writes may touch other generated outputs, and AC8 bounds
which.

### Rollout

One pass at order 6, in the branch's own worktree. The card must route to this unit with its spec
INPROGRESS before the pass, or the scratch-guard refuses the resolution again.

1. `git rev-parse main` must print `a76c6afe7f70b384b7cce7d6bf56e6aed62a2f82`. If it prints anything
   else, stop and return the new sha.
2. `git merge --no-ff --no-commit a76c6afe7`. A conflict in any file outside the four stops the pass:
   `git merge --abort`, then return naming the file.
3. Resolve the four as above, regenerate, run the probe and the checks of §6, and write the
   acceptance ledger.
4. Commit once with both parents. The message names the four resolutions and ends with
   `Pass: TOOL-aTwinnedPass-13` and the commit trailer. No `--no-verify`. A hook refusal is returned,
   not bypassed.
5. The status flip to CLOSED is the pass's last change, a status-only commit.

### Alternatives rejected

- **Keep the base's "Declare the write set" sentence.** It orders the child to make the first
  declaration, which main moved to the main loop, and `LL3 AC2` reds.
- **Fold the `passBase` branch into main's sentence.** The `passBase` child must not run `--dispatch`
  at all, so one sentence cannot serve both, and `TP1 T1` reds.
- **Add `MERGED` lines to the two shard floors.** Git merged them cleanly and each carries its own
  side's raise line, so a third line restates them.
- **Check the landing merge in a scratch worktree with `add_scratch_worktree`.** `git merge-tree`
  answers the same question and writes no tree.

## 5. Production-readiness checklist

- security — No new write path, surface or grant.
- perf / scale — None. Text and floor values only.
- error / empty / loading states — A moved main or a fifth conflict stops the pass before anything is
  committed (Rollout).
- observability — The commit message and the two `MERGED` lines name every figure.
- risks — A floor sum wrong by a miscount reds the suite at its next run. The figures come from both
  sides' own comments and the `counts` line.
- testing — The probe and the direct checks for the pass. The bar, without the self-test suites, at
  the close.
- migration — None.
- user docs — None owed. No user-facing behaviour changes, and S6 found no doc to correct.

## 6. Acceptance criteria

Each `counts`, `region`, `cut` and `window` line below comes from one run of
`bash "$SCRATCH/t13.sh" HEAD MERGE_HEAD`, §4's probe, run after the resolution and before the
commit.

- **AC1** — Before the commit, `git rev-parse MERGE_HEAD` prints
  `a76c6afe7f70b384b7cce7d6bf56e6aed62a2f82`, and both `git diff --name-only --diff-filter=U` and
  `git grep -n '^<<<<<<< '` print nothing. After it, `git rev-list --parents -n 1 HEAD` prints three
  ids: the merge, the pre-merge tip, then `a76c6afe7f70b384b7cce7d6bf56e6aed62a2f82`.
  Red when: the merge is squashed or fast-forwarded, or a marker or unmerged path survives.
  permission: the after-commit half is the main loop's, recorded with the close's observations,
  because the ledger is committed in the merge.
- **AC2** — When `grep -nE '^memory/builds/a(LightenedLoop|TwinnedPass)/README[.]md$' memory/project/readme-contract.txt`
  runs, it prints two lines on consecutive line numbers, `aLightenedLoop` first.
  `python tools/memory-tree/gen_build_index.py --check-format` exits 0.
  Red when: a side's row is lost or doubled.
- **AC3** — When `node --check tools/workflows/unattended-unit.js` runs it exits 0. The probe prints
  `cut passBase same` and `cut unattended same`, and
  `grep -c 'Declare the write set with' tools/workflows/unattended-unit.js` prints 0.
  Red when: the `passBase` branch is edited, main's sentence is not taken whole, or the base's
  sentence survives.
- **AC4** — When `grep -c -e '^FLOOR_ASSERTIONS=3348$' -e '^FLOOR_SHARD_3=451$' -e '^FLOOR_SHARD_4=423$' tools/unattended/unattended.test.sh`
  runs it prints 3. `grep -c "^# MERGED at TOOL-aTwinnedPass-13's reconcile" tools/unattended/unattended.test.sh`
  prints 1. `grep -cE 'by TOOL-aLightenedLoop-8: one region-three|by TOOL-aTwinnedPass-5 on 2026-11-15: B1' tools/unattended/unattended.test.sh`
  prints 2. `bash -n tools/unattended/unattended.test.sh` exits 0. The probe prints a
  `counts unattended.test.sh` line whose two numbers are equal, then `region 3 main-LL8`,
  `region 3 main-LL3` and `region 4 ours-TP3`.
  Red when: a side's raise comment is dropped, the floor is not the sum, an arm line is lost or
  doubled, or a side's arms leave the region its shard floor counts.
  figure: 3348 is DERIVED as 3329 + (3335 - 3329) + (3342 - 3329), each read with `git show` at
  `aebbb4a72`, `a76c6afe7` and the pre-merge tip. The counts are DERIVED at observation.
- **AC5** — When `grep -c '^FLOOR_ASSERTIONS=1043$' tools/workflows/unattended-build.test.sh` runs
  it prints 1, and `grep -c "^# MERGED at TOOL-aTwinnedPass-13's reconcile" tools/workflows/unattended-build.test.sh`
  prints 1. `grep -cE 'RAISED 950 -> 954 by TOOL-aLightenedLoop-3|RAISED 1028 -> 1039 by TOOL-aTwinnedPass-11' tools/workflows/unattended-build.test.sh`
  prints 2. `bash -n tools/workflows/unattended-build.test.sh` exits 0. The probe prints a
  `counts unattended-build.test.sh` line whose two numbers are equal.
  Red when: a side's raise comment is dropped, the floor is not the sum, or an arm line is lost or
  doubled.
  figure: 1043 is DERIVED as 950 + (954 - 950) + (1039 - 950), read as AC4 reads its figure.
- **AC6** — When `git diff --quiet a76c6afe7 -- tools/workflows/unattended-build.js tools/workflows/unattended-build.template.js`
  runs it exits 0, so main's `declare` field is the merge's.
  `git grep -n 'Declare the write set with' -- tools help memory/guides skills ':!*.test.sh'`
  prints nothing.
  Red when: the merge moves main's `declare` text, or a doc or prompt still tells a child to make
  the first declaration.
- **AC7** — When the probe runs it prints `window writes 0`, and
  `grep -c 'NOTHING IN THE WINDOW WRITES THE TREE' tools/unattended/unattended.sh` prints 1.
  Red when: `normpath`, `covers` or `check_generated_output` gains a redirection or a writing command,
  or main's window comment is lost in the merge.
- **AC8** — Before the commit, `python tools/memory-tree/gen_build_index.py --check`,
  `python tools/codebase-map/gen_map.py --check` and `bash tools/unattended/adopt-unattended.sh --check`
  each exit 0. After it, `git show --remerge-diff --format= --name-only HEAD 2>/dev/null | sort -u`
  piped to
  `grep -vE '^(memory/project/readme-contract[.]txt|tools/workflows/unattended-unit[.]js|tools/(unattended/unattended|workflows/unattended-build)[.]test[.]sh|memory/(LIVE[.]md|ledger/|map/generated/|builds/[^/]+/(README[.]md|spec/|build/2026-11-15-build-TOOL-aTwinnedPass-13-)))'`
  prints nothing.
  Red when: a generated output still holds one side's render, or the commit changes a file outside
  the four, the generated outputs and the ledger against git's own merge result.
  cost: about two minutes for the two index checks.
  permission: the after-commit half is the main loop's, as in AC1.
- **AC9** — After the commit, `git merge-tree --write-tree a76c6afe7 HEAD` exits 0, and
  `git merge-base --is-ancestor a76c6afe7 HEAD` exits 0.
  Red when: the landing merge would conflict, or `a76c6afe7` is not in the branch's history.
  permission: the main loop's, as in AC1.

## 7. Gates

`unattended kit gate` · `unattended-build self-test` · `build README slot contract` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `review-join self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `recall floor` · `recall floor arms`

The first six grade this unit's resolutions directly. The last five are owed because a path of the
estimate trips their guard, by `python tools/check-spec-tokens.py --legs-for` at `ea7a44792`, less
the broad guards. Per the brief, the main loop runs the bar once at the close without the self-test
suites, so the four self-test legs above are named as tripped and not observed at this close. No arm
is added or moved, so there is no `New arm:` line. Both suites' arms are each side's own, already
observed red and then green by the units that wrote them.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft from `prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-brief.md`,
  grounded at `ea7a44792` and `a76c6afe7`. The four resolutions and the probe were run on the trial
  merge's files in the scratch directory.

## 10. Reuse audit

No existing seam fits a merge resolution. This unit writes no code, and the probe is a one-off
observation. `python tools/codebase-map/reuse_lookup.py "reconcile a branch with local main: sum suite floors and keep both sides of a prompt ternary"`
ranked generic name stems only (`branches`, `extract_prompt_marker`, `run_main`,
`check_down_floor`). Of the task's named seams, `regen.py --write` is the regeneration step used
here, which is also what `push-main.sh`'s `run_regen` calls. `covers` and `check_generated_output`
are read for item 3 and not changed. `resolve_generated_indexes`, `check_gen_region_only` and
`check_commit_message`'s generated exemption do not apply, because no conflicted file is a generated
output or a gen region. `add_scratch_worktree` (`tools/run-gates/lib-attribute.sh`) is rejected in
§4 for `git merge-tree`. The unit harness's `prebuild` and `passLegs` key shape are not touched. The
nearest records were TOOL-aSparedSpawn-34, a reconcile with local main before landing,
TOOL-aSmoothedDispatch-21, whose `MERGED` floor line this spec's two lines follow, and
PLAY-dOrderedCharter-83, which resolved each conflict by its kind. TOOL-aLightenedLoop-8 is the
direct precedent.

Recall terms used: `python tools/memory-recall/query.py "how was a reconcile merge with main resolved when both sides raised a suite floor" --terms "reconcile merge local main FLOOR_ASSERTIONS summed MERGED conflict readme-contract DRIVER_STEPS passBase declare"`
