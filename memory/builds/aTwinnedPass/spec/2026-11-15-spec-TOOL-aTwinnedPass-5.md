# TOOL-aTwinnedPass-5 — every arm of the build's three suites can go red on the regression it names

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-2 · base c40c39fb6 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aTwinnedPass-5-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aTwinnedPass-5-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-4-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-4-brief.md) | research | TOOL-aTwinnedPass-4 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-5-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-5-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-5-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-5-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-5-pass-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-5-pass-brief.md) | research | — |
| [2026-11-15-review-TOOL-aTwinnedPass-11-closing-diff-round3.md](../reviews/2026-11-15-review-TOOL-aTwinnedPass-11-closing-diff-round3.md) | diff-review | TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-11 |
| [2026-11-15-review-TOOL-aTwinnedPass-4-5-closing-diff-round2.md](../reviews/2026-11-15-review-TOOL-aTwinnedPass-4-5-closing-diff-round2.md) | diff-review | TOOL-aTwinnedPass-4 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's round 1 found arms in this build's three suites that cannot go red on the
regression they name: an absence needle the harness never emits (H3), two `remains` arms that are red
at the tip on git's own `+` worktree marker while the tool is right, and refusals, usage exits, a
staging loop, a stream and a skip side that no arm reaches (M2, M4, M5, M6, L2), plus one admission
arm with no control (L1). This unit corrects or adds each arm, so that each one is green on the
correct code and red under the staged break this spec names for it. The tools themselves do not
change.

## 2. Scope (IN)

- **S1** — H3. In `tools/workflows/unattended-build.test.sh`, T3's paragraph absence reads the
  needle `THIS PASS BUILDS IN A WORKTREE OF ITS OWN`, the paragraph's own opening, which T1 already
  reads as its positive control. It no longer reads `OWN WORKTREE`. Spec 1 is CLOSED and stays
  frozen (`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`, F1 (c)); this spec carries the corrected needle. Observed by AC1.
  **Readers:** by name: `tools/workflows/unattended-build.test.sh` alone spells the old needle, at the
  arm this item edits, and spec 1's frozen T3 bullet · by value: NO VALUE READERS, an absence needle
  is read only by its own arm.
- **S2** — The two `remains` arms of `tools/unattended/pass-tree.test.sh`, T2's for pass 4 and T5's
  for pass 7, compare `git rev-parse --verify -q refs/heads/<branch>` with that branch's tip,
  captured before the refused call. They no longer strip `git branch --list` output. Observed by AC2.
- **S3** — M4. Four refusals of `check_pass_tree_run` are armed in T3 of the pass-tree suite: a
  LANDED run, an ABORTED run, a run-state file naming no run branch, and no run-state file. Each case
  goes through `check_merge_refused` and one `check_has` on that refusal's own text. Observed by AC3.
- **S4** — M5. A new block, T6, in the pass-tree suite, with one helper `check_usage_refused` and
  five calls: `--merge` without `--from`, a second `--branch`, `--remove` carrying `--pass`, slug
  `../x`, and `--pass TOOL-other-2` under slug `tRun`. Each asserts exit 2, an unchanged `HEAD` and
  its own refusal text. Observed by AC4.
  **Readers:** by name: none, since this item adds arms and withdraws no name ·
  by value: NO VALUE READERS, the arms read the tool's exit and text and nothing reads their values.
- **S5** — M6. The fixture kit gains a second `[[generated]]` row, `fx-new.txt`, and `render.sh`
  gains two switches, `FX_RENDER_NEW` and `FX_RENDER_STRAY`. A new block, T7, merges a fresh pass
  with both switches set. It asserts that the merge commit carries `fx-new.txt` and not
  `fx-stray.txt`, that the NOTE names `fx-stray.txt`, and that the tree is left with that one
  untracked file. Observed by AC5.
- **S6** — L1. T1's `--check-commit` admission arm is kept, and a negative control is placed before
  it on the same fixture: a message whose subject names `TOOL-tRun-4` and which carries no `Pass:`
  trailer exits 1 with check 49's subject refusal. Observed by AC6.
- **S7** — M2 and L2, in region 4 of `tools/unattended/unattended.test.sh`. B1 captures stdout
  alone, with stderr in a scratch file under `$TMP/.git/`. It reads `dispatch declared` on stdout,
  reads the note on stderr, and misses the note on stdout. After B6, a new call dispatches
  `ARCH-tRun-4` with `--writes work/idx`, hits `dispatch declared` and misses the condition-1
  refusal. `FLOOR_ASSERTIONS` rises 3339 to 3342 and `FLOOR_SHARD_4` rises 420 to 423, each with a
  `RAISED` line. Observed by AC7.
- **S8** — Each suite's header comment and each block's comment name what the new arms stage and
  what they do not check, and the pass-tree suite's fixture description names the second row and
  the two switches. Observed by AC8.
- **S9** — `memory/map/generated/symbols.json` regenerated, carrying `check_usage_refused`.
  Observed by AC9.

## 3. Non-goals (OUT)

- Any change to `tools/unattended/pass-tree.sh`, `tools/unattended/unattended.sh`,
  `tools/unattended/lib-unattended.sh` or `tools/workflows/unattended-unit.js`. Each finding this unit
  closes is a coverage gap over correct code. A staged break is made by the main loop at the close
  and reverted, and it is never committed.
- H1, H2, M1 and M3: the pass identity's shapes and their arms are `TOOL-aTwinnedPass-4`'s.
- The left-shift gates the report proposes. None is built here (§4, "The left-shift asks").
- A floor for `tools/unattended/pass-tree.test.sh`, which has none at base. Its summary line counts
  what ran, and a block that cannot run exits 2 before the summary.
- The budget row `unattended pass-tree selftest` in `tools/run-gates/selftest-budgets.txt`. It is
  300 s for about 25 tool processes, and this unit adds about 12 (§4, "Cost"). (PINNED 2026-11-15)
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`, and every path
  of the live dDeclaredLoop run.
- Any self-test suite or bar run inside the pass. The arms are checked with `bash -n`, and the main
  loop observes each one red and then green at the close.
- A `help/` page. No page covers the pass-tree tool or `--dispatch` condition 1:
  `grep -rlF pass-tree help/` and `grep -rlF 'condition 1' help/` match nothing at `c40c39fb6`.

### Edges

- **consumes-from** `TOOL-aTwinnedPass-4` — its rewrite of both suites lands first. That covers the
  pass-tree fixture's branch and worktree spelling, which its `check_pass_branch` and
  `remove_pass_tree` confine to `worktree-agent-*` and `.claude/worktrees/agent-*`, a fixture
  whose pass worktrees `git status` does not list, and its T5 arms in the harness suite. Every
  `agent-p<n>` and `/wt/p<n>` literal in §4 is written in the tip's spelling and takes the spelling
  that unit leaves `add_fixture_pass` cutting. Without it, T6 and T7 run against a tool that refuses
  the fixture's own branches.
- **consumes-from** external — the closing review's round 1,
  `2026-11-15-review-TOOL-aTwinnedPass-1-2-3-closing-diff-round1`, items H3, M2, M4, M5, M6, L1 and
  L2. Their Fix and corrected-fix text is the starting design of §4, verified at `c40c39fb6`.
- **hands-off** external — the report's left-shift gates bound to these items, listed in §4 "The
  left-shift asks", for the main loop to file as asks at the build's close.

## 4. Design

### Evidence

The report pins `c40c39fb`. The build's tip `84f2320c4` changes only records past `c40c39fb6`
(`git diff --stat c40c39fb6 84f2320c4` lists eight files, all under `memory/builds/aTwinnedPass/`),
so every line below was read at the tip and holds at the base.

| Line | What sits there |
|---|---|
| `tools/workflows/unattended-build.test.sh@064bace0:278` | `hasnt_`: a case-sensitive `*"$3"*` match |
| `tools/workflows/unattended-build.test.sh@064bace0:1249` | `childU` and `childA`, the default unattended and attended runs, at `:1250` |
| `tools/workflows/unattended-build.test.sh@064bace0:1392` | T1's positive control, `has ... 'THIS PASS BUILDS IN A WORKTREE OF ITS OWN'` |
| `tools/workflows/unattended-build.test.sh@064bace0:1417` | T3's `hasnt_ ... 'OWN WORKTREE'`, inside `for m in childU childA` |
| `tools/workflows/unattended-unit.js@1094ea03:337` | the paragraph, emitted only when `cfg.passBase` is defined; its text opens at `:339` |
| `tools/workflows/unattended-unit.js@1094ea03:419` | the log line, `own worktree from`, lower case |
| `tools/unattended/pass-tree.test.sh@e00f17f5:48` | `run_tool`: stdout in `out`, stderr in `err` and `$T/err`, exit in `rc` |
| `tools/unattended/pass-tree.test.sh@e00f17f5:96` | the fixture kit's one `[[generated]]` row, `fx-out.txt`; `render.sh` at `:106` to `:123`, `FX_RENDER_FAIL` at `:111` |
| `tools/unattended/pass-tree.test.sh@e00f17f5:131` | `RUN.md`: `phase: BUILDING`, `run-branch: refs/heads/run`, dispatch rows for units 2, 3, 4 and 7 |
| `tools/unattended/pass-tree.test.sh@e00f17f5:173` | T1 writes the merge's message to `$T/msg`; `:174` and `:175` are the admission arm |
| `tools/unattended/pass-tree.test.sh@e00f17f5:187` | T2's `git branch --list agent-p4 \| tr -d ' *'` |
| `tools/unattended/pass-tree.test.sh@e00f17f5:195` | `check_merge_refused`, four assertions, run from a directory |
| `tools/unattended/pass-tree.test.sh@e00f17f5:226` | T3's last arm |
| `tools/unattended/pass-tree.test.sh@e00f17f5:252` | T5's `git branch --list agent-p7 \| tr -d ' *'` |
| `tools/unattended/pass-tree.test.sh@e00f17f5:256` | T5's last arm; the summary at `:258` |
| `tools/unattended/pass-tree.sh@def02e16:76` | `check_pass_tree_run`: no file at `:80`, LANDED or ABORTED at `:85`, rc 2 at `:90` |
| `tools/unattended/pass-tree.sh@def02e16:164` | `cmd_merge_tree` calls the run check before the clean-tree refusal at `:165` |
| `tools/unattended/pass-tree.sh@def02e16:224` | the staging of new untracked files after the regeneration; `check_generated_output` at `:230`, the NOTE at `:232` |
| `tools/unattended/pass-tree.sh@def02e16:270` | `main`'s usage exits, `:270` to `:289`; the slug refusal at `:292`; the unit-of-build refusal at `:296` |
| `tools/unattended/unattended.sh@dba68e98:1840` | `read_recorded_phase`, the `phase` fact as written |
| `tools/unattended/unattended.sh@dba68e98:8954` | `resolve_holder_worktree`: `run-branch`, else `branch-ref`, else rc 2 |
| `tools/unattended/unattended.sh@dba68e98:14311` | `check_commit_message` returns 0 for any `Pass: none`; the subject refusal for a trailerless message naming an open pass is at `:14319` |
| `tools/unattended/unattended.sh@dba68e98:14781` | condition 1's note, `>&2` |
| `tools/unattended/unattended.sh@dba68e98:14906` | `for p in $_c1_own; do` |
| `tools/unattended/unattended.sh@dba68e98:14965` | `echo "unattended: dispatch declared — ..."`, on stdout |
| `tools/unattended/unattended.test.sh@c188e38f:250` | `TMP`, the fixture work tree; scratch files sit under `$TMP/.git/` (the tally note at `:670`) |
| `tools/unattended/unattended.test.sh@c188e38f:687` | `run`, which is `run_main_at_head run_driver "$@" 2>&1` |
| `tools/unattended/unattended.test.sh@c188e38f:699` | `build_specced_tree`: specs for `ARCH-tRun-1` to `-4`, none with an `order` verb |
| `tools/unattended/unattended.test.sh@c188e38f:9530` | the TOOL-aTwinnedPass-3 block, B1 at `:9539` to `:9541`, B6 at `:9551` to `:9553`, the conf restored at `:9554` |
| `tools/unattended/unattended.test.sh@c188e38f:19652` | `FLOOR_ASSERTIONS=3339`; `FLOOR_SHARD_4=420` at `:19872` |

The `remains` arms are red at the tip, as the brief says. Probed on 2026-11-15 with git 2.54.0 in a
scratch repository: for a branch that a linked worktree has checked out, `git branch --list agent-p4`
prints `+ agent-p4`, and `tr -d ' *'` leaves `+agent-p4`. `git rev-parse --verify -q
refs/heads/agent-p4` prints the tip and exits 0.

### H3 — the T3 needle

`:1417` becomes the following line.

```
  hasnt_ "TP1 T3 $m has no worktree paragraph" "${!m}" 'THIS PASS BUILDS IN A WORKTREE OF ITS OWN'
```

The needle is the opening that T1 asserts present on the passBase fixture, so the absence and the
presence read one string. Its count of executed assertions does not move.

Spec 1 is CLOSED and is not edited (F1 (c)): `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` keeps a CLOSED spec frozen, so its T3
bullet keeps the old needle and this spec, with its arm, is the record of the corrected one.

F1 asks whether this edit also owes a deviation record.

Staged break: in `tools/workflows/unattended-unit.js`, the paragraph's condition at `:337` becomes
`false`. The shipped paragraph is then emitted on every call, `undefined` standing where the sha would
be, and both T3 runs of the arm go red.

### The two `remains` arms

T2 captures pass 4's tip directly after `write_fixture_pass 4`, and T5 captures pass 7's tip directly
after `write_fixture_pass 7`:

```
P4=$(git rev-parse agent-p4)
...
check_same "T2 branch agent-p4 remains at its tip (AC2)" "$(git rev-parse --verify -q refs/heads/agent-p4)" "$P4"
...
P7=$(git rev-parse agent-p7)
...
check_same "T5 branch agent-p7 remains at its tip (AC5)" "$(git rev-parse --verify -q refs/heads/agent-p7)" "$P7"
```

The labels keep spec 2's AC tags, because those are the criteria they re-observe. Each arm asserts
that the branch exists and that it still points at the commit the pass made, not merely that a name
is listed. Each stays one assertion.

Staged breaks:

- T2: in `cmd_merge_tree`'s not-disjoint branch at `tools/unattended/pass-tree.sh@def02e16:208`, call `remove_pass_tree`
  before the refusal. The branch is then deleted on refusal, and the arm reads the empty string.
- T5: in `cmd_remove_tree` at `tools/unattended/pass-tree.sh@def02e16:258`, the lost-commit test becomes `false`. Pass 7's
  branch is then deleted.

### M4 — the run check's other refusals

The block goes in T3, after its last arm at `:226`. The run-state file is edited in the work tree
only, and restored after each case.

```
# M4: the run check's other refusals. The run check precedes the clean-tree refusal, so each edit
# below leaves the tree dirty on purpose; only the text arm tells the run's refusal from that one.
for ph in LANDED ABORTED; do
  sed -i "s/^phase: BUILDING\$/phase: $ph/" "$RUNMD"
  check_merge_refused "for a run recorded $ph" "$R" agent-p4 "$C"
  check_has "T3 the $ph refusal names the phase" "$err" "the run of tRun is $ph, so it takes no pass back"
  git checkout -q -- "$RUNMD"
done
sed -i '/^run-branch: /d' "$RUNMD"
check_merge_refused "for a run-state file naming no run branch" "$R" agent-p4 "$C"
check_has "T3 the no-run-branch refusal says so" "$err" "names no run branch (neither run-branch nor branch-ref)"
git checkout -q -- "$RUNMD"
mv "$RUNMD" "$T/runmd.away"
check_merge_refused "with no run-state file" "$R" agent-p4 "$C"
check_has "T3 the missing-file refusal names the file" "$err" "build tRun has no run-state file at $RUNMD"
mv "$T/runmd.away" "$RUNMD"
```

That makes 20 assertions: four cases, each with `check_merge_refused`'s four and one text arm.
`check_merge_refused` runs the tool from `$2` in a subshell and leaves `$err` read from `$T/err`, as
the existing T3 text arms already rely on.

The four generic assertions do not tell the run's refusal from the clean-tree refusal that follows
it at `:165`. Under each staged break below, exit 1, one REFUSING line and the unchanged `HEAD` and
status all stay green, because the dirty `RUN.md` is refused next. The text arm is the one that goes
red, and this is said in the block's comment.

Staged breaks, one at a time:

- `:85`'s `LANDED|ABORTED)` case is deleted. Both phase text arms go red.
- `:85` reads `LANDED)` alone. The ABORTED text arm goes red.
- The `2)` case at `:90` is folded into `*)`. The no-run-branch text arm goes red.
- The file test at `:79` is deleted. The read then finds no run branch, and the missing-file text arm
  goes red.

### M5 — the usage exits

T6 is a new block after T5's last arm. The helper is defined at the block's head:

```
# ---- T6: every exit-2 path of main, each before load_driver_conf, with HEAD as it was ----------------
check_usage_refused() { # label · stderr needle · tool argv... -> three assertions
  local l=$1 w=$2 h
  shift 2
  h=$(git rev-parse HEAD)
  run_tool "$@"
  check_same "T6 $l: exits 2" "$rc" 2
  check_same "T6 $l: HEAD is unchanged" "$(git rev-parse HEAD)" "$h"
  check_has "T6 $l: stderr names the refusal" "$err" "$w"
}
check_usage_refused "--merge without --from" "usage: pass-tree.sh" --merge tRun --pass TOOL-tRun-4 --branch agent-p4
check_usage_refused "a second --branch" "usage: pass-tree.sh" --merge tRun --pass TOOL-tRun-4 --branch agent-p4 --branch agent-p4 --from "$C"
check_usage_refused "--remove carrying --pass" "usage: pass-tree.sh" --remove tRun --branch agent-p4 --pass TOOL-tRun-4
check_usage_refused "slug ../x" "'../x' is not a build-folder name" --remove ../x --branch agent-p4
check_usage_refused "a unit of another build" "'TOOL-other-2' is not a unit id of build tRun" --merge tRun --pass TOOL-other-2 --branch agent-p4 --from "$C"
```

That makes 15 assertions. Pass 4's branch is the operand of all five because it holds a commit that
nothing else holds and does not merge cleanly. Under any break below, the call then reaches a verb
that refuses with exit 1 and loses nothing. Each of the five breaks turns that call's exit arm and
text arm red:

- the `--from` requirement at `:286` is deleted. The merge then refuses `--from ''`.
- the duplicate test at `:270` is deleted. The merge then refuses pass 4's conflict.
- the `--remove` test at `:287` is deleted. The removal then refuses pass 4's unique commit.
- `check_slug_shape` at `:291` returns 0. The run check then finds no file for `../x`.
- the `[ "$mid" != "$slug" ]` test at `:296` is deleted. The merge then refuses pass 4's conflict.

### M6 — a render that creates a file

The fixture kit's `kit.toml` heredoc gains a second row, with the same `write` and `check` as the
first. `regen.py` reads rows that share both as one item, so the render still runs once (its header,
`tools/run-gates/regen.py`, "Rows sharing one write and one check are ONE item"):

```
[[generated]]
path = "fx-new.txt"
generator = "render.sh"
write = ["bash", "{kit}/render.sh"]
check = ["bash", "{kit}/render.sh", "--check"]
stage = 1
```

`render.sh` gains two lines after its `FX_RENDER_FAIL` block. They write only in write mode, so
`--check` is unchanged:

```
[ -z "${FX_RENDER_NEW:-}" ] || [ "${1:-}" = --check ] || printf 'new\n' > fx-new.txt
[ -z "${FX_RENDER_STRAY:-}" ] || [ "${1:-}" = --check ] || printf 'stray\n' > fx-stray.txt
```

Neither switch is set by the base commit's render or by `write_fixture_pass`. So `fx-new.txt` is
never tracked, and no earlier block sees either file. T7 is a new block after T6:

```
# ---- T7: the regeneration creates a generated file and leaves a stray one; only the first is committed --
add_fixture_pass 11 && write_fixture_pass 11 p11.txt || { echo "FAIL pass 11"; exit 2; }
out=$(FX_RENDER_NEW=1 FX_RENDER_STRAY=1 bash "$TOOL" --merge tRun --pass TOOL-tRun-11 --branch agent-p11 --from "$C" 2>"$T/err"); rc=$?; err=$(<"$T/err")
check_same "T7 --merge whose regeneration creates fx-new.txt and leaves fx-stray.txt exits 0" "$rc" 0
check_same "T7 the merge commit carries fx-new.txt, a generated output the render created fresh" "$(git ls-tree --name-only "$out" -- fx-new.txt)" "fx-new.txt"
check_same "T7 the merge commit does not carry fx-stray.txt" "$(git ls-tree --name-only "$out" -- fx-stray.txt)" ""
check_has "T7 the NOTE names fx-stray.txt as left untracked" "$err" "no effective generated output covers them: fx-stray.txt"
check_same "T7 fx-stray.txt is the one path the tree's status lists" "$(git status --porcelain)" "?? fx-stray.txt"
rm -f fx-stray.txt
```

That makes 5 assertions. Pass 11 is cut and reset as passes 2 and 3 were, and it conflicts on
`fx-out.txt` and the README region as pass 3 did, which the tool resolves. The NOTE needle carries
the colon and the single leading space that `:232` prints before the first path. A path that git
lists before `fx-stray.txt`, such as an unignored pass worktree, therefore turns it red, and that is
a fixture fault this arm should name.

Staged breaks:

- `:230` reads `if false;`. `fx-new.txt` is left out of the commit, and the NOTE names it first.
  The second, fourth and fifth arms go red.
- `:230` reads `if true;`. `fx-stray.txt` is committed, and the third and fifth arms go red.
- The loop at `:229` to `:231` is deleted. Neither file is staged, and the second and fourth arms go
  red.

### L1 — the admission arm's negative control

The control goes before `:173`, while passes 2 and 3 are merged and units 4 and 7 have rows but no
pass commit:

```
printf 'build TOOL-tRun-4\n' > "$T/msg4"
cc=$(bash "$HERE/unattended.sh" --check-commit "$T/msg4" 2>&1); rc=$?
check_same "T1 --check-commit over a trailerless subject naming open pass 4 exits 1, so the hook grades in this tree" "$rc" 1
check_has "T1 ...with check 49's subject refusal" "$cc" "this commit's subject names TOOL-tRun-4, an open dispatched pass of tRun"
```

That makes 2 assertions. The arm at `:174` and `:175` stays as it is, so its exit 0 now sits beside
an exit 1 from the same hook, the same tree and the same `HEAD`. Spec 2's AC6 sentence on
`--check-commit` keeps an arm. F2 records the alternative, dropping the arm.

Staged break: `check_commit_message`'s binding loop at `tools/unattended/unattended.sh@dba68e98:14269` reads `for f in ;`, so
no run binds and every message is admitted. The control goes red on both arms.

### M2 and L2 — the driver suite

B1, at `:9539` to `:9541`, becomes:

```
out=$(run_main_at_head run_driver --dispatch tRun --pass ARCH-tRun-1 --writes work/idx --writes lane/one 2>"$TMP/.git/tp5-b1.err")
hit  "$out" "dispatch declared"
hit  "$(<"$TMP/.git/tp5-b1.err")" "for ARCH-tRun-1: work/idx"
miss "$out" "so condition 1 leaves them out of the sibling comparison"
```

That is one assertion more. `run` is this same call with `2>&1`. The scratch file sits under
`$TMP/.git/` because `$TMP` is the fixture work tree, and a file there would dirty it.

After B6's `miss` at `:9553` and before the conf is restored at `:9554`:

```
# M2: the own-side skip. ARCH-tRun-4's one path is an index under ARCH-tRun-3's directory claim
# `work`, so the call's own side is the only side that leaves it out.
out=$(run --dispatch tRun --pass ARCH-tRun-4 --writes work/idx)
hit  "$out" "dispatch declared"
miss "$out" "two passes claiming one file are not disjoint"
```

That is two assertions more. All four fixture specs carry no `order`, so `ARCH-tRun-4` dispatches in
the group that B1, B2 and B6 parked. The block's comment changes "Ten assertions" to "Thirteen" and
names both new arms with their staged breaks.

The floors:

```
# RAISED 3339 -> 3342 by TOOL-aTwinnedPass-5 on 2026-11-15: B1 read on stdout alone (+1) and the M2
# own-side arm after B6 (+2), every one unconditional, counted off the block's own lines; no suite
# ran, and their RED-first observation is the close's.
FLOOR_ASSERTIONS=3342
...
# RAISED 420 -> 423 by TOOL-aTwinnedPass-5 on 2026-11-15: the same 3 region-four assertions, see FLOOR_ASSERTIONS.
FLOOR_SHARD_4=423
```

Staged breaks:

- L2: `:14781` loses its `>&2`. The note goes to stdout, so B1's stdout `miss` and its stderr `hit`
  go red.
- M2: `:14906` reads `for p in "$@"; do`. `work/idx` is compared against `ARCH-tRun-3`'s `work` and
  refused, so the M2 `hit` and `miss` go red.

### Cost

Declared bounds, PINNED 2026-11-15 and not measured. The close's runs measure them.

- The pass-tree suite: 4 refused merges, 5 usage calls, 1 merge with its regeneration, 1
  `--check-commit` call and one pass cut. That adds at most 40 s on node a, against a budget row of (PINNED 2026-11-15)
  300 s. (PINNED 2026-11-15)
- Shard 4 of the driver suite: one driver call more, since B1's call is replaced and not added. That
  adds at most 10 s. (PINNED 2026-11-15)
- The harness suite: no new call.

### The left-shift asks

None of these is built here. Per M8, the main loop files each one as an ask at the close.

| Item | The report's left-shift gate |
|---|---|
| H3 | an absence-needle rule under `harness arms (fail branches armed or pinned)`: a `hasnt_` or `miss` needle must be text the suite's subject can emit |
| M2 | a two-sided skip rule under `unattended kit gate`: every condition with a skip carries an arm with the skipped path on each side |
| M4 | a refusal-site rule under `harness arms (fail branches armed or pinned)`: every `print_pass_tree_refusal` site is matched by an arm that greps its text |
| M5 | an exit-code rule under `harness arms (fail branches armed or pinned)`: every documented exit code of a kit tool is asserted by an arm |
| M6 | an extension of `unattended kit gate`: the pass-tree suite carries a render that creates an untracked file, both generated and not |
| L1 | a pairing rule under `harness arms (fail branches armed or pinned)`: an admission arm is paired with a negative control on the same fixture |
| L2 | a stream rule under `unattended kit gate`: a criterion naming a stream is observed by an arm that captures that stream alone |

The hostile-string class arm (H1, M3) and the sha-shape parity arm (M1) are `TOOL-aTwinnedPass-4`'s
to list.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `check_usage_refused` | function, `tools/unattended/pass-tree.test.sh` | `python tools/lexicon/lexicon.py --suggest check_usage_refused --as sh.function`: OK, leads with `check` |
| `P4`, `P7`, `ph`, `cc`, `l`, `w`, `h` | suite variables | no shell-variable cell: `.lexicon.conf` declares `sh.function` alone |
| `FX_RENDER_NEW`, `FX_RENDER_STRAY` | fixture `render.sh` switches, beside `FX_RENDER_FAIL` | no cell |
| `fx-new.txt`, `fx-stray.txt` | fixture files | no cell |

`grep -rn check_usage_refused tools/` matches nothing at `c40c39fb6`.

### Files touched (estimate)

- `tools/workflows/unattended-build.test.sh`
- `tools/unattended/pass-tree.test.sh`
- `tools/unattended/unattended.test.sh`
- `memory/map/generated/symbols.json`

### Rollout

Live. The change is suite arms and one spec line, so there is nothing to switch. The pass builds on
`TOOL-aTwinnedPass-4`'s commit. The pass commit carries
`memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-5-1-acceptance-ledger.md`, one
`**Evidences:** TOOL-aTwinnedPass-5` block, and names every arm's red then green as owed to the main
loop. The status flip to CLOSED is the pass's last change, and landing waits for the owner's ask.

At the close, the main loop stages each break of §7's `New arm:` lines in the subject, one at a time.
It runs the suite or shard that holds the arm, sees the arm red, reverts the break, and sees it green.
No break is committed.

### Alternatives rejected

- **`git branch --list --format='%(refname:short)'` for the `remains` arms.** It is immune to the
  marker, but it still asserts only that a name is listed. Comparing with the captured tip also
  catches a refusal that moved the branch.
- **Committing the `RUN.md` edits for M4, then resetting.** The generic four assertions still could
  not tell the refusals apart, since the tool would then reach pass 4's conflict, and the commit and
  reset add steps that can fail.
- **Arming M4 through `--remove`.** Both verbs call the one run check first. `check_merge_refused`
  already asserts the unchanged tree, and a second population would repeat it.
- **An M6 render that always writes `fx-new.txt`.** Every earlier merge would then carry the file,
  and T1 to T5 would change under it. The switch keeps them as they are, in the way `FX_RENDER_FAIL`
  already does.
- **Reusing pass 7 for T7.** That would tie T7 to whatever `TOOL-aTwinnedPass-4` leaves of pass 7
  after T5, so a pass of its own was chosen.
- **A second B1 call for the stdout read.** A second dispatch of `ARCH-tRun-1` would park or refuse
  another row and move B3's row arithmetic.

### What the design does not check

- Any regression other than the staged breaks named here. Each arm is shown red on its own break,
  and on no other.
- That the generic four assertions of an M4 case come from the run check. Only the text arm tells
  the refusals apart. A refusal whose text is reworded without its arm also turns the text arm red,
  which is intended.
- `--remove`'s own path through the run check. It shares `check_pass_tree_run` with `--merge`, and
  only `--merge` is armed.
- `regen.py`'s merging of the two fixture rows into one item. It is read from the tool's header, and
  T7 relies on it. Two items would run the render twice, which T7 cannot tell apart.
- That the NOTE goes to stderr. T7 reads `$err` alone, so the NOTE moving to stdout would also turn
  the fourth arm red, but nothing names the stream.
- The harness suite's other absence needles. Only T3's is corrected, and the absence-needle rule in
  "The left-shift asks" is what would find the rest.
- A Windows process holding pass 11's worktree open. As the suite's header already says, its
  removal fails and the NOTE names it.

## 5. Production-readiness checklist

- security — no product code, input or surface moves. The arms add coverage for the refusals that
  stop `--merge` writing into a finished run, and for the usage refusal that stops another build's
  unit id reaching a merge subject.
- perf / scale — §4 "Cost": at most 40 s more for the pass-tree suite and 10 s more for shard 4. (PINNED 2026-11-15)
- error / empty / loading states — M4 arms the missing file and the record naming no run branch,
  and M5 arms every exit-2 path.
- observability — each arm's label names its case, and each `FAIL` line carries the output.
- risks — the edges with `TOOL-aTwinnedPass-4`. If that unit's spelling of the fixture differs from
  the tip's, every literal in §4 follows it (§3 "Edges"). An unignored pass worktree reds T7, which
  is the fault that arm is meant to name.
- testing — AC1 to AC9, and the `New arm:` lines in §7.
- migration — N/A: no record shape or stored state moves.
- user docs — N/A: no `help/` page covers these tools (§3).

## 6. Acceptance criteria

The suites are named inside the command that reads them. The arms' red under the staged breaks of
§7 and their green are the main loop's to observe at the close.

- **AC1** — When `grep -cF "'OWN WORKTREE'" tools/workflows/unattended-build.test.sh` runs, it
  prints 0. When `grep -cF "'THIS PASS BUILDS IN A WORKTREE OF ITS OWN'" tools/workflows/unattended-build.test.sh`
  runs, it prints 2: T1's positive control and T3's absence. When
  `grep -cF 'THIS PASS BUILDS IN A WORKTREE OF ITS OWN' tools/workflows/unattended-unit.js` runs, it
  prints 1, so the needle is text the subject emits.
  Red when: T3 still searches for a string the harness never emits.
  permission: the arm's red under §4's staged break and its green are the main loop's.
- **AC2** — When `grep -cF "tr -d ' *'" tools/unattended/pass-tree.test.sh` runs, it prints 0, and
  `grep -c 'rev-parse --verify -q refs/heads/' tools/unattended/pass-tree.test.sh` prints at least
  2. In a scratch repository where a linked worktree holds branch `agent-p4`,
  `git branch --list agent-p4` prints `+ agent-p4`, and
  `git rev-parse --verify -q refs/heads/agent-p4` prints that branch's tip.
  Red when: either arm still reads the listing, which carries git's `+` marker for a branch a
  worktree holds.
  fixture: the scratch repository is built by hand, `git init`, one commit, and
  `git worktree add -b agent-p4`. The tree holds none.
  permission: as AC1.
- **AC3** — When `grep -cF -e 'so it takes no pass back' tools/unattended/pass-tree.test.sh` runs,
  it prints 1, and so does the same count for `names no run branch (neither run-branch nor branch-ref)`
  and for `has no run-state file at`. The four `check_merge_refused` calls they follow sit after
  T3's fork-point arm.
  Red when: a refusal of `check_pass_tree_run` has no arm reading its text.
  permission: as AC1; each text arm goes red under its staged break while the generic four stay
  green.
- **AC4** — When `grep -c '^check_usage_refused ' tools/unattended/pass-tree.test.sh` runs, it
  prints 5, and the same count for `^check_usage_refused()` prints 1.
  Red when: an exit-2 path of `main` has no arm asserting exit 2.
  permission: as AC1.
- **AC5** — When `grep -cF 'path = "fx-new.txt"' tools/unattended/pass-tree.test.sh` runs, it prints
  at least 1, and so does the same count for `FX_RENDER_NEW=1 FX_RENDER_STRAY=1` and for
  `no effective generated output covers them: fx-stray.txt`.
  Red when: no merge's regeneration creates an untracked file, so the staging loop's two branches
  never run.
  permission: as AC1.
- **AC6** — When `grep -cF 'subject names TOOL-tRun-4' tools/unattended/pass-tree.test.sh` runs, it
  prints 1, and that line sits before the arm reading the merge's message exits 0.
  Red when: the admission arm has no control showing that the hook can refuse in that tree.
  permission: as AC1.
- **AC7** — When `grep -c 'tp5-b1.err' tools/unattended/unattended.test.sh` runs, it prints 2, and
  the same count for `--pass ARCH-tRun-4 --writes work/idx)` prints 1.
  `grep -E '^FLOOR_(ASSERTIONS|SHARD_4)=' tools/unattended/unattended.test.sh` prints, after the
  shadowed 675 line, `FLOOR_ASSERTIONS=3342` and `FLOOR_SHARD_4=423`, each below a `RAISED` line
  naming `TOOL-aTwinnedPass-5`.
  Red when: B1 still reads the note through the merged stream, the own-side call is missing, or a
  floor is not raised by the 3 assertions.
  figure: 3342 and 423 are DERIVED from 3339 and 420 at `c40c39fb6`, counted off the changed lines.
  permission: as AC1.
- **AC8** — When `bash -n` runs over each of the three suite files, each exits 0. The comment of
  each new or changed block names its staged break. The pass-tree suite's fixture description, above
  its `set -u` line, names `fx-new.txt`, `FX_RENDER_NEW` and `FX_RENDER_STRAY`, as `grep -c` over
  that header shows.
  Red when: a suite does not parse, or the fixture description omits the second row or a switch.
- **AC9** — When `python tools/lexicon/lexicon.py --suggest check_usage_refused --as sh.function`
  runs, it prints a line opening `OK`, and `memory/map/generated/symbols.json` carries
  `"check_usage_refused"` after `python tools/codebase-map/gen_map.py --write`.
  Red when: a name the lexicon refuses lands, or the index is not regenerated.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 · `unattended-unit.js` with the paragraph's condition at `:337` made `false`, so `childU` and `childA` carry the paragraph and T3's absence reds on both · none
New arm: tools/unattended/pass-tree.test.sh · covers AC2 · the corrected T2 arm reds with `remove_pass_tree` called in the not-disjoint refusal, and the corrected T5 arm with `--remove`'s lost-commit test made `false`; both arms are red at the tip on the `+` marker and green after · none
New arm: tools/unattended/pass-tree.test.sh · covers AC3 · `check_pass_tree_run` with its LANDED/ABORTED case deleted, then reading `LANDED)` alone, then its rc-2 case folded into `*)`, then its file test deleted; each reds that case's text arm · none
New arm: tools/unattended/pass-tree.test.sh · covers AC4 · `main` with the `--from` requirement, the duplicate test, the `--remove` exclusion, `check_slug_shape` and the `$mid` test each removed in turn; each reds that call's exit and text arms · none
New arm: tools/unattended/pass-tree.test.sh · covers AC5 · the post-regeneration loop's `check_generated_output` replaced by `false`, then by `true`, then the loop deleted · none
New arm: tools/unattended/pass-tree.test.sh · covers AC6 · `check_commit_message`'s binding loop given an empty list, so no run binds and the trailerless subject is admitted · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · condition 1's note without `>&2`, which reds B1's stdout miss and stderr hit; and condition 1's loop reading `"$@"`, which refuses ARCH-tRun-4 · FLOOR_ASSERTIONS 3339 to 3342 and FLOOR_SHARD_4 420 to 423

The close's runs of the three suites re-observe every existing arm. No `fail` site moves, so
`tools/unattended/unarmed-branches.txt` is not touched. The pass-tree suite must print no `FAIL`
line, and that observation is the main loop's.

## 8. Open questions

- **F1 — Does spec 1's rev-3 edit also owe a deviation record?** HYGIENE's deviation records cover
  "a departure from the frozen design, or from a spec once its code has started". (a) No record.
  The design spec 1 states, that a call without passBase keeps the base prompt, is unchanged. Only
  T3's needle moves, and the code never emitted the old one. The rev-3 line in spec 1's §9 names the
  review and this unit. (b) A `deviation` record in this build's `build/` folder, with hand-off
  `spec-revised`, cause `review finding` and risk `editorial`, beside the rev-3 edit. (c) Leave
  spec 1 frozen at rev-2, and let this spec and its arm carry the corrected needle. That leaves the
  CLOSED spec naming a needle its arm no longer reads, against the brief's item 2. Recommendation:
  (a).
  RESOLVED (agent, 2026-11-15, delegated): (c). `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` ("a CLOSED spec stays frozen, and its correction is a new unit on
  top") outranks the recommendation, as `TOOL-aTwinnedPass-4` left spec 2 frozen; S1, §4 "H3" and AC1
  are written to (c).
- **F2 — L1: keep the admission arm with a negative control, or drop it?** (a) Keep it, and put the
  negative control of §4 "L1" before it, at 2 assertions more. Spec 2's AC6 sentence on
  `--check-commit` then keeps an arm, and that arm's exit 0 sits beside an exit 1 from the same
  hook in the same tree. (b) Drop it, at 1 assertion fewer. The `Pass: none` trailer arm at `:164`
  already carries the fact the admission follows from. Spec 2's AC6 then has no arm for its second
  sentence, and spec 2 is CLOSED. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the suites' own helpers, and the unit extends those. The probe
`python tools/codebase-map/reuse_lookup.py "suite arm asserts a refusal exits 1 with HEAD and status
unchanged, a fixture usage refusal exits 2"` ranked generic stems: `arm`, `fixture`, `refusal`,
`usage` and `build_fixture`. None of them is a pass-tree helper. The source read found the seams that
do fit. In the pass-tree suite they are `run_tool`, `measure_refusals`, `check_merge_refused`,
`add_fixture_pass`, `write_fixture_pass`, the `FX_RENDER_FAIL` switch and `check_same`, `check_has`
and `check_lacks`. In the driver suite they are `run`, `run_main_at_head`, `run_driver`,
`build_specced_tree`, `hit` and `miss`. M4 calls `check_merge_refused` as it stands. M5's
`check_usage_refused` is that helper's sibling for exit 2, which `check_merge_refused` cannot assert.
M6's switches follow `FX_RENDER_FAIL`. `gotchas.py --for-paths` over the three suites selected
`fixture-passes-by-finding-nothing`, which is H3 and L1 and is answered by T1's positive control and
L1's negative control. It also selected `staged-break-substitutes-a-synthetic-value`, answered by
H3's break, which emits the shipped paragraph and not a synthetic string. It selected
`agent-output-interpolated-into-an-instruction` too, which is `TOOL-aTwinnedPass-4`'s.

Recall terms used: `python tools/memory-recall/query.py "an absence arm whose needle the subject
never emits, and a refusal no arm reaches" --terms "absence needle hasnt_ vacuous arm refusal exit 2
usage staged break red first stderr stream worktree marker"`
