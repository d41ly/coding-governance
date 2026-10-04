# TOOL-aGraftedHelix-21 — the spec commit block's delta loop lists untracked paths as its record does, compares paths, and refuses when its record is unset

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 12

<!-- gen:spec-records -->

*No record names this unit.*

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
  recorded path whose status letters moved during the render is still recognised. Observed by AC1
  and AC2.
- **S2** — The prose around the block says it runs as ONE Bash invocation, because the record is a
  shell variable and the agent's Bash tool keeps no shell state between calls. Observed by AC1.
- **S3** — Before its loop, step 5 refuses when the record variable is unset, tested as `${rec+x}`
  and never by emptiness, so a clean tree, whose record is set and empty, proceeds. The refusal
  exits non-zero naming the record before the loop stages anything, so the block stops before its
  commit, and unit 16 S3's prose returns `committed: false` with that output. Observed by AC1 and AC2.
- **S4** — Unit 16's real-git arm in `tools/workflows/unattended-build.test.sh` plants a third
  foreign path, an untracked file inside an untracked directory, and asserts
  `git ls-tree -r --name-only HEAD` lists no path under that directory. A second arm runs the
  extracted block with step 1's assignment line taken out, the shape a split invocation leaves, and
  asserts a non-zero exit naming the record, `git rev-parse HEAD` unmoved, and no foreign path in
  `git diff --cached --name-only`. NOT OBSERVED by a criterion here: the suite is a kit self-test the
  main loop runs once at the close (§7).
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
  instead.

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
| 5, the delta | `git status --porcelain --untracked-files=all` | the path field of each line |

Under `set -e` the membership test sits in the loop's own `if` or `case`, as unit 16 requires, and
the `${rec+x}` guard precedes the loop.

### The arm's foreign paths

| path | kind | asserted |
|---|---|---|
| a tracked file outside the generator's inputs | modified, unstaged | unit 16's |
| an untracked file at the root | untracked | unit 16's |
| foreign/sub/brief.md | untracked, inside an untracked directory | no `foreign/` path in `HEAD`, and still listed by `git status --porcelain --untracked-files=all` |

### Inventory

No new function, constant or file. The prompt's text changes, and the suite gains one fixture path
and one arm.

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
  empty record proceeds.
- observability — The refusal's text names the record and says the block must run as one
  invocation.
- risks — A path git C-quotes that the loop must stage stops the block, by design (§3).
- testing — S4's two arms, observed RED with the flag removed from step 5's listing and with the
  `${rec+x}` guard deleted.
- migration — None.
- user docs — N/A: the stage is internal to the harness.

## 6. Acceptance criteria

Criteria AC1 and AC2 run unit 16's scratch `node` probe and decode the `commit:specs:` prompt from
its `promptjson:` channel. Each staged break is made in a scratch COPY of the render.

- **AC1** — When the probe runs a call whose SPEC double authors `A-tB-1`, the decoded prompt's block
  lists with `git status --porcelain --untracked-files=all` at step 1 and again at step 5, its
  `${rec+x}` test precedes step 5's loop, and the prose says the block runs as ONE Bash invocation.
  Red when: the two listings differ, or the guard or the instruction is absent. Staged: the flag
  deleted from step 5's listing in the copy makes the two listing lines differ.
- **AC2** — When the block extracted from AC1's decoded prompt runs in unit 16's scratch repository
  at a short path under `%TEMP%`, with foreign/sub/brief.md untracked beside unit 16's two foreign
  paths, it exits 0, `git ls-tree -r --name-only HEAD` names no path under `foreign/`, and
  `git status --porcelain --untracked-files=all` still lists foreign/sub/brief.md. With step 1's
  assignment line deleted from the extracted block, it exits non-zero naming the record, and
  `git rev-parse HEAD` is unchanged.
  Red when: foreign untracked work is committed, or a split block commits. Staged: the run over the
  copy without the flag puts foreign/sub/brief.md in `HEAD`; the run with the guard deleted and
  step 1's line deleted moves `HEAD` and commits the foreign paths.
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

New arm: tools/workflows/unattended-build.test.sh · the extracted block with step 1's assignment deleted refuses and leaves HEAD unmoved; stage the ${rec+x} guard deleted · the suite's floor rises by the arms added

The close runs the legs and the suite. A pass runs the probe and the scratch repository of §6 as its
check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from findings 22 and 17 of the round-1 spec audit of
  units 16 to 19, grounded against unit 16 rev-2 and a two-listing probe on node `a`.

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
