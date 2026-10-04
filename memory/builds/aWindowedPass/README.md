---
slug: aWindowedPass
node: a
opened: 2026-10-04
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aWindowedPass-1 TOOL-aWindowedPass-2 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 TOOL-aWindowedPass-5 TOOL-aWindowedPass-6
---

# aWindowedPass — check 23 grades the disjointness it exists for, and nothing else

## The problem this build exists to solve

Check 23 compares each dispatched pass's committed paths against the write set it declared, which
is the disjointness proof two CONCURRENT passes rest on. It grades every pass, though only 8 of this
repo's 397 dispatch groups ever held two. Hook-forced generated writes and subject-substring
attribution then count against a repo-global, shrink-only ceiling no run can repair, so builds
here and at adopters hold or abort. The owner's prompt is in `prompts/`.

## Expected improvements

- A pass that ran alone is reported, never counted.
- A write outside a declaration is refused at commit time, with the command that fixes it.
- Generated outputs are declared by the kits that generate them.
- A pass commit is named by a trailer, not by a subject substring.
- Each run is graded against zero on its own.

## Detriments if this is not built

- Unattended builds keep holding or aborting on check 23 for writes that collide with nothing.
- Each adopter keeps hand-measuring a ceiling and a generated-path list.
- One run's history keeps blocking another run's landing.

## Build-level rules

- Concurrent passes are graded at least as strictly as today; only solo passes are relieved.
- Reuse first: check 23's own subset test, `covers`, the dispatch rows and the pre-commit hook.
- Every new arm is observed RED on a staged break before it lands.
- Legacy run records keep their verdicts: a record without the new trailer is read the old way.
- No spec audit: none is owed; the closing diff review is the specs' first review.
- Classified at kickoff (M2): all five units MISSING; specced and built inline, in order.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWindowedPass-1` | 2 | check 23 counts only a pass whose window overlapped a sibling pass's |
| 2 | `TOOL-aWindowedPass-2` | 2 | a pass commit carries a `Pass:` trailer, and check 23 attributes by it |
| 3 | `TOOL-aWindowedPass-3` | 2 | a pre-commit step refuses an undeclared write of an open pass, naming the re-declare |
| 4 | `TOOL-aWindowedPass-4` | 2 | kits declare their generated outputs, and check 23 and `--dispatch` read the declarations |
| 5 | `TOOL-aWindowedPass-5` | 2 | each run is graded against zero; the repo-global ceiling is retired |
| 6 | `TOOL-aWindowedPass-6` | 2 | an amend of a committed pass is refused without a widening the close would not honour |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 6 unit(s) · node a · opened 2026-10-04 · streams tooling
ids TOOL-aWindowedPass-1 TOOL-aWindowedPass-2 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 TOOL-aWindowedPass-5 TOOL-aWindowedPass-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWindowedPass-4 — kits declare their generated outputs, and the unattended kit reads them](spec/2026-10-04-spec-TOOL-aWindowedPass-4.md) | 1 | 2 | CLOSED | rev-3 | 2026-10-04 |
| [TOOL-aWindowedPass-2 — a pass commit carries a `Pass:` trailer, and the legs attribute by it](spec/2026-10-04-spec-TOOL-aWindowedPass-2.md) | 2 | 2 | CLOSED | rev-5 | 2026-10-04 |
| [TOOL-aWindowedPass-1 — check 23 counts only a pass whose window overlapped a sibling pass's](spec/2026-10-04-spec-TOOL-aWindowedPass-1.md) | 3 | 2 | CLOSED | rev-4 | 2026-10-04 |
| [TOOL-aWindowedPass-5 — each run is graded against zero; the repo-global ceiling is retired](spec/2026-10-04-spec-TOOL-aWindowedPass-5.md) | 4 | 2 | CLOSED | rev-3 | 2026-10-04 |
| [TOOL-aWindowedPass-3 — a commit-time step refuses an open pass's undeclared write, naming the re-declare](spec/2026-10-04-spec-TOOL-aWindowedPass-3.md) | 5 | 2 | CLOSED | rev-4 | 2026-10-04 |
| [TOOL-aWindowedPass-6 — an amend of a committed pass is refused without a widening the close would not honour](spec/2026-10-04-spec-TOOL-aWindowedPass-6.md) | 6 | 2 | CLOSED | rev-2 | 2026-10-04 |
<!-- /gen:build-units -->

Records: 15 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aWindowedPass-1 TOOL-aWindowedPass-2 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 TOOL-aWindowedPass-5 TOOL-aWindowedPass-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aWindowedPass-4` | no |
| 2 | `TOOL-aWindowedPass-2` | no |
| 3 | `TOOL-aWindowedPass-1` | no |
| 4 | `TOOL-aWindowedPass-5` | no |
| 5 | `TOOL-aWindowedPass-3` | no |
| 6 | `TOOL-aWindowedPass-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
