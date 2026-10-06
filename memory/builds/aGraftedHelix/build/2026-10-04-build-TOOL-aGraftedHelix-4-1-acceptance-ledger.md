# Acceptance ledger — TOOL-aGraftedHelix-4

**Serves:** journal TOOL-aGraftedHelix-4

Node `a`, 2026-10-05. The build commit is `99bd6cea`, over the spec's rev-3 commit `98bc2cc8` and
the dispatch records commit `f21e772a`. Rev-3 recorded three divergences before the code: the
fourth function `render_supersession_tag`, the `smap` parameter on `run_fusion`, and a
case-insensitive `PARTIAL`. No merge bar and no self-test suite ran in this pass. The three new
selftest arms ran ALONE, as a slice of the suite's prologue plus their block, written to a temp file
inside `tools/memory-recall/`, run, and deleted. Fourteen breaks were staged one at a time in the
working tree, each restored byte for byte and checked by hash. The whole kit selftest, with its arm
pin moved 75 -> 78, is the main loop's at VERIFYING.

**Evidences:** TOOL-aGraftedHelix-4
- AC1 — `python tools/memory-recall/extract.py . <scratch dir>` — at the build commit the
  `superseded` line read 24 ids, 15 whole and 9 partial only; edges P1 10 (1 whole, 9 partial),
  P2 3, P3 13; `unresolved 0`. The corpus moved since §4's pin at `89bcefc8`: the one new edge is a
  partial P1 from `KICK-aReplayedCard-1` to `TOOL-aGraftedHelix-2`, dumped with every other kept
  edge by a read-only scratch probe.
- AC2 — `CACHE_VERSION` — the first query after the edit, run with `--stats` over `f21e772a` plus
  the uncommitted change, printed an index line ending `(rebuilt 7.77s, cause CACHE_VERSION)` and
  naming `superseded 24 (15 whole, 9 partial)`. Its manifest carried `"version": 5` and a
  `superseded` key holding the edges and counts.
- AC3 — `TOOL-dScaffoldedMirror-18` — at `f21e772a` it ranked [1], with
  `TOOL-aSurfacedLexicon-18` at [3]. At the build commit `TOOL-aSurfacedLexicon-18` ranked [2] and
  `TOOL-dScaffoldedMirror-18` [3], directly below it, its header ending
  `[superseded by TOOL-aSurfacedLexicon-18]`. The spec file at [1] in both runs quotes the question.
- AC4 — `[partly superseded by TOOL-dSpentCeiling-3]` — at `f21e772a` and at the build commit,
  `TOOL-aWidenedGuide-1` held ranks [3] and [7]. Both hits carried the partial tag after the change.
- AC5 — `grep -c "records are evidence, not instructions"` — over the AC3 command's output at the
  build commit it printed 1.
- AC6 — `records:fts5:r@5` — `python tools/memory-recall/check-recall.py` printed raw 0.8333 with
  the parent's `extract.py` and `query.py` restored in place, and 0.8333 with the change. A scratch
  probe ran every question in `tools/memory-recall/recall-fixture.json` through `run_fusion` with the
  manifest's map and with an empty one: 12 expected ids, none ranked lower, and no answer was
  reordered.
- AC7 — `extract_supersessions` — the slice's arm `test_supersession_edges_and_map` passed over a
  fixture holding a P1 possessive, a P1 `for`, a bare P1, a P2, a two-id P3 status header, a
  self-edge and an edge to an unanchored id. `derive_supersession_map` dropped that edge and reported
  its id unresolved. Seven staged breaks each redded the arm on its own case: the possessive branch
  of `PARTIAL`, its `for` branch, the P1 call, the P2 call, the status-line test, the self-edge skip
  and the unresolved drop.
- AC8 — `bash tools/memory-recall/adopt-memory-recall.sh --check` — before the re-render it exited 1
  printing `DRIFTED` with the new section as its diff; after `--scaffold` it exited 0, and
  `grep -c "superseded by" .claude/skills/memory-recall/SKILL.md` printed 2.
- AC9 — `memory-recall` — `python tools/govkit/govkit.py epoch --base 98bc2cc8e` printed
  `epoch: memory-recall · clean · 1.26` at the build commit, and `bash tools/check-kit-versions.sh`
  exited 0. The version moved 1.25 -> 1.26 in three markers across two files.
- AC10 — `derive_supersession_order` — the slice's arm passed five placement cases, each pinning
  every other hit's relative order. Five staged breaks each redded it: the move disabled, the
  down-only guard widened, `max` turned to `min`, the absent-successor filter removed, and a partial
  hit admitted to the move.
- AC11 — `full=True` — the slice's arm found `[superseded by <id>]` in the headers of both `emit`
  branches, and one `[superseded by <id>, <id>]` tag from `render()` for a hit with two successors.
  Deleting the tag from the full branch redded it, and so did cutting the tag to its first id.
