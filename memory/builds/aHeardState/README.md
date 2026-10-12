---
slug: aHeardState
node: a
opened: 2026-10-11
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8
---

# aHeardState — the turn end refuses a final message without the BUILD/SPEC pair, and a transcript measure counts the prose

## The problem this build exists to solve

The charter makes the `BUILD`/`SPEC` pair mandatory in every final message while a build is in
progress, and nothing checks it. Session 86a064cd (unattended build aPrimedIndex, node a) emitted no
micro-format at all across 1,162 assistant entries, before and after a compaction. The owner's prose
is the mandate, recorded under [prompts/](prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md).

## Expected improvements

- A session routed to a live build cannot end its turn without the pair as adjacent bare list items.
- A commit made since the previous turn end is reported by a `committed` line, or the stop is refused.
- The pair's grammar is read from the charter's micro-format block, so the hook restates nothing.
- Any transcript can be measured for narration share, interjections and pair emission, after the fact.

## Detriments if this is not built

- The state block stays a documented habit, and the first `minimal-prose` reading drops it again.
- An owner reading a run's final messages cannot tell which build, step or unit the run is on.
- Nobody can say how often the rule is broken, because no instrument counts it.

## Build-level rules

- **Classification**: two Tier-2 units, both MISSING at open; one mechanism each (M2).
- The run does not land: the owner asked to be asked first, so it closes into an owner-landing hand-off.
- No change to the charter template or its rules; the hook reads the rendered charter.
- One kit-version bump per kit touched, after that kit's last code move.

## Parked decisions

*None at open.*

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aHeardState-1` | `format-guard`, a Stop hook that refuses a final message missing the pair or a `committed` line |
| 2 | `TOOL-aHeardState-2` | `runlog.py prose`, a report-only measure of a session's prose and pair emission |
| 3 | `TOOL-aHeardState-3` | the format-guard self-test leg's subject pin and budget row (review id 8) |
| 4 | `TOOL-aHeardState-4` | the leg's guard narrowed to the hook files (review id 9) |
| 5 | `TOOL-aHeardState-5` | the leg's guard covers the runlog files its parity arm reads (review id 10) |
| 6 | `TOOL-aHeardState-6` | a bug-class record for a held suite whose guard misses a sibling kit (review id 14) |
| 7 | `TOOL-aHeardState-7` | the hook header states the continuation-commit behaviour, and an arm pins it (review id 3) |
| 8 | `TOOL-aHeardState-8` | the closing review's eighteen minors, batched |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 8 unit(s) · node a · opened 2026-10-11 · streams tooling
ids TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aHeardState-1 — format-guard: the turn end refuses a final message without the BUILD/SPEC pair or a committed line](spec/2026-10-11-spec-TOOL-aHeardState-1.md) | 1 | 2 | INPROGRESS | rev-2 | 2026-10-12 |
| [TOOL-aHeardState-2 — runlog prose: a transcript measure of narration, interjections and pair emission](spec/2026-10-11-spec-TOOL-aHeardState-2.md) | 2 | 2 | INPROGRESS | rev-2 | 2026-10-13 |
| [TOOL-aHeardState-3 — the format-guard self-test leg gets its subject pin and its budget row](spec/2026-10-13-spec-TOOL-aHeardState-3.md) | 3 | 1 | SPECCED | rev-1 | 2026-10-13 |
| [TOOL-aHeardState-4 — the format-guard self-test guard names the hook files, not the whole hooks directory](spec/2026-10-13-spec-TOOL-aHeardState-4.md) | 4 | 1 | SPECCED | rev-1 | 2026-10-13 |
| [TOOL-aHeardState-5 — the format-guard self-test guard covers the runlog files its parity arm reads](spec/2026-10-13-spec-TOOL-aHeardState-5.md) | 5 | 1 | SPECCED | rev-1 | 2026-10-13 |
| [TOOL-aHeardState-6 — the bug-class checklist names a held suite whose guard misses a sibling kit it reads](spec/2026-10-13-spec-TOOL-aHeardState-6.md) | 6 | 1 | SPECCED | rev-1 | 2026-10-13 |
| [TOOL-aHeardState-7 — the format-guard header states what happens to a continuation's commits, and an arm pins it](spec/2026-10-13-spec-TOOL-aHeardState-7.md) | 7 | 1 | SPECCED | rev-1 | 2026-10-13 |
| [TOOL-aHeardState-8 — the closing review's mediums and lows: fixtures that can see the defects, and three small fixes](spec/2026-10-13-spec-TOOL-aHeardState-8.md) | 8 | 1 | SPECCED | rev-1 | 2026-10-13 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 4 record folder(s).

Ids no record names: TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8.

Ids no `spec-audit` record has ever named: TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aHeardState-1` | no |
| 2 | `TOOL-aHeardState-2` | no |
| 3 | `TOOL-aHeardState-3` | no |
| 4 | `TOOL-aHeardState-4` | no |
| 5 | `TOOL-aHeardState-5` | no |
| 6 | `TOOL-aHeardState-6` | no |
| 7 | `TOOL-aHeardState-7` | no |
| 8 | `TOOL-aHeardState-8` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
