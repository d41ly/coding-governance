# TOOL-aGraftedHelix-21 — the spec commit block's delta loop lists untracked paths as its record does, compares paths, and refuses when its record is unset

**Status:** SPECCED · rev-3 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-review-TOOL-aGraftedHelix-20-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-20-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-20 TOOL-aGraftedHelix-22 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-16` writes the spec commit stage's git sequence as one fenced block. Its step 1
records `git status --porcelain --untracked-files=all` into a shell variable, and its step 5 stages
every path a plain `git status --porcelain` lists that the record does not hold. Two defects follow.
Plain porcelain collapses a wholly untracked directory to one `?? <dir>/` line that the per-file
record never holds, so the loop runs `git add -- <dir>/` and stages another writer's untracked work
whole; the finder reproduced the two listings in a scratch repository. And the record lives in a
shell variable, while the agent's Bash tool keeps no variables between calls: a block split across
calls reaches step 5 with the record unset, filters nothing out, and stages every changed path. Both
end in a spec commit carrying foreign work, which breaks the FOREIGN rule unit 15 states and calls
live. This unit makes the two listings one command compared by path, says the block is one
invocation, and refuses an unset record. It closes findings 22 and 17 (both HIGH) of the round-1 spec
audit of units 16 to 19.

## 2. Scope (IN)

- **S1** — Step 5's listing is `git status --porcelain --untracked-files=all`, the same command as
  step 1's record. The loop compares each line's PATH field, the text after the two status columns
  and the space, with the path fields of the record's lines, never whole lines. A wholly untracked
  foreign directory then lists file by file, each file is in the record, and none is staged; a
  recorded path whose status letters moved during the render, such as a foreign ` M` file that
  reads ` D` by step 5, is still recognised and never staged. Observed by AC1 and AC2.
- **S2** — The prose around the block says it runs as ONE Bash invocation, because the record is a
  shell variable and the agent's Bash tool keeps no shell state between calls. Observed by AC1.
- **S3** — The block tests the record variable twice, each time as `${rec+x}` and never by
  emptiness, so a clean tree, whose record is set and empty, proceeds. The EARLY guard sits right
  after step 1, before step 2, so before step 3's first `git add`: unset there, the block exits
  non-zero naming the record, having staged and rendered nothing. The LATE guard sits before step
  5's loop: unset there, the block exits non-zero naming the record AND the cleanup it leaves owed,
  which is to restore every unstaged path under the memory root other than the spec paths and then
  unstage the spec paths with `git reset -q -- <spec paths>`, never `git rm --cached`, which refuses
  an index blob that differs from both `HEAD` and the working copy. Either refusal stops the block
  before its commit, and unit 16 S3's prose returns `committed: false` with that output. Observed by
  AC1 and AC2.
- **S4** — Unit 16's real-git arm in `tools/workflows/unattended-build.test.sh` plants a third
  foreign path, an untracked file inside an untracked directory, and asserts
  `git ls-tree -r --name-only HEAD` lists no path under that directory. This SUPERSEDES unit 16 §4
  "The arm"'s row "`git status --porcelain` lists exactly the two foreign paths, unchanged" by name:
  `git status --porcelain --untracked-files=all` lists exactly the three foreign paths, unchanged,
  because plain porcelain collapses the untracked directory to a third `?? foreign/` line. A second
  and a third arm run the extracted block once per guard, with §6 AC2's two stimuli and its
  assertions. A fourth arm moves unit 16's foreign tracked modified file from ` M` to ` D` between
  step 4 and step 5, and asserts that change stays out of `HEAD`. NOT OBSERVED by a criterion here:
  the suite is a kit self-test the main loop runs once at the close (§7).
- **S5** — The review-harness kit version and the harness's own `unattended-build@` engine identity
  each move once, after this unit's last move. Observed by AC3.

## 3. Non-goals (OUT)

- **Everything else in the block.** Its order, `set -e`, the input check, `-B`, the re-add and the
  post-commit status are unit 16's and are unchanged.
- **A NUL-delimited listing.** `-z` would carry every path byte for byte, but bash command
  substitution drops NUL bytes and the record is a shell variable. Without `-z`, git C-quotes a path
  carrying a space or another unusual byte, identically in both listings, so the comparison still
  matches it. A quoted path the loop must STAGE makes `git add` refuse it, and `set -e` stops the
  block: a loud `committed: false`, never a wrong commit. The generator's outputs carry no such byte.
- **The record as a file under the git directory.** It survives a split, but it is a second carrier
  to clean up and a stale copy a later split call could read. S2 and S3 make the split a refusal
  instead. The early guard refuses before the block's first side effect, so the split shape step 1's
  loss leaves behind owes no cleanup; only a record lost after step 4 does, and the late guard's
  refusal names it.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-16` — the block, its step 1 record and step 5 loop, its
  `set -e` and the prose that returns a failed step's output as `committed: false`, the
  `promptjson:` trace channel, and the real-git arm with its foreign-path fixture; without them there
  is no loop to repair and no arm to extend.

## 4. Design

### Evidence

- In a scratch repository with foreign/sub/brief.md untracked, `git status --porcelain` printed
  `?? foreign/` and `git status --porcelain --untracked-files=all` printed
  `?? foreign/sub/brief.md` (the finder; reproduced on node `a` 2026-10-04 with a spaced file name,
  which the second listing printed C-quoted). No repository config sets `status.showUntrackedFiles`.
- `TOOL-dMendedRecall-2` S2, the CLOSED precedent for this render-then-stage-the-delta rule, takes
  its before and after sets with one listing.
- Unit 15's step 2, which unit 16's block replaces, kept the record in the agent's own context, so
  the dependence on shell state is new in unit 16.

### The loop

| step | listing | compared by |
|---|---|---|
| 1, the record | `git status --porcelain --untracked-files=all` | — |
| after 1, the early guard | none: `${rec+x}` | — |
| 5, before the loop, the late guard | none: `${rec+x}` | — |
| 5, the delta | `git status --porcelain --untracked-files=all` | the path field of each line |

Under `set -e` the membership test sits in the loop's own `if` or `case`, as unit 16 requires. A
guard on a state the block needs runs before the block's first side effect, and a refusal names the
cleanup it leaves owed; the late guard is the second net for a record lost after step 1.

### The arm's foreign paths

| path | kind | asserted |
|---|---|---|
| a tracked file outside the generator's inputs | modified, unstaged | unit 16's, except its listing row |
| an untracked file at the root | untracked | unit 16's, except its listing row |
| foreign/sub/brief.md | untracked, inside an untracked directory | no `foreign/` path in `HEAD` |

The listing row replaces unit 16's for all three: `git status --porcelain --untracked-files=all`
lists exactly these three paths, unchanged.

### Inventory

No new function, constant or file. The prompt's text changes, and the suite gains one fixture path
and the four arms §7 names.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`, by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render

## 5. Production-readiness checklist

- security — No new surface. The loop stages a subset of what it staged before.
- perf / scale — The second listing walks untracked directories file by file, as the first already
  does.
- error / empty / loading states — An unset record is `committed: false` naming it. A clean tree's
  empty record proceeds. A record lost after step 4 leaves rendered views and staged specs, and the
  late guard's refusal names the cleanup that clears them.
- observability — Each refusal's text names the record and says the block must run as one
  invocation; the late guard's names the cleanup too.
- risks — A path git C-quotes that the loop must stage stops the block, by design (§3).
- testing — S4's arms, each observed RED under its own staged break: the flag removed from step 5's
  listing, the early guard deleted, the late guard deleted, and a membership test comparing whole
  lines.
- migration — None.
- user docs — N/A: the stage is internal to the harness.

## 6. Acceptance criteria

Criteria AC1 and AC2 run unit 16's scratch `node` probe and decode the `commit:specs:` prompt from
its `promptjson:` channel. Each staged break is made in a scratch COPY of the render.

- **AC1** — When the probe runs a call whose SPEC double authors `A-tB-1`, the decoded prompt's block
  lists with `git status --porcelain --untracked-files=all` at step 1 and again at step 5, a
  `${rec+x}` test sits between step 1 and step 2 and another precedes step 5's loop, and the prose
  says the block runs as ONE Bash invocation.
  Red when: the two listings differ, or either guard or the instruction is absent. Staged: the flag
  deleted from step 5's listing in the copy makes the two listing lines differ.
- **AC2** — When the block extracted from AC1's decoded prompt runs in unit 16's scratch repository
  at a short path under `%TEMP%`, with foreign/sub/brief.md untracked beside unit 16's two foreign
  paths, it exits 0, `git ls-tree -r --name-only HEAD` names no path under `foreign/`, and
  `git status --porcelain --untracked-files=all` lists exactly the three foreign paths, unchanged.
  With a line inserted between step 4 and step 5 that deletes unit 16's foreign tracked modified
  file, so its status moves from ` M` to ` D`, the block exits 0 and
  `git ls-tree -r --name-only HEAD` still names that file. With step 1's assignment line deleted,
  the block exits non-zero naming the record, `git diff --cached --name-only` is empty, and
  `git status --porcelain --untracked-files=all` equals its value before the run. With `unset rec`
  inserted after step 4, it exits non-zero naming the record and the cleanup, `git rev-parse HEAD`
  is unchanged, and after that cleanup the block, re-run as one invocation, exits 0.
  Red when: foreign untracked work is committed, a foreign deletion is committed, a record lost at
  step 1 leaves anything staged or rendered, or a record lost after step 4 commits. Staged: the run
  over the copy without the flag puts foreign/sub/brief.md in `HEAD`; a membership test comparing
  whole lines puts the deletion in `HEAD`; with the early guard deleted, the step-1 stimulus reaches
  the late guard only after staging and rendering, and its index and listing assertions red; with
  the late guard deleted, the step-4 stimulus commits the foreign paths and moves `HEAD`.
- **AC3** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no review-harness carrier left behind, and
  `bash tools/check-kit-versions.sh` exits 0. Line 3 of `tools/workflows/unattended-build.js`
  carries an engine identity one minor step above its value at the pass's parent.
  Red when: the kit's shipped bytes moved without its version.
  figure: both versions are DERIVED from the pass's parent at observation time, because units 3, 15
  and 16 move both lines first.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · the real-git arm's fixture gains an untracked file inside an untracked directory; stage step 5's listing without --untracked-files=all · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · the extracted block with step 1's assignment deleted refuses with nothing staged or rendered; stage the early guard deleted · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · the extracted block with unset rec after step 4 refuses naming the cleanup, leaves HEAD unmoved, and passes when re-run after it; stage the late guard deleted · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · a foreign tracked file deleted between step 4 and step 5 stays out of HEAD; stage a membership test comparing whole lines · the suite's floor rises by the arms added

The close runs the legs and the suite. A pass runs the probe and the scratch repository of §6 as its
check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from findings 22 and 17 of the round-1 spec audit of
  units 16 to 19, grounded against unit 16 rev-2 and a two-listing probe on node `a`.
- rev-2 · 2026-10-04 · §2 §3 §4 §5 §6 §7 · S1 S3 S4 · AC1 AC2 · folded the round-1 spec audit of
  units 20 to 22 on this unit. Finding 3: AC2 deletes a foreign tracked file between step 4 and
  step 5, so a whole-line membership test reds, with its own arm. Finding 9: S4 and §4 supersede
  unit 16's exactly-two listing row by name, with `--untracked-files=all` and three paths. Findings
  10 and 15: S3 tests the record twice, right after step 1 and before step 5's loop, the late
  refusal names the cleanup, and AC2 and §7 give each guard its own stimulus and staged break.
- rev-3 · 2026-10-04 · §2 §4 · S3 S4 · from the bug-class checklist over the promoting commit, which
  selected `amendment-leaves-its-other-half-standing` and `git-rm-cached-refuses-a-diverged-index-blob`.
  §4 Inventory and S4 counted one arm where §7 names four, and S3's cleanup unstages the spec paths
  with `git reset`, since a staged new spec's blob differs from both `HEAD` and the working copy.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "compare a recorded git status listing with a later one by
path and stage only the new paths"` ranked name-stem neighbours only, `records` in
`tools/memory-tree/gotchas.py` and `git` in `tools/govkit/govkit.py`, and printed
`unscanned layers: .sh`, so its miss is no evidence. The seam extended is unit 16's block itself and
the one-listing rule of `TOOL-dMendedRecall-2` S2; no existing seam fits beyond them. The recall
probe returned unit 15's commit-stage steps, the audit's M5 row, and `TOOL-dTieredTribunal-21`, an
`git add -A` that staged a stray file, and no record of two listings taken with different flags.

Recall terms used: porcelain untracked-files record stage delta foreign render generated view unstaged input shell variable

The question passed with them: "how is a pre-stage git status record compared with a later listing
so foreign untracked work is never staged".
