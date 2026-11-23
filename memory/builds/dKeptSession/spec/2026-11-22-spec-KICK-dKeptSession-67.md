# KICK-dKeptSession-67 — pass-tree regenerates over the merge as it will be committed, so a pass that changes a mirror input merges

**Status:** CLOSED · rev-3 · 2026-11-22 · node d · Tier-2 · base ce776cccc · streams tooling · order 7 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-21-build-KICK-dKeptSession-67-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-67-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-67-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-67-build-brief.md) | research | — |
| [2026-11-22-prompt-KICK-dKeptSession-67-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-67-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-67-2-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-67-2-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-67-3-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-67-3-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-67-bind-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-67-bind-brief.md) | research | — |
| [2026-11-22-prompt-KICK-dKeptSession-67-pin-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-67-pin-brief.md) | research | — |
| [2026-11-22-prompt-KICK-dKeptSession-67-spec-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-67-spec-brief.md) | research | — |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

`pass-tree.sh --merge` runs `regen.py --write` while HEAD is still the pre-merge commit, so a
renderer that reads the committed revision meets the pass's inputs as uncommitted changes and
refuses. The policy mirror is such a renderer, so no pass that changes a mirror input can merge,
KICK-dKeptSession-16's included. This unit runs the regeneration with HEAD on a provisional commit
of the merge, carrying the same parents, tree and message. The lander's `--prepare` regenerates in
the same condition, so every renderer sees the merge's revision and no renderer's check loosens.

## 2. Scope (IN)

- **S1** — The provisional merge, in `run_pass_tree_regen`
  (`tools/unattended/pass-tree.sh#run_pass_tree_regen`). The function takes three arguments: the
  pre-merge HEAD, the pass tip and the merge message file. Its python and kit resolution, and both
  of its announced skips, stay as they are and run before anything moves. It then writes the index
  as a tree (`GIT write-tree`) and makes the provisional commit with `GIT commit-tree <tree> -p
  <pre-merge HEAD> -p <pass tip> -F <message file>`. It detaches HEAD onto that commit with `GIT
  update-ref --no-deref HEAD <commit>`, runs `regen.py --write` as today, and then puts HEAD back on
  the run's branch with `GIT symbolic-ref HEAD "$HW_REF"`, whatever the write's exit. `HW_REF` is
  the ref `check_pass_tree_run` left (`tools/unattended/unattended.sh#resolve_holder_worktree`). It
  returns 1 when the tree, the commit, the detach or the re-attach fails, each with a line naming
  the step that failed, and 1 when the write fails, as today. `cmd_merge_tree`
  (`tools/unattended/pass-tree.sh#cmd_merge_tree`) computes `tip` and writes the message file before
  the call rather than after the staging, so the provisional commit and the merge commit carry one
  message. Observed by AC1, AC2.
- **S2** — The restore, `remove_merge_attempt`
  (`tools/unattended/pass-tree.sh#remove_merge_attempt`), runs `GIT symbolic-ref HEAD "$HW_REF"`
  before its `reset --hard HEAD`, so a failure while HEAD is detached resets to the pre-merge commit
  and not to the provisional one. On a tree where HEAD is already on the run's branch the
  re-attach writes what HEAD already holds. Observed by AC3.
- **S3** — The suite's renderer of a committed revision, in `tools/unattended/pass-tree.test.sh`.
  The fixture kit `fx` gains a third `[[generated]]` row, `fx-rev.txt`, written by a new fixture
  generator `rev.sh` at stage 2, with `check = ["bash", "{kit}/rev.sh", "--check"]`. `rev.sh` models
  `cmd_mirror` (`tools/policy/policy.py#cmd_mirror`). Its inputs are the tracked `in-*.txt` files
  that `git ls-files` lists. In both modes it exits 2 printing `fx-rev: refused · <path> ·
  uncommitted changes; the render reads a revision, commit first` on stderr while an input's
  `git hash-object` differs from its blob at HEAD, an input absent at HEAD included. Otherwise it
  renders one line per input, `<path> <blob id at HEAD>`, sorted, into `fx-rev.txt`: `--check`
  compares and exits 0 or 1, and the write writes. The base gains `in-0.txt`, and its commit is
  amended with the render, since a root commit has no HEAD to render from. Observed by AC1, AC2.
- **S4** — The suite's cases. A block `K67` after the `TP11` block. Pass 13 adds `in-13.txt` in one
  commit and carries `rev.sh`'s re-render in a second commit, as KICK-dKeptSession-16's pass did.
  Pass 14 adds `in-14.txt` in one commit and carries the base's `fx-rev.txt` unrendered. Each is
  merged with `--merge`, pass 13 first. `T4` gains one arm: after its failed regeneration, `git
  symbolic-ref -q HEAD` prints `refs/heads/run`. Observed by AC1, AC2, AC3.
- **S5** — The text. The header of `tools/unattended/pass-tree.sh`, in "4. WHAT `--merge` DOES",
  says the regeneration runs with HEAD on a provisional commit of the merge, the one line of the file
  that spells that phrase. Its "5. WHAT IT DOES NOT CHECK" gains the three bullets that §4 "What it
  does not check" below lists. The kit README's paragraph on parallel passes
  (`tools/unattended/README.md`, "Parallel passes come back through `pass-tree.sh`") replaces
  "re-renders the outputs" with "re-renders the outputs over the merge as it will be committed, so a
  renderer that reads the committed revision, as the policy mirror does, reads the pass's inputs".
  Each of the two grepped phrases sits whole on one line. The suite's header names `rev.sh` and its
  row. None of the three files spells a kit path. Observed by AC4.

## 3. Non-goals (OUT)

- `tools/policy/policy.py`, `tools/policy/guard.py` and the policy kit's `[[generated]]` rows: the
  mirror's refusal and both of its readers stay exactly as landed (§8 F1).
- `tools/run-gates/regen.py` and `tools/push-main.sh`: the lander's two landing paths are the
  precedent this unit follows, never a file it edits.
- Refusing a pass whose carried mirror is stale: the regeneration replaces it, as it replaces every
  other generated output (§8 F2).
- Merging KICK-dKeptSession-16's pass. That is the main loop's act after this unit's pass merges, and
  AC5 observes it.
- The open specs that change a mirror input. Fourteen specs name the catalogue or the preset store,
  PINNED by the brief on 2026-11-22: ids 6, 7, 8, 9, 10, 11, 13, 14, 17, 21, 24, 35, 41 and 44. Each
  merges through this unit's code, and none of them changes.
- A trap that restores HEAD when the process is killed mid-regeneration. §4 "What it does not check"
  states that case and its recovery, and today's code leaves a half-made merge there too.

### Edges

- **consumes-from** external — the lander's `--prepare` order at this spec's base, which regenerates with HEAD detached on the merge it then rewrites; this unit copies that condition and edits nothing of it
- **hands-off** external — the re-run of KICK-dKeptSession-16's `--merge` with this code, the main loop's act once this unit's pass has merged

## 4. Design

### Evidence

- `cmd_mirror` refuses `--write`, `--check` and `--print` while any recorded input differs in the
  working tree from its blob at HEAD. The inputs are the policy file, the catalogue and each
  `derive_mirror_inputs` path. Then it renders at HEAD (`tools/policy/policy.py#cmd_mirror`,
  `#derive_mirror_inputs`). The refusal is TOOL-dGroundRules-25 S20's: the mirror renders a
  revision, never a working tree.
- `render_mirror` reads `read_revision(repo, rev)` and records the inputs' blob ids there. Its
  invariant: two commits with the same input blobs and the same first-parent history render
  byte-identical mirrors (`tools/policy/policy.py#render_mirror`, TOOL-dGroundRules-65). The
  provisional commit and the merge commit share both, so the render made over the first is the
  render of the second.
- `cmd_merge_tree` merges `--no-ff --no-commit`, resolves admitted conflicts to this side, calls
  `run_pass_tree_regen`, stages, and only then commits (`tools/unattended/pass-tree.sh#cmd_merge_tree`).
  At the call, HEAD is the pre-merge commit and the index holds the pass's inputs, which is the
  refusal the brief reports.
- `regen.py --write` follows a failed write with its own check, and reads the item `declined`
  only when that check is fresh (`tools/run-gates/regen.py#run_writes`). The mirror's check refuses
  identically, so the item is FAILED, and `run_pass_tree_regen` returns 1.
- The lander regenerates over a committed revision on both paths. `--prepare` checks out the
  advertised tip detached, merges onto it, folds the mint and the walk, and runs `run_regen` with
  HEAD detached on that merge. It then rewrites the merge over the regenerated tree with
  `commit-tree`, same parents and message (`tools/push-main.sh#cmd_prepare`, `#run_regen`,
  `#write_merge_fold`). The comment there names the reason: "the policy mirror renders only a
  committed input". The attended landing commits each stage before its regeneration and commits the
  regeneration as its own `regen:` commit (the attended loop's REGENERATE block in
  `tools/push-main.sh`).
- The policy guard admits a staged mirror when its blob is a parent's, as at a merge concluded with a
  side (`tools/policy/guard.py#check_parent_sides`). It also admits a staged mirror whose inputs are
  staged as HEAD holds them and whose bytes are `mirror --print` at HEAD
  (`tools/policy/guard.py#check_mirror_render`), and anything on a live run's branch. The merge
  commit's hook runs with HEAD on the pre-merge commit, as today, so none of these readings changes.
- `policy.py settings --write`, the stage-1 item of the same kit, reads `runtime.agents-in-flight` at
  HEAD with no uncommitted-input refusal (`tools/policy/policy.py#cmd_settings`). Today a pass that
  changes that key merges with the settings rendered from the pre-merge HEAD. Over the provisional
  commit it renders from the merge.
- The stage-commit lint gates a `commit` or `commit-tree` placed after a stage in one function's
  scope with no staged test between them (`tools/gate-lint/sh_hygiene.py#scan_stage_file`).
  `run_pass_tree_regen` stages nothing, so its `commit-tree` is `unpaired`, counted and printed and
  never gated. The registered `unchecked-stage` site of `pass-tree.sh` in
  `memory/project/stage-commit-sites.txt` is the `GIT add -u` and `GIT commit` pair in
  `cmd_merge_tree`, which does not move.
- The codebase map keys a function by name, kind and file alone (the `run_pass_tree_regen` row of
  `memory/map/generated/symbols.json`). This unit mints no function, so that file does not move.
- The pass-tree suite's budget row, `unattended pass-tree selftest` in
  `tools/run-gates/selftest-budgets.txt`, is an ESTIMATE of 300 seconds PINNED 2026-11-15 by
  TOOL-aTwinnedPass-2 and carries no `plants=` token. S4 adds two merges, so the row moves only if
  the close's reading exceeds it.
- No page under `help/` names `pass-tree`, by `grep -rl pass-tree help/` at the base. The tool's
  documentation is its header and the kit README's paragraph, which S5 updates.
- No governance carrier changes. `tools/unattended/VERBS.template.md` names `pass-tree.sh --merge`
  per committed pass and says nothing about when it regenerates.

### The flow, after this unit

```
cmd_merge_tree
  merge --no-ff --no-commit; resolve admitted conflicts to this side        (unchanged)
  tip=<pass tip>; write the merge message file                              (moved up, S1)
  run_pass_tree_regen <pre-merge HEAD> <tip> <message file>
    resolve python and regen.py, else announce and return 0                 (unchanged)
    P = commit-tree(write-tree, -p <pre-merge HEAD> -p <tip>, -F <message>)
    update-ref --no-deref HEAD P            HEAD detached on the provisional merge
    regen.py --write                         every renderer reads revision P
    symbolic-ref HEAD $HW_REF               HEAD back on the run's branch, at the pre-merge commit
  add -u; stage generated untracked files; commit -F <message>              (unchanged)
```

At the final `git commit`, the index, HEAD and `MERGE_HEAD` are what today's code presents there
whenever its regeneration does not refuse. So the hooks grade the commit they grade today. The
provisional commit is referenced by HEAD's reflog alone, and git's garbage collection removes it.

### What it does not check

These three are S5's header bullets.

- A process killed while the regeneration runs leaves HEAD detached on the provisional commit, with
  the merge in progress. The next `--merge` refuses at the run check, since the tree no longer has
  the run's branch checked out. The recovery is `git symbolic-ref HEAD <run ref>`, then `git reset
  --hard` and `git clean -fd`.
- A generator that reads HEAD's tree for an output an earlier stage wrote reads the provisional
  commit's bytes, from before the regeneration. The lander's `--prepare` has the same property.
- A generator that reads the checked-out branch's name reads none while HEAD is detached. The lander's
  `--prepare` regenerates detached too, so such a generator already meets this at every landing.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `rev.sh` | fixture generator, written by `pass-tree.test.sh` into its fixture kit | none: no function |
| `fx-rev.txt`, `in-0.txt`, `in-13.txt`, `in-14.txt` | fixture files | none |
| `K67` | suite block label | none |

No function is minted in `pass-tree.sh` or `pass-tree.test.sh`.

### Migration

None. The tool keeps its argv, its exits and its refusal texts. The commits a merge makes are the
same ones, plus the unreferenced provisional commit.

### Rollout

Live at landing. A pass that changes no mirror input merges as it does today. A pass that changes
one merges where today it refuses.

### Files touched (estimate)

- `tools/unattended/pass-tree.sh`: S1, S2 and S5's header text
- `tools/unattended/pass-tree.test.sh`: S3's row and generator, S4's block and `T4` arm, and the
  header naming them
- `tools/unattended/README.md`: S5's paragraph
- `memory/builds/dKeptSession/README.md`, `memory/LIVE.md` and `memory/backlog/KICK.md`: rendered
  and staged by the pre-commit memory-hygiene leg's `gen_build_index.py --write-staged` when the
  pass's commit stages its records, as in KICK-dKeptSession-16's pass; never hand-edited
- The kickoff manifest watches none of these paths (its `watch:` line in
  `memory/guides/SESSION-KICKOFF.md`)

### Alternatives rejected

- **Commit the merge, then regenerate in a follow-up commit**, the attended landing's shape. The
  merge commit's hooks would then grade it before the regeneration. Its pre-commit runs the
  codebase-map freshness leg over a staged `.py` and the memory-hygiene leg over a staged record.
  Each would red the merge whenever the resolution left a generated output stale, the case the
  regeneration exists for. The run's branch would also carry a commit whose outputs no hook saw
  fresh.
- **Accept a staged mirror equal to the render of the staged inputs**, in `cmd_mirror` or in the
  policy kit's `[[generated]]` row. That renders an index, a revision nobody committed, which is
  exactly what S20 refuses. The policy guard's `mirror --print` and the push bar's preflight both
  read the same verb, so loosening it loosens them. The class also stays unfixed: `settings
  --write` and any other renderer of HEAD keep reading the pre-merge commit.
- **Move the run's branch to the provisional commit instead of detaching HEAD.** For the whole
  regeneration the branch would name a commit that never lands, visible to any reader of that ref.
  The lander's own regeneration runs detached, so detaching matches it (§8 F3).
- **Commit the merge, regenerate, then `git commit --amend`.** The first commit fires the hooks
  before the regeneration, the defect of the follow-up shape, and the amend fires them again.
- **Regenerate in a temporary worktree checked out at the provisional commit.** The generators would
  write in another tree, and copying back the paths a regeneration moved would duplicate
  `regen.py`'s dirty-path diff in shell.

## 5. Production-readiness checklist

- security — no new write path or input. The provisional commit is made from the index the merge
  already staged, and HEAD returns to the ref the run check resolved. No hook is skipped: the
  merge commit still goes through `git commit` with hooks running.
- perf / scale — one `write-tree`, one `commit-tree` and two ref writes per merge, against a
  regeneration measured in minutes.
- error / empty / loading states — each of the four git steps that can fail returns 1 naming its
  step, and the caller's restore re-attaches HEAD before it resets. Both announced skips return
  before HEAD moves.
- observability — the regeneration's lines print as today. A failed provisional step prints its own
  line before the existing REFUSING line.
- risks — a generator that depends on HEAD being symbolic, the second and third bullets of §4 "What
  it does not check", which the lander already exercises. The `check-unattended` fork ceiling in
  `memory/project/fork-ceilings.txt` counts check 28's raw-git candidate lines in the kit's non-test
  shell files. New lines spelled through the `GIT` wrapper, with no lowercase `git` in their
  messages, keep it where it is. If the close's reading moves it, the row is raised in this unit
  with its measurement.
- testing — S4's block and the `T4` arm, red at the base on the block's first merge.
- migration — none.
- user docs — no `help/` page describes the tool; its header and the kit README's paragraph (S5).

## 6. Acceptance criteria

The fixture for AC1 to AC3 is the pass-tree suite's fixture repository, built in a scratch
directory as the suite's fixture section builds it, with S3's row, `rev.sh` and `in-0.txt` added.
`<C>` is its records commit, and `<kit>` is the unattended kit's directory.

- **AC1** — When pass 13 adds `in-13.txt` and carries `rev.sh`'s re-render in a second commit, and
  `bash <kit>/pass-tree.sh --merge tRun --pass TOOL-tRun-13 --branch worktree-agent-p13 --from <C>`
  runs in the fixture, it exits 0 and prints one sha, which is `git rev-parse HEAD`. Its stderr
  carries no `pass-tree: REFUSING` line. The merge's first parent is the pre-merge HEAD and its
  second is pass 13's tip. `git show HEAD:fx-rev.txt` equals `git show worktree-agent-p13:fx-rev.txt`
  as captured before the merge. `rev.sh --check`, run from the fixture's top as the suite runs
  `render.sh`, exits 0, and `git symbolic-ref HEAD` prints `refs/heads/run`.
  Red when: the regeneration runs with HEAD on the pre-merge commit. `pass-tree.sh` at ce776cccc is
  that break: there the call exits 1, and its stderr carries `regen: FAILED · stage 2 · fx ·
  fx-rev.txt`, `fx-rev: refused · in-13.txt · uncommitted changes` and `pass-tree: REFUSING - the
  regeneration failed`, the block's RED-first reading.
  fixture: the scratch fixture above, built by the probe; the tree holds none.
- **AC2** — When pass 14 adds `in-14.txt` and carries the base's `fx-rev.txt` unrendered, and the
  same call with `--pass TOOL-tRun-14 --branch worktree-agent-p14` runs after AC1's merge, it exits 0
  and prints one sha. `git show HEAD:fx-rev.txt` differs from `git show worktree-agent-p14:fx-rev.txt`
  as captured before the merge. `grep -c "^in-14.txt $(git rev-parse HEAD:in-14.txt)$" fx-rev.txt`
  prints `1`, and `rev.sh --check`, run from the fixture's top, exits 0.
  Red when: the merge commits the pass's stale bytes, or refuses the pass. At ce776cccc it refuses
  as AC1 says, naming `in-14.txt`.
  fixture: as AC1, with AC1's merge made first.
- **AC3** — When `FX_RENDER_FAIL=1 bash <kit>/pass-tree.sh --merge tRun --pass TOOL-tRun-7 --branch
  worktree-agent-p7 --from <C>` runs in the fixture, as `T4` runs it, it exits 1 with `the
  regeneration failed` on stderr. `git rev-parse HEAD` is the pre-merge sha, `git symbolic-ref -q
  HEAD` prints `refs/heads/run`, `git status --porcelain` prints nothing, and `git rev-parse -q
  --verify MERGE_HEAD` exits 1.
  Red when: the restore resets while HEAD is detached. Without S2's re-attach, HEAD stays on the
  provisional commit and the sha arm reds. With the re-attach replaced by `reset --hard
  <pre-merge sha>`, HEAD is left detached, and only the symbolic-ref arm reds.
  fixture: as AC1.
- **AC4** — When `grep -c "over the merge as it will be committed" README.md` runs in the unattended
  kit, it prints `1`. `grep -c "provisional commit of the merge" pass-tree.sh` prints `1`, the
  header's sentence, and `grep -c "tools/" pass-tree.sh README.md pass-tree.test.sh` prints
  one line per file it names, in that order, each with the count 0.
  Red when: the README still says only "re-renders the outputs", or a new line spells a kit path.
  figure: the three zero counts are PINNED, measured 2026-11-22 at ce776cccc by the same command.
- **AC5** — When, after this unit's pass has merged, `bash tools/unattended/pass-tree.sh --merge
  dKeptSession --pass KICK-dKeptSession-16 --branch worktree-wf_ce213496-950-1 --from
  b4b570ef771580c665b07105eb9c85d33ae89926` runs in the run's tree, it exits 0 and prints one sha
  whose second parent is `4ee5af863`. Its stderr carries no `regen: FAILED` line, and
  `python tools/policy/policy.py mirror --check` then prints `policy: mirror fresh` and exits 0.
  Red when: the refusal the brief reports recurs, a `policy: refused` line naming
  `tools/policy/catalogue.toml` at line 0 with `uncommitted changes`.
  fixture: branch `worktree-wf_ce213496-950-1` at `4ee5af863`, forking from `b4b570ef7`, held in this
  tree on 2026-11-22.
  permission: the main loop's act, which moves the run's branch, made after this unit's own merge.

## 7. Gates

`unattended kit gate` · `shell hygiene (a stage committed with no staged-diff test)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/pass-tree.test.sh · covers AC1 AC2 AC3 · the `K67` block's two merges and `T4`'s symbolic-ref arm, staged RED against `pass-tree.sh` at ce776cccc, where `rev.sh` refuses the merge's uncommitted `in-13.txt` and the block's first merge exits 1 · none

## 8. Open questions

- **F1 — Where does the fix live?** Options: (a) pass-tree's regeneration runs with HEAD on a
  provisional commit of the merge; (b) pass-tree commits the merge and regenerates in a follow-up
  commit; (c) `cmd_mirror` or the policy kit's `[[generated]]` row accepts a staged mirror equal to
  the render of the staged inputs. (b) fires the merge's hooks before its outputs are fresh, and
  (c) renders a revision nobody committed and loosens the verb that the guard and the push bar both
  read. RESOLVED (agent, 2026-11-22, delegated): (a), rung 3; the most capable survivor, fixing the
  class of renderers that read HEAD in the lander's own condition with no mirror check loosened.
  widens: none · relaxes: none
- **F2 — A pass that changes a mirror input and carries a stale mirror: refuse it, or re-render it?**
  The brief asks for this case to be refused. Options: (a) the regeneration re-renders it, as it
  re-renders every generated output, and the merge carries the render at the merge; (b) pass-tree
  refuses a merge whose regeneration moved the mirror. (b) also refuses a legitimate pass. Two passes
  that change the catalogue conflict on the mirror, the tool resolves it to this side by its own
  rule, and the second pass's mirror is then stale by construction. A pass whose sibling changed the
  preset store merges into a render neither carried. Today a pass that changes no input and carries
  a stale mirror is already re-rendered. RESOLVED (agent, 2026-11-22, delegated): (a), rung 3; the
  stale bytes never land, which is what the brief's case guards, and AC2 observes it. widens: none ·
  relaxes: none
- **F3 — Detach HEAD onto the provisional commit, or move the run's branch to it?** Options: (a)
  `update-ref --no-deref HEAD`, then `symbolic-ref HEAD` back; (b) a compare-and-swap of the run's
  branch to the provisional commit and back. (b) has the branch name a commit that never lands for
  the whole regeneration, which other readers of that ref can see. (a) gives every generator the
  condition it already meets at the lander's `--prepare`. RESOLVED (agent, 2026-11-22, delegated):
  (a), rung 3; it matches the lander and never moves a ref another reader holds. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-11-22 · initial draft, from the brief
  `2026-11-22-prompt-KICK-dKeptSession-67-spec-brief`, grounded at ce776cccc on
  `tools/unattended/pass-tree.sh`, its suite, `tools/policy/policy.py`'s mirror, the policy guard,
  `tools/run-gates/regen.py` and the lander's two regeneration paths.
- rev-2 · 2026-11-22 · the header gains a Derived binding on PLAY-dClosedLoop-2, binding the
  unit to the design as one the build added, from the brief
  `2026-11-22-prompt-KICK-dKeptSession-67-bind-brief`. No clause asks for this unit, so no Carries line
  fits, and the Moved, Retired and Deferred keys each release a clause. §1 to §8 and §10 are unchanged.
- rev-3 · 2026-11-22 · AC4's three zero counts and AC5's quoted refusal now name their files and
  the value 0 without a file:line suffix, which the positional check read as three unlisted
  line-zero citations, from the brief `2026-11-22-prompt-KICK-dKeptSession-67-3-spec-writer`. Both
  criteria observe what they did before, and the rest of the text is unchanged.

## 10. Reuse audit

The seam extended is `run_pass_tree_regen` (`tools/unattended/pass-tree.sh#run_pass_tree_regen`),
the tool's one regeneration call, together with its restore `remove_merge_attempt`. The condition it
adopts is the lander's: `cmd_prepare` regenerates with HEAD detached on the merge, and
`write_merge_fold` moves HEAD with `update-ref --no-deref` (`tools/push-main.sh#cmd_prepare`,
`#write_merge_fold`). The suite's fixture kit and its `render.sh` are the seam S3 extends with one
more row. `python tools/codebase-map/reuse_lookup.py "regenerate generated outputs over a merge
before it is committed so a renderer that reads HEAD sees the merged inputs"`, run 2026-11-22,
ranked name stems only (`read_text`, `read`, `merge`, `read_git`, `read_policy_value`). None
regenerates over a provisional commit, so no further seam fits, and the unit extends the two
functions above. The recall query returned the pass-tree spec TOOL-aTwinnedPass-2, the landing
replay TOOL-dGroundRules-14, the install-day mirror deferral TOOL-dGroundRules-31 and this unit's
brief. None of them builds a provisional merge.

Recall terms used: `python tools/memory-recall/query.py "pass-tree merge regeneration refused because the policy mirror renders a committed revision" --terms "pass-tree run_pass_tree_regen regen.py mirror cmd_mirror uncommitted commit-tree write_merge_fold run_regen prepare provisional merge"`
