# TOOL-aTwinnedPass-2 — the pass-tree tool: cut a pass's worktree from the run's tip, and merge it back `--no-ff` with generated outputs re-rendered

**Status:** SPECCED · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 2 · closes TOOL-dDerivedDocket-57

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md) | research | TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-3 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md) | research | TOOL-aTwinnedPass-1 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-2-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A main loop can build two or more disjoint units of one build at once only if each builder has its
own git index and the main loop can bring every pass back without a hand merge. This unit ships one
kit tool, `tools/unattended/pass-tree.sh`, whose `--cut` verb gives a dispatched unit its own
worktree and branch at the run's tip, and whose `--merge` verb merges that branch back `--no-ff`,
resolves only the conflicts a regeneration answers, re-renders the generated outputs with the
run-gates kit's `regen.py --write`, and commits a merge whose second parent is the builder's own pass
commit.

## 2. Scope (IN)

- **S1** — A new file `tools/unattended/pass-tree.sh`, run by the main loop in the run's own tree. It
  sources the driver `unattended.sh` beside it, which sources `lib-unattended.sh`, calls
  `load_driver_conf`, and dispatches one of three verbs: `--cut <slug> --pass <unit>`,
  `--merge <slug> --pass <unit>` and `--remove <slug> --pass <unit>` (F2 (a), F3 (a)). Exit 0 done,
  1 a named refusal on stderr, 2 misconfigured. Observed by AC1, AC2, AC5.
  **Readers:** by name: none, since this item adds a tool and withdraws no name; the worktree and
  branch it takes away are the pass's own, which no file spells · by value: NO VALUE READERS, the
  pass's tree and branch exist only between `--cut` and this verb.
- **S2** — One run check every verb makes first, `check_pass_tree_run`: the run-state file of the
  slug exists, its recorded phase is neither `LANDED` nor `ABORTED`, and `resolve_holder_worktree`
  says this tree has the run's branch checked out, as `check_commit_message` reads the binding. The
  cut and merge verbs also require the tree clean: `git status --porcelain` prints nothing, untracked
  files included. Observed by AC2, AC5.
- **S3** — One derivation of the pass's names, `derive_pass_tree`: branch
  `<run branch>-p<seq>` and path `<run tree>-p<seq>`, `<seq>` being the unit id's trailing number
  (§4, "The names"). Every verb reads it, and nothing else spells either name. Observed by AC1, AC3.
- **S4** — `--cut` refuses a unit with no open dispatch row and a unit whose branch or path already
  exists, naming it, then runs `git worktree add -b <branch> <path> HEAD` and prints the path on
  stdout and nothing else there. Observed by AC1, AC2.
- **S5** — `--merge` refuses unless the unit's branch exists, is ahead of `HEAD`, and has not changed
  the run-state file since the merge base. It runs `git merge --no-ff --no-commit <branch>`, resolves
  to this side each conflicted path that `check_resolvable_path` admits, and on any other conflicted
  path runs `git merge --abort` and refuses with exit 1 naming every such path. Observed by AC3, AC4,
  AC5.
- **S6** — After resolution `--merge` runs `run_pass_tree_regen`, stages every tracked change and
  every new file under an effective generated output, and commits the subject
  `merge(<slug>): <unit>'s pass tree` with a `Pass: none` trailer, hooks running. It then removes the
  pass's worktree and branch through `remove_pass_tree` and prints the merge sha alone on stdout.
  Observed by AC3, AC6, AC8.
  **Readers:** by name: none, since this item adds a tool and withdraws no name; the worktree and
  branch it takes away are the pass's own, which no file spells · by value: NO VALUE READERS, the
  pass's tree and branch exist only between `--cut` and this verb.
- **S7** — A failure after the merge started and before its commit landed, a regeneration or a
  commit refusal, restores the tree to the pre-merge `HEAD` with nothing staged, no merge in
  progress and no new file, and refuses with exit 1. Observed by AC4, AC6.
- **S8** — `--remove` takes away the worktree and branch of a pass that returned `committed: false`.
  It refuses a branch that is ahead of `HEAD`, naming `--merge`. Observed by AC7.
  **Readers:** by name: none, since this item adds a tool and withdraws no name; the worktree and
  branch it takes away are the pass's own, which no file spells · by value: NO VALUE READERS, the
  pass's tree and branch exist only between `--cut` and this verb.
- **S9** — The tool's header states the order the main loop runs it in, the two unit-harness keys it
  pairs with, `tree` and `writes`, and what it does not check (§4, "The header"). Observed by AC9.
- **S10** — The suite `tools/unattended/pass-tree.test.sh`, over a fixture repository, with the arms
  of §4, "The suite". Observed by AC1 to AC8 through the `New arm:` lines of §7.
- **S11** — The kit names the tool: `tools/unattended/kit.toml` withholds the suite from
  `govkit apply` beside the kit's other non-gate suites, `tools/unattended/README.md` names the tool
  and its two pairing points, and `tools/run-gates/selftest-budgets.txt` carries the suite's row.
  Observed by AC10.
- **S12** — The verbs guide's "Drive the build as ONE program" bullet names the parallel route, in
  `tools/unattended/VERBS.template.md` and its copy `memory/guides/UNATTENDED-VERBS.md`, byte-equal
  past line 1. Observed by AC9.
- **S13** — `memory/map/generated/symbols.json` regenerated with `gen_map.py --write`, carrying the
  new functions. Observed by AC10.
- **S14** — A measured before and after: two disjoint units built serially through the unit harness in
  one tree, against the same two built in parallel through `tree`, `--cut` and `--merge`, on a frozen
  clone, wall clock per phase, recorded by the main loop under this build's `build/` folder.
  Observed by AC11.

## 3. Non-goals (OUT)

- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`: called as they
  are, never changed. The live dDeclaredLoop branch rewrote them.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.
- The unit harness and its keys, which are `TOOL-aTwinnedPass-1`'s, and `--dispatch`'s condition 1,
  which is `TOOL-aTwinnedPass-3`'s.
- The build harness `unattended-build.js`, the unattended Skill's loop, and how a main loop picks
  which units go together: the build order and M6 already say which may.
- Resolving a conflict on any path that is neither under an effective generated output nor a
  gen-region-only change. Such a merge is aborted and refused, never resolved here.
- A cap on how many passes run at once: that is the review protocol's fan-out bound, unchanged.
- A new driver verb, or any change to `tools/unattended/unattended.sh` or `lib-unattended.sh`.
- Re-stamping the kickoff manifest at a merge, which ask `TOOL-dDerivedDocket-57` names: a pass that
  edits a watched carrier re-stamps it in its own commit, the manifest is then a path that pass
  declares, and condition 1 keeps two such passes out of one group.
- The kit version: the lander's `mint` moves it (`tools/push-main.sh@c7cd70b9:26`, "KIT VERSIONS ARE
  MINTED HERE").
- A page under `help/` (§4, "Docs").
- A `--no-verify` on any commit, or any edit of a hook's verdict: a refused merge commit is the main
  loop's to read.

### Edges

- **consumes-from** `TOOL-aTwinnedPass-3` — the library predicate `check_generated_output`, which
  `check_resolvable_path` calls for the generated half of its test rather than re-spelling the
  `covers` loop a fourth time.
- **consumes-from** `TOOL-aTwinnedPass-1` — the unit harness's `tree` and `writes` keys, which this
  tool's header documents and its `--cut` output feeds: `tree` must admit the path `--cut` prints,
  git's own top-level spelling, `C:/...` on node a. Without that key a pass cut here has no builder
  that works in its tree.

## 4. Design

### Evidence

Read at base `aebbb4a72`.

| Citation | What sits there |
|---|---|
| `tools/unattended/unattended.sh@eb567029:99` | `KIT_DIR`, derived from the driver's own path, so a sourcing tool gets the driver's kit directory |
| `tools/unattended/unattended.sh@eb567029:638` | `load_driver_conf`: cds to the top level, loads `.unattended.conf`, exits 2 on a refusal |
| `tools/unattended/unattended.sh@eb567029:890` | `GENERATED_INDEXES=$(resolve_generated_indexes ...)`: the effective `index:generator` pairs |
| `tools/unattended/unattended.sh@eb567029:1573` | `fact`, the `## Run facts` reader |
| `tools/unattended/unattended.sh@eb567029:1840` | `read_recorded_phase` |
| `tools/unattended/unattended.sh@eb567029:8954` | `resolve_holder_worktree`: `run-branch`, else `branch-ref`, against `git symbolic-ref -q HEAD`; leaves `HW_REF` |
| `tools/unattended/unattended.sh@eb567029:14227` | `check_pass_open` over a key's declared set |
| `tools/unattended/unattended.sh@eb567029:14271` | `check_commit_message` skips a `LANDED` or `ABORTED` record, then asks `resolve_holder_worktree` at `tools/unattended/unattended.sh@eb567029:14272` |
| `tools/unattended/unattended.sh@eb567029:14311` | `check_commit_message` returns 0 on a `Pass: none` trailer before reading anything else |
| `tools/unattended/unattended.sh@eb567029:14352` | the generated exemption, `covers "${q%%:*}" "$p"` over `GENERATED_INDEXES` |
| `tools/unattended/unattended.sh@eb567029:14444` | `derive_spec_token_key` finds a run-gates file with `resolve_kit_dir "$2" run-gates <file> "$KIT_DIR"` |
| `tools/unattended/unattended.sh@eb567029:15540` | a sourced driver returns before `main` |
| `tools/unattended/lib-unattended.sh@a3e03db6:746` | `covers`; `overlaps` at `tools/unattended/lib-unattended.sh@a3e03db6:751` |
| `tools/unattended/lib-unattended.sh@a3e03db6:839` | `resolve_generated_indexes`: the kits' `[[generated]]` rows, then the conf's pairs |
| `tools/unattended/lib-unattended.sh@a3e03db6:1027` | `pass_commit`: walks `<anchor>..HEAD` with no `--first-parent`, skips a `Pass: none` commit |
| `tools/unattended/lib-unattended.sh@a3e03db6:1117` | `read_pass_declarations`, one line per key, `current` keeping each unit's last key |
| `tools/unattended/lib-unattended.sh@a3e03db6:1154` | `check_gen_region_only <before> <after>`: returns 1 unless both objects exist |
| `tools/push-main.sh@c7cd70b9:851` | `resolve_lander_kit`: `resolve_python`, `resolve_kit_dir`, then the file test under the top level |
| `tools/push-main.sh@c7cd70b9:902` | `run_regen`: no python or no kit announces and returns 0; a failed `--write` returns 1 |
| `tools/run-gates/regen.py@07644e72:320` | a `[[regenerate]]` row with no `stage` is skipped and announced, so `--write` never re-renders it |
| `tools/memory-tree/routed_commits.py@5e29003b:6` | the routed-commits leg grades non-merge commits; `tools/memory-tree/routed_commits.py@5e29003b:60` says a merge's own content is not graded |
| `tools/hooks/scratch-guard.js@7c31933f:784` | `checkOriented` returns null when `agent_id` is present: a subagent's commit is not orientation-gated |
| `.gitattributes@0b13fe87:94` | the `merge=ours` rows: `memory/LIVE.md`, the ledger, the gotchas index, the as-built view at `.gitattributes@0b13fe87:104`, `.governance/instructions.lock` at `.gitattributes@0b13fe87:108` |
| `tools/run-gates/lib-attribute.sh@072e6d1f:59` | `add_scratch_worktree`: `git worktree add --detach`, its messages left to the caller |

### What the brief says that the code does not

- **Item 5.** The two lib predicates are not all the tool needs. The run check needs `fact`,
  `read_recorded_phase` and `resolve_holder_worktree`, the open-row check needs `check_pass_open`,
  and the effective generated set needs `load_driver_conf`; all five are in the driver, not the
  library. So the tool sources the driver, as its own suite does
  (`tools/unattended/unattended.sh@eb567029:43`, "SOURCED, it defines and returns"), and copies none
  of them.
- **Item 8.** The routed-commits leg does not read a merge commit
  (`tools/memory-tree/routed_commits.py@5e29003b:6`). The subject naming the unit is for a reader of
  the log; the leg grades the pass commit, which is a non-merge parent.
- **Items 1 to 3, a consequence they do not state.** In a pass tree, `--check-commit` grades
  nothing: it finds the run by grepping run-state files for the tree's own branch ref
  (`tools/unattended/unattended.sh@eb567029:14269`), and a pass branch `<run branch>-p<seq>` is no
  run's branch. Git checks a branch out in one worktree at most, so a pass tree cannot hold the run's
  branch. Check 23 still grades the pass commit at the close.
- **Item 7.** `check_gen_region_only` returns 1 when either object is absent, so a path the pass added
  or deleted is never gen-region-only and aborts the merge unless a generated output covers it.
- **The `merge=ours` rows.** On a node with `merge.ours.driver` set to `true`, as node a has, those
  paths never conflict, so the resolution never sees them and `regen.py --write` re-renders them. On a
  clone without that driver they fall back to a text merge (`.gitattributes@0b13fe87:92`);
  `.governance/instructions.lock` is not an effective generated output, so a conflict there aborts.

### Command line

```
bash <kit>/pass-tree.sh --cut <slug> --pass <unit-id>      # prints the pass tree's path
bash <kit>/pass-tree.sh --merge <slug> --pass <unit-id>    # prints the merge commit's sha
bash <kit>/pass-tree.sh --remove <slug> --pass <unit-id>   # prints nothing
```

`--pass` is `--dispatch`'s own flag name for a unit. A unit id must match the driver's
`UNIT_ID_ERE` and carry the slug as its middle field. An unknown flag, a missing value or two verbs
is exit 2 with a usage line. The tool parses its own argv; it never calls the driver's `main`.

### The run check

`check_pass_tree_run <slug>` runs `runmd_of`, refuses a missing run-state file, reads
`read_recorded_phase` and refuses `LANDED` or `ABORTED`, then calls `resolve_holder_worktree` and
refuses its 1 and 2, naming `HW_REF` and `HW_HEAD`. The recorded phase and no derived one, for
`check_commit_message`'s reason: it takes no network. The clean test is a separate function call the
cut and merge verbs make, `git status --porcelain --untracked-files=normal` printing nothing,
because both write the tree and the merge's restore removes every untracked file (§4, "Restoring").

### The names

`derive_pass_tree <unit>` leaves `PT_BRANCH` and `PT_PATH` and prints nothing:

| Name | Value | Example on node a |
|---|---|---|
| `PT_BRANCH` | `${HW_REF#refs/heads/}-p<seq>` | `branch/dazzling-jackson-b895c0-p2` |
| `PT_PATH` | `${ROOT}-p<seq>`, `ROOT` being the driver's `git rev-parse --show-toplevel` | `C:/projects/coding-governance/.claude/worktrees/dazzling-jackson-b895c0-p2` |

`-p` and never `/p`: a ref `branch/x/p2` cannot sit beside a ref `branch/x`, git keeps loose refs as
files and `branch/x` would have to be a directory. The path is the run tree's sibling, at the same
depth, so it inherits the run tree's MAX_PATH margin less the suffix. Measured on node a at base:
the longest tracked path is 129 characters, PINNED 2026-11-15 at `aebbb4a72`.
This run tree's top level is 71 characters, PINNED 2026-11-15 at `aebbb4a72`.
A pass tree's deepest tracked file reaches 206 of 260 characters, PINNED 2026-11-15 at `aebbb4a72`,
at a three-digit sequence. Where the run tree sits under `.claude/worktrees/`, the sibling does
too, which node a's `.git/info/exclude` ignores; where the run tree is the main checkout, the
sibling sits beside it, outside the repository. `add_scratch_worktree` places its scratch trees
under the common git directory instead; a pass tree is not scratch, the builder's agent works in
it, and the brief derives it from the run's tree.

### `--cut`

1. `check_pass_tree_run`, the clean test, `derive_pass_tree`.
2. The open row: `read_pass_declarations "$rel" current`, one row whose unit field is the unit, and
   `check_pass_open` over that row's anchor, unit and declared set returns 0. A unit with no row, or
   whose pass already committed, is refused, naming `--dispatch`.
3. Refuse when `git rev-parse --verify -q "refs/heads/$PT_BRANCH"` resolves, or `PT_PATH` exists,
   or `git worktree list --porcelain` names `PT_PATH`, naming which and `--merge` or `--remove`.
4. `git worktree add -q -b "$PT_BRANCH" "$PT_PATH" HEAD`; git's stderr is passed through on failure,
   with a refusal line naming the path.
5. `printf '%s\n' "$PT_PATH"`. Nothing else reaches stdout.

### `--merge`

1. `check_pass_tree_run`, the clean test, `derive_pass_tree`. Refuse a branch that does not exist,
   naming `--cut`, and a branch with no commit `HEAD` lacks (`git rev-list --count HEAD..<branch>`
   is 0), naming `--remove`.
2. `mb=$(git merge-base HEAD "$PT_BRANCH")`. Refuse when `git diff --quiet "$mb" "$PT_BRANCH" -- "$rel"`
   fails: the pass wrote the run-state file, which M6 condition 3 forbids it and which the main loop
   alone writes in this mode. Nothing has been touched yet.
3. `git merge --no-ff --no-commit -q "$PT_BRANCH"`. Exit 0 or 1 continues; any other exit runs the
   restore and refuses with git's output.
4. The conflicted set, `git diff --name-only --diff-filter=U -z`, written to a scratch file and read
   by redirect. Each path goes through `check_resolvable_path <path> <mb> <branch>`, which returns 0
   when `check_generated_output "$p" "$GENERATED_INDEXES"` admits it, the library predicate
   `TOOL-aTwinnedPass-3` adds (never an inline copy of its loop), or when
   `check_gen_region_only "$mb:$p" "$PT_BRANCH:$p"` returns 0.
5. Any path it refuses: `git merge --abort`, then refuse with exit 1, one line naming every such path:
   `pass-tree: REFUSING - <unit>'s pass and the run's branch both changed <paths>, which are neither an
   effective generated output nor a gen-region-only change, so the two passes were not disjoint; the
   merge was aborted, HEAD is <sha8> as before, and <branch> is left as it was`.
6. Every admitted path: `git checkout --ours -- "$p" && git add -- "$p"`. A failure, a path this
   side deleted for one, runs the restore and refuses naming the path.
7. `run_pass_tree_regen`, below. A failure runs the restore and refuses.
8. `git add -u`, then each path `git ls-files --others --exclude-standard -z` lists that an effective
   generated output covers is added. Any other new file is named in one stderr note and left
   untracked.
9. `git commit -q -F <scratch message>`, no `--no-verify`: subject `merge(<slug>): <unit>'s pass
   tree`, a body line naming the branch and its tip `<sha8>`, then `Pass: none`. Like the lander's
   scripted commits it carries no co-author trailer. A refused commit runs the restore and refuses,
   the hook's lines left on stderr as the hook printed them.
10. `remove_pass_tree`. A failure prints one note naming what is left and how to remove it, and the
    verb still exits 0, because the merge has landed; a later `--cut` of the unit names the leftover.
11. `git rev-parse HEAD` on stdout.

`run_pass_tree_regen` finds `regen.py` the way `run_regen` does: `resolve_python`, then
`resolve_kit_dir "$py" run-gates regen.py "$KIT_DIR"`, then the file test under `ROOT`. No python
or no kit prints the lander's two announce lines in this tool's voice on stderr and returns 0, so
the merge commits what git and the resolution left and the bar grades freshness. Otherwise
`"$py" "$ROOT/$dir/regen.py" --write`, its output on stderr less the ` · moved: none` lines, and a
non-zero exit returns 1.

### Restoring

The restore is `git reset -q --hard HEAD`, which also ends the merge, then `git clean -qfd`. It is
exact because both writing verbs required a clean tree, untracked files included, so every untracked
non-ignored file present is one this verb made. Ignored files are never touched. Step 5 uses
`git merge --abort` as the brief names, and it is exact there, because nothing but the merge has
written yet.

### `remove_pass_tree` and `--remove`

`remove_pass_tree` runs `git worktree remove --force "$PT_PATH"` then `git branch -D "$PT_BRANCH"`.
`--force`, because a pass tree may hold a builder's scratch; after a merge the branch's commits are
reachable from `HEAD`, and `--remove` refuses a branch with any commit `HEAD` lacks, so `-D` drops
no commit in either caller. `--remove` runs the run check, `derive_pass_tree`, refuses when neither
the branch nor the path exists, and refuses a branch ahead of `HEAD`, naming `--merge`. It needs no
clean run tree, since it writes nothing there. The unit's dispatch row stays open, as it does today
for a pass that never committed: re-dispatching or deferring it is the main loop's, by M6.

### The header

The comment above the first function states, in this order:

1. What the tool is and that it runs in the run's own tree, by the main loop, never in a pass tree.
2. The order, for a group the build order marks parallel: `--dispatch` and `--brief` for each unit on
   the run's branch; one records commit carrying their rows, ending `Pass: none`; `--cut` for each;
   one unit-harness call per unit, concurrently, each with `tree` set to the path `--cut` printed and
   `writes` set to the paths that unit's `--dispatch` declared, space-separated; then, in turn,
   `--merge` for each pass that returned `committed: true` and `--remove` for each that did not.
3. Why the main loop and not the builder records the dispatch and brief rows: both write the
   run-state file, and `--merge` refuses a pass branch that changed it.
4. The names and their MAX_PATH reason, the resolution rule, the restore, and the `Pass: none`
   trailer with what it buys: `pass_commit` and check 23 read the builder's commit on the second
   parent and skip the merge.
5. What it does not check: §4, "What the design does not check", condensed.

No line spells the kit's own install prefix: the install-prefix leg refuses a kit file naming its own
directory, so the header writes `<kit>/pass-tree.sh`.

### The suite

`tools/unattended/pass-tree.test.sh`, `set -u`, finds the tool from its own directory, builds
everything under one `mktemp -d` removed on exit, and ends `PASS (<n> assertions)` or
`FAIL (<n> assertions)` with exit 1. Under `FOREIGN_PREFIX_PROBE=1` it stops after its first arm
that runs the tool, printing `foreign-prefix-probe: stopped after 1 arm`, as every declared suite does.

The fixture repository, `<tmp>/r` on branch `run`, holds:

- `.unattended.conf` in the shape of `tools/unattended/unattended.test.sh`'s `mkconf`, so
  `load_driver_conf` loads it with no refusal and no NOTE.
- The run-state file `RUN.md` of a build `tRun`, with a `## Run facts` section holding
  `phase: BUILDING` and `run-branch: refs/heads/run`, and one hand-written dispatch row per unit,
  in the grammar `read_pass_declarations` reads, anchored at the fixture commit: `TOOL-tRun-2`
  declaring `p2.txt`, `-3` `p3.txt`, `-4` `p4.txt`, `-5` `p5.txt`, `-7` `p7.txt` and `-8` `p8.txt`.
  `TOOL-tRun-6` has no row.
- A fixture kit at the suite's own tool-root prefix, derived from the suite's directory and never
  typed, whose `kit.toml` holds one `[[generated]]` row for `fx-out.txt` with `write`, `check` and
  `stage`, and its generator `render.sh`: it writes the sorted list of tracked `p*.txt` files into
  `fx-out.txt` and into a `<!-- gen:fx -->` region of `README.md`, and with `--check` compares. With
  `FX_RENDER_FAIL` set, the write first creates the new file `fx-partial.txt` and both modes exit 1,
  so a failed regeneration leaves an untracked file the restore must remove. One row serves both
  readers: `resolve_generated_indexes` and `regen.py` read the same `[[generated]]` tables.
- A copy of `regen.py`, and what it imports, at the run-gates kit's place under that prefix, since
  `run_pass_tree_regen` resolves the kit relative to the real kit and tests the file under the
  fixture's top level.

A pass is simulated, never built: the suite commits in the pass tree with `Pass: <unit>`, after
writing its product file and running `render.sh` there, so passes 2 and 3 each rewrite `fx-out.txt`
and the README region differently from one tip.

| Arm | What it does | Criterion |
|---|---|---|
| T1 | `--cut` 2 and 3; stdout, branch, path, `HEAD` of each tree | AC1 |
| T2 | the cut refusals: another branch checked out, an untracked file, `TOOL-tRun-6`, a second `--cut` of 2 | AC2 |
| T3 | pass 2 and pass 3 commit; `--merge` 2 then 3; parents, regenerated output, subject, trailer, trees gone, `pass_commit` | AC3, AC8 |
| T4 | `--cut` 4 from the same tip as 2, pass 4 writes `p2.txt`; `--merge` 4 after 2 | AC4 |
| T5 | the merge refusals: not the run's tree, dirty, `TOOL-tRun-6` with no branch, pass 5 not ahead, pass 8 committing a `RUN.md` line | AC5 |
| T6 | pass 7 commits `p7.txt`; `--merge` 7 with `FX_RENDER_FAIL=1` | AC6 |
| T7 | `--remove` 5, cut and never committed; `--remove` 7, committed and left unmerged by T6, refused | AC7 |

Ceiling: about twenty-five tool processes, each sourcing the driver, and four regenerations of
one fixture item. A driver launch measured about 1.16 s, PINNED by TOOL-aQuenchedHarness-10
(`tools/unattended/unattended.sh@eb567029:15430`).
The suite's row declares 300 s, an ESTIMATE PINNED 2026-11-15, which the close's run confirms.

### Kit wiring

- `tools/unattended/kit.toml`: `pass-tree.test.sh` joins the `project-owned` include list beside
  `check-arms-groups.test.sh`. It is not the sibling of a gate (the tool defines no `fail` helper), so
  the arm-bearing exception does not reach it, and it is withheld like the kit's other non-gate suites.
- `tools/unattended/README.md`: one paragraph after the commit-msg hook paragraph naming
  `pass-tree.sh`, its three verbs, that it pairs with the unit harness's `tree` key and finds
  `regen.py` beside the run-gates kit, announcing a skip without it.
- `tools/run-gates/selftest-budgets.txt`: the row `unattended pass-tree selftest`, budget 300, argv
  `bash {prefix}/unattended/pass-tree.test.sh`, its note naming the estimate as above.

### Docs

The verbs guide's "Drive the build as ONE program" bullet gains one sentence after "The unit harness
then builds ONE unit per call from its brief and its spec.": "A group the build order marks parallel
may build at once, each pass in its own tree: the order is `pass-tree.sh`'s header, `--cut` before
the harness call that carries `tree` and `writes`, `--merge` or `--remove` after it." Both copies, in
one commit.

No page under `help/` describes unattended passes: the drive table renders the unit harness as one
row of a registry and names no driver verb (`help/reference/drive.md`). The docs leg grades a script
only where a page shows it, so `pass-tree.sh` owes no row, and the charter's docs rule binds a
user-facing change; this tool is driven by the main loop through the verbs guide it reads.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `pass-tree.sh`, `pass-tree.test.sh` | files | no file cell: `.lexicon.conf` declares function and type cells only; kebab as the kit's siblings |
| `cmd_cut_tree`, `cmd_merge_tree`, `cmd_remove_tree` | the verbs | `--suggest ... --as sh.function`: OK, leading `cmd`. `cmd_cut` alone was not taken, because a govkit spec names a Python `cmd_cut` |
| `check_pass_tree_run`, `check_resolvable_path` | checks | OK, leading `check` |
| `derive_pass_tree` | the names | OK, leading `derive` |
| `run_pass_tree_regen` | regeneration | OK, leading `run` |
| `remove_pass_tree` | cleanup | OK, leading `remove` |
| `print_pass_tree_refusal` | the refusal line | OK, leading `print` |
| `main` | entry | OK, reserved |
| `PT_BRANCH`, `PT_PATH` | globals | no shell-variable cell |

None of these names occurs in the tree at base, by `git grep -w`. The suite's helpers lead with a
declared verb too, so `lexicon.py --check` stays at its pin.

### Files touched (estimate)

- `tools/unattended/pass-tree.sh`
- `tools/unattended/pass-tree.test.sh`
- `tools/unattended/kit.toml`
- `tools/unattended/README.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/generated/symbols.json`

### Rollout

Live, with no switch: nothing calls the tool until a main loop does, so the default is the
serial path every run takes today. The build README requires the owner's explicit ask before
landing.

### Alternatives rejected

- **A cherry-pick of the pass commit** (F1 (b)). It rewrites the commit, so the builder's sha in its
  own ledger and log no longer names what landed, and a conflict there stops mid-pick with no
  `--abort` that names both sides.
- **The verbs in the driver** (F2 (b)). See F2.
- **Sourcing `lib-unattended.sh` alone and copying the run readers.** Two copies of "which tree
  holds this run" is the two-answers class the library exists to end.
- **`add_scratch_worktree`.** It makes a detached tree, and a pass needs a branch the merge can name;
  it lives in another kit's gov-only library; its body is one `git worktree add`.
- **Resolving every conflict to this side and letting the bar find the damage.** A product
  conflict is two passes that were not disjoint, and the brief puts that outside this tool.
- **Refusing a merge when `regen.py` cannot be found.** The unattended kit does not require the
  run-gates kit, so every adopter without it could never merge; the lander announces and continues
  for the same reason.

### What the design does not check

- A pass tree's commits are not graded by `--check-commit` (above). Check 23 grades them at the
  close, and `--merge` refuses only the run-state file and an unresolvable conflict.
- A generated output whose generator has no staged `[[generated]]` or `[[regenerate]]` row,
  `.claude/agents` and `.claude/roles.json` today, is resolved to this side and not re-rendered. The
  `roles render wiring` leg reds that state at the bar. The same holds for a gen region no staged
  item renders: the pass's half of it is dropped, and only that region's own check sees it.
- A hand edit inside a gen region is not told from a render, as `check_gen_region_only` says of itself.
- Two passes that changed one path compatibly and merged with no conflict are not looked at: the
  conflict set is what git leaves, and regeneration then re-renders every generated output.
- A path the `merge=ours` attribute takes on a node with the driver set keeps this side's bytes
  without a conflict, which is what that attribute is for.
- Check 39 of the kit gate grades phase reads in the driver alone, so this tool's
  `read_recorded_phase` call is outside its population. check-arms does not discover the tool,
  because it defines no `fail` helper; its suite arms each refusal instead.
- Two slugs whose runs name one branch would derive one pass branch for two units sharing a
  sequence number. `--cut` refuses the second, naming the first.
- A Windows process holding a file in a pass tree makes `git worktree remove` fail; the note names
  the path, and the branch is then not deleted either.
- How many passes run at once.

## 5. Production-readiness checklist

- security — no new input beyond a slug and a unit id, both shape-checked against the driver's own
  patterns; every git call is argv, never `eval`; no `--no-verify`; deny by default on every
  conflict the two rules do not admit; the restore removes only files a verb that required a clean
  tree made.
- perf / scale — one driver source per call; one `regen.py --write` per merge, whose wall on node a
  this unit does not pin; AC11 measures the whole serial and parallel routes.
- error / empty / loading states — every refusal is one stderr line, exit 1, with the tree as it was;
  a missing `regen.py` is announced; a failed cleanup after a landed merge is a note, exit 0.
- observability — the merge subject names the unit; the body names the pass branch and tip; regen's
  moved items reach stderr.
- risks — a regeneration that rewrites a file the passes did not touch lands in the merge commit;
  the pass tree's `--check-commit` gap; MAX_PATH on a deeper run tree.
- testing — AC1 to AC11 and the `New arm:` lines of §7.
- migration — N/A: no record shape or conf key moves.
- user docs — the verbs guide (S12); no `help/` page owed (§4, "Docs").

## 6. Acceptance criteria

- **AC1** — When `bash pass-tree.sh --cut tRun --pass TOOL-tRun-2` runs in the fixture's run tree,
  stdout is one line, the fixture top level followed by `-p2`, absolute and free of a backtick;
  `git -C <that path> symbolic-ref HEAD` prints `refs/heads/run-p2`; its `git rev-parse HEAD` equals
  the run tree's.
  Red when: stdout carries a second line, or the branch or path is spelled other than §4 derives it.
  fixture: the suite's fixture repository, built under one `mktemp -d`; the tree holds none.
- **AC2** — When `--cut` runs with another branch checked out, with an untracked file present, for
  `TOOL-tRun-6`, which has no dispatch row, and for `TOOL-tRun-2` a second time, each exits 1 with
  one `pass-tree: REFUSING` line on stderr, the last naming the existing path, and
  `git worktree list --porcelain` and `git branch --list 'run-p*'` print what they printed before.
  Red when: any of the four creates a tree or a branch, or exits 0.
  fixture: as AC1.
- **AC3** — When passes 2 and 3, cut from one tip, each commit their own product file and both
  rewrite `fx-out.txt` and the README's `gen:fx` region, and `--merge` runs for 2 then 3, each exits
  0 with one sha on stdout; `git rev-parse <sha>^2` is that pass's commit; `fx-out.txt` lists
  `p2.txt` and `p3.txt`, as `render.sh --check` confirms; the subject reads
  `merge(tRun): TOOL-tRun-3's pass tree`; `git log -1 --format='%(trailers:key=Pass,valueonly)'`
  prints `none`; neither pass tree nor branch remains; `git status --porcelain` prints nothing.
  Red when: the merge fast-forwards, either conflict is left unresolved, the output is not
  re-rendered, or the trailer is missing.
  fixture: as AC1.
- **AC4** — When pass 4, cut from the same tip as pass 2, commits its own `p2.txt` and `--merge` runs
  for 4 after 2 has merged, it exits 1, its stderr names `p2.txt` and does not name `fx-out.txt`,
  `HEAD` is the pre-merge sha, `git status --porcelain` prints nothing, `git rev-parse -q --verify
  MERGE_HEAD` fails, and branch `run-p4` still exists.
  Red when: the conflict is resolved, the abort leaves a merge in progress or a staged path, or the
  pass's branch is deleted.
  fixture: as AC1.
- **AC5** — When `--merge` runs from a tree on another branch, with an untracked file present, for a
  unit with no pass branch, for a branch with no commit beyond `HEAD`, and for a branch whose commit
  wrote the fixture's `RUN.md`, each exits 1 with one `pass-tree: REFUSING` line and `HEAD` and
  `git status --porcelain` are unchanged.
  Red when: any of the five merges, or leaves the tree changed.
  fixture: as AC1.
- **AC6** — When `--merge` runs with `FX_RENDER_FAIL=1` in its environment over a pass whose merge
  would succeed, it exits 1, `HEAD` is the pre-merge sha, `git status --porcelain` prints nothing,
  `fx-partial.txt` is absent, and no `MERGE_HEAD` remains.
  Red when: the merge commits without its regeneration, or the restore leaves `fx-partial.txt` or a
  merge in progress.
  fixture: as AC1.
- **AC7** — When pass 5 is cut and never commits, `bash pass-tree.sh --remove tRun --pass
  TOOL-tRun-5` exits 0 and neither `run-p5` nor its path remains; when a pass branch holds a commit
  `HEAD` lacks, `--remove` exits 1 naming `--merge` and the branch remains.
  Red when: `--remove` drops a committed pass, or leaves the tree or branch of an uncommitted one.
  fixture: as AC1.
- **AC8** — When, after AC3, a subshell sources `tools/unattended/lib-unattended.sh` in the fixture
  and calls `pass_commit <anchor> TOOL-tRun-2 <run-state file>`, it prints pass 2's commit
  and not the merge; and `bash tools/unattended/unattended.sh --check-commit` over a file holding the
  merge's message exits 0.
  Red when: the merge carries no `Pass: none`, so the walk names it, or the second parent is not the
  pass commit, so the walk finds none.
  fixture: as AC1.
- **AC9** — When `grep` runs over `pass-tree.sh`, its header names `--dispatch`, `--brief`, `tree`,
  `writes`, `Pass: none`, `--cut`, `--merge` and `--remove` above its first function, and
  `grep -c 'tools/unattended'` over it prints 0; `grep -c "pass-tree.sh"` prints 1 for each of
  `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, and the comparison
  below prints nothing.
  ```
  diff <(tail -n +2 tools/unattended/VERBS.template.md) <(tail -n +2 memory/guides/UNATTENDED-VERBS.md)
  ```
  Red when: the header omits the order or a key, spells the kit's prefix, or the two guide copies differ.
- **AC10** — When `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` runs for each
  function of §4's inventory, each prints a line opening `OK`; `memory/map/generated/symbols.json`
  carries an entry for each; `grep -c "pass-tree.test.sh"` prints at least 1 over
  `tools/unattended/kit.toml` and over `tools/run-gates/selftest-budgets.txt`, the first inside the
  `project-owned` include list; and `grep -c "pass-tree.sh"` over
  `tools/unattended/README.md` prints at least 1.
  Red when: a name the lexicon refuses lands, the index is not regenerated, or the suite ships to
  adopters or has no budget row.
- **AC11** — When the main loop builds two disjoint units of one build through
  `tools/workflows/unattended-unit.js` serially in one tree, and the same two in parallel with `tree`,
  `--cut` and `--merge`, on one frozen clone, the record under this build's `build/` folder gives the
  wall clock of each phase of each route and the two totals.
  Red when: the record lacks a phase or a route, or the clone moved between the routes.
  cost: two builds of two units each, PINNED 2026-11-15 at 15 to 50 minutes a unit by the brief.
  permission: the main loop's, at the close; a pass runs no harness.
  figure: every wall time is DERIVED by the measurement; the record states its node and base.

## 7. Gates

`lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `policy fixtures` · `install-prefix self-test` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `unattended skill wiring` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/unattended/pass-tree.test.sh · covers AC1 AC2 · base aebbb4a72, which has no tool, so every arm's run exits 127; and the tool with `derive_pass_tree` spelling `/p<seq>`, which `git worktree add` refuses beside the run's branch · none
New arm: tools/unattended/pass-tree.test.sh · covers AC3 AC8 · the tool with `--no-ff` dropped, which fast-forwards pass 2 so `<sha>^2` does not resolve; and with the `Pass: none` line dropped, so `pass_commit` names the merge · none
New arm: tools/unattended/pass-tree.test.sh · covers AC4 · the tool with `check_resolvable_path` returning 0 for every path, which resolves `p2.txt` and exits 0 · none
New arm: tools/unattended/pass-tree.test.sh · covers AC5 · the tool with the run-state diff refusal removed, which merges the branch that wrote `RUN.md` · none
New arm: tools/unattended/pass-tree.test.sh · covers AC6 · the tool with the restore's `git clean -qfd` removed, which leaves `fx-partial.txt` behind · none
New arm: tools/unattended/pass-tree.test.sh · covers AC7 · the tool with the ahead refusal removed from `--remove`, which drops a committed pass · none

The close's run of `pass-tree.test.sh` re-observes every arm; no existing suite's arm moves, and
`tools/unattended/unarmed-branches.txt` is not touched because the tool defines no `fail` helper.

## 8. Open questions

- **F1 — Does `--merge` merge `--no-ff`, or cherry-pick the pass commit?** (a) `git merge --no-ff`:
  the builder's commit and its `Pass:` trailer stay reachable unchanged on the second parent, which
  `pass_commit` walks with no `--first-parent`, and `git merge --abort` restores an exact state.
  (b) A cherry-pick: a linear history, but the pass commit is rewritten, its sha in the builder's
  ledger names nothing on the run's branch, and a conflict leaves a half-applied pick.
  Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F2 — Do the verbs live in their own file, or in the driver?** (a) Their own file,
  `pass-tree.sh`, sourcing the driver for its readers: no driver verb set, verb carrier or driver suite
  moves, and the live dDeclaredLoop branch, which rewrote driver functions, meets no new hunk in the
  driver. The cost is that check 39 and check-arms do not see the file. (b) Two driver verbs: check
  39 grades the phase read and check-arms the refusals, but the verb set, the help text, the verbs
  guide's per-verb contract and the driver suite's shards all move, in a build whose README holds the
  unattended suites to the arms it adds. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F3 — What takes away the tree and branch of a pass that returned `committed: false`?**
  (a) A third verb, `--remove`, sharing `remove_pass_tree` with `--merge` and refusing a committed
  pass. (b) `--merge` itself, which on a branch not ahead of `HEAD` removes both and exits with a
  code of its own: one verb fewer, but a refusal and a cleanup share one exit path. (c) By hand, the
  header printing the two git commands: the names are then spelled twice. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

The seams this unit extends: the driver's own readers, reached by sourcing `unattended.sh` and calling
`load_driver_conf` as its suite does (`fact`, `read_recorded_phase`, `resolve_holder_worktree`,
`check_pass_open`, the effective `GENERATED_INDEXES`); the library's `covers`,
`check_gen_region_only` and `read_pass_declarations`; and the run-gates kit's `regen.py --write`,
found as `run_regen` and `derive_spec_token_key` find a sibling kit's file, through
`resolve_kit_dir`. `tools/codebase-map/reuse_lookup.py "cut a git worktree on a new branch for one
pass and merge it back no-ff resolving generated outputs and regenerating"` ranked `git`, `resolve`,
`resolve_kit_dir`, `merge`, `run_git` and `resolve_python` first, then `resolve_generated_indexes`
and `add_scratch_worktree`. `resolve_kit_dir`, `resolve_python` and `resolve_generated_indexes` are
reused as named; `merge` is the row driver's and the settings merger's, which merge file contents,
not branches; `add_scratch_worktree` makes a detached tree in another kit's gov-only library, so no
existing seam fits the cut or the merge themselves, and they are new code beside the readers they
call.

Recall terms used: `python tools/memory-recall/query.py "how were concurrent passes merged back into
the run branch with generated indexes re-rendered" --terms "wave worktree merge no-ff generated
indexes regen gen region pass_commit Pass trailer dispatch parallel M6 dDerivedDocket"`
