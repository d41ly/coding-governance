---
slug: aWindowedPass
node: a
opened: 2026-10-04
streams: tooling
roster: TOOL
authorized-by: prompt
status: OPEN
ids: TOOL-aWindowedPass-1
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

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-04 · streams tooling
ids TOOL-aWindowedPass-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
