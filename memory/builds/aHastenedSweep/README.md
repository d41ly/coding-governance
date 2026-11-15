---
slug: aHastenedSweep
node: a
opened: 2026-11-15
streams: tooling
roster: TOOL
ids: TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4
authorized-by: prompt
status: OPEN
---

# aHastenedSweep — the memory-hygiene runner's per-item rescans removed, every verdict byte-identical

## The problem this build exists to solve

The `memory hygiene` leg is the bar's costliest leg on node a, and every `--only 12` or `--only 25` a
spec writer runs pays the same cost. An analysis on 2026-11-15 found most of it in rescans repeated
once per item where once in total would do: check 25's by-name pass copies every reader line per
unresolved token, `gotchas.py` recomputes basenames per anchor and path pair, and `corpus_ids.py`
rebuilds its roots per citation and re-enters the shell for a set its parent already holds. The
prompt and its brief are in `prompts/`.

## Expected improvements

- Check 25's by-name pass skips a line that cannot hold the token before copying it.
- Checks 13 to 19 compute each basename and root set once, and share one corpus walk.
- The shell hands `corpus_ids` the index set it already computed.

## Detriments if this is not built

- Every full bar and push keeps paying minutes of the hygiene leg for repeated work.
- Spec writers keep spending hours on `--only 12,25` reruns.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, Tier-2: each changes a shipped kit's checker in `tools/memory-tree/`.
- Every verdict stays byte-identical: no check weakened, no population skipped, no exemption added.
- `memory/builds/dDeclaredLoop/`, the live run's worktree `unattended-declared-loop-d56bf0`, its branch and its run-state file are not touched.
- No spec audit: not declared (owner, at kickoff).
- R5 (the commit recipe and the render stamp), R6 and the spec-writer prompt scope are out: owner decisions.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aHastenedSweep-1` | check 25's by-name END loop tests `index()` before `test_whole_token` |
| 2 | `TOOL-aHastenedSweep-2` | `gotchas.selectable` computes basenames once, and `corpus_ids.walk` computes `_roots` once per walk |
| 3 | `TOOL-aHastenedSweep-3` | the hygiene shell hands `corpus_ids.py --check` its index set when checks 1 to 5 recorded no failure |
| 4 | `TOOL-aHastenedSweep-4` | checks 13 to 16 and 17 to 19 run in one Python process over one frozen, memoized walk |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
