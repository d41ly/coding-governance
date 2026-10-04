# TOOL-aGraftedHelix-16 — the spec commit stage re-stages the authored specs after the generator renders them, and a real-git arm runs the prompt's own git block

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 11

<!-- gen:spec-records -->

*No record names this unit.*

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
  `git status --porcelain -- <spec paths>`. Any output returns `committed: false` with that output
  quoted in `why`, so the stage's existing validation throws by name. Observed by AC1 and AC2.
- **S3** — The stage's git sequence, from the pre-stage record through S2's check, is written in the
  prompt as ONE fenced shell block whose only placeholder is `<spec paths>`. The prose steps around
  it say what each command is for and never restate a command. That makes the block the one copy an
  arm can run. Observed by AC1.
- **S4** — `tools/workflows/unattended-build.test.sh` gains a real-git arm. It drives the rendered
  harness with the suite's stub hooks to the commit stage, takes the TRACED `commit:specs:` prompt,
  extracts its fenced block, substitutes the authored spec's path, and runs the block in a scratch
  repository holding a minimal memory tree with the real `gen_build_index.py`. NOT OBSERVED by a
  criterion here: the suite is a kit self-test the main loop runs once at the close (§7).
- **S5** — The review-harness kit version and the harness's own `unattended-build@` engine identity
  each move once, after this unit's last move. Observed by AC3.

## 3. Non-goals (OUT)

- **The rest of unit 15's stage.** Its trigger, schema, path fill, validation table and remedy are
  unit 15's and are unchanged.
- **Verifying the commit from inside the program.** A workflow script has no filesystem, so S2's
  check is the agent's report, and the resolver's read at `HEAD` stays the cross-check unit 15 names.
- **A second copy of the block in the suite.** The arm reads the traced prompt. A typed copy would
  stay green over a prompt that drifted, which is the class finding 31 names.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-15` — the commit stage, its prompt steps, its
  `SPEC_COMMIT_SCHEMA` and the `committed: false` validation that turns S2's report into a named
  throw; without them there is no stage to repair.

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

### The block

The fenced block S3 names, in this order:

1. Record `git status --porcelain --untracked-files=all` before anything is staged.
2. `git add -- <spec paths>`.
3. `python {{MEMORY_TREE_DIR}}/gen_build_index.py --write`.
4. `git add -- <spec paths>` again, then stage each path changed now that step 1 did not list.
5. `git commit`, with the subject and trailers unit 15 states.
6. `git status --porcelain -- <spec paths>`, which must print nothing.

The builder writes step 4's second half as a loop over `git status --porcelain` filtered by step 1's
record, held in a shell variable inside the block. The program fills the slug and the ids into the
commit subject before the prompt is sent, so `<spec paths>`, which the agent finds, is the one
placeholder left.

### The arm

The scratch repository is the `_b1` shape of `tools/memory-tree/check-memory-hygiene.test.sh`: a
conf naming its memory root, a charter, a build README carrying the build-index region, and
`memory/project/stale-header-waiver.txt`, committed once. The arm then writes one spec carrying a
status header and no records region, untracked, and runs the extracted block. It asserts that
`git status --porcelain -- <spec>` prints nothing, and that `git rev-parse HEAD:<spec>` equals
`git hash-object <spec>`. Its staged break removes step 4's re-add from a scratch copy of the
render, and the arm reds on both assertions.

### Inventory

No new function, constant or file. The prompt's text changes, and the suite gains one arm.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`, by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render

## 5. Production-readiness checklist

- security — No new surface. The stage stages the same paths, twice.
- perf / scale — One more `git add` and one `git status` per call that authored anything.
- error / empty / loading states — A spec left dirty is `committed: false` with the porcelain lines,
  and unit 15's validation throws naming them.
- observability — The `why` text quotes the dirty paths.
- risks — A pre-commit hook that rewrites a spec after staging would also leave it dirty. S2 reports
  that case by name instead of letting the resolver find it.
- testing — S4's arm, observed RED with the re-add removed.
- migration — None.
- user docs — N/A: the stage is internal to the harness.

## 6. Acceptance criteria

Criteria AC1 and AC2 run unit 15's scratch `node` probe under the session scratchpad: the rendered
`tools/workflows/unattended-build.js` evaluated as an AsyncFunction with stub hooks that trace each
agent label and prompt. Each staged break is made in a scratch COPY of the render.

- **AC1** — When the probe runs a call whose SPEC double authors `A-tB-1`, the traced
  `agent:commit:specs:tB` prompt holds exactly one fenced shell block. In it a
  `git add -- <spec paths>` line follows the `gen_build_index.py --write` line, and the last
  command is `git status --porcelain -- <spec paths>`. The prompt says a non-empty status returns
  `committed: false`.
  Red when: the re-add or the post-commit status is missing. Staged: the re-add deleted in the copy
  leaves no `git add` line after the `--write` line.
- **AC2** — When the block extracted from AC1's traced prompt runs in a scratch repository at a
  short path under `%TEMP%`, built as §4 "The arm" states, `git status --porcelain -- <spec>` prints
  nothing and `git rev-parse HEAD:<spec>` equals `git hash-object <spec>`.
  Red when: the commit holds the pre-render blob. Staged: the same run over the copy without the
  re-add prints ` M <spec>` and the two hashes differ.
- **AC3** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no review-harness carrier left behind, and
  `bash tools/check-kit-versions.sh` exits 0. Line 3 of `tools/workflows/unattended-build.js`
  carries an engine identity one minor step above its value at the pass's parent.
  Red when: the kit's shipped bytes moved without its version.
  figure: both versions are DERIVED from the pass's parent at observation time, because units 3 and
  15 move both lines first.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · the traced commit-stage block run for real in a scratch repository with the real generator; stage the post-render re-add deleted · the suite's floor rises by the arms added

The close runs the legs and the suite. A pass runs the probe and the scratch repository of §6 as its
check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 21 of the round-1 spec audit of units 10
  to 15, grounded against `gen_build_index.py` and the harness template at base `5266d22e`.

## 10. Reuse audit

The seams are the ones unit 15's §10 found by reading the harness, plus two read for this unit:
`cmd_write` and `plan` in `tools/memory-tree/gen_build_index.py`, and the `_b1` fixture in
`tools/memory-tree/check-memory-hygiene.test.sh`, which already runs the real generator in a scratch
repository. No existing seam fits an arm that runs a traced prompt's commands: the harness suite's
arms read traces and never execute them. The recall probe returned `TOOL-aStagedLane-3` and
`TOOL-aWokenSentinel-15`, the rulings unit 15 cites, and no record of a prompt executed by its suite.

Recall terms used: unattended-build spec stage writers author commit resolver subjects blob HEAD audit pinned resumeFromRunId caller
