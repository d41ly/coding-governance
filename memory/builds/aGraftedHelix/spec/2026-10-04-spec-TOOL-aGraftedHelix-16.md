# TOOL-aGraftedHelix-16 — the spec commit stage re-stages the authored specs after the generator renders them, and a real-git arm runs the prompt's own git block

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-1 · base 5266d22e · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-17 TOOL-aGraftedHelix-18 TOOL-aGraftedHelix-19 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-15`'s commit stage stages the authored specs, then runs
`gen_build_index.py --write`, then stages only the paths its pre-stage record did not list. The
generator renders the `gen:spec-records` region into every tracked spec carrying a status header and
adds the region where it is missing (`tools/memory-tree/gen_build_index.py:2088-2107`, reached from
`cmd_write` at `:2306`). The authored specs are tracked by then and were listed, so their rendered
bytes stay unstaged. The commit holds each spec's pre-render blob, and the resolver's `HEAD:` against
`hash-object` compare (`tools/workflows/unattended-build.template.js:804-811`) throws the dirty-tree
refusal on the first call that unit exists to fix. Every criterion of unit 15 uses a commit double,
so none sees it. This unit re-stages the specs after the render, checks the commit left them clean,
and adds an arm that runs the prompt's git sequence for real. It closes finding 21 (HIGH) of the
round-1 spec audit of units 10 to 15.

## 2. Scope (IN)

- **S1** — In the commit stage's prompt, the step that runs `gen_build_index.py --write` is followed
  by `git add -- <spec paths>` again, so the staged set is the authored specs plus every path
  changed now that the pre-stage record did not list. The rule unit 15 states for FOREIGN paths is
  unchanged. Observed by AC1 and AC2.
- **S2** — After the commit and before the sha is returned, the prompt runs
  `git status --porcelain -- <spec paths>`. Any output returns `committed: false`, and the prompt
  tells the agent to quote those porcelain lines in `why`, so the stage's existing validation throws
  naming them. Observed by AC1 and AC4.
- **S3** — The stage's git sequence, from the pre-stage record through S2's check, is written in the
  prompt as ONE fenced shell block that opens with `set -e` and whose only placeholders are
  `<spec paths>` and `<attribution trailer>`, the trailer the charter mandates, which only the agent
  knows. The prose steps around it say what each command is for and never restate one of
  the block's command lines. The prose says that a step exiting non-zero returns `committed: false`
  with that step's output in `why`. That makes the block the one copy an arm can run, and a failed
  render stops the block instead of committing past it. Observed by AC1.
- **S4** — `tools/workflows/unattended-build.test.sh` gains a real-git arm. It drives the rendered
  harness with the suite's stub hooks to the commit stage, decodes the `commit:specs:` prompt from its
  `promptjson:` trace line (S7), extracts its fenced block, substitutes the authored spec's path, and
  runs the block in the scratch repository §4 "The arm" builds, foreign paths included.
  NOT OBSERVED by a criterion here: the suite is a kit self-test the main loop runs once at the
  close (§7).
- **S5** — The review-harness kit version and the harness's own `unattended-build@` engine identity
  each move once, after this unit's last move. Observed by AC3.
- **S6** — Before anything is staged, the block refuses when an input of the generator carries a
  change the index does not hold: `git diff --name-only` over the memory root, `.memory-tree.conf`
  and the generator's directory names a path outside the spec paths, or `.memory-tree.conf` is
  untracked. The block then exits non-zero naming those inputs, with nothing rendered or staged.
  This is `TOOL-dMendedRecall-2` rev-3 S3's input rule, adopted. Observed by AC2.
- **S7** — The suite's stub `agent` hook traces each prompt a second time, as
  `promptjson:<label>:` followed by `JSON.stringify` of the prompt, on one line. The existing
  `prompt:` line stays byte-identical, so the suite's reads of `^prompt:<label>:` keep reading what
  they read today. A canary arm asserts that a multi-line prompt's `promptjson:` line decodes to a
  string holding a newline. NOT OBSERVED by a criterion here: the suite is a kit self-test the main
  loop runs once at the close (§7).

## 3. Non-goals (OUT)

- **The rest of unit 15's stage.** Its trigger, schema, path fill, validation table and remedy are
  unit 15's and are unchanged.
- **Verifying the commit from inside the program.** A workflow script has no filesystem, so S2's
  check is the agent's report, and the resolver's read at `HEAD` stays the cross-check unit 15 names.
- **A second copy of the block in the suite.** The arm reads the traced prompt. A typed copy would
  stay green over a prompt that drifted, which is the class finding 31 names.
- **The delta loop's listing mode and where the pre-stage record lives.** The loop below lists with
  plain `git status --porcelain` and filters by a shell variable. A wholly untracked foreign
  directory and a block split across Bash calls are `TOOL-aGraftedHelix-21`'s (§3 Edges), so the
  foreign untracked file this unit's fixture plants sits at the repository root, where both listing
  modes print the same line.
- **Unit 15 §5's sentence that hygiene check 9 refuses a commit whose views a foreign edit moved.**
  This unit does not rest on it. Check 9 runs `gen_build_index.py --check` over the worktree
  (`tools/memory-tree/check-memory-hygiene.sh:1039-1041`), and `cmd_check` (`:2130`) compares a disk
  render with disk bytes, never the index. S6's input rule is the guard here.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-15` — the commit stage, its prompt steps, its
  `SPEC_COMMIT_SCHEMA` and the `committed: false` validation that turns S2's report into a named
  throw; without them there is no stage to repair.
- **hands-off** `TOOL-aGraftedHelix-21` — the delta loop's listing taken with `--untracked-files=all`
  like the record and compared by path, the record surviving a block split across Bash calls, and
  the foreign untracked directory in this unit's fixture (findings 22 and 17 of the round-1 audit of
  units 16 to 19).

## 4. Design

### Evidence

- `cmd_write` calls `plan(root, conf, create_missing=True)` (`gen_build_index.py:2306`). For every
  unit of every build, `plan` adds the `gen:spec-records` pair where it is missing and renders the
  region (`gen_build_index.py:2088-2107`). `render_spec_records` always writes content, an explicit
  empty-records line included.
- The generator reads tracked files only, which is why unit 15 stages the specs before it runs.
  Both facts together put the rendered bytes in the working tree and the pre-render bytes in the
  index.
- Commit `14e5f2655` shows the generator rewriting the records region of every sibling spec.
- `plan()` lists its inputs with `git ls-files` (`gen_build_index.py:698`) and reads their bytes off
  the disk, so a foreign unstaged edit to a sibling spec's status header, a `BACKLOG.md` or
  `DECISIONS.md` moves `memory/LIVE.md`, the ledger shard and the build README's regions. Those are
  clean at the record and changed after the render, so the delta loop stages them.
  `TOOL-dMendedRecall-2` rev-3 S3 decided this case for the inherited-red auto-file: when an input
  carries an unstaged change, render nothing and stage no view. Its function `write_ask_views` is
  absent at this tree's HEAD, so this unit cites the spec record, not the function.
- `gen_build_index.py` inserts its own directory on `sys.path`, imports `tree_lib` (`:149`) and
  `backlog` (`:290`), and never sets `dont_write_bytecode`. Only this repository's `.gitignore:1`
  hides the `__pycache__/` it writes, and `adopt-memory-tree.sh` adds no such ignore.
  `TOOL-dMendedRecall-2` rev-2 S2 added `-B` to the same render-then-stage rule after its fixture's
  first close committed two bytecode caches.
- The render fills `{{MEMORY_TREE_DIR}}` repo-relative: the rendered harness's checklist line reads
  `python tools/memory-tree/gotchas.py` (`tools/workflows/unattended-build.js:361`).
- `tools/workflows/unattended-build.test.sh:170` traces every prompt as
  `String(prompt).replace(/\n/g, " ")`, so the `prompt:` line holds no block that can run, and 18
  reads of the form `grep '^prompt:<label>:'` depend on that line staying one line.

### The block

The fenced block S3 names. It opens with `set -e`, then in this order:

1. Record `git status --porcelain --untracked-files=all` into a shell variable, before anything is
   staged.
2. The input check S6 states. The memory root is derived inside this step's own command, from the
   first spec path, as the part before `/builds/`. Its pathspecs are that root,
   `.memory-tree.conf` and `{{MEMORY_TREE_DIR}}`. A dirty input exits non-zero naming it.
3. `git add -- <spec paths>`.
4. `python -B {{MEMORY_TREE_DIR}}/gen_build_index.py --write`.
5. `git add -- <spec paths>` again, then stage each path changed now that step 1 did not list.
6. `git commit`, with the subject and trailers unit 15 states, the trailers passed as `--trailer`
   so `Pass: none` and `<attribution trailer>` close the message as one trailer block.
7. `git status --porcelain -- <spec paths>`, which must print nothing.

The builder writes step 5's second half as a loop over `git status --porcelain` filtered by step 1's
record. Under `set -e` the filter is never a `grep` that exits 1 on no match inside a command
substitution, or a call with no foreign changes would stop before the commit; a membership test in
the loop's own `if` or `case` is the shape. The program fills the slug and the ids into the commit
subject before the prompt is sent, so `<spec paths>`, which the agent finds, and
`<attribution trailer>`, which the program cannot know, are the two placeholders left. The surrounding prose names each step's purpose, says the block runs as written, and spells
none of its command lines a second time, so an agent following prose and an arm running the block
cannot diverge.

### The arm

The scratch repository is the `_b1` shape of `tools/memory-tree/check-memory-hygiene.test.sh`: a
conf naming its memory root, a charter, a build README carrying the build-index region, and
`memory/project/stale-header-waiver.txt`. Its first commit also installs the WHOLE memory-tree kit
directory at the directory the rendered block's step-4 line names, derived from that line and never
typed in the suite, as unit 9's copy-install fixture (its AC12) installs a kit. A two-file copy
fails at `import backlog` (`gen_build_index.py:290`). The repository carries no `.gitignore`.

Two foreign paths are planted after that commit: one tracked file outside the memory root, the conf
and the kit directory, modified and unstaged, and one untracked file at the repository root. The arm
then writes one spec carrying a status header and no records region, untracked, and runs the
extracted block with both placeholders filled. It runs it with `PYTHONDONTWRITEBYTECODE` unset, because
a host that sets it hides the `-B` break: node `a` sets it to `1`, and there the break committed no
cache until the variable was unset. A `python` that does not run on the host is reached through the
suite's resolved launcher, and the block's text is not edited for it. It asserts:

| assertion | what it rules out |
|---|---|
| the block exits 0 | a step failing silently |
| `git status --porcelain -- <spec>` prints nothing, and `git rev-parse HEAD:<spec>` equals `git hash-object <spec>` | the pre-render blob committed |
| `git show HEAD:<spec>` holds `<!-- gen:spec-records -->` | a green run where the generator never ran |
| `git show --name-only --format= HEAD` holds the spec and the build README and neither foreign path | the delta loop staging nothing, or staging foreign work |
| `git status --porcelain` lists exactly the two foreign paths, unchanged | foreign work moved or swallowed |
| `git ls-tree -r --name-only HEAD` holds no `__pycache__` path | bytecode caches committed |
| `gen_build_index.py --check` in a clean clone of HEAD exits 0 | views derived from bytes the commit does not hold |

A variant adds a foreign unstaged edit to a second spec's status header and asserts that the block
exits non-zero naming that spec, with `HEAD` and the index unmoved.

Staged breaks, each made in a scratch copy of the render: step 5 removed whole, the re-add and the
loop, reds the first pair, which is unit 15's defect; the loop's filter inverted puts a foreign path
in `HEAD`; `-B` removed puts a `__pycache__` path in `HEAD`; step 2 removed lets the variant commit,
and the clean clone's `--check` reads drift.

The re-add removed ALONE is not a red here, measured: step 5's loop compares whole lines, and an
authored spec's line moves from `?? <spec>` in the record to `AM <spec>` after the render, so the loop
stages the rendered spec too. The re-add's own red in this unit is AC1's order predicate. It becomes
the only stager of a spec once `TOOL-aGraftedHelix-21` compares by path, because the record holds the
spec's path.

### Inventory

No new function, constant or file. The prompt's text changes, the suite's stub hook gains one trace
line per agent call, and the suite gains the real-git arm and the canary.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`, by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render

## 5. Production-readiness checklist

- security — No new surface. The stage stages the same paths, twice, and refuses rather than
  renders over another writer's unstaged input.
- perf / scale — One more `git add`, one `git diff` and one `git status` per call that authored
  anything.
- error / empty / loading states — A spec left dirty is `committed: false` with the porcelain lines,
  and unit 15's validation throws naming them. A failing step stops the block under `set -e` and
  returns its output. A dirty input is `committed: false` naming the input.
- observability — The `why` text quotes the dirty paths or the dirty inputs.
- risks — A pre-commit hook that rewrites a spec after staging would also leave it dirty. S2 reports
  that case by name instead of letting the resolver find it. Until `TOOL-aGraftedHelix-21` lands,
  the loop's plain listing collapses a wholly untracked directory to one line the record never holds.
- testing — S4's arm, observed RED on each staged break §4 "The arm" names, and S7's canary.
- migration — None.
- user docs — N/A: the stage is internal to the harness.

## 6. Acceptance criteria

Criteria AC1, AC2 and AC4 run unit 15's scratch `node` probe under the session scratchpad: the
rendered `tools/workflows/unattended-build.js` evaluated as an AsyncFunction with stub hooks that
trace each agent label, and each prompt as `promptjson:<label>:` plus its JSON encoding, the channel
S7 adds to the suite. Each staged break is made in a scratch COPY of the render.

- **AC1** — When the probe runs a call whose SPEC double authors `A-tB-1`, the decoded
  `commit:specs:tB` prompt holds exactly one fenced shell block. Its first line is `set -e`. In it a
  `git add -- <spec paths>` line follows the `gen_build_index.py --write` line, which carries `-B`,
  and the last command is `git status --porcelain -- <spec paths>`. Outside the block, no line or
  inline code span reproduces one of the block's own command lines: `git add -- <spec paths>`,
  `git commit`, `git status --porcelain` or `gen_build_index.py --write`. The prose says a non-empty
  status returns `committed: false` with the porcelain lines quoted in `why`, and that a step exiting
  non-zero returns `committed: false` with its output. Before the predicate is wired, its hits and
  near-misses over the real decoded prompt are printed.
  Red when: the re-add or the post-commit status is missing, a block command is restated in prose,
  or the quoting instruction is absent. Staged: the re-add deleted in the copy leaves no
  `git add -- <spec paths>` line after the `--write` line, the loop's own `git add` being a different
  line; a prose `git add -- <spec paths>` step re-inserted outside the block
  reds the restatement predicate; the quoting sentence deleted reds its assertion.
- **AC2** — When the block extracted from AC1's decoded prompt runs in a scratch repository at a
  short path under `%TEMP%`, built as §4 "The arm" states with both foreign paths planted, every
  assertion of §4's table holds: the block exits 0, `git status --porcelain -- <spec>` prints
  nothing, `git rev-parse HEAD:<spec>` equals `git hash-object <spec>`, `git show HEAD:<spec>` holds
  `<!-- gen:spec-records -->`, `git show --name-only --format= HEAD` names no foreign path,
  `git ls-tree -r --name-only HEAD` names no `__pycache__` path, and `gen_build_index.py --check` in
  a clean clone of `HEAD` exits 0. With a foreign unstaged edit to a second spec's status header
  added, the block exits non-zero naming that spec, and `git rev-parse HEAD` is unchanged.
  Red when: the commit holds the pre-render blob, the generator never ran, a foreign path or a cache
  is committed, or the commit holds views derived from a foreign input. Staged: the run over the copy
  without step 5 prints ` M <spec>` and the two hashes differ; each other break §4 "The arm" names
  reds its own row.
- **AC3** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no review-harness carrier left behind, and
  `bash tools/check-kit-versions.sh` exits 0. Line 3 of `tools/workflows/unattended-build.js`
  carries an engine identity one minor step above its value at the pass's parent.
  Red when: the kit's shipped bytes moved without its version.
  figure: both versions are DERIVED from the pass's parent at observation time, because units 3 and
  15 move both lines first.
- **AC4** — When the probe runs a call whose commit double returns
  `{committed: false, why: ' M <path>'}`, the run throws, and the thrown text holds ` M <path>`.
  Red when: the `why` text is dropped between the agent's report and the throw.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · the decoded commit-stage block run for real in a scratch repository holding the whole memory-tree kit and two foreign paths; stage the re-add removed, the filter inverted, -B removed and the input check removed · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · a multi-line prompt's promptjson line decodes to a string holding a newline; stage the channel flattened like the prompt line · the suite's floor rises by the arms added

The close runs the legs and the suite. A pass runs the probe and the scratch repository of §6 as its
check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 21 of the round-1 spec audit of units 10
  to 15, grounded against `gen_build_index.py` and the harness template at base `5266d22e`.
- rev-2 · 2026-10-04 · §2 §3 §4 §5 §6 §7 §10 · S2 S3 S4 S6 S7 · AC1 AC2 AC4 · folded the round-1
  spec audit of units 16 to 19 on this unit. Findings 4, 11 and 18: the scratch repository installs
  the whole kit at the path the block names, the block opens with `set -e`, and the arm asserts the
  rendered region. Finding 2: two planted foreign paths and a name-list assertion on `HEAD`. Finding
  23: S6, `TOOL-dMendedRecall-2`'s input rule, and the clean-clone `--check`. Finding 24: `-B` on the
  render. Finding 16: S7's `promptjson:` channel. Finding 3: AC1's restatement predicate. Finding 5:
  AC1's quoting assertion and AC4. §3 gains the hands-off to `TOOL-aGraftedHelix-21`, promoted from
  findings 22 and 17, and points away from unit 15 §5's check-9 sentence.
- rev-3 · 2026-10-05 · §2 §4 §6 · S3 · AC1 AC2 · the builder, against a scratch run of the block
  before any code. The commit's attribution trailer is the charter's and only the agent knows it, so
  `<spec paths>` could not be the block's only placeholder without dropping the trailer unit 15
  requires; `<attribution trailer>` is the second, and step 6 passes both trailers as `--trailer`.
  The re-add removed alone left the commit clean, because step 5's whole-line loop also stages a
  spec whose line moved from `??` to `AM`, so AC2's first-pair break is step 5 removed whole and the
  re-add's own red here is AC1's. The `-B` break committed no cache on node `a` until
  `PYTHONDONTWRITEBYTECODE` was unset, so the arm unsets it. AC1's re-add break names the
  `git add -- <spec paths>` line, since the loop carries a `git add` of its own.

## 10. Reuse audit

The seams are the ones unit 15's §10 found by reading the harness, plus three read for this unit:
`cmd_write` and `plan` in `tools/memory-tree/gen_build_index.py`, the `_b1` fixture in
`tools/memory-tree/check-memory-hygiene.test.sh`, which already runs the real generator in a scratch
repository, and the render-then-stage rule of `TOOL-dMendedRecall-2` (`-B` at rev-2 S2, the input
rule at rev-3 S3), adopted here as a rule and not as code. No existing seam fits an arm that runs a
traced prompt's commands: the harness suite's arms read traces and never execute them. The rev-1
recall probe returned `TOOL-aStagedLane-3` and `TOOL-aWokenSentinel-15`, the rulings unit 15 cites,
and missed `TOOL-dMendedRecall-2`, because its terms named only the harness's vocabulary. The rev-2
probe, written in the mechanism's own terms, ranked that record's spec second.

Recall terms used: unattended-build spec stage writers author commit resolver subjects blob HEAD audit pinned resumeFromRunId caller

Recall terms used (rev-2): render stage generated view unstaged input write_ask_views gen_build_index -B bytecode left unstaged
