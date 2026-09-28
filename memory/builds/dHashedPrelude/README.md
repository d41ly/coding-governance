---
slug: dHashedPrelude
node: d
opened: 2026-09-28
streams: tooling
roster: TOOL
ids: TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3
spec-audit: 2026-09-28
authorized-by: prompt
---

# dHashedPrelude — the memory-recall selftest's live-log guard is made able to fail

## The problem this build exists to solve

`tools/memory-recall/selftest.py` guards this repository's live query log, because a gate that
writes to the instrument it measures is how upstream's log came to be 96% self-inflicted refusals.
The suite hashes `<git-common-dir>/recall/queries.jsonl` before and after itself. The `before` hash
is taken at the top of `main()`, and every arm has already run by then: `check()` calls `fn()`
inside the decorator, at module import. The two hashes bracket nothing, so the row `the live query
log is byte-identical after this run` cannot fail. Observed on 2026-09-22 on node `d`: four fixture
queries reached the real log as qids 592-595 and the row still reported ok.

## Expected improvements

- An arm that writes to the live query log reds the suite instead of passing beside it.
- The ordering the guard depends on is itself gated, so it cannot regress unnoticed.
- `tools/memory-recall/README.md` stops publishing a selftest count four vintages stale.

## Detriments if this is not built

- The live log keeps accumulating synthetic rows, and every recall figure is measured over it.
- The next contributed arm calling `query.main` in process is invisible, as the last one was.
- A reader who trusts the green row has no reason to hash the log by hand, and the memory note
  telling them to do so has to stay.

## Build-level rules

- **Every unit observes its own RED first.** A guard nobody has seen fail is an assertion about
  nothing. The staged break is described in the unit's acceptance, observed, then unstaged.
- **No arm may write to the real query log, not even to prove this works.** The break is staged
  into the working tree, run once, and reverted; nothing that writes to the log is committed.
- **Every run of the suite is bracketed by an external `sha256sum` of the live log**, and the two
  readings go in the unit's acceptance ledger. The guard under repair does not grade itself.
- **The kit version moves in the commit that makes the last engine-byte change**, never in an
  earlier one: `govkit epoch` reds when the last bump precedes the last move.
- **No count of a derived population is written in prose.** The defect being fixed in unit 3 is
  that rule broken once already, in the README of the file this build edits.

## Parked decisions

- **The kit version bump is the owner's call, taken against the recommendation.** `selftest.py` is
  declared `role = "project-owned"` in `tools/memory-recall/kit.toml`, so it ships to no adopter
  and `govkit epoch` (which grades `engine`, `seed`, `rendered` and `merged`) never asks for a bump
  on its account. The bump also enters `Conf.digest()` and invalidates every node's warm recall
  cache. The owner ruled 1.12 to 1.13 anyway on 2026-09-28, on the ground that an edit inside the
  kit directory is a kit edit. Unit 3 carries both sides and `epoch --base 3cf05f29` is run as an
  observation either way. The landing reconcile then carried it to 1.19: `aRepatriatedFork` had
  taken the same kit to 1.18 on `main` while this build ran, so the contested bump cost a merge
  rather than a cache rebuild.
- **`tools/lexicon/README`'s half of `TOOL-aProbedToolkit-14` stays open.** Unit 3 closes only the
  memory-recall half, because that is the file this build already edits. The row is updated to say
  which half drained.
- **The selftest summary line still counts rows, not arms.** It prints `len(_checks)`, which is 78
  against 73 declared arms; the declared count lives only in the pin row's detail. Two spec
  criteria reached for the summary line and had to be corrected. Option seen: print both figures.
  Refused here because it changes an output line the upstream fork's own gate leg parses, which is
  a fourth unit's worth of blast radius. `TOOL-dHashedPrelude-2` §3.
- **`tools/**/*.py` carries no `eol=lf` pin.** The blob is LF and a Windows checkout is CRLF, so
  the same anchor sits at two different byte offsets; a spec at rev-2 pinned the worktree pair and
  called them measured at BASE. Option seen: pin and renormalize. Refused here because the
  renormalize touches every kit. `TOOL-dHashedPrelude-2` §4.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dHashedPrelude-1` | 2 | the live-log baseline is captured at module scope above the first decorated arm, and the guard's comment states what it does not check |
| 2 | `TOOL-dHashedPrelude-2` | 2 | two arms: one reads the suite's own source and reds when the baseline does not precede the first decorated arm, when `main()` does not read it, or when the append is still conditional; the other drives the verdict over its five states. The arm-count pin moves 71 to 73 |
| 3 | `TOOL-dHashedPrelude-3` | 1 | the kit's published facts are re-derived: the README stops stating a selftest count, the kit version moves with the shipped bytes, and the build's two deferrals get backlog rows |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node d · opened 2026-09-28 · streams tooling
ids TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dHashedPrelude-1 — the live-log baseline is captured above the first decorated arm](spec/2026-09-28-spec-TOOL-dHashedPrelude-1.md) | 1 | 2 | CLOSED | rev-6 | 2026-09-28 |
| [TOOL-dHashedPrelude-2 — two arms red when the live-log guard stops bracketing the arms](spec/2026-09-28-spec-TOOL-dHashedPrelude-2.md) | 2 | 2 | CLOSED | rev-6 | 2026-09-28 |
| [TOOL-dHashedPrelude-3 — the kit's published facts stop being a typed count, and its version moves](spec/2026-09-28-spec-TOOL-dHashedPrelude-3.md) | 3 | 1 | CLOSED | rev-4 | 2026-09-28 |
<!-- /gen:build-units -->

Records: 5 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dHashedPrelude-1` | no |
| 2 | `TOOL-dHashedPrelude-2` | no |
| 3 | `TOOL-dHashedPrelude-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
