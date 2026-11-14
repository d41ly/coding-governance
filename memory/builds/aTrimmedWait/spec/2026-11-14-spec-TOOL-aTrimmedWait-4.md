# TOOL-aTrimmedWait-4 — `gen_build_index.py --write` writes only the artifacts whose bytes moved

**Status:** CLOSED · rev-3 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 4 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aTrimmedWait-4-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aTrimmedWait-4-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md) | research | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-4-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-4-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-4-ruling.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-4-ruling.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`gen_build_index.py --write` rewrites every artifact it renders, 3206 files on this tree, though <!-- PINNED 2026-11-14 -->
a commit's change moves a handful and a clean tree moves none. Rewriting them all costs 16.8 s,
where comparing them first costs 0.8 s (PINNED, §4). This unit makes `--write` write only what
moved, so every caller pays for its own change and the tree it leaves is byte-identical to today's.

## 2. Scope (IN)

- **S1** — `cmd_write` writes the as-built view only when its bytes moved, and writes only the
  artifacts `derive_moved_artifacts` names, on the plain path as well as the staged one. The
  `staged` flag then selects the declines and the staging alone. Observed by AC1, AC2, AC3.
- **S2** — The summary line becomes `build-index: wrote <n> artifact(s), <k> unchanged`, where
  `<n>` counts the files written and `<k>` the rendered artifacts left in place. Observed by AC1.
- **S3** — A changed tree rendered by this unit's `--write` is byte-identical to the same tree
  rendered by the base's. Observed by AC4.
- **S4** — The acceptance ledger records `--write` on a clean tree, timed before and after on
  node a. Observed by AC5.

## 3. Non-goals (OUT)

- No change to what `plan()` renders, or to `--check`, `--check --staged` or `--write-staged`'s
  declines.
- No change to orphan removal. An orphaned ledger shard is still deleted on every `--write`.
- No cache of any reader's result across runs, and no change to the readers in other kits. §8 F1
  holds that choice.
- No reach-scoped render. §8 F1 holds that choice too.
- No kit version bump. The build's rule moves versions once, after the last code move.

### Edges

- **consumes-from** `TOOL-aTrimmedWait-3` — `derive_moved_artifacts` and the `staged` parameter of
  `cmd_write`. Without them this unit has no compare to route the plain write through and would
  write a second one.

## 4. Design

### The change

Today `cmd_write` writes the view whenever it is armed
(`tools/memory-tree/gen_build_index.py@5a0864b8:3225`). It then writes every rendered artifact in
a loop over `artifacts.items()` (`tools/memory-tree/gen_build_index.py@5a0864b8:3228`), and
prints `build-index: wrote {len(artifacts)} artifact(s)`
(`tools/memory-tree/gen_build_index.py@5a0864b8:3235`). After TOOL-aTrimmedWait-3, the staged
path already writes only `derive_moved_artifacts(root, artifacts)` and a moved view. This unit
removes the condition that keeps the plain path on the full loop. The two paths then write the
same set, and differ only in the declines before the render and the `git add` after it.

The view is still written BEFORE `plan()`. `plan()` renders the coverage regions from
`DESIGN_VIEW`, so one `--write` stays a fixed point. A view left in place has the bytes it would
have been given (`tools/memory-tree/gen_build_index.py@5a0864b8:3216`).

### Why the outcome is byte-identical

`derive_moved_artifacts` compares each file's bytes with the UTF-8 encoding `write_text` writes
(`tools/memory-tree/gen_build_index.py@5a0864b8:296`). A file it leaves in place therefore
already holds the bytes the base would have written. A CRLF copy of a rendered file is moved by
that compare and rewritten to LF, as the base rewrites it. A text compare through `read_text`
would leave it in place, since that reader normalises CRLF
(`tools/memory-tree/tree_lib.py@54a65cd4:418`), so AC3 is the case that tells the two apart. A
missing file is moved. A file that cannot be read is moved too, and the write then fails or
succeeds exactly as it does today.

What changes is the mtime of every file left in place. No reader in this repository reads an
artifact's mtime, and git re-hashes a file only when its stat data moved, so fewer files are
re-hashed by the next `git status` (UNVERIFIED as a time; not measured).

### The summary line

No reader parses `build-index: wrote … artifact(s)`. A search of `tools/`, `skills/` and
`.githooks/` for the phrase on 2026-11-14 found only the print itself. The new line keeps the
`build-index: wrote` prefix and adds the unchanged count, so a person can tell a no-op render
from one that moved files.

### Measurements (PINNED, node a, 2026-11-14)

- `plan()` renders 3207 artifacts in 47.5 s in-process. `gen_build_index.py --check` takes 42.5 s
  wall.
- Of the 3206 written by a scratch `--write`, rewriting them all takes 16.8 s, and comparing them
  first takes 0.8 s, with 0 moved on a clean tree. The scratch copy was under the session's
  scratch directory on node a, so Defender's per-file cost there is the worktree's.
- The rest of the render's 47.5 s is in readers this unit does not touch: `collect()` 11.1 s,
  of which the per-build scans of the tracked list are 3.3 s and the rosters 8.0 s;
  `read_carries_coverage` 15.6 s, in `tools/check-spec-tokens.py`; `read_landed_unclosed` 8.6 s,
  in the drift-audit kit.

### Inventory

| Minted | Kind | Graded by |
|---|---|---|
| `test_write_moved` | selftest function | `lexicon naming predicates`, cell `py.function` |

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **Compare by `read_text`.** It normalises CRLF, so a CRLF artifact would be left in place where
  the base rewrites it, and the tree would differ from the base's.
- **Compare by mtime or by a stored hash.** Either answers from state the render did not read, and
  a hand edit that kept the size and mtime would read unmoved. Reading the bytes costs 0.8 s here.
- The two mechanisms §8 F1 names are not rejected here. They are the owner's choice.

## 5. Production-readiness checklist

- security — No new write path. The write set shrinks to a subset of today's, chosen by a
  compare of bytes this process reads.
- perf / scale — A clean `--write` saves the 16.8 s write half and keeps the 47.5 s render. A
  changed tree writes only its moved files. Every caller benefits: the build harness's spec stage,
  `--new-build`, `--write-staged` and a person's render.
- error / empty / loading states — A missing or unreadable artifact counts as moved and is
  written, as today. An empty render writes nothing and prints `wrote 0 artifact(s)`.
- observability — The summary line names both counts.
- risks — A caller that relied on every artifact's mtime moving would see fewer move. None is
  known in this tree. The search above is the evidence.
- testing — AC1 to AC3 are generator runs in a fixture repository. AC4 compares two renders of
  one clone. AC5 times a clone. The arm of §7 repeats AC1 to AC3.
- migration — None. The tree `--write` leaves is the tree it left before.
- user docs — The `gen_build_index.py` row of `tools/memory-tree/README.md` says that `--write`
  writes only the artifacts whose bytes moved. No page under `help/` describes `--write`'s write
  set, and `help/reference/drive.md` shows the command only.

## 6. Acceptance criteria

`<f>` is a fixture repository under `%TEMP%/<short-name>`. It is built by the generator's own
`_fixture` helper, rendered with `--write` and committed. `<gbi>` is
`tools/memory-tree/gen_build_index.py` in this worktree, run with `<f>` as the working directory.

- **AC1** — When `python <gbi> --write` runs again in `<f>`, it exits 0 and prints
  `build-index: wrote 0 artifact(s)`, followed by the unchanged count. The `st_mtime_ns` of every
  tracked file under `<f>` is the value recorded before the run.
  Red when: an unmoved artifact is rewritten, so an mtime moves. At base the line reads
  `wrote <m> artifact(s)` with `<m>` every artifact, and each artifact's mtime moves.
- **AC2** — When the spec's status token `INPROGRESS` in `<f>` is changed to `DEFERRED` and
  `python <gbi> --write` runs, the files whose `st_mtime_ns` moved are exactly the spec plus the
  paths `git status --porcelain` then reports as rendered. Afterwards `python <gbi> --check` exits
  0.
  Red when: a moved artifact is left unwritten, so `--check` exits 1.
- **AC3** — When a rendered build README in `<f>` is rewritten with CRLF line endings and
  `python <gbi> --write` runs, that file's bytes afterwards hold no `\r\n` and equal the base's
  render of it.
  Red when: the compare normalises CRLF, so the file keeps its CRLF bytes and is counted
  unchanged.
- **AC4** — When a clone of this repository at the unit's commit has one spec's status changed,
  and `--write` runs once from this unit's generator and once from a copy of the generator at base
  `846d51d3`, each from a clean checkout of that change, `git diff --binary` after each, together
  with the untracked files each adds, is byte-identical between the two runs.
  Red when: any artifact differs between the two renders.
  cost: two full renders, about two minutes.
  fixture: one clone under `%TEMP%/<short-name>`, and the base kit through `git worktree add` at
  `846d51d3` beside it; neither is in the tree today.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --write` runs on a clean clone,
  timed once with the base generator and once with this unit's, the ledger records both wall times
  and both summary lines.
  Red when: the two timings are not the same command on the same tree.
  cost: two full renders.
  figure: both times are DERIVED at observation. The expected saving is the 16.8 s of §4, PINNED
  on 2026-11-14.

## 7. Gates

`build-index selftest` · `memory hygiene` · `lexicon naming predicates` · `tier2-review self-test` · `policy fixtures`

The first three grade this unit's change. The last two are owed by the guard the generator's path
trips. The main loop runs the merge bar once, at the close. No leg is added.

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 · `test_write_moved` over the fixture of §6, with the second render, the status flip and the CRLF rewrite each staged in turn; RED at base, where every artifact is rewritten and the summary line has no unchanged count · none

What this arm does not check: the base parity of AC4 over the real tree, and the time of AC5.

## 8. Open questions

- **F1 — Which mechanism does this unit build: the moved-only write measured here, or the
  reach-scoped render the build README's roster names?** The roster reads "`--write` re-renders
  only the regions its changed inputs reach". The measurement of §4 says what each candidate can
  save on this tree.
  - (a) The moved-only write, as §2 states. It saves the 16.8 s write half on every `--write`,
    adds no state, and leaves a byte-identical tree by construction.
  - (b) A reach-scoped render: map each changed input to the regions it reaches and render only
    those. Two readers read the whole tree. The rosters read every memory file's ids
    (`tools/memory-tree/gen_build_index.py@5a0864b8:831`), and the Landed-unclosed column globs
    every spec under `builds/*/spec/` (`tools/drift-audit/drift_report.py#signal_spec_status`).
    A spec status change, the commonest commit, still pays both. The coverage join reads only the
    chain builds' specs (`tools/check-spec-tokens.py#read_carries_specs`), so a change outside
    them could skip its 15.6 s, and the render loop's share, under 10 s, could shrink. Both need a <!-- PINNED 2026-11-14 -->
    second statement, beside the renderer, of what every region reads. A wrong entry there
    becomes a silent stale artifact. And a roster kept from the last render is the
    output-read-as-input `rosters()` forbids.
  - (c) A persistent cache of each per-file parse, keyed on the blob id, kept under the git
    directory. It would cut most of the 8.0 s of rosters on a warm run. The 24.2 s in the two
    other kits' readers would stay, and the cache is a new state file every reader must key
    correctly.
  - Recommendation: (a), which this spec is written to. It is the one candidate whose saving
    holds on every commit and whose output cannot differ from the base's. (c) and per-kit caches
    for the coverage and Landed-unclosed readers are each one mechanism, so each would be its own
    unit, and they are worth filing as an ask with the §4 figures. (b) fails the build's rule that
    a scoped answer must prove its inputs, because its reach map is an authored second answer.
  - RESOLVED (owner, 2026-11-14): (a), the moved-only write.

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.
- rev-2 · 2026-11-14 · §8 F1 · ratified · F1 resolved by the owner at (a), the moved-only write,
  recorded in 2026-11-14-prompt-TOOL-aTrimmedWait-4-ruling.
- rev-3 · 2026-11-14 · §1 §8 · each fact the writing-practice leg's pinned-facts arm named is pinned
  on its line, with no change of meaning, by `2026-11-14-prompt-TOOL-aTrimmedWait-5-writing-practice`.

## 10. Reuse audit

The seam is TOOL-aTrimmedWait-3's `derive_moved_artifacts` and the `staged` parameter it gives
`cmd_write` in `tools/memory-tree/gen_build_index.py`. This unit routes the plain write through
the compare that unit builds, rather than writing a second one. `tools/codebase-map/reuse_lookup.py`
for "write only the generated files whose bytes changed" ranked `write_text` in this same file
and name stems elsewhere (`write_file`, `write_change`, `write_record`). Each of those writes one
file unconditionally, so none is a compare-then-write seam. Recall returned no record of a
moved-only write. Its nearest hit, the TOOL-dLinkedLibrary-5 scout, names `cmd_write`'s
`artifacts` dict and byte compare as the render's seam, which is the one used here.

Recall terms used: pre-commit check-9 gen_build_index staged render write artifacts stage index
drift refused unchanged bytes
