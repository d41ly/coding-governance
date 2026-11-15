# TOOL-aTwinnedPass-2 — the pass-tree tool: merge a pass's own branch back `--no-ff` with generated outputs re-rendered, or take it away

**Status:** INPROGRESS · rev-2 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 2 · closes TOOL-dDerivedDocket-57

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aTwinnedPass-2-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aTwinnedPass-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md) | research | TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-3 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md) | research | TOOL-aTwinnedPass-1 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-2-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-2-4-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-4-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-2-5-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-5-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-2-pass-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-pass-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A main loop can build two or more disjoint units of one build at once only if each builder has its
own git index and the main loop can bring every pass back without a hand merge. The runtime gives
each builder its own worktree and branch (`TOOL-aTwinnedPass-1` asks for it with
`isolation: 'worktree'` and resets it to the commit the pass was dispatched from). This unit ships
one kit tool, `tools/unattended/pass-tree.sh`, run by the main loop in the run's own tree, whose
`--merge` verb merges such a branch back `--no-ff`, resolves only the conflicts a regeneration
answers, re-renders the generated outputs with the run-gates kit's `regen.py --write`, commits a
merge whose second parent is the builder's own pass commit, and then takes the pass's worktree and
branch away; and whose `--remove` verb takes away those of a pass that committed nothing.

## 2. Scope (IN)

- **S1** — A new file `tools/unattended/pass-tree.sh`, run by the main loop in the run's own tree. It
  sources the driver `unattended.sh` beside it, which sources `lib-unattended.sh`, calls
  `load_driver_conf`, and dispatches one of two verbs:
  `--merge <slug> --pass <unit> --branch <branch> --from <sha>` and
  `--remove <slug> --branch <branch>` (F2 (a), F3 (a), F4 (a)). Exit 0 done, 1 a named refusal on
  stderr, 2 misconfigured. Observed by AC1, AC3, AC5.
  **Readers:** by name: none, since this item adds a tool and withdraws no name; the worktree and
  branch it takes away are the pass's own, named only by the unit harness's return · by value:
  NO VALUE READERS, the pass's worktree and branch exist only between the harness call and this verb.
- **S2** — One run check both verbs make first, `check_pass_tree_run`: the run-state file of the
  slug exists, its recorded phase is neither `LANDED` nor `ABORTED`, and `resolve_holder_worktree`
  says this tree has the run's branch checked out, as `check_commit_message` reads the binding.
  `--merge` also requires the tree clean: `git status --porcelain` prints nothing, untracked files
  included. Observed by AC3.
- **S3** — One branch check both verbs make, `check_pass_branch <branch>`: `git check-ref-format
  --branch` admits the name, and it is not the run's own branch (`HW_REF`). It leaves `PT_BRANCH`.
  Whether the branch exists is each verb's own question (§4). Observed by AC3, AC5.
- **S4** — `--merge` refuses, before it writes anything, a branch that does not exist, a branch with
  no commit `HEAD` lacks, a `--from` that is not 7 to 40 lowercase hex digits naming a commit, a
  branch whose merge base with `HEAD` is not that commit, and a branch that changed the run-state
  file since that merge base. Observed by AC3.
- **S5** — `--merge` runs `git merge --no-ff --no-commit <branch>`, resolves to this side each
  conflicted path that `check_resolvable_path` admits, and on any other conflicted path runs
  `git merge --abort` and refuses with exit 1 naming every such path. Observed by AC1, AC2.
- **S6** — After resolution `--merge` runs `run_pass_tree_regen`, stages every tracked change and
  every new file under an effective generated output, and commits the subject
  `merge(<slug>): <unit>'s pass tree` with a `Pass: none` trailer, hooks running. It then removes the
  worktree that holds the branch, found through `derive_holder_where`, and deletes the branch,
  through `remove_pass_tree`, and prints the merge sha alone on stdout. Observed by AC1, AC6.
  **Readers:** by name: none, since this item adds a tool and withdraws no name; the worktree and
  branch it takes away are the pass's own, named only by the unit harness's return · by value:
  NO VALUE READERS, the pass's worktree and branch exist only between the harness call and this verb.
- **S7** — A failure after the merge started and before its commit landed, a regeneration or a
  commit refusal, restores the tree to the pre-merge `HEAD` with nothing staged, no merge in
  progress and no new file, through `remove_merge_attempt`, and refuses with exit 1. Observed by AC4.
- **S8** — `--remove` takes away the worktree and branch of a pass that returned `committed: false`.
  It refuses a branch holding a commit no other branch, remote-tracking ref or tag holds, naming
  `--merge`; a branch that no longer exists is a stderr note and exit 0. Observed by AC5.
  **Readers:** by name: none, since this item adds a tool and withdraws no name; the worktree and
  branch it takes away are the pass's own, named only by the unit harness's return · by value:
  NO VALUE READERS, the pass's worktree and branch exist only between the harness call and this verb.
- **S9** — The tool's header states the order the main loop runs it in, the unit-harness keys it
  pairs with, `TOOL-aTwinnedPass-1`'s commit key and `writes`, and what it does not check (§4,
  "The header"). Observed by AC7.
- **S10** — The suite `tools/unattended/pass-tree.test.sh`, over a fixture repository, with the arms
  of §4, "The suite". Observed by AC1 to AC6 through the `New arm:` lines of §7.
- **S11** — The kit names the tool: `tools/unattended/kit.toml` withholds the suite from
  `govkit apply` beside the kit's other non-gate suites, `tools/unattended/README.md` names the tool
  and its pairing with the unit harness, and `tools/run-gates/selftest-budgets.txt` carries the
  suite's row. Observed by AC8.
- **S12** — The verbs guide's "Drive the build as ONE program" bullet names the parallel route, in
  `tools/unattended/VERBS.template.md` and its copy `memory/guides/UNATTENDED-VERBS.md`, byte-equal
  past line 1. Observed by AC7.
- **S13** — `memory/map/generated/symbols.json` regenerated with `gen_map.py --write`, carrying the
  new functions. Observed by AC8.
- **S14** — A measured before and after: two disjoint units built serially through the unit harness in
  one tree, against the same two built in parallel through the harness's commit key and `--merge`,
  on a frozen clone, wall clock per phase, recorded by the main loop under this build's `build/`
  folder. Observed by AC9.

## 3. Non-goals (OUT)

- Making a pass's worktree or branch. The runtime makes both for an `agent()` call carrying
  `isolation: 'worktree'`, and `TOOL-aTwinnedPass-1` asks for it and resets it. This tool never
  spells the runtime's names or places, and reads only the branch the harness returned.
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
- **consumes-from** `TOOL-aTwinnedPass-1` — the unit harness's commit key, whose value is this tool's
  `--from`, its `writes` key, and the pass branch its return carries, which is this tool's
  `--branch`. This tool's header documents the key under the name that unit's spec gives it. Without
  that unit a builder never works on a branch of its own, and nothing hands this tool one.

## 4. Design

### Evidence

Read at base `aebbb4a72`; every blob below is the same at the build's tip `96d5e73e4`.

| Citation | What sits there |
|---|---|
| `tools/unattended/unattended.sh@eb567029:43` | "SOURCED, it defines and returns": a sourcing caller gets the driver's functions |
| `tools/unattended/unattended.sh@eb567029:99` | `KIT_DIR`, derived from the driver's own path, so a sourcing tool gets the driver's kit directory |
| `tools/unattended/unattended.sh@eb567029:638` | `load_driver_conf`: cds to the top level, loads `.unattended.conf`, exits 2 on a refusal |
| `tools/unattended/unattended.sh@eb567029:890` | `GENERATED_INDEXES=$(resolve_generated_indexes ...)`: the effective `index:generator` pairs |
| `tools/unattended/unattended.sh@eb567029:1177` | `UNIT_ID_ERE`, the unit-id shape |
| `tools/unattended/unattended.sh@eb567029:1573` | `fact`, the `## Run facts` reader |
| `tools/unattended/unattended.sh@eb567029:1840` | `read_recorded_phase` |
| `tools/unattended/unattended.sh@eb567029:8954` | `resolve_holder_worktree`: `run-branch`, else `branch-ref`, against `git symbolic-ref -q HEAD`; leaves `HW_REF` |
| `tools/unattended/unattended.sh@eb567029:9304` | `derive_holder_where`: reads `HW_REF`, prints the path `git worktree list --porcelain` shows with that ref checked out, else one of two fixed remedy sentences |
| `tools/unattended/unattended.sh@eb567029:14271` | `check_commit_message` skips a `LANDED` or `ABORTED` record, then asks `resolve_holder_worktree` at `tools/unattended/unattended.sh@eb567029:14272` |
| `tools/unattended/unattended.sh@eb567029:14311` | `check_commit_message` returns 0 on a `Pass: none` trailer before reading anything else |
| `tools/unattended/unattended.sh@eb567029:14352` | the generated exemption, `covers "${q%%:*}" "$p"` over `GENERATED_INDEXES` |
| `tools/unattended/unattended.sh@eb567029:14444` | `derive_spec_token_key` finds a run-gates file with `resolve_kit_dir "$2" run-gates <file> "$KIT_DIR"` |
| `tools/unattended/unattended.sh@eb567029:15540` | a sourced driver returns before `main` |
| `tools/unattended/lib-unattended.sh@a3e03db6:62` | `GIT`, the pinned git wrapper every driver read goes through |
| `tools/unattended/lib-unattended.sh@a3e03db6:746` | `covers`; `overlaps` at `tools/unattended/lib-unattended.sh@a3e03db6:751` |
| `tools/unattended/lib-unattended.sh@a3e03db6:839` | `resolve_generated_indexes`: the kits' `[[generated]]` rows, then the conf's pairs |
| `tools/unattended/lib-unattended.sh@a3e03db6:1027` | `pass_commit`: walks `<anchor>..HEAD` with no `--first-parent`, skips a `Pass: none` commit |
| `tools/unattended/lib-unattended.sh@a3e03db6:1154` | `check_gen_region_only <before> <after>`: returns 1 unless both objects exist |
| `tools/push-main.sh@c7cd70b9:851` | `resolve_lander_kit`: `resolve_python`, `resolve_kit_dir`, then the file test under the top level |
| `tools/push-main.sh@c7cd70b9:902` | `run_regen`: no python or no kit announces and returns 0; a failed `--write` returns 1 |
| `tools/run-gates/regen.py@07644e72:320` | a `[[regenerate]]` row with no `stage` is skipped and announced, so `--write` never re-renders it |
| `tools/memory-tree/routed_commits.py@5e29003b:6` | the routed-commits leg grades non-merge commits; `tools/memory-tree/routed_commits.py@5e29003b:60` says a merge's own content is not graded |
| `tools/hooks/scratch-guard.js@7c31933f:784` | `checkOriented` returns null when `agent_id` is present: a subagent's commit is not orientation-gated |
| `.gitattributes@0b13fe87:94` | the `merge=ours` rows: `memory/LIVE.md`, the ledger, the gotchas index, the as-built view at `.gitattributes@0b13fe87:104`, `.governance/instructions.lock` at `.gitattributes@0b13fe87:108` |

### What the brief says that the code does not

- **R4, `check_generated_output`.** No function of that name is at base. `TOOL-aTwinnedPass-3` adds
  it to the library (its S1), hence the edge above; this unit builds after it, at order 2.
- **R4, "found by `git worktree list --porcelain`".** The driver already derives a worktree from a
  branch over exactly that output, `derive_holder_where`, for `HW_REF`. The tool sets `HW_REF` local
  to `remove_pass_tree` and calls it, rather than writing a second awk over the porcelain. Its two
  remedy sentences are never a directory, so `[ -d ]` on its line tells a path from "none holds it".
- **R2.** The runtime's worktree place and branch name are observed, not code here; the tool takes
  the branch the harness returned and finds the worktree from it.
- **Item 5.** The two lib predicates are not all the tool needs. The run check needs `fact`,
  `read_recorded_phase` and `resolve_holder_worktree`, the cleanup `derive_holder_where`, and the
  effective generated set `load_driver_conf`; all five are in the driver, not the library. So the
  tool sources the driver, as its own suite does (`tools/unattended/unattended.sh@eb567029:43`), and
  copies none of them.
- **Item 8.** The routed-commits leg does not read a merge commit
  (`tools/memory-tree/routed_commits.py@5e29003b:6`). The subject naming the unit is for a reader of
  the log; the leg grades the pass commit, which is a non-merge parent.
- **A consequence R3 does not state.** In a pass's worktree, `--check-commit` grades nothing: it
  finds the run by grepping run-state files for the tree's own branch ref
  (`tools/unattended/unattended.sh@eb567029:14269`), and the runtime's branch is no run's branch. Git
  checks a branch out in one worktree at most, so a pass's worktree cannot hold the run's branch.
  Check 23 still grades the pass commit at the close.
- **Item 7.** `check_gen_region_only` returns 1 when either object is absent, so a path the pass added
  or deleted is never gen-region-only and aborts the merge unless a generated output covers it.
- **The `merge=ours` rows.** On a node with `merge.ours.driver` set to `true`, as node a has, those
  paths never conflict, so the resolution never sees them and `regen.py --write` re-renders them. On a
  clone without that driver they fall back to a text merge (`.gitattributes@0b13fe87:92`);
  `.governance/instructions.lock` is not an effective generated output, so a conflict there aborts.

### Command line

```
bash <kit>/pass-tree.sh --merge <slug> --pass <unit-id> --branch <branch> --from <sha>   # prints the merge commit's sha
bash <kit>/pass-tree.sh --remove <slug> --branch <branch>                              # prints nothing
```

`--pass` is `--dispatch`'s own flag name for a unit. A unit id must match the driver's
`UNIT_ID_ERE` and carry the slug as its middle field. An unknown flag, a missing value, a flag the
verb does not take, or two verbs is exit 2 with a usage line. The tool parses its own argv; it never
calls the driver's `main`.

### The run check and the branch check

`check_pass_tree_run <slug>` runs `runmd_of`, refuses a missing run-state file, reads
`read_recorded_phase` and refuses `LANDED` or `ABORTED`, then calls `resolve_holder_worktree` and
refuses its 1 and 2, naming `HW_REF` and `HW_HEAD`. The recorded phase and no derived one, for
`check_commit_message`'s reason: it takes no network. The clean test is a separate call `--merge`
makes, `git status --porcelain --untracked-files=normal` printing nothing, because the merge's
restore removes every untracked file (§4, "Restoring"). `--remove` writes nothing in this tree and
needs no clean test.

`check_pass_branch <branch>` refuses a name `git check-ref-format --branch` refuses, a leading `-`
included, and a name whose `refs/heads/` form is `HW_REF`, then sets `PT_BRANCH`. It does not test
existence: `--merge` refuses an absent branch, and `--remove` notes it.

### `--merge`

1. `check_pass_tree_run`, the clean test, `check_pass_branch`. Refuse a branch
   `git rev-parse --verify -q "refs/heads/$PT_BRANCH"` does not resolve, and a branch with no commit
   `HEAD` lacks (`git rev-list --count HEAD..<branch>` is 0), naming `--remove`.
2. `--from`: refuse unless it matches `^[0-9a-f]{7,40}$` and `git rev-parse --verify -q
   "<from>^{commit}"` resolves; `PT_FROM` is the full sha. `mb=$(git merge-base HEAD "$PT_BRANCH")`.
   Refuse when `mb` is not `PT_FROM`: `pass-tree: REFUSING - <unit>'s branch <branch> forks from
   <mb8>, not from <from8>, the commit it was dispatched from: its builder did not reset its worktree
   to that commit, so the merge would carry another line's history in`.
3. Refuse when `git diff --quiet "$mb" "$PT_BRANCH" -- "$rel"` fails: the pass wrote the run-state
   file, which M6 condition 3 forbids it and which the main loop alone writes in this mode. Nothing
   has been touched yet.
4. `git merge --no-ff --no-commit -q "$PT_BRANCH"`. Exit 0 or 1 continues; any other exit runs the
   restore and refuses with git's output.
5. The conflicted set, `git diff --name-only --diff-filter=U -z`, written to a scratch file and read
   by redirect. Each path goes through `check_resolvable_path <path> <mb> <branch>`, which returns 0
   when `check_generated_output "$p" "$GENERATED_INDEXES"` admits it (never an inline copy of its
   loop), or when `check_gen_region_only "$mb:$p" "$PT_BRANCH:$p"` returns 0.
6. Any path it refuses: `git merge --abort`, then refuse with exit 1, one line naming every such path:
   `pass-tree: REFUSING - <unit>'s pass and the run's branch both changed <paths>, which are neither an
   effective generated output nor a gen-region-only change, so the two passes were not disjoint; the
   merge was aborted, HEAD is <sha8> as before, and <branch> is left as it was`.
7. Every admitted path: `git checkout --ours -- "$p" && git add -- "$p"`. A failure, a path this
   side deleted for one, runs the restore and refuses naming the path.
8. `run_pass_tree_regen`, below. A failure runs the restore and refuses.
9. `git add -u`, then each path `git ls-files --others --exclude-standard -z` lists that an effective
   generated output covers is added. Any other new file is named in one stderr note and left
   untracked.
10. `git commit -q -F <scratch message>`, no `--no-verify`: subject `merge(<slug>): <unit>'s pass
    tree`, a body line naming the branch, its tip `<sha8>` and `--from` `<sha8>`, then `Pass: none`.
    Like the lander's scripted commits it carries no co-author trailer. A refused commit runs the
    restore and refuses, the hook's lines left on stderr as the hook printed them.
11. `remove_pass_tree`. A failure prints one note naming what is left and the `--remove` call that
    takes it away, and the verb still exits 0, because the merge has landed.
12. `git rev-parse HEAD` on stdout.

`run_pass_tree_regen` finds `regen.py` the way `run_regen` does: `resolve_python`, then
`resolve_kit_dir "$py" run-gates regen.py "$KIT_DIR"`, then the file test under `ROOT`. No python
or no kit prints the lander's two announce lines in this tool's voice on stderr and returns 0, so
the merge commits what git and the resolution left and the bar grades freshness. Otherwise
`"$py" "$ROOT/$dir/regen.py" --write`, its output on stderr less the ` · moved: none` lines, and a
non-zero exit returns 1.

### Restoring

`remove_merge_attempt` is `git reset -q --hard HEAD`, which also ends the merge, then
`git clean -qfd`. It is exact because `--merge` required a clean tree, untracked files included, so
every untracked non-ignored file present is one this verb made. Ignored files are never touched,
and a single `-f` never enters a nested repository. Step 6 uses `git merge --abort` as the brief
names, and it is exact there, because nothing but the merge has written yet.

### `remove_pass_tree` and `--remove`

`remove_pass_tree` sets `HW_REF` local to itself to `refs/heads/$PT_BRANCH` and reads one line from
`derive_holder_where`. When that line is a directory, it runs `git worktree remove --force` on it;
then `git branch -D "$PT_BRANCH"`. `--force`, because a pass's worktree may hold a builder's scratch;
a branch whose worktree the runtime already took away is deleted all the same.

`--remove` runs the run check and `check_pass_branch`. A branch that does not resolve prints one
stderr note naming it, that no worktree can hold an absent branch, and exits 0: the runtime takes
away a worktree it judges unchanged (R2), so an absent branch is an expected end, and the note keeps
a mistyped name visible. A branch holding a commit no other ref holds,
`git rev-list --count "refs/heads/$PT_BRANCH" --not --exclude="$PT_BRANCH" --branches --remotes
--tags` above 0, is refused naming `--merge`, so `-D` never drops a pass's work. A branch whose
builder skipped the reset sits at the default branch's tip, which that branch holds, so it is taken
away; after a merge, `--merge`'s own call finds every commit reachable from `HEAD`. The unit's
dispatch row stays open, as it does today for a pass that never committed: re-dispatching or
deferring it is the main loop's, by M6.

### The header

The comment above the first function states, in this order:

1. What the tool is and that it runs in the run's own tree, by the main loop, never in a pass's
   worktree.
2. The order, for a group the build order marks parallel: `--dispatch` and `--brief` for each unit on
   the run's branch; one records commit carrying their rows and brief files, ending `Pass: none`; one
   `unattended-unit.js` call per unit, concurrently, each with the commit key, under the name
   `TOOL-aTwinnedPass-1`'s spec gives it, set to that records commit's sha, and `writes` set to the
   paths that unit's `--dispatch` declared, space-separated; then, in turn, `--merge` for each pass
   that returned `committed: true`, with `--branch` the branch its return carries and `--from` the
   same sha, and `--remove` for each that did not.
3. Why the main loop and not the builder records the dispatch and brief rows: both write the
   run-state file, and `--merge` refuses a pass branch that changed it.
4. The `--from` refusal and what it catches, the resolution rule, the restore, and the `Pass: none`
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

The fixture repository, `<tmp>/r`, holds two branches. `main` carries the base commit, then one more
commit adding `m1.txt`, the default branch moving on. `run`, checked out, is cut from the base
commit and carries the records commit `C`:

- `.unattended.conf` in the shape of `tools/unattended/unattended.test.sh`'s `mkconf`, so
  `load_driver_conf` loads it with no refusal and no NOTE.
- The run-state file `RUN.md` of a build `tRun`, with a `## Run facts` section holding
  `phase: BUILDING` and `run-branch: refs/heads/run`, and one hand-written dispatch row per unit the
  suite merges, in the grammar `read_pass_declarations` reads, anchored at the base commit.
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

A pass is simulated, never built. `add_fixture_pass <n>` does what the runtime and the builder's
first order do: `git worktree add -q -b agent-p<n> <tmp>/wt/p<n> main`, then `git reset -q --hard C`
in it; `add_fixture_pass <n> noreset` stops before the reset. The suite then commits in that
worktree with `Pass: TOOL-tRun-<n>`, after writing its product file and running `render.sh` there,
so passes 2 and 3 each rewrite `fx-out.txt` and the README region differently from `C`.

| Arm | What it does | Criterion |
|---|---|---|
| T1 | passes 2 and 3 commit; `--merge` 2 then 3, each `--from C`; parents, regenerated output, subject, trailer, worktrees and branches gone, `pass_commit`, `--check-commit` | AC1, AC6 |
| T2 | pass 4 from `C` writes `p2.txt`; `--merge` 4 after 2 | AC2 |
| T3 | the merge refusals: a tree on another branch, an untracked file, branch `agent-none`, branch `run`, branch `-x`, pass 5 never committing, pass 8 committing a `RUN.md` line, `--from HEAD`, and pass 9 cut `noreset` and committing `p9.txt` | AC3 |
| T4 | pass 7 commits `p7.txt`; `--merge` 7 with `FX_RENDER_FAIL=1` | AC4 |
| T5 | `--remove` 5, reset and never committed; `--remove` 10, cut `noreset` and never committed; `--remove` 7, committed and left unmerged by T4, refused; `--remove agent-none` | AC5 |

Ceiling: about twenty-five tool processes, each sourcing the driver, and four regenerations of
one fixture item. A driver launch measured about 1.16 s, PINNED by TOOL-aQuenchedHarness-10
(`tools/unattended/unattended.sh@eb567029:15430`).
The suite's row declares 300 s, an ESTIMATE PINNED 2026-11-15, which the close's run confirms.

### Kit wiring

- `tools/unattended/kit.toml`: `pass-tree.test.sh` joins the `project-owned` include list beside
  `check-arms-groups.test.sh`. It is not the sibling of a gate (the tool defines no `fail` helper), so
  the arm-bearing exception does not reach it, and it is withheld like the kit's other non-gate suites.
- `tools/unattended/README.md`: one paragraph after the commit-msg hook paragraph naming
  `pass-tree.sh`, its two verbs, that it takes the branch and the commit the unit harness's commit key
  carried, and that it finds `regen.py` beside the run-gates kit, announcing a skip without it.
- `tools/run-gates/selftest-budgets.txt`: the row `unattended pass-tree selftest`, budget 300, argv
  `bash {prefix}/unattended/pass-tree.test.sh`, its note naming the estimate as above.

### Docs

The verbs guide's "Drive the build as ONE program" bullet gains one sentence after "The unit harness
then builds ONE unit per call from its brief and its spec.": "A group the build order marks parallel
may build at once, each pass on a branch of its own: `--dispatch` and `--brief` for each unit, one
records commit, then one harness call per unit carrying that commit and `writes`, run concurrently,
then `pass-tree.sh --merge` per committed pass in turn and `--remove` per uncommitted one, as that
tool's header states." The commit key appears there as `passBase`, the name `TOOL-aTwinnedPass-1`'s spec gives
it. Both copies, in one commit.

No page under `help/` describes unattended passes: the drive table renders the unit harness as one
row of a registry and names no driver verb (`help/reference/drive.md`). The docs leg grades a script
only where a page shows it, so `pass-tree.sh` owes no row, and the charter's docs rule binds a
user-facing change; this tool is driven by the main loop through the verbs guide it reads.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `pass-tree.sh`, `pass-tree.test.sh` | files | no file cell: `.lexicon.conf` declares function and type cells only; kebab as the kit's siblings |
| `cmd_merge_tree`, `cmd_remove_tree` | the verbs | `--suggest ... --as sh.function`: OK, leading `cmd` |
| `check_pass_tree_run`, `check_pass_branch`, `check_resolvable_path` | checks | OK, leading `check` |
| `run_pass_tree_regen` | regeneration | OK, leading `run` |
| `remove_pass_tree`, `remove_merge_attempt` | cleanup, restore | OK, leading `remove`; `restore` and `reset` are not declared verbs |
| `print_pass_tree_refusal` | the refusal line | OK, leading `print` |
| `main` | entry | OK, reserved |
| `add_fixture_pass` | the suite's pass simulation | OK, leading `add`; `cut` is not a declared verb |
| `PT_BRANCH`, `PT_FROM` | globals | no shell-variable cell |

None of these names occurs in the tree at base outside this spec, by `git grep -w`. The suite's
other helpers lead with a declared verb too, so `lexicon.py --check` stays at its pin.

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
- **`--remove` refusing any branch ahead of `HEAD`, as rev-1 had it.** A branch left at the default
  branch's tip by a skipped reset is ahead of `HEAD` once that branch moves on, and could then be
  neither merged nor removed.
- **Resolving every conflict to this side and letting the bar find the damage.** A product
  conflict is two passes that were not disjoint, and the brief puts that outside this tool.
- **Refusing a merge when `regen.py` cannot be found.** The unattended kit does not require the
  run-gates kit, so every adopter without it could never merge; the lander announces and continues
  for the same reason.

### What the design does not check

- A pass's commits are not graded by `--check-commit` (above). Check 23 grades them at the close,
  and `--merge` refuses only the run-state file, a foreign fork point and an unresolvable conflict.
- That `--branch` is the branch the harness returned for `--pass`: the tool takes the main loop's
  word. A wrong pairing merges a real pass under another unit's subject; `pass_commit` still reads
  the pass commit's own `Pass:` trailer.
- A builder that reset to the right commit and then merged or rebased something else in: the fork
  point still reads `--from`, and only a conflict or the bar sees the foreign content.
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
- A pass whose harness return carried no branch leaves its worktree for `git worktree list` and the
  branch-reconcile kit to show; the tool has nothing to take it away by.
- A Windows process holding a file in a pass's worktree, or a lock on that worktree, makes
  `git worktree remove --force` fail; the note names the path, and the branch is then not deleted
  either, since git refuses to delete a branch a worktree has checked out.
- Where the runtime puts a pass's worktree: a run tree that is the primary checkout sees the
  runtime's worktrees under its own `.claude/worktrees/`, which node a ignores in its common
  `info/exclude` and no tracked ignore file does, so on another clone the clean test refuses there.
- How many passes run at once.

## 5. Production-readiness checklist

- security — no new input beyond a slug, a unit id, a branch name and a sha, each shape-checked
  (`UNIT_ID_ERE`, `git check-ref-format --branch`, lowercase hex) before any git call uses it; every
  git call is argv, never `eval`; no `--no-verify`; deny by default on every conflict the two rules
  do not admit and on a foreign fork point; the restore removes only files a verb that required a
  clean tree made; `--remove` never drops a commit no other ref holds.
- perf / scale — one driver source per call; one `regen.py --write` per merge, whose wall on node a
  this unit does not pin; AC9 measures the whole serial and parallel routes.
- error / empty / loading states — every refusal is one stderr line, exit 1, with the tree as it was;
  a missing `regen.py` is announced; a failed cleanup after a landed merge is a note, exit 0; an
  absent branch at `--remove` is a note, exit 0.
- observability — the merge subject names the unit; the body names the pass branch, its tip and the
  dispatch commit; regen's moved items reach stderr.
- risks — a regeneration that rewrites a file the passes did not touch lands in the merge commit;
  the pass worktree's `--check-commit` gap; a runtime that changes where or whether it keeps a
  changed worktree.
- testing — AC1 to AC9 and the `New arm:` lines of §7.
- migration — N/A: no record shape or conf key moves.
- user docs — the verbs guide (S12); no `help/` page owed (§4, "Docs").

## 6. Acceptance criteria

- **AC1** — When passes 2 and 3, each made by `add_fixture_pass` and reset to `C`, each commit their
  own product file and both rewrite `fx-out.txt` and the README's `gen:fx` region, and
  `bash pass-tree.sh --merge tRun --pass TOOL-tRun-<n> --branch agent-p<n> --from <C>` runs for 2
  then 3, each exits 0 with one sha on stdout; `git rev-parse <sha>^2` is that pass's commit;
  `fx-out.txt` lists `p2.txt` and `p3.txt`, as `render.sh --check` confirms; the second subject reads
  `merge(tRun): TOOL-tRun-3's pass tree`; `git log -1 --format='%(trailers:key=Pass,valueonly)'`
  prints `none`; `git worktree list --porcelain` names neither pass worktree,
  `git branch --list 'agent-p*'` names neither branch; `git status --porcelain` prints nothing.
  Red when: the merge fast-forwards, either conflict is left unresolved, the output is not
  re-rendered, the trailer is missing, or a pass worktree or branch remains.
  fixture: the suite's fixture repository, built under one `mktemp -d`; the tree holds none.
- **AC2** — When pass 4, reset to `C` as pass 2 was, commits its own `p2.txt` and `--merge` runs for
  4 after 2 has merged, it exits 1, its stderr names `p2.txt` and does not name `fx-out.txt`,
  `HEAD` is the pre-merge sha, `git status --porcelain` prints nothing, `git rev-parse -q --verify
  MERGE_HEAD` fails, and branch `agent-p4` and its worktree still exist.
  Red when: the conflict is resolved, the abort leaves a merge in progress or a staged path, or the
  pass's branch or worktree is taken away.
  fixture: as AC1.
- **AC3** — When `--merge` runs from a tree on another branch, with an untracked file present, for
  branch `agent-none`, which does not exist, for branch `run`, for branch `-x`, for pass 5's branch,
  which has no commit beyond `HEAD`, for pass 8's branch, whose commit wrote the fixture's `RUN.md`,
  with `--from HEAD`, and for pass 9's branch, cut from `main` with no reset, with `--from <C>`, each
  exits 1 with one `pass-tree: REFUSING` line, the last naming the reset and `C`'s first eight
  digits, and `HEAD` and `git status --porcelain` are unchanged.
  Red when: any of the nine merges, exits 0, or leaves the tree changed; or pass 9's merge carries
  `m1.txt` into `run`.
  fixture: as AC1.
- **AC4** — When `--merge` runs with `FX_RENDER_FAIL=1` in its environment over a pass whose merge
  would succeed, it exits 1, `HEAD` is the pre-merge sha, `git status --porcelain` prints nothing,
  `fx-partial.txt` is absent, and no `MERGE_HEAD` remains.
  Red when: the merge commits without its regeneration, or the restore leaves `fx-partial.txt` or a
  merge in progress.
  fixture: as AC1.
- **AC5** — When `bash pass-tree.sh --remove tRun --branch agent-p5` runs for pass 5, reset and never
  committed, and for pass 10's `agent-p10`, cut from `main` with no reset and never committed, each
  exits 0 and neither branch nor worktree remains; when it runs for pass 7's branch, holding a commit
  no other ref holds, it exits 1 naming `--merge` and the branch and worktree remain; and for
  `agent-none` it exits 0 with one stderr line naming `agent-none`.
  Red when: `--remove` drops a committed pass, leaves the worktree or branch of an uncommitted one,
  or refuses the pass that skipped the reset.
  fixture: as AC1.
- **AC6** — When, after AC1, a subshell sources `tools/unattended/lib-unattended.sh` in the fixture
  and calls `pass_commit <anchor> TOOL-tRun-2 <run-state file>`, it prints pass 2's commit
  and not the merge; and `bash tools/unattended/unattended.sh --check-commit` over a file holding the
  merge's message exits 0.
  Red when: the merge carries no `Pass: none`, so the walk names it, or the second parent is not the
  pass commit, so the walk finds none.
  fixture: as AC1.
- **AC7** — When `grep` runs over `pass-tree.sh`, its header names `--dispatch`, `--brief`,
  `unattended-unit.js`, the commit key `passBase`, `writes`,
  `Pass: none`, `--merge`, `--from` and `--remove` above its first function, and
  `grep -c 'tools/unattended'` over it prints 0; `grep -c "pass-tree.sh"` prints 1 for each of
  `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, and the comparison
  below prints nothing.
  ```
  diff <(tail -n +2 tools/unattended/VERBS.template.md) <(tail -n +2 memory/guides/UNATTENDED-VERBS.md)
  ```
  Red when: the header omits the order or a key, spells the kit's prefix, or the two guide copies differ.
- **AC8** — When `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` runs for each
  function of §4's inventory, each prints a line opening `OK`; `memory/map/generated/symbols.json`
  carries an entry for each of the tool's; `grep -c "pass-tree.test.sh"` prints at least 1 over
  `tools/unattended/kit.toml` and over `tools/run-gates/selftest-budgets.txt`, the first inside the
  `project-owned` include list; and `grep -c "pass-tree.sh"` over
  `tools/unattended/README.md` prints at least 1.
  Red when: a name the lexicon refuses lands, the index is not regenerated, or the suite ships to
  adopters or has no budget row.
- **AC9** — When the main loop builds two disjoint units of one build through
  `tools/workflows/unattended-unit.js` serially in one tree, and the same two in parallel through the
  harness's commit key and `--merge`, on one frozen clone, the record under this build's `build/`
  folder gives the wall clock of each phase of each route and the two totals.
  Red when: the record lacks a phase or a route, or the clone moved between the routes.
  cost: two builds of two units each, PINNED 2026-11-15 at 15 to 50 minutes a unit by the brief.
  permission: the main loop's, at the close; a pass runs no harness.
  figure: every wall time is DERIVED by the measurement; the record states its node and base.

## 7. Gates

`lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `policy fixtures` · `install-prefix self-test` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `unattended skill wiring` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/unattended/pass-tree.test.sh · covers AC1 AC6 · base aebbb4a72, which has no tool, so every arm's run exits 127; then the tool with `--no-ff` dropped, which fast-forwards pass 2 so `<sha>^2` does not resolve, and with the `Pass: none` line dropped, so `pass_commit` names the merge · none
New arm: tools/unattended/pass-tree.test.sh · covers AC2 · the tool with `check_resolvable_path` returning 0 for every path, which resolves `p2.txt` and exits 0 · none
New arm: tools/unattended/pass-tree.test.sh · covers AC3 · the tool with the `--from` fork-point refusal removed, which merges pass 9 and carries `m1.txt` in; and with the run-state diff refusal removed, which merges the branch that wrote `RUN.md` · none
New arm: tools/unattended/pass-tree.test.sh · covers AC4 · the tool with `remove_merge_attempt`'s `git clean -qfd` removed, which leaves `fx-partial.txt` behind · none
New arm: tools/unattended/pass-tree.test.sh · covers AC5 · the tool with `--remove`'s lost-commit refusal removed, which drops pass 7's commit; and with it widened to rev-1's ahead-of-`HEAD` test, which refuses pass 10 · none

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
- **F3 — What takes away the worktree and branch of a pass that returned `committed: false`?**
  (a) A second verb, `--remove`, sharing `remove_pass_tree` with `--merge` and refusing a branch
  whose deletion would lose a commit. (b) `--merge` itself, which on a branch not ahead of `HEAD`
  removes both and exits with a code of its own: one verb fewer, but a refusal and a cleanup share
  one exit path. (c) By hand, the header printing the git commands: the lookup of the worktree is
  then spelled twice. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F4 — How does `--merge` learn the commit the pass was dispatched from?** (a) A flag,
  `--from <sha>`, the same sha the main loop handed the unit harness as its commit key: one value the
  main loop already holds, checked for shape and for naming a commit, and compared with the fork
  point exactly. (b) Derived from the run-state file, as the commit that first carries the unit's
  dispatch row: no extra flag, but it is the records commit only while the main loop starts every
  pass at that commit, and the derivation is a pickaxe walk over the file's history per merge. (c) No
  value: refuse a branch carrying any commit the default branch holds and `HEAD` lacks. It catches
  a skipped reset, but not a reset to the wrong commit of the run's own line. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.
- rev-2 · 2026-11-15 · title · §1 · §2 S1 to S9 · S14 · §3 · Edges · §4 · AC1 to AC9 renumbered · §7 · F3 · F4 · §10 · the
  revision record `2026-11-15-prompt-TOOL-aTwinnedPass-1-revision`, R1 to R6: the runtime cuts each
  pass's worktree, so `--cut`, `derive_pass_tree` and the `-p<seq>` names are gone (R4, replacing
  item 6); `--merge` takes `--branch` and `--from` and refuses a foreign fork point (R4, item 7); the
  cleanup finds the worktree through `derive_holder_where` (R4, item 8); `--remove` takes a branch
  and refuses only a lost commit (R4, item 9); the header and verbs guide state R5's order with the
  commit key for `tree` (R5, items 9 and 10); the suite simulates the runtime's worktree and reset
  (item 10). F1 to F3 stay RESOLVED (R6); F4 is new.

## 10. Reuse audit

The seams this unit extends: the driver's own readers, reached by sourcing `unattended.sh` and calling
`load_driver_conf` as its suite does (`fact`, `read_recorded_phase`, `resolve_holder_worktree`,
`derive_holder_where`, the effective `GENERATED_INDEXES`); the library's `check_gen_region_only`,
and `TOOL-aTwinnedPass-3`'s `check_generated_output` over `covers`; and the run-gates kit's
`regen.py --write`, found as `run_regen` and `derive_spec_token_key` find a sibling kit's file,
through `resolve_kit_dir`. `tools/codebase-map/reuse_lookup.py "cut a git worktree on a new branch
for one pass and merge it back no-ff resolving generated outputs and regenerating"` ranked `git`,
`resolve`, `resolve_kit_dir`, `merge`, `run_git` and `resolve_python` first, then
`resolve_generated_indexes` and `add_scratch_worktree`. `resolve_kit_dir`, `resolve_python` and
`resolve_generated_indexes` are reused as named; `merge` is the row driver's and the settings
merger's, which merge file contents, not branches. For rev-2, `grep -rn "worktree list --porcelain"
tools/` found the driver's `derive_holder_where`, reused for the cleanup; the other readers list
paths and map no branch to its worktree. No existing seam fits the merge itself, so it is new code beside the readers it calls.

Recall terms used: `python tools/memory-recall/query.py "how were concurrent passes merged back into
the run branch with generated indexes re-rendered" --terms "wave worktree merge no-ff generated
indexes regen gen region pass_commit Pass trailer dispatch parallel M6 dDerivedDocket"`
