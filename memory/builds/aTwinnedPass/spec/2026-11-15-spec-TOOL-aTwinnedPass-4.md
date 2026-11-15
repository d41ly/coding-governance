# TOOL-aTwinnedPass-4 — a pass's branch, worktree and fork sha cross every handoff only in the runtime's own spelling

**Status:** CLOSED · rev-2 · 2026-11-15 · node a · Tier-2 · base c40c39fb6 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aTwinnedPass-4-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aTwinnedPass-4-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-4-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-4-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-4-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-4-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-4-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-4-brief.md) | research | TOOL-aTwinnedPass-5 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-4-pass-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-4-pass-brief.md) | research | — |
| [2026-11-15-review-TOOL-aTwinnedPass-11-closing-diff-round3.md](../reviews/2026-11-15-review-TOOL-aTwinnedPass-11-closing-diff-round3.md) | diff-review | TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 TOOL-aTwinnedPass-5 TOOL-aTwinnedPass-11 |
| [2026-11-15-review-TOOL-aTwinnedPass-4-5-closing-diff-round2.md](../reviews/2026-11-15-review-TOOL-aTwinnedPass-4-5-closing-diff-round2.md) | diff-review | TOOL-aTwinnedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

A builder's returned `branch` and `worktree` are free text, and today they reach the main loop's
instruction and a `git worktree remove --force` held only to shapes wide enough to carry `$(id)`, a
`..` segment or another session's branch (closing review round 1, H1 and H2). This unit holds the
pass identity to the one spelling the runtime cuts, `worktree-agent-<id>` at
`<primary tree>/.claude/worktrees/agent-<id>`, at both ends of the handoff: the unit harness returns
`''` for anything else, and `pass-tree.sh` refuses a branch or a holder outside it. It also widens
`--from` to the 7 to 64 hex digits the harness already admits as `passBase` (M1), and adds the arms
that feed both ends the characters the shapes exist to block (M3).

## 2. Scope (IN)

- **S1** — `tools/workflows/unattended-unit.js`: `BRANCH_SHAPE` becomes `^worktree-agent-[A-Za-z0-9]+$`.
  A value failing it returns `''`, as today. Observed by AC1, AC2.
- **S2** — `tools/workflows/unattended-unit.js`: `TREE_SHAPE` admits only an absolute path, either
  separator, whose last three segments are `.claude`, `worktrees` and `agent-<id>`, every earlier
  segment drawn from `[A-Za-z0-9._ -]`, and no `..` segment anywhere (§4, "The two harness shapes").
  A value failing it returns `''`, and `nextAction` names the path unusable, as today. Observed by
  AC1, AC2.
- **S3** — `tools/workflows/unattended-build.test.sh`: the `TP1` fixture's worktree moves to the
  runtime's spelling, and a new `TP4` group feeds both shapes six hostile values each, plus three
  controls; `FLOOR_ASSERTIONS` is raised 1000 to 1028 with its RAISED line. Observed by AC2.
- **S4** — `tools/unattended/pass-tree.sh` `check_pass_branch`: after its existing checks, it refuses
  a name outside `^worktree-agent-[A-Za-z0-9]+$`. Observed by AC5.
- **S5** — `tools/unattended/pass-tree.sh`: a new check, `check_pass_holder`, refuses a branch some
  worktree holds unless that worktree is exactly `<primary tree>/.claude/worktrees/agent-<id>` for the
  branch's own `<id>`, and leaves the admitted path in `PT_WHERE`. Both verbs call it before they
  write anything. `remove_pass_tree` removes only `PT_WHERE`, still with `--force`, and no longer
  reads `derive_holder_where` itself. Observed by AC3, AC4, AC5, AC6.
  **Readers:** by name: `tools/unattended/pass-tree.sh` alone calls `remove_pass_tree`, and
  `derive_holder_where` keeps its driver callers, so no name is withdrawn · by value: NO VALUE READERS,
  the holder path lives only between the check and the removal in one verb call.
- **S6** — `tools/unattended/pass-tree.sh` `cmd_merge_tree`: `--from` admits `^[0-9a-f]{7,64}$`, and
  the one refusal splits in two, a shape refusal naming "7 to 64" and a refusal for a value that
  names no commit. Observed by AC7.
- **S7** — `tools/unattended/pass-tree.test.sh`: `add_fixture_pass` cuts branch `worktree-agent-p<n>`
  at `$R/.claude/worktrees/agent-p<n>`, with `.claude/worktrees/` in the fixture's `info/exclude`;
  every arm naming a pass branch, a pass worktree or `agent-none` is respelled to match, and the T3
  `--from` needle reads "7 to 64". A new `TP4` block adds the holder, name and `--from` arms of §4.
  Observed by AC3 to AC7.
- **S8** — The tool's header: section 4 says both verbs refuse a branch or a holder outside the
  runtime's spelling, and section 5 gains the lines of §4, "What the design does not check", that
  concern the tool. Observed by AC8.
- **S9** — `memory/map/generated/symbols.json` regenerated with `gen_map.py --write`, carrying
  `check_pass_holder`. Observed by AC8.

## 3. Non-goals (OUT)

- Editing `TOOL-aTwinnedPass-1`'s or `TOOL-aTwinnedPass-2`'s spec. Both are CLOSED, and a CLOSED spec
  stays frozen with its correction landing as a new unit on top
  (`memory/guides/BUILD-METHOD.md@28d18878:146`). The brief asks for spec 2's two lines naming 40 to
  be made true; this spec is that correction instead. It supersedes spec 2's S4 "7 to 40" and its §4
  `--merge` step 2, spec 2's §3 bullet saying the tool never spells the runtime's names or places,
  and spec 1's fixture value `/w/agent-x1`, which the new `TREE_SHAPE` refuses.
- The T3 absence needle, the own-side dispatch arm, the `check_pass_tree_run` refusals, the exit-2
  paths, the fresh-render arms, the `--check-commit` arm and the stream arm: `TOOL-aTwinnedPass-5`'s.
- The `+` marker that `git branch --list` prints before a branch another worktree holds, which keeps
  the two `remains` arms red at the tip. This unit respells those two lines with the fixture and
  leaves them red; `TOOL-aTwinnedPass-5` fixes how they read.
- `COMMIT_SHAPE` and `passBase` in the harness: already 7 to 64 digits
  (`tools/workflows/unattended-unit.js@1094ea03:178`).
- The raw `branch` and `worktree` on the harness's log line
  (`tools/workflows/unattended-unit.js@1094ea03:436`): the log is not the instruction channel, and its
  comment says it keeps raw values on purpose.
- A cross-check in the harness that the worktree's `<id>` equals the branch's. The destructive end,
  `check_pass_holder`, makes that check (F1).
- A conf key for the runtime's spelling: one runtime cuts these names today, and another runtime's
  passes are refused, which is the safe direction.
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`;
  `memory/builds/dDeclaredLoop/`; the build harness `unattended-build.js`; the unattended Skill's loop.
- The kit version, which the lander's `mint` moves; a page under `help/`, since none describes
  unattended passes (spec 2 §4, "Docs").
- The left-shift gates the review names, which this unit does not build (Edges).

### Edges

- **consumes-from** external — the closing review round 1,
  `2026-11-15-review-TOOL-aTwinnedPass-1-2-3-closing-diff-round1`: H1 (id 1), H2 (id 2), M1 (ids 5
  and 14) and M3 (id 8), whose Fix and corrected-fix text is this design's starting point.
- **hands-off** `TOOL-aTwinnedPass-5` — the respelled pass-tree suite fixture: every pass branch is
  cut in the `worktree-agent-*` spelling, at the primary tree's `.claude/worktrees/agent-*`, so
  every literal that unit writes takes that spelling. The two `remains` arms of T2 and T5 are
  respelled with the fixture and left red for its fix. Both units edit both suites, so it builds
  after this one.
- **hands-off** external — the left-shift gates for the main loop to file as asks (M8's disposition
  where a unit does not build the gate): the class-wide hostile-string arm over every agent-returned
  value reaching `nextAction` (H1, M3), since this unit arms only `branch` and `worktree`; and a parity
  arm that reads the sha shape, and the branch shape, from both ends of the harness-to-tool handoff
  (M1). H2's left-shift arm, an outside holder refused by `--remove`, is built here (S7).

## 4. Design

### Evidence

Read at base `c40c39fb6`. `git diff --stat c40c39fb6 84f2320c4` moves only records, so every blob
below is the same at the build's tip.

| Citation | What sits there |
|---|---|
| `tools/workflows/unattended-unit.js@1094ea03:178` | `COMMIT_SHAPE`, 7 to 64 lowercase hex, which grades `passBase` |
| `tools/workflows/unattended-unit.js@1094ea03:339` | the worktree paragraph asks for `branch` as `git branch --show-current` prints it and `worktree` as `git rev-parse --show-toplevel` prints it |
| `tools/workflows/unattended-unit.js@1094ea03:442` | `TREE_SHAPE`, refusing only CR, LF and backtick; `BRANCH_SHAPE` at `tools/workflows/unattended-unit.js@1094ea03:443` admits any branch name |
| `tools/workflows/unattended-unit.js@1094ea03:481` | `ownTree` is spliced into `nextAction` inside a code span; `ownBranch` reaches only the return |
| `tools/workflows/unattended-build.template.js@cc868b60:311` | the `..` segment test, `(^|[\\/])\.\.([\\/]|$)`, refusing one in `scratch` and `repo` |
| `tools/workflows/unattended-build.test.sh@064bace0:1388` | `TP_OK` returns `"worktree":"/w/agent-x1"`; its needles at `tools/workflows/unattended-build.test.sh@064bace0:1399` and `tools/workflows/unattended-build.test.sh@064bace0:1422` |
| `tools/workflows/unattended-build.test.sh@064bace0:1340` | `read_next_action` stops at the first `"`, so an escaped quote inside `nextAction` truncates what it returns |
| `tools/unattended/pass-tree.sh@def02e16:98` | `check_pass_branch`: a leading `-`, `check-ref-format`, the run's own branch |
| `tools/unattended/pass-tree.sh@def02e16:149` | `remove_pass_tree`: `derive_holder_where`, then `git worktree remove --force` on whatever it names, then `branch -D` |
| `tools/unattended/pass-tree.sh@def02e16:179` | `--from` against `^[0-9a-f]{7,40}$`, one refusal for shape and resolution at `tools/unattended/pass-tree.sh@def02e16:181` |
| `tools/unattended/pass-tree.sh@def02e16:249` | `cmd_remove_tree`: run, branch, existence, lost-commit count, then `remove_pass_tree` |
| `tools/unattended/unattended.sh@dba68e98:9304` | `derive_holder_where`: the path `git worktree list --porcelain` shows holding `HW_REF`, else a remedy sentence that is never a directory |
| `tools/unattended/pass-tree.test.sh@e00f17f5:50` | `add_fixture_pass` cuts `agent-p<n>` at `$T/wt/p<n>`, outside the fixture's primary tree |

Live, on node a, 2026-11-15: `git worktree list --porcelain` prints the primary tree first as
`worktree C:/projects/coding-governance`, and each runtime-cut pass as
`worktree C:/projects/coding-governance/.claude/worktrees/agent-a062c1d85fb878113` with
`branch refs/heads/worktree-agent-a062c1d85fb878113`. The runtime cuts every pass under the primary
tree, even for a session running in a linked worktree; spec 1 recorded the same as its R2. A SHA-1
repository answers `git rev-parse --verify -q` over 64 hex digits with exit 1.

### What the review says that the code does not

- **H1's "final segment".** The runtime's suffix is three segments, `.claude`, `worktrees` and
  `agent-<id>`; the brief's "last two" counts them short. The shape below matches all three.
- **H2's holder "under `.claude/worktrees/agent-`".** A prefix test admits a holder at another
  pass's place. The runtime names the worktree after the same `<id>` as the branch, so the tool
  compares the holder with the one path the branch implies (F1).
- **M3's T5 fixtures.** A hostile value placed after the agent id fails the new shapes on the id's
  own class, and so cannot tell a loosened character class from a strict one. Each hostile worktree
  below carries its payload in an earlier segment, where only the class or the `..` test refuses it.
- **M1's sha256 fixture.** The tool's `--from` check is a regex and then `rev-parse`; splitting the
  refusal lets a SHA-1 fixture observe that 64 digits pass the shape and fail only the lookup, which
  is the half this unit changes. A full sha256 fixture would rebuild the suite's whole repository
  for one arm (Alternatives rejected).
- **The suite's own fixture.** Every `pass-tree.test.sh` branch is `agent-p<n>` at `$T/wt/p<n>`, so
  S4 and S5 refuse every pass the suite merges. The fixture moves to the runtime's spelling, and
  each arm keeps the refusal it reached before: `run` still meets the own-branch refusal and `-x` the
  leading-dash refusal, because the new shape test runs after both.

### The two harness shapes

```js
const TREE_SHAPE = /^(?!.*(^|[\\/])\.\.([\\/]|$))(\/|[A-Za-z]:[\\/])([A-Za-z0-9._ -]+[\\/])*\.claude[\\/]worktrees[\\/]agent-[A-Za-z0-9]+$/
const BRANCH_SHAPE = /^worktree-agent-[A-Za-z0-9]+$/
```

The leading lookahead is `tools/workflows/unattended-build.template.js@cc868b60:311`'s `..` test,
copied: a workflow script is evaluated alone, and that template already copies its sibling's checks
the same way so both keep one answer. The segment class admits a space (F2) and no `$`, `(`, `)`,
`"`, `'`, `;`, `&`, `|`, `<`, `>`, backtick, CR, LF or `:` past the drive letter. The two call sites at
`tools/workflows/unattended-unit.js@1094ea03:444` and `:445` do not move. The comment above them
gains one sentence: the shapes are the runtime's own spelling, and `pass-tree.sh` refuses the same
branch shape at the other end. A probe of this regex over the twelve values of AC1 printed the
expected answer for each on node a, 2026-11-15.

### `check_pass_branch` and `check_pass_holder`

`check_pass_branch` keeps its three refusals in order, then refuses a name outside
`^worktree-agent-[A-Za-z0-9]+$`, before `PT_BRANCH` is set:

`pass-tree: REFUSING - '<name>' is not a branch the runtime cuts for a pass (worktree-agent-<id>), so it is not a pass's branch; nothing was written`

`check_pass_holder` runs on `PT_BRANCH`:

1. `PT_WHERE=""`. With `HW_REF` local and set to `refs/heads/$PT_BRANCH`, one line from
   `derive_holder_where`. A line that is not a directory means no worktree holds the branch: return 0.
2. The primary tree is the first `worktree ` line of `GIT worktree list --porcelain`, the same
   output `derive_holder_where` reads, so both paths carry one spelling. The wanted path is
   `<primary>/.claude/worktrees/${PT_BRANCH#worktree-}`.
3. A holder that is not that string exactly is refused, and the function returns 1:
   `pass-tree: REFUSING - <branch> is checked out at <holder>, not at <wanted>, where the runtime cuts that pass's worktree, so that tree is not a pass's and is left as it is; nothing was written`
4. Otherwise `PT_WHERE` is the holder.

An empty primary line fails the comparison and refuses, so an unreadable worktree list denies.

`cmd_merge_tree` calls `check_pass_holder` right after the branch-existence refusal, before the
commit count and `--from`, so a merge it refuses has written nothing. `cmd_remove_tree` calls it
after the existence note and before the lost-commit count. `remove_pass_tree` drops its own
`derive_holder_where` call and runs `GIT worktree remove --force "$PT_WHERE"` when `PT_WHERE` is set,
then `branch -D` as today. It can therefore remove only a path the check admitted. With `PT_WHERE`
empty while some worktree still holds the branch, `branch -D` fails and the existing note names it.

### `--from`

```
[[ $4 =~ ^[0-9a-f]{7,64}$ ]]   else: --from '<v>' is not 7 to 64 lowercase hex digits, so the fork point cannot be compared; nothing was written
rev-parse --verify -q "$4^{commit}"   else: --from '<v>' names no commit here, so the fork point cannot be compared; nothing was written
```

Both set `PT_FROM=""` and return 1, as the one refusal does today.

### The header

Section 4 gains one sentence after its first: both verbs refuse a branch outside the runtime's
`worktree-agent-<id>` and a worktree holding it anywhere but `<primary tree>/.claude/worktrees/agent-<id>`
for the same `<id>`, so neither ever removes a tree it did not cut. Section 5 gains the bullets below
marked "(tool)". No line spells the kit's install prefix.

### The arms

`tools/workflows/unattended-build.test.sh`:

- `TP_OK`'s worktree becomes `/w/.claude/worktrees/agent-x1`, and the T1 and T4 needles follow it.
- A new `TP4` group after `TP1`, each call through `run_wf` with the args `${TP_U%\}}',"passLegs":"PL"}'`.
  It gets four assertions per hostile case and one or two per control:

| Case | `branch` returned | `worktree` returned | Assertions |
|---|---|---|---|
| `$(id)` | `worktree-agent-x1$(id)` | `/w/$(id)/.claude/worktrees/agent-x1` | 4 |
| double quote | `worktree-agent-x1"` | `/w/a"b/.claude/worktrees/agent-x1` | 4 |
| `;` | `worktree-agent-x1;id` | `/w/a;id/.claude/worktrees/agent-x1` | 4 |
| `..` | `worktree-agent-x1/../x` | `/w/../.claude/worktrees/agent-x1` | 4 |
| backtick | ``worktree-agent-x1`id` `` | ``/w/a`id`/.claude/worktrees/agent-x1`` | 4 |
| newline | `worktree-agent-x1` then LF then `b` | `/w/a` then LF then `b/.claude/worktrees/agent-x1` | 4 |
| old spelling | `agent-x1` | `/w/agent-x1` | 2 |
| a segment past the id | valid | `/w/.claude/worktrees/agent-x1/sub` | 1 |
| backslash form | valid | `C:\w\.claude\worktrees\agent-x1` | 1 |

  Each hostile case asserts, on the `RESULT` line, `"branch":""` and `"worktree":""` and the absence
  of `worktrees/agent-x1`, and on `read_next_action` that `nextAction` carries `whose path the
  builder returned unusable`. The absence reads the whole `RESULT` line, not `read_next_action`: that
  reader stops at the first `"`, so an admitted value carrying a quote would truncate it and the arm
  could not fail. The presence assertion keeps the absence from passing on a missing `nextAction`.
  The old spelling asserts both fields empty; the segment past the id asserts `"worktree":""`; the
  backslash form asserts the `RESULT` line carries `"worktree":"C:\\w\\.claude\\worktrees\\agent-x1"`,
  JSON's own escaping. The hostile values are JSON-escaped in the returns string, and are written
  without passing through a heredoc that would turn an escape into a byte.
- `FLOOR_ASSERTIONS` 1000 to 1028, with the line
  `# RAISED 1000 -> 1028 by TOOL-aTwinnedPass-4: the 28 its TP4 group executes — six hostile cases of four, the old spelling's two, and one each for the segment past the id and the backslash form. Counted by reading, not measured by a run: the pass that wrote it runs no suite.`

`tools/unattended/pass-tree.test.sh`, the respelling first:

- `add_fixture_pass` runs `git -C "$R" worktree add -q -b "worktree-agent-p$1" "$R/.claude/worktrees/agent-p$1" main`,
  and the reset and `write_fixture_pass` read that path. The fixture appends `.claude/worktrees/` to
  `$R/.git/info/exclude` before the base commit, as node a's common `info/exclude` does, so the
  clean test and the `ls-files --others` walk do not see the pass worktrees.
- Every `agent-p<n>` becomes `worktree-agent-p<n>`, every `/wt/p<n>` needle becomes
  `/.claude/worktrees/agent-p<n>`, `agent-none` becomes `worktree-agent-none`, and the T3 needle reads
  `--from 'HEAD' is not 7 to 64 lowercase hex digits`. `-x` and `run` are unchanged.

Then a `TP4` block after T5. Every branch in it is cut at `$C`, which `run` holds, so none holds a
commit no other ref holds:

| Arm | Set-up | Call | Asserts | n |
|---|---|---|---|---|
| outside holder, `--remove` | `worktree-agent-q1` at `$T/elsewhere/agent-q1`, with untracked `keep.txt` | `--remove tRun --branch worktree-agent-q1` | exit 1; one REFUSING line; it names `elsewhere/agent-q1`; the directory and `keep.txt` remain; `git rev-parse --verify -q refs/heads/worktree-agent-q1` succeeds | 6 |
| outside holder, `--merge` | as above | `--merge tRun --pass TOOL-tRun-4 --branch worktree-agent-q1 --from $C` | exit 1; stderr carries `where the runtime cuts that pass's worktree`; `HEAD` and `git status --porcelain` unchanged; the directory remains | 5 |
| a name outside the shape | `agent-q2` at `$R/.claude/worktrees/agent-q2` | `--remove`, then `--merge` naming `agent-q2` | each exits 1 with `is not a branch the runtime cuts for a pass`; the directory remains | 5 |
| a holder at another pass's place | `worktree-agent-q3` at `$R/.claude/worktrees/agent-zz` | `--remove` | exit 1; the directory remains | 2 |
| a confined holder with scratch | `worktree-agent-q4` at `$R/.claude/worktrees/agent-q4`, with untracked `scratch.txt` | `--remove` | exit 0; the directory is gone | 2 |
| `--from` of 64 digits | the branch `worktree-agent-p4`, left by T2 with its commit | `--merge ... --from <64 hex naming nothing>` | exit 1; stderr carries `names no commit` and lacks `is not 7 to 64` | 3 |
| `--from` of 65 digits | as above | `--merge ... --from <65 hex>` | stderr carries `is not 7 to 64` | 1 |

`--merge` reaches `--from` for `worktree-agent-p4` because that branch exists, is held at its own
place, and holds a commit `HEAD` lacks. The suite carries no floor, so no line is raised there.

Ceilings: the `TP4` group adds nine `node` launches to a suite whose budget row declares 500 s; the (PINNED 2026-11-15)
`pass-tree.test.sh` block adds nine tool processes, about 10 s at the 1.16 s driver launch spec 2 (PINNED 2026-11-15)
pinned, to a row declaring 300 s. Neither row moves, an ESTIMATE PINNED 2026-11-15 that the close's
run confirms.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `check_pass_holder` | the holder check | `python tools/lexicon/lexicon.py --suggest check_pass_holder --as sh.function` printed `OK`, leading `check` |
| `PT_WHERE` | global, the admitted holder | no shell-variable cell |
| `TP4` | the arm groups' label prefix in both suites | not a code name |

`git grep -nw` finds neither `check_pass_holder` nor `PT_WHERE` in the tree at base.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/unattended/pass-tree.sh`
- `tools/unattended/pass-tree.test.sh`
- `memory/map/generated/symbols.json`
- `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-4-1-acceptance-ledger.md`

### Rollout

Live, with no switch. Every pass the runtime cuts already carries this spelling, so a main loop
driving runtime-cut passes sees no change; any other branch or holder is refused, where today it is
merged or force-removed.

### Alternatives rejected

- **H2's finder fix, a dirty-tree refusal before `--force`.** The skeptic judged it unsound: a pass's
  worktree may hold a builder's scratch, and a refusal there leaves every such pass behind.
- **A prefix test on the holder, `<primary>/.claude/worktrees/agent-*`** (F1 (b)).
- **A sha256 fixture for M1.** It needs git 2.29 or later and a second copy of the whole fixture
  repository for one arm; the split refusal observes the changed half in the existing fixture.
- **Holding the run's own branch and `-x` behind the new shape.** It would make the own-branch and
  leading-dash refusals unreachable, the class `guard-above-a-fold-makes-its-fallback-dead` names,
  and turn two existing arms red for no defect.
- **A shared module for the `..` test.** The runtime evaluates each workflow script alone, which is
  why the build template copies its sibling's checks rather than importing them.

### What the design does not check

- (tool) The holder comparison is textual. A worktree registered under another spelling of the same
  path, by drive-letter case, an 8.3 short name or a link, is refused, which is the safe direction.
- (tool) A branch no worktree holds is deleted by `--remove` without a holder check, since there is
  no tree to lose; the lost-commit refusal still guards its commits.
- (tool) A runtime that cuts passes under another name or place: each such pass is refused, never
  merged or removed, until the tool learns the spelling.
- A path segment carrying a character outside `[A-Za-z0-9._ -]`, a non-ASCII user name or a `~`
  among them, returns `''`, and `nextAction` names the path unusable.
- That the returned `worktree`'s `<id>` matches the returned `branch`'s: the harness grades each
  alone, and `check_pass_holder` holds them together at the destructive end.
- The log line's raw `branch` and `worktree`.
- That the branch shape is spelled identically in the harness and the tool: two spellings, and the
  parity arm is handed off as an ask.
- Every other agent-returned field reaching `nextAction`; only `sha` and `base` already pass
  `COMMIT_SHAPE`.

## 5. Production-readiness checklist

- security — closes H1 and H2: agent free text reaches `nextAction` and `git worktree remove --force`
  only in the runtime's spelling; the holder is compared with one derived path, deny by default on an
  unreadable list; no new input, no `eval`, no new write path.
- perf / scale — one more `git worktree list --porcelain` per verb call; the suites' ceilings are in
  §4, "The arms".
- error / empty / loading states — each new refusal is one stderr line, exit 1, nothing written; a
  branch no worktree holds keeps today's behaviour.
- observability — the holder refusal names the holder and the wanted path, so an operator sees which
  tree was spared and why.
- risks — a runtime that changes its spelling turns every merge into a refusal, a loud failure with
  the tree intact; a Windows path with a character outside the class degrades `nextAction`.
- testing — AC1 to AC8 and the `New arm:` lines of §7.
- migration — N/A: no record shape or conf key moves.
- user docs — the tool's header; no `help/` page describes unattended passes (§3).

## 6. Acceptance criteria

- **AC1** — When a `node -e` probe reads `TREE_SHAPE` and `BRANCH_SHAPE` out of
  `tools/workflows/unattended-unit.js` and tests them, each of the six hostile worktrees and six
  hostile branches of §4's `TP4` table, `/w/agent-x1`, `agent-x1` and
  `/w/.claude/worktrees/agent-x1/sub` fails; and `/w/.claude/worktrees/agent-x1`,
  `C:\w\.claude\worktrees\agent-x1`, the live
  `C:/projects/coding-governance/.claude/worktrees/agent-a062c1d85fb878113` and
  `worktree-agent-a062c1d85fb878113` pass.
  Red when: a shape keeps base's class, drops the `..` lookahead, drops the backslash alternative, or
  admits a segment past the id.
- **AC2** — When `run_wf` evaluates the harness with `passBase` and `passLegs` set and each hostile
  return of §4's table, the `RESULT` line carries `"branch":""` and `"worktree":""` and lacks
  `worktrees/agent-x1`, and `nextAction` carries `whose path the builder returned unusable`; with
  `TP_OK`, the `RESULT` line carries `"worktree":"/w/.claude/worktrees/agent-x1"` and `nextAction`
  names that path.
  Red when: either shape admits a hostile value, or refuses the runtime's own spelling.
  fixture: the `TP1` args and `run_wf` of the build harness's suite; the pass observes the same with
  a `node -e` stub of `agent`.
  permission: the suite's run is the main loop's, at the close.
- **AC3** — When `bash tools/unattended/pass-tree.sh --remove tRun --branch worktree-agent-q1` runs
  in a fixture whose `worktree-agent-q1` is checked out at `<tmp>/elsewhere/agent-q1` with an
  untracked `keep.txt`, and no commit of it is unique, it exits 1 with one `pass-tree: REFUSING` line
  naming that holder, and the directory, `keep.txt` and the branch remain.
  Red when: `--remove` force-removes the worktree or deletes the branch.
  fixture: a hand-built repository in the pass-tree suite's shape, a primary tree on `run` with
  `.unattended.conf` and the run-state file of build `tRun`; the tree holds none.
- **AC4** — When `--merge tRun --pass TOOL-tRun-4 --branch worktree-agent-q1 --from <C>` runs in that
  fixture, it exits 1, its stderr carries `where the runtime cuts that pass's worktree`, and `HEAD`,
  `git status --porcelain` and the outside worktree are as they were.
  Red when: the merge reaches its later refusals or merges, so the holder is checked only at removal.
  fixture: as AC3.
- **AC5** — When `--remove` and `--merge` name `agent-q2`, held at `<primary>/.claude/worktrees/agent-q2`,
  each exits 1 with `is not a branch the runtime cuts for a pass` and the worktree remains; and when
  `--remove` names `worktree-agent-q3`, held at `<primary>/.claude/worktrees/agent-zz`, it exits 1 and
  that worktree remains.
  Red when: `check_pass_branch` admits a name outside `worktree-agent-<id>`, or the holder test is a
  prefix test.
  fixture: as AC3.
- **AC6** — When `--remove` names `worktree-agent-q4`, held at `<primary>/.claude/worktrees/agent-q4`
  with an untracked `scratch.txt`, it exits 0 and the directory and branch are gone; and when
  `--merge` runs for a pass at `<primary>/.claude/worktrees/agent-p2` on `worktree-agent-p2`, it exits
  0 and `git worktree list --porcelain` no longer names that path.
  Red when: `check_pass_holder` refuses the runtime's own place, or `--force` is dropped.
  fixture: as AC3.
- **AC7** — When `--merge` runs over a branch that would otherwise merge, with `--from` set to 64 hex
  digits naming no commit, its stderr carries `names no commit` and lacks `is not 7 to 64`; with 65
  digits, or with `HEAD`, it carries `is not 7 to 64 lowercase hex digits`.
  Red when: the shape stays `{7,40}`, admits more than 64 digits, or the two refusals stay one.
  fixture: as AC3, on a SHA-1 repository, where `git rev-parse --verify -q` refuses 64 digits.
- **AC8** — When `grep` runs over `tools/unattended/pass-tree.sh`, its header names
  `worktree-agent-<id>` and `.claude/worktrees/agent-<id>` above the first function, and
  `grep -c 'tools/unattended'` over it prints 0; `python tools/lexicon/lexicon.py --suggest
  check_pass_holder --as sh.function` prints a line opening `OK`; and
  `memory/map/generated/symbols.json` carries `check_pass_holder`.
  Red when: the header omits the spelling or spells the kit's prefix, or the index is not regenerated.

## 7. Gates

`workflow script syntax` · `unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `install-prefix self-test` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/workflows/unattended-build.test.sh · covers AC2 · the TP4 hostile cases red under both shapes replaced by `/[\s\S]*/`, which admits every string; the `..` worktree case alone red with only the lookahead dropped; the `$(id)`, quote and `;` worktree cases red at base's shapes; the backslash control red with `[\\/]` narrowed to `\/`; the old-spelling control red at base's shapes; the segment-past-the-id control red with the trailing `$` dropped · FLOOR_ASSERTIONS 1000 -> 1028
New arm: tools/unattended/pass-tree.test.sh · covers AC3 AC4 AC5 AC6 · `check_pass_holder` returning 0 always, which force-removes q1 and lets q1's merge reach the commit-count refusal; the shape test removed from `check_pass_branch`, which removes q2; the holder test widened to a `agent-*` prefix, which removes q3; `remove_pass_tree`'s `--force` dropped, which leaves q4 · none
New arm: tools/unattended/pass-tree.test.sh · covers AC7 · the `--from` shape restored to `{7,40}`, which refuses the 64-digit value by shape; widened to `{7,}`, which admits 65 digits to the lookup · none

The respelled `pass-tree.test.sh` arms re-observe AC6 at their existing T1 to T5 sites. At this
unit's close the two `remains` arms are still red, as at the tip; `TOOL-aTwinnedPass-5` turns them
green. `check-arms` grades nothing here: `pass-tree.sh` defines no `fail` helper and the harness is
JavaScript, so neither is in its population.

## 8. Open questions

- **F1 — Is the holder compared with the one path the branch implies, or with any `agent-*` place?**
  (a) Exactly `<primary>/.claude/worktrees/agent-<id>` for the branch's own `<id>`: the runtime names
  both after one id, the test is one string comparison, and a pass's branch checked out at another
  pass's place is refused. (b) Any holder under `<primary>/.claude/worktrees/agent-`, as the review's
  corrected fix words it: admits a holder at another pass's place, which `--force` then removes along
  with that pass's scratch. Recommendation: (a), on which §4 and AC5 are written; (b) drops AC5's q3
  case.
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F2 — Does `TREE_SHAPE`'s segment class admit a space?** (a) Yes, `[A-Za-z0-9._ -]`: a Windows
  user directory often carries one, and `nextAction` puts the path in a code span the main loop must
  quote anyway. (b) No: a space splits an unquoted word, and such a pass's `nextAction` degrades to
  "returned unusable" while the merge, which takes the branch alone, still works. Recommendation: (a),
  on which §4 is written.
  RESOLVED (agent, 2026-11-15, delegated): (a).

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft, from the brief
  `2026-11-15-prompt-TOOL-aTwinnedPass-4-brief` and the closing review round 1's H1, H2, M1 and M3.
- rev-2 · 2026-11-15 · §4 step 2 of `check_pass_holder`: the holder path is `<primary>/.claude/worktrees/${PT_BRANCH#worktree-}`, not `agent-${PT_BRANCH#worktree-}`, which doubled the `agent-` prefix; S5, AC5 and AC6 already said so, and the builder built to them (its report, merge `850143b3b`). Status CLOSED with the pass's code merged.

## 10. Reuse audit

The seams this unit extends: the harness's own `TREE_SHAPE` and `BRANCH_SHAPE` call sites, whose
consts change and whose readers do not; the build template's `..` test at
`tools/workflows/unattended-build.template.js@cc868b60:311`, copied into `TREE_SHAPE` as that
template copies its sibling's; `check_pass_branch`, extended by one refusal; the driver's
`derive_holder_where`, now read once by `check_pass_holder`; and `print_pass_tree_refusal` for every
new line. `python tools/codebase-map/reuse_lookup.py "hold an agent-returned worktree path and branch
name to the runtime's shape before a destructive git command"` ranked `git`, `shape`, `run_git`,
`GIT`, `add_scratch_worktree` and `common_git_dir` among its first; `shape` is the govkit matrix's,
`add_scratch_worktree` cuts a scratch tree rather than checking one, and `common_git_dir` answers the
common git directory, not the primary worktree's path. No existing seam answers "the primary tree's
path", so `check_pass_holder` reads the first record of the porcelain list `derive_holder_where`
already reads. `python tools/memory-tree/gotchas.py --for-paths` over the two subject files selected
`agent-output-interpolated-into-an-instruction`, `fixture-passes-by-finding-nothing`,
`heredoc-escape-reaches-the-regex` and `guard-above-a-fold-makes-its-fallback-dead`, each answered in
§4.

Recall terms used: `python tools/memory-recall/query.py "how is an agent-returned path or branch
validated before it reaches an instruction or a git command" --terms "TREE_SHAPE BRANCH_SHAPE
COMMIT_SHAPE worktree-agent nextAction scratch dot-dot segment shape check refusal pass-tree"`
