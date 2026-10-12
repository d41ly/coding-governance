# TOOL-aTrimmedHook-5 — under LIVE_LANDED_UNCLOSED the classifier renders when anything outside its pathspec is staged

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-KICK-aTrimmedHook-1-runlog-2270b345.md](../build/2026-10-11-build-KICK-aTrimmedHook-1-runlog-2270b345.md) | journal | KICK-aTrimmedHook-1 TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 TOOL-aTrimmedHook-3 TOOL-aTrimmedHook-4 TOOL-aTrimmedHook-6 TOOL-aTrimmedHook-7 |
| [2026-10-11-build-TOOL-aTrimmedHook-5-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aTrimmedHook-5-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aTrimmedHook-5-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-5-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's H2 and M4, one defect at two grades. With `LIVE_LANDED_UNCLOSED=1`, which this
repository sets, `LIVE.md`'s Landed-unclosed column comes from the drift-audit kit's grep over tracked
product source, its conf and its kit, none of which the classifier diffs. A commit staging a
non-structural memory edit beside a source line that first cites a unit id now skips a render that
would have gone red. This unit makes the classifier render whenever the key is on and anything outside
its memory pathspec is staged.

## 2. Scope (IN)

- **S1 — the wider staged read, only under the key.** In `tools/memory-tree/gen_build_index.py`,
  when the conf's `LIVE_LANDED_UNCLOSED` is `1`, `check_staged_render` lists the staged set with no
  pathspec, and any staged path outside the memory root, the conf and the kit answers "render" with a
  reason naming the key. With the key blank, the pathspec and the answer are as before. Observed by
  AC1 and AC2.
- **S2 — the arms.** `test_staged_render` gains two arms in a fixture whose conf sets the key: a
  source file staged beside a non-structural memory edit renders, and the same pair with the key blank
  skips. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- **N1** — no narrower predicate over the drift kit's `EVIDENCE_GLOBS`: reading that declaration here
  would be a second reader of the drift kit's rule, and the coarse rule costs only a render on a
  commit that mixes source and memory.
- **N2** — a commit staging only product source still never reaches check 9, because the pre-commit
  hook runs the hygiene leg only when `memory/**` is staged; that is pre-existing.
- **N3** — no change to `read_landed_unclosed` or the render.

### Edges

none

## 4. Design

`read_landed_unclosed` reads the key as blank (off) or `1` (on) and refuses anything else; the
classifier reads it the same way and treats any other value as on, since a render is the safe answer
and the render itself will refuse the value. Under the key, the name-status call drops its pathspec,
so the one `git diff` lists every staged path; the existing loop already classifies memory, conf and
kit paths, and a path matching none of them now returns "render" instead of being out of view. No
extra process is started: the same one call, wider.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`

### Rollout

Order 4, after TOOL-aTrimmedHook-4 in the same file; TOOL-aTrimmedHook-7 follows.

### Alternatives rejected

- **Diff the drift kit's evidence globs, conf and kit only.** More precise, but it re-reads another
  kit's declaration, which is the two-readers class; the review offered both and named the coarse one.

## 5. Production-readiness checklist

- security — N/A — a wider read of the same index.
- perf / scale — none: the same single `git diff`, without a pathspec.
- error / empty / loading states — the key blank keeps the BASE behavior of this function.
- observability — the render-owed reason names the key and the path.
- risks — under the key, every commit mixing source and memory renders; that is the cost of the
  render reading source.
- testing — AC1 and AC2 are `--selftest` arms.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `gen_build_index.py --selftest` runs, the arm whose fixture conf sets
  `LIVE_LANDED_UNCLOSED=1` and stages a product-source file beside a no-id memory edit sees a render owed; with
  the key read as blank, the same arm sees a skip, which is the arm observed RED.
  Red when: the arm sees a skip with the key on.
  cost: one fixture repo; seconds.
- **AC2** — When `gen_build_index.py --selftest` runs, the arm staging the same pair with the key
  blank sees a skip.
  Red when: it sees a render owed, which would mean the key no longer gates the wider read.

## 7. Gates

`build-index selftest` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: tools/memory-tree/gen_build_index.py test_staged_render · covers AC1 AC2 · the key read as blank · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from the closing review's H2 and M4.

## 10. Reuse audit

The seam is `check_staged_render`'s own name-status call; the key is read as `read_landed_unclosed`
reads it. `python tools/codebase-map/reuse_lookup.py "render inputs outside the memory root"` returned
only name-stem matches. Recall named `TOOL-aMendedFleet-13`, which introduced the key and the
product-source read.

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
