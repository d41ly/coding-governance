---
slug: aSightedSkeptic
node: a
opened: 2026-10-01
streams: tooling
roster: TOOL
status: OPEN
authorized-by: prompt
ids: TOOL-aSightedSkeptic-1
---

# aSightedSkeptic — the Tier-2 review harness, briefed, calibrated and measured

## The problem this build exists to solve

`tools/workflows/tier2-review.js` closes every build here and ships to every adopter, and its own
record says it does not converge. Of 194 closing diff reviews, none came back `CLEAN`. Long builds
plateau: one ran nine rounds, every one BLOCKED. In later rounds, half the confirmed findings are
defects the previous round's fix introduced.

Seven causes were found in its prompts and arguments, plus a measurement gap. Skeptics get no repo,
range or by-design list. Proposed fixes are never judged. Finders get no intent and no checklist. The
lens set misses the repo's signature defect. Severity is undefined. Intensity is fixed. And recall is
never measured. The owner's prompt and the list are in `prompts/`.

## Expected improvements

- Fold rounds stop finding defects in fixes nobody judged.
- A skeptic reads the right tree and the right range.
- Lenses judge the diff against stated intent and the project's own bug classes.
- BLOCKER means one thing across finders, skeptics and synthesis.
- Small diffs can be reviewed light.
- Per-lens yield and recall become measurable.

## Detriments if this is not built

- Closing reviews keep plateauing, and each round re-spends a full fan on defects in the last fix.
- A skeptic in the wrong checkout keeps confirming or refuting against code nobody asked about.
- Whether a lens earns its tokens stays unanswerable, so the lens set keeps being chosen by feel.

## Build-level rules

- Every harness change lands in `tools/workflows/tier2-review.template.js` and its render, and assumes nothing about an adopter beyond what the harness requires today.
- A project-specific input arrives as an `args` field; its absence is ANNOUNCED in the log and the report, never defaulted silently.
- Fan-out stays inside `tools/hooks/agent-cap.js`: the lens array stays a literal of at most five, and a skipped lens is skipped inside its thunk.
- No governance carrier is edited. Five lenses sit inside the review protocol's stated three to six.
- Each unit's arms go into `tools/workflows/tier2-review.test.sh` and are observed RED first; the suite runs once, at `VERIFYING`.
- No spec audit (owner, 2026-10-01): the closing diff review is the specs' first review.
- Classified at kickoff (M2): all nine units MISSING.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aSightedSkeptic-1` | MISSING | the skeptic is briefed with the repo, the range, the context and the by-design list |
| 2 | `TOOL-aSightedSkeptic-2` | MISSING | the skeptic judges each proposed fix as well as the claim |
| 3 | `TOOL-aSightedSkeptic-3` | MISSING | finders are handed intent: a `specs` argument, and the range's commit messages by default |
| 4 | `TOOL-aSightedSkeptic-4` | MISSING | a `checklist` argument whose classes are split across the lenses |
| 5 | `TOOL-aSightedSkeptic-5` | MISSING | five diff lenses, with verification and intent added, and project lens notes |
| 6 | `TOOL-aSightedSkeptic-6` | MISSING | one severity rubric; a skeptic may re-grade, or answer uncertain |
| 7 | `TOOL-aSightedSkeptic-7` | MISSING | an intensity argument whose light setting announces the lenses it skips |
| 8 | `TOOL-aSightedSkeptic-8` | MISSING | every finding keeps its lens, a findings ledger lands beside the report, and the confirmed set is returned |
| 9 | `TOOL-aSightedSkeptic-9` | MISSING | the replay benchmark: a ledger scored for recall against a past round's known findings |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-01 · streams tooling
ids TOOL-aSightedSkeptic-1

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
