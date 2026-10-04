# TOOL-aMendedFleet-102 — the two drifted inline `resolve_kit_dir` copies match their canonical source

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · order 103

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The held `python resolver (behaviour + inline parity + idiom ban)` leg is red on every scheduled
run in the census (cause C6 of the held-red census journal). Its parity arm holds every inline copy
of `resolve_kit_dir` byte-identical to `tools/lib/resolve_kit_dir.py`. Commit `e40a24ddc` moved the
canonical copy from `.resolve()` to `.absolute()`, so a junction cannot move the anchor, and added a
`..`-part refusal on a receipt row. The copies in `tools/memory-tree/backlog.py` and
`tools/memory-tree/transition_audit.py` arrived by merge from node d's dDerivedDocket build carrying
the older block and were never re-synced. This unit re-syncs both copies, reusing node d's bytes.

## 2. Scope (IN)

- **S1** — The inline block in `tools/memory-tree/backlog.py` becomes byte-identical to the
  canonical block, by applying that file's hunk of node d's commit `d26a9fc1f`. Observed by AC1,
  AC2 and AC3.
  **Readers:** by name: `_resolve_anchor_at` in `tools/memory-tree/backlog.py` is the copy's one
  caller; the parity arm of `tools/lib/resolve-python.test.sh` spells the block by its marker.
  by value: the parity arm compares the block's bytes; `_resolve_anchor_at` reads the returned
  kit directory, which is unchanged for an anchor already absolute.
- **S2** — The inline block in `tools/memory-tree/transition_audit.py` becomes byte-identical to
  the canonical block, by applying that file's hunk of the same commit. Observed by AC1, AC2 and
  AC3.
  **Readers:** by name: `resolve_recall_kit` in `tools/memory-tree/transition_audit.py` is the
  copy's one caller; the same parity arm spells the block by its marker.
  by value: the parity arm compares the block's bytes; `resolve_recall_kit` reads the returned
  kit directory, which is unchanged for an anchor already absolute.

## 3. Non-goals (OUT)

- The other two files of `d26a9fc1f`, `tools/unattended/lib-unattended.sh` and
  `tools/unattended/unattended.sh`. They fix a different leg on node d's branch and are not this
  cause.
- Why a red parity leg could land. The leg is a held self-test, off the bar by the owner's ruling,
  so a drift is seen by the daily job after landing. That trade is recorded and is not this unit's.
- Any change to the canonical block or to the parity arm.
- Moving the memory-tree kit version. Both files are shipped bytes, so the close's
  `kit epoch (shipped bytes move, the version moves)` leg owes a bump, and the build moves every kit
  version it owes once, after its last pass.

### Edges

- **consumes-from** external — node d's `dUnstuckLanding` commit `d26a9fc1f` on
  `origin/branch/unattended-build-closing-f90fd9`, whose two Python hunks this unit applies so the
  later reconcile is identical hunks rather than a conflict.

## 4. Design

### Evidence

Read at base `7af5f564` and re-read at the branch head `34a99ad17`.

- Replaying the parity arm's own `blk` extractor (copied from `tools/lib/resolve-python.test.sh`)
  over every tracked file carrying the `resolve_kit_dir` open marker compares 66 copies against the
  canonical, one block per file. Exactly two differ from the canonical, the two named above, each by the same three lines: `Path(here)` calls
  `.resolve()`, the receipt hit calls `.resolve()`, and the hit test lacks `".." not in hit.parts`.
- The failed-job log of scheduled run `37196051126` carries exactly two `FAIL` lines for this
  suite, one naming each file, so this is the suite's only cause on that run.
- `git log -G` on the canonical file dates the move to `e40a24ddc`. Both copies were introduced by
  `3bd4e18b7`, a dDerivedDocket repair, and reached this line through merge `5cb052dab`.
- Node d's `d26a9fc1f` changes those three lines in each file and nothing else in them. Its commit
  message records the same leg red at `origin/main` `35438ba0` and re-synced. The `aGraftedHelix`
  branch still carries the drifted copies.
- Unit 5 (`TOOL-aMendedFleet-5`, CLOSED at `bc5df3709`) added three lines above the block in
  `transition_audit.py`, so the hunk's offset moves and its content does not.
- Both copies return the tree's `tools/memory-recall` directory from `tools/memory-tree` when called
  with an absolute anchor at the branch head. Both callers already pass a resolved `__file__`
  parent, so the change is behaviour-neutral on every install that is not reached through a
  junction or a receipt row carrying a `..` part.

### Mechanism

Apply the two Python hunks of `d26a9fc1f` with `git show d26a9fc1f -- <file>` piped to
`git apply`, one file at a time, and confirm each applied block equals the canonical block. No
hand edit, so the bytes are node d's.

### Files touched (estimate)

- `tools/memory-tree/backlog.py`
- `tools/memory-tree/transition_audit.py`

### Alternatives rejected

- **Hand-edit the three lines.** It produces the same block, but a hand edit can differ from node
  d's hunk in whitespace, and the reconcile would then conflict on bytes both sides meant to agree.
- **Import the canonical module instead of carrying the block inline.** `<prefix>/lib/` ships to no
  adopter, which is why every consumer carries the block inline (the canonical file's docstring).

## 5. Production-readiness checklist

- security — the re-synced block gains the canonical's refusal of a receipt row whose path carries
  a `..` part, so the copies stop following an escaping receipt row. No new surface.
- perf / scale — N/A: the same filesystem probes.
- error / empty / loading states — unchanged: the `LookupError` refusal is byte-identical.
- observability — N/A: no new output.
- risks — a receipt row the old copies followed through a `..` part is now skipped; the tree's own
  receipt has none, which AC3 observes.
- testing — AC1 to AC3 are direct and take seconds; AC4 is the held leg's own verdict.
- migration — N/A.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `git grep -c 'Path(here).resolve()' -- tools/memory-tree/backlog.py tools/memory-tree/transition_audit.py`
  runs, it prints nothing and exits 1.
  Red when: either copy keeps the old call; at base it counted 1 in each file.
  Staged break: restore `.resolve()` on that line of one file and the probe counts 1.
- **AC2** — When the parity arm's `blk` function, copied out of the python resolver suite that sits
  beside the canonical in `tools/lib/`, extracts the `resolve_kit_dir` block from `tools/lib/resolve_kit_dir.py` and from every file
  `git grep -l` finds carrying the open marker, every block compares equal, and at least one block
  is compared per file that probe lists.
  Red when: a copy differs; at base two of the blocks differed. Staged break: AC1's, which makes
  `tools/memory-tree/backlog.py` the one block that differs.
  figure: the file count is DERIVED at observation time from `git grep -l`; it was 67, the canonical
  included, at `34a99ad17`.
- **AC3** — When `python -B -c` imports `backlog` and `transition_audit` from `tools/memory-tree`
  and calls each module's `resolve_kit_dir` with `memory-recall`, `extract.py` and that directory's
  absolute path, both print the tree's `tools/memory-recall` directory.
  Red when: either raises `LookupError` or prints another directory, which would mean the re-sync
  changed what the callers resolve.
- **AC4** — When the held leg runs after landing, its two parity `FAIL` lines are gone; the remote
  observation is the first scheduled run of `.github/workflows/remote-ci.yml` after the landing,
  read with `gh run view --log-failed`, where the `python resolver` held job passes.
  Red when: either parity `FAIL` line still prints.
  permission: the leg is a held self-test, which no unit pass runs; the daily held job runs it on
  the hosted runner, and the main loop may run it on demand.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `transition-audit arms` · `memory-hygiene self-test` · `backlog migration selftest` · `verdict-epoch self-test` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: none · the existing parity arm is the arm, and AC1's staged break is what reds it · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the census journal's C6 row, the leg's failed-job log of
  run `37196051126`, a replay of the parity arm's extractor over the tree, and node d's `d26a9fc1f`.

## 10. Reuse audit

The seam is node d's commit `d26a9fc1f`, whose two Python hunks this unit applies unchanged, and the
canonical block in `tools/lib/resolve_kit_dir.py` they converge on. No code seam is added.
`python tools/codebase-map/reuse_lookup.py "inline copy of a canonical block kept byte-identical by a parity check"`
ranked `canonical_ctx`, `find_block` and `lf_pin_block` in `tools/govkit/govkit.py`, none of which
gates inline copies, and its header reports `.sh` unscanned, so it cannot see the parity arm. Recall
found that arm, the `PARITY_ROWS` table of `tools/lib/resolve-python.test.sh`, through the
`TOOL-aRepatriatedFork-47` spec's own reuse audit, and found the census row naming both files.

Where the report and the tree disagree: none. The census named both files and the `.resolve()`
call, and the replay at `34a99ad17` finds the same two blocks and a third differing line the census
did not name, the missing `..`-part test.

Recall terms used: `python tools/memory-recall/query.py "why must every inline resolve_kit_dir copy be byte-identical to the canonical and never call resolve" --terms "resolve_kit_dir inline copy canonical byte-identical parity drifted absolute resolve junction resolve-python.test.sh lib"`
